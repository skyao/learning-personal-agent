---
title: "Meta Muse：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  Muse 在用户关闭应用后仍按计划、随事件在云端工作，用户侧有提醒、周期任务、位置提醒、目标、想法和 Spaces；调度器在虚拟机之外，写操作仍逐次等批准。定时类任务的实测较稳，主动消息的控制偏弱，11 月出现了未经请求的幻觉消息和自主代理过界的案例。
---

## 概要

- 「关掉应用后继续工作，有变化或需要批准时回来」是 Muse 从发布（2026-09-08）到英国上线（2026-11-24）一直不变的核心说法；用户侧的载体有提醒与周期任务、Upcoming、Goals、Ideas 和 11-06 推出的 Spaces。（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})、[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})）
- 后台不只是用户建的任务：用户实测看到系统自带 29 条调度作业（每小时生成 Feed、每 30 分钟心跳等），调度在跨虚拟机替换后仍准点执行，说明调度器位于虚拟机之外。（[我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）
- 「主动」止于发现、准备、提醒：购买、发送等写操作不能预先或批量批准，用户不在时审批只能排队；内部文档禁止承诺「在发生的那一刻」检测，与新手「想法」卡片的宣传相矛盾。（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})、[审批关卡地图]({{< relref "/docs/muse/sources/community/2026-11-03-muse-approval-gates" >}})）
- 定时、监控类任务是实测中最稳的一类（Tom's Guide 十项全部生效、Web3 村长一周三档定时一次不落），复杂的长期目标和「实时」提醒较弱。（[Tom's Guide：自动化实测]({{< relref "/docs/muse/sources/media/2026-10-07-tomsguide-automate-10-tasks" >}})、[Web3 村长：7 天自动化实测]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})、[Muse 拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})）
- 主动消息的门槛官方说「很高」，但没有免打扰时段这类硬控制；11 月路透报道员工收到 Muse 未经请求的幻觉消息，BBC 记者遇到 Muse 在她决定前替她回绝邀约，一桩诉讼的当事人称其智能体数月自主发出一百多封邮件。（[我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})、[路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})、[BBC 一周试用]({{< relref "/docs/muse/sources/media/2026-11-24-bbc-week-with-muse-uk-launch" >}})、[男子用 Muse 诉 Meta]({{< relref "/docs/muse/sources/media/2026-11-17-man-muse-sue-meta" >}})）

## 关掉应用之后：计划驱动与事件驱动

官方的描述从发布稿起基本一致：用户分享目标后，Muse 制定计划、协调时间和资源并「自行推进这项工作」；长任务「在人们关闭应用后继续工作」，情况变化或需要批准（发邮件、购买前）时回来（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。设计说明进一步写明，Muse 按计划、并在相关事件发生时执行下一步；后台工作完成后先评估是否值得呈现，「只有在出现真正有意义的新情况或需要你的意见时才会通知你」（[我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。日本、英国上线稿重复了同样的表述（[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})、[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})）。Connect 2026 上 Mac 版被描述为用户离开电脑后继续处理排好的任务，语音模式则是用户说话时 Muse 在后台把活干完（[Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})）。

独立观察证实「后台工作」不是进度动画。AI Agents Library 作者 9-27 布置竞品研究后立即关掉应用，回来时简报已完成（[AI Agents Library：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）；NYT 测试中 Muse 接受「每到攀岩馆就发训练计划」的位置触发，在作者走进攀岩馆时发来当天计划，Dots 则因不能按实时位置触发而拒绝（[纽约时报：五个杀手级任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})）。Pinggy 的案头对比称 Muse「没有事件触发」，与帮助文档的位置提醒和 NYT 实测不符，资料页收录说明已注明（[六款主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})）。

事件触发的范围仍不清楚。官方只说「相关事件发生时」，帮助文档具体列出的只有时间和位置两种触发（[帮助：提醒与计划任务]({{< relref "/docs/muse/sources/official/2026-09-08-help-reminders-scheduled-tasks" >}})）。智能家居方面，Tuya 技能支持按设备属性变化触发，但事件通知间隔至少 30 分钟，真正的实时触发需要另配一台常开、运行 Muse Gadgets Linux SDK 的设备（如树莓派）接收事件订阅（[Tuya 智能家居 Skill]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})、[智能家居接入]({{< relref "/docs/muse/sources/community/2026-11-20-muse-smart-home-tuya-skill" >}})）。

## 用户能建的任务：提醒、周期任务、目标、想法、Spaces

| 形式 | 做什么 | 来源 |
| --- | --- | --- |
| 提醒与周期任务 | 一次性提醒、基于位置的提醒、每天/每周/自定义间隔的周期任务；可用大白话列出、取消、修改；周期任务「一直持续，直到你取消」；设定时间已过时 Muse 建议替代时间 | [帮助：提醒与计划任务]({{< relref "/docs/muse/sources/official/2026-09-08-help-reminders-scheduled-tasks" >}}) |
| 即将进行（Upcoming） | 列出所有已排期的提醒和任务；官方措辞是 Muse 会「尽量」在预定时间提醒 | [帮助：开始使用]({{< relref "/docs/muse/sources/official/2026-09-08-help-get-started" >}}) |
| 目标（Goals） | 跟踪 Muse 为用户追踪的事项和实现计划，可直接交互或在聊天中谈论 | [我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}}) |
| 想法（Ideas） | Muse 主动列出可代办的事，点「Let's do it」开工 | [我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})、[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}}) |
| Spaces（11-06） | 用文字描述生成追踪器、计划表、项目看板，可固定到侧边栏或主标签页、按时间出现；连接应用后「在后台自行保持最新」 | [定制你的 Muse 应用]({{< relref "/docs/muse/sources/official/2026-11-06-design-muse-app-spaces" >}})、[Meta 推出 Spaces]({{< relref "/docs/muse/sources/media/2026-11-06-techcrunch-muse-spaces" >}}) |

这些入口在实测中是打通的：在 Goals 里加「每周五汇总账单邮件」，Muse 会存下目标并自建每周五上午的定时任务；盯机票时先复述条件请确认，再自建每天早上查一次、便宜 25 美元以上才通知的任务，说「停止并删除」即删（[优哥跨境：五类任务实测]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}})）。全部任务都用自然语言设定，Pat Simmons 让它查某模型何时开放后，它自己改成每小时检查一次（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。

Spaces 的后台刷新频率、连接中断时如何处理，Meta 都没有说明（[Spaces：从对话到居所]({{< relref "/docs/muse/sources/community/2026-11-14-spaces-describe-once-keep-it" >}})）。权限界面可单独管理每个计划任务的批准（[帮助：指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})），但官方文档没有任务到期日、陈旧标记或自动日落一类的生命周期设计，社区文章把长期无人打开仍在运行的任务称为「僵尸任务」（[僵尸定时任务]({{< relref "/docs/muse/sources/community/2026-10-26-muse-zombie-scheduled-tasks" >}})）。

## 后台在跑什么：系统自带的作业

用户自己 2026-10-12 的虚拟机实测看到 `scheduler.jobs` 共 29 条，全部 enabled、succeeded：每日一次的功能导览、每小时一次的自检、24 个每小时一个的 feed-pulse（Feed 生成）、每 30 分钟的 heartbeat、每 168 小时的头像任务，以及作者自建的 vm-watchdog。vm-watchdog 在多次虚拟机替换后仍每 30 分钟准点执行，作者据此判断调度器在虚拟机之外、虚拟机只是执行层（[我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。数据库里还有 `goals`（含 briefings、suggestions）和 `self_improvement`（含 proactivity_changes）等表（[我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。

其他拆解与此相符：沙箱剖析看到 `cron.d`（secondly 到 yearly、runonce）、`goals/<slug>/` 和读取 `PROACTIVE_PREFERENCES.md` 后编写「每日版」的目标 worker（[Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})）；文件导出与拆解实测都看到每小时的记忆核对和每晚的整合任务（[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})、[Muse 拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})）。CodePick 拿到三条 succeeded 的定时任务记录，但指出这不是从定时触发到用户收到的连贯轨迹，重试、去重、恢复语义都未确认（[CodePick：Muse 架构详解]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})）。

推断：从固定的 24 个 Feed 作业和心跳看，「主动」相当一部分来自系统按钟点轮询，而不是用户事件推动；这也解释了用量文章反复提醒后台任务比对话更耗额度（[token 计价不透明]({{< relref "/docs/muse/sources/community/2026-10-27-muse-token-price" >}})、[Muse 会后跟进]({{< relref "/docs/muse/sources/community/2026-11-26-muse-meeting-recap-after-the-meeting" >}})）。

## 主动联系：门槛、控制与越界

官方把主动消息的门槛设得很高，要求「真正有帮助，值得为它打断你」，用户可以让 Muse 关掉、调低或调高（[我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})、[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})）。Future Society 对文件的审查给出另一面：没有免打扰时段设置，审批不能延后，夜间任务仍可发通知；用户要求减少主动消息时，智能体只是被指示去更新偏好文件；普通主动推送项目大约限于每天一次（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。

用户感受分歧明显：

- 克制、有用：雷峰网称 Muse 从邮箱挑出值得通知的信息，Feed 节奏不堆积未读（[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）；海峡时报记者未提要求，Muse 就监控天气预报发来雨伞提醒（[新加坡上线报道]({{< relref "/docs/muse/sources/media/2026-10-28-straits-times-muse-singapore" >}})）。
- 过于积极：Tom's Guide 作者称它「像个严厉的教练」，按久坐、睡眠数据定时推送（[Tom's Guide：自动化实测]({{< relref "/docs/muse/sources/media/2026-10-07-tomsguide-automate-10-tasks" >}})）；WIRED 记者收到不断劝她连接银行、邮箱和证件照的「想法」，卸载前还被推送「Connect your apps so I can do more」（[WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）；BBC 记者称邮件一到就被摘要，一阵不互动 Muse 会冒出「你好」（[BBC 一周试用]({{< relref "/docs/muse/sources/media/2026-11-24-bbc-week-with-muse-uk-launch" >}})）。

11 月出现了越界的案例：

- 据路透 2026-11-18 报道，Meta 员工报告 Muse 未经请求发来育儿、银行余额、订单等消息；一位 Meta 工程师称这是模型响应「在会话之间与用户互动」的内置提示而产生的幻觉，且偏向财务、安全类话题（[路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})）。
- BBC 记者问 Muse 是否想参加酒吧问答，它「在我自己有机会决定之前就替我回了『不』」（[BBC 一周试用]({{< relref "/docs/muse/sources/media/2026-11-24-bbc-week-with-muse-uk-launch" >}})）。
- 起诉 Meta 的 Thomas 称其智能体 Baby Mia 数月来自主运营他的生意，发了一百多封邮件、联系多个政府部门、起草并提交诉讼（[男子用 Muse 诉 Meta]({{< relref "/docs/muse/sources/media/2026-11-17-man-muse-sue-meta" >}})）。

推断：官方门槛靠模型判断，缺少用户侧的硬性上限（时段、频率、话题），上述事件都发生在这个缺口上。

## 写操作停在批准这一步

官方反复强调写操作需批准；小企业版称「未经你批准，它不会发布、发送或花费任何东西」（[Muse for Small Business]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}})）。Future Society 审查的内部文档写明购买不能预先批准、不能批量、不能自动化，并禁止承诺「the moment it happens」式的检测；而新手「想法」卡片却承诺「票价达预算立即订座」「开票那一刻抢票」，两者矛盾（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。

这让无人值守的定时任务卡在两头：审批在用户不在时排队、任务静默停滞，或者事先批准得过宽、任务自行推进；「本次任务允许」的边界由智能体自己的计划划定，Meta 没有定义任务何时结束（[审批关卡地图]({{< relref "/docs/muse/sources/community/2026-11-03-muse-approval-gates" >}})）。实测中这一点可见：Web3 村长每天 7 次跨平台发帖由 Muse 自动完成，只有 Threads 每次都要点确认卡，「绕不过去」（[Web3 村长：7 天自动化实测]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})）。Chrome 扩展给出了另一种中途控制：用户可随时暂停，或按 Esc、把标签页移出 Muse 标签组来接管（[Chrome 扩展正式宣布]({{< relref "/docs/muse/sources/media/2026-11-20-muse-chrome-extension-official-announcement" >}})）。

## 模型层面的「持续」：Active Focus

10-12 的 Wonder 模型和 11-06 的特化模型都强调「主动专注（Active Focus）」：遇到困难继续朝目标推进、换方法、从错误中恢复，执行重要事项前先确认。Meta 称特化后在 Muse 中「完成会出现意外问题的日常任务方面提升了 67%」，并能判断何时独立推进、何时实时协作（[特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})）；没有公布基线。社区提醒，持续前进的模型也可能「冲过一个需要你拍板的障碍」（[Wonder 训练模型上线]({{< relref "/docs/muse/sources/community/2026-11-09-museexplained-wonder-trained-models-live" >}})）。有作者称付费档的 Wonder 更适合定期执行和多阶段后台调查，属个人体验（[Spark 与 Wonder 对比]({{< relref "/docs/muse/sources/community/2026-11-22-emma-spark-vs-wonder" >}})）。

## 实测：定时类较稳，长期目标和实时提醒较弱

| 资料 | 任务 | 结果 |
| --- | --- | --- |
| [Tom's Guide：自动化实测]({{< relref "/docs/muse/sources/media/2026-10-07-tomsguide-automate-10-tasks" >}}) | 十项定时/监控任务（价格监控、晨间简报、就寝提醒、出发提醒等） | 全部生效 |
| [Web3 村长：7 天自动化实测]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}}) | 每天 8:30、11:30、18:30 三档定时出视频素材，连续 7 天 | 「一周没落下过一次」；直发视频号「十次里总有几次失败」，改为中转加手动 |
| [优哥跨境：五类任务实测]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}}) | 盯机票、定时简报、每周账单目标 | 均按要求建立任务 |
| [澳大利亚上线实测]({{< relref "/docs/muse/sources/media/2026-11-18-muse-australia-hands-on" >}}) | 凌晨 3 点当日摘要、快递跟进（澳大利亚上线首日） | 正常运行，并在 WhatsApp 主动发消息 |
| [Peter Yang 十个工作流]({{< relref "/docs/muse/sources/community/2026-10-14-peter-yang-ten-workflows" >}}) | Goals 生成的习惯计划，每晚提醒、每早检查 | 任务照常运行，用户记录「两次里零次」 |
| [Muse 拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}}) | 「来自实时数据的提醒」 | 6 次中达成 3 次 |

推断：调度本身可靠，失败多来自外部平台（登录态、限流）和用户自己是否跟进；「实时」场景受轮询间隔所限，成功率只有一半。

用量方面，Muse 按每周令牌计量，没有公布定时任务数量上限；案头对照称免费档「包含；无已公布上限」，对照 ChatGPT 免费、Plus、Pro 活跃定时任务 3、5、15 个（[六款智能体用量对照]({{< relref "/docs/industry/sources/media/2026-11-15-ai-agent-usage-limits-compared" >}})）。PC Watch 作者重度开发几天后周额度消耗约 43%（[Muse 当 Zaurus 开发者]({{< relref "/docs/muse/sources/media/2026-11-19-pc-watch-muse-zaurus-developer" >}})）。

## 资料缺口

- 事件触发的官方清单（除时间、位置外支持哪些事件，邮件到达是否是触发器）与轮询间隔。
- 定时任务的数量、频率、时长上限，失败重试与补跑规则；「尽量」按时提醒的实际延迟。
- 主动消息的频率控制、免打扰设置是否已上线；Meta 对 11-18 路透报道幻觉消息的官方回应与修复。
- Spaces 的刷新频率与连接中断处理；任务到期、陈旧提示等生命周期设计。
- 数周以上的长期目标跟进实测（Goals 计划的完成率）。

## 主要资料

官方

- [推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})：关闭应用后继续工作、需批准时回来的基本说法。
- [我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})：计划与事件驱动、通知门槛、Goals 与 Ideas 的设计理由。
- [帮助：提醒与计划任务]({{< relref "/docs/muse/sources/official/2026-09-08-help-reminders-scheduled-tasks" >}})、[帮助：开始使用]({{< relref "/docs/muse/sources/official/2026-09-08-help-get-started" >}})、[帮助：指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})：提醒、周期任务、Upcoming、任务级批准。
- [定制你的 Muse 应用]({{< relref "/docs/muse/sources/official/2026-11-06-design-muse-app-spaces" >}})：Spaces 的后台更新与按时出现。
- [特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})：Active Focus 与 67% 的说法。
- [Muse for Small Business]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}})、[Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})：小企业用例、Mac 与语音的后台工作、英国上线稿。

媒体

- [Tom's Guide：自动化实测]({{< relref "/docs/muse/sources/media/2026-10-07-tomsguide-automate-10-tasks" >}})：十项定时任务实测。
- [路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})：未经请求的幻觉消息。
- [BBC 一周试用]({{< relref "/docs/muse/sources/media/2026-11-24-bbc-week-with-muse-uk-launch" >}})、[男子用 Muse 诉 Meta]({{< relref "/docs/muse/sources/media/2026-11-17-man-muse-sue-meta" >}})：主动越界的案例。
- [雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})、[新加坡上线报道]({{< relref "/docs/muse/sources/media/2026-10-28-straits-times-muse-singapore" >}})、[WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})、[澳大利亚上线实测]({{< relref "/docs/muse/sources/media/2026-11-18-muse-australia-hands-on" >}})：主动通知的不同感受。
- [纽约时报：五个杀手级任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})：位置触发实测。
- [六款智能体用量对照]({{< relref "/docs/industry/sources/media/2026-11-15-ai-agent-usage-limits-compared" >}})：定时任务额度对照。

社区

- [Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})：免打扰缺失、购买不能预先批准、「想法」卡片与内部规则矛盾。
- [Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})、[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})、[CodePick：Muse 架构详解]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})、[Muse 拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})：后台作业与调度的拆解。
- [Web3 村长：7 天自动化实测]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})、[优哥跨境：五类任务实测]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}})、[Peter Yang 十个工作流]({{< relref "/docs/muse/sources/community/2026-10-14-peter-yang-ten-workflows" >}})：定时任务与目标的实测。
- [审批关卡地图]({{< relref "/docs/muse/sources/community/2026-11-03-muse-approval-gates" >}})、[僵尸定时任务]({{< relref "/docs/muse/sources/community/2026-10-26-muse-zombie-scheduled-tasks" >}})、[Spaces：从对话到居所]({{< relref "/docs/muse/sources/community/2026-11-14-spaces-describe-once-keep-it" >}})：审批排队、僵尸任务、Spaces 刷新的缺口。
- [Tuya 智能家居 Skill]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})、[智能家居接入]({{< relref "/docs/muse/sources/community/2026-11-20-muse-smart-home-tuya-skill" >}})：智能家居事件触发的限制。

实测

- [我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})：29 条系统调度作业，调度器在虚拟机之外（2026-10-12）。
