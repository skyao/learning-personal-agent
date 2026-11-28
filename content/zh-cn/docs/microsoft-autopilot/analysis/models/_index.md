---
title: "Microsoft Autopilot：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 运行在 OpenAI 的 GPT-6.1 Sol 上（OpenAI 作为微软子处理方），管理员关闭 OpenAI 时自动改用 Azure OpenAI 托管的 GPT-5.6 Sol；用户不能选模型。另有一个未具名的「第二个 AI 模型」审查操作。Scout 时期经 GitHub Copilot、可逐条切换模型的做法不再出现。
---

## 概要

- 管理员文档与应用卡写明 Autopilot 运行在 GPT-6.1 Sol 上，由作为微软子处理方的 OpenAI 提供（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。
- 管理员在「作为 Microsoft 子处理方运营的 AI 提供方」设置中关闭 OpenAI 后，Autopilot 自动改用 Azure OpenAI 托管的 GPT-5.6 Sol（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）；两种处理方式的隐私差别见[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})。
- 用户不能用提示词切换模型，也没有模型选择控件（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。这与 Scout 时期继承 GitHub Copilot 模型目录、逐条切换模型的做法不同。
- 操作审查用「第二个 AI 模型」，型号未公开（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。
- Autopilot 针对英语优化，界面已翻译不代表各语言都做过评估（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。

## 2026-11：GPT-6.1 Sol，退路是 GPT-5.6 Sol

| 情形 | 模型 | 提供与处理方 | 来源 |
| --- | --- | --- | --- |
| 默认 | GPT-6.1 Sol | OpenAI，作为微软子处理方 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}}) |
| 管理员关闭 OpenAI | GPT-5.6 Sol | Azure OpenAI 托管 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 操作审查 | 未具名的「第二个 AI 模型」 | 未说明 | [Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}}) |

应用卡称用户不能用提示词切换模型，Autopilot「也没有单独的模型选择控件」（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。Redmondmag 称管理中心的报表显示使用的 AI 模型和工具（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。

## Copilot 层面的多模型

9 月的定价博文称 USL 与 UBB 都运行在多家实验室的模型上，「目前指的是 OpenAI 和 Anthropic」，更多实验室和开放权重模型将加入；GPT-5.6 和 Sonnet 5 含在 USL 内，Opus 5 等带限额（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。博文的内部成本对比脚注称 Cowork 使用 Opus 5 与 GPT-5.6 Sol（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。Copilot 博客称员工可手动选 OpenAI 或 Anthropic 模型，访问由组织策略治理（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。Fortune 引 Copilot 副总裁 Annie Pearl：Copilot 主要依赖 Anthropic 和 OpenAI 的模型，也用 xAI 的 Grok（[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})）。

新闻手册与 The Neuron 介绍的 Microsoft-Decision-1.1 用于在 Copilot 与 Cowork 之间路由、决定 Cowork 中 Auto 的推理强度（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})），资料没有说 Autopilot 使用 Auto 或该模型。

推断：Copilot 整体是多模型路由，Autopilot 却固定为单一 OpenAI 模型、不给用户选择；这可能与它需要稳定的长期行为和统一的审查链有关，资料没有给出理由。GPT-6.1 Sol 也出现在 OpenAI dots 的分析中（[dots：模型]({{< relref "/docs/dots/analysis/models" >}})），两款产品此时用的是同一家的模型。

## 更名前：Scout 经 GitHub Copilot 的模型（2026-06 至 2026-09）

以下为 2026-11-14 分析的内容。11 月的 Autopilot 文档不再提 GitHub Copilot 和模型选择器。

### 经 GitHub Copilot 处理

FAQ 写明：模型目录继承自 GitHub Copilot，可用模型由组织的 GitHub Copilot 管理员决定；支持的模型可能包括第三方和开源模型，包括来自中国提供方的模型；各提供方可能限制某些国家或地区使用，组织需自行确保合规（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。社区综述照此转述（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。这一处理路径带来的隐私后果见[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})。

负责任 AI FAQ 称 Scout 不使用用户数据训练模型，没有提到为 Scout 专门训练或微调（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。

### 用户与管理员的选择

入门页的设置有 Default model 与 Default reasoning effort（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。7 月更新加入撰写框的模型选择器、上下文窗口大小（含 Max）、每个自动化独立的推理强度（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。组策略 `DisabledModels` 按模型 ID、`DisabledProviders` 按提供方禁用（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）。

6 月报道中可见的模型：

| 来源 | 日期 | 说法 |
| --- | --- | --- |
| [TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}}) | 06-05 | 模型选择器涵盖 OpenAI 与 Anthropic，含 GPT 5.5 |
| [Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}}) | 06-06 | Claude Opus 和 Sonnet、最高到 5.4 的 GPT 变体、Gemini 3.1 Pro，另有自动路由模式 |

两者只隔一天，版本说法不同，资料无法判断哪个准确。

### 9 月的 Copilot 层面

更名文章称 Cowork、Code、Autopilot 以及 Astra、Fable 等前沿模型运行在按用量计费（UBB）上；Auto 会对每个请求权衡准确性、速度和成本做路由，管理员可设定哪些模型系列对不同用户组可用（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。文中的 Auto 是 Chat/Office 中 Copilot 的机制，没有说 Autopilot 是否使用。iThome 称 Autopilot 没有公开绑定单一模型（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。社区作者转述 Fortune 称 Copilot 主要依赖 Anthropic 和 OpenAI 的模型，也用 xAI 的 Grok，并猜测 Astra、Fable 与 OpenAI、Anthropic 的同名模型有关，自己标注未确认（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 资料缺口

- 操作审查所用「第二个 AI 模型」的型号与提供方。
- 是否会提供 Anthropic 等其他模型；关闭 OpenAI 后能力是否有差别。
- 每次任务的模型调用量如何折算 Copilot Credits。

## 主要资料

- 官方：[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})（模型目录与处理路径）；[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})（用户选择）；[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})（管理员禁用）；[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})。
- 媒体：[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 2026-11 新增官方：[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})（GPT-6.1 Sol、GPT-5.6 Sol、无选择控件）；[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})（审查模型）；[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})（英语优化）；[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})（Copilot 多模型背景）。
- 2026-11 新增媒体：[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})。
