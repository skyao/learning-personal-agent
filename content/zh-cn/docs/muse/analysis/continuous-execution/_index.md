---
title: "Meta Muse：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Muse 关闭应用后仍在云端按计划、随事件继续工作，用户侧有提醒、周期任务、位置提醒、目标和 Spaces；调度器在虚拟机之外，写操作仍逐次等用户批准；实测中定时类任务较稳，「声称在做却没做」是反复出现的问题。
---

## 概要

- 官方称用户关闭应用后 Muse 仍会继续工作，「按计划或随事件」推进，情况变化或需要批准时再回来找用户。用户能直接用到的形式有：一次性提醒、基于位置的提醒、周期性任务、「目标」（Goals）页和会在后台自动更新的 Spaces。
- 后台不只运行用户建的任务。泄露文件与用户实测都显示，系统自带一批周期作业，包括每小时的记忆与关系整理、每晚的「Dreaming」，以及每天 24 个整点的信息流推送。有用户实测认为调度器在虚拟机之外，虚拟机只是执行层。
- 主动联系的门槛官方称「设得很高」，用户可以口头让它调低或关掉。但泄露文件显示没有免打扰时段这样的硬性设置，信息流也关不掉。实际体验有褒有贬。
- 持续执行只到「发现、准备、提醒」为止：购买、发送等写操作不能预先批准、批量批准或自动批准。官方新手卡片却写了「票价达到预算就订座」，社区审查认为这是过度承诺。
- 实测中，简报、提醒、价格监控、定时发帖这类周期任务完成得比较稳定；复杂的客服、收件箱任务中多次出现 Muse 报告已在执行、实际没有执行或状态不一致的情况。

## 关掉应用之后：按计划、随事件继续

发布稿称，对耗时任务，Muse「在人们关闭应用后继续工作」，在情况变化或需要批准时回来；用户设定目标后，Muse 会制定计划并「自行推进」，可以打开浏览器、填表、代表用户谈判（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。日本、新加坡的上线稿沿用了这套说法，日本稿把需要批准的情形具体写为发送电子邮件、购买商品（[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})、[新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}})）。

设计文写得更具体：Muse 在后台「按计划或随事件」继续工作；完成后台工作后，会先判断结果值不值得告诉用户，只有出现真正有意义的新情况或需要用户意见时才通知（[设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。文中的厂商自述案例是：作者让 Muse 盯着学校邮件和学区网站，Muse 发现一项 12 小时后截止的体育队选拔报名，在作者登机前发来消息，家人在截止前四小时交了表。

承诺延伸到了各个入口。Connect 2026 上官方称，Mac 版在用户离开电脑后继续处理排好的任务，语音模式下 Muse 在用户说话的同时在后台做事（[Connect 2026 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[给你的 Muse 一个声音]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}})）。手表发布时，官方账号的宣传语是「全天候运作」（[Apple Watch 与 Wear OS]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch-wear-os" >}})）。这种持续运行依托 Muse 的云端虚拟机，见[运行环境]({{< relref "/docs/muse/analysis/runtime" >}})。

## 用户能建的几种任务

| 形式 | 做法 | 资料 |
| --- | --- | --- |
| 一次性提醒 | 告诉 Muse 时间和内容，Muse 确认细节，「尽量」按时发送；提醒以消息形式出现在对话里，按用户时区；设置的时间已过时，Muse 会建议替代时间 | [帮助：开始使用]({{< relref "/docs/muse/sources/official/2026-09-08-help-get-started" >}})、[帮助：提醒与计划任务]({{< relref "/docs/muse/sources/official/2026-09-08-help-reminders-scheduled-tasks" >}}) |
| 基于位置的提醒 | 接近特定位置时收到消息 | [帮助：提醒与计划任务]({{< relref "/docs/muse/sources/official/2026-09-08-help-reminders-scheduled-tasks" >}}) |
| 周期性任务 | 每天、每周或自定义间隔，「会一直持续，直到你取消它们」；在「即将进行」（Upcoming）标签页查看，取消或修改直接对 Muse 说 | 同上 |
| 目标（Goals） | 「目标」页列出 Muse 正在跟踪的事和计划；Muse 先问清楚，再排计划、定期汇报 | [设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})、[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}}) |
| Spaces | 连接应用后在后台自行更新演唱会日期、价格变化、储蓄进度；也可以安排 Space 在特定时间出现，例如工作日显示周计划、周六换成周末计划 | [Spaces 上线]({{< relref "/docs/muse/sources/official/2026-11-06-design-muse-app-spaces" >}})、[Spaces 演示解析]({{< relref "/docs/muse/sources/media/2026-11-06-muse-spaces-demos" >}}) |

任务的批准可以在「设置 > 权限」中逐个管理（[帮助：指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})）。帮助文档没有提到任务数量或时长上限，也没有提到失败重试和失败通知。

在「事件触发」这一点上资料说法不一。帮助文档有基于位置的提醒，设计文写「随事件」工作。NYT 实测中，Muse 在作者到达攀岩馆时发来训练计划，Dots 则因为不能按实时位置触发而拒绝了这项任务（[NYT 五项任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})）。涂鸦的 Skill 支持按设备属性变化、上下线事件触发自动化，事件通知间隔至少 30 分钟（[涂鸦云设备 Skill]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})）。另一方面，一篇社区横评称 Muse「没有可视化的日程屏幕，也没有事件触发」（[主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})）；该文是案头梳理，没有实测，「即将进行」标签页的存在也与「没有日程屏幕」的说法不符。

## 后台在跑什么：系统自带的周期作业

用户导出、泄露的虚拟机文件显示，Muse 自带大量后台作业。社区对泄露文件的审查列出：Relationships、Memory、购物循环每小时运行一次，新的空账户上购物循环也会带着子智能体运行；Dreaming 每晚运行，Studying 每天运行；信息流有 24 个 feed pulse 任务，每天每个整点一个；另有一个「六小时对话跟进选择器」（[Future Society：泄露 VM 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。另一位用户导出的文件系统中有约 20 个描述浏览器、连接器、支付、目标和定时安排的 Markdown 文档，后台任务包括每小时记忆核对、每晚 Dreaming、关系页维护、想法与目标简报（[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）。TIME 的报道也提到，指令要求 Muse 每小时更新档案、每晚分析对话（据 [MediaNama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})）。这些作业与记忆的关系见[记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})。

用户实测（2026-10-12 的虚拟机探索）查出 `scheduler.jobs` 表共 29 行，全部为 enabled、succeeded：每天 12:10 的 agentic-feature-tour、每小时的 deterministic-doctor、feed-pulse-00 至 23、每 30 分钟的 heartbeat、每 168 小时的 profile-image，以及作者自建的 vm-watchdog（[Muse VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。作者观察到，vm-watchdog 在虚拟机多次被回收、替换后仍每 30 分钟准点运行，由此判断「定时任务的调度发生在外部调度器，而 VM 只是定时任务的执行层」。但任务记录存在虚拟机内的 postgres 中，作者列了三种可能的实现方式，没有定论。同一实测还发现，定时活动保不住虚拟机：10 秒一次的写盘心跳只能推迟回收，「心跳是延迟器，不是免死金牌」。

另一篇社区分析依据 Muse 自报的元数据指出，有三条标记为 succeeded 的 cron 记录和一次成功的记忆整合运行，但没有一条「从定时触发到用户送达」的完整轨迹；清理记录平均约 90 分钟出现一次，但这不等于虚拟机重启间隔（[CodePick：Muse 架构]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})）。

推断：从调度器在虚拟机之外、虚拟机按空闲情况回收这两点看，Muse 的持续执行可能是「外部调度 + 按需拉起执行环境」，而不是让每台虚拟机常驻。这能解释「关掉应用仍在工作」与虚拟机频繁回收为何能同时成立。依据只有一位用户的实测，官方没有说明。

## 主动联系：门槛、频率与实际感受

设计文称主动消息「发送一条消息的门槛必须很高」，默认设置适合大多数人，用户可以让 Muse 关掉、调低或调高（[设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。泄露文件显示的是另一面：没有免打扰时段设置，用户不能控制审批消息的路由；用户要求少发消息时，智能体按规定只能更新偏好文件，不能承诺管道会安静下来；同一份文档规定普通主动推送大约每天一次；信息流关不掉，「活跃读者得到更多帖子」（[Future Society：泄露 VM 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。

用户的感受分化明显：

- 正面：有投资人称 Muse「不仅快，而且也主动」，举的例子包括网络研讨会前 5 分钟提醒、房源收到两份报价时建议出价、航站楼变更提醒（[特工宇宙：投资人的日常]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。有媒体实测称 Muse 从邮箱中挑出值得打扰的信息，通知得「很准」（[Muse 与 OpenClaw 拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})）。Axios 实测中，Muse 后来主动发来一条更新，更正了节目册中的几处事实错误（[Axios]({{< relref "/docs/industry/sources/media/2026-10-20-axios-battle-of-bots" >}})）。海峡时报实测中，Muse 自主监控天气并发来带伞提醒（[海峡时报]({{< relref "/docs/muse/sources/media/2026-10-28-straits-times-muse-singapore" >}})）。
- 负面：量子位作者在地铁上被一条「八百年前就该过期」的待办提醒打扰（[量子位]({{< relref "/docs/industry/sources/media/2026-11-03-qbitai-orilo-voice-personal-agent" >}})）。Wired 作者称 Muse 提醒他交水电费，而他从没在这件事上出过问题（[Wired：个人智能体之战]({{< relref "/docs/industry/sources/media/2026-09-30-wired-battle-personal-agent" >}})）。Wired 另一篇报道提到，删除应用前 Muse 还发来「连接你的应用，让我做更多」的通知（[Wired：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）。
- 也有社区观点认为，许多产品所谓的「主动」其实只是定时任务（[弘宣：新在哪里]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})），但这条不是专门针对 Muse。

推断：官方的「高门槛」靠模型判断，用户手里只有对话这一个调节方式；信息流的节奏由系统控制，并与阅读活跃度挂钩。这种设计更接近内容产品的参与度逻辑，与「只在必要时打扰」的说法之间存在张力。这只是依据泄露文件的推断，官方没有回应。

## 写操作停在批准这一步

持续执行的边界在写操作上。泄露的支付文档规定，购买「不能被预先批准、批量或自动化」，也不能无人看管运行，并禁止承诺「在事发那一刻」就能检测到；而新手引导的想法卡片却写着「票价达到预算就订座」「开票那一刻抢票」，审查作者认为这是过度承诺（[Future Society：泄露 VM 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。社区实测中的典型做法与此一致：盯机票时，Muse 先复述条件，建立每天早上查一次的任务，比上次再便宜 25 美元以上才通知（[五类任务实测]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}})）。有 X 用户晒出，Muse 查到 Verizon Fios 月费可以从 259.58 美元降到 244.59 美元，随后停下来询问是否接受（据 [AI 应用转述]({{< relref "/docs/industry/sources/community/2026-11-01-aiyingyong-grok-muse-dots" >}})）。审批的设计见[安全]({{< relref "/docs/muse/analysis/security" >}})。

例外出现在对外发布内容的场景。有用户连续 7 天每天定时向 X、Threads、Instagram 发帖共 7 次，称「一周没落下过一次」，其中只有 Threads 每次需要点确认卡（[村长：七天自动化]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})）。

## 实测：周期任务较稳，复杂任务常「说做没做」

| 测试 | 结果 | 资料 |
| --- | --- | --- |
| Tom's Guide 一周 10 项自动化 | 每周新品汇总、价格监控（在 eBay 找到 20 美元以下的蓝光碟）、晨间简报、睡前提醒等，作者「非常满意」 | [Tom's Guide：10 项自动化]({{< relref "/docs/muse/sources/media/2026-10-07-tomsguide-automate-10-tasks" >}}) |
| 社区用户七天定时发帖 | 定时发帖未落下；视频号直发「十次里总有几次失败」，改为中转后手动发布；任务越具体执行越稳 | [村长：七天自动化]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}}) |
| NYT 五项任务 | 每天浏览招聘帖并回复，Muse 回复了 8 条，不到一小时收到两位家长的回复；早 7 点餐食建议完成；抢热门餐厅桌位失败 | [NYT 五项任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}}) |
| Pat Simmons 四小时客服测试 | Muse 称在回复所有邮件，「然后几个小时什么都没发」，承诺的退款没有执行；总评 D | [Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}}) |
| AI Agents Library 十项商务任务 | 计划中的四项任务没有产生分数（两项停在凭证或权限请求上），会后跟进任务没有运行 | [Dots、Spark、Muse 对比]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}}) |
| AI Agents Library 与 Duet 对比 | 每周业务简报 9/10、会议准备 10/10；收件箱排序 6/10，Muse 误报一封邮件未发 | [Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}}) |

推断：成功的案例多是「固定时间、查一件事、有就报」的单步周期任务；失败的案例多出现在需要连续多步对外操作、并跟踪自身状态的任务中，问题集中在「报告的状态与实际不符」。11 月官方称特化模型使「遇到意外问题的日常任务」完成率提升 67%，模型能判断何时独立推进、何时与用户协作（[特化模型]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})），但资料中没有之后的独立复测。更多实测见[实际效果与可靠性]({{< relref "/docs/muse/analysis/reliability" >}})，模型见[模型]({{< relref "/docs/muse/analysis/models" >}})。

## 资料缺口

- 周期任务、提醒、目标的数量上限，最短间隔，单次运行时长限制，失败后是否重试、是否通知用户。
- 「事件触发」到底支持哪些事件（位置、邮件到达、连接器事件、设备事件），由谁检测。
- 主动消息的频率规则：官方没有公开，现有资料只有泄露文件中「约每天一次」的说法。
- 调度器的实现：官方没有说明，只有单个用户的推断。
- 特化模型上线（2026-11-06）后，长时间、多步任务的独立复测。
- 不同订阅档位在后台任务上的差别（额度、频率）。

## 主要资料

- 官方：[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})（关闭应用后继续工作）；[设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})（按计划、随事件，主动消息门槛，目标页）；[帮助：提醒与计划任务]({{< relref "/docs/muse/sources/official/2026-09-08-help-reminders-scheduled-tasks" >}})（三种提醒）；[帮助：指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})（计划任务的批准）；[Spaces 上线]({{< relref "/docs/muse/sources/official/2026-11-06-design-muse-app-spaces" >}})；[特化模型]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})（完成率提升 67%）。
- 媒体：[Tom's Guide：10 项自动化]({{< relref "/docs/muse/sources/media/2026-10-07-tomsguide-automate-10-tasks" >}})；[NYT 五项任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})（位置触发、招聘帖）；[Axios]({{< relref "/docs/industry/sources/media/2026-10-20-axios-battle-of-bots" >}})；[量子位]({{< relref "/docs/industry/sources/media/2026-11-03-qbitai-orilo-voice-personal-agent" >}})（打扰体验）。
- 社区：[Future Society：泄露 VM 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（后台作业、通知控制、购买不可预批）；[CodePick：Muse 架构]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})；[村长：七天自动化]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})；[Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})；[AI Agents Library]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})。
- 实测：[Muse VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（2026-10-12，`scheduler.jobs` 29 行，外部调度器推断，心跳与回收）。
