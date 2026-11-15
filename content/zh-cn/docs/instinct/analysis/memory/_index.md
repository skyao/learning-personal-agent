---
title: "Instinct：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-15
sourcesUntil: 2026-11-13
description: >
  Instinct 接入邮件、日历、消息应用，用户还可以授权银行账户；它把邮件以纯文本存下来以备检索，断开连接后不会自动删除。记忆机制只有一篇媒体资料描述（后台批处理写入、用 Git 管理），创始人强调偏好一次告知即可永久复用。用户能否查看和编辑记忆，资料没有说明。
---

## 概要

- 接入范围：邮件、日历、消息应用（Gmail、WhatsApp、Google Workspace 等），内测期条款还包括设备的音频、位置和屏幕；用户可以授权银行账户，让它逐笔审查扣费。
- 内测期多名用户发现：断开 Gmail 后，Instinct 仍保留着以纯文本存储的邮件；之后设置里加了删除外部数据的工具，但截至 2026-10-17 的资料，删除仍要用户手动申请。
- 据 InfoQ，Instinct 的记忆由后台批处理统一写入，用 Git 管理，支持 Diff 和回滚，检索以关键词和别名为主。这是资料中唯一的机制描述，未注明出处。
- 创始人称偏好说一次就能永久复用，它还会从总体品味推出其他偏好，并按用户的阅读风格调整回复。
- 跨用户共享上下文靠「可信网络」：不同用户的 Instinct 之间可以互查日历空闲、共享文件，权限按关系分级。

## 接入的个人数据

内测期的 TechCrunch 报道称，Instinct 连接邮件、消息应用、日历，以及设备的音频、位置和屏幕（[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})）。Top5Apps 称这是「该领域最深的触达」（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。TechCrunch 的短信类智能体合集写的是连接邮件、日历、Google Workspace（[TechCrunch：短信类智能体合集]({{< relref "/docs/industry/sources/media/2026-10-24-techcrunch-text-message-agents" >}})）。WIRED 和 Android Authority 的作者接入的是 Gmail 和 WhatsApp（[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})、[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})）。

创始人在访谈中称，用户可以授权关联银行账户，让它逐笔审查交易记录和连续扣费，提醒久未使用的订阅（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。C 轮公告提到，iMessage 位置共享增强后，Instinct 能识别用户何时到达某地，给出基于位置的建议（[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})）。

授权是分步给出的：创始人称普通用户通常要 2 到 3 周才开放银行卡、邮箱、完整日历这些核心权限（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。Android Authority 作者也建议先从基本任务试起，不要一开始就开放所有账户（[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})）。

## 邮件以纯文本保存，断开后不自动删除

内测期的 TechCrunch 报道汇总了几位用户在 X 上的反馈：Peter Yang 发现 Instinct 索引并保留了他的邮件，要求删除 Gmail 记录时它没有照做；Claire Vo 上午 11 点断开 Google 连接，下午 2 点仍收到邮件摘要，机器人回答说邮件以纯文本形式存储，以备之后搜索。报道称团队之后在设置里加了删除外部数据的工具（[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})）。

后来的资料显示问题没有完全消失：WIRED 2026-09-24 引用 X 用户的说法，断开邮箱后 Instinct 仍保留了一份收件箱副本（[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})）；Android Authority 2026-10-17 写明，断开 Gmail 不会自动删除已存储的邮件和信息，需要在仪表板里手动请求删除（[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})）。六款主动型智能体对比一文引用的修订后条款，授权 Instinct「access, copy, collect, and index data from your Connected Services」（[六款主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})）。

这些说法都来自用户反馈和条款，没有 Instinct 的官方说明：Instinct 没有回应 WIRED 的置评请求（[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})）。数据用途和训练条款见 [隐私]({{< relref "/docs/instinct/analysis/privacy" >}})。

## 记忆如何形成：一篇媒体资料的描述

InfoQ 比较各家记忆设计时写道：Instinct 更强调可控性，记忆统一通过后台批处理写入，采用 Git 管理，支持 Diff 和回滚，以关键词和别名检索为主；对照的是 Town 的 5 到 20 页 Wiki 和 Muse 的记忆溯源、每晚「Dream」整理（[InfoQ：千问谈下限与上限]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})）。InfoQ 没有注明 Instinct 这部分的出处，资料库里也没有第二个来源。

创始人对记忆的说法偏向效果：用户告诉过一次的偏好可以永久复用，它还会从总体品味推出航司、舱位、座位、饮食、支付卡、常住酒店等其他偏好；它会逐渐读懂用户风格（比如反感冗长套话、重大决策只看核心数据）并自适应，而不是套用预设的性格模板（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。Android Authority 作者的使用记录与此相符：每天早上收到一份重要邮件和待办清单，白天它会标出重要邮件并询问是否要处理（[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})）。

用户能否查看、编辑某条记忆，资料没有说明。灵螺创新泛称这类产品都没有直观展示「我的记忆有哪些」的方式，但没有专门分析 Instinct，且文章在推广自家产品（[灵螺创新：Personal AI Center]({{< relref "/docs/industry/sources/community/2026-11-04-lingluo-personal-ai-center" >}})）。

推断：如果 InfoQ 的描述属实，Git 式版本管理和回滚是一种给开发者看的可控性，并不等于给用户看的可见性；资料中的用户反馈集中在「断开后数据还在」，说明用户侧的删除和可见性是这个产品记忆设计的薄弱处。

## 可信网络：跨用户共享上下文

2026-09-28 C 轮公告称，用户的 Instinct 可以与可信朋友、同事的 Instinct 协调日程，直接共享文件、PDF、图片和电子表格（[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})）。TechCrunch 9 月称这项功能允许用户的助理联系其他人的助理处理部分任务（[TechCrunch：Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}})）。Top5Apps 记作 9 月 9 日上线的 Trusted Person 网络（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

创始人称权限按关系分级、可撤销：伴侣能共享大部分信息，同事只能看到空闲时段和项目相关的少量邮件（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。明义价值观指出，难点在于让 Instinct 知道社交边界，不向其他 Instinct 泄露允许之外的数据（[明义价值观：穿透 AI 产业链]({{< relref "/docs/industry/sources/community/2026-10-31-mingyi-personal-agent-industry-chain" >}})）。越权防护见 [安全]({{< relref "/docs/instinct/analysis/security" >}})。

## 资料缺口

- 记忆的官方说明：存什么、存多久、用户能否查看和编辑某条记忆。InfoQ 的 Git 管理一说需要一手出处。
- 断开连接后的删除流程：仪表板里的删除工具覆盖哪些数据，删除是否彻底，现在是否改为自动删除。
- 银行账户授权通过什么机制接入（如 Plaid）、权限范围。
- 群聊和可信网络中，对方的信息会不会进入自己的 Instinct 的记忆。

## 主要资料

- 媒体：[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})，内测期的邮件保留问题；[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})、[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})，断开后不自动删除；[InfoQ：千问谈下限与上限]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})，Git 管理的记忆；[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})，可信网络与位置共享；[TechCrunch：短信类智能体合集]({{< relref "/docs/industry/sources/media/2026-10-24-techcrunch-text-message-agents" >}})，接入范围。
- 社区：[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})，创始人对偏好记忆、授权节奏和权限分级的说法；[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})，接入范围；[六款主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})，条款原文；[明义价值观：穿透 AI 产业链]({{< relref "/docs/industry/sources/community/2026-10-31-mingyi-personal-agent-industry-chain" >}})，可信网络的边界问题。
