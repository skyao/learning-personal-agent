---
title: "你的智能体忘了任务的中间部分"
linkTitle: "智能体忘了任务中段"
date: 2026-11-04
originalTitle: "Your Agent Forgot the Middle of the Job"
sourceUrl: "https://aihomebuilding.com/stories/muse-mid-job-forgetting-context-rot-2026"
author: "Frank DeLuca"
publisher: "AIHomeBuilding"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-22
tags: [记忆与上下文, 模型, 持续执行]
products: [muse]
---

{{< source-info >}}

## 收录说明

本页收录的文章于 2026-11-04 发布在 AIHomeBuilding。直接下载后以 article.article-body 抽取全文，未做删改。头图为装饰图，未收。原文全文存于本目录的 original.md，网站上不显示，待翻译。

作者限定：所有硬数字来自通用智能体与模型研究，非 Muse 本身；Meta 未公布 Muse 的上下文腐烂、漂移率或召回率，15%–40%、13.1%、39% 是对“这个物种”的警告，不是这款产品的分数；开篇 12 步任务为虚构场景。

## 内容摘要

文章以一个 12 步、跨数日的虚构任务开篇：让 Muse 比较三家供应商、查收件箱里的续订日期、建截止日历、起草取消信，周五收到的报告里一个续订日期与另一家供应商的日期调换了。作者区分三种遗忘机制：一是上下文腐烂（context rot），Chroma 2025 年研究测试 18 个前沿模型，发现上下文变长后性能下降 15% 至 40%；二是“中间丢失”（lost in the middle），Liu 等人 2023 年的研究表明模型对长上下文开头与结尾的信息利用优于中间；三是漂移，arXiv:2512.12791 的评估框架报告复杂场景下记忆检索召回率仅 13.1%。文章列出 Muse 的三项设计防御：成果落文件、跨会话记忆文件可读可编辑、摘要续跑，并给出五点检查清单（写文件简报、关键约束放前面并重复、拆腿验收、逐行核对中期摘要、换手时重新简报）。

## 保留理由

已收资料里没有系统讲长任务遗忘三种机制的文章；15%–40%、13.1%、39% 三组数字与“拆腿验收”的清单是后续讨论长任务可靠性的直接参照。
