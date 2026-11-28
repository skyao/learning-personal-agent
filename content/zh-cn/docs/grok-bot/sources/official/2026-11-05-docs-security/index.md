---
title: "文档：Grok Bot 安全"
linkTitle: "文档：安全"
date: 2026-11-05
originalTitle: "Grok Bot security"
sourceUrl: "https://docs.x.ai/grok-bot/security"
altUrls: ["https://cursor.com/docs/grok-bot/security"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：网络策略增为四种模式，新增 Allow All Sites Except These（至多 50 个站点）；应用聊天中 Bot 可见 Vault 已存卡的号码和安全码；Shared Bot 改称 Team Bot"
tags: [安全, 隐私, 运行环境, 模型]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：文档给出控制路径：网络策略、审批与 Auto Review、推理钩子、身份与登录、日志审计、数据保留、模型、提示注入。网络策略有四种模式（Allow All Network Access、Allow All Sites Except These、Defaults + Team Allowlist、Team Allowlist Only），Enterprise 专有，未设置时默认全放行；屏蔽模式下 Blocked Sites 最多 50 个站点，按主机名匹配并含子域，是尽力而为而非安全边界。批准环节有 Allow once、Always allow、Deny，Auto Review 是独立审查模型，评估 shell 命令、应用调用、计算机使用、自动化写入和委派；Action Recording 为 Enterprise 专有，默认关闭，保留 90 天。Bot 没有自己的身份，连接器令牌留在 Cursor 后端；Vault 中的登录和 Secure Form 的值由系统填入、模型不接收，但在 Grok Bot 应用的聊天中，Bot 能看到已存卡的号码和安全码以便在结账时填写，Vault 不适用于 Team Bots。计算机位于美国，模型由系统自行选择，没有模型选择器，团队模型允许列表不适用；对提示注入采取分层防护，并说明只能降低而不能消除风险。

**保留理由**：这是安全和隐私最系统的一篇，覆盖网络、审批、凭证、日志、数据保留、模型和提示注入，且明确写出哪些不审查，是评估 Bot 信任边界的主要依据。
