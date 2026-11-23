---
title: "你给 AI 智能体立了 40 条规矩，它只遵守约一半：是哪一半"
linkTitle: "40 条规矩只遵守一半"
date: 2026-10-20
originalTitle: "You Gave Your AI Agent 40 Rules. It Follows About Half. Here Is Which Half."
sourceUrl: "https://aihomebuilding.com/stories/muse-standing-instructions-half-stick-2026"
author: "Frank DeLuca"
publisher: "AIHomeBuilding"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-22
tags: [记忆与上下文, 模型, 实测评测]
products: [muse]
---

{{< source-info >}}

## 收录说明

本页收录的文章于 2026-10-20 发布在 AIHomeBuilding。直接下载后以 article.article-body 抽取全文，未做删改。头图为装饰图，未收。原文全文存于本目录的 original.md，网站上不显示，待翻译。

作者限定：无 Muse 自身指令遵守率的公开数据，所有基准测的都是通用模型而非 Muse 的收件箱与日历工作负载；阶梯耐久性估计为定性判断；mouse.dev 拆解为第三方逆向工程，非 Meta 文档。

## 内容摘要

文章说明 Muse 的常驻指令存在三个文件：描述每段对话都试图遵守的价值观与习惯的 persona 文件、保存关于用户的事实与偏好的记忆文件、描述用户本人的 user 文件，并由夜间后台任务整理；第三方对 Muse 运行时的拆解（mouse.dev）显示记忆以纯 Markdown 保存，每小时后台任务用原始消息核对新声明。作者引用的研究数据是：2026 年论文《The Compliance Gap》将同一指令置于系统提示、用户消息、工具描述、多处重复四种位置，遵守率从工具描述中的 26% 到重复时的 65%；IFScale 基准给前沿模型同时下达最多 500 条指令，最佳模型在最大密度下遵守率仅 68%；华盛顿大学的 Offscript 研究用自动化审计检查 Reddit 真实用户的自定义指令，86.4% 的对话被标记为可能偏离，人工复核确认 22.2% 为实质违规。作者据此提出原创的四级阶梯：裸文本指令、指令加机器检查、检查加拦截关卡、自动化执行；并以自家生产线为例，文本禁 em dash 规则失效、改用 grep 计数关卡后才生效。

## 保留理由

已收资料里没有讨论常驻指令遵守率的文章；26%–65%、68%、86.4%/22.2% 四组数字与“裸文本—检查—关卡—自动化”四级阶梯是本篇独有的分析框架，且直接关联 Muse 的 persona/memory/user 三文件结构。
