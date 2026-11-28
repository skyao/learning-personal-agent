---
title: "消息中心 MC1557730：Autopilot 在 Frontier 推出"
linkTitle: "MC1557730"
date: 2026-11-17
originalTitle: "MC1557730 - Autopilot availability in Frontier"
sourceUrl: "https://admin.microsoft.com/#/MessageCenter/:/messages/MC1557730"
altUrls: ["https://m365admin.handsontek.net/?p=26391"]
author: "未署名"
publisher: "Microsoft 365 消息中心"
language: en
fidelity: 转载全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [开放与价格, 安全, 隐私, 运行环境]
products: [microsoft-autopilot]
reprintUrl: "https://mc.merill.net/message/MC1557730"
dateNote: "存档站显示 Published Nov 17, 2026"
---

{{< source-info >}}

**收录说明**：Microsoft 365 管理中心的消息中心公告，原文需管理员登录，依据第三方存档站 mc.merill.net 的完整转录存档。删去了存档站的导航、讨论区与相关帖。已翻译。

**内容摘要**：MC1557730 于 2026-11-17 发布，称 Autopilot 从当天起在 Frontier Public 分阶段推出，租户启用前给管理员 24 小时通知。Autopilot 是常驻云端的个人智能体，有自己的账号与身份、存储和邮箱、远程计算机；默认关闭，管理员须在 MAC 开启访问、设置 Copilot Credits 计费策略并为安全组启用，负责的用户需有 Microsoft 365 Copilot 许可和消耗计费，初期限合格的美国客户。必需控制为 Microsoft Entra Agent ID、隔离运行环境 Microsoft local (MXC)、Microsoft 365 审计日志与 Agent 365 成本管理，另有强烈推荐与最安全配置的控制项。合规部分指出本版本记忆始终开启、Microsoft 365 Copilot 个性化设置不适用、部分操作可无需单独确认，且 Autopilot 对话暂不受 eDiscovery、保留或法律保留覆盖。

**保留理由**：管理员视角的官方准入与合规细节：默认关闭、仅限美国、必需控制清单、24 小时通知，以及记忆始终开启和对话未纳入 eDiscovery 的限制。这些在已收的 MC1479277、MC1546354 中没有。

---

MC1557730 - Autopilot 在 Frontier 推出

消息中心

### 摘要

Autopilot 将从 2026 年 11 月 17 日起在 Frontier Public 推出，它是一个常驻的云端智能体，需要管理员启用并具备 Microsoft 365 Copilot 许可。它拥有自己的身份、安全控制与合规考量。管理员必须配置访问与计费；用户通过 Copilot 主页创建 Autopilot。

[讨论](#discussion)由 zap.ms 提供支持

[### 消息 ID

MC1557730

在消息中心查看](https://admin.microsoft.com/#/MessageCenter/:/messages/MC1557730)

### 发布日期

2026 年 11 月 17 日

### 服务

Microsoft Copilot（Microsoft 365）

### 标签

新功能

用户影响

管理员影响

### 更多信息

**是什么、为什么：**

Autopilot 将于 2026 年 11 月 17 日在 Frontier Public 内开始分阶段推出。在租户中启用 Autopilot 之前，我们会给管理员 24 小时通知。

Autopilot 是一个常驻的、基于云的个人智能体，它替你分担工作，并让委托的目标随时间持续推进，而不是一次只处理一个提示词。

Autopilot 有自己的账户与身份、存储和邮箱，以及自己的远程计算机。访问控制、审批护栏以及受支持的信息保护与合规能力，有助于让委托的工作保持在批准的边界内。

**推出时间表：**

- Frontier Public 推出于 2026 年 11 月 17 日开始。
- Autopilot 分阶段向符合条件的客户推出。
- 正式可用时间将另行确认。

**对你的组织的影响：**

**谁受影响**

- 已加入 Frontier 的组织
- Microsoft 365 管理员
- 满足许可与管理员配置前提的最终用户

**平台 / 服务**

- Microsoft 365
- Microsoft Copilot

**将会发生什么**

- Autopilot 将陆续向已加入 Frontier 的租户提供
- Autopilot 默认关闭，除非管理员完成必需的启用步骤，否则不可用
- 除非满足所有管理员前提，否则用户无法创建 Autopilot

**需要采取的行动 / 建议：**

**前提条件**

Autopilot 的责任人（即智能体所分配到的负责用户）必须拥有 Microsoft 365 Copilot 许可证并开启消费计费。可用性初期限于符合条件的美国客户。

 此外，需要以下控制项：

- **身份平台：** Microsoft Entra Agent ID。自动预配。
- **隔离运行时环境：** Microsoft local (MXC)
- **不可变审计日志与成本管理：** Microsoft 365 审计日志与 Agent 365 成本管理。

强烈建议以下控制项：

- **访问与授权治理：** Microsoft Entra ID Governance（最小特权访问）、Microsoft Entra Global Secure Access（工具、MCP 与数据检查），以及 Microsoft Entra Conditional Access。
- **数据安全与内部风险：** Microsoft Purview 数据丢失防护与 Microsoft Purview 内部风险管理。
- **威胁防护：** Microsoft Defender XDR 与 Dynamic Agent Risk。

要获得最安全的配置，还建议以下控制项：

- **智能体安全：** Microsoft Perception（有限预览）、Microsoft Entra Conditional Access 动态控件（有限预览）、Microsoft Entra ID Governance 动态权限（有限预览）

本许可与控件指南适用于 Frontier 公开预览。正式可用时可能适用额外要求与安全建议。

 我如何从 Microsoft 获得这些必需与强烈建议的能力？

1. **必需的 Microsoft 安全能力：** Intune P1/ME3、任意 Microsoft 365 商业许可证
2. **强烈建议的 Microsoft 安全能力：** Entra Suite、Purview Suite/ME5、Defender Suite/ME5、Agent 365 付费许可证
3. **最安全的配置：** 按用户计费

**管理员操作（必需）**

- 管理员在 MAC（Microsoft 365 管理中心）中开启对 Autopilot 的访问
- 管理员设置 Copilot Credits 计费策略
- 管理员为一个安全组启用 Autopilot

**用户操作**

- 在 Copilot 主页体验的左侧面板中进入 Autopilot，选择「创建你的 Autopilot」
- 在 Teams、Copilot 应用或 Outlook 中与你的 Autopilot 交流

**建议**

- 在启用之前，与安全与合规相关方一起审阅此变更

**合规考量**

Autopilot 默认关闭。管理员通过 Microsoft 365 管理中心和安全组分配控制访问。Autopilot 有自己的身份；代用户执行的工作使用该用户的权限。自动化检查会审阅有后果的操作，但有些操作可以无需单独确认就继续。

 在启用此 Frontier 预览之前，请与你的安全与合规团队一起审阅 Autopilot 文档。本版本中记忆始终开启，Microsoft 365 Copilot 个性化设置不适用。数据保护与审计能力有预览限制；Autopilot 对话尚未纳入 eDiscovery、保留或法律保留的覆盖范围。
