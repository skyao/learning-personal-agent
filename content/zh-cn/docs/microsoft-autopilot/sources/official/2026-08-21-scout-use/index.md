---
title: "使用 Microsoft Scout"
linkTitle: "文档：使用指南"
date: 2026-08-21
originalTitle: "Use Microsoft Scout"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [持续执行, 记忆与上下文, 功能更新]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-08-05"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：文档是 Microsoft Scout 的完整使用指南，涵盖对话、模型与推理强度选择、文件处理与 Co-Create、搜索、shell 命令、浏览器控制和 Microsoft 365。子 agent 有 Explore、Task、Code review、Research、General-purpose 五类。Heartbeat 可设置 Prompt、Interval（15 分钟、30 分钟、1 小时或 2 小时）、Work days 和 Work hours，并使用独立的更严格权限策略；Automations 支持 Schedule 或 Condition 触发和 One-shot。记忆会跨会话保存并记录来源，会话历史按设备存放在 OneDrive；skill 分 Bundled、Workspace（~/.copilot/m-skills/）、Global user（~/.copilot/skills/）三层，另有 mini mode 和敏感度标签处理。

**保留理由**：这是功能细节最全的操作文档，Heartbeat 参数、Automations 字段、记忆机制和 skill 目录都以此为准。

---

使用 Microsoft Scout

[本文为预发布文档，内容可能变更。]

重要

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能获得 Microsoft Scout 的**早期访问**权限。Frontier 让你直接接触 Microsoft 最新的 AI 创新。Frontier 预览受你客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是预览功能。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布前提供，以便客户提前访问并提供反馈。
- 有关详细信息，请访问我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

Microsoft Scout 是一款桌面 AI 应用，可对你的文件执行操作、运行命令、控制浏览器，并与你的 Microsoft 365 数据协同工作。本文说明如何使用各项能力。

## 进行对话

Microsoft Scout 窗口带有聊天界面，你可以在其中输入请求，并收到以富 Markdown 渲染的回复。

### 发送消息

1. 选择窗口底部的聊天输入框。
2. 输入你的请求。
3. 按 **Enter** 或选择**发送**（Send）。

Microsoft Scout 会立即开始工作。它的回复以完整的 Markdown 格式实时流式呈现：标题、表格、带语法高亮的代码块、Mermaid 图表和内嵌图片。

### 发送后续消息

你可以在 Microsoft Scout 仍在工作时发送更多消息。消息会排队并按顺序处理。如果你的后续消息改变了方向，Microsoft Scout 会调整它的做法。

### 回答 Microsoft Scout 的问题

当 Microsoft Scout 需要更多信息时，它会提供一组选项。选择一个选项并确认。当问题没有固定答案时，你可以输入自己的回答，而不选择预设选项。如果你不想回答，选择**跳过**（Skip）——Microsoft Scout 会凭已知信息继续。

### 缩短过长的对话

长对话可能触及模型的上下文上限。为了在保留重要细节的同时腾出空间，可以按需压缩（compact）对话。Microsoft Scout 会总结较早的轮次，并从缩短后的历史继续，因此你可以在同一段对话中继续工作。

## 选择模型与推理强度

Microsoft Scout 让你控制由哪个模型运行，以及它进行多少推理。

- **按消息切换模型**：使用撰写框中的模型选择器为下一条消息切换模型，而无需新建对话。
- **设置默认推理强度（reasoning effort）**：在**设置**（Settings）中，选择 Microsoft Scout 使用的默认推理强度。更高的强度耗时更多，但能处理更复杂的任务。
- **选择上下文窗口（context window）大小**：选择模型在上下文中保留多少对话历史，最大可选 **Max**，即支持的最大窗口。

## 整理你的对话

左侧导航列出你的对话和自动化。为了保持条理：

- **筛选列表**：显示全部项目、仅聊天或仅自动化。
- **固定并重新排序**：固定重要对话，并把它们拖到你想要的顺序。
- **打开聊天操作**：右键单击对话以重命名、固定、删除或标记为未读。
- **标记为未读**：给对话加上标记，以便稍后再看。

## 处理文件

Microsoft Scout 会在你的工作区目录中读取、写入和搜索文件，也可以处理工作区之外的文件。当 Microsoft Scout 第一次需要工作区之外的文件夹（例如你的「下载」或「文档」文件夹）时，它会请你授予对该文件夹的访问权限。你批准一次之后，Microsoft Scout 就可以在后续操作中使用该文件夹。

### 创建文件

让 Microsoft Scout 创建文件，它会直接写入你的工作区。例如：

- 「创建一个 markdown 文件，总结我们的架构决策。」
- 「把你在我邮件里找到的销售数据生成一份 CSV。」
- 「构建一个显示项目状态的 HTML 仪表板。」

创建的文件会出现在你的工作区目录中，Microsoft Scout 可以在对话中内嵌显示图片。

### 编辑文件

Microsoft Scout 可以读取并修改你工作区中已有的文件：

- 「更新 README，加入新的 API 端点。」
- 「修正 report.docx 中的格式。」
- 「给电子表格加一列计算后的总计。」

### 与 Microsoft Scout 共同创建文件

Co-Create（共同创建）工作区可以存储在本地，也可以由 OneDrive 或 SharePoint 作为后端。要添加云后端工作区，选择 Co-Create 面板顶部的 **Workspace** 菜单（它显示当前工作区名称），选择**添加工作区**（Add workspace），选择 OneDrive 或 SharePoint，然后选择一个现有文件夹或创建新文件夹。云后端工作区默认对 Microsoft 365 组织账户可用；你可以在**设置**中打开或关闭 **OneDrive & SharePoint Workspaces** 能力。当你和 Microsoft Scout 同时处理同一个文件时，你的编辑和 Microsoft Scout 的编辑会自动合并。Co-Create 在应用内编辑器中打开文件，并包含适用于 Markdown、源代码、结构化数据和 HTML 的编辑器。支持的文件类型包括文本和代码文件、Markdown、配置文件、CSV 和 TSV、Mermaid 图表以及 Excalidraw 绘图。在 Markdown 编辑器中，你可以针对特定段落添加内联评论。

当 Microsoft Scout 正在写入时，你会看到：

- 编辑器上方的一个 **Agent is editing this file**（智能体正在编辑此文件）标记。
- Microsoft Scout 最后编辑位置上的彩色光标。
- 当你已经空闲几秒钟后，编辑器会滚动跟随 Microsoft Scout 的光标，因此在你打字时它不会抢占焦点。

你可以在 Microsoft Scout 工作时继续输入。你的更改会保存到工作区中的文件，Microsoft Scout 下次处理该文件时会读取它们。

注意

如果你断开连接，编辑器仍可使用，你的编辑仍会留在屏幕上，但在连接恢复之前它们不会与 Microsoft Scout 同步。

### 搜索文件

Microsoft Scout 会在你的工作区目录中搜索内容：

- 「找出所有提到季度预算的文件。」
- 「哪些 TypeScript 文件导入了 auth 模块？」
- 「给我看看项目文件夹里最近修改的文件。」

### 使用文档 skill

对于结构化的文档创建，Microsoft Scout 会加载专门的 skill：

| skill | 用途 |
| --- | --- |
| Word (docx) | 报告、备忘录、提案、信函——任何结构化的 Word 文档 |
| Excel (xlsx) | 电子表格、数据分析、格式化表格、图表 |
| PowerPoint (pptx) | 幻灯片、演示文稿、路演材料 |
| Web Artifacts Builder | 可交互的 HTML 仪表板、数据可视化、组织架构图 |

当 Microsoft Scout 判断需要这些 skill 时，它们会自动激活。

## 搜索与研究

Microsoft Scout 提供快速的本地搜索和更广泛的研究能力。

### 本地搜索

Microsoft Scout 使用快速的模式匹配工具在工作区的文件中搜索：

- 按名称模式查找文件：「在 components 目录中找出所有 `.tsx` 文件。」
- 搜索文件内容：「哪些文件引用了 `AuthContext` 变量？」
- 组合模式：「找出所有导入了 API 客户端的测试文件。」

本地搜索很快，且不需要网络访问。

### 网络研究

对于需要互联网上最新信息的问题，Microsoft Scout 会搜索网络、抓取页面，并汇总结果并附上引用。

### 研究 agent

对于需要并行搜索多个来源的复杂调查，Microsoft Scout 可以启动专门的研究 agent。这些 agent 会搜索代码仓库、抓取文档、验证说法，并汇总详细的发现。对于这类宽泛的问题，可以使用研究 agent：

- 「使用 PKCE 实现 OAuth 2.0 的最佳实践是什么？」
- 「比较这三个 CSS-in-JS 库的优缺点。」
- 「找到这个 API 端点的文档，并解释分页如何工作。」

## 运行 shell 命令

Microsoft Scout 在你的机器上执行 shell 命令。你可以让它运行脚本、安装包、构建项目、检查系统状态，或使用 `git`、`gh`、`curl` 和 PowerShell 等开发者工具。

### 常见开发任务

- 运行构建：「构建项目并向我显示所有错误。」
- 运行测试：「运行测试套件并报告失败。」
- 运行 linter：「对 src 目录执行 lint 并修复所有问题。」
- 使用 git：「显示最近 3 次提交的 diff」或「创建一个分支并提交我的更改。」
- 使用 gh：「列出我打开的 PR」或「用这段描述创建一个 PR。」
- 调试：「以详细输出运行失败的测试，并解释错误。」

### shell 命令的权限层级

命令被分为三个层级：

| 层级 | 行为 | 示例 |
| --- | --- | --- |
| 自动批准 | 无需提示即可运行 | `ls`、`cat`、`grep`、`git log`、`git diff`、`docker ps`、`npm list`、`gh pr list`、`kubectl get` |
| 提示 | 暂停等待你的批准 | `npm install`、`git push`、`curl`、网络请求、文件写入 |
| 拒绝 | 完全阻止 | 像 `rm -rf /`、`format` 这样的破坏性命令 |

当命令需要批准时，Microsoft Scout 会在运行前向你显示确切的命令。选择**批准**（Approve）继续，或选择**拒绝**（Deny）阻止它。

### 自定义 shell 权限

在**设置** > **权限**中，你可以：

- 向**允许列表**（allow list）添加模式，使特定命令无需提示即可运行。
- 向**拒绝列表**（deny list）添加模式，以阻止某类命令。
- 打开或关闭**自动批准只读**（Auto-approve read-only）。
- 定义始终需要批准才能访问的**敏感路径**（sensitive path）。

## 控制浏览器

Microsoft Scout 可以自动化浏览器。它可以浏览网站、填写表单、点击按钮、截取屏幕截图，并从页面中提取内容。

### 浏览器控制能做什么

- 导航到任意 URL 并与页面元素交互（点击、输入、填写表单、上传文件）。
- 对页面拍摄快照，以检查页面的当前状态。
- 截取整页或特定元素的屏幕截图。
- 读取控制台日志并检查网络请求以进行调试。
- 从页面中提取文本内容。
- 在交互前等待元素加载。

### 示例

- 「进入 Azure 门户，查看我的资源组本月的费用。」
- 「打开那个 wiki 页面，更新发布说明部分。」

### Microsoft Loop 集成

捆绑的 Loop skill 使用浏览器控制来编辑 Microsoft Loop 文档。让 Microsoft Scout 更新 Loop 页面，它会导航到该文档、进行编辑并确认更改。

## 使用 Microsoft 365

Microsoft Scout 可以处理 Outlook 邮件和日历、Teams 会议和消息、SharePoint 列表，以及 OneDrive、SharePoint 和 Teams 中的文件。它可以检索可用的会议转录、预订会议室、管理收件箱规则，并帮助管理文件共享和访问。

请求示例、批准指导和访问排障，请参阅[在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)。

## 委派给子 agent

对于复杂或可并行的工作，Microsoft Scout 会启动专门的子 agent，它们在后台运行，完成后报告结果。

### 可用的 agent 类型

| agent 类型 | 它做什么 | 何时使用 |
| --- | --- | --- |
| Explore | 跨多个文件和模块的快速代码库研究 | 理解不熟悉的代码、追踪数据流、分析架构 |
| Task | 运行构建、测试、lint 和安装 | 运行测试套件、构建项目、安装依赖 |
| Code review | 分析代码更改中的缺陷和安全问题 | 审查 diff、在提交前检查逻辑错误 |
| Research | 带引用的详尽网络和代码仓库搜索 | 调查技术问题、比较库、查找文档 |
| General-purpose | 用于复杂多步骤工作的完整工具集 | 跨文件重构、实现功能、复杂迁移 |

### 委派如何工作

1. Microsoft Scout 判断某项任务适合并行执行或隔离的上下文。
2. 它带着具体指令启动一个或多个子 agent。
3. 子 agent 在后台独立工作。
4. 它们完成后，Microsoft Scout 把结果并入你的对话。

你也可以显式请求委派：「研究其他团队如何实现缓存，同时你开始设置数据库配置。」

## 使用 Heartbeat 模式

Heartbeat 是一种后台模式，Microsoft Scout 会定期运行某个提示词，而不等待你发送消息。

### 启用 Heartbeat

1. 从应用导航打开 **Heartbeat** 面板。
2. 将 Heartbeat 切换为**开启**。
3. 配置以下设置：

| 设置 | 它控制什么 |
| --- | --- |
| 提示词（Prompt） | Microsoft Scout 在每次检入时做什么。请像写一条重复执行的指令那样写它。 |
| 间隔（Interval） | Heartbeat 运行的频率：每 15 分钟、30 分钟、1 小时或 2 小时。 |
| 工作日（Work days） | Heartbeat 在星期几处于活动状态（例如周一至周五）。 |
| 工作时间（Work hours） | 活动窗口的开始和结束时间（例如上午 9 点到下午 6 点）。 |

### Heartbeat 权限

Heartbeat 有自己的权限策略，与你的交互式会话分开。由于 Heartbeat 期间你不在场批准操作，该策略通常更严格：

- 外发消息（电子邮件、Teams）只使用通用内容——绝不使用私有数据。
- 暂定的日历事件被视为忙碌（这是保守的选择）。
- 通常需要批准的操作在 Heartbeat 模式下会被跳过。

你可以从 Heartbeat 面板自定义 Heartbeat 权限。

### 查看 Heartbeat 活动

Heartbeat 面板显示最近检入的日志。每条记录显示 Microsoft Scout 做了什么以及何时做的。选择任意记录可查看完整详情。

## 创建自动化

Automations（自动化）是按计划运行或在条件满足时运行的独立任务。

### 创建自动化

1. 打开 **Automations** 面板。
2. 选择**新建自动化**（New automation）。
3. 填写表单：

| 字段 | 描述 |
| --- | --- |
| 名称 | 此自动化的描述性名称。 |
| 提示词 | Microsoft Scout 在触发时执行的指令。 |
| 触发类型 | **Schedule**（按时间表运行）或 **Condition**（在某个条件变为真时运行）。 |
| 时间表 | 对于时间表触发：何时运行（例如「每周一上午 9 点」）。 |
| 条件 | 对于条件触发：检查什么，以及多久检查一次。 |
| 一次性（One-shot） | 如果启用，自动化运行一次后停用。 |
| 推理强度 | 此自动化运行时 Microsoft Scout 使用的推理强度。 |
| 上下文大小 | 此自动化的上下文窗口大小，独立于你的其他对话设置。 |

1. 选择**保存**（Save）。

### 管理自动化

在 Automations 面板中，你可以：

- **启用或禁用**自动化而不删除它。
- **编辑**提示词、时间表或触发条件。
- **查看历史**以查看过去的运行及其结果。
- **删除**你不再需要的自动化。

### 导入自动化

你可以使用 Automations 面板中的导入功能，从 GitHub 仓库导入自动化定义。

## 管理权限

权限系统让你对 Microsoft Scout 能做什么进行精细控制。

### 打开权限设置

转到**设置** > **权限**，以使用完整的权限编辑器。

### 配置工具组

打开或关闭整个能力类别：

| 类别 | 它控制什么 |
| --- | --- |
| 文件系统访问 | 在工作区中读取、写入和搜索文件 |
| Shell | 运行 shell 命令和脚本 |
| 浏览器控制与网页浏览 | 浏览器和网页自动化 |
| WorkIQ | 复杂的 Microsoft 365 查询 |

当你禁用某个类别时，Microsoft Scout 完全无法使用那些工具——它们不会出现在系统提示词中。

### 配置 shell 模式

为 shell 命令定义自定义的允许和拒绝模式：

- **允许模式**：匹配这些模式的命令会被自动批准，无需提示。例如 `npm test` 或 `python *.py`。
- **拒绝模式**：匹配这些模式的命令总是被阻止。

### 标记敏感路径

添加需要显式批准才能让 Microsoft Scout 读取或写入的目录或文件路径，即使该操作本来会获得自动批准。

## 使用记忆与会话历史

Microsoft Scout 会跨对话记住偏好、决策和上下文，并可以搜索你过去的会话历史。

### 记忆如何工作

- Microsoft Scout 会在你工作时主动保存重要信息——你无需开口要求。
- 记忆跨会话持久保存，并可在未来的对话中使用。
- 每条记忆都会记录其来源（provenance，即它来自哪里）：会话推断、导入或外部。

### 搜索过去的会话

Microsoft Scout 可以搜索你的对话历史以回忆之前的工作：

- 「我上周做了什么？」
- 「在上一个项目中我是如何处理身份验证的？」
- 「找到我设置 CI 流水线的那次会话。」

会话历史搜索帮助你重温决策、找到类似问题的先前做法，并回忆起早前对话中的上下文。

你也可以按需恢复较早的对话，从上次停下的地方继续。你的会话历史按设备存储在 OneDrive 中，因此每台设备保留自己的对话。

### 查看和管理记忆

1. 打开**设置**。
2. 在记忆部分选择**查看记忆**（View memories）。
3. 查看已存储的记忆。删除任何不再相关的记忆。

### 记忆与隐私

来自外部来源的记忆（电子邮件和网页消息）会标注其来源。Microsoft Scout 把外部来源的记忆当作数据而非指令，并在据此行动前与你确认。

## 使用迷你模式

迷你模式（mini mode）提供一个紧凑、始终可见的窗口，用于快速交互。

在设置的**窗口行为**部分，你可以配置：

- Microsoft Scout 是否以迷你模式启动。
- 始终置顶行为。
- 用于切换迷你模式的键盘快捷键。

## 处理敏感度标签

Microsoft Scout 会跟踪你在会话期间访问的内容上的 Microsoft 信息保护（Microsoft Information Protection，MIP）敏感度标签。

### 标签如何工作

- 当你读取带有敏感度标签（例如「机密」）的电子邮件或文件时，会话的敏感度级别会升高。
- Microsoft Scout 不会把带标签的内容写入未受保护的目标（Teams 频道、纯文本文件、外部工具）。
- 如果你让 Microsoft Scout 共享机密内容，它会提醒你会话的敏感度级别并要求确认。
- 在把提升敏感度级别的会话中创建的文档对外共享之前，你应当先给它们加上标签。

界面会显示当前会话的敏感度级别。

## 管理 skill

### 查看活动 skill

Microsoft Scout 在对话期间加载的 skill 会出现在对话上下文中。捆绑 skill 始终可用。Microsoft Scout 会从你的 skill 目录中发现自定义 skill。

### 创建自定义 skill

1. 转到你的 skill 目录（`~/.copilot/skills/`）。
2. 创建一个以你的 skill 命名的子文件夹（例如 `weekly-report/`）。
3. 在子文件夹内创建一个名为 `SKILL.md` 的文件。
4. 添加一个带有描述的 YAML frontmatter 块，随后是 skill 指令。

   ```
   ---
   description: "Generates a weekly status report from my recent activity."
   ---

   Review my sent emails, calendar events, and completed tasks from the past
   week. Create a markdown summary organized by project, highlighting key
   decisions, blockers, and next steps.
   ```
5. 保存文件。Microsoft Scout 会在未来的对话中自动发现它。

### skill 层级

| 层级 | 位置 | 行为 |
| --- | --- | --- |
| Bundled | 随应用一起提供 | 始终可用，随应用版本更新 |
| Workspace | `~/.copilot/m-skills/` | 通过云同步跨设备同步 |
| Global user | `~/.copilot/skills/` | 在此机器的所有对话中可用 |

### 禁用捆绑 skill

在**设置**中，你可以打开或关闭单个捆绑 skill（如果你不需要它们）。

## 相关内容

- [Microsoft Scout 概述](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [在 Microsoft Scout 中使用 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)
- [Microsoft Scout 常见问题](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- [Microsoft Scout 新功能](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
- [Microsoft Scout 负责任 AI 概述](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview)
