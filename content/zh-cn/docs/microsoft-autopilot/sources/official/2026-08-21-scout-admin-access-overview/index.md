---
title: "Microsoft Scout 管理员访问概述"
linkTitle: "文档：管理员访问概述"
date: 2026-08-21
originalTitle: "Admin access overview for Microsoft Scout"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-10
tags: [安全, 隐私, 运行环境]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-08-21"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。待翻译。

**内容摘要**：Microsoft Scout 仅在 Microsoft Frontier 中提供，访问需要两道关口都完成。第一道在 Microsoft 365 admin center 的 Copilot Frontier 中设置 No access、All users 或 Specific users，保存后约需三小时生效；第二道包括 Intune 策略、Frontier 组织注册（attestation）表单，以及按需分配 GitHub Copilot 许可。由于数据可能经 GitHub 流向第三方推理路径，管理员必须明确声明并选择加入。用户登录要求 GitHub Copilot Business 或 Enterprise 席位，并且组织或企业策略允许 GitHub Copilot app；自 2026 年 7 月 27 日起该 app 有独立策略（app 1.1 版本引入）。文档还给出报错信息与对应的管理员处理方法。

**保留理由**：这是两道管理员关口、GitHub Copilot 策略前提以及数据可能流向 GitHub 的出处，用来解释用户为何无法登录。
