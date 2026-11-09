---
title: "Meta 在悄悄给部分 Muse 请求签名，DataDome 发现"
linkTitle: "Muse 请求悄悄签名"
date: 2026-10-31
originalTitle: "Meta Is Quietly Signing Some Muse Web Requests, DataDome Finds"
sourceUrl: "https://www.allthingsmuse.com/articles/meta-muse-web-bot-auth-signed-requests/"
author: "Icarus"
publisher: "All Things Muse"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-09
tags: [安全]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图 Jolly 插画与文中的「Earlier coverage」栏目。发表日期在窗口外（10 月 31 日），本轮经 Cloudflare 立场文件一文内链发现，属首报回填。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：DataDome 威胁研究副总裁 Jérôme Segura 在 10 月 30 日的 LinkedIn 帖子中称，Meta 自 10 月 12 日前后开始悄悄测试 Web Bot Auth，“since around Oct. 12”，签署请求覆盖 Meta-WebIndexer 与 Muse 至少两个 agent，签署量在逐步增加；Meta 未公开确认，其公开爬虫文档未提及 Web Bot Auth、HTTP message signatures 或签名密钥目录。Web Bot Auth 是 HTTP Message Signatures 的应用形式，该标准作为 RFC 9421 于 2024 年 2 月发布、由 Cloudflare 于 2025 年 5 月提议，签署方在请求中附加 Signature、Signature-Input、Signature-Agent 三个头，接收方从固定路径发布的目录取公钥验签。Muse 自 9 月 8 日美国上线以来存在身份问题：上线两周内 Amazon 以其浏览时不表明身份等理由将其屏蔽；DataDome Q3 报告称 Muse 不表明身份，同时统计其 9 月 22 日至 10 月 3 日间产生 2910 万次请求、占 9 月智能体浏览器流量的 33%。架构上，每个 Muse 用户的 agent 运行在各自的云虚拟机内并内置完整浏览器，Q3 样本中 99.3% 的 Muse 请求来自云与内容分发基础设施，其中 Cloudflare 占 81.2%、Fastly 占 18.1%，仅 0.6% 来自消费级互联网服务商。局限在于，Segura 称签署量相对较小，帖子未给出数量、占比及两个 agent 之间的分布；DataDome 已为客户增加对 Meta Web Bot Auth 请求的验证支持，但 Meta 签署大部分流量或公开表态之前，网站面对的是可验证与不可验证两类 Meta 流量。

**保留理由**：本篇是仓库中首篇记录 Muse 流量获得可验证身份（签名测试）的资料，提供了 Web Bot Auth 机制与 RFC 9421 的出处，并与 DataDome「Muse 不表明身份」的 Q3 结论形成时间线对照（测量窗口 9 月 22 日–10 月 3 日，签署始于 10 月 12 日前后）。
