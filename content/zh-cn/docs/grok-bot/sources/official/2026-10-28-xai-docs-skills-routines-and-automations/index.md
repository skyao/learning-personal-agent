---
title: "文档（docs.x.ai）：技能与例程"
linkTitle: "docs.x.ai：技能与例程"
date: 2026-10-28
originalTitle: "Skills and routines"
sourceUrl: "https://docs.x.ai/grok-bot/skills-routines-and-automations"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [持续执行, 功能更新]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「例程」和 cursor.com 文档「Work」与这页部分重合。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：技能是跨 Bot 共享的私有库，可以发布给团队；「Teach a task」可以录屏演示一个流程（最长 10 分钟、不录麦克风），生成技能草稿。例程可以按定时触发，也可以由 Slack、GitHub、Linear、Sentry、PagerDuty、邮件或 webhook 事件触发。每个 Bot 最多 50 个例程，调度间隔至少 5 分钟，所有例程合计每小时最多运行 300 次、单个例程最多 200 次，超限不自动重试。新建例程不会立即运行，用 Test 试跑会真实执行并消耗用量；文档提醒高频例程一天就可能耗尽一周用量。

**保留理由**：给出了 Grok Bot 持续执行的触发方式和配额数字，可以和其他产品的定时、事件机制对照。
