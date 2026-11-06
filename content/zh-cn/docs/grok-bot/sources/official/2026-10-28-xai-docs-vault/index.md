---
title: "文档（docs.x.ai）：Vault 与安全登录"
linkTitle: "docs.x.ai：Vault 与安全登录"
date: 2026-10-28
originalTitle: "Vault and secure sign-in"
sourceUrl: "https://docs.x.ai/grok-bot/vault"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「Secrets」讲到的密钥管理与这页约一半重合，这页另讲 Vault 的登录、卡和付款。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Vault 存放登录信息、银行卡和联系信息，Bot 看不到密码、卡号和安全码，只能看到联系信息和登录条目的列表；Vault 全账号共享，不能只给某个 Bot。可以从 1Password、Chrome、Safari、Bitwarden 等导出的 CSV 导入，文件只在本机读取。存在 Vault 里的卡会在结账时自动填入，没有「每次批准」的设置；想逐笔批准就不要存卡。也可以连接 Link 或 X Money 作为付款账户，Link 付款会弹出一次性卡，显示商家、商品和总额，由用户选择付款、换方式或拒绝。

**保留理由**：官方对凭证与付款隔离的具体设计：模型看不到密码和卡号，但存卡后付款不再逐笔确认，这一点值得留意。
