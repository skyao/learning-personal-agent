---
title: "Instinct：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-15
sourcesUntil: 2026-11-13
description: >
  主动性是 Instinct 在评测中最常被提到的长处：它会跟进用户丢下的事、追踪价格、发现航班变动并争取退款，急事会主动打电话。但它没有公开的定时任务或触发器说明，WIRED 横评中它也没发现邮件与日历的冲突。任务的生命周期和数量限制，资料都没有写。
---

## 概要

- 实测中的长期跟进案例：发现阿拉斯加航空把航班提前 90 分钟，据此全额退票，省下约 550 美元（WIRED）；追踪机票降价、追回里程（Android Authority）；发现餐厅订位日期错成抵达前一周（社区转述）。
- Top5Apps 称它「最有能力、最主动」，会跟进用户丢下的线程、提醒用户忘了的事；WIRED 记者称它不会发太多消息。
- 反例：WIRED 2026-10-27 横评中，邮件提醒与日历会议冲突，Instinct 没有指出，只问要不要每天早上做这项检查，该项 2/5。
- 用户发短信或打电话，它也回短信或回电话；创始人称急事它会主动给用户打电话。
- 没有公开的定时任务、事件触发或审批工作流文档；创始人描述的「数月长期目标」是愿景，不是已上线功能。

## 跟进与提醒：实测中的长期任务

WIRED 记者 Zoë Schiffer 的使用记录里，最典型的一次是：纽约与迈阿密的行程冲突时，Instinct 发现阿拉斯加航空把航班提前了 90 分钟，据此取消机票、全额退款，省下约 550 美元，并重订了回旧金山的单程票。它还主动提醒作者「不要打开」一封朋友邀请烧烤的邮件，事后证实是钓鱼邮件（[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})）。

Android Authority 作者用了一个月：Instinct 追踪机票价格，一降价就通知；还会联系航空公司追回漏记的里程、代为联系客服（[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})）。施言AI 转述的一个 Hacker News 用户案例中，Instinct 对照旅行行程和餐厅订单，发现订位日期错成了抵达前一周，而用户并没有让它检查（[施言AI：10 个海外用户案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})）。WIRED 的横评记录了它的早间消息：提议收掉「昨天的两件未了事」，用户可以标为完成（[WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

Top5Apps 认为主动性是 Instinct 的区别所在：它会跟进用户丢下的线程、就用户忘记的事提醒，评语是「真正主动——跟进被丢下的线程，预约你早该做的检查」，并称它是「最有能力、最主动」的智能体（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。潮涌AI 称它「会主动追问进度」（[潮涌AI：全球 Top15]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})）。WIRED 记者的感受是它「不会发太多消息」，对照的 Lindy 每天早上发消息，还擅自进入 Zoom 会议（[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})）。

## 没发现的冲突

WIRED 2026-10-27 的六款智能体同日横测中，记者设置了一个日程冲突：邮件里提醒下午 2 点给妈妈打电话，日历上同一时段有会议。Instinct 没有指出重叠，只回了一句「想让我每天早上跑这个检查吗」，该项得 2/5；只有 Dots 和 Claude Duet 发现了冲突（[WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

推断：WIRED 的长期使用中它能发现航班变动，横测中却没发现新设的冲突。一种可能是它的主动检查依赖持续一段时间的后台运行和对用户的熟悉程度，同日横测不利于它；资料没有说明它的触发机制，这一点无法核实。

## 主动联系的方式

Top5Apps 写道，用户发短信或打电话，它就回短信或回电话，包括主动联系（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。创始人称遇到紧急事项，比如合同下午三点前要签、只剩五分钟，它会主动打电话给用户（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。C 轮公告提到位置触发的建议：借助 iMessage 位置共享，它能识别用户到达某地并给出建议（[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})）。

群聊里有一个与主动发言有关的细节：有新成员加入群聊时，个人 Instinct 待发出的回复会先暂扣，之后才分享给群组（据 TechCrunch 转述创始人在 X 上的说明，[TechCrunch：群聊上线]({{< relref "/docs/instinct/sources/media/2026-10-05-techcrunch-group-chats" >}})）。

## 机制不透明，愿景大于文档

六款主动型智能体对比一文指出，Instinct 没有公开触发模型，关于日程、事件和审批工作流的公开文档极少，除购买外没有说明，外界无法检查它内部的日程或事件流水线（[六款主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})）。资料中也没有任务列表、暂停、停止、失败重试的界面描述，没有任务数量或时长的限制。

创始人描述的更多是方向：用户指令会从单次任务转向「四个月里把全马成绩提高半小时」这类长期目标；它可以每隔 5 秒在后台扫描刷新餐厅订位；小团队和一人公司的后台运营可以「原生寄生在 Instinct 之上」，在设定库存周转率阈值之类的原则后自主调配供应商和财务账户（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。这些是创始人自述，没有数据或实测佐证。他还称未来 90% 以上的 Token 消耗发生在用户看不见的后台，主动式智能体的算力需求比被动式 AI 高两到三个数量级（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})），这与 [运行环境]({{< relref "/docs/instinct/analysis/runtime" >}}) 中的后台批处理设计和算力约束是一回事。

行业背景：海外独角兽社群转述的一项调研称，目前约 10% 的交互由智能体先发起，这个数字是在讨论 Muse 时给出的，不是 Instinct 的数据（[海外独角兽：PA 社群讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}})）。InfoQ 认为，常驻后台的产品需要在主动检查的价值、频率和算力开销之间取舍（[InfoQ：千问谈下限与上限]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})）。

## 资料缺口

- 触发机制：是否有定时任务、事件触发、条件监控，用户能否创建、查看和取消。
- 主动联系的频率控制和打扰规则；用户能否关闭主动电话。
- 长期任务失败时如何汇报，有没有重试。
- 「四个月长期目标」「一人公司运营」是否已有用户在用。

## 主要资料

- 媒体：[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})，航班退票与钓鱼提醒；[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})，价格追踪与里程追回；[WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})，横测中未发现冲突；[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})，位置触发；[TechCrunch：群聊上线]({{< relref "/docs/instinct/sources/media/2026-10-05-techcrunch-group-chats" >}})，群聊中暂扣回复。
- 社区：[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})，「最主动」的评价；[六款主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})，机制不公开；[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})，创始人对主动执行的设想；[施言AI：10 个海外用户案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})，订位日期错误的用户案例；[海外独角兽：PA 社群讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}})、[InfoQ：千问谈下限与上限]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})，行业背景。
