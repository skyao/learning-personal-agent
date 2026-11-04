# 目录页模板

新建产品目录或类型子目录时使用。`<产品名>` 替换为产品显示名，例如 Muse；`<product>` 替换为目录名，例如 muse。

## `<product>/_index.md`

```markdown
---
title: "<产品名>"
linkTitle: "<产品名>"
weight: 100
description: >
  <产品名> 的资料收集与分析
---

- [资料收集](sources/)
- [分析总结](analysis/)
```

产品概览的正文属于分析，收集时只建上面这个最小页面，不写产品介绍。

## `<product>/analysis/_index.md`

新建产品目录时一并建立这个占位页，正文留空。分析页面由用户另行安排，收集时不修改。

```markdown
---
title: "<产品名> 资料分析和总结"
linkTitle: "分析总结"
weight: 20
description: >
  基于资料收集的分析与阶段性总结
---
```

## `<product>/sources/_index.md`

```markdown
---
title: "<产品名> 资料收集"
linkTitle: "资料收集"
weight: 10
no_list: true
description: >
  <产品名> 的原始资料：官方、媒体、社区与实测，按原文全文保存，外文资料为中文全文翻译
---

{{< source-list >}}

## 行业综合中涉及 <产品名> 的资料

{{< source-list section="/docs/industry/sources" product="<product>" >}}
```

`industry/sources/_index.md` 只保留第一个 `{{< source-list >}}`。

## 类型子目录的 `_index.md`

四个子目录的 `title`、`linkTitle`、`weight` 固定如下：

| 目录 | title | linkTitle | weight |
| --- | --- | --- | --- |
| `official/` | `<产品名> 官方资料` | 官方 | 10 |
| `media/` | `<产品名> 媒体报道` | 媒体 | 20 |
| `community/` | `<产品名> 社区文章` | 社区 | 30 |
| `exploration/` | `<产品名> 实测记录` | 实测 | 40 |

```markdown
---
title: "<产品名> 官方资料"
linkTitle: "官方"
weight: 10
no_list: true
---

{{< source-list >}}
```

行业综合的子目录 title 用「行业综合」代替产品名，不加空格，例如「行业综合官方资料」。

`no_list: true` 关闭 Docsy 在目录页末尾自动生成的子页面列表，避免与资料表格重复。
