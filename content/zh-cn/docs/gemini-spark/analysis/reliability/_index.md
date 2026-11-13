---
title: "Gemini Spark：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Spark 在 Google 生态内的信息整理（收件箱、周报、行程规划）上表现好，在外部网站上的动作（订餐、订房、订座）和常识判断上频繁失败；各测评对它的排名从并列第一到中下游不等。
---

## 概要

- 强项是 Google 生态里的读和写：AI Agents Library 的对照测试中，Spark 赢下收件箱分拣、周度商务简报和会后跟进，十项均分 8.7，与 Dots 的 8.8 接近；The Verge 称它给出了「最详细、最个性化」的旅行行程。
- 弱项是外部网站上的动作和常识：订寿司店、订 Airbnb 都没成；WIRED 的午餐订单只给老板点了一个春卷；日程冲突没指出来；把同住男友当成「密友」；邮件语气像业务同事。
- 研究和后台工作偏「交卷快」：WIRED 要求研究 30 分钟，Spark 几分钟就给了结果。
- 排名差异很大：AI Agents Library 中与 Dots 几乎持平；Top5Apps 排第 4（4.2 分）；Enterpret 用户讨论统计排 12 款中第 8，「完成任务」一项排第 10；WIRED 六款同测中 Spark 没有获得任何单项奖。
- 已知的系统性故障只有一次：2026-10-13 至 10-16 表格写入被策略检查拦截。官方没有公布完成率、出错率或可用性数据。

## 实测一览

| 测试 | 时间与条件 | 结果 | 资料 |
| --- | --- | --- | --- |
| WIRED 上手 | 2026-05 Beta 首周，授权 Gmail、Docs、Calendar | 五页派对行程细致到信用卡后四位；男友被列为「密友」、作者本人不在宾客名单；订寿司店触发验证码后失败；邮件语气需改写 | [WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}}) |
| The Verge 上手 | 2026-06-01，AI Ultra | 生日日历、Taskmaster 邮件、学前清单基本完成但有瑕疵；街区派对任务不顺，邮件提到不存在的报名表，演示文稿难看；Doc 无法共享给妻子 | [The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}}) |
| The Verge 旅行规划 | 2026-06-02 | 几分钟生成「最详细、最个性化」的周末行程；唯一失败是预订 Airbnb | [The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}}) |
| AI Agents Library | 2026-08 测试，个人 Google 账号；与 Dots、Muse 对照，每项 10 分 | 十项均分 8.7（Dots 8.8）；六项重叠任务均分 8.50（Dots 9.08、Muse 7.75），去掉做网页后 9.00 略高于 Dots 的 8.94 | [AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}}) |
| WIRED 六款同测 | 2026-10-27 刊出，一天内测五项，只共享 Gmail 和 Calendar | 晨间选题 5/5、午餐 1/5、日程冲突 1/5、度假行程 3/5、失眠检查 2/5；综合最佳为 Dots | [WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}}) |
| Top5Apps | 2026-11 评测（初版 2026-09-19） | 4.2 分，排第 4；未给 Spark 的逐项分数 | [Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) |
| Enterpret Feedback Bench | 2026-08-31 至 11-01 的用户帖子统计，Spark 2,960 名发帖用户 | 44.2 分，12 款中第 8；「完成任务」一项排第 10 | [Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}}) |

## 做得好的：Google 生态内的整理和起草

AI Agents Library 的六项重叠任务中，Spark 的得分是会议准备 8.5、收件箱分拣 8.5、竞品与动态调研 9.0、制作网页 6.0、周度商务简报 9.5、内容计划 9.5；它在会后跟进上以 9.5 对 7.0 胜过 Dots，电子表格任务得 8.5（[AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})）。作者的结论是 Spark 在工作位于 Google Workspace 时最强，Dots 擅长交付成品，「区分它们的是形态，而不是质量」；作者也提醒三款在收件箱分拣上准确性都不够——能看到消息存在，却不知道事情是否仍成立。

The Verge 的旅行规划中，Spark 用上了驾车路线、宠物、孩子年龄、家人饮食禁忌和已买的演唱会票（[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})）；WIRED 六款同测中，Spark 的晨间选题得了唯一的 5/5，WIRED 称它给出了「最好的角度」（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

## 做不好的：外部动作与常识

- **外部网站**：订寿司店触发发到作者手机的六位验证码，最终作者打电话订位（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})）；订 Airbnb 被网站的安全和认证政策挡住（[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})）；午餐订单只给老板加了一个春卷，是该项「唯一真正失败」的一款（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。
- **常识与关系**：宾客名单把同住男友写成「密友和经常同行的伙伴」，WIRED 的结论是智能体技术上聪明却「仍然缺乏任何常识」（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})）；失眠检查中评论作者「早上日历空着」，被认为不相干（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。
- **语气**：给妻子的邮件像发给业务同事（[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})）；WIRED 的邮件也要改写（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})）。
- **编造与遗漏**：邮件提到不存在的共享报名表、日历链接指向预告片而不是正片、漏了妻子的邮箱（[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})）。
- **成品**：制作网页是 Spark 在 AI Agents Library 中最弱的一项（6.0）（[AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})）。

The Verge 作者还提到，多步骤任务约 4 分钟完成，但自己一直盯着它，质疑「每一步都要你微观管理」的价值（[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})）。

## 测评之间的分歧

同一时期的测评对 Spark 的相对位置差异很大：AI Agents Library 中 Spark 与 Dots 几乎持平；WIRED 认为 Dots 综合最好、Spark 多数任务落后；Enterpret 的用户讨论统计里 Spark（第 8）反而高于 Dots（第 12）（[AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})、[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})、[Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})）。

口径差异可以部分解释这些分歧：

- AI Agents Library 测的是工作类任务，三款产品测试时间和套餐不同（Spark 在 2026-08，早于 Task 改版），作者自称「不是受控的实验室实验」。
- WIRED 偏生活类任务，只测一天、只共享了 Gmail 和 Calendar。
- Enterpret 是用户帖子的统计，Spark 只有 2,960 名发帖用户、声量份额 1.6%；Enterpret 称用户对 Spark 的评价「高于 ChatGPT Dots」，Spark「更受喜爱，讨论更少」，但「它的弱点恰是最重要的方面」，即完成任务。统计期跨越改名前后，帖子可能混入 Gemini 普通聊天的讨论。Enterpret 本身是做反馈分析工具的厂商。

推断：几份测评一致的地方是——Spark 在用户自己的 Google 数据上整理、起草做得好，一旦要在 Google 之外的网站完成动作就容易失败。排名差异主要取决于测评偏工作还是偏生活。

## 故障与官方说法

- 2026-10-13 起多名用户报告 Spark 写入 Google 表格失败，10-16 楼主回报后端回归已修复；楼主建议增加会话内自动遥测与一键上报（[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})，详见[连接器]({{< relref "/docs/gemini-spark/analysis/connectors" >}})）。
- 官方帮助页自述「Gemini 仍在学习，可能会犯错」，监控不适合追踪变化很快的数据，计划运行时间只是大致的（[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})、[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})）。

## 资料缺口

- 官方的完成率、出错率、可用性数据或状态页。
- 改用 3.7 Flash（8 月）、推出 Argon（10 月）、Chrome 自动浏览（7 月）之后的独立实测；本库的深度实测多在 5–8 月。
- 计划和话题监控的长期使用实测。
- 用户自己的实测（`exploration/` 为空）。

## 主要资料

- 官方：[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})、[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})（官方自述的局限）。
- 媒体：[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})、[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})、[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})（早期实测）；[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})。
- 社区：[AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})；[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})；[Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})；[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})。
