#!/usr/bin/env python3
"""把分析页草稿中的短宏展开成 Hugo relref 链接，写入 docs/<product>/analysis/。

用法：
  python3 skills/analyze/scripts/expand_drafts.py <product> <草稿目录>

草稿目录中：
  refs.tsv          每行「键<TAB>资料路径<TAB>链接文字」，如
                    AU	/docs/workbuddy/sources/official/2026-10-28-help-automation	帮助：定时任务
  <slug>.md         主题页草稿，写到 docs/<product>/analysis/<slug>/_index.md
  _overview.md      产品总览草稿，写到 docs/<product>/analysis/_index.md

草稿中的宏：
  [[AU]]            -> [帮助：定时任务]({{< relref "/docs/..." >}})
  [[AU|定时任务页]]  -> 自定义链接文字
  [[t:runtime]]     -> [运行环境]({{< relref "/docs/<product>/analysis/runtime" >}})
  [[t:runtime|文字]] -> 自定义链接文字

未知的键会报错退出，不写任何文件。展开后仍有 [[ 残留时也报错。
"""
import os
import re
import sys

TOPICS = {
    'runtime': '运行环境', 'memory': '记忆与上下文', 'continuous-execution': '持续执行',
    'connectors': '连接器', 'channels': '交互渠道', 'devices': '设备', 'models': '模型',
    'security': '安全', 'privacy': '隐私', 'access-pricing': '开放与价格',
    'business': '商业与规模', 'reliability': '实际效果与可靠性',
}
MACRO = re.compile(r'\[\[([A-Za-z0-9:_-]+)(?:\|([^\]]*))?\]\]')


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    product, src = sys.argv[1], sys.argv[2]
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    dst = os.path.join(root, 'content', 'zh-cn', 'docs', product, 'analysis')

    refs = {}
    with open(os.path.join(src, 'refs.tsv'), encoding='utf-8') as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip('\n')
            if not line.strip() or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) != 3:
                sys.exit(f'refs.tsv 第 {n} 行应为三列：{line}')
            refs[parts[0]] = (parts[1], parts[2])

    errors, out = [], {}

    def sub(m, fname):
        key, text = m.group(1), m.group(2)
        if key.startswith('t:'):
            slug = key[2:]
            if slug not in TOPICS:
                errors.append(f'{fname}: 未知主题 {slug}')
                return m.group(0)
            return f'[{text or TOPICS[slug]}]({{{{< relref "/docs/{product}/analysis/{slug}" >}}}})'
        if key not in refs:
            errors.append(f'{fname}: 未知键 {key}')
            return m.group(0)
        path, name = refs[key]
        return f'[{text or name}]({{{{< relref "{path}" >}}}})'

    for fname in sorted(os.listdir(src)):
        if not fname.endswith('.md'):
            continue
        text = open(os.path.join(src, fname), encoding='utf-8').read()
        text = MACRO.sub(lambda m: sub(m, fname), text)
        if '[[' in text:
            errors.append(f'{fname}: 展开后仍有 [[ 残留')
        slug = fname[:-3]
        target = os.path.join(dst, '_index.md') if slug == '_overview' else os.path.join(dst, slug, '_index.md')
        out[target] = text

    if errors:
        sys.exit('\n'.join(errors))
    for target, text in out.items():
        os.makedirs(os.path.dirname(target), exist_ok=True)
        open(target, 'w', encoding='utf-8').write(text)
        print('wrote', os.path.relpath(target, root))


if __name__ == '__main__':
    main()
