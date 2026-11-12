#!/usr/bin/env python3
"""列出某个产品（或某个主题）可用的资料，输出 TSV，供分析时筛选。

用法：
  inventory.py product <product>            该产品的全部资料，加上 industry 中 products 含该产品的资料
  inventory.py tag <标签> [<标签> ...]       所有产品中带任一标签的资料（主题维度用）
  inventory.py ... --since YYYY-MM-DD       只列 collectedAt 不早于该日期的资料（增量更新用）

输出列：relref 路径、产品目录、类型、date、collectedAt、fidelity、translation、tags、products、title
只读 frontmatter，不读正文；只用标准库。
"""
import os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'content', 'zh-cn')
DOCS = os.path.normpath(os.path.join(ROOT, 'docs'))


def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    fm = {}
    if not m:
        return fm
    for line in m.group(1).split('\n'):
        k, _, v = line.partition(':')
        if not _ or line.startswith(' '):
            continue
        v = v.strip()
        if v.startswith('[') and v.endswith(']'):
            v = [x.strip().strip('"') for x in v[1:-1].split(',') if x.strip()]
        else:
            v = v.strip('"')
        fm[k.strip()] = v
    return fm


def sources():
    for product in sorted(os.listdir(DOCS)):
        base = os.path.join(DOCS, product, 'sources')
        if not os.path.isdir(base):
            continue
        for kind in ('official', 'media', 'community', 'exploration'):
            kd = os.path.join(base, kind)
            if not os.path.isdir(kd):
                continue
            for d in sorted(os.listdir(kd)):
                p = os.path.join(kd, d, 'index.md')
                if os.path.isfile(p):
                    fm = frontmatter(p)
                    yield product, kind, '/docs/%s/sources/%s/%s' % (product, kind, d), fm


def main(argv):
    since = None
    if '--since' in argv:
        i = argv.index('--since'); since = argv[i + 1]; del argv[i:i + 2]
    if len(argv) < 2 or argv[0] not in ('product', 'tag'):
        sys.exit(__doc__)
    mode, args = argv[0], argv[1:]
    rows = []
    for product, kind, ref, fm in sources():
        tags = fm.get('tags', []) if isinstance(fm.get('tags'), list) else []
        prods = fm.get('products', []) if isinstance(fm.get('products'), list) else []
        if mode == 'product':
            ok = product == args[0] or (product == 'industry' and args[0] in prods)
        else:
            ok = any(t in tags for t in args)
        if not ok or (since and fm.get('collectedAt', '') < since):
            continue
        rows.append([ref, product, kind, fm.get('date', ''), fm.get('collectedAt', ''), fm.get('fidelity', ''),
                     fm.get('translation', ''), ','.join(tags), ','.join(prods), fm.get('title', '')])
    for r in rows:
        print('\t'.join(r))
    sys.stderr.write('%d 篇\n' % len(rows))


if __name__ == '__main__':
    main(sys.argv[1:])
