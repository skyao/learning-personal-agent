---
title: "管理 dots 的权限和能力"
linkTitle: "文档：企业管理指南"
date: 2026-11-05
originalTitle: "Manage dots permissions and capabilities"
sourceUrl: "https://learn.chatgpt.com/docs/enterprise/dots-admin-guide"
altUrls: ["https://learn.chatgpt.com/codex/enterprise/dots-admin-guide"]
publisher: "OpenAI（ChatGPT Learn）"
language: en
fidelity: 全文翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期；按规则取收集日期"
tags: [安全, 开放与价格, 商业与规模]
products: [dots]
---

{{< source-info >}}

dot 是 ChatGPT 中的一个个人智能体，可以承担长期工作、使用已连接的应用，并把任务委派给 Work 或 Codex。由你决定谁可以使用 dots、配置它们的能力，并管理整个工作区中的个人 dots。成员们连接自己的账户，并告诉自己的 dot 要做什么。

**[dots 安全指南](https://learn.chatgpt.com/codex/enterprise/dots-security)**

与你的安全团队进行详细审查时，请使用 dots 安全指南。本管理指南涵盖工作区设置、访问和日常管理。

关于当前的开放范围、支持的套餐和工作区设置，请参阅[在 ChatGPT 工作区中管理 dots](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)。

## 找到你需要的内容

| 如果你需要…… | 从这里开始 |
| --- | --- |
| 给一个群组开通访问 | [为工作设置 dots](#set-up-dots-for-work) |
| 选择 dot 可以使用哪些数据和工具 | [应用访问](#2-configure-app-access)和[计算机能力](#available-admin-controls) |
| 设置 Slack | [Slack 连接和 dot 身份](#3-configure-communication-channels) |
| 查找、暂停、恢复或删除一个个人 dot | [管理你工作区中的 dots](#manage-dots-in-your-workspace) |
| 跟踪采用情况或调查一个操作 | [监控使用情况](#monitor-usage)和[查看管理员活动与合规记录](#review-admin-activity-and-compliance-records) |
| 在有人更换角色或离职时移除访问权限 | [管理访问变更](#manage-access-changes) |

## 为工作设置 dots {#set-up-dots-for-work}

### 1. 配置基于角色的访问

工作区所有者通过工作区默认设置和自定义角色来管理访问。要给选定的群组开通访问，请保持工作区默认设置为关闭，并给这些群组分配一个自定义角色。检查分配给某个成员的每一个角色：只要有一个角色授予了访问权限，在另一个角色中关闭它并不会移除访问权限。

在**权限**（Permissions）中检查这些权限：

- **使用 dots**（Use dots）：允许成员使用 dots。
- **把 dots 添加到 Slack 和 Microsoft Teams**（Add dots to Slack and Microsoft Teams）：允许成员在可用的地方把自己的 dot 连接到受支持的消息渠道。
- **允许本地计算机访问**（Allow local computer access）：允许 dots 使用成员的本地计算机。
- **为 dots 使用自定义规则**（Use custom rules for dots）：允许成员为自己的 dot 添加或编辑规则。

关于角色的创建、分配和访问检查，请参阅[基于角色的访问控制指南](https://learn.chatgpt.com/codex/enterprise/roles-and-workspace-permissions#set-the-workspace-default-then-create-targeted-custom-roles)。

1. 打开**管理控制台**（Admin Console）> **权限**。
2. 在「权限 > 工作区默认设置 > 工作区能力」下，如果应当默认开放，就启用**使用 dots**；否则通过一个自定义角色授予访问权限。
3. 设置 Slack 参与和自定义 dot 规则。本地计算机访问需要管理员另行选择开启；启用之前，请查看[本地计算机访问设置](https://learn.chatgpt.com/codex/enterprise/cloud-local-access#enable-local-computer-access)。
4. 在**让智能体使用云端计算机**（Let agents use cloud computers）下，在你的政策允许浏览网站、访问在线服务和与应用交互的地方，检查**使用浏览器**、**允许网络访问**和**允许计算机操作**。同时检查工作区默认设置和自定义角色。
5. 在「工作区能力」下，根据你的工作区政策设置「使用密码管理器」。
6. 保存，然后为一位预期的成员检查访问权限。

当你启用 dots 时，系统可能会要求你打开一些仍处于关闭状态的云端计算机能力。Dots、Work Cloud 和团队自动化共用这些权限。请选择你所在组织的政策所允许的能力。

之后要查看它们，请前往**管理控制台** > **权限** > **工作区默认设置** > **工作区能力** > **让智能体使用云端计算机**。本地计算机访问是另一个单独的选择开启项。

在你启用访问之后，成员们仍然需要完成 [Slack](https://learn.chatgpt.com/codex/dots/channels#slack) 和[本地计算机](https://learn.chatgpt.com/codex/dots/computers-and-apps#connect-your-computer)的设置。他们已经设置好的受支持应用连接，可能可以供他们的 dot 使用。

### 2. 配置应用访问 {#2-configure-app-access}

个人 dot 可以使用其所有者现有的 ChatGPT 应用连接。通过每一个连接，它只能读取或修改已连接账户所允许、且工作区所允许的内容。设置访问时，请检查：

1. **成员可以使用哪些应用。** 在[插件控制](https://learn.chatgpt.com/codex/enterprise/apps-and-connectors)中设置可用的应用和允许的操作。
2. **已连接的账户能访问什么。** 在源应用中检查该账户的权限。启用 dots 并不会让它获得对每一个共享盘、频道或文档的访问权限。
3. **什么时候需要批准。** 检查已连接应用针对特定操作（比如发送一条消息）的批准设置。仅仅启用这个应用，并不等于授权发送。选项请参阅[应用权限](https://help.openai.com/en/articles/20001495-managing-app-permissions-in-chatgpt)。

例如，读取一份文档的权限，可能并不包括编辑或分享它。要限制对某个特定来源的访问，请检查已连接的账户和应用权限。

关于自动审查（Auto-review），以及授权起草与授权发送之间的区别，请参阅[批准与无人值守工作](https://learn.chatgpt.com/codex/enterprise/dots-security#set-rules-for-approvals-and-unattended-work)。

### 3. 配置通信渠道 {#3-configure-communication-channels}

成员可以用两种方式把 Slack 连接到自己的 dot：

| 设置 | 成员体验 | 需要配置什么 |
| --- | --- | --- |
| 通过插件连接成员的 Slack 账户 | 成员在 ChatGPT 中与自己的 dot 交谈。它可以使用他们的 Slack 连接，而没有自己的 Slack 身份。 | Slack 插件访问、已连接的账户、允许的操作和批准。 |
| 给 dot 一个自己的 Slack 身份 | 所有者可以在 Slack 中给 dot 发消息或提及它，它发的帖子对该对话中的人可见。 | Dots 消息权限、Slack 应用批准，以及每位成员的 dot 设置。 |

关闭一个 dot 的 Slack 身份，并不会移除它通过成员已连接的 Slack 账户获得的访问权限。移除 Slack 访问时，两者都要检查。关于成员的设置，请参阅[消息](https://learn.chatgpt.com/codex/dots/channels#slack)。

**在成员把自己的 dot 连接到 Slack 之前**

- **ChatGPT 工作区所有者：** 通过工作区默认设置或自定义角色，为预期的成员启用「使用 dots」和「把 dots 添加到 Slack 和 Microsoft Teams」。
- **Slack 工作区所有者或应用管理员：** 确保 ChatGPT 应用已安装在 Slack 中。如果你的工作区要求，批准应用请求。请参阅 [Slack 的应用批准指南](https://slack.com/help/articles/360024269514-Manage-app-requests-for-your-workspace)。
- **每位成员：** 从你的 dot 的个人资料中把它连接到 Slack。请参阅[在 Slack 中给你的 dot 发消息](https://learn.chatgpt.com/codex/dots/channels#slack)。

启用 ChatGPT 的权限，并不会在 Slack 中安装应用，也不会连接成员的 dot。

### 验证一个已批准的工作流

配置好访问之后，用这项工作所针对的成员、已连接账户和计算机环境来测试工作流。使用一次性文档和测试接收方。

1. **检查实际生效的权限。** 检查工作区默认设置和每一个已分配的角色。确认这个工作流需要哪些应用、云端能力和本地连接。
2. **从一个允许的来源准备一份草稿。** 检查来源、已连接的身份和输出。如果工作流同时使用一个已登录的网站和一个应用连接，两个账户都要检查。
3. **测试批准行为。** 使用一个无害的操作和测试接收方。记录指示、任何批准请求，以及接收服务中的最终状态。仅有书面政策，并不会产生由产品强制执行的限制。
4. **检查可用的记录。** 检查活动和合规记录，确认你能重建这次测试的哪些部分。记录任何缺失的记录。

将结果与你的安全团队批准的要求进行比较。在把这个工作流用于受影响的数据之前，解决必需的限制或记录方面的任何缺口。

## 可用的管理控制 {#available-admin-controls}

| **领域** | **管理能力** |
| --- | --- |
| dots 访问 | 通过工作区权限授予或撤销 dots 访问权限。 |
| 云端和已连接的本地计算机 | 控制「使用浏览器」「允许网络访问」「允许计算机操作」「使用密码管理器」和本地计算机访问。 |
| 消息与参与 | 启用或禁用 Slack 参与。 |
| 已连接的应用 | 通过[插件控制](https://learn.chatgpt.com/codex/enterprise/apps-and-connectors)设置可用的应用和允许的操作。 |
| 自定义 dot 规则 | 禁用时，成员无法添加或编辑自定义规则，已保存的规则也不会生效。 |
| 模型 | 企业模型控制和默认设置不适用于主 dot。请单独检查委派出去的 Work 和 Codex 任务。 |

关于云端浏览器的站点规则和仍在开发中的控制，请参阅[浏览器、网络和设备访问](https://learn.chatgpt.com/codex/enterprise/dots-security#review-browser-network-and-device-access)。关于已连接的计算机和委派出去的任务，请参阅[按工作环境划分的控制](https://learn.chatgpt.com/codex/enterprise/dots-security#controls-by-work-environment)。

## 检查开放范围和数据要求

在启用 dots 之前，请在[开始使用你的 dot](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)和设置过程中显示的工作区通知中查看当前的开放范围。在安全指南的[资格与数据要求](https://learn.chatgpt.com/codex/enterprise/dots-security#confirm-eligibility-and-data-requirements)中查看关于地区、数据驻留、企业密钥管理（Enterprise Key Management）和 HIPAA 覆盖范围的内容。在启用访问之前，确认你的工作区配置、任何适用的商业伙伴协议（BAA）以及预期的工作流满足你所在组织的要求。

检查对 dot 本身、它委派给 Work 或 Codex 的任务以及任何已连接计算机的要求。关于云端浏览器、网络和计算机操作，请参阅[云端安全](https://learn.chatgpt.com/codex/enterprise/chatgpt-work-cloud-security)。关于在员工设备上的工作，请参阅[本地计算机访问](https://learn.chatgpt.com/codex/enterprise/cloud-local-access)。

## 管理你工作区中的 dots {#manage-dots-in-your-workspace}

打开**管理控制台** > **Dots**，查看在你的工作区中创建的个人 dots。使用这份清单找到一个 dot，查看它的所有者和状态，然后打开它的详情进行管理。

### 查看一个 dot 的详情

详情包括创建这个 dot 的成员、它处于活跃还是暂停状态、它的身份，以及它的 Slack 或 Microsoft Teams 连接状态。身份是这个 dot 的服务账户，在没有服务账户时则是它的 dot ID。连接状态显示是否连接了某个消息服务；[消息权限](#3-configure-communication-channels)控制谁可以设置这个连接。

### 暂停和恢复一个 dot

当你需要临时停止一个 dot 时，从管理控制台暂停它。管理员的暂停会阻止成员恢复这个 dot。在清单中检查，确认它的状态是已暂停。

恢复一个 dot 会还原它之前的用户状态。原本活跃的 dot 会重新变为活跃；成员此前已经暂停的 dot 仍然保持暂停。在管理员暂停期间停止计费，如果这个 dot 回到活跃状态，计费会恢复。

### 删除一个 dot

当一个 dot 应当从工作区中移除时，从管理控制台删除它。删除完成后，它不再出现在清单中，计费也会暂停。删除会移除这个 dot 的上下文；它不会为以后恢复而保留这个 dot。

这个 dot 创建的文件、Codex 会话线程和 ChatGPT 对话是单独存储的，不会随它一起被删除。需要时，请在各自的位置检查并删除这些内容。当你想保留这个 dot 并在以后恢复它时，请使用暂停。

### 撤销和恢复访问

要移除某位成员使用 dots 的权限，请检查工作区默认设置，以及直接分配或通过群组分配的每一个角色。移除每一个适用的**使用 dots** 授权。关闭一个角色的权限，在另一个角色仍然授予访问权限时，并不会移除访问权限。

| 变更 | dot 会怎样 | 需要检查什么 |
| --- | --- | --- |
| 撤销成员的 dots 权限 | 这个 dot 对成员隐藏，被暂停，并在清单中显示为已禁用。计费停止。在权限被撤销期间，这个 dot 无法恢复。 | 检查成员实际生效的权限，以及这个 dot 在清单中的状态。 |
| 恢复成员的 dots 权限 | 这个 dot 回到之前的用户状态。如果它原本是活跃的，会重新变为活跃，计费恢复。 | 检查恢复的权限，以及这个 dot 是活跃的还是仍处于用户暂停状态。 |

对于离职交接，还要在[管理访问变更](#manage-access-changes)中检查连接和委派出去的工作。

## 监控使用情况 {#monitor-usage}

工作区分析包括已启用 dot 的数量和 dots 的总活跃用户数。已启用的 dots 是指未被暂停的 dots。把这两个指标结合起来使用，了解有多少 dots 处于启用状态，以及有多少人在使用它们。

对于按成员或工作区的每日报告，请使用 [Analytics API](https://learn.chatgpt.com/codex/enterprise/analytics-api)。每日使用量端点 `/v1/analytics/workspaces/{workspace_id}/usage` 用 `client_id = DOTS` 来标识 dots。

dot 在 Work 或 Codex 中启动或管理的任务，计入这些产品的使用限额，并出现在它们的报告中。在检查使用情况时，要把这些任务也包括进来。关于可用的控制，请参阅 [Work 的使用量与成本](https://learn.chatgpt.com/codex/enterprise/chatgpt-work-usage-and-cost)；在设定预算时，请查看你的套餐的现行条款。

## 查看管理员活动与合规记录 {#review-admin-activity-and-compliance-records}

审计日志会记录管理员对 dots 的操作，包括暂停、恢复、删除、管理和已保存档位的变更。使用这些记录来检查管理员所做的变更。

要调查一个 dot 做过的工作，请使用 [Compliance API](https://learn.chatgpt.com/codex/enterprise/compliance-api#confirm-the-administration-boundaries)。受支持的 dots 记录包括用户提示和回复、受支持的工具调用事件，以及已连接应用的 MCP 调用及其结果。归属于 dots 的记录使用 `client_id = DOTS`；在可用时，智能体对象会包含 dot ID、名称和类型。

工作区所有者或管理员可以在管理控制台中选择自己的工作区，然后打开**凭证** > **管理员密钥**，创建一个具有适当可用权限的密钥：`enterprise.analytics.usage.read` 用于统一的使用量报告，`CODEX_LOG` 访问用于 dots 合规记录。在支持的情况下，只有工作区所有者才能授予广泛的合规访问或**对话消息**（Conversation messages）访问。使用[管理员 API 参考](https://chatgpt.com/public/admin/api-reference)列出并下载合规 JSONL 文件，并选择 `client_id = DOTS` 的记录。

### 为一次调查检查记录

把一个无害的测试操作与可用的导出记录进行比较。检查它们是否标识出了用户、dot、发起的请求、工具、适用的批准和结果。记录缺失的字段和事件。一个被请求的工具调用并不能证明某个操作已经完成；请使用接收服务的记录来确认结果。

根据下载的记录中包含的消息和已连接数据的敏感程度来保护这些记录。

## 管理访问变更 {#manage-access-changes}

当有人更换角色或离职时，请检查他们的 dot 的权限、连接和进行中的工作：

1. **移除 dots 访问权限。** 检查工作区默认设置，以及直接分配或通过群组分配的每一个角色。移除每一个授予访问权限的权限；任何剩下的授权都可能让它保持启用。
2. **检查已连接的账户和设备。** 检查插件授权、网站会话、本地计算机访问，以及这个 dot 的 Slack 身份。每一项都有自己的设置。
3. **决定进行中的工作怎么处理。** 查看[暂停和删除控制](#manage-dots-in-your-workspace)，然后分别检查进行中的任务、周期性时间安排，以及委派给 Work 或 Codex 的任务。决定什么应该停止，以及谁应该接手剩下的职责。
4. **在需要时删除数据。** 访问变更和删除是两个单独的步骤。按照删除流程处理这个 dot 的上下文，以及存储在其他地方的任何文件或任务。

关于添加和移除工作区成员，请参阅[用户生命周期管理](https://learn.chatgpt.com/codex/enterprise/user-lifecycle)。关于移除 dots 访问权限，请参阅[在 ChatGPT 工作区中管理 dots](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)。

### 记录移除访问的结果

完成访问变更检查清单后，记录移除了哪些权限、应用授权、网站会话、计算机连接和消息身份。分别检查进行中的工作和时间安排，包括委派给 Work 或 Codex 的工作。记录任何仍在进行的工作及其负责人。

移除访问权限并不会撤销已经在另一个服务中完成的操作。当一个操作需要撤销时，请检查接收服务。

### 应对一个意外的操作

从管理控制台暂停这个 dot，在清单中确认它的暂停状态，并请成员检查受影响的任务。保存任务链接和可用的活动记录，检查涉及的应用或计算机权限，并按照你所在组织的事件处理流程进行。能否撤销一个操作，取决于这个操作和相应的服务。

## 帮助成员用好 dots

帮助成员选择要委派的工作，并连接他们需要的账户和工具。鼓励他们告诉自己的 dot 做什么、什么时候做，以及谁应该看到结果。

例如，「Prepare a weekly project update for me to review」（准备一份每周项目更新供我审阅）要求的是一份草稿。「Post the approved update in our team channel every Friday」（每周五把已批准的更新发到我们的团队频道）则同时给出了发布的许可。成员应当检查重要的结果，并知道如何查看活动、更改时间安排以及暂停自己的 dot。分享[入门](https://learn.chatgpt.com/codex/dots/getting-started)、[任务与记忆](https://learn.chatgpt.com/codex/dots/tasks-and-memory)和[控制](https://learn.chatgpt.com/codex/dots/controls)，帮助他们开始使用。
