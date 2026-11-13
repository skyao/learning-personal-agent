---
title: "Today AI：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  记忆是 Today 的核心卖点：官方称「活记忆」存为可读、可改、可删的结构化条目，所有交互放在单一长对话里。实测中跨周记忆有效，但也出现归纳不准；团队把长期积累的上下文视为主要壁垒，同时承认它「不是绝对的壁垒」。
---

## 概要

- 官方称 Today 的「活记忆（Living Memory）」是一行行结构化事实（人物、偏好、承诺、项目），用户可查看、修改、删除，删除后立即不再影响建议。多篇实测确认有记忆面板且可编辑。
- 记忆来自两条路径：用户授权的连接器（邮件、日历、飞书、健康数据），以及日常对话。团队称采用渐进式授权，需要时才请求权限。
- 产品只有一个长对话，没有会话列表；团队认为按任务分对话框是上下文能力有限时的妥协，「未来 Agent 就应该是单 session 的形态」。
- 实测有正反两面：二阶变量称数周前提到的考试仍被记得并按时提醒；Founder Park 发现对个人情况的部分归纳不准确，纠错后建议是否跟着变尚未验证。
- 团队把使用中沉淀的上下文（Context lock-in）视为主要壁垒，但承认记忆技术上可导出，「不是绝对的壁垒」。

## 结构化、可编辑的「活记忆」

官方博客称 Today 的记忆存成一行行结构化事实，不是搜不动的聊天记录；用户可用平实语言打开查看，任一行可改、任一条可删，删后立即不再影响建议；记忆限定在用户账户内，每行可审计（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）。官方定义文进一步称，个人智能体应记住稳定事实，「逐字聊天导出不算」，用户删除的事实立即停用（[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})）。

能力页的说法更谨慎：长期记忆在多次对话间延续人物、偏好、项目和目标，可「在产品支持范围内」修正或删除，Memory 不代表永久保存每一项输入，Today 不会记住分享的所有内容（[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})）。

品玩、Founder Park、极客公园的实测都描述了右侧的「记忆」面板，内容可查看、修改、删除（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})、[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})、[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})）。

## 记忆的来源与管理

智能涌现整理的团队自述称，记忆来自两条路径：用户授权连接器（飞书、健康、日历）让 Today 自己了解用户，以及日常对话中积累偏好和关注点（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。品玩写道记忆从邮件、对话和软件行为中持续提取，整理成偏好、关系、承诺和进行中的任务（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。

品玩还记录了团队对记忆管理的说明：记忆至少分三类生命周期（只服务当次交互；有时效、任务结束前必须保留；长期保留的习惯、关系、目标和偏好），通过主动遗忘、压缩和更新管理，规则综合类型、时效、潜在价值、重要程度和用户偏好，细节可逐步降级、需要时再检索（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。这些是团队对记者的口述，官方页面没有展开。

Today Recording 展示了记忆在具体功能中的用法：会议转写交给 Memory 对照已有的项目、团队、决定来读，多场会议挂在同一项目下，以最新确认的决定为当前状态；Memory 只为 Summary 提供理解，不覆盖录音，无法确认的名字保留不确定（[官方：Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})）。

官方称计划探索「家庭共享记忆」（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）；集成页称云连接授权一次即可在所有设备使用（[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})）。

## 单一长对话与「助理人格」

Founder Park 实测国内版：左侧只有一个对话页，看不到会话列表（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。团队自述坚持单 session 单对话框，为此用尽可能小的模型、提高 Context 信息密度、降低延迟、分 Bubble 回复；注册时必须给助手起名（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。晚点称助手有自己的档案页，记录它是谁和每天交流后的记录（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）；极客公园称它每天写日记总结当天对话（[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})）；品玩提到 AI 伙伴可设名字、切换性格、查看日记和亲密度（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。

单一对话也带来门槛。晚点称公测一个月后用户两极分化，有人下载两分钟就卸载，不习惯长对话；团队因此上线 multi-task，把复杂任务移到独立任务里（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。

## 实测：记得住，也会记错

正面案例：

- 二阶变量作者第一天提到要报名金融从业资格考试，数周后公告发出时 Today 仍记得并提醒（[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})）。
- 品玩作者约采访，第二天对方回信后，Today 无需再次指令就接上了之前的任务（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。
- 产品笔记作者让 Today 推荐周末带娃活动，无需说明城市和孩子情况（[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})）。

问题：

- Founder Park 称 Today 对个人情况的部分归纳并不准确，「工作节奏」卡片可能只是有限信息的推断；纠正记忆后建议是否跟着变「还需要更长时间检验」，Agent 越主动，错误记忆的代价越大（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。《生活有变量》引用这一体验，认为记忆和下一次行动能否一起改正，比记住多少更重要（[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})）。
- 二阶变量称 Today 的主要上下文来自协同办公软件，生活类来源有限（QQ 邮箱、微信读书），日常 App 数据难以突破商业壁垒（[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})）。

## 记忆作为壁垒

团队自述称壁垒可能来自使用中沉淀的 Context，记忆技术上可以导出换产品，但摩擦成本高，这种 Context lock-in「不是绝对的壁垒」（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。晚点访谈中受访者称长期使用积累的数据带来的切换成本是主要壁垒，并称个性化是主动化的前提，不是模型天然具备的，需要专门设计和训练（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。

## 资料缺口

- 记忆的存储与检索实现；三类生命周期、主动遗忘规则的官方说明。
- 记忆导出功能是否存在、格式如何。
- 纠错后的建议是否随之改变，缺少较长周期的实测。
- 家庭共享记忆的进展。

## 主要资料

- 官方：[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})（活记忆的设计原则）；[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})（记忆范围的限定说法）；[Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})（记忆用于会议纪要）。
- 媒体：[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})（记忆分层与跟进实测）；[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})（记忆来源、单 session、壁垒）；[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})（个性化、切换成本）；[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})（归纳不准）；[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})（跨周记忆、上下文来源）；[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})。
- 社区：[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})；[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})。
