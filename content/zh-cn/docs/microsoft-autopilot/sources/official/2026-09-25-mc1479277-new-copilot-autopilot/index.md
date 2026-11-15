---
title: "MC1479277：Copilot 新 Home、Code 与 Autopilot（按用量计费）"
linkTitle: "消息中心 MC1479277"
date: 2026-09-25
originalTitle: "MC1479277 - Microsoft Copilot: New ways to work across Microsoft Copilot and Microsoft 365"
sourceUrl: "https://admin.microsoft.com/#/MessageCenter/:/messages/MC1479277"
altUrls: []
author: "未署名"
publisher: "Microsoft 365 消息中心"
language: en
fidelity: 转载全文
translation: 已翻译
collectedAt: 2026-11-14
tags: [开放与价格, 功能更新]
products: [microsoft-autopilot]
reprintUrl: "https://mc.merill.net/message/MC1479277"
updatedAt: "2026-11-09"
dateNote: "存档站显示 Published Sep 25, 2026、Last Updated Nov 9, 2026（第 4 版；此前版本为 10-05、10-12、11-04）"
---

{{< source-info >}}

**收录说明**：Microsoft 365 管理中心的消息中心公告，原文需管理员登录，依据第三方存档站 mc.merill.net 的完整转录存档，取的是 2026-11-09 的第 4 版。删去了存档站的导航、讨论区、相关帖与版本历史。公告涉及新 Copilot 的多项更新，按全文存档，摘要侧重 Autopilot。已翻译。

**内容摘要**：这条消息中心公告 2026-09-25 发布、2026-11-09 更新，称 Autopilot 此前叫 Scout，是 Copilot app 中具备持久上下文、身份和记忆的 always-on 个人 agent，入口是导航栏的 Autopilot 标签页。Autopilot 采用用量计费（UBB），可用用户须有 Microsoft 365 Copilot 许可证和支出策略；推出时间与管理控制细节「将在可用时更新」。公告的待办部分要求管理员在 Microsoft 365 管理中心 Copilot > Cost management 中配置支出策略。其余部分涉及新 Home（Chat 与 Cowork 合在一屏）、Code（同样 UBB）、Copilot Managed Runtime、SharePoint 与 OneDrive 中 Copilot 的正式发布等。

**保留理由**：这是更名后面向管理员的 Autopilot 公告，写明 UBB 前提（Microsoft 365 Copilot 许可证加支出策略，不再提 GitHub Copilot）与 Scout 的更名关系，并显示截至 11-09 仍未给出推出时间；MC1332811 是 Scout 桌面版的公告。

---

MC1479277 - Microsoft Copilot：在 Microsoft Copilot 和 Microsoft 365 中工作的新方式

消息中心（Message Center）

### 摘要

Microsoft Copilot 的更新包括新的 Home 体验、增强的 Office 集成、采用用量计费的 Code 和 Autopilot 功能、面向企业代码的 Copilot Managed Runtime，以及在 SharePoint 和 OneDrive 中正式发布。管理员必须配置支出策略，并通过 Microsoft 365 管理中心管理访问权限。

[讨论](#discussion)powered by zap.ms

[### 消息 ID

MC1479277

在消息中心查看](https://admin.microsoft.com/#/MessageCenter/:/messages/MC1479277)

### 最后更新

Nov 9, 2026

Published Sep 25, 2026

[查看版本历史](#version-history)

### 服务

Microsoft Copilot (Microsoft 365)

### 标签

Updated message

New feature

User impact

Admin impact

[### 路线图 ID

501451

查看路线图详情](https://mc.merill.net/message/RM501451)

### 平台

Web

### 更多信息

2026 年 11 月 9 日更新：我们更新了 Copilot 应用 UI 更新部分，加入了新的细节。感谢你的耐心等待。

**内容与原因：**

我们正在演进 Microsoft Copilot，以便更好地把人们依赖的工具与他们在工作中构建、定制和扩展 AI 所需的能力连接起来。更新包括 Copilot 应用中新的 Home 体验和增强的 Office 能力；用于构建解决方案和自动化工作的 Code 和 Autopilot；用于运行代码的企业级平台；以及对 Copilot Notebooks、SharePoint 和 OneDrive 中的 Copilot、Work IQ 的更新。

**对你的组织的影响：**

**Copilot 应用中的 Home：**

- 用户打开 Copilot 应用时，将进入 Home，它把 Chat 和 Cowork 合在一个屏幕上。用户可以在提示框中切换 Chat 和 Cowork。详见[博客](https://aka.ms/AA13g7uq)。这些更新将在 10 月向 Frontier 推出，面向所有可访问 Copilot 应用的 Microsoft 365 用户。
- 作为此次更新的一部分，我们对左侧导航窗格做了如下更新：1) Agents & Plugins 将取代 Chat 中独立的 Agents 入口（部分预览用户称为 Agents & Skills）以及 Cowork 中的 Customize 入口。2) 对有权使用 Cowork 的用户，Cowork 中的 Automations 将移到 Home 导航窗格。这些更新将在 10 月向 Frontier 推出，面向所有可访问 Copilot 应用的 Microsoft 365 用户。
- Researcher 和 Analyst 将不再默认固定在 Copilot 应用导航窗格中。用户仍可从 Plugins 访问这些 agent，并可按自己的偏好把它们固定到导航窗格。希望这些 agent 继续为其用户固定的组织，可以[通过 Microsoft 365 管理中心预先固定](https://learn.microsoft.com/microsoft-365/admin/manage/agent-registry?view=o365-worldwide#manage-pinned-agents)。
- Chat 可以完成长时间运行的多步骤知识工作，包括起草电子邮件、管理会议、在 Teams 中工作、管理 OneDrive 和 SharePoint 文件、查找人员，以及创建 Word、PowerPoint、Excel、PDF 和 HTML 文件。敏感操作需要用户批准。用户可以在 Chat 的 Tasks 视图中跟踪和管理自己长时间运行的活动，入口在 Copilot 应用导航窗格的右上方。这些能力将在本月晚些时候向 Frontier 推出，拥有 Microsoft 365 Copilot 许可证的用户可用。
- Chat 将开始展示生成回复时使用的 Skills，让用户更透明地了解 Copilot 如何作答。此更新将在 10 月开始在全球推出，拥有 Microsoft 365 Copilot 许可证的用户可用。

**Code：**

- 新的 Code 体验在 Copilot 应用中为用户提供了一个专门的位置，用自然语言创建跟踪器、仪表板和应用。用户可以前往 Copilot 应用导航窗格中的 Code 标签页访问 Code。详见[博客](https://aka.ms/AA13g7uq)。
- Code 采用用量计费。符合条件的用户需要有 Microsoft 365 Copilot 许可证和支出策略。
- Code 将在本月晚些时候向 Frontier 推出。
- 准备工作：要为你的租户启用 Copilot Code，管理员必须[部署统一应用](https://learn.microsoft.com/windows/client-management/deploy-unified-copilot-app)并[把目标通道设置为 beta](https://learn.microsoft.com/windows/client-management/copilot-update-policy-control#targetchannel-copilot)。

**Autopilot：**

- Autopilot 此前称为 Scout，是 Copilot 应用中常开（always-on）的个人 agent，具有持久的上下文、身份和记忆。用户可以前往 Copilot 应用导航窗格中的 Autopilot 标签页访问 Autopilot。详见[博客](https://aka.ms/AA13g7uq)。
- Autopilot 采用用量计费。符合条件的用户需要有 Microsoft 365 Copilot 许可证和支出策略。
- 有推出时间和管理员控制细节后，我们会更新此消息。

**Copilot 应用 UI 更新：** 更多细节请参阅 [MC1546354](https://admin.cloud.microsoft/?#/MessageCenter/:/messages/MC1546354)。

**Copilot 应用中的完整 Office 能力：**

- 用户可以在 Copilot 应用中使用完整的 Word、Excel 和 PowerPoint 创建、编辑和协作能力，与 Copilot 并排使用。用户还可以从 Copilot 应用导航窗格的 Library 访问最近的 Word、Excel 和 PowerPoint 文件。详见[博客](https://aka.ms/AA13g7uq)。
- 通过 Chat 访问的能力包含在 Microsoft 365 Copilot 用户订阅许可中。通过 Cowork 访问的能力采用用量计费。
- 这些能力将在本月晚些时候向 Frontier 推出。

**Copilot Managed Runtime：**

- Copilot Managed Runtime 是一个企业级平台，用于在 Microsoft 365 租户边界内、在 IT 治理下运行代码。它支持在 Code、Cowork、Copilot Studio 以及受支持的命令行和 SDK 体验中构建的应用。管理员可以在 Microsoft 365 管理中心管理这些应用。详见[博客](https://aka.ms/CopilotManagedRuntime-Blog)。
- Managed Runtime 现已开始以公开预览（public preview）形式推出。

**Copilot Notebooks 更新：**

- Copilot Notebooks 将新增任务委派、完整的 Office 编辑和协作、交互式报告创建、音频概览更新、模型选择，以及 Copilot 应用和 OneNote 中更新后的用户体验。
- 这些更新将在本月晚些时候向 Frontier 推出。

**SharePoint 和 OneDrive 更新：**

- 我们宣布 SharePoint 中的 Copilot 正式发布（general availability）。已处于公开预览中的日常 AI 能力继续包含在 Microsoft 365 Copilot 用户订阅许可（USL）中。新的 agent 能力，以及比预览期间能达到的更大规模的工作能力，将通过用量计费（UBB）提供，并消耗 Copilot Credits。我们同时宣布 OneDrive 中的 Copilot 正式发布，其许可结构与 SharePoint 相同。更多关于 SharePoint 和 OneDrive 中 Copilot 的内容，详见[博客](https://aka.ms/CopilotinSP/blog/GA)。
- 正式发布将在本月晚些时候开始推出。随着推出推进，租户可用性可能随后到来。
- 准备工作：继续使用包含在 Microsoft 365 Copilot 用户订阅许可（USL）中的能力无需任何操作。管理员可以前往 Microsoft 365 管理中心 > Copilot > Cost Management，控制谁可以通过 UBB 访问 SharePoint 的高级能力。现有的成本管理策略可能自动包含新推出的服务。针对 SharePoint 中 Copilot 公开预览的现有 PowerShell 退出设置，在 11 月 1 日之前继续有效；之后请通过 SharePoint 站点 AI 设置管理可用性。

**Work IQ 中的业务应用：**

- Work IQ 现在包含 Dynamics 365 Sales、Dynamics 365 Customer Service 和 Power Platform 的数据，使 Copilot 能够基于业务和生产力数据来支撑回复与任务。详见[博客](https://aka.ms/BizAppsInWorkIQ/Blog)。
- 这些更新将在本月晚些时候开始以公开预览形式推出。
- 准备工作：管理员可以在 Power Platform 管理中心为 Copilot 配置 Dynamics 365 和 Power Platform 数据源。管理员还可以在 Microsoft 365 管理中心的 Copilot > Settings 下管理业务应用在 Copilot 中的可用性，并通过 Agents > Tools 下的 Work IQ Model Context Protocol (MCP) 管理访问。

**需要采取的行动 / 建议：**

除上述各项更新中列出的指引之外：

- 用户要访问通过用量计费提供的能力，必须有支出策略。请在 Microsoft 365 管理中心的 Copilot > Cost management 下启用 Copilot Credit 消耗并配置支出策略。向用户说明用量计费的场景，以及如何通过 IT 申请访问权限。更多关于支出策略和用量计费的信息，详见[博客](https://aka.ms/Sept25/EvolvingModel)以及标题为 **Evolving Copilot pricing and new FinOps capabilities for AI** 的消息中心帖子。
- 请关注此帖，获取更新后的可用性和部署细节。
