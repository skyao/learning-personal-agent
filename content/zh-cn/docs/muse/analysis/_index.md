---
title: "Meta Muse 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  Meta Muse 是独立 App 形态、免费起步、每个用户一台云端虚拟机的消费级个人智能体，主攻生活杂事和购物；本页依据截至 2026-11-28 收集的 273 篇 Muse 资料和 78 篇涉及 Muse 的行业资料，于 2026-11-28 全面重写。
---

## 概要

- **一人一台云端虚拟机，「常驻」的是状态而不是计算。** 智能体框架跑在虚拟机内的容器里，凭证、审批、出站检查 Sentinel 放在容器外；实测中虚拟机空闲几分钟到半小时即被回收，只有一块约 100 GB 的加密用户卷延续。11 月起多了 Chrome 扩展和 Mac 应用两个本地执行面。环境对用户高度开放，可审计，也让攻击面完全公开。（[运行环境]({{< relref "/docs/muse/analysis/runtime" >}})）
- **记忆是可读可改的文件，接入的个人数据在跟踪产品中最宽。** 记忆由每小时、每晚的后台任务形成，Meta 自家社交数据自动接入；为联系人（包括非用户）维护的人物页是最大争议。遗忘官方自称「尽力而为」，记忆没有关闭开关。（[记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})、[隐私]({{< relref "/docs/muse/analysis/privacy" >}})）
- **「主动」止于发现、准备、提醒。** 定时与监控任务实测最稳，调度器在虚拟机之外；购买、发送等写操作不能预先或批量批准。主动消息缺少免打扰之类的硬控制，11 月出现未经请求的幻觉消息和自主代理越界的案例。（[持续执行]({{< relref "/docs/muse/analysis/continuous-execution" >}})）
- **接入路径多，「宣布」「可用」「有成交」之间差距大。** 目录连接器、自定义连接器、云端浏览器、用户自己的 Chrome 四条路径并存；浏览器路线遭亚马逊、银行、eBay、美联航等封堵。Meta 的应对是 Poppy 协议（11-13 发布 1.0）与沃尔玛 Agent Gateway 这类商家自建通道，截至 11-28 都刚起步，黑五前后的已验证成交证据仍少。（[连接器]({{< relref "/docs/muse/analysis/connectors" >}})）
- **入口快速扩张，代发消息时身份就是用户本人。** 从 App、网页、WhatsApp 扩展到 Mac、Chrome、实时语音与化身、Muse Mail、美国付费用户的商家电话和 Instagram 私信；手表和眼镜 Beta 已上线，专用硬件 Muse Charm 仍未发货。代发短信、WhatsApp 时对方无从分辨是 AI，电话的披露规则也未公布。（[交互渠道]({{< relref "/docs/muse/analysis/channels" >}})、[设备]({{< relref "/docs/muse/analysis/devices" >}})）
- **只用 Meta 自研模型，用户不能选。** 发布时是 Muse Spark，10 月推出 Muse Wonder，11 月起推送「用 Wonder 训练的特化模型」；付费档是否直接由 Wonder 运行说法不一。官方评测几乎全是自测，独立基准 ShellBench 中 Wonder Full 位于中游。（[模型]({{< relref "/docs/muse/analysis/models" >}})）
- **门槛最低，开放最快。** 一个 Meta 账户、年满 18 岁即可免费使用，付费档 Power 每月 20 美元、Maximum 每月 100 美元，只按每周令牌额度区分。截至 2026-11-28 已开放美国、加拿大、日本、新加坡、墨西哥、澳大利亚、英国 7 个市场，新功能多按「美国付费用户先行」分批放开。（[开放与价格]({{< relref "/docs/muse/analysis/access-pricing" >}})）
- **规模与份额领先，单位经济与成交未证实。** 官方只公布过一组数字：据 Meta 2026-10-21 Q3 财报电话会，美加超过 1000 万人设置了 Muse；Forter 称 11-19 至 11-25 Muse 占其网络智能体订单的 52%。收入押在向商家收交易费上，费率与开始时间未公布，第三方估算的单用户成本多高于订阅价。（[商业与规模]({{< relref "/docs/muse/analysis/business" >}})）
- **安全架构公开得最系统，但问题也最多。** 上线不到三个月资料记录了 11 起漏洞与事件，第三方研究演示了经 Sentinel「读取」通道静默外传数据的攻击链；没有独立审计。11 月起监管介入：蒙大拿州牵头多州调查，英国 CMA、ICO 在上线前介入，FCA 称 Meta 拒绝联合测试。实测中日常杂事表现好，跨来源核对、网站拦截、「说做了没做」是反复出现的问题；Meta 不公布完成率，也没有状态页。（[安全]({{< relref "/docs/muse/analysis/security" >}})、[隐私]({{< relref "/docs/muse/analysis/privacy" >}})、[实际效果与可靠性]({{< relref "/docs/muse/analysis/reliability" >}})）

## 定位

官方把 Muse 称为面向所有人的个人 AI 智能体，强调没有学习门槛，并把它定为迈向 Zuckerberg「个人超级智能」愿景的第一步（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})）。设计文章说，Muse 从「助手」演进为「智能体」：一个主对话、主动、有头像和个性（[我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。到 11-24 的英国上线稿，官方口径变为「活儿它干，控制权在你」，突出用户掌控与审批（[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})）。

据 Alexandr Wang 的访谈转述，Meta 没有跟进编程智能体，而选择做消费级个人智能体，理由是 Meta 最擅长做消费级产品（[Muse 是玩龙虾玩出来的]({{< relref "/docs/muse/sources/media/2026-10-12-36kr-wang-openclaw-origin" >}})、[Muse 是怎麼做出來的]({{< relref "/docs/muse/sources/media/2026-11-03-wang-how-muse-was-built" >}})）。Muse 与 OpenClaw 的关系被反复讨论：Nat Friedman 称代码从零构建、产品深受 OpenClaw 启发，也有记者称它是「给普通人用的 OpenClaw」（[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})、[Sources：Zuckerberg 谈 Muse]({{< relref "/docs/muse/sources/media/2026-09-08-sources-zuckerberg-on-muse" >}})）。

Muse 与 Meta 既有业务深度绑定：自动连接 Facebook、Instagram、Threads，经 WhatsApp 和 Instagram 私信使用，可在 Marketplace 代卖，小企业版接入 Meta 的商家工具（[Muse for Small Business]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}})、[Muse 进 Instagram 私信]({{< relref "/docs/muse/sources/media/2026-11-24-techcrunch-muse-instagram-dms" >}})、[Marketplace 代卖上线]({{< relref "/docs/muse/sources/media/2026-11-21-muse-sell-facebook-marketplace" >}})）；Meta 在测试让 Muse 跟进用户看到广告之后的行为，见[商业与规模]({{< relref "/docs/muse/analysis/business" >}})。Muse App 与 Meta AI App 是彼此独立的产品，共用模型系列（[帮助：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})、[特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})）。

与其他跟踪产品相比，资料中的主要差异：

| 对比对象 | 差异 | 资料 |
| --- | --- | --- |
| OpenAI Dots | Dots 内置 ChatGPT、偏工作、订阅起步；Muse 独立 App、免费起步、偏生活杂事和购物 | [Tom's Guide：Muse 与 Dots]({{< relref "/docs/industry/sources/media/2026-09-30-tomsguide-muse-vs-dots" >}})、[Dots 与 Muse 横评]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})、[Engadget：Dot 与 Muse]({{< relref "/docs/industry/sources/media/2026-10-11-engadget-dot-vs-muse" >}}) |
| Grok Bot | 多位作者认为 Grok Bot 更像一人公司的工作团队，Muse 对生活场景优化更好 | [Pat Simmons：三方对照]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})、[海外独角兽：PA 社群讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}}) |
| Claude Duet | Duet 仅限受邀的美国订阅用户；Muse 免费、多国开放、可观看和接管 | [AI Agents Library：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[20 美元四智能体对比]({{< relref "/docs/industry/sources/community/2026-11-22-four-agents-twenty-dollars" >}}) |
| Instinct | 同被称为「最火」的产品；Instinct 没有 Meta 的分发和算力，靠邀请制口碑增长 | [明义价值观：穿透 AI 产业链]({{< relref "/docs/industry/sources/community/2026-10-31-mingyi-personal-agent-industry-chain" >}})、[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) |
| Today、灵光 | 国内媒体称 Today 为「中国版 Muse」，灵光 2.0 被定位为对标 Muse | [AI新榜：普通人需要吗]({{< relref "/docs/industry/sources/media/2026-10-12-aixinbang-do-people-need" >}})、[AI故事计划：二线厂更着急]({{< relref "/docs/industry/sources/media/2026-11-05-aigushijihua-second-tier-personal-agent" >}}) |

WIRED 的六款同场评测把 Muse 评为「最易上手」（[WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）；Forter 按真实订单统计，Muse 是智能体购物份额最大的一家（[六款购物智能体排名]({{< relref "/docs/industry/sources/media/2026-11-21-forter-ai-shopping-agents-ranked" >}})）。国内资料的常见判断是：Muse 的价值在入口而非基准分数，美国服务分散、人力成本高，这类产品是刚需；在超级 App 集中的中国存在感低（[Z Finance：齐俊元与伪命题]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})、[甲子光年：是不是好生意]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-09-08 | 在美国发布：iOS、Android、muse.ai、WhatsApp；免费档与 Power、Maximum 订阅；同日公布安全架构与漏洞赏金 | [推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})、[帮助：关于订阅]({{< relref "/docs/muse/sources/official/2026-09-08-help-about-subscriptions" >}}) |
| 2026-09-16 | 商家电话 beta 扩大（美国） | [电话代打 beta 首报]({{< relref "/docs/muse/sources/media/2026-10-05-muse-phone-call-beta" >}})、[Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}}) |
| 2026-09-17 | Mac 应用上线 | [Muse 拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}}) |
| 2026-09-18 | 加拿大上线 | [Muse 登陆澳大利亚]({{< relref "/docs/muse/sources/media/2026-11-17-muse-launches-australia" >}}) |
| 2026-09-20 | 亚马逊开始封堵 Muse 购物（另有资料作 9-21） | [GeekWire：亚马逊屏蔽 Muse]({{< relref "/docs/muse/sources/media/2026-09-20-geekwire-amazon-blocks-muse" >}}) |
| 2026-09-21 | macOS 客户端零日被披露，Meta 数小时内热修复 | [Ars Technica：Muse 零日漏洞]({{< relref "/docs/muse/sources/media/2026-09-21-arstechnica-muse-zero-day" >}}) |
| 2026-09-23 | Connect 2026：宣布眼镜、语音与化身、Muse Mail、Mac 电脑操作、Muse Charm 与零售合作 | [Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[TechCrunch：Connect 上的 Muse]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}}) |
| 2026-09-24 | 用户可让 Muse 导出整个文件系统的报道，Meta 称是预期行为 | [The Verge：下载整个文件系统]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}}) |
| 2026-09-28 | 卫报报道 Marketplace 住址泄露事件 | [卫报：泄露家庭住址]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}}) |
| 2026-09-29 | Muse for Small Business | [Muse for Small Business]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}}) |
| 2026-10-06 | Meta 与 Sierra 宣布 Personal Agent Protocol（Poppy） | [Poppy 协议发布]({{< relref "/docs/industry/sources/community/2026-10-06-introducing-personal-agent-protocol" >}}) |
| 2026-10-12 | 发布 Muse Wonder 模型 | [推出 Muse Wonder（新闻稿）]({{< relref "/docs/muse/sources/official/2026-10-12-introducing-muse-wonder-models" >}}) |
| 2026-10-20 | 分享链接暴露对话，Meta 暂停分享功能 | [Ars Technica：分享链接泄露]({{< relref "/docs/muse/sources/media/2026-10-20-arstechnica-shared-conversations-exposed" >}}) |
| 2026-10-21 | Q3 财报电话会：美加超过 1000 万人设置 Muse，提出交易费路线 | [Muse 101：智能体商务]({{< relref "/docs/muse/sources/community/2026-11-04-muse-101-agentic-commerce" >}})、[Muse 是怎么赚钱的]({{< relref "/docs/muse/sources/community/2026-11-28-emma-muse-monetization" >}}) |
| 2026-10-23 | 日本上线（日本时间） | [日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}}) |
| 2026-10-27 | 新加坡上线；眼镜 Beta 帮助页 | [新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}})、[帮助：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}}) |
| 2026-11-04 | 约 11 小时停运，无官方说明 | [11 月 4 日停运 11 小时]({{< relref "/docs/muse/sources/community/2026-11-06-is-muse-down-nov-4-outage" >}}) |
| 2026-11-05 | 墨西哥上线；实时语音与化身在美国推送 | [墨西哥上线]({{< relref "/docs/muse/sources/media/2026-11-05-muse-launches-mexico" >}})、[语音与表情化身]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}}) |
| 2026-11-06 | Spaces 上线；推送用 Wonder 训练的特化模型 | [定制你的 Muse 应用]({{< relref "/docs/muse/sources/official/2026-11-06-design-muse-app-spaces" >}})、[特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}}) |
| 2026-11-09 | Apple Watch、Wear OS 上线 | [上线手表双平台]({{< relref "/docs/muse/sources/media/2026-11-10-techcrunch-muse-apple-watch-wear-os" >}}) |
| 2026-11-10 | Muse Mail 向美加付费用户开放 | [Muse Mail 全面开放]({{< relref "/docs/muse/sources/media/2026-11-21-muse-mail-rolls-out-to-everyone" >}}) |
| 2026-11-12 | 商家电话向美国付费用户正式开放 | [Muse 电话代打上线]({{< relref "/docs/muse/sources/media/2026-11-12-techcrunch-muse-phone-calls-paid" >}}) |
| 2026-11-13 | Poppy 1.0 发布；Chrome 扩展上架（11-20 Wang 正式宣布，称约 20 万用户） | [Poppy 协议 1.0 发布]({{< relref "/docs/muse/sources/official/2026-11-13-poppy-personal-agent-protocol" >}})、[Chrome 扩展正式宣布]({{< relref "/docs/muse/sources/media/2026-11-20-muse-chrome-extension-official-announcement" >}}) |
| 2026-11-16 | 漏洞赏金研究环境开放 | [漏洞赏金研究环境]({{< relref "/docs/muse/sources/official/2026-11-16-bugbounty-securing-muse" >}}) |
| 2026-11-17 | 澳大利亚上线（第六个市场） | [Muse 上线澳大利亚]({{< relref "/docs/muse/sources/official/2026-11-17-muse-available-australia" >}})、[Muse 登陆澳大利亚]({{< relref "/docs/muse/sources/media/2026-11-17-muse-launches-australia" >}}) |
| 2026-11-18 | 路透社报道早期安全事故；Loblaw 成为首个加拿大零售伙伴；Wang 宣布试穿功能 | [路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})、[Loblaw 接入 Muse]({{< relref "/docs/muse/sources/official/2026-11-18-loblaw-first-canadian-retail-partner" >}})、[Muse 试穿功能]({{< relref "/docs/muse/sources/media/2026-11-18-try-on-clothes-shopping" >}}) |
| 2026-11-20 | Muse Mail 向所有支持市场开放（含免费档）；NebuSec 公开经浏览器窃取对话的攻击链 | [Muse Mail 全面开放]({{< relref "/docs/muse/sources/media/2026-11-21-muse-mail-rolls-out-to-everyone" >}})、[黑进 Muse 窃取对话]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-hacking-muse-browser-use" >}}) |
| 2026-11-23 | 蒙大拿州牵头多州调查；沃尔玛 Agent Gateway 上线（日期说法不一） | [蒙大拿州调查 Muse 隐私]({{< relref "/docs/muse/sources/official/2026-11-23-montana-ag-investigation-muse" >}})、[沃尔玛黑五购物]({{< relref "/docs/muse/sources/media/2026-11-23-walmart-agent-gateway-black-friday" >}}) |
| 2026-11-24 | 英国上线（第七个市场）；Instagram 私信接入；CMA 声明 | [Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})、[英国第七个市场]({{< relref "/docs/muse/sources/media/2026-11-24-muse-launches-uk" >}})、[Muse 进 Instagram 私信]({{< relref "/docs/muse/sources/media/2026-11-24-techcrunch-muse-instagram-dms" >}})、[CMA 英国上线声明]({{< relref "/docs/muse/sources/media/2026-11-24-cma-statement-uk-launch-muse" >}}) |
| 2026-11-25 | 报道称亚马逊与 Meta 谈判解除封锁 | [亚马逊或解除 Muse 封锁]({{< relref "/docs/muse/sources/media/2026-11-25-techcrunch-amazon-muse-blockade-talks" >}}) |
| 2026-11-26 | WIRED 报道 Meta 拒绝 FCA 联合测试 | [Meta 拒绝 FCA 联合测试]({{< relref "/docs/muse/sources/media/2026-11-26-wired-meta-refused-fca-muse-test" >}}) |

## 整体架构

Muse 的执行全部在云端：每个用户一台 Linux 虚拟机，智能体框架 Hatch 跑在容器里，按需拉起、空闲回收，状态留在加密用户卷和记忆文件中（[运行环境]({{< relref "/docs/muse/analysis/runtime" >}})）。数据从三处进入：Meta 自家账户自动连接，目录与自定义连接器按 OAuth 授权，手机和 Mac 同步本地通讯录、日历、消息与健康数据（[记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})、[设备]({{< relref "/docs/muse/analysis/devices" >}})）。触发有三类：用户在任一入口发消息；提醒、周期任务、目标与 Spaces 按计划运行；后台任务每小时、每晚整理记忆（[持续执行]({{< relref "/docs/muse/analysis/continuous-execution" >}})）。对外行动经云端浏览器、连接器、用户自己的 Chrome、Mac 应用，或以 Muse 自己的邮箱和电话、用户本人的消息账号发出（[连接器]({{< relref "/docs/muse/analysis/connectors" >}})、[交互渠道]({{< relref "/docs/muse/analysis/channels" >}})）。凭证由容器外的服务管理，网络出站与连接器调用经宿主侧 Sentinel 审查，敏感写入每次走客户端审批卡（[安全]({{< relref "/docs/muse/analysis/security" >}})）。收费按每周令牌额度分三档，长期收入设想是向商家收交易费（[开放与价格]({{< relref "/docs/muse/analysis/access-pricing" >}})、[商业与规模]({{< relref "/docs/muse/analysis/business" >}})）。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境]({{< relref "/docs/muse/analysis/runtime" >}}) | 每用户一台云端虚拟机，实测 2 vCPU、约 8 GB、空闲即回收；Chrome 扩展与 Mac 构成本地补充；共享内核与 Meta 可访问数据是两处公开弱点 |
| [记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}}) | Markdown 文件为源头、后台任务维护；接入数据最宽；遗忘「尽力而为」，11 月出现篡改与疑似串号问题 |
| [持续执行]({{< relref "/docs/muse/analysis/continuous-execution" >}}) | 提醒、周期任务、目标、Spaces 可在用户离开后运行；写操作逐次审批；主动消息缺硬控制 |
| [连接器]({{< relref "/docs/muse/analysis/connectors" >}}) | 四条接入路径，目录扩到一百多项；平台封堵是最大变量；Poppy 与沃尔玛网关刚起步 |
| [交互渠道]({{< relref "/docs/muse/analysis/channels" >}}) | 一个主对话、八类入口；Muse Mail 与电话是智能体自己的身份，代发消息时是用户本人；AI 身份披露不透明 |
| [设备]({{< relref "/docs/muse/analysis/devices" >}}) | 终端只是入口与本地数据来源；Mac、Android 权限最宽、事故最多；Charm 未发货 |
| [模型]({{< relref "/docs/muse/analysis/models" >}}) | 只用 Meta 自研模型，Spark、Wonder、特化模型三代；用户不能选；官方评测多为自测 |
| [安全]({{< relref "/docs/muse/analysis/security" >}}) | 安全边界放在模型之外，公开最系统；11 起漏洞与事件，读取通道可外传；无独立审计 |
| [隐私]({{< relref "/docs/muse/analysis/privacy" >}}) | 训练默认开启、不进广告系统但影响广告；Confidential VM 未上线；他人信息争议引来美英监管 |
| [开放与价格]({{< relref "/docs/muse/analysis/access-pricing" >}}) | Meta 账户即可免费用，20、100 美元两档付费；7 个市场；功能按美国付费用户先行 |
| [商业与规模]({{< relref "/docs/muse/analysis/business" >}}) | 官方只有「1000 万人设置」一组数字；智能体流量与订单份额领先；交易费未落地，单位经济未证实 |
| [实际效果与可靠性]({{< relref "/docs/muse/analysis/reliability" >}}) | 横向实测多排前两名，强在生活杂事；四类反复出现的失败；无官方完成率与状态页 |

## 资料缺口

各主题页列有细项，整体上最缺的是：

- Meta 的一手运营数据：Q3 电话会一手记录，10-21 之后的用户数、付费人数、订阅收入，交易费的费率、范围与开始时间。
- 隐私政策原文与各地区版本、各类数据保存期限；「不用私人消息训练」的适用范围；Confidential VM 的上线时间。
- 独立安全审计；Meta 对 NebuSec 攻击链、路透社 11-18 报道、蒙大拿调查的回应。
- 官方完成率、可用性或状态页；一个月以上的长期使用记录；黑五、网络周的已验证成交。
- 商家电话的单价、上限、AI 身份披露规则与成功率；代发消息是否标明 AI。
- 免费档官方额度、加购令牌价格、各市场本币价；各市场渠道与连接器的官方对照。
- Muse Charm 的规格、价格与发货；眼镜 Beta 的开放范围。
- Poppy 在 Muse 应用内的实际行为；亚马逊谈判结果的第二来源。
