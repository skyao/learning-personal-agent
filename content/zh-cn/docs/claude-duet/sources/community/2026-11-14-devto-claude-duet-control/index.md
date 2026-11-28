---
title: "Claude Duet 先开口，控制权就变了：审批疲劳才是真正的风险"
linkTitle: "先开口的控制权"
date: 2026-11-14
originalTitle: "Claude Duet Messages You First. That Changes Who Is in Control."
sourceUrl: "https://dev.to/suraj_khaitan_f893c243958/claude-duet-messages-you-first-that-changes-who-is-in-control-3n74"
author: "Suraj Khaitan"
publisher: "DEV Community"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
tags: [安全, 持续执行]
products: [claude-duet]
dateNote: "发表日在窗口外（11 月 14 日），属本轮检索发现的回填；页面标注 Posted on Nov 14。"
---

{{< source-info >}}

**收录说明**：直接下载；删去封面图、作者头像与文末作者简介、讨论提问。文首的「午饭前十二次审批」为作者明确标注的假设场景，不是真实发生的 Duet 事件。原文全文存于本目录的 original.md，网站上不显示。

**内容摘要**：作者认为 Claude Duet 真正的改变不是功能，而是控制权的位置：聊天助手等用户先开口，主动式智能体则自行决定何时需要用户、读用户没有特意展示的内容、按自己的时间表要求用户做决定，同意由此从「逐项批准」变成了「授予常驻权限」。文章梳理了 Anthropic 公布的防护设计——后果性操作须经审批、意图检查在模型之外、Duet 不交易证券也不在账户间转移资金，并指出这些控制能处理机器能处理的部分，处理不了人的一端：审批请求过多会让人不再细读、只管点通过，作者称之为审批疲劳，并以一个明确标注为假设的场景说明，一张按设计完整显示了收件地址的审批卡，也可能因为收件域名与客户域名只差一个字母而被用户放过。文末作者给出四周小团队试用计划与向任何主动式智能体提问的七个问题，结论是主动式智能体的首要设计目标不是速度或自主性，而是保护用户真正读审批卡的那一刻。

**保留理由**：提供了已收资料里没有的东西：对 Claude Duet 控制架构的独立分析，把 Anthropic 自己承认的审批疲劳问题作为核心论点展开，并区分了机器能处理的控制与人注意力这一端无法由机器兜底的部分。
