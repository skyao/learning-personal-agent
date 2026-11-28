---
title: "Autopilot 如何审查操作"
linkTitle: "文档：操作审批机制"
date: 2026-11-24
originalTitle: "How Autopilot reviews actions"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/approval"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
tags: [安全, 持续执行]
products: [microsoft-autopilot]
updatedAt: "2026-11-24"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-10。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。待翻译。

**内容摘要**：Autopilot 用第二个 AI 模型在操作执行前，把它与用户的请求（含隐含步骤和“只读”“先别发”等限制）比对，无论以用户身份还是自己的身份行事规则相同。读取、搜索、起草直接运行并少量抽查；发送、分享、删除、修改及创建或修改自动化由自动审查决定，匹配则直接运行，不匹配或无法检查则弹出审批卡；付款和敏感浏览器步骤始终需要批准。只有用户自己的消息算请求，邮件、文档、网页里的指令不构成授权；审批卡出现在与 Autopilot 的 Teams 一对一聊天（及发起请求的 Microsoft Copilot），只有 Allow（单次）和 Deny，没有“总是允许”，过期则该操作不运行。本版本没有面向用户或管理员的自动审查设置。

**保留理由**：Scout 文档是分级权限，而这篇讲的是由第二个模型做的自动审查，以及审批卡的三种提示原因和“无总是允许”，是已收资料里没有的新机制。
