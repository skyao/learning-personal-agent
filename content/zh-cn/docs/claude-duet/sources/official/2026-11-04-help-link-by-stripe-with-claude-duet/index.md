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
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "帮助文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-04T20:42:32Z）"
tags: [安全, 连接器]
products: [claude-duet]
---

{{< source-info >}}

（收集说明：直接下载。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

## 收集者摘要

文档说明如何把 Stripe 的数字钱包 Link 连接到 Claude Duet 并用它付款。Link 只在 Claude Duet 中可用（Claude、Cowork、Claude Code 中不可用），要求美国的 Pro、Max 或 Ultra 套餐和美国的付款方式，与让 Claude 操作 Stripe 账户的 Stripe 连接器是两回事。连接在 Claude Duet 的头像菜单中完成，不在连接器目录里。每次购买前 Claude Duet 都会询问，用户批准最高金额前不会提交付款，每笔购买使用只对该笔有效的一次性卡；Claude Duet 能看到已保存付款方式的后四位、有效期和账单地址，看不到完整卡号。文档还说明了订单、扣款、选错商品等问题分别找谁处理。

## 保留理由

说明了 Claude Duet 代付款的具体机制（一次性卡、最高金额批准、可见的支付信息范围），是分析其支付设计的一手资料。
