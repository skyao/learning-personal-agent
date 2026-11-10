---
title: "Microsoft Scout 常见问题"
linkTitle: "文档：常见问题"
date: 2026-08-21
originalTitle: "Microsoft Scout common questions"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/faq"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [运行环境, 模型, 安全]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-08-21"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：文档以问答形式说明 Microsoft Scout 的能力、与 Copilot Chat 的差异、skill、Heartbeat、Automations、shell 三级权限（Auto-approve、Prompt、Deny）和子 agent。它不支持移动设备，并列出可读写的文件类型。LLM 处理经由 GitHub Copilot，模型目录继承自 GitHub Copilot，可用模型由 GitHub Copilot 管理员决定；Scout 不适用于 US Government cloud（GCC、GCC High、DoD）及主权云环境。已知限制包括：默认只在工作区目录内操作，不验证用户自建 skill，后台模式权限更严格。其余问答涉及 ghe.com 登录、GitHub Copilot 许可仍无法登录的检查项、Teams 转录、SharePoint Lists、Outlook 规则、文件共享和 Co-Create 工作区存放位置。

**保留理由**：这是 Scout 不支持移动端、不适用政府云与主权云、模型来源于 GitHub Copilot 等限制的集中说明，并含与 Copilot Chat 的对照表。

---

Microsoft Scout 常见问题

[本文为预发布文档，内容可能变更。]

重要

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能获得 Microsoft Scout 的**早期访问**权限。Frontier 让你直接接触 Microsoft 最新的 AI 创新。Frontier 预览受你客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是预览功能。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布前提供，以便客户提前访问并提供反馈。
- 有关详细信息，请访问我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

在这里找到关于 Microsoft Scout 的常见问题的答案，它是面向 Windows 和 macOS 的 AI 桌面应用。

## 什么是 Microsoft Scout？

Microsoft Scout 是一款桌面 AI 应用，可以代表你在你的文件、shell、浏览器和 Microsoft 365 中执行操作。它在你的工作区中读写文件、运行 shell 命令、控制浏览器、查询你的 Microsoft 365 数据，并在后台自主工作。你只需在对话中描述你需要什么，Microsoft Scout 就会完成工作——敏感操作前会先得到你的批准。

## Microsoft Scout 能为我做什么？

Microsoft Scout 可以：

- 在你的工作区目录中读取、写入和搜索文件。
- 在你的机器上运行 shell 命令、构建、测试和脚本。
- 使用 git、gh、curl 和 PowerShell 探索代码库、应用补丁、运行 linter 并调试失败。
- 自动化浏览器交互——导航页面、填写表单、拍摄快照并检查网络流量。
- 使用快速的模式匹配工具搜索你的工作区。
- 在互联网上搜索实时信息。
- 读取并管理你的电子邮件、日历、Teams 聊天和频道、OneDrive 文件、To Do 任务和会议。
- 使用 WorkIQ 跨 Microsoft 365 服务查询复杂问题。
- 创建和编辑 Word 文档、Excel 电子表格、PowerPoint 演示文稿和图表。
- 按时间表在后台自主运行（Heartbeat 模式）。
- 执行按时间表触发或按条件触发的自动化。
- 把复杂工作委派给专门的子 agent 并行执行。
- 跨对话记住偏好、决策和上下文。

按类别查看完整划分，请参阅[什么是 Microsoft Scout？](https://learn.microsoft.com/en-us/microsoft-scout/overview#what-can-microsoft-scout-do)

## Microsoft Scout 安全吗？

安全。Microsoft Scout 在你的 Microsoft 365 安全边界内运行：

- 在 Windows 上，身份验证使用你组织的 Microsoft 365 凭据。
- Microsoft Scout 只访问你的账户被允许使用的服务和数据。
- shell 命令由你控制的权限系统把关。
- 你可以标记敏感路径，要求访问前获得显式批准。
- Microsoft Scout 把外部内容（电子邮件、网页、Teams 消息）标记为不受信任，并将其视为数据而非指令。

## Microsoft Scout 与 Copilot Chat 有何不同？

Microsoft Scout 是一款本地桌面 AI 应用，在你的机器和你的 Microsoft 365 数据上执行操作；而 Copilot Chat 是一款基于云的对话式应用，用于生成内容和洞察。

| 特性 | Copilot Chat | Microsoft Scout |
| --- | --- | --- |
| 它是什么 | 用于起草、总结、回答问题的云端 AI | 在你的文件、shell、浏览器和 Microsoft 365 上执行操作的桌面 AI 应用 |
| 最适合 | 快速、聚焦的单一任务支持 | 多步骤工作流、本地开发、自主后台任务 |
| 访问本地文件 | 否（基于云） | 是（完整工作区访问） |
| shell 命令 | 否 | 是（三级权限） |
| 浏览器控制 | 否 | 是（浏览器自动化） |
| 自主模式 | 否 | 是（Heartbeat 和自动化） |
| 主要场景 | 快速起草、问答、总结文档 | 构建项目、运行测试、浏览器自动化、多步骤工作流、计划任务 |

Microsoft Scout 在你的桌面上本地运行，可以与你的开发环境、文件系统和 shell 交互，因此非常适合软件开发、自动化以及需要本地访问的任务。

## Microsoft Scout 有哪些 skill？

Microsoft Scout 包含以下捆绑 skill：

- Word (docx) —— 创建、读取和编辑 Word 文档。
- Excel (xlsx) —— 创建、读取和编辑 Excel 电子表格和 CSV 文件。
- PowerPoint (pptx) —— 创建、读取和编辑 PowerPoint 演示文稿。
- Loop —— 使用浏览器自动化编辑 Microsoft Loop 文档。
- Web Artifacts Builder —— 构建可交互的 HTML 仪表板和数据可视化。

你也可以通过把 `SKILL.md` 文件放入你的 skill 目录（`~/.copilot/skills/`）来创建自己的自定义 skill。Microsoft Scout 会自动发现自定义 skill。

详细说明请参阅 [Microsoft Scout skill](https://learn.microsoft.com/en-us/microsoft-scout/overview#bundled-skills)。

## 我可以创建自己的自定义 skill 吗？

可以。通过在 skill 目录中添加含 `SKILL.md` 文件的文件夹来创建自定义 skill：

- **捆绑 skill**：`~/.copilot/bundled-skills/`（随应用提供，用户不可编辑）。
- **工作区 skill**：`~/.copilot/m-skills/`（跨你的设备同步）。
- **全局用户 skill**：`~/.copilot/skills/`（在此机器的所有对话中可用）。

每个 `SKILL.md` 文件包含一个带描述的 YAML frontmatter 块，随后是用 Markdown 编写的 skill 指令。Microsoft Scout 会在每段对话开始时自动发现你的自定义 skill。

分步说明请参阅[创建自定义 skill](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#create-a-custom-skill)。

## 什么是 Heartbeat 模式？

Heartbeat 是一种自主后台模式，Microsoft Scout 会定期运行某个提示词，而不等待你发送消息。你可以配置：

- **提示词**：Microsoft Scout 在每次检入时做什么（例如分拣收件箱或检查日程冲突）。
- **间隔**：运行频率（每 15 分钟、30 分钟、1 小时或 2 小时）。
- **工作时间**：Heartbeat 处于活动状态的日期和时段。
- **权限**：一套独立的权限策略，控制 Heartbeat 在你不在场时可以做什么。

Heartbeat 适用于重复性维护任务、收件箱分拣、日程监控以及其他不需要持续关注的后台工作流。

详情请参阅[使用 Heartbeat 模式](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#use-heartbeat-mode)。

## 什么是自动化？

Automations（自动化）是独立运行的、按时间表触发或按条件触发的任务。与 Heartbeat（使用单个重复执行的提示词）不同，自动化是各自带有时间表、提示词以及可选多步骤工作流的离散任务。

- **按时间表触发**：在特定时间运行（例如「每周一上午 9 点」）。
- **按条件触发**：当你定义的条件变为真时运行。
- **一次性**：运行一次后停用。

你在 Automations 面板中创建、编辑、暂停和删除自动化。

详情请参阅[创建自动化](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#create-automations)。

## shell 命令权限如何工作？

Microsoft Scout 对 shell 命令使用三级权限系统：

| 层级 | 行为 | 示例 |
| --- | --- | --- |
| 自动批准 | 无需提示即可运行 | `ls`、`cat`、`grep`、`git log`、`git diff`、`docker ps`、`npm list`、`gh pr list`、`kubectl get` |
| 提示 | 暂停等待你的批准 | `npm install`、`git push`、`curl`、网络请求、文件写入 |
| 拒绝 | 完全阻止 | 像 `rm -rf /`、`format` 这样的破坏性命令 |

你可以在**设置** > **权限**中自定义哪些命令自动批准、哪些命令被阻止。你也可以把目录标记为敏感路径，使其访问前始终需要批准。

详情请参阅[管理权限](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#manage-permissions)。

## Microsoft Scout 可以把工作委派给子 agent 吗？

可以。Microsoft Scout 可以启动专门的子 agent，它们在后台运行并在完成后报告结果：

| agent 类型 | 它做什么 |
| --- | --- |
| Explore | 跨多个文件和模块的快速代码库研究 |
| Task | 运行构建、测试、lint 和安装 |
| Code review | 分析代码更改中的缺陷和安全问题 |
| Research | 带引用的详尽网络和代码仓库搜索 |
| General-purpose | 用于复杂多步骤工作的完整工具集 |

通过使用子 agent，Microsoft Scout 可以并行处理复杂的调查、在后台运行长时间任务，并处理那些适合隔离执行上下文的工作。

详情请参阅[委派给子 agent](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#delegate-to-sub-agents)。

## 如何开始使用 Microsoft Scout？

开始使用只需几个步骤：

1. 下载并安装适用于 Windows 或 macOS 的 Microsoft Scout。
2. 使用你的 Microsoft 365 凭据登录。
3. 配置你的工作区目录（Microsoft Scout 读写文件的位置）。
4. 可选：连接到 Microsoft 365 以访问电子邮件、日历、Teams 和 OneDrive。
5. 在聊天中输入你想完成的事情，然后发送消息。

详细说明请参阅[开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)。

## Microsoft Scout 能在移动设备上使用吗？

不能。Microsoft Scout 是面向 Windows 和 macOS 的桌面应用。它需要本地文件系统访问、shell 访问和浏览器控制能力，而这些在移动平台上不可用。

## Microsoft Scout 支持哪些文件类型？

Microsoft Scout 可以读取和创建多种文件类型：

- **Word**：`.doc`、`.docx`、`.docm`、`.dot`、`.dotx`、`.odt`、`.rtf`
- **Excel**：`.csv`、`.xls`、`.xlsm`、`.xlsx`、`.ods`
- **PowerPoint**：`.odp`、`.ppt`、`.pptm`、`.pptx`
- **PDF**：`.pdf`
- **Markdown**：`.md`、`.markdown`、`.mdx`
- **图片**：`.png`、`.jpg`、`.jpeg`、`.gif`、`.webp`、`.bmp`、`.svg`、`.ico`
- **文本**：`.txt`、`.log`
- **代码**：`.js`、`.ts`、`.py`、`.java`、`.c`、`.cpp`、`.go`、`.rb`、`.rs` 等
- **配置**：`.json`、`.yaml`、`.yml`、`.toml`、`.ini`、`.xml`、`.env`
- **音频**：`.mp3`、`.wav`、`.m4a`、`.ogg`、`.aac`、`.flac`
- **视频**：`.mp4`、`.mov`、`.avi`、`.mkv`、`.webm`、`.wmv`
- **压缩包**：`.zip`、`.rar`、`.7z`、`.tar`、`.gz`、`.bz2`

## 我可以在不下载文件的情况下预览它们吗？

可以。Microsoft Scout 使用富 Markdown 渲染在对话中直接显示结果。图片内嵌显示，代码块带语法高亮，表格和图表原生渲染。你可以用各自的原生应用打开保存到工作区的文件。

## 操作批准如何工作？

在 Microsoft Scout 执行敏感操作之前（例如发送电子邮件、在 Teams 中发帖，或运行需要批准的命令），它会暂停并向你准确显示它计划做什么。你的选择有：

- **批准**：让 Microsoft Scout 继续执行该操作。
- **始终允许**：批准，并将此模式加入自动批准列表，用于未来的操作。
- **拒绝**：阻止该操作。

你也可以在决定前查看任何操作的技术细节。对于 shell 命令，Microsoft Scout 会显示它想要运行的确切命令。

详情请参阅[批准操作](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#have-a-conversation)。

## 我可以在 Microsoft Scout 工作时暂停或停止它吗？

可以。你可以随时发送后续消息，引导 Microsoft Scout 转向不同方向、提供额外上下文，或让它停止。消息会排队并按顺序处理。

## 如果我失去连接会怎样？

如果 Microsoft Scout 与后端的连接断开，进行中的工作会暂停。连接恢复后，Microsoft Scout 会自动继续。断开连接之前已完成的工作会保留。

## 我的文件保存在哪里？

Microsoft Scout 创建的文件会保存到你的工作区目录（你在设置期间配置的文件夹）。你可以随时通过文件管理器访问这些文件，或让 Microsoft Scout 向你显示工作区中的内容。

## 我可以一次下载所有输出文件吗？

你的工作区目录已经把文件保存在本地。你不需要下载它们，因为它们就在你的机器上。

## 管理员可以禁用 Microsoft Scout 吗？

管理员在受管环境中通过组策略和 Microsoft Intune 管理 Microsoft Scout。Microsoft Scout 管理模板让他们控制谁可以使用 Scout，并关闭特定能力，包括自动化等后台模式。有关详细信息，请参阅[使用组策略管理 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy) 和 [Microsoft Scout 管理员访问概述](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)。

## 有已知限制吗？

有。以下限制是设计使然：

- Microsoft Scout 在你的工作区目录内运行。除非你显式授予权限，否则它无法访问该目录之外的文件。
- shell 命令受三级权限系统约束。危险命令默认被阻止。
- 浏览器控制包含在 Microsoft Scout 中。
- Microsoft Scout 只能访问你的账户被授权使用的 Microsoft 365 数据。
- Microsoft 不验证用户创建的自定义 skill。请仔细审查自定义 skill 的输出。
- 后台模式（Heartbeat 和自动化）使用的权限策略比交互式对话更严格。

## 我如何提供反馈？

通过以下方式分享反馈：

- **点赞或点踩**：直接在对话中评价 Microsoft Scout 的任何回复。
- **报告问题**：使用应用菜单中的反馈选项报告问题或提出改进建议。

## Microsoft Scout 会连接外部模型进行处理吗？

会。Microsoft Scout 通过 GitHub Copilot 处理你的提示词和内容，GitHub Copilot 会连接来自 Microsoft 和第三方提供方（包括开源模型）的 AI 模型。Scout 从 GitHub Copilot 继承其模型目录，你的 GitHub Copilot 管理员决定 Scout 可以使用哪些模型。你可以在 Microsoft GitHub Copilot 文档中找到关于模型提供方及相关信息的详情。支持的模型可能包括第三方和开源模型，包括来自中国提供方的模型。由于这一处理通过 GitHub Copilot 进行，它受你组织的 [GitHub 客户协议](https://github.com/customer-terms)和 [GitHub 通用隐私声明](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)约束。

## 有不支持的国家或地区吗？

Microsoft Scout 目前通过 Frontier 预览计划提供。可用性由该计划的注册情况决定，而不是由 Scout 专属的支持国家或地区列表决定，并且你组织的管理员控制是否为你启用 Scout。

由于 Microsoft Scout 通过 GitHub Copilot 处理提示词和内容，GitHub 的条款和限制适用于该处理，包括适用的贸易管制和制裁要求。详情请参阅 [GitHub 与贸易管制](https://docs.github.com/site-policy/other-site-policies/github-and-trade-controls)。

各个模型提供方可能限制从某些国家或地区使用其模型。你组织有责任确保其对 Microsoft Scout 以及通过 GitHub Copilot 提供的模型的使用符合这些限制。管理员可以限制哪些模型和模型提供方可用。详情请参阅[在 Intune 中管理 Microsoft Scout 的管理员控制项](https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy)。

Microsoft Scout 不适用于美国政府云环境（包括 GCC、GCC High 和 DoD）以及主权和国家云环境。

随着 Microsoft Scout 从预览转为正式发布，区域可用性可能会变化。

## 我可以用 ghe.com 上的 GitHub Enterprise Cloud 登录吗？

可以。在登录屏幕上，打开 **Use a GitHub Enterprise host**，输入你的企业主机（例如 `your-org.ghe.com`），然后选择 **Sign in to GitHub**。登录步骤请参阅[开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started#sign-in)。

## 用户有 GitHub Copilot 许可证但仍无法登录 Microsoft Scout，我该检查什么？

Microsoft Scout 需要两个 GitHub 侧的条件，而不仅仅是一个许可证：

- 该用户已被分配 Copilot **Business** 或 **Enterprise** 席位。
- 你的组织或企业策略允许该用户使用 GitHub Copilot 应用。仅分配席位还不够。

如果用户已有席位，但看到「GitHub Copilot access required」消息或「You aren't authorized to use this Copilot feature」错误，请在企业级和组织级启用 **GitHub Copilot app** 策略（对于 1.1 之前的应用版本，还要启用 **Copilot in the CLI** 策略）。企业设置会覆盖组织设置。同时确认用户使用的是持有该席位的组织 GitHub 账户登录，而不是个人账户。留出几分钟让更改传播，然后让用户退出并重新启动 Microsoft Scout。

完整检查清单请参阅 [Microsoft Scout 管理员访问概述](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview#troubleshoot-github-copilot-access)。

## Microsoft Scout 可以检索 Teams 会议转录并预订会议室吗？

可以。Microsoft Scout 可以检索可用的 Teams 会议转录、查找会议室并预订会议室。有关详细信息，请参阅[在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)。

## Microsoft Scout 可以处理 SharePoint 列表吗？

可以。Microsoft Scout 可以处理 SharePoint 列表。有关详细信息，请参阅[在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)。

## Microsoft Scout 可以管理 Outlook 收件箱规则吗？

可以。Microsoft Scout 可以管理 Outlook 收件箱规则。有关详细信息，请参阅[在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)。

## Microsoft Scout 可以共享 Microsoft 365 文件并管理访问权限吗？

可以。Microsoft Scout 可以把 OneDrive 和 SharePoint 文件共享给特定人员、设置查看或编辑访问权限，并显示当前谁有访问权限。存储在 Teams 中的文件通过其 SharePoint 位置共享。Scout 只与登录的人员共享——它不会创建匿名链接——也无法移除已有的访问权限。有关详细信息，请参阅[在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365#share-files-and-manage-access)。

## 我可以在哪里存储 Co-Create 工作区？

你可以把 Co-Create 工作区存储在本地，或由 OneDrive 或 SharePoint 作为后端。要添加云后端工作区，打开 Co-Create 面板顶部的 **Workspace** 菜单并选择**添加工作区**，然后选择 OneDrive 或 SharePoint。云后端工作区默认对 Microsoft 365 组织账户可用；你可以在**设置**中打开或关闭 **OneDrive & SharePoint Workspaces** 能力。有关详细信息，请参阅[使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#co-create-files-with-microsoft-scout)。

## 相关内容

- [Microsoft Scout 概述](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout)
- [在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)
- [Microsoft Scout 新功能](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
