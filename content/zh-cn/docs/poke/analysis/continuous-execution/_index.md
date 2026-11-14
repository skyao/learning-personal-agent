---
title: "Poke：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-09
description: >
  「先发消息、会跟进」是 Poke 的核心卖点：它留意已连接账户中的信号主动提醒，用户用纯文本建自动化，外部服务经 API 推事件触发；后台实时自动化和主动更新只在 Pro 及以上提供，频繁运行的自动化是用量的主要来源。
---

## 概要

- 主动性是 Poke 定位的一部分：Cognition 称它「会先给你发消息，会跟进你」，新闻稿称它留意未付发票、航班变更、续费通知、改期请求等信号并主动回应。
- 三类触发：账户中的信号（邮件、日历等）、用户用自然语言创建的定时或重复自动化、外部服务经入站 API 推送的事件。
- 主动能力按档位收费：价格页把「主动更新」和「后台实时自动化」列为 Pro 起才有，Ultra 的自动化频率限制最高。
- 成本集中在这里：创始人称真正花钱的是实时推理（如对每封来信都跑的自动化），官方也称高用量通常来自运行很频繁的自动化。
- 唯一的独立实测（Unite.AI）认为主动提醒有用，但邮件分拣不够敏锐，可能埋没紧急邮件、转发琐碎内容。

## 三种触发方式

**账户中的信号。** 新闻稿称 Poke 住在消息应用中，「留意已连接账户中的可行动信号」，如未付发票、航班变更、续费通知、改期请求，以简洁的消息回应（[发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}})）。官网首页称它会自动使用已集成的服务及其记忆，在恰当的时候提供帮助，并能创建提醒、提前着手任务（[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}})）。Unite.AI 实测称它不等提示就能根据连接的数据呈现到期账单、日程冲突等更新（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。

**用户建的自动化。** TechCrunch 04-08 写道，用户可以用纯文本编写自己的自动化，例如每日用药提醒、每天告知是否需要带伞，并分享给朋友（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）；分享的载体是 Recipe（见[连接器]({{< relref "/docs/poke/analysis/connectors" >}})）。Unite.AI 设置了每周日晚间汇总下一周的自动化（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。发布说明 2025-12-01 称 Poke 会提醒用户检查尚未执行的重复自动化，并能创建和管理重复日历事件（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）；2026-01-12 推出第一方 TripIt 自动化（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）。

**外部事件。** 入站 API 让任何能发 webhook 的服务触发 Poke，文档举例有 GitHub Action 部署失败告警、CI/CD、监控、Typeform 提交、CRM 事件和定时任务（[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})）。API 有频率限制但文档未给数值，建议合并请求、在自动化消息间加延迟、为不同自动化建不同的 key（[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})）。

## 主动能力按档位收费

| 档位 | 与持续执行相关的内容 | 资料 |
| --- | --- | --- |
| Free | 无主动更新、无后台实时自动化 | [价格页]({{< relref "/docs/poke/sources/official/2026-11-09-pricing" >}}) |
| Pro（19 美元/月） | 主动更新、后台运行的实时自动化、更高频率限制；额度用尽后最耗资源的工作等到重置 | [价格页]({{< relref "/docs/poke/sources/official/2026-11-09-pricing" >}})、[文档：Usage & Resets]({{< relref "/docs/poke/sources/official/2026-11-09-docs-usage-and-resets" >}}) |
| Ultra（199 美元/月） | 自动化频率限制最高；积分用完可降为 Pro 体验或按量付费 | [价格页]({{< relref "/docs/poke/sources/official/2026-11-09-pricing" >}})、[文档：Usage & Resets]({{< relref "/docs/poke/sources/official/2026-11-09-docs-usage-and-resets" >}}) |

截至 2026-11-09 的价格页同时写「每个方案都能用上 Poke 的全部功能」（[价格页]({{< relref "/docs/poke/sources/official/2026-11-09-pricing" >}})），与 Free 没有主动更新的对比表并存。

官方用量文档称，高用量通常由运行非常频繁的自动化造成，建议让 Poke 检查并精简最频繁的那些（[文档：Usage & Resets]({{< relref "/docs/poke/sources/official/2026-11-09-docs-usage-and-resets" >}})）。von Hagen 对 TechCrunch 说，真正让 Poke 花钱的是实时推理，如对每封来信都运行的自动化、实时航班值机，不需要实时数据的请求大概可以免费使用（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）。

推断：Poke 把「主动」拆成了两层，基于对话的提醒和定时任务各档都可用，而持续监听账户、实时响应的后台自动化才收费。这一划分与创始人对成本来源的说法一致。

## 主动性的边界

资料没有说明 Poke 如何控制主动发消息的频率，用户能否调低或关闭主动更新。Unite.AI 的实测结论是邮件分拣「还不够敏锐」，可能把紧急邮件埋没却转发琐碎内容（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。潮涌AI把「主动化」列为其筛选的 15 家创业公司的共识，称 Poke「会主动发消息追问进度」（[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})）。

## 资料缺口

- 自动化的数量上限、最短间隔、单次运行时长；Free、Pro 各自的额度数值。
- 主动消息的频率控制与关闭方式；用户如何查看、暂停、删除已有自动化。
- 自动化失败时的通知与重试机制。
- 长期使用（数周以上）中自动化是否按时执行的独立记录。

## 主要资料

- 官方：[发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}})、[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}})（主动提醒的主张）、[价格页]({{< relref "/docs/poke/sources/official/2026-11-09-pricing" >}})、[文档：Usage & Resets]({{< relref "/docs/poke/sources/official/2026-11-09-docs-usage-and-resets" >}})（档位与用量）、[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})（事件触发）、[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})（自动化相关更新）、[Cognition 公告]({{< relref "/docs/poke/sources/official/2026-07-23-cognition-welcoming-interaction" >}})
- 媒体：[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})（纯文本自动化、成本来源）、[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})（实测）
- 社区：[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})
