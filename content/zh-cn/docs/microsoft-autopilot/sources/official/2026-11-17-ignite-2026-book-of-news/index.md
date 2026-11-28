---
title: "Microsoft Ignite 2026 新闻手册（Book of News）"
linkTitle: "Ignite 2026 新闻手册"
date: 2026-11-17
originalTitle: "Microsoft Ignite 2026 | Book of News"
sourceUrl: "https://news.microsoft.com/events/ignite/2026/book-of-news/"
altUrls: []
author: "未署名"
publisher: "Microsoft"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [发布, 安全, 商业与规模]
products: [microsoft-autopilot]
updatedAt: "2026-11-19"
dateNote: "页面不标发布日期；按 Ignite 首日 2026-11-17 记，article:modified_time 为 2026-11-19"
---

{{< source-info >}}

**收录说明**：Ignite 2026 官方新闻汇编（Book of News），直接下载，从「Introduction」起存档全文；删去了页首的会议信息、主题演讲视频与「Try Instant Summaries」开关。各条目下的「Instant Summary」是页面自带的 AI 摘要，照原文保留。全文约 2 万词，涉及 Azure、Foundry、GitHub、Copilot、Edge、Microsoft IQ、安全、Windows，Autopilot 只占少数条目。已翻译。

**内容摘要**：Ignite 2026 Book of News 全文中与 Autopilot 相关的条目有四处。Copilot 部分把 Autopilot 列为新 Copilot 的一部分，称其为 persistent、proactive 的个人生产力智能体。专条「Autopilot is rolling out to Frontier customers」称它是微软首个企业级长时运行的个人生产力智能体，有自己的身份、记忆和工具，可跟进线程、运行周期性工作、无需再次提示地推进项目，同事可在 Teams 频道或群聊中 @mention，操作绑定自己的 agent ID 并经安全检查，管理员可见可管；用户可在 Copilot app 左侧导航找到它。Agent 365 Cost Management 的计费对象列表包含 Autopilot；Entra Agent ID 的 preview 将扩展到 Microsoft Autopilot 智能体，以区分本地智能体与 Autopilot 的活动。

**保留理由**：微软官方一次性给出的 Autopilot 官方定位（首个企业级长时运行个人智能体），以及 Autopilot 被纳入 Agent 365 成本管理和 Entra Agent ID preview 的出处，这两点在已收资料中没有。

---

## 引言

### 什么是《新闻手册》？

即时摘要：

Microsoft Ignite 2026《新闻手册》（Book of News）是了解本次大会重要发布的指南。你可以通过交互式目录浏览各主题，并点击右下角的「翻译」按钮以其他语言阅读。如对内容有疑问或反馈，请发送邮件至 [[email protected]](https://www.microsoft.com/cdn-cgi/l/email-protection#bfdac9dad1cbdcd0d2ffd2d6dccdd0ccd0d9cb91dcd0d2)（译注：原文为 "[[email protected]]"，邮箱地址被页面的反爬机制替换，未显示实际地址）。如果你有兴趣就这些发布或微软更广泛的战略与产品与行业分析师交流，请联系 [[email protected]](https://www.microsoft.com/cdn-cgi/l/email-protection#384f5d554b59565954414b4c4a5d54594c5157564b784f5d154f574a545c4f515c5d165b5755)（译注：原文同为被替换后的 "[[email protected]]"）。

Microsoft Ignite 2026《新闻手册》把大会的重要发布汇集到一份交互式指南中。读者可以通过目录浏览主题、把内容翻译成其他语言，并联系大会团队或分析师关系团队获取更多信息。

## Azure

即时摘要：

AI 已进入生产环境，而智能体需要完整的堆栈。Azure 把芯片、基础设施、数据和运营整合为一个系统。**Azure Cobalt 200** 虚拟机、**Azure HorizonDB**、**Rayfin** 和 **Fabric apps** 现已正式可用。新的预览版把 **Microsoft Foundry** 的模型和智能体带到 **Azure Kubernetes Service**，并新增 **Azure SRE Agent** 和扩展的**机密计算（confidential computing）**来运行和保护它们。

这些更新以及下文列出的更新，标志着 Azure 的下一章：从芯片到智能体构建，并具备组织大规模运行 AI 所需的安全与控制。

Azure 正在统一芯片、基础设施、数据和运营，帮助组织大规模运行生产级 AI 和智能体。Azure Cobalt 200 虚拟机、Azure HorizonDB、Rayfin 和 Fabric apps 现已正式可用；新的预览版把 Microsoft Foundry 扩展到 Azure Kubernetes Service（AKS），并新增 Azure SRE Agent 能力以及机密计算保护。

### 品牌、基础设施与芯片

#### Azure Chaos Studio Workspaces 与 AKS 扩展现已正式可用

即时摘要：

Azure Chaos Studio Workspaces 和 Azure Chaos Studio 的 Azure Kubernetes Service（AKS）扩展现已正式可用，扩展了组织测试应用如何响应和从中断中恢复的方式。这些更新扩展了 Azure Chaos Studio——一项托管服务，允许组织向应用注入受控故障，以测试其响应和恢复能力。

Azure Chaos Studio Workspaces 提供了一种更简单的方式来组织和运行韧性测试。组织可以定义要测试的资源，并应用可复用的场景来代表各类中断，例如可用性区域丢失或数据库故障转移。这样更容易测试应用如何应对贴近现实的中断，并可反复执行这些测试。

面向 AKS 的 Azure Chaos Studio 扩展把韧性测试带到运行于 AKS 的应用。该扩展运行实验所需的权限更少，为组织向 Kubernetes Pod 注入受控中断并观察应用的响应和恢复提供了更安全的方式。

这些更新帮助组织验证应用能否如预期般从中断中恢复。通过在受控环境中注入故障，组织可以在类似故障意外发生之前发现薄弱环节并加以改进。

[**了解这项发布的更多信息**](https://aka.ms/chaosstudio/workspaces-ga)**。**

Azure Chaos Studio Workspaces 和 Azure Kubernetes Service 的 Azure Chaos Studio 扩展现已正式可用，为组织提供更安全、更简单的方式来测试应用韧性。团队可以组织可复用的中断场景，模拟可用性区域丢失或数据库故障转移等事件，并以更少的权限向 Kubernetes Pod 注入受控中断——在真实事故出现之前发现薄弱环节。

#### Azure 扩展机密计算，保护高度敏感的数据

即时摘要：

Microsoft Azure 正在扩展其机密计算产品，帮助组织从数据中释放更多价值、扩大 AI 创新规模，并以更强的信心和控制力开展协作——不仅保护数据存储的位置和移动方式，也保护数据被处理的方式。目前有三项产品进入预览：

- VR72 多 GPU 机密计算，将推进 Azure 的机密计算 AI 路线图，并开辟保护超出单个 GPU 的大型模型的路径。
- Azure Confidential Enclaves 和 AKS Kata CoCo 机密容器，将在更大的虚拟机内创建一个更小的可信执行环境。这有助于企业缩小必须被信任和验证的范围，而不是把这种信任寄托在整个周边系统上。
- Azure Confidential Clean Room，将使组织能够汇集数据开展多方分析，同时帮助保护每个参与方的敏感原始数据不被其他协作者和云运营商看到。这将开辟新的机会：在不放弃对受保护信息控制权的前提下生成共享洞察。

[**了解这项发布的更多信息。**](https://aka.ms/acc-ignite2026)

Azure 正在通过三项预览扩展机密计算，在敏感数据被处理时加以保护。VR72 多 GPU 机密计算开辟了保护跨多个 GPU 的模型的路径；Azure Confidential Enclaves 和 AKS Kata CoCo 机密容器缩小了可信环境；Azure Confidential Clean Room 使多方分析无需暴露参与方的原始数据。

#### 为智能体 AI 时代打造，Azure Cobalt 200 虚拟机现已正式可用

即时摘要：

Azure Cobalt 200 虚拟机（VM）基于微软自研的 Arm 架构处理器，现已正式可用。到今年年底，它们将部署到 24 个 Azure 区域，加入目前在澳大利亚东部、美国中部、美国东部、印度尼西亚中部、意大利北部、美国中南部、西班牙中部、瑞典中部、英国南部、美国西部 2 和美国西部 3 的现有数据中心部署。

Cobalt 200 是为 AI 智能体打造的，智能体的大量工作是在 AI 模型之外、由通用中央处理器（CPU）完成的。由于智能体会不断创建临时工作区，CPU 速度决定了任务完成的速度。Cobalt 200 虚拟机提供的 CPU 性能比 Cobalt 100 高出最多 50%，因此组织也能用同样数量的机器完成更多工作。

Cobalt 200 虚拟机的客户现在可以把每台虚拟机设为恒速模式，或设为追求峰值速度的加速模式。两种新虚拟机类型分别服务于大型内存数据库（Mpsv4）和搜索等存储密集型作业，后者内置最多 23 TB 存储（Lpsv5）。

[**了解这项发布的更多信息**](https://aka.ms/Cobalt200VMs-GA)**。**

Azure Cobalt 200 虚拟机由微软的 Arm 架构处理器驱动，现已正式可用，并计划在年底前覆盖 24 个 Azure 区域。它们为 AI 智能体周边的 CPU 密集型工作而打造，CPU 性能比 Cobalt 100 高出最多 50%，新增恒速和加速模式，并推出面向大型内存数据库和存储密集型工作负载的虚拟机选项，内置存储最多 23 TB。

### 核心

### Azure 以新的监控和 AI 能力扩展智能体化运营

即时摘要：

智能体化运营把 AI 智能体直接引入 Azure，帮助团队更快调查问题、持续优化资源，并以更强的信心采取行动。**Azure Monitor、Azure Copilot 和 Azure SRE Agent 中扩展的智能体能力**将提供更丰富的运营上下文、更强的治理，以及运营智能体的共同基础，同时让人始终掌握控制权。

**新的自然语言能力**现已在 Azure Monitor 中正式可用，帮助用户规划和部署云工作负载。Azure Copilot spaces 和自定义技能（custom skills）处于预览，将让团队定制智能体，以更快、更高效、更准确地开展运营，同时携带持久上下文。用户还可以通过 Azure Workload Center（预览）把智能体化运营扩展到 Oracle 和 SAP，用于工作负载健康监控和配置校验。

Azure SRE Agent 的新能力处于预览，将实现**企业规模的智能体化安全运营**。客户管理的密钥将让团队完全控制智能体数据，而 Entra Agent ID 与 Agent 365 集成将为用户提供一致的方式，在智能体整个生命周期内发现、治理、审计和管理它们。跨智能体通信将使上下文和任务能够在智能体之间共享，加快事件解决。Azure SRE Agent 还将与 Microsoft Teams 集成，并把调查扩展到多云环境。这些更新将帮助组织从智能体试验走向在复杂生产环境中的部署。

Azure Monitor 健康模型（health models）现已正式可用，**把遥测转化为可据以行动的运行状况上下文**。用户可以把遥测转化为实时健康图，连接应用架构、依赖关系和业务优先级。这帮助团队了解受影响的是什么、区分平台问题与应用故障，并按业务影响确定事件优先级。同样的上下文使 AI 智能体能够调查问题、识别根因、建议修复措施并自动化工作流。

[**了解这项发布的更多信息**](https://aka.ms/ignite2026/agenticops)。

Azure 正在 Azure Monitor、Azure Copilot 和 Azure SRE Agent 中拓宽智能体化运营，使团队能够更快调查事件、优化资源，并在企业规模上治理运营智能体。新增和预览能力带来自然语言运营、持久自定义上下文、SAP 和 Oracle 监控、客户管理密钥、跨智能体通信、Teams 与多云集成，以及已正式可用的健康模型——把遥测转化为感知业务、可据以行动的上下文。

### 面向生产级 AI 应用和智能体的 Azure 基础设施基础

即时摘要：

为满足生产级 AI 应用的独特需求——从智能体网络和安全，到隔离、机密性、上下文与状态——新能力将在计算、存储和网络之上铺开一个 AI 基础。

**从 Microsoft Foundry 到 Azure 的连续体验：** Microsoft Foundry 让客户可以在完全托管的环境中部署，并轻松扩展到 Kubernetes，以获得对基础设施性能、安全和经济性的更强控制。客户现在可以使用已有的基础设施、安全策略和治理，把 Foundry 中的开放权重模型和智能体部署到自己的 Azure Kubernetes Service（AKS）集群。团队将能够根据成本、延迟和数据驻留要求选择 GPU 和区域。Foundry 将负责环境搭建，让从试验到生产的开发工作流保持一致。这将把 Foundry 的简洁与 Kubernetes 的灵活和控制结合起来。

**Azure AI 基础设施**：对于生产级 AI，基础设施直接决定智能体的性能、安全性和运营成本。Azure 的最新能力将针对推理和智能体优化底层基础设施，把基础设施决策与业务成果联系起来：

- **Agent Grid** 将通过集中策略执行，保护智能体、模型、工具和 Azure 服务之间的交互。
- **面向 AKS 的 Agent Sandbox 扩展**将在虚拟机级别隔离的沙箱中运行智能体编写的代码。
- **AKS 的 Flex 节点（Flex nodes）** 将把同一批 AKS 集群扩展到 Azure 之外的客户服务器。
- **Azure Cobalt 200** 虚拟机为 AI 模型周边的服务增加 CPU 性能。

**开放与选择**：Azure 的 AI 基础以保持开放为设计目标。包括 vLLM、Ray 和 Kubernetes 在内的开源项目让工作负载保持可移植，而微软是过去三年对 Cloud Native Computing Foundation 项目贡献最大的公有云厂商。

除 Azure Cobalt 200 已正式可用外，所有能力均处于预览。

[**了解这项发布的更多信息**](https://aka.ms/ai-infra-ignite26)。

Azure 正在把 Microsoft Foundry 扩展到 Azure Kubernetes Service，使组织能够利用现有的基础设施、安全和治理，把开放权重模型和智能体从试验推进到生产。预览能力——包括 Agent Grid、面向 AKS 的 Agent Sandbox 扩展和 AKS 的 Flex 节点——加强了网络和隔离，而正式可用的 Azure Cobalt 200 虚拟机提升了 AI 模型周边的 CPU 服务。对 vLLM、Ray 和 Kubernetes 的支持让这一基础保持开放和可移植。

### 推出 Azure Catalyst

即时摘要：

**Azure Catalyst** 是一项全新的统一体验，用于跨 Azure 和 GitHub 的智能体化现代化，帮助组织对基础设施、应用和数据实施现代化，并加速 AI 转型。它已正式可用。

Azure Catalyst 把 AI 驱动的发现、规划、迁移和现代化结合起来，帮助 IT 团队和开发者在现代化生命周期中协同工作。通过把全资产范围的洞察与 Azure Copilot 和 GitHub Copilot 中由智能体辅助的执行连接起来，组织可以减少人工投入、现代化复杂系统，并释放现有应用中的业务逻辑，以构建新的 AI 驱动体验和智能体化业务流程。

Azure Catalyst 汇集了新增和扩展的能力，包括：

- **Azure Catalyst 智能体**（原 Azure Copilot migration agent）现已正式可用，其新能力处于预览，把该智能体从迁移规划扩展到更深入的现代化和执行。增强内容包括更丰富的资产洞察、AI 驱动的应用发现、现代化策略与成本对比，以及跨应用、数据库、存储和网络的扩展规划与执行。
- **GitHub Copilot 现代化更新**，包括智能体治理规则手册（agent governance rulebooks）、命令行界面和集成开发环境中的自带模型（bring-your-own-model）支持，现已正式可用。新能力处于预览，扩展了应用与数据库一体化现代化、从 BizTalk 迁移到 Azure Logic Apps 等现代化场景。

[**了解这项发布的更多信息**](https://aka.ms/modernization-ignite26)。

Azure Catalyst 现已正式可用，统一了跨 Azure 和 GitHub 的 AI 驱动发现、规划、迁移和现代化。该体验把全资产范围的洞察与 Azure Copilot 和 GitHub Copilot 的执行连接起来；增强的 Azure Catalyst 智能体、治理规则手册、自带模型支持以及新的预览场景，帮助团队以更少的人工投入对应用、数据库、存储、网络和 BizTalk 环境实施现代化。

### 推出 Windows Server 2028

即时摘要：

对于依赖 Windows 应用和基础设施的企业，Windows Server 提供可信的基础，既延续现有的技能、工具和投资，又支持从数据中心到边缘的关键工作负载。**Windows Server 2028** 现已进入预览。它将强化组织已经依赖的基础设施，同时把 Windows Server 扩展到企业 AI 推理和混合智能。功能包括：

**更强的安全**：Windows Server 2028 将默认强化安全，包括加固的 Server Core 配置、新的安全基线、虚拟机的 Trusted Launch（受信任启动）、后量子加密和自动化证书管理。这些能力将帮助保护身份、工作负载和加密通信，同时帮助组织为新兴威胁和不断演变的监管要求做好准备。

**加速的企业基础设施：** 组织将能够通过 NVMe over Fabrics、原生 NVMe 存储以及从弹性文件系统（ReFS）启动的能力，提升存储和数据密集型工作负载的性能与效率——从而从现代基础设施和加速硬件中获得更多收益。

**简化的规模化管理：** 组织将能够使用 Microsoft Intune、Azure Arc、Windows Admin Center 和 vMode，在数据中心、云和远程位置更一致地管理 Windows Server。

**企业混合智能：** Windows Server 2028 将扩展组织已经信任的基础设施，在贴近业务关键应用和数据的位置支持企业 AI 推理。相关投入包括：

- **软件**：受支持的运行时和推理平台，包括 Windows ML、Foundry Local、vLLM 和 Llama.cpp。
- **安全**：Microsoft Execution Containers，以及横跨硬件、操作系统、虚拟机监控程序和运行时的多层保护。
- **治理与控制**：与 Agent 365 集成，帮助组织治理其环境中的 AI。
- **硬件**：支持加速 AI 芯片，包括 AMD MI350P 加速器和 NVIDIA GB300 Grace Blackwell Ultra Desktop Superchip。

这些能力共同帮助组织在其控制的基础设施上运行 AI，同时作为混合 AI 架构的一部分连接到 Azure。安全、性能和管理功能通过 Windows Server Insider Program 提供预览。混合智能功能通过早期访问计划向有限数量的客户提供。有硬件要求。

[**了解这项发布的更多信息**](https://aka.ms/WindowsServer2028Announcement)。

Windows Server 2028 现已进入预览，以默认加固的安全、后量子加密、更快的 NVMe 存储，以及跨数据中心、云和边缘更一致的管理，强化了这一熟悉的企业平台。它还通过受支持的运行时、Execution Containers、Agent 365 治理以及来自 AMD 和 NVIDIA 的加速芯片，把 Windows Server 扩展到混合 AI 推理，使组织能够在贴近关键应用和数据的位置运行 AI，同时连接到 Azure。
### 数据

#### Azure Cosmos DB 改进开发、检索和数据保护

即时摘要：

Azure Cosmos DB 推出七项更新，改进搜索和检索质量，帮助开发者设计并演进应用，并加强对生产数据的保护。包括：

##### **开发者工具与应用设计**

- **Azure Cosmos DB Shell：** 现已在 Visual Studio Code 和 Azure 门户中正式可用，该 shell 让开发者以交互方式浏览资源、查询和管理数据，并通过 MCP 集成启用 AI 辅助工作流。
- **AI 辅助数据建模器及 VS Code 中 Azure Cosmos DB 扩展的其他更新：** 这些更新现处预览，将把账户洞察、AI 驱动的建议，以及针对分区键和容器配置的引导式数据建模直接带入 VS Code。
- **Azure Cosmos DB 的 Rust SDK：** 现已正式可用，该 SDK 提供原生 Rust 客户端，内置性能和韧性能力，帮助团队构建可靠的分布式生产应用。

##### **搜索与检索质量**

- **语义重排器（semantic reranker）：** 现已正式可用，该能力使用 AI 模型评估候选搜索结果，并根据查询和内容的含义与上下文重新排序。
- **全文搜索中的 FuzzyBM25 分数投影更新：** 现已正式可用，这些更新通过向应用提供相关性分数，扩展了全文搜索。

##### **数据移动与生产保护**

- **Azure Cosmos DB 的 Azure Backup：** 现已正式可用，Azure Backup 增加了独立的、基于保管库的保护层，用于集中备份策略、监控、保留和恢复。

这些更新共同支持 Azure Cosmos DB 的应用生命周期：提升检索相关性，帮助团队设计并演进应用，并保护生产数据。

[**了解这项发布的更多信息**](https://aka.ms/ignite26/cosmosdb)。

Azure Cosmos DB 新增七项更新，覆盖开发、检索和数据保护。正式发布的版本包括 Azure Cosmos DB Shell、原生 Rust SDK、语义重排、全文相关性分数和基于保管库的 Azure Backup；VS Code 扩展中的预览增强则把账户洞察、AI 驱动的建议和引导式数据建模带入 VS Code。

#### Azure DocumentDB 扩展开发者工具、数据主权和安全

即时摘要：

Azure DocumentDB 推出五项功能更新，帮助开发者构建应用、实施更细粒度的访问控制，并在混合环境中运行兼容 MongoDB 的工作负载。

##### **更快的开发与预配**

- **Visual Studio Code 的 Azure DocumentDB 扩展：** 现已正式可用，该扩展让开发者连接集群、浏览数据库和集合、检查文档并运行查询——全部在 Visual Studio Code 内完成。
- **近乎即时的 Azure DocumentDB 集群预配：** 现已面向 M10 到 M30 集群正式可用，该能力缩短了新环境的等待时间。开发者和 AI 智能体可以更快开始测试、试验和生产上线。

##### **混合部署与数据主权**

- **由 Azure Arc 支持的 DocumentDB：** 现已进入预览，该产品将把 Azure DocumentDB 扩展到混合和多云环境。组织将能更灵活地在应用和数据需要驻留的位置运行兼容 MongoDB 的工作负载，包括有数据主权、数据驻留和基础设施控制要求的场景。
- **Azure Local 上的 DocumentDB：** 现已进入预览，该产品将在 Azure Local 基础设施上运行兼容 MongoDB 的文档工作负载。组织将能够把应用和数据保留在自己的环境中，以满足主权、驻留和监管要求。

##### **更细粒度的访问控制**

- **面向数据库和集合的细粒度基于角色的访问控制：** 现已进入预览，Azure DocumentDB 将让组织把自定义角色和权限限定到单个数据库和集合。这将支持最小权限访问，而不必授予用户和应用超出需要的集群级权限。

[**了解这项发布的更多信息**](https://aka.ms/ignite26/documentdb)。

Azure DocumentDB 正在为混合环境中兼容 MongoDB 的工作负载扩展工具、部署选择和访问控制。其 Visual Studio Code 扩展和面向 M10 到 M30 集群的近即时预配已正式可用；同时，Azure Arc 和 Azure Local 的预览把工作负载扩展到混合和受控环境，细粒度基于角色的访问控制则为单个数据库和集合带来最小权限。

#### Azure HorizonDB 正式可用，服务关键业务应用

即时摘要：

**Azure HorizonDB** 现已正式可用，是一项完全托管、兼容 PostgreSQL 的数据库服务，把企业级安全、韧性和规模与内置的向量搜索和 AI 能力结合起来。它帮助开发者利用已经依赖的事务数据构建智能的关键业务应用。

**安全与业务连续性**

运行关键应用的企业需要保护敏感数据并保持业务连续性。Azure HorizonDB 支持用 Microsoft Entra ID 进行身份验证和访问，用专用终结点实现网络隔离，用用户分配的托管标识作为服务身份。服务管理密钥和客户管理密钥对静态数据加密，加密的客户端连接保护传输中的数据。多区域复制和分布式存储支持快速恢复，帮助组织保持应用韧性。

##### **AI 开发与平台连接**

把模型、数据和熟悉的工具结合起来，可以减少开发者构建 AI 驱动应用的集成工作。**内置 AI 模型管理**处于预览，将把生成模型和排序模型与数据一起管理；**AI Functions** 和 **AI Pipelines** 处于预览，将使开发者能够直接在 SQL 查询中调用模型，而不影响应用性能。

Microsoft 平台连接同时支持开发和分析。**Visual Studio Code（VS Code）的 PostgreSQL 扩展**现已正式可用，把 AI 支持的数据库管理、查询计划和监控带入开发者的工具。把 Azure HorizonDB 镜像到 Microsoft Fabric（预览）将使运营数据可与其他业务数据一起用于分析。

[**了解这项发布的更多信息**](https://aka.ms/ignite26/horizondb)**。**

Azure HorizonDB 现已正式可用，作为完全托管、兼容 PostgreSQL 的服务，面向智能的关键业务应用。企业级安全、多区域复制和分布式存储保护事务数据；AI 模型管理、可从 SQL 调用的 AI Functions 和 Pipelines，以及在 Microsoft Fabric 中镜像 Azure HorizonDB 的能力（均处预览），把运营数据与模型和分析连接起来。已正式可用的 Visual Studio Code PostgreSQL 扩展增加了 AI 支持的管理和监控。

### Azure Managed Redis 预览 Redis 8 和智能体工具包

即时摘要：

Azure Managed Redis 推出两项预览更新，帮助开发者构建响应迅速的现代应用和 AI 应用：

- **Azure Managed Redis 中的 Redis 8：** 对现有服务的这一更新将把对 JSON、搜索、时序数据、向量搜索和其他数据类型的支持整合到一个 Redis 版本中，简化能力管理。应用将能够查找相关信息、提供推荐、复用对相似 AI 请求的相关响应，并让 AI 智能体访问上下文和记忆。该更新将扩展应用存储、搜索和处理数据的方式，同时保留 Azure Managed Redis 作为 Azure 托管服务的属性。
- **Azure Managed Redis 智能体工具包（agent kit）：** 该预览将把 Redis 和 Azure 的指导带入 AI 辅助开发，通过检查应用如何连接和使用 Azure Managed Redis。该智能体工具包将识别可能影响可靠性、网络连接和性能的配置设置，然后提出变更建议供开发者评估。这将帮助团队识别常见的配置问题，并采用更一致的开发实践。

[**了解这项发布的更多信息**](https://aka.ms/ignite26/AMR)。

Azure Managed Redis 正在预览 Redis 8 和一个新的智能体工具包，以支持响应迅速的现代应用和 AI 应用。Redis 8 统一了 JSON、搜索、时序、向量搜索和其他数据类型，使应用和智能体能够检索上下文、提供推荐，并复用对相似 AI 请求的相关响应；智能体工具包则检查配置，并就可靠性、连接性和性能提出改进建议。

#### Azure SQL 扩展现代化、韧性和本地开发选项

即时摘要：

Azure SQL 的更新将帮助组织对 SQL Server 工作负载实施现代化，并构建云和 AI 应用。这些更新增强了韧性和资源灵活性，简化了迁移和灾难恢复，并把 Azure SQL Database 开发带到本地环境。

##### **韧性与灵活资源**

Azure SQL Managed Instance 新一代通用用途层（Next-gen General Purpose tier）现提供两项正式可用的更新：

- **区域冗余：** 在受支持的区域，服务组件分布在 Azure 可用性区域之间，帮助应用抵御数据中心中断，而无需更改应用逻辑。
- **区域冗余实例的灵活内存：** 使用 Premium 系列硬件的客户可以独立于处理能力调整内存，以满足工作负载需要，而无需增加处理器核心。

Azure SQL Managed Instance 是一项基于 SQL Server 的完全托管云数据库服务。它负责日常备份、修补和数据库引擎更新。新能力帮助组织提升韧性，并按工作负载定制资源。

##### **迁移与灾难恢复**

Azure SQL Managed Instance link 现已正式可用，支持包含多个数据库的 **SQL Server Always On 可用性组**。它以接近实时的方式把数据库更改从 SQL Server 复制到 Azure SQL Managed Instance，实现停机时间极短的迁移和 Azure 中的灾难恢复。

客户可以扩展现有受支持的可用性组，或从独立数据库创建新组。一条链接可以复制组内的所有数据库，减少了为每个数据库单独配置链接的需要。

##### **使用 Azure SQL Database 进行本地开发**

Azure SQL Database 容器现处预览，将让开发者**在本地运行 Azure SQL Database 引擎**，无需 Azure 订阅、共享云实例或信用卡。开发者将能够使用与 Azure SQL Database 相同的数据库引擎、T-SQL 方言、系统视图、连接协议和驱动程序行为来构建和测试。

该容器将支持账本（ledger）、向量搜索和嵌入工作流。开发者将能够使用熟悉的驱动程序、框架和 Visual Studio Code 工具，并在把应用迁移到 Azure SQL Database 之前，在持续集成环境中运行集成测试。本地开发免费；云数据库和模型的使用仍按各自收费标准计费。

[**了解这项发布的更多信息**](https://aka.ms/ignite26/mssql)。

Azure SQL 正在增强韧性、简化迁移，并把 Azure SQL Database 开发带到本地环境。正式可用的更新增加了区域冗余、灵活内存，以及通过 Azure SQL Managed Instance link 实现的多数据库复制，帮助客户调整资源、以极短停机时间迁移并加强灾难恢复。预览中的 Azure SQL Database 容器允许在本地使用引擎，并支持安全飞地（secure enclaves）、账本和向量搜索等能力。

#### Fabric 中的 Database Hub 正式可用；SQL 和 PostgreSQL 数据库智能体进入预览

即时摘要：

**Fabric 中的 Database Hub（Database Hub in Fabric）** 现已正式可用，为组织提供一个统一位置，用于发现、监控和管理跨 Azure、Microsoft Fabric、本地环境和其他云的数据库。更广阔的视图帮助管理员识别新出现的瓶颈、确定运营工作的优先级，并更一致地应用治理实践，使数据库团队能够减少在管理复杂性上的时间，把更多时间用于改进关键业务系统。

##### **借助数据库智能体实现 AI 辅助运营**

在 Fabric 中的 Database Hub 内，**数据库智能体（database agents）** 处于预览，将把 AI 辅助的 SQL 和 PostgreSQL 运营带入熟悉的工具。它们将帮助团队从被动监控转向自动化、智能化的数据库运营。这些智能体使用 Microsoft 编写的技能来应对常见的性能和健康场景，持续观察组织数据库资产中的运营信号，检测特定引擎的问题并解释其重要性。它们会推荐修复措施，或在 AI 辅助下执行已批准的操作。

数据库智能体将辅助而非取代人的判断。它们将在现有的身份权限、审批边界和可审计操作的范围内工作。它们将在受支持的 Microsoft 数据库服务中通过两个熟悉的位置提供：

- **Fabric 中 Database Hub 内的数据库智能体：** 数据库专业人员和开发者将能够使用 AI 辅助指导，调查其数据库资产中的 SQL 和 PostgreSQL 性能、健康和运营问题。
- **Visual Studio Code 的 Microsoft PostgreSQL 扩展中的数据库智能体：** 开发者和数据库专业人员将能够在不离开开发环境的情况下调查 PostgreSQL 的性能和运营问题。

[**了解这项发布的更多信息**](https://aka.ms/ignite26/databases)**。**

Fabric 中的 Database Hub 现已正式可用，作为发现、监控和管理跨 Azure、Fabric、本地环境和其他云数据库的统一位置。预览中的 SQL 和 PostgreSQL 数据库智能体将持续分析运营信号，解释性能和健康问题，并在现有权限和审计控制范围内推荐或执行已批准的修复——既可在 Database Hub 中，也可在 Visual Studio Code 的 Microsoft PostgreSQL 扩展中。

#### Microsoft Fabric HorizonDB 以预览形式把 PostgreSQL 带入 Fabric

即时摘要：

**Microsoft Fabric HorizonDB** 是一项新的预览数据库产品，将把 PostgreSQL——开发者最喜爱的数据库之一——直接带入 Microsoft Fabric。它将在同一个位置连接应用、数据分析和 AI。

**面向变化工作负载的无服务器数据库**

智能体构建应用的速度超过以往任何开发者。它们为原型、试验和短期任务创建数据库，工作完成后就将其删除。这些工作负载时而突发、时而空闲，需求难以预测。Fabric HorizonDB 正是为这些模式构建的无服务器 PostgreSQL。

- 数据库将在数秒内完成预配，并随需求自动伸缩。
- 空闲数据库将暂停，在下一次查询到来时恢复。

##### **Fabric apps 的托管后端**

Fabric HorizonDB 还将为 Fabric apps 启用。它将提供带有数据 API、身份验证、存储和托管的托管后端，使开发者能够从想法直接走到内置 PostgreSQL 的可运行应用。

跨运营数据和分析数据查询
Fabric HorizonDB 将把实时运营数据和 OneLake 中的分析数据结合起来，使应用能够同时基于两者采取行动。

**事务分析一体查询（Translytical queries）**

单条 PostgreSQL 查询将把 Fabric HorizonDB 中的实时数据与 OneLake 中的分析数据结合起来，运行在 Fabric Data Warehouse 的横向扩展计算上。

**镜像**

Fabric HorizonDB 的表将复制到 Fabric 用于分析，无需单独的管道。

##### **反向 ETL**

来自 Fabric Data Warehouse 的丰富数据将回流到 Fabric HorizonDB，应用和智能体可以快速读取。

**[了解这项发布的更多信息。](https://aka.ms/AAncdv4)**

Microsoft Fabric HorizonDB 正在预览 Fabric 内部的无服务器 PostgreSQL，在同一个环境中连接应用、分析和 AI。数据库在数秒内完成预配，随需求伸缩，空闲时暂停；托管后端以内置 API、身份验证、存储和托管支持 Fabric apps。事务分析一体查询、镜像和反向 ETL 随后把实时运营数据与 OneLake 和 Fabric Data Warehouse 的洞察连接起来，无需单独的管道。

### Azure 上的 PostgreSQL 简化迁移并扩展现代化选项

即时摘要：

Microsoft 正在整个 PostgreSQL 生命周期上投入，以简化采用和现代化。这些更新帮助企业在迁移到 Azure、保持版本最新，并以内置的性能、安全和韧性运行高要求的应用。

- **更简单的迁移和现代化。** Azure Database Migration Service（DMS）对 Oracle 到 PostgreSQL 数据迁移的支持现已进入预览。结合 Microsoft PostgreSQL VS Code 扩展中的评估、架构转换和应用转换，它将提供从准备、代码转换到数据移动的第一方路径。此外，客户将能够使用 Azure DMS（预览）通过无缝的托管体验，把现有的 Azure Database for PostgreSQL 工作负载迁移到 Azure HorizonDB。DMS 将负责连接校验、数据复制、在线迁移的持续同步、监控和计划内切换，简化在高性能、可扩展 PostgreSQL 平台上的现代化。
- **更多性能和规模选择。** 可突发 v2 计算（Burstable v2 compute）处于预览，将为开发工作和需求变化的工作负载增加灵活性。Cobalt 200 现已在 Azure Database for PostgreSQL 中正式可用，在 Intel 和 AMD 的 x64 选项之外增加了微软设计的 Arm64 计算。客户在 Azure 上实施现代化和扩展时，可以选择最适合其工作负载的架构。
- **对敏感工作负载的更强保护。** AMD v6 机密计算现已正式可用，帮助保护使用中的数据。时间点还原不可变性（point-in-time restore immutability）同样已正式可用，帮助保护备份免遭更改或删除。
- **扩展的备份和韧性。** Azure Backup for Azure Database for PostgreSQL 灵活服务器和弹性集群版本 2 处于预览，将通过基于快照的备份和直接还原支持更大的数据库。同区域到区域冗余高可用性的转换现已正式可用，帮助抵御可用性区域故障，而无需重建服务器。

这些增强为关键和受监管应用强化了 Azure 上的 PostgreSQL。组织可以随需求增长扩大 PostgreSQL 的使用，同时保持性能、保护和韧性。

[**了解这项发布的更多信息**](https://aka.ms/Ignite26/Postgres_on_Azure)。

Microsoft 正在通过预览服务简化 Azure 上的 PostgreSQL 迁移和现代化，包括 Oracle 到 PostgreSQL 的迁移，以及从 Azure Database for PostgreSQL 到 Azure HorizonDB 的托管过渡。客户还可获得预览的可突发计算和基于快照的备份选项，而正式可用的 Cobalt 200 计算、AMD v6 机密计算、不可变的时间点还原和就地转换为区域冗余高可用性，提升了关键工作负载的性能、保护和韧性。

#### Power BI 以预览形式推出自定义数据应用创建功能

即时摘要：

Power BI Pro 客户将获得一种新方式（现处预览），可以直接在 Power BI Desktop 中创建专用数据应用。

##### **从查看报表到采取行动**

数据应用把可信的业务数据、分析和操作结合在一个交互式体验中。用户不仅可以查看报表：他们可以录入信息、更新记录，并把更改写回底层数据源。团队无需切换工具即可把洞察转化为行动。

##### **用可信模型和自然语言构建**

客户将能够从可信的 Power BI 语义模型——定义业务数据和指标的有序、受治理的层——开始，用自然语言描述他们想要的应用，从而减少上手所需的技术投入。Power BI Pro 客户还将获得 Fabric Database 能力，使他们能够构建同时支持分析型和事务型场景的应用。这通过现有的许可选项把 AI 辅助的应用创建带给 Power BI 用户。

把预览访问扩展到 Power BI Pro 客户，将使更多组织能够在熟悉的 Power BI 环境中探索安全、量身定制的应用，用于规划、审批、跟踪和数据收集。

[**了解这项发布的更多信息**](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/microsoft-fabric-is-fueling-frontier-transformation/5422989)。

Power BI Pro 客户现在可以预览他们直接在 Power BI Desktop 中创建的专用数据应用。用户从受治理的语义模型开始，用自然语言描述应用，应用随后把可信的分析与数据结合起来。客户还可以更新记录并作出（译注：原文此处为「make.」，句子似乎被截断）。对 Fabric Database 能力的访问进一步支持规划、审批、跟踪和数据收集等分析型和事务型场景，而无需离开 Power BI。

#### Rayfin 和 Fabric apps 正式可用

即时摘要：

**Rayfin 和 Fabric apps** 现已正式可用，简化了开发者和 AI 智能体构建和部署完整业务应用的方式，并内置企业数据、安全和治理。自预览发布以来，构建者已用 Rayfin 创建了超过 10 万个应用。

##### **互联的应用后端**

AI 使在几分钟内构建应用成为可能，但生产部署仍然需要数据库、身份验证、后端服务以及对可信业务数据的访问。Rayfin 把这些能力汇集在 Microsoft Fabric 中。开发者可以选择 Microsoft SQL 数据库或 Fabric HorizonDB，连接现有的 Fabric 语义模型、仓库和湖仓，并复用可信的业务定义和访问控制，而无需构建单独的后端技术栈。

##### **规模化的治理与集成**

这些新能力现已正式可用，可以通过 OneLake 治理中心（OneLake Governance hub）中的集中应用治理、增强的安全控制和内置可观测性，帮助组织大规模管理应用。Fabric apps 还在向熟悉的工具扩展（译注：原文为「familiar e-tools」，其中「e-tools」应为笔误）：

- **Microsoft Copilot：** 人们可以用自然语言创建应用。通过 Fabric apps 与 Copilot Managed Runtime 的集成，业务用户将能够为需要大量应用能力的应用访问数据库和后端服务。
- **Power BI Pro 和 Power BI Desktop：** 集成使用户能够把可信的语义模型转化为交互式业务应用，把分析从洞察延伸到行动。

[**了解这项发布的更多信息**](https://aka.ms/FabricApps-Ignite26)。

Rayfin 和 Fabric apps 现已正式可用，为开发者和 AI 智能体提供一条受治理的路径来构建完整业务应用，数据库、身份验证、后端服务和可信企业数据都已连接就绪。自预览以来，已有超过 10 万个应用用 Rayfin 创建；新的集中治理、安全和可观测性功能，以及与 Microsoft Copilot 和 Power BI 的集成，现在帮助组织从自然语言创建和分析走向规模化的生产部署。
## Microsoft Foundry

即时摘要：

Foundry 的更新提供新能力，使 AI 智能体和模型能够持续改进，利用实时信号为 AI 系统的每一层提出并推动变更。

在智能体优化器（agent optimizer）的带领下，Foundry 利用客户对「好」的独特定义和相应的评估，改进智能体循环的每一步。

这与新的训练能力相结合，使模型能够自动进行后训练，并为高级用户提供可编程选项。为支持这一点，Foundry 带来新的 Microsoft AI（MAI）模型和合作伙伴产品。

Foundry IQ 属于 Microsoft IQ，现在开箱即提供企业知识图谱，覆盖客户全部非结构化数据和应用数据，为自定义应用和用例提供丰富体验。

Microsoft Foundry 正在引入持续改进循环，利用实时信号、评估和智能体优化器，在整个 AI 系统中推荐并推动变更。新的自动化和可编程训练选项帮助适配模型，并由 Microsoft AI 和合作伙伴产品提供支持。Foundry IQ 属于 Microsoft IQ，还会跨非结构化数据和应用数据创建企业知识图谱，为更丰富的自定义应用和体验提供依据。

### Foundry 中的持续改进

#### 把生产经验转化为更好的智能体

即时摘要：

Microsoft Foundry 中的**持续改进**建立在现有可观测性和评估能力之上，帮助客户创建学习循环。评估为质量、安全、延迟和成本建立基线，生产跟踪显示智能体的行为方式。新能力帮助团队识别机会、测试变更，并衡量每次迭代是否改善结果。

**多轮评估（Multi-turn evaluation）** 现已正式可用，按照质量标准评估完整对话。团队还可以从经过整理、验证的「黄金」数据集生成任务特定的评分标准评估器（rubric evaluators），新的安全支持与质量评估一起处于预览。

Foundry 通过**新的洞察能力**（现已正式可用）自动分析生产信号。它把反复出现的故障（如幻觉和 token 激增）分组，并对最频繁的问题和修复措施排序，供团队调查。

**人工标注功能**处于预览，将使客户能够为智能体跟踪记录添加专家评分、评论和预期答案，并整理黄金数据集，使评估反映业务的判断。这些信息会反馈到改进循环中。

**智能体优化器**针对团队的评估提出并测试候选变更，让开发者比较结果并选择要部署的内容。它已正式可用，并正在为客户评估结果带来显著提升。

**Microsoft Foundry 中的训练**有新能力处于预览，当智能体层面的变更不够时，将用组织数据适配受支持的模型。托管训练（Managed Training）将端到端运行整个过程，团队将用同一基线测试得到的模型。

**可编程训练（Programmed Training）** 处于预览，将让 AI 工程师在受支持的开放权重模型上编写自己的训练循环，包括监督微调和强化学习，而由 Foundry 运行计算。

每一次部署的改进都会成为下一个基线。团队可以继续衡量生产结果并测试变更，在提升质量或降低成本的同时检查是否出现回归。

[**了解这项更新的更多信息**](https://aka.ms/miq-ignitelaunchblog)**。**

Microsoft Foundry 正在把生产跟踪、评估和专家反馈转化为智能体可重复的学习循环。正式可用的多轮评估、生产洞察和智能体优化器揭示反复出现的故障、测试提议的变更并衡量改进；预览中的人工标注、托管训练和可编程训练让团队在智能体层面的变更不够时融入业务判断并适配受支持的模型。每次部署都会成为质量、安全、延迟和成本的下一个基线。

### 新模型

### Microsoft-Decision-1.1 现已正式可用

即时摘要：

**Microsoft-Decision-1.1** 现已正式可用，是一个快速、高性价比的模型，旨在在软件中大规模做出可靠决策。它使应用能够动态做出智能决策，而不依赖硬编码规则，同时解决把 AI 更广泛地嵌入软件的三项关键挑战：成本、延迟和控制。该模型已可用于企业生产部署，在 Microsoft Foundry 中提供，也可通过 OpenRouter 和 Vercel 获取。

与通用大语言模型不同，Microsoft-Decision-1.1 专为结构化决策而构建，例如路由、分类、优先级排序、校验和工作流控制。它在开发者定义的约束内从允许的动作中作出选择，并提供经过校准的置信度分数，使应用可以在不确定性高时暂缓处理。它以远低于更大模型的成本快速完成决策，而后者可以留给更复杂的推理任务。

在 10 月发布的 Microsoft-Decision-1 基础上，新模型以同样有竞争力的价格，在智能和速度上带来显著提升。它构建在新的基础模型 Gemma 4 26B A4B 之上，并新增多模态支持，可分析问题指令中的图像。

在 Artificial Analysis Decision Index v2.1 上，Microsoft-Decision-1.1 得分为 68，比第一个模型高 6 分，领先于 Jev 1.14、Google 的 Gemini-Decision-1 和 OpenAI 的 GPT-6 Luna (Decisions)。Microsoft-Decision-1.1 的速度也是第一个模型的两倍以上。

该模型正在被集成到 Microsoft 各产品中，以实现更快、更节省 token 的决策，包括：

- 在 Copilot 中，Microsoft-Decision-1.1 把用户请求路由到正确的体验，判断该由 Copilot 还是 Cowork 处理最合适。
- 在 Cowork 中，它为 Auto 提供支持，动态调整 Cowork 对每项任务投入的推理工作量。

[**了解这项发布的更多信息**](https://aka.ms/decision-model-ga)。

Microsoft-Decision-1.1 现已在 Microsoft Foundry、OpenRouter 和 Vercel 中正式可用，用于快速、经济的路由、分类、优先级排序、校验和工作流控制。该模型实时处理频繁、小型的智能体决策，以毫秒计，使前沿模型可以专注于更深层的推理；其正式发布版带来更强的性能、Gemma 4 26B A4B 基础模型和图像输入。微软已把它集成到 Copilot 的路由和 Cowork 的自适应 Auto 模式中。

### Microsoft Foundry 新增面向编码、图像和安全性的 AI 模型

即时摘要：

**Microsoft Foundry 中的新模型**让组织在为每项任务匹配正确模型时拥有更多选择，并具备用自身上下文持续改进模型的控制力。Foundry 现在包含来自 Microsoft AI（MAI）等方不断壮大的第一方模型家族，为企业级信任和规模效率而构建。新模型的优势包括：

- **代码：** MAI-Code-2 处理高要求的智能体编码工作，MAI-Code-2-Flash 支持大批量日常编码，让开发者可以选择适合任务的性能与成本平衡。两者均已在 GitHub 中正式可用，Code-2-Flash 在 Foundry 中处于私人预览。
- **创作：** MAI-Image-2.7 和 MAI-Image-2.7-Flash 处于预览，将提供更精准的编辑和更一致的图像生成，帮助品牌在整个营销活动中保持统一形象。
- **安全：** MAI-Cyber-2-Flash 专为网络安全构建，仅在 Codename MDASH 中以预览形式提供。凭借涵盖代码漏洞发现、校验和修复的新能力，它帮助安全团队更快、更经济地发现、确认和修复漏洞。
- **决策：** Microsoft-Decision-1.1 现已正式可用。它构建在 Gemma 之上，支持快速、高性价比的路由、分类、优先级排序和校验，现在还包括图像输入。它与 Laya 和 Decisions API 一起，为开发者提供更多方式选择适合每个工作负载的决策模型，并以更低的集成复杂度把决策能力带入智能体和工作流。
- **路由：** Foundry Models 中的模型路由器（model router）让模型选择更容易。借助扩展的模型池（包含 Foundry 中排名前 50 的模型）、AI Gateway 中对模型路由器的支持，以及对 messages 和 responses API 的扩展支持，客户可以把智能模型选择带入现有工作流。他们还可以访问更广泛的模型，并在不手动选择和管理模型的情况下优化质量、成本和性能。
- **选择：** Microsoft Foundry 提供来自 OpenAI、Claude、Muse、Mistral、开源社区等的 11,000 多个模型。来自 fal 的视频生成模型（包括 Kling、LTX 和 MiniMax）现已在 Foundry 中预览。Foundry 上的 Baseten 同样处于预览，将把 Baseten 的推理平台引入 Foundry，使组织能够运行针对速度、吞吐量和成本优化的开放模型，并在全球或美国数据区（US Data Zone）以无服务器按需付费方式部署。

受支持的模型可以在 Foundry 中作为与智能体相同的持续改进工作流的一部分进行评估和部署。

[**了解这项发布的更多信息。**](https://aka.ms/foundrymodelsignite2026)

Microsoft Foundry 正在扩展编码、图像创作、网络安全和工作流决策方面的模型选择。新的 Microsoft AI 模型包括 MAI-Code-2、MAI-Code-2-Flash、MAI-Image-2.7、MAI-Image-2.7-Flash 和 MAI-Cyber-2-Flash，而正式可用的 Microsoft-Decision-1.1 增加了高效的多模态路由和校验。扩展的路由器、11,000 多个可用模型、预览的视频生成选项和 Baseten 集成，帮助客户在相同的评估和部署工作流中优化质量、速度和成本。
## GitHub

即时摘要：

新的 Copilot 能力正在帮助开发者构建智能体、跨工具工作并交付更高质量的代码。Microsoft Copilot SDK 2.0 把经过生产验证的执行框架（harness）带入安全、可扩展的智能体部署。该框架由原生 Rust 运行时驱动，支持六种语言。GitHub Copilot 应用把 Azure DevOps 仓库从克隆推进到合并，并把测试带到真实的、已登录的浏览器中。Copilot 代码审查通过在 CLI 和应用中提供本地审查、机密检测、自适应审查工作量、跨仓库上下文和仓库洞察，帮助更早发现问题。

新的 GitHub Copilot 能力帮助开发者构建和部署智能体、跨工具工作并更早发现代码问题。Microsoft Copilot SDK 2.0 增加了经过生产验证、由 Rust 驱动的智能体执行框架，覆盖六种语言；GitHub Copilot 应用把 Azure DevOps 仓库从克隆推进到合并，并在真实登录的浏览器中测试；增强的代码审查增加了本地 CLI 和应用审查、机密检测、自适应工作量、跨仓库上下文和仓库洞察。

### GitHub

#### Microsoft Copilot SDK 2.0 提升 AI 应用的安全性和规模

即时摘要：

**Microsoft Copilot SDK** 现已升级到 **2.0**，对于希望构建智能体、尤其是大规模部署的企业来说是一次重大改进。此次更新包含基于原生 Rust 运行时构建的改进版 Copilot 执行框架，使开发者能够把智能体直接集成到应用内，也支持需要强大企业安全性的多租户、大规模应用。

该 SDK 使用与 Microsoft 和 GitHub 生产环境中部署的相同的执行框架技术，并支持六种编程语言。现已正式可用。

[**了解这项发布的更多信息**](https://aka.ms/copilot-sdk/blog-2.0)。

Microsoft Copilot SDK 2.0 现已正式可用，为企业提供更安全、更可扩展的基础，把智能体嵌入应用。其增强的 Copilot 执行框架运行在原生 Rust 运行时上，支持多租户、大规模部署，并使用 Microsoft 和 GitHub 部署的同一套经过生产验证的技术，覆盖六种编程语言。

## Microsoft Copilot

即时摘要：

随着我们与 AI 协作的方式不断演变，Microsoft Copilot 也在演变。新的 Copilot 包括 **Home**，这是 Chat 和 Cowork 的统一起点；**Auto**，Copilot 的智能路由器，为你的任务动态选择正确的模型和工作量，优化质量、速度和成本；以及 Copilot 中的 **Word**、**Excel** 和 **PowerPoint**，可在对话旁创建和协作处理文件。它还包括 **Code**，让任何人都能用自然语言构建安全应用；以及 **Autopilot**，一个常驻、主动的个人生产力智能体。**Copilot Managed Runtime** 安全托管你在 Cowork、Code 和 Copilot Studio 中构建的内容。

下文详述的这些更新，标志着为工作而构建的 Copilot 的下一章：一个人与 AI 协作的互联平台，具备组织完成更多工作所需的上下文、选择和控制。[了解更多](https://aka.ms/MicrosoftIgnite26Blog)。

Microsoft Copilot 正在演变为一个互联的工作平台：Home 统一 Chat 和 Cowork，Auto 选择正确的模型和推理工作量，Word、Excel 和 PowerPoint 就在对话旁边。Copilot Code 支持用自然语言创建应用，Autopilot 提供常驻的个人生产力，Copilot Managed Runtime 安全托管在 Cowork、Code 和 Copilot Studio 中构建的解决方案——在人与 AI 协作中为组织提供上下文、选择和控制。

### Microsoft Copilot

#### Agent 365 借助面向 AI 的 FinOps 把 AI 支出转化为业务价值

即时摘要：

Agent 365 是微软面向 AI 的可观测性平台，把组织中智能体和 AI 服务的管理、治理、安全和业务价值汇集在一起。AI 支出正在快速增长并超出 IT 的范围，领导者需要了解它花费多少、带来什么。

借助 Agent 365，面向 AI 的 FinOps 超越控制，力求最大化业务价值，让 IT 和业务领导者具备规划、控制和优化 AI 投资的可见性。功能包括：

[Microsoft 管理中心](https://aka.ms/microsoftadmincenter)中的 **Agent 365 Cost Management** 是一个集中位置，用于查看和控制不断增加的按使用量计费的 AI 服务，包括 Copilot Cowork、Copilot Code、GitHub Copilot CLI、Microsoft Copilot Studio、Copilot Managed Runtime、Autopilot 和 Work IQ API。

- 管理员将能够看到是什么推动了支出；设置支出策略、限额和警报；并通过 Microsoft Fabric 扩展分析，用于自定义成本分摊和报表。预览中。
- 管理员将能够预测支出、用平实语言提问，并根据优化建议采取行动。本月在 Frontier 计划中提供。
- 12 月，这些能力将扩展到包含跨 Microsoft 和非 Microsoft 智能体的价值洞察，以及向业务领导者的委派。

**Agent 365 Business Analytics** 现已在 Frontier 计划中提供，是面向业务领导者的新体验，提供必要的数据来了解 AI 支出、衡量其价值并决定下一步投资方向。他们将能够：

- 了解支出：洞察跨智能体、服务、模型和用户的成本驱动因素。
- 推动业务价值：通过成功率、用户满意度和受助时长等指标，衡量 AI 辅助对特定岗位和任务的价值。
- 优化 ROI：预测成本场景、根据建议采取行动、用平实语言提问，然后与 IT 合作调整成本分摊的护栏。

用户今天就可以开始使用 Agent 365 Business Analytics [应用](https://aka.ms/a365analytics)。Microsoft 服务的洞察要求租户中至少有一个 Microsoft 365 Copilot 许可证，非 Microsoft 服务的洞察则要求有 Agent 365 许可证。

[**了解这项发布的更多信息**](https://techcommunity.microsoft.com/blog/ai-finops-blog/introducing-microsoft-agent-365-business-analytics-turn-ai-investment-into-busin/4574149)。

Agent 365 正在把 FinOps 纪律带入 AI，跨智能体和 AI 服务提供集中成本管理、预测、策略、警报和业务价值衡量。预览和 Frontier 能力揭示支出驱动因素，支持通过 Fabric 进行自定义成本分摊，并衡量任务成功率、满意度和受助时长等结果；12 月，价值洞察将扩展到 Microsoft 和非 Microsoft 智能体，并允许向业务领导者委派。
#### Autopilot 正在向 Frontier 客户推出

即时摘要：

**Autopilot** 是微软首个面向个人生产力的企业级长时运行智能体。它将驻留在组织租户中，拥有自己的身份、记忆和对工具的访问权限，可以跟进线程、运行周期性工作，并在无需等待另一次提示的情况下持续推进项目。它为协作而设计，同事将能够在 Teams 频道或群聊中 @提及 某人的 Autopilot，以询问信息或请求其支持的操作。Autopilot 在设计上注重安全：它采取的操作（即使用户委托）都绑定到自己的智能体 ID 并经过安全检查，管理员可以看见并管理它。客户将能够在 Copilot 应用的左侧导航中找到 Autopilot。Autopilot 正通过 Frontier 计划推出。

**[了解这项发布的更多信息](https://aka.ms/MicrosoftIgnite26Blog)****。**

Autopilot 是微软首个企业级长时运行的个人生产力智能体，正通过 Frontier 计划推出。凭借组织租户内自己的身份、记忆和工具访问权限，它可以在没有提示的情况下持续推进项目、跟进线程并运行周期性工作。同事可以在 Teams 中 @提及 用户的 Autopilot，而管理员对绑定该智能体身份、经过安全检查的操作保持可见性和控制。

#### Copilot Managed Runtime 现已正式可用，并新增能力

即时摘要：

Copilot Managed Runtime 为应用提供 Microsoft 托管的托管与执行，并与应用的创建位置分离。构建者可以从 Copilot Code、Copilot Cowork 和 Microsoft Copilot Studio 等体验开始，也可以使用兼容的第三方开发工具。当应用发布到 Copilot Managed Runtime 后，组织便获得一种通用的方式来托管、运行和治理它。

随着 **Copilot Managed Runtime 正式可用**，微软正在扩展这一产品，为跨 Microsoft Copilot 和兼容第三方开发工具构建的应用提供可选的、由 Microsoft Fabric 服务构成的数据后端。

借助新的集成，可选地需要持久数据或额外后端能力的应用可以开箱即用地使用 Fabric 作为底层数据基础。Fabric 可以提供数据库、存储和数据 API 等后端能力，而 Copilot Managed Runtime 继续提供应用托管和企业管理层。

该集成把灵活的应用创建、Microsoft 托管的托管与治理，以及**可选的 Fabric 数据后端**结合起来，让组织选择适合自身需求的开发体验，同时为在 Microsoft 环境中运行应用提供一致的路径。

微软还宣布 **Copilot Managed Runtime 中的智能体与工作流（Agents and Workflows）**。第一个迭代版本将允许用户在本地构建自定义 Copilot Studio 智能体和工作流，用自己选择的开发工具进行修改，然后使用 CLI 发布到 Copilot Studio。这也为开发者提供了在 Copilot Studio 上协作开发智能体的方式，并通过 GitHub 等平台实现版本控制。

[**了解这项发布的更多信息**](https://aka.ms/CopilotManagedRuntime-Ignite-Blog)**。**

Copilot Managed Runtime 现已正式可用，提供一致的 Microsoft 托管环境，用于托管、执行和治理在 Copilot Code、Copilot Cowork、Copilot Studio 和兼容第三方工具中创建的应用。可选的 Microsoft Fabric 集成增加了数据库、存储和数据 API；新的智能体与工作流支持本地开发、通过 CLI 发布到 Copilot Studio，以及通过 GitHub 等平台进行协作式版本控制。

#### Copilot Workspaces 帮助团队与 Copilot 协作

即时摘要：

Copilot Workspaces 把团队、他们的工作和 Copilot 带到 Microsoft Copilot 应用中的共享空间。作为 Copilot Notebooks 的演进，Workspaces 帮助团队把共享上下文转化为持续工作流上的共同进展。

Work IQ 可以根据当前工作流推荐相关工作区，帮助人们快速上手。进入工作区后，团队成员可以协作处理共享文档，而 Copilot 串联起各项工作，呈现哪些内容发生了变化、哪些问题尚未解决、哪些操作需要关注，使每个人都能快速了解进展并推动工作继续。即将推出的是，团队将能够把个人 Autopilot 带入 Workspaces，让人和智能体在同一个空间协作，团队成员可以从亲自动手转向指挥工作。

Copilot Workspaces 通过 Frontier 计划在 Copilot 应用中提供。

[**了解这项发布的更多信息**](https://aka.ms/MicrosoftIgnite26Blog)。

Copilot Workspaces 把团队、共享内容和 Copilot 带入 Microsoft Copilot 应用中一个持续协作的空间。Work IQ 可以推荐相关工作区，Copilot 则跟踪共享文档中的更改、未解决的问题和待办操作，使成员能够快速了解现状。Workspaces 通过 Frontier 计划提供，不久将让团队把个人 Autopilot 智能体带入同一空间，并从完成工作转向指挥工作。

#### Dynamics 365 CRM 和 ERP 插件现已在 Copilot 中提供

即时摘要：

两个新的 Dynamics 365 插件让用户无需切换应用，即可在 Microsoft Copilot 中完成销售、财务和运营任务。它们是：

- **Dynamics 365 Sales 插件**现已正式可用，把销售能力带入 Copilot。销售人员可以制定客户计划、准备客户会议、了解交易进展并确定管道优先级。新的交易洞察跟踪季度预测的进展、梳理决策者和参与缺口，并标记需要关注的交易和风险。在该插件中，销售人员还可以在 PowerPoint 中创建演示文稿、为新客户调整现有演示文稿、刷新幻灯片数据，并确认审批和共享要求。
- **Dynamics 365 ERP 应用插件**现已正式可用，把企业资源规划（ERP）上下文和操作带入 Copilot Cowork 和 Excel。专门构建的业务技能让 Copilot 和智能体掌握常见财务和运营任务的知识。例如，在从采购到付款（Source-to-Pay）流程中，采购负责人可以简化采购申请、报价请求和采购订单的处理。

[**了解这项发布的更多信息**](https://aka.ms/A365AnalyticsLearn)**。**

两个已正式可用的 Dynamics 365 in Copilot 插件让用户直接在 Microsoft Copilot 中完成 CRM 和 ERP 工作。Sales 插件支持客户计划、会议准备、管道优先级排序、交易风险分析和 PowerPoint 创建，ERP 应用插件则把财务和运营上下文带入 Copilot Cowork 和 Excel，使用专门构建的技能简化采购申请、报价请求和采购订单等流程。

#### 使用 Copilot Code 轻松构建安全应用

即时摘要：

**Copilot Code** 将让每个人都能用自然语言构建仪表板、跟踪器和应用，使用与 GitHub Copilot 相同的智能体技术。云项目将在安全沙箱中运行、留在你的租户内，并且易于在内部共享，也可通过 iOS 和 Android 随身使用。新的本地沙箱将把这些保护扩展到人们的设备上，限制 Code 及其运行的一切所能读取、写入和访问的网络内容。

IT 将能够保持控制。受支持的应用将能够通过 Copilot Managed Runtime 发布，延续现有的 Microsoft 365 身份、安全和治理控制，应用可在 Microsoft 管理中心中查看和管理。

Copilot Code 在 Frontier 计划中于 Windows、Web、iOS 和 Android 上提供，本地沙箱在 Windows 上可用，即将登陆 macOS。Copilot Code 将于 12 月正式可用。

[**了解这项发布的更多信息**](https://aka.ms/MicrosoftIgnite26Blog)。

Copilot Code 让人们使用 GitHub Copilot 背后的智能体技术，通过自然语言创建仪表板、跟踪器和应用。云沙箱和本地沙箱限制网络访问，Copilot Managed Runtime 则把 Microsoft 365 身份、安全、治理和管理员可见性扩展到已发布的应用。它通过 Frontier 计划在 Windows、Web、iOS 和 Android 上提供，计划于 12 月正式可用，macOS 本地沙箱支持即将推出。

#### Microsoft Copilot 应用中的 Home

即时摘要：

**Home** [于 9 月发布](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)，现正在全球推出，是 Copilot 中的新起点，把 Chat 和 Cowork 结合在一起，让人们可以轻松地在快速提问和委派复杂工作流之间切换。更新包括使用 **Auto**（Copilot 的智能路由器，为任务动态选择正确的模型和工作量）时的两项新能力：

- Auto 现在会建议把复杂任务从 Chat 转到 Cowork，帮助用户选择能给出最佳响应的模式。如果用户选择继续在 Cowork 中处理，其上下文会随之迁移，使其保持在工作流中。此能力已正式可用。
- Cowork 中的 Auto 将使用 Microsoft-Decision-1.1——一个快速、高性价比的决策模型——根据用户任务动态选择工作量级别。它会把任务拆分为多个部分，为每个部分匹配模型，最终使用决策模型快速确定每个部分的合适工作量级别。此能力面向 Frontier 客户提供。

其他新能力包括：

- **Copilot Cowork** 将根据近期的 Work IQ 信号推荐要开始的任务，并调用公司已经构建的声明式智能体，帮助用户完成更多复杂工作。声明式智能体通过 Frontier 计划提供私人预览。
- **Office in Copilot** 现已正式可用，把 Word、Excel 和 PowerPoint 的全部能力带入 Microsoft Copilot 应用，使人们可以直接从对话转向创建和协作处理文档、工作簿和演示文稿。

  人们可以用 Copilot 塑造自己的工作，或直接用 Office 熟悉的格式设置、评论和实时共同创作能力进行编辑，然后在需要时无缝过渡到完整的 Office 应用。文件保存到 OneDrive，并继承 Microsoft 365 权限、敏感度标签和合规控制，帮助人们安全协作，而无需重建上下文或从头开始。

[**了解这项发布的更多信息**](https://aka.ms/MicrosoftIgnite26Blog)**。**

Home 正在全球推出，作为 Copilot 应用中 Chat 和 Cowork 的统一入口。正式可用的 Auto 建议可以把复杂工作转入 Cowork 而不丢失上下文，Frontier 客户则可以使用 Microsoft-Decision-1.1 调整工作量、根据 Work IQ 推荐任务并调用公司智能体。Office in Copilot 也已正式可用，把 Word、Excel 和 PowerPoint 的能力嵌入到对话中，并在创建和协作时直接沿用 Microsoft 365 的保护。

#### Microsoft 扩展 Dynamics 365 Activate，支持智能体化 ERP 迁移

即时摘要：

新能力将把 Microsoft Dynamics 365 Activate 从 CRM 扩展到 ERP，帮助组织及其实施伙伴评估现有的 SAP ECC 环境并迁移到 Dynamics 365。对于 CRM，Salesforce 迁移体验现已正式可用。

随着 SAP ECC 临近主流维护终止，评估 ERP 选项的组织必须决定迁移、简化或重新设计哪些自定义项、集成和业务流程。Dynamics 365 Activate 是一个实施和迁移平台，使用智能体能力支持这项工作，并由项目团队审查和验证每一项建议。

新增和即将推出的能力如下，从今天开始逐步推出，并将在未来数周持续：

- **SAP ECC 发现**将分析现有的 SAP ECC 环境，包括业务流程、配置、自定义项和依赖关系。它将识别迁移复杂性、潜在差距和需要进一步评估的领域，帮助团队在实施开始前确定项目范围。
- **需求分析**将帮助团队把业务需求转化为 Dynamics 365 需求。
- **配置**将帮助团队设置新的 Dynamics 365 环境。**数据迁移**将帮助把数据从现有系统迁移到 Dynamics 365。项目上下文将从评估一直延续到实施，使团队不必在每个阶段重复工作。

Dynamics 365 Activate 构建在 Success by Design——微软的实施方法之上。

[**了解这项发布的更多信息**](https://aka.ms/D365Ignite2026)**。**

Microsoft Dynamics 365 Activate 正从 CRM 扩展到 ERP，利用智能体能力和人工验证，帮助组织评估 SAP ECC 环境并迁移到 Dynamics 365。该平台将在未来数周推出，将分析流程、配置、自定义项和依赖关系，把需求转化为要求，配置新环境，迁移数据，并从评估到实施保留项目上下文。Salesforce CRM 迁移体验现已正式可用。

#### Microsoft 与 Salesforce 宣布在 Copilot、Teams 和 Fabric 中提供 Salesforce

即时摘要：

Microsoft 与 Salesforce 继续合作，在 Microsoft Copilot、Microsoft Teams 和 Microsoft Fabric 中新增 Salesforce 集成。这把 Salesforce 的客户上下文、业务流程和操作带入人们每天使用的 Microsoft 工具。

**Copilot 中的 Salesforce** 现已在预览中提供，包含 38 个以上的预置销售技能，将把客户上下文与整个业务中正在进行的工作连接起来。在 Copilot 内，销售人员将能够通过经过身份验证的 Salesforce MCP 访问，在其现有 Salesforce 权限范围内安全地获取客户信息并执行受支持的业务操作。随后，销售人员将能够借助 Work IQ 把该上下文用于整个 Microsoft 365——Work IQ 会从 Teams 会议、Outlook 邮件和文档中添加相关上下文。

对许多组织来说，工作首先从 Teams 开始，人们在这里共享文件、做出决策并相互交接工作。Teams 中的 Sales Cloud 现已进入试点，将把 Salesforce 客户上下文直接带入这种协作，使销售人员能够实时查看管道和配额进展、交易通知和简报材料。

此外，Microsoft 和 Salesforce 正在 Salesforce Data 360 与 Microsoft Fabric 之间建立双向的零拷贝（Zero Copy）连接。借助现已正式可用的 Data Federation，共同客户现在可以直接在 Salesforce Data 360 内查询和分析受支持的 Microsoft Fabric OneLake 数据。这种原生的零拷贝连接让组织能够把客户工作流和 CRM 体验建立在全企业范围的运营和财务数据之上，同时把源数据留在 Fabric 中。

[**了解这些更新的更多信息**](https://aka.ms/AA1457n5)。

Microsoft 和 Salesforce 正在通过 Copilot、Teams 和 Fabric 中的新集成扩大合作。Copilot 中的 Salesforce 插件把客户上下文和 38 个以上预置销售技能带入 Microsoft Copilot（译注：原文为「Microsoft Copilot365」，其中「365」应为笔误），Teams 中的 Sales Cloud 则提供实时管道洞察和交易更新。Salesforce Data 360 与 Microsoft Fabric 之间的双向零拷贝连接还使组织能够跨平台分析企业数据，而无需移动源数据。

#### Today 帮助人们确定优先事项并处理重要工作

即时摘要：

**Today** 是 Microsoft Copilot 应用和 Outlook 中的新体验，将通过呈现关键优先事项并主动准备下一步，帮助人们掌握工作。

Today 将汇集来自电子邮件、日历、聊天和会议的信息，创建需要关注事项的个性化视图。它还将主动准备工作，包括邮件草稿、聊天消息和日程变更，供用户审阅和批准。

该体验包括两项能力：

- **Today Brief** 将提供个性化的早晨简报，突出优先事项并准备下一步，帮助用户在一天开始时了解进展并准备好行动。这项每日刷新包含在 Microsoft 365 Copilot 许可证中。
- **Today Feed** 将在早晨简报的基础上，随着新的电子邮件、消息和会议到来全天自动刷新，帮助用户在一天展开过程中掌握不断变化的优先事项。全天的周期性更新需要 Copilot 额度（Copilot credits）。

Today 将通过 Frontier 计划开始私人预览。

[**了解这项发布的更多信息**](https://aka.ms/MicrosoftIgnite26Blog)。

**Today** 是 Copilot 和 Outlook 中的新功能，把来自电子邮件、日历、聊天和会议的信息结合起来，帮助识别优先事项并准备待批准的下一步。Today Brief 包含在 Microsoft 365 Copilot 许可证中，提供个性化的早晨概览并准备操作供用户审阅。Today Feed 需要 Copilot 额度，会随着新信息到来全天更新优先事项。该体验将通过 Frontier 计划开始私人预览。
## Microsoft Edge

即时摘要：

行业研究表明，约 85% 的工作在浏览器中完成，这使其成为需要管理和保护的关键端点。Microsoft Edge for Business 是业界领先的安全企业浏览器——现在是全球使用最广泛的企业浏览器[1](#Footnote1)。随着 AI 从聊天转向采取行动，浏览器治理比以往任何时候都更重要。Edge for Business 通过原生集成提供安全能力，最大化来自 Microsoft 365 的保护。新的更新带来为企业治理而构建的智能体化浏览，以及面向当今网络安全格局的基础安全。

Microsoft Edge for Business 正在增加新的 AI 和安全功能，帮助组织保护和管理人以及 AI 智能体基于浏览器的活动。约 85% 的工作发生在浏览器中，这些更新把智能体化浏览与内置的 Microsoft 365 安全保护结合起来，帮助组织在 AI 从对话转向行动时保持控制。

### Edge for Business

#### Edge for Business 增加受治理的 AI 工作流和更强的安全

即时摘要：

Microsoft Edge for Business 现在是全球使用最广泛的企业浏览器[1](#Footnote1)，它宣布了新的 AI 和安全能力，旨在帮助组织提高生产力，同时让人和智能体的活动受到治理和保护。这些能力包括：

**AI 更新：**

- 技能录制器（Skills recorder）将让员工在 Edge for Business 中录制工作流，并把它转化为可供 Copilot Cowork 使用的可复用、可共享技能。IT 将能够控制该能力何时启用，生成的技能将在员工现有权限和组织策略的范围内运行。录制的技能每次都会遵循相同的步骤，以实现可预测、高效的执行。技能录制器与 Cowork 一起处于预览。
- 新的受管智能体浏览体验将使 IT 能够在智能体任务需要浏览器时，强制 Microsoft 和第三方智能体使用 Edge for Business。每个智能体将在一个专用窗口中工作，拥有自己的 Microsoft Entra 智能体身份，并在用户现有权限和组织策略的范围内运行。视觉提示将清楚表明某个窗口属于智能体。该体验现已进入预览。

**安全更新：**

- 扩展安全性（Extension safety）现已正式可用，提供组织范围的清单，并带有 Akamai 和 Spin.AI 在扩展和版本级别的风险评分，帮助管理员评估风险并做出允许或阻止的决定。扩展泄露控制（Extension leak control）处于预览，将更进一步，阻止选定的组织已安装扩展读取受保护页面上的内容。
- 面向 Edge for Business 的原生 Microsoft Sentinel 连接器将把浏览器安全事件和审计日志带入 Microsoft Sentinel，帮助团队在一个地方调查和狩猎威胁。该连接器处于预览。
- Edge for Business 中的 Microsoft Entra Global Secure Access 将简化安全访问，使 Windows PC 上的员工能够通过已登录的工作配置文件访问私有 Web 应用，而无需单独的 VPN 客户端、网络代理或浏览器扩展。该集成处于预览。

*1 基于员工超过 1,000 人的组织中 Windows 设备上的全球浏览器使用时长份额。*

[**了解这项发布的更多信息**](https://aka.ms/EdgeIgnite26)。
**[下载与这项发布相关的视觉素材。](https://msftglobalcomms-my.sharepoint.com/:f:/g/personal/global_msftglobalcomms_onmicrosoft_com/IgCu2rsoKP-1QIRcGw-FZ_uTAS8sy4r_vXCOOD-74p3FEYU?e=z38MOs)**

Microsoft Edge for Business 正在增加新的 AI 工作流和更强的安全保护。预览功能让员工为 Copilot Cowork 录制可复用、可共享的技能，并让 Microsoft 和第三方 AI 智能体拥有各自独立身份的浏览器窗口。安全更新包括已正式可用的浏览器扩展风险评估工具，以及扩展数据访问控制、Microsoft Sentinel 集成和通过 Microsoft Entra Global Secure Access 无需单独 VPN 即可访问私有 Web 应用的预览控制。

## Microsoft IQ

即时摘要：

微软相信 AI 应当放大客户的业务优势。今天，**Microsoft IQ** 正在扩展为完整的企业上下文管理平台。

Microsoft IQ 汇集使每个组织与众不同的数据、知识、专业能力和经过验证的工作方式，并把这种智能用于应用和智能体。新功能通过业务插件提供一个受治理的归属地，供团队复用技能、工具和智能体。增强的上下文管理能力通过 Work IQ、Fabric IQ、Foundry IQ 和 Web IQ，把智能体与工作、业务数据、非结构化内容和现实世界知识连接起来，并由 Microsoft Foundry 提供持续改进。

这些更新共同帮助组织保留、应用并发展自己的 IQ，使今天构建的内容成为未来构建的基础。

**Microsoft IQ** 正在扩展为企业上下文管理平台，把组织的数据、知识、专业能力和经过验证的工作方式带入应用和智能体。可复用的业务插件、技能、工具和智能体帮助团队安全地共享并基于行之有效的内容继续构建，把 AI 与人们的工作、业务数据、非结构化内容和现实世界知识连接起来。通过 Microsoft Foundry 的持续改进，帮助这种组织智能随时间增长。

### Microsoft IQ

#### 推出 Microsoft IQ，面向企业 AI 的平台

即时摘要：

**Microsoft IQ** 现已正式可用，把客户的智能用于他们构建的应用和智能体，使团队能够复用行之有效的内容，并在模型、工具和业务需求变化时保留所学。每一次改进都会增加客户的 IQ，为未来的工作提供更强的起点。Microsoft IQ 汇集两项能力：

- **企业上下文管理**通过 Work IQ、Fabric IQ、Foundry IQ 和 Web IQ，以及可复用的业务插件、技能、工具和智能体，把智能体与人们的工作方式、业务数据、非结构化内容和现实世界信息连接起来。业务插件为每个场景组织这些上下文和专业能力。
- **Microsoft Foundry 中的持续改进**把评估和生产洞察连接到智能体优化和模型训练，显著改善客户成果。

新的 Microsoft IQ 构建在客户已经使用的产品之上，无需新的 SKU 或订阅。它与 **Microsoft Agent 365 治理**一起，帮助客户在扩展应用、采用新模型和改进智能体时保留、应用和发展自己的 IQ。

[**了解这项发布的更多信息**](https://aka.ms/miq-ignitelaunchblog)。

**Microsoft IQ** 现已正式可用，把企业上下文管理与持续改进结合起来，使组织能够保留并复用其应用和智能体所学到的内容。它把 AI 与人们的工作、业务数据、非结构化内容和现实世界信息连接起来，而 Microsoft Foundry 使用评估和生产洞察来改进智能体并训练模型。Microsoft IQ 构建在客户已经使用的产品之上，无需新订阅，并与 Microsoft Agent 365 一起帮助组织治理其智能体。

### Microsoft IQ：企业上下文管理

#### Microsoft IQ 把智能体连接到你的业务专业能力

即时摘要：

**新的企业上下文管理能力**把智能体连接到它们理解手头工作所需的信息、含义和专业能力。Work IQ 带来工作数据以及决策背后的上下文，Fabric IQ 把业务数据与指标和运营含义连接起来，Foundry IQ 激活非结构化内容，Web IQ 提供现实世界信息。这些来源共同帮助智能体利用组织所知道的更多内容。上下文能力已在 Microsoft Copilot、GitHub Copilot、Microsoft Foundry 以及任何通过 MCP 接入的智能体执行框架中正式可用。

组织还可以发现并复用企业 AI 的构建模块，这些模块在 Microsoft Copilot 中通过 Microsoft IQ API 提供。业务插件把能力打包以便安装和复用；技能为特定任务捕获可复用的指令、专业知识和支持资源；工具为智能体提供可调用的能力，例如从业务系统检索信息或执行操作；智能体可以发布以供整个组织复用。这些能力已正式可用。

**Microsoft IQ 中的业务插件**在 Frontier 计划中提供，把这种复用推进一步。插件打包的是单项能力，而业务插件将基于可复用的技能，构建受管理的、场景特定的指导层级。它们将告诉智能体应使用哪些上下文、工具、技能和权威来源，帮助组织在团队之间一致地应用其专业能力。

Microsoft IQ 中的业务插件：

- 由领域专家策划。获授权的团队围绕智能体需要完成的工作，为组织、业务部门或项目组织指导内容。
- 支持层级继承。智能体可以从组织结构中继承相关指导，使团队能够复用共同的专业基础，并添加场景特定的上下文。
- 全程受治理。敏感度标签、变更审计和治理洞察支持随时间管理这些指导内容。

业务插件旨在帮助智能体使用相关指令和来源，同时减少不必要的上下文。目标是随着组织扩大技能和专业能力的复用，获得更高质量的结果并降低 token 成本。

[**了解这项发布的更多信息**](https://aka.ms/miq-ignitelaunchblog)。

Microsoft IQ 现在通过 Microsoft Copilot、GitHub Copilot、Microsoft Foundry 和其他兼容智能体平台中正式可用的能力，把 AI 智能体连接到组织的知识和专业能力。组织可以复用业务插件、技能、工具和智能体，而 Frontier 计划中新的业务插件让专家提供智能体可跨团队使用的指导。敏感度标签、审计和其他控制帮助组织管理这些指导，目标是改善结果并降低成本。

### Foundry IQ

#### Foundry IQ 把非结构化数据带给应用和智能体

即时摘要：

Foundry IQ 帮助开发者把非结构化数据用于传统应用搜索和智能体工作负载。它把关键词、向量和混合搜索与语义排序结合起来，服务于搜索驱动的应用；并通过智能体检索为更复杂的问题跨知识源规划和迭代。新能力加深了应用和智能体发现和连接信息的方式：

- **知识图谱**（预览）将连接跨文档的实体和关系，并把内容组织成主题。智能体将能够追踪从某项法规到供应商再到受影响产品的连接，并引用支持来源。基于主题的检索将帮助回答跨集合的更广泛问题，例如一组合同中贯穿的主题。
- **Microsoft-Retriever-1**（预览）是一个新的检索模型，将运行迭代搜索和查询规划，以实现更快、更高效的依据获取。
- **每个新 Foundry 项目中的 Foundry IQ 资源**（预览）将从第一天起在基于使用量的无服务器计划上提供依据能力。
- **SharePoint 索引知识源**现已正式可用，把 SharePoint 内容带入 Foundry IQ 检索，使应用和智能体能够在遵守源权限的同时找到相关信息。

这些更新帮助开发者构建搜索体验和智能体，使其能够检索相关内容、追踪跨文档的关系，并把响应建立在组织数据之上。

[**了解这项发布的更多信息**](https://aka.ms/miq-ignitelaunchblog)。

Foundry IQ 正在扩展应用和 AI 智能体跨文档及其他内容检索和连接信息的方式。预览中的新功能包括帮助识别跨文档关系和主题的知识图谱、帮助智能体更快更高效找到相关信息的 Microsoft-Retriever-1，以及在新 Foundry 项目中内置的、帮助把 AI 响应建立在信息之上的访问能力。现已正式可用的 SharePoint 集成让应用和智能体在遵守现有权限的同时找到相关的组织内容。

### Fabric IQ

#### 借助 Fabric IQ 把可信业务上下文带入更多体验

即时摘要：

跨 Microsoft Copilot 和 Fabric apps 的新 Fabric IQ 集成现已正式可用，跨 Excel、GitHub Copilot、ChatGPT 和 Claude 的集成也已可用，使人们和 AI 每天使用的体验更容易获得可信的企业数据和业务上下文。

Fabric IQ 提供一个共享智能层，把企业数据与人、应用和 AI 智能体所需的业务含义和运营上下文连接起来。它结合 Microsoft OneLake 的统一数据、Power BI 语义模型中的可信指标，以及本体（ontologies）中的运营上下文，使人与智能体对业务形成一致理解，包括指导最佳操作的规则。专业化的数据智能体基于这些上下文，对企业数据进行推理，并为自然语言问题提供相关答案。

**在 Microsoft Copilot 中**，用户可以把 Fabric IQ 直接带入工作，获得以可信业务上下文为依据的答案。他们还可以在 Copilot 中访问 Power BI 语义模型，该能力已正式可用。

**在 Excel 中**，用户可以在 Edit with Copilot 中开启 Fabric IQ（预览），向受治理的语义模型提问，并创建与 Fabric 实时连接的透视表。

**通过 Fabric apps**，开发者可以把由 Power BI 语义模型和 Fabric 数据智能体驱动的对话体验嵌入其自定义应用，使用户能够直接在应用内探索和交互企业数据。GitHub Copilot 中的 Fabric IQ 本体（预览）将把可信业务上下文带入应用开发。

**面向 ChatGPT 和 Claude 的新 Fabric IQ 连接器**处于预览，将把 Power BI 语义模型的洞察直接带入这两个助手。用户将能够在不打开报表的情况下对企业数据提问，答案将基于组织分析师已经维护的度量值，因此 ChatGPT 或 Claude 中的收入数字将与公司季度业务回顾中的数字一致。

[**了解这项发布的更多信息**](https://aka.ms/miq-ignitelaunchblog)。

Fabric IQ 正在把可信的业务数据和信息带入 Microsoft Copilot、Fabric apps 以及人们每天使用的其他工具。新的集成有的已正式可用，有的处于预览，把这些能力扩展到 Excel、GitHub Copilot、ChatGPT 和 Claude。用户可以就组织的数据提问，并创建连接实时数据的透视表。ChatGPT 和 Claude 中的答案将基于其组织已经使用的相同信息，因此例如收入数字可以与公司季度业务回顾中的数字一致。

### Web IQ

#### Web IQ 现面向 Azure 客户正式可用

即时摘要：

Web IQ 现在面向所有 Azure 客户正式可用，使开发者更容易以新的更低价格，把来自整个 Web 的新鲜、相关知识带入 AI 智能体和应用。Web IQ 把现实世界知识——来自网页、新闻、图像、视频等——与专业数据连接起来，扩展智能体在其基础模型和业务数据之外所知的内容，使其能够提供更好的答案和操作。其他更新包括：

- **Web IQ 中的 Auto 模式**让把正确的现实世界知识带入智能体变得更简单。Auto 模式无需开发者选择和编排各个 API，而是把 Web、图像、视频、新闻以及新的地点（Places）和天气（Weather）类别整合到一个快速、高性价比的体验中。这减少了把网络依据构建到应用中的工作量，同时帮助智能体为其响应检索相关外部上下文。现已正式可用。
- **Web IQ Auto Advanced** 改进了对更复杂问题的检索。当初始结果不够充分时，Auto Advanced 可以评估响应、优化查询并检索额外信息。这为开发者提供了一种无需自行构建迭代检索逻辑即可改善高要求场景结果的方法。现已正式可用。
- **Web IQ Scopes** 让组织能够更好地控制其 AI 智能体可以访问的 Web 内容。这使开发者和企业管理员在把 AI 响应的依据建立在 Web 内容上时，可以包含或排除特定的 URL、域、站点和路径。现已正式可用。
- **专业知识域**新增三个数据类别。**Web IQ Places** 提供 2.075 亿个现实世界实体的智能信息，帮助客户更快构建位置感知体验、改进本地发现和推荐，并减少维护地点数据的工作量。**Web IQ Weather** 把微软的天气智能直接带入 AI 智能体，帮助客户更快构建天气感知体验、改进规划和推荐，并应对不断变化的天气状况。Web IQ Places 和 Web IQ Weather 已正式可用。**Web IQ Commerce** 将为 AI 购物智能体提供覆盖 400 多亿条商品列表的结构化商品数据。商品 ID、图像、描述、价格、库存和多商家报价将帮助智能体比较商品，并大规模提供更快、更高质量的推荐。Web IQ Commerce 处于私人预览。
- **Web IQ 的医疗健康增强**通过可信、可引用的健康证据，帮助组织构建更好的健康智能体和其他 AI 体验。新的健康感知排序使用来源可信度信号（参考美国国家医学院独立确立的原则），把可信的健康来源排在论坛和博客之前。它在 Web IQ API 上运行，无需新的集成或单独的 SKU。正式可用。

[**了解这些更新的更多信息**](https://aka.ms/webiqnews)**。**

Web IQ 现在面向所有 Azure 客户正式可用，帮助开发者更轻松、更低成本地为 AI 智能体和应用提供来自网站、新闻、图像、视频和其他来源的最新信息，使其能够提供更好的答案和操作。Auto 模式和 Auto Advanced 简化了检索，即使是复杂问题；Scopes 让组织更好地控制智能体可以访问哪些 Web 来源。新的地点和天气能力帮助智能体提供特定位置的信息和天气预报，而私人预览中的 Commerce 将为购物智能体提供来自 400 多亿条商品列表的信息。新的健康相关搜索改进帮助智能体找到可信的医学信息来源。

### Work IQ

#### Work IQ 为 Copilot 和智能体扩展上下文、操作和控制

即时摘要：

Work IQ 正在扩展，新能力为 Copilot 和智能体提供更丰富的组织上下文、更多行动方式，以及供企业治理智能体运行方式的额外控制。

这些新能力包括：

- **更丰富的上下文：** Work IQ 正在扩展智能体可以跨 Microsoft 365 和业务应用访问的信息。新的检索能力帮助智能体找到相关的、感知权限的信息，而记忆可以让有用的用户和组织上下文跨体验使用。现已正式可用。
- **更多行动方式：** 新的智能体能力超越了回答问题，可以创建和编辑工作内容、处理运行时间更长的任务并执行更复杂的工作流。现已正式可用。
- **更主动的智能体：** 新的监听能力将让智能体在相关事件发生时作出响应，例如新消息或业务事件，而无需由人发起每一次交互。预览中。
- **扩展的企业控制：** 新的治理能力将提供更细粒度的策略和人工审批选项，帮助组织控制智能体可以访问什么、可以采取哪些操作。预览中。
- **扩展的合作伙伴平台：** Work IQ 正在扩展到第三方 AI 平台，计划与 OpenAI 和 Anthropic 集成（即将推出），为客户提供更多方式把组织上下文带入他们使用的 AI 体验和智能体。现已正式可用。

这些更新共同推动 Work IQ 从为 AI 体验提供上下文，发展到让智能体能够理解组织的工作、代表组织行动，并在企业控制范围内运行。

[**了解这项发布的更多信息**](https://aka.ms/miq-ignitelaunchblog)。

Work IQ 正在扩展，新能力帮助 AI 智能体更好地理解组织的工作、采取行动并在其规则内运行。正式可用的更新帮助智能体在遵守现有权限的同时找到相关信息、记住有用的上下文、创建和编辑内容并处理更复杂的任务。预览中的新能力将让智能体无需提示即可监听相关事件（如新消息），并让管理员更好地控制智能体可以访问和执行的内容。Work IQ 还在向第三方 AI 平台扩展，计划与 OpenAI 和 Anthropic 集成（即将推出）。

### 持续改进

#### 持续改进帮助智能体和模型在生产中学习

即时摘要：

Microsoft IQ 中的持续改进让 Microsoft Foundry 的新能力落地，使应用和智能体在上线后持续变好。它把实时生产信号转化为每一层的改进，从智能体的配置到模型本身。团队定义成功标准，衡量质量、延迟和每个成功结果的成本，然后在部署前批准变更。

Foundry 中的智能体优化器（Agent Optimizer）根据这些成功标准评估智能体，生成改进的配置并排序，使团队可以部署最佳配置。当配置变更不再带来收益时，团队可以通过后训练把相同的标准和生产信号应用到模型本身。

- 托管训练是一种简单、自动化的模型质量改进方式，覆盖大多数自定义需求。
- 可编程训练处于预览，为 AI 工程师提供更强的控制，使其能够为受支持的开放权重模型编写自定义训练循环，包括监督微调和强化学习，而由 Foundry 管理计算。

这些工具共同为团队提供一条从简单、自动化优化到完全自定义训练的路径。这项工作建立在已正式可用的 Foundry 能力之上：

- 从团队工作的地方开始。制作者可以从 Copilot 开始，专业开发者可以在 GitHub 或 Foundry 中构建。
- 选择并适配模型。Foundry 使团队能够根据质量和成本要求比较模型、选择适合任务的模型，并用自有数据适配受支持的模型。
- 构建和运行智能体。Foundry Agent Service 把模型连接到企业知识和工具，使智能体能够跨业务系统采取行动。面向受支持智能体的托管运行时，具备身份和授权，帮助团队在生产中运行它们。
- 在生产中运营和改进。集成的跟踪、评估和安全控制帮助团队理解行为并评估变更，与企业治理的连接则支持监督。

行之有效的内容会被保留。被证明有价值的上下文、技能和评估，通过企业上下文管理可在智能体和工作流之间复用，使每一次改进都建立在前一次之上。

[**了解这项发布的更多信息**](https://aka.ms/miq-ignitelaunchblog)。

Microsoft IQ 和 Foundry 正在增加能力，帮助组织在应用和 AI 智能体投入使用后持续改进它们。团队可以为质量、速度和成本设定目标，然后在部署前评估并批准改进。智能体优化器生成并排序潜在变更，使团队可以部署最佳方案。当这些变更不再带来收益时，托管训练和处于预览的可编程训练帮助团队改进底层 AI 模型。组织还可以跨智能体和工作流复用并基于所学内容继续构建。
## 安全

即时摘要：

随着 AI 智能体从回答问题转向采取行动，安全成为信任的基础。**Microsoft Perception 现已正式可用**，把专业安全智能体和剧本汇集起来，用于调查威胁并加强防御。**Agent 365、Microsoft Entra、Intune、Defender** 和 **Purview** 中新的智能体治理和安全能力，让组织对智能体及其身份、工具、访问和数据拥有更强的可见性和控制。

这些更新以及下文列出的更新，共同帮助组织在智能体企业的每一层建立信任，让人和智能体能够自由行动，并具备组织所需的安全、控制和问责。

随着智能体从回答问题转向采取行动，微软正在加强智能体安全。Microsoft Perception 现已正式可用，把专业安全智能体和剧本结合起来，用于调查威胁并加强防御。Microsoft Agent 365、Microsoft Entra、Intune、Defender 和 Purview 中的新能力帮助组织监控和控制智能体，包括其身份、工具、访问和数据。

### Agent 365

#### Agent 365 中的动态智能体风险（Dynamic Agent Risk）进入预览

即时摘要：

**动态智能体风险（Dynamic Agent Risk）** 处于预览，将利用微软的安全上下文引擎，把运行时信号（身份、访问、数据、端点、云和网络）、安全态势和爆炸半径融合为全面的智能体风险评估——安全团队无需再拼凑孤立的安全工具来获得完整的智能体风险视图。

动态智能体风险将跟随智能体，在其采取新操作、成为恶意活动目标或收到代码或模型更新时持续更新——始终随风险变化而更新——并作为核心基础构件，与 Agent Registry 一起在 Microsoft 365 管理中心以及 Defender、Entra、Intune 和 Purview 中可见。

此外，与风险管理平台 Check Point、Cyera、Darktrace 和 Zenity 的合作，把合作伙伴的智能体安全信号带入 Microsoft Sentinel，并将其作为 Microsoft 为 Agent 365 计算智能体风险时的证据。计划中的流程使用专用的智能体风险连接器和商定的数据架构。Sentinel 分析规则把传入的合作伙伴信号转化为警报。Microsoft Security 随后把受支持的警报关联到智能体，并纳入其风险评估。Microsoft 计算统一的低、中、高风险级别，而提供数据的厂商仍作为数据源可见。整体风险设计考虑运行时风险、暴露面和爆炸半径，合作伙伴信号提供运行时证据。

这种对智能体风险的权威理解，将构成以速度和规模开展全面运行时风险缓解和遏制的基础，通过 Microsoft Perception 全天候运行。

[**了解这项发布的更多信息**](https://aka.ms/secureAIannounce)。

Microsoft Agent 365 中现处预览的动态智能体风险，帮助组织持续评估 AI 智能体带来的安全风险。它把智能体的身份、访问、数据和活动信息结合起来，在智能体采取新操作、遭遇攻击和收到更新时评估风险。评估结果将在 Microsoft 的管理和安全产品中提供，并通过 Microsoft Sentinel 纳入风险管理平台合作伙伴 Check Point、Cyera、Darktrace 和 Zenity 的信息。这些信息将帮助组织借助 Microsoft Perception 更快响应威胁。

#### 管理洞察现已成为 Microsoft 智能体的默认功能

即时摘要：

在 Microsoft 管理中心中，面向 Microsoft 预构建智能体和基于 Microsoft 平台构建的智能体，Agent 365 使用和活动洞察的访问范围正在扩大。这一变更已正式可用，无论 Agent 365 许可状态如何，都扩展了对智能体概览、活跃用户以及活动、会话、异常率和运行时等高级使用指标的访问。这为管理员提供智能体使用和活动的基础可见性，帮助他们了解哪里可能需要额外的管理、治理和安全能力。

Viva Insights 将取消智能体洞察对 Agent 365 许可证的要求，同时保留至少 50 个已分配 Copilot 许可证的要求。符合条件的组织可以查看智能体、用户和会话指标，导出数据，并通过灵活查询进行探索。

这些变更将使更多组织获得智能体使用和运营信息。要获得 Agent 365 管理指标、治理和安全能力的全部价值，客户仍需 Agent 365 或 ME7 许可证。客户仍需 Agent 365 许可证才能获得企业级管理、安全和治理，包括来自 Microsoft Defender 的风险和安全洞察、Defender 高级狩猎功能中的 Agent Map、Microsoft Purview，以及第三方智能体的完整洞察。

[**了解这项更新的更多信息。**](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753)

微软正在扩大 Microsoft 管理中心中 Agent 365 使用和活动洞察的访问范围，使其面向 Microsoft 预构建智能体和基于 Microsoft 平台构建的智能体正式可用，且无需 Agent 365 许可证。管理员可以看到有多少人在使用智能体、它们运行的频率以及表现如何。符合条件的 Viva Insights 客户也不再需要 Agent 365 许可证即可获得智能体洞察。第三方智能体的高级洞察以及额外的管理、治理和安全能力仍需 Agent 365 或 ME7 许可。

#### Microsoft Agent 365 扩展对智能体及其工具的治理

即时摘要：

Microsoft Agent 365 正在增加能力，帮助 IT 管理员识别需要关注的智能体、了解智能体和模型的使用情况，并治理整个智能体资产中的工具、策略和模型：

- **新的操作中心（action center）** 将把治理任务集中到一个专注的体验中，最初会呈现不活跃的智能体和无主智能体，供审查和清理。管理员可以从需要关注的智能体开始，而不必搜索整个清单。操作中心预计于 12 月进入私人预览。
- Agent Map 中的**业务用例和任务分类**将帮助管理员了解智能体做什么，并识别执行相似工作的智能体。这些洞察将支持关于保留或合并哪些智能体的决策。该能力处于预览。
- **Copilot 和 Cowork 的插件与技能治理**让管理员可以从 Microsoft 365 管理中心集中管理插件和技能的可用性，并向特定用户和组分配访问权限。插件与技能治理已正式可用。
- **对 MCP 服务器和工具的扩展治理**将让管理员把来自 Azure AI Gateway 和 LiteLLM 等第三方网关的 MCP 服务器带入集中治理体验，具备对工具使用和依赖关系的可见性，以及管理可用性的控制，包括了解当某个 MCP 服务器被阻止时哪些插件可能受影响。Azure AI Gateway 和 LiteLLM 网关支持处于预览。
- **本地和影子智能体治理**将增加阻止之外的更细粒度控制。管理员还将能够观察本地和影子 MCP 服务器及相关活动，以识别需要调查的工具。该能力处于预览。

这些更新建立在 Agent 365 现有的清单和管理控制之上，支持组织在部署更多智能体时持续治理。

[**了解这项更新的更多信息。**](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753)

Microsoft Agent 365 正在增加能力，帮助 IT 管理员监控和管理 AI 智能体及其使用的工具。新的操作中心预计于 12 月进入私人预览，将帮助管理员识别不活跃的智能体和没有所有者的智能体。Agent Map 的新能力处于预览，将帮助识别执行相似工作的智能体。新的控制现已正式可用，让管理员管理哪些用户和组可以访问插件和技能。预览中的其他功能提供更多方式来监控和控制 AI 智能体及其连接的工具，包括 MCP 服务器。

#### Microsoft Agent 365 新能力帮助最大化 AI 投资价值

即时摘要：

Microsoft Agent 365 正在扩展其业务价值能力，帮助 IT、业务和安全领导者优化 AI 支出并把投资转化为业务影响。现已在 Frontier 预览中提供的 **Agent 365 Business Analytics** 帮助领导者了解 AI 投资在何处创造价值。其他增强扩展了跨 Microsoft 和第三方智能体成本与结果的报告，并提供帮助提高效率、最大化 AI 投资价值的建议。

[**了解这项更新的更多信息。**](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753)

Microsoft Agent 365 正在增加业务分析能力（现已在 Frontier 预览中提供），帮助 IT、业务和安全领导者了解其 AI 投资的价值。扩展的报告覆盖跨 Microsoft 和第三方智能体的成本与结果，并提供建议，帮助组织提高效率并最大化业务影响。

### Codename MDASH

#### Codename MDASH：新的智能体化代码安全系统进入预览

即时摘要：

**Codename MDASH，微软的智能体化代码安全系统**，现面向符合条件的组织提供预览。它增加了新能力，将帮助安全和工程团队基于经过验证的发现开展工作。AI 模型的进步正在改变漏洞被发现和利用的方式。

Codename MDASH 在四阶段流水线中使用 100 多个专业 AI 智能体。它将绘制攻击面、扫描代码、通过智能体辩论验证发现、去除重复项，并在可能时用触发输入复现发现。

Codename MDASH 的新能力包括：

- **质量改进：** 减少低质量结果和误报，使团队能够减少分诊时间，把更多时间用于可处理的漏洞。
- **仓库分片（Repository sharding）：** 通过把代码库划分为逻辑单元来分析大型仓库，每次扫描使用更少的 token。
- **进度可见性：** 让扫描阶段、已完成工作、已用时间和结果可用性更可见，以便更好地了解扫描进度。
- **更广泛的 MAI Cyber 模型支持：** Codename MDASH 现在支持更多 MAI Cyber 模型家族成员，包括 MAI Cyber 1.1 Flash，并将在评估测试完成后使用 MAI-Cyber-2，在保持安全发现质量的同时提高效率。

[**了解这项发布的更多信息**](https://aka.ms/perceptionignite)。

Codename MDASH 是微软的智能体化代码安全系统，现面向符合条件的组织提供预览。100 多个专业智能体绘制攻击面、扫描代码、通过辩论验证发现、去除重复项，并在可能时复现漏洞。新的质量控制、仓库分片和更清晰的进度报告减少了误报和 token 使用，而更广泛的 MAI Cyber 模型支持在保持已验证结果的同时提高扫描效率。

### Defender

#### 集成安全运营中心正式可用，漏洞屏蔽进入预览

即时摘要：

**集成安全运营中心（Integrated Security Operations Center，ISOC）** 的核心能力已正式可用。安全信息和事件管理（SIEM）能力的完整范围以及包含的 90 天 Defender 数据保留现已进入预览。

ISOC 将把 SIEM 和威胁保护结合起来，为智能体化 SOC 提供基础，让人和智能体拥有共同的基础来观察、理解并在整个环境中采取行动，使网络技术栈作为一个系统运作。

此外，**漏洞屏蔽（vulnerability shielding）** 将把 Defender 中的攻击干扰从遏制受损资产扩展到预判和屏蔽漏洞。它将成为新网络技术栈中的一个执行器，并以预览形式提供。新的屏蔽能力将通过自主向已知存在漏洞的系统部署有针对性的临时控制，帮助组织在环境遭受活跃攻击期间提供保护。这将防止攻击者在系统尚未修补时利用活跃漏洞，为防御者争取更多时间应用永久修复。

[**了解这项发布的更多信息。**](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/ignite-2026-whats-new-in-microsoft-defender--sentinel/4569975)

Microsoft 集成安全运营中心（ISOC）的核心能力现已正式可用，为人与智能体提供共同基础，统一威胁保护与安全信息和事件管理（SIEM）工作流。完整的 SIEM 能力和包含的 90 天 Defender 数据保留处于预览，同时还有漏洞屏蔽——一项新的攻击干扰能力，可在活跃攻击期间自主向已知存在漏洞的系统应用有针对性的临时控制，为防御者争取时间部署永久补丁。

#### Microsoft Defender 扩展对本地 AI 智能体的运行时保护

即时摘要：

通过在 Windows 上**扩展对本地 AI 智能体的运行时保护**，Microsoft Defender 正在帮助组织在 AI 智能体跨端点运行时检测并阻止恶意指令。

- **Windows 上的智能体原生运行时保护**已面向 Claude Code、GitHub Copilot CLI、GitHub Copilot 应用、Claude Desktop (Code)、VS Code GitHub Copilot 扩展和 VS Code Claude Code 扩展正式可用。
- **Windows 上基于网络的运行时保护**已面向 Open Claw、Ollama Desktop、ChatGPT Classic 和 ChatGPT Desktop (Chat) 正式可用。

本地 AI 智能体可以使用用户的访问权限读取文件、与工具交互并采取行动；当智能体处理的内容中隐藏的恶意指令可能影响其采取非预期操作时，就会产生风险。Defender 会扫描本地 AI 智能体的调用以发现这些威胁，并借助网络 DLP、Microsoft Entra 和 Microsoft Purview 把保护扩展到数据和访问，帮助防止敏感数据在网络中被暴露或外泄。运行时保护可以在 Defender 或 Microsoft Intune 门户中配置，选择审计或阻止模式。

这些更新共同帮助安全团队在智能体成为日常工作一部分时保护本地 AI 智能体、敏感数据和访问。本地 AI 智能体的运行时保护将面向 Defender for Endpoint P2 客户提供。

[**了解这项发布的更多信息。**](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/ignite-2026-whats-new-in-microsoft-defender--sentinel/4569975)

Microsoft Defender 现在为 Windows 上的一系列本地 AI 智能体提供正式可用的运行时保护，包括 GitHub Copilot、Claude、ChatGPT、Open Claw 和 Ollama 体验。它扫描智能体调用以发现隐藏的恶意指令，并与网络 DLP、Microsoft Entra 和 Purview 协作保护数据和访问。Defender for Endpoint P2 客户可以通过 Defender 或 Intune 以审计或阻止模式配置控制。

#### Microsoft 威胁情报新增零日威胁和新兴威胁洞察

即时摘要：

Microsoft Defender 中的威胁情报将新增零日与新兴威胁体验，以预览形式提供，旨在帮助安全团队更早发现最紧迫的威胁，并更快理解它们。

零日攻击在修复可用之前利用软件缺陷，使组织几乎没有预警。新兴威胁是情报仍在演变中的新威胁或快速发展中的威胁。有关这些威胁的信息往往分散在单独的文章、报告、遥测和事件中，使安全团队难以快速获得一个清晰、有时间敏感性的整体图景。随着 AI 提高攻击的速度和覆盖范围，防御者需要更快的方式了解哪些威胁对自己最重要。这些新能力内置于 Microsoft Defender 中改版后的威胁情报体验，将把零日与新兴威胁推到前台：

- **零日与新兴威胁标签：** 关于零日和新兴威胁的威胁情报内容将被清楚标注，使其从其他威胁情报文章中脱颖而出。
- **更新的威胁情报概览和威胁分析文章：** 新的零日小组件和最新威胁视图将在 Microsoft Security Research 发现新的零日和新兴威胁研究后不久加以突出展示。安全团队将能够按行业和地区筛选，聚焦于与自己最相关的威胁。
- **电子邮件通知：** 安全团队将能够注册以通过电子邮件接收零日和新兴威胁更新。
- **保护验证：** 安全团队现在可以从威胁分析文章运行 Perception 中的「防御某威胁」剧本（"Protect against a threat"），检查现有覆盖情况并创建针对其环境定制的检测，补充内置保护。

[**了解这项更新的更多信息。**](https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/)

Microsoft Defender 正在预览零日与新兴威胁体验，把紧迫、快速变化的情报汇入一个按优先级排列的视图。新标签、小组件、行业和地区筛选、更新的分析文章和电子邮件警报帮助团队更早识别相关威胁，而 Microsoft Perception 剧本则验证现有保护并创建针对特定环境的检测，以补充内置防御。

#### 新投入降低本地部署安全风险

即时摘要：

一项新的**本地部署安全计划（on-premises security initiative）** 即将在 Secure Now 中提供指导，从受支持的 Exchange Server、SharePoint Server 和 Skype for Business Server 工作负载开始。该计划旨在帮助组织了解其最重要的风险、把符合条件的工作负载迁移到 Microsoft 365，并更好地保护需要保留在本地的关键系统。

该计划汇集安全指导、迁移支持和产品投入，使组织能够减少本地部署足迹，同时加强其保留的系统。该计划的关键部分是**本地基线安全模式（On-Premises Baseline Security Mode）**，旨在把更多微软推荐的安全设置内置到受支持的服务器产品中，减少手动设置和持续维护。

这项工作将改善三个方面：更快交付安全更新并帮助其到达已连接的服务器；让更安全的配置更容易建立和维护；在面对新兴威胁时应用临时保护，直到永久更新可用。

部分保护和指导现已可用，包括受支持范围内的安全更新、加固指导、健康工具和紧急缓解能力。其他能力将随时间推出，可用性因产品和工作负载而异。

微软继续建议把符合条件的工作负载迁移到 Microsoft 365，以获得云安全和韧性。对于必须留在本地的系统，组织现在就可以采取行动：使用受支持的版本、及时应用更新、启用可用的保护，并确认恢复计划已就绪。

[**了解这项发布的更多信息**](https://aka.ms/OnpremSecInitiativeBlog)。

微软正在为受支持的 Exchange Server、SharePoint Server 和 Skype for Business Server 工作负载启动本地部署安全计划。指导、迁移支持以及未来的本地基线安全模式，可以帮助组织减少服务器足迹、建立更安全的默认设置、加快更新，并针对新兴威胁应用临时保护。微软继续建议把符合条件的工作负载迁移到 Microsoft 365，并及时更新和加固必须留在本地的系统。

### Entra

#### Microsoft Entra 为智能体 AI 时代扩展安全身份与访问

即时摘要：

Microsoft Entra 正在推出新能力，帮助组织在每一次 AI 交互中保持可见性、控制和保护，同时在整个资产中发现、排序并降低身份安全风险。

##### **Entra Agent ID**

- **面向已发现本地智能体的智能体 ID** 处于预览，将自动为已发现的本地智能体分配智能体 ID，首先从 GitHub Copilot CLI 和 Claude Code 开始，以区分智能体与人的活动，并帮助保护其访问。
- **面向 Microsoft 云智能体的智能体 ID** 处于预览，将把智能体 ID 扩展到 Microsoft Autopilot 智能体，使管理员能够保护其身份和对资源的访问。

##### **Entra ID**

- **Microsoft MCP Server for Enterprise**（正式可用）：智能体和应用通过受控的、基于权限的接口，以自然语言访问 Microsoft Entra 数据。
- **条件访问策略计划（Conditional Access policy plans）** 处于预览，将通过一次表达访问意图并在各类身份上一致执行细粒度控制，简化规模化的策略管理。
- **高保障凭据（High assurance credentials）** 处于预览，将通过覆盖账户生命周期的验证来加强身份保障，包括入职、高风险凭据注册、特权访问和账户恢复，并具备凭据来源证明。
- **Microsoft Entra Backup and Recovery Premium** 处于预览，将通过 30 天备份保留和与 Microsoft 365 Backup 的集成来提升韧性。
##### **Entra Tenant Governance**

- **跨租户配置管理**处于预览，将通过单一管理窗格体验在各租户间部署、监控和执行资源配置，保持一致的身份和安全配置。

##### **Entra ID Governance**

- **Privileged Identity Management** 处于预览，将通过即时角色和组激活降低权限滥用和未授权访问的风险，同时通过 MyAccess、安全的 Azure VM 连接以及对常设访问和特权会话的更强控制，实现最小权限访问。
- **动态成员组（Dynamic membership groups）** 处于预览，将通过 MemberOf Next 和 Transitive Reports To 能力减少手动组维护。

##### **Entra Global Secure Access**

Microsoft Entra Global Secure Access 统一 Internet Access 和 Private Access，把身份感知的零信任控制扩展到私有应用、互联网、SaaS、AI 和智能体。

- **智能体流量获取（Agentic traffic acquisition）**（正式可用）：通过有选择地获取智能体流量，改善可见性和策略执行。
- **本地智能体**处于预览，将获得对本地智能体、目标、MCP 服务器和资源的网络可见性和控制。
- **MCP 防火墙**处于预览，将控制对 MCP 服务器、工具、资源、提示、协议和传输的访问。
- **未批准智能体（Unsanctioned agents）** 处于预览，将通过 Agent 365 协调 Intune、Defender 和 Global Secure Access 策略。
- **自适应访问**处于预览，将应用网络策略并考虑不断变化的风险。

##### **Entra External ID**

- **改进的客户身份体验**（预览）：灵活登录体验，包括应用原生身份验证、托管登录选项、AI 辅助开发和增强的安全控制。

[**了解这项发布的更多信息**](https://aka.ms/ignite/entra)。

Microsoft Entra 正在为人、智能体和跨租户环境扩展身份、访问和网络能力。预览中的智能体 ID 将区分本地智能体和 Autopilot 活动。新的治理、备份、特权访问、组和凭据功能将加强韧性和身份保障。Global Secure Access 中正式可用的智能体流量获取改善了可见性和策略执行。正式可用的 Microsoft MCP Server for Enterprise 提供基于权限、使用自然语言的 Entra 数据访问。

#### AI 就绪计划（AI Readiness Initiatives）加强安全基础

即时摘要：

Perception 中新的 AI 就绪计划将于 1 月进入预览，帮助组织跟踪关键安全工作随时间的进展。这些计划与 Secure Now 中列出的优先事项保持一致，帮助加强安全基础，并持续降低身份、设备、数据、端点、AI 智能体、代码、网络等方面的暴露风险。

每项新计划都将为智能体和安全团队提供一个共同、结构化的计划，用于弥合其安全基础中某一领域的差距。进展将使用实时租户数据衡量，为团队提供差距已弥合、暴露风险已下降的证据。

- **修补与漏洞管理：** 将评估、屏蔽并协调优先漏洞的修补。
- **现代化身份验证：** 将通过引导抗钓鱼通行密钥（passkeys）的推广，加强管理员身份安全。
- **智能体发现与治理：** 将帮助组织加强其 AI 智能体的安全基础。

修补与漏洞管理计划是这种方法在实践中如何运作的一个例子，它把智能体和安全团队结合起来，持续管理在每月 Windows 更新中发现的漏洞。当新漏洞被披露时，智能体可以评估暴露情况、识别组织环境中最重要的漏洞、在适当情况下应用屏蔽，并通过 Microsoft Intune 协调永久修复。终结点管理员保持对部署的控制，而智能体帮助验证风险已降低。

[**了解这项更新的更多信息**](https://aka.ms/exposurenewsignite)。

Microsoft Perception 中新的 AI 就绪计划将于 1 月进入预览，为智能体和安全团队提供共同、可衡量的计划，以加强身份、设备、数据、端点、智能体、代码和网络等方面的基础。首批计划覆盖漏洞管理、抗钓鱼身份验证和智能体治理，使用实时租户数据衡量进展。对于每月 Windows 漏洞，智能体可以评估暴露情况、应用屏蔽并协调 Intune 修复，而管理员保留部署控制权。

### Intune

#### Microsoft Intune 帮助保护 AI 采用安全并降低端点风险

即时摘要：

Microsoft Intune 正在推出处于预览的**本地 AI 智能体治理**新控制。IT 将能够通过 Microsoft Agent 365 发现受管设备上运行着哪些智能体，把装有未批准智能体的设备标记为不符合 Intune 软件合规策略，并应用 Microsoft Entra 条件访问，阻止这些设备访问公司数据。

对于已批准的智能体，Intune 策略将通过 Microsoft Execution Containers 界定它们可以访问什么、可以做什么。Microsoft Entra Global Secure Access 将把这些保护扩展到网络，对本地智能体如何访问互联网、SaaS 和私有资源提供细粒度控制。

这些能力共同让 IT 了解端点上的智能体，并能够根据风险检测采取行动，使组织在采用 AI 智能体时不必在创新和控制之间做选择。

**[了解这项发布的更多信息。](https://techcommunity.microsoft.com/blog/microsoftintuneblog/what%E2%80%99s-new-in-microsoft-intune-at-ignite/4570003)**

面向本地 AI 智能体治理的新 Microsoft Intune 控制处于预览。IT 将能够通过 Microsoft Agent 365 发现受管设备上运行着哪些智能体，把装有未批准智能体的设备标记为不符合 Intune 策略，并使用 Microsoft Entra 阻止这些设备访问公司数据。面向已批准智能体的策略通过 Microsoft Execution Containers 界定边界。Microsoft Entra Global Secure Access 增加了对互联网、SaaS 和私有资源连接的细粒度网络控制。

### Perception

#### Microsoft Perception 新能力现已可用

即时摘要：

**Microsoft Perception**（原 Project Perception）现已正式可用，包括 7 月宣布的智能体和剧本。

Microsoft Perception 使用专业智能体和多智能体工作流执行常见安全任务。这些智能体有三种角色：红队智能体从攻击者视角寻找弱点。蓝队智能体分诊警报、调查攻击、检测威胁并创建威胁情报。绿队智能体帮助确定安全弱点的优先级，让团队知道该关注哪里。每个智能体执行专门任务，剧本则编排它们的能力以应对更广泛的安全挑战。

新能力包括：

- **更广泛的分诊与调查：** Triage Agent 现在覆盖典型 Microsoft Defender 队列中约 80% 的警报。Investigation Agent 可以跨端点、身份、电子邮件、Active Directory 和云资源追踪攻击，并建议按优先级排列的响应操作。
- **扩展的第三方支持：** Triage Agent 现在处理 AWS 和 Salesforce 的警报与事件。Investigation Agent 可以对 AWS 和 Okta 数据进行推理。Detection Authoring Agent 可以对 AWS、Salesforce 和 Okta 数据进行推理。同样，Threat Intelligence Agent 可以把外部研究转化为结构化的威胁画像和建议操作。
- **新的检测剧本：** 检测新兴威胁剧本使用结构化威胁情报创建租户感知的 Kusto 查询语言（KQL）检测建议，针对历史数据进行测试，并建议调优。
- **经授权的 Web 应用测试：** Web App Pen Test Agent 处于预览，将通过 Run web pen test 和 Protect web app 剧本验证可利用的弱点，并提供证据和修复指导。
- **仓库规模的漏洞发现：** Codename MDASH 识别并验证代码漏洞，支持跨 Microsoft Defender、GitHub、Azure DevOps、CI/CD 和 Microsoft Security Exposure Management 的开发者和安全工作流。
- **智能体化风险优先级排序：** Posture Prioritization Agent 以及用于规划态势修复和防御威胁的剧本，将帮助团队聚焦关键暴露面并规划协调保护。
- 预览中的 **Reduce exposure risk** 剧本将调用 Risk Reduction Agent，评估可用于降低风险的路径并推荐正确的响应。当永久修复准备好时，该智能体可以通过 Microsoft Intune 协调修补，由 IT 保持对部署的控制。当无法立即修补或修补可能中断业务时，该智能体可以通过提供有针对性的保护来帮助屏蔽漏洞，同时团队推进永久修复。
- **保护 AI 智能体和剧本：** 智能体化安全的扩展将帮助团队调查并降低 AI 智能体风险。Microsoft Perception 和 Microsoft 365 共同把信号、上下文和注册表数据带入智能体格局的一致视图。剧本把这种理解转化为按优先级排列的修复和协调响应，帮助团队在智能体行为与访问权限演变时遏制风险并作出响应。私人预览中。
- **SOC 工作流中的剧本：** 团队可以自动触发剧本，或直接从 Microsoft Defender 启动剧本。
- **API 优先的可扩展性：** API 和 Model Context Protocol 支持使组织能够从 ITSM、SIEM 和 SOAR 工具启动剧本，并把智能体会话和产物返回到现有工作流。
- **治理与成本透明度：** 最小权限访问、审批控制、审计日志、使用量视图和成本计算器，帮助组织治理智能体活动并规划支出。

[**了解这项发布的更多信息**](https://aka.ms/perceptionignite)**。**

Microsoft Perception 现已正式可用，通过剧本编排专业的红队、蓝队和绿队安全智能体，用于测试、调查、检测、分诊和确定弱点优先级。扩展后的智能体覆盖典型 Defender 警报的约 80%，跨 Microsoft 和第三方环境追踪攻击，创建租户感知的检测建议，并验证可利用的弱点和代码漏洞。新的预览增加了 Web 应用测试、仓库规模漏洞发现、智能体化风险优先级排序、API 优先的可扩展性、新剧本等。

### Purview

#### Microsoft Purview 帮助加速 Copilot 部署并保护智能体交互

即时摘要：

随着企业越来越多地使用 AI 处理公司信息，它们需要知道哪些数据是敏感的、谁可以访问，以及如何防止数据被不当共享。Microsoft Purview 的新能力处于预览，将通过以下方式应对这些挑战：

- **更快实现保护**，通过对敏感数据进行高精度、可扩展且最新的分类和标注。Microsoft Purview 将改进自动分类和标注敏感信息（如财务记录、个人信息和机密业务文档）的方式，使保护保持最新，同时减少手动调整的需要。
- **加速 Copilot 采用：** Copilot 的数据丢失防护能力将通过基于依据的保护得到加强，即使文件未标注，也能阻止 Copilot 引用含有敏感信息的文件。它还将把提示保护扩展到附件、链接文件和文本。
- **扩展 AI 智能体的安全能力：** Microsoft Purview 将把数据安全能力扩展到 Windows 上运行的端点智能体，帮助组织控制 AI 智能体可以访问和共享哪些数据。安全团队将能够对单个智能体或智能体组应用保护，并帮助防止敏感信息通过其对话和与其他工具的连接被暴露。

[**了解这项发布的更多信息**](https://aka.ms/SecureData/Blog)。

Microsoft Purview 正在预览对敏感数据的更快保护、面向 Copilot 的更强数据丢失防护能力，以及面向 AI 智能体的扩展安全能力。这些能力包括对敏感数据更精确、可扩展且最新的分类和标注。数据丢失防护将得到加强，即使文件未标注，也能阻止 Copilot 引用含有敏感信息的文件。面向 Windows 端点 AI 智能体的扩展安全能力将帮助安全团队防止敏感信息通过智能体对话和与其他工具的连接被暴露。

## Windows

即时摘要：

随着智能体从试点走向生产，组织要求对智能体可以做什么进行清晰的治理，并要求在 AI 运行位置上有更多选择。新的**进程容器控制**将为 IT 提供更细粒度的控制，以在 Windows 设备上隔离和治理智能体。混合智能让组织能够在最能创造价值的地方运行 AI，更新覆盖 **Windows** 客户端、**Windows 365 云 PC** 和 **Windows Server**，以及 **Windows 上的 Copilot** 中利用本地上下文的新能力。建立在安全基础之上，新的 **Windows** 和 **Intune** 安全改进使设备、应用和智能体保持安全、最新并处于 IT 控制之下。

新的进程容器控制将帮助 IT 在 Windows 设备上隔离和管理智能体。Windows 客户端、Windows 365 云 PC 和 Windows Server 的更新，以及 Windows 上 Copilot 中利用本地上下文的新能力，将帮助组织治理和管理 AI。新的 Windows 和 Intune 安全改进将帮助设备、应用和智能体保持安全、最新并处于 IT 控制之下。

### Windows

#### Windows 上的 Copilot 在文件操作、PC 诊断和搜索方面的改进

即时摘要：

Windows 上 Copilot 的新能力将利用设备上的上下文进行故障排查和文件管理，并从任务栏更便捷地访问 Copilot。所有更新均处于预览，包括：

##### **Copilot 中的本地文件管理**

Copilot 将支持对 Windows PC 上的文件进行 AI 辅助的文件管理。用户将能够用平实语言描述查找、整理、移动、复制或重命名文件等任务，Copilot 将帮助执行这些操作。

##### **Copilot 中的本地 PC 诊断**

Copilot 将能够使用 Windows 诊断信息帮助诊断 Windows PC 上的问题，更好地理解问题的可能原因，并提供清晰的解释和建议的下一步。

##### **在新的 Windows 搜索体验中更便捷地访问 Copilot**

作为 Windows 新搜索体验的一部分，用户将能够直接从任务栏访问 Copilot，提出问题、获得受支持操作的帮助，并查找整个组织内的信息。用户可以通过 Windows 设置选择启用 Windows 搜索中的 Copilot，IT 管理员可以通过策略在整个组织内管理该体验。

[**了解这项发布的更多信息**](https://aka.ms/WindowsAtIgnite2026)。

Windows 上 Copilot 的新能力将利用设备上的上下文进行故障排查和文件管理，并从任务栏更便捷地访问 Copilot。用户将能够通过向 Copilot 发出自然语言请求来管理本地文件，并在新的 Windows 搜索体验中直接从任务栏访问这个 AI 助手。

#### Windows 365 在 Direct Stream、Windows 365 管理助手等方面的全新能力

即时摘要：

目前已有数万个组织使用 Windows 365 云 PC 来提供设计上安全、易于管理的工作空间，这些新增强进一步简化了体验：

- **Direct Stream**：Windows 365 和 Azure Virtual Desktop 背后的云流媒体技术带来了现已面向云 PC 用户正式可用的增强，可在多变的网络上实现更可靠的连接和高保真多媒体体验，支持全天生产力。此外，通过与 NVIDIA 合作实现的 Direct Stream 增强，启用 GPU 的云 PC 用户将能够在图形密集型应用中工作，即使在较差的网络条件下也能以低延迟支持最多两路 4K 60 帧/秒串流（明年年初在部分区域预览）。
- **Windows 365 管理助手：** Microsoft Intune 中由 AI 驱动的体验，现处预览，将使 IT 管理员能够更轻松地监控云 PC 健康状况、调查问题、识别可能原因并加快故障排查。
- **Windows 移动应用管理（MAM）：** 支持对 Windows 应用应用安全和数据保护策略，同时允许访问云 PC 的 Windows 设备保持非托管状态。现处预览。
- **基于上下文的重定向：** 支持使用 Microsoft Entra 身份验证上下文，根据每个连接的信任级别动态允许或限制剪贴板、驱动器、打印机和 USB 重定向。现已正式可用。

[**了解这项发布的更多信息**](https://aka.ms/W365Ignite26Blog)。

**[下载与这项发布相关的视觉素材。](https://msftglobalcomms-my.sharepoint.com/:f:/g/personal/global_msftglobalcomms_onmicrosoft_com/IgAJqdt1iULvTqss9Pp2X7OsAZLyWlsaG6Et2trELnog9gM?e=AqG3uO)**

Windows 365 正在改进云 PC 的性能、管理和数据保护。正式可用的 Direct Stream 增强加强了连接性和多媒体质量。从明年年初在部分区域开始，得益于与 NVIDIA 的合作，用户可以在 GPU 云 PC 上更流畅地运行图形密集型应用。其他更新包括用于监控云 PC 健康状况的 Intune AI 助手、Windows 应用的新安全和数据保护能力，以及基于 Microsoft Entra 身份验证上下文的基于上下文的重定向。

#### 新的 Windows 和 Microsoft Intune 能力

即时摘要：

微软正在推出新的 Windows 和 Microsoft Intune 能力，旨在帮助组织把 AI 从试点带入日常工作，同时让设备、应用和 AI 智能体保持安全、最新并处于 IT 控制之下。

**Windows 基线保护**（私人预览）将应用并维护关键安全设置，使设备从启动之时起就受到保护，减少攻击面并执行以硬件为根的安全和完整性功能。新的 **Windows 端点安全平台（Windows Endpoint Security Platform）** 现已正式可用，为经批准的安全产品提供更安全的方式来保护设备，同时提高可靠性。

微软还在把 Windows 管理扩展到 PC 之外，涵盖服务器、应用和新的 Windows 体验。Microsoft Intune 和 Windows Autopatch 将支持**面向类客户端场景的 Windows Server 2028**（私人预览），与 PC 一起管理；企业应用管理（Enterprise App Management）将**把自动更新扩展到所有 Windows 应用，而不仅是 IT 部署的应用**（私人预览）。**声明式设备管理**（预览）将确保当 IT 定义期望结果后，Windows 会努力应用并维护它。

新的**体验控制（experience controls）**（私人预览）将让 IT 团队有时间按自己的节奏，借助推荐的控件评估和引入即将推出的 Windows 体验和功能。

Windows Autopatch 中新增的 **操作系统可靠性报告**（私人预览）将呈现可靠性洞察，使 IT 能够更快、更有信心地修补，保持合规，了解 Windows 停止错误的趋势，发现反复出现的故障模式，并准确看到受影响的设备。这些能力共同把安全、管理和智能辅助带入更统一的体验。

[**了解这项发布的更多信息**](https://aka.ms/WindowsAtIgnite2026)。

新的 Windows 和 Microsoft Intune 能力包括更新的基线保护和一个新的端点安全平台。Intune 和 Windows Autopatch 将支持 Windows Server 2028，自动更新将扩展到所有 Windows 应用，而不仅是 IT 部署的应用。其他更新包括声明式设备管理、面向 IT 的新控制，以及 Windows Autopatch 中用于可靠性洞察的操作系统可靠性报告。

#### Windows 365 for Agents 扩展到 Microsoft Foundry，推出持久云 PC

即时摘要：

随着使用计算机的智能体日益普及，IT 越来越需要大规模提供安全、受管且可靠的工作空间，不仅为员工，也为在组织中工作的智能体。**Windows 365 for Agents** 正在引入新能力，以安全地大规模运行企业级 AI 智能体。这对没有 API 的遗留业务应用的组织尤其有用。

- Windows 365 for Agents 现在**符合 Copilot 额度（Copilot Credits）的适用范围**——Copilot 额度是符合条件的 Microsoft 服务按使用量计费的通用货币——从而实现统一的 AI 计费、治理、报告和成本管理体验。
- 智能体制作者可以通过 Microsoft Copilot Studio 以及 Microsoft Foundry 把 Windows 365 for Agents 带入其智能体体验。在 Copilot Studio 中，Windows 365 for Agents 作为标准执行框架（Standard harness）中的计算机使用工具提供，并将在 12 月在 Microsoft Copilot 执行框架中进入预览。明年年初的预览中，Foundry 构建者将能够使用 Windows 365 for Agents 的 Model Context Protocol (MCP)，使智能体能够在受治理的云 PC 上执行计算机使用任务。
- 使用 Windows 365 for Agents 云 PC 的智能体将能够**使用智能体身份访问本地应用**（预览），把自动化扩展到没有 API 的遗留业务应用。
- Windows 365 for Agents 将在 Frontier 中**支持持久云 PC**（预览），帮助 IT 管理员部署、管理和保护始终在线的个人智能体。这将支持长时间运行的业务流程自动化，同时保持企业安全和合规。

[**了解这项发布的更多信息**](https://aka.ms/W365Ignite26Blog)。

**[下载与这项发布相关的视觉素材。](https://msftglobalcomms-my.sharepoint.com/:f:/g/personal/global_msftglobalcomms_onmicrosoft_com/IgD9mkHr64w1T6W7Yvv_-FgLAc8umkBrTpBIDl_IQ6SCtAI?e=DINHs0)**

Windows 365 for Agents 现在符合 Copilot 额度的适用范围，可实现统一的 AI 计费、治理、报告和成本管理体验。该平台在 Copilot Studio 的标准执行框架中提供，并将在 12 月在 Microsoft Copilot 执行框架中进入预览。明年年初，Foundry 构建者将能够在预览中使用 Windows 365 for Agents 的 Model Context Protocol。Windows 365 for Agents 云 PC 上的智能体将能够使用智能体身份访问本地应用，把自动化扩展到没有 API 的遗留应用。Windows 365 for Agents 还将支持持久云 PC，帮助 IT 管理员部署、管理和保护始终在线的个人智能体。

#### Windows 扩展本地和混合能力

即时摘要：

Windows 现在通过增加本地模型执行、混合编排以及扩展的云 PC 和服务器选项，支持更广泛的 AI 工作负载部署位置。

这些更新共同为本地 PC、云 PC 和基于服务器的环境中的 AI 工作负载提供更多执行路径。更新包括：

- **Windows 365 云 PC 支持运行最新的本地 AI 模型**，包括用于开发和 AI 工作负载的最多 32 vCPU 和启用 GPU 的云 PC。此能力已正式可用。借助 Foundry Local，开发者可以直接在规格合适的云 PC 上运行兼容的 AI 模型，对于需要更多计算容量或性能的工作负载，可按可预测的订阅成本使用。
- **带 AVD Hybrid 的 Windows Server 2025**（私人预览）将支持通过 Windows Server 和 Azure Virtual Desktop 基础设施管理的多用户 AI 开发环境。组织将能够在其直接管理的环境中运行受支持的模型，而不必完全依赖云托管的推理。

[**了解这项发布的更多信息**](https://aka.ms/WindowsAtIgnite2026)。

Windows 现在通过增加本地模型执行、混合编排以及扩展的云 PC 和服务器选项，支持更广泛的 AI 工作负载部署位置。更新包括 Windows 365 云 PC 支持运行最新的本地 AI 模型，包括最多 32 vCPU 和启用 GPU 的云 PC。借助 Foundry Local，开发者可以直接在规格合适的云 PC 上运行兼容的 AI 模型。此外，带 AVD Hybrid 的 Windows Server 2025 将支持通过 Windows Server 和 Azure Virtual Desktop 基础设施管理的多用户 AI 开发环境。

#### Windows 推出帮助隔离和治理 AI 智能体的控制

即时摘要：

Windows 正在推出新的进程容器控制，提供组件对象模型（COM）和进程间通信（IPC）治理、细粒度网络策略和身份证明保护，使组织对智能体的运行方式以及其活动如何被隔离、观察和治理拥有更清晰的边界。

这些更新均处于预览，包括：

- **进程容器能力**将为每个运行的智能体或应用提供一个受保护的工作区，明确限制它可以与谁通信、可以访问哪些网络，以及如何证明自己的身份。这将降低智能体访问错误数据、冒充其他对象或影响设备其余部分的风险。
- **学习与宽松模式（learning and permissive mode）** 现已正式可用，将允许团队在全面执行限制之前观察智能体通常如何与系统服务通信。这将帮助管理员安全地创建策略，而不会在推广过程中破坏合法工作流。

[**了解这项发布的更多信息**](https://aka.ms/WindowsAtIgnite2026)。

Windows 正在推出新的进程容器控制，提供 COM 和 IPC 治理、细粒度网络策略和身份证明保护，使组织对智能体的运行方式以及其活动如何被隔离、观察和治理拥有更清晰的边界。进程容器控制将为每个运行的智能体或应用提供一个受保护的工作区，明确限制它可以与谁通信。新的学习与宽松模式将允许团队在全面执行限制之前观察智能体通常如何与系统服务通信。
