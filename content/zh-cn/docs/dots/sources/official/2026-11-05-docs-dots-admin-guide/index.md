---
title: "管理 dots 的权限和能力"
linkTitle: "文档：企业管理指南"
date: 2026-11-05
originalTitle: "Manage dots permissions and capabilities"
sourceUrl: "https://learn.chatgpt.com/docs/enterprise/dots-admin-guide"
altUrls: ["https://learn.chatgpt.com/codex/enterprise/dots-admin-guide"]
publisher: "OpenAI（ChatGPT Learn）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标日期；按规则取收集日期；2026-11-28 发现原文更新：新增「Enterprise preview and billing」一节（预览期按角色启用，2026-11-18 起成员默认可用，除非工作区选择退出；预览免费，委派给 Work 或 Codex 的任务按标准费率计费）；权限步骤与控制表新增 Wallet（企业工作区默认关闭）；Microsoft Teams 全部删去"
tags: [开放与价格, 安全, 商业与规模]
products: [dots]
---

{{< source-info >}}

**收录说明**：OpenAI 在 ChatGPT Learn 上发布的 dots 文档，文档不标日期，页面日期取第一轮收集日期 2026-11-05。第一轮收集时直接翻译，原文未单独存档；2026-11-28 按新流程重新抓取（直接下载），原文存于本目录的 original.md（网站上不显示）：页内相对链接改为绝对地址，没有其他需要清理的网页元素。新版有新增和改写，旧译文已删去（由 git 保留），已翻译。

**内容摘要**：这一页面向工作区所有者，说明如何配置和管理 dots。预览期管理员可以为选定角色启用 dots，2026-11-18 起成员默认可用，除非工作区选择退出；预览本身免费，dot 委派给 Work 或 Codex 的任务按标准费率另计。设置步骤包括在自定义角色中开通「使用 dots」、Slack 参与、本地电脑访问、云端计算机能力和 Wallet，Wallet 在企业工作区默认关闭。只要有一个角色授予了访问，关闭另一个角色不会移除访问。管理员可以在 Admin Console 查看、暂停、恢复、删除 dots，用量看 Analytics API，记录用 Compliance API 的 `client_id = DOTS` 查询。

**保留理由**：这是 dots 在企业工作区中如何授权、如何计费、记录到哪里查的官方说明；新版加入了默认开启日期、预览计费和 Wallet 开关。

---

dot 是 ChatGPT 中的个人智能体（personal agent），可以承担持续性工作、使用连接的应用，并把任务委派给 Work 或 Codex。你可以选择谁能使用 dots、配置它们的能力，并在整个工作区管理个人 dot。成员连接自己的账号，并告诉自己的 dot 要处理什么工作。

**[dots 安全指南](https://learn.chatgpt.com/codex/enterprise/dots-security)**

请与你的安全团队一起用 dots 安全指南做详细评审。本管理指南涵盖工作区设置、访问权限和日常管理。

关于当前的可用情况、支持的套餐和工作区设置，见 [在 ChatGPT 工作区中管理 dots](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)。

## 找到你需要的部分

| 如果你需要…… | 从这里开始 |
| --- | --- |
| 给一个群组授予访问权限 | [为工作设置 dots](#set-up-dots-for-work) |
| 选择 dot 可以使用哪些数据和工具 | [应用访问权限](#2-configure-app-access) 和[计算机能力](#available-admin-controls) |
| 设置 Slack | [Slack 连接与 dot 身份](#3-configure-communication-channels) |
| 查找、暂停、恢复或删除个人 dot | [在工作区中管理 dots](#manage-dots-in-your-workspace) |
| 跟踪采用情况或调查某个操作 | [监控用量](#monitor-usage) 和[查看管理员活动与合规记录](#review-admin-activity-and-compliance-records) |
| 在有人换岗或离职时移除访问权限 | [管理访问权限的变更](#manage-access-changes) |

## 企业预览与计费

在预览期间，符合条件的 ChatGPT Enterprise、Edu 和 Healthcare 工作区中的管理员可以为选定的角色启用 dots。从 2026 年 11 月 18 日起，除非工作区选择退出，成员默认拥有访问权限。每位成员自行决定是否创建个人 dot。

工作区访问权限与计费是分开的。符合条件的 Enterprise 工作区可以按 dot 所做工作的类型支付固定费用，也可以按用量付费。预览期免费。dot 委派给 ChatGPT Work 或 Codex 对话串的任务会按标准费率另行收费。计费详情见帮助中心的[dot 入门](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)。

## 为工作设置 dots

### 1. 配置基于角色的访问权限

工作区所有者通过工作区默认设置和自定义角色来管理访问权限。要给选定的群组授予访问权限，请保持工作区默认设置为关闭，并为这些群组分配一个自定义角色。检查分配给某位成员的每一个角色：只要有一个角色授予了访问权限，在另一个角色中将其关闭并不会移除该权限。

在 **权限** 中检查以下权限：

- **使用 dots**：允许成员使用 dots。
- 允许成员在支持的地方把他们的 dots 连接到 Slack。
- **允许访问本地计算机**：允许 dots 使用成员的本地计算机。
- **为 dots 使用自定义规则**：允许成员为其 dots 添加或编辑规则。

关于角色的创建、分配和访问权限检查，见[基于角色的访问控制指南](https://learn.chatgpt.com/codex/enterprise/roles-and-workspace-permissions#set-the-workspace-default-then-create-targeted-custom-roles)。

1. 打开 **管理控制台**（Admin Console）> **权限**。
2. 在「权限 > 工作区默认设置 > 工作区能力」下，如果希望默认就可用，请启用 **使用 dots**；否则通过自定义角色授予访问权限。
3. 设置 Slack 参与和自定义 dot 规则。访问本地计算机需要管理员单独选择启用；启用前请先阅读[本地计算机访问设置](https://learn.chatgpt.com/codex/enterprise/cloud-local-access#enable-local-computer-access)。
4. 在 **允许智能体使用云端计算机** 下，在你的策略允许浏览网站、访问在线服务和与应用交互的范围内，检查 **使用浏览器**、**允许网络访问** 和 **允许使用计算机**。请同时检查工作区默认设置和自定义角色。
5. 在「工作区能力」下，按你的工作区策略设置「使用密码管理器」。
6. Wallet 在企业工作区中默认关闭。该设置可用后，前往 **管理控制台 → 权限 → 工作区能力 → 使用 Wallet** 为符合条件的成员授予访问权限。成员必须通过生物识别审核并批准每一笔 Wallet 付款。
7. 保存，然后检查一位目标成员的访问情况。

启用 dots 时，系统可能会要求你开启仍未开启的云端计算机能力。Dots、Work Cloud 和团队自动化共用这些权限。请选择你所在组织的策略允许的能力。

以后要查看这些设置，请前往 **管理控制台** > **权限** > **工作区默认设置** > **工作区能力** > **允许智能体使用云端计算机**。本地计算机访问是单独的启用项。

在你启用访问权限后，成员仍需完成 [Slack](https://learn.chatgpt.com/codex/dots/channels#slack) 和[本地计算机设置](https://learn.chatgpt.com/codex/dots/computers-and-apps#connect-your-computer)。他们已经设置好的受支持应用连接，可能可以供其 dot 使用。

### 2. 配置应用访问权限

个人 dot 可以使用其所有者现有的 ChatGPT 应用连接。通过每个连接，它只能读取或更改所连接账号允许、且工作区允许的内容。设置访问权限时，请检查：

1. **成员可以使用哪些应用。** 在[插件控制](https://learn.chatgpt.com/codex/enterprise/apps-and-connectors)中设置可用的应用和允许的操作。
2. **所连接的账号可以访问什么。** 在来源应用中检查该账号的权限。启用 dots 并不会让它访问每一个共享云端硬盘、频道或文档。
3. **何时需要批准。** 检查所连接应用针对具体操作的批准设置，例如发送消息。仅启用应用并不等于授权发送。各选项见[应用权限](https://help.openai.com/en/articles/20001495-managing-app-permissions-in-chatgpt)。

例如，读取某份文档的权限可能不包含编辑或分享它。要限制对某个特定来源的访问，请检查所连接账号和应用的权限。

关于自动审核，以及授权草稿与授权发送之间的区别，见[批准与无人值守工作](https://learn.chatgpt.com/codex/enterprise/dots-security#set-rules-for-approvals-and-unattended-work)。

### 3. 配置沟通渠道

成员可以通过两种方式把 Slack 连接到自己的 dot：

| 设置方式 | 成员体验 | 需要配置什么 |
| --- | --- | --- |
| 通过插件连接成员自己的 Slack 账号 | 成员在 ChatGPT 中与自己的 dot 对话。dot 可以使用成员的 Slack 连接，而无需拥有自己的 Slack 身份。 | Slack 插件访问权限、所连接的账号、允许的操作和批准设置。 |
| 给 dot 自己的 Slack 身份 | 所有者可以在 Slack 中给 dot 发消息或提及它，它的帖子对该对话中的人可见。 | Dots 消息权限、Slack 应用批准，以及每位成员的 dot 设置。 |

关闭 dot 的 Slack 身份并不会移除它通过成员所连接的 Slack 账号获得的访问权限。移除 Slack 访问权限时，两处都要检查。成员设置见[消息功能](https://learn.chatgpt.com/codex/dots/channels#slack)。

**在成员把 dot 连接到 Slack 之前**

- **ChatGPT 工作区所有者：** 通过工作区默认设置或自定义角色，为目标成员启用 **使用 dots** 以及把 dots 连接到 Slack 的权限。
- **Slack 工作区所有者或应用管理员：** 确保 ChatGPT 应用已安装在 Slack 中。如果你的工作区要求，请批准应用请求。见 [Slack 的应用批准指引](https://slack.com/help/articles/360024269514-Manage-app-requests-for-your-workspace)。
- **每位成员：** 在 dot 的个人资料中把它连接到 Slack。见[在 Slack 中给 dot 发消息](https://learn.chatgpt.com/codex/dots/channels#slack)。

启用 ChatGPT 中的权限并不会在 Slack 中安装应用，也不会连接成员的 dot。

### 验证已批准的工作流

配置好访问权限后，与成员、所连接的账号以及为该项工作准备的计算机环境一起测试该工作流。请使用可丢弃的文档和测试收件人。

1. **检查实际生效的权限。** 查看工作区默认设置和每一个已分配的角色。确认该工作流需要哪些应用、云端能力和本地连接。
2. **从允许的来源准备一份草稿。** 检查来源、所连接的身份和输出。如果该工作流同时使用已登录的网站和应用连接，请检查两个账号。
3. **测试批准行为。** 使用一个无害的操作和测试收件人。记录指令、任何批准请求，以及接收服务中的最终状态。仅有书面策略并不会形成产品强制执行的限制。
4. **查看可用的记录。** 检查活动记录和合规记录，确认测试的哪些部分可以还原。记录任何缺失的记录。

把结果与你的安全团队批准的要求进行比较。在把该工作流用于受影响的数据之前，解决所需限制或记录方面的任何差距。

## 可用的管理员控制项

| **领域** | **管理员能力** |
| --- | --- |
| dots 访问权限 | 通过工作区权限授予或撤销 dots 访问权限。 |
| 云端与所连接的本地计算机 | 控制「使用浏览器」「允许网络访问」「允许使用计算机」「使用密码管理器」以及本地计算机访问。 |
| Wallet | 为符合条件的成员授予 Wallet 访问权限。在企业工作区中默认关闭。 |
| 消息与参与 | 启用或停用 Slack 参与。 |
| 连接的应用 | 通过[插件控制](https://learn.chatgpt.com/codex/enterprise/apps-and-connectors)设置可用的应用和允许的操作。 |
| 自定义 dot 规则 | 禁用后，成员无法添加或编辑自定义规则，已保存的规则也不会生效。 |
| 模型 | 企业模型控制项和默认设置不适用于主 dot。请单独检查委派的 Work 和 Codex 任务。 |

关于仍在开发中的云端浏览器站点规则和控制项，见[浏览器、网络与设备访问](https://learn.chatgpt.com/codex/enterprise/dots-security#review-browser-network-and-device-access)。关于所连接的计算机和委派任务，见[按工作环境划分的控制项](https://learn.chatgpt.com/codex/enterprise/dots-security#controls-by-work-environment)。

## 查看可用性与数据要求

在启用 dots 之前，请在[dot 入门](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)中查看当前的可用情况，以及设置过程中显示的工作区提示。当前各地区的可用情况和覆盖范围，请使用帮助中心的 [ChatGPT 数据驻留与推理驻留](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)；其他推广方面的考虑，见安全指南的[资格与数据要求](https://learn.chatgpt.com/codex/enterprise/dots-security#confirm-eligibility-and-data-requirements)。在启用访问权限之前，请确认你的工作区配置、任何适用的商业伙伴协议（BAA）以及预期的工作流都符合你所在组织的要求。

请检查 dot 本身、它委派给 Work 或 Codex 的任务，以及任何所连接的计算机的要求。关于云端浏览器、网络和计算机使用，见[云端安全](https://learn.chatgpt.com/codex/enterprise/chatgpt-work-cloud-security)。关于在员工设备上的工作，见[本地计算机访问](https://learn.chatgpt.com/codex/enterprise/cloud-local-access)。

## 在工作区中管理 dots

打开 **管理控制台** > **Dots**，查看你的工作区中创建的个人 dot。用这份清单找到某个 dot，查看其所有者和状态，然后打开它的详情进行管理。

### 查看 dot 的详情

详情包括创建该 dot 的成员、它的活动或暂停状态、它的身份，以及它的 Slack 连接状态。身份是该 dot 的服务账号，如果没有服务账号，则为它的 dot ID。连接状态显示 Slack 是否已连接；[消息权限](#3-configure-communication-channels)控制谁能建立该连接。

### 暂停与恢复 dot

当你需要临时停止某个 dot 时，可以从管理控制台暂停它。管理员暂停会阻止成员自行恢复该 dot。请在清单中确认其状态为已暂停。

恢复 dot 会恢复它之前的用户状态。原本处于活动状态的 dot 会重新变为活动状态；成员此前已暂停的 dot 则保持暂停。管理员暂停期间计费停止，如果 dot 回到活动状态则恢复计费。

### 删除 dot

当某个 dot 应从工作区中移除时，可以从管理控制台删除它。删除完成后，它不再出现在清单中，计费也暂停。删除会移除该 dot 的上下文；它不会保留该 dot 以便日后恢复。

dot 创建的文件、Codex 对话串和 ChatGPT 对话是分开存储的，不会随 dot 一起删除。需要时，请在各自的存放位置查看并删除这些内容。如果你想保留 dot 以便日后恢复，请使用暂停。

### 撤销与恢复访问权限

要移除某位成员使用 dots 的权限，请查看工作区默认设置以及直接分配或通过群组分配的每一个角色。移除每一处适用的 **使用 dots** 授权。如果另一个角色仍然授予该权限，仅关闭某一个角色的权限并不会移除访问。

| 变更 | dot 会受到什么影响 | 需要检查什么 |
| --- | --- | --- |
| 撤销成员的 dots 权限 | 该 dot 对成员隐藏、被暂停，并在清单中显示为已禁用。计费停止。权限被撤销期间该 dot 无法恢复。 | 检查成员实际生效的权限，以及该 dot 在清单中的状态。 |
| 恢复成员的 dots 权限 | 该 dot 回到它之前的用户状态。如果原本是活动状态，它会重新变为活动状态，计费恢复。 | 检查恢复后的权限，以及该 dot 是活动状态还是仍由用户暂停。 |

在处理离职时，也请查看[管理访问权限的变更](#manage-access-changes)中的连接和委派工作。

## 监控用量

工作区分析包括已启用 dot 的数量和 dots 的总活跃用户数。已启用的 dot 是未被暂停的 dot。把这两项指标结合起来，可以了解有多少 dot 已启用、有多少人在使用它们。

要按成员或工作区生成每日报告，请使用 [Analytics API](https://learn.chatgpt.com/codex/enterprise/analytics-api)。每日用量端点 `/v1/analytics/workspaces/{workspace_id}/usage` 会用 `client_id = DOTS` 标识 dots。

dot 在 Work 或 Codex 中启动或管理的任务计入这些产品各自的用量限额，并出现在它们的报告中。查看用量时请把这些任务算进去。可用的控制项见 [Work 用量与成本](https://learn.chatgpt.com/codex/enterprise/chatgpt-work-usage-and-cost)；设置预算时，请查看你所用套餐的当前条款。

## 查看管理员活动与合规记录

审计日志会记录管理员对 dots 的操作，包括暂停、恢复、删除、管理和保存层级变更。用这些记录查看管理员所做的更改。

要调查 dot 做过的工作，请使用 [Compliance API](https://learn.chatgpt.com/codex/enterprise/compliance-api#confirm-the-administration-boundaries)。受支持的 dots 记录包括用户提示词和回复、受支持的工具调用事件，以及连接应用的 MCP 调用和结果。归属于 dots 的记录使用 `client_id = DOTS`；在可用时，agent 对象包含 dot ID、名称和类型。

工作区所有者或管理员可以在管理控制台中选择自己的工作区，然后打开 **凭据** > **管理员密钥**，创建一个具有相应可用权限的密钥：用于统一用量报告的 `enterprise.analytics.usage.read`，或用于 dots 合规记录的 `CODEX_LOG` 访问权限。在支持的地方，只有工作区所有者可以授予广泛的合规权限或 **对话消息** 访问权限。使用 [Admin API 参考](https://chatgpt.com/public/admin/api-reference)列出并下载合规 JSONL 文件，以及筛选 `client_id = DOTS` 的记录。

### 为调查检查记录

把一个无害的测试操作与可用的导出记录进行比对。检查记录是否能标识用户、dot、发起的请求、工具、适用的批准以及结果。记录缺失的字段和事件。请求了工具调用并不代表操作已完成；请用接收服务的记录确认结果。

请根据其中所含消息和连接数据的敏感程度，保护下载的记录。

## 管理访问权限的变更

当有人换岗或离职时，请检查其 dot 的权限、连接和正在进行的工作：

1. **移除 dots 访问权限。** 查看工作区默认设置以及直接分配或通过群组分配的每一个角色。移除每一处授予访问权限的设置；任何仍然保留的授权都可能让它保持启用。
2. **检查所连接的账号和设备。** 查看插件授权、网站会话、本地计算机访问，以及该 dot 的 Slack 身份。每一项都有自己的设置。
3. **决定正在进行的工作如何处理。** 查看[暂停与删除控制项](#manage-dots-in-your-workspace)，然后分别检查活动任务、重复性计划和委派给 Work 或 Codex 的任务。决定哪些应当停止，以及任何剩余职责应由谁接手。
4. **在需要的地方删除数据。** 访问权限变更和删除是分开的步骤。按照流程删除该 dot 的上下文，以及存放在别处的任何文件或任务。

关于添加和移除工作区成员，见[用户生命周期管理](https://learn.chatgpt.com/codex/enterprise/user-lifecycle)。关于移除 dots 访问权限，见[在 ChatGPT 工作区中管理 dots](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)。

### 记录移除访问权限的结果

完成访问权限变更清单后，记录移除了哪些权限、应用授权、网站会话、计算机连接和消息身份。单独检查活动中的工作和计划，包括委派给 Work 或 Codex 的工作。记录任何仍在进行的工作及其负责人。

移除访问权限并不会撤销已在其他服务中完成的动作。需要撤销某个动作时，请检查接收服务。

### 应对意外操作

从管理控制台暂停该 dot，在清单中确认其暂停状态，并请成员查看受影响的任务。保存任务链接和可用的活动记录，检查涉及的应用或计算机权限，并遵循你所在组织的事件处理流程。能否撤销某个操作，取决于该操作和对应的服务。

## 帮助成员用好 dots

帮助成员选择要委派的工作，并连接他们需要的账号和工具。鼓励他们告诉自己的 dot 做什么、什么时候做，以及谁应该看到结果。

例如，「为我准备一份每周项目更新供我审阅」只是要求一份草稿。「每周五把已批准的更新发布到我们的团队频道」则同时授予了发布权限。成员应检查重要结果，并知道如何查看活动、更改计划和暂停自己的 dot。分享[入门](https://learn.chatgpt.com/codex/dots/getting-started)、[任务与记忆](https://learn.chatgpt.com/codex/dots/tasks-and-memory)和[控制项](https://learn.chatgpt.com/codex/dots/controls)，帮助他们上手。
