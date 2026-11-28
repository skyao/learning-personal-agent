---
title: "Hertz 试点 Decagon 网关：Muse 可代改租车预订"
linkTitle: "Hertz 接入 Muse"
date: 2026-11-13
originalTitle: "Hertz opens a direct line to Muse with Decagon’s Personal Agent Gateway"
sourceUrl: "https://decagon.ai/blog/hertz-opens-a-direct-line-to-muse-with-decagons-personal-agent-gateway"
author: "Alan Yiu"
publisher: "Decagon"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-15
tags: [连接器, 发布]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载全文。去掉了订阅、招聘、相关文章与话题导航等区块；题图为装饰图，未收。Unite.AI 同日报道了同一事件，系本公告的转述，不另收。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Decagon 产品副总裁 Alan Yiu 于 2026 年 11 月 13 日发文称，Hertz 成为首批加入 Decagon 个人智能体网关（Personal Agent Gateway）试点的企业之一：试点将让 Muse 通过 Meta 对开放式个人智能体协议（Poppy）的实现，接入 Hertz 的 AI 驱动预订与客服平台，租车人只需向 Muse 提问即可更改或延长已有 Hertz 预订，并在同一对话中收到确认答复。运作方式是：Muse 把请求发给 Hertz 的个人智能体专属通道（与 Hertz 现有聊天、语音渠道并列的智能体对智能体通道），Hertz 的 Decagon 智能体按既有智能体处理预订请求时所用的同一套智能体操作规程（AOPs）完成变更，再把更新后的预订发回 Muse 由其向租车人确认；文中以「多留车两天」为例说明这一流程。Hertz 的 Decagon 智能体执行请求时沿用其现有聊天智能体的同一套 AOPs，包括客户验证、租车政策与转接真人客服，Hertz 自行决定通过该通道开放哪些请求，并可随试点推进扩大范围。Muse 将成为 Hertz 该通道上的第一个个人智能体；Decagon 表示正着手把更多企业与个人智能体接入该网关，企业只需设定一次政策，每个新接入的个人智能体都使用同一通道与同一套 AOPs，无需重建逻辑。

**保留理由**：此前已收的 Sierra Poppy 1.0 发布稿与 Muse 官方 Poppy 稿只说明了 Poppy 标准的发布与机制，本篇首次记录了 Poppy 落地到具体企业的首批试点案例：Hertz 成为首批试点企业、Muse 是其通道上第一个个人智能体，并具体说明了 Decagon 网关下「Muse 请求—Hertz 专属通道—Decagon 智能体按 AOPs 执行—回传确认」的完整运作方式。

---

Hertz 通过 Decagon 的个人智能体网关为 Muse 开通直达通道

发布于 2026 年 11 月 13 日

Alan Yiu，Decagon 产品副总裁

发布于 2026 年 11 月 13 日

Alan Yiu

产品副总裁

## 文章

个人智能体已经在客户旅程中代表其所有者行动，从预订行程到更改预订，或处理账单问题。随着越来越多客户转向这些智能体，企业也能从更高的使用可见性中受益。

Hertz 是首批通过一项新试点为个人智能体开通直达通道的企业之一。Hertz 正在加入 Decagon 的[个人智能体网关（Personal Agent Gateway）](https://decagon.ai/blog/personal-agents-are-here)，这将让 Muse 能够使用 Meta 对开放式个人智能体协议（Personal Agent Protocol，Poppy）的实现，连接到 Hertz 由 AI 驱动的预订与客户支持平台。该试点将让租车人只需向 Muse 提出请求，就能更改或延长其现有的 Hertz 预订。

对租车人来说，这意味着他们可以把预订更改交给自己的智能体，并在同一段对话中得到确认的答复。

## 一次 Muse 请求如何到达 Hertz

假设一位 Muse 用户需要把车多留两天。Muse 不会拨打 Hertz 电话或打开 [hertz.com](http://hertz.com)，而是把请求发送到 Hertz 的个人智能体通道——一个与 Hertz 现有聊天和语音渠道并列的专属智能体对智能体通道。

Hertz 的 Decagon 智能体将使用与其现有智能体中处理预订请求相同的智能体操作规程（Agent Operating Procedures，AOPs）来处理这次更改。完成后，它会将更新后的预订发回 Muse，由 Muse 与租车人确认。Hertz 可以看到通过该通道进来的请求，并复用其为在其他地方服务租车人而已经构建的预订逻辑。

## 构建在 Hertz 的政策之上

Muse 会把租车人的请求带给 Hertz，并在同一段对话中返回结果。Hertz 的 Decagon 智能体将使用管理其现有聊天智能体的同一套 AOPs 来履行该请求，包括客户验证、租车政策和转接真人客服。

这就是把个人智能体连接到企业自有智能体的价值所在，超越了通过 API 或 MCP 暴露单个工具。企业保留对整个工作流的控制：执行哪些操作、以什么顺序执行，以及依据哪些政策。

Hertz 还决定通过该通道开放哪些请求，并可以随着从试点中学习而扩大范围。

> 「在 Hertz，我们专注于在租车旅程的每个环节提供无缝体验，这意味着要在客户所在之处与他们相遇。随着越来越多旅行者开始使用 Muse 这样的个人智能体来规划和管理行程，我们与 Decagon 的合作让我们能够探索服务客户的新方式，同时交付他们期望从 Hertz 获得的始终如一、可靠的体验。」
> - Yatin Patel，Hertz 客户体验与移动应用产品管理高级总监

## 更多个人智能体，更多客户

Muse 将成为 Hertz 该通道上的第一个个人智能体。我们正致力于通过 Decagon 的个人智能体网关连接更多企业与个人智能体。

该通道正是为这种增长而构建的。企业只需设定一次政策，每个新的个人智能体都连接到同一通道和同一套 AOPs，无论它使用哪种授权协议，因此随着更多智能体接入，无需重建逻辑。

客户会继续把这样的任务交给他们的智能体。现在就为这些智能体开通通道的企业，可以决定对话如何进行，并在大多数同行尚未开始之前，就从真实流量中学习。
