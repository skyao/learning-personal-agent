---
title: "Manus Cue：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Cue 的安全设计依赖「独立身份」：智能体用自己的邮箱、电话、钱包，不需要用户交出账号密码；付款每笔需批准、在预算内进行，Cue 不保存支付凭证。但审批规则没有设置开关，靠对话立规矩；资料库中没有针对 Cue 的漏洞报道，也没有官方安全说明。
---

## 概要

- 付款有三条官方承诺（钱包弹窗）：每一笔开销都需用户批准；Cue 绝不存储支付凭证；Cue 只负责支付，订单、交付、退款由商家管理。发布文另说付款在用户设定的预算内。
- 除付款外，其他动作的审批「由你自己设定」，但实测发现设置里没有单独的审批开关，边界要在对话中告诉智能体，它记下后遵守。
- 独立身份被多位作者看作 Cue 的安全优势：用户不必交出自己的邮箱和账号密码，外部系统能区分是谁在行动。代价是对方看得出是 AI 代发，风控严格的平台会封号。
- 截至 2026-11-10，资料库中没有针对 Cue 的漏洞或安全事件报道；Manus 本体的漏洞报道按收集规则未收。

## 付款：每笔批准、预算内、不存凭证

发布文称智能体「在你设定的预算内付款」（[Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})）。应用商店介绍称经用户批准后购买付款，扫码点单时付款由用户确认（[Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})）。xiangxiang103 截到的钱包弹窗列了三条：每一笔开销都需要用户批准；Cue 绝不存储支付凭证；Cue 仅负责支付，订单、交付、退款由商家管理（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。钱包通过 Stripe Link 授权，见[连接器](../connectors/)。

「每笔批准」与「在预算内付款」两种说法如何并存（预算内是否仍逐笔确认），资料没有说明。AIX财经、鸿煊、AI问消都只重述「在预算内付款」（[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})、[AI问消]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}})）。

## 其他动作：靠对话立规矩

xiangxiang103 转述官网常见问题：智能体何时需要批准「是你自己设定的」，遇到需要拍板的事会带回来（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。他实测给智能体立了规矩（职责、汇报格式、付款前确认、单笔上限），智能体回复把职责和执行边界记下，之后发邮件前先给草稿确认；但设置菜单里「没有单独的‘审批规则’开关」（同上）。作者建议第一天就把付款、下单、改预约、对外发邮件设为先问用户。

在代注册 Claude 的实测中，智能体走到年龄确认和条款同意处停下来问作者，没有替人勾选（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。

推断：审批规则存在智能体的记忆或指令里，而不是由系统强制执行。这样设置灵活，但规则是否被遵守取决于模型本身；与 Claude Duet 在模型之外另设分类器和审批层（见 [Claude Duet：安全]({{< relref "/docs/claude-duet/analysis/security" >}})）相比，约束更弱。资料只有一位用户一天的观察，无法判断规则的遵守率。

## 独立身份的安全含义

xiangxiang103 认为，只有给智能体独立身份才能避免交出用户自己的账号密码；他把 Cue 与 Muse 对比：Muse 用用户的账号、看不到密码，发邮件付款前要用户点头，Cue 用智能体自己的身份（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。Datawhale 认为独立邮箱、电话或支付让外部系统能区分行动身份，已发出的信和付出的钱应可审计，但独立身份「并不等于办事一定可靠」（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。阿言er 强调拥有钱包「也不能被写成可以不经授权任意花钱」（[阿言er]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。鸿煊把「平台会不会封、出错能否撤销」列为这条路线需要核查的问题（[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。

实测中的两面：邮件页脚写明「Sent on behalf of 用户名」，对方知道是 AI 代发（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})，见[交互渠道](../channels/)）；用 @bot.cue.im 邮箱和云电脑注册的 Claude 账号约 22 分钟后因「可疑信号」被暂停（同上，见[实际效果与可靠性](../reliability/)）。

## 资料缺口

- 官方的安全说明：提示注入、恶意网页、越权操作的防护；智能体之间、群聊中的权限隔离。
- 审批规则的系统实现：是否有强制执行的审批层，「预算」如何设置。
- 针对 Cue 的漏洞报道、漏洞赏金、独立审计。
- 智能体登录第三方网站时凭证的存放方式。

## 主要资料

官方
- [Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})：预算内付款
- [Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})：批准后付款，扫码付款由用户确认

社区
- [xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})：钱包弹窗三条、对话立规矩、条款处停下、注册被封
- [Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[阿言er]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})：独立身份的安全含义

媒体
- [AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})：预算内付款
