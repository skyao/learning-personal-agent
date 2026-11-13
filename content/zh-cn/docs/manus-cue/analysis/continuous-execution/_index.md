---
title: "Manus Cue：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Cue 的持续执行靠三样东西：自动化（定时或按事件触发）、智能体自己的邮箱和电话（替用户盯通知、接来电），以及关掉应用后仍在运行的云电脑。唯一的详细实测认为「蹲守」类任务最有用，但也发现智能体口头答应却没建任务。
---

## 概要

- 官方提供自动化（Automations）：按时间表运行，也可以响应受支持的事件和条件；示例是每日议程、每周购物清单、留意重要变化。
- 智能体自己的邮箱和电话让它能在用户不在时接收外部信息：xiangxiang103 的智能体主动转告了一封账号被封的邮件；官方称它会替用户接电话并留下摘要。
- 实测中「蹲守」（盯价格、放票、空位）是作者认为最有价值的用法，任务建好后每天在跑、遵守用户立的规矩。
- 问题出在任务建立阶段：智能体追问三轮才建好任务，之前一次说「我先安排跟踪」时实际什么都没建。
- 主动打扰的频率、任务数量上限、失败重试，资料都没有涉及。

## 自动化：定时与事件触发

帮助文档称，用户可以在 Cue 里描述想完成什么、何时完成，建立定时自动化（Scheduled Automation）（[帮助：Manus 2.0 新功能]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-what-is-new-in-manus-2-0" >}})）。应用商店介绍更进一步：自动化「可以按时间表运行，也可以响应受支持的事件和条件」，由用户决定触发条件和后续动作，示例有每日议程汇总、每周购物清单、留意重要变化（[Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})、[App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})）。哪些事件受支持，资料没有列出。

Manus 本体的 Automations 可以由新邮件、广告数据变化、日历事件、Slack 消息、Notion 更新等触发（据 [xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}}) 转述官方功能）；Cue 是否使用同一套触发器，资料没有说明。阿言er 把 Cue 的计划自动化与 ChatGPT Tasks、WorkBuddy 等的定时能力并列为对「主动性」的尝试（[阿言er]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。

## 用户离开后：云电脑继续跑，邮箱和电话收信息

发布文称智能体能在用户设定的预算内付款、在自己的机器上完成任务，并「替你接听电话，并在 Cue 里给你留下一份摘要」（[Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})）。xiangxiang103 确认关掉应用后智能体仍在运行（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。

xiangxiang103 的智能体在 2:51 主动发来一条消息，转告 Claude 账号被封的邮件，并提出帮忙写申诉；作者认为这正是智能体自带邮箱「能替你盯住通知」的用处（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。官网示例中电话的用法是：用户在飞机上或倒时差时来电由智能体接，问清来意，急事推送到用户的 Slack，诊所回电的信息记入日历（同上，转述官网示例）。电话代接没有实测记录。

## 蹲守：实测中最有价值的用法

xiangxiang103 统计官网六十多个示例，「一大半都在干‘蹲守’这件事」：盯价格、盯放票、盯空位（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。他的蹲机票实测过程：

1. 第一次说要盯机票，智能体回答「明白，我先安排跟踪」，查任务列表才发现「其实什么都没安排」。
2. 再次交代后，智能体追问三轮；它自己写的日期选项算错一天，又回头问；「一个成人」是它自己默认、没有问过的。
3. 最终任务设为每天上午 9 点（上海时间）检查，持续到 12 月 10 日，并先查了一遍现价（最低一班 2103 元一个成人）；任务卡里是它写给自己的英文指令，含「Never book or pay」。

作者的结论是任务「建好之后是真的每天在跑，还守着你立的规矩」，建议把指令一次说全（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。

推断：Cue 的持续执行与 Muse、Dots 的「主动简报」思路不同，更接近为单个目标设一个长期监视器；它的价值依赖智能体自己的邮箱和电话作为信息入口。实测问题集中在建任务时的确认环节，而不是任务运行本身，但只有一份实测、跑了一天，长期稳定性无从判断。

## 资料缺口

- 受支持的事件和条件清单、自动化数量与运行频率的上限、失败通知与重试。
- 主动联系用户的规则：何时推送、频率如何控制。
- 电话代接与摘要的实测；数周以上的蹲守任务结果。

## 主要资料

官方
- [帮助：Manus 2.0 新功能]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-what-is-new-in-manus-2-0" >}})：定时自动化
- [Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})、[App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})：按时间表或事件运行
- [Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})：接电话留摘要

社区
- [xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})：蹲机票全过程、邮件通知转告、官网示例统计
- [阿言er]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})：与其他产品定时能力并列
