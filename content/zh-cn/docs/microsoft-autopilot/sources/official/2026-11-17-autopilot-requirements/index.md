---
title: "Autopilot（Frontier）要求"
linkTitle: "文档：使用要求"
date: 2026-11-17
originalTitle: "Autopilot (Frontier) requirements"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/requirements"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [开放与价格, 运行环境, 安全]
products: [microsoft-autopilot]
updatedAt: "2026-11-17"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-17。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：列出在 Microsoft Copilot 中使用 Autopilot 的前提：无需在设备上单独安装代理，默认关闭；责任人须有 Microsoft 365 Copilot 许可证并开启消费计费，需由支出策略覆盖，Copilot 许可证不含 Autopilot 用量，每个启用用户可创建一个 Autopilot。必需的安全能力为 Microsoft Entra Agent ID（自动预配）、Microsoft local (MXC) 隔离执行环境（需 Intune Plan 1 或 Microsoft 365 E3）和 Microsoft 365 审计日志；另有强烈建议与有限预览的能力。可用性初期限于美国的部分 Frontier 客户，针对英语优化，且文档称 Autopilot 的云端计算机与本地设备分离，不应把早期桌面预览的说明当作云端体验的设置要求。

**保留理由**：给出云端 Autopilot 的许可证、计费与安全能力前提清单，并明确区别于早期桌面预览，与 MC1479277 的 UBB 前提和旧 Scout 的 Intune、GitHub Copilot 许可证要求相比，新增了 Entra Agent ID、MXC 等必需安全能力和美国限定。

---

Autopilot（Frontier）要求

[本文档为预发布文档，可能变更。]

重要

- 访问 Autopilot（Frontier）需要加入适用的 **[Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)**、获得预览分配并同意参与条款。仅加入 Frontier 并不会启用每一项预览功能。Frontier 预览受客户协议中适用的预览条款约束，其可用性与能力可能变化。
- 此功能处于预览阶段。
- 预览功能可能功能受限，且未必会正式发布。这些功能在正式发布之前提供，以便客户提前访问并反馈意见。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

本文介绍在 Microsoft Copilot 中使用 Autopilot 的前提条件。你无需在设备上单独安装代理。Autopilot 默认关闭。仅加入 Frontier 并不能让 Autopilot 可用；你的管理员还需要为 Autopilot 授予许可、设置支出策略并激活它。

## 账户与许可

Autopilot 的责任人，即智能体所分配到的负责用户，必须拥有 Microsoft 365 Copilot 许可证并开启消费计费。可用性初期限于美国符合条件的客户。

| 要求 | 详情 |
| --- | --- |
| Microsoft 365 工作或学校账户 | 与你的组织关联的账户。不支持个人 Microsoft 账户。 |
| Microsoft 365 Copilot 许可证 | 分配给负责用户的有效 [Microsoft 365 Copilot 许可证](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-licensing)。 |
| 预览访问 | 你的组织必须将你加入 Frontier，并为你或你所在的组激活 **Autopilot（Frontier）**。由你的管理员确认分配。 |
| 支出策略 | Autopilot 按用量以 Copilot Credits 计费。你的组织必须开启按用量计费，且你必须被包含 Autopilot 的支出策略覆盖。如果你未被覆盖，或策略达到限额，Autopilot 对你不可用。Copilot 许可证不含 Autopilot 用量。更多信息见[查看用量与限额](https://learn.microsoft.com/en-us/copilot/autopilot/using#review-usage-and-limits)。 |

每个启用的用户可创建一个 Autopilot。

## 安全要求与建议

在用户使用 Autopilot 之前，你的组织必须具备所需的 Microsoft 安全能力。另有强烈建议的附加能力，而最安全的配置还会加入处于有限预览的控件。本许可与控件指南适用于 Frontier 公开预览。正式发布时可能适用额外要求与安全建议。

### 必需的安全能力

以下能力是 Autopilot 所必需的。

| 能力 | Microsoft 解决方案 | 许可 |
| --- | --- | --- |
| 身份平台 | Microsoft Entra Agent ID | 自动预配。 |
| 隔离执行环境 | Microsoft local (MXC) | Microsoft Intune Plan 1 或 Microsoft 365 E3 |
| 不可变审计日志与成本管理 | Microsoft 365 审计日志 | 任意 Microsoft 365 商业许可证 |

### 强烈建议的安全能力

Microsoft 强烈建议以下能力，用于治理访问、保护数据并检测威胁。

| 能力 | Microsoft 解决方案 | 许可 |
| --- | --- | --- |
| 访问与授权治理 | 用于最小特权访问的 Microsoft Entra ID Governance、用于工具与数据检查的 Microsoft Entra Global Secure Access，以及 Microsoft Entra Conditional Access | Microsoft Entra Suite |
| 数据安全与内部风险 | Microsoft Purview 数据丢失防护与 Microsoft Purview 内部风险管理 | Microsoft Purview Suite 或 Microsoft 365 E5 |
| 威胁防护 | Microsoft Defender XDR | Microsoft Defender Suite 或 Microsoft 365 E5 |

### 最安全的配置

要获得最安全的配置，请加入以下智能体安全能力。这些能力处于有限预览。

- Microsoft Perception
- Microsoft Entra Conditional Access 动态控件
- Microsoft Entra ID Governance 动态权限

## 访问

| 要求 | 详情 |
| --- | --- |
| Microsoft Copilot | 在 Web 上登录 [copilot.cloud.microsoft](https://copilot.cloud.microsoft)，或在 Microsoft Copilot 桌面应用中使用组织账户登录。Autopilot 出现在左侧导航的 **主页** 标签页。 |
| Microsoft Teams | 设置完成后，Autopilot 可以通过 Teams 中的一对一私聊联系你，用于更新、提问与审批。 |
| 移动应用 | 在 iOS 与 Android 上，你可以通过 Microsoft 365 Copilot、Microsoft Teams 与 Microsoft Outlook 应用使用 Autopilot。使用工作账户登录。 |
| 功能与提供商访问 | 必需的智能体与 AI 提供商设置必须允许该体验。Frontier 不会覆盖这些控件。更多信息见[为组织配置 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure)。 |
| 任务特定访问 | 执行账户需要对任务所用的邮件、日历、对话、文件、工具与目标位置拥有权限。技能与例程不会授予访问权。 |
| Microsoft Edge（可选） | 要让 Autopilot 在浏览器中工作（在已启用的情况下），Microsoft Edge 必须在你设备上打开、使用工作账户登录，并已连接到 Autopilot。见[在 Microsoft Edge 浏览器中工作](https://learn.microsoft.com/en-us/copilot/autopilot/edge)。 |

Autopilot 的云端计算机与你的本地设备分离，Autopilot 无法访问你的本地文件夹或应用。不要把早期桌面预览的说明当作云端体验的设置要求。

## 可用性

可用性初期限于美国部分符合条件的 Frontier 客户，新的 Frontier 租户会陆续推出。支持的语言、访问方式与各项功能可能因预览分配而异。Autopilot 针对英语优化。有本地化界面并不代表每种语言或工作流都已评估。在依赖它之前，先确认你组织支持的配置。

后台工作依赖已授权的访问与可用的服务。待处理的审批、缺失的权限或服务问题都可能阻塞计划中的运行。不保证执行不中断或在特定时间完成。

关于当前的能力指引，见 [Autopilot 概述](https://learn.microsoft.com/en-us/copilot/autopilot/overview)与[应用卡片](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)。

## 相关内容

- [Autopilot 入门](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)
- [为组织配置 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure)
- [Autopilot 概述](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [Autopilot 常见问题](https://learn.microsoft.com/en-us/copilot/autopilot/faq)
