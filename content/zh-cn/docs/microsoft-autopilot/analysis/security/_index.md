---
title: "Microsoft Autopilot：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  Scout 的安全设计是本产品资料最详尽的部分：Auto-approve/Prompt/Deny 三级权限、默认所有操作都需确认、影响他人的 Microsoft 365 动作必须批准、外部内容当作数据而非指令，外加 Entra 身份、Purview 与十余项 Intune 策略。资料中没有漏洞或安全事件报道，但官方文档之间对 Purview 是否生效有张力。
---

## 概要

- 权限分 Auto-approve、Prompt、Deny 三级；默认 Auto-approve 关闭，所有操作都需确认；批准时显示确切命令或邮件预览，选项为 Approve、Always allow、Deny。
- 发送、共享、回复、转发或更新他人可见信息的操作，执行前须用户确认；删除始终需要明确批准（社区实测）。
- 提示注入防护：邮件、网页、Teams 消息标记为不受信任的外部内容，「作为数据而非指令处理」；资料没有给出防护效果的数据。
- 企业控制：每个智能体在受治理的 Entra 身份下运行，凭据限定任务范围并在日志中脱敏；Purview 策略在发送或写入前执行；管理员有 `ForcePrompt`、`RestrictToWorkspace` 等十余项策略。
- 官方文档自身有张力：发布博文称 Purview 即时执行，负责任 AI FAQ 称经 GitHub Copilot 处理时敏感度标签等保护不适用，生成内容未必继承标签。
- 产品的出发点是回应 OpenClaw 的安全顾虑：微软 Defender 团队曾称 OpenClaw 应视为带持久凭据的不受信任代码执行。

## 三级权限与默认值

入门页给出默认值：WorkIQ connectivity 开、Shell access 开、Auto-approve 关，须按能力显式启用自动批准（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。shell 命令的示例分级（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）：

| 级别 | 示例 |
| --- | --- |
| 自动批准 | ls、cat、grep、git log 等只读命令 |
| 提示 | npm install、git push、curl、网络请求、文件写入 |
| 拒绝 | rm -rf /、format 等破坏性命令 |

用户可在设置中加允许/拒绝列表、标记必须显式批准的敏感路径；工具组（文件系统、shell、浏览器、WorkIQ）可整体关闭，关闭后「不会出现在系统提示词中」（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。

Microsoft 365 操作中，凡修改共享信息或影响他人的动作（发邮件、发 Teams、建改日历事件与列表项、改收件箱规则、共享文件）都先请求批准（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）。社区实测称可按类别授予长期权限，但删除始终需要明确批准（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。后台模式的权限更严，见[持续执行]({{< relref "/docs/microsoft-autopilot/analysis/continuous-execution" >}})。

负责任 AI FAQ 提醒，无需逐步批准的自主模式只用于低风险场景，不适用于法律文件、医疗决定、绕过审批流程的财务交易等无人审核即需准确的场景（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。

## 提示注入

FAQ 与负责任 AI 文档称外部内容（邮件、网页、Teams 消息）标记为不受信任，作为数据而非指令处理（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})、[负责任 AI 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-overview" >}})）；记忆同样标注来源，外部来源的记忆据以行动前要确认（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。社区作者转述 The Register 称提示注入防御不明确，微软未回应（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。Forrester 的 Pollard 把智能体被操纵或提示注入列为主要风险之一（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。

## 身份、凭据与 Purview

发布博文称每个智能体在自己受治理的 Entra 身份下运行，而非共享匿名服务账户；身份背后的凭据限定于当前任务，在日志或诊断中被隐去；Purview 数据保护策略（敏感度标签、DLP）「在发送或写入任何内容之前即时执行」（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）。Command Line 对谈补充 Agent 365 提供统一控制平面（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。

使用指南说明敏感度标签的具体行为：读到带标签内容后会话敏感度升高，不把带标签内容写入未受保护的目标（Teams 频道、纯文本文件、外部工具），共享机密内容前要求确认（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。但负责任 AI FAQ 写明 Scout 生成或修改的内容「未必自动继承或强制执行这些标签」（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})），且经 GitHub Copilot 处理时敏感度标签强制等 Microsoft 365 保护不适用（见[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})）。社区作者指出这与博文「Purview 已强制执行」的说法有些别扭，认为两者可同时成立（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

推断：Purview 的控制作用在 Scout 写入 Microsoft 365 目标的环节；模型调用经 GitHub 处理的环节不在 Purview 覆盖之内。这是文档拼合得出的理解，官方没有统一说明。

## 管理员策略

组策略页列出（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）：

| 策略 | 作用 |
| --- | --- |
| `ForcePrompt` | 所有非读取操作强制人工批准 |
| `DisabledPermissions` | 禁用 shell、write、mcp、url、custom-tool |
| `DisabledServers` | 阻止指定 tool server |
| `RestrictToWorkspace` | 文件系统和 shell 限定在工作区 |
| `BrowserEgressBlockedOrigins` | 阻止浏览器访问指定来源 |
| `DisabledModels` / `DisabledProviders` | 禁用模型或提供方 |
| `DisableHeartbeat` / `DisableWorkflows` | 禁用后台模式 |

策略是设备级的，Windows 存在 `HKLM\SOFTWARE\Policies\Scout`，标准用户无法修改；macOS 通过 mobileconfig 下发（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})、[管理员：Intune 部署]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-18-scout-admin-intune-setup" >}})）。访问本身有两道关口：Microsoft 365 管理中心的 Frontier 访问（保存后约三小时生效），以及 Intune 策略、声明表单和 GitHub Copilot 席位（[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})）。

## 从 OpenClaw 的安全顾虑出发

GeekWire 引微软 Defender 团队的指引：OpenClaw 应视为带持久凭据的不受信任代码执行，「不适合在标准个人或企业工作站上运行」；Shahine 称企业加固是头号任务（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。Semafor 写明企业大多在等待 OpenClaw 的安全漏洞被修补（[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})）。iThome 把微软、Google 等的「云端隔离、人工核准与更严格的安全控管」视为对 OpenClaw 安全顾虑的回应（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

微软称把策略合规贡献回 OpenClaw 上游（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）；OpenClaw 博客列出 Policy 插件、执行批准提示中的密钥脱敏、区分「确定未运行」与「结果未知」的命令等（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。

Command Line 对谈中 Werner 指出隐私方面的难点：「如果我把我的智能体派给你，它不应该告诉你关于我的一切」（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。The Neuron 转述 Shahine：信任是「最关键也最未知」的问题，因为「AI 的超能力是非确定性」（[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})）。

## 外部评价

- Forrester 的 Pollard：Scout 不会带来全新的数据风险，但会「放大已经存在的任何数据治理问题」，区别在于它可能对数据采取行动（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。
- 社区作者建议先清理权限、保持批准提示开启、抵制点「始终允许」，因为它「会比任何审计员更快地发现你的过度共享」（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。
- 资料库中没有针对 Scout/Autopilot 的漏洞报道、安全事件或漏洞赏金信息。

## 资料缺口

- 提示注入防护的测试结果、独立审计、漏洞赏金。
- Autopilot 云端形态的权限模型是否沿用 Scout 的三级权限与策略。
- Entra 身份与「用户身份」在实际操作中如何分工。

## 主要资料

- 官方：[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})、[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})（三级权限与默认值）；[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})（影响他人的操作需批准）；[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})、[负责任 AI 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-overview" >}})（提示注入与适用范围）；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（Entra 身份、Purview、零信任）；[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})、[管理员：Intune 部署]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-18-scout-admin-intune-setup" >}})、[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})（管理员策略与访问关口）。
- 媒体：[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})（Defender 指引）；[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})（Forrester 观点）；[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
