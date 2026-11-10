---
title: "Poke 文档：Poke API"
linkTitle: "Poke API"
date: 2026-11-09
originalTitle: "Poke API"
sourceUrl: "https://poke.com/docs/api"
author: "未署名"
publisher: "The Interaction Company of California"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-09
tags: [连接器, 持续执行]
products: [poke]
dateNote: "帮助文档页没有标注发布或更新日期，取收集日期（美东）"
---

{{< source-info >}}

**收录说明**：Poke 帮助文档，直接下载后抽取。待翻译。

**内容摘要**：Poke API 允许从应用、脚本和自动化工具以编程方式向 Poke 发消息，这些消息由 Poke 处理，可完全访问邮件、日历、提醒和已连接的集成，效果与用户亲自发短信相同。用法是向 POST https://poke.com/api/v1/inbound/api-message 发送带 Bearer API key 的 JSON，整个 body 会作为上下文转发给 agent；API key 在 Kitchen 的 API Keys 中创建，只显示一次。旧端点 inbound-sms/webhook 已弃用，只接受 pk_ 开头的 V1 key，新端点需要 V2 key。文档给出浏览器扩展、GitHub Action 部署失败告警、Typeform/CRM 事件、VS Code 扩展等触发示例，并建议用环境变量保存 key、可建多个 key、泄露即吊销。消息到达后，Poke 评估请求、决定使用哪些工具（邮件、日历、Notion/Whoop 等集成）、执行并回复。

**保留理由**：说明外部事件如何触发 Poke 执行，是“事件驱动的持续运行”和 API key 凭证管理的官方细节。
