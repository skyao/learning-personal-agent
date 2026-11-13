---
title: "Gemini Spark：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  使用 Spark 必须开启 Keep Activity，第三方据此称 Google 会用活动数据训练并做人工审核；官方承认任务中可能把用户信息分享给网站和第三方 MCP 服务器。数据删除分散在多个入口，他人信息如何处理没有说明。
---

## 概要

- 使用 Spark 的前提是开启「保留活动」（Keep Activity）。Freistyle AI 引 Google 帮助页称，这意味着活动数据用于改进服务（包括训练）并有部分人工审核，被审核的聊天最多保留 3 年。The Verge 转述 Google 的承诺是 Personal Intelligence「不会直接在你的 Gmail 收件箱上训练」。两种说法所指的数据范围不同，本库没有收 Gemini 隐私政策原文来核对。
- 官方帮助页明列：任务中 Gemini 可能向网站分享用户的姓名、联系信息、文件、偏好甚至敏感信息；接自定义 MCP 应用时，即使服务器不是恶意的，信息也可能泄露。
- 删除分散在多个入口：删除任务线程连带删除活动记录和计划，但不删除远程浏览器与代码执行数据，这两类要在设置里另删；关闭任务模式会删除它们；取消订阅后数据保留。
- 他人信息（配偶邮箱、宾客名单、通讯录）如何处理，资料没有官方说明。实测者对 Spark 挖掘个人数据的程度普遍不适。
- 地区上，Spark 不在欧洲经济区、瑞士、英国和尼日利亚提供，官方没有说明原因。

## 训练与 Keep Activity

| 说法 | 来源与口径 | 资料 |
| --- | --- | --- |
| 开启 Personal Intelligence 时，Gemini「不会直接在你的 Gmail 收件箱上训练」，但用户仍须相信 Google 妥善管理数据 | The Verge 转述 Google 的承诺，2026-06-01 | [The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}}) |
| Tasks 必须开启 Keep Activity：Google 用活动数据改进服务（包括训练），有部分人工审核，被审核的聊天最多保留 3 年 | Freistyle AI 引 Google 帮助页（2026-10-28 访问） | [Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}}) |
| 「默认用收件箱衍生的摘要训练（需要开着 Keep Activity）」 | Top5Apps，未注出处 | [Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) |

Keep Activity 是 Spark 的硬性前提：关闭后任务不再列在侧栏，自定义应用不可用（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})、[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})）。Freistyle AI 的对照是：OpenAI 默认不用 Business、Enterprise、Edu 工作区内容训练，Meta 允许退出，xAI 的 Grok Bot 页面没有说明（[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。

推断：Spark 没有「不训练」的开关可选——不开 Keep Activity 就用不了任务。Verge 转述的承诺只针对 Gmail 收件箱本身，而 Keep Activity 涉及的是用户与 Gemini 的交互活动；两者并不矛盾，但「收件箱内容经由任务对话进入活动记录后是否用于训练」，资料无法回答。

## 任务中向外分享的信息

帮助页把下面两类列为隐私风险：

- 浏览网站时，Gemini 可能与网站分享用户的姓名、联系信息、文件、偏好以及来自聊天、关联应用、Personal Intelligence 的敏感信息（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。分享健康、财务、证件号等信息前会暂停请求许可（详见[安全]({{< relref "/docs/gemini-spark/analysis/security" >}})）。
- 使用自定义应用时，Gemini 可能分享聊天以及 Connected Apps、Personal Intelligence、技能、任务、已登录网站中的信息；Google 不控制、不监控第三方 MCP 服务器，数据发出后受对方的隐私做法约束（[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})）。

Mac 上加入「已连接的文件夹」的公共云盘，其中被共享的数据对所有有权访问该云盘的人可见（[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})）。

## 保存与删除

| 操作 | 删除什么 | 不删除什么 | 资料 |
| --- | --- | --- | --- |
| 删除任务线程 | 该任务、Gemini 应用活动记录中的相关活动、关联计划 | 已创建或修改的文件、远程浏览器数据、远程代码执行数据 | [帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}}) |
| 设置中删除浏览器数据、代码执行数据 | 远程浏览器的 Cookie 等登录信息；远程计算机上的数据 | — | [帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}}) |
| 关闭任务模式 | 远程浏览器数据、远程代码执行数据；计划暂停 | 本地 Chrome 浏览数据；已有任务、线程、计划、文件 | [帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}}) |
| 取消或降级订阅 | — | 数据保留；进行中的任务做完，计划暂停 | [帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}}) |
| Mac 文件临时备份 | 开始新查询或任务时，或 24 小时后自动删除 | — | [帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}}) |

远程浏览器数据「为你方便而保存，供后续会话使用」，Gemini 也可能代用户自动删除（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。各类数据的具体保存期限，除 Mac 备份的 24 小时和第三方转述的人工审核 3 年外，资料中没有。相册任务另有「Gemini 应用隐私中心」和「Google 相册中的 Gemini 功能隐私中心」（[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}})），本库没有收这两页。

## 他人信息

资料中没有 Spark 如何处理第三方信息的官方说明，而实测中 Spark 大量使用他人信息：

- The Verge 作者没说名字，Spark 就从邮件里找到妻子的邮箱，后来又直呼作者父母的名字；Spark 还请求访问通讯录，被作者拒绝（[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})、[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})）。
- WIRED 的派对宾客名单把作者同住的男友写成「密友」（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})）。

## 实测者的感受

- WIRED 作者授权 Gmail、Docs、Calendar 后写道「隐私，再见」；Spark 引用的邮件和旅行文档有些连作者自己都不记得，行程里还列出了信用卡后四位（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})）。
- The Verge 作者称看到 Spark 把数据当作需要挖掘的东西而不是需要保护的东西，感到不适，「永远无法摆脱被监视的感觉」，并认为分享多少个人信息与 AI 有多有用直接相关（[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})）。
- The Verge 另一篇的结论是，Spark 未必值得财务成本加隐私代价（[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})）。
- Freistyle AI 建议只用与私人生活无关的账号使用 Tasks，客户个人信息、付款详情、密码、合同都不要放进去（[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。

## 地区与账号

Spark 在支持 Gemini 应用的地区可用，但欧洲经济区、尼日利亚、瑞士和英国除外；只支持个人 Google 账号，工作和学校账号不可用（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。官方没有说明排除这些地区的原因。

## 资料缺口

- Gemini 隐私政策与 Keep Activity 说明的原文：任务数据是否用于训练、人工审核范围、各类数据保存期限。
- 远程浏览器与远程计算机数据的保存期限和自动删除规则。
- 他人信息（联系人、邮件往来对象）的处理规则。
- 排除欧洲经济区、英国等地的原因，是否与监管有关。

## 主要资料

- 官方：[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})（隐私风险、删除）；[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})；[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})；[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})；[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})；[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}})。
- 媒体：[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})、[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})、[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})。
- 社区：[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})（Keep Activity 与训练）；[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})。
