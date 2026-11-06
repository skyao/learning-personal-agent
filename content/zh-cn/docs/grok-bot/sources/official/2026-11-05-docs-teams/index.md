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
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 开放与价格, 运行环境, 商业与规模]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：这是管理员部署指南。Teams 套餐默认开启且无法关闭，Enterprise 由管理员开启，并可用「Manage Group Access」限定用户组；Privacy Mode (Legacy) 会完全阻止 Grok Bot。架构上，Grok Bot 是在每用户一个 Firecracker microVM 中运行的计算机使用智能体，桌面和移动端只是聊天、审核与审批的瘦客户端。管理控制涵盖云端智能体委派、模板公开分享、共享 Bot、Agent Email、连接器策略、本地执行上限，以及 Enterprise 专有的网络控制、Team Setup Scripts、Team Secrets、强制 Auto-review、Action Recording、审计日志、OpenTelemetry 导出、数据保留（Bot 60 至 365 天、计算机与消息 30 至 365 天）和成员计算机管理。用户组设置只放宽、不收紧（网络策略除外）；文末给出推荐的安全基线配置，并说明目前没有单独的 Grok Bot 支出上限。

**保留理由**：汇总了团队与企业版各控制项的归属与默认值，并给出推荐配置，是对照看 Teams 与 Enterprise 能力差异的主要资料。

---

Grok Bot 为团队中的每个人提供用于日常工作的常驻 Bot：研究、运营、文档、浏览和自动化。本页面向正在团队和组织中推广 Grok Bot 的团队与组织管理员。安全审查人员应先阅读 [Grok Bot 安全](https://cursor.com/docs/grok-bot/security) 和 [Grok Bot 安全常见问题](https://cursor.com/docs/grok-bot/security-faq)。想了解审批模型的成员也应从那里开始。

## 可用性

| 套餐 | 访问方式 |
| --- | --- |
| 个人（Individuals） | 包含在每个付费 Cursor 套餐中，可通过个人 SuperGrok 链接获得，或在自助式 Grok Business 套餐中占用一个席位 |
| 团队（Teams） | 已包含；每位成员都有访问权限，用量遵循席位的额度 |
| 企业（Enterprise） | 从[你的仪表板](https://cursor.com/dashboard/bot)为团队启用 Grok Bot |

该表说明的是产品访问权限，不是管理员控制项清单。Grok Bot 已包含在 Teams 中。若干设置**仅限 Enterprise**，不会出现在自助式 Teams 中。[管理员控制](#admin-controls) 会逐项标注。

[套餐与计费](https://cursor.com/help/grok-bot/plans) 是套餐与用量的权威对照表。

## 为团队启用 Grok Bot

在 Teams 套餐中，Grok Bot 默认启用，每位成员无需任何管理员操作即可访问。对于处于[隐私模式（旧版）（Privacy Mode (Legacy)）](#before-you-roll-out)或[旧的基于请求的套餐](https://cursor.com/docs/models-and-pricing#legacy-request-based-pricing)的团队，它保持关闭。没有可以将其关闭的开关。

在 Enterprise 套餐中，管理员从 [Cursor 仪表板中的 Grok Bot](https://cursor.com/dashboard/bot) 启用它。启用后，你可以授予所有团队成员访问权限，或用「管理用户组访问权限（Manage Group Access）」将其限制到特定[用户组](https://cursor.com/dashboard/members?subtab=groups)。关闭 Grok Bot 会阻止所有成员，但不会删除他们的计算机。

两种套餐的管理员都可以在 Grok Bot 页面用「邀请团队（Invite Team）」引入成员。团队中已有的 Cursor 用户会收到一封包含下载链接的电子邮件。新用户会收到加入你的 Cursor 团队的邀请（通过电子邮件或邀请链接），其中也会指向 Grok Bot。通过 SCIM 管理成员资格的团队只会看到现有用户选项。

若要在受管设备上自行安装桌面应用并规划更新，请参阅[将 Grok Bot 部署到你的组织](https://cursor.com/docs/grok-bot/deployment)。

## 推广之前

- **迁离隐私模式（旧版）。** 该设置会完全阻止 Grok Bot，系统会在启用前提示你更改。请在团队设置中检查隐私设置。
- **为共享出口地址做规划。** 如果你的公司按源 IP 限制服务，请参阅[静态出口 IP](https://cursor.com/docs/grok-bot/security#static-egress-ips)。
- **清理你的网关。** 如果成员设备位于 Zscaler 或其他 TLS 检查代理之后，请放行 Cursor 的域名（包括嵌套的 `*.*.cursorvm.com` 模式），并在成员连接之前将它们排除在检查之外。请参阅[配置 TLS 检查代理](https://cursor.com/docs/grok-bot/proxies)。
- **决定成员如何从计算机登录公司工具。** 请参阅[身份与登录](https://cursor.com/docs/grok-bot/security#identity-and-sign-ins)。
- **审查 Grok Bot 继承的策略**：所有套餐上的团队规则和连接器策略，以及 Enterprise 上的团队自动审查规则和 MCP 允许列表。

## 架构

### Grok Bot 如何构建

Grok Bot 是一个计算机使用智能体（computer-use agent），负责操作应用程序、浏览器和开发环境。它在 Cursor 的云中运行，每个用户的工作都在一台专用云计算机上执行。桌面和移动应用是用于聊天、审核和审批的瘦客户端（thin clients）。

安全模型基于四项原则：

- **按用户隔离（Per-user isolation）。** 每个用户的工作都在专用的 Firecracker microVM 中运行；这是一种与其他用户实现硬件级隔离的微型虚拟机。
- **默认无访问权限（No access by default）。** Bot 只能使用用户或团队授予它的账号和连接的应用。
- **人工审批关卡（Human approval gates）。** 敏感操作需要用户批准，并由一个名为 Auto Review 的独立审查模型评估。
- **管理控制（Administrative control）。** 团队管理员可以设置团队规则、云端智能体委派、模板分享和本地执行上限。网络控制、团队安装脚本、团队秘密、允许本地出口路由、允许在 Bot 计算机上使用 Sudo、操作记录、强制自动审查、自动审查规则以及组织范围的启用开关仅限 Enterprise。

各部分组合如下：

1. **本地机器。** 聊天、审核和审批在成员的设备上进行。工作在托管计算机中运行。可选的[本地执行](https://cursor.com/docs/grok-bot/security#local-execution)默认要求逐条命令批准，也可以关闭。
2. **环境。** 每位用户一个持久化的 Firecracker microVM。该用户运行的每个 Bot 都共享那台计算机。管理员从 [Cursor 仪表板](https://cursor.com/dashboard/bot) 的 Grok Bot 页面管理 Grok Bot。团队规则、云端智能体委派、公开模板分享和在本地计算机上执行可供团队管理员使用。该页面上**仅限 Enterprise** 的项：组织范围的启用开关、网络控制、团队安装脚本、团队秘密、允许本地出口路由、允许在 Bot 计算机上使用 Sudo、操作记录、强制自动审查、自动审查规则和计算机管理。成员永远看不到此页面。
3. **Bot。** 在托管计算机内使用 shell、浏览器和计算机。Bot 默认没有任何访问权限，只能使用成员为其登录的账号行事。它从成员的 Vault、已连接的密码管理器或安全表单（Secure Form）中填充登录信息和卡信息，而不查看具体的值，并将单点登录和通行密钥（passkeys）等步骤交给成员处理。
4. **连接的应用。** 你团队的 Cursor MCP（Model Context Protocol）策略会完整适用，允许或阻止每个连接器。OAuth 令牌保留在 Cursor 的连接器后端，Bot 调用工具时不会收到这些令牌。
5. **云端智能体（Cloud Agents）。** Grok Bot 可以把编码任务委派给受你现有 [Cloud Agent](https://cursor.com/docs/cloud-agent) 控制的其他计算机。管理员可以禁止生成。
6. **模型与数据。** Grok Bot 管理模型选择。启用隐私模式后，客户数据不会被用于训练；Cursor 在其服务器上执行这一规则，当无法验证该设置时，系统默认不进行训练。

### 用户如何隔离

每位用户获得一台具有硬件级隔离的专用计算机，一个用户无法访问另一个用户的计算机。每台计算机都是一个 Firecracker microVM，拥有自己的内核、内存和虚拟设备。

在一个用户内部，边界有所不同：该用户的所有 Bot 共享一台计算机，Bot 隔离的是人格和工作区，而非计算资源。应把计算机上的某个登录或文件视为该用户运行的每个 Bot 都可访问，将浏览器从不必要的账号中退出登录，并在工作完成后删除敏感的临时文件。当某个工作负载需要自己的计算机和凭证集时，为它单独分配一个 Cursor 用户。

[共享 Bot](https://cursor.com/help/grok-bot/shared-bots) 是「每位用户一个 Bot」的例外。Bot 要么是个人 Bot，要么是共享 Bot：成员可以将一个云端托管的 Bot 分享给团队中的所有人，或只分享给特定人员和用户组，这些成员可以与它聊天。每位成员的聊天都是私密的，包括对所有者及该 Bot 的管理者（Managers）也是如此。在成员自己的聊天或 Slack 私信中，Bot 通常在该成员的计算机上工作，在询问后使用该成员连接的账号，并使用该成员的 Grok Bot 用量。在 Slack 频道、线程、群组私信和群聊中，共享 Bot 使用它自己的一台计算机。所有者或管理者添加到共享 Bot 的秘密、应用和文件，会在每位队友的聊天中可用。

## 管理员控制

大多数 Grok Bot 设置位于 [Cursor 仪表板](https://cursor.com/dashboard/bot) 的 Grok Bot 页面，只有管理员可见。少数设置位于团队设置、你的团队市场（Team Marketplace）或你的身份提供商中。若干控制项仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用；其余在 Teams 和 Enterprise 上可用。Enterprise 团队还可以在某个用户组的 Grok Bot 选项卡中，为一组人群放宽其中若干控制项；请参阅[用户组设置](#group-settings)。

### 访问与身份

谁可以使用 Grok Bot，以及成员如何配置。

#### 启用 Grok Bot

Grok Bot 页面上的组织范围开关，旁边是**管理用户组访问权限（Manage Group Access）**。开启它会打开一个设置模态框，内容涵盖隐私模式、计费和模型可用性，并提议在云端智能体关闭时将其开启，还会要求你接受 Grok Bot 条款。关闭它会阻止所有成员，但不会删除他们的计算机。请参阅[为团队启用 Grok Bot](#enabling-grok-bot-for-your-team)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### SCIM

通过你的身份提供商进行 SCIM 2.0 的配置与取消配置。成员使用其 Cursor 账号登录 Grok Bot，因此你现有的 [SCIM](https://cursor.com/docs/account/teams/scim) 和 SSO 设置会延续适用。有关 Okta 和 Entra ID 的步骤，包括应用分配和计算机浏览器的登录规则，请参阅[配置身份与访问](https://cursor.com/docs/grok-bot/identity)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### 团队图标

Grok Bot 为整个团队显示的图像，例如成员将 Bot 分享给所有人时。管理员从团队设置的「团队资料（Team Profile）」部分上传、更改或移除它。请使用不超过 2 MB 的 PNG、JPEG 或 WebP。

### 智能体能力

Bot 可以代表成员做什么。每项控制都适用于每位成员的 Bot。

#### 云端智能体

允许或阻止 Bot 将编码任务委派给 Cursor [Cloud Agents](https://cursor.com/docs/cloud-agent)。该开关位于 Grok Bot 页面，适用于整个团队，默认开启。被委派的工作在受你现有 Cloud Agent 控制的其他计算机上运行。当团队不需要委派时，请将其关闭。

#### 公开模板分享

控制成员是否可以在团队之外发布 Bot 模板。关闭后，分享仅限团队内部，Cursor 会在其服务器上执行该策略，包括对已经公开的模板。Enterprise 团队初始设置为关闭公开分享；其他团队初始设置为允许。关于共享模板包含的内容，请参阅[分享 Bot](https://cursor.com/docs/grok-bot/work#share-a-bot)。

#### 管理共享 Bot

控制谁可以使用每个[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)，并自动将共享 Bot 添加到成员的侧边栏。在 Grok Bot 页面的**共享 Bot（Shared Bots）**下打开**管理共享 Bot（Manage Shared Bots）**。**访问权限（Access）**列显示谁可以使用每个共享 Bot，例如整个团队、特定人员或用户组，或仅其所有者。点击它可以更改谁有访问权限。在 Bot 的**自动添加（Auto-add）**列中，选择**所有团队（All team）**或一个或多个用户组，或清除选择。自动添加仅适用于有访问权限的用户组。通过这种方式获得 Bot 的成员无法将其从侧边栏隐藏。管理员也可以在这里删除共享 Bot。删除会为团队中的所有人移除它，移除其 Slack 应用，且无法撤销。用户组在「成员与用户组（Members & Groups）」页面管理。

#### 页面分享

控制成员如何在团队内分享[页面（Pages）](https://cursor.com/help/grok-bot/pages)。在 Grok Bot 页面的**分享（Sharing）**下找到**页面分享（Page sharing）**，然后选择**团队中的任何人（Anyone on the team）**、**特定队友（Specific teammates）**或**关闭（Off）**。**团队中的任何人**是默认值。当你收紧设置时，已经分享的页面保持分享状态。该控制项会在页面功能到达你的团队时出现。

#### 智能体电子邮件（Agent Email）

让成员认领一个 `mail.grokbot.com` 地址，其 Bot 可以读取该地址的邮件并从该地址发信。该开关位于 Grok Bot 页面的 **Bot 能力（Bot Capabilities）**下，默认关闭；在开启之前，成员没有任何电子邮件工具。当成员在聊天中要求发邮件时，只有在 Auto-review 允许或成员批准后才会发送。Bot 自行撰写的电子邮件（包括由例程发出的邮件）会作为草稿等待，直到成员按下**发送（Send）**。新闻简报和首次联系邮件会包含退订链接，收到的邮件只会通过成员设置的例程起作用。关闭它会移除 Bot 的电子邮件工具并停止电子邮件例程；现有地址仍会继续接收邮件。请参阅[为你的 Bot 提供电子邮件地址](https://cursor.com/help/grok-bot/agent-email)。

#### 连接器策略

Grok Bot 继承你团队的 Cursor 连接器策略。没有单独的 Grok Bot 连接器列表，成员在 Grok Bot 的**连接应用（Connect apps）**下找到被允许的连接器。从仪表板 [Plugins & MCPs 页面](https://cursor.com/dashboard/plugins)上的团队市场设置成员可以使用哪些服务器，而不是在 Grok Bot 页面上设置。MCP 允许列表仅限 Enterprise；请参阅 [MCP 服务器信任管理](https://cursor.com/docs/enterprise/model-and-integration-management#mcp-server-trust-management)。任何被允许的连接器都可供成员运行的每个 Bot 使用，被阻止的连接器会显示为**被团队管理员禁用（Disabled by team admin）**。向成员推送连接器（无论是强制还是默认开启）不可用。如果你的团队使用允许列表网络策略，并希望远程 MCP 服务器也受同一列表约束，请在**网络（Network）**下开启 **Apply to MCP servers**；它默认关闭。请参阅 [MCP 服务器与网络策略](https://cursor.com/docs/grok-bot/security#mcp-servers-and-the-network-policy)。

#### 在本地计算机上执行

限制 Bot 通过桌面应用在成员自己的机器上可以做什么：打开文件和运行任务。在 Grok Bot 页面上选择**始终允许（Always allow）**、**每次都询问（Ask every time）**或**从不允许（Never allow）**。**始终允许**是默认值，将选择权留给每位成员，而成员自己的设置默认在每个任务前询问。**每次都询问**会让每个本地任务都请求批准，**从不允许**会为整个团队关闭本地执行。当成员自己的设置比团队设置更严格时，仍以成员自己的设置为准。除非 Bot 有具体理由需要在成员机器上工作，否则请选择**从不允许**。请参阅[本地执行](https://cursor.com/docs/grok-bot/security#local-execution)。

#### 允许本地出口路由

让成员通过自己的计算机路由 Grok Bot 的 Web 流量。关闭后，Grok Bot 中的该选项会被禁用。该开关位于 Grok Bot 页面的 **Bot 计算机（Bot Computers）**下，默认开启。关闭它会在五分钟内停止活动路由。重新开启会恢复每位成员之前的选择。请参阅[通过你的桌面路由流量](https://cursor.com/docs/grok-bot/settings#route-traffic-through-your-desktop)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

### 规则与审批

Bot 遵循的指导，以及阻止操作和模型请求的审查层。

#### 团队规则

每位成员的 Bot 都遵循的规则。从 Grok Bot 页面添加它们，并将每条规则的范围设为 Cursor、Grok Bot 或两者。应用于 Grok Bot 的规则始终是必需的，因此成员无法将其关闭。保持规则简短且数量少，例如「绝不将公司数据转移到个人账号」。规则指导 Bot；对于审批行为，请使用[自动审查规则](#auto-review-rules)。对于属于某一组人群的指导，请在[用户组设置](#group-settings)下添加组规则（Group Rules）。

#### 强制自动审查

防止成员关闭 Auto-review。该开关位于 Grok Bot 页面，默认关闭。开启后，Bot 在运行有风险的操作之前总会先检查，并在需要时请求批准。这包括在无人可以回应审批的聊天中的共享 Bot，否则这些 Bot 会在没有 Auto-review 的情况下运行。在依赖团队自动审查规则之前，请先开启它。用户组可以用**不对此用户组强制（Don't enforce for this group）**为其自己的成员解除锁定；请参阅[用户组设置](#group-settings)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### 自动审查规则

全团队范围的「先询问（Ask first）」和「自动允许（Allow automatically）」规则，在成员自己的规则之上适用于每位成员的 Bot。在 Grok Bot 页面上用「配置规则（Configure Rules）」添加它们；更改会自动保存。成员可以在「设置（Settings）」>「通用（General）」>「自动审查（Auto-review）」下看到团队规则，但不能编辑或删除它们；规则冲突时「先询问」优先。关闭强制实施后，团队规则将停止适用。请参阅[审批与 Auto Review](https://cursor.com/docs/grok-bot/security#approvals-and-auto-review)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### 推理钩子

将每个 Grok Bot 模型请求签名后发送到你的组织运行或通过安全供应商使用的 AI 安全服务器。你的服务器在模型运行之前允许或拒绝该请求。从 Grok Bot 页面的**安全与合规（Security & Compliance）**打开[推理钩子（Inference Hooks）](https://cursor.com/dashboard/bot/inference-hooks)。新配置从影子模式（Shadow mode）开始，会在审计日志中记录拒绝，但不阻止成员。推理钩子处于 beta 阶段，所有 Enterprise 团队均可使用。请参阅 [Grok Bot 推理钩子](https://cursor.com/docs/grok-bot/inference-hooks)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

### 计算机与网络

团队计算机如何设置、可以访问什么，以及你如何重建或终止它们。

#### 网络控制

限制团队计算机可以访问哪些目标。在 Grok Bot 页面的**网络（Network）**下找到它，名称为 **Grok Bot 网络访问（Grok Bot Network Access）**。选择**允许所有网络访问（Allow All Network Access）**、**默认值 + 团队允许列表（Defaults + Team Allowlist）**或**仅团队允许列表（Team Allowlist Only）**，并为允许列表模式列出域名和 IP 范围。目录用户组可以带有自己的策略，锁定后团队策略会适用于所有人。没有策略的团队默认允许全部。关于各模式以及新策略如何到达运行中的计算机，请参阅[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)。

在允许列表模式下，**Apply to MCP servers** 开关会出现在目标列表下方。它默认关闭。开启后，每个连接的应用（包括 GitHub、X 和 Origin 等内置连接器）都必须按其发送请求的主机匹配一个允许的目标，否则 Bot 与该应用的连接会被拒绝。命令服务器不受影响。关于每个内置连接器需要哪些主机，请参阅 [MCP 服务器与网络策略](https://cursor.com/docs/grok-bot/security#mcp-servers-and-the-network-policy)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### 团队安装脚本

安装脚本的清单，会在每台团队计算机上运行，使各处都具有相同的工具。在 Grok Bot 页面的 **Bot 计算机（Bot Computers）**下找到**团队安装脚本（Team Setup Scripts）**。不要让秘密值出现在安装脚本中；当脚本需要凭证时，将其存储为[团队秘密（Team Secret）](#team-secrets)并从环境中读取。成员不会在应用中看到这些脚本。关于清单如何运行，以及如何安装可访问私有服务的网络客户端，请参阅[连接到私有网络](https://cursor.com/docs/grok-bot/private-networks)。若只想在一组人群的计算机上运行额外脚本，请在[用户组设置](#group-settings)下添加它们。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### 团队秘密

团队范围的值，由团队安装脚本作为环境变量读取，因此脚本可以持有许可证密钥、认证密钥或服务令牌，而值不会出现在清单中。在 Grok Bot 页面的**团队秘密（Team Secrets）**下添加它们：每个秘密是一个环境变量名称和一个值。Cursor 会加密存储该值，保存后仪表板不会再显示它。团队管理员（包括不付费的管理员）可以添加、替换或删除它们。

它们如何到达计算机：

- 你的团队安装清单中以及用户组[安装脚本](#group-settings)中的每个安装脚本（Setup Script）和检查脚本（Check Script），都会在其环境中带有团队秘密运行。按名称引用秘密，例如 `"$MY_LICENSE_KEY"`。
- 秘密只存在于脚本的进程环境中。脚本一旦结束，除非脚本将其写到某处，否则值就消失了，因此不要在计算机上存储任何你不希望该成员运行的每个 Bot 都能访问的内容。
- 脚本输出在记录日志之前会检查是否包含秘密值，匹配到的内容会被脱敏。
- 只有当一台计算机的团队安装恰好来自一个团队时，它才会收到秘密。如果某位成员的计算机应用了两个或更多团队的安装设置，它不会从其中任何一个团队获得秘密，因为来自不同团队的脚本共享同一个计算机用户。
- 更改（包括轮换的值）会在脚本下一次运行时生效：计算机启动时、定期刷新时，或你重建它时。请参阅[推广到现有计算机](https://cursor.com/docs/grok-bot/private-networks#roll-out-to-existing-computers)。

限制：每个团队最多 100 个秘密，每个值最多 32 KB，总计最多 96 KB。名称必须是有效的环境变量名称，计算机运行时保留的名称（例如 `PATH`、`HOME` 以及任何以 `SAND_` 或 `LD_` 开头的名称）在保存时会被拒绝。团队秘密用于你控制的脚本。它们不会让值直接对 Bot 可用，并且与[成员存储在 Bot 上的秘密](https://cursor.com/help/grok-bot/secrets)是分开的。它们无法通过管理 API 使用。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### 允许在 Bot 计算机上使用 Sudo

让 Bot 在自己的计算机上以 root 身份运行命令。该开关位于 Grok Bot 页面的 **Bot 计算机（Bot Computers）**下，默认开启。现有计算机会在重启后应用更改。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### 管理成员计算机与数据

让管理员可以一次重建、终止或永久删除许多成员的计算机，或删除他们的所有 Grok Bot 数据，并为每位成员给出结果。在 Grok Bot 页面的**安全与合规（Security & Compliance）**下找到它。重建会将成员迁移到最新镜像和团队安装脚本，同时保留他们的 Bot、文件和登录信息。终止会结束成员当前的工作并保留持久磁盘；成员的下一个会话会在其上启动一台新计算机。删除会移除计算机及其存储的文件，成员的下一个会话会启动一台空计算机。要自动删除不活动的计算机，请使用[计算机保留期（Retention Period for Computers）](#data-retention)。这些操作都不会移除访问权限：要移除访问权限，请将成员从团队中移除，或为其用户组关闭 Grok Bot，并在你的身份提供商中撤销其会话。请参阅[管理 Grok Bot 计算机](https://cursor.com/docs/grok-bot/computers)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

### 数据保留

在你选择的期限过后自动删除 Grok Bot 数据。在 Grok Bot 页面的**数据保留（Data Retention）**下找到这些设置。每项都默认关闭。

| 设置 | 删除什么 | 期限 |
| --- | --- | --- |
| **Bot 保留期（Retention Period for Bots）** | 在该期限内无人发消息的 Bot，以及它们的对话、记忆、技能和例程。Bot 的所有者会在删除前 30 天收到电子邮件，在此期间发送一条消息即可保留该 Bot。 | 60 至 365 天 |
| **计算机保留期（Retention Period for Computers）** | 成员的计算机及其文件，一旦在该期限内无人给他们的任何 Bot 发消息。请参阅[自动删除不活动的计算机](https://cursor.com/docs/grok-bot/computers#delete-inactive-computers-automatically)。 | 30 至 365 天 |
| **消息保留期（Retention Period for Messages）** | 每天删除早于该期限的 Bot 消息和附件。不会通知任何人。 | 30 至 365 天 |

开启某项设置或缩短其期限时，会先要求你确认。已删除的数据无法恢复。每次更改和删除都会记录在[审计日志](https://cursor.com/dashboard/audit-log)中。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

### 日志与审计

记录什么，以及记录到哪里。

#### 操作记录

记录 Bot 做了什么：每次工具调用及其结束方式，允许或拒绝该调用的决定（Auto-review、某个钩子或成员），连接器（MCP）工具调用、shell 命令、浏览器导航、计算机使用会话、文件传输、Bot 发送的消息、例程运行、护栏干预、它读取的技能，以及它交给子智能体或云端智能体处理的工作。事件是元数据，在存储或导出之前会经过清理。shell 命令会擦除秘密；浏览器导航会将每个页面保留为 `scheme://host/path` 及其标题，但会去除查询字符串和凭证；计算机使用会话会记录操作次数、截图数量和会话时长，但不记录截图、点击或键入的文本；其他每个事件都带有 id、结果和时长，绝不包含工具参数、文件路径或消息内容。该开关位于 Grok Bot 页面，默认关闭。记录的事件不会出现在审计日志页面上。要在你自己的收集器中接收它们，请配置 [OpenTelemetry 导出（OpenTelemetry Export）](https://cursor.com/docs/enterprise/opentelemetry-export)，它会传递每个标记为 `cursor.surface=grok_bot` 的事件；[Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire#shared-grok_bot-attributes) 列出了每个事件和属性。保留细节见[日志与审计](https://cursor.com/docs/grok-bot/security#logging-and-audit)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### 审计日志

管理员、安全和身份验证事件，以及 Grok Bot 控制平面事件：Bot 创建、成员访问权限更改、团队安装清单、MCP 身份验证、Slack 账号关联和例程。每一行都会标明执行操作的应用程序，因此你可以将日志筛选为 Grok Bot。在[审计日志页面](https://cursor.com/dashboard/audit-log)查看它们，或将其流式传输到你的 SIEM；请参阅[审计日志](https://cursor.com/docs/enterprise/compliance-and-monitoring#audit-logs)。关于 Bot 执行的操作，请使用[操作记录](#action-recording)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

#### OpenTelemetry 导出

将 Cursor 的使用指标和日志（包括已记录的 Grok Bot 操作）流式传输到你运行的收集器。这是操作记录事件的客户路径。在**团队设置（Team Settings）** > **OpenTelemetry 导出（OpenTelemetry Export）**下配置它。端点要求和事件架构见 [OpenTelemetry 导出](https://cursor.com/docs/enterprise/opentelemetry-export)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

### 用户组设置

上述控制项设置全团队基线。若要为一组人群放宽该基线，请从[成员 > 用户组](https://cursor.com/dashboard/members?subtab=groups)打开你的团队拥有的用户组，并使用其 **Grok Bot** 选项卡。除网络策略外，用户组设置只会放宽：用户组可以授予其成员比团队允许的更多权限，绝不会更少，属于多个用户组的成员会得到最宽松的结果。这与[用户组模型访问权限](https://cursor.com/docs/enterprise/model-and-integration-management#how-team-and-group-model-access-combine)的规则相同。用户组控制项若保留为团队的值，则不会改变任何东西，因此请在 Grok Bot 页面上收紧控制，再按用户组放宽。

该选项卡有四个部分：

- **Bot 能力。** 当团队将这些功能关闭或设置得更严格时，为用户组成员允许[云端智能体](#cloud-agents)、[智能体电子邮件](#agent-email)或[允许本地出口路由](#allow-local-egress-routing)，或提高[在本地计算机上执行](#execution-on-local-computer)的上限。对于 Auto-review，**不对此用户组强制（Don't enforce for this group）**会解除团队的[强制自动审查](#enforce-auto-review)锁定，使用户组成员可以关闭 Auto-review；用户组自动审查规则会与团队的[自动审查规则](#auto-review-rules)合并，规则冲突时「先询问」优先。
- **网络。** 用户组自己的网络策略，如[网络控制](#network-controls)所述。它会为组成员取代团队策略，无论更宽松还是更严格；属于多个用户组的成员会得到最严格的一个。锁定的团队策略适用于所有人。**Apply to MCP servers** 只在团队的 Grok Bot 页面上设置；用户组会继承它，且无法将其关闭。
- **组规则（Group Rules）。** 用户组 Bot 的规则，与[团队规则](#team-rules)合并。成员无法将其关闭。
- **安装脚本（Setup Scripts）。** 在用户组成员的计算机上与[团队安装脚本](#team-setup-scripts)一起运行的清单。它们使用相同的结构并以相同方式运行，同样适用无秘密规则，并读取与团队清单相同的[团队秘密](#team-secrets)；没有用户组级别的秘密。请参阅[团队安装如何运行你的脚本](https://cursor.com/docs/grok-bot/private-networks#how-team-setup-runs-your-scripts)。

用户组设置适用于你的团队拥有的用户组，无论你是手动管理成员资格，还是通过 [SCIM](https://cursor.com/docs/account/teams/scim#directory-groups) 同步。它们与[组织用户组（Organization Groups）](https://cursor.com/docs/enterprise/organization-groups)是分开的。若要控制谁可以使用 Grok Bot，请改用 Grok Bot 页面上的**管理用户组访问权限**；请参阅[为团队启用 Grok Bot](#enabling-grok-bot-for-your-team)。

*仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)上可用。*

## 管理 API

通过[管理 API（Admin API）](https://cursor.com/docs/account/teams/admin-api#grok-bot)启用 Grok Bot，并管理能力、强制 Auto-Review、用户组访问权限、网络策略、团队规则和安装脚本。[团队秘密](#team-secrets)只能从仪表板管理。

若要从脚本重建、终止或删除成员的计算机，或删除他们的所有 Grok Bot 数据，请使用[组织 API（Organization API）](https://cursor.com/docs/account/organizations/organization-admin-api#grok-bot-computers)。它需要一个具有 `admin:*` 范围的组织 API 密钥，因为一台计算机服务于成员所属的每个团队。

## 安全

安全模型、网络策略、审批与 Auto Review、身份、日志、数据处理和认证见 [Grok Bot 安全](https://cursor.com/docs/grok-bot/security)。常见审查问题见 [Grok Bot 安全常见问题](https://cursor.com/docs/grok-bot/security-faq)。若要让自己的 AI 安全服务器检查每个模型请求，请参阅 [Grok Bot 推理钩子](https://cursor.com/docs/grok-bot/inference-hooks)。

## 推荐配置

对于安全敏感的部署，以下是推荐的基线配置。

对于管理员：

1. **配置网络控制。仅限 Enterprise。** 没有策略的团队默认允许全部。自助式 Teams 无法设置此项。如果你选择了允许列表模式，并希望它也覆盖连接的应用，请将连接器使用的主机（例如 `api.github.com`、`api.x.com`、`api.origin.cursor.com`）添加到列表中，然后开启 **Apply to MCP servers**；在你开启之前它一直关闭。请参阅 [Grok Bot 安全](https://cursor.com/docs/grok-bot/security#network-policy)。
2. **在启用 Grok Bot 之前，审查 Teams 市场中的连接器策略。** 任何被允许的连接器都可供成员运行的每个 Bot 使用。
3. **在依赖团队规则之前开启强制自动审查。仅限 Enterprise。** 成员可以在其上添加更严格的个人规则；规则冲突时「先询问」优先。
4. **将「在本地计算机上执行」设为「从不允许」**，除非 Bot 需要在成员机器上操作。默认值将选择权留给每位成员。
5. **如果你不需要委派，请禁用云端智能体生成。**
6. **保持公开模板分享关闭**，除非成员应当向团队之外发布 Bot 模板。
7. **添加团队自动审查规则。仅限 Enterprise。** 覆盖应始终先询问或可以自动继续的操作。生产部署、外部电子邮件、付款和接受法律条款是很好的「先询问」示例。保持自动规则的范围狭窄。
8. **通过你的身份提供商限制登录到受管设备。** Grok Bot 登录使用你的 SSO，因此设备感知的登录策略会适用于它。这限制的是登录，而不是托管计算机本身。

对于成员：

1. **绝不要将凭证粘贴到聊天中。** 遮蔽的秘密请求是受支持的路径。
2. **对于涉及账号、金钱或共享资源的操作，优先选择「允许一次」而不是「始终允许」。**
3. **将 Bot 的浏览器登录到与任务规模相称的账号**，并让它从不必要的账号中退出登录。在源系统支持时，使用范围受限的服务账号。
4. **新角色从只读任务和草拟输出开始**，并让发送、发布、购买、删除和生产环境更改始终处于审批之后。
5. **定期审查连接的应用和活动例程**，并在其源系统发生变化时暂停例程。

## 常见问题

### 我可以为团队开启或关闭 Grok Bot 吗？

组织范围的**启用 Grok Bot** 开关仅限 Enterprise。它位于 Cursor 仪表板的 Grok Bot 页面。自助式 Teams 不会获得此开关。禁用会阻止成员，但不会删除他们的计算机。

### 我可以通过管理 API 管理 Grok Bot 吗？

可以。使用[管理 API](https://cursor.com/docs/account/teams/admin-api#grok-bot)。

### 我可以为 Grok Bot 设置支出上限吗？

目前没有单独的 Grok Bot 支出上限。账号级的按需控制会适用，按产品划分的用量见仪表板用量页面。

### 为什么成员看到某个应用显示为「被团队管理员禁用」？

你团队的连接器策略阻止了该服务器。请在 **Teams 市场**中启用它，如果你使用 MCP 允许列表，请将其服务器 URL 添加到允许列表中，并让成员重启应用。如果某个被允许的应用对普通成员仍然因供应商侧的权限错误而失败，请检查提供商的要求；有些供应商将其 MCP 端点限制为仅限其自己的管理员。请参阅[连接应用](https://cursor.com/help/grok-bot/connect-apps)。

### 成员如何请求访问权限？

成员可以从应用发送请求。在管理员尚未完成设置的池化（pooled）Enterprise 团队中，成员会看到一条团队设置消息。下一步是管理员使用仅限 Enterprise 的启用开关。自助式 Teams 不使用该开关。

### 我可以查看团队使用 Grok Bot 所做的工作类型吗？

可以，在所有 Enterprise 团队上。分析仪表板的对话洞察（Conversation Insights）页面有一个 **Grok Bot** 来源，按工作类型（Type of Work）和自动化程度（Level of Automation）对 Bot 对话分组。请参阅 [Grok Bot 对话洞察](https://cursor.com/docs/account/teams/analytics#grok-bot-conversation-insights)。

隔离、出口、审批、日志和数据处理方面的问题见 [Grok Bot 安全常见问题](https://cursor.com/docs/grok-bot/security-faq)。
