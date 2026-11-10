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
translation: 已翻译
collectedAt: 2026-11-10
tags: [安全, 持续执行]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-06-11"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：Microsoft Scout 通过 Windows Group Policy 和 Microsoft Intune 使用 ADMX/ADML 管理模板进行企业管理，策略为设备级，存放在 HKLM\SOFTWARE\Policies\Scout，标准用户无法修改。可管理的内容包括要求批准工具操作、阻止特定 tool server、限制权限类型、禁用 AI 模型或提供方、禁用 Heartbeat 与 Automations、将文件系统访问限制在工作区、阻止浏览器出口来源和控制 Frontier 访问。文档以表格列出各策略项、注册表值名称与类型，例如 DisabledServers、ForcePrompt、DisableHeartbeat、DisableWorkflows、RestrictToWorkspace。

**保留理由**：这是管理员可用策略项及其注册表值的完整清单，其他管理文档只讲接入与部署。

---

在 Intune 中管理 Microsoft Scout 的管理员控制项

[本文为预发布文档，内容可能变更。]

重要

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能获得 Microsoft Scout 的**早期访问**权限。Frontier 让你直接接触 Microsoft 最新的 AI 创新。Frontier 预览受你客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是预览功能。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布前提供，以便客户提前访问并提供反馈。
- 有关详细信息，请访问我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

Microsoft Scout 通过 Windows 组策略和 Microsoft Intune，使用管理模板（Administrative Template，ADMX/ADML）文件支持企业管理。这些策略是设备范围的，存储在 `HKLM\SOFTWARE\Policies\Scout` 下。由于策略在设备级别管理，标准用户无法修改它们。

## 可用的管理员控制项

管理员可以使用这些策略管理 Microsoft Scout 的功能和能力，包括：

- 要求对工具操作进行批准
- 阻止特定的工具服务器（tool server）
- 限制权限类型
- 禁用 AI 模型或提供方
- 禁用 Heartbeat 与 Automations
- 将文件系统访问限制在工作区
- 阻止浏览器出口（egress）目标
- 控制 Frontier 访问

## 策略参考

以下策略设置可用。

| 策略设置 | 注册表值 | 类型 | 描述 |
| --- | --- | --- | --- |
| 策略版本 | `PolicyVersion` | `REG_DWORD` | 存储策略架构版本，用于诊断和未来的迁移。 |
| 禁用的工具服务器 | `DisabledServers` | `REG_SZ` | 以逗号分隔的、要阻止的工具服务器键列表，例如 `filesystem`、`playwright` 或 `WorkIQ`。 |
| 禁用的权限类型 | `DisabledPermissions` | `REG_SZ` | 以逗号分隔的、要拒绝的权限类型列表，例如 `shell`、`write`、`mcp`、`url` 或 `custom-tool`。 |
| 对所有非读取操作强制人工批准 | `ForcePrompt` | `REG_DWORD` | 要求每个非读取的工具操作都经用户批准，无论本地批准设置如何。 |
| 禁用的 AI 模型 | `DisabledModels` | `REG_SZ` | 以逗号分隔的、要阻止的模型 ID 列表。 |
| 禁用的 AI 模型提供方 | `DisabledProviders` | `REG_SZ` | 以逗号分隔的、要阻止的提供方名称列表，例如 `anthropic` 或 `openai`。 |
| 禁用 Heartbeat | `DisableHeartbeat` | `REG_DWORD` | 禁用 Heartbeat 监控功能。 |
| 禁用 Automations | `DisableWorkflows` | `REG_DWORD` | 阻止用户创建或运行自动化（automation）。 |
| 将文件系统访问限制在工作区 | `RestrictToWorkspace` | `REG_DWORD` | 将文件系统和 shell 访问限制在当前工作区目录。 |
| 阻止的浏览器出口来源 | `BrowserEgressBlockedOrigins` | `REG_SZ` | 以逗号分隔的、被阻止用于浏览器自动化流量的 HTTP 或 HTTPS 来源（origin）列表。 |

## 相关内容

- [Microsoft Scout 管理员访问概述](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)
- [使用 Intune 设置 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)
- [开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Microsoft Scout 常见问题](https://learn.microsoft.com/en-us/microsoft-scout/faq)
