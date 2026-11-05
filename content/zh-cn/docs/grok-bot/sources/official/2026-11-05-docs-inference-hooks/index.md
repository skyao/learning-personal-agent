---
title: "文档：推理钩子（Inference hooks）"
linkTitle: "文档：推理钩子"
date: 2026-11-05
originalTitle: "Grok Bot inference hooks"
sourceUrl: "https://cursor.com/docs/grok-bot/inference-hooks"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

**收集者摘要**：推理钩子把每个受管的 Grok Bot 模型请求签名后发给组织自己运行、或经安全厂商提供的 AI 安全服务器，服务器返回允许（allow）或拒绝（deny）。拒绝会终止该轮，成员看到拦截提示；检查失败按所选模式处理：影子模式（Shadow，默认，只记录不拦截）、放行模式（失败时放行）、拦截模式（失败时拦截）。开启 Validate Tool Calls 后，服务器还会在工具调用运行前检查，但不检查工具运行后的实际效果，也不检查 Bot 回复成员的内容。请求帧含完整对话，不含系统提示和模型隐藏推理，也永远不带秘密值；范围覆盖 Grok Bot 的子智能体、长对话摘要和例程，不含云端智能体、语音通话等。该功能为 beta，面向所有 Enterprise 团队，Cursor 声明不保存发往钩子的内容。

**保留理由**：最细的一份企业侧安全控制文档，写明了哪些内容会被检查、哪些不会，以及失败时放行还是拦截，用来评估 Bot 的内容与工具调用审查边界。
