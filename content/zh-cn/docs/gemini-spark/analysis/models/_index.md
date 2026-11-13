---
title: "Gemini Spark：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Spark 发布时跑在 Gemini 3.5 上，8 月 13 日换成 Gemini 3.7 Flash；10 月起任务模式可在 Flash 与顶级模型 Argon 之间手动切换，并选择思考级别，档位越高越耗用量。
---

## 概要

- 模型换过两次：2026-05-19 发布时「运行在 Gemini 3.5 上，并使用 Antigravity harness」；2026-08-13 起改用 Gemini 3.7 Flash，官方称改进了对 Workspace 应用的工具使用。
- 截至 2026-11-10，任务模式只对 AI Pro 和 Ultra 开放，可用模型为 Flash 和 Argon；无订阅和 AI Plus 用户没有任务模式。
- 用户可以在任务中手动切换模型和思考级别（低、中、高，默认低）；更高的模型和思考级别消耗更多用量。
- 图片生成和编辑用 Nano Banana 模型。
- 是否为 Spark 专门训练或优化模型，资料没有说明；官方只说 3.7 Flash 改进了 Spark 用到的工具调用。

## 模型变化时间线

| 日期 | 模型 | 官方说法 | 资料 |
| --- | --- | --- | --- |
| 2026-05-19 | Gemini 3.5（同日发布 3.5 Flash）+ Antigravity harness | 「Spark 运行在 Gemini 3.5 上」 | [I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}}) |
| 2026-08-13 | Gemini 3.7 Flash | 改进了对 Google Workspace 应用的工具使用，复杂多技能工作流的准确性和输出质量更高，能更高效地合并文件、起草邮件、更新状态文档 | [3.7 Flash 发布]({{< relref "/docs/gemini-spark/sources/official/2026-08-13-gemini-3-7-flash-spark" >}}) |
| 2026-10（具体日期资料未载） | Flash、Argon 可选 | Argon 为顶级智能、动态深度推理，面向复杂工作流 | [帮助：Gemini 模型]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-gemini-models" >}}) |

iThome 2026-10 的比较表把 Spark 的主要模型列为「Gemini 3.5 系列」（[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})），晚于 8 月的换代，信息已过时。

## 按订阅档位与思考级别选择

帮助页的模型表（[帮助：Gemini 模型]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-gemini-models" >}})）：

| 档位 | 聊天模式 | 任务模式 |
| --- | --- | --- |
| 无 Google AI 计划 | Auto 或 Flash-Lite | 不可用 |
| AI Plus | Flash-Lite、Flash、Pro | 不可用 |
| AI Pro、AI Ultra | 另有 Argon | Flash、Argon |

- 有 Google AI 计划的用户可以在聊天和任务模式中手动切换模型和思考级别；思考级别分低、中、高，不选时默认为低（[帮助：Gemini 模型]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-gemini-models" >}})）。创建任务时从顶部模型菜单更改（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。
- 更高的模型和更高的思考级别消耗更多用量；聊天达到限额后继续使用 Flash-Lite（[帮助：Gemini 模型]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-gemini-models" >}})）。任务达到用量上限时如何降级，帮助页没有写。
- 自动选择模型的说明只针对聊天，任务模式是否也会自动路由，页面没有明说。
- 任务中可以用 Nano Banana 模型生成和编辑图像（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。

一名开发者论坛用户称，表格写入失败的故障「就在他们推出 Argon 的时候」开始（[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})），这只是时间上的重合，没有证据表明两者有关。

## 与其他产品对照

iThome 的比较表列出：Dots 用 GPT-6 Astra，Muse 用 Muse Spark 模型，Grok Bot 官方没有公开绑定单一模型，Microsoft Autopilot 支持多模型路由（[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

推断：Spark 的默认模型是 Flash 档而非最强的 Argon，结合「更高模型消耗更多用量」的规则看，Google 在任务模式上倾向用较便宜的模型跑大部分工作，把 Argon 留给用户手动选择的复杂任务；资料中没有 Google 对此的说明。

## 资料缺口

- 是否有为 Spark 或任务模式专门训练、微调的模型；Antigravity harness 的具体作用。
- Argon 的推出日期、在任务模式下的用量消耗倍数。
- 任务模式是否自动路由模型；达到用量上限后的降级方式。

## 主要资料

- 官方：[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})；[3.7 Flash 发布]({{< relref "/docs/gemini-spark/sources/official/2026-08-13-gemini-3-7-flash-spark" >}})；[帮助：Gemini 模型]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-gemini-models" >}})；[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})。
- 媒体：[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})（模型对照）。
- 社区：[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})。
