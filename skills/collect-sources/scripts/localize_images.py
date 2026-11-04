"""下载 Markdown 中的图片到 <页面目录>/images/，并把链接改为相对路径。
用法：localize_images.py <输入md> <页面目录> [基准URL]   输出改写后的 Markdown 到标准输出。"""
import sys, re, os, hashlib, urllib.request, urllib.parse
src, page_dir = sys.argv[1], sys.argv[2]
base = sys.argv[3] if len(sys.argv) > 3 else ""
text = open(src, encoding="utf-8").read()
os.makedirs(os.path.join(page_dir, "images"), exist_ok=True)
done = {}
def fetch(url):
    full = urllib.parse.urljoin(base, url)
    if full in done: return done[full]
    req = urllib.request.Request(full, headers={"User-Agent": "Mozilla/5.0", "Accept": "image/avif,image/webp,image/png,image/jpeg,*/*", "Referer": base or full})
    try:
        data = urllib.request.urlopen(req, timeout=40).read()
    except Exception as e:
        print(f"WARN 下载失败 {full}: {e}", file=sys.stderr); done[full] = url; return url
    ext = {b"\x89PNG": ".png", b"GIF8": ".gif", b"RIFF": ".webp", b"\xff\xd8\xff": ".jpg"}
    suffix = next((v for k, v in ext.items() if data.startswith(k)), ".img")
    name = f"img-{len(done)+1:02d}-{hashlib.md5(full.encode()).hexdigest()[:6]}{suffix}"
    open(os.path.join(page_dir, "images", name), "wb").write(data)
    print(f"{name} {len(data)//1024}KB <- {full[:100]}", file=sys.stderr)
    done[full] = "images/" + name; return done[full]
def repl(m):
    return f"![{m.group(1)}]({fetch(m.group(2))})"
text = re.sub(r"!\[([^\]]*)\]\(<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\)", repl, text)
sys.stdout.write(text)
