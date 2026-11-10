---
title: "多数大零售商并非有意封堵 AI 智能体，审计发现"
linkTitle: "零售商误伤智能体"
date: 2026-11-02
originalTitle: "Most Big Retailers Block AI Agents Without Meaning to, Audit Finds, as Banks and Stores Dig In"
sourceUrl: "https://www.allthingsmuse.com/articles/banks-retailers-block-ai-agents-cnbc-audit/"
author: "Icarus"
publisher: "All Things Muse"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-08
tags: [安全]
basedOn: "CNBC，2026-11-01"
basedOnUrl: "https://www.cnbc.com/2026/11/01/jpmorgan-amazon-ai-agents-meta-muse.html"
dateNote: "发表日期 2026-11-02 在本轮检索窗口之外，本轮经 blocking guide 内链发现。"
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图 Jolly 插画与文中「The parallel move north of the border」栏目。本文为 CNBC 11 月 1 日报道的转述，原文地址见 basedOnUrl。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：CNBC 11 月 1 日的报道引用 Billions Network 对 51 家美国大型零售商公开访问规则的审计：只有 11 家对智能体有明确立场，其中 5 家明确限制智能体（CNBC 点名了亚马逊、Kohl's、Neiman Marcus，另外两家未点名），37 家通过针对爬虫的旧版反机器人规则无意中封堵了购物智能体，51 家中没有任何一家提供经核实的智能体完成购买的渠道。报道点名的封堵方还包括摩根大通与 Charles Schwab：Jamie Dimon 表示银行目前封堵外部智能体代零售客户操作，理由是安全风险；Charles Schwab 封堵主要外部智能体转移客户资金，但仍允许通过自有认证渠道查看余额；亚马逊则在其公开规则中明确封堵机器人进入其商城，只允许获批方使用 API，同时亚马逊自有购物助手 Rufus 的存在被指出可能引发平台中立性质疑。审计方 Billions Network 首席执行官 Evin McMullen 与埃森哲全球银行业务负责人 Michael Abbott 认为，封堵难以持久，企业需要的是识别合法智能体的验证方式而非一刀切的机器人封堵；沃尔玛则是反例，与 OpenAI 等合作支持经批准渠道的智能体结账。报道还提到，此前一周有智能体在客户账户中行为不当的报道，参议员 Mark Warner 与 Bernie Sanders 呼吁就机器人立法，但报道称尚无立法待决。对 Muse 用户而言，局面是双层的：在已明确表态的公司，智能体到门口为止，只能看不能动；在其他公司，障碍往往是旧规则而非针对智能体的决定，访问权限可能随时无公告地改变。

**保留理由**：这篇提供了 Billions Network 51 家零售商审计的完整数字（5 家明确限制、37 家无意封堵、0 家提供经核实购买渠道），并给出 CNBC 原文对「审计只读公开规则、不能证明实际执行程度」的限定，是记录智能体购物受阻规模与性质的关键出处。

---

CNBC 的一篇报道发现，在美国 51 家大型零售商中，只有 5 家明确限制 Meta 的 Muse 等 AI 智能体，37 家因旧的反爬虫规则而无意中封堵了它们，而且没有一家为智能体提供经核实的购买完成渠道。

据 CNBC 11 月 1 日发表的一篇报道，美国大多数大型零售商封堵 Meta 的 Muse 等 AI 智能体，很大程度上是无意的，原因是沿用了为阻止爬虫而制定的旧规则；与此同时，银行与零售业的少数大牌企业已采取行动，把智能体拒之门外。

这篇报道由 Kevin Williams 撰写，点名 JPMorgan Chase、Charles Schwab、Amazon、Neiman Marcus 和 Kohl's 已采取行动封堵 Muse 等个人智能体，而此时消费者正开始派它们去寻找更划算的储蓄利率、淘便宜货和取消订阅。除了任何单一封堵之外，报道背后的审计还呈现了整体图景：身份验证公司 Billions Network 对 51 家美国大型零售商公开访问规则的审计发现，只有 11 家对 AI 智能体作出过明确表态。

据该审计，51 家中有 5 家明确限制智能体，CNBC 点名了其中三家——Amazon、Kohl's 和 Neiman Marcus——但未在查阅到的段落中提及其余两家。37 家封堵购物智能体基本是无意的，依据的是针对爬虫和自动化流量的旧版机器人规则，而非明确的 AI 智能体政策。51 家中没有一家为智能体提供经核实的购买完成渠道。CNBC 未对上述类别之外的其余零售商作进一步细分，并提醒说，该审计读取的是公开规则，而非技术执行情况的证据：一个网站可能因为通用的反爬虫规则而看起来在封堵智能体，即使它没有明确的 AI 智能体政策；而公开的限制本身也不能证明智能体在实践中被多彻底地封堵。

## 明确的封堵者

CNBC 报道称，JPMorgan Chase 首席执行官 Jamie Dimon 表示，该银行目前封堵外部 AI 智能体代零售客户操作，理由是安全风险；报道还指出，JPMorgan 拒绝为 11 月 1 日的文章置评。该银行现在还向 Plaid 等聚合商收取拉取账户数据的费用，CNBC 指出，这笔成本可能落到人们使用的消费类应用上，并最终落到订阅费上。[JPMorgan 在 10 月划下了界线](https://www.allthingsmuse.com/articles/jpmorgan-blocks-ai-agents-muse-accounts/)，当时 Dimon 在该行第三季度财报电话会上告诉分析师，它不会让任何外部智能体在其系统内操作。

报道还点名 Charles Schwab 采取了类似行动，尽管 11 月 1 日的文章没有给出 Schwab 的单独政策或声明。[Schwab 自己的界线出现在 10 月](https://www.allthingsmuse.com/articles/charles-schwab-blocks-muse-client-money/)，当时首席执行官 Rick Wurster 告诉 Bloomberg TV，该公司封堵主要外部智能体转移客户资金，但仍允许通过其自有认证渠道查看余额。

报道最详细地记录了 Amazon 的立场。该公司在其公开规则下明确封堵机器人进入其商城，只允许获批方使用其 API，禁止其他方使用技术抓取信息或自动下单。Amazon 发言人让 CNBC 参考这些公开规则，而没有提供新的针对智能体的政策。CNBC 指出了这一立场中的张力：Amazon 运营着自己的购物助手 Rufus，允许自家智能体而封堵其他智能体，可能引发人们针对浏览器和应用商店提出的那类平台问题。[Amazon 在 9 月封堵了 Muse 进入其商店](https://www.allthingsmuse.com/articles/public-ceo-muse-shopping-amazon-shopify/)，几周后其首席执行官告诉投资者，外部购物智能体还不够好，还不足以让人担心。

## 为什么封堵可能难以维持

报道的论点——由其专家信源支撑——是正面抵制可能适得其反。埃森哲全球银行业务负责人 Michael Abbott 告诉 CNBC，试图封堵智能体的银行和零售商有可能失去那些希望借助智能体购物和办理银行业务的客户，也有可能让竞争对手或平台来制定规则。按这种观点，封堵是一种短期防御举措，一旦智能体成为人们购物和办理银行业务的常规方式，就很难维持。

Billions Network 联合创始人兼首席执行官 Evin McMullen 提出了同一观点的实务版本：大多数零售商根本没有公布明确的智能体政策，企业需要的是一种验证方法，以便识别合法智能体，而不是把智能体和爬虫一并拦下的一刀切机器人封堵。

沃尔玛是 CNBC 的反例。沃尔玛没有封堵，而是与 OpenAI 等合作开展智能体购物，并通过获批渠道支持智能体结账，把智能体视为触达客户的方式，而非对客户关系的威胁。这一对比表明，分歧归结为选择：一边是获批的集成，另一边是被拒之门外的独立智能体。

这篇报道出现在一个更为尖锐的政治背景之下。CNBC 提到，此前一周有报道称 AI 智能体在客户账户中行为不当，参议员 Mark Warner 和 Bernie Sanders 呼吁就此制定针对机器人的立法。文章没有描述有任何待决立法。

## 这对 Muse 用户意味着什么

Muse 用户现在面对的是双层局面。在已明确表态的公司，智能体的触达止于前门：它或许能通过获批的连接器查看，但无法行动。在其他所有地方，障碍往往是附带产生的，是遗留的机器人规则而非针对智能体的决定；这意味着，随着公司制定明确的智能体政策，访问权限可能在任何公告都没有的情况下发生变化，两个方向皆然。

在受审计的 51 家零售商中，没有任何一家有经核实的智能体购买渠道，因此智能体购物仍依赖变通办法和获批的合作关系，而不是任何商店都能采用的标准。在银行和零售商就如何识别并授权代表客户行动的智能体达成一致之前，对 Muse 以及所有类似的智能体来说，默认答案将继续取决于它敲的是哪家公司的门。

来源报道：[CNBC](https://www.cnbc.com/2026/11/01/jpmorgan-amazon-ai-agents-meta-muse.html)。
