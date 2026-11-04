"""about.fb.com 页面：要点框 + 正文（含视频、图片位置），截到 Categories 之前。"""
import sys, re
from bs4 import BeautifulSoup
from markdownify import markdownify as md
s = BeautifulSoup(open(sys.argv[1], encoding="utf-8").read(), "html.parser")
def meta(k):
    t = s.find("meta", attrs={"property": k}); return t["content"] if t else ""
print("TITLE:", s.find("h1").get_text(" ", strip=True))
print("PUB:", meta("article:published_time"), "MOD:", meta("article:modified_time"))
for v in s.find_all("video"):
    src = [x.get("src") for x in v.find_all("source")] or [v.get("src")]
    v.replace_with(s.new_string(f"\n\n[VIDEO {src[0]}]\n\n"))
import json
for g in s.select("div.jetpack-slideshow"):
    items = json.loads(g.get("data-gallery") or "[]")
    lines = [f"[IMG {it['src'].split('?')[0]} | {it.get('alt','')}]" for it in items]
    g.replace_with(s.new_string("\n\n" + "\n\n".join(lines) + "\n\n"))
for h in s.find_all(["h2", "h3"]):
    if h.get_text(strip=True) in ("Takeaways", "ポイント", "要点", "Key takeaways"):
        blk = h.parent
        while len(blk.find_all("li")) < 2 and blk.parent: blk = blk.parent
        print("=== TAKEAWAYS"); print(md(str(blk), heading_style="ATX", bullets="-").strip())
        break
art = s.find("article")
for t in art.select("script,style,noscript,form,button,svg"): t.decompose()
out = md(str(art), heading_style="ATX", bullets="-")
out = re.split(r"\n\s*(Categories|カテゴリー|タグ)\s*\n", out)[0]
print("=== BODY"); print(re.sub(r"\n{3,}", "\n\n", out).strip())
