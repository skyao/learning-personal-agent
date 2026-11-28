---
title: "Microsoft Autopilot 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  Microsoft Autopilot（2026-09-25 前名为 Microsoft Scout）是微软 Copilot 中的常驻个人智能体：2026-06-02 以 Scout 桌面应用发布 Frontier 实验版，2026-11-17 起改为微软托管的云端智能体、在 Frontier 向美国部分客户分阶段推出；分析覆盖到 2026-11-28 收集的资料。
---

## 概要

- 资料描述的是两种形态。2026-06 至 09 的 Scout 是用户 Windows/Mac 上的桌面应用，以用户身份读写本机、跑 shell；2026-11-17 起的 Autopilot 运行在微软托管的云环境，有自己的远程计算机，无法访问本地文件夹或应用，只在启用后借用户的 Edge 浏览器操作已登录站点（[运行环境]({{< relref "/docs/microsoft-autopilot/analysis/runtime" >}})）。
- 它有自己的名称、头像、邮箱、日历和 Entra Agent ID，在 Teams、Outlook 中与用户并列出现，同事可 @提及；有些操作以自己的身份做，有些用代表用户的授权（[交互渠道]({{< relref "/docs/microsoft-autopilot/analysis/channels" >}})）。
- 审批从 Scout 的「默认全确认」改为自动审查：第二个 AI 模型把每个操作与用户请求比对，相符就直接运行；付款和敏感浏览器步骤始终要批准，没有「始终允许」，本版本也没有审查设置（[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})）。
- 运行在 OpenAI 的 GPT-6.1 Sol 上（OpenAI 为微软子处理方），用户不能选模型；管理员关掉 OpenAI 时改用 Azure OpenAI 的 GPT-5.6 Sol，数据驻留与 EU Data Boundary 由管理员自行确认（[模型]({{< relref "/docs/microsoft-autopilot/analysis/models" >}})、[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})）。
- 记忆分对话、个人、工作区三类，存在用户 OneDrive 的 lobster.repo（Git 仓库），本版本不能关闭；eDiscovery、保留、法律保留不覆盖 Autopilot 会话（[记忆与上下文]({{< relref "/docs/microsoft-autopilot/analysis/memory" >}})、[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})）。
- 持续执行以例程为单位，按时间表或事件运行，「不是实时监控」；云端化后设备关机不再中断（[持续执行]({{< relref "/docs/microsoft-autopilot/analysis/continuous-execution" >}})）。
- 开放与价格：需 Microsoft 365 Copilot 许可证，用量另按 Copilot Credits 计费，必须被支出策略覆盖，额度用完静默停止；初期仅美国，没有 GA 日期，单价官方称 GA 前公布（[开放与价格]({{< relref "/docs/microsoft-autopilot/analysis/access-pricing" >}})）。
- 用户数、完成率、独立实测都还没有：规模只有 5 月的内部数字，实测只有 6 月的 Scout 0.22 版（[商业与规模]({{< relref "/docs/microsoft-autopilot/analysis/business" >}})、[实际效果与可靠性]({{< relref "/docs/microsoft-autopilot/analysis/reliability" >}})）。

## 定位

官方称 Autopilots 是一类常驻后台、自主工作、拥有自己身份、无需每次提示就行动的智能体，Scout 是「我们的第一个 Autopilot 智能体」，面向 Microsoft 365 的常驻个人智能体（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}})）。Nadella 在 Build 上称它们是「企业级的 Claws」（[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})）。官方对谈把它与「野外常见的普通 claw」相区别：在 OpenClaw 代码之上加企业身份、治理和安全（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。

与微软其他产品的关系：FAQ 把 Copilot Chat 定为云端问答、Scout 定为本机执行（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）；9 月的新 Copilot 分为 Home、Code、Autopilot 三部分，Cowork 端到端交付一项任务，Autopilot 长期持有角色与目标（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。GeekWire 与 Computerworld 把它列在 Copilot Tasks、Copilot Cowork、Agent Mode 之后的又一款智能体工具（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})、[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。

与其他跟踪产品相比：iThome 把 Gemini Spark 归为个人、把 Autopilot 归为「企业数字同事」（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）；dSebastien 认为它在托管型智能体中是「异类」：唯一建立在开源运行时上并贡献上游、每个智能体有目录身份、住在 Microsoft 365 界面里而非独立应用，而 dots、Muse、Grok Bot、Gemini、Claude Duet 都先面向个人销售（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。小企业对比文章认为对 Microsoft 365 用户「现在就能用」的是 Cowork，Autopilot 仍在预览（[六款智能体小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。

2026-11 的文档给出了与微软其他 Copilot 体验的分工：Chat 用于提问，Cowork 处理委托的多步任务，Code 构建软件，Autopilot 专注持久工作和跟进；Office 与 Code 的能力不自动成为 Autopilot 的功能（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。产品页称 Autopilot 处理跨数天、数周的目标、决策和承诺，「带给你决策，而不是通知」（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})）；新闻手册称它是「微软首个面向个人生产力的企业级长时运行智能体」（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。文档不再提 OpenClaw，但存储文件名 lobster.repo 仍沿用原型 Lobster 的名字（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）。

Ignite 后的报道中，The Neuron 把它看作微软对 Muse、Dots、Grok Bot、Claude Duet 的回应（[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})）；UC Today 认为 Ignite 上各家智能体都进了 Teams，只有 Autopilot 有独立的目录身份和具名管理者（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-02-26 | Omar Shahine 向 Microsoft AI Accelerator 小组演示基于 OpenClaw 的个人助手 Lobster | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| 2026-03-31 | Shahine 转任新角色，负责把 OpenClaw 和个人智能体带入 Microsoft 365 | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| 2026-05-01 | 内部每天超过 3,000 名用户测试 ClawPilot（一周前 100） | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| 2026-06-02 | Build 发布 Microsoft Scout，称首个 Autopilot，以实验版向 Frontier 组织提供；消息中心 MC1332811 同日发布 | [Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}}) |
| 2026-06-05 | 桌面客户端开始向 Frontier 组织推出 | [TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}}) |
| 2026-07 | Co-Create 编辑器、模型与推理控制、To Do、Teams 频道发帖、会话历史恢复等 | [新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}}) |
| 2026-07-27 | GitHub Copilot app 1.1 起有独立策略 | [管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}}) |
| 2026-08 | Teams 转录与会议室、SharePoint Lists、收件箱规则、文件共享、云端 Co-Create 工作区、GitHub Enterprise Cloud 登录 | [新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}}) |
| 2026-09-25 | 更名 Autopilot，新 Copilot 分为 Home、Code、Autopilot；按用量计费；本月底扩展到私有预览 | [新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}}) |
| 2026-09-25 | OpenClaw 博客列出微软的上游贡献，称 Autopilot 以 OpenClaw 为基础 | [OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}}) |
| 2026-09-25 | 定价博文：Copilot 分为 USL（每用户订阅）与 UBB（Copilot Credits），Autopilot 属 UBB；消息中心 MC1479277 称 Autopilot 需 Microsoft 365 Copilot 许可证与支出策略 | [Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}}) |
| 2026-10-30 | MC1332811 过期 | [消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}}) |
| 2026-10-30 | 十月新功能汇总：Autopilot 11 月向 Frontier 推出 | [Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}}) |
| 2026-11-09 | MC1546354：UBB 入口 2027 年 1 月底起对 Copilot 许可证用户默认可见 | [消息中心 MC1546354]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-09-mc1546354-ubb-discoverability" >}}) |
| 2026-11-17 | Ignite：Autopilot 在 Frontier 分阶段推出，初期限美国部分客户，无 GA 日期；Autopilot Learn 文档集首次出现 | [消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}}) |
| 2026-11-20 | 「自定义 Autopilot」文档（技能与插件）；Redmondmag 报道推出 | [自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}}) |
| 2026-11-24 | 审批、FAQ、概述、使用等文档更新 | [Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}}) |
| 2026-11-28 | 产品页：最终定价与打包方案在 GA 前公布 | [Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}}) |

## 整体架构

按 2026-11 的 Learn 文档，Autopilot 是 Microsoft Copilot 里的云端智能体，每个启用的用户一个。它在微软管理的云环境中有自己的远程计算机和工作区，不碰用户设备上的文件和应用，只在所有者的私人对话中借 Edge 浏览器操作已登录站点。数据来自用户已有权限内的 Microsoft 365（Teams、Outlook、OneDrive、SharePoint，经 Work IQ / Microsoft IQ），首次设置时熟悉过去 30 天的内容；扩展靠技能和 IT 批准的插件。用户在 Copilot 应用里配置，日常经 Teams 私聊和邮件往来，同事可在群聊、频道中 @提及它。工作由用户的请求和例程（按时间表或事件）触发，每个有后果的操作先由第二个模型审查，不符才在 Teams 中出审批卡。模型是 OpenAI 的 GPT-6.1 Sol；记忆与会话存在用户 OneDrive 的 lobster.repo。身份是独立的 Entra Agent ID，配具名管理者，由 Agent 365 治理；用量按 Copilot Credits 计费，由管理员的支出策略设限。

更名前的 Scout（2026-06 至 09）是 Windows/Mac 桌面应用：Electron 外壳加 GitHub Copilot 组件，在用户设备上以用户身份运行，三级权限默认全确认，模型调用与计费都经 GitHub Copilot，访问需要 Intune 策略和 GitHub Copilot 席位。11 月的要求页称不应把早期桌面预览的说明当作云端体验的要求。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境](runtime/) | 2026-11 起为微软托管的云端计算机，不能访问本地文件夹，只借 Edge 操作已登录站点；Scout 是桌面应用 |
| [记忆与上下文](memory/) | 三类记忆存在 OneDrive 的 lobster.repo，可查看删除导出，不能关闭；首次设置读过去 30 天 |
| [持续执行](continuous-execution/) | 例程按时间表或事件运行，「不是实时监控」；云端化后关机不中断，额度用完静默停止 |
| [连接器](connectors/) | Microsoft 365 原生，扩展靠技能和 IT 批准的插件，添加不授权；无第三方插件清单 |
| [交互渠道](channels/) | Copilot 应用管理，Teams 私聊与邮件沟通，同事 @提及；有自己的名字、邮箱与 Entra Agent ID |
| 设备 | 云端 Autopilot 无需安装，移动端借 Microsoft 365 Copilot、Teams、Outlook 应用，本机只经 Edge；没有专用硬件。资料仍只到这一层，不单独成页（见[运行环境]({{< relref "/docs/microsoft-autopilot/analysis/runtime" >}})、[交互渠道]({{< relref "/docs/microsoft-autopilot/analysis/channels" >}})） |
| [模型](models/) | GPT-6.1 Sol（OpenAI 子处理），退路 Azure OpenAI 的 GPT-5.6 Sol；用户不能选；审查用第二个模型 |
| [安全](security/) | 自动审查替代默认全确认，无「始终允许」、无设置；Entra Agent ID、MXC、审计日志为必需；合规覆盖有缺口 |
| [隐私](privacy/) | 默认经 OpenAI 子处理，驻留自行确认；记忆不能关、eDiscovery 不覆盖；称不用于训练 |
| [开放与价格](access-pricing/) | Frontier 预览、仅美国、无 GA；Copilot 许可证 + Copilot Credits，单价未公布 |
| [商业与规模](business/) | 无用户数；许可证之上的用量收费，由 Agent 365 承接；能力开放给其他智能体 |
| [实际效果与可靠性](reliability/) | 云端版无独立实测；应用卡不公布通过率，文档强调审批不等于完成 |

## 资料缺口

- **Autopilot 云端版的独立实测与用户反馈。** 截至 11-28 资料库只有官方文档与报道，唯一的实测是 6 月的 Scout 0.22 版。
- Copilot Credits 单价、Autopilot 的典型消耗与最终打包方案（官方称 GA 前公布）；GA 时间与美国以外的开放计划。
- 云端计算机的规格与持久化；MXC 在 Autopilot 中的作用；Redmondmag 所说「受管设备本地运行」设置是否存在。
- 自动审查模型的型号与误判率；抗提示注入评估的定量结果。
- OpenAI 子处理时的数据保存期限与处理地点；eDiscovery、保留覆盖 Autopilot 的时间表。
- 用户数、组织数等对外数字。
- Scout 桌面应用在 Autopilot 推出后是否保留、原用户如何迁移。
