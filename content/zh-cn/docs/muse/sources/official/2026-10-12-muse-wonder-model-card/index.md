---
title: "Muse Wonder 模型卡（节选）"
linkTitle: "Muse Wonder 模型卡"
date: 2026-10-12
originalTitle: "Muse Wonder Model Card"
sourceUrl: "https://research.meta.ai/static/muse-wonder-model-card"
author: "未署名"
publisher: "Meta"
language: en
fidelity: 节选
translation: 待翻译
collectedAt: 2026-11-05
updatedAt: "2026-10-23"
dateNote: "发布日期取模型卡中的 Date of Release；PDF 元数据创建于 2026-10-23，卡中有一条 2026-10-23 的 ExploitGym 评估更正，按更新日期记"
tags: [模型]
products: [muse]
---

{{< source-info >}}

**收录说明**：模型卡 PDF 由 Muse Wonder 研究博客链接。按「模型资料的收录原则」只收与 Personal Agent 直接相关的部分（用户 2026-11-05 决定）：第 1 节模型概况、第 2 节预期用途、第 3 节的总体评测方法与「Personal and Professional Agents」一组基准的说明和分数、第 6 节局限与使用条件。未收：第 3 节的编码与通用基准、第 4 节前沿风险评估（化学生物、网络安全、失控）、第 5 节 Trust and Safety、附录。评测分数表在 PDF 中是图片，原图收入 images/，其中 Personal and professional agents 一组分数另行转录为表格。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：模型卡介绍 Muse Wonder 与 Muse Wonder Full 两个模型：2026-10-12 发布，输入支持文本、图像、视频、音频，推理时上下文长度 1M tokens，预期用途中特别强调「personal and professional agentic tasks」。个人与专业智能体一组共 9 项基准，与 GPT-6 Astra、Claude Fable 5.1、Claude Opus 5.5（均为 max 推理强度）对比：Muse Wonder Full 在内部综合指数 Personal Superintelligence Index（59.1）、Harvey LAB-AA、Vals Finance Agent V2、AutomationBench-AA 上分数最高，MemoryBench 上 Muse Wonder（85.6）与 Muse Wonder Full（85.5）都高于对比模型；在 HealthBench Pro、GDP.pdf、JobBench、OSWorld V2.1 上低于对比模型中的最高分。卡中说明了两项内部基准：MemoryBench 测试在 64K 到 100K tokens 的多轮对话中准确回忆关键信息，FocusBench 测试智能体在住房、出行、IT、金融等个人事务中跨多轮交互克服现实阻碍、适应变化环境的能力。局限部分指出模型在多步推理中仍会出错、不适合 18 岁以下用户，并建议在能采取现实行动的智能体场景中加入人工确认等护栏；使用受 Muse 补充服务条款约束。

**保留理由**：Muse Wonder 是驱动 Muse 的模型（见同日发布的新闻稿与研究博客），这份模型卡给出了它在个人智能体类任务上的官方评测数字和两项面向个人智能体的内部基准（MemoryBench、FocusBench）的定义，是比较 Muse 底层能力的一手来源。
