---
title: "查看 Autopilot 记住了什么"
linkTitle: "文档：记忆管理"
date: 2026-11-17
originalTitle: "Check what Autopilot remembers"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/memory"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [记忆与上下文, 隐私, 功能更新]
products: [microsoft-autopilot]
updatedAt: "2026-11-17"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-17。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：说明 Autopilot 保留对话记忆、关于用户的个人记忆和工作区记忆，用户可在管理面板 Settings 的 Memory 下通过 Review what [name] knows 查看、修正或删除，也可在私人对话中询问。本版本记忆无法关闭，M365 Copilot 个性化设置不适用；记忆、对话历史和导出文件相互独立，删除对话不会删除已保存记忆。文档给出用提示词检查记忆来源、导出为 JSON 或 ZIP 到 OneDrive（需批准写入）、删除偏好和永久删除会话的做法，并介绍用导出脚本把 OneDrive 中的 lobster.repo 下载到 Windows PC，内含 Latest files、repository.git 和 README.txt。

**保留理由**：记忆机制的用户侧说明：三类记忆、记忆文件名（MEMORY.md、USER.md、每日笔记）、lobster.repo 存储与导出方式，已收资料对 Autopilot 的记忆只有概述，没有这些操作细节。

---

查看 Autopilot 记住了什么

[本文为预发布文档，内容可能变更。]

重要

- 访问 Autopilot（Frontier）需要完成相应的 **[Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)** 注册、预览分配并接受参与条款。仅完成 Frontier 注册并不会启用每一项预览功能。Frontier 预览受你的客户协议中适用的预览条款约束，其可用性与功能可能变化。
- 此功能处于预览阶段。
- 预览功能可能功能受限，并且可能不会正式发布。这些功能在正式发布之前提供，以便客户提前使用并提供反馈。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

Autopilot 会保留对话记忆、关于你的个人记忆，以及针对其所做工作的工作区记忆。要查看它记住了什么，请打开管理面板并选择**设置（Settings）**。在**记忆（Memory）**下，选择**查看 [name] 了解什么（Review what [name] knows）**，其中 [name] 是你的 Autopilot 的名称。你可以在那里修正或删除记忆。

你也可以在私人对话中询问。例如「你记得关于我的什么？」或「你记得我喜欢怎样写状态更新吗？」让它修正或忘记某个具体偏好，例如「忘掉你了解的有关 [主题] 的内容」，然后让它再检查一下受影响的记忆。确认结果；不要把一句自然语言请求当作变更成功的证明。

此版本中记忆无法关闭，你的 Microsoft 365 Copilot 个性化设置也不适用于 Autopilot。记忆、对话历史和导出的文件是彼此独立的。删除一段对话不会移除已保存的记忆或另存的导出文件，忘记一条记忆也不会抹掉更早的聊天消息或导出文件。

### 检查已保存的细节及其来源

从你的私人对话开始。要求它给出保存的信息及其来源，而不是只依赖一份摘要。

- 「你记得我的状态更新偏好是什么吗？展示保存的笔记，以及每条事实来自哪里。」
- 「列出你可以访问的记忆文件。展示相关文件的完整内容，不要做摘要。」

如果 Autopilot 提到某个文件，例如 `MEMORY.md`、`USER.md` 或某份每日笔记，你可以在后续提问中点名该文件。文件名和可用记录在预览期间可能变化。某份笔记无法访问或不存在，并不能证明别处没有副本。

### 导出记忆或对话记录

要求一个明确的范围、格式和可访问的保存位置。导出文件可能包含敏感的个人与组织信息。

1. 说明你要哪些记录。例如「把你记得的关于我的一切导出到我的 OneDrive 中的一个 JSON 文件，并告诉我你保存在哪里。」想要更多控制，可以指定文件夹，让它标明包含的记录和日期，并让它列出无法访问的内容。
2. 留意用于保存文件的批准卡片。它很容易被忽略，而在你允许之前，Autopilot 不会写入导出文件。
3. 询问最终的文件名、位置，以及包含与排除记录的摘要。
4. 打开保存的文件，检查其中是否包含所要的材料。在保留或分享之前，检查它的访问权限与分类。

对于一段对话，可以试：「把这段对话以 JSON 导出到这个 OneDrive 文件夹。说明包含或排除了哪些消息和附件。」

对于可访问的会话文件，你可以请求打包：「把我所有的会话文件收集起来，打包成一个 ZIP 文件。放到我的 OneDrive 里，并告诉我确切位置。」让它列出覆盖的对话和日期，以及任何遗漏。

导出文件是 Autopilot 创建该文件时所能访问内容的快照。它之后不会更新，也可能不带有原始内容的敏感度标签。

可访问会话文件的 ZIP 并不能证明存在完整的跨对话或 Teams 历史导出。清单里可能既有对话，也有后台会话或自动化会话。如果 Autopilot 无法访问另一段对话的记录，请在导出说明中保留这一限制。

在工作环境中创建的文件仍需送达预期的保存位置。不要因为回复里提到了下载链接，就以为存在直接的下载链接。如果 ZIP 无法获得预期的敏感度标签，不要把上传成功当作标签成功；请咨询管理员，并按其中所含最敏感的材料加以保护。

### 下载你的记忆与会话的完整副本

Autopilot 把你的记忆和会话保存在 OneDrive 中一个名为 `lobster.repo` 的文件里。你可以用 Autopilot 导出脚本，把它的一份私人副本下载到 Windows PC 上。你的 OneDrive 中的任何内容都不会被更改、共享或删除。

你需要一台 Windows PC。脚本使用 Windows 自带的 Windows PowerShell，以及 Git（脚本会提示安装）。

1. 从你组织批准的位置下载 `Lobster-Export.zip`。右键单击它，选择**全部解压缩**，然后打开解压出来的 `Lobster export` 文件夹。不要在 zip 文件内部运行脚本。
2. 双击 `Get-LobsterRepo.cmd`。
3. 如果缺少 Git，输入 `Y` 以通过 Windows 包管理器安装 Git for Windows，然后按其提示操作。
4. 按 Enter 继续，当 Windows 请求管理员批准时选择**是**。
5. Microsoft Edge 会打开 Microsoft 登录页面。选择你自己的工作账户。不要使用他人的账户。
6. 当浏览器显示你已登录时，回到 PowerShell 窗口。在第二次管理员提示处选择**是**。
7. 如果脚本找到多个 `lobster.repo`，输入要下载的那一个的编号。
8. 下载完成后，文件资源管理器会打开新的文件夹。

该文件夹名为 `Lobster export <date time>`，位于你的用户配置文件中。它包含：

| 项目 | 内容 |
| --- | --- |
| `Latest files` | 最新版本中各文件的可读副本，例如记忆和会话记录。 |
| `repository.git` | 完整的 Git 仓库，包括更早的版本和历史。 |
| `README.txt` | 关于该副本的简短说明。 |

该副本可能包含敏感的个人与组织信息。请把它放在受保护的位置。

如果出了问题，请使用下表。

| 消息 | 该怎么办 |
| --- | --- |
| 管理员批准被拒绝 | 再次运行脚本并选择**是**，或请 IT 支持与你一起运行。 |
| hosts 文件已有其他条目 | 请 IT 支持检查现有的 `cowork.local.microsoft.com` 条目。 |
| 浏览器显示证书警告 | 不要绕过它。关闭该标签页并向 IT 支持报告。 |
| 你的组织尚未批准此次登录 | 请咨询 IT 支持。Cowork 应用可能需要在你的组织中获得同意。 |
| 尝试 3 次后仍无法连接 | 检查你的网络、VPN 或代理连接，然后再次运行脚本。 |
| 未找到 `lobster.repo` | 你的 Autopilot 工作区可能存放在别处。请咨询你的支持团队。 |
| 部分分支或标签引用无法下载 | 副本不完整。请在新的文件夹中再次运行脚本。 |
| 临时设置无法自动移除 | 把警告文本发给 IT 支持。其中写明了要移除的 hosts 文件行和证书。 |

要查看更详细的信息，请在脚本文件夹中打开 PowerShell 并运行 `.\Get-LobsterRepo.ps1 -Verbose`。要选择另一个新文件夹，请加上 `-OutputFolder`。该文件夹不得由 OneDrive 同步。

对于已获批准的合规或隐私请求，你的管理员也可以导出你的 Autopilot 数据的一份副本。更多信息，请参阅[导出用户的 Autopilot 数据](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure#export-a-users-autopilot-data)。

### 移除已保存的偏好

点明主题，并明确要求从已保存的记忆中移除，而不是从当前回复中略去。你也可以在**查看 [name] 了解什么**中移除一条记忆。

1. 提问：「忘掉我旧的状态更新格式，并从你可访问的记忆笔记中移除该偏好。告诉我哪些记录发生了变化，以及有哪些你无法移除。」
2. 让 Autopilot 再次检查受影响的笔记，并报告它现在对该偏好还记得什么。
3. 检查可能仍然包含该内容的单独导出文件、摘要或文件。

报告说已移除，并不能证明受保留策略管理的记录、备份或所有副本都已被抹除。当你需要正式的访问、保留或删除答复时，请使用你组织的数据管理流程。

### 单独管理对话历史

用上文提到的活动路径找到相关的工作。你也可以问：「列出你可以访问的过往对话，并把它们与后台会话或自动化会话区分开。」

要删除一段对话，请在对话列表中选中它旁边的 **...** 菜单。已删除的对话会从列表中移除，但其存储记录会保留，直到你让 Autopilot 移除它。要永久移除，请问「删除标题为 [名称] 的会话」，然后追问「你现在能永久删除它吗？」并确认结果。在执行破坏性操作之前，先确认所选的是正确的对话。

当你在与 Autopilot 的 Teams 聊天中编辑或删除一条消息时，Autopilot 的对话副本也会更新。开始一段新对话不是删除记忆的操作。独立保存的记忆和导出文件需要单独检查。

如果你想换一个新的 Autopilot 重新开始，请先导出你想保留的任何内容，然后联系你的管理员。不要自行重命名、移动或删除 Autopilot 的文件。
