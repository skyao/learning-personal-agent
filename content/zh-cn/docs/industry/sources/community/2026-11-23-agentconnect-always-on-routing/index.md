---
title: "常驻智能体如何拆分路由、执行与权限"
linkTitle: "AgentConnect：路由与权限"
date: 2026-11-23
originalTitle: "How always-on agents split routing, execution, and permissions"
sourceUrl: "https://www.agentconnect.md/blog/always-on-agents-router-worker/"
altUrls: ["https://www.agentconnect.md/zh/blog/always-on-agents-router-worker/"]
author: "The AgentConnect team"
publisher: "AgentConnect"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
tags: [持续执行, 交互渠道, 安全]
products: [claude-duet, grok-bot, muse, dots]
---

{{< source-info >}}

**收录说明**：直接下载，图片收入 images/；相对链接改为绝对地址。经 Hacker News 检索发现。作者是开源编排平台 AgentConnect 的团队，文中把自家产品列为比较对象之一。站点另有官方中文版，记入 altUrls，存档用英文版。删去站点导航、栏目与阅读时长、作者头像、文末的话题标签、页内目录、推荐阅读和产品推广。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：文章依据公开文档与代码、第三方上手评测和自己的使用，比较 DeepSeek 的 `dsh-superagent`、xAI 的 Grok Bot、Anthropic 的 Claude Duet 与 AgentConnect 如何把常驻智能体拆成协调与执行两层；Claude Tag 作为「一个对话一个会话」的基线，Muse 与 Dots 作为参照。四者的差别在于协调者看到的范围多大、不带执行日志时怎样恢复任务状态，以及多人共用频道时怎样防止跨权限泄露。关于 Duet，文中写它的界面顶部是主对话 Everything，下面是用户建的主题频道，共享同一份记忆，任务按状态分组；作者在预览账号中看到 Everything 的 Scheduled 标签页默认有两项周期任务：每天五次的 Check-in 和每天一次的 Morning brief。作者说明没有做统一的跨产品基准测试，Duet 的内部架构未公开，相关部分是根据界面和行为推断。

**保留理由**：已收资料中少见的跨产品架构比较，含 Claude Duet 预览账号里的默认定时任务等观察；出自同类产品的厂商，比较时需留意立场。
