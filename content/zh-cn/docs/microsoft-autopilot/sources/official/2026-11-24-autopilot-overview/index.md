---
title: "Autopilot（Frontier）概述"
linkTitle: "文档：产品概述"
date: 2026-11-24
originalTitle: "Autopilot (Frontier) overview"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/overview"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [功能更新, 运行环境, 持续执行]
products: [microsoft-autopilot]
updatedAt: "2026-11-24"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-10。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：Autopilot 被描述为 Microsoft Copilot 中常驻的云端智能体：用户描述目标、来源和边界，它可准备文档、查看可访问的对话、跟进工作，并通过自动化运行周期任务。它有自己的工作身份、记忆、计算机和工作区，每人一个，设备关机时也能运行计划任务。用户在网页或桌面版 Copilot 的 Home 标签左侧导航里按名字找到它，并通过 Teams 一对一私聊接收更新、问题和审批。它有自己的邮箱和日历，可把草稿共享到用户的 OneDrive 文件夹，也可使用 Microsoft To Do 和 Planner 的共享任务；Routines 可按计划或事件触发。右侧管理面板含 Overview、Activity、Routines、Settings；Teams 的 @Copilot 与 Autopilot 是两回事。

**保留理由**：这是 Frontier 云端版的官方总览，与 Scout 桌面应用文档相比，入口改为 Copilot 网页/桌面与 Teams，并出现自有邮箱日历、Microsoft IQ/Work IQ 等新要素。

---

Autopilot（Frontier）概述

[本文档为预发布文档，可能变更。]

重要

- 访问 Autopilot（Frontier）需要完成相应的 **[Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)** 登记、预览分配并接受参与条款。仅登记 Frontier 并不会启用每一项预览功能。Frontier 预览受客户协议中适用的预览条款约束，其可用性和能力可能发生变化。
- 此功能处于预览阶段。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布之前提供，以便客户提前访问并提供反馈。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

Autopilot 是 Microsoft Copilot 中一个常驻的云端智能体。描述你想要的结果、它应使用的来源，以及它行动的边界。它可以准备文档、审阅可访问的对话、跟进工作，并通过自动化运行重复性任务。

Autopilot 有自己的工作场所身份、记忆、计算机和工作区。每个人可以拥有一个 Autopilot。已保存的上下文帮助它把工作延续到单次对话之外。它可以在你的设备关机时运行计划中的工作，前提是具备访问权限、审批和服务可用。

你在网页或桌面版的 Microsoft Copilot 中与 Autopilot 协作，它会按名字出现在左侧导航的 **Home** 标签上。它还会在 Microsoft Teams 中使用与你的一对一私密聊天来发送更新、提出问题和请求审批。Autopilot 不会扩大你可以访问的数据范围。

## Autopilot 能做什么？

Autopilot 把对话、重复性的后台工作和连接的工具集中在一处：

- **准备可供审阅的工作成果。** 使用你的 Autopilot 可用的工具，请求草稿、文档、演示文稿或分析。
- **跟进承诺。** 请求列出尚未解决的决策、即将到来的交付物、会议准备，或起草跟进事项。
- **重复一项任务。** 用时间表、完整的指令和预期的投递目的地设置一个例程。
- **跨 Microsoft 365 工作。** 在该任务的权限范围内使用已获授权的 Teams、Outlook、OneDrive 和 SharePoint 内容。Autopilot 在你的邮箱和日历之外拥有自己的邮箱和日历，并且可以把草稿共享到你现有的 OneDrive 文件夹。它还可以使用 Microsoft To Do 和 Planner 中的共享任务来追踪进度和跟进情况。
- **继续一个项目。** 使用已保存的偏好和工作上下文，同时检查来源和需求的变化。
- **审阅进度。** 打开 **活动** 以找到正在运行的工作、需要你输入的请求以及例程结果。

**例程** 可以按时间表运行，也可以在某个事件发生时运行。

## 从一个结果开始

描述你需要的结果、涉及的人员和来源，以及任何限制。例如，要求每天汇总尚未解决的发布决策并起草跟进事项，但不发送消息。

Autopilot 使用其可用的能力规划并执行工作，不会在每一步都询问你。在它发送、共享、删除或更改某物之前，一项自动审阅会把该操作与你的请求进行比较。相符的操作会运行；其他操作等待你的批准。请在结果的目的地审阅实际结果，而不要把审批或进度消息当作完成的证据。

## 找到你的工作

在 Microsoft Copilot 中，选择 **Home**。你的 Autopilot 会按名字出现在左侧导航中，与其他 Copilot 区域（如 **插件**）并列。
你可以使用左侧导航中的这些区域与 Autopilot 协作：

| 区域 | 你用它做什么 |
| --- | --- |
| 你的 Autopilot 的名称 | 打开你的主对话来发出指令、提问和审阅回复。在那里你还可以展开右上角的图标，打开 Autopilot 的管理面板。 |
| **插件** | 选择你的 Autopilot 的名称，发现能力并管理在你的体验中呈现的技能。 |

点击你的 Autopilot 后，使用右上角的展开面板按钮，展开与 Autopilot 协作的其他区域。

| 区域 | 你用它做什么 |
| --- | --- |
| 区域 | 你用它做什么。 |
| 概述 | 查看并打开你的 Autopilot 一直在处理的文件，以及你的 Autopilot 聊天历史。 |
| 活动 | 监控你的 Autopilot 采取的操作，包括活动中的任务、它需要你输入的地方，以及历史活动。 |
| 例程 | 在左侧导航中选择你的 Autopilot 的名称，展开右侧面板，然后选择「例程」标签页，在那里你可以暂停、编辑、运行或删除重复性工作。 |
| 设置 | 编辑你的 Autopilot 的名称和外观，并审阅它的记忆和权限。 |

## 理解身份、上下文与访问

Autopilot 的名称、外观、电子邮件地址和 Microsoft Entra 身份，把它的贡献与你的区分开。有些操作使用该身份；另一些使用代表你的授权访问。执行操作的账户、所请求的资源和操作本身都会影响访问。

Microsoft IQ 为互联的 Copilot 体验提供组织层面的依据，Work IQ 则提供工作上下文，例如人员、项目以及相关的 Microsoft 365 信息。依据和记忆不会授予权限，也不保证准确。

Autopilot 的云端工作区可以在会话之间保留工作上下文。它与你的本地设备分开；Autopilot 无法访问你的本地文件夹或应用。在已启用的地方，当你要求时，它可以在你设备上的 Microsoft Edge 中工作。对于你想保留的交付物，请指定一个可访问的保存位置，并核实生成的文件及其共享设置。

## 扩展 Autopilot 能做的工作

技能提供任务指令；插件连接能力和服务，并可以包含技能。两者本身都不会授予对数据的访问权限。可用的能力取决于你的组织设置。

| 能力 | 示例 |
| --- | --- |
| 文档和演示文稿技能 | 准备可供审阅的可编辑成果。 |
| Microsoft 365 工具 | 处理已获授权的邮件、日历、对话和文件。 |
| 插件 | 把 Autopilot 连接到其他服务并添加其技能。 |
| 你自己的技能 | 在对话中创建技能或上传一个技能，用 `/` 使用它，并与同事共享。 |

有关细节和技能控制项，请参阅[自定义 Autopilot 能做什么](https://learn.microsoft.com/en-us/copilot/autopilot/plugins)。

## 保持对后台工作的监督

审阅已授权操作的范围、自动化指令、收件人和结果。审批卡会解释某个操作为什么需要你审阅，而只有你自己的请求才授权操作；电子邮件、文件或网页中的指令不能。有关细节，请参阅[设置权限](https://learn.microsoft.com/en-us/copilot/autopilot/approval#set-permissions)。活动并不保证构成完整的管理审计记录。敏感度标签识别并不证明所有生成的文件都继承标签，也不证明每项操作都被数据丢失防护覆盖。

## Autopilot 与其他 Copilot 体验如何配合

Home 把 Copilot 中的对话式工作和被委托的工作汇集在一起。Cowork 处理被委托的任务，Code 专注于构建解决方案。Autopilot 提供持久的跟进。Teams 的 **@Copilot** 能力与你的 Autopilot 是不同的东西。这些体验的可用性和控制项各不相同。

## 相关内容

- [开始使用 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)
- [使用 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/using)
- [Autopilot 场景](https://learn.microsoft.com/en-us/copilot/autopilot/scenarios)
- [Autopilot 常见问题](https://learn.microsoft.com/en-us/copilot/autopilot/faq)
- [Autopilot 要求](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)
- [Autopilot 应用卡](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)
