---
title: "Poke 文档：创建 Recipe"
linkTitle: "创建 Recipe"
date: 2026-11-09
originalTitle: "Creating Recipes"
sourceUrl: "https://poke.com/docs/creating-recipes"
author: "未署名"
publisher: "The Interaction Company of California"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-09
tags: [连接器, 商业与规模]
products: [poke]
dateNote: "帮助文档页没有标注发布或更新日期，取收集日期（美东）"
---

{{< source-info >}}

**收录说明**：Poke 帮助文档，直接下载后抽取。待翻译。

**内容摘要**：Kitchen 是创建、发布和追踪自己 Poke recipe 的地方；一个 recipe 打包了引导上下文与首条消息行为、所需集成（MCP 模板）和分享/安装链接。向导中可设置名称、inputContext、prefilledFirstText，并选集成；支持本地凭证共享的集成可标记为共享，用户无需自行设置。已发布 recipe 的修改只影响新注册用户；发布后生成 referral 链接 poke.com/r/<referralCode> 并具备获得 payouts 的资格。页面还介绍 poke npm 包（需 Node.js 18+）的 login、mcp add、tunnel 与 --recipe 命令，tunnel 期间工具每 5 分钟自动同步，凭证存于 ~/.config/poke/credentials.json；Payouts 可查看唯一用户数与累计收益，收款目标为 Venmo。

**保留理由**：给出第三方开发者创建、分发 Recipe 并获得分成的机制与 CLI 细节，是 Poke 生态与商业模式的官方出处。
