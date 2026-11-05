---
title: "帮助：连接应用"
linkTitle: "帮助：连接应用"
date: 2026-11-05
originalTitle: "Connect apps"
sourceUrl: "https://cursor.com/help/grok-bot/connect-apps"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [连接器, 安全]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

**收集者摘要**：应用让 Bot 使用外部服务，连接属于登录 Grok Bot 的同一账号，Bot 只能做该账号本来就能做的事，不能提升权限。添加方法是在侧边栏「Connect apps」中授权并在浏览器完成登录；团队管理员可禁用某些应用，显示「Disabled by team admin」。连接 Google 系应用时，Grok Bot 以「Grok」而非 Cursor 的名义登录，公司 Google 管理员需先在 API 控制里将 Grok 设为受信任；Microsoft 365 同样需管理员批准。文中逐个说明 Google Calendar、Sheets、Slack、Gmail、X、Power BI（只读）、BigQuery、Databricks Genie、Asana、Vanta、Shop Pay 的能力与限制，Gmail 同一时间只能连一个邮箱。1Password 集成需批准每次登录，Bot 看不到值，不填支付卡，只提供个人保险库里的登录。文末列出两个已知问题：Zoom 授权报错 4700、SharePoint 应用级权限报错 AADSTS50011，目前无解或只能改用委托权限。

**保留理由**：列出各连接器的具体能力、管理员批准流程和已知问题，对研究连接器的权限边界和落地摩擦有用。
