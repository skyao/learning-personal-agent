---
title: "Claude Duet：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  截至 2026-11-12 只有六七份针对 Claude Duet 的实测，多为发布后一两周的早期体验；评价一致的是界面好、晨报与会议准备好、读和起草强，问题集中在动作推进弱、跟进安静、速度慢、上下文不足时编造。
---

## 概要

- 实测资料少且早：WIRED 在发布约一天后测试；Claire Vo、Alarcon、fig.blue、Aakash、aiagentslibrary 的体验都在 10-26 至 10-31；ChatPRD 九项任务是唯一的多产品同题横评。没有官方完成率、错误率或可用性数据。
- 做得好的：界面（WIRED「最佳界面」）；晨报与会议准备（aiagentslibrary 10/10，Aakash 称明显优于其他个人智能体）；发现问题（日程冲突、坏掉的报名页）；编程类任务（ChatPRD 的修 bug、发布视频）。
- 做得差的：推进和跟进（交出去的任务没下文）；个人杂事和购物（官方自己承认订票较弱，买鞋任务选错颜色、碰到封锁）；速度（线程常要 10 分钟以上）；上下文稀薄时以用户口吻编造。
- 总排名多在中游：WIRED「大多数测试中得分处于中游」；ChatPRD 报告 Grok 93%、Duet 79%；Alarcon 排第三，Aakash 和 Claire Vo 都没有把它当作主力。唯一明确的正面个例是 fig.blue，称它已在取代自己大部分 AI 工作流。
- 官方的自我评价是：可能误读对话、误判紧急程度，围绕工作构建，个人事务较弱。

## 实测清单

| 资料 | 时间与条件 | 主要结论 |
| --- | --- | --- |
| [WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})（媒体一手） | 发布约一天后，iPhone，同日测六款 | 午餐订购 3/5、日程冲突 4/5、旅行规划 3/5、开放式检查 2/5、新闻选题 4/5；「大多数测试中得分处于中游」；评为最佳界面 |
| [Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}}) | TestFlight 早期版本，无桌面端 | 界面出众；收件箱与 Slack 分诊「还行，而非出色」；买球票没下文；线程常要 10 分钟以上；不是首选 |
| [ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}}) | 四个智能体同题九项，由 Claude Computer Use 和 Codex 操作，Claude 评分 | 修 Sentry bug 与 Dots 并列最好，发布视频最好；剪视频失败（拒绝下载）、买鞋选错；Grok 93%、Duet 79%，作者称无透明评分公式 |
| [aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}}) | 10-27 至 10-28，Max 5x | 每周业务简报、会议准备 10/10，收件箱分诊 9.3/10；与 Muse 测试的日期和输入不同，不是受控对比 |
| [Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}}) | 10-29 第一天，Max | 整理保险跟进清楚但没有推进，碰到本机访问的墙；「不算差，但也算不上好」，排在 Grok Bot、Dots 之后 |
| [fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}}) | 早期使用，未注明时长 | 响应快、回复简短；「第一个让我觉得有用多于繁琐的」；有线程运行中不可见、仓库访问挂接失败等故障 |
| [Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}}) | 约一周，通过人脉提前拿到 | 会议准备、晨报优于同类；发现坏掉的网络研讨会页面；以作者口吻编造；Claude 之外基本做不了事；Instinct 仍是首选 |

Claire Vo 在 Lenny's Newsletter 的四智能体节目只收到任务清单和时间轴，没有 Duet 的结果（[Claire Vo：四个智能体]({{< relref "/docs/industry/sources/community/2026-10-28-claire-vo-four-agents" >}})）。LaoZhang AI 11-02 时称还没有关于 Duet 的独立同任务测试（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})），这一说法之后已被 ChatPRD 等资料超过。

## 读、起草与发现问题较强

- 晨报与会议准备：aiagentslibrary 给每周业务简报和会议准备都打了 10/10，收件箱分诊时 Duet 告诉作者一箱自动化邮件无需回复，并问是否连接了正确的 Gmail 账户（[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。Aakash 称 Duet 的会议准备「比其他个人智能体好得多」，晨报告诉他该跳过什么（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。
- 发现问题：Aakash 的例子中，Duet 先于他发现网络研讨会报名页无人能注册，因为该场次从未在 WebinarJam 中创建；它还标出六条最糟的已排期帖子（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。WIRED 的日程冲突测试中，只有 Dots 和 Duet 主动发现了冲突（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。
- 编程与制作：ChatPRD 称 Duet 修 Sentry bug 时找到第二个 bug，并认出 Dots 已修复原问题、不重复提交；发布视频抓住了价值主张、用了品牌，还请求 ElevenLabs MCP 配音，是四个中最好的（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。

## 推进、跟进与个人杂事较弱

- 推进：Aakash 称 Duet「主要在阅读和起草回复方面帮助了我，而在采取行动方面很吃力」（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）；Alarcon 第一天的保险跟进只做了总结（[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})）。
- 跟进：Claire Vo 的球票任务交出后没有再被提起，最终没有买成（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})，详见[持续执行]({{< relref "/docs/claude-duet/analysis/continuous-execution" >}})）。
- 个人杂事与购物：官方称核心功能围绕工作构建，「个人事务（例如订票）没有那么强」（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。ChatPRD 的买鞋任务中 Duet 反复遇到被封锁的购物网站，搜的是带红条纹的白鞋而不是带白条纹的红鞋，还找到了最贵的选项（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。WIRED 的午餐订购只得 3/5，Duet 选了 Freshroll，WIRED 认为另一家 DragonEats 更好吃也更便宜（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。
- 拒绝或卡住：ChatPRD 的剪视频任务中 Duet 不肯下载视频，在编辑开始前就失败（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）；施言转述的 Reddit 案例里，每日岗位推荐中有三个岗位不存在，投递卡在 Cloudflare 验证码（[施言：十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})，二手，无原帖链接）。
- 编造：Aakash 称用他的口吻写草稿时，Duet 声称了他从未说过的事，每份草稿都要逐行检查；上下文稀薄时编造，上下文丰富时追问（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。
- 速度：Claire Vo 称多个线程常要 10 分钟以上（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})）；ChatPRD 称 Duet「很慢」（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。

## 怎么读这些评测

ChatPRD 的作者提醒，这是对她自己配置的实际比较，不是受控评估：Muse 没接 Slack 和 GitHub，Duet 做家庭报纸时只有工作日历，「表面上智能的差异实际上可能是访问权限的差异」（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。aiagentslibrary 也声明 Duet 与 Muse 的测试日期和输入不同（[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。Claire Vo 称「我的体验是一个快照」（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})）。

推断：现有评测的分歧主要来自用户已有的 Claude 上下文多少，以及任务落在 Claude 连接器之内还是之外。上下文丰富、任务在 Gmail、日历、Slack、GitHub 之内的评测者（aiagentslibrary、Aakash 的会议准备、fig.blue）评价高；需要外部网站、购物、本机文件的任务评价低。这与[记忆与上下文]({{< relref "/docs/claude-duet/analysis/memory" >}})、[连接器]({{< relref "/docs/claude-duet/analysis/connectors" >}})两页的结论一致。

## 资料缺口

- 官方的任务完成率、错误率、可用性数据或状态页。
- 发布一个月以上的长期使用记录；研究预览期间更新后的复测。
- 更多独立的同题横评，尤其是控制了连接器和上下文的对比。
- Claire Vo 四智能体节目的评分与结论（目前只有任务清单）。

## 主要资料

- 官方：[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})（自承局限）、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})
- 媒体：[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})（同日横评）
- 社区：[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})、[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})、[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})、[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})、[Claire Vo：四个智能体]({{< relref "/docs/industry/sources/community/2026-10-28-claire-vo-four-agents" >}})（无结果）、[施言：十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})（二手）、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})
