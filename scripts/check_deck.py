"""簡報檢查關卡（簡報 graph 的「出處檢查」與「渲染檢查」）。

用法：
    python scripts/check_deck.py              # 檢查 docs/index.html
    python scripts/check_deck.py --json out.json

每張投影片是一個 <section class="slide" data-src="wiki/…md wiki/…md">。
檢查項目：
    D1 每張投影片都有 data-src，且指向存在的 wiki 頁面
    D2 投影片中的每個數字，都出現在它引用的 wiki 頁面裡（防止簡報自己生出數字）
    D3 每張投影片文字不超過 MAX_CHARS 字（避免字太多、跑出畫面）
    D4 投影片張數在 8–15 張之間
    D5 沒有禁用語（不給健康建議）
    D6 最後一張有免責聲明
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECK = ROOT / "docs" / "index.html"
MAX_CHARS = 260
BANNED = ["你應該", "建議大家", "建議你", "一定要吃早餐", "不要吃早餐", "你最好", "應該吃早餐", "應該不吃早餐"]
NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")
SKIP_TAGS = {"script", "style"}


class Deck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = []
        self.cur = None
        self.depth = 0
        self.skip = 0
        self.no_count = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP_TAGS:
            self.skip += 1
        if tag == "section" and "slide" in (a.get("class") or "").split():
            self.cur = {"src": (a.get("data-src") or "").split(), "text": [], "count": []}
            self.depth = 1
            return
        if self.cur is not None and tag == "section":
            self.depth += 1
        if self.cur is not None and "src-note" in (a.get("class") or "").split():
            self.no_count = 1  # 出處列不算字數、不檢查數字

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self.skip:
            self.skip -= 1
        if self.cur is not None and tag == "footer":
            self.no_count = 0
        if self.cur is not None and tag == "section":
            self.depth -= 1
            if self.depth == 0:
                self.slides.append(self.cur)
                self.cur = None

    def handle_data(self, data):
        if self.cur is None or self.skip:
            return
        self.cur["text"].append(data)
        if not self.no_count:
            self.cur["count"].append(data)


def main(argv):
    html = DECK.read_text(encoding="utf-8")
    d = Deck()
    d.feed(html)
    errs = []
    n = len(d.slides)
    if not 8 <= n <= 15:
        errs.append(f"D4 投影片有 {n} 張，應在 8–15 張之間")
    for i, s in enumerate(d.slides, 1):
        body = "".join(s["count"])
        text = re.sub(r"\s+", "", body)
        if not s["src"]:
            errs.append(f"第 {i} 張 D1 沒有 data-src")
        pages = []
        for src in s["src"]:
            p = ROOT / src
            if not p.exists():
                errs.append(f"第 {i} 張 D1 引用的頁面不存在：{src}")
            else:
                pages.append(p.read_text(encoding="utf-8"))
        corpus = re.sub(r"\s+", "", "".join(pages))
        corpus_nums = {x.replace(",", "") for x in NUM_RE.findall(corpus)}
        if pages:
            for num in sorted(set(NUM_RE.findall(text))):
                if num.replace(",", "") not in corpus_nums:
                    errs.append(f"第 {i} 張 D2 數字「{num}」在引用的 wiki 頁面中找不到")
        if len(text) > MAX_CHARS:
            errs.append(f"第 {i} 張 D3 文字 {len(text)} 字，超過 {MAX_CHARS}")
        for w in BANNED:
            if w in text:
                errs.append(f"第 {i} 張 D5 出現禁用語「{w}」")
    if d.slides and "不構成醫療建議" not in "".join(d.slides[-1]["text"]):
        errs.append("D6 最後一張缺少免責聲明")
    print(f"檢查 {n} 張投影片")
    for e in errs:
        print(f"    - {e}")
    print("結果：" + ("全部通過" if not errs else f"{len(errs)} 個問題"))
    if "--json" in argv:
        Path(argv[argv.index("--json") + 1]).write_text(json.dumps(errs, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if not errs else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
