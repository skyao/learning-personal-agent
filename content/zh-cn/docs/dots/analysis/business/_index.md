---
title: "OpenAI Dots：商业与规模"
linkTitle: "商业与规模"
weight: 110
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  dots 目前靠捆绑进高价订阅和企业版变现，没有交易抽佣或广告；官方没有公布用户数，唯一的规模数字是高管所说的「100 万个 dots 在运行」，而社交平台情绪统计显示用户好感在同类产品中最低。
---

## 概要

- 商业模式是订阅捆绑：dots 不单独收费，放在 100 美元起的 Pro 和 Business Premium 里，企业版 2026-11-18 起计费；另有面向企业职能的「专职 dots」试点和与微软 Agent 365 的集成。
- 规模：官方资料没有用户数、收入或付费数据。据二手转述，OpenAI 高管 Thibault Sottiaux 在 2026-10-11 称已有 100 万个 dots 在运行，这是智能体数量，不是独立用户数。
- 口碑：Enterpret 对 27.7 万条公开帖子的统计显示，Dots 上线五周的发帖用户约为 Gemini Spark 的四倍，但用户好感在 12 款产品中最低。
- 成本是公认的约束：Altman 称 dots「要消耗大量算力」；行业估算个人智能体的运行成本远高于聊天产品，但没有 dots 专项的单位经济数据。
- 战略上，社区分析认为 OpenAI 做 dots 是为了守住 ChatGPT 的用户入口，同时争夺工作场景。

## 订阅捆绑，企业版另计

发布稿写明第一个 dot 包含在 Pro 或 Business Premium 中，不额外收费；企业方向是「从有针对性的企业试点开始」的专职 dots，承担采购、发票、邮件营销、客户支持、商务合同等职责，并与微软合作接入 Agent 365 的企业治理和安全控制（[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})）。企业版 2026-11-18 起计费，管理员暂停 dot 时停止计费，说明企业侧按 dot 计费（[管理员指南]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-admin-guide" >}})），单价资料中没有。价格细节见[开放与价格]({{< relref "/docs/dots/analysis/access-pricing" >}})。

媒体和分析把这一模式与其他厂商对照：InfoQ 总结的路径是 Muse 走交易分成和广告、Instinct 暂不收费、Dots「与现有订阅体系结合，并开始面向企业推进专业 Agent 的试点」（[InfoQ]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})）。中金认为平台型助手（包括 Dots）可以复用既有的分发渠道和付费体系加快变现（[中金研报]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})）。多略的分析指出，用户从 20 美元的 Plus 升到 100 美元的 Pro，同一用户的月收入变为 5 倍（[多略：生意本质]({{< relref "/docs/industry/sources/community/2026-11-08-duolue-business-essence" >}})）。

资料中没有 dots 做交易抽佣或广告的信息。交易场景出现过一次：酒店集团温德姆 CEO 在三季度财报电话会上点名 Meta Muse、OpenAI Dots 等智能体可以代旅客搜索和预订（[Skift：温德姆]({{< relref "/docs/industry/sources/media/2026-10-22-skift-wyndham-ai-booking-agents" >}})）；同期也有亚马逊等平台拦截智能体的报道（见[连接器]({{< relref "/docs/dots/analysis/connectors" >}})）。

## 规模：只有零散的口径

| 数字 | 口径与出处 | 资料 |
| --- | --- | --- |
| 100 万个 dots 在运行 | OpenAI 高管 Thibault Sottiaux，2026-10-11；智能体数量，不是独立用户数；二手转述，一手出处未收录 | [黑咖啡：全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}}) |
| 上线五周 13,279 名发帖用户 | Enterpret 统计 2026-08-31 至 11-01 的 Reddit、X、YouTube、应用商店公开帖子；约为 Gemini Spark（2,960）的四倍 | [Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}}) |

同一份 Enterpret 统计中，Dots 的 Feedback Bench 得分 38.5，12 款中第 12，用户好感 0.372 最低；在直接比较的帖子里，77% 选 Muse 而非 Dots，69% 选 Grok Bot 而非 Dots。其方法是用模型标注公开帖子，反映的是社交平台上的讨论，不是使用数据。

作为参照，Meta 称 Muse 在美加已有超过 1000 万人设置（各资料的时点和口径不一，见 Muse 的分析），这类数字 OpenAI 没有公布。CNBC 的受访者指出，下载和设置不等于已成为日常习惯（[CNBC：OpenAI 跟随 Meta]({{< relref "/docs/industry/sources/media/2026-09-30-cnbc-openai-follows-meta" >}})）。

## 成本：贵在全天候运行

Altman 在 DevDay 上说 dots 是一款高端产品，「它要消耗大量算力」（[Wired：个人智能体之战]({{< relref "/docs/industry/sources/media/2026-09-30-wired-battle-personal-agent" >}})）。行业估算（均非 dots 专项）：甲子光年转引巴克莱的估算，免费个人智能体的运行成本约为免费 ChatGPT 的 10 倍，转引 a16z 的估算，充分使用的个人智能体每用户每天成本可能高达 20 美元（[甲子光年]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）；中金以 Muse 为基准测算，重度用户每月的硬件成本约 71.5 美元（[中金研报]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})）。AI 新榜的文章转述竞争对手员工嘲讽 OpenAI 缺算力，并推测 OpenAI 谨慎开放与算力有限有关（[AI 新榜：普通人需要吗]({{< relref "/docs/industry/sources/media/2026-10-12-aixinbang-do-people-need" >}})），这是记者的推测。

推断：100 美元的门槛、首月之后迟迟未公布的用量条款、企业版按 dot 计费，都与「每个 dot 一台常驻云端计算机」的成本结构一致。dots 要像 Altman 所说走向大众，需要大幅降低单位成本，资料中没有 OpenAI 在这方面的具体说法。

## 为什么做：守入口，也争工作场景

发布当天，Altman 称使用 dot 后「我终于找回了一些注意力」，CFO Sarah Friar 称 dots 是「可以拍拍你肩膀的智能体」（[CNBC DevDay]({{< relref "/docs/dots/sources/media/2026-09-29-cnbc-devday-dots" >}})）。CNBC 指出 dots 在 Muse 发布三周后入场，同类创业公司 CEO 认为这「继续验证了这一品类」（[CNBC：OpenAI 跟随 Meta]({{< relref "/docs/industry/sources/media/2026-09-30-cnbc-openai-follows-meta" >}})）。

社区与媒体的分析有两种解读：一是防御，若用户都在 Muse 这类应用里调用模型，模型厂商就只收算力费，推出个人智能体是为了避免「退化为后台供应商」（[AIX 财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）；二是扩张，Dots「不仅想做 personal agent，同样想做最好的 work agent」，依托 ChatGPT 的用户关系、插件生态和 Codex（[明义：产业链]({{< relref "/docs/industry/sources/community/2026-10-31-mingyi-personal-agent-industry-chain" >}})）。Wired 问及 dots 与传闻硬件的关系，Altman 拒绝回答。

## 资料缺口

- dots 的用户数、活跃度、付费转化和收入；「100 万个 dots」的一手出处。
- dots 的单位成本和毛利。
- 专职 dots 的试点客户、企业单价、Agent 365 集成进度。
- 是否会引入交易抽佣或广告。
- CNBC DevDay 直播稿中关于 IPO 和融资的内容（本库只收了与 dots 相关的两条）。

## 主要资料

- 官方：[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})（捆绑与企业试点）；[管理员指南]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-admin-guide" >}})（企业计费）。
- 媒体：[CNBC DevDay]({{< relref "/docs/dots/sources/media/2026-09-29-cnbc-devday-dots" >}})、[CNBC：OpenAI 跟随 Meta]({{< relref "/docs/industry/sources/media/2026-09-30-cnbc-openai-follows-meta" >}})（发布时的定位）；[甲子光年]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})（成本与付费意愿）；[AIX 财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})（战略动机）。
- 社区：[Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})（讨论量与好感）；[黑咖啡：全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})（100 万个 dots）；[中金研报]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})（平台型变现）。
