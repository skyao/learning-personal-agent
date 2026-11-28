---
title: "文档（docs.x.ai）：Grok Bot 如何工作"
linkTitle: "docs.x.ai：工作原理"
date: 2026-11-23
originalTitle: "How Grok Bot Works"
sourceUrl: "https://docs.x.ai/grok-bot/how-grok-bot-works"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-23）"
tags: [记忆与上下文, 运行环境, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的文档现以 docs.x.ai（SpaceXSI Docs）为准，cursor.com 的文档地址已 308 跳转到这里。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：文档以一个请求「报名与去年相同的会议并报销」为例，按五步说明 Grok Bot 如何工作：从记忆取回上一年的票和用卡规则，在 Gmail 找收据，在云端电脑上用浏览器登录并付款（登录凭据依次来自 Vault、1Password、Secure Form），发邮件给财务前由 Auto Review 拦下询问，最后把费用记入 Google Drive 的表格并回报。每个 Bot 有自己的记忆（偏好、规则、带日期的工作日志），姓名和时区等少量信息在所有 Bot 之间共享；所有 Bot 共用同一台云端电脑，各有自己的屏幕。Bot 没有自己的账号或凭据，所做的一切以用户身份进行，但各 Bot 之间并不隔离。文末还说明主 Bot 与单一职责 Bot 的分工和一组最佳实践。

**保留理由**：从一个任务串起记忆、连接器、云端电脑、凭据、审批和安全边界，是已收文档中对整体运行机制最集中的说明，尤其交代了所有 Bot 共用电脑和登录态这一点。
