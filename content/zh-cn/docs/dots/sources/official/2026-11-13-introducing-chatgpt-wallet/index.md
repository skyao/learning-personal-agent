---
title: "推出 ChatGPT Wallet"
linkTitle: "推出 ChatGPT Wallet"
date: 2026-11-13
originalTitle: "Introducing ChatGPT Wallet"
sourceUrl: "https://openai.com/index/introducing-chatgpt-wallet/"
reprintUrl: "https://web.archive.org/web/20261117093639/https://openai.com/index/introducing-chatgpt-wallet/"
author: "OpenAI"
publisher: "OpenAI"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "openai.com 对自动访问返回 403，依据 Internet Archive 2026-11-17 09:36:39（UTC）的快照"
tags: [发布, 安全, 开放与价格, 商业与规模]
products: [dots]
---

{{< source-info >}}

**收录说明**：openai.com 对直接下载返回 403，依据 Wayback 快照抽取全文。页首的栏目链接、文末的标签和「Keep reading」推荐未收入；页首视频只保留 Vimeo 链接，删去了外链后的「(opens in a new window)」提示，站内相对链接改为绝对地址。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：OpenAI 于 2026-11-13 推出 ChatGPT Wallet，称它是第一个让智能体付款时接触不到用户真实卡片信息、且每笔购买都要做安全验证的钱包，与 American Express、Chase、Mastercard、Visa 合作打造。用户添加一次卡片，每次购买前核对商品、总价和所选卡片，再用 Face ID 或指纹批准；批准后由支付网络提供支付令牌（含卡号、安全码、有效期）代替真实卡片信息，卡片原有的积分和争议保护不变。OpenAI 同时发布 Commerce Partner Playbook，建议商家用 Web Bot Auth 识别带签名的智能体请求、与风控和支付服务商协作（列出 Forter、Riskified、Sardine、Signifyd、Adyen、Checkout.com、Stripe），并通过插件或 WebMCP 工具接入。Wallet 当天开始在 dots 中推出，先面向美国 18 岁以上、持有符合条件的美国发行卡片的 ChatGPT Pro 订阅用户；OpenAI 预计以后用户可以设定消费上限、品类或时间段，让智能体预先获批完成购买。

**保留理由**：这是 dots 代用户付款的官方发布文，写明了支付令牌、逐笔生物识别批准、发卡和支付网络合作方、首批开放范围，以及对商家网站的接入要求。

---

2026 年 11 月 13 日

推出 ChatGPT Wallet

与支付网络、银行和商家一起构建可信的智能体支付。

[视频：推出 ChatGPT Wallet](https://player.vimeo.com/video/1246467101?h=c0fe6f20de)

我们推出 ChatGPT Wallet，为智能体安全支付树立新标杆。这是第一个让智能体在无法接触用户实际卡片信息的情况下付款、且每笔购买都要求安全验证的钱包，同时为符合条件的争议保留原有的卡片奖励和保护。ChatGPT Wallet 与 American Express、Chase、Mastercard 和 Visa 合作打造，初期将通过 [dots](https://openai.com/index/introducing-dots/) 向美国的 ChatGPT Pro 订阅用户提供。伴随 ChatGPT Wallet，我们还发布工具和指南，帮助企业服务使用智能体的客户。

每周有 12 亿人使用 ChatGPT，其中许多人用它研究产品、比较选项、决定买什么。有了 ChatGPT Wallet，我们现在帮助人们完成购买，并为他们的智能体提供一种商家可以用现有系统接受的付款方式。

要接受来自 ChatGPT Wallet 的付款，网站需要确保智能体不会被无意中拦截，支付和风控系统也需要能识别智能体发起的合法购买。我们先向 ChatGPT Pro 用户限量开放，以便从真实使用中学习，并与商家、银行和支付网络合作，改善兼容性和可靠性。

## 一次购买如何完成

ChatGPT Wallet 为智能体提供安全的代付方式。用户添加一次卡片，之后批准每笔购买时无需重新输入支付信息。

每笔购买前，用户查看商品、总价和所选卡片，然后通过 Face ID 或指纹扫描等安全检查批准。每次批准都会形成一条清晰记录，说明用户授权智能体进行了哪笔购买。

用户批准后，支付网络提供一个支付令牌——用户实际卡片信息的替代品——包含卡号、安全码和有效期。款项记到用户所选卡片上，而 ChatGPT Wallet 不会把用户的实际卡片信息分享给商家或智能体。

我们正在让智能体主导的商业可靠地融入现有系统。用户在与商家的符合条件争议中（例如商品有缺陷时）保留卡片原有的奖励和保护。银行和支付网络贡献其专业能力来评估交易。用户直接与商家交易，商家保留客户关系，并掌控定价、履约、退货和客户服务。

随着时间推移，我们预计用户将能够通过设定明确的参数——例如消费上限、购买品类或时间段——把购买完全委托给智能体，并用在现有保护基础上增强的保障措施预先批准这些购买，包括生物识别检查和清晰的授权记录。

1 of 3

> 「与 OpenAI 合作，我们正在把 American Express 支付的信任、安全和掌控带入新的 AI 驱动购物体验。ChatGPT Wallet 是我们首个 American Express 智能体式商业体验集成，让符合条件的卡会员在查看并批准每笔购买的同时使用其 Amex 卡。我们很高兴在这一早期阶段共同学习，并逐步把这些体验带给更多卡会员。」

——**Luke Gebb**，American Express 全球创新执行副总裁兼主管

> 「智能体进行购买，应当加强而不是绕过支付中固有的信任。我们与 OpenAI 的合作把 Mastercard 的支付和安全专业能力带入 ChatGPT Wallet，帮助把用户批准的购买与商家和银行已在使用的系统连接起来。全行业共同努力，才能把智能体式商业的承诺变成人们和商家都能信任的体验。」

——**Sherri Haymond**，Mastercard 全球数字商业化执行副总裁兼主管

> 「要实现智能体式商业的承诺，消费者、商家和银行都需要信任整个过程。我们正与 OpenAI 合作，把 Visa 可信的基础设施带入这一体验，帮助把用户批准的购买与商家已在使用的系统连接起来。」

——**Rubail Birwadker**，Visa 全球增长主管

- American Express
- Mastercard
- Visa

## 让商家为智能体式商业做好准备

智能体式商业仍处于早期。随着智能体开始承担更多购物和购买任务，许多网站和支付系统仍在适应这种模式。一些网站可能会无意中拦截通过 ChatGPT Wallet 或其他智能体支付产品进行的购买，我们正专注于帮助商家完成这一过渡。

伴随 ChatGPT Wallet，我们发布 [Commerce Partner Playbook](https://developers.openai.com/commerce)，提供工具和实用指南，帮助商家通过其现有网站和系统服务使用智能体的客户。它涵盖提供商品信息、确保智能体访问，以及与支付和风控服务商合作减少不必要的拒付。商家可以从与其客户最相关的方面开始：

- **帮助客户找到准确的商品信息。** [在 ChatGPT 中认领你的商家](https://openai.com/index/introducing-businesses-chatgpt/)，验证后更新商家详情，并上传包含当前价格和库存的商品数据源。
- **确保 ChatGPT 智能体可以访问你的网站。** 配置你的 CDN 或防火墙，使其能识别使用 Web Bot Auth 的带签名请求，并确认你的一般站点安全措施没有无意中拦截 ChatGPT 智能体。浏览器访问不需要插件或商品数据源。
- **与你的支付和风控服务商合作，支持智能体购买。** Wallet 的支付令牌适用于现有结账流程，但风控系统仍可能把智能体发起的合法购买标记为可疑，导致拒付或取消。你可以与服务商合作，了解他们如何识别这些交易。我们也在与 Forter、Riskified、Sardine 和 Signifyd 等防欺诈合作伙伴，以及 Adyen、Checkout.com 和 Stripe 等支付服务商合作，帮助他们的系统识别智能体发起的合法购买。
- **为智能体提供更多与你商家打交道的方式。** 构建插件，让智能体通过你现有的系统查询库存、管理购物车或执行其他操作。网站也可以添加 WebMCP 工具。

## 可用范围

ChatGPT Wallet 从今天起在 dots 中推出，让用户可以让自己的 dot 代为完成购买。初期面向美国年满 18 岁、持有符合条件的美国发行卡片的 ChatGPT Pro 订阅用户。我们将与商家、银行和支付网络合作，从早期使用中学习并扩大可用范围，让更多客户和商家从智能体式商业中受益。
