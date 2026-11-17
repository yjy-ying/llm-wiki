"""引句卡檢查（撰寫頁面之前執行）。

用法：
    python scripts/check_cards.py        # 檢查所有 cards/S?.md
    python scripts/check_cards.py S6     # 只檢查指定資料

每張卡必須：
    C1 欄位齊全（原文、章節、主詞、比較對象、中文）
    C2 原文逐字存在於 raw_text/S?.txt
    C3 主詞是「S? 作者」或「S? 轉述（…）」
    C4 中文保留限定詞、沒有用到禁止詞（例：suggested 不可譯成「顯示」）
    C5 主詞是轉述時，中文要寫出「轉述」
    C6 有比較對象時，中文要寫出比較對象（以「比」字檢查）
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cards import ROOT, all_cards, check_zh  # noqa: E402
from extract_text import norm  # noqa: E402

FIELDS = ["原文", "章節", "主詞", "比較對象", "中文"]


def check(cards):
    errs = []
    cache = {}
    seen = set()
    for c in cards:
        where = f"cards/{c['sid']}.md:{c['line']} {c['id']}"
        if c["id"] in seen:
            errs.append(f"{where} 卡片編號重複")
        seen.add(c["id"])
        missing = [f for f in FIELDS if not c.get(f)]
        if missing:
            errs.append(f"{where} C1 缺少欄位：{'、'.join(missing)}")
            continue
        sid = c["sid"]
        if sid not in cache:
            src = ROOT / "raw_text" / f"{sid}.txt"
            cache[sid] = norm(src.read_text(encoding="utf-8")) if src.exists() else None
        if cache[sid] is None:
            errs.append(f"{where} C2 找不到 raw_text/{sid}.txt")
        else:
            pos = 0
            for piece in re.split(r"\.\.\.|…", c["原文"]):
                pn = norm(piece)
                if not pn:
                    continue
                k = cache[sid].find(pn, pos)
                if k < 0:
                    errs.append(f"{where} C2 原文中找不到：\"{piece.strip()[:50]}\"")
                    break
                pos = k + len(pn)
        if not re.match(rf"^{sid} (作者|轉述)", c["主詞"]):
            errs.append(f"{where} C3 主詞須為「{sid} 作者」或「{sid} 轉述（…）」")
        for e in check_zh(c["原文"], c["中文"]):
            errs.append(f"{where} C4 {e}")
        if "轉述" in c["主詞"] and "轉述" not in c["中文"]:
            errs.append(f"{where} C5 主詞是轉述，中文要寫出「轉述」")
        if c["比較對象"] != "無" and "比" not in c["中文"]:
            errs.append(f"{where} C6 有比較對象（{c['比較對象']}），中文要寫出比較")
    return errs


def main(argv):
    ids = {a.upper() for a in argv}
    cards = [c for c in all_cards() if not ids or c["sid"] in ids]
    errs = check(cards)
    print(f"檢查 {len(cards)} 張引句卡")
    for e in errs:
        print(f"    - {e}")
    print("結果：" + ("全部通過" if not errs else f"{len(errs)} 個問題"))
    return 0 if not errs else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
