---
title: "开始使用 Microsoft Scout"
linkTitle: "文档：快速入门"
date: 2026-08-21
originalTitle: "Get started with Microsoft Scout"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/get-started"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [运行环境, 安全, 连接器]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-08-05"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：文档列出使用前提：组织的 Microsoft 365 工作或学校账户（不支持个人账户）、Microsoft 365 Copilot 许可、Windows 上最新的 Visual C++ redistributable、本地管理员权限（含 Intune 账户）以及 GitHub Copilot Business 或 Enterprise 许可。步骤包括安装、登录 Microsoft 365 与 GitHub（可选 GitHub Enterprise Cloud 主机）、设置工作区目录、连接 Microsoft 365 并发起第一次对话。默认设置为 WorkIQ connectivity 开、Shell access 开、Auto-approve 关；权限分 Auto-approve、Prompt、Deny 三级。文档还介绍了 Settings 中的主要分组。

**保留理由**：这是安装、登录前提与默认权限设置的官方来源，列出了许可证和账户要求。

---

开始使用 Microsoft Scout

[本文为预发布文档，内容可能变更。]

重要事项

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能获得 Microsoft Scout 的**早期访问**。Frontier 让你直接接触 Microsoft 最新的 AI 创新。Frontier 预览受客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是一项预览功能。
- 预览功能的功能可能受限，且可能不会正式发布。这些功能在正式发布之前提供，以便客户提前访问并提供反馈。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

Microsoft Scout 是一个桌面 AI 应用，可在你的文件、shell、浏览器、开发工具和 Microsoft 365 数据之间采取行动。本文引导你完成安装、登录和第一次对话。

## 先决条件

开始之前，请确保你具备：

- **受支持的平台**：Windows 11 或 macOS 12（Monterey）或更高版本。
- **与你的组织关联的 Microsoft 365 工作或学校账户**：不支持个人 Microsoft 账户。
- **Microsoft 365 Copilot 访问权限**：已为你的账户分配有效的 [Microsoft 365 Copilot 许可证](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-licensing)。
- **Microsoft Visual C++ 可再发行组件（仅 Windows）**：最新的 [Microsoft Visual C++ 可再发行组件](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)库。
- **本地管理员权限**：在你的机器上安装应用的权限，包括启用了 Intune 的账户。
- **GitHub Copilot Business 或 Enterprise 许可证**：用于访问 Copilot 订阅。了解如何[为你的组织设置 GitHub Copilot](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-organization)。

你的 IT 管理员还需要在你登录之前完成 Microsoft Scout 访问设置。详情请参阅 [Microsoft Scout 的管理员访问概述](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)。

## 安装 Microsoft Scout

[下载并安装适用于 Windows 或 macOS 的 Microsoft Scout 安装程序](https://aka.ms/msscout)。

运行安装程序并按照屏幕提示操作。安装后，Microsoft Scout 会出现在你的应用程序菜单中。

## 登录

1. 打开 Microsoft Scout。
2. 选择 **Sign in to Microsoft 365**。
3. 使用你的组织 Microsoft 365 凭据进行身份验证。
4. 在提示时授予所请求的权限。
5. 如果你的组织使用 GitHub Enterprise Cloud，请开启 **Use a GitHub Enterprise host** 并输入你的企业主机（例如 `your-org.ghe.com`）。留空则在 github.com 上登录。
6. 选择 **Sign in to GitHub**，并使用拥有 Business 或 Enterprise GitHub Copilot 许可证的 GitHub 账户登录。在提示时于浏览器中完成登录。

Microsoft Scout 使用你组织的 Microsoft 365 身份安全地为你登录。你的组织的身份提供方管理你的凭据。

## 配置工作区

登录后，Microsoft Scout 会要求你设置工作区目录。这个文件夹是 Microsoft Scout 读写文件的位置。

1. 选择一个工作区目录，或接受默认位置。
2. 查看初始权限配置。

你稍后可以在 **Settings** 中更改工作区目录。

提示

选择一个你用于进行中项目的目录。Microsoft Scout 在该目录内运行，因此它可以创建文档、运行脚本并整理文件。

## 选择个性（可选）

Microsoft Scout 提供可改变其对话风格的个性预设。默认个性是有帮助且专业的——适合大多数用户。你可以随时使用提示输入框旁的应用图标切换。

## 连接到 Microsoft 365

要访问你的 Microsoft 365 数据（电子邮件、日历、Teams 和 OneDrive）：

1. 打开 **Settings**。
2. 选择 **Sign in to Microsoft 365** 并完成身份验证流程。

连接后，Microsoft Scout 可以帮助你在 Microsoft 365 内容之间工作。它可以读取、起草和管理电子邮件、日历事件、Teams 聊天和 OneDrive 文件。发送、共享、回复、转发或更新他人可见信息的操作，在执行前需要你确认。

## 开始你的第一次对话

1. 选择窗口底部的聊天输入框。
2. 输入你想完成的事情。例如：
   - 「创建一份 Word 文档，总结我本周的电子邮件。」
   - 「明天找一个空闲时间，与 Alex 开一个 30 分钟的会议。」
   - 「为我明天的会议准备一份简报。」
   - 「在我的工作区中搜索提到季度回顾的文件。」
3. 按 **Enter** 或选择 **Send**。

Microsoft Scout 开始工作，并在对话中显示进度，包括操作、权限提示、创建的文件和最终结果。

提示

明确说明你想要什么。不要说「帮我处理电子邮件」，而要说「为 Sarah 关于预算审查的邮件起草一封回复，感谢她并确认我将参加周四的会议。」

## 查看默认设置

Scout 配置了以下默认值：

- **WorkIQ connectivity: ON**\
  开箱即用，可在你的 Microsoft 365 数据中进行搜索。
- **Shell access: ON**\
  允许 Microsoft Scout 请求执行终端命令。操作仍遵循权限系统，可能需要批准。
- **Auto-approve: OFF**\
  所有操作都需要用户确认。必须按能力显式启用自动批准。

## 了解权限

在 Microsoft Scout 工作时，某些操作可能需要你的批准。权限系统有三个级别：

| 级别 | 会发生什么 |
| --- | --- |
| Auto-approve | 如果配置明确允许，操作会自动运行。 |
| Prompt | Microsoft Scout 暂停并向你展示它想做什么。你批准或拒绝。 |
| Deny | 操作被阻止。危险命令默认使用此级别。 |

当批准提示出现时：

1. 查看 Microsoft Scout 想做什么。
2. 选择 **Approve** 允许操作，或选择 **Deny** 阻止操作。
3. 可选：选择 **Always allow**，以便将来自动批准类似操作。

你可以随时在 **Settings** > **Permissions** 中自定义权限。

## 查看结果

Microsoft Scout 使用富 Markdown 直接在对话中呈现结果：标题、表格、带语法高亮的代码块、Mermaid 图表和内联图片。Microsoft Scout 创建的文件会保存到你的工作区目录。

要找到 Microsoft Scout 创建的文件：

1. 检查你的工作区目录中是否有新文件。
2. 图片和视觉产物可能会内联出现在对话中，作为文件创建时也会保存到你的工作区。如果你查看原始消息，内联图片可能会显示为指向已保存文件的 Markdown 图片链接。
3. 文档（Word、Excel、PowerPoint）会保存到你的工作区，并可在其原生应用中打开。

## 探索设置

打开 **Settings** 配置 Microsoft Scout。Settings 是一个单一的分组窗口，顶部有搜索框，因此你可以通过输入选项名称来查找。主要分组包括：

- **Appearance**：主题（浅色、深色或系统）
- **Default model**：选择使用哪个 AI 模型
- **Default reasoning effort**：设置模型默认的推理量
- **Workspace directory**：更改文件保存位置
- **Permissions**：控制工具访问和 shell 命令
- **Integrations**：连接 Microsoft Scout 所使用的服务
- **Memory**：查看和管理已存储的偏好
- **Privacy, Cloud sync, Power management, Window behavior**：其他自定义选项

有关详细配置说明，请参阅[配置工具组](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#configure-tool-groups)。

## 后续步骤

- [使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout) —— 所有能力的综合指南
- [使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365) —— 使用会议、邮件、列表和文件
- [Microsoft Scout 概述](https://learn.microsoft.com/en-us/microsoft-scout/overview) —— 功能摘要和产品概述

## 相关内容

- [Microsoft Scout 概述](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [Microsoft Scout 常见问题](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- [Microsoft Scout 新功能](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
- [Microsoft Scout 的负责任 AI 概述](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview)
