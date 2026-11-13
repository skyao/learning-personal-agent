---
title: "Today AI：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Today 国际站列出 55 项云集成，以办公协作、开发与健康设备为主；国内版接入飞书、钉钉、企业微信、腾讯文档和邮箱。它不碰外卖、打车、订票、购物等交易，淘宝、天猫明确不支持。团队称会一家家谈合作，并开放第三方提交集成。
---

## 概要

- 国际站集成页（2026-11-05 收集）列出 55 项云集成，标题写「50+」，另有 17 项标 Soon；每项写明能读什么、能做什么。会改变事物的操作先等用户确认。
- 国内版接入的是办公类入口：邮箱（含 163、QQ）、飞书、钉钉、企业微信、腾讯文档、腾讯会议、滴答清单、微信读书。国际站把飞书、钉钉、腾讯文档仍标为 Soon，两个版本的清单不同。
- 交易类服务基本空白：多篇资料称 Today 现阶段不碰外卖、打车、订票、购物；实测中它明确不支持淘宝、天猫；有用户称挂号、缴费、订酒店、买机票「一个都进不去」。
- 微信不是能完整接入的数据源，但可以绑定微信作为对话入口（见[交互渠道]({{< relref "/docs/today/analysis/channels" >}})）。团队认为用户想代劳的多是非熟人网络的事，缺微信数据影响有限。
- 生态策略是开放与谈判并行：集成页开放「List Your Integration」提交；被问到亚马逊封禁 Muse，团队称会「一家家去谈合作」。

## 国际站：55 项云集成

集成页把云集成与设备能力分开列出。云集成包括 Gmail、Google Calendar/Drive/Contacts、Microsoft 365、Slack、Discord、Notion、X、LinkedIn、Todoist、Asana、Linear、Zoom、GitHub、Figma、HubSpot、YNAB、QuickBooks，以及 WHOOP、Oura、Garmin、Fitbit 等健康设备。标为 Soon 的有 Feishu、Lark、DingTalk、WhatsApp、Reddit、Instagram、Jira、Tencent Docs、Salesforce、Stripe、Strava 等；官方称这些「已经建好但尚未对所有账户开放」，有的在测试，有的在等合作方审核（[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})）。

官方博客称健康集成遵循 Apple HealthKit 和 Android Health Connect 的权限，并称「社区 Skills」可让智能体装一次即继承一套工作流（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）。资料中没有 Skills 的具体清单或使用实测。

## 国内版：办公入口为主

Founder Park 称国内版已接入邮箱（含 163、QQ 邮箱）、飞书、钉钉、腾讯文档（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）；智能涌现称国内版上线后迅速支持飞书、钉钉、企业微信、滴答清单（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。二阶变量看到的接入列表分本机、云端、其他设备三类，云端最上面是飞书、钉钉、企业微信、腾讯会议，另有 QQ 邮箱和微信读书（[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})）。

团队称接入其他连接器暂未遇到明显阻碍，MCP、对 Agent 友好的服务商和 Phone Use 都可能打通生态；关于微信，团队认为用户想让 Agent 代劳的多是非熟人网络的琐事，微信沉淀的是熟人社交，所以没有微信数据也乐观（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。

## 交易类服务的空白

- 产品笔记称 Today 现阶段不碰点外卖、打车、盯低价、订票、购物，作者认为国内交易被大厂生态封闭，不碰是聪明的选择（[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})）；Founder Park 也称目前不太涉及购物、代下单（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。
- 二阶变量让 Today 推荐手账，它明确不支持淘宝和天猫，转而搜索当当、孔网、京东和海外文具商（[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})）。
- AIX财经称一位 Today 用户让 Agent 挂号、缴费、订酒店、买机票，「一个都进不去」（[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。

二阶变量据此称 Today 更像信息助手，是「无法执行和跑腿的秘书」（[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})）。这一判断与品玩（确认后发出邮件）、极客公园（汉化游戏 mod）中的执行实测不完全一致，差别在于交易与第三方平台操作，而不是一般的执行能力。

极客公园、黑咖啡、鸿煊等文章都认为，国内生活服务集中在微信、淘宝、美团、支付宝等超级 App 里，接口要一家家打通（[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})、[黑咖啡]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。

## 授权与开放策略

集成页称权限按来源授予，可以只连日历、之后再加邮件；断开某来源即移除访问权限；任何会改变事物的操作都先等用户确认；第三方可通过「List Your Integration」提交集成，会被审核用户价值、权限和数据安全（[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})）。官方定义文建议权限分阶段给（[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})）。

晚点访谈中，被问到亚马逊封禁 Muse，受访者称会尽最大努力一家家谈合作，生态不是一成不变的（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。产品笔记作者推断，腾讯、蚂蚁在投资人之列，可能为后续开放合作提供可能（[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})）。

## 资料缺口

- 国内版完整的连接器清单与读写范围；国际站与国内版的差异对照。
- 社区 Skills 的数量、来源与审核。
- 连接器失效（授权过期、接口变化）的处理方式。
- 与腾讯、蚂蚁等投资方是否有生态合作。

## 主要资料

- 官方：[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})（云集成清单、授权与开放）；[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})。
- 媒体：[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})、[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})、[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})（国内版清单、交易空白）；[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})（谈合作）；[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})（用户反馈）；[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})。
- 社区：[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})；[黑咖啡]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})（国内生态围墙）。
