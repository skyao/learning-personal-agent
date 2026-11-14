---
title: "Poke：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-09
description: >
  Poke 的安全资料以厂商自述为主：SOC 2 Type II、CASA Tier 2 认证和定期渗透测试；真人操作员 Poke Human 只看任务所需细节；入站 API key 等同于能代用户发指令的凭证。哪些动作需要用户批准、如何防提示注入，资料没有说明。
---

## 概要

- 官方称具备 SOC 2 Type II 和 CASA Tier 2 认证，由安全公司定期做渗透测试；创始人称对智能体和人类员工都限制权限。TechCrunch 声明没有做自己的安全审计。
- 资料中没有完整的审批模型。唯一的线索是发布说明修复过「起草邮件时陷入反复批准循环」的 bug，说明发邮件前有批准步骤。
- Poke Human 的真人操作员只能看到完成任务所需的细节（如餐厅名、用餐人数），不能访问聊天记录、记忆或集成（官方说法）。
- 入站 API key 与 Poke CLI 凭证都能直接驱动用户的 Poke，文档要求妥善保存、泄露即吊销。
- 资料库中没有针对 Poke 的漏洞报道、安全事件或漏洞赏金信息。

## 认证与渗透测试

2025-09-08 新闻稿称平台采用「业界领先的安全标准」，包括 SOC 2 Type II 和 CASA Tier 2 认证，并由网络安全公司定期做渗透测试（[发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}})）。TechCrunch 04-08 转述创始人的说法：多层安全模型，包括定期渗透测试、安全检查，对智能体和人类员工都限制权限；默认情况下团队看不到 token 内部的内容。TechCrunch 注明「并未进行自己的安全审计」（[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})）。

官方文档页首的免责声明称 Poke 可能出错，重要信息需要核实，它不能提供医疗、财务或法律建议（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})）。

## 审批：只有零星线索

资料没有说明哪些动作（发送邮件、付款、删除、对外沟通）需要用户批准，也没有审批设置页。可见的线索有：

- 2025-11-03 发布说明修复了「部分用户在让 Poke 起草邮件时陷入反复批准循环」的 bug（[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})），可见发邮件有批准环节。
- 入站 API 的消息「像你亲自发短信一样被处理」，可以完全访问邮件、日历、提醒和已连接的集成（[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})），API 触发的任务与用户本人下的指令权限相同。
- Poke Human 代付的现实开销按成本价从 Ultra 积分余额中扣除（[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})），资料没有说明每笔是否需要用户确认。

推断：Poke 的权限边界主要由「连了哪些集成」决定，没有像其他跟踪产品那样公开说明分级审批或独立的审查模型。这是资料缺失，不一定说明产品没有这些机制。

## 真人操作员的权限

FAQ 称 Poke Human 把需要真人的现实任务（餐厅预订、打电话、下单、叫车）派给真人操作员，操作员只能看到完成任务所需的具体细节，比如餐厅名和人数，无法访问聊天记录、记忆或集成（[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})）。Unite.AI 评测复述了这一说法（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。这是官方描述，资料中没有独立核实。

## 凭证与身份

- **API key**：任何拿到 key 的人都能向用户的 Poke 发消息。文档建议放环境变量、不提交到 Git、泄露立即吊销，并可为不同用途建多个 key 分别吊销（[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})）。
- **CLI 凭证**：`poke login` 的凭证存在本机 `~/.config/poke/credentials.json`（[文档：Creating Recipes]({{< relref "/docs/poke/sources/official/2026-11-09-docs-creating-recipes" >}})）。
- **MCP 授权**：Poke 向 MCP 服务器发送 Bearer token 和用户 ID（[文档：MCP Servers]({{< relref "/docs/poke/sources/official/2026-11-09-docs-mcp-servers" >}})）；用户填入的第三方 MCP API key 如何存放，文档没有说明。
- **手机号即身份**：账户在有人首次用某个号码给 Poke 发消息时自动创建；合并账户要用短信验证码确认手机号（[文档：Merging Accounts]({{< relref "/docs/poke/sources/official/2026-11-09-docs-merging-accounts" >}})）。

## 用户对信任的顾虑

Unite.AI 评测认为，把收件箱、日历和智能家居的访问权交给 AI 智能体需要一定程度的信任，有些人还没准备好（[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})）。创始人在 Apple 报道中称团队在意「拥有一个传递信任的品牌」（[TechCrunch：Apple Messages for Business]({{< relref "/docs/poke/sources/media/2026-06-04-techcrunch-apple-messages-for-business" >}})）。

## 资料缺口

- 审批模型：哪些动作需批准、能否设置；Poke Human 代付是否逐笔确认。
- 提示注入与恶意邮件、恶意网页的防护说明。
- SOC 2 报告或认证的范围与日期；渗透测试的执行方。
- 漏洞赏金、安全事件与厂商回应；加入 Cognition 后安全体系是否变化。

## 主要资料

- 官方：[发布新闻稿]({{< relref "/docs/poke/sources/official/2025-09-08-introducing-poke-press-release" >}})（认证与渗透测试）、[FAQ]({{< relref "/docs/poke/sources/official/2026-11-09-faq" >}})（Poke Human 权限）、[文档：API]({{< relref "/docs/poke/sources/official/2026-11-09-docs-api" >}})、[文档：Creating Recipes]({{< relref "/docs/poke/sources/official/2026-11-09-docs-creating-recipes" >}})、[文档：MCP Servers]({{< relref "/docs/poke/sources/official/2026-11-09-docs-mcp-servers" >}})（凭证）、[文档：Merging Accounts]({{< relref "/docs/poke/sources/official/2026-11-09-docs-merging-accounts" >}})（手机号与账户）、[发布说明]({{< relref "/docs/poke/sources/official/2026-07-23-docs-release-notes" >}})（批准循环 bug、免责声明）
- 媒体：[TechCrunch 04-08]({{< relref "/docs/poke/sources/media/2026-04-08-techcrunch-agents-easy-as-text" >}})（创始人对安全模型的说法、未审计声明）、[TechCrunch：Apple Messages for Business]({{< relref "/docs/poke/sources/media/2026-06-04-techcrunch-apple-messages-for-business" >}})、[Unite.AI 评测]({{< relref "/docs/poke/sources/media/2026-09-09-unite-ai-poke-review" >}})
