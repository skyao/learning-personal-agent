---
title: "你的智能体雇了帮手，没人审计交接"
linkTitle: "智能体雇帮手，无人审计交接"
date: 2026-10-31
originalTitle: "Your Agent Hires Help. Nobody Audits the Handoff."
sourceUrl: "https://aihomebuilding.com/stories/muse-delegation-depth-handoff-loss-2026"
author: "Marcus Washington"
publisher: "AIHomeBuilding"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-22
tags: [安全, 模型, 实测评测]
products: [muse]
---

{{< source-info >}}

## 收录说明

本页收录的文章于 2026-10-31 发布在 AIHomeBuilding。直接下载后以 article.article-body 抽取全文，未做删改。头图为装饰图，未收。原文全文存于本目录的 original.md，网站上不显示，待翻译。

作者限定：1.9% 是借用的代理值，Meta 未公布 Muse 自身的交接缺陷率；DynaFlow 用的是 27B 参数模型做数学竞赛题，不是 Muse Spark 做消费任务；“只 spawn 一层”来自第三方对生产提示词副本的解读，非 Meta 官方说法。

## 内容摘要

文章以 2025 年 2 月购物智能体绕过确认步骤完成 31.43 美元 Instacart 采购（《华盛顿邮报》报道，AI Incident Database 第 1028 号）开篇，指出 Muse 可把任务拆给并行子智能体，Meta 将多智能体协调列为模型内置能力。新加坡国立大学的 DynaFlow 研究发现，协调器未经训练时 1.9% 的交接出现严重信息传递缺陷，改用显式可审计的程序调用交接后降至 0.9%，六项基准准确率从 77.18% 升至 88.08%。作者以 1.9% 为代理值推算至少一次严重缺陷的概率：1 次交接约 1.9%、3 次约 5.6%、5 次约 9.1%、10 次约 17.4%。文中还引用 2026 年 10 月 6 日行业报告中智能体向攻击者转移 281,200 美元及 5 月一笔 175,000 美元错址转账；Stripe Link 条款写明用户对连接智能体发起的交易负责，即使源于 bug、幻觉或误解。

## 保留理由

已收资料里没有讨论多智能体交接损耗的文章；DynaFlow 的 1.9%/0.9% 与 77.18%→88.08% 是可复核的公开研究数字，交接深度与缺陷概率的对照表是本篇独有的分析工具。
