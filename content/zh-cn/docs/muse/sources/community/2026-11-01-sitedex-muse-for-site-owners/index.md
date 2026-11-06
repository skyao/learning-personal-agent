---
title: "Meta Muse 智能体与你的网站：需要检查什么"
linkTitle: "Sitedex：网站如何识别 Muse"
date: 2026-11-01
originalTitle: "Meta's Muse agent: what your site can and can't see"
sourceUrl: "https://www.sitedex.dev/guides/meta-muse-for-site-owners"
author: "未署名"
publisher: "Sitedex"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
tags: [运行环境]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载。文末推广自家 fetchcheck 工具的两处（一段建议与一个链接）已去掉；副标题未收。Sitedex 是一家机器人检测服务商，本文是其面向网站主的指南。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文章核对了 Meta 已公开的资料：Muse 在虚拟机里用一个真实的 Chromium 浏览器上网，读取页面靠无障碍树快照；Meta 称 Muse 上网时显示为用户本人的活动，因此网站看到的 Muse 访问可能像普通顾客。截至 11 月 1 日，Meta 没有为 Muse 公布用户代理、IP 段或签名；Meta 面向网站主的页面列出的 5 个爬虫里也没有 Muse，也未提及签名请求。但作者发现 `meta.com/.well-known/http-message-signatures-directory` 上已有一个含 5 把 Ed25519 密钥的文件，这是 Web Bot Auth 使用的地址，Meta 未说明由什么签名，作者也未观察到带签名的 Muse 请求。文中还提到亚马逊 9 月屏蔽 Muse 的原因之一是不亮明智能体身份，以及沃尔玛结账时的人机验证曾拦住 Muse，沃尔玛对 TechCrunch 称并非有意屏蔽。

**保留理由**：独立核查了 Meta 面向网站主的爬虫清单与 Web Bot Auth 密钥目录，给出 Muse 在网站侧可识别性的实测结论，是已收资料中唯一从网站主角度讨论 Muse 浏览身份的资料。

---

## Meta 的 Muse 智能体：你的网站能看到什么、看不到什么

Meta 于 9 月 8 日[发布了 Muse](https://www.pbs.org/newshour/nation/meta-launches-personal-ai-agent-muse-to-help-with-everyday-tasks)，这是一款面向美国成年人的个人智能体。人们在 Muse 应用或 WhatsApp 中给它发消息，Meta 称它能「打开浏览器、填写表单，并代他们协商」。Muse 与 Muse Spark 不是一回事，后者是 WhatsApp、Instagram、Facebook 和 Messenger 中 Meta AI 背后的模型。

Meta [已经描述过](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)该智能体如何浏览。它在一个虚拟机中运行「一个真实的、最新的基于 Chromium 的浏览器」，读取页面的部分则基于「页面的无障碍树（accessibility tree）快照」工作。关于身份，Meta 表示：「当 Muse 浏览互联网时，它会显示为你的活动。」对你的网站来说，一次 Muse 访问看起来可能就像你的顾客。

## Meta 已公开的关于识别 Muse 的信息

截至 2026 年 11 月 1 日，Muse 没有用户代理（user agent）、IP 段或签名。Meta [面向网站主的页面](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)列出了五个爬虫（FacebookExternalHit、Meta-WebIndexer、Meta-ExternalAds、Meta-ExternalAgent 和 Meta-ExternalFetcher），Muse 不在其中。该页面没有提及签名请求。

我们能观察到的一点是：一个包含五把 Ed25519 密钥的文件已在 `meta.com/.well-known/http-message-signatures-directory` 上线，这是 Web Bot Auth 使用的地址。Meta 没有说明什么会用该文件签名，我们也没有观察到带签名的 Muse 请求。

网站方面则采取了两种做法。亚马逊在 9 月[屏蔽了 Muse](https://www.engadget.com/2263659/amazon-bars-metas-muse-ai-from-shopping-on-its-site/)，理由之一是 Muse 在浏览时不表明自己是 AI 智能体。沃尔玛是 Muse 公开点名的购物合作伙伴，但用户报告 Muse 在其结账环节失败，那里一个「证明你是人」的步骤把它挡在了门外。沃尔玛[告诉 TechCrunch](https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/)，这些拦截并非有意为之。

## 现在该做什么

如果你希望在 Meta AI 中被引用，请允许 Meta-WebIndexer。Meta 称它有助于「在 Meta AI 的回答中引用并链接到网站」。

如果你希望智能体完成购买或注册，请亲自走一遍该流程，找出会拦住自动化浏览器的人机校验。

给你的按钮和表单字段加上标签。Meta 表示其浏览器读取无障碍树，因此没有无障碍名称的控件能提供给它的信息就更少。

本页反映的是截至 2026 年 11 月 1 日阅读到的 Meta 已公开页面。
