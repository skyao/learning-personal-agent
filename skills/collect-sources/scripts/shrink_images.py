"""把目录中超过上限的图片缩到 1000 像素宽并重新编码；动图不处理，只报告。
用法：shrink_images.py <images目录> [上限KB，默认600]   输出改名对照（旧名 新名），供改写 Markdown 链接。"""
import sys, os
from PIL import Image
d = sys.argv[1]; limit = int(sys.argv[2]) * 1024 if len(sys.argv) > 2 else 600 * 1024
for name in sorted(os.listdir(d)):
    p = os.path.join(d, name)
    if os.path.getsize(p) <= limit: continue
    im = Image.open(p)
    if getattr(im, "is_animated", False):
        print(f"SKIP-ANIMATED {name} {os.path.getsize(p)//1024}KB", file=sys.stderr); continue
    if im.width > 1000: im = im.resize((1000, round(im.height * 1000 / im.width)), Image.LANCZOS)
    base, ext = os.path.splitext(name)
    has_alpha = im.mode in ("RGBA", "LA", "P")
    # 先试 PNG 量化，过大再转 JPEG
    out = os.path.join(d, base + ".png")
    im.convert("RGBA" if has_alpha else "RGB").quantize(256).save(out, optimize=True) if ext.lower() == ".png" else None
    if ext.lower() != ".png" or os.path.getsize(out) > limit:
        out2 = os.path.join(d, base + ".jpg"); im.convert("RGB").save(out2, quality=85, optimize=True)
        if out != out2 and os.path.exists(out) and out != p: os.remove(out)
        out = out2
    if out != p and os.path.exists(p): os.remove(p)
    print(name, os.path.basename(out), f"{os.path.getsize(out)//1024}KB")
