"""Wiki 程式檢查 ①–⑥（規則見 AGENTS.md 第 8 節）。

用法：
    python scripts/lint_wiki.py            # 檢查全部頁面
    python scripts/lint_wiki.py --json out.json   # 另存 JSON 報告

全部通過 → exit 0；有任何失敗 → exit 1。
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_text import norm  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW_TEXT = ROOT / "raw_text"

CONTENT_DIRS = ("studies", "concepts", "topics", "debates")
SID = r"S[1-7]"
DISCLAIMER = "僅供教學，不構成醫療建議"
BANNED = ["你應該", "建議大家", "建議你", "一定要吃早餐","不要吃早餐", "你最好", "應該吃早餐", "應該不吃早餐"]
# ② 不要求出處的小節（標題含這些字）
CITE_EXEMPT_SECTIONS = ("例子", "出處", "相關", "關係", "延伸")

LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)")
QUOTE_RE = re.compile(r'^\s*>\s*["“](.+?)["”]\s*[—–-]+\s*(' + SID + r')\b')


def content_pages():
    pages = [p for d in CONTENT_DIRS for p in sorted((WIKI / d).glob("*.md"))]
    if (WIKI / "glossary.md").exists():
        pages.append(WIKI / "glossary.md")
    return pages


def all_pages():
    return sorted(WIKI.rglob("*.md"))


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def links_of(p: Path):
    """回傳 (行號, 目標 Path) 清單（只算本機相對連結）。"""
    out = []
    for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        for _, target in LINK_RE.findall(line):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = target.split("#")[0]
            out.append((i, (p.parent / path).resolve()))
    return out


def check_links():
    errs = []
    for p in all_pages():
        for i, t in links_of(p):
            if not t.exists():
                errs.append(f"{rel(p)}:{i} 連結目標不存在 → {t.name}")
    return errs


def blocks(text: str):
    """把頁面切成 (小節標題, 行號, 區塊類型, 內容)。區塊 = 段落 / 條列項目 / 引句 / 表格。"""
    section = ""
    cur, cur_kind, cur_line = [], None, 0
    out = []

    def flush():
        nonlocal cur, cur_kind
        if cur:
            out.append((section, cur_line, cur_kind, "\n".join(cur)))
        cur, cur_kind = [], None

    in_code = False
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            flush()
            continue
        if in_code:
            continue
        if not s:
            flush()
            continue
        if s.startswith("#"):
            flush()
            section = s.lstrip("#").strip()
            continue
        if s.startswith(">"):
            kind = "quote"
        elif s.startswith("|"):
            kind = "table"
        elif re.match(r"^([-*+]|\d+\.)\s", s):
            kind = "item"
            if line[:1] in "-*+0123456789":  # 新的頂層條列項目
                flush()
        else:
            kind = cur_kind if cur_kind in ("item", "para") else "para"
        if cur_kind and kind != cur_kind and not (cur_kind == "item" and kind == "para"):
            flush()
        if not cur:
            cur_line = i
            cur_kind = kind
        cur.append(s)
    flush()
    return out


def check_citations():
    errs = []
    for p in content_pages():
        if p.name == "glossary.md":
            continue
        bl = blocks(p.read_text(encoding="utf-8"))
        for idx, (section, line, kind, body) in enumerate(bl):
            if kind not in ("para", "item") or not section:
                continue
            if any(k in section for k in CITE_EXEMPT_SECTIONS):
                continue
            if body.startswith("*") and DISCLAIMER in body:
                continue
            if "一句話重點" in body:
                continue
            if re.search(r"\b" + SID + r"\b", body):
                continue
            if "本 wiki 的" in body:  # 明確標示為 wiki 自己的說明／解讀（AGENTS.md 5 節）
                continue
            nxt = bl[idx + 1] if idx + 1 < len(bl) else None
            if nxt and nxt[2] == "quote" and re.search(SID, nxt[3]):
                continue
            errs.append(f"{rel(p)}:{line} 〔{section}〕缺少出處 S?：{body[:40]}…")
    return errs


def check_quotes():
    errs = []
    cache = {}
    for p in content_pages():
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            m = QUOTE_RE.match(line)
            if not m:
                if re.match(r'^\s*>\s*["“]', line):
                    errs.append(f"{rel(p)}:{i} 引句格式錯誤（應為 > \"...\" — S?, 章節）")
                continue
            quote, sid = m.group(1), m.group(2)
            src = RAW_TEXT / f"{sid}.txt"
            if not src.exists():
                errs.append(f"{rel(p)}:{i} 找不到 raw_text/{sid}.txt（先跑 extract_text.py）")
                continue
            if sid not in cache:
                cache[sid] = norm(src.read_text(encoding="utf-8"))
            text = cache[sid]
            pos = 0
            for piece in re.split(r"\.\.\.|…", quote):
                piece_n = norm(piece)
                if not piece_n:
                    continue
                found = text.find(piece_n, pos)
                if found < 0:
                    errs.append(f"{rel(p)}:{i} 引句在 {sid} 原文中找不到：\"{piece.strip()[:60]}\"")
                    break
                pos = found + len(piece_n)
    return errs


def check_orphans():
    errs = []
    index = WIKI / "index.md"
    indexed = {t for _, t in links_of(index)} if index.exists() else set()
    linked_from_others = {}
    for p in all_pages():
        if p.name in ("index.md", "log.md"):
            continue
        for _, t in links_of(p):
            if t != p.resolve():
                linked_from_others.setdefault(t, set()).add(p)
    for p in content_pages():
        r = p.resolve()
        if r not in indexed:
            errs.append(f"{rel(p)} 沒有列在 index.md")
        if p.name != "glossary.md" and r not in linked_from_others:
            errs.append(f"{rel(p)} 沒有被任何其他頁面連結（孤兒頁面）")
    return errs


def check_format():
    errs = []
    for p in content_pages():
        t = p.read_text(encoding="utf-8")
        if p.name != "glossary.md":
            if "**一句話重點**" not in t:
                errs.append(f"{rel(p)} 缺少「一句話重點」")
            if not re.search(r"^##\s*出處", t, re.M):
                errs.append(f"{rel(p)} 缺少「## 出處」")
        if DISCLAIMER not in t:
            errs.append(f"{rel(p)} 缺少免責聲明")
        if p.parent.name in ("concepts", "topics") and not re.search(r"^##+.*例子", t, re.M):
            errs.append(f"{rel(p)} 缺少含「例子」的小標")
        if "[[" in t:
            errs.append(f"{rel(p)} 使用了 [[...]] 連結（GitHub 不支援）")
    return errs


def check_banned():
    errs = []
    for p in all_pages():
        if p.name == "log.md":
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip().startswith(">"):
                continue
            for w in BANNED:
                if w in line:
                    errs.append(f"{rel(p)}:{i} 出現禁用語「{w}」")
    return errs


def check_card_usage():
    """⑩ 頁面引句都來自引句卡；⑪ 引句上方的中文句保留限定詞，轉述要寫出「轉述」。"""
    from cards import all_cards, check_zh
    cards = all_cards()
    by_sid = {}
    for c in cards:
        if c.get("原文"):
            by_sid.setdefault(c["sid"], []).append(c)
    errs = []
    for p in content_pages():
        lines = p.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            m = QUOTE_RE.match(line)
            if not m:
                continue
            quote, sid = m.group(1), m.group(2)
            qn = [norm(x) for x in re.split(r"\.\.\.|…", quote) if norm(x)]
            card = next((c for c in by_sid.get(sid, [])
                         if all(x in norm(c["原文"]) for x in qn)), None)
            if card is None:
                errs.append(f"{rel(p)}:{i + 1} ⑩ 引句沒有對應的引句卡（cards/{sid}.md）")
                continue
            j = i - 1
            while j >= 0 and (lines[j].strip().startswith(">") or not lines[j].strip()):
                j -= 1
            zh = lines[j] if j >= 0 else ""
            # 用整張卡的原文判斷限定詞：頁面只引半句時，另一半的限定詞仍要保留
            for e in check_zh(card["原文"], zh):
                errs.append(f"{rel(p)}:{j + 1} ⑪ {card['id']}：{e}")
            if "轉述" in card["主詞"] and "轉述" not in zh:
                errs.append(f"{rel(p)}:{j + 1} ⑪ {card['id']}：卡片主詞是轉述，中文要寫出「轉述」")
    return errs


CHECKS = [
    ("①", "連結沒斷", check_links),
    ("②", "每個說法有出處", check_citations),
    ("③", "引句存在於原文", check_quotes),
    ("④", "沒有孤兒頁面", check_orphans),
    ("⑤", "格式完整", check_format),
    ("⑥", "沒有禁用語", check_banned),
    ("⑩⑪", "引句來自卡片且保留限定詞", check_card_usage),
]


def main(argv):
    report = {}
    total = 0
    print(f"檢查 {len(content_pages())} 個內容頁\n")
    for no, name, fn in CHECKS:
        errs = fn()
        report[f"{no} {name}"] = errs
        total += len(errs)
        print(f"{'[PASS]' if not errs else '[FAIL]'} {no} {name}" + (f"（{len(errs)}）" if errs else ""))
        for e in errs:
            print(f"    - {e}")
    print(f"\n結果：{'全部通過' if total == 0 else f'{total} 個問題'}")
    if "--json" in argv:
        out = Path(argv[argv.index("--json") + 1])
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
