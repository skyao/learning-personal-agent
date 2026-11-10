---
title: "Microsoft Scout 负责任 AI 概述"
linkTitle: "文档：负责任AI概述"
date: 2026-08-21
originalTitle: "Responsible AI overview for Microsoft Scout"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [安全, 隐私]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-06-02"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：文档先说明 Microsoft 的 Responsible AI FAQ 用于帮助理解 AI 技术如何运作，并需考虑包含技术、使用者和部署环境的整个系统。随后列出 Microsoft Scout 的 AI 驱动功能：文件系统访问、shell 命令执行（三级权限）、浏览器自动化、代码与 CLI、Microsoft 365 集成、WorkIQ 查询、Heartbeat、Automations、委派、记忆与会话历史、操作批准、对话控制、隐私保护和 MIP 敏感度标签跟踪。文档指出 Scout 会展示每一步、在敏感操作前请求批准，并允许随时暂停、继续或取消，在工作区目录内按用户控制的权限运行。

**保留理由**：这是 Scout 负责任 AI 文档的入口，给出 AI 驱动功能的完整清单，并指向详细的 Responsible AI FAQ。

---

Microsoft Scout 负责任 AI 概述

[本文为预发布文档，可能会变更。]

重要

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能**抢先体验** Microsoft Scout。Frontier 让你直接接触 Microsoft 最新的 AI 创新。Frontier 预览受你客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是一项预览功能。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布之前提供，以便客户抢先体验并提供反馈。
- 更多信息，请访问我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

AI 系统不仅包括技术，还包括使用它的人、受它影响的人以及部署它的环境。Microsoft 的 Responsible AI FAQ 旨在帮助你理解 AI 技术如何运作、系统所有者和用户可以做出哪些影响系统性能和行为的选择，以及思考整个系统（包括技术、人员和环境）的重要性。你可以使用 Responsible AI FAQ 更好地理解 Microsoft 开发的特定 AI 系统和功能。

Responsible AI FAQ 是将 Microsoft 的 AI 原则付诸实践的更广泛努力的一部分。了解更多，请参阅 [Microsoft AI 原则](https://www.microsoft.com/ai/responsible-ai)。

## AI 驱动的功能

Microsoft Scout 包含一份不断增长的 AI 驱动功能清单。要了解特定功能的能力和影响，请查看下面的列表。

- **文件系统访问** - Microsoft Scout 根据你的自然语言指令，在你的工作区目录中读取、写入和搜索文件。
- **Shell 命令执行** - 在你的机器上以三级权限系统（自动批准、提示、拒绝）运行命令和脚本。
- **浏览器自动化** - 控制浏览器以浏览页面、填写表单、截取快照并检查网络流量。
- **代码与 CLI** - 使用 git、gh、curl 和 PowerShell 探索代码库、应用补丁、运行构建和测试，并调试失败。
- **Microsoft 365 集成** - 读取并管理你的电子邮件、日历、Teams 聊天、OneDrive 文件和会议。
- **WorkIQ 查询** - 跨 Microsoft 365 服务运行复杂查询，以综合来自多个来源的信息。
- **Heartbeat 模式** - 按可配置的日程在后台自主运行提示词。
- **Automations** - 独立执行按计划或条件触发的任务。
- **委派** - 启动专门的子智能体，用于并行研究、代码审查、构建和复杂的多步工作。
- **记忆与会话历史** - 跨对话记住偏好、决策和上下文，并从会话历史中回忆先前的工作。
- **操作批准** - Microsoft Scout 在执行敏感操作之前请求你的批准，例如发送电子邮件、在 Teams 中发帖或运行需要许可的命令。
- **对话控制** - 你可以随时暂停、继续或取消 Microsoft Scout 的进展。
- **隐私保护** - 外部内容（电子邮件和网页）被标记为不受信任，并作为数据处理，而不是指令。
- **敏感度标签跟踪** - 跟踪会话期间访问的内容上的 Microsoft 信息保护（Microsoft Information Protection，MIP）敏感度标签。

关于这些功能如何负责任地使用 AI 的详细信息，请参阅[Microsoft Scout 的负责任 AI FAQ](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq)。

## 关于 Microsoft Scout

Microsoft Scout 是一款面向 Windows 和 macOS 的桌面 AI 应用，可跨你的文件、shell、浏览器和 Microsoft 365 数据代你采取行动。你用自然语言描述你的需求，Microsoft Scout 完成这项工作——读写文件、运行命令、控制浏览器、查询你的 Microsoft 365 账户，并在后台自主工作。

Microsoft Scout 在工作时显示每一步，在敏感操作前请求你的批准，并让你随时暂停、继续或取消。它在你的工作区目录内运行，并遵守由你控制的细粒度权限系统。

## 相关内容

- [Microsoft Scout 概述](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout)
- [Microsoft Scout 常见问题](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- [Microsoft Scout 的负责任 AI FAQ](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq)
- [Microsoft AI 原则](https://www.microsoft.com/ai/responsible-ai)
