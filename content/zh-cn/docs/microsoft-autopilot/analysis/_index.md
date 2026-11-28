---
title: "Microsoft Autopilot 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  Microsoft Autopilot 是微软 Microsoft Copilot 中的常驻云端个人智能体，前身是 2026-06-02 发布的 Microsoft Scout，2026-09-25 更名，2026-11-17 起在 Frontier 向美国部分客户分阶段推出；分析覆盖到 2026-11-28 收集的资料。
---

## 概要

- Autopilot 运行在微软托管的云环境中，每人一个，有自己的远程计算机和工作区，用户关机后继续工作；它无法访问本地文件夹或应用，只在启用后借用户的 Edge 浏览器操作已登录站点（[运行环境]({{< relref "/docs/microsoft-autopilot/analysis/runtime" >}})）。
- 它有自己的名称、头像、邮箱、日历和 Entra Agent ID，在 Teams、Outlook 中与用户并列出现，同事可 @提及；有些操作以自己的身份做，有些用代表用户的授权（[交互渠道]({{< relref "/docs/microsoft-autopilot/analysis/channels" >}})）。
- 审批靠自动审查：第二个 AI 模型把每个操作与用户请求比对，相符就直接运行；付款和敏感浏览器步骤始终要批准，没有「始终允许」，本版本也没有审查设置（[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})）。
- 运行在 OpenAI 的 GPT-6.1 Sol 上（OpenAI 为微软子处理方），用户不能选模型；管理员关掉 OpenAI 时改用 Azure OpenAI 的 GPT-5.6 Sol，数据驻留与 EU Data Boundary 由管理员自行确认（[模型]({{< relref "/docs/microsoft-autopilot/analysis/models" >}})、[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})）。
- 记忆分对话、个人、工作区三类，存在用户 OneDrive 的 lobster.repo（Git 仓库），本版本不能关闭；首次设置读过去 30 天的邮件、会议、聊天和文件；eDiscovery、保留、法律保留不覆盖 Autopilot 会话（[记忆与上下文]({{< relref "/docs/microsoft-autopilot/analysis/memory" >}})、[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})）。
- 后台工作以例程为单位，按时间表或事件运行，「不是实时监控」（[持续执行]({{< relref "/docs/microsoft-autopilot/analysis/continuous-execution" >}})）；扩展靠技能和 IT 批准的插件，添加不授予权限（[连接器]({{< relref "/docs/microsoft-autopilot/analysis/connectors" >}})）。
- 开放与价格：需 Microsoft 365 Copilot 许可证，用量另按 Copilot Credits 计费，必须被支出策略覆盖，额度用完静默停止；初期仅美国，没有 GA 日期，单价官方称 GA 前公布（[开放与价格]({{< relref "/docs/microsoft-autopilot/analysis/access-pricing" >}})）。
- 用户数、完成率、独立实测都没有：规模只有 2026-05 的内部数字，应用卡不公布评估通过率（[商业与规模]({{< relref "/docs/microsoft-autopilot/analysis/business" >}})、[实际效果与可靠性]({{< relref "/docs/microsoft-autopilot/analysis/reliability" >}})）。

## 定位

官方称 Autopilot 是「常驻的、基于云的个人智能体」，替用户分担工作、让工作持续推进而无需指挥每一步（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})）。新闻手册称它是「微软首个面向个人生产力的企业级长时运行智能体」，与 Home、Code、Managed Runtime 等并列为「新的 Copilot」（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。产品页称它处理跨数天、数周的目标、决策和承诺，「带给你决策，而不是通知」（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})）。

与微软其他 Copilot 体验的分工：Chat 用于提问，Cowork 处理委托的多步任务，Code 构建软件，Autopilot 专注持久工作和跟进；Office 与 Code 的能力不自动成为 Autopilot 的功能（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。Redmondmag 的说法是 Cowork 完成单个多步任务，Autopilot 管理没有明确终点的持续职责（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。应用卡强调 Teams 的 @Copilot 不是 Autopilot（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

起源是 CVP Omar Shahine 用开源 OpenClaw 搭的个人助手 Lobster；Build 发布时 Nadella 称 Autopilots 是「企业级的 Claws」（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})、[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})）。11 月的文档不再提 OpenClaw，但存储文件名 lobster.repo 沿用了原型的名字（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）。

与其他跟踪产品相比：The Neuron 把它看作微软对 Muse、Dots、Grok Bot、Claude Duet 的回应，优势在于离工作近（[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})）；UC Today 认为 Ignite 上各家智能体都进了 Teams，只有 Autopilot 有独立的目录身份和具名管理者（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})）；iThome 把它归为「企业数字同事」（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。dSebastien 指出 dots、Muse、Grok Bot、Gemini、Claude Duet 都先面向个人销售，Autopilot 住在 Microsoft 365 里、只面向企业（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-02-26 | Omar Shahine 向 Microsoft AI Accelerator 小组演示基于 OpenClaw 的个人助手 Lobster | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| 2026-05-01 | 内部每天超过 3,000 名用户测试 ClawPilot（一周前 100） | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| 2026-06-02 | Build 发布 Microsoft Scout，称首个 Autopilot；以桌面应用的实验版向 Frontier 组织提供 | [Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}}) |
| 2026-09-25 | 更名 Autopilot，新 Copilot 分为 Home、Code、Autopilot；Autopilot 按 Copilot Credits 用量计费，需 Microsoft 365 Copilot 许可证 | [新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})、[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}}) |
| 2026-09-25 | OpenClaw 博客称 Autopilot 以 OpenClaw 为基础，列出微软的上游贡献 | [OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}}) |
| 2026-10-30 | 十月新功能汇总：Autopilot 11 月向 Frontier 推出 | [Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}}) |
| 2026-11-09 | MC1546354：UBB 入口 2027 年 1 月底起对 Copilot 许可证用户默认可见 | [消息中心 MC1546354]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-09-mc1546354-ubb-discoverability" >}}) |
| 2026-11-17 | Ignite：以云端形态在 Frontier 分阶段推出，初期限美国部分客户，无 GA 日期；Autopilot Learn 文档集首次出现 | [消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}}) |
| 2026-11-20 | 「自定义 Autopilot」文档（技能与插件） | [自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}}) |
| 2026-11-24 | 审批、FAQ、概述、使用文档更新 | [Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}}) |
| 2026-11-28 | 产品页：最终定价与打包方案在 GA 前公布 | [Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}}) |

## 整体架构

Autopilot 是 Microsoft Copilot 里的云端智能体，每个启用的用户一个。它在微软管理的云环境中有自己的远程计算机和工作区，不碰用户设备上的文件和应用，只在所有者的私人对话中借 Edge 浏览器操作已登录站点。数据来自用户已有权限内的 Microsoft 365（Teams、Outlook、OneDrive、SharePoint，经 Work IQ / Microsoft IQ），首次设置时熟悉过去 30 天的内容；扩展靠技能和 IT 批准的插件。用户在 Copilot 应用里配置，日常经 Teams 私聊和邮件往来，同事可在群聊、频道中 @提及它。工作由用户的请求和例程（按时间表或事件）触发，每个有后果的操作先由第二个模型审查，不符才在 Teams 中出审批卡。模型是 OpenAI 的 GPT-6.1 Sol；记忆与会话存在用户 OneDrive 的 lobster.repo。身份是独立的 Entra Agent ID，配具名管理者，由 Agent 365 治理；用量按 Copilot Credits 计费，由管理员的支出策略设限。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境](runtime/) | 微软托管的云端计算机，每人一个；不能访问本地文件夹，只借 Edge 操作已登录站点；规格无文档 |
| [记忆与上下文](memory/) | 三类记忆存在 OneDrive 的 lobster.repo，可查看删除导出，不能关闭；首次设置读过去 30 天 |
| [持续执行](continuous-execution/) | 例程按时间表或事件运行，「不是实时监控」；不继承创建对话的全部权限；额度用完静默停止 |
| [连接器](connectors/) | Microsoft 365 原生，扩展靠技能和 IT 批准的插件，添加不授权；无第三方插件清单 |
| [交互渠道](channels/) | Copilot 应用配置，Teams 私聊与邮件沟通，同事 @提及；有自己的名字、邮箱与 Entra Agent ID |
| 设备 | 无需安装，移动端借 Microsoft 365 Copilot、Teams、Outlook 应用，本机只经 Edge；没有专用硬件。资料只到这一层，不单独成页（见[运行环境]({{< relref "/docs/microsoft-autopilot/analysis/runtime" >}})、[交互渠道]({{< relref "/docs/microsoft-autopilot/analysis/channels" >}})） |
| [模型](models/) | GPT-6.1 Sol（OpenAI 子处理），退路是 Azure OpenAI 的 GPT-5.6 Sol；用户不能选；审查用第二个模型 |
| [安全](security/) | 自动审查，无「始终允许」、无设置；Entra Agent ID、MXC、审计日志为必需；合规覆盖有缺口 |
| [隐私](privacy/) | 默认经 OpenAI 子处理，驻留自行确认；记忆不能关、eDiscovery 不覆盖；称不用于训练 |
| [开放与价格](access-pricing/) | Frontier 预览、仅美国、无 GA；Copilot 许可证 + Copilot Credits，单价未公布 |
| [商业与规模](business/) | 无用户数；许可证之上的用量收费，由 Agent 365 承接；起源于 OpenClaw 业余项目 |
| [实际效果与可靠性](reliability/) | 无独立实测；应用卡不公布通过率，文档强调审批不等于完成 |

## 资料缺口

- **独立实测与用户反馈。** 截至 11-28 只有官方文档与报道，没有任何对云端 Autopilot 的实测。
- Copilot Credits 单价、Autopilot 的典型消耗与最终打包方案；GA 时间与美国以外的开放计划。
- 云端计算机的规格与持久化；MXC 在 Autopilot 中的作用；Redmondmag 所说「受管设备本地运行」的设置是否存在。
- 自动审查模型的型号与误判率；抗提示注入评估的定量结果。
- OpenAI 子处理时的数据保存期限与处理地点；eDiscovery、保留覆盖 Autopilot 的时间表。
- 用户数、组织数等对外数字。
