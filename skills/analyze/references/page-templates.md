# 分析页模板

## 产品总览 `docs/<product>/analysis/_index.md`

已有的占位页改写为产品总览，frontmatter 保留 `title`、`linkTitle`、`weight: 20`，补 `description` 与 `analyzedAt`。

```markdown
---
title: "<产品名> 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-12          # 本页最后一次依据资料更新的日期
sourcesUntil: 2026-11-10        # 本次分析覆盖到的最晚 collectedAt
description: >
  <一句话：这个产品是什么、分析覆盖到何时>
---

## 概要

（5–8 条要点，每条是一个结论，句末链接到展开它的主题页。）

## 定位

（产品是什么、面向谁、由谁做、与厂商其他产品的关系、和其他跟踪产品相比的主要差异。）

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-09-08 | 发布 | [官方发布]({{< relref "/docs/<product>/sources/official/..." >}}) |

## 整体架构

（把各主题串起来的一段描述：在哪里运行、接什么数据、怎么触发、怎么审批、怎么收费。可配一张示意图。）

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境](runtime/) | 一句话结论 |

资料较少、没有单独成页的主题，在这里各写一两句，并说明资料不足。

## 资料缺口

（这个产品整体上还缺哪些资料，供下一轮收集参考。）
```

## 产品的主题页 `docs/<product>/analysis/<slug>/_index.md`

```markdown
---
title: "<产品名>：<主题>"
linkTitle: "<主题>"
weight: <topics.md 中的 weight>
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-10
description: >
  <一句话结论>
---

## 概要

（3–5 条结论。）

## <按 topics.md 的问题组织的小节，小节名写成具体内容，不写「问题一」>

（事实 + 出处；分析与推断单独成段，写明是推断及依据。）

## 资料缺口

## 主要资料

（本页引用的资料按类型列出：官方 / 媒体 / 社区 / 实测，每条一行链接加一句用途。）
```

主题内容多、需要拆分时，在主题目录下再建子页面（例如 `security/sentinel.md`），`_index.md` 保留概要和导航。

## 主题维度的目录页 `analysis/_index.md`

`content/zh-cn/analysis/` 与 `docs/` 平级，用户 2026-11-12 已建好（标题「Personal Agent 分析」，`cascade` 设 `type: "docs"`，顶部菜单 weight 30），不要覆盖。正文可在主题页陆续完成后补一张主题索引表。

## 主题页 `analysis/<slug>/_index.md`

```markdown
---
title: "<主题>"
linkTitle: "<主题>"
weight: <topics.md 中的 weight>
analyzedAt: 2026-11-20
products: [muse, dots, ...]     # 本页覆盖的产品
description: >
  <一句话结论>
---

## 概要

（5–8 条跨产品的结论。）

## 各家做法对照

| 产品 | 做法 | 关键限制 | 详见 |
| --- | --- | --- | --- |
| Muse | … | … | [Muse：运行环境]({{< relref "/docs/muse/analysis/runtime" >}}) |

## <分歧点、共性、演变趋势等小节>

## 资料缺口

## 主要资料

（主要列 industry 资料和本页直接引用的原始资料；各产品的资料通过产品主题页查看，不在这里重复列出。）
```
