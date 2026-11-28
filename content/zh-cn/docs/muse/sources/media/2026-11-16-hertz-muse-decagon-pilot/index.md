---
title: "Hertz 试点为 Muse 开通改签与续租直连通道"
linkTitle: "Hertz 改签续租试点"
date: 2026-11-16
originalTitle: "Hertz Pilots a Direct Line for Muse to Change and Extend Rental Reservations"
sourceUrl: "https://www.allthingsmuse.com/articles/hertz-muse-decagon-pilot/"
author: "Icarus"
publisher: "All Things Muse"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-20
tags: [连接器]
products: [muse]
dateNote: "页面显示 2026 年 11 月 16 日，元数据为 2026-11-17T04:20:00Z"
---

{{< source-info >}}

**收录说明**：直接下载全文；首图与文内 Poppy 关联卡片插画为装饰图，未收；站内相对链接已改为绝对地址。依据 Decagon 11 月 13 日公告与 Hertz 高管引语。发表日期 2026-11-16，本轮检索新发现（回填）；已收的 Poppy 1.0 篇中 Hertz 仅一笔带过，本文为该试点的专门跟进。

**内容摘要**：Hertz 加入 Decagon 的 Personal Agent Gateway 开展试点，租车人可向 Muse 提出改签或延长已有预订，并在同一对话中得到确认结果；Decagon 于 11 月 13 日宣布该试点，Hertz 是首批向个人智能体开放直连通道的企业之一，Muse 是其通道上的首个个人智能体。连接采用 Meta 对开放式个人智能体协议 Poppy 的实现，该协议于 11 月 13 日发布 1.0 版，Muse 从此在访问每个网站时优先寻找 Poppy。以续租两天为例，请求经专用的智能体对智能体通道到达 Hertz 的 Decagon 智能体，后者沿用既有智能体的操作规程（AOPs，包括客户验证、租赁政策与转接真人）处理，再把更新后的订单回传给 Muse 向租车人确认。Hertz 产品管理、客户体验与移动应用高级总监 Yatin Patel 表示，此次合作旨在探索个人智能体时代服务客户的新方式并保持体验一致可靠；试点目前仍为未来时态，Decagon 未给出上线日期，Hertz 也未说明覆盖哪些订单或地点。与已上线的 Expedia 酒店预订连接器不同，该试点连接的是企业自有的客服智能体，沿用 Hertz 自有聊天渠道的同一套规程，并遵循 Meta 于 10 月与 Sierra 等合作伙伴预览的开放标准，该标准旨在让企业在智能体行动前识别其身份并声明权限范围。

**保留理由**：已收资料中首个企业级个人智能体直连通道的落地案例，记录了 Poppy 1.0 发布、Decagon 网关与 AOPs 的运作机制，以及与标准连接器不同的“企业自有智能体直连”路线，是个人智能体生态从消费端购物向企业服务延伸的证据。

---

Hertz 加入 Decagon 的 Personal Agent Gateway 试点，租车人可以让 Muse 更改或延长已有预订，并在同一对话中得到确认结果。

Hertz 正加入 [Decagon 的 Personal Agent Gateway](https://decagon.ai/blog/hertz-opens-a-direct-line-to-muse-with-decagons-personal-agent-gateway) 的一项试点，该试点将把 Muse 连接到 Hertz 的 AI 驱动预订与客户支持平台。Decagon 于 11 月 13 日宣布这项试点。Hertz 是首批向个人智能体提供直连通道的企业之一，而 Muse 将是 Hertz 通道上的首个个人智能体。

该试点将让租车人通过询问 Muse 来更改或延长已有的 Hertz 预订，而不必致电 Hertz 或打开其网站。Muse 在同一对话中返回确认结果。

## 一次 Muse 请求如何到达 Hertz

该连接使用 Meta 对开放的个人智能体协议（Personal Agent Protocol）的实现，称为 Poppy。这正是[于 11 月 13 日达到 1.0 版](https://www.allthingsmuse.com/articles/poppy-personal-agent-protocol-1-0/)的同一协议，当时 Muse 开始在其访问的每个网站上优先寻找 Poppy。

假设一位租车人需要多用两天车。Muse 把请求发送到 Hertz 的个人智能体通道，这是一条专用的智能体对智能体通道，与 Hertz 的聊天和语音渠道并列。Hertz 的 Decagon 智能体使用在其现有智能体中运行预订请求的同一套智能体操作规程（Agent Operating Procedures，AOPs）来处理这次更改。这些规程包括客户验证、租赁政策，以及转接真人。更改完成后，Decagon 智能体把更新后的预订发回 Muse，由 Muse 向租车人确认。

Hertz 决定哪些请求可以通过该通道处理，并且可以在从试点中学习的过程中扩大范围。Hertz 保留对其智能体所遵循工作流的控制，包括哪些操作发生、以什么顺序、依据哪些政策。

Hertz 产品管理、客户体验与移动应用高级总监 Yatin Patel 表示，随着越来越多旅行者使用像 Muse 这样的个人智能体来规划和管理行程，这项合作让 Hertz 探索服务客户的新方式，并保持体验的一致与可靠。

## 一项有限的试点

这是一项试点，而 Decagon 的措辞用的是将来时。网关将启用该连接，试点将让租车人进行更改。Decagon 没有给出租车人最早何时可以使用的日期，Hertz 也没有说明涵盖哪些预订或地点。

这项试点是进入企业的一条不同于标准连接器的路线。旅行者已经可以通过 [Muse 上已上线的 Expedia 连接器](https://www.allthingsmuse.com/articles/expedia-connector-live-on-muse/) 预订酒店，该连接器在聊天内处理搜索和预订。Hertz 的试点则把 Muse 连接到企业自己的支持智能体，因此对已有预订的更改会走 Hertz 在自己聊天渠道中应用的同一套规程。它遵循 [Meta 于 10 月与 Sierra 及其他合作伙伴预览的开放标准](https://www.allthingsmuse.com/articles/meta-sierra-personal-agent-protocol/)，该标准旨在让企业在智能体行动前识别个人智能体并声明其被允许做什么。

Decagon 表示正在努力通过该网关连接更多企业和个人智能体。对 Hertz 租车人来说，第一项测试范围窄而实用。租车人通过 Muse 多用两天车，不用打电话。
