---
title: "为组织配置 Autopilot（Frontier）"
linkTitle: "文档：管理员配置"
date: 2026-11-17
originalTitle: "Configure Autopilot (Frontier) for your organization"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [开放与价格, 安全, 隐私, 模型]
products: [microsoft-autopilot]
updatedAt: "2026-11-17"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-17。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：面向管理员的配置文档：Autopilot 默认关闭，需让用户加入 Frontier、建立覆盖 Autopilot 的支出策略（按 Copilot Credits 计费），并在 Microsoft 365 管理中心激活 Autopilot (Frontier) 代理；每个启用用户可创建一个 Autopilot，初期仅限美国的合格客户。文档说明自动审查系统（第二个 AI 模型）按动作类型决定放行或需用户批准，付款与敏感浏览器步骤始终需批准。模型为 OpenAI 作为 Microsoft 子处理方提供的 GPT-6.1 Sol，关闭 OpenAI 后改用 Azure OpenAI 托管的 GPT-5.6 Sol。另列出记忆无法关闭、合规覆盖现状（eDiscovery、保留、法律保留不覆盖 Autopilot 会话；提示词 DLP 仍在部分租户测试），以及管理员用脚本导出用户 lobster.repo 的步骤。

**保留理由**：首次给出云端 Autopilot 的管理员视角：激活向导、支出策略、实例管理、合规缺口和数据导出，旧 Scout 文档（Intune 部署桌面应用）与 MC1479277 都没有覆盖这些细节，也首次写明模型型号与回退模型。

---

为组织配置 Autopilot（Frontier）

[本文为预发布文档，可能会变更。]

重要

- 访问 Autopilot（Frontier）需要加入适用的 **[Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)**，并完成预览分配与参与条款。仅加入 Frontier 并不会启用每一项预览功能。Frontier 预览受你客户协议中适用的预览条款约束，其可用性和能力可能变化。
- 此功能处于预览阶段。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布之前提供，以便客户抢先体验并提供反馈。
- 更多信息，请访问我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

本文面向为本组织准备 Autopilot 的管理员。Autopilot 默认关闭。要开启它，你需要让用户加入 Frontier、建立覆盖 Autopilot 的支出策略，并在 Microsoft 365 管理中心激活 **Autopilot (Frontier)** 代理。每一步都是必需的；仅启用 Frontier 并不会让 Autopilot 可用。

Autopilot 作为 Microsoft Copilot 的一部分在云端运行。每个已启用的用户可创建一个 Autopilot。产品能力见 [Autopilot 概述](https://learn.microsoft.com/en-us/copilot/autopilot/overview)。

## 先决条件

开始之前，请确保：

- 使用具有相应 Microsoft 365 管理员角色的组织账户，且该角色对应你打算更改的设置。
- 确认目标用户拥有 Microsoft 365 Copilot 许可证和工作账户。初期仅限美国的合格客户使用。
- 确认你的组织具备必需的 Microsoft 安全能力，并查看推荐的能力。更多信息见[安全要求与建议](https://learn.microsoft.com/en-us/copilot/autopilot/requirements#security-requirements-and-recommendations)。
- 确定应获得 Autopilot 的用户或组。
- 为 Copilot Credits 选择计费方式，例如按用量付费的 Azure 订阅或预付 Copilot Credits。
- 查看适用的预览条款、已批准的 AI 提供方，以及允许的数据与工作流。

当前的 Frontier 角色与先决条件见[开始使用 Microsoft Frontier 计划](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/get-started-frontier)。

## 为目标用户启用 Frontier

使用 Microsoft 365 管理中心管理 Frontier 访问权限。

1. 登录 Microsoft 365 管理中心。
2. 选择 **Copilot**，然后选择 **设置（Settings）**。
3. 选择 **查看全部（View all）**。
4. 在 **搜索所有 Copilot 设置（Search all Copilot settings）** 中，输入 `Frontier`。
5. 选择 **Copilot Frontier**。
6. 选择 **无访问权限（No access）**、**所有用户（All users）** 或 **特定用户和组（Specific users and groups）**，并应用预期的分配。

Frontier 更改可能需要一段时间才会显示。[Frontier 管理指南](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/get-started-frontier#enroll-users-in-frontier) 说明了传播过程和其他代理访问控制。Frontier 不会覆盖已禁用的代理，也不会代你开启 AI 提供方。

## 为 Autopilot 设置支出策略

Autopilot 按 Copilot Credits 的使用量计费。每个创建 Autopilot 的用户都必须被一项包含 Autopilot 的支出策略覆盖。如果用户未被覆盖，或策略的额度用完，Autopilot 对该用户就不工作，且 Autopilot 不会向该用户显示说明。

你可以在激活过程中创建策略（向导会建议新建一项 Autopilot 支出策略），也可以提前在成本管理中创建：

| 向导步骤 | 要做的事 |
| --- | --- |
| 打开成本管理 | 在 Microsoft 365 管理中心，转到 **Copilot** > **成本管理（Cost management）** > **配置（Configuration）** > **支出策略（Spending policies）**，然后选择 **添加支出策略（Add spending policy）**。 |
| 策略范围 | 为策略命名，选择 **身份（Identity）**，然后选择 **所有用户（All users）** 或将要使用 Autopilot 的组。 |
| 代理与服务 | 在 **Microsoft Copilot** 下，确保选中 **Autopilot**。 |
| 限额与提醒 | 设置每月限额、每用户限额或两者，并按需添加电子邮件提醒。 |
| 计费方式 | 选择额度如何支付，例如按用量付费的 Azure 订阅或预付 Copilot Credits。 |
| 查看并添加策略 | 检查设置并保存策略。 |

Autopilot 的消耗计入策略的计费方式。如果用户属于多项支出策略，则以支出限额最高的策略为准。如果你组织中的用户已有 Autopilot，请添加一项覆盖他们的支出策略。为你的租户开启计费检查后，未被覆盖的用户将无法使用 Autopilot。

关于支出策略的更多信息，见[管理由用量计费启用的 AI 体验](https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-credits#add-identity-based-spending-policy)。

## 为用户激活 Autopilot

在代理注册表（Agent Registry）中激活该代理，并选择谁可以创建 Autopilot。

1. 在 Microsoft 365 管理中心，转到 **代理（Agents）** > **所有代理（All agents）**。
2. 搜索 `Autopilot`，选择 **Autopilot (Frontier)**，然后选择 **激活（Activate）**。
3. 完成激活向导的五个步骤：

   | 向导步骤 | 要做的事 |
   | --- | --- |
   | **选择用户（Select users）** | 选择 **所有用户** 或可以创建 Autopilot 的特定组。让此范围与你的支出策略保持一致。 |
   | **支出策略** | 选择你的 Autopilot 支出策略。如果没有，保留向导建议的新 Autopilot 支出策略，并选择 **自定义策略（Customize policy）** 设置限额和计费方式。 |
   | **安全策略** | 查看为该代理列出的默认 Microsoft Entra、Microsoft Purview 和 Microsoft Defender 防护。它们分别在各个安全产品中管理，且可能未开启，因此请在那里检查其状态。 |
   | **接受权限（Accept permissions）** | 查看代理的权限，以及 Autopilot 可不经逐步确认即可行动的提示。 |
   | **记忆与个性化（Memory & personalization）** | 查看代理的记忆能力和用户控制项。 |
   | **查看并激活（Review & activate）** | 确认代理、支出策略、用户与组以及权限，然后选择 **激活代理（Activate agent）**。 |

你无需在此页面上选择或分配许可证。

关于激活及其他代理操作的详细信息，见 [Microsoft 365 管理中心内可用代理的治理与生命周期操作](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions)。

## 确认 Autopilot 访问权限

让一位已启用的用户在 [copilot.cloud.microsoft](https://copilot.cloud.microsoft) 登录，并检查左侧导航的 **主页（Home）** 标签页中是否显示 Autopilot。Autopilot 仅对已激活**且**被包含 Autopilot 的支出策略覆盖的用户显示。对于尚无 Autopilot 的用户，选择它会启动 Autopilot 创建流程。

如果导航中没有 Autopilot，或 Autopilot 停止响应，请检查：

- 用户的 Frontier 分配。
- 用户的 Copilot 许可证。
- **Autopilot (Frontier)** 的激活范围。
- 用户是否被支出策略覆盖，以及策略是否还有剩余额度。
- 允许的代理与 AI 提供方设置。

留出时间让更改生效。不要让用户反复创建代理来排查访问权限缺失的问题。

关于许可的指导，见 [Microsoft Copilot 许可](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-licensing)。将 [Autopilot 要求](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)用作面向用户的先决条件清单。

## 监视和管理 Autopilot 实例

用户创建各自的 Autopilot 后，使用该代理的详细信息面板查看并治理它们。

1. 在 **代理** > **所有代理** 中，选择 **Autopilot (Frontier)**。
2. 选择 **实例（Instances）** 查看你组织中的用户已创建的 Autopilot。

要更改谁可以创建 Autopilot，请更新激活范围。将用户从激活范围中移除，并不会移除其已有的 Autopilot。要停止一个已有的 Autopilot，还需将该用户从支出策略中移除，然后阻止或删除该实例。阻止用户大约需要一小时才能传到 Autopilot，而代表所有者进行的工作可能持续更久，因此不要依赖它来立即停止。

要跟踪 Autopilot 使用的 Copilot Credits，请转到 **Copilot** > **成本管理**。为支出策略添加提醒，以便在接近限额时收到通知。

在 **Autopilot (Frontier)** 条目上执行治理操作，例如激活、阻止和分配用户。在推出期间，代理注册表可能会暂时显示一个与 Autopilot 关联的额外条目。仅当 **Autopilot (Frontier)** 未显示全部实例时，才用它列出 Autopilot 实例。

## 查看身份和权限

Autopilot 拥有专用的 Microsoft Entra 身份。有些操作使用该身份，另一些则使用代表用户获得的授权访问权限。Autopilot 不会扩大用户对 Microsoft 365 数据的访问范围。应查看其行事账户、资源访问权限和允许的操作，而不是把创建代理视为授予对所有组织数据的访问权限。

用户可以检查 **代理设置（Agent settings）**，包括 **计算机与访问权限（Computer & Access）**。代理设置并不授权 Autopilot 执行某项操作。

Autopilot 及其自动化可以在无需每一步都给出新提示的情况下完成工作。应教会用户检查已保存的指令、收件人、目标位置和权限范围。更多信息见[设置权限](https://learn.microsoft.com/en-us/copilot/autopilot/approval#set-permissions)。

## 查看插件、技能和浏览器使用

用户可以从目录添加插件、创建或上传自己的技能，并与组织中的特定人员共享技能。被你组织策略阻止的插件会显示为 **被策略阻止（Blocked by policy）**，无法添加。对于你组织管理的插件，连接由你处理，因此用户无需登录或输入密钥。共享技能不会转移共享者的登录状态、连接或权限。关于在你组织中管理和治理插件的指导，见[插件文档](https://learn.microsoft.com/en-us/plugins)。

在已启用的情况下，Autopilot 还可以在用户设备的 Microsoft Edge 中工作，但仅限于用户在其私密对话中提出的请求。在执行付款或账户更改等敏感操作之前，它会请求用户批准。它读取的页面内容由其云端模型处理。你组织的策略、Edge 策略和数据丢失防护仍可阻止浏览器操作。面向用户的指导见[自定义 Autopilot 能做什么](https://learn.microsoft.com/en-us/copilot/autopilot/plugins)和[在你的 Microsoft Edge 浏览器中工作](https://learn.microsoft.com/en-us/copilot/autopilot/edge)。

## 了解自动检查和审批

Autopilot 可以执行多步任务，并代表用户跨已连接的服务采取行动，而无需在每一步都询问。与其他 AI 体验一样，它可能比预期更宽泛地理解请求。例如，清理旧项目文件的请求可能影响到比用户预期更多的内容。激活流程中包含一则提示，说明 Autopilot 可不经逐步确认即可行动。在激活 Autopilot 之前，请查看其权限，并考虑用户打算执行的任务是否适合自动执行。

Autopilot 使用一个自动审查系统，即第二个 AI 模型，在操作运行前审查操作。该审查系统会将每项操作与用户的请求及其设定的任何限制进行比较，然后决定该操作可以继续还是需要用户批准。

| 操作类型 | 会发生什么 |
| --- | --- |
| 读取、搜索和起草 | 不中断地运行。会抽查一小部分。 |
| 发送、共享、删除或更改内容；创建或更改自动化 | 由自动审查系统决定。与请求相符的操作会运行；其他操作等待用户批准。 |
| 付款和敏感的浏览器步骤 | 始终需要用户批准。 |

- **只有所有者本人的请求才算数。** 自动审查系统只把所有者本人的消息视为请求。电子邮件、文档或网页中的指令不会授权某项操作。
- **可见性与设置。** 在可用的情况下，用户可以在 Autopilot 面板的 **最近批准（Recent approvals）** 下查看最近被批准的操作，并对其提供反馈。本版本中，自动审查系统没有管理员或用户设置。

请让用户在允许某项操作之前检查范围、收件人、文件和数据，并检查重要结果，尤其是在涉及文件、访问权限或通信时。面向用户的指导见[设置权限](https://learn.microsoft.com/en-us/copilot/autopilot/approval#set-permissions)。

## 查看模型治理

Autopilot 运行在 GPT-6.1 Sol 上，由作为 Microsoft 子处理方运营的 OpenAI 提供。如果你的组织在 AI 提供方设置中关闭 OpenAI，Autopilot 会自动改用托管在 Azure OpenAI 中的 GPT-5.6 Sol。用户无法通过提示词切换模型，Autopilot 也没有单独的模型选择控件。

- **数据处理。** 开启 OpenAI 后，Autopilot 的提示词及相关数据由作为 Microsoft 子处理方的 OpenAI 处理。请在 Microsoft 365 管理中心的 **Copilot** > **设置** > **作为 Microsoft 子处理方运营的 AI 提供方（AI providers operating as Microsoft subprocessors）** 下查看此设置。
- **数据驻留。** 在广泛启用 Autopilot 之前，请确认该提供方的处理符合你的数据驻留和欧盟数据边界（EU Data Boundary）要求。如果不符合，请关闭该提供方，Autopilot 将使用托管在 Azure OpenAI 中的模型。

更多信息见 [OpenAI 作为 Microsoft 在线服务中的子处理方](https://learn.microsoft.com/en-us/copilot/implement/openai-subprocessor)。

## 查看记忆与个性化

Autopilot 会记住信息，以便提供个性化帮助。它保存对话记忆、关于其所有者的个人记忆，以及为其所完成工作的空间记忆。

- **查看记忆。** 用户可以在 Autopilot 面板的 **查看 [name] 知道什么（Review what [name] knows）** 下看到 Autopilot 记住了什么，其中 *[name]* 是其 Autopilot 的名称。用户可以通过在聊天中提出请求来更正、删除或导出记忆，例如「忘掉我正在做 Project X 这件事。」忘记某条记忆不会抹去更早的聊天消息或导出内容。
- **没有开关。** 本版本中 Autopilot 的记忆无法关闭，Microsoft 365 Copilot 的个性化设置也不适用于它。
- **与对话分离。** 删除对话不会删除记忆。

## 查看合规覆盖情况

Autopilot 通过两种方式访问内容：以自身的代理身份，以及使用所有者的访问权限代表所有者访问。大多数 Microsoft Purview、Microsoft Entra 和 Microsoft Defender 控制适用于代理身份。代表所有者完成的工作只被部分覆盖。下表说明当前覆盖情况。

| 能力 | 当前状态 |
| --- | --- |
| 审计 | 记录在统一审计日志中。AI 与工具调用，以及 Autopilot 以自身身份所做的任何操作（例如向同事发送 Teams 消息），都显示在 Autopilot 名下。代表所有者进行的文件和邮件读取显示在所有者账户下，带有内部服务名称，没有代理 ID。Autopilot 记录上的会话 ID 可以把它们关联起来。会话列表可能包含后台自动化，因此用户看到的条目可能比预期多。 |
| 针对提示词的数据丢失防护（DLP） | 正在部分租户中测试。含有敏感信息的提示词在到达模型之前会被阻止。用户看到的是通用错误，而不是策略通知；同一聊天中的后续提示词仍可得到回答。 |
| 敏感度标签 | 带标签的电子邮件和文件不会被排除。Autopilot 可以以自身身份或代表所有者读取它们。 |
| eDiscovery、保留和法律保留 | 不适用于 Autopilot 会话。Microsoft Copilot 中的会话不存储在适用保留与保留项的位置。 |
| 面向 AI 的数据安全态势管理与活动资源管理器 | 不显示 Autopilot。 |
| Microsoft Entra 和 Microsoft Defender | 条件访问、ID 保护和访问评审适用于代理身份，更改大约需要一小时生效。以 **所有用户** 为目标的策略不包括代理用户。Defender 将该代理列为用户，而不列入其代理清单。 |

显示敏感度标签并不能证明每个生成的文件都继承了该标签。用户活动不是完整的管理审计记录。不要从功能是否存在或通用 Copilot 防护推断合规覆盖范围。

在预览期间，请遵循以下建议：

- **依赖权限与加密。** 权限与加密是能可靠地让内容远离 Autopilot 的控制手段。只与需要的人共享敏感内容，并在适当之处使用加密。
- **检查条件访问覆盖范围。** 以 **所有用户** 为目标的策略不适用于 Autopilot 的代理身份。如果你依赖某项策略，请确保它明确覆盖代理身份。
- **考虑处于法律保留状态的用户。** 由于 eDiscovery、保留和法律保留不覆盖 Autopilot 会话，请考虑不要为受保留约束或有严格保留要求的用户启用 Autopilot。
- **给更改留出时间。** 阻止用户或更改条件访问大约需要一小时才能传到 Autopilot，而代表所有者进行的工作可能持续更久。
- **与用户设定预期。** 确定允许的来源、收件人和存储目标位置，并告知用户如何报告不确定的结果、被阻止的操作和疑似信息泄露。

## 帮助用户访问、导出和删除其数据

用户管理自己的 Autopilot 记忆和会话。对于已批准的合规或隐私请求，管理员可以导出用户 Autopilot 记忆和会话的副本。更多信息见[导出用户的 Autopilot 数据](#export-a-users-autopilot-data)。管理员不能代表用户删除这些数据。不提供批量删除，且「我的账户」隐私页面不会删除 Autopilot 数据。

| 操作 | 如何运作 |
| --- | --- |
| 查看记忆与历史记录 | 用户在 Autopilot 面板中打开 **查看 [name] 知道什么**，或在聊天中提问，例如「你记得关于我的哪些事？」 |
| 导出记忆或会话 | 用户在聊天中向 Autopilot 提出请求。用户批准写入后，Autopilot 会把导出内容保存到用户的 OneDrive。如需完整副本，用户可以在 Windows PC 上运行导出脚本。更多信息见[下载记忆和会话的完整副本](https://learn.microsoft.com/en-us/copilot/autopilot/memory#download-a-full-copy-of-your-memories-and-sessions)。 |
| 为合规或隐私请求导出用户数据 | 管理员使用自己的账户运行导出脚本。更多信息见[导出用户的 Autopilot 数据](#export-a-users-autopilot-data)。 |
| 删除一条记忆 | 用户在 Autopilot 面板中移除它，或在聊天中向 Autopilot 提出请求。 |
| 删除一个会话 | 用户在会话列表中选择该会话旁的 **...** 菜单。 |
| 永久移除已删除的会话 | 用户在聊天中向 Autopilot 提出请求。 |
| 批量删除、离职用户删除或经核验的删除 | 联系 Microsoft 支持。 |

与用户分享以下要点：

- **批准写入。** 保存导出内容会写入 OneDrive，因此请留意批准卡片。
- **保护导出内容。** 导出的文件可能不带敏感度标签。请根据其中所含的最敏感信息来处理它们。
- **永久移除已删除的会话。** 删除会话后它会从列表中移除，但底层记录会保留，直到用户请 Autopilot 将其移除。用户先说「删除标题为 [name] 的会话」，然后说「你现在能把它永久删除吗？」
- **Teams 中的编辑会同步过来。** 当用户在 Teams 中与 Autopilot 的聊天里编辑或删除消息时，Autopilot 对该会话的副本也会更新。
- **单独处理记忆。** 删除对话不会移除已保存在记忆中的信息。用户还应移除相应的记忆，并确认它已消失。

面向用户的提示见[查看 Autopilot 记住了什么](https://learn.microsoft.com/en-us/copilot/autopilot/memory)。

### 从头开始

如果用户想清除 Autopilot 的所有工作数据，包括对话历史、记忆、技能和自动化，应先导出任何想保留的内容。如需完全重置、批量删除、离职用户清理或跨位置核验删除，请联系 Microsoft 支持。

## 导出用户的 Autopilot 数据

Autopilot 将每个用户的记忆和会话存储在用户 OneDrive 中一个名为 `lobster.repo` 的文件里。对于已批准的合规或隐私请求，租户管理员可以使用 Autopilot 导出脚本下载另一用户的 `lobster.repo` 副本。你使用自己的管理员账户登录；脚本绝不会使用用户的凭据。用户 OneDrive 中的任何内容都不会被更改、共享或删除。

### 导出之前

确保你具备：

- 一台装有 Windows PowerShell 的 Windows PC。如果缺少 Git for Windows，脚本会提示安装。
- [GitHub 上提供](https://github.com/microsoft/autopilot-resources/blob/main/workspace-export/Autopilot-Workspace-Export.zip)的 `Autopilot-Workspace-Export.zip` 文件。右键单击它，选择 **全部解压（Extract All）**，然后打开解压后的 `Autopilot-Workspace-Export` 文件夹。不要从 zip 文件内部运行脚本。
- 一个可在 Microsoft 365 管理中心访问该用户 OneDrive 的管理员账户。
- 一项已批准的请求，并带有可记录为导出原因的参考编号。
- 如需更多细节，请查阅 [Autopilot-resources GitHub 仓库](https://github.com/microsoft/autopilot-resources)中的 [README.md 文件](https://github.com/microsoft/autopilot-resources/blob/main/workspace-export/README.md)。

### 导出用户的数据

按以下步骤为自己授予临时访问权限、运行导出，然后移除你的访问权限。

1. 在 Microsoft 365 管理中心为自己授予对该用户 OneDrive 的临时访问权限：

   1. 转到 [admin.microsoft.com](https://admin.microsoft.com)，使用你的管理员账户登录。使用 InPrivate 窗口可让此登录与你的日常工作账户分开。
   2. 选择 **用户（Users）** > **活动用户（Active users）**，然后选择该用户的姓名。
   3. 在用户页面上，选择 **OneDrive** 标签页。
   4. 在 **获取文件访问权限（Get access to files）** 下，选择 **创建文件链接（Create link to files）**。
   5. 复制出现的链接，例如 `https://contoso-my.sharepoint.com/personal/user_contoso_com`。此链接就是该用户的 OneDrive 地址。

   此步骤会使你成为该用户 OneDrive 的管理员，直到你移除访问权限；该授权会记录在审计日志中。可能需要几分钟才能生效。
2. 在解压后的 `Autopilot-Workspace-Export` 文件夹中打开 PowerShell，并运行以下命令。使用第 1 步中的链接作为 `-TargetOneDriveUrl` 的值。

   ```
   powershell -NoProfile -ExecutionPolicy Bypass -File .\Export-AutopilotWorkspace.ps1 -TargetUser user@contoso.com -Reason "Privacy request 1234" -Account admin@contoso.com -TargetOneDriveUrl "https://contoso-my.sharepoint.com/personal/user_contoso_com"
   ```

   | 参数 | 描述 |
   | --- | --- |
   | `-TargetUser` | 你要导出其数据的用户的登录名。 |
   | `-Reason` | 导出原因，例如请求参考编号。它会记录在导出清单中。 |
   | `-Account` | 你的管理员账户。脚本会在登录时预选它。 |
   | `-TargetOneDriveUrl` | 可选。第 1 步中该用户的 OneDrive 地址。如果不提供，脚本会尝试自动查找该用户的 OneDrive。 |
   | `-OutputFolder` | 可选。用于导出的新文件夹。它不能由 OneDrive 同步。 |
3. 出现提示时，选择 **是（Yes）** 以批准你 PC 上的管理员访问权限。
4. 使用你的管理员账户登录。只有浏览器登录才会将你标识为管理员；你的 Windows 账户无关紧要。如果 Microsoft Edge 用其他账户自动登录，请把脚本打印的登录地址复制到 InPrivate 窗口（Ctrl+Shift+N）中。
5. 当浏览器显示你已登录时，返回 PowerShell 窗口，在第二个管理员提示处选择 **是**。
6. 脚本会找到该用户的 OneDrive，并确认其所有者与 `-TargetUser` 匹配。它会显示找到的仓库，并要求你输入该用户的登录名以确认。如果找到多个 `lobster.repo`，请输入要下载的那个的编号。
7. 导出完成后，将脚本最后打印的导出清单哈希与请求一并记录。
8. 移除你对该用户 OneDrive 的访问权限。脚本会为此打印一条 `Set-SPOUser ... -IsSiteCollectionAdmin $false` 命令，你也可以在 SharePoint 管理中心移除。

### 查看导出的文件

脚本会在你的用户配置文件中创建一个名为 `Autopilot export <date time>` 的新文件夹，并在文件资源管理器中打开它。该文件夹包含：

| 项目 | 内容 |
| --- | --- |
| `Latest files` | 最新版本中文件的可读副本，例如记忆和会话记录。 |
| `repository.git` | 完整的 Git 仓库，包括较早的版本和历史。 |
| `README.txt` | 关于该副本的简短说明。 |
| `export-manifest.json` | 记录谁为用户导出了数据、为谁导出、何时导出以及为何导出，并附每个文件的 SHA-256 哈希。 |

导出内容包含用户的个人和组织信息。请按照你组织处理该请求的流程以及其中所含的最敏感信息来存储和共享它。

### 导出故障排除

如果脚本因某条消息而停止，请使用下表解决。

| 消息 | 要做的事 |
| --- | --- |
| 管理员批准被拒绝（Administrator approval was declined） | 再次运行脚本并选择 **是**，或请 IT 支持与你一起运行。 |
| Hosts 文件已有其他条目（Hosts file already has a different entry） | 请 IT 支持检查现有的 `cowork.local.microsoft.com` 条目。 |
| 浏览器显示证书警告（Browser shows a certificate warning） | 不要绕过它。关闭标签页并向你的安全团队报告。 |
| 你的组织尚未批准此登录（Your organization has not approved this sign-in） | 联系 IT 支持；该登录应用可能需要在你的组织中获得同意。 |
| 3 次尝试后仍无法连接（Could not connect after 3 attempts） | 检查你的网络、VPN 或代理连接，然后再次运行脚本。 |
| 未找到 Autopilot 工作区（No Autopilot workspace was found） | 该用户可能没有 Autopilot，或其工作区可能存储在其他位置。联系 Microsoft 支持。 |
| 部分分支或标签引用无法下载（Some branch or tag references could not be downloaded） | 副本不完整。把脚本重新运行到一个新文件夹中。 |
| 临时设置无法自动移除（Temporary setup could not be removed automatically） | 警告中会指明要移除的 hosts 文件行和证书。请手动移除它们。 |
| 你无权访问某用户的 OneDrive（You do not have access to the OneDrive of a user） | 完成第 1 步，等待几分钟，然后使用 `-TargetOneDriveUrl` 再次运行脚本。 |

要查看更多细节，请在工具的文件夹中打开 PowerShell 并运行 `.\Export-AutopilotWorkspace.ps1 -Verbose`。使用 `-OutputFolder` 选择另一个新文件夹；它不能由 OneDrive 同步。

如果 PowerShell 报告脚本运行已被禁用，请使用 `Export-AutopilotWorkspace.cmd`，或上文所示的 powershell `-ExecutionPolicy Bypass -File` 形式。如果你的组织完全阻止 PowerShell，请联系 IT 支持。

## 查看用量和推出情况

支出策略控制谁可以使用 Autopilot、设置每月和每用户限额与提醒，并决定计费方式。在 **Copilot** > **成本管理** 中跟踪 Copilot Credit 的使用情况。

如果用户未被支出策略覆盖，或策略达到限额，Autopilot 会停止运行自动化和监视工作，并停止响应新请求。Autopilot 不会向用户显示说明，因此请告知用户：如果 Autopilot 停止响应，请联系你。在扩大访问范围之前，请检查策略限额和提醒。

从有边界的工作流和有限的受众开始。检查自动化结果、审批、失败或不确定的操作，以及最终的文件或消息。在扩大访问范围之前，先在你自己的配置中验证更改。

## 相关内容

- [Autopilot 要求](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)
- [开始使用 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)
- [Autopilot 概述](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [使用 Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/using)
- [Autopilot 的应用卡片](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)
- [Microsoft 365 管理中心内可用代理的治理与生命周期操作](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions)
