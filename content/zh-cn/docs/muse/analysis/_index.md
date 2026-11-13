---
title: "Meta Muse 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Meta Muse 是独立 App 形态、免费起步、每个用户一台云端虚拟机的消费级个人智能体，主攻生活杂事和购物；分析覆盖截至 2026-11-12 收集的 125 篇 Muse 资料和 64 篇涉及 Muse 的行业资料。
---

## 概要

- Muse 给每个用户一台隔离的云端 Linux 虚拟机（Muse Secure VM），智能体框架和工具跑在虚拟机内的运行时单元里，凭证、Sentinel 审查等服务放在单元之外。这套环境对用户相当透明，可以查看文件、接管浏览器，甚至打包导出整个文件系统，相应也带来了安全问题。（[运行环境](runtime/)）
- 记忆以 Markdown 文件为源头，由每小时、每晚的后台任务形成，用户可以查看和编辑。接入的个人数据比同类产品宽，Meta 自家社交数据是最大的区别。但删除内容后 Muse 可能仍然记得，记忆没有关闭开关，为联系人（包括非用户）维护的「人物页」是最大的争议。（[记忆与上下文](memory/)、[隐私](privacy/)）
- 「主动」止于发现、准备、提醒：周期任务、目标、后台更新的 Spaces 可以在用户离开后运行，但购买、发送等写操作不能预先或批量批准。（[持续执行](continuous-execution/)）
- 外部服务有四条接入路径：审核上架的目录连接器、Muse 现场生成的自定义连接器、虚拟机内的浏览器、Mac/安卓/Gadget 本地接入。生态扩张快，第三方申请不到一周超过 1,500 份；浏览器路线则招来亚马逊、摩根大通、嘉信和加拿大五大银行的封堵。（[连接器](connectors/)）
- 入口是独立的 Muse App、网页和 WhatsApp，之后扩展到 Mac、眼镜 Beta、语音与化身、手表和自有邮箱 Muse Mail；专用硬件 Muse Charm 已宣布未发货。（[交互渠道](channels/)、[设备](devices/)）
- 门槛在跟踪产品中最低：一个 Meta 账户即可免费使用，付费档 Power 每月 20 美元、Maximum 每月 100 美元，按每周令牌额度区分。截至 2026-11-12 已开放美国、加拿大、日本、新加坡、墨西哥五国。（[开放与价格](access-pricing/)）
- 规模领先、单位经济未证实：据 Meta Q3 财报电话会，上线约六周美加超过 1000 万人完成设置；长期收入押在向商家收取交易费上，费率未公布，第三方估算的单用户成本高于 20 美元的订阅价。（[商业与规模](business/)）
- 官方的安全架构在同类产品中公开得最系统，但没有独立审计；上线两个月内资料记录了至少六起漏洞和事件。实测评价分歧大，日常杂事表现好，多步骤业务流程和「说做了实际没做」是反复出现的问题。（[安全](security/)、[实际效果与可靠性](reliability/)）

## 定位

官方把 Muse 称为「全球首个面向所有人打造的个人 AI 智能体」，强调「没有学习门槛」，并把它定为迈向 Zuckerberg「个人超级智能」愿景的第一步（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})）。设计文章说，Muse 从「助手」演进为「智能体」：一个主对话、主动、有头像和个性，系统提示词第一行是「Your purpose is to make your user's life better」（[设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。

据 Alexandr Wang 的访谈转述，Meta 没有跟进编程智能体，而选择做消费级个人智能体，理由是 Meta「最擅长的事情始终是做消费级产品」（[36 氪：Wang 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-12-36kr-wang-openclaw-origin" >}})、[Wang 谈 Muse 是怎么做出来的]({{< relref "/docs/muse/sources/media/2026-11-03-wang-how-muse-was-built" >}})）。Muse 与 OpenClaw 的关系被反复讨论：Nat Friedman 称 Muse 代码从零构建，但产品「深受 OpenClaw 启发」；Alex Heath 称它「本质上就是给普通人用的 OpenClaw」（[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})、[Sources：Zuckerberg 谈 Muse]({{< relref "/docs/muse/sources/media/2026-09-08-sources-zuckerberg-on-muse" >}})）。

Muse 与 Meta 的既有业务深度绑定：连接 Facebook、Instagram、Messenger、Marketplace，经 WhatsApp 使用，小企业版接入 Meta 的商家和广告工具（[Muse for Small Business]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}})）。Muse App 与 Meta AI App 是彼此独立的产品，底层模型系列共用（[眼镜 Beta 帮助]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})、[特化模型]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})）。

与其他跟踪产品相比，媒体和社区资料中的主要差异是：

| 对比对象 | 差异 | 资料 |
| --- | --- | --- |
| OpenAI Dots | Dots 内置 ChatGPT、100 美元起、偏工作；Muse 独立 App、免费起步、偏生活杂事和购物。Tom's Guide 认为「最大的区别不是模型——而是客户」 | [Tom's Guide]({{< relref "/docs/industry/sources/media/2026-09-30-tomsguide-muse-vs-dots" >}})、[DataCamp]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})、[Engadget]({{< relref "/docs/industry/sources/media/2026-10-11-engadget-dot-vs-muse" >}}) |
| Grok Bot | 多位作者认为 Grok Bot 更像一人公司的工作团队，Muse 对生活场景优化更好 | [Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})、[海外独角兽讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}}) |
| Claude Duet | Duet 仅限受邀的美国 Pro/Max 用户、浏览器不可见；Muse 免费、多国开放、可观看和接管 | [aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}}) |
| Instinct | 都被称为「最火」的产品；Instinct 无 Meta 的分发和算力，靠邀请制口碑增长 | [明亿：产业链]({{< relref "/docs/industry/sources/community/2026-10-31-mingyi-personal-agent-industry-chain" >}})、[TOP5]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) |
| Today、灵光 | 国内媒体称 Today 为「中国版 Muse」，蚂蚁灵光 2.0 被官方定位为对标 Muse | [爱心榜]({{< relref "/docs/industry/sources/media/2026-10-12-aixinbang-do-people-need" >}})、[AI 故事计划：二线厂]({{< relref "/docs/industry/sources/media/2026-11-05-aigushijihua-second-tier-personal-agent" >}}) |

Wired 的六款同场评测把 Muse 评为「最易上手」，Dots 为「最佳整体」（[Wired：所有主要智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。国内资料的常见判断是：Muse 的价值在入口而非基准分数，美国服务分散、人力成本高，Muse 式产品是「真刚需」，在超级 App 集中的中国则存在感低（[ZFinance]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})、[甲子光年]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-04 | 漏洞赏金计划开始非公开覆盖 Muse | [漏洞赏金回顾]({{< relref "/docs/muse/sources/official/2026-11-02-securing-muse-bug-bounties" >}}) |
| 2026-08-27 | 据 404 Media，Meta 内部启动针对 KVM 逃逸的加固冲刺 | [404 Media：上线前的 VM 逃逸]({{< relref "/docs/muse/sources/media/2026-10-05-404media-vm-escape-before-launch" >}}) |
| 2026-09-08 | 发布：美国，iOS、Android、muse.ai、WhatsApp；Muse Spark 驱动，Secure VM、Sentinel，漏洞赏金公开；Confidential VM「今年晚些时候」 | [推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}}) |
| 2026-09-18 | 加拿大上线（据墨西哥上线报道；海峡时报称美加 9-08 同时首发）；登顶美国 App Store 免费榜 | [墨西哥上线]({{< relref "/docs/muse/sources/media/2026-11-05-muse-launches-mexico" >}})、[海峡时报]({{< relref "/docs/muse/sources/media/2026-10-28-straits-times-muse-singapore" >}}) |
| 2026-09-20 | 亚马逊屏蔽 Muse 购物 | [GeekWire]({{< relref "/docs/muse/sources/media/2026-09-20-geekwire-amazon-blocks-muse" >}}) |
| 2026-09-21 | Patrick Wardle 披露 macOS 客户端零日，Meta 约一天内修复 | [Wardle]({{< relref "/docs/muse/sources/community/2026-09-21-wardle-not-a-mused" >}})、[Ars Technica]({{< relref "/docs/muse/sources/media/2026-09-21-arstechnica-muse-zero-day" >}}) |
| 2026-09-23 | Connect：语音与实时化身、Mac 计算机操作、Muse Mail、AI 眼镜、更多连接器，展示 Muse Charm | [Connect 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[让你的 Muse 栩栩如生]({{< relref "/docs/muse/sources/official/2026-09-23-bringing-your-muse-to-life" >}}) |
| 2026-09-24 | 用户让 Muse 导出整个文件系统，Verge 报道 | [Verge]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}}) |
| 2026-09 下旬 | Marketplace 住址泄露事件 | [卫报]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}}) |
| 2026-09-29 | Muse for Small Business | [Muse for Small Business]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}}) |
| 2026-10-03 | Wired 报道 Muse 为亲友建档（Relationships 任务） | [Wired]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}}) |
| 2026-10-12 | Muse Wonder 与 Muse Wonder Full 发布，Wonder「首先面向订阅用户」 | [推出 Muse Wonder]({{< relref "/docs/muse/sources/official/2026-10-12-introducing-muse-wonder-models" >}}) |
| 2026-10-20 至 10-22 | 分享链接可经被动 DNS 枚举，分享功能暂停后恢复 | [Ars Technica]({{< relref "/docs/muse/sources/media/2026-10-20-arstechnica-shared-conversations-exposed" >}})、[Verge]({{< relref "/docs/muse/sources/media/2026-10-22-verge-muse-sharing-back-on" >}}) |
| 2026-10-21 | Meta Q3 财报电话会：美加超 1000 万人设置 Muse（转述） | [Muse 101]({{< relref "/docs/muse/sources/community/2026-11-04-muse-101-agentic-commerce" >}}) |
| 2026-10-23 | 日本上线 | [日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}}) |
| 2026-10-27 | 新加坡上线（官方稿日期；海峡时报写 10-28）；眼镜 Beta 帮助页 | [新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}})、[眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}}) |
| 2026-11-02 | 漏洞赏金回顾：630 多份提交、64 项有效发现、已付超过 100 万美元 | [漏洞赏金回顾]({{< relref "/docs/muse/sources/official/2026-11-02-securing-muse-bug-bounties" >}}) |
| 2026-11-04 | 连接器开发者指南、Gadgets、Home Link 页面（收集日期） | [连接器指南]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})、[Home Link]({{< relref "/docs/muse/sources/official/2026-11-04-muse-home-link" >}}) |
| 2026-11-05 | 语音与化身向美国全体用户推出；墨西哥上线 | [给你的 Muse 一个声音]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}})、[墨西哥上线]({{< relref "/docs/muse/sources/media/2026-11-05-muse-launches-mexico" >}}) |
| 2026-11-06 | Spaces 上线；向 Muse 与 Meta AI 推送用 Wonder 训练的特化模型 | [Spaces]({{< relref "/docs/muse/sources/official/2026-11-06-design-muse-app-spaces" >}})、[特化模型]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}}) |
| 2026-11-09 | Apple Watch 与 Wear OS；The Times 称数周内进入英国；印度卢比定价 | [TechCrunch]({{< relref "/docs/muse/sources/media/2026-11-10-techcrunch-muse-apple-watch-wear-os" >}})、[The Times]({{< relref "/docs/muse/sources/media/2026-11-09-times-muse-uk-launch" >}})、[印度定价]({{< relref "/docs/muse/sources/media/2026-11-09-india-pricing-ahead-of-launch" >}}) |
| 2026-11-10 至 11-11 | Muse Mail 向美加付费用户开放，Wang 称将开放给免费档；Uber Courier 接入 | [Muse Mail 付费用户]({{< relref "/docs/muse/sources/media/2026-11-10-muse-mail-paid-subscribers" >}})、[Muse Mail 免费档]({{< relref "/docs/muse/sources/media/2026-11-11-muse-mail-free-plans-soon" >}})、[Uber Courier]({{< relref "/docs/muse/sources/media/2026-11-10-uber-courier-deliveries" >}}) |

## 整体架构

每个用户的 Muse 运行在一台 Meta 托管的云端虚拟机上：智能体框架和工具在运行时单元内，凭证服务、安全分类器、Sentinel 和推理代理在单元外。Mac 应用和安卓手机可以作为本地执行端，Gadgets SDK 和 Home Link 用来接入家中设备。

上下文来自主对话、记忆文件和后台任务整理出的人物页；数据通过目录连接器、自定义连接器、浏览器登录和本地设备接入，Meta 自家的 Facebook、Instagram、Marketplace 数据是一大来源。

工作的触发方式有三种：用户在 App、网页、WhatsApp、语音或手表上发起请求；提醒、周期任务和目标；系统自带的后台作业（记忆整理、做梦、信息流推送）。

连接器操作和网络出站都要经过 Sentinel；写操作默认需要用户批准，非敏感工具可以设为「始终允许」，连接器指南把购买、发邮件等敏感写入限定为每次批准。付款使用绑定商家、金额和时限的一次性卡号。

大部分功能免费，按每周令牌额度区分免费档和 Power、Maximum 两个付费档；新模型、Muse Mail、Home Link 等新功能往往先给付费用户。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境](runtime/) | 每个用户一台隔离的云端虚拟机，用户实测为 2 vCPU、8 GB，空闲即回收，只有用户盘保留；Confidential VM 截至 2026-11-12 未上线 |
| [记忆与上下文](memory/) | 记忆是可查看、可编辑的 Markdown 文件，由后台任务形成；遗忘有限，只能重置清空 |
| [持续执行](continuous-execution/) | 提醒、周期任务、目标、Spaces 在后台运行；写操作不能预先批准，复杂任务有「报告已做实际没做」的情况 |
| [连接器](connectors/) | 四条接入路径，生态扩张快；浏览器路线招致亚马逊和多家银行封堵，Meta 推动 Personal Agent Protocol |
| [交互渠道](channels/) | 独立 App、网页、WhatsApp 加语音、手表、Muse Mail；对外以用户名义沟通，多处未标明是 AI |
| [设备](devices/) | 手机、Mac、手表已上线，眼镜处于 Beta，Muse Charm 未发货；Gadgets SDK 开源 |
| [模型](models/) | 由自研 Muse Spark 驱动，Muse Wonder 先给订阅用户，11 月起推送特化模型；用户不能自选 |
| [安全](security/) | Sentinel、凭证隔离、一次性卡号，架构公开最系统但无独立审计；两个月内至少六起事件（[事件详情](security/incidents/)） |
| [隐私](privacy/) | 默认用于训练、可关闭；承诺不进广告系统；为非用户建人物页是最大争议 |
| [开放与价格](access-pricing/) | 免费起步，Power 20 美元、Maximum 100 美元；五国开放，英国、印度在即 |
| [商业与规模](business/) | 美加超 1000 万人设置；押注交易费，单位经济未证实，交易流量尚小 |
| [实际效果与可靠性](reliability/) | 排名分歧大，生活杂事好、多步骤业务流程差；没有官方完成率，11-04 有一次未公告的停运 |

## 资料缺口

- Meta 官方的 DAU、MAU、付费人数、订阅收入，以及「1000 万」的具体口径；Q3 财报电话会的一手记录。
- 交易费的费率、适用商家和推出时间，Muse 促成的成交额。
- 隐私政策原文、各类数据的保存期限、各地区的条款和监管动态。
- Muse Confidential VM 的上线时间和技术方案；独立的安全审计。
- 免费档的官方额度，额外令牌的价格，日本和墨西哥的本币价格。
- 官方的完成率、出错率、可用性数据或状态页；数周以上长期使用的稳定性。
- 眼镜 Beta 的开放范围、Muse Charm 的规格和发货时间。
- 部分重要资料只收到链接或节选：Wardle 的 OBTS 演讲、Gmail 收件箱实测、Skift 对 Expedia 的测试（原文截断）。
