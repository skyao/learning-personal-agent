---
title: "Team Bots 发布"
linkTitle: "Team Bots"
date: 2026-09-28
originalTitle: "Team Bots: shared AI teammates that learn as they work"
sourceUrl: "https://x.ai/news/team-bots"
reprintUrl: "https://web.archive.org/web/20261009055522/https://x.ai/news/team-bots"
author: "未署名"
publisher: "SpaceXAI（xAI）"
language: en
fidelity: 转载全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "x.ai 对自动访问返回 403，依据 Wayback 快照 20261009055522；日期取页面结构化数据的 datePublished"
tags: [发布, 记忆与上下文, 连接器, 开放与价格]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：x.ai 对自动访问返回 403，原文依据 Internet Archive 快照存档；去掉了「Back to news」链接、下载与联系销售按钮和文末「Try Grok Bot today」推广区，视频改为一行链接。去掉了文末无正文的「Try Team Bots today」推广标题。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Team Bots 是可由团队共享的 Grok Bot，每个由四部分构成：上下文（文件、指令、技能）、插件（如 Salesforce、Notion、GitHub，可个人连接或团队统一配置）、凭证（用于没有插件的第三方 API）和记忆。Bot 共享，但每个人与它的对话保持私有，Bot 为每个用户分别保存上下文和记忆，同时使用团队共享的技能；每个 Team Bot 有自己的 Slack 账号，可邀请进频道。xAI 内部用法包括：每个大客户配一个 Bot，夜间查看新闻、Gong 通话、Notion 和 Slack，早上在客户频道发简报；工程 Bot 连 Notion、Linear、Hex、Datadog 和 Cursor；市场 Bot 按品牌准则审稿；Data Bot 用共享的只读凭证查询 Databricks。外部案例为 Harper（24 小时内建成，称为客户节省超过 12 万美元）。Team Bots 以公开 beta 面向 Teams 和 Enterprise 套餐开放。

**保留理由**：这是 Grok Bot 从个人 Bot 扩到团队共享的发布文，明确了共享时对话私有、记忆按人分开、技能共享的设计，并列出开放范围。

---

给 Grok Bot 提供它所需的文件、应用和专业能力，然后分享它，让整个团队基于同样的上下文工作。

[视频](https://media.x.ai/v1/website/grok-bot-team-bots-launch-video-42fbbc12.mp4)

今天我们推出 Team Bots——与你的团队一起工作、一起学习的 Grok Bots。给一个 Team Bot 访问它所需的文件、应用和专业能力，然后分享它，让每个人都能基于同样的上下文工作。

在 SpaceXAI，Team Bots 每天早上为客户团队做简报、协调工程项目，并回答整个公司的数据问题。下面介绍它们如何工作、我们如何使用它们，以及如何为你自己的工作流构建一个。

## Team Bots 将上下文、工具和记忆结合在一起

你围绕团队共享的角色或工作流构建 Team Bot。每个人都能访问同一个 Bot 及其专业能力，同时仍可以单独与它一起工作。

每个 Team Bot 汇集四样东西来帮助它完成工作：

- **上下文（Context）** 为它提供相关文件、指令和技能，从品牌指南到内部文档。
- **插件（Plugins）** 让它能在 Salesforce、Notion 和 GitHub 等应用中工作。插件可以由每个人连接，也可以为整个团队配置。
- **凭证（Credentials）** 让它安全访问没有插件的第三方 API。
- **记忆（Memories）** 帮助它保留所学内容，并随着时间推移在其角色上不断改进。

尽管 Bot 是共享的，每个人与它的对话仍保持私密。Bot 为每个用户保留独立的上下文和记忆，同时利用团队共享的技能。

团队还可以在 Slack 中与 Team Bot 协作。每个 Team Bot 都有自己的账号名（handle），因此你可以把它邀请到频道，让每个人都能提问、贡献上下文并查看它的回复。

## Team Bots 在 SpaceXAI 承担工作

在 SpaceXAI，我们正在一些上下文最密集的工作流中使用 Team Bots。以下是来自销售与客户成功、产品与工程、市场和数据分析的四个例子。

### 销售与客户成功

在 SpaceXAI，每个重要销售客户都有一个专门的 Team Bot。每个 Bot 由客户主管（AE）、客户成功经理（CSM）、解决方案架构师（SA）和销售负责人共享。

每晚，Bot 会查看公司新闻、最近的 Gong 通话、Notion 文档和相关 Slack 线程。每天早上，它在客户所在的 Slack 频道发布简报，说明发生了什么变化以及每个人接下来该做什么，包括针对其角色定制的草稿。

一天中，客户团队在 Slack 中使用该 Bot 评估策略、用客户数据检验它的思路，并规划下一步。Bot 记住团队做出的决定，并随着时间积累丰富的上下文。当人员在这个客户上轮换进出时，它成为记录系统，并能快速让新团队成员跟上进度。

Harper 是一家服务小企业的保险公司，它构建了一个 Team Bot 来识别保单失效的客户，并帮助他们恢复保障，从而减少团队的手工工作，并为客户节省了大量费用。

> 「起初，我们不得不通过三个平台手动检查每位客户、获取他们的余额详情，并向他们发送个性化电子邮件。我们在 24 小时内构建了一个 Team Bot 来自动化这项工作，从数百份保单中为客户节省了超过 120,000 美元。现在这对我们来说是一台持续运转的引擎，既节省我们的时间，也节省客户的钱。」

Dakotah Rice，Harper 首席执行官

Customer Bot

为一个客户账户共享的 Bot。它让 AE、CSM、SA 和销售负责人保持同步，在工作日早上发布简报，并为每个人起草下一步行动。

[添加到 Grok Bot](https://x.ai/bot/XuWFUtbBJNcGBisijI1FZ)

### 产品与工程

我们的 Engineering Team Bot 从项目的 Slack 频道工作，并连接到 Notion、Linear、Hex、Datadog 和 Cursor。它跟踪产品决策、分诊缺陷报告、创建工单，并启动 Cloud Agents 来处理定义明确的修复。

我们通过技能把我们的发布流程教给这个 Bot。它知道如何处理 PR 审查、何时向团队求助，以及一项更改在完成前需要什么证据。它跨工具和 agent 协调工作，然后在 Slack 中报告进度和阻碍。

我们在构建 Team Bots 时使用了这套配置。该 Bot 引导了一个 Cursor Project，后者编排了数百个 Cloud Agents，帮助一个五人团队每天发布超过 100 个 PR，并在几周内推出 Team Bots。

EPD Teammate

你的 EPD 团队项目或功能的协调者。它跟进项目的 Slack 频道，在 Linear 中提交清晰的缺陷，并运行 Cursor 云 agent，返回通过验证、状态为绿的 PR，让整个团队保持同步。

[添加到 Grok Bot](https://x.ai/bot/bt93P5KxADS3G69xRa_q1)

### 市场

大型市场团队花费大量时间保持其品牌、信息和语气一致。我们构建 Marketing Bot 来让这项工作更轻松。

我们让该 Bot 访问我们的品牌指南、博客文章和社交文案。每当有人在 Slack 中分享草稿以供审批，它会根据我们的语气和最新信息审查作品。区域团队可以获得反馈，并在自己的时区继续推进，而无需等待总部的审批周期。

对于网站和 SEO 更改，Marketing Bot 把工作从审查推进到上线。一旦内容更新通过审查，Bot 就会进行更改，并在 Slack 中发布预览链接以供最终签核。市场团队的任何人都可以发布网站更新，而无需提交工单或等待工程部门，且每项更改都会经过相同的品牌和 SEO 检查。

> 「我们正朝着为每个市场职能构建 Team Bots 的方向努力。这些 Bot 帮助我们深入挖掘市场和客户情报、出现在 AI 答案中、审查发布，并告诉我们什么在起作用。」

Angela Ferrante，Amplitude 市场负责人

Marketing Bot

让你的市场团队保持品牌一致。根据你的品牌指南和最新信息审查任何产物，并把已批准的网站和 SEO 更改从审查推进到预览和签核，让每个区域都能按自己的时间表发布。

[添加到 Grok Bot](https://x.ai/bot/YHpL0gdPx1l98iS02wGak)

### 数据分析

我们的数据分析团队每天收到数十个一次性分析请求。它构建了 Data Bot，让 SpaceXAI 的任何人都能获得答案，而无需等待分析师或配置数据仓库访问权限。

Data Bot 使用共享的只读凭证查询 Databricks 中已批准的表。它还连接到 Datadog、Hex 和 Statsig，以调查问题并呈现结果。

数据分析团队已经花了两年时间构建一个用于处理超过 45,000 张表的技能库。它把现有技能库交给了 Data Bot，其中包括查找正确数据、为反欺诈分析功能使用情况、遵循 SpaceXAI 的图表标准，以及安全更新公司范围仪表盘的指令。Data Bot 还会记住对其查询的更正，因此它从一个人那里学到的东西会改善它给所有人的答案。

Data Bot

用只读查询、清晰的指标定义和图表，从你的数据仓库回答团队的一次性数据问题。它会记住每一次更正和确认，因此答案会随着时间推移对所有人变得更好。

[添加到 Grok Bot](https://x.ai/bot/1AEEU5lIoAeb4gQM20vj3)

## 开始使用 Team Bots

Team Bots 今天以公开 beta 形式在 Teams 和 Enterprise 套餐中提供。把你最喜欢的 Grok Bots 拿出来与团队分享。要开始使用，试试我们为[销售](#customer-bot)、[产品管理](#epd-teammate)、[市场](#marketing-bot)或[数据分析](#data-bot)预构建的 Team Bots 之一。
