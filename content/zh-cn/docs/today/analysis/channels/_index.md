---
title: "Today AI：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Today 以自有 App 为主入口，所有交互在一个长对话里；国内版可绑定微信作为对话入口，WhatsApp 标为 Soon。团队 3 月试过只住在 IM 里的形态后放弃。Today 没有自己的邮箱、号码等对外身份，对外发送都以用户名义、经用户确认。
---

## 概要

- 主入口是桌面端、移动端和网页端的自有 App，界面为左侧单一对话、右侧简报、任务、记忆面板。
- 团队 3 月探索过像 Instinct 那样只住在 IM 里、没有独立 App 的形态，因缺少 GUI 难以引导用户、拿不到设备权限而放弃。
- 国内版可以绑定微信，直接在微信里发语音、图片、文件，极客公园作者后来不再打开 App。国际站集成页把 WhatsApp 对话标为 Soon；macOS 可读写 iMessage（作为数据源）。
- Today 不给智能体分配独立的邮箱、号码或钱包；邮件等对外发送以用户名义进行，先经用户确认。
- 用户须给助手起名，可设形象与对话风格；官方称语音会作为「一等输入」投入。

## 自有 App 为主，IM 为辅

智能涌现整理的团队自述称，3 月曾探索类似 Instinct 的住在 IM 里、没有独立 App 的形态，因为没有 GUI 对用户探索 Agent 能力的引导很弱，且没有客户端拿不到一部分设备权限，最终确定做独立 App（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。晚点对照了三种界面：Instinct 主要交互在用户的 iMessage，Muse 和 Today 有移动端、电脑端各端应用（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。潮涌AI统计的 15 家产品中七家住在短信、iMessage 或 WhatsApp 里，Today 属于以 App 为主界面的少数（[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})）。

极客公园描述电脑版界面：左侧对话，右侧简报、任务、记忆和关联应用（[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})）。Founder Park 称国内版能把整理结果做成 HTML 页面一键分享，不必塞回聊天框（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。

微信可作为对话入口：极客公园作者绑定微信后直接在微信里发语音、图片、文件，用到后来不再打开 App，「它更像是微信列表里的一个好友」（[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})）；品玩作者首次打开即接入微信，在对话里让 Today 约采访（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。国际站集成页未列微信，WhatsApp 对话标 Soon；设备部分列有 macOS Messages（读写 iMessage，需 Full Disk Access）和 Android 短信通话（仅直装版）（[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})）。资料没有说明 iMessage 能否作为与 Today 对话的入口。

## 没有独立身份，对外以用户名义

官方称对外发送一律先经用户批准（[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})）。品玩实测：Today 从 Gmail 找联系人、查日历后起草邮件，作者回复「确认」后邮件发出（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。资料中没有 Today 拥有独立邮箱、电话号码或对外身份的描述；鸿煊综述把 Cue 等「给每个 Agent 一套外部可寻址身份」列为另一条路线（[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。

## 助手的名字与形象

Today 注册时必须给助手起名（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})），国内版还可设置形象和对话风格（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。官方称会把语音当作一等输入投入，Today Recording 的 Summary 和追问在各平台都可用（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[官方：Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})）。

## 资料缺口

- 微信绑定的实现方式（公众号、企业微信还是个人号）、限制与稳定性。
- WhatsApp 入口的上线时间；iMessage 能否作为对话入口。
- 语音对话的实测。

## 主要资料

- 官方：[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})（WhatsApp、Messages）；[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})；[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})；[Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})。
- 媒体：[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})（放弃纯 IM 形态）；[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})、[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})（微信入口实测）；[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})；[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})。
- 社区：[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})（渠道路线对照）。
