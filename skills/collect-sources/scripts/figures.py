"""列出页面正文中的 figure / img / video，按文档顺序，附前一段文字以便定位。"""
import sys
from bs4 import BeautifulSoup
s = BeautifulSoup(open(sys.argv[1], encoding="utf-8").read(), "html.parser")
root = s.find("article") or s.find("main") or s.body
for el in root.find_all(["figure", "img", "video", "table"]):
    if el.name == "img" and el.find_parent("figure"): continue
    if el.name == "video" and el.find_parent("figure"): continue
    imgs = el.find_all("img") if el.name != "img" else [el]
    srcs = [i.get("src") or "" for i in imgs]
    alts = [i.get("alt") or "" for i in imgs]
    sources = [x.get("srcset") or x.get("src") or "" for x in el.find_all("source")]
    cap = el.find("figcaption"); cap = cap.get_text(" ", strip=True) if cap else ""
    prev = el.find_previous(["p", "h2", "h3"]); prev = prev.get_text(" ", strip=True)[:60] if prev else ""
    print(f"--- {el.name} | after: {prev}")
    for a, b in zip(srcs, alts): print("   IMG", a[:110], "| ALT", b[:160])
    for x in sources[:2]: print("   SRC", x[:140])
    if cap: print("   CAP", cap[:200])
