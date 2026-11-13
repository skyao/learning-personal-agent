#!/usr/bin/env python3
"""列出某个产品（或某个主题）可用的资料，输出 TSV，供分析时筛选。

用法：
  inventory.py product <product>            该产品的全部资料，加上 industry 中 products 含该产品的资料
  inventory.py tag <标签> [<标签> ...]       所有产品中带任一标签的资料（主题维度用）
  inventory.py ... --since YYYY-MM-DD       只列 collectedAt 不早于该日期的资料
  inventory.py product <product> --new      只列「未分析」的资料（增量更新用）：既没有被
                                            docs/<product>/analysis/ 下任何页面用 relref 引用，
                                            也不在 references/uncited/<product>.tsv（已读、有意不引用）中
  inventory.py product <product> --new --record "<说明>"
                                            把当前 --new 列出的全部资料追加到 uncited/<product>.tsv，
                                            记为已读、不引用；只在更新完页面、剩下的确实不需引用时运行

输出列：relref 路径、产品目录、类型、date、collectedAt、fidelity、translation、tags、products、title
只读 frontmatter，不读正文；只用标准库。
"""
import datetime, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'content', 'zh-cn')
DOCS = os.path.normpath(os.path.join(ROOT, 'docs'))
UNCITED = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references', 'uncited'))
RELREF = re.compile(r'relref\s+"(/docs/[^"#]+?)/?(?:#[^"]*)?"')


def cited(product):
    """该产品分析页里用 relref 引用过的全部资料路径。"""
    refs = set()
    for d, _, files in os.walk(os.path.join(DOCS, product, 'analysis')):
        for f in files:
            if f.endswith('.md'):
                refs.update(RELREF.findall(open(os.path.join(d, f), encoding='utf-8').read()))
    return refs


def uncited_record(product):
    p = os.path.join(UNCITED, product + '.tsv')
    if not os.path.isfile(p):
        return p, set()
    return p, {l.split('\t')[0] for l in open(p, encoding='utf-8') if l.startswith('/docs/')}


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
    record = None
    if '--record' in argv:
        i = argv.index('--record'); record = argv[i + 1]; del argv[i:i + 2]
    new = '--new' in argv
    if new:
        argv.remove('--new')
    if len(argv) < 2 or argv[0] not in ('product', 'tag') or (new and argv[0] != 'product') or (record and not new):
        sys.exit(__doc__)
    mode, args = argv[0], argv[1:]
    if new:
        record_path, seen = uncited_record(args[0])
        seen |= cited(args[0])
    rows = []
    for product, kind, ref, fm in sources():
        tags = fm.get('tags', []) if isinstance(fm.get('tags'), list) else []
        prods = fm.get('products', []) if isinstance(fm.get('products'), list) else []
        if mode == 'product':
            ok = product == args[0] or (product == 'industry' and args[0] in prods)
        else:
            ok = any(t in tags for t in args)
        if not ok or (since and fm.get('collectedAt', '') < since) or (new and ref in seen):
            continue
        rows.append([ref, product, kind, fm.get('date', ''), fm.get('collectedAt', ''), fm.get('fidelity', ''),
                     fm.get('translation', ''), ','.join(tags), ','.join(prods), fm.get('title', '')])
    if record:
        os.makedirs(UNCITED, exist_ok=True)
        fresh = not os.path.isfile(record_path)
        with open(record_path, 'a', encoding='utf-8') as f:
            if fresh:
                f.write('# 已读、有意不引用的资料（inventory.py --new 据此排除）。列：路径、记录日期、说明\n')
            for r in rows:
                f.write('%s\t%s\t%s\n' % (r[0], datetime.date.today().isoformat(), record))
        sys.stderr.write('已记入 %s：%d 篇\n' % (os.path.relpath(record_path), len(rows)))
        return
    for r in rows:
        print('\t'.join(r))
    sys.stderr.write('%d 篇\n' % len(rows))


if __name__ == '__main__':
    main(sys.argv[1:])
