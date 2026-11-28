---
title: "使用 Autopilot"
linkTitle: "文档：使用方法"
date: 2026-11-24
originalTitle: "Use Autopilot (Frontier)"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/using"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [功能更新, 持续执行, 开放与价格]
products: [microsoft-autopilot]
updatedAt: "2026-11-24"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-10。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：文档介绍如何在 Copilot 的 Home 中点击 Autopilot 名字，展开右上角管理面板，用加号新建对话，描述目标、来源和行动限制。Activity 视图可按 Type（Chats、Routines、Files、Approvals）、Source（Teams、Outlook）、Status（Needs you、In progress、Didn’t finish、Completed）筛选，但不是完整的管理审计日志。Autopilot 自行判断请求是当下任务还是 routine，已有 routine 完全满足时复用，否则新建；routine 私有，可 Run now、Edit、Delete 或开关。对话和个人工作保存在 OneDrive，临时文件任务后不保留；按 Copilot Credits 通过支出策略计费，页面顶部有 Credits in use 标识，但不显示已用或剩余数量，超限时无法运行自动化、监控或响应新请求，也无解释。

**保留理由**：补充了云端版的实际操作入口、Activity 筛选维度、routine 管理与复用规则，以及 Credits in use 标识这一计费可见性细节，是已收资料里没有的操作层说明。

---

使用 Autopilot（Frontier）

［本文为预发布文档，可能变更。］

重要

- 访问 Autopilot（Frontier）需要完成相应的 **[Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)** 注册、预览分配，并遵守参与条款。仅注册 Frontier 并不会启用每一项预览功能。Frontier 预览受你的客户协议中适用的预览条款约束，其可用性与能力可能变化。
- 此功能处于预览阶段。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布之前提供，以便客户提前访问并提供反馈。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

使用 Autopilot 委托任务、按计划重复工作，并查看结果。要首先创建你的 Autopilot，参见 [Autopilot 入门](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)。

在 Microsoft Copilot 中，选择 **Home**（主页），然后在左侧导航中选择你的 Autopilot 名称，打开它的概览。使用 **Plugins**（插件）启用额外能力；或者选中左侧导航中的 Autopilot 名称，展开右侧窗格，选择 **Routines** 标签页，在那里你可以暂停、编辑、运行或删除重复性工作。预览期间，这些控件可能有所变化。

## 在 Autopilot 视图中工作

点击左侧导航中的 Autopilot 后，使用右上角的展开面板图标打开 Autopilot 的管理面板。
**Overview**（概览）标签页显示文件、最近的聊天，以及与你的 Autopilot 的 Teams 和 Outlook 对话。加号可让你开始新聊天。

1. 在 **Home** 标签页中，于左侧导航中选择你的 Autopilot 名称。
2. 打开管理面板，使用加号开始新聊天。
3. 描述你想要的结果、要使用的来源，以及对操作的限定。
4. 使用发送控件提交消息。
5. 回答澄清性问题。
6. 检查完成的结果，必要时要求修改。

例如："Review this week's launch discussion and draft a status update. List unresolved decisions and their owners. Don't send the update."（译注：意为「回顾本周的发布讨论并起草一份状态更新。列出未决事项及其负责人。不要发送这份更新。」）

当这有助于确定正确的文件或对话时，提供来源链接或附上受支持的上下文。Autopilot 只能使用行为账户、可用工具和组织策略所允许的来源。

### 检查敏感度标签

Autopilot 能识别受支持的 Microsoft 365 内容上的标签，并显示对话标签。带标签的内容不会被排除在 Autopilot 可读取的范围之外，而新文件可能不会继承该标签。预览期间，数据丢失防护的覆盖范围有限。在共享最终文件之前，检查它的分类、访问权限和目的地。

### 在时间线上跟踪工作

使用 **Activity**（活动）视图跟进工作；不要把它当作完整的管理审计日志。

1. 使用筛选器选择你想查看的活动类型。
2. 选择 **Type**（类型，Chats、Routines、Files、Approvals）、**Source**（来源，Teams、Outlook）或 **Status**（状态，Needs you、In progress、Didn't finish、Completed）。
3. 打开相关条目，查看其对话、决策和活动。
4. 在其目的地确认任何外部影响，例如已保存的文件、已发送的消息或日历事件。

你也可以在其对话中回复，来重定向或停止进行中的工作。

## 设置例行任务

用自然语言告诉 Autopilot 你想达成什么，Autopilot 会建议相关的例行任务。
你的例行任务只有你能看到。

Autopilot 决定如何处理一个请求：

| 请求 | Autopilot 的处理方式 |
| --- | --- |
| 它能现在完成的工作，例如起草一封回复 | 当前对话中的一个任务 |
| 带结果，或带时间/事件触发条件的定时工作。 | 一个例行任务（routine） |

如果已有例行任务恰好就是你所要求的，Autopilot 会复用它。否则，它会新建一个，而不是修改已有的。

### 管理例行任务

在右侧面板中使用 **Routines** 找到你正在运行和已暂停的例行任务。每个 **Routine** 显示其时间安排，以及一个开启或关闭定时运行的开关。选择三个点可看到这些选项：

| 选项 | 作用 |
| --- | --- |
| **Run now**（立即运行） | 立即启动该例行任务，包括其指令中的任何操作。 |
| **Edit**（编辑） | 让你编辑该例行任务。 |
| **Delete**（删除） | 移除该例行任务。 |

暂停未来的运行不会撤销已经完成的工作。当指令变化时，检查已保存的指令和权限，而不要假定先前的某段对话已经更新了它们。

## 保存并核实交付物

指定你希望 Autopilot 使用的 OneDrive 或 SharePoint 目的地。行为账户需要拥有对该位置的访问权限。

| 工作 | 保存位置 |
| --- | --- |
| 你的对话和个人工作 | 你的 OneDrive |
| 任务期间使用的临时文件 | 任务结束后不保留 |

检查最终文件确实存在于所要求的位置、能以预期的账户打开，并具有适当的访问权限和标签。位于 Autopilot 工作环境中的文件未必已上传或共享。报告为部分完成的情况——例如创建了文件但无法核实其访问权限——在重试前需要复核。

## 查看用量与限制

Autopilot 按用量通过 Copilot Credits 计费，经由管理员管理的支出策略。Autopilot 页面顶部的 **Credits in use**（使用中的额度）指示器表示额度适用。选择它查看详情。Autopilot 不显示已用或剩余额度的数量；向管理员询问用量信息。

如果你不在某项支出策略的覆盖范围内，或该策略达到上限：

- Autopilot 无法运行自动化、监控工作，或响应新的请求。
- Autopilot 不会向你显示解释。如果它停止响应，请联系管理员。
- 自动化可能显示为已暂停，直到额度可用。

关于许可与访问，参见 [Autopilot 要求](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)。

## 提供反馈

你的反馈帮助 Microsoft 改进 Autopilot。

1. 在一条回复下，选择 **I like something**（我喜欢某处）或 **I don't like something**（我不喜欢某处）。
2. 如果你选择 **I don't like something**，描述发生了什么以及你期望什么。如果有帮助，附上截图。
3. 在提交前，查看其中包含的提示、回复和诊断数据。不要包含敏感信息。

你也可以让 Autopilot 记录一个 bug 并描述问题。更多信息，参见[通过 Microsoft 365 应用提供关于 Microsoft Copilot 的反馈](https://support.microsoft.com/topic/c481c26a-e01a-4be3-bdd0-aee0b0b2a423)。

## 相关内容

- [Autopilot 概览](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [Autopilot 入门](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)
- [Autopilot 场景](https://learn.microsoft.com/en-us/copilot/autopilot/scenarios)
- [Autopilot 常见问题](https://learn.microsoft.com/en-us/copilot/autopilot/faq)
- [Autopilot 应用卡片](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)
