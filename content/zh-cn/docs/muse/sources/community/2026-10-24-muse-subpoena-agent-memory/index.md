---
title: "2000 万条已删聊天其实没删：你的 AI 智能体记得你什么"
linkTitle: "2000 万条已删聊天"
date: 2026-10-24
originalTitle: "20 Million Deleted Chats Weren't Deleted: What Your AI Agent Remembers About You"
sourceUrl: "https://aihomebuilding.com/stories/muse-subpoena-agent-memory-2026"
author: "Catherine Chen"
publisher: "AIHomeBuilding"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-22
tags: [隐私, 安全, 记忆与上下文]
products: [muse]
---

{{< source-info >}}

## 收录说明

本页收录的文章于 2026-10-24 发布在 AIHomeBuilding。直接下载后以 article.article-body 抽取全文，未做删改。头图为装饰图，未收。原文全文存于本目录的 original.md，网站上不显示，待翻译。

作者限定：时报案的命令针对 OpenAI 而非 Meta，各家政策不同，文章在部分地方做了概括；作者核实了 Muse 的文档化控制，但无法测试任何提供方在真实法律命令下的行为；单部署的文件计数仅作示例，不代表典型用户；作者自述是“读起来像律师的记者”，非法律建议。

## 内容摘要

文章以纽约时报诉 OpenAI 案的法院命令开篇：2025 年 5 月 13 日，曼哈顿联邦治安法官 Ona Wang 命令 OpenAI 保留并隔离本应删除的全部输出日志数据；2025 年 11 月 7 日，法院命令 OpenAI 向纽约时报及共同原告移交超过 2000 万条去标识化 ChatGPT 日志，其中一些是作者在命令下达数月前已删除的对话。DuckDuckGo 的调查发现 75% 的受访者不知道 AI 聊天记录可被执法部门传唤；《华盛顿邮报》的调查发现至少十几起法院案件引用过 AI 聊天记录作为证据；在 United States v. Heppner 案中，法院裁定被告的 Claude 对话不受律师—客户特权或工作成果保护。作者对照 Meta 自身文档与一个真实重度部署，盘点 Muse 实际留存的六层记录：主聊天无法删除、子聊天可归档或删除，唯一完整清除是 Reset；记忆图谱可删但仅尽力而为，文档写明清除对话不等于私密、记忆仍可写入；活动账本记录全部动作与授权；常驻许可只能由用户在设置中逐项撤销；Gmail、日历与健康同步可断开、令牌移除；工作区文件与生成物可由用户删除与下载。该部署中六层共存 18 份每日记忆日志、263 个人物画像、21 个群组画像与一份 transcript 数据库。

## 保留理由

这是唯一一篇把传票与删除权问题落到 Muse 六层留存结构的文章；2000 万条日志移交、Heppner 案无特权、18/263/21 的部署计数是已收资料里没有的法律与实测结合的证据。
