---
title: "Gemini Spark：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Spark 没有独立应用，只是 Gemini 应用（手机、网页、Mac）里的一种模式；10 月起从独立空间并入主界面，改名为 Task。它不用自己的号码或邮箱，对外以用户的 Gmail 发信。
---

## 概要

- Spark 只能在 Gemini 应用里用：Gemini 移动应用（Android 和 iPhone）、Mac 版 Gemini 应用、gemini.google.com 网页版。没有独立应用，也不接短信、iMessage、WhatsApp。
- Beta 阶段它是 Gemini 里的一个独立空间（「Switch to Spark」）；2026-10 起改成输入框旁的「Chat / Task」切换，聊天和任务共用一条历史，Spark 这个名字从界面上消失。官方没有发公告，帮助页称改名是因为用户总在说「任务」。
- 对外沟通用的是用户自己的账号：以用户的 Gmail 起草和发送邮件、发日历邀请，发送前要用户确认措辞。I/O 时预告的「给 Spark 发短信和电子邮件」，截至 2026-11-10 的资料里没有看到落地。
- 手机通知在需要用户输入时发出；用户正在网页上看同一个任务时不推手机。

## 只在 Gemini 应用里

帮助页写明任务只在 Gemini 移动应用、Mac 版 Gemini 应用和网页版可用，在 iPhone 上也能用（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。WIRED 在 Beta 首周的描述是：Spark 是 Gemini 聊天机器人里的一个新标签页，可以从手机和电脑控制，「你不需要 Android 手机；它在 iPhone 上也能用」（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})）。

第三方比较中，WIRED 把 Spark 称为「Gemini 应用内的 beta 版」，与有独立应用的 Grok Bot、Claude Duet 和通过短信工作的 Instinct 对照（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）；Top5Apps 同样强调它在 Gemini 应用内、没有独立应用（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。iThome 列出的触发方式是文字、语音、排程和背景任务（[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

## 2026-10：从独立空间并入主界面

| 日期 | 观察到的变化 | 资料 |
| --- | --- | --- |
| 2026-10-01 前后 | 网页版服务器端改版：侧栏的「Switch to Spark」独立空间去掉，提示框下方改为 Chat / Task 切换，任务线程与对话合并到同一个侧栏，新增「Scheduled」区域；Google 没有发布官方博客 | [Chrome Unboxed]({{< relref "/docs/gemini-spark/sources/media/2026-10-01-chromeunboxed-ditching-spark-brand" >}}) |
| 2026-10-12 | Android 版改版：输入框上方新增 Chat / Task 按钮，导航抽屉中的 Spark 消失，聊天和任务合并为同一历史（可按全部、就绪、需要关注、进行中筛选）；账号菜单「Gemini Spark Settings」改名「Task settings」；Google 在界面上称之为「Spark 的新家」；9to5Google 称当时在 iOS 和网页版还没看到 | [9to5Google]({{< relref "/docs/gemini-spark/sources/media/2026-10-12-9to5google-task-redesign" >}}) |
| 截至 2026-11-10 | 帮助页称 2026-10 Spark 改名为 Task，用词改为 tasks / task mode；在文本框下方用「任务」切换启动 | [帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[帮助：Gemini 模型]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-gemini-models" >}}) |

两篇媒体报道对网页版是否已改版的说法不一致：Chrome Unboxed 10 月 1 日前后就在网页版看到了，9to5Google 10 月 12 日称网页版还没有。两者都是服务器端推送的界面观察，可能是灰度不同。

帮助页给出的改名理由是：自 5 月起与订阅用户测试 Spark Beta，用户希望 Gemini 直接把「任务」做完，这个词不断出现，「所以我们将其更名为 Task」；现有任务和计划都保留（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。Chrome Unboxed 和 9to5Google 都认为这是在淡化 Spark 品牌，9to5Google 称「由于体验不再孤立，开始任务变得快得多」（[Chrome Unboxed]({{< relref "/docs/gemini-spark/sources/media/2026-10-01-chromeunboxed-ditching-spark-brand" >}})、[9to5Google]({{< relref "/docs/gemini-spark/sources/media/2026-10-12-9to5google-task-redesign" >}})）。

## 对外以用户的身份沟通

Spark 没有自己的邮箱或号码。实测中它通过用户的 Gmail 起草、发送邮件，WIRED 作者确认措辞后，Spark 自动把邮件发了出去（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})）；The Verge 作者让它找到妻子的邮箱并附上文档发信（[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})）。发送通信属于每次都要确认的操作（详见[安全]({{< relref "/docs/gemini-spark/analysis/security" >}})）。鸿煊把这种做法归类为「Gemini 产品内身份」，与给智能体发独立邮箱、电话号码的 Manus Cue 等产品对照（[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。

I/O 发布稿预告 Spark 将能「给 Spark 发短信和电子邮件」（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})），截至 2026-11-10 的帮助页和更新日志里没有这一功能。

## 通知与上手引导

- 7 月 13 日起，需要用户输入时的通知更详细；用户正在网页版看该任务线程时，不发手机通知（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})）。
- 7 月 17 日起，在任务里输入「set up」「get started」或「interview me」，Spark 会帮用户设置首批技能和任务（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})、[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。

## 资料缺口

- I/O 预告的短信、邮件入口是否上线或已取消。
- 语音入口（Gemini Live）与任务的关系；帮助页只提到可以在 Live 对话中创建计划。
- iOS 与网页版完成改版的时间。

## 主要资料

- 官方：[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})（入口与改名理由）；[帮助：Gemini 模型]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-gemini-models" >}})；[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})（短信与邮件预告）；[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})（通知、上手引导）。
- 媒体：[Chrome Unboxed]({{< relref "/docs/gemini-spark/sources/media/2026-10-01-chromeunboxed-ditching-spark-brand" >}})、[9to5Google]({{< relref "/docs/gemini-spark/sources/media/2026-10-12-9to5google-task-redesign" >}})（改版观察）；[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})、[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})；[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})；[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 社区：[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})；[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})。
