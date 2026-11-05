---
title: "文档：Grok Bot 安全"
linkTitle: "文档：安全"
date: 2026-11-05
originalTitle: "Grok Bot security"
sourceUrl: "https://cursor.com/docs/grok-bot/security"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 隐私, 运行环境, 模型]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：文档给出控制路径：团队策略、网络策略、零数据保留、连接器令牌留在后端、Auto Review。网络策略有三种模式（全部放行、默认加团队允许列表、仅团队允许列表），Enterprise 专有，未设置时默认全放行；MCP 服务器需另开「Apply to MCP servers」才受同一名单约束。批准环节有允许一次、始终允许、拒绝，Auto Review 是独立审查模型，评估 shell 命令、应用调用、计算机使用、自动化写入和委派，但不审查记忆写入等副作用。Bot 没有自己的身份，只能做到所属成员能做的事；连接器令牌留在 Cursor 后端，保存在 Vault 的登录和卡由系统填入而不让模型看到。计算机为每用户一个 Firecracker microVM，位于美国；模型由系统自行选择，没有模型选择器，团队模型允许列表不适用。对提示注入采取分层防护，并说明只能降低而不能消除风险。

**保留理由**：这是安全和隐私最系统的一篇，覆盖隔离、网络、审批、凭证、日志、数据保留、模型和提示注入，且明确写出哪些不审查，是评估 Bot 信任边界的主要依据。
