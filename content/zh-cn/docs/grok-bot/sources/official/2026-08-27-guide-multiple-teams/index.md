---
title: "指南：我如何运行多个 Grok Bot 团队"
linkTitle: "指南：多个 Bot 团队"
date: 2026-08-27
originalTitle: "How I run multiple teams of Grok Bots"
sourceUrl: "https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots"
author: "Eric Zakariasson"
publisher: "SpaceXAI（xAI）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "日期取页面元数据 article:published_time"
tags: [持续执行, 连接器]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：此前 Wayback 没有快照、原站返回 403，暂未收录；2026-11-28 原站可直接下载，补收。去掉了下载与联系销售按钮，视频改为一行链接。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：作者平时把 Coder、Writer、Researcher 等 Grok Bot 分在不同对话里，同时做多个项目时难以区分信号与噪声。于是他仿照人类团队的做法：每个项目对应一个 Grok Bot 频道和 Notion 数据库中的一条记录，在 Notion 里建 Projects 与 Tasks 两个数据库，并建一个 projects Manager Bot，用 Project Ops 技能创建项目、开频道并配备 Bot。配备规则是先复用已有 Bot、除项目经理外最多提议五个 Bot（每个频道上限六个）、仅在没有合适的 Bot 且他同意时才新建。Bot 卡住时会把任务标为 Blocked 并在频道里通知他。作者称这是仍在尝试的实验性做法。

**保留理由**：提供了用户自己组织多 Bot 协作的具体做法，比功能说明更贴近实际使用方式。

---

每个项目对应一个频道、一份成员名单和一块 Notion 看板。一种像人类团队那样协调 Bot 的实验性做法。

---

大多数时候，我把自己的 Grok Bot 当作彼此独立的对话来用。Coder 在一个对话里，Writer 在另一个，Researcher 在第三个。这样一直都没问题，直到你需要同时应付几个不同的项目。这时就很难从噪声里分辨出信号，也很难让它们保持同步。

作为个人，也作为由人组成的团队，我们习惯按项目来协调工作。每个项目有一份规格说明、一份计划，也许还有一个用来沟通的 Slack 频道。然后每个项目里会有不同的任务，由某个人承担。

于是我把这套做法照搬了过来。每个项目对应一个 Grok Bot 频道，以及 Notion 数据库里的一条记录。注意，这是我还在尝试的实验性做法。

[视频](https://media.x.ai/v1/website/grok-bot-guides-how-i-run-multiple-teams-of-grok-bots-06-video-a47249eb.mp4)

0:00 / 0:00

一个项目，一个频道，一份名单。

## 搭建

我在 Notion 里建了两个数据库：Projects 和 Tasks。然后建了一个 **projects**（复数）Manager Bot。它负责项目和任务在更高层面的协调。它有一个 Project Ops 技能，负责创建项目、开频道，并配上合适的 Bot。它承担的是元层面的工作。

一个项目等于侧栏里的一个频道，频道里有这支 Bot 团队（还有我）。

![侧栏中的一个项目频道](images/img-01-51bb94.avif)侧栏中的一个项目频道![频道成员名单](images/img-02-0ef96d.avif)频道成员名单

我加上的配备规则：

- 先复用已有的 Bot。可以是 Coder、Researcher、Writer，或者我已经定义好的任何其他 Bot。
- 除项目经理（PM）外最多提议五个 Bot。每个频道上限六个 Bot（只是我随手定的数字）。
- 只有在现有的 Bot 都不合适、并且我同意之后，才新建 Bot。它可以是某个领域日后会被反复用到的专家，也可以只服务于这个项目的临时 Bot。

Projects 数据库长这样：

![Notion 中的 Projects 数据库](images/img-03-608aa2.avif)Notion 中的 Projects 数据库

## 我如何使用

频道建好之后，我就在里面和这份名单上的 Bot 交流，一起把项目的任务范围理清。

项目经理也在频道里，但主要是看进展，并确保数据库是最新的。

当某个 Bot 卡住或需要更多输入时，它会把任务标为 *Blocked*，然后在频道里通知我。通常 Bot 们自己就能完成很多事，我只要看着卡片被移来移去就行。说实话，挺有满足感的。

![任务在看板上移动](images/img-04-459f73.avif)任务在看板上移动

有意思的是，我在这上面搭得越多，它就越像一个最初为人类设计的系统。一块看板、一个管理者、认领任务的专家、一个阻塞列、一个频道。

目前的实验就是这些。如果你也在运营一支 Bot 团队，我想看看你的做法。你是怎么运行你的团队的？

—

作者：Eric Zakariasson
