---
title: "Microsoft Scout（Frontier）概述"
linkTitle: "文档：产品概述"
date: 2026-08-21
originalTitle: "Microsoft Scout (Frontier) overview"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/overview"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [功能更新, 运行环境, 持续执行]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-08-05"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：Microsoft Scout 是面向 Windows 和 macOS 的桌面 AI 应用，可读写文件、运行 shell 命令、控制浏览器、查询 Microsoft 365 数据，并在后台自主运行；敏感操作需用户批准。文档列出文件、命令、浏览器、Microsoft 365、自主运行和子 agent 委派等能力，并介绍分级权限、Heartbeat（每 15–120 分钟一次的后台检查）、Automations、Co-Create 以及跨对话记忆。内置 skill 包括 Word、Excel、PowerPoint、Loop 和 Web Artifacts Builder，用户也可自行放入 SKILL.md 创建 skill。平台要求为 Windows 11 或更高版本、macOS 12 Monterey 或更高版本；使用需加入 Frontier 预览计划，属预览功能。

**保留理由**：这是 Scout 官方的产品能力总览与平台版本要求的出处，其他文档多只展开某一侧面。

---

Microsoft Scout（Frontier）概述

[本文为预发布文档，可能会变更。]

重要

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能**抢先体验** Microsoft Scout。Frontier 让你直接接触 Microsoft 最新的 AI 创新。Frontier 预览受你客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是一项预览功能。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布之前提供，以便客户抢先体验并提供反馈。
- 更多信息，请访问我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

Microsoft Scout 是一款面向 Windows 和 macOS 的桌面 AI 应用，可代你采取行动。它读写文件、运行 shell 命令、控制浏览器、查询你的 Microsoft 365 数据，并在后台自主工作。你在聊天对话中描述你的需求，Microsoft Scout 完成这项工作——敏感操作在执行前需经你批准。

## Microsoft Scout 能做什么？

Microsoft Scout 在单个桌面应用中结合本地和云端能力：

- **操作你的文件**：在工作区中创建、编辑和搜索文档。可处理 Word、Excel、PowerPoint、代码文件等。
- **运行命令**：借助分级权限系统执行 shell 命令、构建、测试和脚本。
- **自动化浏览器**：浏览网页、填写表单并与 Web 应用交互。
- **连接 Microsoft 365**：处理 Outlook 邮件和日历、Teams 会议和消息、SharePoint 列表，以及 OneDrive、SharePoint 和 Teams 中的文件。更多信息，请参阅[在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)。
- **自主工作**：按你定义的日程或触发器在后台运行。
- **委派工作**：启动专门的子智能体，用于并行研究、代码审查和复杂任务。

## 工作方式

1. **你在聊天界面中用自然语言描述任务**。
2. **Microsoft Scout 选择工具**并逐步推进，实时显示进度。
3. **你批准敏感操作**，之后才会执行（发送电子邮件、运行命令、写入文件）。
4. **Microsoft Scout 直接在对话中交付结果**，或将文件保存到你的工作区。

## 主要功能

### 本地与云端集成

Microsoft Scout 在你的桌面上运行，经许可访问你批准的文件系统和 shell，同时连接到你的 Microsoft 365 账户。这意味着它可以在你的工作区中编辑代码、运行构建、通过电子邮件发送结果，并安排后续会议——全都在一次对话中完成。

Microsoft Scout 还可以获取可用的 Teams 会议转录、预订会议室、处理 SharePoint 列表和 Outlook 收件箱规则，并帮助管理文件共享和访问权限。更多信息，请参阅[在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)。

### 细粒度权限

你通过详细的权限系统控制 Microsoft Scout 能做什么：

- 启用或禁用整个能力类别，例如文件系统、shell、浏览器和 Microsoft 365。
- 定义哪些 shell 命令自动批准，哪些需要你的许可。
- 标记始终需要明确批准的敏感目录。

### 自主模式

- **Heartbeat**：定期的后台检查（每 15–120 分钟一次），在你离开时运行提示词。
- **Automations**：按计划或条件触发的任务，独立执行。

### Co-Create（共同创建）

Co-Create 让你和 Microsoft Scout 同时编辑同一个受支持的文件，你所做的更改会自动合并。Co-Create 工作区可以存储在 OneDrive 或 SharePoint 中。更多信息，请参阅[与 Microsoft Scout 共同创建文件](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#co-create-files-with-microsoft-scout)。

### 记忆与委派

Microsoft Scout 会跨对话记住你的偏好和决定。对于复杂工作，它可以启动专门的子智能体并行运行，并在完成后报告结果。

## 内置技能

Microsoft Scout 包含用于常见任务的内置技能：

| 技能 | 作用 |
| --- | --- |
| Word、Excel、PowerPoint | 创建和编辑 Microsoft Office 文档 |
| Loop | 通过浏览器自动化编辑 Microsoft Loop 文档 |
| Web Artifacts Builder | 构建交互式 HTML 仪表板和可视化 |

你也可以通过把 `SKILL.md` 文件放入技能目录来创建自己的自定义技能。

## 平台

Microsoft Scout 作为桌面应用提供，适用于：

- **Windows**（Windows 11 或更高版本）
- **macOS**（macOS 12 Monterey 或更高版本）

## 后续步骤

- [开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started) — 安装、配置并运行你的第一个任务
- [使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout) — 全部能力的综合指南
- [在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)
- [Microsoft Scout 常见问题](https://learn.microsoft.com/en-us/microsoft-scout/faq) — 常见问题解答

## 相关内容

- [Microsoft Scout 的新功能](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
- [Microsoft Scout 负责任 AI 概述](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview)
