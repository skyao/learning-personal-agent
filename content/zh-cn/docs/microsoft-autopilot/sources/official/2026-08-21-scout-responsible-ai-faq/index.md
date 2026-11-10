---
title: "Microsoft Scout 负责任 AI 常见问题"
linkTitle: "文档：负责任AI问答"
date: 2026-08-21
originalTitle: "Responsible AI FAQ for Microsoft Scout"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [隐私, 安全, 模型]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-06-02"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：文档说明 Microsoft Scout 面向信息工作者和开发者，不适用于需要无人工审核即保证准确的场景，如法律文件、医疗决定或绕过批准流程的财务交易。评估围绕任务完成、响应质量以及安全与合规；已列出的限制包括误解模糊指令、搜索结果可能不准确、不验证用户自建 skill 等。数据方面，LLM 交互经 GitHub Copilot 处理，提示和内容可能传出 Microsoft 365，包括第三方模型提供方，而会话与记忆数据存放在用户的 OneDrive。文档称 Scout 不使用用户数据训练 AI 模型，外部内容（邮件、网页、Teams 消息）作为数据而非指令处理；生成内容未必继承敏感度标签。

**保留理由**：这是 Scout 数据流向 GitHub Copilot 及第三方模型提供方、记忆与会话存放位置，以及不用于训练的官方表述的出处。

---

Microsoft Scout 负责任 AI 常见问题

[本文为预发布文档，可能发生变更。]

重要

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能**提前访问** Microsoft Scout。Frontier 让你直接接触微软最新的 AI 创新。Frontier 预览受你客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是一项预览功能。
- 预览功能可能功能受限，也可能不会正式发布。这些功能在正式发布前提供，以便客户提前访问并提供反馈。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

本常见问题解答（FAQ）说明 Microsoft Scout 这一 AI 桌面应用的 AI 影响。

## 什么是 Microsoft Scout？

Microsoft Scout 是面向 Windows 和 macOS 的桌面 AI 应用，会代表你在你的文件、shell、浏览器和 Microsoft 365 数据之间采取行动。你用自然语言描述你需要什么，Microsoft Scout 就执行这项工作——读写文件、运行命令、控制浏览器、查询你的 Microsoft 365 账户，并在后台自主工作。Microsoft Scout 采取的每个动作都在对话中可见。敏感操作在执行前需要你的明确批准。

## Microsoft Scout 有哪些能力？

Microsoft Scout 可以：

- 读取、写入和搜索你的工作区目录中的文件。
- 通过三级权限系统（自动批准、提示、拒绝）运行 shell 命令、构建、测试和脚本。
- 使用 git、gh、curl 和 PowerShell 探索代码库、应用补丁、运行 linter，并调试失败。
- 自动化浏览器交互——导航页面、填写表单、拍摄快照、检查控制台日志和网络请求，以及上传文件。
- 用快速模式匹配工具搜索你的工作区。
- 在互联网上搜索实时信息。
- 启动专门的研究智能体，进行并行调查，提供详细发现和引文。
- 读取和管理你的电子邮件、日历、Teams 聊天、OneDrive 文件和会议。
- 使用 WorkIQ 跨 Microsoft 365 服务查询复杂问题。
- 创建和编辑 Word 文档、Excel 电子表格、PowerPoint 演示文稿、Loop 文档和交互式 HTML 制品。
- 按计划在后台自主运行（heartbeat 模式）。
- 执行按计划或按条件触发的自动化。
- 把复杂工作委派给专门的子智能体（explore、task、code review、research、general-purpose）。
- 跨对话记住偏好、决策和上下文。
- 搜索过去的会话历史，以回忆起先前的工作和决策。

在对话过程中，Microsoft Scout 会按需加载专门技能。

## Microsoft Scout 的预期用途是什么？

Microsoft Scout 面向希望在本机与 Microsoft 365 账户之间自动化任务的信息工作者和开发者。典型用例包括：

- 构建和测试软件项目（运行构建、测试、lint、调试失败）。
- 探索和编辑代码库（搜索文件、应用补丁、重构）。
- 自动化 Web 工作流（填写表单、从门户提取数据、与企业应用交互）。
- 管理 Microsoft 365 数据（起草和发送电子邮件、安排会议、整理文件）。
- 运行自主后台任务（收件箱分诊、日程监控、周期性报告）。
- 从非结构化输入创建结构化文档（会议记录 → 格式化报告，数据 → 电子表格）。

Microsoft Scout 不适用于需要在无人审核的情况下保证准确性的用例。例如法律文件、医疗决定，或绕过审批流程的财务交易。在批准向外发送、发布或共享信息的操作之前，始终审核 AI 生成的内容。仔细考虑让应用无需逐步批准即可执行某些操作的可选模式是否适合该用例。

## Microsoft Scout 如何评估，使用哪些指标衡量性能？

微软在多个方面评估 Microsoft Scout：

- **任务完成**：Microsoft Scout 是否成功执行了所请求的操作（例如创建文件、运行命令或发送电子邮件）。
- **响应质量**：其输出是否基于自然语言指令满足用户意图。
- **安全与合规**：持续评估，以确保 Microsoft Scout 在微软的负责任 AI 原则范围内运作。

## Microsoft Scout 有哪些局限，用户如何尽量减小这些局限的影响？

当前的局限包括：

- Microsoft Scout 可能误解模糊或过于宽泛的指令，导致采取不符合你意图的动作。
- 把 AI 生成的文档、消息和代码当作草稿。在发送、共享或部署之前始终审核内容。
- 在搜索你的工作区或 Microsoft 365 账户时，Microsoft Scout 可能产生不准确的信息，尤其是源数据不完整或过时时。
- 依赖关系众多的复杂多步任务可能无法总按预期完成，这会引入风险。
- Shell 命令受三级权限系统约束。危险或意料之外的命令可能被阻止或需要批准。
- Microsoft Scout 在你的工作区目录内运作。除非你明确授权，否则它无法访问该目录之外的文件。
- Microsoft Scout 依赖你现有的 Microsoft 365 权限。它无法访问你的账户无权使用的数据或服务。
- 微软不验证用户编写的自定义技能。请仔细审核自定义技能的输出，因为其质量取决于技能的编写方式。
- 后台模式（heartbeat 和 automations）使用的权限策略比交互式对话更严格。

要尽量减小这些局限：

- 提供清晰、具体的指令。包含你希望做什么以及在哪里的细节。较简单的任务更可能以更高准确度完成。彻底测试复杂或多步任务是否按预期完成。
- 在批准操作之前，审核所有生成的内容，例如代码、电子邮件、文档和消息。
- 如果 Microsoft Scout 方向不对，使用暂停和取消控件停止工作。
- 自定义 shell 权限，使其匹配你的工作流和安全要求。
- 把敏感目录或文件标记为访问前需要明确批准。
- 租户管理员和用户应仔细考虑何时适合使用不要求逐步批准的可选自主执行模式。只有在仔细审核任务、权限以及可能受影响的数据或系统之后，才将这些模式用于低风险场景。管理员可以为其组织禁用或限制此类模式。

## Microsoft Scout 如何处理操作批准？

在 Microsoft Scout 执行敏感操作之前——例如发送电子邮件、在 Teams 中发帖、运行写入磁盘或访问网络的命令，或修改自动批准模式之外的文件——它会显示批准提示。你有以下选项：

- **批准（Approve）**：允许该操作执行这一次。
- **始终允许（Always allow）**：批准，并把该模式加入未来操作的自动批准列表。
- **拒绝（Deny）**：阻止该操作。

对于某些操作，例如发送电子邮件或运行 shell 命令，Microsoft Scout 会在你批准前显示内容预览或确切命令。未经你明确同意，Microsoft Scout 不会执行敏感操作。

## Microsoft Scout 如何处理我的数据？

Microsoft Scout 在 Microsoft 365 和你的本机（以及在特定情况下，外部 AI 服务）的安全与合规边界内运作，具体取决于你的指令、权限和配置。

- **身份验证与访问控制**：Microsoft Scout 使用你现有的 Microsoft 365 凭据，并以适用于你账户的相同权限和访问控制运作。它只访问你的账户被允许使用的服务和数据。
- **租户隔离**：你的 Microsoft 365 数据隔离在你组织的租户内，受你组织现有的安全、合规和治理控制约束。
- **外部 AI 处理（GitHub Copilot）**：Microsoft Scout 中的 LLM 交互通过 GitHub Copilot 处理，后者按单独的条款运作。在这些情况下，提示、内容及相关数据可能被传输到 Microsoft 365 之外，包括传输到通过 GitHub Copilot 配置的第三方模型提供方。当数据通过 GitHub Copilot 处理时，某些 Microsoft 365 保护——例如数据驻留承诺、保留策略、敏感度标签强制执行、eDiscovery 和其他合规控制——不适用于该处理。
- **本地文件访问**：Microsoft Scout 可以根据你授予的权限，读取、写入和修改你本地设备上或你配置的工作区内的数据。除非你明确授权，否则它不会访问该目录之外的文件。
- **Shell 命令把关**：Shell 命令受你控制的三级权限系统约束。危险命令默认被阻止。
- **数据主体权利**：依照微软的隐私标准，支持访问、删除、更正和可移植性请求。
- **文件存储与记忆**：Microsoft Scout 创建的文件存储在你本机的工作区目录中。会话和记忆数据存储在用户的 OneDrive 中；OneDrive 会话数据和记忆留在你的租户内，受 Microsoft DPA 及你按 Purview 配置设定的标准 OneDrive 控制覆盖。自动化指令和工具输出存储在最终用户的设备本地，不受 M365 DPA 覆盖，受你的终结点管理和设备控制约束。
- **外部内容标记**：电子邮件、网页和 Teams 消息会被标记为外部内容，并作为数据而非指令处理，以防提示注入。
- **敏感度标签**：Microsoft Scout 可以识别并显示其访问内容关联的敏感度标签。但是，由 Microsoft Scout 生成或修改的内容在所有场景下未必自动继承或强制执行这些标签。用户在共享或存储内容前应应用适当的标签和控制。

Microsoft Scout 不使用你的数据训练 AI 模型。

## 哪些运营因素和设置支持有效且负责任的使用？

- Microsoft Scout 是面向 Windows 和 macOS 的桌面应用，受你组织的访问策略和许可约束。
- 在批准向外发送、发布或共享信息的操作之前，始终审核 AI 生成的内容。
- 如果 Microsoft Scout 偏离方向，使用对话控件（暂停、继续、取消）管理工作。
- 从 **设置** > **权限** 自定义 shell 权限，使其匹配你的工作流和安全要求。
- 把敏感目录或文件标记为访问前需要明确批准。
- 将 heartbeat 和自动化权限与交互式对话权限分开配置，以控制 Microsoft Scout 在你不在时可以做什么。
- 管理员可以通过 Intune 管理中心管理对 Microsoft Scout 的访问，包括为特定用户禁用访问，或控制整个组织内的部署。

## 相关内容

- [Microsoft Scout 负责任 AI 概述](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview)
- [Microsoft Scout 概述](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [Microsoft Scout 入门](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout)
- [Microsoft Scout 常见问题](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- [微软 AI 原则](https://www.microsoft.com/ai/responsible-ai)
