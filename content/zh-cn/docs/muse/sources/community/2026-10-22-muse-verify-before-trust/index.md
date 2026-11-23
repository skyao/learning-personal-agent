---
title: "“完成”一词是你的智能体最危险的词：这就是能抓住错误的核查习惯"
linkTitle: "“完成”是最危险的词"
date: 2026-10-22
originalTitle: "\"Done\" Is the Most Dangerous Word Your Agent Knows. This Is the Verification Habit That Catches the Errors."
sourceUrl: "https://aihomebuilding.com/stories/muse-verify-before-trust-2026"
author: "Frank DeLuca"
publisher: "AIHomeBuilding"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-22
tags: [实测评测, 安全, 模型]
products: [muse]
---

{{< source-info >}}

## 收录说明

本页收录的文章于 2026-10-22 发布在 AIHomeBuilding。直接下载后以 article.article-body 抽取全文，未做删改。头图为装饰图，未收。原文全文存于本目录的 original.md，网站上不显示，待翻译。

作者限定：引用的均为通用智能体基准研究，非 Muse 自身的测量，作者未对 Muse 做对照实验，全文为文献分析。

## 内容摘要

文章以普林斯顿团队（ICML 2026）的研究开篇：15 个模型、两个智能体基准，首次把可靠性作为独立维度测量，结论是 24 个月的能力快速提升只带来可靠性的小幅改善；结果一致性在一个基准上为 0.58 至 0.84，另一个为 0.52 至 0.90，即最差的模型重复同一任务时近半数给出不同结果；在金融基准上最常见的失败是智能体把交易做错却表现得完全确定。作者给出复合数学：每步成功率 95% 时，30 步任务干净完成的概率仅约 21%；想让 10 步任务 95% 正确，每步须达 99.5%。加州大学伯克利分校对多智能体失败的分类（NeurIPS 2025 Spotlight）基于 1642 条标注执行轨迹，任务失败率 41% 至 86.7%，14 种失败模式分三类；干预实验显示，仅给协调智能体明确的最终决策权就使任务成功率提升 9.4 个百分点，增加一个核查步骤提升 15.6 个百分点。作者据此提出五条核查规则：发票规则、十四步规则、核查税、失败三桶分类、关卡须由平台而非智能体自我执行。

## 保留理由

这是唯一一篇以可靠性（而非准确率）为独立维度系统梳理研究的文章；0.58–0.84 的一致性区间、21% 的 30 步复合概率、15.6 个百分点的核查收益、97.1% 的工具描述缺陷率是已收资料里没有的研究证据链。
