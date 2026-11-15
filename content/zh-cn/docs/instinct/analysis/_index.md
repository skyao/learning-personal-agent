---
title: "Instinct 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-15
sourcesUntil: 2026-11-13
description: >
  Instinct 是旧金山创业公司 Spear Street Technology 的个人智能体，没有独立 App，用户通过 iMessage、短信、WhatsApp、电话与它交流，它用云端的手机和电脑替用户办事。邀请制、对用户免费，2026-09 以 100 亿美元估值融资 10 亿美元。分析覆盖截至 2026-11-13 收集的 8 篇 Instinct 资料和 27 篇涉及 Instinct 的行业资料。
---

## 概要

- **没有界面的智能体。** 没有独立 App，入口是 iMessage、短信、WhatsApp、电话和邮件；它有自己的电话号码、邮箱、虚拟手机和云端电脑，像人一样操作网站，走不通就打电话。纯消息的形态在评测中评价两极。（[交互渠道]({{< relref "/docs/instinct/analysis/channels" >}})、[运行环境]({{< relref "/docs/instinct/analysis/runtime" >}})）
- **主动跟进是长处。** 长期使用者记录了它发现航班提前 90 分钟后退票省约 550 美元、追踪价格、识别钓鱼邮件；Top5Apps 称它「最有能力、最主动」，打 4.5 分，仅次于 Muse。但 WIRED 的同日横测把它评为「最烦人」。（[持续执行]({{< relref "/docs/instinct/analysis/continuous-execution" >}})、[实际效果与可靠性]({{< relref "/docs/instinct/analysis/reliability" >}})）
- **安全记录最受质疑。** 内测期被测出容易被钓鱼、未经确认代发邮件；之后的实测里仍有越权发信、违背指令取消订单。能确认的审批只有付款。创始人称有独立的安全防火墙和守门人系统，这是自述。（[安全]({{< relref "/docs/instinct/analysis/security" >}})）
- **数据给得多，删得难。** 接入邮件、日历、消息应用，内测期条款还包括设备屏幕和键盘输入；邮件以纯文本保存，断开后不自动删除。条款允许用部分对话训练模型。（[记忆与上下文]({{< relref "/docs/instinct/analysis/memory" >}})、[隐私]({{< relref "/docs/instinct/analysis/privacy" >}})）
- **免费与邀请制是一体的。** 对用户免费、没有公布定价；每人 5 个邀请名额，邀请码被炒到 200 到 300 美元。创始人称限制开放是因为算力成本每周翻倍。（[开放与价格]({{< relref "/docs/instinct/analysis/access-pricing" >}})）
- **自研推理管线降本。** 底层模型未披露；创始人称自研的混合推理管线接近 Opus 5 级别，批处理使吞吐提高 3 到 8 倍，这是免费的前提。（[模型]({{< relref "/docs/instinct/analysis/models" >}})）
- **估值建立在交易入口的设想上。** 14 人团队，五个月四轮融资到 100 亿美元估值；创始人自述年化 GMV 接近 10 亿美元、40% 用户绑定主信用卡，计划向商家收佣金，但据转引的 Sacra 记录目前没有收入。（[商业与规模]({{< relref "/docs/instinct/analysis/business" >}})）
- **商家侧接入刚起步。** 2026-10 成为 Poppy 协议首批设计伙伴、Shop Pay 首批接入智能体，温德姆点名开放库存；同时亚马逊等平台在拦截智能体。（[连接器]({{< relref "/docs/instinct/analysis/connectors" >}})）

## 定位

官网称 Instinct 是「理解你正在做什么、什么对你重要的个人助理」，「没有新的界面」（[官网首页]({{< relref "/docs/instinct/sources/official/2026-11-05-instinct-homepage" >}})）。创始人 Noah Shinn 称它不是又一个工具，而是代替用户行动的「日常智能」，「最好的 Agent 应该尽可能没有界面」；他认为 Muse 是功能丰富的 AI 原生 App，Instinct 则让 App 本身消失（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。他把它比作 Apple Pay 或美国运通那样的交易分发与结算网络，主要面向预订、旅行类交易（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。

在跟踪的产品里，Instinct 与 [Poke]({{< relref "/docs/poke/analysis" >}}) 同属「住在消息应用里」的独立创业公司产品，与 Muse、Dots、Gemini Spark 这类依托大平台的产品不同。中金把它和 Manus Cue 归为「跨平台独立助手」，优势是跨生态整合、利益相对中立，劣势是缺少流量入口、受平台授权限制（[中金：消费级 AI 的破晓时分]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})）。飞雪谈AI 称它是「通信入口型」，尝试成为消费者决策和交易的入口（[飞雪谈AI：对比分析与趋势]({{< relref "/docs/industry/sources/community/2026-10-16-feixue-personal-agent-comparison" >}})）。TechCrunch 9 月称它是文本类 AI 助理中最受欢迎的之一（[TechCrunch：Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}})）。

各家横评的排位：Top5Apps 第二（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})），潮涌AI 全球创业公司 Top15 第一（[潮涌AI：全球 Top15]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})），Enterpret 用户声量榜 12 款中第六（[Enterpret：12 款个人智能体用户排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})），一位美国投资人用的四款中排第四（[特工宇宙：投资人用四款 Agent]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})），WIRED 同日横测「最烦人」（[WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-02 | 推出非公开测试版（据 The Information） | [WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}}) |
| 2026-04 | 种子轮，估值约 5000 万美元（据 Forbes） | [潮涌AI：全球 Top15]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}}) |
| 2026-08 初 | A 轮 7500 万美元，估值 5 亿美元 | [潮涌AI：全球 Top15]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}}) |
| 2026-08-21 至 22 | 内测用户在 X 上集中质疑隐私与安全 | [TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}}) |
| 2026-08-24 | TechCrunch 报道争议；B 轮 2.5 亿美元（另有 3.5 亿美元的说法），估值 25 亿美元 | [TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})、[TechCrunch：Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}}) |
| 2026-09-09 前后 | 助理专属邮箱；可信网络 | [TechCrunch：短信类智能体合集]({{< relref "/docs/industry/sources/media/2026-10-24-techcrunch-text-message-agents" >}})、[TechCrunch：Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}}) |
| 2026-09-16 | Instinct Concierge（代打电话）早期体验 | [TechCrunch：Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}}) |
| 2026-09-24 | WIRED 长期使用记录 | [WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}}) |
| 2026-09-28 | C 轮 10 亿美元，估值 100 亿美元；创始人首次长访谈（Colossus 播客） | [SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})、[播客 Invest Like the Best]({{< relref "/docs/instinct/sources/media/2026-09-28-colossus-invest-like-the-best" >}}) |
| 2026-09-29 | Selections，第一次收入实验（潮涌AI 称） | [潮涌AI：全球 Top15]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}}) |
| 2026-10-05 | 群聊，先向早期访问用户开放 | [TechCrunch：群聊上线]({{< relref "/docs/instinct/sources/media/2026-10-05-techcrunch-group-chats" >}}) |
| 2026-10-06 | 成为 Poppy 协议首批设计伙伴 | [Poppy 协议发布]({{< relref "/docs/industry/sources/community/2026-10-06-introducing-personal-agent-protocol" >}}) |
| 2026-10-17 | Android Authority 一个月使用记录 | [Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}}) |
| 2026-10-22 | 温德姆点名 Instinct 等智能体可预订其酒店 | [Skift：温德姆开放库存]({{< relref "/docs/industry/sources/media/2026-10-22-skift-wyndham-ai-booking-agents" >}}) |
| 2026-10-27 | WIRED 六款智能体横测，评为「最烦人」 | [WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}}) |
| 2026-10-28 | Shop Pay 结账进入四款个人智能体，含 Instinct | [Shop Pay 进 Muse]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}}) |
| 2026-11-13 | Poppy 1.0 发布，Instinct 列于首批设计伙伴 | [Poppy 1.0 发布]({{< relref "/docs/industry/sources/community/2026-11-13-releasing-personal-agent-protocol-1-0" >}}) |

## 整体架构

用户在 iMessage、WhatsApp、短信里给 Instinct 发消息，或者打电话、转发邮件（[交互渠道]({{< relref "/docs/instinct/analysis/channels" >}})）。Instinct 接入用户的邮件、日历、消息应用，用户可以再授权银行账户；邮件以纯文本存下来以备检索，偏好记一次长期复用（[记忆与上下文]({{< relref "/docs/instinct/analysis/memory" >}})）。执行时，它用云端自己的手机和电脑像人一样打开网站和应用，用自己的邮箱注册账号，网站不支持时打电话或发 WhatsApp（[运行环境]({{< relref "/docs/instinct/analysis/runtime" >}})、[连接器]({{< relref "/docs/instinct/analysis/connectors" >}})）。后台任务批处理运行，它会主动跟进用户丢下的事，急事打电话提醒（[持续执行]({{< relref "/docs/instinct/analysis/continuous-execution" >}})）。付款走一次性 Stripe Link 卡或 Shop Pay，需用户确认；其他对外动作的审批规则没有公开（[安全]({{< relref "/docs/instinct/analysis/security" >}})）。整个服务对用户免费，靠融资和自研推理管线支撑，计划向商家收佣金（[模型]({{< relref "/docs/instinct/analysis/models" >}})、[商业与规模]({{< relref "/docs/instinct/analysis/business" >}})）。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境]({{< relref "/docs/instinct/analysis/runtime" >}}) | 云端自己的手机和电脑，像人一样操作网站；后台批处理；算力成本每周翻倍，是不开放注册的原因 |
| [记忆与上下文]({{< relref "/docs/instinct/analysis/memory" >}}) | 接入邮件、日历、消息应用和银行账户；邮件纯文本保存，断开后不自动删除；InfoQ 称记忆用 Git 管理 |
| [持续执行]({{< relref "/docs/instinct/analysis/continuous-execution" >}}) | 主动跟进被评为长处；横测中未发现日程冲突；没有公开的触发机制 |
| [连接器]({{< relref "/docs/instinct/analysis/connectors" >}}) | 不靠插件，模拟人操作，走不通就打电话；自己的邮箱；Poppy、Shop Pay、温德姆；亚马逊拦截 |
| [交互渠道]({{< relref "/docs/instinct/analysis/channels" >}}) | 没有 App，iMessage、短信、WhatsApp、电话、邮件；Concierge 代打电话；群聊；形态评价两极 |
| 设备 | 资料不足，不单独成页。没有专用硬件和独立 App；创始人称普通 AirPods 就能承载语音交互，有用户把它绑在 iPhone 的 Action Button 上（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）；内测期条款允许接收用户设备的屏幕截图和键盘输入（[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})），但没有资料描述用户端客户端 |
| [模型]({{< relref "/docs/instinct/analysis/models" >}}) | 底层模型未披露；创始人称自研混合推理管线接近 Opus 5 级别、吞吐提高 3 到 8 倍 |
| [安全]({{< relref "/docs/instinct/analysis/security" >}}) | 容易被钓鱼、越权发信、违背指令；只有付款有明确审批；创始人自述的防火墙与守门人系统 |
| [隐私]({{< relref "/docs/instinct/analysis/privacy" >}}) | 内测期「永久且不可撤销」的许可；用对话训练；广告说法矛盾；群聊中非用户的数据处理未说明 |
| [开放与价格]({{< relref "/docs/instinct/analysis/access-pricing" >}}) | 邀请制、免费、未公布定价；邀请码被炒卖；限美国、18 岁以上 |
| [商业与规模]({{< relref "/docs/instinct/analysis/business" >}}) | 14 人、100 亿美元估值；创始人自述 GMV 与绑卡率；佣金模式，目前无收入；多处数字口径不一 |
| [实际效果与可靠性]({{< relref "/docs/instinct/analysis/reliability" >}}) | 长期使用偏正面，同日横测偏负面；失误集中在不经确认对外行动；没有完成率数据 |

## 资料缺口

- **官方资料极少。** 资料库中唯一的官方资料是官网首页；公司没有博客、帮助中心或文档站，公告发在 X（[官网首页]({{< relref "/docs/instinct/sources/official/2026-11-05-instinct-homepage" >}})）。功能说明、条款、隐私政策都要靠媒体和用户转述。
- **创始人访谈的原稿。** 大量数字（GMV、留存、降本倍数）来自 Z Finance 的中文整理稿，Colossus 播客原稿只有节选；「1300 美元月均消费」查不到出处。
- **现行服务条款与隐私政策原文**，以及训练默认设置、删除流程。
- **审批规则与安全机制的官方说明**，内测期问题是否修复。
- **运营数据的独立来源**：用户数、收入、B 轮金额（2.5 亿还是 3.5 亿美元）、公司成立时间。
- **公开开放与定价**：Selections 是什么，何时公开开放。
