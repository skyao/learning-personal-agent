---
title: "关于 Gemini 模型"
linkTitle: "帮助：模型与档位"
date: 2026-11-05
originalTitle: "About Gemini models"
sourceUrl: "https://support.google.com/gemini/answer/18648722?hl=en"
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-28
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）。2026-10 Spark 改名为 Task 后，帮助页的用词已改为 tasks / task mode；2026-11-28 发现原文更新：模型从 Flash-Lite、Flash、Pro、Argon 换成 Gemini 4 Hydrogen、Neon、Carbon；档位表去掉思考级别一列，无订阅与 Plus 用户的任务也可用 Hydrogen；新增 AI 积分说明；删去「查看回答由哪个模型生成」与「开关自动选择模型」两节。原文存档已覆盖，旧译文删除，已重新翻译"
tags: [模型, 开放与价格]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的默认（Computer）视图；页面中的界面小图标已下载。这是 Gemini 的通用模型说明页，按「模型资料的收录原则」收入，因为其中写明了任务模式按订阅档位可用的模型。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：页面介绍三个模型：Gemini 4 Hydrogen（高速、均衡，用于聊天和任务模式）、Gemini 4 Neon（前沿级智能，用于深入分析和复杂工作流）、Gemini 4 Carbon（最强，用于高级编码和长周期难题）。档位表中，任务可用的模型是：无订阅与 Google AI Plus 为 Hydrogen，Pro 为 Hydrogen 与 Neon，Ultra 为 Hydrogen、Neon 与 Carbon；聊天另有 Auto。使用 Auto 时 Gemini 在 Hydrogen 与一个快速轻量模型之间选择；手动选择模型时才能调整思考级别，默认 Low。达到用量上限后聊天改用轻量模型，也可以升级或购买 AI 积分继续用更高级的模型。

**保留理由**：给出 Gemini 4 系列模型与订阅档位在任务模式中的对应，可与 11-05 版的 Flash / Argon 档位对照。

---

使用 Gemini 应用时，不同的 Gemini 模型可以根据你的具体需求提供最佳体验，无论你想要快速的日常答案，还是对复杂问题进行深入分析。有些模型仅在 Google AI 套餐中提供。[了解如何从 Gemini 应用管理你的 Google AI 套餐](https://support.google.com/gemini/answer/14517446)。

**重要：** 以下信息适用于你通过个人 Google 账号访问 Gemini 的情况。如果你通过工作或学校账号访问 Gemini，模型和功能的可用性取决于你的 Workspace 许可。[了解使用工作或学校账号的 Gemini 应用](https://support.google.com/gemini/answer/14620100)。

## Gemini 模型概览

Google 提供多个 Gemini 模型，面向不同类型的任务：

- **Gemini 4 Hydrogen：** 一个高速、能力强的模型，在标准聊天和任务模式中平衡性能与响应速度。
- **Gemini 4 Neon：** 前沿级智能，在深入分析和复杂工作流中性能出色。
- **Gemini 4 Carbon：** 我们最强的模型，专为高级编码和最困难的长周期问题设计。

## 模型可用性

对特定 Gemini 模型、思考级别和任务功能的访问，取决于你的套餐和剩余可用用量。以下信息可能随时变更，恕不另行通知。

|  |  |  |
| --- | --- | --- |
| **Google AI 套餐** | **可用模型（聊天）** | **可用模型（任务）** |
| 无 Google AI 套餐 | - Auto\* | - Hydrogen |
| Google AI Plus | - Auto\* - Hydrogen | - Hydrogen |
| Google AI Pro | - Auto\* - Hydrogen - Neon | - Hydrogen - Neon |
| Google AI Ultra | - Auto\* - Hydrogen - Neon - Carbon | - Hydrogen - Neon - Carbon |

\*使用 Auto 时，Gemini 会在 Hydrogen 或一个快速轻量模型之间选择，并为每个提示选择适当的思考级别，同时节省你的用量。

## 思考级别

当你手动选择模型时，可以调整模型生成回答时使用的推理深度：

- **低：** 为直接的问题提供快速、简洁的回答。
- **中：** 为日常任务平衡处理速度与推理深度。
- **高：** 让模型仔细处理并推理复杂、多步骤的提示。

**提示：**

- 更高级的模型和更高的思考级别会消耗更多用量。[详细了解 Gemini 应用的限制](https://support.google.com/gemini/answer/16275805)。
- 如果你有 Google AI 套餐并达到用量上限，你的对话将继续使用我们的快速轻量模型。
- 你也可以选择升级或购买 AI 积分，以继续使用更高级的模型。[详细了解 AI 积分。](https://support.google.com/googleone/answer/16287445)

## 自动选择模型

Gemini 应用使用自动模型选择来为你的提示决定最佳模型。

你的提示会自动在 Hydrogen 和我们的快速轻量模型之间路由，并配以最合适的思考级别，以提供尽可能好的回答并节省你的用量。

**提示：**

- 要使用更高级的模型，请手动选择它们。
- 要使用更高级的模型，请升级到 Google AI 套餐。[了解如何管理你的 Google AI 套餐](https://support.google.com/gemini/answer/14517446)。

## 手动切换模型

如果你有 Google AI 套餐，可以在对话模式和任务模式中手动切换模型。[详细了解 Gemini 应用中的任务](https://support.google.com/gemini/answer/17094507)。

在对话模式或任务模式中切换模型

1. 在 Android 手机或平板上访问 [gemini.google.com](https://gemini.google.com)，或打开 Gemini 移动应用 ![](images/img-01-4a5c21.png)。
2. 在聊天框底部点击当前选中的模型 ![](images/img-02-25cf80.png)。
3. 点击你要使用的模型。
   - 标有锁形图标的更高级模型需要升级到符合条件的套餐
4. （可选）选择你偏好的思考级别：
   - 低
   - 中
   - 高

Gemini 会在当前对话中继续使用该模型和思考级别，包括你之后回到同一段对话时。

**提示：** 如果你手动选择模型时没有选择思考级别，将默认为「低」。

## 相关资源

- [Gemini 应用隐私中心](https://support.google.com/gemini/answer/13594961)
- [登录 Gemini 应用需要什么](https://support.google.com/gemini/answer/13278668)
- [使用 Gemini 应用](https://support.google.com/gemini/answer/13275745)
- [Gemini 应用的限制与功能可用性](https://support.google.com/gemini/answer/16275805)
- [从 Gemini 应用管理你的 Google AI 套餐](https://support.google.com/gemini/answer/14517446)
