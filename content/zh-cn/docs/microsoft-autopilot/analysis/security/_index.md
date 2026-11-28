---
title: "Microsoft Autopilot：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 改用「自动审查」：第二个 AI 模型在操作运行前把它与用户请求比对，相符就直接运行，不符才出审批卡；读取、搜索、起草不中断，付款和敏感浏览器步骤始终要批准，审批卡只有单次「允许」，没有「始终允许」，本版本没有面向用户或管理员的审查设置。每个 Autopilot 有自己的 Entra Agent ID 和具名管理者，必需能力含 MXC 与审计日志；官方坦承 eDiscovery、保留、DSPM for AI 不覆盖、提示词 DLP 受限。
---

## 概要

- 审批从 Scout 的「三级权限、默认全确认」改为自动审查：第二个 AI 模型在操作运行前把它与用户请求（含「只读」「先别发」等限制）比对，相符的直接运行、不出审批卡，不符或无法检查的才等用户批准（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。
- 分级：读取、搜索、起草不中断（抽查一小部分）；发送、共享、删除、更改内容和创建或更改自动化由自动审查决定；付款和其他敏感浏览器步骤始终需批准，即使用户自己提出了该操作（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。
- 审批卡只有单次「允许」和「拒绝」，没有「始终允许」；过期未答则不运行。本版本自动审查没有面向用户或管理员的设置；文档承认它看不到 Autopilot 所知的一切，可能出错（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。
- 提示注入的口径：只有所有者本人的消息算请求，邮件、文档、网页中的指令不构成授权，即使声称来自用户；官方称这能降低而不能消除风险（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。
- 身份与治理：每个 Autopilot 有自己的 Entra Agent ID 和具名管理者，IT 可限定范围、随时阻止（约一小时生效）；必需能力为 Entra Agent ID、MXC 隔离执行环境、Microsoft 365 审计日志（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。
- 官方列出的预览期缺口：敏感度标签不排除读取，eDiscovery、保留、法律保留不覆盖 Autopilot 会话，DSPM for AI 与活动资源管理器看不到它，提示词 DLP 只在部分租户测试；审计日志中代表所有者的读取记在所有者名下、没有代理 ID（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})）。

## 2026-11：第二个模型做自动审查

「Autopilot 如何审查操作」一页说明，Autopilot 用第二个 AI 模型在操作运行前审查，把操作与用户的请求比对，包括隐含步骤和「只读」「先别发」之类的限制；无论以用户还是以自己的身份行事，规则相同（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。

| 操作类型 | 处理 |
| --- | --- |
| 读取、搜索、起草 | 不中断；小部分被抽查 |
| 发送、共享、删除、更改邮件/日历/文件/聊天；创建或更改自动化 | 自动审查判断：与请求相符则直接运行，不符或无法检查则出审批卡 |
| 付款及其他敏感的浏览器步骤 | 始终需要批准，即使是用户提出的 |

来源：[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})。入门页的说法是「Autopilot 不要求批准每一步」，与请求相符的操作可不经审批卡运行，其他操作和所有付款等待允许或拒绝（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。Edge 中须批准的敏感步骤包括更改账户、结账或付款、输入银行卡、永久删除、向外部站点提交个人信息或消息（[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})）。场景页的惯例是发送回复、移动会议、发提醒前先问（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。

审批卡出现在 Teams 一对一聊天（以及发起请求的 Copilot 对话），显示触达对象的姓名与邮箱、外部人员标「外部」、只读预览和执行身份；只有「允许」（单次）和「拒绝」，「没有『始终允许』的选项」；过期未答则该操作不运行，任务其余部分继续（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。卡片说明出现原因：可能超出请求、需确认一致、安全检查未能完成（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。自动化运行中每一步与保存的指令比对（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。

文档对这套机制的局限写得直接（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）：

- 自动审查本版本没有管理员或用户设置；用户只能在「最近批准」查看并反馈。
- 自动审查看不到 Autopilot 所知的一切，可能出错；判定相符的操作没有审批卡直接运行。
- Autopilot 可能把请求解释得比本意更宽，例如「清理旧项目文件」影响比预期更多的内容；激活向导也提示管理员它可不经逐步确认就行动。

Redmondmag 称管理中心有设置决定某些操作能否自动批准（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})），与 Learn 文档「没有管理员设置」不一致。

推断：Scout 默认全确认、用户逐类放开；Autopilot 反过来默认放行「与请求相符」的操作，把判断交给另一个模型。这降低了审批打扰，但安全边界从用户可见的规则变成了模型判断，且用户和管理员都无法调节。

## 提示注入：只认所有者的消息

只有用户自己的消息算请求；「出现在电子邮件、文档或网页中的指令不构成对操作的授权」，即使声称来自用户；Autopilot 不会要求在聊天中回复确认，用户写「看着不错，发吧」被当作请求（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。应用卡称这些措施降低而不能消除提示注入风险，并把抗提示注入列为评估领域之一，但不公布通过率（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。评估中出现过的次优结果包括「遵循被注入指令」（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

## Entra Agent ID 与必需的安全能力

Copilot 博客写明每个 Autopilot 有自己的 Entra Agent ID 和一个具名管理者，IT 可限定访问并随时阻止，登录和操作以自己的名义记录（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）；UC Today 照此转述（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})）。管理员文档补充：条件访问、ID 保护、访问评审适用于代理身份，更改约一小时生效；以「所有用户」为目标的策略不包括代理用户；Defender 把它列为用户而非代理（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。新闻手册称 Entra Agent ID 预览将扩展到 Autopilot，区分本地智能体与 Autopilot 的活动（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。

要求页列出的安全能力（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）：

| 级别 | 能力 | 获取途径 |
| --- | --- | --- |
| 必需 | Entra Agent ID（自动预配） | — |
| 必需 | 隔离执行环境 Microsoft local (MXC) | Intune Plan 1 或 Microsoft 365 E3 |
| 必需 | 不可变审计日志与成本管理 | Microsoft 365 审计日志（任意商业许可证） |
| 强烈建议 | Entra ID Governance、Global Secure Access、条件访问 | Entra Suite |
| 强烈建议 | Purview DLP 与内部风险管理 | Purview Suite 或 E5 |
| 强烈建议 | Defender XDR | Defender Suite 或 E5 |
| 最安全配置 | Microsoft Perception、条件访问动态控件、动态权限（有限预览） | — |

消息中心通告的强烈建议项另含 Dynamic Agent Risk，与要求页略有出入（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})）。激活向导的「安全策略」一步显示该代理默认的 Entra、Purview、Defender 防护，但它们在各产品中分别管理，「可能未开启」（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。

## 审计与合规的缺口

管理员文档写明（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）：统一审计日志中，AI 与工具调用、以自身身份做的操作记在 Autopilot 名下；代表所有者的文件和邮件读取记在所有者账户下，用内部服务名，「没有代理 ID」，需用会话 ID 关联。用户界面的「活动」不是完整的管理审计记录（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。

官方建议预览期依赖权限与加密挡住内容，「权限与加密是能可靠地让内容远离 Autopilot 的控制手段」，并列出不适用或受限的保护：敏感度标签不排除读取，eDiscovery、保留、法律保留不适用于 Autopilot 会话，DSPM for AI 与活动资源管理器不显示 Autopilot，提示词 DLP 只在部分租户测试、被阻止时只显示通用错误（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。文档建议考虑不为受法律保留或严格保留要求的用户启用，从有边界的工作流和有限受众开始（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。

应用卡把法律申报、医疗决策、绕过审批的金融交易列为不适用场景，高影响决策不要用它自动化（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

## 外部评价（2026-06 至 11）

The Register 6 月称 Scout 由 OpenClaw 驱动，「尚不清楚还包含哪些针对常见 AI 攻击手段的其他保护」，向微软询问未获回复（[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})）。Fortune 转述微软的护栏说法：明确权限、完整审计日志和追踪，由人决定自主程度（[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})）。UC Today 认为身份是买方的分界线，Autopilot 的身份模型可作基准，但提醒不要把 Frontier 推出当成可买的产品（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})）。资料库中仍没有针对 Autopilot 的漏洞报道或独立安全审计。

## 更名前：Scout 的权限与策略（2026-06 至 2026-09）

以下为 2026-11-14 分析的内容。三级权限、`ForcePrompt` 等 Intune 组策略属于 Scout 桌面应用；Autopilot 的新文档没有沿用这些设置。

### 三级权限与默认值

入门页给出默认值：WorkIQ connectivity 开、Shell access 开、Auto-approve 关，须按能力显式启用自动批准（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。shell 命令的示例分级（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）：

| 级别 | 示例 |
| --- | --- |
| 自动批准 | ls、cat、grep、git log 等只读命令 |
| 提示 | npm install、git push、curl、网络请求、文件写入 |
| 拒绝 | rm -rf /、format 等破坏性命令 |

用户可在设置中加允许/拒绝列表、标记必须显式批准的敏感路径；工具组（文件系统、shell、浏览器、WorkIQ）可整体关闭，关闭后「不会出现在系统提示词中」（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。

Microsoft 365 操作中，凡修改共享信息或影响他人的动作（发邮件、发 Teams、建改日历事件与列表项、改收件箱规则、共享文件）都先请求批准（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）。社区实测称可按类别授予长期权限，但删除始终需要明确批准（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。后台模式的权限更严，见[持续执行]({{< relref "/docs/microsoft-autopilot/analysis/continuous-execution" >}})。

负责任 AI FAQ 提醒，无需逐步批准的自主模式只用于低风险场景，不适用于法律文件、医疗决定、绕过审批流程的财务交易等无人审核即需准确的场景（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。

### 提示注入

FAQ 与负责任 AI 文档称外部内容（邮件、网页、Teams 消息）标记为不受信任，作为数据而非指令处理（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})、[负责任 AI 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-overview" >}})）；记忆同样标注来源，外部来源的记忆据以行动前要确认（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。社区作者转述 The Register 称提示注入防御不明确，微软未回应（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。Forrester 的 Pollard 把智能体被操纵或提示注入列为主要风险之一（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。

### 身份、凭据与 Purview

发布博文称每个智能体在自己受治理的 Entra 身份下运行，而非共享匿名服务账户；身份背后的凭据限定于当前任务，在日志或诊断中被隐去；Purview 数据保护策略（敏感度标签、DLP）「在发送或写入任何内容之前即时执行」（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）。Command Line 对谈补充 Agent 365 提供统一控制平面（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。

使用指南说明敏感度标签的具体行为：读到带标签内容后会话敏感度升高，不把带标签内容写入未受保护的目标（Teams 频道、纯文本文件、外部工具），共享机密内容前要求确认（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。但负责任 AI FAQ 写明 Scout 生成或修改的内容「未必自动继承或强制执行这些标签」（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})），且经 GitHub Copilot 处理时敏感度标签强制等 Microsoft 365 保护不适用（见[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})）。社区作者指出这与博文「Purview 已强制执行」的说法有些别扭，认为两者可同时成立（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

推断：Purview 的控制作用在 Scout 写入 Microsoft 365 目标的环节；模型调用经 GitHub 处理的环节不在 Purview 覆盖之内。这是文档拼合得出的理解，官方没有统一说明。

### 管理员策略

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

### 从 OpenClaw 的安全顾虑出发

GeekWire 引微软 Defender 团队的指引：OpenClaw 应视为带持久凭据的不受信任代码执行，「不适合在标准个人或企业工作站上运行」；Shahine 称企业加固是头号任务（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。Semafor 写明企业大多在等待 OpenClaw 的安全漏洞被修补（[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})）。iThome 把微软、Google 等的「云端隔离、人工核准与更严格的安全控管」视为对 OpenClaw 安全顾虑的回应（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

微软称把策略合规贡献回 OpenClaw 上游（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）；OpenClaw 博客列出 Policy 插件、执行批准提示中的密钥脱敏、区分「确定未运行」与「结果未知」的命令等（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。

Command Line 对谈中 Werner 指出隐私方面的难点：「如果我把我的智能体派给你，它不应该告诉你关于我的一切」（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。The Neuron 转述 Shahine：信任是「最关键也最未知」的问题，因为「AI 的超能力是非确定性」（[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})）。

### 外部评价

- Forrester 的 Pollard：Scout 不会带来全新的数据风险，但会「放大已经存在的任何数据治理问题」，区别在于它可能对数据采取行动（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。
- 社区作者建议先清理权限、保持批准提示开启、抵制点「始终允许」，因为它「会比任何审计员更快地发现你的过度共享」（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。
- 资料库中没有针对 Scout/Autopilot 的漏洞报道、安全事件或漏洞赏金信息。

## 资料缺口

- 自动审查模型的误判率；抗提示注入评估的结果。
- Redmondmag 所说「自动批准设置」是否存在，与「没有管理员设置」的关系。
- MXC 在云端 Autopilot 中隔离什么。
- 独立安全审计、漏洞赏金；eDiscovery 与保留何时覆盖 Autopilot。

## 主要资料

- 官方：[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})、[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})（三级权限与默认值）；[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})（影响他人的操作需批准）；[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})、[负责任 AI 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-overview" >}})（提示注入与适用范围）；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（Entra 身份、Purview、零信任）；[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})、[管理员：Intune 部署]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-18-scout-admin-intune-setup" >}})、[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})（管理员策略与访问关口）。
- 媒体：[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})（Defender 指引）；[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})（Forrester 观点）；[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 2026-11 新增官方：[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})（自动审查与审批卡）；[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})（身份、审计、合规缺口、评估）；[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})（必需与建议的安全能力）；[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})；[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})（Entra Agent ID、具名管理者）。
- 2026-11 新增媒体：[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})、[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})。
- industry：[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})。
