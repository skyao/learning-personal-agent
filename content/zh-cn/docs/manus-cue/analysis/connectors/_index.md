---
title: "Manus Cue：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Cue 有连接器页（Gmail、Google Calendar、Outlook、GitHub、Shopify、Instagram 等），付款走 Stripe Link 钱包，Skills 与 Manus 分开配置；但资料对连接机制、授权粒度、第三方开放都没有说明，Cue 更多依靠智能体自己的身份和云电脑直接与外部服务打交道。
---

## 概要

- 官方只笼统地说经用户许可可以连接电子邮件、日历和消息服务，用户随时决定开放哪些应用。实测看到的连接器页第一屏是 GitHub、Gmail、Meta Ads Manager、Instagram、Outlook Mail、Google Calendar、Google Workspace、Shopify。
- 官网示例展示过 Trip.com、Oura、Gmail、MyFitnessPal；实测查机票时直接出 Trip.com 卡片，不需要专门连接。
- 钱包通过 Stripe Link 授权，添加支付方式仅在美国提供。
- Skills 与 Manus 互不相通，要在 Cue 里另行配置。
- 鸿煊把 Dots、Muse 等归为「接入现有生态」的路线，把 Cue 归为「独立身份」路线：智能体用自己的邮箱、电话、钱包直接对外办事，连接器反而不是重点。

## 连接器页

应用商店介绍称，经用户许可，Cue 可以连接并使用受支持的应用，包括电子邮件、日历和消息服务，用户可以随时决定 Cue 能用哪些应用、有哪些权限（[Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})、[App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})）。

xiangxiang103 列出设置菜单有「连接器」一项，第一屏是 GitHub、Gmail、Meta Ads Manager、Instagram、Outlook Mail、Google Calendar、Google Workspace、Shopify，没有看到 Oura 和 MyFitnessPal；查机票时直接出现 Trip.com 卡片，预订平台不用专门连（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。Datawhale 和鸿煊称官网展示的连接器有 Trip.com、Oura、Gmail、MyFitnessPal（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。两者口径不同（应用内列表与官网展示），不矛盾。

授权 Gmail 后，智能体可以从用户收件箱里找信息，例如酒店确认号、最晚免费取消时间（据 [xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}}) 转述官网示例）。这类连接器读的是用户自己的账号，与智能体自己的 @bot.cue.im 邮箱是两回事。

连接器用什么机制（官方 API、MCP 或其他）、授权粒度如何、失效如何处理，资料都没有说明。

## 钱包：Stripe Link，仅美国

官网示例里反复出现「费用走我的 Link」，设置页弹窗「为 Cue 设置安全支付」，授权 Link 钱包让智能体替用户完成交易；添加支付方式的弹窗底部写着「仅在美国提供」（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。钱包的审批规则见[安全](../security/)。

## Skills 与 Manus 分开

帮助文档写明，Cue 与 Manus 的 Skills 配置相互独立，在 Manus 中创建或导入的 Skills 不会自动出现在 Cue，需要在 Cue 内另行配置（[帮助：Skills]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-skills" >}})）。这与 Claude Duet 直接沿用 Claude 账号的技能和连接器不同（见 [Claude Duet：连接器]({{< relref "/docs/claude-duet/analysis/connectors" >}})）。

## 生态策略

肖弘称「海外的生态开放，很容易就能做出不错的体验」，并在准备国内版本、希望与各方合作（据[财经涂鸦]({{< relref "/docs/manus-cue/sources/media/2026-09-29-caijingtuya-xiaohong-on-cue" >}})转述）。中金把 Cue 与 Instinct 归为「独立型助手」，认为其服务和工具调用受平台授权限制，外部模型、账户连接、电话与浏览器执行会产生持续费用（[中金]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})）。潮涌认为平台开始反抗（亚马逊封禁 Muse 购物、Manus 被监管拦下），靠模拟用户操作的路线面临平台关系风险（[潮涌]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})）。

推断：Cue 的连接器清单偏向通用办公与电商工具，与官网偏美国生活服务的示例并不完全对应；它对生活服务的覆盖更可能依靠智能体用自己的身份上网和打电话，而不是依靠连接器。这使它少受「平台是否开放接口」的限制，但更容易遇到注册风控和 IP 问题（见[运行环境](../runtime/)）。

## 资料缺口

- 完整连接器清单、连接机制、授权粒度与撤销方式。
- 是否开放给第三方开发者；与商家（扫码点单）的合作方式。
- 除 Link 外的支付方式、钱包的地区计划。

## 主要资料

官方
- [Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})、[App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})：连接应用的笼统说明
- [帮助：Skills]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-skills" >}})：Skills 与 Manus 分开

媒体
- [财经涂鸦]({{< relref "/docs/manus-cue/sources/media/2026-09-29-caijingtuya-xiaohong-on-cue" >}})：肖弘谈海外生态

社区
- [xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})：连接器页第一屏、Trip.com 卡片、Link 钱包
- [Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})：官网展示的连接器
- [中金]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})、[潮涌]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})：独立型助手的平台限制
