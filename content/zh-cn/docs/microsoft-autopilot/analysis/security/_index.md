---
title: "Microsoft Autopilot：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 的审批靠「自动审查」：第二个 AI 模型在操作运行前把它与用户请求比对，相符就直接运行，不符才出审批卡；付款和敏感浏览器步骤始终要批准，审批卡没有「始终允许」，本版本没有面向用户或管理员的审查设置。每个 Autopilot 有自己的 Entra Agent ID 和具名管理者，必需能力含 MXC 与审计日志；官方坦承 eDiscovery、保留、DSPM for AI 不覆盖，提示词 DLP 受限。没有独立安全审计或漏洞报道。
---

## 概要

- 自动审查：第二个 AI 模型在操作运行前把它与用户请求（含「只读」「先别发」等限制）比对，相符的直接运行、不出审批卡，不符或无法检查的才等用户批准。
- 分级：读取、搜索、起草不中断（抽查一小部分）；发送、共享、删除、更改内容和创建或更改自动化由自动审查决定；付款和其他敏感浏览器步骤始终需批准。
- 审批卡只有单次「允许」和「拒绝」，没有「始终允许」，过期未答则不运行；本版本自动审查没有用户或管理员设置，文档承认它可能出错。
- 提示注入：只有所有者本人的消息算请求，邮件、文档、网页中的指令不构成授权；官方称能降低而不能消除风险。
- 身份与治理：每个 Autopilot 有自己的 Entra Agent ID 和具名管理者，IT 可限定范围、随时阻止（约一小时生效）；Entra Agent ID、MXC 隔离执行环境、审计日志为必需能力。
- 合规缺口由官方列出：敏感度标签不排除读取，eDiscovery、保留、法律保留不覆盖会话，DSPM for AI 看不到它，提示词 DLP 只在部分租户测试；代表所有者的读取在审计日志中没有代理 ID。

## 自动审查：第二个模型

「Autopilot 如何审查操作」一页说明，Autopilot 用第二个 AI 模型在操作运行前审查，把操作与用户的请求比对，包括隐含步骤和「只读」「先别发」一类限制；无论以用户还是以自己的身份行事，规则相同（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。

| 操作类型 | 处理 |
| --- | --- |
| 读取、搜索、起草 | 不中断；小部分被抽查 |
| 发送、共享、删除、更改邮件/日历/文件/聊天；创建或更改自动化 | 自动审查判断：与请求相符则直接运行，不符或无法检查则出审批卡 |
| 付款及其他敏感的浏览器步骤 | 始终需要批准，即使是用户提出的 |

来源：[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})。入门页的说法是「Autopilot 不要求批准每一步」，所有付款等待允许或拒绝（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。Edge 中须批准的步骤包括更改账户、结账或付款、输入银行卡、永久删除、向外部站点提交个人信息或消息（[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})）。场景页的惯例是发送回复、移动会议、发提醒前先问（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。

审批卡出现在 Teams 一对一聊天（以及发起请求的 Copilot 对话），显示触达对象的姓名与邮箱、外部人员标「外部」、只读预览和执行身份；只有「允许」（单次）和「拒绝」，「没有『始终允许』的选项」；过期未答则该操作不运行，任务其余部分继续；卡片会说明出现原因（可能超出请求、需确认一致、安全检查未能完成）（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。自动化运行中每一步与保存的指令比对（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。

文档对这套机制的局限写得直接：

- 本版本自动审查没有管理员或用户设置；用户只能在「最近批准」查看并反馈（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。
- 自动审查看不到 Autopilot 所知的一切，可能出错；判定相符的操作没有审批卡直接运行（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。
- Autopilot 可能把请求解释得比本意更宽，例如「清理旧项目文件」影响比预期更多的内容；激活向导也提示管理员它可不经逐步确认就行动（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。

Redmondmag 称管理中心有设置决定某些操作能否自动批准（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})），与 Learn 文档「没有管理员设置」不一致。

推断：这套设计默认放行「与请求相符」的操作，把判断交给另一个模型，降低了审批打扰；代价是安全边界从用户可见的规则变成模型判断，而且用户和管理员都无法调节。

## 提示注入：只认所有者的消息

只有用户自己的消息算请求；「出现在电子邮件、文档或网页中的指令不构成对操作的授权」，即使声称来自用户；Autopilot 不会要求在聊天中回复确认，用户写「看着不错，发吧」被当作请求（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。应用卡称这些措施降低而不能消除提示注入风险，把抗提示注入列为评估领域，但不公布通过率；评估中出现过「遵循被注入指令」的次优结果（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

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

消息中心通告的强烈建议项另含 Dynamic Agent Risk，与要求页略有出入（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})）。激活向导的「安全策略」一步显示该代理默认的 Entra、Purview、Defender 防护，但它们在各产品中分别管理，「可能未开启」（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。技能与例程不授予访问权，执行账户须对任务所用资源有权限（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。

## 审计与合规的缺口

统一审计日志中，AI 与工具调用、以自身身份做的操作记在 Autopilot 名下；代表所有者的文件和邮件读取记在所有者账户下，用内部服务名，「没有代理 ID」，需用会话 ID 关联（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。用户界面的「活动」不是完整的管理审计记录（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。

官方建议预览期依赖权限与加密挡住内容——「权限与加密是能可靠地让内容远离 Autopilot 的控制手段」——并列出不适用或受限的保护：敏感度标签不排除读取，eDiscovery、保留、法律保留不适用于 Autopilot 会话，DSPM for AI 与活动资源管理器不显示 Autopilot，提示词 DLP 只在部分租户测试、被阻止时只显示通用错误（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。文档建议考虑不为受法律保留或严格保留要求的用户启用，从有边界的工作流和有限受众开始（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。应用卡把法律申报、医疗决策、绕过审批的金融交易列为不适用场景（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

## 背景与外部评价

产品起点是 OpenClaw 的安全顾虑：GeekWire 引微软 Defender 团队的指引，OpenClaw 应视为带持久凭据的不受信任代码执行，「不适合在标准个人或企业工作站上运行」（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。The Register 6 月称「尚不清楚还包含哪些针对常见 AI 攻击手段的其他保护」，向微软询问未获回复（[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})）。Fortune 转述微软的护栏说法：明确权限、完整审计日志和追踪，由人决定自主程度（[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})）。Forrester 的 Pollard 认为这类智能体会「放大已经存在的任何数据治理问题」（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）；社区作者建议先清理过度共享、不要轻易放开权限（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。UC Today 认为身份是买方的分界线，Autopilot 的身份模型可作基准（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})）。

资料库中没有针对 Autopilot 的漏洞报道、安全事件、独立审计或漏洞赏金信息。

## 资料缺口

- 自动审查模型的误判率；抗提示注入评估的结果。
- Redmondmag 所说「自动批准设置」是否存在。
- MXC 在云端 Autopilot 中隔离什么。
- 独立安全审计、漏洞赏金；eDiscovery 与保留何时覆盖 Autopilot。

## 主要资料

- 官方：[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})（自动审查与审批卡）；[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})（身份、审计、合规缺口、评估）；[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})（安全能力）；[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})；[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})（Entra Agent ID、具名管理者）。
- 媒体：[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})、[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})、[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})。
- 社区：[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})。
- industry：[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})。
