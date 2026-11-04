"""从 Next.js RSC 数据中按顺序提取媒体：alt、浅色图、视频、表格标题。"""
import sys, re
t = open(sys.argv[1], encoding="utf-8").read().replace('\\"', '"').replace('\\\\', '\\')
seen = []
for m in re.finditer(r'"alt":"((?:[^"\\]|\\.)*)"(.{0,1500})', t, re.S):
    alt, rest = m.group(1), m.group(2)
    src = re.search(r'"(?:lightCandidates|candidates)":\[\{"desktopSource":"([^"]+)"', rest) or re.search(r'"desktopSource":"([^"]+)"', rest) or re.search(r'"src":"([^"]+)"', rest)
    key = (alt, src.group(1) if src else "")
    if key not in seen: seen.append(key)
for alt, src in seen: print(f"{src}\n    ALT: {alt}")
print("---- videos")
for v in dict.fromkeys(re.findall(r'"(https://[^"]+\.mp4[^"]*)"', t)): print(v[:160])
for c in dict.fromkeys(re.findall(r'"caption":"((?:[^"\\]|\\.){5,300})"', t)): print("CAP:", c)
