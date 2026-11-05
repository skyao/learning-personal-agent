---
title: "文档：使用 Grok Bot 工作"
linkTitle: "文档：使用 Grok Bot 工作"
date: 2026-11-05
originalTitle: "Work with Grok Bot"
sourceUrl: "https://cursor.com/docs/grok-bot/work"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 记忆与上下文, 持续执行, 连接器]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

**收集者摘要**：文档按四部分写：Bot、消息与协作、计算机与应用、技能与例程。Bot 是有名字、工作和长期上下文的持久队友，记忆保存稳定偏好、重要事实和工作摘要，但文档提醒记忆不能代替权威来源，安全边界应靠批准和规则而非记忆。同一账号下所有 Bot 共用一台持久云端计算机，工作区为 /workspace；登录时先用 Vault、再用连接的密码管理器、最后用安全表单，单点登录、通行密钥、验证码等交给用户接管。应用（连接器）账号级共用，OAuth 令牌留在后端。群聊可放 2 到 6 个 Bot，Bot 之间异步交接；例程可按时间表或事件触发（如 Slack 消息、GitHub 通知），测试例程会真实执行动作。还介绍了「Teach a task」示范教学（最多记录十分钟，逐步推出），恢复顺序为从最轻的重试到最后的重置。

**保留理由**：这是日常使用层面最全的一篇，覆盖记忆范围、计算机共享、凭证处理、群聊与交接、例程和恢复，可与产品设计文章对照。
