---
title: "文档：配置身份与访问"
linkTitle: "文档：身份与访问"
date: 2026-11-05
originalTitle: "Configure identity and access"
sourceUrl: "https://docs.x.ai/grok-bot/identity-and-access"
altUrls: ["https://cursor.com/docs/grok-bot/identity"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-11
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：Okta FastPass 在按 Okta Verify and FastPass 页面设置后可在 Bot 计算机上使用（旧版称计算机不运行设备信任代理）；新增 Okta、Entra ID 各自分步的分配与规则/策略步骤"
tags: [安全, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：面向使用 Okta 或 Microsoft Entra ID 作身份提供方的管理员。Grok Bot 使用 Cursor 账号，因此没有独立的 Okta 或 Entra 应用，需要把现有 Cursor 应用分配给工程以外的用户组，才能让他们访问，文中分别给出 Okta 与 Entra ID 的步骤；SCIM 仅限 Enterprise，Entra ID 的按组分配需要 P1 或 P2。另一项改动是在身份提供方里为 Bot 的计算机浏览器会话增加认证规则（Okta 中设备平台选 **Other Desktop**，Entra ID 中新建条件访问策略放行 Linux），因为这台 Linux 计算机不是托管设备，也未纳入 MDM；Okta FastPass 只有在按 Okta Verify and FastPass 页面设置后才能在计算机上运行，要求托管或合规设备的规则无论如何都会失败。这条规则只影响 Bot 在计算机浏览器里打开的、由身份提供方发放的应用，不影响 Grok Bot 登录或连接应用的登录。撤销用户在身份提供方的权限会终止其计算机内的应用会话，管理员也可随时终止成员的计算机。

**保留理由**：说明托管计算机在企业身份体系里的位置：登录走 Cursor SSO，而计算机内的登录不满足设备信任，因此要单独放行，对理解其与企业身份的关系有用。
