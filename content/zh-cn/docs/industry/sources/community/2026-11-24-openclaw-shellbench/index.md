---
title: "ShellBench：面向日常真实任务的智能体基准测试"
linkTitle: "ShellBench 基准测试"
date: 2026-11-24
originalTitle: "Introducing ShellBench, the benchmark for real-world tasks"
sourceUrl: "https://openclaw.ai/blog/shellbench"
altUrls: ["https://arxiv.org/abs/2611.32946"]
author: "Vincent Koc"
publisher: "OpenClaw"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-27
tags: [实测评测, 安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载。原文全文存于本目录的 original.md，网站上不显示，待翻译。模型×框架单次尝试通过率表据文中图表转录（图内注：DeepSeek V4.1 Flash 未在 Hermes 框架下测试，总体按可用框架等权平均；来源为 ShellBench 报告表 1）；其余三张图表（重复可靠性、框架通过率与安全、成本前沿）的数据已在正文中给出，未另行转录；作者头像与头图为装饰图，未收。arXiv 论文（arXiv:2611.32946）记入 altUrls。受测模型中属跟踪产品者仅 Muse（Wonder Full 与 Wonder 1.0），products 只列 muse。

**内容摘要**：OpenClaw Foundation 与 Parsewave、Hugging Face、红帽、加州大学伯克利分校合作，于 2026 年 11 月 24 日发布 ShellBench 基准测试：100 个日常真实任务、53,100 次评分运行，任务源自 1,000 万次以上匿名化真实智能体交互，覆盖 12 个模型与 5 种 agent 框架，并以 381 条安全标准考核正确性之外的安全性。单次尝试通过率最高也只有约六成，GPT-6 Astra 以 62.5% 居首，Claude Fable 5.2（61.9%）与 GPT-6.1 Sol（61.4%）紧随其后；Muse Wonder Full 总体 47.4%，在 Pi 框架下 56.0%、Claude Code 下 38.1%，Muse Wonder 1.0 总体 39.7%。全部运行中有 15.7% 至少违反一条安全检查，即使满足全部正确性标准的运行中仍有 9.9% 违反安全要求；模型选择对成绩的影响远大于框架选择，同一框架内最高与最低模型的中位差距为 45.7 个百分点。

**保留理由**：本篇以 100 个日常真实任务与 381 条安全标准横向衡量 12 个模型在 5 种框架下的表现，提供了 Muse Wonder Full 与 Wonder 1.0 的逐项通过率。安全违规率与重复试验数据为个人智能体的可靠性与安全性现状提供了已收 PersonalAgentBench 之外的另一组独立证据。
