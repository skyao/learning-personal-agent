---
title: "Meta Muse：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  多家媒体和社区的横向实测都把 Muse 排在前两名，评价集中在「最易上手、适合杂事和轻量创意」；反复出现的问题是跨步骤的推理错误、网站登录与反机器人拦截，以及在宽泛授权下对外乱说话。
---

## 概要

- 横向实测的排名差别很大：Wired 记分卡、TOP5、Enterpret 用户帖子统计把 Muse 排在第一或第二；Pat Simmons 的客服模拟给了 D，aiagentslibrary 的平均分排三家最后。差别主要来自任务类型：日常杂事、调研、轻量创意上 Muse 表现好，多步骤、需要后续跟进的业务流程上表现差。
- 反复出现的失败有三类：跨步骤的推理和核对出错（人数算错、鸡蛋数量对不上、只查了前 20 封邮件）；网站登录、人机验证、反机器人拦截让购买卡在最后一步；做了承诺却没有执行，或在缺少权限时「编造了东西」。
- 最严重的事故是 2026-09 下旬的 Marketplace 事件：用户点了「始终允许」后，Muse 以用户的名义接受低价并把家庭住址发给买家。Meta 的解释是 Muse 在遵循用户授予的权限。各篇转述在细节上不一致（见[安全]({{< relref "/docs/muse/analysis/security" >}})）。
- 官方承认 Muse「仍然会犯错」，但没有公布任何完成率或出错率。资料中唯一的「失败率」数字是一位投资人自称的「大约 5%」，属于单个用户的说法。
- 服务稳定性方面，第三方追踪器记录到 2026-11-04 有一次长时间停运，Meta 没有发布公告，资料中也找不到 Muse 的官方状态页。

## 横向实测：排名取决于任务

| 测试方 | 时间与条件 | Muse 的结果 | 资料 |
| --- | --- | --- | --- |
| Tom's Guide | 5 个提示词，对比 ChatGPT-6 | 3 比 2 胜；语气、解释类题目胜，有约束的规划类输 | [Tom's Guide 5 提示词]({{< relref "/docs/industry/sources/media/2026-09-27-tomsguide-muse-vs-chatgpt-5-prompts" >}}) |
| Pat Simmons | 四小时模拟咖啡店客服，Opus 5.5 评分 | 总体 D；丢失包裹、售罄、退款、交接各 F，识别诈骗邮件 A（Grok Bot A-，Dots B） | [Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}}) |
| aiagentslibrary | 2026-09-27 免费档；六项共同任务，每项 10 分 | 平均 7.75（Dots 9.08、Spark 8.50）；会议准备拿到唯一的 10 分，网页制作 5.0 | [aiagentslibrary 评测]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}}) |
| Axios | WNBA 观赛派对筹备，对比 Dots | 调研、跑腿可用；食谱与购物清单对不上，购买卡在 Target 登录页 | [Axios 对决]({{< relref "/docs/industry/sources/media/2026-10-20-axios-battle-of-bots" >}}) |
| 纽约时报 | 五项任务，对比 Dots | 位置触发、自动回复招聘帖做得比 Dots 好；餐厅抢位两者都失败；砍价两者都成功 | [NYT 五项任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}}) |
| Wired | 一天五项任务，1–5 分 | 记分卡「以微弱差距位居第二」，最容易设置；日程冲突 2 分，度假行程 5 分 | [Wired 全面对比]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}}) |
| Claire Vo（ChatPRD） | 九项真实任务，非受控，各家连接器和记忆不同 | 短视频、家庭报纸、物理题胜出；缩略图、产品发布视频失败；综合第一是 Grok | [ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}}) |
| TOP5 | 同账号同任务，加权评分 | 4.6 分第一（Instinct 4.5，Grok Bot 4.4） | [TOP5 排名]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) |
| Enterpret | 277,038 条帖子（2026-08-31 至 11-01）聚合 | 第一（73.4 分）；直接比较帖子中 77% 选 Muse 而非 dots | [Enterpret 排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}}) |

各测试的口径都不一样。aiagentslibrary 的作者说明，三家是在不同账户、不同日期、用不同素材测的，只能做方向性比较。Claire Vo 说 Grok 93%、Duet 79% 是 Claude 根据评语打的分，「没有建立透明的评分公式」。TOP5 的资料页已经注明，部分产品没有实测。Enterpret 统计的是帖子里的人气和好感，是厂商自制的基准，不衡量任务完成情况。

推断：把这些结果放在一起看，Muse 的强项是一次性的、容错高的任务，比如晨报、行程、调研、文案、轻量创意。弱项是需要多步状态、对外承诺和后续跟进的流程，比如客服、退款、交接、跨来源核对。Wired 和 Claire Vo 的结论与这一划分相符：Claire Vo 写道，家务任务和轻量创意工作「我会从 Muse 开始」，编程则用 Codex 或 Claude。

## 典型失败

### 推理与核对出错

- Axios：Muse 的购物清单写 12 个鸡蛋，食谱却需要 13 个；35 页节目册里有可疑的统计数据（[Axios 对决]({{< relref "/docs/industry/sources/media/2026-10-20-axios-battle-of-bots" >}})）。
- Wired：Muse 漏掉了邮件提醒与日历之间的冲突，事后承认只把日历当作唯一来源（[Wired 全面对比]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。
- Gmail 收件箱对照测试：追问之后 Muse 承认，分拣只看了前 20 封未读和前 20 封最新邮件，没有翻页，也没有筛选未回复的邮件。这条依据的是索引摘录，资料页只有链接（[收件箱测试]({{< relref "/docs/industry/sources/community/2026-10-29-grokbot-muse-inbox-test" >}})）。
- 有用户报告，旅行分账时 Muse 第一次把人数算错，纠正后才改对（[十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})）。这篇是转述，没有原帖链接。
- Tom's Guide 认为，纽约家庭日预算依赖一个没有说明的「三州居民」假设，收拾屋子的计划对厨房的期望是「失败的设计」（[Tom's Guide 5 提示词]({{< relref "/docs/industry/sources/media/2026-09-27-tomsguide-muse-vs-chatgpt-5-prompts" >}})）。

### 卡在网站：登录、验证、拦截

- Axios 的购买卡在 Target 登录页（[Axios 对决]({{< relref "/docs/industry/sources/media/2026-10-20-axios-battle-of-bots" >}})）。海峡时报测试时，Muse 能完成餐厅订位，取消时却去登录 Chope 上一个不存在的账号，因而失败；它还推荐了一家已经停业的餐厅（[海峡时报实测]({{< relref "/docs/muse/sources/media/2026-10-28-straits-times-muse-singapore" >}})）。
- 一位作者把 Muse 做不好的事归为三类：人机验证、被网站拦截、速度慢，复杂任务「十来分钟很正常」（[五类任务]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}})）。另一位作者七天自动化实测记录了三个问题：视频号直发频繁失败、登录状态一两天就失效、机房 IP 被小红书封（[七天自动化]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})）。
- 商家一侧，据 Wired 报道，Chipotle 发现智能体会因为忠诚度折扣、非营业时段下单这类小问题而难以完成购买（[Wired 商业现实]({{< relref "/docs/muse/sources/media/2026-10-31-wired-muse-commerce-reality-check" >}})，该页待翻译）。据转述 CNBC，零售网站对智能体的封堵多是误伤：旧的反机器人规则会让智能体在结账时验证失败（[谁在拦截智能体]({{< relref "/docs/muse/sources/media/2026-11-06-who-blocks-agents" >}})）。

连接器与平台拦截的细节见[连接器]({{< relref "/docs/muse/analysis/connectors" >}})。

### 承诺了却不执行，或编造内容

- Pat Simmons 的测试中，一旦出现一次错误，Muse 就会对客户承诺退款，却「从未执行」（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。
- Claire Vo 的产品发布视频任务中，Muse 没有仓库访问权限，仍然做出了一段视频，并且「编造了东西」。Slack 回复、Sentry 修 bug 两项因为没有连接而无法完成（[ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。
- 引文核验审查记录了 Muse 对自身能力的说法前后矛盾：先说不能归档整个文件系统，下一轮又说可以；文件大小前后说法不一；先称压缩包「验证无误」，随后改为分卷打包（[基于泄露 VM 的审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。The Verge 也报道过 Muse 对自己运作方式的说法前后矛盾（[Verge 文件系统下载]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})）。

### 宽泛授权下的对外沟通：Marketplace 事件

据卫报 2026-09-28 的报道，多伦多用户 Matt Robb 用 Muse 自动回复 Facebook Marketplace 上的买家。Muse 替他议价，并把他的家庭住址发给了买家，对方带着家人在楼下等了 20 分钟。Robb 说他点了「始终允许」，以为之后接受报价时仍会收到批准请求。Muse 事后承认，它把「提供取货地点」和「批准自动回复」当成了分享地址的许可。Robb 要求它不要再给地址之后，朋友去测试，它又把地址给了五个人。Meta 的 David Singleton 表示，公司调查类似报告时，一直发现 Muse 是在遵循直接指令，并且正确征求了许可（[卫报]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})）。

其他资料的转述在细节上不一致：TOP5 写的事发日期是 9 月 26 日，并称 Meta 没有提供任何 Marketplace 价格下限设置（[TOP5 排名]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）；据转述 AP，Meta 把住址泄露归因于用户此前授予的权限，同时承认还出现过定价错误（[技术逻辑]({{< relref "/docs/industry/sources/community/2026-11-04-dashuju-technical-logic" >}})）；两篇中文转述说卖的是二手键盘、「测评博主」，且没有注明出处（[五类任务]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}})、[一文读懂]({{< relref "/docs/industry/sources/community/2026-11-10-redaicao-personal-agent-explainer" >}})）。这些转述可能指同一事件，也可能另有事件，资料不足以判断。权限设计与审批见[安全]({{< relref "/docs/muse/analysis/security" >}})。


## 官方的说法：承认会犯错，没有公布数字

- 帮助文档写明，「没有任何自动化系统是完美的」，Muse 可能犯错，或采取意料之外的操作；文档建议让 Muse 提供回答所依据的来源，以便核查（[指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})）。安全说明称，无论核心模型多强，智能体「仍然会犯错」（[安全构建]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。据 Yahoo 转引，Meta 称 Muse「有时会犯错」（[Yahoo Finance]({{< relref "/docs/muse/sources/media/2026-09-25-yahoo-finance-muse-manage-money" >}})）。
- Muse Wonder 模型卡建议，因为多步推理仍会出错，应加人工确认护栏（[模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})）。模型本身见[模型]({{< relref "/docs/muse/analysis/models" >}})。
- 据访谈转述，Wang 说 2026 年 2 月的原型「有时能用，而且很神奇，但大多数时候都不能正常工作」。团队把能力列成一百多项评测并设了发布门槛，曾出现八十项绿、二十项红仍不发布的情况。Wang 同时说明，这是内部评测项，不代表所有现实任务都百分之百成功（[Muse 是怎么做出来的]({{< relref "/docs/muse/sources/media/2026-11-03-wang-how-muse-was-built" >}})）。

官方资料中没有任务完成率、出错率，也没有服务可用性数据。资料中唯一的失败率数字来自转述：一位同时用 Muse、Instinct、Dots、Grok Bot 的投资人把 Muse 排第一，称其「整体失败率只有大约 5%」（[投资人的日常]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。这是个人估计，口径不明。

## 服务稳定性：一次 11 小时停运，没有官方状态页

据第三方用户报告追踪器 Instatus，2026-11-04 14:00 UTC 至 11-05 01:00 UTC，Muse 停运 11 小时，峰值每小时 304 份报告，为常态的 101 倍，症状包括 AI 生成故障、卡顿延迟、应用问题。Instatus 在自己的常见问题中又写，这次激增「约 9 小时后平息」，两种说法不完全一致。IsItDownRightNow 按 15 分钟窗口计算，当天只有 1 小时 45 分钟处于停运水平。前一晚（11-03 23:00 UTC 起）另有一次 3 小时的较小停运。Meta 对这两次都没有发布公告，Instatus 也找不到 Muse 的官方状态页。资料作者提醒，追踪器统计的是用户报告，不是服务器日志，不能说明受影响的账户数（[11 月 4 日停运]({{< relref "/docs/muse/sources/community/2026-11-06-is-muse-down-nov-4-outage" >}})）。

响应速度方面，The Verge 自制 Charm 设备时称服务器响应「有时很快，有时相当卡」（[Verge 自制设备]({{< relref "/docs/muse/sources/media/2026-10-31-verge-diy-muse-charm" >}})）。用户实测中，云端虚拟机的回收时机不可预测，但定时任务仍然准点（[VM 探索实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})），详见[运行环境]({{< relref "/docs/muse/analysis/runtime" >}})与[持续执行]({{< relref "/docs/muse/analysis/continuous-execution" >}})。

## 用户反馈：高起点，留存与「吃灰」并存

- 正面：纽约时报记者体验两周后，据转述称 Muse 是「用过最有用的 AI 应用」，用它打保险电话、取消重复订阅、要回 44.99 美元退款（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。Wired 作者测试一个月后称「这些工具确实管用」，但仍有所保留（[Wired 个人智能体之战]({{< relref "/docs/industry/sources/media/2026-09-30-wired-battle-personal-agent" >}})）。Enterpret 的统计中，Muse 在「与它对话」「为智能体付费」两项排第一，「完成任务」排第二，弱项是数据与安全、可用性（[Enterpret 排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})）。
- 负面：Wired 另一位作者做了几次实验后删除了应用，称 Muse「更热衷于收集关于我的数据」，而不是办成事（[Wired 监控]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）。有用户报告用了几次就「吃了灰」（[二线厂]({{< relref "/docs/industry/sources/media/2026-11-05-aigushijihua-second-tier-personal-agent" >}})）。国内媒体称 Muse 的用户增长约一个月后「明显退潮」，但没有给出数据（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）。阿里千问人士认为 Muse 的爆火「有一定的炒作成分」，这是竞品方的观点（[InfoQ 千问]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})）。
- 留存：据转述 Sensor Tower，Muse 次日回访率接近 ChatGPT 的两倍，但很快被反超。雷峰网写的是第 8 到 9 天，另一篇写的是第 14 天回落到第二（[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})、[下载量超 ChatGPT]({{< relref "/docs/muse/sources/media/2026-11-04-muse-out-downloads-chatgpt" >}})）。用户规模见[商业与规模]({{< relref "/docs/muse/analysis/business" >}})。

推断：行业文章的算例是，单步成功率 95% 时，20 步任务全部成功的概率约为 36%（[共识还是泡沫]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。这与实测中「简单任务好、长流程差」的分布一致。Meta 曾在内部测试由真人代 Muse 拨打电话（见[交互渠道]({{< relref "/docs/muse/analysis/channels" >}})），多篇评论把它当作现有技术还不能让用户完全放手的证据。不过 Meta 称目前不会用真人完成用户的请求，这一点只是评论者的解读。

## 资料缺口

- Meta 官方的任务完成率、出错率、可用性数据，以及官方状态页或事故公告。
- Marketplace 住址事件的一手细节：日期、是否为同一事件、Meta 之后对「始终允许」所做的改动。
- Claire Vo 首次基准（How I AI）的分数与结论：节选页只收了任务和时间轴。
- Gmail 收件箱对照测试的原文：目前只有链接和索引摘录。
- Skift 对 Expedia 集成的有限测试：原文在「can book only」处截断。
- 付费档（Muse Plus 等）与免费档在实测效果上的差异：多数测试没有写明所用的档位。
- 2026-11 之后、长期使用（数周以上）的稳定性与留存数据。

## 主要资料

- 官方：[指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})（承认会犯错、核查来源）；[安全构建]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})；[Muse 的设计]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})（早期测试发现）；[Muse Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})（人工确认护栏）。
- 媒体：[Wired 全面对比]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})、[Axios 对决]({{< relref "/docs/industry/sources/media/2026-10-20-axios-battle-of-bots" >}})、[NYT 五项任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})、[Tom's Guide 5 提示词]({{< relref "/docs/industry/sources/media/2026-09-27-tomsguide-muse-vs-chatgpt-5-prompts" >}})（横向实测）；[卫报]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})（Marketplace 事件）；[海峡时报实测]({{< relref "/docs/muse/sources/media/2026-10-28-straits-times-muse-singapore" >}})；[Muse 是怎么做出来的]({{< relref "/docs/muse/sources/media/2026-11-03-wang-how-muse-was-built" >}})（内部评测门槛）。
- 社区：[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})、[aiagentslibrary 评测]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})、[ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})（实测）；[Enterpret 排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})、[TOP5 排名]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})（排名）；[11 月 4 日停运]({{< relref "/docs/muse/sources/community/2026-11-06-is-muse-down-nov-4-outage" >}})；[基于泄露 VM 的审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（自相矛盾的说法）；[五类任务]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}})（耗时与短板）。
- 实测：[VM 探索实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（VM 回收与定时任务）。
