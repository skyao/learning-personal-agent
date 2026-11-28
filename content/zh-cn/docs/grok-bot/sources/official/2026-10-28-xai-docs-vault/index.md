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
collectedAt: 2026-11-28
updatedAt: 2026-11-19
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：应用聊天中 Bot 能看到已存卡的号码和安全码；新增 Team Bot 自有登录、Shop Pay、一张订单卡批量最多 500 笔支付、iPhone 1.18.0 无法保存登录的问题"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「Secrets」讲到的密钥管理与这页约一半重合，这页另讲 Vault 的登录、卡和付款。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Vault 存放登录信息、银行卡和联系信息，Bot 看不到已存的密码，能看到联系信息和有哪些登录条目；在 Grok Bot 应用的聊天中，Bot 还能看到已存卡的号码和安全码，在用户点订单卡上的 Pay 之后填入结账。Vault 全账号共享，不能只给某个 Bot，也不适用于 Team Bots；Team Bot 的所有者或管理者可在 Bot's accounts 下为它添加专属登录，只有管理者能看到和修改。可导入 1Password、Chrome 或 Edge、Safari 或 Apple Passwords、Firefox、Bitwarden、LastPass 导出的 CSV（须小于 5 MB，文件只在本机读取）。存在 Vault 里的卡会在结账时自动填入，没有「每次批准」的设置；想逐笔批准就不要存卡。也可连接 Link、X Money 或 Shop Pay 作为付款账户，一张订单卡可批量覆盖最多 500 笔卡支付；Link 付款会弹出一次性卡，显示商家、商品和总额，由用户选择付款、换方式或拒绝。

**保留理由**：官方对凭证与付款隔离的具体设计：模型看不到密码，但应用聊天中能看到卡号和安全码，存卡后付款不再逐笔确认，这几点值得留意。
