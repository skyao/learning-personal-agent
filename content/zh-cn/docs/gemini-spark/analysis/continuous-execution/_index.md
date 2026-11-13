---
title: "Gemini Spark：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Spark 用「任务、计划、技能」三块拼出后台工作：计划可按时间、Gmail 来信或话题事件触发，上限为 50 个活跃计划、15 个并发任务；实测中它交卷快、跟进弱，很少主动发现问题。
---

## 概要

- 官方把持续执行拆成三块：任务是「做什么」，计划是「何时做」，技能是「如何做」。三者在 5 月 19 日首发时就已具备。
- 计划有三种触发方式：按时间（一次到每年）、Gmail 监控（来信符合筛选条件）、话题监控（新闻、财经、体育、本地活动等出现特定事件，6 月起）。官方提醒运行时间只是大致的，不适合追踪变化很快的数据。
- 数量上限是 50 个活跃计划、15 个并发任务；达到计算用量或并发上限时计划不运行。关闭任务模式或降级订阅，计划暂停而不删除。
- 10 月改版后，计划集中在「Scheduled」页面，按进行中、已暂停、已完成、建议整理。
- 实测中 Spark 的「后台」能力不突出：WIRED 要它研究 30 分钟，它几分钟就交卷；日程冲突没指出来；Enterpret 的用户讨论统计里，「完成任务」一项排 12 款中第 10。每日晨报（Daily Brief）在官方资料里是另一个智能体，不属于 Spark。

## 任务、计划、技能三块

帮助页称三者可以看作「做什么、何时做和如何做」；任务里的计划与 Gemini 普通聊天中的「已计划操作」不是一回事（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。I/O 发布稿给的例子是设置重复任务或触发器，比如每月解析信用卡账单、标记新增或隐藏的订阅，或教它一个技能每天汇总孩子学校的截止日期（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})）。产品页的例子更偏工作：每周一上午 9:00 扫描收件箱出简报和优先待办，并在日历上排深度工作时段；收到询问摄影服务的邮件时，提取客户姓名、日期记入「Client Tracker」表并建 Drive 文件夹（[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})）。

## 三种触发方式

| 类型 | 触发条件 | 创建方式 | 资料 |
| --- | --- | --- | --- |
| 基于时间 | 一次、每小时、每天、每周、每月、每年 | 可手动创建，也可对话创建 | [帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}}) |
| Gmail 监控 | 收到符合筛选条件的邮件 | 在任务线程或 Live 对话中创建 | [帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}}) |
| 话题监控 | 新闻、财经、体育、本地活动等出现特定事件 | 同上 | [帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})、[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}}) |

话题监控 6 月 30 日上线，官方举的例子是球赛一结束就推送集锦、股价到达阈值时生成财务报告，关注范围除邮件外包括博客、新闻、社交媒体、金融、购物、天气、体育（[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})、[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})）。

官方同时写明了它不适合做的事：监控「仍不适合追踪变化很快的数据」，也不适合时间要求极高的任务，例如门票一开售就通知；计划的运行时间是大致的，高流量期可能延迟（[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})）。

## 生命周期与上限

截至 2026-11-10 的帮助页（[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})、[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})）：

- **状态**：计划分活跃、已暂停、已完成；任务分就绪、需要关注、进行中。已完成的计划只能删除，不能编辑或恢复。
- **上限**：活跃计划最多 50 个，达到上限要先暂停或删除一个；同时运行的任务最多 15 个。帮助页正文写的是「任务当前可拥有的活跃计划数量上限为 50」，资料页摘要写作「活跃计划最多 50 个」，是每个任务 50 个还是总共 50 个，原文措辞不够明确。
- **不运行的原因**：达到计算用量上限、已有 15 个并发任务、运行时间本身有差异、高流量延迟。
- **时区**：时间计划锁定在创建时所在地点的时区，旅行时仍按原时区运行，搬家后要让 Gemini 修改。
- **停止与接管**：用户可随时停止或接管任务；用户拒绝某项操作时，Gemini 停下且「不会尝试其他方式来完成它」。
- **关停**：关闭任务模式后所有计划自动暂停；取消或降级订阅后，进行中的任务会做完，计划暂停但不删除；删除任务线程会删除其中所有计划。

第三方转述的数字与官方一致：Datawhale 综述与鸿煊称「最多 50 个活动计划，同时运行任务上限 15」，Freistyle AI 称「一次运行最多 15 项任务」（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})、[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。

## 界面：从独立空间到「Scheduled」页面

10 月以前 Spark 是 Gemini 里的独立空间。2026-10-01 前后，Chrome Unboxed 在网页版看到侧栏新增「Scheduled」区域，集中放定时和重复任务，可检查、暂停、调整（[Chrome Unboxed]({{< relref "/docs/gemini-spark/sources/media/2026-10-01-chromeunboxed-ditching-spark-brand" >}})）。9to5Google 2026-10-12 报道 Android 版改版后的「Scheduled」页面，按进行中（Active）、已暂停（Paused）、已完成（Completed）、建议（Suggested）整理任务与计划（[9to5Google]({{< relref "/docs/gemini-spark/sources/media/2026-10-12-9to5google-task-redesign" >}})）。

一名开发者论坛用户反映，并入聊天后侧栏里普通聊天和 Spark 任务混在一起，没有文件夹或标签区分（[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})）。这是单个用户的看法。

## 主动联系用户

- 7 月 13 日起，需要用户输入时的通知更详细；用户正在网页版看这个任务线程时，不再往手机推送通知（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})）。
- 6 月预告「即将」支持从手机给 Mac 上的 Spark 派多步骤任务，如找到销售报告、取出营收数字再发邮件（[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})）；7 月 14 日远程控制 Mac 上线（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})）。
- I/O 发布稿把每日简报（Daily Brief）列为与 Spark 并列的「一个新的智能体」（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})）。Top5Apps 把「主动的 Daily Brief」算作 Spark 的功能（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})），与官方说法不符。

## 实测：交卷快，跟进弱

- The Verge（2026-06-01）：一个多步骤任务约 4 分钟完成，但作者发现自己一直盯着它或看手机通知，质疑「每一步都要你微观管理」的价值（[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})）。
- WIRED 六款同测（2026-10-27）：要求花 30 分钟做深度研究，只有 Muse 和 Dots 在大部分时间里持续研究，其他几款（包括 Spark）瞬间或几分钟后给出结果；日程冲突测试中 Spark 没有指出下午 2 点会议与「给妈妈打电话」提醒的重叠，得 1/5，同项只有 Dots 得 5/5（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。
- Enterpret 统计 2026-08-31 至 11-01 的用户讨论：「完成任务」一项 Spark 排 12 款中第 10，这一项占 Spark 用户讨论的三分之一以上（[Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})）。

推断：官方的计划机制（三种触发、50 个计划、话题监控）设计得比较完整，但实测资料几乎都在测单次任务，没有一篇长期跑计划或监控的测试；「后台工作」的实际效果目前缺少证据。

## 资料缺口

- 长期运行计划和话题监控的实测（数周以上），包括延迟、漏报和误报。
- Spark 是否会在没有计划的情况下主动联系用户；通知的频率控制。
- 50 个活跃计划的口径（每个任务还是总数）。
- 从手机给 Mac 派任务的实测。

## 主要资料

- 官方：[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})（触发、上限、生命周期）；[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})；[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})；[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})、[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})、[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})、[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})（示例与上线时间）。
- 媒体：[Chrome Unboxed]({{< relref "/docs/gemini-spark/sources/media/2026-10-01-chromeunboxed-ditching-spark-brand" >}})、[9to5Google]({{< relref "/docs/gemini-spark/sources/media/2026-10-12-9to5google-task-redesign" >}})（Scheduled 页面）；[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})；[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})。
- 社区：[Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})；[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})（Daily Brief 的错误归属）；[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})、[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})（数字转述）；[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})。
