---
title: "Copilot 十月新功能汇总（含 Autopilot 与新 Home）"
linkTitle: "Copilot 十月新功能"
date: 2026-10-30
originalTitle: "What’s New in Microsoft Copilot | October 2026"
sourceUrl: "https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--october-2026/4568528"
altUrls: []
author: "Daniel_Vargas"
publisher: "Microsoft Tech Community（Microsoft Copilot Blog）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-14
tags: [功能更新, 运行环境, 开放与价格]
products: [microsoft-autopilot]
updatedAt: "2026-11-13"
dateNote: "JSON-LD datePublished 为 10/30/2026；article:modified_time 为 2026-11-13，页面标 Version 5.0"
---

{{< source-info >}}

**收录说明**：Microsoft Copilot 的月度新功能汇总，全文涉及 Copilot app、Cowork、Office 应用、Teams 与管理员功能，按全文存档；摘要只写 Autopilot 相关部分。线索来自 aguidetocloud 的 11 月汇总。直接下载，删去了作者卡片、标签等页面元素。已翻译。

**内容摘要**：这是 Microsoft Copilot 2026 年 10 月的月度新功能汇总，涵盖 Copilot app、Cowork、Workspaces、Word/Excel/PowerPoint、Teams 与管理员功能。文中称 Autopilot 是「always-on、cloud-based personal agent」，用户通过给它目标来塑造职责，它拥有自己的账号、邮箱和文件，启用时可与同事协作，并能跨用户的本地文件和它自己的远程计算机运行。访问控制、审批护栏和受支持的信息保护与合规能力用于让关键操作保持在人的控制之下，组织可通过 Agent 365 了解谁在使用 Autopilot、管理其访问、评估风险并衡量业务价值。文中写明 Autopilot 11 月向 Frontier 推出。同一汇总称新的 Home 把 Chat 与 Cowork 合在一处，10 月进入 Frontier、11 月全球推出。

**保留理由**：这是更名后对 Autopilot 形态最具体的官方描述（云端、自有账号与邮箱、远程计算机加本地文件、Agent 365 治理），并给出 11 月进入 Frontier 的时间；Learn 文档仍只描述 Scout 桌面应用。

---

欢迎阅读 2026 年 10 月版的 What's New in Microsoft Copilot！每个月，我们都会介绍新功能与功能增强，帮助 Microsoft 365 客户及时了解 Copilot 的最新能力，让用户在每天使用的应用中更高效、更有成效。

让我们来仔细看看本月有哪些新内容：

**用户功能：**

- [Copilot 中更新的 Home 导航、Projects（项目）、Workspaces（工作区）与 Autopilot](#community-4568528-home)
- [Copilot Cowork 的角色型插件、Outlook 与 Planner 增强以及任务目录](#community-4568528-role)
- [Copilot Workspaces 的文件编辑、音频更新与更多引用类型](#community-4568528-notebooks)
- [Copilot in OneDrive 中的 Prompt Gallery](#community-4568528-prompt)
- [SharePoint 中的 Knowledge base](#community-4568528-base)
- [Copilot in Excel 的会计技能、数据清理技能与交互式画布](#community-4568528-Excel)
- [Copilot in PowerPoint 的模型更新、品牌套件改进与技能](#community-4568528-brand)
- [Copilot in Word 的法律插件与按文档类型设计](#community-4568528-legal)
- [Copilot in Microsoft Edge 的更新体验](#community-4568528-Edge)
- [Copilot in Teams 的智能回顾与 Queues 应用更新](#community-4568528-teams)
- [Copilot 的新生命科学连接器](#community-4568528-life)
- [政府云中的 Copilot 编辑能力](#community-4568528-clouds)

**IT 管理员功能：**

- [Insights Agent 与 Workforce Insights Agent](#community-4568528-agents)
- [Microsoft Purview 数据丢失防护的保留配置与 Microsoft Cowork 扩展](#community-4568528-loss)

## 用户功能

#### 访问、组织并推进工作的新方式

**Home** 是 Copilot app 中工作的起点，现在**把 Chat 与 Cowork 合在一处**，并新增**共享导航窗格**。Chat 与 Cowork 提供两种完成工作的方式。Chat 可以回答问题、探索想法、执行操作并创建初稿，Cowork 则可用于委派复杂的多步骤任务。共享导航窗格采用了新的布局：

- **Agents & Plugins** 提供一个统一的位置，用来发现和访问 agent、技能（skills）与连接器。
- **Automations** 按计划或在指定事件发生时运行 Cowork 任务，让例行工作无需手动提示就能持续推进。
- **Workspaces** 为团队在 Copilot app 中提供共享空间，与 Copilot 一起处理持续进行的工作流。
- **Projects** 把相关的任务、指令与上下文放在一起。
- **合并的 Chat 与 Cowork 对话历史**，带搜索和筛选，帮助用户快速回到正确的对话线程。

此更新 10 月向 Frontier 推出，11 月在全球推出。

**Projects** 提供一个专用空间，把相关的聊天、任务、指令与上下文放在一起，用户无需每次重建上下文即可接着工作。用户可以设置适用于整个项目的指令，把文件、会议、聊天和任务添加为共享上下文，并从集中的 Outputs 视图访问项目任务创建的文件。这有助于用户在持续进行的工作中保持上下文和一致性，同时让每个项目专注于一个特定主题。了解更多：[使用 projects](https://learn.microsoft.com/copilot/cowork/cowork-projects)。此功能 10 月已在 Cowork 中推出，11 月在 Copilot Chat 中推出。

**Autopilot 是一个 always-on、基于云的个人 agent**，替用户分担工作，并让工作持续推进，而无需用户指挥每一步。用户通过给它设定目标来塑造它的职责，持久的上下文与记忆则帮助它在整个 Microsoft 365 中与用户的优先事项保持关联。Autopilot 拥有自己的账号、邮箱和文件，能够推进工作、在启用时与同事协作、通过用户已在使用的 Microsoft 365 体验保持可访问，并能跨用户的本地文件和它自己的远程计算机运行。访问控制、审批护栏以及受支持的信息保护与合规能力，帮助保护敏感信息，并让关键操作保持在人的控制之下。借助 Agent 365，组织可以了解谁在使用 Autopilot、管理并治理它的访问、评估风险，并衡量业务价值以指导推广。Autopilot 11 月向 Frontier 推出。

Word、Excel 和 PowerPoint 中的 Copilot 体验正在获得**焕新的设计**，与 Copilot app 中的设计保持一致，带来一致的用户体验。这一焕新设计简化了聊天与响应的布局，并改进了导航。此功能 10 月已推出。

技能（Skills）帮助把专业知识转化为 Copilot 可自动应用的可复用能力，使执行更快、结果更一致，也让知识在团队间更容易共享。**技能正从仅在 Cowork 中提供扩展到 Copilot Chat**，把可复用的专业能力直接带入日常工作流程。用户现在可以在 Copilot Chat 中用自然语言直接创建自己的技能，通过 Agents & Plugins 部分发现同事或所在组织共享的技能，并选择在工作流程中何时以及如何使用技能。通过沉淀可复用的指令与专业知识，技能帮助团队在各 Copilot 体验中推广一致的做法。此功能 11 月推出。

#### Copilot Cowork 的角色型插件、Outlook 与 Planner 增强以及任务目录

**Cowork 中的角色型插件**为销售、服务、教育、法律和财务等领域的常见业务流程提供预置技能。用户可在 Roles & Industry 下访问这些插件，其中的技能面向会议准备、案件分流、认证证据和对照 playbook 审查合同等场景。这为用户提供了一种更快的方式，按预定义的工作流程开始专门化、可重复的工作，而不是从空白提示开始。了解更多：[Copilot Cowork 可用的插件](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-available-plugins)。此功能 10 月已推出。

**Cowork 中的 OneNote 与 Planner 能力**把用户的笔记、决策、任务和计划带入 Cowork 工作所依据的上下文。Cowork 现在可以通过 OneNote 插件读取和更新笔记本。借助 Planner 能力，用户可以用自然语言查看、创建和更新计划、bucket、目标与任务，再利用这些上下文在 Microsoft 365 中开展相关工作。这帮助用户在一次对话中从记录与规划工作过渡到付诸行动，进展经用户批准后写回 OneNote 和 Planner。这些功能[10 月向 Frontier 推出，11 月在全球推出](https://www.microsoft.com/microsoft-365/roadmap?id=567315)。

Cowork 中的**任务目录**现在为销售、营销、客户服务和财务的常见场景提供建议任务。用户可以选择一个任务、提供所需信息，再交给 Cowork 完成。这帮助用户无需从头构建每个请求，就能开始常见的角色型工作。此功能 10 月已推出。

Cowork 允许用户在新请求中**引用之前的 Copilot Chat 对话和 Cowork 任务**，从而在早期工作的基础上继续，无需重新建立上下文。用户可以把一次聊天或一个任务作为上下文加入提示，就像引用文件或会议一样，让 Cowork 把之前的决策或产出纳入新任务。这使用户可以轻松地从 Chat 中最初的探索转到更复杂的 Cowork 任务，或把一个任务的结果作为另一个任务的起点。此功能 10 月已推出。

#### Copilot Workspaces 的文件编辑、音频更新与更多引用类型

**Copilot Workspaces** 为团队在 Copilot app 中提供与 Copilot 一起工作的共享空间。作为 Copilot Notebooks 的演进，Copilot Workspaces 把上下文、团队成员和工作文件汇集在一起，让团队可以创建、打磨并推进持续进行的工作流。现有的笔记本将变为工作区，体验经过更新，专为团队协作设计。可以与团队同时跨不同文档协作，并通过实时光标看到他们正在处理什么。此变更 10 月已向 Frontier 推出。

**Copilot Workspaces 现在允许用户直接在工作区内创建、编辑和协作处理 Word、Excel 和 PowerPoint 文件。**用户可以在聊天中让 Copilot 创建或编辑 Office 文件，然后使用 Office 能力直接在这些文件中工作，无需离开 notebook。这帮助用户在从与 Copilot 协作转到打磨和协作处理 Office 文件时，让内容与工作流程保持在一起。此功能 10 月已向 Frontier 推出，1 月在全球推出。

**Copilot Workspace 中的 Audio Overview（音频概览）**新增按主题划分的剧集、敏感度标签支持和更多受支持的内容类型。较长的概览现在可以拆分为按主题划分的剧集，保存到 OneDrive 的音频概览现在会继承其来源的敏感度标签。Audio Overview 还可以对更多引用类型进行推理，例如 Outlook 邮件、Teams 会议和聊天、OneNote 与 Loop 页面，以及纯文本（.txt）文件。此外，现在还提供了新的音频格式，例如 「Critique and Debate」。此功能 10 月已向 Frontier 推出，11 月在全球推出。

**Copilot Workspace 现在接受更多文件类型作为引用**，如 JPG、PNG、CSV 和 TSV 文件。用户可以把图像、结构化列表和表格与传统文档一起添加到工作区，作为 Copilot 的依据上下文。这些额外的上下文帮助 Copilot 生成更相关的演示文稿、报告和简报。此功能 10 月已推出。

#### Copilot in OneDrive 中的 Prompt Gallery

Copilot in OneDrive 中新的 **Prompt Gallery** 为常见的文件任务提供现成可用的提示。用户选择 OneDrive 右下角的 Copilot 按钮，选择 Open Prompt Gallery，然后按 Create、Analyze、Find 和 Collaborate 等类别浏览提示。这帮助用户发现 Copilot 能做什么，并更快地从中获得价值。此功能[10 月已推出](https://www.microsoft.com/microsoft-365/roadmap?id=571308)。

#### SharePoint 中的 Knowledge base

**SharePoint 中的 Knowledge base** 帮助组织把来自整个 Microsoft 365 的信息转化为可供人、Copilot 和 agent 使用的共享知识。它汇集来自邮件、消息、会议和 SharePoint 内容的信息，创建一个可访问、保持最新的知识库。这使人们更容易找到组织知识，也为 Copilot 和 agent 提供可在工作中使用的相关上下文。了解更多：[Introducing a team knowledge base, curated by Copilot and agents](https://techcommunity.microsoft.com/blog/SPBlog/introducing-a-team-knowledge-base-curated-by-copilot-and-agents/4564203)。此功能 10 月已向 Frontier 推出。

#### Copilot in Excel 的会计技能、数据清理技能与交互式画布

**Excel 中的会计技能**把财务推理与 Excel 原生能力结合起来，帮助会计人员对账、准备日记账分录并分析财务表现以用于报告。Copilot 直接在工作簿中工作，让更改保持可见且可撤销，财务专业人员可以审查结果并保留最终决定权。该功能 10 月已向 Frontier 推出，11 月在全球推出。

**Excel 中的数据清理技能**帮助用户发现容易被忽略的数据质量问题。Copilot 扫描工作簿中的重复项、格式不一致和数据类型错误等问题，然后直接在文件中推荐修复方案。用户审查并批准每一项更改，因此你所在组织的分析建立在人们可以信任的数据之上。此功能 10 月已推出。

**Excel 中的交互式画布（Interactive canvas）**使用 Copilot 把工作簿数据转化为包含关键可视化、指标和洞察的精美报告。画布会随底层数据变化自动更新，用户也可以通过与 Copilot 聊天来修改它。团队无需手工制作报告，就能获得最新、可共享的数据视图。此功能 10 月已向 Insiders 推出，[11 月在全球推出](https://www.microsoft.com/microsoft-365/roadmap?id=569424)。

#### Copilot in PowerPoint 的模型更新、品牌套件改进与技能

**PowerPoint 中的 Sonnet 5.5** 带来更强的设计视角，帮助用户借助 Copilot 创建精致、视觉效果出众的演示文稿。当用户把想法变成演示文稿时，该模型帮助改进幻灯片版式、强化视觉层次，并更一致地应用模板。这帮助用户创建更用心、更统一、能够吸引听众的演示文稿。此功能 10 月已推出。

**PowerPoint 中的品牌套件（Brand Kit）设置现在更简单，**品牌管理者可以更快地创建和配置品牌套件。精简的素材管理和改进的工作流程减少了建立一个套件所需的步骤。组织可以用更少的设置工作量，大规模推出带品牌的演示文稿体验。了解更多：[创建和管理官方品牌套件](https://support.microsoft.com/microsoft-365-copilot/create-and-manage-official-brand-kits-in-the-microsoft-365-copilot-app)。此功能 10 月已推出。

品牌管理者现在可以在 PowerPoint 中**发布和取消发布官方品牌套件**。专用的发布流程控制套件何时对用户可用，并允许管理者在需要时将其下架。组织可以更好地控制员工和 Copilot 在演示文稿中使用哪些品牌素材。此功能 10 月已推出。

**Create interactive slide（创建交互式幻灯片）**让用户通过一个简单的提示或现有内容生成交互式幻灯片。用户可以创建交互式的信息呈现方式，例如仪表板洞察、业务流程、时间线或对比。这有助于让复杂信息对演示听众来说更易理解、更有吸引力、更令人印象深刻。此功能 10 月已推出。

**模板评估技能（template assessment skill）**通过识别可能影响 Copilot 生成的演示文稿的问题，帮助用户为品牌套件准备 PowerPoint 模板。该技能评估一个模板，并在品牌套件发布前针对潜在问题提供可操作的建议。这帮助组织预先改进其模板，使 Copilot 能够使用已评估过潜在问题的品牌套件生成内容。此功能 10 月已推出。

**Record a skill（录制技能）**让用户把经常重复的演示文稿任务变成可复用的技能。用户可以捕获自己经常执行的任务，将其保存为技能，并在需要完成同类工作时再次运行。这帮助用户更快、更一致地完成可重复的演示文稿任务，无需每次从头开始。此功能 10 月已推出。

#### Copilot in Word 的法律插件与按文档类型设计

**法律插件（legal plugin）**把 20 多个专门构建的法律技能和合作伙伴构建的插件直接带入 Word，建立在此前以 Legal Agent 推出的能力之上。法律团队可以使用这些能力，根据先例起草协议、对照法律 playbook 审查合同，并直接在文档中做出精确的编辑和修订标记（redline）。通过把法律专用的推理与 Word 的原生能力结合，这帮助法律团队在 Word 内完成更复杂的文档工作流程。了解更多：[Copilot for legal](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-microsoft-copilot-for-legal/4564246)。此功能 10 月已推出。

**按文档类型的格式与设计（Document-specific formatting and design）**帮助用户创建精致、专业的文档。Copilot 会根据所创建文档的类型，自动应用量身定制的结构、版式、格式和视觉设计。这帮助用户更快地从空白页走到设计良好的文档，在格式和版式上花费更少的精力。此功能 10 月已推出。

Word 中的 **Markdown 支持**让用户轻松把基于 Markdown 的工作流程中的内容带入 Word 并继续处理。用户可以在写作时使用 Markdown 快捷方式，在 Word 与 Markdown 之间复制粘贴并保留格式，并在网页版中在 .md 与 .docx 文件之间转换。这帮助用户在基于 Markdown 的工作流程与 Word 之间更顺畅地切换，无需手动重建或重新格式化内容。此功能 10 月已推出。

#### Copilot in Microsoft Edge 的更新体验

**Copilot in Microsoft Edge 的体验正在变得更简洁**，所有 Copilot 入口使用更新后的图标，并采用精简的 Copilot 侧窗格。这些用户体验变更将在未来几周内陆续推出，现有的安全、合规、隐私和企业控制保持不变。用户获得更清爽、更一致的 Copilot 访问方式，而组织保持与现在相同的治理。此功能 10 月已推出。

#### Copilot in Teams 的智能回顾与 Queues 应用更新

**不保存转录的智能回顾（Intelligent recap）**让会议组织者开启 AI 生成的会议摘要，而无需在会后保留转录。拥有 Copilot 许可证的组织者可以在会前开启或关闭它，有许可证的组织者和参与者可以在会议期间管理它。会后可获得包含关键决策、行动项和要点的回顾。无法或不愿保留转录的组织仍然可以为用户提供会议回顾，同时满足其隐私与合规需求。此功能 5 月在 Public Preview 推出，[10 月在全球推出](https://www.microsoft.com/microsoft-365/roadmap?id=558286)。

**Queues 应用中的智能通话回顾（Intelligent call recaps）**帮助用户通过 AI 生成的摘要笔记，了解已录音或已转录的队列通话，笔记涵盖关键讨论要点和后续行动。要打开回顾，用户在 Queues 应用的通话历史中找到通话记录并选择 Recap。此功能[9 月已推出](https://www.microsoft.com/microsoft-365/roadmap?id=568933)。

用户可以在 Teams Phone 的 **Queues 应用共享通话历史**中使用 Copilot，快速了解通过呼叫队列处理的通话并发掘关键细节。已录音的通话结束后，拥有 Copilot 的用户现在可以在共享通话历史中打开通话记录，从 Recap 选项卡访问 Copilot Chat 侧边栏，并就该通话提问。此功能[9 月已推出](https://www.microsoft.com/microsoft-365/roadmap?id=568933)。

#### Copilot 的新生命科学连接器

**新的生命科学连接器**为研究人员和其他生命科学专业人员带来值得信赖的、面向行业的资源，扩展了 Microsoft Copilot 的连接器生态系统。这些连接器把研究与证据、药物发现、研发、监管情报和临床开发等领域的信息带入 Copilot，用户可以在工作流程中查找、推理并据此行动。这使组织能够在更广泛的专业生命科学工作流程中使用 Copilot。可在 [Microsoft Marketplace](https://marketplace.microsoft.com/en-us/) 中找到连接器、插件和 agent。

- **‌Research & Evidence（研究与证据）：** Article Galaxy/Research Solutions, bioRxiv, Consensus, PubMed, Scite/Research Solutions, MedlinePlus

- **Target Discovery & Biology（靶点发现与生物学）：** Open Targets, Synapse.org/Sage Bionetworks, PopHIVE

- **Drug Discovery（药物发现）：** Amass, ChEMBL, CAS, DrugBank, drug data, EDEN Basecamp Research, Inductive Bio

- **Lab & Enterprise R&D Data（实验室与企业研发数据）：** SciLeads

- **Regulatory & Competitive Intelligence（监管与竞争情报）：** Cortellis Regulatory Intelligence, NyquistAI, FDA Safety, Clarivate IPOne CompuMark Trademarks

- **Clinical Development & Healthcare Data（临床开发与医疗数据）：** ClinicalTrials.gov, NPI Registry, RxNorm, CMS Coverage, ICD-10

- **Scientific Content Creation（科学内容创作）：** BioRender

#### 政府云中的 Copilot 编辑能力

**PowerPoint、Word 和 Excel 中的 Copilot 编辑能力正在向 Government Community Cloud（GCC）推出。**用户可以让 Copilot 直接在其文件中创建和编辑内容，包括 Excel 中的仪表板、PowerPoint 中的概览幻灯片、Word 中的表格等，并以其组织的工作上下文为依据。此功能[10 月已推出](https://www.microsoft.com/microsoft-365/roadmap?id=561322)。

## IT 管理员功能

#### Insights Agent 与 Workforce Insights Agent

**Insights Agent** 让用户用自然语言就 Copilot 中的 agent 使用情况提问，包括日活、周活和月活用户、采用趋势以及 agent 之间的比较。Insights Agent V2（Frontier）是一个抢先体验预览版，在管理员启用反馈共享后，还允许 agent 所有者查看针对其所拥有 agent 提交的点赞与点踩评分及评论。这些洞察为开发者和管理员提供评估采用情况、识别需要调查的领域的依据。此功能 10 月已推出。

**Workforce Insights Agent** 使 Copilot 能基于客户自己的组织数据给出可信、与上下文相关的回答。该 agent 现在为管理员提供专用工作区，用于配置组织定义、数据描述和业务上下文，并能够验证 AI 在人员和组织类查询中如何基于这些上下文进行推理。此功能[11 月向 Frontier 推出](https://www.microsoft.com/microsoft-365/roadmap?id=515145)。

#### Microsoft Purview 数据丢失防护的保留配置与 Microsoft Cowork 扩展

管理员现在可以在 Microsoft Purview Data Lifecycle Management 中**为 Microsoft Copilot 记忆配置保留**。Purview 保留策略现在可以保留已保存的记忆，使安全与合规团队能够看到变更，用于调查、监管要求和数据生命周期治理。此功能[10 月已推出](https://www.microsoft.com/microsoft-365/roadmap?id=569612)。

**Microsoft Purview 数据丢失防护（Data Loss Prevention，DLP）正在扩展到 Microsoft Cowork**，使数据安全管理员能在 Microsoft Copilot chat 和 Cowork 中使用同一条策略。这一集成为管理员提供控制手段，可阻止用户引用带敏感度标签的内容、拦截包含受支持类型敏感数据的提示，并阻止敏感提示被发送到 Bing 进行网页搜索。此功能[10 月已进入 public preview](https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=570845)。

*你知道吗？* [*AI at Work Roadmap*](https://www.microsoft.com/microsoft-365/roadmap) *是你获取生产力应用和智能云服务最新更新的地方。* [*Microsoft 365 Copilot release notes*](https://learn.microsoft.com/copilot/microsoft-365/release-notes?tabs=all) *是你查看已正式发布（generally available）且特定于各平台的 Microsoft 365 Copilot 功能的地方。请定期回来查看哪些功能正在开发、即将推出和已正式发布。请注意，本文中提到的日期是暂定的，可能会变更。*
