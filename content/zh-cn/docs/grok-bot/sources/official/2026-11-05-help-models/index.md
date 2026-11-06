---
title: "帮助：Grok Bot 用哪些模型"
linkTitle: "帮助：使用的模型"
date: 2026-11-05
originalTitle: "Which AI models power Grok Bot?"
sourceUrl: "https://cursor.com/help/grok-bot/models"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [模型, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Grok Bot 不绑定单一模型，每个任务用它认为最可能得到最佳结果的后端模型，可以是 xAI 自家模型，也可以是子处理方名单上的第三方模型，同一用户的不同请求可能不同。用户看不到某个请求实际用了哪个模型，用量和支出界面统一记作 Grok Bot 用量；用户不能指定、请求或屏蔽某个模型，设置里也没有模型选择器。团队的 Cursor 模型允许列表或屏蔽列表对 Grok Bot 无效，启用时会显示相关提示。文中答复称，把任务路由到 Opus 5.5 不会改变每个 token 的价格。只有子处理方名单上的服务商才能处理数据。

**保留理由**：这是官方对模型选择方式的说明，说明模型不可见、不可选，且可能含第三方模型，对判断其模型层的透明度和合规影响有用。

---

Grok Bot 如何为每个请求选择背后的模型、你在用量中看到什么、它如何影响你的用量限制，以及它如何与团队模型设置交互。

Grok Bot 不绑定单一模型。对于每项任务，它使用最有可能带来最佳结果的后端模型。这可以是 xAI 的第一方模型，也可以是[子处理方名单](https://trust.cursor.com/subprocessors)上某家提供商的第三方模型，而且选择可能因请求而异。

## 我能看到哪个模型处理了某个 Grok Bot 请求吗？

不能。Grok Bot 不显示某个请求背后的模型。你的用量和支出视图将此活动记为 Grok Bot 用量，而不是按提供商或模型名称记录。见[套餐和支出界面把什么称为用量？](https://cursor.com/help/grok-bot/plans#what-do-the-plan-and-spending-screens-call-usage)。

## 我能在 Grok Bot 中选择、请求或屏蔽某个特定模型吗？

不能。Grok Bot 没有按用户或按请求的模型选择，[Grok Bot 设置](https://cursor.com/docs/grok-bot/settings)中也没有模型选择器。用户不能被路由到某个特定模型，也不能被路由离开某个特定模型。Grok Bot 始终使用最有可能为该任务产生最佳结果的模型。

## Grok Bot 使用 Opus 5.5 会让每个 token 更贵吗？

不会。我们努力为你提供最佳的性价比（price-performance），并尽可能延长你的用量。你用得多快取决于你交给 Grok Bot 的工作类型以及每项任务需要多少投入，而把任务路由到 Opus 5.5 不会改变你每个 token 的成本。要查看你的用量去了哪里，在 Grok Bot 中打开 **Settings** > **Usage & Billing**，或见 [Grok Bot 用量如何运作？](https://cursor.com/help/grok-bot/plans#how-does-grok-bot-usage-work)。

## 我团队的 Cursor 模型允许列表适用于 Grok Bot 吗？

不适用。Grok Bot 不受你团队的 Cursor [模型允许列表或屏蔽列表](https://cursor.com/docs/enterprise/model-and-integration-management#model-access-control)治理。它使用 xAI 第一方模型，并可能使用第三方模型，无论那些设置如何。设有模型允许列表的团队在[启用 Grok Bot](https://cursor.com/docs/grok-bot/teams#enabling-grok-bot-for-your-team)时会看到此提示。关于数据处理，见 Grok Bot 安全页面上的[模型与数据](https://cursor.com/docs/grok-bot/security#models-and-data)。

## Grok Bot 可以使用哪些第三方提供商？

仅限[子处理方名单](https://trust.cursor.com/subprocessors)上的提供商。模型集合会随时间变化；该名单是哪些提供商可以处理你的数据的权威参考。
