---
title: "Poke：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-09
description: >
  资料库中只有 Unite.AI 一份独立评测：设置快、无需 App、能主动提醒，适合轻量任务；但邮件分拣不够敏锐，产品「仍偶尔不可靠」。官方发布说明记录了时区错误、收不到回复、集成断开等问题的修复，没有任何完成率数据。
---

## 概要

- 唯一的独立评测（Unite.AI，2026-09-09）认为 Poke 适合轻量的任务自动化，通用推理、编程和研究深度不及 ChatGPT。
- 能做的：总结未读邮件、生成每周摘要、设置自动化、接受语音备忘、主动呈现账单与日程冲突。问题：邮件分拣可能埋没紧急邮件；只支持 Gmail、Outlook；「仍偶尔不可靠」。
- 官方发布说明列出的已修复问题集中在日历时区、邮件（抄送丢失、搜索超时）、集成断开和回复送达。2026-03-19 起发布说明只记重大更新，之后的小修复不再可见。
- 没有任务完成率、出错率或可用性数据；官方提供 status.poke.com 状态页，资料未收其内容。
- 社区讨论体量小：Enterpret Feedback Bench 中 Poke 排第 11（得分 38.8，声量份额 0.2%）；官网首页的好评推文是官方精选，不作为独立证据。

## 唯一的独立评测

Unite.AI 2026-09-09 的评测完成了总结未读邮件、生成每周摘要、设置每周日晚间汇总下一周的自动化、发送语音备忘、浏览 Recipe 等任务；优点是设置不到两分钟、无需安装 App、能不等提示主动呈现到期账单和日程冲突（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。

列出的缺点（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）：

- 邮件分拣还不够敏锐，可能把紧急邮件埋没，却转发琐碎内容。
- 邮件只支持 Gmail 和 Outlook，iCloud、Yahoo 和 Google Workspace 不受支持。
- 一个账户不能管理多个手机号。
- 对一个「仍偶尔不可靠」的产品，Ultra 档价格偏高。

与其他助手的比较：Poke 安静住在短信里、会主动提醒，ChatGPT、Claude 是需要主动打开的工作区；Poke 为「轻量任务自动化而非重度知识工作」而打造；Gemini 深度绑定 Google 生态，工具分散在 Google 之外时选 Poke（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。

评测称过去的时区和日期错误、提醒偶尔迟发「已经解决」，依据是官方发布说明（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。这一结论引自厂商，不是评测自己的长期观察。评测页面有联盟链接披露。

## 发布说明中的已修复问题

官方发布说明在 2025-11 至 2026-02 记录了较多修复（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）：

| 类别 | 问题 |
| --- | --- |
| 日历 | 日历事件时区错误（2025-12-01、2026-02-02 两次） |
| 邮件 | 抄送收件人被丢弃；邮件搜索超时；起草邮件时陷入反复批准循环；占位邮箱地址；重复的入门邮件 |
| 集成 | Todoist 集成意外断开（2026-01-12）；Outlook 订阅同步失败（2026-02-02） |
| 送达 | 部分用户收不到 Poke 的回复；被意外退回 bouncer 模式 |

2026-03-19 起发布说明改为只记录重大更新（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})），所以此后的问题与修复在资料中看不到。官方文档页首写「和我们人类一样，Poke 有时也会犯错」，并给出 status.poke.com 状态页（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）。Cognition 称加入后其模型和基础设施会让 Poke「更快、更可靠」（[Cognition 公告]({{< relref "/docs/poke/sources/official/2026-07-23-cognition-welcoming-interaction" >}})）。

## 社区反馈与宣传材料

Enterpret 的 Feedback Bench 1.1 统计 2026-08-31 至 11-01 的用户发帖，Poke 排第 11，得分 38.8，声量份额 0.2%，用户好感 0.490；Muse 第 1（73.4），ChatGPT Dots 第 12（38.5）。帖子少的产品分数会被拉向常态值（[Enterpret Feedback Bench]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})），Poke 的样本很小，排名参考价值有限。

官网首页的社区推文称 Poke 是「终身订阅」「最好的一版 AI 助手」，有用户称「对 99% 的人来说 Poke 比 OpenClaw 更好」（[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}})）。这些是官方挑选的宣传，不当作独立评价。

## 资料缺口

- 第二份独立实测；用户自己的实测（`exploration/` 为空）；数周以上的长期使用记录。
- 任何口径的任务完成率、出错率；状态页的历史可用性。
- 2026-03-19 以后的问题记录；Poke Human 真人任务的完成情况。
- Product Hunt 上的一周评测（收集时原站与 Wayback 都取不到）。

## 主要资料

- 媒体：[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})（唯一的独立评测）
- 官方：[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})（已修复问题、免责声明）、[Cognition 公告]({{< relref "/docs/poke/sources/official/2026-07-23-cognition-welcoming-interaction" >}})、[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}})（精选推文）
- 社区：[Enterpret Feedback Bench]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})（社区声量与好感）
