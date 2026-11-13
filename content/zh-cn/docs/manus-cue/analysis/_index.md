---
title: "Manus Cue 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Cue 是 Manus（Butterfly Effect）2026-09-28 随 Manus 2.0 推出的独立应用，给每个个人智能体一套自己的邮箱、电话号码、钱包和云电脑，以智能体自己的身份替用户办事；分析覆盖截至 2026-11-10 收集的 10 篇 Cue 资料和 16 篇涉及 Cue 的行业资料。
---

## 概要

- Cue 的核心主张是给智能体独立身份：每个智能体有 `@bot.cue.im` 邮箱、可选的付费电话号码、Stripe Link 钱包和一台云电脑，以自己的名义对外沟通。行业资料普遍称这是同期产品中「最激进」「走得最远」的路线。（[交互渠道](channels/)）
- 智能体在自己的云电脑上运行，关掉应用仍在跑。实测到的是 Ubuntu 虚拟机，配置与出口 IP 因人而异，IP 常落在非主要西方国家。（[运行环境](runtime/)）
- 用户在像即时通信软件的应用里管理多个智能体，可单聊、拉群分工，也可经 iMessage、Telegram、LINE、Slack 联系，或扫商家二维码生成专用智能体。群聊在唯一的详细实测中表现不佳。（[交互渠道](channels/)）
- 持续执行靠自动化（定时或按事件）加智能体自己的邮箱和电话收信息；实测认为「蹲守」类任务最有价值，问题在建任务时的确认环节。（[持续执行](continuous-execution/)）
- 付款每笔批准、在预算内、不存凭证；其他动作的审批规则靠对话设定，没有设置开关。没有官方安全说明，也没有针对 Cue 的漏洞报道。（[安全](security/)）
- 截至 2026-11-10 仍是邀请制抢先体验，获得资格免费附带 Plus；电话号码、Cloud Computer 和 Pro、Max 档位另行收费。官方没有定价页，电话价格有 0.99、9.9、9.99 美元三种说法。（[开放与价格](access-pricing/)）
- 资料很薄：只有两份实测（都在发布次日），没有任何用户规模数据，官网首页因技术原因未收。反馈集中在价格、电话、IP 等落地摩擦，而非任务成功率。（[实际效果与可靠性](reliability/)、[商业与规模](business/)）

## 定位

发布文称 Cue 是「一款新的独立应用，用来管理你的个人智能体」，可在手机和桌面上使用，构建在与 Manus 相同的基础设施之上；每个智能体都有自己的电子邮件、电话号码、钱包和电脑（[Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})）。帮助中心称它是「供个人智能体团队使用的独立应用」，也可以只留一个个人助理做跑腿、提醒、调研（[帮助：Manus 2.0 新功能]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-what-is-new-in-manus-2-0" >}})）。应用商店的定位是线上线下的日常任务助手，从点咖啡、规划旅行到安排一天和辅助学习（[Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})）。

Cue 与 Manus 本体分开：独立应用、独立域名（cue.im），Skills 不互通（[帮助：Skills]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-skills" >}})），电话用量计入 Cue 自己的每周额度、不消耗 Manus credits（[帮助：会员定价]({{< relref "/docs/manus-cue/sources/official/2026-10-23-help-membership-pricing" >}})）。xiangxiang103 的概括是「Cue 负责生活，Manus 本体负责干活」（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。肖弘把 Manus 比作「卖电脑的生意」，财经涂鸦认为 Cue 把出售计算资源与持续运行时间的路线推向个人智能体（[财经涂鸦]({{< relref "/docs/manus-cue/sources/media/2026-09-29-caijingtuya-xiaohong-on-cue" >}})）。

Cue 是 Manus 被 Meta 收购、交易遭中国监管叫停、2026-09-01 恢复独立后推出的第一款新产品，硅星人称它是「一款要和 Muse 抢用户的产品」（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）。

第三方资料中与其他跟踪产品的主要差异：

| 对比对象 | 差异 | 资料 |
| --- | --- | --- |
| Meta Muse | Muse 是用用户账号办事的「分身」、一个长期了解用户的主助手；Cue 是有独立身份、可拉群分工的「一群员工」，多个固定职责的助手放在前台。发布次日 Muse 打电话仍用用户号码，Cue 有专属号码 | [xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})、[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}}) |
| Muse、Dots、Gemini Spark | 中金把它们归为依托既有平台的「平台型助手」，Cue 与 Instinct 是「独立型助手」，优势在跨生态与利益对齐，劣势是缺入口、服务成本高；鸿煊把前者归为「接入现有生态」路线，Cue 归为「独立身份」路线 | [中金]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}}) |
| Instinct | 都是独立创业产品；Instinct 没有独立应用，只走短信、电话、iMessage、WhatsApp，Cue 是独立应用并给智能体发独立身份 | [AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}}) |

AIX财经称各家对 Personal Agent 定义不一，「Cue 给出的定义最激进」：一个有独立手机号、邮箱、支付和电脑的智能体（[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。AI新榜、Datawhale、阿言er 都把「独立身份」看作 Cue 区别于同期产品的核心（[AI新榜]({{< relref "/docs/industry/sources/media/2026-10-12-aixinbang-do-people-need" >}})、[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[阿言er]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2025-12 | Manus 宣布 ARR 突破 1 亿美元；宣布加入 Meta | [硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})、[潮涌]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}}) |
| 2026-04 | 收购被中国监管叫停 | [硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})、[潮涌]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}}) |
| 2026-09-01 | Manus 宣布恢复独立运营 | [硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}}) |
| 2026-09-08 | Meta 发布 Muse（对照） | [AI新榜]({{< relref "/docs/industry/sources/media/2026-10-12-aixinbang-do-people-need" >}}) |
| 2026-09-28 | 随 Manus 2.0 发布 Cue：网页、桌面、Android，iOS 待审；抢先体验，公共邀请码 MEETCUE；当晚 Manus 称将组建团队开发国内产品 | [Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})、[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}}) |
| 2026-09-29 | OpenAI 发布 Dots（对照）；xiangxiang103、硅星人发表首批实测 | [K姐]({{< relref "/docs/industry/sources/community/2026-10-20-kjie-mismatched-business" >}})、[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})、[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}}) |
| 2026-10-01 | 帮助中心 Manus 2.0 页列出 Cue；Skills 与 Manus 分开 | [帮助：Manus 2.0 新功能]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-what-is-new-in-manus-2-0" >}})、[帮助：Skills]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-skills" >}}) |
| 2026-10-08 | 帮助文档：Cue 支持 iMessage、Telegram、LINE、Slack；Manus 据报完成超 5 亿美元融资 | [帮助：多个消息平台]({{< relref "/docs/manus-cue/sources/official/2026-10-08-help-multiple-messaging-platforms" >}})、[潮涌]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}}) |
| 2026-10-23 | 帮助文档：电话号码单独订阅，计入 Cue 每周额度 | [帮助：会员定价]({{< relref "/docs/manus-cue/sources/official/2026-10-23-help-membership-pricing" >}}) |
| 2026-11-04 | Google Play 介绍删去「视可用情况而定」 | [Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}}) |
| 2026-11-05 | 美国区 App Store 已上架 iOS 版，内购列出五国号码、Pro、Max、Cloud Computer | [App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}}) |
| 2026-11-09 | 社区称仍为邀请制内测 | [AI问消]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}}) |

## 整体架构

用户在 Cue 应用（Android、iOS、M 系列 Mac，网页版说法不一）里新建一个个智能体，给每个指定职责；应用像即时通信软件，可以单聊、拉群，也可以把智能体接到 iMessage、Telegram、LINE、Slack（[交互渠道](channels/)）。每个智能体有自己的资料页，指令、记忆、文件、自动化按智能体组织（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）。

每个智能体在一台云端 Linux 电脑上运行，用户可以在应用里看它操作，关掉应用它继续工作（[运行环境](runtime/)）。它对外用自己的身份：@bot.cue.im 邮箱、可选的电话号码、Stripe Link 钱包；用户自己的 Gmail、日历等通过连接器授权（[连接器](connectors/)）。它按自动化的时间表或事件运行，也通过自己的邮箱和电话接收外部信息并转告用户（[持续执行](continuous-execution/)）。付款每笔需批准，其他审批规则在对话中设定（[安全](security/)）。用量按周计算，电话和云电脑另行收费（[开放与价格](access-pricing/)）。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境](runtime/) | 每个智能体一台云端电脑，与 Manus 共用基础设施；实测为 Ubuntu 虚拟机，配置与出口 IP 因人而异，IP 问题影响注册和验证 |
| 记忆与上下文 | —。资料不足：应用商店介绍称「Memory and Dream」帮 Cue 记住饮食偏好、出行习惯、学习进度和想坚持的计划，用户回来时从中断处继续（[Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})、[App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})）；记忆按智能体组织（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）；实测中群聊与私聊记忆不互通，审批规则通过对话记入（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）；Skills 与 Manus 不互通（[帮助：Skills]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-skills" >}})）。记忆如何形成、能否查看和删除，资料没有说明 |
| [持续执行](continuous-execution/) | 自动化按时间表或事件运行，邮箱和电话收信息；蹲守任务实测有效，建任务时会口头答应却没建 |
| [连接器](connectors/) | 有 Gmail、日历、GitHub、Shopify 等连接器，钱包走 Stripe Link（仅美国），Skills 与 Manus 分开；机制与授权粒度未说明 |
| [交互渠道](channels/) | 每个智能体有 @bot.cue.im 邮箱和付费电话号码（仅语音），邮件带「Sent on behalf of」页脚；应用内单聊、群聊，另有四个消息平台和扫码入口 |
| 设备 | —。资料不足：发布时有网页、桌面、Android，iOS 待审（[Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})）；2026-11-05 美国区 App Store 已上架，要求 iOS 18，可在 M1 及以上 Mac 和 Vision Pro 上运行（[App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})）；9-29 实测 Mac 版仅 M 系列，Windows「即将推出」，网页版找不到登录入口（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。没有专用硬件 |
| 模型 | —。资料不足：资料库中没有 Cue 使用什么模型的任何说明，AI问消称「模型用的谁家的没说」（[AI问消]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}})）。Manus 2.0 的 Cascade 架构是否用于 Cue，资料没有说明 |
| [安全](security/) | 付款每笔批准、预算内、不存凭证；其他审批靠对话设定；独立身份避免交出用户账号，但身份可识别、易被风控封号；无漏洞报道 |
| 隐私 | —。资料不足：没有 Cue 的隐私政策、训练用途、保存期限或通话对象信息处理的资料（App Store 的 App Privacy 栏收集时未收，见 [App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})）。xiangxiang103 认为独立邮箱的好处是用户不必交出自己的邮箱地址（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})） |
| [开放与价格](access-pricing/) | 邀请制抢先体验，免费附带 Plus；电话、云电脑、Pro、Max 另收费；无官方定价页，电话价格三种说法 |
| [商业与规模](business/) | Cue 无规模数据，社交声量份额 0.5%；「卖电脑的生意」；Manus 恢复独立后的产品，对标 Muse |
| [实际效果与可靠性](reliability/) | 只有发布次日的两份实测；邮箱、云电脑、蹲守能用，「说完成不等于完成」，群聊需要用户主导；反馈集中在落地摩擦 |

## 资料缺口

- **实测**：只有 2026-09-29 的两份；没有用户自己的实测（`exploration/` 为空），没有发布一个月以上的复测；电话代接、扫码点单、付款、四个消息平台都没有实测。
- **官网**：cue.im 首页是单页应用，六十多个示例任务只能经 xiangxiang103 转述看到；官网常见问题未收。
- **定价**：官方定价页、各档位额度与计费周期、电话价格变化的说明。
- **技术**：云电脑规格与持久化、出口 IP 规则、使用的模型、连接器机制。
- **安全与隐私**：官方安全说明、隐私政策、数据用途与保存期限、通话对象信息处理。
- **规模**：用户数、邀请发放进度、收入；Manus 公司数字的一手出处。
- **中文实测**：腾讯云开发者社区「Cue 的第一轮实测」等收集阶段未取得的文章。
