---
title: "Today AI：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  主动性是 Today 最被强调、也最被实测认可的能力：官方把主动开口限定在早晚两份简报，另有单次与周期任务；实测中提前提醒考试报名、模型发布、展会等案例较多。团队自评主动性「只有二三十分」，也有作者嫌它主动得「烦」。
---

## 概要

- 官方设计是「克制的主动」：只在早晨和傍晚两个锚点主动开口，其余默认折叠；主动不等于自主，未经确认不发邮件、不改日历、不给任何人发消息。
- 团队按用户是否回复、是否阅读主动消息调整推送频次，两种正向信号都没有就判断为骚扰并降频。
- 支持单次与周期任务，符合条件的任务在云端继续，完成后返回结果、需要输入时再找用户。长期目标（学语言、健身）是团队重点描述的场景。
- 实测中主动提醒的成功案例较多：考试报名、新模型发布、Suno 下载政策变化、周末活动、行业大会。品玩作者也称主动程度有时让人「烦」。
- 晚点访谈中团队称主动化是个人 AI 助理最重要的价值来源，并自评当前主动性「只有二三十分」。

## 早晚两份简报

官方称 Today 只在一天的两个锚点先开口：晨间简报只讲少数会塑造这一天的事，晚间收尾把滑过去的事往前滚并问一个去向问题；其余默认折叠，除非自上次查看后有变化且关系到还来得及做的决定；每条主动消息都得是用户愿意让人特地来告诉的事（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）。官方定义文称误报侵蚀信任快过漏报（[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})）。

实测印证了这一形态。Founder Park 称早间简报挑出当天的日程和变化，晚间回顾推进了什么，内容大多放在右侧面板，不频繁弹窗（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。产品笔记称国内版新增了简报时间偏好设置，简报「不是总结」，基本可以当待办用（[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})）。

## 主动性的频率控制

团队自述：根据用户反馈调整主动推送频次，一看用户是否回复了主动消息，二看是否至少读了；正向信号都没有，就认为确实在做骚扰（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。官方评测框架设有「主动克制」维度，考察无话可说时是否保持沉默（[官方评测框架]({{< relref "/docs/today/sources/official/2026-09-20-today-assistant-benchmark" >}})）。

用户感受并不一致。品玩作者称 Today 主动程度有时让人「烦」（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。Founder Park 认为 Today 比 Muse 更积极（Muse 为主动消息设了较高门槛），是否会被习惯性忽略待观察（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。

## 定时任务、事件跟进与长期目标

能力页称支持单次和周期任务，可设定时间，符合条件的任务在云端继续，完成后返回结果，需要输入时再找用户；生成建议和发送通知是两个独立环节，部分预先授权或已安排的任务可以自动运行（[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})）。

官方称目标是按「月」推进健身、学习、储蓄这类人生弧线，长期任务跨天存活（[官方：Meet Today]({{< relref "/docs/today/sources/official/2026-08-03-meet-today" >}})）。团队举例：把学语言委托给 Today 后，它每天中午发一个课程并在交互中改进（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。

实测案例：

| 来源 | 案例 |
| --- | --- |
| [品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}}) | 9 月 2 日主动推送 GPT-6「Astra」即将发布，次日 OpenAI 发布；提前提醒 Suno 下载政策收紧；约采访对方回信后主动接上任务 |
| [极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}}) | 连飞书后每天 9 点推送选题，并主动追问稿件进度 |
| [二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}}) | 考试报名公告一出即提醒；常在周五推荐周末展览；从飞书读到选题和截稿日后，建议去腾讯全球数字生态大会现场 |
| [产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}}) | 简报给出的选题「都是我写过的或计划写的」 |

Today Recording 的会前提醒也属主动行为：连上日历后在锁屏以 Live Activity 问是否录音，不点就不录；官方说明尚不会从会议自动生成行动建议或自动建任务（[官方：Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})）。

品玩作者区分了「定时任务式主动」和「基于记忆判断状态变化再行动」，认为 Today 的案例属于后者（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。

## 团队的自我评估

晚点访谈中受访者称主动化是个人 AI 助理最重要的特质和价值来源，个性化、模型、Infra 降本都是为它铺路；自评「今天的主动性仍只有二三十分」，如果还得主要靠用户自己学怎么用，普及会很慢（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。

## 资料缺口

- 任务数量、周期任务频率、单任务时长的上限；失败重试与通知机制。
- 主动消息降频的具体阈值，用户能否手动调节主动程度（除简报时间外）。
- 长期目标（数周以上）跟进效果的实测。

## 主要资料

- 官方：[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[Meet Today]({{< relref "/docs/today/sources/official/2026-08-03-meet-today" >}})、[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})（简报设计与克制原则）；[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})（任务机制）；[Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})；[官方评测框架]({{< relref "/docs/today/sources/official/2026-09-20-today-assistant-benchmark" >}})。
- 媒体：[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})（频率控制、长期目标）；[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})（自评）；[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})、[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})、[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})、[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})（实测）。
- 社区：[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})。
