---
title: "WorkBuddy：开放与价格"
linkTitle: "开放与价格"
weight: 100
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 2026-03-04 正式发布，不设邀请制；国内个人版按积分计费，7 月起分体验版（免费）、标准 99 元、高级 199 元、旗舰 999 元四档，积分与 CodeBuddy 共享。10 月底起又可通过 Buddy One VIP 与腾讯文档、会议、ima、网盘打包购买。
---

## 概要

- 开放：2026-03-04 正式版发布，macOS、Windows 双平台，资料中没有邀请制或等候名单；另有海外版（Gmail、Outlook 连接器，巴西葡萄牙语、印尼语界面）。
- 计费单位是积分：内置模型按 Token 定价和任务复杂度扣积分；自定义模型的费用由用户付给第三方。
- 国内个人版自 2026-07-01 起四档：体验版免费（每月 500 积分）、标准版 99 元/月、高级版 199 元/月、旗舰版 999 元/月；连续包月七折，连续包年 5.6 折。积分按月发放、不结转。
- 与 CodeBuddy 同账号共享积分，二者统称 Buddy AI。10 月底推出的 Buddy One VIP 把 WorkBuddy 和腾讯文档、腾讯会议、ima、腾讯网盘捆在一个会员里，共享积分和 1TB 存储。
- 价格表中多项「限时」「限免」没有写截止日期。

## 开放范围

4.5.0（2026-03-04）正式发布，支持 macOS 与 Windows（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）；4.6.2 增加 Windows ARM 下载入口（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。资料中没有邀请制、等候名单或年龄限制的说明。海外版在日志中单独出现：5.6.0 新增巴西葡萄牙语和印尼语界面，5.7.5、5.7.6（10-03、10-04）为海外版加入 Outlook、Gmail 连接器（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。各即时通讯渠道有各自的账号要求，如微信助理要求国内版、QQ 机器人要求实名认证（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。

企业微信入口：据数智奔流，企业微信桌面端 5.0.12 起可在「智能机器人」入口限量免费领取试用，领完可以向管理员申请；企业管理后台可统一采买、分配名额、调配额度（作者转述官方直播）（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。

## 国内个人版价格（2026-07-01 起）

2026-07-01 起，Buddy AI（WorkBuddy、CodeBuddy 等系列产品统称）国内个人版从单一的专业版扩展为三档付费套餐（[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})）：

| 项目 | 体验版 | 标准版 | 高级版 | 旗舰版 |
| --- | --- | --- | --- | --- |
| 月付 | 免费 | 99 元/月 | 199 元/月 | 999 元/月 |
| 连续包月（7 折） | — | 70 元/月 | 140 元/月 | 700 元/月 |
| 连续包年（5.6 折） | — | 672 元/年 | 1,344 元/年 | 6,720 元/年 |
| 基础积分/月 | 500 | 2,000 | 4,000 | 20,000 |
| 限时加赠积分/月 | — | 2,000 | 5,000 | 30,000 |
| 自动任务数 | 3（限免 99） | 15（限免 99） | 30（限免 99） | 99 |
| 创建项目数 | 5 | 10 | 15 | 20 |
| 资料库容量 | 5 GB | 10 GB | 20 GB | 50 GB |
| 个人助理数 | 3 | 5 | 8 | 10 |
| 模型调度 | Auto（限免全模型可选） | 全模型可选 | 全模型可选 | 全模型可选 |

来源：[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})（页面最后更新 2026-09-24）。CLI 访问从标准版起提供。加量包仅标准版及以上可买，1,000 积分 50 元，有效 1 个月，不退款（[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})）。

7 月 1 日前的付费会员按过渡规则升级为标准版，已开月付自动续费的享半年保价：2026-12-31 前 58 元/月，2027-01-01 起 70 元/月（[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})）。

企业版另行计费，资料中只有规则没有价格：有效期为新购当日到次月当日，到期后企业无法使用任何功能（[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})）。

## 积分规则

- 积分按月发放、当月有效、不累积结转；赠送部分自到账起 1 个月有效；会员到期后月额度降为体验版（[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})）。
- 扣减时先用最先到期的积分，到期时间相同时先基础积分、后赠送积分（[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})）。
- 消耗取决于模型 Token 定价和任务复杂度；上下文窗口越大单轮越多（[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})、[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。积分与 Token 的换算没有公开。
- 循环检测时用户选择终止，已产生的部分消耗进入退费评估（[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})）。
- 连接器自身的读写不消耗积分（[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})）；专属邮箱在界面查看邮件不消耗（[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})）；记忆提取不消耗（[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})）。

日志中的配套功能：5.2.2 用量与到期提醒，5.2.3 夜间折扣展示，5.4.7（09-01）「订阅和用量」页可应用内购买积分、管理自动续费，5.0.3 起有「成长计划」领积分（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

## Buddy One VIP：与腾讯办公产品打包

5.9.1（10-22）新增 Buddy One 会员购买（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。权益说明页（最后更新 10-28）写明（[帮助：Buddy One 权益]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-buddy-one-benefits" >}})）：

- 一个会员包含 WorkBuddy、腾讯文档、腾讯会议、ima、腾讯网盘的权益；WorkBuddy 部分为每个套餐周期 20,000 基础积分、30,000 赠送积分、1TB 存储及旗舰版其他权益。
- WorkBuddy 积分将统一升级为 Buddy One 积分，几款产品共享积分与存储，不重复发放。
- 已有标准版、高级版的用户购买后立即生效，原套餐剩余部分按规则退款；旗舰版可免费转换一次。
- 会员失效后积分清零、1TB 扩容收回，已存文件保留。

Buddy One VIP 的价格资料没有给出。WorkBuddy 部分的积分数与旗舰版（20,000 基础 + 30,000 限时加赠）相同，但两页的「赠送」是否同一口径、是否同样限时，资料没有说明。

《中国新闻周刊》把 Buddy One 写成 WorkBuddy 10 月底发布的「连接文档、会议和网盘的协同体系智能体」（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})），与帮助中心把 Buddy One 写成会员和积分体系的说法不同。

## 资料缺口

- Buddy One VIP 的价格；企业版价格。
- 「限时」加赠积分和「限免」自动任务数的截止日期。
- 海外版的价格与开放地区。
- 积分与 Token 的换算、各模型单价；典型任务消耗多少积分。

## 主要资料

- 官方：[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})（价目表、过渡规则）、[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})（积分规则、企业版有效期）、[帮助：Buddy One 权益]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-buddy-one-benefits" >}})（Buddy One VIP）、[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})（自定义模型费用）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（发布、海外版、计费功能）、[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})（渠道的账号要求）
- 媒体：[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})（Buddy One 的另一种说法）
- 社区：[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})（企业微信试用）
