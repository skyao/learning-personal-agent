---
title: "Microsoft Autopilot：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 的后台工作以「例程」（routine）为单位，按时间表或事件触发，运行在云端、设备关机也继续；例程只在运行时检查来源，「不是实时监控」，不继承创建对话的全部权限；额度用完时静默停止。官方把它宣传为长期持有角色与目标，但文档层面仍是定时例程。
---

## 概要

- 后台工作叫例程（routine）：按计划或在事件发生时运行，须写明做什么、何时运行、投递到哪里；Autopilot 自行判断一个请求是当前任务还是例程，已有例程恰好匹配则复用。
- 场景页的例程多是固定时刻：工作日 8 点和 13 点分拣收件箱、7:30 会议简报、每周四 15 点周报等；官方称例程「只在运行时检查来源，这不是实时监控」。
- 定时工作不继承创建对话的全部权限，运行时每一步与保存的指令比对，不符则出审批卡。
- 运行在云端，设备关机不中断；但不保证不中断或按时完成，额度用完或不在支出策略内时例程静默停止。
- 停止请求不证明已取消或回滚；IT 阻止用户约需一小时生效。

## 例程

使用页说明例程可按时间表或在事件发生时运行；Autopilot 自行判断请求是当前任务还是例程，已有例程恰好就是所要求的就复用，否则新建而不改已有的；例程只有创建者可见，可开关定时运行、立即运行（Run now）、编辑、删除，暂停不撤销已完成的工作（[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。FAQ 要求例程写明做什么、何时运行、投递位置，计划运行不继承创建时对话的全部上下文（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。应用卡称自动化「使用计划和完整保存的指令」，按保存的身份、目标位置和权限运行（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。创建时 Autopilot 会建议一组起始例程供审阅（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。

场景页的示例（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）：

| 例程 | 时间 |
| --- | --- |
| 收件箱分拣 | 工作日 8 点和 13 点 |
| 会议简报 | 7:30 |
| 每日简报 | 东部时间 8 点 |
| 周报 | 每周四东部时间 15 点 |
| 承诺跟踪、跟进循环、盯住某事变化、保护日历专注时间、项目推进 | 按需 |

TestingCatalog 举的例子是每周日发送的周报邮件（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）；Tech Community 博文作者的「Sunday Reset」通过邮件投递，回复即可继续对话（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。博文的另一个例子「把我送到 Ignite 再送回来」包括订机票酒店（批准后预订）、注册、地面交通和报销（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。

活动标签页分「Working now」与「Needs your input」，可按类型（Chats、Routines、Files、Approvals）、来源（Teams、Outlook）、状态（Needs you、In progress、Didn't finish、Completed）筛选；用户可在对话中回复来重定向或停止（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。

## 定时，而非实时

场景页写明「例程只在运行时检查来源，这不是实时监控」，云端运行也不保证简报在特定时间前准备好（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。应用卡称监控条件本身并不使每个事件或工作信号都成为触发器，监控不保证立即检测到（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

应用卡另声明，Teams 中的 @Copilot 和其他 Copilot 体验里的并行智能体都不构成 Autopilot 的同等能力（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。同期 Cowork 有按计划或事件运行任务的 Automations（[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})），Today Feed 全天刷新需要 Copilot 额度（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）；三者与 Autopilot 例程的分工，资料没有说明。

## 权限与停止

定时工作不继承创建对话的全部权限；创建或更改自动化本身要经自动审查（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。运行期间每一步与保存的指令比对，不符时审批卡出现在该自动化的投递聊天；审批卡过期未答，该操作不运行，任务其余部分继续（[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。详见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})。

停止与结果的口径：

- 「停止请求并不证明已经开始的操作已被取消或回退」；审批不证明操作已完成，须在目的地核实（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。
- IT 阻止用户约需一小时传到 Autopilot，代表所有者进行的工作可能持续更久，「不要依赖它来立即停止」（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。
- 用户不在支出策略覆盖内或策略达上限时，Autopilot 停止运行自动化和监视工作、不响应新请求，且不向用户显示说明；自动化可能显示为已暂停（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。
- 后台工作依赖已授权访问与可用服务，待处理审批、缺失权限或服务问题都可能阻塞计划运行（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。

## 「长期角色」的宣传

Copilot 博客与新闻手册称 Autopilot 监视 Teams 频道、跟进邮件、运行周期性工作、无需再次提示就推进项目，示例是供应商评审流程（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）；这一说法 9 月更名时已出现：给它名字、角色和目标，它可在数天后重拾项目（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})、[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})）。产品页称它处理跨数天、数周的目标、决策和承诺，「带给你决策，而不是通知」（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})）。博文作者称「主动不意味着不断打扰我」，结果有时是完成的任务，有时是准备到可迅速决定的状态（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。Redmondmag 把它与 Cowork 区分为：Cowork 完成单个多步任务，Autopilot 管理没有明确终点的持续职责（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。

推断：文档层面的持续执行是「定时或事件例程 + 运行时检查」，「长期角色」主要体现在记忆和身份上，而不是实时的事件驱动；打扰频率、例程数量与时长上限，资料都没有给出。

## 资料缺口

- 例程的数量、频率、运行时长上限；事件触发支持哪些事件。
- 失败重试策略；「Didn't finish」之后的处理。
- Autopilot 例程、Cowork Automations、Today Feed 之间的分工。
- 数周以上的运行稳定性报告。

## 主要资料

- 官方：[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})（例程与示例）；[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})（权限、停止、额度）；[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（长期角色的说法）；[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})。
- 媒体：[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})。
