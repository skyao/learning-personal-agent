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
collectedAt: 2026-11-05
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）。2026-10 Spark 改名为 Task 后，帮助页的用词已改为 tasks / task mode"
tags: [模型, 开放与价格]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的默认（Computer）视图；页面中的界面小图标已下载。这是 Gemini 的通用模型说明页，按「模型资料的收录原则」收入，因为其中写明了任务模式按订阅档位可用的模型。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：页面介绍 Flash-Lite、Flash、Pro、Argon 等模型和思考级别，并用表格列出各订阅档位在聊天与任务中可用的模型：无订阅和 Google AI Plus 不能使用任务；Google AI Pro 和 Ultra 在任务中可用 Flash 与 Argon，聊天中另有 Flash-Lite 和 Pro。开启自动选择时，多数提示用 Flash-Lite，需要更多推理时用 Flash 或 Pro；有订阅的用户可以在聊天模式和任务模式中手动切换模型。

**保留理由**：说明了 Task 运行时可选哪些模型、与订阅档位的关系，属于 Personal Agent 运行时选用模型的资料。

---

使用 Gemini 应用时，不同的 Gemini 模型可以根据你的具体需求提供最佳体验，无论你想要快速的日常回答，还是针对复杂问题的深入分析。部分模型仅在 Google AI 计划中提供。[了解如何从 Gemini 应用管理你的 Google AI 计划](https://support.google.com/gemini/answer/14517446)。

**重要：** 以下信息适用于你通过个人 Google 账号访问 Gemini 的情况。如果你通过工作或学校账号访问 Gemini，模型和功能的可用性将取决于你的 Workspace 许可证。[了解使用工作或学校账号的 Gemini 应用](https://support.google.com/gemini/answer/14620100)。

## Gemini 模型概览

Google 提供多种 Gemini 模型，针对不同类型的任务设计：

- **Gemini Flash-Lite：** 快速、高性价比的模型，专为快速回答日常问题和轻量任务而构建。
- **Gemini Flash：** 高速、能力强的模型，在标准聊天和任务模式中平衡性能与响应速度。
- **Gemini Pro：** 高级推理模型，专为复杂提示、精细编程和深度问题解决而设计。
- **Gemini Argon：** 顶级智能、动态深度推理，以及面向复杂工作流的最高性能。

## 模型可用性

对特定 Gemini 模型、思考级别和任务功能的访问，因你的计划和剩余可用用量而异。以下信息可能在不另行通知的情况下变更。

|  |  |  |  |
| --- | --- | --- | --- |
| **Google AI 计划** | **可用模型（聊天）** | **可用模型（任务）** | **思考级别** |
| 无 Google AI 计划 | - Auto 或 Flash-Lite\* | - N/A | 低（Low）、中（Medium）、高（High） |
| Google AI Plus | - Flash-Lite - Flash - Pro | - N/A | 低、中、高 |
| Google AI Pro | - Flash-Lite - Flash - Pro - Argon | - Flash - Argon | 低、中、高 |
| Google AI Ultra | - Flash-Lite - Flash - Pro - Argon | - Flash - Argon | 低、中、高 |

\*如果开启了自动模型选择，Gemini 将为每个提示选择合适的模型。大多数提示会使用 Flash-Lite 以获得快速回答。需要更多推理的提示可能会使用 Flash 或 Pro。如果关闭自动模型选择，所有回答都将使用 Flash-Lite。

## 思考级别

使用 Gemini 时，你可以调整模型生成回答时所使用的推理深度：

- **低：** 为直接的问题提供快速、简洁的回答。
- **中：** 为日常任务平衡处理速度与推理深度。
- **高：** 让模型仔细处理并推理复杂的多步骤提示。

**提示：**

- 更高级的模型和更高的思考级别会消耗更多用量。[进一步了解 Gemini 应用的限额](https://support.google.com/gemini/answer/16275805)。
- 如果你有 Google AI 计划并达到用量限额，你的聊天将继续使用 Flash-Lite。

## 自动模型选择

Gemini 应用使用自动模型选择来为你的提示决定最佳模型。[了解如何开启或关闭此功能。](#switch)

开启自动模型选择后，你的提示会被自动路由到最高效的模型和思考级别，以提供最佳回答并节省你的用量。

### 查看哪个模型生成了回答

在 Gemini 移动应用中

1. 在 Android 手机或平板电脑上，打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在左上方，点按「菜单」![Menu](images/img-02-f92da0.png)，然后在面板中点按一个聊天。
3. 在回答底部，点按「更多」![](images/img-03-53995d.png)。
4. 从菜单中选择「查看回答详情」![](images/img-04-53cb50.png)。
5. 详情中将包含用于生成该回答的模型。

在 Gemini 网页应用中

1. 在 Android 手机或平板电脑上，访问 [gemini.google.com](https://gemini.google.com)。
2. 在左上方，点按「菜单」![Menu](images/img-02-f92da0.png)，然后在面板中点按一个聊天。
3. 在回答底部，点按「更多」![](images/img-05-f0faa8.png)。
4. 从菜单中选择「查看回答详情」![](images/img-06-e480d5.png)。
5. 详情中将包含用于生成该回答的模型。

## 手动切换模型

如果你有 Google AI 计划，可以在聊天模式和任务模式中手动切换模型。[进一步了解 Gemini 应用中的任务](https://support.google.com/gemini/answer/17094507)。

在聊天模式或任务模式中切换模型

1. 在 Android 手机或平板电脑上，访问 [gemini.google.com](https://gemini.google.com) 或打开 Gemini 移动应用 ![](images/img-01-4a5c21.png)。
2. 在聊天框底部，点按当前选中的模型 ![](images/img-07-25cf80.png)。
3. 点按你想使用的模型。
   - 标有锁形图标的更高档位模型需要符合条件计划升级
4. （可选）选择你偏好的思考级别：
   - 低
   - 中
   - 高

Gemini 将在当前对话中继续使用该模型和思考级别，包括你之后返回到同一对话时。

**提示：** 如果你不选择思考级别，它将默认为低。

### 开启或关闭自动模型选择

在 Gemini 移动应用中

1. 在 Android 手机或平板电脑上，访问 [gemini.google.com](https://gemini.google.com)。
2. 在左上方，点按「菜单」![Menu](images/img-02-f92da0.png)。
3. 在左下方，点按「设置」![](images/img-08-bbb6bc.png) >「用量限额」![](images/img-08-bbb6bc.png)。
4. 在底部，开启 ![](images/img-09-61b4ad.png) 或关闭 ![](images/img-09-61b4ad.png) 自动模型选择。

在 Gemini 网页应用中

1. 在 Android 手机或平板电脑上，打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在左上方，点按「菜单」![Menu](images/img-02-f92da0.png)。
3. 在左下方，点按「设置」![](images/img-08-bbb6bc.png) >「用量限额」![](images/img-08-bbb6bc.png)。
4. 在底部，开启 ![](images/img-09-61b4ad.png) 或关闭 ![](images/img-09-61b4ad.png) 自动模型选择。

## 相关资源

- [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961)
- [登录 Gemini 应用需要什么](https://support.google.com/gemini/answer/13278668)
- [使用 Gemini 应用](https://support.google.com/gemini/answer/13275745)
- [Gemini 应用的限额与功能可用性](https://support.google.com/gemini/answer/16275805)
- [从 Gemini 应用管理你的 Google AI 计划](https://support.google.com/gemini/answer/14517446)
