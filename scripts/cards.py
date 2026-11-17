"""引句卡（evidence cards）的共用定義：卡片解析與限定詞對照表。

卡片檔：cards/S?.md，每張卡格式如下（AGENTS.md 第 5.1 節）：

    ## C6-01
    - 原文："英文逐字引句"
    - 章節：Breakfast and weight
    - 主詞：S6 轉述（2007 研究）     ← 「S6 作者」或「S6 轉述（…）」
    - 比較對象：than those who eat breakfast（沒有就寫「無」）
    - 中文：中文譯句

限定詞不用手寫，由 HEDGES 自動從原文偵測，並要求中文句保留。
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"

# (英文限定詞 regex, 中文必須出現其一, 中文不可出現)
HEDGES = [
    (r"\bmay\b", ["可能", "或許", "也許"], []),
    (r"\bmight\b", ["可能", "或許", "也許"], []),
    (r"\bcould\b", ["可能", "或許"], []),
    (r"\bsuggest(s|ed)?\b", ["暗示", "提出", "認為"], ["顯示", "證明", "證實"]),
    (r"\btends? to\b", ["傾向", "往往"], []),
    (r"\bprobably\b", ["可能", "大概", "或許"], []),
    (r"\bunlikely\b", ["不太可能"], ["不會是"]),
    (r"\bapparently\b", ["似乎", "看來", "推測"], []),
    (r"\bmy guess\b", ["推測", "猜"], []),
    (r"\bassociat(ed|ion)\b", ["相關", "關聯", "有關"], ["造成", "導致"]),
    (r"\bsignificantly\b", ["顯著"], []),
    (r"\bpossibility\b", ["可能"], []),
    (r"\bfar fewer\b", ["遠少"], []),
    (r"\baverage\b", ["平均"], []),
    (r"\boften\b", ["往往", "常"], []),
]

FIELD_RE = re.compile(r"^-\s*(原文|章節|主詞|比較對象|中文)：(.*)$")


def hedges_in(english: str):
    """回傳原文中出現的限定詞清單：[(英文片語, 允許中文, 禁止中文)]。"""
    out = []
    for pat, allow, forbid in HEDGES:
        m = re.search(pat, english, re.I)
        if m:
            out.append((m.group(0), allow, forbid))
    return out


def check_zh(english: str, zh: str):
    """檢查中文句是否保留限定詞、沒有用到禁止詞。回傳錯誤訊息清單。"""
    errs = []
    for word, allow, forbid in hedges_in(english):
        if not any(a in zh for a in allow):
            errs.append(f"原文有「{word}」，中文需含其一：{'／'.join(allow)}")
        for f in forbid:
            if f in zh:
                errs.append(f"原文是「{word}」，中文不可用「{f}」")
    return errs


def parse_cards(path: Path):
    """解析一個卡片檔，回傳 [{id, line, 原文, 章節, 主詞, 比較對象, 中文}]。"""
    cards, cur = [], None
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if s.startswith("## "):
            cur = {"id": s[3:].strip(), "line": i, "file": path}
            cards.append(cur)
            continue
        m = FIELD_RE.match(s)
        if m and cur is not None:
            key, val = m.group(1), m.group(2).strip()
            if key == "原文":
                q = re.match(r'^["“](.*)["”]$', val)
                val = q.group(1) if q else val
            cur[key] = val
    return cards


def all_cards():
    cards = []
    for p in sorted(CARDS.glob("S*.md")):
        sid = p.stem
        for c in parse_cards(p):
            c["sid"] = sid
            cards.append(c)
    return cards
