---
title: "文档：面向 Teams 和 Enterprise 的 Grok Bot"
linkTitle: "文档：Teams 与 Enterprise"
date: 2026-11-05
originalTitle: "Grok Bot for Teams and Enterprise"
sourceUrl: "https://cursor.com/docs/grok-bot/teams"
altUrls: ["https://docs.x.ai/grok-bot/teams-and-enterprises"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
updatedAt: 2026-11-10
dateNote: "文档不标日期，取收集日期；2026-11-10 发现原文更新，按新版覆盖原文存档：新增管理员的「Bot sharing」设置（Everyone / Admins only）、Slack 中未关联账号的成员使用共享 Bot 及其用量归属等内容；旧译文对应 11-05 版，已移除，待重新翻译"
tags: [安全, 开放与价格, 运行环境, 商业与规模]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：这是管理员部署指南。Teams 套餐默认开启且无法关闭，Enterprise 由管理员开启，并可用「Manage Group Access」限定用户组；Privacy Mode (Legacy) 会完全阻止 Grok Bot。架构上，Grok Bot 是在每用户一个 Firecracker microVM 中运行的计算机使用智能体，桌面和移动端只是聊天、审核与审批的瘦客户端。管理控制涵盖云端智能体委派、模板公开分享、共享 Bot、Agent Email、连接器策略、本地执行上限，以及 Enterprise 专有的网络控制、Team Setup Scripts、Team Secrets、强制 Auto-review、Action Recording、审计日志、OpenTelemetry 导出、数据保留（Bot 60 至 365 天、计算机与消息 30 至 365 天）和成员计算机管理。用户组设置只放宽、不收紧（网络策略除外）；文末给出推荐的安全基线配置，并说明目前没有单独的 Grok Bot 支出上限。

**保留理由**：汇总了团队与企业版各控制项的归属与默认值，并给出推荐配置，是对照看 Teams 与 Enterprise 能力差异的主要资料。

---

Grok Bot 为团队中的每个人提供用于日常工作的常驻 Bot：研究、运营、文档、浏览和自动化。本页面向正在部署 Grok Bot 的团队与组织管理员。安全审查人员应先阅读 [Grok Bot 安全](https://cursor.com/docs/grok-bot/security)和 [Grok Bot 安全常见问题](https://cursor.com/docs/grok-bot/security-faq)。想了解批准模型的成员也应从那里开始。

## 可用范围 {#availability}

| 套餐 | 访问方式 |
| --- | --- |
| 个人 | 包含在每一份付费 Cursor 套餐中，可通过个人 SuperGrok 关联，或通过自助服务 Grok Business 套餐的席位获得 |
| Teams | 包含；每位成员都有访问权限，用量按席位额度计算 |
| Enterprise | 从[你的仪表盘](https://cursor.com/dashboard/bot)为团队启用 Grok Bot |

该表说明的是产品访问权限，不是管理员控制项列表。Grok Bot 包含在 Teams 中。若干设置为 **Enterprise 专属**，不会出现在自助服务 Teams 中。[管理员控制项](#admin-controls)会逐一标出。

[套餐与计费](https://cursor.com/help/grok-bot/plans)是套餐与用量的权威对照表。

## 为你的团队启用 Grok Bot {#enabling-grok-bot-for-your-team}

在 Teams 套餐中，Grok Bot 默认启用，每位成员无需管理员操作即可访问。处于 [Privacy Mode (Legacy)](#before-you-roll-out)或[旧的按请求计费套餐](https://cursor.com/docs/models-and-pricing#legacy-request-based-pricing)的团队会保持关闭。没有可以关闭它的开关。

在 Enterprise 套餐中，管理员从 [Cursor 仪表盘中的 Grok Bot](https://cursor.com/dashboard/bot)启用。启用后，你可以向所有团队成员开放访问，或用「Manage Group Access」限制为特定的[组](https://cursor.com/dashboard/members?subtab=groups)。关闭 Grok Bot 会阻止所有成员，但不会删除他们的计算机。

两种套餐的管理员都可以在 Grok Bot 页面用「Invite Team」邀请成员加入。团队中已有的 Cursor 用户会收到一封带下载链接的电子邮件。新用户会收到加入你 Cursor 团队的邀请，方式为电子邮件或邀请链接，邀请中也会指向 Grok Bot。通过 SCIM 管理成员资格的团队只会看到「现有用户」选项。

如果你要在受管设备上自行安装桌面应用并规划更新，参见[将 Grok Bot 部署到你的组织](https://cursor.com/docs/grok-bot/deployment)。

## 部署之前 {#before-you-roll-out}

- **停用 Privacy Mode (Legacy)。** 该设置会完全阻止 Grok Bot，启用前系统会提示你更改。请在 Team Settings 中检查隐私设置。
- **为共享出站地址做规划。** 如果你的公司按源 IP 限制服务，参见[静态出站 IP](https://cursor.com/docs/grok-bot/security#static-egress-ips)。
- **清理你的网关。** 如果成员设备位于 Zscaler 或其他 TLS 检查代理之后，请允许 Cursor 的域名（包括嵌套的 `*.*.cursorvm.com` 模式），并在成员连接前将它们排除在检查之外。参见[配置 TLS 检查代理](https://cursor.com/docs/grok-bot/proxies)。
- **决定成员如何从计算机登录公司工具。** 参见[身份与登录](https://cursor.com/docs/grok-bot/security#identity-and-sign-ins)。
- **审查 Grok Bot 继承的策略**：所有套餐上的 Team Rules 和连接器策略，以及 Enterprise 上的团队 Auto-review 规则和 MCP 允许列表。

## 架构 {#architecture}

### Grok Bot 如何构建 {#how-grok-bot-is-built}

Grok Bot 是一个计算机使用智能体（computer-use agent），负责操作应用、浏览器和开发环境。它运行在 Cursor 的云中，每个用户的工作都在一台专用的云计算机上执行。桌面和移动应用是用于聊天、审阅和批准的瘦客户端。

安全模型基于四项原则：

- **按用户隔离。** 每个用户的工作都在一台专用的 Firecracker microVM 中运行，这是一种与其他用户有硬件级隔离的微型虚拟机。
- **默认无访问权限。** Bot 只能使用用户或团队授予它的账号和已连接应用。
- **人工批准关卡。** 敏感操作需要用户批准，由名为 Auto Review 的独立审查模型评估。
- **管理控制。** 团队管理员可以设置 Team Rules、Cloud Agent 委派、模板共享和本地执行上限。网络控制（Network Controls）、Team Setup Scripts、Team Secrets、Allow Local Egress Routing、Allow Sudo on Bot Computers、Action Recording、Enforce Auto-review、Auto-review 规则以及组织级启用开关为 Enterprise 专属。

各部分这样组合在一起：

1. **本地设备。** 聊天、审阅和批准发生在成员的设备上。工作则在托管的计算机中运行。可选的[本地执行](https://cursor.com/docs/grok-bot/security#local-execution)默认要求逐条命令批准，也可以关闭。
2. **环境。** 每个用户一台持久的 Firecracker microVM。该用户运行的每个 Bot 都共享这台计算机。管理员从 [Cursor 仪表盘](https://cursor.com/dashboard/bot)的 Grok Bot 页面管理 Grok Bot。团队管理员可以使用 Team Rules、Cloud Agent 委派、公开模板共享和 Execution on Local Computer。该页面上 **Enterprise 专属**的内容包括：组织级启用开关、Network Controls、Team Setup Scripts、Team Secrets、Allow Local Egress Routing、Allow Sudo on Bot Computers、Action Recording、Enforce Auto-review、Auto-review 规则和计算机管理。成员永远看不到这个页面。
3. **Bot。** 在托管计算机内执行 shell、浏览器和计算机操作。Bot 默认没有访问权限，只在成员为它登录账号后才行动。它从成员的 Vault、已连接的密码管理器或安全表单（Secure Form）中填入登录信息和卡，但看不到这些值，并把单点登录和通行密钥（passkeys）等步骤交给成员。
4. **已连接的应用。** 你团队的 Cursor MCP（Model Context Protocol）策略完整适用，允许或阻止每个连接器。OAuth 令牌留在 Cursor 的连接器后端，Bot 调用工具时不会收到令牌。
5. **Cloud Agents。** Grok Bot 可以在你现有的 [Cloud Agent](https://cursor.com/docs/cloud-agent)控制下，把编码任务委派给单独的计算机。管理员可以禁止创建。
6. **模型与数据。** Grok Bot 负责选择模型。启用 Privacy Mode 时，客户数据不用于训练；Cursor 在其服务器上执行这一规则，当该设置无法验证时，系统默认不进行训练。

### 用户如何隔离 {#how-users-are-isolated}

每个用户获得一台具有硬件级隔离的专用计算机，一个用户无法访问另一个用户的计算机。每台计算机是一台 Firecracker microVM，拥有自己的内核、内存和虚拟设备。

在一个用户内部，边界不同：该用户的所有 Bot 共享一台计算机，Bot 隔离的是人格和工作区，而不是计算资源。请把计算机上的登录状态或文件视为该用户运行的每个 Bot 都能访问，让浏览器退出 Bot 不再需要的账号，并在工作完成后移除敏感的临时文件。当某个工作负载需要自己的计算机和凭据集时，为它单独分配一个 Cursor 用户。

[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)是「每个用户一个 Bot」的例外。Bot 分为个人和共享两种：成员把云端托管的 Bot 共享给团队中的所有人，或只共享给特定的人和组，这些成员可以与它聊天。每个成员的聊天都是私密的，所有者和 Bot 的 Manager 也无法读取。在成员自己的聊天或 Slack 私信中，Bot 通常在该成员的计算机上工作，询问后使用该成员已连接的账号，并使用该成员的 Grok Bot 用量。在 Slack 频道、线程、群组私信和群聊中，共享 Bot 使用它自己的一台计算机。所有者或 Manager 添加到共享 Bot 的秘密、应用和文件，会在每位队友的聊天中可用。

## 管理员控制项 {#admin-controls}

大多数 Grok Bot 设置位于 [Cursor 仪表盘](https://cursor.com/dashboard/bot)的 Grok Bot 页面，只有管理员能看到。少数设置位于 Team Settings、你的 Team Marketplace 或你的身份提供商中。有些控制项仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供；其余在 Teams 和 Enterprise 中提供。Enterprise 团队还可以从某个组的 Grok Bot 标签页为一组人群放宽其中若干控制项；参见[组设置](#group-settings)。

### 访问与身份 {#access-and-identity}

谁可以使用 Grok Bot，以及成员如何被配置。

#### 启用 Grok Bot {#enable-grok-bot}

Grok Bot 页面上的组织级开关，旁边是 **Manage Group Access**。打开它会弹出一个设置对话框，涵盖隐私模式、计费和模型可用性，并在 Cloud Agents 关闭时提供开启选项，还会要求你接受 Grok Bot 条款。关闭它会阻止所有成员，但不会删除他们的计算机。参见[为你的团队启用 Grok Bot](#enabling-grok-bot-for-your-team)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### SCIM {#scim}

通过你的身份提供商进行 SCIM 2.0 配置和取消配置。成员使用其 Cursor 账号登录 Grok Bot，因此你现有的 [SCIM](https://cursor.com/docs/account/teams/scim)和 SSO 设置会延续适用。Okta 和 Entra ID 的步骤（包括应用分配和计算机浏览器的登录规则）参见[配置身份与访问](https://cursor.com/docs/grok-bot/identity)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### 团队图标 {#team-icon}

Grok Bot 为整个团队显示的图片，例如成员向所有人共享 Bot 时。管理员可以在 Team Settings 的 Team Profile 部分上传、更改或移除它。请使用不超过 2 MB 的 PNG、JPEG 或 WebP。

### 智能体能力 {#agent-capabilities}

Bot 可以代表成员做什么。每项控制都适用于每位成员的 Bot。

#### Cloud Agents {#cloud-agents}

允许或阻止 Bot 把编码任务委派给 Cursor [Cloud Agents](https://cursor.com/docs/cloud-agent)。开关位于 Grok Bot 页面，适用于整个团队，默认开启。委派的工作会在你现有 Cloud Agent 控制下的单独计算机上运行。当你的团队不需要委派时，请关闭它。

#### 公开模板共享 {#public-template-sharing}

控制成员是否可以在团队之外发布 Bot 模板。关闭后共享仅限团队内，Cursor 会在其服务器上执行该策略，包括对已经公开的模板。Enterprise 团队默认关闭公开共享；其他团队默认允许。共享模板包含什么，参见[共享 Bot](https://cursor.com/docs/grok-bot/work#share-a-bot)。

#### Bot 共享 {#bot-sharing}

控制谁可以与队友共享 Bot。在 Grok Bot 页面的 **Sharing** 下找到 **Bot sharing**，选择 **Everyone** 或 **Admins only**。**Everyone** 是默认值。设为 **Admins only** 时，成员会看到 **Only team admins can share Bots**，且 **Share** 控件对他们禁用；Cursor 会在其服务器上执行这一限制。已经共享的 Bot 保持共享，管理员在 **Manage Bots** 中设置的访问权限仍然适用。参见[谁可以共享 Bot？](https://cursor.com/help/grok-bot/shared-bots#who-can-share-bots)

#### Allow Shared Logins {#allow-shared-logins}

允许共享 Bot 的 Manager 把自己的应用登录信息作为共享连接器共享。在 Grok Bot 页面的 **Sharing** 下找到 **Allow Shared Logins**。它默认关闭。开启后，所有使用该 Bot 的人都通过该 Manager 的账号行事，包括 Bot 所做的更改。关闭时，Manager 会看到 **Your admin has turned off sharing logins with Bots**。参见[共享连接器如何工作？](https://cursor.com/help/grok-bot/shared-bots#how-do-shared-connectors-work)

#### Slack 工作区访问 {#slack-workspace-access}

允许你 Slack 工作区中不属于该团队的成员在 Slack 中使用共享 Bot，无需关联 Cursor 账号。它适用于共享给你组织的 Bot，或共享给团队的 Bot（当该团队是组织唯一的团队或不属于任何组织时）。他们的回复使用团队的用量。Slack 访客和 Slack Connect 频道永远不在范围内。在 Grok Bot 页面的 **Sharing** 下找到 **Slack Workspace Access**。它默认开启。在组织中，由组织管理员为每个团队设置。该设置会在到达你的团队时出现。参见[谁可以在 Slack 中与共享 Bot 对话？](https://cursor.com/help/grok-bot/shared-bots#who-can-talk-to-a-shared-bot-in-slack)

#### 管理 Bot {#manage-bots}

列出你团队中的每个 Bot。在 Grok Bot 页面的 **Shared Bots** 下打开 **Manage Bots**，按共享范围或所有者筛选列表。**Access** 列显示谁可以使用每个[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)，例如整个团队、特定的人或组，或仅其所有者。点击它可以更改谁有访问权限。在 Bot 的 **Auto-add** 列中，选择 **All team** 或一个或多个组，把 Bot 添加到这些成员的侧边栏，或清除该设置。自动添加只适用于有访问权限的组。通过这种方式获得 Bot 的成员无法从侧边栏隐藏它。管理员可以在这里删除任何 Bot。删除 Bot 会为所有使用它的人移除该 Bot 及其 Slack 应用，且无法撤销。组在 Members & Groups 页面管理。

#### 页面共享 {#page-sharing}

控制成员如何在团队内共享[页面（Pages）](https://cursor.com/help/grok-bot/pages)。在 Grok Bot 页面的 **Sharing** 下找到 **Page sharing**，选择 **Anyone on the team**、**Specific teammates** 或 **Off**。**Anyone on the team** 是默认值。收紧设置时，已经共享的页面保持共享。该控件会在 Pages 到达你的团队时出现。

#### Agent Email {#agent-email}

允许成员领取一个 `mail.grokbot.com` 地址，其 Bot 可以读取邮件并从中发送邮件。开关位于 Grok Bot 页面的 **Bot Capabilities** 下，默认关闭；在开启之前，成员没有电子邮件工具。当成员在聊天中请求一个邮箱时，只要 Auto-review 允许或成员批准，就会发送。Bot 自行撰写的电子邮件（包括来自例程的邮件）会作为草稿等待，直到成员按下 **Send**。简报和首次联系的邮件会包含退订链接，收到的邮件只通过成员设置的例程处理。关闭它会移除 Bot 的电子邮件工具并停止邮件例程；已有地址仍会继续接收邮件。参见[给你的 Bot 一个电子邮件地址](https://cursor.com/help/grok-bot/agent-email)。

#### 连接器策略 {#connector-policy}

Grok Bot 继承你团队的 Cursor 连接器策略。没有单独的 Grok Bot 连接器列表，成员在 Grok Bot 的 **Connect apps** 下找到允许的连接器。请在仪表盘的 [Plugins & MCPs 页面](https://cursor.com/dashboard/plugins)的 Team Marketplace 中设置成员可以使用哪些服务器，而不是在 Grok Bot 页面设置。MCP 允许列表为 Enterprise 专属；参见 [MCP 服务器信任管理](https://cursor.com/docs/enterprise/model-and-integration-management#mcp-server-trust-management)。任何被允许的连接器都可供成员运行的每个 Bot 使用，被阻止的连接器会显示为 **Disabled by team admin**。目前无法向成员推送连接器，无论强制还是默认开启。如果你的团队使用允许列表网络策略，并希望远程 MCP 服务器也遵守同一列表，请在 **Network** 下开启 **Apply to MCP servers**；它默认关闭。参见 [MCP 服务器与网络策略](https://cursor.com/docs/grok-bot/security#mcp-servers-and-the-network-policy)。

#### 在本地计算机上执行 {#execution-on-local-computer}

限制 Bot 通过桌面应用在成员自己的设备上可以做什么：打开文件和运行任务。在 Grok Bot 页面选择 **Always allow**、**Ask every time** 或 **Never allow**。默认值 **Always allow** 把选择权留给每位成员，成员自己的设置默认是每个任务前询问。**Ask every time** 会让每个本地任务都请求批准，**Never allow** 则为整个团队关闭本地执行。当成员自己的设置比团队设置更严格时，仍以成员设置为准。除非 Bot 有明确理由在成员设备上工作，否则请选择 **Never allow**。参见[本地执行](https://cursor.com/docs/grok-bot/security#local-execution)。

#### Allow Local Egress Routing {#allow-local-egress-routing}

让成员通过自己的计算机路由 Grok Bot 的 Web 流量。关闭后，Grok Bot 中的该选项不可用。开关位于 Grok Bot 页面的 **Bot Computers** 下，默认开启。关闭后，活动路由会在五分钟内停止。重新开启会恢复每位成员之前的选择。参见[通过桌面路由流量](https://cursor.com/docs/grok-bot/settings#route-traffic-through-your-desktop)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

### 规则与批准 {#rules-and-approvals}

Bot 遵循的指引，以及阻止操作和模型请求的审查层。

#### Team Rules {#team-rules}

每位成员的 Bot 都遵循的规则。从 Grok Bot 页面添加，并把每条规则的作用范围设为 Cursor、Grok Bot 或两者。应用于 Grok Bot 的规则始终是必需的，成员无法关闭。规则要简短且数量少，例如「绝不把公司数据转移到个人账号」。规则为 Bot 提供指引；批准行为请使用 [Auto-review 规则](#auto-review-rules)。属于某一组人群的指引，请在[组设置](#group-settings)下添加 Group Rules。

#### Enforce Auto-review {#enforce-auto-review}

阻止成员关闭 Auto-review。开关位于 Grok Bot 页面，默认关闭。开启后，Bot 在运行风险操作前总会先检查，并在需要时请求批准。这包括在无人能回答批准的聊天中的共享 Bot，否则它们会在没有 Auto-review 的情况下运行。在依赖团队 Auto-review 规则之前，请先开启它。组可以用 **Don't enforce for this group** 为其成员解除锁定；参见[组设置](#group-settings)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### Auto-review 规则 {#auto-review-rules}

团队范围的「Ask first」和「Allow automatically」规则，在每位成员自己的规则之上，适用于其所有 Bot。在 Grok Bot 页面用「Configure Rules」添加；更改会自动保存。成员可以在「Settings」>「General」>「Auto-review」下看到团队规则，但不能编辑或删除，规则冲突时「Ask first」优先。关闭强制执行后，团队规则不再适用。参见[批准与 Auto Review](https://cursor.com/docs/grok-bot/security#approvals-and-auto-review)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### Inference Hooks {#inference-hooks}

把每个经过签名的 Grok Bot 模型请求发送到你组织运行或通过安全供应商使用的 AI 安全服务器。你的服务器在模型运行前允许或拒绝该请求。从 Grok Bot 页面的 **Security & Compliance** 打开 [Inference Hooks](https://cursor.com/dashboard/bot/inference-hooks)。新配置从影子模式（Shadow mode）开始，它会把拒绝记录到审计日志中，但不阻止成员。推理钩子（Inference hooks）处于 beta 阶段，所有 Enterprise 团队均可使用。参见 [Grok Bot 推理钩子](https://cursor.com/docs/grok-bot/inference-hooks)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

### 计算机与网络 {#computers-and-network}

团队计算机如何设置、可以访问什么，以及如何重建或终止它们。

#### 网络控制 {#network-controls}

限制团队计算机可以访问哪些目的地。在 Grok Bot 页面的 **Network** 下找到 **Grok Bot Network Access**。选择 **Allow All Network Access**、**Defaults + Team Allowlist** 或 **Team Allowlist Only**，并为允许列表模式列出域名和 IP 范围。目录组可以有自己的策略，锁定后团队策略会适用于所有人。没有策略的团队默认允许全部。各模式以及新策略如何到达运行中的计算机，参见[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)。

在允许列表模式下，目的地列表下方会出现 **Apply to MCP servers** 开关。它默认关闭。开启后，每个已连接的应用（包括 GitHub、X 和 Origin 等内置连接器）都必须根据其发送请求的主机匹配一个允许的目的地，Bot 与不匹配应用的连接会被拒绝。命令服务器不受影响。每个内置连接器需要哪些主机，参见 [MCP 服务器与网络策略](https://cursor.com/docs/grok-bot/security#mcp-servers-and-the-network-policy)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### Team Setup Scripts {#team-setup-scripts}

安装脚本清单，会在每台团队计算机上运行，使各处都有相同的工具。在 Grok Bot 页面的 **Bot Computers** 下找到 **Team Setup Scripts**。不要在设置脚本中放入秘密值；当脚本需要凭据时，把它存为 [Team Secret](#team-secrets) 并从环境中读取。成员在应用中看不到这些脚本。清单如何运行，以及如何安装访问私有服务的网络客户端，参见[连接到私有网络](https://cursor.com/docs/grok-bot/private-networks)。如果只在一组人群的计算机上运行额外脚本，请在[组设置](#group-settings)下添加。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### Team Secrets {#team-secrets}

团队范围的值，Team Setup 脚本会将其作为环境变量读取，这样脚本可以持有许可证密钥、认证密钥或服务令牌，而值不会出现在清单中。在 Grok Bot 页面的 **Team Secrets** 下添加：每个秘密由一个环境变量名和一个值组成。Cursor 会加密存储该值，保存后仪表盘不会再显示它。团队管理员（包括未付费管理员）可以添加、替换或删除它们。

它们如何到达计算机：

- 你的 Team Setup 清单以及组 [Setup Scripts](#group-settings) 中的每个 Setup Script 和 Check Script，都会在其环境中带着团队的秘密运行。按名称引用秘密，例如 `"$MY_LICENSE_KEY"`。
- 秘密只存在于脚本的进程环境中。脚本结束后，除非脚本把它写到某处，否则该值就消失了，因此不要在计算机上存储任何你不希望该成员运行的每个 Bot 都能访问的内容。
- 脚本输出在记录前会检查是否包含秘密值，匹配到的内容会被遮蔽。
- 计算机只有在 Team Setup 恰好来自一个团队时才会收到秘密。如果某位成员的计算机应用了两个或更多团队的设置，它不会从其中任何一个团队获得秘密，因为不同团队的脚本共享同一个计算机用户。
- 更改（包括轮换后的值）会在脚本下次运行时生效：计算机启动时、定期刷新时，或你重建它时。参见[推广到现有计算机](https://cursor.com/docs/grok-bot/private-networks#roll-out-to-existing-computers)。

限制：每个团队最多 100 个秘密，每个值最多 32 KB，总计最多 96 KB。名称必须是有效的环境变量名，计算机运行时保留的名称（例如 `PATH`、`HOME`，以及任何以 `SAND_` 或 `LD_` 开头的名称）在保存时会被拒绝。Team Secrets 用于你控制的脚本。它们不会直接让 Bot 获得某个值，并且与[成员存储在 Bot 上的秘密](https://cursor.com/help/grok-bot/secrets)是分开的。它们不能通过 Admin API 使用。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### 允许在 Bot 计算机上使用 Sudo {#allow-sudo-on-bot-computers}

允许 Bot 在其自己的计算机上以 root 身份运行命令。开关位于 Grok Bot 页面的 **Bot Computers** 下，默认开启。现有计算机会在重启后应用更改。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### 管理成员计算机与数据 {#manage-member-computers-and-data}

允许管理员一次重建、终止或永久删除许多成员的计算机，或删除他们的全部 Grok Bot 数据，并为每位成员给出结果。在 Grok Bot 页面的 **Security & Compliance** 下找到它。重建会把成员迁移到最新镜像和 Team Setup Scripts，同时保留他们的 Bot、文件和登录信息。终止会结束成员当前的工作并保留持久磁盘；该成员的下一次会话会在其上启动一台新计算机。删除会移除计算机及其存储的文件，成员的下一次会话会启动一台空计算机。要自动删除不活跃的计算机，请使用[计算机保留期](#data-retention)。这些操作都不会移除访问权限：要移除访问权限，请把成员从团队中移除，或为其所在组关闭 Grok Bot，并在你的身份提供商中撤销其会话。参见[管理 Grok Bot 计算机](https://cursor.com/docs/grok-bot/computers)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

### 数据保留 {#data-retention}

在 Grok Bot 数据超过你选择的期限后自动删除它们。这些设置位于 Grok Bot 页面的 **Data Retention** 下。每项默认关闭。

| 设置 | 删除什么 | 期限 |
| --- | --- | --- |
| **Retention Period for Bots** | 在期限内无人发过消息的 Bot，连同其对话、记忆、技能和例程。Bot 的所有者会在删除前 30 天收到电子邮件，在该窗口内发一条消息即可保留 Bot。 | 60 至 365 天 |
| **Retention Period for Computers** | 当某位成员的所有 Bot 在期限内都无人发消息后，该成员的计算机及其文件。参见[自动删除不活跃的计算机](https://cursor.com/docs/grok-bot/computers#delete-inactive-computers-automatically)。 | 30 至 365 天 |
| **Retention Period for Messages** | 超过期限的 Bot 消息和附件，每天执行。不会通知任何人。 | 30 至 365 天 |

开启某项设置或缩短其期限时，会先要求你确认。已删除的数据无法恢复。每次更改和删除都会记录在[审计日志](https://cursor.com/dashboard/audit-log)中。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

### 日志与审计 {#logging-and-audit}

记录什么，以及记录到哪里。

#### Action Recording {#action-recording}

记录 Bot 做了什么：每次工具调用及其结果、允许或拒绝该调用的决定（Auto-review、钩子或成员）、连接器（MCP）工具调用、shell 命令、浏览器导航、计算机使用会话、文件传输、Bot 发送的消息、例程运行、护栏干预、它读取的技能，以及它交给子智能体或云智能体的工作。事件都是元数据，在存储或导出前会先清理。Shell 命令会清除秘密；浏览器导航会保留每个页面为 `scheme://host/path` 加标题，但去掉查询字符串和凭据；计算机使用会话记录操作与截图数量以及会话时长，不记录截图、点击或输入的文字；其他每个事件都只带 ID、结果和时长，绝不包含工具参数、文件路径或消息内容。开关位于 Grok Bot 页面，默认关闭。记录的事件不会出现在审计日志页面上。要在你自己的收集器中接收它们，请配置 [OpenTelemetry 导出](https://cursor.com/docs/enterprise/opentelemetry-export)，它会投递每个标记为 `cursor.surface=grok_bot` 的事件；[Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire#shared-grok_bot-attributes)列出了每个事件和属性。保留详情见[日志与审计](https://cursor.com/docs/grok-bot/security#logging-and-audit)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### 审计日志 {#audit-logs}

管理员、安全和认证事件，以及 Grok Bot 控制平面事件：Bot 创建、成员访问权限变更、Team Setup 清单、MCP 认证、Slack 账号关联和例程。每一行都会标明执行操作的应用程序，因此你可以把日志筛选为 Grok Bot。在[审计日志页面](https://cursor.com/dashboard/audit-log)查看，或流式传输到你的 SIEM；参见[审计日志](https://cursor.com/docs/enterprise/compliance-and-monitoring#audit-logs)。Bot 执行的操作，请使用 [Action Recording](#action-recording)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

#### OpenTelemetry 导出 {#opentelemetry-export}

把 Cursor 的使用指标和日志（包括记录的 Grok Bot 操作）流式传输到你运行的收集器。这是获取 Action Recording 事件的客户路径。在 **Team Settings** > **OpenTelemetry Export** 下配置。端点要求和事件模式见 [OpenTelemetry 导出](https://cursor.com/docs/enterprise/opentelemetry-export)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

### 组设置 {#group-settings}

上述控制项设定团队范围的基线。要为一组人群放宽该基线，从 [Members > Groups](https://cursor.com/dashboard/members?subtab=groups)打开你团队拥有的某个组，并使用其 **Grok Bot** 标签页。除网络策略外，组设置只会放宽：组可以授予成员比团队允许的更多权限，绝不会更少，属于多个组的成员会得到最宽松的结果。这与[组模型访问](https://cursor.com/docs/enterprise/model-and-integration-management#how-team-and-group-model-access-combine)的规则相同。组控制项保持在团队值时不会改变任何东西，因此请在 Grok Bot 页面上收紧控制，再按组放宽。

该标签页有四个部分：

- **Bot Capabilities。** 当团队关闭或设置更严格时，为组成员允许 [Cloud Agents](#cloud-agents)、[Agent Email](#agent-email)或 [Allow Local Egress Routing](#allow-local-egress-routing)，或提高 [Execution on Local Computer](#execution-on-local-computer)的上限。对于 Auto-review，**Don't enforce for this group** 会解除团队的 [Enforce Auto-review](#enforce-auto-review)锁定，让组成员可以关闭 Auto-review；组 Auto-review 规则会与团队的 [Auto-review 规则](#auto-review-rules)合并，规则冲突时「Ask first」优先。
- **Network。** 组自己的网络策略，如[网络控制](#network-controls)所述。它会替换组成员的团队策略，无论更宽松还是更严格，属于多个组的成员会得到最严格的策略。锁定的团队策略适用于所有人。**Apply to MCP servers** 只在团队的 Grok Bot 页面上设置；组会继承它，且无法关闭。
- **Group Rules。** 组内 Bot 的规则，与 [Team Rules](#team-rules)合并。成员无法关闭它们。
- **Setup Scripts。** 在组成员计算机上与 [Team Setup Scripts](#team-setup-scripts)一起运行的清单。它们使用相同的结构并以相同方式运行，同样适用禁止秘密的规则，并读取与团队清单相同的 [Team Secrets](#team-secrets)；没有组级秘密。参见[Team Setup 如何运行你的脚本](https://cursor.com/docs/grok-bot/private-networks#how-team-setup-runs-your-scripts)。

组设置适用于你团队拥有的组，无论你手动管理成员资格，还是通过 [SCIM](https://cursor.com/docs/account/teams/scim#directory-groups)同步。它们与[组织组](https://cursor.com/docs/enterprise/organization-groups)是分开的。要控制谁可以使用 Grok Bot，请改用 Grok Bot 页面上的 **Manage Group Access**；参见[为你的团队启用 Grok Bot](#enabling-grok-bot-for-your-team)。

*在 [Enterprise 套餐](https://cursor.com/docs/enterprise)中提供。*

## Admin API {#admin-api}

通过 [Admin API](https://cursor.com/docs/account/teams/admin-api#grok-bot)启用 Grok Bot 并管理能力、Enforce Auto-Review、组访问、网络策略、团队规则和设置脚本。[Team Secrets](#team-secrets)只能从仪表盘管理。

要从脚本重建、终止或删除成员的计算机，或删除他们的全部 Grok Bot 数据，请使用[组织 API](https://cursor.com/docs/account/organizations/organization-admin-api#grok-bot-computers)。它需要具有 `admin:*` 范围的 Organization API 密钥，因为一台计算机服务于成员所属的每个团队。

## 安全 {#security}

安全模型、网络策略、批准与 Auto Review、身份、日志、数据处理和认证见 [Grok Bot 安全](https://cursor.com/docs/grok-bot/security)。常见审查问题见 [Grok Bot 安全常见问题](https://cursor.com/docs/grok-bot/security-faq)。要让你自己的 AI 安全服务器检查每个模型请求，参见 [Grok Bot 推理钩子](https://cursor.com/docs/grok-bot/inference-hooks)。

## 推荐配置 {#recommended-configuration}

对于安全敏感的部署，这是推荐的基线。

面向管理员：

1. **配置网络控制。仅 Enterprise。** 没有策略的团队默认允许全部。自助服务 Teams 无法设置此项。如果你选择允许列表模式，并希望它也覆盖已连接的应用，请把连接器使用的主机（例如 `api.github.com`、`api.x.com`、`api.origin.cursor.com`）加入列表，然后开启 **Apply to MCP servers**；在你开启之前它处于关闭状态。参见 [Grok Bot 安全](https://cursor.com/docs/grok-bot/security#network-policy)。
2. **在启用 Grok Bot 之前，审查 Teams Marketplace 中的连接器策略。** 任何被允许的连接器都可供成员运行的每个 Bot 使用。
3. **在依赖团队规则之前，开启 Enforce Auto-review。仅 Enterprise。** 成员可以在其之上添加更严格的个人规则，规则冲突时「Ask first」优先。
4. **把 Execution on Local Computer 设为 Never allow**，除非 Bot 需要在成员设备上操作。默认值把选择权留给每位成员。
5. **禁用 Cloud Agent 创建**，如果你不需要委派。
6. **保持公开模板共享关闭**，除非成员应当在团队之外发布 Bot 模板。
7. **把 Bot 共享设为 Admins only**，如果共享 Bot 应先经过审查再让队友使用。共享 Bot 会把它所有者的应用、秘密和文件带入每位队友的聊天。
8. **保持 Allow Shared Logins 关闭**，除非某个共享 Bot 应当通过一位 Manager 的账号为所有使用者行事。
9. **添加团队 Auto-review 规则。仅 Enterprise。** 覆盖那些应始终先询问或可以自动继续的操作。生产部署、外部电子邮件、付款和接受法律条款是很好的「Ask first」例子。自动规则要保持范围狭窄。
10. **通过你的身份提供商限制登录到受管设备。** Grok Bot 登录使用你的 SSO，因此感知设备的登录策略会适用于它。这限制的是登录，而不是托管计算机本身。

面向成员：

1. **绝不要把凭据粘贴到聊天中。** 受支持的路径是使用遮蔽的秘密请求。
2. **对于涉及账号、金钱或共享资源的操作，优先选择 Allow once 而不是 Always allow。**
3. **让 Bot 的浏览器登录与任务规模相称的账号**，并让它退出不再需要的账号。在源系统支持时，使用范围受限的服务账号。
4. **新角色先从只读任务和草稿输出开始**，并让发送、发布、购买、删除和生产环境更改始终处于批准之后。
5. **定期审查已连接的应用和活动例程**，并在例程的源系统发生变化时暂停该例程。

## 常见问题 {#faq}

### 我可以为我的团队开启或关闭 Grok Bot 吗？

组织级的 **Enable Grok Bot** 开关仅限 Enterprise。它位于 Cursor 仪表盘的 Grok Bot 页面。自助服务 Teams 没有这个开关。禁用会阻止成员，但不会删除他们的计算机。

### 我可以通过 Admin API 管理 Grok Bot 吗？

可以。使用 [Admin API](https://cursor.com/docs/account/teams/admin-api#grok-bot)。

### 我可以设置 Grok Bot 支出上限吗？

目前没有单独的 Grok Bot 支出上限。账号级的按需控制适用，各产品的拆分在仪表盘用量页面上。

### 为什么成员看到某个应用显示为 Disabled by team admin？

你团队的连接器策略阻止了该服务器。在 **Teams Marketplace** 中启用它，如果你使用 MCP 允许列表，把其服务器 URL 加入允许列表，然后让该成员重启应用。如果某个被允许的应用对普通成员仍然失败并报供应商侧权限错误，请检查提供商的要求；有些供应商把其 MCP 端点限制为仅其自己的管理员可用。参见[连接应用](https://cursor.com/help/grok-bot/connect-apps)。

### 成员如何请求访问权限？

成员可以从应用发送请求。在管理员尚未完成设置的组织级 Enterprise 团队中，成员会看到团队设置消息。下一步是管理员使用 Enterprise 专属的启用开关。自助服务 Teams 不使用该开关。

### 我可以看到我的团队用 Grok Bot 做什么类型的工作吗？

可以，在所有 Enterprise 团队中。Analytics 仪表盘的 Conversation Insights 页面有一个 **Grok Bot** 来源，按 Type of Work 和 Level of Automation 对 Bot 对话分组。参见 [Grok Bot Conversation Insights](https://cursor.com/docs/account/teams/analytics#grok-bot-conversation-insights)。

隔离、出站、批准、日志和数据处理方面的问题见 [Grok Bot 安全常见问题](https://cursor.com/docs/grok-bot/security-faq)。
