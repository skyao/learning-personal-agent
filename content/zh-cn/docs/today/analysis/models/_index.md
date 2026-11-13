---
title: "Today AI：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  官方只说底层是「前沿模型」并有模型编排，没有点名；极客公园在实测截图中看到 Today 调用 Claude Opus 5 处理编程任务。团队认为前沿模型的「说人话」能力在变差，从第一天起计划自己做「交互模型」，截至 2026-10-16 已有早期实验版本。
---

## 概要

- 官方称 Today 用「前沿模型」并有模型编排，未公开具体模型；内部评估覆盖规划、记忆检索和连接器成功率。
- 极客公园实测中，Today 处理游戏 mod 汉化时自行编写 Prompt，调用 Claude Opus 5 执行（据页面截图）。这是资料中唯一的具体模型信息。
- 团队称单一长对话要求低延迟，因此「用尽可能小的模型」，并提高上下文信息密度。
- 晚点访谈中团队称从第一天起计划自己做模型，已提前开始训练，有早期实验版本；理由是内部个人助理评测集上部分新模型分数越来越低：coding 变强，「说人话」变差。
- 官方发布了一套助理评测框架 v0.1（12 个维度），发布时尚未对任何产品打分。

## 前沿模型 + 编排

官方博客称底层把前沿模型、任务执行和云计算机组合成智能体循环，内部栈含模型编排；内部测试覆盖规划、记忆检索和连接器成功率，场景取自真实使用（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[官方：Meet Today]({{< relref "/docs/today/sources/official/2026-08-03-meet-today" >}})）。

极客公园作者把游戏 mod 压缩包发给 Today，它自行拆包读文档，「调用了 Claude Opus 5 开始汉化」，侧边栏可见代码重构过程（[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})）。从描述看，主对话的模型与执行编程任务的模型可能不同，但资料不足以确认路由规则。

团队自述为降低延迟、提高 Context 密度，「用尽可能小的模型」（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。

## 自研「交互模型」

团队称 Today 更需要一个「交互模型」：更拟人、语气自然，又能真正执行任务；认为应用公司应向下做模型（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。晚点访谈中受访者称：

- Today 从第一天起就计划自己做模型，后训练、中训练、预训练都只是手段；最近已提前开始训练，有一个早期实验版本。
- 在 Today 内部面向个人 AI 助理的评测集上，部分新模型的分数越来越低：coding 越来越强，交互越来越「不说人话」，这是优化目标的分化，也是新公司的机会。
- 算力储备不算竞争要素，可以靠市场和资源解决。

（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）潮涌AI转述了同一理由（[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})）。

## 评测：先定框架，暂无分数

官方 2026-09-20 发布助理评测框架 v0.1（版本日期 9 月 18 日）：12 个维度，总分为已测维度的无加权平均并附覆盖率标签，只给分数不排名，Today 自己的分数也只在此框架下公布；文章写明「目前什么都还没测，Today 没测，任何产品都没测」，计划首个公布的指标是转写准确率（[官方评测框架]({{< relref "/docs/today/sources/official/2026-09-20-today-assistant-benchmark" >}})）。

Today Recording 公布了一项转写评测：用公开基准中 5.5 小时的多人重叠长会议，与三家语音供应商的原始输出对比，说话人归属错误率下降超过四个百分点，文字误差保持稳定（[官方：Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})）。供应商名称与基准名称未公开。

## 资料缺口

- 主对话、后台任务、转写各用什么模型；模型路由规则。
- 自研模型的规模、训练方式与上线计划。
- 内部个人助理评测集的内容与结果。
- 评测框架 v0.1 之后是否公布过分数。

## 主要资料

- 官方：[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[Meet Today]({{< relref "/docs/today/sources/official/2026-08-03-meet-today" >}})（前沿模型与编排）；[官方评测框架]({{< relref "/docs/today/sources/official/2026-09-20-today-assistant-benchmark" >}})；[Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})（转写评测）。
- 媒体：[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})（自研模型）；[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})（交互模型、小模型）；[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})（调用 Claude Opus 5）。
- 社区：[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})。
