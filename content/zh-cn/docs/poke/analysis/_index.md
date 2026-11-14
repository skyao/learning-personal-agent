---
title: "Poke 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-09
description: >
  Poke 是帕洛阿尔托创业公司 The Interaction Company of California 的个人助手，没有独立 App，只住在 iMessage、Telegram、WhatsApp 等消息应用里，会主动发消息；2026-07 加入 Cognition。分析覆盖截至 2026-11-09 收集的 18 篇 Poke 资料和 3 篇涉及 Poke 的行业资料。
---

## 概要

- Poke 把助手做成一个「联系人」：无需安装 App，输入手机号后它在消息应用里与用户对话。2026-06-04 成为 Apple Messages for Business 上首个获批的 AI 智能体；WhatsApp 则受 Meta 条款与监管影响时断时续。（[交互渠道]({{< relref "/docs/poke/analysis/channels" >}})）
- 「先发消息、会跟进」是核心卖点：留意已连接账户中的信号主动提醒，用户用纯文本建自动化，外部服务经 API 推事件触发。后台实时自动化只在付费档提供，也是成本的主要来源。（[持续执行]({{< relref "/docs/poke/analysis/continuous-execution" >}})）
- 连接器以 MCP 为底层，第一方集成、Recipe 和用户自填的 MCP 地址走同一套机制；开发者可发布 Recipe 并获得拉新分成。邮件只支持 Gmail 和 Outlook。（[连接器]({{< relref "/docs/poke/analysis/connectors" >}})）
- 价格从 beta 期「跟 AI 砍价」的协商定价演变为 Free、Pro 19 美元、Ultra 199 美元三档；2026-03-19 取消准入排队全面开放，官方称全球可用。（[开放与价格]({{< relref "/docs/poke/analysis/access-pricing" >}})）
- 公司约 10 人，2026-04 估值 3 亿美元，2026-07 以「low nine figures」的估值并入 Cognition。规模只有消息量（「最近三个月超过 1 亿条」）和「数十万人」，创始人称运行成本高、难以盈利。（[商业与规模]({{< relref "/docs/poke/analysis/business" >}})）
- 安全资料以厂商自述为主（SOC 2 Type II、CASA Tier 2、渗透测试）；审批模型、提示注入防护没有公开说明。（[安全]({{< relref "/docs/poke/analysis/security" >}})）
- 只有一份独立评测：适合轻量任务、能主动提醒，但邮件分拣不够敏锐、「仍偶尔不可靠」。运行环境、记忆、模型、隐私的资料都很少。（[实际效果与可靠性]({{< relref "/docs/poke/analysis/reliability" >}})）

## 定位

新闻稿把 Poke 定位为直接接入消息平台的 AI 助手，批评现有助手「住在自己的应用里」、对用户的真实生活一无所知（[发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}})）。官网首页的标语是「Meet Poke, your new favorite contact」（[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}})），Cognition 的描述是「它会先给你发消息，会跟进你，感觉不太像软件，更像一个朋友」（[Cognition 公告]({{< relref "/docs/poke/sources/official/2026-07-23-cognition-welcoming-interaction" >}})）。据创始人自述，产品起初是以邮件为中心的客户端，用户反馈后转向通用的对话助手（[General Catalyst]({{< relref "/docs/poke/sources/community/2025-09-08-general-catalyst-seeding-interaction" >}})、[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）。

TechCrunch 称它是「我们普通人的 OpenClaw」：不需要终端和依赖管理（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）。von Hagen 认为多模型是主要优势，因为几乎所有竞争对手都绑定自家模型，「Meta AI 永远只能使用 Meta 的模型，ChatGPT 永远只能使用 OpenAI 的模型」（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）。

与其他跟踪产品相比：

| 对比对象 | 差异 | 资料 |
| --- | --- | --- |
| ChatGPT、Claude、Gemini | Unite.AI 认为 Poke 安静住在短信里主动提醒，前两者是要主动打开的工作区；Gemini 深度绑定 Google 生态，Poke 跨 Gmail、Outlook、Notion、GitHub | [Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}}) |
| Muse、Dots 等 | 创始人称大厂产品绑定自家模型，Poke 按任务选模型 | [TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}}) |
| Instinct 等短信类智能体 | 同属住在短信、iMessage、WhatsApp 里的路线；TechCrunch 合集列 24 款，Instinct 估值 100 亿美元，Poke 已被收购 | [TechCrunch 短信智能体合集]({{< relref "/docs/industry/sources/media/2026-10-24-techcrunch-text-message-agents" >}})、[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}}) |

潮涌AI把 Poke 排在其 15 家个人智能体创业公司的第 9 位，把它被 Cognition 收购看作「整合已开始」的例证（[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2025-09-08 | 公开发布，可在 Poke.com 注册；宣布 1500 万美元种子轮（标题写估值 1 亿美元）；渠道为 iMessage、SMS | [发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}})、[General Catalyst]({{< relref "/docs/poke/sources/community/2025-09-08-general-catalyst-seeding-interaction" >}}) |
| 2025-11-03 | 集成库改版，新增 Linear、Notion、GitHub、Ramp 等第一方集成 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2025-11-17 | iMessage 行内回复；FAQ 上线 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2025-12-12 | 支持 Microsoft Outlook | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2025-12-22 | WhatsApp 已读回执、输入状态、行内回复 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-01-12 | Reconnect Account 按钮、第一方 TripIt 自动化 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-02-02 | WhatsApp 暂不可用（意大利、巴西除外）期间改用 Telegram；可创建表格和图表 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-03-19 | 取消 bouncer 全面开放，推出 Recipes；TechCrunch 称之为公开发布 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})、[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}}) |
| 2026-04-08 | 据 TechCrunch，再融资 1000 万美元，投后估值 3 亿美元 | [TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}}) |
| 2026-06-04 | 获准上 Apple Messages for Business | [TechCrunch：Apple Messages for Business]({{< relref "/docs/poke/sources/media/2026-06-04-techcrunch-apple-messages-for-business" >}})、[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-06-08 | 可认领 @poke.com 邮箱 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-06-18 | Poke Ultra（199 美元/月）上线；网站搭建 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-06-25 | Poke Human（真人操作员）并入 Ultra | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-07-23 | Cognition 宣布 The Interaction Company 加入，Poke 照常运营 | [Cognition 公告]({{< relref "/docs/poke/sources/official/2026-07-23-cognition-welcoming-interaction" >}})、[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-07-24 | TechCrunch：交易估值「low nine figures」；明年部分任务改用 SWE-1.7 | [TechCrunch：Cognition 收购]({{< relref "/docs/poke/sources/media/2026-07-24-techcrunch-why-cognition-bought-poke" >}}) |
| 2026-09-09 | Unite.AI 评测 | [Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}}) |
| 2026-11-09 | 收集时官网仍为三档价格与「Poke is joining Cognition」横幅 | [价格页]({{< relref "/docs/poke/sources/official/2026-11-09-pricing" >}})、[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}}) |

## 整体架构

用户在 poke.com 输入手机号，Poke 在 Apple Messages、Telegram、WhatsApp 或 RCS 中与用户对话（[交互渠道]({{< relref "/docs/poke/analysis/channels" >}})）。它接入用户的 Gmail 或 Outlook 邮箱、日历和联系人，以及经 MCP 接入的各类服务；Recipe 把集成和引导打包，可分享（[连接器]({{< relref "/docs/poke/analysis/connectors" >}})）。它根据账户信号、用户建的自动化和经入站 API 推来的外部事件主动行动（[持续执行]({{< relref "/docs/poke/analysis/continuous-execution" >}})）；需要现实操作的任务由 Ultra 档的真人操作员完成。按任务选择模型，付费档用前沿模型；用量按额度或积分计，用尽后降级而不断服（[开放与价格]({{< relref "/docs/poke/analysis/access-pricing" >}})）。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| 运行环境 | —。资料不足：资料没有说明 Poke 在什么环境中运行。Cognition 称两个团队都押注「always-on cloud agents」（[Cognition 公告]({{< relref "/docs/poke/sources/official/2026-07-23-cognition-welcoming-interaction" >}})）。可见的能力有生成表格、图表和带 LaTeX 格式的 PDF（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})），以及为用户搭建并发布网站（FAQ 写 `yourname.poke.site`，发布说明写 `yourname.poke.com`，见 [FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})、[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）。本地 MCP 服务器经隧道接入（[文档：Creating Recipes]({{< relref "/docs/poke/sources/official/2026-11-09-docs-creating-recipes" >}})）。创始人称真正花钱的是实时推理（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})） |
| 记忆与上下文 | —。资料不足：官网称 Poke 会使用已集成的服务「及其 memory」（[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}})）；Unite.AI 称它跨对话保留上下文和偏好（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。记忆、Recipe、集成绑定在账户上，合并账户时只保留所选账户的，另一个账户的数据 30 天后删除（[文档：Merging Accounts]({{< relref "/docs/poke/sources/official/2026-11-09-docs-merging-accounts" >}})）。记忆如何形成、能否查看和删除，资料没有说明 |
| [持续执行]({{< relref "/docs/poke/analysis/continuous-execution" >}}) | 账户信号、纯文本自动化、入站 API 三种触发；后台实时自动化与主动更新为 Pro 起；邮件分拣不够敏锐 |
| [连接器]({{< relref "/docs/poke/analysis/connectors" >}}) | MCP 为底层，第一方、Recipe、自填 MCP 三种来源；入站 API；Recipe 创作者拉新分成；邮件只支持 Gmail、Outlook |
| [交互渠道]({{< relref "/docs/poke/analysis/channels" >}}) | 无 App，住在消息应用里；首个获批的 Apple Messages for Business AI 智能体；WhatsApp 受 Meta 条款与监管左右 |
| 设备 | —。资料不足：没有专用硬件和独立 App，网页端只做设置与管理（[文档：Welcome]({{< relref "/docs/poke/sources/official/2026-11-09-docs-welcome" >}})）；桌面上可以用 API 自建浏览器扩展、VS Code 扩展等入口（[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})） |
| 模型 | —。资料不足：创始人称 Poke 按任务选择大厂或开源模型（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）；Pro 在复杂任务上用前沿模型，Ultra 有积分时每个动作都用前沿模型（[价格页]({{< relref "/docs/poke/sources/official/2026-11-09-pricing" >}})、[文档：Usage & Resets]({{< relref "/docs/poke/sources/official/2026-11-09-docs-usage-and-resets" >}})）；明年将在部分任务上改用 Cognition 的 SWE-1.7（[TechCrunch：Cognition 收购]({{< relref "/docs/poke/sources/media/2026-07-24-techcrunch-why-cognition-bought-poke" >}})）。具体模型名称资料没有 |
| [安全]({{< relref "/docs/poke/analysis/security" >}}) | SOC 2 Type II、CASA Tier 2、渗透测试均为厂商自述；Poke Human 操作员只看任务细节；审批模型未公开 |
| 隐私 | —。资料不足：新闻稿称「以隐私为基础」（[发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}})）；据 TechCrunch 转述公司说法，默认团队看不到 token 内容，除非用户在设置中打开开关提供日志（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）；删除账户最多需 24 小时，备份归档清除不一定立即（[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})）。是否用于训练、保存期限、隐私政策原文都没有（法律文档按收录规则未收） |
| [开放与价格]({{< relref "/docs/poke/analysis/access-pricing" >}}) | Free、Pro 19 美元、Ultra 199 美元；从协商定价到固定档位；2026-03-19 全面开放，官方称全球可用 |
| [商业与规模]({{< relref "/docs/poke/analysis/business" >}}) | 种子轮 1500 万美元、估值 3 亿美元后以「low nine figures」并入 Cognition；规模只有消息量，创始人称难以盈利 |
| [实际效果与可靠性]({{< relref "/docs/poke/analysis/reliability" >}}) | 只有 Unite.AI 一份独立评测；发布说明记录时区、邮件、集成问题的修复；无完成率数据 |

## 资料缺口

- **规模与财务**：用户数、付费用户数、收入；「数十万人」的口径；收购金额与结构。
- **技术**：运行环境、使用的具体模型、记忆的形成与管理方式。
- **安全与隐私**：审批模型、提示注入防护；数据用途、训练、保存期限（隐私政策按收录规则未收，分析中无从引用）。
- **实测**：第二份独立实测、用户自己的实测（`exploration/` 为空）、长期使用记录；2026-03-19 之后的问题记录。
- **价格**：Free、Pro 的额度数值；各地区本币价格。
- **Cognition 之后**：SWE-1.7 切换、与 Devin 整合是否落地；2026-08 以后没有新的媒体报道。
