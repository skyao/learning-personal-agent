---
title: "WorkBuddy：商业与规模"
linkTitle: "商业与规模"
weight: 110
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 的规模数据只有腾讯称的「累计完成 90 亿次任务请求」，口径不明。商业上是积分订阅加企业版，并以 Buddy One 把它与腾讯文档、会议、网盘打包；战略重心是腾讯办公生态与企业微信。
---

## 概要

- 规模数据只有一条：《中国新闻周刊》引腾讯官方数据，称 WorkBuddy 上线以来累计完成 90 亿次任务请求，没有统计截止日期，也不是用户数。
- 收入来源是个人版订阅与加量包、企业版；积分与 CodeBuddy 共享（详见[开放与价格]({{< relref "/docs/workbuddy/analysis/access-pricing" >}})）。
- 10 月底起用 Buddy One VIP 把 WorkBuddy 与腾讯文档、腾讯会议、ima、腾讯网盘打包，产品定位从单一工具转向腾讯办公全家桶的入口。
- 6 月起向团队和企业扩展：Teams 协作、企业智能体、企业自建技能市场；10 月 14 日与企业微信深度融合。
- 第三方把它看作腾讯在办公入口上的布局，早于海外 9 月的一批 Personal Agent 发布。

## 规模：一个口径不明的数字

《中国新闻周刊》写道：「据腾讯官方数据，WorkBuddy 上线以来已累计完成了 90 亿次任务请求」（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）。数字没有统计截止日期；「任务请求」的定义不明，不能换算成用户数或活跃度。同文举了一个用户案例：长沙一家包子铺的老板用 WorkBuddy 自动整理群接龙、生成订单日历，包子日销量从 300 个涨到 800 个（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})），属个案叙述。

资料中没有用户数、日活、付费人数或收入。阿言er 也提醒，发布日期先后「不能单凭这些日期证明哪一家用户最多、增长最快」（[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。

## 商业模式：积分订阅与打包会员

- **个人订阅**：体验版免费，标准、高级、旗舰三档付费，另售加量包（[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})）。
- **企业版**：单独计费；据数智奔流转述官方直播，管理后台可统一采买、分配名额、调配额度（[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})、[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。
- **捆绑**：与 CodeBuddy 共享积分，「无需分别订阅」（[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})）；Buddy One VIP 让 WorkBuddy、腾讯文档、ima、腾讯网盘共享积分与 1TB 存储（[帮助：Buddy One 权益]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-buddy-one-benefits" >}})）。
- **获客与留存**：日志中有成长计划（「领取 Buddy 赚积分」）、邀请入口、夜间折扣（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

成本结构与单位经济资料没有涉及。从模型排队问题看（见[模型]({{< relref "/docs/workbuddy/analysis/models" >}})），算力供给是约束之一。

## 战略：腾讯办公生态的入口

官方简介称 WorkBuddy 是腾讯出品的「全场景 AI 工作台」，「完美连接腾讯办公生态」（[帮助：简介]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-overview" >}})）。更新日志中出现的腾讯产品包括腾讯文档、乐享、ima、元宝搜索、腾讯会议、企业微信、微信支付、混元模型和腾讯云 Token Plan（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。腾讯官网面向国际用户的文章则强调把 AI 带进用户已经在用的 Word、Excel、PowerPoint、腾讯文档、Notion，而不是困在自己的标签页里（[腾讯官网文章]({{< relref "/docs/workbuddy/sources/official/2026-10-12-tencent-six-apps" >}})）。

向团队和企业扩展的节点（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）：5.0.0（06-03）Teams 团队协作（项目、成员、计划看板、资产库）；5.3.3（07-21）企业智能体、企业旗舰版网盘扩容；5.0.0 企业自建 Skill 与插件市场；5.5.0 行业 Buddy 应用；5.7.0 开发者可分享专家、应用、技能。10 月 14 日与企业微信深度融合，数智奔流称腾讯希望把它从聊天工具推向「数字同事」（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。

推断：从产品线看，腾讯把 WorkBuddy 当作把自家办公产品串起来的执行层，变现靠订阅和会员捆绑，而不是交易抽佣或广告。微信支付插件和美团助手出现在日志中，但没有资料说明其商业安排。

## 第三方的判断

阿言er 把 WorkBuddy 与阿里千问办公（8 月 3 日公测）并列为中国办公生态入口，称中国厂商已在「争夺文件、通信和日常工作流里的助手位置」，并指出 WorkBuddy 的更新日志最早列有 3 月 4 日正式发布，「不是等海外 9 月的新品牌出来后才突然开始」（[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。黑咖啡全景解读提到腾讯另有 Handy Bot 在微信内测试，开放时间未公布（[黑咖啡全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})）；它与 WorkBuddy 的关系资料没有说明。

## 资料缺口

- 用户数、日活、付费人数、收入；「90 亿次任务请求」的一手出处、截止日期和定义。
- 企业版客户数与价格。
- Buddy One 的战略定位与价格；Handy Bot 与 WorkBuddy 的关系。
- 微信支付、美团助手的分成安排。

## 主要资料

- 官方：[帮助：简介]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-overview" >}})（定位）、[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})、[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})、[帮助：Buddy One 权益]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-buddy-one-benefits" >}})（收费与打包）、[腾讯官网文章]({{< relref "/docs/workbuddy/sources/official/2026-10-12-tencent-six-apps" >}})（国际版文章）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（团队、企业、生态功能）
- 媒体：[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})（90 亿次、包子铺案例）
- 社区：[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})（办公入口）、[黑咖啡全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})（Handy Bot）、[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})（企业版、数字同事）
