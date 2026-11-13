---
title: "Grok Bot：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 的持续执行以「例程」（Routine）为核心：每个 Bot 可挂最多 50 个按时间表或按 Slack、GitHub、邮件、webhook 等事件触发的例程，在云端运行、不依赖用户设备；限制主要来自用量额度与每小时运行次数，写操作仍要用户批准，无人在场时发起的批准约 30 分钟后过期。
---

## 概要

- 官方文档把持续执行拆成两件事：技能（Skill）说明「怎么做」，例程（Routine）说明「何时做」。例程可按时间表运行，也可由 Slack 消息、GitHub、Linear、Sentry、PagerDuty 事件、发到 Bot 邮箱的邮件或 webhook 触发，在云端运行，合上笔记本不影响（[文档：技能、例程与自动化]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-skills-routines-and-automations" >}})）。在社区比较中，事件触发的种类是 Grok Bot 与其他跟踪产品的主要区别。
- 例程有明确的数量与频率上限：每个 Bot 最多 50 个例程，日程间隔至少 5 分钟，所有例程合计每小时最多 300 次、单个例程最多 200 次，超限即失败且不自动重试。合计上限在 2026-10-23 由 100 次提高到 300 次。
- 实际约束更多来自用量：每次运行（包括「测试」）都消耗用量，官方提醒每小时的日程或繁忙频道的 Slack 触发器「可能一天就用掉一周的用量」。
- 无人值守不等于自动执行：官方建议发送、购买、删除、发布、生产变更始终放在批准之后。用户不在场时开始的工作，其批准约 30 分钟后过期（2026-10-26 前为约 10 分钟）。
- 主动性由三部分构成：主 Bot 主动找可分担的工作（2026-10-02 起）、Bot 自己创建和修改例程、「默认安静」的汇报约定。实测中，简报、监控类周期任务运行较稳；资料中没有完成率等量化数据。

## 例程：按时间表或事件唤醒 Bot

官方介绍称，Bot「在你离开时继续运行，只在需要判断时把你拉进来」（[更多计划]({{< relref "/docs/grok-bot/sources/official/2026-08-26-grok-bot-more-plans" >}})）。入门指南把与 Bot 的交流方式分为三种：聊天、例程与触发器、其他 Bot（[Grok Bot 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})）。设计文章写道，团队最初把例程当作次要配置，后来因为它对自主工作越来越重要，「把它们移到了 Bot 的主界面」（[设计 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-03-designing-grok-bot" >}})）。

截至 2026-11-05 的帮助文档，例程的触发方式如下（[帮助：例程]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-routines" >}})、[文档：使用 Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})、[帮助：Bot 邮箱]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-agent-email" >}})）：

| 触发方式 | 要点 |
| --- | --- |
| 时间表 | 每小时、间隔、每日等，按设置中 Bot 的时区运行；间隔至少 5 分钟 |
| Slack | 在 Bot 被提及、出现某词或短语、用户对消息做出反应或任意消息时启动；可监视单个频道或整个 Slack。触发器属于例程，不属于 Slack 应用，需要在拥有该 Bot 的 Cursor 账户上连接 Slack |
| GitHub、Linear、Sentry、PagerDuty、Microsoft Teams | 更新日志 v0.17.0（2026-08-12）已列出 Teams、Linear、Sentry、PagerDuty 触发；v0.56.0（2026-09-17）起 GitHub 例程可监视单个拉取请求 |
| 邮件 | 新邮件不会自行唤醒 Bot，只有用户建立的例程会处理来信；可监视任意人、特定地址或整个域，不能按主题过滤；默认只对通过标准邮件认证的发件人运行 |
| webhook | 例程详情给出 POST URL 和密钥，以 `Authorization: Bearer` 鉴权；返回 200 只表示「接受了调用并启动了一次运行」，不表示 Bot 已完成指令 |
| 只有新活动才触发 | 触发器建立之前的消息、事件不会触发运行 |

例程通常通过聊天让 Bot 创建或修改，也可以由 Bot 自己建立。有用户报告其 Bot「能够创建（和更新）自己的例程」，如监视日历、等待 Slack 的特定回复、每天早上运行（[James Pember 实测]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})）。另一位作者在对话中让 Bot 建了工作日 9:04 的 AI 简报和每周一 9:05 的发帖复盘两个例程，称「整个过程我一个配置项都没填」（[鱼皮实测]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。

技能可以手写，也可以演示生成。「教一个任务」（Teach a task）在一对一会话的电脑视图中录制可见操作，最长十分钟，不录麦克风，生成技能草稿后再挂到例程上；官方称该功能逐步推出（[文档：技能、例程与自动化]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-skills-routines-and-automations" >}})、[FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。

## 生命周期与数量限制

| 项目 | 规定 | 资料 |
| --- | --- | --- |
| 例程数 | 每个 Bot 最多 50 个；删除 Bot 同时删除其例程 | [文档：技能、例程与自动化]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-skills-routines-and-automations" >}}) |
| 运行记录 | 每个例程保留最近 20 条；状态分运行中、成功、失败，失败时显示原因 | 同上；[帮助：例程]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-routines" >}}) |
| 频率 | 日程间隔至少 5 分钟；所有例程合计每小时最多 300 次，单个例程最多 200 次；超限报 `Automation run rate limit exceeded`，不自动重试 | 同上 |
| 首次运行 | 新例程不在创建时运行，等下一个预定时间；「测试」会执行真实工作，可能改文件、调用已连接应用，并消耗用量 | 同上 |
| 管理 | 桌面在 Bot 详情页、手机在 Bot 资料页，可暂停、恢复、测试、编辑、删除；删除不可撤销 | 同上；[文档：使用 Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}}) |
| 长期无人 | 用户离开很久后，Grok Bot 可能询问是否继续运行例程，不回应就暂停 | [文档：使用 Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}}) |
| 停止 | 「立即停止」可结束当前工作，但不会撤销已完成的动作；用户的直接消息优先于后台工作 | 同上 |

帮助文档还承认一个已知问题：所有 Grok Bot 例程共享的某个限制会让部分运行失败，即使用户自己的运行次数低于上限也会遇到，官方称「我们的工程师正在修复」，失败的运行需要用户自己重跑（[帮助：例程]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-routines" >}})）。

更新日志记录了几项与生命周期有关的改动（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）：

| 版本与日期 | 改动 |
| --- | --- |
| v0.56.0（2026-09-17） | 让 Bot 停止时，它交接出去的其他 Bot 和它启动的云代理也一并停止 |
| v0.65.0（2026-09-30） | 自动更新默认开启，Grok Bot 会在用户离开时重启以应用更新 |
| v0.75.2（2026-10-22） | 例程遇到已登出的连接器时，聊天显示「重新连接」卡片，每天最多一次 |
| v0.75.5（2026-10-23） | 例程每小时合计上限由 100 次提高到 300 次，单个例程最多 200 次 |
| v0.78.5（2026-11-04） | 对常用清单定时补货时，每笔订单请求一次批准 |
| v0.79.2（2026-11-05） | 一次性例程运行一次后关闭 |

官方文档称关闭应用、笔记本或手机不会停止后台回合或例程（[FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})、[文档总览]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-overview" >}})）。用户实测也提到，把本地选题工作流搬到云端后，电脑关机也能每天收到简报，但「它工作的速度不算快，适合交代完任务就去忙别的」（[鱼皮实测]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。

## 用量是频率的实际上限

每次运行都消耗用量，从不运行的例程不消耗。文档写明，每小时日程、短间隔或繁忙频道上的 Slack 触发器「可能一天就用掉一周的用量」；每周用量用得太快时，建议先暂停不需要的例程、放宽日程、收窄 Slack 触发器，再考虑升级套餐（[文档：技能、例程与自动化]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-skills-routines-and-automations" >}})）。群聊中每条 Bot 回复，包括 Bot 之间的消息，都计入用量（[帮助：群聊]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-group-chats" >}})）。

Pat Simmons 的对比实验中，Grok Bot 在 YouTube 任务里「自己完成了全部工作，而不是交给其他 bot」，期间两次触到用量限制（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。另一面，鱼皮的文章称跑完上述任务后每周额度只用掉了 1%（[鱼皮实测]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。两者任务量和套餐不同，不能直接比较。

推断：例程的硬上限（每小时 300 次）对个人用户很少构成约束；决定能挂多少例程、多高频率的，主要是每周用量额度。官方把「放宽日程、收窄触发器」写进文档，说明高频例程耗尽额度是常见问题。

## 无人值守时的批准

官方建议按顺序放权：先让 Bot 做只读、准备类工作，审阅结果，再加经批准的动作或例程；「只有在定义了重试和失败情况后，才创建例程」；发送、购买、删除、发布和生产变更始终放在批准之后（[文档：用例]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-use-cases" >}})）。官方给出的岗位起始提示，每条都停在审核点之前，例如「返回一份审阅清单；不要发送或登记任何人」。工作指南中的示例提示要求 Bot 的定时器创建时处于停用（Disabled）状态，等用户手动启用（Enable）（[用 Grok Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-09-24-guide-grok-bot-for-work" >}})）。

无人在场时发起的工作，例如例程或另一个 Bot 发来的消息，其批准约 30 分钟后过期；用户所在聊天中的批准会一直等待（[FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。这个时长有过变化：一篇 2026-10 初的社区成本对比依据 xAI 文档写的是约 10 分钟，过期后操作不执行，并以此与 Claude Duet「完成其余任务、稍后把审批带回」的做法对比（[四产品成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。更新日志 v0.77.0（2026-10-26）改为 Auto-review 批准卡「保持打开 30 分钟，而不是 10 分钟」，同时规定用户用自己的话启动的后台工作不再需要 Auto-review 批准才能开始（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

官方客服案例展示了「先提议、人批准、再分批执行」的流程：IncidentWatch 每五分钟审阅过去 15 分钟的工单，发现不属于已知事故的激增就提醒值班工程师；IncidentSweep 在工程师批准后分小批处理，批准后不再追加工单，出错即停止并报告。官方称 9 月 18 日的一次事故中，它在约 10 分钟内清理了 204 张工单（[IncidentSweep]({{< relref "/docs/grok-bot/sources/official/2026-10-20-incident-sweep" >}})）。

## 主动性：主 Bot、自建例程与「默认安静」

更新日志 v0.66.0（2026-10-02）写道，主 Bot（以星标标记）「会发现自己可以替你分担的工作，并提供处理选项」（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。官方销售文章把主动性列为 Team Bots 的一项原则（[Grok Bot 用于销售]({{< relref "/docs/grok-bot/sources/official/2026-10-27-grok-bot-sales" >}})）。官方展示的企业用法多为夜间工作、早上交付：客户 Team Bot 每晚查看公司新闻、Gong 通话、Notion 和 Slack，每天早上在客户 Slack 频道发简报（[Team Bots]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})）。

打扰频率的控制主要靠提示词与用户约定，资料中没有官方的免打扰设置。官方示例提示要求无新内容时保持静默（[用 Grok Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-09-24-guide-grok-bot-for-work" >}})）。应用侧只提供按 Bot 开关通知，在其完成或等待用户时提醒（[文档：设置与通知]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-settings-and-notifications" >}})）。一位用户的 BotOps 做法是让 L3「节奏执行器」在太平洋时间 9:00 和 18:00 跑找房例程，大多数运行没有发现就保持沉默，有价值才逐级上报，规则是「没有发现，就不 ping」（[BotOps]({{< relref "/docs/grok-bot/sources/community/2026-09-06-granda-botops" >}})）。

多 Bot 协作也能延续工作：一个 Bot 可以发消息唤醒另一个 Bot 并稍后回复。文档建议每个阶段只设一个负责人，并行交接会产生重复工作；目前没有开关能禁止 Bot 互发消息，只能在聊天里告诉它们（[文档：使用 Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})、[帮助：群聊]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-group-chats" >}})）。

## 实测中的表现

- 周期简报与监控：有作者称 Grok Bot「确实可以经常 24 小时工作」，例如持续整理推文（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）；有用户报告 Bot 开始在 Slack 中替其分流产品问题和 bug，并自动为双周例会准备预读材料（[James Pember 实测]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})）。
- 跨来源核对：WIRED 的日程冲突测试中，Grok Bot 得 2/5，没有发现邮件提醒与日历之间的冲突，事后回复称「从现在起我会在检查日历的同时检查你的自我提醒邮件」（[WIRED 实测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。
- 事件响应：一篇社区综述（案头梳理，未实测）称 Grok Bot 是对比的六款中「唯一能即时响应 GitHub issue 的托管型智能体」（[主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})）。

以上是个人使用报告，不能代表普遍水平；资料中没有例程的成功率、失败率等量化数据。

## 资料缺口

- 例程的实际成功率、失败原因分布；「共享速率限制」已知问题的影响范围与修复时间。
- 各套餐的每周用量额度分别能支撑多少次例程运行。
- 数周以上的长期例程运行报告；自动更新重启对正在运行的任务有什么影响。
- 主 Bot 主动发现工作的触发条件、频率控制，以及用户能否关闭这一功能。

## 主要资料

**官方**

- [文档：技能、例程与自动化]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-skills-routines-and-automations" >}})：触发方式、数量与速率上限、测试与用量
- [帮助：例程]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-routines" >}})：触发器细节、webhook、速率限制已知问题
- [文档：使用 Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})：长期离开后暂停、停止、Bot 间交接
- [FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})：后台运行、批准约 30 分钟过期
- [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：主 Bot 主动性、上限调整、批准时长变化
- [文档：用例]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-use-cases" >}})：放权顺序与审核点
- [帮助：Bot 邮箱]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-agent-email" >}})：邮件例程
- [帮助：群聊]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-group-chats" >}})：Bot 互发消息与用量
- [设计 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-03-designing-grok-bot" >}})、[更多计划]({{< relref "/docs/grok-bot/sources/official/2026-08-26-grok-bot-more-plans" >}})、[Grok Bot 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})：例程在产品中的定位
- [IncidentSweep]({{< relref "/docs/grok-bot/sources/official/2026-10-20-incident-sweep" >}})、[Team Bots]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})、[Grok Bot 用于销售]({{< relref "/docs/grok-bot/sources/official/2026-10-27-grok-bot-sales" >}})、[用 Grok Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-09-24-guide-grok-bot-for-work" >}})：官方案例
- [文档：设置与通知]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-settings-and-notifications" >}})、[文档总览]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-overview" >}})：通知与后台运行

**媒体**

- [WIRED 实测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})：日程冲突测试

**社区**

- [BotOps]({{< relref "/docs/grok-bot/sources/community/2026-09-06-granda-botops" >}})、[James Pember 实测]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})、[鱼皮实测]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})：用户的例程用法
- [Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})：用量限制
- [四产品成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})：早期批准过期时长
- [Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})：社区评价
