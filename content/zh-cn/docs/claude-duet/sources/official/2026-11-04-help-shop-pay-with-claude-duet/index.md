---
title: "如何在 Claude Duet 中使用 Shop Pay"
linkTitle: "帮助：Shop Pay 付款"
date: 2026-11-04
originalTitle: "How to use Shop Pay with Claude Duet"
sourceUrl: "https://support.claude.com/en/articles/17666489-how-to-use-shop-pay-with-claude-duet"
author: "未署名"
publisher: "Anthropic"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "帮助文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-04T20:42:36Z）"
tags: [安全, 连接器]
products: [claude-duet]
---

{{< source-info >}}

**收录说明**：直接下载。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文档说明如何把 Shopify 的钱包 Shop Pay 连接到 Claude Duet 并用它付款，结构与 Link 一文相同。Shop Pay 只在 Claude Duet 中可用，面向美国的 Pro、Max 和 Ultra 套餐，与让 Claude 操作 Shopify 店铺的 Shopify 连接器是两回事；在 Claude Duet 的头像菜单中连接，移动端也可从推荐连接器列表中选择。每次购买前都会询问，每笔购买使用一次性卡，Claude Duet 只能看到付款方式的后四位、有效期和账单地址。

**保留理由**：与 Link 一文共同说明 Claude Duet 的第二种支付渠道，可对照两种钱包在条件和流程上的差异。

---

连接 Shop Pay——Shopify 的钱包——到 Claude Duet，让它能为你批准的购买付款。

Shop Pay 可在 Claude Duet 中使用，后者是面向美国 Pro、Max 和 Ultra 套餐的研究预览（research preview）。它目前不在 Claude、Cowork 或 Claude Code 中提供。

Shop Pay 与 Shopify 连接器是分开的，后者让 Claude 在你的 Shopify 店铺中工作。你可以只用其中一个而不用另一个。

## 你可以做什么

- **批准每一笔购买。** Claude Duet 被设计为在每次购买前询问。
- **用一次性卡（one-time card）付款。** 每次购买都使用一张仅对该次购买有效的一次性卡。

## 如何连接

Shop Pay 没有列在连接器目录中。你需要在 Claude Duet 中连接它。

1. 在 Claude Duet 中选择你的头像。
2. 选择连接支付的选项，然后选择 Shop Pay；在移动端也可以从推荐连接器列表中选择。
3. 登录你的 Shop Pay 账号并批准访问。

当你请求需要付款的东西时，Claude Duet 也会建议连接 Shop Pay。

Claude Duet 可以看到你已保存的付款方式的后四位和有效期，以及你的账单地址。它无权访问你完整的银行卡号或银行账号。

## 如何用 Shop Pay 付款

1. 向 Claude Duet 提出你需要什么，例如「再订一些寄件标签，和上次一样。」
2. Claude Duet 找到商品，并请你批准购买。
3. 点击「Review in Shop Pay」（在 Shop Pay 中查看），然后批准购买。
4. Claude Duet 使用一张限定于已批准金额的一次性卡，通过 Shop Pay 付款。

## 当前局限

- Shop Pay 仅在 Claude Duet 中提供，面向美国的 Pro、Max 和 Ultra 套餐。
- 某些网站可以阻止 Claude Duet 付款。如果发生这种情况，你可能需要自己完成购买。

## 常见问题

### Claude Duet 可以不问我就买东西吗？

不可以，Claude Duet 被设计为在每次购买前询问。

### 为什么我在连接器目录中找不到 Shop Pay？

Shop Pay 内置于 Claude Duet，因此你要在那里连接它。

### Shop Pay 和 Shopify 连接器是一回事吗？

不是。Shopify 连接器让 Claude 在你的 Shopify 店铺中工作，例如管理商品和订单。Shop Pay 为购买付款。你需要分别连接它们。

### 关于扣款、退款或购买问题，我应该联系谁？

你购买商品的商店负责处理退款、退货和订单问题。请直接联系该商店。关于你的 Shop Pay 账号或扣款的问题，请联系 **[Shop 支持](https://help.shop.app/en/shop/report-issue/contact-the-shop-support-team)**。关于 Claude Duet 本身的问题，在对话中告诉 Claude Duet 发生了什么，它会把你的报告转达给我们的团队。

### 如何断开 Shop Pay？

1. 在 Claude Duet 中，选择你的 Claude Duet 头像。
2. 选择 payments（支付），然后选择 Shop Pay。
3. 选择「Disconnect」（断开连接）。
