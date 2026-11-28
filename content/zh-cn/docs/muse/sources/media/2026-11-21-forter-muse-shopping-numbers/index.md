---
title: "Forter 实测：Muse 占智能体订单 52%，平均订单 220 美元"
linkTitle: "Muse 占智能体订单 52%"
date: 2026-11-21
originalTitle: "Meta's Muse shopping agent, by the numbers"
sourceUrl: "https://ai.forter.com/meta-muse-shopping"
author: "Forter Intelligence"
publisher: "Forter"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-26
tags: [商业与规模]
products: [muse]
updatedAt: 2026-11-25
dateNote: "活页数据指南：2026-11-21 发布、2026-11-25 更新，数据每日刷新；本页数字为 2026-11-26 取文时的快照（近 7 天为 11 月 19–25 日，90 天为 8 月 28 日–11 月 25 日）"
---

{{< source-info >}}

**收录说明**：直接下载全文；页面为每日刷新的活页数据指南，取文时更新日期为 2026-11-25，数字以取文快照为准；删去页眉栏目名与作者行，修正了抽取时粗体数字后丢失的空格；无图片。已收 CNBC 11 月 24 日购物报道（2026-11-24-cnbc-muse-instagram-ad-boost）的数据源头即 Forter 的这份实测，本页为一手数据页。

**内容摘要**：Forter 按其商户网络实测统计：近 7 天（2026 年 11 月 19–25 日）Muse 占智能体订单的 52%，90 天（8 月 28 日–11 月 25 日）占订单 46%、支出 43%，平均订单 220 美元，比全部智能体的 230 美元低 5%。Forter 自 9 月 21 日起检出 Muse 的订单，检出当周智能体订单环比增长 229%，到 90 天期末智能体订单量为首周的 10.6 倍。Muse 经商店自有页面结账（scraper 方式），这类结账占 90 天智能体订单的 70%；支付走 Link by Stripe 生成的一次性卡，商店看到的是新卡号。Muse 的订单 92% 落在北美；Meta 于 9 月 23 日宣布与零售商等合作，扎克伯格称 Meta 将从交易中收取少量费用。

**保留理由**：Forter 声明独立于 Meta，数据是其商户网络的实测订单而非 Meta 官方数字；已收资料里还没有这样一份独立第三方购物数据。

---

Meta 于 2026 年 9 月 8 日推出其个人 AI agent Muse，几周之内，它在 Forter 网络上下的订单就超过了任何其他 AI agent。以下是它在 Forter 全球商户网络上被独立测量到的购买量、花费额，以及在何处、以何种方式结账。

- **52%** 近 7 天（2026 年 11 月 19 日–11 月 25 日）的智能体订单占比
- **46%** 90 天（2026 年 8 月 28 日–11 月 25 日）的智能体订单占比，以及 43% 的智能体支出占比
- **229%** 智能体订单的月环比增幅，即 Forter 首次检出 Muse 的那一周（9 月 21 日）
- **220 美元** Muse 的平均订单金额，全部智能体为 230 美元

## Muse 是什么

Meta 把 Muse 描述为「一个个人 AI agent」，它「不只是回答问题，而是真的把活干了」。它运行在 Muse Secure VM 上——一台自带浏览器的专用安全电脑——可在 Muse 应用里或直接在 WhatsApp 中使用。它能打开浏览器、填写表单，并在购买前请求批准。付款时，它通过 Link by Stripe 结账，后者面向 agent 的钱包会生成一次性卡号，从而隐藏购物者的真实卡信息；Meta 表示 Shop Pay 即将支持。Muse 正在美国陆续上线，覆盖 iOS、Android 和 muse.ai，人们所需的大部分功能免费，更多功能需订阅方案（[Meta，2026 年 9 月 8 日](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)）。

## Muse 买了多少

近 7 天（2026 年 11 月 19 日–11 月 25 日），Muse 下了 Forter 网络上 52% 的智能体订单，超过任何其他 agent。

在最近 90 天（2026 年 8 月 28 日–11 月 25 日）里，它下了 46% 的智能体订单、占 43% 的智能体支出，不过 Forter 自 9 月 21 日起才检出它的订单。

近 7 天全部 agent 的份额：Muse 52%、Grok 21%、ChatGPT 18%、Instinct 5%、ChatGPT Agent 2%、Google 2%。

从 11 月 23 日起，Forter 的[黑五与网一实时数据](https://ai.forter.com/peak-season)会显示 Muse 在本假日季智能体订单中的份额。

## Muse 效应

在 Forter 首次检出 Muse 的那一周，其网络上的智能体订单比一个月前增长了 229%。

到最近 90 天期末，智能体订单量达到其第一周水平的 10.6 倍（2026 年 8 月 28 日–11 月 25 日）。

## Muse 如何结账

Muse 是一个抓取型（scraper）agent：它加载商店自己的页面、填写表单并点击完成结账，和人一样，因此它能在没有集成的商店购物。这也让它同样受制于那些绊住人的东西——会变化的页面和令人困惑的表单——以及会质询每一个自动化浏览器的 bot 防护。

像它这样通过商店自有页面购物的 agent，在最近 90 天（2026 年 8 月 28 日–11 月 25 日）里下了 70% 的智能体订单。

## Muse 每单花多少

Muse 的平均订单为 220 美元，比全部智能体的 230 美元低 5%（2026 年 8 月 28 日–11 月 25 日）。

全部智能体按行业的平均订单：旅行 513 美元、实体商品 241 美元、数字商品 135 美元、外卖 120 美元。

## Muse 的订单来自哪里

Muse 的订单 92% 落在北美，全部智能体为 88%（2026 年 8 月 28 日–11 月 25 日）。

## 零售商与 Muse

Meta 于 9 月 23 日宣布与零售商及其他企业建立合作，Mark Zuckerberg 表示 Meta「将对交易收取少量费用」（[CNBC，2026 年 10 月 3 日](https://www.cnbc.com/2026/10/03/meta-muse-shopping-ai-agent.html)）。

## Muse 对你的商店意味着什么

- **Muse 通过你的页面购买，** 所以你的顾客所用的结账流程就是 Muse 所用的：让商品详情、价格和库存在页面上可读，并保持结账步骤可预期。
- **不要用 bot 规则把 Muse 的购物者挡在门外。** 对自动化浏览器一律质询会挡住替真实顾客行动的 agent；应当判断订单背后的身份与意图（[AI agent 欺诈](https://ai.forter.com/ai-agent-fraud)）。
- **预期看到新的卡号。** Muse 用 Link 的一次性卡付款，所以回头客的 agent 订单可能带着一张你没见过的卡。
- **检查你的商店。** 免费的 [AI 就绪检查](https://ai.forter.com/ai-readiness)会显示 agent 在哪里卡住。

## 问答

### Meta 的 Muse 是什么？

Muse 是 Meta 的个人 AI agent，于 2026 年 9 月 8 日推出。它在 Muse 应用或 WhatsApp 中工作，运行自己的安全浏览器，能填写表单并在请求批准后进行购买。

### Muse 能替你买东西吗？

能。在你批准购买后，Muse 会在商店自己的页面上结账，并用 Link by Stripe 付款，后者会生成一次性卡号。

### Muse 免费吗？

Meta 说，人们所需的大部分功能免费，想做更多事的人可以订阅付费方案。

### Muse 下多少网购订单？

近 7 天（2026 年 11 月 19 日–11 月 25 日），Muse 下了 Forter 网络上 52% 的智能体订单。

### 商店如何区分 Muse 和恶意 bot？

看订单背后是谁，而不是看下单的浏览器：Muse 替真实购物者行动，其身份、支付与历史可以像任何其他顾客一样被评判。一概封禁自动化浏览器，也会把 Muse 的购物者挡在外面。

## 关于数据

Forter 网络识别为由 AI agent 下的订单，在 Forter 全球商户网络中聚合、匿名化并每日刷新。除非某句写明是近 7 天，否则份额指最近 90 天数据（2026 年 8 月 28 日–11 月 25 日）内的智能体订单份额或智能体支出份额；订单金额以美元计。

协议型 agent（ChatGPT 和 Google）通过商业协议结账，按购物者来自哪里识别；抓取型 agent（Muse、Instinct、Grok 和 ChatGPT Agent）驱动商店自己的结账页面，按 agent 平台识别。ChatGPT Agent 与 ChatGPT 的协议结账分开统计，「全部智能体」对每笔智能体订单只计一次。Instinct 和 Grok 自 2026 年 9 月 1 日起统计，Muse 自 9 月 21 日起统计，即 Forter 开始可靠检出它们的那天，这可能晚于它们开始下单的时间；自第一周以来的增长包含了它们的加入。

Forter 独立于 Meta：这些是 Forter 对其网络上订单的测量，不是 Meta 的数字。

同样的数据可通过[公开 API](https://intelligence.forter.com/openapi.json) 免费获取 JSON，本页也有 [Markdown 版](https://ai.forter.com/meta-muse-shopping.md)。

## Muse 与其他所有 agent，实时

Muse 与协议型 agent 的对比、各 agent 的订单与支出份额，以及它们在哪里购物。

[Open Agentic Commerce](https://ai.forter.com/agentic-commerce)
