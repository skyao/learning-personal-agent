---
title: "使用 Intune 设置 Microsoft Scout"
linkTitle: "文档：Intune 部署"
date: 2026-06-18
originalTitle: "Set up Microsoft Scout with Intune"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-10
tags: [安全, 运行环境]
products: [microsoft-autopilot]
updatedAt: "2026-06-18"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-06-02"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。原文中多处图片位于 images/。待翻译。

**内容摘要**：文档面向 Frontier 客户的 Intune 管理员，说明如何为受管用户启用 Microsoft Scout。关键设置是 Windows ADMX 策略中的 Allow Microsoft Scout Frontier access（对应 AllowScoutFrontierAccess），未启用或未配置时，用户可能看到 waitlist 画面而无法登录。流程分三部分：导入 microsoft-scout.admx 和 microsoft-scout.adml、创建 Windows 配置策略并分配，以及用 microsoft-scout.mobileconfig 创建 macOS 自定义配置文件（Device channel）。文档给出验证步骤和排障表，并提示部分预发布模板与截图仍显示内部名称 Clawpilot。

**保留理由**：这是 Intune 逐步部署流程与所需模板文件的官方来源，并含 macOS 配置文件做法及内部名称 Clawpilot 的说明。
