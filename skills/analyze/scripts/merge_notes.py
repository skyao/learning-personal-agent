#!/usr/bin/env python3
"""核对提取笔记的覆盖，并按主题合并（2026-11-28 Muse 全面重写时使用）。

用法: merge_notes.py <临时目录> check|merge

临时目录中应有：
  groups/gNN.tsv     分组清单（inventory.py 的行）
  notes/gNN.md       各组笔记（extract-brief.md 的格式）
  drafts/refs.tsv    键、资料路径、链接文字三列
check  逐组列出清单中没有在笔记里出现的资料路径。
merge  写 bytopic/<小节>.md，并把每条要点里的资料路径改写成 KEY=/docs/...，
       写主题页的 fork 可直接照抄 [[KEY]] 短宏，也能按路径回资料页核对。"""
import sys, os, re, glob
S, mode = sys.argv[1], sys.argv[2]
refs = {}
for l in open(f'{S}/drafts/refs.tsv'):
    k, p, _ = l.rstrip('\n').split('\t'); refs[p] = k
PATH = re.compile(r'/docs/[a-z0-9-]+/sources/[a-z]+/[A-Za-z0-9._-]+')
if mode == 'check':
    for g in sorted(glob.glob(f'{S}/groups/g*.tsv')):
        n = os.path.basename(g)[:-4]; nf = f'{S}/notes/{n}.md'
        want = [l.split('\t')[0] for l in open(g) if l.startswith('/docs')]
        if not os.path.exists(nf): print(n, 'NO NOTES', len(want)); continue
        have = set(m.rstrip('.') for m in PATH.findall(open(nf).read()))
        miss = [w for w in want if w not in have]
        print(n, f'{len(want)-len(miss)}/{len(want)}', ' '.join(miss))
    sys.exit()
os.makedirs(f'{S}/bytopic', exist_ok=True)
sec = {}
unknown = set()
for nf in sorted(glob.glob(f'{S}/notes/g*.md')):
    cur = None
    for line in open(nf):
        m = re.match(r'^##\s+([a-z-]+)\s*$', line)
        if m: cur = m.group(1); continue
        if cur is None or not line.strip() or line.strip() == '无': continue
        def rep(mm):
            p = mm.group(0).rstrip('.')
            if p in refs: return f'{refs[p]}={p}'
            unknown.add(p); return p
        sec.setdefault(cur, []).append(PATH.sub(rep, line.rstrip('\n')))
for k, v in sec.items():
    open(f'{S}/bytopic/{k}.md', 'w').write('\n'.join(v) + '\n')
    print(k, len(v), os.path.getsize(f'{S}/bytopic/{k}.md') // 1024, 'KB')
print('unknown paths', len(unknown), list(unknown)[:10])
