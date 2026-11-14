---
title: "Microsoft Autopilot：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  Scout 不绑定单一模型：模型调用经 GitHub Copilot 处理，模型目录继承自 GitHub Copilot，由组织的 GitHub Copilot 管理员决定可用范围；用户可逐条消息切换模型与推理强度。是否为 Scout 专门训练模型，资料没有说明。
---

## 概要

- LLM 处理经由 GitHub Copilot，模型目录继承自 GitHub Copilot，可能包括第三方和开源模型，「包括来自中国提供方的模型」（官方 FAQ）。
- 用户可设默认模型与推理强度，在撰写框逐条切换模型，每个自动化可单独设推理强度和上下文大小。
- 管理员可按模型 ID 或提供方（如 anthropic、openai）禁用模型。
- 6 月的两份报道列出的模型版本不一致（GPT 5.5 与「最高 5.4」）。
- 9 月的 Copilot 把 Astra、Fable 等前沿模型归入按用量计费，Autopilot 本身用哪个模型没有说明。

## 经 GitHub Copilot 处理

FAQ 写明：模型目录继承自 GitHub Copilot，可用模型由组织的 GitHub Copilot 管理员决定；支持的模型可能包括第三方和开源模型，包括来自中国提供方的模型；各提供方可能限制某些国家或地区使用，组织需自行确保合规（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。社区综述照此转述（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。这一处理路径带来的隐私后果见[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})。

负责任 AI FAQ 称 Scout 不使用用户数据训练模型，没有提到为 Scout 专门训练或微调（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。

## 用户与管理员的选择

入门页的设置有 Default model 与 Default reasoning effort（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。7 月更新加入撰写框的模型选择器、上下文窗口大小（含 Max）、每个自动化独立的推理强度（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。组策略 `DisabledModels` 按模型 ID、`DisabledProviders` 按提供方禁用（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）。

6 月报道中可见的模型：

| 来源 | 日期 | 说法 |
| --- | --- | --- |
| [TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}}) | 06-05 | 模型选择器涵盖 OpenAI 与 Anthropic，含 GPT 5.5 |
| [Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}}) | 06-06 | Claude Opus 和 Sonnet、最高到 5.4 的 GPT 变体、Gemini 3.1 Pro，另有自动路由模式 |

两者只隔一天，版本说法不同，资料无法判断哪个准确。

## 9 月的 Copilot 层面

更名文章称 Cowork、Code、Autopilot 以及 Astra、Fable 等前沿模型运行在按用量计费（UBB）上；Auto 会对每个请求权衡准确性、速度和成本做路由，管理员可设定哪些模型系列对不同用户组可用（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。文中的 Auto 是 Chat/Office 中 Copilot 的机制，没有说 Autopilot 是否使用。iThome 称 Autopilot 没有公开绑定单一模型（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。社区作者转述 Fortune 称 Copilot 主要依赖 Anthropic 和 OpenAI 的模型，也用 xAI 的 Grok，并猜测 Astra、Fable 与 OpenAI、Anthropic 的同名模型有关，自己标注未确认（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 资料缺口

- Autopilot 默认使用的模型与路由规则；云端版是否仍经 GitHub Copilot。
- 6 月模型清单的准确版本。

## 主要资料

- 官方：[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})（模型目录与处理路径）；[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})（用户选择）；[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})（管理员禁用）；[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})。
- 媒体：[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
