---
title: "Poke：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-09
description: >
  Poke 的连接器以 MCP 为底层：第一方集成、经批准的第三方 Recipe 和用户自填的 MCP 地址都走同一套机制；另有入站 API 让任何能发 webhook 的服务触发 Poke。开发者可在 Poke Kitchen 发布 Recipe 并获得分成。
---

## 概要

- 集成有三种来源：第一方集成、Recipe（打包好授权与引导的模板，含经批准的第三方 Recipe）、用户在 poke.com/integrations/new 填入任意兼容 MCP 的服务器地址。
- 邮件只支持 Gmail 和 Outlook（2025-12-12 起支持 Outlook），官方称暂无支持 iCloud、Yahoo 的计划。其余集成覆盖生产力、开发者、健康、智能家居等，第三方说有 40 多项。
- 开发者侧有 npm 包 `poke`（登录、添加 MCP、把本地 MCP 服务器经隧道暴露）和入站 API（`POST /api/v1/inbound/api-message`），后者把任意 JSON 当作上下文交给 Poke。
- 生态激励：Recipe 发布后有分享链接，创作者每带来一个注册用户可得 10 美分到 1 美元；MCP 文档还称可从安装用户的 MCP 使用中获得收入。FAQ 却称「还没有推荐计划」，两处说法未交代关系。
- 资料没有提到平台方拦截 Poke 的情况；Poke 不做购物代下单类的浏览器操作，现实任务改由真人操作员（Poke Human）完成。

## 三种接入方式，同一套 MCP 机制

帮助文档写明，添加集成有两条路：用 Recipe（预制模板，替用户处理 OAuth 或 API key 授权），或对没有 Recipe 的服务在 poke.com/integrations/new 填 MCP URL 和可选的 API key，「连接任何兼容 MCP 的服务器」；poke.com/recipes 收录「第一方和经批准的第三方 recipe」（[文档：Managing Integrations]({{< relref "/docs/poke/sources/official/2026-11-09-docs-managing-integrations" >}})）。用户在 poke.com/integrations 查看、断开、重试或刷新连接，失效后需要重新认证（[文档：Managing Integrations]({{< relref "/docs/poke/sources/official/2026-11-09-docs-managing-integrations" >}})）；2026-01-12 增加了 Reconnect Account 按钮（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）。

MCP 文档给出网页、CLI（`mcp add`、`tunnel`）和预填链接三种添加方式；部分需要 OAuth 的 MCP 只能走网页集成流程。不支持动态客户端注册（DCR）的 OAuth 服务器，可以传 client id 和 secret，或在 Kitchen 建模板，由 Poke 替每位用户处理 OAuth。工具列表在连接创建或重新认证时自动同步（[文档：MCP Servers]({{< relref "/docs/poke/sources/official/2026-11-09-docs-mcp-servers" >}})）。Poke 向 MCP 服务器发的每个请求都带 `Authorization: Bearer` 头和 `X-Poke-User-Id` 头，文档建议服务方据此按用户限流、按用户返回数据、记审计日志（[文档：MCP Servers]({{< relref "/docs/poke/sources/official/2026-11-09-docs-mcp-servers" >}})）。

本地 MCP 服务器用 `npx poke tunnel` 暴露：隧道只转发本地端口、不启动服务器，工具每 5 分钟自动同步，隧道停了连接就离线（[文档：Creating Recipes]({{< relref "/docs/poke/sources/official/2026-11-09-docs-creating-recipes" >}})、[文档：MCP Servers]({{< relref "/docs/poke/sources/official/2026-11-09-docs-mcp-servers" >}})）。CLI 要求 Node.js 18 以上，凭证存在 `~/.config/poke/credentials.json`（[文档：Creating Recipes]({{< relref "/docs/poke/sources/official/2026-11-09-docs-creating-recipes" >}})）。

## 集成清单

| 类别 | 集成 | 资料 |
| --- | --- | --- |
| 邮件与日历 | Gmail、Google Calendar；Microsoft Outlook（邮件、日历、联系人、附件，2025-12-12 起，可与 Google 账户同时连接） | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})、[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}}) |
| 生产力 | Linear、Todoist、Notion、Asana（2025-11-03 第一方）；Granola | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})、[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}}) |
| 开发者 | GitHub、DeepWiki、Sentry、Vercel、Netlify、Supabase（2025-11-03）；PostHog、Devin、Cursor Cloud Agents | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})、[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}}) |
| 商业 | Ramp、Webflow | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |
| 健康与智能家居 | Strava、Withings、Oura、Fitbit；Philips Hue、Sonos | [TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}}) |
| 出行 | 第一方 TripIt 自动化（2026-01-12） | [发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}}) |

FAQ 称完整支持 Gmail 与 Outlook 的收件箱、日历、联系人同步，暂无支持 iCloud、Yahoo Mail 的计划（[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})）。Unite.AI 评测另称「Google Workspace 均不受支持」，同时又说支持 Gmail，含义没有澄清（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。Unite.AI 称可连接 40 多项服务（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。发布说明记录过集成稳定性问题：2026-01-12 修复 Todoist 集成意外断开，2026-02-02 修复 Outlook 订阅同步失败（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）。

## Recipe 与创作者分成

Recipe 把引导上下文（`inputContext`）、预填的首条消息（`prefilledFirstText`）、所需集成（MCP 模板）和分享链接打包在一起；已发布 Recipe 的修改只影响新注册的用户（[文档：Creating Recipes]({{< relref "/docs/poke/sources/official/2026-11-09-docs-creating-recipes" >}})）。2026-03-19 全面开放时 Recipe 同时推出，新老用户都可以用它设置自动化和集成并分享给他人（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）。据 TechCrunch 04-08 报道，用户已创建数千个 Recipe 和自动化，公司计划做成目录；创作者每带来一个经其 Recipe 注册的用户，Poke 付 10 美分到 1 美元（按地区）（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）。Creating Recipes 文档中的 Payouts 显示唯一用户数与累计收益，收款走 Venmo（[文档：Creating Recipes]({{< relref "/docs/poke/sources/official/2026-11-09-docs-creating-recipes" >}})）。MCP 文档称 Recipe 作者日后可以更新服务器地址而无需用户重新添加，并「从安装你 recipe 的用户使用 MCP 中获得收入」（[文档：MCP Servers]({{< relref "/docs/poke/sources/official/2026-11-09-docs-mcp-servers" >}})）。

FAQ 对「你们有推荐计划吗」的回答是「还没有」（[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})）。推断：FAQ 说的可能是面向普通用户的推荐奖励，与 Recipe 创作者分成不是一回事，但资料没有说明。

## 入站 API：让外部事件触发 Poke

API 文档的端点是 `POST https://poke.com/api/v1/inbound/api-message`，用 Bearer key 认证，任意 JSON body 作为上下文转发给智能体，响应只表示是否送达；消息「像你亲自发短信一样被处理」，可以完全访问邮件、日历、提醒和已连接的集成（[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})）。文档列出的用法有 GitHub Action 部署失败告警、CI/CD、webhook、监控、Typeform 提交、CRM 事件、定时任务，以及「无需等待原生集成」地桥接任何能发 webhook 的服务（[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})）。API key 在 Kitchen 创建、只显示一次；旧端点只接受 `pk_` 开头的 V1 key，新端点要 V2 key（[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})）。

推断：入站 API 与 MCP 分工明确，MCP 让 Poke 主动读写外部服务，API 让外部服务把事件推给 Poke，两者合起来构成 Poke 的事件触发能力（见[持续执行]({{< relref "/docs/poke/analysis/continuous-execution" >}})）。

## 与平台方的关系

资料中没有平台拦截 Poke 的记录。潮涌AI称亚马逊封禁了 Muse 的购物行为，并称同类产品 Wajo 声称其架构符合亚马逊服务条款（[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})），这些说的不是 Poke。Poke 处理订餐厅、打电话、下单、叫车这类需要现实操作的任务，交给真人操作员 Poke Human（[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})、[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})），而不是由智能体自动操作网站。

## 资料缺口

- 完整的第一方集成清单与每项的读写范围（「40 多项」只出自 Unite.AI）。
- Recipe 审批规则、目录规模；创作者分成与「还没有推荐计划」的关系；MCP 使用收入的计费方式。
- 入站 API 的频率限制数值（文档只给建议，没有数字）。
- 集成授权粒度：能否只授权只读、能否限制某个集成的可写动作。

## 主要资料

- 官方：[文档：Managing Integrations]({{< relref "/docs/poke/sources/official/2026-11-09-docs-managing-integrations" >}})、[文档：MCP Servers]({{< relref "/docs/poke/sources/official/2026-11-09-docs-mcp-servers" >}})、[文档：Creating Recipes]({{< relref "/docs/poke/sources/official/2026-11-09-docs-creating-recipes" >}})（集成机制与 Recipe）、[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})（入站 API）、[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})（集成时间线与故障修复）、[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})
- 媒体：[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})（集成清单、Recipe 分成）、[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})（集成数量与邮件支持范围）
- 社区：[潮涌AI]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})（平台拦截的行业背景）
