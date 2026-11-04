"""抽取网页正文为 Markdown。用法：extract.py <html> <css选择器或auto>"""
import sys, re, json
from bs4 import BeautifulSoup
from markdownify import markdownify as md
html = open(sys.argv[1], encoding="utf-8", errors="replace").read()
s = BeautifulSoup(html, "html.parser")
meta = {}
for k in ["og:title", "article:published_time", "article:modified_time", "og:url", "author", "og:image"]:
    t = s.find("meta", attrs={"property": k}) or s.find("meta", attrs={"name": k})
    if t and t.get("content"): meta[k] = t["content"]
for t in s.find_all("script", type="application/ld+json"):
    try:
        d = json.loads(t.string or "")
        for x in (d if isinstance(d, list) else d.get("@graph", [d])):
            for k in ["datePublished", "dateModified", "headline"]:
                if isinstance(x, dict) and x.get(k): meta.setdefault("ld:" + k, x[k])
    except Exception: pass
print("META", json.dumps(meta, ensure_ascii=False))
sel = sys.argv[2] if len(sys.argv) > 2 else "auto"
if sel == "auto":
    cands = s.select("article") or s.select("main") or [s.body]
    node = max(cands, key=lambda n: len(n.get_text()))
else:
    node = s.select_one(sel)
for t in node.select("script,style,noscript,nav,footer,form,button,svg"): t.decompose()
out = md(str(node), heading_style="ATX", bullets="-")
out = re.sub(r"\n{3,}", "\n\n", out)
print(out)
