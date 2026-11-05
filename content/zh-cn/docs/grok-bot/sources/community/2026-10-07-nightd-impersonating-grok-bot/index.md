---
title: "冒充 Grok Bot：为了好玩，（没有）为了利益"
linkTitle: "nightd：伪造 Web Bot Auth 签名"
date: 2026-10-07
originalTitle: "Impersonating Grok Bot for Fun and (No) Profit"
sourceUrl: "https://nightd.dev/blog/impersonating-grok-bot-for-fun-and-no-profit/"
author: "Kevin"
publisher: "nightd.dev（个人博客）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
tags: [安全, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：直接下载；去掉了文末的分享按钮和返回链接。作者为独立的安全研究者，文章是对 Grok Bot 云端计算机环境的分析，含代码；文中的披露时间线照录。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

## 收集者摘要

作者分析了 Grok Bot 用来向网站证明自己身份的 Web Bot Auth 机制：该标准用 Signature 请求头验证自动化程序的身份，而不依赖 User-Agent 或 IP 白名单。作者在 Bot 的桌面环境中找到负责签名的脚本，发现启动脚本虽然从环境变量中删除了令牌，但签名进程仍持有凭证，可以从进程环境中读出，进而在 Bot 之外为任意请求生成有效的 Grok Bot 签名（有效期 90 秒），从而访问 Cloudflare 放行 Grok Bot 的网站。文章附有披露时间线。

## 保留理由

从安全角度揭示了 Grok Bot 云端计算机中凭证的存放方式，以及「智能体身份认证」这一机制的弱点，可与官方安全文档中关于凭证隔离的说法对照。
