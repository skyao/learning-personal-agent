---
title: "沃尔玛让 Meta 的 Muse 逛它的货架——但按它的规矩来"
linkTitle: "沃尔玛与 Muse 的规矩"
date: 2026-11-24
originalTitle: "Walmart is letting Meta's Muse shop its shelves — but on its own terms"
sourceUrl: "https://digiday.com/marketing/walmart-is-letting-metas-muse-shop-its-shelves-but-on-its-own-terms/"
author: "Krystal Scanlon"
publisher: "Digiday"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-24
tags: [连接器, 商业与规模]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载后用 extract.py 抽取；删去页首活动推广、分享按钮与文末推荐/热读栏目；首图为 2024 年沃尔玛资料照片、装饰图，未收。原文全文存于本目录 original.md，网站上不显示，已翻译。

**内容摘要**：电子商务研究公司 Marketplace Pulse 的创始人 Juozas Kaziukėnas 注意到沃尔玛为 Muse 更新的技术说明手册后，Digiday 也查看并核实了该手册；据 The Verge 报道，该整合将于 11 月 24 日上线，赶上黑五网一购物季。手册称 Muse 可代用户搜索商品、回答问题、建立购物车，并在获得许可后完成订单，还可调用沃尔玛自家的购物助手 Sparky 回答有关商品、门店与比价的问题。该整合基于模型上下文协议（MCP），让智能体以更直接可靠的方式与沃尔玛的购物系统交互，沃尔玛可在不交出用户完整购物记录的情况下帮助 Muse 识别用户的常用品牌。沃尔玛还推出了 Agent Profiles，每个 AI 智能体在用户沃尔玛账户内拥有专属档案，购物者可区分智能体购买与自己购买，用户可要求每次购买都审批，或设定 50、100 或 200 美元等消费上限，并可随时关闭智能体的访问权限。亚马逊已于 9 月阻止 Muse 访问其电商网站，称第三方 AI 智能体应公开运作并尊重零售商是否参与的决定，Meta 则否认了有关 Muse 能看到用户密码或支付信息的说法；沃尔玛与 Meta 均未回应 Digiday 的置评请求。

**保留理由**：以沃尔玛技术说明手册为依据，写明了 Muse 与沃尔玛购物系统的交互方式与 MCP 基础，并记录了亚马逊阻止 Muse 与沃尔玛开放网关的对照，是已收核查记录之外的媒体报道视角。

---

沃尔玛让 Meta 的 Muse 逛它的货架——但按它的规矩来

文：[Krystal Scanlon](https://digiday.com/author/krystal/)  •  2026 年 11 月 24 日  •

- [Facebook](https://www.facebook.com/dialog/share?app_id=610029874501691&display=popup&href=https%3A%2F%2Fdigiday.com%2Fmarketing%2Fwalmart-is-letting-metas-muse-shop-its-shelves-but-on-its-own-terms%2F%3Futm_medium%3Dsocial%26utm_campaign%3Ddigidaysiteshare&utm_source=facebook&redirect_uri= "Share in Facebook")
- [Twitter](https://twitter.com/intent/tweet?url=https%3A%2F%2Fdigiday.com%2Fmarketing%2Fwalmart-is-letting-metas-muse-shop-its-shelves-but-on-its-own-terms%2F%3Futm_medium%3Dsocial%26utm_campaign%3Ddigidaysiteshare%26utm_source%3Dtwitter&text=Walmart%20is%20letting%20Meta%E2%80%99s%20Muse%20shop%20its%20shelves%20%E2%80%94%20but%20on%20its%20own%20terms "Share in Twitter")
- [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdigiday.com%2Fmarketing%2Fwalmart-is-letting-metas-muse-shop-its-shelves-but-on-its-own-terms%2F%3Futm_medium%3Dsocial%26utm_campaign%3Ddigidaysiteshare%26utm_source%3Dlinkedin&title=Walmart%20is%20letting%20Meta%E2%80%99s%20Muse%20shop%20its%20shelves%20%E2%80%94%20but%20on%20its%20own%20terms "Share in LinkedIn")
- [Reddit](http://www.reddit.com/submit?url=https%3A%2F%2Fdigiday.com%2Fmarketing%2Fwalmart-is-letting-metas-muse-shop-its-shelves-but-on-its-own-terms%2F%3Futm_medium%3Dsocial%26utm_campaign%3Ddigidaysiteshare%26utm_source%3Dreddit&title=Walmart%20is%20letting%20Meta%E2%80%99s%20Muse%20shop%20its%20shelves%20%E2%80%94%20but%20on%20its%20own%20terms "Share in Reddit")

Ivy Liu

沃尔玛只让 Meta 的 Muse 智能体通过它自建并控制的网关进入其商店，这种对待 AI 智能体访问的方式，就像零售媒体网络当年对待广告位：把它当作可以按自己的条件分配的库存。

这家零售商正准备推出一个连接 Muse 的连接器，为这个 AI 智能体提供对其电商基础设施的限定访问，也就是说，由沃尔玛设定 Meta 的智能体可以浏览和购物的护栏与边界。

电商研究公司 Marketplace Pulse 的创始人 Juozas Kaziukėnas 注意到沃尔玛为 Muse 更新的技术说明手册后发现了这一能力。据 [The Verge](https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday)，该整合将于明天（11 月 24 日）上线，赶上黑五网一购物季。

Digiday 也查看并核实了这份手册，它描述了 Muse 如何代用户与沃尔玛的购物系统交互。这包括搜索商品、回答问题、建立购物车，以及在获得许可后完成订单等任务。Muse 还可以调用沃尔玛自家的购物助手 Sparky 来回答有关商品、门店与比价的问题。

因此，沃尔玛的购物者可以让 Muse 比较三台电视、为晚宴找到特定食材，或让智能体把商品加入其沃尔玛购物车。Muse 随后可以使用沃尔玛的系统执行这些任务。例如，沃尔玛可以帮助 Muse 识别客户常用的牛奶品牌，而不交出他们的全部购物历史。

这超出了人们对聊天机器人的通常预期——用户可能只是请求推荐。相反，Muse 通过通往沃尔玛自有市场的网关，可以对这些推荐采取行动，处理购物涉及的跑腿工作，甚至在用户给出必要许可后完成购买。

沃尔玛上个月在它的[博客文章](https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers)中谈到了这一愿景。

该整合基于模型上下文协议（Model Context Protocol，MCP）构建，让 AI 智能体以更直接可靠的方式与沃尔玛的购物系统交互。它被设计为让智能体代客户购物，同时不让智能体访问客户更广泛的购买历史或不必要的个人信息。例如，沃尔玛可以帮助 Muse 识别客户常用的牛奶品牌，而不交出他们的全部购物历史。

## **沃尔玛希望智能体按它的规矩购物**

沃尔玛也开始引入 Agent Profiles，让每个 AI 智能体在客户的沃尔玛账户内拥有专属档案。这意味着购物者可以区分 AI 智能体进行的购买与自己完成的购买，同时决定愿意给智能体多少自主权。客户可以要求每次购买都审批，或设定一个消费上限（例如 50、100 或 200 美元），允许智能体在此金额内消费而无需每次都请求审批。客户还可以随时关闭智能体的访问权限。

这一进展之前，亚马逊已于 9 月阻止 Muse 访问其电商网站，主张第三方 AI 智能体应公开运作，并尊重零售商是否参与的决定。当时亚马逊表示已要求 Meta 将其网站从 Muse 的购物体验中移除，但 Meta 拒绝了。它还提出了对 Muse 未经授权访问客户账户、并可能获取客户凭证的担忧。不过 Meta 对这些说法提出异议，称 Muse 无法看到用户的密码或支付详情。

虽然沃尔玛今后可能与 Muse 更紧密地合作，但这种方式可能给它的广告业务带来问题。尤其是，随着 Muse 越来越多地被允许接管商品发现，它的赞助商品位将处于何地，品牌对 AI 智能体推荐什么又能有多少影响力？

「将会出现一种新的广告机制，品牌付钱不是为了赞助位，而是为了向智能体购买『赞助考量』，」All Star Elite 数字增长负责人 Abhishek Bora 说。「如果智能体接管了购买过程，一个产品更好、优惠更好的新品牌，在没有评论、使用或购买历史的情况下，如何被智能体考虑？」

沃尔玛与 Meta 均未回应 Digiday 的置评请求。
