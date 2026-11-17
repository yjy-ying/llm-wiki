"""關卡 0：把 raw/ 的原文轉成 raw_text/S?.txt，並驗證原文身分。

用法：
    python scripts/extract_text.py          # 處理全部
    python scripts/extract_text.py S2 S5    # 只處理指定編號

驗證項目：
    - 檔案存在
    - 抽出的文字夠長（避免下載到錯誤頁面、驗證頁）
    - 文字中包含 sources 預期的標題關鍵句（避免放錯論文）
任何一項失敗 → exit code 1，不可進行 ingest。
"""
import html
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "raw_text"

# 編號 → (檔名, 必須出現的標題關鍵句)
SOURCES = {
    "S1": ("01_cahill2013_circulation.pdf",
           "Prospective Study of Breakfast Eating and Incident Coronary Heart Disease"),
    "S2": ("02_rong2019_jacc.pdf",
           "Association of Skipping Breakfast With Cardiovascular and All-Cause Mortality"),
    "S3": ("03_dhurandhar2014_ajcn.pdf",
           "effectiveness of breakfast recommendations on weight loss"),
    "S4": ("04_betts2014_ajcn.xml",
           "causal role of breakfast in energy balance and health"),
    "S5": ("05_sievert2019_bmj.xml",
           "Effect of breakfast on weight and energy intake"),
    "S6": ("06_harvard_breakfast_skipper.html",
           "Confessions of a breakfast skipper"),
    "S7": ("07_ibanez2019_editorial.pdf",
           "Breakfast: a marker for cardiovascular risk prediction"),
}
MIN_CHARS = 3000


def norm(s: str) -> str:
    """比對用正規化：NFKC、小寫、去掉空白與各種連字號。"""
    s = unicodedata.normalize("NFKC", s).lower()
    s = re.sub(r"[‐-―−\-]", "", s)
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", "", s)


def from_pdf(p: Path) -> str:
    import pymupdf
    with pymupdf.open(p) as d:
        return "\n".join(page.get_text() for page in d)


def from_xml(p: Path) -> str:
    root = ET.parse(p).getroot()
    parts = []
    for tag in ("front", "body", "back"):
        for el in root.iter(tag):
            parts.append(" ".join(el.itertext()))
    return "\n\n".join(parts)


class _Text(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "nav", "footer", "header"}

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.chunks = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.depth += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.depth:
            self.depth -= 1
        if tag in ("p", "div", "h1", "h2", "h3", "li", "br"):
            self.chunks.append("\n")

    def handle_data(self, data):
        if not self.depth:
            self.chunks.append(data)


def from_html(p: Path) -> str:
    raw = p.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r"<article.*?</article>", raw, re.S | re.I)
    parser = _Text()
    parser.feed(m.group(0) if m else raw)
    text = html.unescape("".join(parser.chunks))
    # <article> 不一定包含標題，從 <title> 補回來
    t = re.search(r"<title>(.*?)</title>", raw, re.S | re.I)
    if t:
        text = html.unescape(t.group(1).strip()) + "\n\n" + text
    text = "\n".join(line.strip() for line in text.splitlines())
    return re.sub(r"\n\s*\n+", "\n\n", text).strip()


def extract(sid: str) -> list[str]:
    fname, title = SOURCES[sid]
    p = RAW / fname
    if not p.exists():
        return [f"找不到檔案 raw/{fname}"]
    ext = p.suffix.lower()
    text = from_pdf(p) if ext == ".pdf" else from_xml(p) if ext == ".xml" else from_html(p)
    errors = []
    if len(text) < MIN_CHARS:
        errors.append(f"文字只有 {len(text)} 字元，可能是錯誤頁面或驗證頁")
    if norm(title) not in norm(text):
        errors.append(f"找不到預期標題「{title}」，可能放錯論文")
    OUT.mkdir(exist_ok=True)
    (OUT / f"{sid}.txt").write_text(text, encoding="utf-8")
    return errors


def main(argv):
    ids = [a.upper() for a in argv] or list(SOURCES)
    failed = False
    for sid in ids:
        if sid not in SOURCES:
            print(f"[FAIL] {sid}: 未知編號")
            failed = True
            continue
        errs = extract(sid)
        if errs:
            failed = True
            for e in errs:
                print(f"[FAIL] {sid}: {e}")
        else:
            n = len((OUT / f"{sid}.txt").read_text(encoding="utf-8"))
            print(f"[ OK ] {sid}: {SOURCES[sid][0]} → raw_text/{sid}.txt（{n:,} 字元）")
    print("關卡 0：" + ("未通過，停止 ingest" if failed else "全部通過"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
