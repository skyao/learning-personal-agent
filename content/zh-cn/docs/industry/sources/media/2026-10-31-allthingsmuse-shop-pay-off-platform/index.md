---
title: "Shop Pay 结账进入 Muse，覆盖 Shopify 之外的商店"
linkTitle: "Shop Pay 进 Muse"
date: 2026-10-31
originalTitle: "Shop Pay Now Checks Out Inside Muse, Including at Stores Outside Shopify"
sourceUrl: "https://www.allthingsmuse.com/articles/shopify-shop-pay-ai-agents-off-platform/"
author: "Icarus"
publisher: "All Things Muse"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-12
tags: [连接器, 商业与规模]
products: [muse, claude-duet, grok-bot, instinct]
dateNote: "元数据 published_time 为 2026-11-01T00:19:00Z（美东 10 月 31 日 20:19），页面显示日期为 10 月 31 日，date 取 10 月 31 日"
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图 Jolly 插画与站内「Earlier coverage」推荐卡片。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Shopify 在 10 月 28 日发布的 Fall '26 版中把 Shop Pay 结账放进包括 Muse 在内的个人智能体，结账首次覆盖非 Shopify 商店，店外支付走卡组织 token，店外商家无需改动结账流程即可接入（据 The Defiant 的报道）。首批智能体为 Muse、Claude Duet、Grok Bot 与 Instinct，店外支付使用 Visa、Mastercard 与 Discover 的卡组织 token，American Express 列为即将推出。这是对 Shopify 与 Meta 9 月合作的延伸，当时 Muse 已可在 Shopify 商店内用 Shop Pay 结账，此次把同一结账方式扩展到 Shopify 店面之外。结账流程保留在智能体对话内，买家每次购买需点按允许或拒绝，Shopify 称买家的卡号不会透露给智能体，并称已有超过 4 亿人信任 Shop Pay。同期推出的 Shop.md 技能可让智能体搜索超过 10 亿件商品、用 Shop Pay 结账并跟踪订单，Shopify 的智能体连接器现已支持包括 ChatGPT、Claude、微软 Copilot、谷歌 Gemini 与 Perplexity 在内的九个智能体。

**保留理由**：提供了 Shop Pay 首次走出 Shopify 平台进入 Muse 等智能体的出处，并列出首批四个智能体与三家已支持的卡组织，是已收资料中关于 Muse 购物闭环扩展到店外商家的直接证据。

---

Shopify 的 Fall '26 版本把 Shop Pay 结账放进了 Muse 等个人智能体，并用卡组织 token 向 Shopify 之外的商店付款，而不共享……

Shopify 已将 Shop Pay 结账扩展到包括 Meta 的 Muse 在内的个人 AI 智能体，而且结账首次覆盖 Shopify 并不驱动的商店。该公司于 10 月 28 日在其 Fall '26 Edition 中宣布了这一变化，[The Defiant 报道](https://thedefiant.io/converge/tradfi-and-fintech/shopify-takes-shop-pay-into-ai-agents-and-off-platform-checkouts)称，智能体现在可以使用一次性卡凭证在外部商店付款，而那些零售商无需添加新的集成。

据 The Defiant 报道，首批上线的智能体是 Muse、Claude Duet、Grok Bot 和 Instinct。对于来自 Shopify 平台之外商家的购买，付款使用 Visa、Mastercard 和 Discover 的卡组织 token。据 [Let's Data Science](https://letsdatascience.com/news/shopify-extends-shop-pay-to-ai-agents-with-card-network-toke-4384d341) 报道，American Express 在 Shopify 的发布材料中被列为即将支持。

对 Muse 用户来说，实际的变化在于智能体能在哪里完成购买。Shopify 和 Meta [在 9 月宣布了一项合作](https://www.allthingsmuse.com/articles/shopify-muse-shop-pay-checkout/)，让 Muse 能在 Shopify 驱动的商店用 Shop Pay 结账。这次发布把同一种结账扩展到 Shopify 自己的店面之外，因此智能体在别处找到的商品仍然可以通过 Shop Pay 结算。

## 在对话里结账是怎么运作的

整个流程留在智能体对话内。Shopify 的示例界面展示了 Muse 内部一台意式咖啡机的 Shop Pay 结账，带有供买家使用的「允许」和「拒绝」按钮。买家批准每一次购买，Shopify 称买家的卡号绝不会与智能体共享。Shopify 还表示，已有超过 4 亿人信任 Shop Pay。

token 的安排正是让平台外触达成为可能的原因。Shopify 不是把卡号交给智能体，而是把支付 token 化，因此智能体是在 token 的规则范围内花钱，而不是持有卡号。据 The Defiant 的报道，Shopify 之外的零售商无需改动结账流程即可被触达。

这次发布还增加了其他面向智能体的东西。Shop.md 是一个技能，让智能体搜索超过 10 亿件商品、用 Shop Pay 结账并追踪订单。面向智能体的 Shopify 连接器现在可与九个智能体配合，包括 ChatGPT、Claude、Microsoft Copilot、Google Gemini 和 Perplexity，商家可以在对话内管理商品、库存、订单和业绩。

## 为什么这对 Muse 用户重要

这一公告正值大公司之间在购物智能体问题上出现分裂之际。亚马逊在 9 月封锁了 Muse，JPMorgan 也已采取行动封锁智能体，而 Shopify 走的是相反方向，把结账放进竞争对手的智能体里。这一变化对 Muse 用户很实际：智能体的购物触达不再止于 Shopify 平台的边缘，而审批环节在付款那一刻仍留在买家手里。
