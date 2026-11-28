---
title: "Microsoft Autopilot：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 的持续执行以「例程」（routine）为单位：按时间表或事件触发，运行在云端、设备关机时也继续；例程只在运行时检查来源，「不是实时监控」，不继承创建对话的全部权限，额度用完时静默停止。Scout 时期的 Heartbeat 与 Automations 在新文档中没有再出现。
---

## 概要

- Autopilot 的后台工作叫例程（routine）：按计划或在事件发生时运行，须写明做什么、何时运行、投递到哪里；Autopilot 自行判断一个请求是当前任务还是例程，已有例程恰好匹配则复用（[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。
- 场景页给出的例程多是固定时刻：工作日 8 点和 13 点分拣收件箱、7:30 会议简报、每周四 15 点周报等；官方称例程「只在运行时检查来源，这不是实时监控」，监控条件也不使每个事件都成为触发器（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。
- 定时工作不继承创建对话中的全部权限，运行时每一步都与保存的指令比对，不符则在该例程的投递聊天里出审批卡（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。
- 云端运行使设备休眠不再中断工作，这是相对 Scout 桌面版的主要变化；但官方不保证不中断或在特定时间前完成，额度用完或不在支出策略内时例程静默停止（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。
- 停止请求不证明已取消或回滚，审批不证明已执行；IT 阻止用户约需一小时生效（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。

## 2026-11：例程

使用页说明例程可按时间表或在事件发生时运行；Autopilot 自行判断请求是当前任务还是例程，已有例程恰好就是所要求的就复用，否则新建而不改已有的；例程只有创建者可见，可开关定时运行、立即运行、编辑、删除，暂停不撤销已完成的工作（[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。FAQ 要求例程写明做什么、何时运行、投递位置，计划运行不继承创建时对话的全部上下文（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。应用卡称自动化「使用计划和完整保存的指令」，按保存的身份、目标位置和权限运行（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

场景页的示例（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）：

| 例程 | 时间 |
| --- | --- |
| 收件箱分拣 | 工作日 8 点和 13 点 |
| 会议简报 | 7:30 |
| 每日简报 | 东部时间 8 点 |
| 周报 | 每周四东部时间 15 点 |
| 承诺跟踪、跟进循环、盯住某事变化、保护日历专注时间、项目推进 | 按需 |

TestingCatalog 举的例子是每周日发送的周报邮件（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）；Tech Community 博文作者的「Sunday Reset」也通过邮件投递，回复邮件即可继续对话（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。

活动标签页分「Working now」与「Needs your input」，可按类型（Chats、Routines、Files、Approvals）、来源（Teams、Outlook）、状态（Needs you、In progress、Didn't finish、Completed）筛选（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。

## 定时而非实时

场景页写明「例程只在运行时检查来源，这不是实时监控」，云端运行也不保证简报在特定时间前准备好（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。应用卡称监控条件本身并不使每个事件或工作信号都成为触发器，监控不保证立即检测到（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

应用卡另声明，Teams 中的 @Copilot 和其他 Copilot 体验里的并行软件智能体都不构成 Autopilot 中的同等能力（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。同期 Cowork 也有按计划或事件运行任务的 Automations（[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})），Today Feed 全天刷新需要 Copilot 额度（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})），三者与 Autopilot 例程的分工资料没有说明。

## 权限与停止

定时工作不继承创建对话的全部权限；创建或更改自动化本身要经自动审查（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。运行期间每一步与保存的指令比对，不符时审批卡出现在该自动化的投递聊天；审批卡过期未答，该操作不运行，任务其余部分继续（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})。

停止和结果的口径（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）：

- 「停止请求并不证明已经开始的操作已被取消或回退」；审批不证明操作已完成，须在目的地核实。
- IT 阻止用户约需一小时传到 Autopilot，代表所有者进行的工作可能持续更久，「不要依赖它来立即停止」。
- 用户不在支出策略覆盖内或策略达上限时，Autopilot 停止运行自动化和监视工作、不响应新请求，且不向用户显示说明；自动化可能显示为已暂停（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。

## 长期角色的宣传

Copilot 博客和新闻手册沿用 9 月的说法：监视 Teams 频道、跟进邮件、运行周期性工作、无需再次提示就推进项目，示例仍是供应商评审流程（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。产品页称 Autopilot 处理跨数天、数周的目标、决策和承诺，「带给你决策，而不是通知」（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})）。博文作者称「主动不意味着不断打扰我」，结果有时是完成的任务，有时是准备到可迅速决定的状态（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。Redmondmag 把它与 Cowork 区分为没有明确终点的持续职责（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。

推断：文档层面的持续执行仍是「定时例程 + 运行时检查」，与 Scout 的 Heartbeat、Automations 相近；「长期角色」主要体现在记忆和身份上，而不是事件驱动的实时触发。

## 更名前：Scout 的 Heartbeat 与 Automations（2026-06 至 2026-09）

以下为 2026-11-14 分析的内容。Autopilot 的新文档没有出现 Heartbeat 一词，只有例程；桌面版「设备休眠即暂停」的限制随云端化不再适用。

### Heartbeat：定期检入

FAQ 与使用指南给出设置项：提示词（每次检入做什么，如分拣收件箱、检查日程冲突）、间隔（15 分钟、30 分钟、1 小时或 2 小时）、工作日和工作时间（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。Heartbeat 面板显示最近的检入日志。

Heartbeat 有独立的权限策略，通常更严：外发的邮件、Teams 消息「只使用通用内容——绝不使用私有数据」；暂定的日历事件视为忙碌；通常需批准的操作在 Heartbeat 下被跳过。用户可在面板中自定义这套权限（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。负责任 AI FAQ 建议把后台权限与交互权限分开配置（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。

### Automations：时间表、条件、一次性

Automations 的触发类型是 Schedule 或 Condition（条件为真时触发，需设检查频率），可勾选 One-shot（运行一次后停用），并单独设置推理强度与上下文大小；可启用/禁用、编辑、查看历史、删除，并可从 GitHub 仓库导入定义（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。8 月更新加入了自动化运行时会话过期的就地恢复（[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。TestingCatalog 称其为内置的「类似 Zapier 的编排」（[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})）。

管理员可用策略 `DisableHeartbeat`、`DisableWorkflows` 分别禁用两者（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）。社区作者建议把 heartbeat 和自动化权限严格收紧，因为它们在无人注视时运行（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

### 实际用例

| 来源 | 用例 | 性质 |
| --- | --- | --- |
| [Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}}) | 每天早上监控 GitHub 讨论，找出各应用功能负责人并开 Teams 聊天跟踪；设置外出回复时自行推算日期、检查冲突、创建时间块 | 微软员工自述 |
| [Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}}) | 每天四次检查是否还有需要关注的事；CRM 管道检查（浏览器导航、检查商机、导出到 SharePoint、发 Teams 消息）端到端完成 | 社区实测 |
| [Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}}) | 跨时区协调会议、识别交付物并在日历预留时间、发现停滞的决策 | 官方宣称 |

### 桌面版的限制

社区作者指出，桌面版要求机器保持运行，设备休眠时自动化暂停；云端版当时为有限访问，可不依赖设备运行（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。FAQ 说明连接中断时工作暂停、恢复后继续（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）；社区综述把「连接断开会使工作中断」列为已记录的局限（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

### 9 月：从定时任务到长期角色

更名文章称：给 Autopilot 一个名字、角色和目标，它监视频道、跟进线程、运行周期性工作，「在数天后重新拾起一个项目，无需等待提示」；示例是搭建并管理完整的供应商评审流程。「你设定目标和边界；Autopilot 处理其余的事」（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。同文中主动起草、提出日程变更的 Today 属于 Copilot Home，不是 Autopilot。iThome 称其触发方式为文字、@mention 或预设任务（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。社区作者的区分是：Cowork 端到端完成一项任务后交回，Autopilot 长期持有一个角色和一个目标（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

发布前，GeekWire 转述 Shahine 的设想：Lobster 提出可采取的行动方案并等待用户批准，而非持续被提示（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。

推断：Scout 的持续执行是「用户写提示词 + 定时器」，主动性的边界由权限策略划定；Autopilot 的宣传转向「目标驱动」，但如何控制打扰频率、任务数量与时长上限，资料都没有给出。

## 资料缺口

- 例程的数量、频率、运行时长上限；事件触发支持哪些事件。
- 失败重试策略；「Didn't finish」后的处理。
- Autopilot 例程、Cowork Automations、Today Feed 之间的分工。
- 云端版数周以上的运行稳定性报告。

## 主要资料

- 官方：[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})（Heartbeat 与 Automations 设置）；[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})、[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})（后台权限与禁用）；[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})；[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}})；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（长期角色）。
- 媒体：[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})、[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})（用例与休眠限制）；[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 2026-11 新增官方：[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})（例程与示例）；[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})（权限、停止、额度）；[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})。
- 2026-11 新增媒体：[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})。
