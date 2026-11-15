---
title: "Instinct：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-15
sourcesUntil: 2026-11-13
description: >
  Instinct 不靠插件市场，而是用云端电脑像人一样操作网站，网站走不通就打电话、发 WhatsApp。它有自己的邮箱用来注册和管理账号。商家侧的接入从 2026-10 起出现：加入 Poppy 协议的首批设计伙伴、Shop Pay 首批接入、温德姆开放库存；与此同时，亚马逊等平台拦截智能体，Instinct 对此拒绝置评。
---

## 概要

- 用户侧接入的是邮件、日历、消息应用、Google Workspace；对外部服务，Instinct 主要用云端电脑操作网页和应用，网站不支持时用电话（Concierge）或 WhatsApp 联系商家。
- 2026-09 起，Instinct 给每个用户的助理一个专属邮箱，用来注册服务、管理账号、联系商家，不占用用户自己的收件箱。
- 商家侧：2026-10 成为 Meta 与 Sierra 牵头的 Poppy（个人智能体协议）首批设计伙伴；2026-10-28 成为 Shop Pay 结账首批接入的四款智能体之一；温德姆 2026-10-22 点名它可以预订温德姆酒店。
- 平台拦截：据 The Verge 报道，Instinct 的助理也无法访问亚马逊；有用户因 Resy 高频访问被封号。Instinct 拒绝置评。
- 没有开放给第三方开发者的插件或 API；创始人称在与垂直平台谈合作，但截至资料日期未公布。

## 用云端电脑操作网站，走不通就打电话

官网举的任务都是生活事务：为新菜谱订食材、订周末回家的火车票、订杂货、给朋友送花、找周末球场（[官网首页]({{< relref "/docs/instinct/sources/official/2026-11-05-instinct-homepage" >}})）。内测期报道列出的有预约订位、安排机场用车、清理收件箱、购物、找便宜机票（[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})）。创始人举的例子包括调用 Spotify 的收听偏好选演出、为周末聚会叫 Uber、与外卖服务交互（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。

这些任务不靠官方 API，而是靠云端电脑像人一样操作（见 [运行环境]({{< relref "/docs/instinct/analysis/runtime" >}})）。网站走不通时换渠道：WIRED 记者的威尼斯行程中，Instinct 用 WhatsApp 联系了不接受常规预订的小店（[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})）；2026-09-16 上线的 Concierge 可以直接给不接受在线预订的餐厅打电话（[TechCrunch：Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}})、[潮涌AI：全球 Top15]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})）。电话渠道的细节见 [交互渠道]({{< relref "/docs/instinct/analysis/channels" >}})。

## 助理自己的邮箱

TechCrunch 短信类智能体合集概括了 2026-09-09 的前文：Instinct 开始为用户的助理提供专属邮箱地址，用来代用户创建和管理账号、注册服务、联系商家、跟进请求，而不必填满用户的个人收件箱（[TechCrunch：短信类智能体合集]({{< relref "/docs/industry/sources/media/2026-10-24-techcrunch-text-message-agents" >}})）。2026-09-17 的 TechCrunch 报道也提到了「上周」上线的邮箱（[TechCrunch：Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}})）。Datawhale 的综述把这归为用独立邮箱、电话或支付工具区分「行动身份」的做法（[Datawhale：Personal Agent 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。

## 商家侧的接入：协议、支付、酒店库存

**Poppy 协议。** Sierra 2026-10-06 的博客宣布，Meta 与 Sierra 与 Genesys、Instinct、Rocket、Shopify、Stripe、Walmart 等共同开发个人智能体协议（Personal Agent Protocol，Poppy），定义个人智能体与商家互动时的认证、消费者授权，以及商家对智能体行为的可见性；用户决定授予智能体读或写的权限，基于 OAuth（[Poppy 协议发布]({{< relref "/docs/industry/sources/community/2026-10-06-introducing-personal-agent-protocol" >}})）。2026-11-13 的 1.0 发布把 Instinct 列为首批设计伙伴，但 1.0 的落地案例（Shopify、Mercury、Synchrony、土耳其航空）和 Muse 全面启用都没有提到 Instinct 是否已经实现（[Poppy 1.0 发布]({{< relref "/docs/industry/sources/community/2026-11-13-releasing-personal-agent-protocol-1-0" >}})）。

**Shop Pay。** 据 All Things Muse 转述 The Defiant，Shopify 在 2026-10-28 的 Fall '26 发布中把 Shop Pay 结账放进个人智能体，首批是 Muse、Claude Duet、Grok Bot 和 Instinct，覆盖 Shopify 之外的商家；买家每次购买要点允许或拒绝，Shopify 称卡号不透露给智能体（[Shop Pay 进 Muse]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}})）。另据 Top5Apps，Muse、Grok Bot、Instinct 都通过 Stripe Link 付款（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。付款审批见 [安全]({{< relref "/docs/instinct/analysis/security" >}})。

**温德姆。** Skift 报道，温德姆 CEO 在 2026-10-22 的第三季度财报电话会上点名 Muse、Dots、Instinct 等 AI 助手可以搜索并预订温德姆酒店，温德姆通过中央预订系统直接向智能体提供房态和价格（[Skift：温德姆开放库存]({{< relref "/docs/industry/sources/media/2026-10-22-skift-wyndham-ai-booking-agents" >}})）。

**创始人的说法。** 创始人称他们主动登门拜访垂直领域巨头的高管，用 Instinct 用户与其生态交互的数据谈合作；建议传统公司先对 1% 的用户开放 API 做灰度测试；称将来会公布重塑餐厅预订的「重量级合作」；认为与 OTA 更可能走向合作（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。截至 2026-11-13 的资料，没有看到这类合作公布。

## 平台拦截

据 36氪转述 The Verge 报道，亚马逊认为 Muse「持续访问」违反政策，Grok、Instinct 的助理和 Dots 也无法访问亚马逊；Instinct 拒绝置评（[36氪：Agent 遭集体拉黑]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})）。Top5Apps 称亚马逊依据 8 月加入的 Agent Terms 屏蔽智能体，任何零售商都可以照搬（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。一位用四款智能体的美国投资人提到 LinkedIn 明文禁止 bot，Zillow、亚马逊会把 bot 挡回去，这是对这类产品的泛指（[特工宇宙：投资人用四款 Agent]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。高频访问导致 Resy 封号的报告见 [运行环境]({{< relref "/docs/instinct/analysis/runtime" >}})。

生活有变量的文章认为，Instinct 这类产品能连接现成服务，但还要证明访问是否稳定、授权覆盖哪些动作、出了问题能否继续处理（[生活有变量：大厂的防守战]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})）。

推断：Instinct 的连接方式是「先模拟人，再争取协议」。模拟人覆盖面广、不需要对方配合，但随着亚马逊等平台用条款和技术手段拦截，长期要靠 Poppy、Shop Pay、温德姆这类商家主动开放的通道。它作为 14 人团队能进入 Poppy 首批名单，与创始人出身 Sierra 有关的可能性较大（TechCrunch 称他是前 Sierra 研究科学家，[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})），但资料没有直接说明原因。

## 资料缺口

- 用户侧连接的完整清单和授权方式（OAuth 还是让智能体登录），连接失效时如何处理。
- Instinct 是否已实现 Poppy 协议、Shop Pay 在 Instinct 里的实际体验。
- 创始人所说的餐厅预订「重量级合作」是否公布。
- 平台拦截后 Instinct 的应对，以及它对亚马逊问题的立场（目前只有「拒绝置评」）。

## 主要资料

- 官方：[官网首页]({{< relref "/docs/instinct/sources/official/2026-11-05-instinct-homepage" >}})，任务范围。
- 媒体：[TechCrunch：短信类智能体合集]({{< relref "/docs/industry/sources/media/2026-10-24-techcrunch-text-message-agents" >}})、[TechCrunch：Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}})，专属邮箱与电话；[Shop Pay 进 Muse]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}})，Shop Pay 首批接入；[Skift：温德姆开放库存]({{< relref "/docs/industry/sources/media/2026-10-22-skift-wyndham-ai-booking-agents" >}})，温德姆开放库存；[36氪：Agent 遭集体拉黑]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})，平台拦截；[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})，用 WhatsApp 联系小店。
- 社区：[Poppy 协议发布]({{< relref "/docs/industry/sources/community/2026-10-06-introducing-personal-agent-protocol" >}})、[Poppy 1.0 发布]({{< relref "/docs/industry/sources/community/2026-11-13-releasing-personal-agent-protocol-1-0" >}})，Poppy 协议；[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})，创始人谈合作；[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})，Stripe Link 与亚马逊条款；[生活有变量：大厂的防守战]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})、[特工宇宙：投资人用四款 Agent]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})、[Datawhale：Personal Agent 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})，第三方观点。
