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
translation: 待翻译
collectedAt: 2026-11-05
tags: [运行环境]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载。文末推广自家 fetchcheck 工具的两处（一段建议与一个链接）已去掉；副标题未收。Sitedex 是一家机器人检测服务商，本文是其面向网站主的指南。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：文章核对了 Meta 已公开的资料：Muse 在虚拟机里用一个真实的 Chromium 浏览器上网，读取页面靠无障碍树快照；Meta 称 Muse 上网时显示为用户本人的活动，因此网站看到的 Muse 访问可能像普通顾客。截至 11 月 1 日，Meta 没有为 Muse 公布用户代理、IP 段或签名；Meta 面向网站主的页面列出的 5 个爬虫里也没有 Muse，也未提及签名请求。但作者发现 `meta.com/.well-known/http-message-signatures-directory` 上已有一个含 5 把 Ed25519 密钥的文件，这是 Web Bot Auth 使用的地址，Meta 未说明由什么签名，作者也未观察到带签名的 Muse 请求。文中还提到亚马逊 9 月屏蔽 Muse 的原因之一是不亮明智能体身份，以及沃尔玛结账时的人机验证曾拦住 Muse，沃尔玛对 TechCrunch 称并非有意屏蔽。

**保留理由**：独立核查了 Meta 面向网站主的爬虫清单与 Web Bot Auth 密钥目录，给出 Muse 在网站侧可识别性的实测结论，是已收资料中唯一从网站主角度讨论 Muse 浏览身份的资料。
