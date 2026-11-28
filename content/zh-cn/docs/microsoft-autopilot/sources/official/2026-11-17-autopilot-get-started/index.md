---
title: "Autopilot（Frontier）入门"
linkTitle: "文档：入门指南"
date: 2026-11-17
originalTitle: "Get started with Autopilot (Frontier)"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/get-started"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [运行环境, 交互渠道, 持续执行]
products: [microsoft-autopilot]
updatedAt: "2026-11-17"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-10。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：引导用户打开 Autopilot、创建自己的 Autopilot 并运行第一个任务。前提是工作或学校账号（不支持个人 Microsoft 账号）、Microsoft Copilot 许可证和 Frontier 预览注册，管理员还需授权、用支出策略覆盖并激活。每人只能有一个 Autopilot，创建时选择名称与外观并确认建议的起始例程，预配约需 10 到 30 分钟，完成后通过邮件和 Teams 通知；就绪后用户审阅它从近期工作中推断出的人员、职责与周期性承诺，选择 Looks good 确认。可在 Microsoft Copilot 网页或桌面应用、Teams 一对一私聊、iOS 与 Android 上的 Microsoft 365 Copilot、Teams、Outlook 应用中使用；符合请求的动作无需审批卡，其余及所有付款需 Allow 或 Deny。

**保留理由**：提供云端 Autopilot 的创建流程、10 到 30 分钟预配、入口和渠道等用户视角细节，已收的旧 Scout 文档是桌面应用安装流程，没有这些。

---

Autopilot（Frontier）入门

[本文为预发布文档，内容可能变更。]

重要

- 访问 Autopilot（Frontier）需要完成相应的 **[Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)** 注册、预览分配并接受参与条款。仅完成 Frontier 注册并不会启用每一项预览功能。Frontier 预览受你的客户协议中适用的预览条款约束，其可用性与功能可能变化。
- 此功能处于预览阶段。
- 预览功能可能功能受限，并且可能不会正式发布。这些功能在正式发布之前提供，以便客户提前使用并提供反馈。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

本文带你打开 Autopilot、创建你的 Autopilot，并运行第一个任务。

## 先决条件

开始之前，请确认你具备：

- 与你的组织关联的 Microsoft 365 工作或学校账户。不支持个人 Microsoft 账户。
- Microsoft Copilot 访问权限——分配到你账户的有效 [Microsoft Copilot 许可证](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-licensing)。
- Frontier 预览注册——Autopilot 通过 [Frontier 计划](https://adoption.microsoft.com/copilot/frontier-program/)提供。Autopilot 默认关闭。你组织的管理员为 Autopilot 授权、用支出策略覆盖按用量计费，并为你激活 Autopilot。

请在 [Autopilot 要求](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)中确认其他资格条件与任务特定的访问权限。

## 打开 Autopilot

1. 使用你的工作或学校账户登录 [copilot.cloud.microsoft](https://copilot.cloud.microsoft)，或打开 Microsoft Copilot 桌面应用。
2. 选择**主页（Home）**，然后在左侧导航中选择 Autopilot。设置完成后，该入口会显示你的 Autopilot 名称。

如果 Autopilot 没有出现在导航中，请让管理员检查你的访问权限。仅完成 Frontier 注册并不能让 Autopilot 可用；管理员还需为其授权、用支出策略覆盖，并激活它。

## 创建你的 Autopilot

你只能有一个 Autopilot。如果还没有，请选择**创建你的 Autopilot（Create your Autopilot）**并按提示操作。

1. 选择名称和外观。同事会在 Microsoft Copilot、Microsoft Teams 和 Outlook 中看到它们。
2. 查看建议的起始例程（routine）。用复选框接受或拒绝。
3. 随后 Autopilot 会自动预配。

预配可能需要 10 到 30 分钟。你可以在它完成期间离开页面。Autopilot 就绪时，你会收到一封邮件和一条 Teams 通知。

就绪后，请审阅 Autopilot 从你近期工作中推断出的人员、职责和周期性承诺。把这份档案当作初稿。选择**看起来不错（Looks good）**接受它，或在依赖它之前修改或重置任何不准确的地方。

设置完成后，你的 Autopilot 名称会出现在左侧导航的**主页**标签页上。选择它的名称即可打开你的主对话。要查看它的工作或设置，请展开右上角的管理面板。

## 可以在哪里使用 Autopilot

你可以在以下位置使用 Autopilot：

- **Microsoft Copilot** —— 在网页或桌面应用中，于左侧导航的**主页**标签页选择你的 Autopilot 名称。
- **Microsoft Teams** —— Autopilot 与你进行一对一的私聊，用于更新、提问，以及需要你的上下文或批准的决定。
- **移动端** —— 在 iOS 和 Android 上，用 Microsoft 365 Copilot、Teams 或 Outlook 应用查看进度、添加指令或改变方向。

## 运行你的第一个任务

从一个有边界的请求开始，不要发送消息，也不要更改共享信息。

1. 在左侧导航中选择你的 Autopilot 名称，打开你的主对话。
2. 在输入框中描述结果、相关来源和限制。例如「总结本周的上线讨论，并为评审起草一份议程。不要发送消息，也不要更改日历事件。」
3. 用发送控件提交消息。
4. 回答任何澄清性问题。在回应之前，查看它请求的操作与批准项。
5. 对照来源检查结果。如果你要求保存文件，请打开最终链接，核实其位置和访问权限。

Autopilot 不会要求你批准每一步。与你的请求相符的操作可以不经批准卡片直接运行；其他操作以及所有付款，都会等待你选择**允许（Allow）**或**拒绝（Deny）**。详情请参阅[设置权限](https://learn.microsoft.com/en-us/copilot/autopilot/approval#set-permissions)。

## 查看活动与设置

选择**活动（Activity）**标签页。用**正在进行（Working now）**找到进行中的工作，用**需要你的输入（Needs your input）**找到需要你关注的请求。

选择**设置**标签页，查看你的 Autopilot 的名称、外观、记忆和计算机。选择你的 Autopilot 名称可更改其名称和外观。

## 相关内容

- [使用 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/using)
- [Autopilot 场景](https://learn.microsoft.com/en-us/copilot/autopilot/scenarios)
- [Autopilot 概述](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [Autopilot 要求](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)
- [Autopilot 常见问题](https://learn.microsoft.com/en-us/copilot/autopilot/faq)
- [Autopilot 的应用卡片](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)
