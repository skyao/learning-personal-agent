---
title: "Claude Duet：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Claude Duet 只在自己的独立应用里与用户交流，以手机为主，一个主线程加多个频道；它不给他人打电话、不发短信，对外只能经批准从用户已连接的账号发邮件。界面被 WIRED 评为六款中最好。
---

## 概要

- Duet 是独立应用，与主 Claude 应用分开，官方列出 iOS、Android 与 claude.ai；候补名单要选手机类型，设置在手机上完成。桌面端的说法不一（见下）。
- 交流方式像给人发消息：打字或语音，一个持续的主线程，可以为不同主题建频道。没有短信、iMessage、WhatsApp、电话等外部渠道。
- 对外沟通只有一条路：经用户批准，从已连接的账号发邮件。Duet 不给他人打电话，也不发短信，没有自己的邮箱或号码。
- 界面评价高：WIRED 评为「最佳界面」；评测者称它「几乎就像 Claude 的一个简化视图」。短板是只能单人使用，频道不能与他人共享。

## 独立应用，以手机为主

发布稿称 Duet「存在于自己的应用中，与主 Claude 应用分开」，提供 iOS、Android 与 claude.ai，从早期用户那里学到的东西将决定两者如何协同（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。帮助文档要求加入候补名单时选择 iPhone 或 Android，邀请邮件在手机上打开，访问权限与候补名单所用邮箱及手机上的 Apple 或 Google 账号绑定（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。

桌面端的资料互相矛盾：Claire Vo 测试 TestFlight 早期版本时 Duet 没有桌面应用，她认为仅限手机的体验与她工作的地方脱节（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})）；fig.blue 则提到桌面应用可以访问用户允许的本地主机（[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})）；Alarcon 称领取限额重置的按钮只在网页或桌面应用中，Duet 手机应用不显示（[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})）。这些资料不足以确定 Duet 是否有正式的桌面应用。

## 主线程、频道与 Everything

用户通过打字或语音，在同一个持续的对话线程里给 Duet 发消息（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）；主线程保持在一处，可以为不同主题建独立频道，频道共享同一份记忆（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。

评测者描述的界面：「Everything」汇总所有请求，频道是针对单一工作流的独立聊天，分组把频道归在一起；在 Everything 里让它规划下周内容，它会自己拆成任务并归到各频道；任务卡、按钮选项设计得好（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。fig.blue 称可以用 Cmd-k 调出频道列表切换（[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})）。

语音方面，fig.blue 认为 Duet 的语音交互只是「美化版的语音转文字」，Dots 在语音上仍占优（[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})）。

## 不打电话、不发短信，经批准从用户账号发邮件

帮助文档写明 Duet「不会给其他人打电话或发送短信」；经用户批准，它可以从已连接的账号发送电子邮件（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。资料中没有 Duet 拥有自己的邮箱、号码或对外身份的说法；对外沟通都以用户的账号进行，发出前需要批准（见[安全]({{< relref "/docs/claude-duet/analysis/security" >}})）。

与其他产品对照：Instinct 通过短信、iMessage、WhatsApp、电话工作，Muse 有 App 和 WhatsApp，Duet 则在应用内给用户发消息，「仍不能发短信或打电话」（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})、[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。Aakash 把这一点列为他仍首选 Instinct 的原因之一（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。

## 界面评价与单人限制

WIRED 称 Duet 的专用应用在导航和跟进进行中的任务方面「极其易用」，在六款中评为「最佳界面」（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。Aakash 称它「几乎就像 Claude 的一个简化视图」（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。

Claire Vo 认为频道借用了 Slack 的理念，让每个项目有专属空间，但频道只用于组织一个人的工作，不能与他人共享；「Duet 显然是一个单人智能体」，不适合需要共享的小团队（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})）。官方称 Team 与 Enterprise 套餐计划以后引入（见[开放与价格]({{< relref "/docs/claude-duet/analysis/access-pricing" >}})）。

## 资料缺口

- 桌面应用是否正式提供；claude.ai 网页版的功能范围。
- 是否计划接入短信、WhatsApp 等外部渠道，或给 Duet 独立的邮箱、号码。
- 多人共享频道或团队版的计划细节。

## 主要资料

- 官方：[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})（独立应用、平台、主线程）、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})（候补名单选手机、频道、不打电话不发短信）
- 媒体：[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})（最佳界面）
- 社区：[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})（界面概念、与 Instinct 对比）、[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})（无桌面端、单人）、[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})（频道切换、语音、桌面应用）、[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})（重置按钮不在手机端）、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})（渠道对比）
