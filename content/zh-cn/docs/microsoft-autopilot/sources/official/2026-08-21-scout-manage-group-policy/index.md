---
title: "在 Intune 中管理 Microsoft Scout 的管理员控制项"
linkTitle: "文档：管理员策略清单"
date: 2026-08-21
originalTitle: "Manage admin controls in Intune for Microsoft Scout"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-10
tags: [安全, 持续执行]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-06-11"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。待翻译。

**内容摘要**：Microsoft Scout 通过 Windows Group Policy 和 Microsoft Intune 使用 ADMX/ADML 管理模板进行企业管理，策略为设备级，存放在 HKLM\SOFTWARE\Policies\Scout，标准用户无法修改。可管理的内容包括要求批准工具操作、阻止特定 tool server、限制权限类型、禁用 AI 模型或提供方、禁用 Heartbeat 与 Automations、将文件系统访问限制在工作区、阻止浏览器出口来源和控制 Frontier 访问。文档以表格列出各策略项、注册表值名称与类型，例如 DisabledServers、ForcePrompt、DisableHeartbeat、DisableWorkflows、RestrictToWorkspace。

**保留理由**：这是管理员可用策略项及其注册表值的完整清单，其他管理文档只讲接入与部署。
