---
title: "Microsoft Autopilot 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  Microsoft Autopilot（2026-09-25 前名为 Microsoft Scout）是微软基于 OpenClaw 做的企业常驻智能体，2026-06-02 以 Frontier 实验版发布、9 月底进入私有预览；分析覆盖到 2026-11-10 收集的资料。
---

## 概要

- 资料描述的是两个阶段：Learn 文档（2026-08 版）中的 Scout 是运行在用户 Windows/Mac 上的桌面应用，以用户身份读写工作区、跑 shell、控制浏览器；9 月更名后的 Autopilot 被官方描述为租户内拥有自己计算机的云端「数字队友」，但没有文档（[运行环境]({{< relref "/docs/microsoft-autopilot/analysis/runtime" >}})）。
- 持续执行靠 Heartbeat（15 分钟到 2 小时间隔的定期检入）和 Automations（时间表或条件触发），后台权限比交互式对话更严；桌面版设备休眠时暂停（[持续执行]({{< relref "/docs/microsoft-autopilot/analysis/continuous-execution" >}})）。
- 安全设计是资料最详尽的部分：三级权限、默认所有操作都需确认、影响他人的 Microsoft 365 动作必须批准、外部内容当数据不当指令，加上 Entra 身份、Purview 与十余项 Intune 策略（[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})）。
- 隐私的关键点是模型调用经 GitHub Copilot 处理、可能传给第三方模型提供方，数据驻留、敏感度标签强制、eDiscovery 等 Microsoft 365 保护不适用，管理员须单独声明（[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})）。
- 进入门槛高：Frontier、Intune 策略、声明表单、GitHub Copilot 席位，文档另要求 Microsoft 365 Copilot 许可证；预览期用量从 GitHub Copilot 额度扣除，9 月后改按用量计费，价格未公布（[开放与价格]({{< relref "/docs/microsoft-autopilot/analysis/access-pricing" >}})）。
- 规模只有发布前的内部数字（2026-05-01 每天超过 3,000 名内部用户）；实际效果只有一篇 6 月的社区实测，没有完成率数据（[商业与规模]({{< relref "/docs/microsoft-autopilot/analysis/business" >}})、[实际效果与可靠性]({{< relref "/docs/microsoft-autopilot/analysis/reliability" >}})）。

## 定位

官方称 Autopilots 是一类常驻后台、自主工作、拥有自己身份、无需每次提示就行动的智能体，Scout 是「我们的第一个 Autopilot 智能体」，面向 Microsoft 365 的常驻个人智能体（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}})）。Nadella 在 Build 上称它们是「企业级的 Claws」（[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})）。官方对谈把它与「野外常见的普通 claw」相区别：在 OpenClaw 代码之上加企业身份、治理和安全（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。

与微软其他产品的关系：FAQ 把 Copilot Chat 定为云端问答、Scout 定为本机执行（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）；9 月的新 Copilot 分为 Home、Code、Autopilot 三部分，Cowork 端到端交付一项任务，Autopilot 长期持有角色与目标（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。GeekWire 与 Computerworld 把它列在 Copilot Tasks、Copilot Cowork、Agent Mode 之后的又一款智能体工具（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})、[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。

与其他跟踪产品相比：iThome 把 Gemini Spark 归为个人、把 Autopilot 归为「企业数字同事」（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）；dSebastien 认为它在托管型智能体中是「异类」：唯一建立在开源运行时上并贡献上游、每个智能体有目录身份、住在 Microsoft 365 界面里而非独立应用，而 dots、Muse、Grok Bot、Gemini、Claude Duet 都先面向个人销售（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。小企业对比文章认为对 Microsoft 365 用户「现在就能用」的是 Cowork，Autopilot 仍在预览（[六款智能体小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。

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
| 2026-10-30 | MC1332811 过期 | [消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}}) |
| 2026-11-17 至 20 | Ignite，官方称将分享更多信息（截至 11-10 尚未举行） | [新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}}) |

## 整体架构

按 2026-08 的 Learn 文档，Scout 是 Windows/Mac 上的桌面应用（Electron 外壳加 GitHub Copilot 组件），在用户设备上以用户身份运行：读写工作区目录、执行 shell、控制浏览器、启动子 agent，通过 Work IQ 和用户已有权限访问 Microsoft 365 数据，通过 MCP 服务器和 skill 扩展。用户在聊天界面下达任务，或配置 Heartbeat 与 Automations 让它在后台运行。每个动作按 Auto-approve/Prompt/Deny 三级权限审批，影响他人的动作必须确认；管理员用 Intune 策略收紧。模型调用经 GitHub Copilot 处理，用量走 GitHub 计费；会话与记忆存在用户的 OneDrive。

9 月后官方改称 Autopilot 在租户内拥有自己的身份、记忆、计算机和工作区，出现在 Teams、Outlook、频道和文档中，按用量计费；这一形态的架构细节截至 11-10 没有文档。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境](runtime/) | 文档中的 Scout 在用户设备上运行；9 月称云端托管，无文档 |
| [记忆与上下文](memory/) | 上下文来自用户已有的 Microsoft 365 权限；记忆主动形成、标注来源、可删除，存于 OneDrive |
| [持续执行](continuous-execution/) | Heartbeat 定期检入 + Automations 条件触发，后台权限更严；休眠即暂停 |
| [连接器](connectors/) | Microsoft 365 原生，外部靠 MCP、浏览器和 skill；9 月起有插件注册表 |
| [交互渠道](channels/) | 桌面聊天为主，Teams/Outlook 对外；Autopilot 可被 @提及；身份口径不一 |
| 设备 | 只有 Windows 11 与 macOS 12 以上的桌面应用，不支持移动端，没有专用硬件；资料都只说到这一层，不单独成页（见[运行环境]({{< relref "/docs/microsoft-autopilot/analysis/runtime" >}})） |
| [模型](models/) | 经 GitHub Copilot 处理、继承其模型目录，用户可逐条切换，管理员可按提供方禁用 |
| [安全](security/) | 三级权限、默认全确认、外部内容当数据；Purview 是否覆盖模型处理环节有张力 |
| [隐私](privacy/) | 数据会离开 Microsoft 365，驻留与标签保护不适用；不训练；政府云不可用 |
| [开放与价格](access-pricing/) | 多道企业关口；预览期扣 GitHub Copilot 额度，9 月后 UBB，价格未公布 |
| [商业与规模](business/) | 只有内部用户数；起于业余项目，依附 Copilot 与 GitHub 订阅 |
| [实际效果与可靠性](reliability/) | 一篇正面的社区实测；主要摩擦在部署与登录 |

## 资料缺口

- **Autopilot 本身的文档。** 截至 11-10，Learn 文档仍全部描述 Scout 桌面应用；云端 Autopilot 的运行环境、权限、隐私条款、价格、模型都只有 9 月一篇博文。Ignite（11-17 至 20）后可能有新资料。
- 桌面应用在更名后是否保留，与云端版的关系。
- 按用量计费的单价；是否仍需 GitHub Copilot 席位。
- 用户数、组织数等对外数字。
- 9 月后的实测与长期使用报告；完成率等量化数据。
- OpenClaw 作为基础的一手确认（目前只有 OpenClaw 博客与微软 6 月文章）。
