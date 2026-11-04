"""找出同时包含开头短语和结尾短语的最小元素，输出其 CSS 选择器与 Markdown。
用法：container.py <html> <开头短语> <结尾短语>"""
import sys, re
from bs4 import BeautifulSoup
from markdownify import markdownify as md
s = BeautifulSoup(open(sys.argv[1], encoding="utf-8", errors="replace").read(), "html.parser")
a, b = sys.argv[2], sys.argv[3]
best = None
for el in s.find_all(True):
    t = el.get_text()
    if a in t and b in t and (best is None or len(t) < len(best.get_text())):
        best = el
if best is None: sys.exit("no container")
sel = best.name + "".join("." + c for c in best.get("class", [])) + (("#" + best["id"]) if best.get("id") else "")
print("SELECTOR:", sel)
for t in best.select("script,style,noscript,form,button,svg"): t.decompose()
print(re.sub(r"\n{3,}", "\n\n", md(str(best), heading_style="ATX", bullets="-")))
