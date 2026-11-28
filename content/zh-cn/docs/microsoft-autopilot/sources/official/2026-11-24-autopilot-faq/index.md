---
title: "Autopilot（Frontier）常见问题"
linkTitle: "文档：常见问题"
date: 2026-11-24
originalTitle: "Autopilot (Frontier) FAQ"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/faq"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [开放与价格, 记忆与上下文, 运行环境, 隐私]
products: [microsoft-autopilot]
updatedAt: "2026-11-24"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-17。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：FAQ 称 Autopilot 是 Microsoft Copilot 中常驻的云端智能体，拥有专属身份、记忆、计算机和工作区，笔记本关闭或关机时也能继续运行，每位启用用户只能有一个。它保留会话记忆、个人记忆和工作区记忆，本版本记忆不能关闭，删除会话不会删除已保存的记忆；云端计算机与用户设备分离，不能访问本地文件夹和应用，启用时可在用户设备的 Microsoft Edge 中工作。计费按 Copilot Credits 通过管理员设置的支出策略，未被覆盖或达到上限时，Autopilot 停止运行自动化并停止响应，且不给出解释。Autopilot 默认关闭，需组织加入 Frontier、管理员授权许可证、支出策略并激活；开通需 10 到 30 分钟，初期仅限美国的合格客户，优化英语，可经 iOS 和 Android 的 Microsoft 365 Copilot、Teams、Outlook 使用。DLP 在预览期受限，带标签内容不会被排除在可读范围之外。

**保留理由**：这篇一处汇集了云端形态下的访问条件、支出策略断供行为、记忆不可关闭、数据导出与删除、移动端和地区限制，补足了 Scout 桌面文档与 MC1479277 之外的细节。

---

Autopilot（Frontier）常见问题

[本文档为预发布文档，可能变更。]

重要

- 访问 Autopilot（Frontier）需要完成相应的 **[Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)** 登记、预览分配并接受参与条款。仅登记 Frontier 并不会启用每一项预览功能。Frontier 预览受客户协议中适用的预览条款约束，其可用性和能力可能发生变化。
- 此功能处于预览阶段。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布之前提供，以便客户提前访问并提供反馈。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

本文回答关于 Autopilot 的常见问题。有关 Autopilot 的更多信息，请参阅 [Autopilot 概述](https://learn.microsoft.com/en-us/copilot/autopilot/overview)。

## 了解 Autopilot

这些问题说明你可以把哪些工作委托给 Autopilot，以及它与其他 Copilot 体验的关系。

### 什么是 Autopilot？

Autopilot 是 Microsoft Copilot 中一个常驻的云端智能体。你描述想要的结果并设定边界，它帮助在 Microsoft 365 中推进工作。它可以准备文档、跟进工作，并通过例程运行重复性任务。它拥有专属的身份、记忆、计算机和工作区，因此工作可以延续到单次对话之外。它的操作仍受适用于该任务的权限和策略约束。更多信息请参阅 <overview>。

### Autopilot 与 Copilot Chat 有何不同？

用 Copilot Chat 提问和处理对话式工作。当你需要持续的跟进、重复性工作以及跨对话的连续性时，使用 Autopilot。Autopilot 可以在后台持续工作，不需要你逐步提示。

### Autopilot 与 Home、Today、Cowork 和 Code 是什么关系？

Home 是 Copilot 应用中工作的起点。Today 是一个独立的个性化体验，用于需要你关注的工作。Cowork 处理被委托的多步骤任务，Code 专注于构建软件和解决方案。Autopilot 专注于持久的工作和跟进。在预览期间，这些体验的可用性各不相同。

Copilot 中的 Office 集成并不意味着每项 Office 能力都能在 Autopilot 中使用。同样，为 Code 或 GitHub Copilot 描述的软件任务和并行智能体并不自动成为 Autopilot 的功能。请使用你所处体验中提供的控制项，而不要假设任务可以在它们之间转交。

### 我关闭应用后，Autopilot 还会继续工作吗？

会。Autopilot 在云端运行，因此即使你关闭 Copilot 应用，或者笔记本电脑合上或关机，它也能继续工作并完成任务。例程可以在你不在场时，使用其配置的指令和权限运行。你也可以从手机上查看进度、添加指令或改变方向。

后台运行并不保证执行不中断，也不保证在特定时间完成。缺少访问权限、需要审批或服务不可用，都可能导致工作无法完成。

## 委托工作并跟进到底

给 Autopilot 一个结果、它应使用的信息，以及它可以做什么的限定。对需要重复的工作使用例程。

### 什么是例程？

例程是 Autopilot 按计划运行的工作，例如晨间简报或每周状态汇总。说明它应该做什么、何时运行，以及你希望结果投递到哪里。包含它需要的来源、收件人和约束；不要假设一次计划运行会继承你创建它时那段对话中讨论过的一切。

在启用重复性工作之前，请检查计划、指令和所请求的权限。

### Autopilot 能监控频道、跟进讨论串并标记风险吗？

你可以让 Autopilot 检查它有权限访问的对话，找出未解决的问题、承诺和变更。对固定时间表的检查使用例程。例如，让它每天早上总结尚未解决的发布决策，并起草需要你审阅的跟进事项。告诉它使用哪些对话、什么算作风险或机会，以及通知谁。

### Autopilot 能在之后的对话中接着做一个项目吗？

已保存的偏好、决策和工作上下文帮助 Autopilot 随时间延续工作。告诉它你指的是哪个项目或哪项先前的工作，并提供任何已变更的需求。记忆并不是每段对话的完整记录，也不会授予对来源的访问权限或授权新的操作。

### Autopilot 能帮助处理会议、截止日期和时间块吗？

你可以让 Autopilot 准备会议简报、查找会议时间、起草邀请，或审阅即将到来的交付物，或为某项任务在日历上留出时间。说明你希望它使用的人员、日期范围、时区和日历。可用的操作取决于它的访问权限和你的组织设置。

查找时间、起草邀请和发送邀请是不同的操作。在批准更改之前，请核对组织者、参与者和日历。要求一份截止日期摘要，并不会自动授权发送邀请或更改日历。

## 身份、记忆与工作数据

Autopilot 在每项任务和每段对话所允许的访问范围内，使用组织上下文和已保存的工作信息。

### 为什么 Autopilot 有自己的名称和电子邮件地址？

它的工作场所身份让同事能在 Teams 和 Outlook 中认出它的贡献，并将其与你的贡献区分开。请核对设置期间呈现的身份。它的 Microsoft Entra 身份也让你的组织能够管理该智能体的访问权限。

### 如何将我的 Autopilot 添加为 Microsoft 365 个人资料中的助手？

1. 打开你的 Microsoft 365 个人资料。或者打开 Microsoft 365 Copilot，选择左下角的账户，然后选择「我的 Microsoft 365 个人资料」。
2. 在个人资料页头选择 **更新你的个人资料**。
3. 打开 **联系人**，在 **助手** 字段中选择你的 Autopilot。
4. 选择 **保存更改**。

你的管理员控制此个人资料字段是否可用以及是否可编辑。如果该字段缺失或为只读，请向管理员求助。设置个人资料中的助手本身并不会授予 Autopilot 权限或启用协作。

### Autopilot 总是以自己的身份操作吗？

不是。它的身份与某项操作所使用的账户相关但不同。有些操作使用 Autopilot 自己的身份；另一些则使用代表你的授权访问来读取或处理你的 Microsoft 365 资源。例如，它可能使用你的权限读取你的日历，同时以自己的身份与同事沟通。

拥有独立身份并不会让 Autopilot 不受限制地访问你的数据。权限适用于执行操作的账户、资源以及所请求的操作。

### Autopilot 能访问什么？

Autopilot 可以通过它所具备的能力，处理已获授权的 Microsoft 365 内容，包括 Teams 对话、电子邮件、日历以及 OneDrive 和 SharePoint 中的文件。访问取决于所使用的账户、资源权限和组织策略。添加技能并不会授予额外的访问权限。

### Autopilot 如何使用 Microsoft IQ 和 Work IQ？

Microsoft IQ 是为互联的 Copilot 体验所描述的更广泛的组织智能。Work IQ 提供工作上下文，例如人员、项目以及相关的 Microsoft 365 信息。这些上下文帮助 Autopilot 把工作建立在你的组织之上，而不是只依赖当前的提示词。

建立依据并不会授予对信息的访问权限，也不保证答案正确。请审阅对你的任务重要的来源、日期和结论。

### Autopilot 会在对话之间记住内容吗？

会。Autopilot 保留对话记忆、关于你的个人记忆，以及它所做工作的工作区记忆。要查看它记住了什么，请在 Autopilot 面板中打开 **查看 [name] 知道什么**，其中 *[name]* 是你的 Autopilot 的名称。你也可以在私密对话中问「你记得关于我的什么？」，或要求它更正、忘记或导出某条特定记忆。请确认结果，而不要假设更改已经成功。

在此版本中记忆无法关闭，并且你的 Microsoft 365 Copilot 个性化设置不适用于 Autopilot。记忆与对话历史是分开的：删除一段对话并不会删除已从该对话保存的记忆。更多信息请参阅[查看 Autopilot 记住了什么](https://learn.microsoft.com/en-us/copilot/autopilot/memory#)。

### Autopilot 的计算机和工作区是什么？

Autopilot 有一个由 Microsoft 管理的云环境，可以在其中处理文件并执行任务。它的工作区可以在会话之间保留工作上下文。它仅为完成某项任务而使用的临时文件，在任务完成后不会保留。

这台云端计算机与你的设备是分开的。Autopilot 无法访问你的本地文件夹或已安装的应用。在已启用的地方，当你要求时，它可以在你设备上的 Microsoft Edge 中工作。

### Autopilot 能使用我的网络浏览器吗？

在你的组织启用的情况下，Autopilot 可以在你设备上的 Microsoft Edge 中工作，使用你已登录的网站。你首次使用时开启浏览器使用，并且只有你在私密对话中发出的请求才能使用它。自动化和共享对话不会使用你的浏览器。
Autopilot 只在该对话所使用的标签页中工作，并且在付款、账户变更或永久删除等敏感操作之前会请求你批准。浏览器使用功能正在预览期间逐步推出。更多信息请参阅[在你的 Microsoft Edge 浏览器中工作](https://learn.microsoft.com/en-us/copilot/autopilot/edge)。

### 我的文件和 Autopilot 的工作保存在哪里？

你的对话和个人工作保存在你的 OneDrive 中。

要区分在 Autopilot 工作区中创建的文件与保存在你和同事都能打开的位置的文件。对于你想保留的交付物，指定一个执行操作的账户可以访问的 OneDrive 文件夹或 SharePoint 位置，并向 Autopilot 询问保存位置或链接。

不要假设文件创建步骤成功就意味着文件已上传、共享或添加标签。请核实你能打开最终文件，并且其访问权限和敏感度标签合适。

### 如何导出或删除我的 Autopilot 数据？

在你的私密对话中向 Autopilot 提出请求。例如，「把你记得的关于我的一切导出为 JSON 文件放到我的 OneDrive 里，并告诉我你保存在哪里。」要移除一段对话，请它按名称删除该会话，然后问：「你现在能永久删除它吗？」从列表中移除对话不一定删除其存储记录。

如果 Autopilot 保存导出内容时出现审批卡，请在允许之前审阅它。导出是一份快照，可能不携带原始的敏感度标签。更多提示和细节请参阅[查看 Autopilot 记住了什么](https://learn.microsoft.com/en-us/copilot/autopilot/memory)。

要将你的记忆和会话的完整副本下载到 Windows PC，请使用 Autopilot 导出脚本。更多信息请参阅[下载你的记忆和会话的完整副本](https://learn.microsoft.com/en-us/copilot/autopilot/memory#download-a-full-copy-of-your-memories-and-sessions)。对于已获批准的合规或隐私请求，你的管理员可以导出你的 Autopilot 数据副本。更多信息请参阅[导出用户的 Autopilot 数据](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure#export-a-users-autopilot-data)。

### 我可以用新的 Autopilot 重新开始吗？

先导出你想保留的所有内容，然后联系你的管理员。不要自行重命名、移动或删除 Autopilot 的文件。

### 技能和插件如何扩展 Autopilot？

技能为某一类任务提供指令。插件把 Autopilot 连接到工具和服务，并可以提供额外的技能。技能和插件本身都不会授予使用数据或执行操作的权限。

| 能力 | 它能帮你做什么 |
| --- | --- |
| 文档和演示文稿技能 | 准备可供审阅的可编辑成果。 |
| Microsoft 365 工具 | 处理已获授权的邮件、日历、对话和文件。 |
| 插件 | 把 Autopilot 连接到其他服务并添加其技能。 |
| 你自己的技能 | 教 Autopilot 以可重复的方式完成某项任务。 |

在 **插件** 中，你可以从目录添加插件、创建或上传技能，并找到同事与你共享的技能。在编辑器中输入 `/` 即可使用技能，或让 Autopilot 自己选择一个相关的技能。标有 **被策略阻止** 的项目在你所在的组织中不可用。更多信息请参阅[自定义 Autopilot 能做什么](https://learn.microsoft.com/en-us/copilot/autopilot/plugins)和[插件文档](https://learn.microsoft.com/en-us/plugins)。

### 我可以与同事共享技能吗？

可以。你可以把已保存的技能共享给组织中的特定人员。他们打开链接、添加技能，并在自己的 Autopilot 中使用。共享不会共享你的登录信息、连接或权限。更多信息请参阅[共享技能](https://learn.microsoft.com/en-us/copilot/autopilot/plugins#share-a-skill)。

## 审阅操作并应用组织控制

后台工作仍然需要监督。检查 Autopilot 计划做什么、使用什么权限，以及实际结果。

### Autopilot 会在不逐次询问的情况下发送消息或更改内容吗？

可以。Autopilot 可以在不逐步询问你的情况下完成任务。在它发送、共享、删除或更改某物，或者创建或更改例程之前，一项自动检查会把该操作与你要求的内容进行比较。如果操作与你的请求相符，它就会运行。如果不符，或者检查无法完成，你会在 Teams 中收到审批卡；如果你是在 Microsoft Copilot 中提出的请求，也会在那里收到。付款和其他敏感浏览器步骤始终需要你批准。

只有你自己的消息才算作请求。电子邮件、文档或网页中的指令不会授权任何操作。在审批卡上，**允许** 会执行所列操作一次，**拒绝** 会取消它们。在允许某项操作之前，请核对收件人、目的地和执行操作的账户。更多信息请参阅[设置权限](https://learn.microsoft.com/en-us/copilot/autopilot/approval#set-permissions)。

### 我如何跟踪工作并进行干预？

打开管理面板，选择 **活动** 标签页来审阅操作和更新。查看 **正在处理** 以审阅进行中的工作，或查看 **需要你的输入** 以找到需要你关注的请求。你可以在那之下查看 Today 及以后（译注：原文为 "Today and beyond"）的内容，看到已完成的活动和已运行的例程。
选择 **概述** 浏览对话，或选择 **例程** 审阅计划中的工作。打开一段对话以澄清或更改任务，或要求 Autopilot 停止它。当重复性工作不再符合你的意图时，请审阅或暂停它。

停止请求并不证明已经开始的操作已被取消或回退。在重试发送、邀请或文件更改之前，请检查完成了什么。

### 我应该如何验证结果？

在结果的目的地检查结果：打开已保存的文档、审阅日历事件，或确认已发送的消息及其收件人。审批授权了一项操作，但并不证明该操作已完成。在依赖 AI 生成的内容之前，请审阅其准确性和适宜性。

### 适用哪些治理和审计控制？

你的组织控制对预览版和 Microsoft 365 资源的访问。Autopilot 的身份、权限和自动审批检查约束了它能做的工作。

面向用户的活动有助于你跟踪任务，但并不保证构成完整的管理审计记录。请询问你的管理员，哪些审计、保留和合规控制覆盖你所启用的 Autopilot 体验。有关配置指导，请参阅[为你的组织配置 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure)。

### Autopilot 支持敏感度标签和数据丢失防护吗？

Autopilot 能识别受支持的 Microsoft 365 内容上的敏感度标签。但是，带标签的电子邮件和文件并未被排除在 Autopilot 可读取的范围之外，它生成的内容也可能不会继承该标签。针对提示词的数据丢失防护（DLP）在预览期间受到限制，因此不要假设 Microsoft Purview DLP 在所有工具和目的地都有一致的覆盖。如果提示词被阻止，你可能只会看到一个通用错误。

在将 Autopilot 用于敏感信息之前，请与管理员确认适用的保护措施。在共享目标文件之前，请检查其标签和访问权限。

### 我的数据会被用于训练 AI 模型吗？

有关 Autopilot 如何处理你的数据以及它所使用模型的信息，请参阅 [Autopilot 应用卡](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)。

## 访问与可用性

Autopilot 仍是预览版。访问权限和各项能力会因组织和推广进度而异。

### 我需要安装什么吗？

云端 Autopilot 体验在 Microsoft Copilot 中运行，不需要在你的设备上单独安装智能体。要让 Autopilot 在已启用的浏览器中工作，你需要让 Microsoft Edge 连接到 Autopilot。有关受支持的访问方式，请参阅 [Autopilot 要求](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)。

### Autopilot 的额度用完后会怎样？

Autopilot 通过管理员设置的支出策略，按 Copilot Credits 的用量计费。如果你不在支出策略的覆盖范围内，或者策略达到其上限，Autopilot 会停止运行自动化和监控工作，并停止响应新的请求。发生这种情况时，Autopilot 不会向你显示说明。如果 Autopilot 停止响应，请联系你的管理员。更多信息请参阅[查看用量和限制](https://learn.microsoft.com/en-us/copilot/autopilot/using#review-usage-and-limits)。

### 我如何获得访问权限？

Autopilot 默认关闭。你的组织必须让你加入 Frontier，你的管理员必须为 Autopilot 授予许可证、用支出策略覆盖基于用量的计费，并为你激活 Autopilot。加入 Frontier 并不意味着你的账户已启用所有已公布的能力。要了解如何加入 Frontier，请参阅 [Frontier 计划](https://adoption.microsoft.com/copilot/frontier-program/)。有关先决条件，请参阅[开始使用 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started#prerequisites)。

### 我可以在手机上使用 Autopilot 吗？

可以。Autopilot 可通过 Microsoft 365 Copilot、Microsoft Teams 和 Microsoft Outlook 应用在 iOS 和 Android 上使用。使用你的工作账户登录。你可以从手机上查看进度、添加指令，或改变现有任务的方向。

### 我可以拥有多少个 Autopilot？

一个。每位已启用的用户只能创建一个 Autopilot。

### 设置需要多长时间？

完成设置步骤后，预配可能需要 10 到 30 分钟。你可以离开该页面；当你的 Autopilot 就绪时，你会收到一封电子邮件和一条 Teams 通知。有关步骤，请参阅[创建你的 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started#create-your-autopilot)。

### 支持哪些语言和地区？

可用性最初仅限于美国的合格客户。Autopilot 针对英语进行了优化。有关当前可用性，请参阅 [Autopilot 要求](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)。

### 我如何提供反馈？

在一条回复下方选择 **我喜欢某些内容** 或 **我不喜欢某些内容**。你也可以要求 Autopilot 记录一个 bug。更多信息请参阅[提供反馈](https://learn.microsoft.com/en-us/copilot/autopilot/using#provide-feedback)。

## 相关内容

- [Autopilot 概述](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [使用 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/using)
- [Autopilot 要求](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)
- [为你的组织配置 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure)
- [Autopilot 应用卡](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)
