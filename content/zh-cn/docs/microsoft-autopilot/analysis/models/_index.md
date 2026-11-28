---
title: "Microsoft Autopilot：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 运行在 OpenAI 的 GPT-6.1 Sol 上（OpenAI 作为微软子处理方），管理员关闭 OpenAI 时自动改用 Azure OpenAI 托管的 GPT-5.6 Sol；用户不能选模型。操作审查由一个未具名的「第二个 AI 模型」完成。Copilot 整体是 OpenAI 与 Anthropic 等多模型路由，Autopilot 是其中固定单一模型的例外。
---

## 概要

- 管理员文档与应用卡写明 Autopilot 运行在 GPT-6.1 Sol 上，由作为微软子处理方的 OpenAI 提供。
- 管理员在「作为 Microsoft 子处理方运营的 AI 提供方」设置中关闭 OpenAI 后，Autopilot 自动改用 Azure OpenAI 托管的 GPT-5.6 Sol；两种处理方式的隐私差别见[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})。
- 用户不能用提示词切换模型，也没有模型选择控件。
- 操作审查用「第二个 AI 模型」，型号未公开。
- 针对英语优化，界面已翻译不代表各语言都做过评估。

## GPT-6.1 Sol，退路是 GPT-5.6 Sol

| 情形 | 模型 | 提供与处理方 | 来源 |
| --- | --- | --- | --- |
| 默认 | GPT-6.1 Sol | OpenAI，作为微软子处理方 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}}) |
| 管理员关闭 OpenAI | GPT-5.6 Sol | Azure OpenAI 托管 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 操作审查 | 未具名的「第二个 AI 模型」 | 未说明 | [Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}}) |

应用卡称用户不能用提示词切换模型，Autopilot「也没有单独的模型选择控件」（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。Redmondmag 称管理中心的报表显示使用的 AI 模型和工具（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。应用卡与要求页称 Autopilot 针对英语优化（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。

GPT-6.1 Sol 也出现在 OpenAI dots 的分析中（[dots：模型]({{< relref "/docs/dots/analysis/models" >}})），两款产品此时用的是同一家的模型。

## Copilot 层面的多模型

9 月的定价博文称 Copilot 的 USL 与 UBB 都运行在多家实验室的模型上，「目前指的是 OpenAI 和 Anthropic」，更多实验室和开放权重模型将加入；GPT-5.6 和 Sonnet 5 含在 USL 内，Opus 5 等带限额；Auto 在准确度、速度、成本之间路由（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。同文的内部成本对比脚注称 Cowork 使用 Opus 5 与 GPT-5.6 Sol（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。Copilot 博客称员工可手动选 OpenAI 或 Anthropic 模型，访问由组织策略治理（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。Fortune 引 Copilot 副总裁 Annie Pearl：Copilot 主要依赖 Anthropic 和 OpenAI 的模型，也用 xAI 的 Grok（[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})）。

新闻手册与 The Neuron 介绍的 Microsoft-Decision-1.1 用于在 Copilot 与 Cowork 之间路由、决定 Cowork 中 Auto 的推理强度（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})）；资料没有说 Autopilot 使用 Auto 或该模型。

推断：Copilot 整体是多模型路由，Autopilot 却固定为单一 OpenAI 模型、不给用户选择，可能与它需要稳定的长期行为和统一的审查链有关；资料没有给出理由。

## 早期预览的模型

Scout 桌面预览（2026-06 至 09）的模型目录继承自 GitHub Copilot，用户可逐条消息切换，管理员可按提供方禁用（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[Scout 组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）；当时的报道列出 OpenAI、Anthropic、Gemini 等模型，版本说法不一（[TestingCatalog 06-05]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})、[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。11 月的 Autopilot 文档不再提 GitHub Copilot 和模型选择。

## 资料缺口

- 操作审查所用「第二个 AI 模型」的型号与提供方。
- 是否会提供 Anthropic 等其他模型；关闭 OpenAI 后能力是否有差别。
- 模型调用如何折算 Copilot Credits。

## 主要资料

- 官方：[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})（GPT-6.1 Sol、GPT-5.6 Sol、无选择控件）；[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})（审查模型）；[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})（英语优化）；[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})（Copilot 多模型背景）；[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[Scout 组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})（早期预览）。
- 媒体：[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[TestingCatalog 06-05]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})。
