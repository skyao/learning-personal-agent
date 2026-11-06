---
title: "文档：配置身份与访问"
linkTitle: "文档：身份与访问"
date: 2026-11-05
originalTitle: "Configure identity and access"
sourceUrl: "https://cursor.com/docs/grok-bot/identity"
altUrls: ["https://docs.x.ai/grok-bot/identity-and-access"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：面向使用 Okta 或 Microsoft Entra ID 的管理员。Grok Bot 使用 Cursor 账号，因此没有独立的 Okta 或 Entra 应用，需要把现有 Cursor 应用分配给工程以外的用户组，才能让他们访问；SCIM 仅限 Enterprise。另一项改动是在身份提供方里为 Bot 的计算机浏览器会话增加认证规则，因为这台 Linux 计算机不运行 Okta FastPass 等设备信任代理，也未纳入 MDM。这条规则只影响 Bot 在计算机浏览器里打开的、由身份提供方发放的应用，不影响 Grok Bot 登录或连接应用的登录。撤销用户在身份提供方的权限会终止其计算机内的应用会话，管理员也可随时终止成员的计算机。

**保留理由**：说明托管计算机在企业身份体系里的位置：登录走 Cursor SSO，而计算机内的登录不满足设备信任，因此要单独放行，对理解其与企业身份的关系有用。
