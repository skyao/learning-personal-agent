---
title: "Poke：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-09
description: >
  Poke 没有独立 App，只住在消息应用里：截至 2026-11 的官方文档列出 Apple Messages、Telegram、WhatsApp 和 RCS；2026-06-04 起成为 Apple Messages for Business 上首个获批的 AI 智能体，WhatsApp 则受 Meta 条款和监管限制时断时续。
---

## 概要

- 渠道就是产品：用户在 poke.com 输入手机号，Poke 直接给用户发消息，无需安装 App。手机号是账户身份的主要依据。
- 渠道清单随时间变化：2025-09 发布时是 iMessage 和 SMS（另提 WhatsApp），2026-11 文档列 Apple Messages、Telegram、WhatsApp、RCS，各处说法不完全一致。
- 2026-06-04 Poke 获准上 Apple Messages for Business，官方称是该平台「首个也是唯一」获验证的 AI 智能体。审批条件包括真人支持、AI 身份标识、按 Apple 规范定制界面，创始人称合规用了几个月。
- WhatsApp 是最不稳定的渠道：Meta 2025 年秋禁止通用聊天机器人后 Poke 的支持受限，监管介入后在巴西恢复，2026-02 起官方以 Telegram 作为备用。
- 智能体以 Poke 自己的身份出现（「新联系人」），另可认领 @poke.com 邮箱地址；资料没有说明它以用户名义对外发消息时如何标识。

## 只住在消息应用里

新闻稿的出发点是：现有助手「住在自己的应用里」，用户要复制粘贴、管理新登录、学新界面；Poke 则「住在 iMessage、WhatsApp 和 SMS 中」，联合创始人称用户想用给伴侣、朋友和同事发短信的方式给 AI 发消息（[发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}})）。General Catalyst 文章中的创始人自述，产品起初以邮件为中心，用户反馈后转向不需要学新界面的对话助手（[General Catalyst]({{< relref "/docs/poke/sources/community/2025-09-08-general-catalyst-seeding-interaction" >}})）。官网首页的标语是「Meet Poke, your new favorite contact」（[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}})）。

使用方式：在 poke.com 输入手机号，Poke 直接发消息过来，无需安装 App（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）。Unite.AI 实测称设置不到两分钟，Poke 接受语音备忘，但会产生短信和数据费用（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。网页端只承担设置、集成、Kitchen 与订阅管理（[文档：Welcome]({{< relref "/docs/poke/sources/official/2026-11-09-docs-welcome" >}})、[文档：Usage & Resets]({{< relref "/docs/poke/sources/official/2026-11-09-docs-usage-and-resets" >}})）。桌面上不想掏出手机时，官方建议用 API 自建浏览器扩展、VS Code 扩展等入口，把内容发给 Poke（[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})）。

## 渠道清单的变化

| 时间 | 渠道 | 资料 |
| --- | --- | --- |
| 2025-09-08 | iMessage、SMS；「关于」一节另列 WhatsApp | [发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}}) |
| 2025-11-17 | 支持 iMessage 行内回复（Poke 能看到回复所指的消息） | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2025-12-22 | WhatsApp 支持已读回执、输入状态与行内回复 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-02-02 | WhatsApp 暂时不可用期间（意大利和巴西除外）可改用 Telegram，在设置的 Messaging 中选择 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-04-08 | TechCrunch：iMessage、SMS、Telegram 及部分市场的 WhatsApp；iMessage 借助 Linq 接入 | [TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}}) |
| 2026-06-04 | Apple Messages for Business 获批 | [TechCrunch：Apple Messages for Business]({{< relref "/docs/poke/sources/media/2026-06-04-techcrunch-apple-messages-for-business" >}})、[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-06-08 | 可认领 @poke.com 邮箱地址，与主邮箱一起使用 | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 2026-11-09 | 文档：Apple Messages、Telegram、WhatsApp、RCS；首页：Messages、WhatsApp、Telegram | [文档：Welcome]({{< relref "/docs/poke/sources/official/2026-11-09-docs-welcome" >}})、[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}}) |

账户合并文档还提到可通过 Telegram 或 LINE 创建没有手机号的账户（[文档：Merging Accounts]({{< relref "/docs/poke/sources/official/2026-11-09-docs-merging-accounts" >}})），但其他官方页面没有列出 LINE。FAQ 称用户可在设置中改选渠道，取决于平台，Poke 可能用不同号码发消息；更换手机号要发邮件给客服，不能自助；暂不支持一个账户绑多个手机号（[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})）。

## Apple Messages for Business：首个获批的 AI 智能体

据 TechCrunch 2026-06-04 报道，Apple Messages for Business 原本供航空、零售等企业与客户沟通，此前未对独立第三方 AI 智能体开放（[TechCrunch：Apple Messages for Business]({{< relref "/docs/poke/sources/media/2026-06-04-techcrunch-apple-messages-for-business" >}})）。获批条件包括：证明需要时能提供真人支持、AI 被清楚标识为 AI、提交消息服务商的证词、按 Apple 规范定制界面（如显示链接预览而非行内链接）。von Hagen 称满足这些标准花了几个月。现有用户收到可选的迁移邀请，订阅保留，可用 Apple Pay（[TechCrunch：Apple Messages for Business]({{< relref "/docs/poke/sources/media/2026-06-04-techcrunch-apple-messages-for-business" >}})）。

费用方面，von Hagen 称公司按用户数向消息服务商付费，不能透露价格，但「明显低于」Meta 的收费；TechCrunch 文末更正，付款对象是消息服务商，不是 Apple（[TechCrunch：Apple Messages for Business]({{< relref "/docs/poke/sources/media/2026-06-04-techcrunch-apple-messages-for-business" >}})）。Cognition 的公告称 Poke 是「唯一获准在 Apple Messages 上原生发短信的 AI agent」（[Cognition 公告]({{< relref "/docs/poke/sources/official/2026-07-23-cognition-welcoming-interaction" >}})），TechCrunch 短信智能体合集称这让 Poke「格外引人注目」（[TechCrunch 短信智能体合集]({{< relref "/docs/industry/sources/media/2026-10-24-techcrunch-text-message-agents" >}})）。

推断：Apple 审批要求「AI 被清楚标识」，Poke 以独立联系人的身份出现，与此一致；但资料没有说明 Poke 替用户发邮件、发消息时，收信方能否看出是 AI 代发。

## WhatsApp 受平台条款与监管左右

TechCrunch 04-08 写道，Meta 2025 年秋禁止其他通用聊天机器人上 WhatsApp，Poke 的 WhatsApp 支持因此受限；欧盟、意大利、巴西监管机构启动反垄断调查后，Poke 回到巴西，并希望 Meta 降价后在欧盟恢复。von Hagen 把 Meta 的收费称为「恶意服从」（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）。官方发布说明 2026-02-02 的条目与此对应：WhatsApp 暂不可用（意大利和巴西除外）期间改用 Telegram（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）。截至 2026-11-09，文档仍把 WhatsApp 列为渠道之一（[文档：Welcome]({{< relref "/docs/poke/sources/official/2026-11-09-docs-welcome" >}})），资料没有说明在哪些地区恢复。

## 同类产品中的位置

TechCrunch 2026-10-24 的短信智能体合集列出 24 款经 iMessage、WhatsApp、Telegram、RCS 运行的产品，Poke 是其中之一，条目内容是对自家前两篇报道的概括（[TechCrunch 短信智能体合集]({{< relref "/docs/industry/sources/media/2026-10-24-techcrunch-text-message-agents" >}})）。潮涌AI称其筛选的 15 家创业公司中有七家住在短信、iMessage 或 WhatsApp 里，称之为「界面正在消失」（[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})）。

推断：短信路线的门槛在渠道方，而不在技术。Poke 的两个关键节点（WhatsApp 受限、Apple 获批）都是平台方的决定，渠道的开放程度和收费直接决定了 Poke 能覆盖哪些地区的用户。

## 资料缺口

- 各渠道的地区可用性对照（WhatsApp 在欧盟以外哪些地区可用、RCS 与 SMS 的关系）。
- 迁移到 Apple Messages for Business 后的体验差异、迁移比例。
- Poke 替用户对外发邮件、消息时的身份披露方式；@poke.com 邮箱的用途与限制。
- 消息服务商的名称与按用户计费的价格。

## 主要资料

- 官方：[发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}})（最初的渠道与产品主张）、[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})（渠道变化时间线）、[文档：Welcome]({{< relref "/docs/poke/sources/official/2026-11-09-docs-welcome" >}})、[官网首页]({{< relref "/docs/poke/sources/official/2026-11-09-poke-homepage" >}})（当前渠道清单）、[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})、[文档：Merging Accounts]({{< relref "/docs/poke/sources/official/2026-11-09-docs-merging-accounts" >}})（手机号与账户）、[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})（桌面入口）、[Cognition 公告]({{< relref "/docs/poke/sources/official/2026-07-23-cognition-welcoming-interaction" >}})
- 媒体：[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})（Linq、WhatsApp 限制）、[TechCrunch：Apple Messages for Business]({{< relref "/docs/poke/sources/media/2026-06-04-techcrunch-apple-messages-for-business" >}})（Apple 审批条件与费用）、[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})（设置体验）、[TechCrunch 短信智能体合集]({{< relref "/docs/industry/sources/media/2026-10-24-techcrunch-text-message-agents" >}})（同类产品）
- 社区：[General Catalyst]({{< relref "/docs/poke/sources/community/2025-09-08-general-catalyst-seeding-interaction" >}})（产品转向自述）、[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})
