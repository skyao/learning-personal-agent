---
title: "帮助：例程"
linkTitle: "帮助：例程"
date: 2026-11-05
originalTitle: "Routines"
sourceUrl: "https://cursor.com/help/grok-bot/routines"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [持续执行, 功能更新, 开放与价格]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：例程让一个 Bot 在定时或事件发生时运行某个流程，事件包括 Slack 消息、GitHub、Linear、Sentry、PagerDuty 事件、邮件或 webhook 调用。例程在云端运行，电脑关闭也不影响；通过在聊天里让 Bot 创建和修改，时间表按设置里的时区计算，新例程不会在创建时立刻运行，要试跑须用 Test，而 Test 会真实执行动作并消耗用量。Slack 触发和 webhook 是例程的一部分，webhook 返回 200 只表示已接受并启动，不表示已完成。每次运行都消耗用量，频繁的时间表或繁忙频道的触发器可能一天用完一周额度；例程每小时合计最多运行 300 次，单个最多 200 次，超出会失败且不自动重试。文中还提到一个已知问题：所有 Grok Bot 例程共享的某个速率限制会导致部分运行失败，官方称正在修复。

**保留理由**：写明例程的触发方式、测试行为、消耗用量与速率限制，是研究持续执行能力及其代价的直接材料。
