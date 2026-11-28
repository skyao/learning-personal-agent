---
title: "观察列表：暂未跟踪的 Personal Agent 产品"
linkTitle: "观察列表"
weight: 950
date: 2026-11-09
description: >
  已经注意到、但暂不纳入跟踪的 Personal Agent 产品：来源、简介与值得关注的理由
---

这些产品是 2026-11-09 收集 Poke 时，从 TechCrunch 短信类智能体合集和几次检索中发现的。用户当天决定暂不纳入跟踪，先记在这里观察。2026-11-28 复查过一次，新动态记在各产品的「近况」一条。它们没有建产品目录，也不收资料；以后决定纳入时，按 `skills/collect-sources/references/tracking.md` 的流程新建产品 skill。

简介只复述来源中的说法，官方网站尚未核实。标注「据检索结果」的信息来自检索摘要和二手报道，原文没有直接读取。

## 优先关注

### Underdog

- **厂商**：Conway Research（据检索结果，创始人为 Sigil Wen，a16z 投资）
- **来源**：
  - TechCrunch 短信类智能体合集（2026-10-24），已收入[行业综合](../industry/sources/media/2026-10-24-techcrunch-text-message-agents/)
  - TechCrunch 发布报道（2026-10-06，未直接读取）：[Silicon Valley's AI wunderkind launches Underdog, the most private Instinct/Muse competitor yet](https://techcrunch.com/2026/10/06/silicon-valleys-ai-wunderkind-launches-underdog-the-most-private-instinct-muse-competitor-yet/)
- **简介**：注重隐私的 AI 助手，2026 年 10 月初开始邀请制测试。模型完全在用户设备上运行，个人数据留在用户自己的硬件上。首个版本支持 Mac 和 Windows，计划推出 Linux、iPhone 和 Android 版。初期免费，并声明永远不加广告。据检索结果，收入计划来自助手经 Stripe 代付时的小额抽成。
- **值得关注的理由**：已跟踪的产品都在云端运行，Underdog 是唯一走本地运行路线的。它可以和 Muse 的云端 VM、dots 的云端电脑对照，看「运行环境」和「隐私」两方面的另一种设计。

### Wajo（Fo）

- **厂商**：Wajo
- **来源**：
  - TechCrunch 短信类智能体合集（2026-10-24），已收入[行业综合](../industry/sources/media/2026-10-24-techcrunch-text-message-agents/)
  - 官网：[wajo.ai](https://wajo.ai/join-wajo)
- **简介**：Wajo 的第一款消费级智能体 Fo，能打电话给商家、发邮件、加入群聊、预订和购买，并与人协调完成日常事务。Fo 有自己的身份：独立的邮箱地址、电话号码和支付卡，与商家打交道时不需要用户交出自己的凭证。遇到自己处理不了的事，可以引入真人助理完成。2026 年 9 月公开上线，有免费档，更重的工作量和自定义智能体在付费的 Pro 档。
- **值得关注的理由**：「智能体自己的身份 + 支付卡」直接对应笔记关注的用户控制：凭证、支付、对外通信。Muse Mail、Grok Bot 的 Bot 邮箱只解决了邮箱这一项，Wajo 把电话和支付也独立出来了。

### Tab

- **厂商**：Tab（据检索结果，创始人为 Brennan Erbz、Stafford Schlitt、Ammar Amdani）
- **来源**：
  - TechCrunch 短信类智能体合集（2026-10-24），已收入[行业综合](../industry/sources/media/2026-10-24-techcrunch-text-message-agents/)
  - TechCrunch 发布报道（2026-10-07，未直接读取）：[Another personal AI assistant has launched: meet Tab, which emerged from stealth with a $300M valuation](https://techcrunch.com/2026/10/07/another-personal-ai-assistant-has-launched-meet-tab-which-emerged-from-stealth-with-a-300m-valuation/)
- **简介**：用户通过 iMessage 或 WhatsApp 把日常事务交给 Tab，从订购杂货到挑生日礼物，由它代为处理。2026 年 10 月初结束隐身状态，估值 3 亿美元，投资方包括 SV Angel、Valar Ventures、American Spirit。据检索结果，目前仍是排队进入的私测。
- **值得关注的理由**：形态与 Poke、Instinct 接近，都是没有独立 App、住在消息应用里的智能体，可以作为同类对照。等它开放使用、有更多一手资料后再评估。

## 其次关注

### 腾讯 LightVela

- **厂商**：腾讯
- **来源**：
  - 特工宇宙《腾讯悄咪咪上线了个国产版 Muse》（人人都是产品经理，2026-09-28）：[woshipm.com/ai/6471130.html](https://www.woshipm.com/ai/6471130.html)
  - 雷科技《腾讯版Muse？LightVela新版实测：越来越像个人Agent，但还不够完美》（36氪经授权发布，2026-11-18）：[36kr.com/p/4073960952141449](https://eu.36kr.com/zh/p/4073960952141449)
- **简介**：把开源智能体 Hermes Agent 托管到云端：在云端为用户开一个专属的 Hermes Agent 实例，用户在网页面板上配置模型、通道和技能，之后在微信、QQ、飞书里直接对话，不需要服务器和代码。底层框架开源，可以接入各家厂商的模型。文章称它 2026 年 4 月上线，是腾讯在 OpenClaw 一键部署模板（2026-01）、Qclaw（2026-04）之后的延续；启航 AI 版新用户可免费体验一个月，赠 4500 积分。
- **值得关注的理由**：国内少见的、接入微信等国内渠道的云端个人智能体。不过它属于「开源 Agent 的云端托管版」，与 2026-11-06 判定不收的 OpenClaw 及云端托管版同类，纳入前要先看这一决定是否适用。
- **近况**（2026-11-28 复查）：雷科技 11-18 的实测称，LightVela 2026 年 4 月开启公测、9 月底面向所有用户开放；过去两个月的升级包括可创建多个各有人设、长期记忆和技能的助手，10 月加入云电脑，另有「我的工作台 Beta」。主要交互界面是网页，没有桌面客户端或手机 App，支持微信、飞书、钉钉、QQ；技能接入 SkillHub，连接器有腾讯会议、飞书、钉钉、腾讯文档、腾讯自选股、ima 共 6 个。实测中云端浏览器截图、网站上线等任务未能完成。作者的结论是「越来越像Personal Agent了」，但只想交代一句话等结果的用户，「LightVela这次的体验确实不足以让我放心推荐」。未见腾讯官方公告。

### Martin

- **厂商**：Martin
- **来源**：
  - TechCrunch 短信类智能体合集（2026-10-24），已收入[行业综合](../industry/sources/media/2026-10-24-techcrunch-text-message-agents/)
  - 官网：[trymartin.com](https://www.trymartin.com)
- **简介**：通用个人助理，可以通过短信、电话、WhatsApp、邮件、Slack 和自己的 iOS App 联系。能管理日历、邮件、提醒、任务、笔记和通信，也能代用户发消息、打电话，每天给出需要关注事项的摘要。订阅价格从每月 21 美元起。
- **值得关注的理由**：比 2026 年这一批新产品出现得早，渠道最多（短信、电话、WhatsApp、邮件、Slack、App 并存），可以看早期个人助理怎样演变成今天的形态。

### Town

- **厂商**：Town
- **来源**：
  - TechCrunch 短信类智能体合集（2026-10-24），已收入[行业综合](../industry/sources/media/2026-10-24-techcrunch-text-message-agents/)
  - 官网：[town.com](https://www.town.com)
  - 官方新闻稿《Town Raises $108M at a $1B Valuation to Bring AI Assistants to Whole Teams》（2026-10-19）：[town.com/press/series-b](https://www.town.com/press/series-b)
- **简介**：面向职业场景，给每个用户一个「Townie」助手，学习用户的工作方式，处理重复的职业事务，可接入邮件、日历、文档、Slack 等平台。2026 年 6 月完成 5500 万美元 A 轮融资，由 Andreessen Horowitz 和 Forerunner 领投。
- **值得关注的理由**：个人工作也在 Personal Agent 的范围内。Town 只做职业场景，可以和 Microsoft Autopilot、WorkBuddy 这类厂商级工作智能体对照。
- **近况**（2026-11-28 复查）：官方新闻稿称，Town 2026-10-19 宣布 1.08 亿美元 B 轮融资，估值 10 亿美元，由 Forerunner Ventures 和 Menlo Ventures 共同领投，a16z、First Round Capital 继续跟投。Townie 可以和团队里其他人的 Townie 协作，也能通过邮件和短信与公司外的客户、合作方、候选人打交道；默认不用客户接入的数据训练模型，不绑定单一模型厂商。新闻稿称 Town 2026 年 6 月公开上线、几周内 ARR 达到七位数，7 月以来付费客户增长 4 倍。新闻稿没有提价格。
