---
title: "如何在 Claude Duet 中使用 Link by Stripe"
linkTitle: "帮助：Link 付款"
date: 2026-11-04
originalTitle: "How to use Link by Stripe with Claude Duet"
sourceUrl: "https://support.claude.com/en/articles/17666484-how-to-use-link-by-stripe-with-claude-duet"
author: "未署名"
publisher: "Anthropic"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "帮助文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-04T20:42:32Z）"
tags: [安全, 连接器]
products: [claude-duet]
---

{{< source-info >}}

**收录说明**：直接下载。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文档说明如何把 Stripe 的数字钱包 Link 连接到 Claude Duet 并用它付款。Link 只在 Claude Duet 中可用（Claude、Cowork、Claude Code 中不可用），要求美国的 Pro、Max 或 Ultra 套餐和美国的付款方式，与让 Claude 操作 Stripe 账户的 Stripe 连接器是两回事。连接在 Claude Duet 的头像菜单中完成，不在连接器目录里。每次购买前 Claude Duet 都会询问，用户批准最高金额前不会提交付款，每笔购买使用只对该笔有效的一次性卡；Claude Duet 能看到已保存付款方式的后四位、有效期和账单地址，看不到完整卡号。文档还说明了订单、扣款、选错商品等问题分别找谁处理。

**保留理由**：说明了 Claude Duet 代付款的具体机制（一次性卡、最高金额批准、可见的支付信息范围），是分析其支付设计的一手资料。

---

连接 Link——Stripe 的数字钱包——到 Claude Duet，让它能为你批准的购买付款。

Link 可在 Claude Duet 中使用；Claude Duet 是面向美国 Pro、Max 和 Ultra 套餐（需使用美国付款方式）的研究预览。目前它无法在 Claude、Cowork 或 Claude Code 中使用。

Link 与 Stripe 连接器是两回事，后者让 Claude 在你的 Stripe 账户中工作。你可以只用其中一个，而不用另一个。

## 你可以做什么

- **批准每一笔购买。** Claude Duet 的设计是在每次购买前询问你，并且在你批准最高金额之前不提交 Link 付款。你批准时，Link 可能会在你选定的付款方式上放置一笔临时授权。只有商家完成购买后，最终扣款才会完成。
- **使用一次性卡付款。** 每笔购买都使用一张只对该笔购买有效的一次性卡。

## 如何连接

Link 不会列在连接器目录中。你需要在 Claude Duet 中连接它。

1. 在 Claude Duet 中选择你的头像。
2. 选择连接付款的选项，然后选择 Link。
3. 登录你的 Link 账户并批准访问。

当你请求某件需要付款的事情时，Claude Duet 也会建议连接 Link。

Claude Duet 可以看到你已保存付款方式的最后四位数字和有效期，以及你的账单地址。它无权访问你的完整卡号或银行账号。

## 如何使用 Link 付款

1. 向 Claude Duet 提出你的需求，例如「为办公室打印机重新订购墨水」。
2. Claude Duet 找到商品，并请你批准购买。
3. 使用 Link 移动应用或 app.link.com 创建或登录你的 Link 账户，然后批准你的消费请求（Spend Request）。
4. Claude Duet 使用一张限定商家和金额的一次性卡付款。

## 当前限制

- Link 仅在 Claude Duet 中可用，且仅限美国的 Pro、Max 和 Ultra 套餐。
- 需要美国的付款方式。
- 在你于 Link 应用中批准金额之前，Claude Duet 无法使用 Link 付款。
- 在你批准消费请求后，商家仍可能拒绝或阻止结账。
- 失败的购买可能会在所选资金来源上暂时显示为待处理。
- Claude Duet 无法使用 Link 进行定期付款。
- 有些网站会阻止 Claude Duet 付款。如果发生这种情况，你可能需要自己完成购买。

---

## 常见问题

### Claude Duet 可以在不询问我的情况下买东西吗？

Claude Duet 的设计是在每次购买前询问，并且在你于 Link 应用中批准金额之前，它无法使用 Link 付款。

### 为什么我在连接器目录中找不到 Link？

Link 内置于 Claude Duet，因此你要在那里连接它。

### Link 和 Stripe 连接器是一回事吗？

不是。Stripe 连接器让 Claude 在你的 Stripe 账户中工作，例如检查未付发票。Link 为购买付款。你需要分别连接它们。

### 关于扣款、退款或购买问题，我应该联系谁？

- 有关订单状态、配送、取消、退货、损坏或错误商品以及商品退款，请联系商店。
- 有关 Link 账户问题、批准问题、付款方式问题、重复或错误的付款金额、无法识别的 Link 付款，或失败购买后仍处于待处理状态的付款授权，请联系 **[Link Support](https://support.link.com/topics/link-agent-wallet)**。
- 如果 Claude Duet 选择的商品、商店、数量或选项与你要求的不同，或者 Claude Duet 本身没有正常工作，请联系**[我们的支持团队](https://support.claude.com/en/articles/9015913-how-to-get-support)**。你可以直接在聊天中告诉 Claude Duet 发生了什么，它会将你的报告转交给我们团队。
- 如果你不认识某笔购买，请拒绝任何待处理的批准请求，断开 Claude Duet 与 Link 的连接，并尽快联系 Link Support。

### 如何断开 Link？

1. 在 Claude Duet 中，选择你的 Claude Duet 头像。
2. 选择付款，然后选择 Link。
3. 选择「断开连接」。
