---
title: "文档：面向 Teams 和 Enterprise 的 Grok Bot"
linkTitle: "文档：Teams 与 Enterprise"
date: 2026-11-05
originalTitle: "Grok Bot for Teams and Enterprise"
sourceUrl: "https://docs.x.ai/grok-bot/teams-and-enterprises"
altUrls: ["https://cursor.com/docs/grok-bot/teams"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-17
dateNote: "文档不标日期，取收集日期；2026-11-10 发现原文更新，按新版覆盖原文存档：新增管理员的「Bot sharing」设置（Everyone / Admins only）、Slack 中未关联账号的成员使用共享 Bot 及其用量归属等内容；2026-11-28 发现原文更新：Shared Bots 改称 Team Bots，新增 Microsoft Teams 开关；本地出口路由分 Always on / Members decide / Always off 三种；网络控制新增 Allow All Sites Except These（至多 50 站点）"
tags: [安全, 开放与价格, 运行环境, 商业与规模]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：这是管理员部署指南。Teams 套餐默认开启且无法关闭，Enterprise 由管理员开启，并可用「Manage Group Access」限定用户组；Privacy Mode (Legacy) 会完全阻止 Grok Bot。架构上，Grok Bot 是在每用户一个 Firecracker microVM 中运行的计算机使用智能体，桌面和移动端只是聊天、审核与审批的瘦客户端。管理控制涵盖云端智能体委派、模板公开分享、Bot sharing（Everyone 或 Admins only）、Team Bot 的 Microsoft Teams 接入、Agent Email、连接器策略、本地执行上限，以及 Enterprise 专有的网络控制（四种模式，含最多 50 个站点的屏蔽名单）、本地出口路由（Always on、Members decide、Always off）、Team Setup Scripts、Team Secrets、强制 Auto-review、Action Recording、审计日志、OpenTelemetry 导出、数据保留（Bot 60 至 365 天、计算机与消息 30 至 365 天）和成员计算机管理。用户组设置只放宽、不收紧（网络策略除外）；文末给出推荐的安全基线配置，并说明目前没有单独的 Grok Bot 支出上限。

**保留理由**：汇总了团队与企业版各控制项的归属与默认值，并给出推荐配置，是对照看 Teams 与 Enterprise 能力差异的主要资料。

---

Grok Bot 面向团队与企业

Grok Bot 为团队中的每个人提供用于日常工作的常驻 Bot（standing Bots）：研究、运营、文档、浏览和自动化。本页面向正在推广 Grok Bot 的团队与组织管理员。安全评审人员应先读 [Grok Bot 安全](https://docs.x.ai/grok-bot/security) 和 [Grok Bot 安全 FAQ](https://docs.x.ai/grok-bot/security-faq)。想了解审批模型的成员也应从那里开始。

## 可用性

| 套餐 | 访问方式 |
| --- | --- |
| 个人 | 随每个付费 Cursor 套餐提供，可通过个人 SuperGrok 关联，或在自助式 Grok Business 套餐中占一个席位 |
| 团队 | 包含在内；每位成员都有访问权，用量按席位额度计 |
| 企业 | 从[你的仪表盘](https://cursor.com/dashboard/bot)为团队启用 Grok Bot |

这张表说明的是产品访问权，不是管理员控制项清单。Teams 套餐包含 Grok Bot。有几项设置仅限 Enterprise，在自助式 Teams 中不会出现。[管理控制](#admin-controls)会逐项标出。

[套餐与计费](https://grok.com/help/grok-bot/plans) 是套餐与用量的权威对照表。

## 为团队启用 Grok Bot

在 Teams 套餐中，Grok Bot 默认开启，每位成员无需管理员操作即可使用。处于[隐私模式（旧版）](#before-you-roll-out)或[旧版按请求计费套餐](https://cursor.com/docs/models-and-pricing#legacy-request-based-pricing)的团队则保持关闭。没有可以关闭它的开关。

在 Enterprise 套餐中，管理员从 [Cursor 仪表盘中的 Grok Bot](https://cursor.com/dashboard/bot) 开启。开启后，你可以向所有团队成员开放，或用**管理组访问权限**（Manage Group Access）限定为特定的[组](https://cursor.com/dashboard/members?subtab=groups)。关闭 Grok Bot 会阻止所有成员使用，但不会删除他们的计算机。

两种套餐的管理员都可以在 Grok Bot 页面上用**邀请团队**（Invite Team）把成员拉进来。团队中已有的 Cursor 用户会收到一封带下载链接的邮件。新用户会收到加入你的 Cursor 团队的邀请（邮件或邀请链接），其中也会指引他们使用 Grok Bot。通过 SCIM 管理成员关系的团队只会看到「已有用户」这个选项。

要自己在受管设备上安装桌面应用并规划更新，见[将 Grok Bot 部署到你的组织](https://docs.x.ai/grok-bot/deployment)。

## 推广之前

* 停用隐私模式（旧版）。该设置会完全阻止 Grok Bot，启用前系统会提示你修改。在团队设置（Team Settings）中检查隐私设置。
* 为共享出口地址做准备。如果你的公司按来源 IP 限制服务，见[静态出口 IP](https://docs.x.ai/grok-bot/security#static-egress-ips)。
* 清理网关。如果成员设备位于 Zscaler 或其他 TLS 检查代理之后，请在成员连接前放行 Cursor 的域名（包括嵌套的 `*.*.cursorvm.com` 模式）并免除检查。见[配置 TLS 检查代理](https://docs.x.ai/grok-bot/proxies)。
* 决定成员如何从计算机登录公司工具。见[身份与登录](https://docs.x.ai/grok-bot/security#identity-and-sign-ins)。
* 检查 Grok Bot 继承的策略：所有套餐都有团队规则和连接器策略，Enterprise 还有团队自动审查规则和 MCP 允许列表。

## 架构

### Grok Bot 的构成

Grok Bot 是一个计算机使用智能体，操作应用、浏览器和开发环境。它运行在 Cursor 的云端，每个用户的工作都在一台专用云计算机上执行。桌面端和移动端应用只是用于聊天、审核和审批的瘦客户端。

安全模型建立在四项原则之上：

* 每用户隔离。每个用户的工作运行在专用的 Firecracker microVM 中，这是一种与其他用户有硬件级隔离的微型虚拟机。
* 默认无访问权。Bot 只能使用用户或团队授予它的账户和已连接应用。
* 人工审批关卡。敏感操作需要用户批准，由一个名为 Auto Review 的独立审查模型评估。
* 管理控制。团队管理员可以设置团队规则、云端智能体委派、模板分享和本地执行上限。网络控制、团队安装脚本、团队密钥、本地出口路由、允许在 Bot 计算机上使用 sudo、操作记录、强制自动审查、自动审查规则和组织级启用开关仅限 Enterprise。

各部分的关系如下：

1. 本地机器。聊天、审核和审批在成员设备上进行。工作在托管的计算机上运行。可选的[本地执行](https://docs.x.ai/grok-bot/security#local-execution)默认要求逐条命令批准，也可以关闭。
2. 环境。每个用户一台持久的 Firecracker microVM。该用户运行的每个 Bot 共用这台计算机。管理员从 [Cursor 仪表盘](https://cursor.com/dashboard/bot)的 Grok Bot 页面管理 Grok Bot。团队规则、云端智能体委派、公开模板分享和「在本地计算机上执行」对团队管理员可用。该页面上仅限 Enterprise 的项有：组织级启用开关、网络控制、团队安装脚本、团队密钥、本地出口路由、允许在 Bot 计算机上使用 sudo、操作记录、强制自动审查、自动审查规则和计算机管理。成员看不到这个页面。
3. Bot。在托管计算机内使用 shell、浏览器和计算机。Bot 默认没有访问权，只能以成员为它登录的账户行事。它从成员的 Vault、已连接的密码管理器或安全表单（Secure Form）填充登录信息和银行卡，且看不到这些值，并把单点登录和通行密钥等步骤交给成员。
4. 已连接应用。你团队的 Cursor MCP（Model Context Protocol）策略完全适用，逐个允许或阻止连接器。OAuth 令牌留在 Cursor 的连接器后端，Bot 调用工具时不会拿到令牌。
5. 云端智能体。Grok Bot 可以在你现有的[云端智能体](https://cursor.com/docs/cloud-agent)控制下，把编码任务委派给另外的计算机。管理员可以禁止派生。
6. 模型与数据。Grok Bot 管理模型选择。启用隐私模式后，客户数据不用于训练；Cursor 在其服务器上强制执行，无法核实该设置时，系统默认不用于训练。

### 用户如何隔离

每个用户获得一台有硬件级隔离的专用计算机，一个用户无法访问另一个用户的计算机。每台计算机都是一个 Firecracker microVM，有自己的内核、内存和虚拟设备。

在一个用户内部，边界不同：该用户的所有 Bot 共用一台计算机，Bot 隔离的是人格和工作区，不是计算资源。把计算机上的登录或文件视为该用户运行的每个 Bot 都能访问，把浏览器从 Bot 不再需要的账户退出登录，工作完成后删除敏感的临时文件。当某项工作负载需要自己的计算机和凭据集时，给它单独的 Cursor 用户。

[Team Bot](https://docs.x.ai/grok-bot/team-bots) 是「每用户一个 Bot」的例外。Bot 要么是个人 Bot，要么是共享 Bot：成员把托管在云端的 Bot 分享给团队所有人，或只分享给特定的人和组，这些成员可以与它聊天。每个成员的聊天都是私密的，所有者和管理者（Manager）也看不到。在成员自己的聊天或 Slack 私聊中，Bot 通常在该成员的计算机上工作，询问后使用该成员连接的应用，并消耗该成员的 Grok Bot 用量。在 Slack 频道、话题、群组私聊和群聊中，Team Bot 使用自己的一台计算机。所有者或管理者为 Team Bot 添加的密钥、应用和文件，在每个队友的聊天中都可用。

## 管理控制

大多数 Grok Bot 设置位于 [Cursor 仪表盘](https://cursor.com/dashboard/bot)的 Grok Bot 页面，只有管理员能看到。少数位于团队设置、你的团队市场（Team Marketplace）或身份提供商中。有几项控制仅在 [Enterprise 套餐](https://cursor.com/docs/enterprise)提供，其余在 Teams 和 Enterprise 都可用。Enterprise 团队还可以在某个组的 Grok Bot 标签页中为这一批人放宽其中几项；见[组设置](#group-settings)。

### 访问与身份

谁可以使用 Grok Bot，以及成员如何开通。

#### 启用 Grok Bot

Grok Bot 页面上的组织级开关，旁边是**管理组访问权限**（Manage Group Access）。开启时会弹出一个设置对话框，涵盖隐私模式、计费和模型可用性，提议在云端智能体关闭时将其开启，并要求你接受 Grok Bot 条款。关闭会阻止所有成员，但不会删除他们的计算机。见[为团队启用 Grok Bot](#enabling-grok-bot-for-your-team)。

Enterprise 套餐可用。

#### SCIM

通过身份提供商进行 SCIM 2.0 的开通与停用。成员用 Cursor 账户登录 Grok Bot，因此你现有的 [SCIM](https://cursor.com/docs/account/teams/scim) 和 SSO 设置继续有效。Okta 和 Entra ID 的步骤（包括应用分配和计算机浏览器的登录规则）见[配置身份与访问](https://docs.x.ai/grok-bot/identity-and-access)。

Enterprise 套餐可用。

#### 团队图标

Grok Bot 为整个团队显示的图片，例如成员把 Bot 分享给所有人时。管理员在团队设置的**团队资料**（Team Profile）部分上传、更改或移除它。使用不超过 2 MB 的 PNG、JPEG 或 WebP。

### 智能体能力

Bot 可以代表成员做什么。每项控制都适用于每位成员的 Bot。

#### 云端智能体

允许或阻止 Bot 把编码任务委派给 Cursor [云端智能体](https://cursor.com/docs/cloud-agent)。开关在 Grok Bot 页面上，作用于整个团队，默认开启。被委派的工作在你现有的云端智能体控制下于单独的计算机上运行。团队不需要委派时请关闭。

#### 公开模板分享

控制成员能否把 Bot 模板发布到团队之外。关闭则分享仅限团队内，Cursor 在其服务器上执行该策略，包括已经公开的模板。Enterprise 团队默认关闭公开分享，其他团队默认允许。关于共享模板包含什么，见[分享 Bot](https://docs.x.ai/grok-bot/bots#share-a-bot)。

#### Bot 分享

控制谁可以与队友分享 Bot。在 Grok Bot 页面的**分享**（Sharing）下找到 **Bot 分享**（Bot sharing），选择**所有人**（Everyone）或**仅管理员**（Admins only）。默认是**所有人**。选**仅管理员**时，成员会看到提示「只有团队管理员可以分享 Bot」（Only team admins can share Bots），他们的**分享**控制被禁用；Cursor 在其服务器上执行这一限制。已经分享的 Bot 保持分享，管理员在**管理 Bot**（Manage Bots）中设置的访问权仍然有效。见[谁能做什么](https://docs.x.ai/grok-bot/team-bots#who-can-do-what)

#### 允许共享登录

让 Team Bot 的管理者把他们自己的应用登录共享为共享连接器。在 Grok Bot 页面的**分享**下找到**允许共享登录**（Allow Shared Logins）。它默认关闭。开启后，使用该 Bot 的所有人都通过该管理者的账户行事，包括 Bot 所做的更改。关闭时，管理者会看到「你的管理员已关闭与 Bot 共享登录」（Your admin has turned off sharing logins with Bots）。见[与团队共享一个账户](https://docs.x.ai/grok-bot/create-a-team-bot#share-one-account-with-the-team)

#### Slack 工作区访问

允许 Slack 工作区中不在团队里的成员，无需关联账户即可在 Slack 中使用 Team Bot。它适用于分享给整个组织的 Bot，或分享给该团队的 Bot（当该团队是组织唯一的团队，或不属于任何组织时）。他们的回复消耗团队的用量。Slack 访客和 Slack Connect 频道从不包含在内。在 Grok Bot 页面的**分享**下找到 **Slack 工作区访问**（Slack Workspace Access）。它默认开启。在组织中，由组织管理员为每个团队设置。设置到达你的团队后才会显示。见[把 Team Bot 加到 Slack](https://docs.x.ai/grok-bot/create-a-team-bot#add-it-to-slack)

#### 管理 Bot

列出团队中的每个 Bot。在 Grok Bot 页面的**共享 Bot**（Shared Bots）下打开**管理 Bot**（Manage Bots），按分享范围或所有者筛选列表。**访问权**（Access）列显示谁可以使用每个 [Team Bot](https://docs.x.ai/grok-bot/team-bots)，例如整个团队、特定的人或组，或仅其所有者。点击它可以更改谁有访问权。在 Bot 的**自动添加**（Auto-add）列中，选择**全团队**（All team）或一个或多个组，把该 Bot 添加到这些成员的侧边栏，或清除它。自动添加只对拥有访问权的组生效。以这种方式获得 Bot 的成员无法从侧边栏隐藏它。管理员可以在这里删除任何 Bot。未分享的 Bot 显示**未分享**（Not shared）：管理员无法打开它，但可以删除它。删除 Bot 会把它及其 Slack 应用从所有使用者那里移除，且无法撤销。组在「成员与组」页面管理。

#### Microsoft Teams

让团队的 Team Bot 加入 Microsoft Teams。在 Grok Bot 页面的**共享 Bot**下，在**启用 Microsoft Teams**（Enable Microsoft Teams）旁选择**启用**（Enable），并用 Microsoft Teams 或全局管理员账户登录。之后该行会显示已为你的组织启用 Microsoft Teams，**撤销**（Revoke）可将其关闭。只有团队管理员可以启用。Microsoft Teams 管理员仍需在 Teams 管理中心批准每个 Bot。**管理 Microsoft Teams 账户**（Manage Microsoft Teams accounts）列出已关联 Microsoft Teams 账户的成员，并允许取消关联。见[在 Microsoft Teams 中使用 Grok Bot](https://docs.x.ai/grok-bot/microsoft-teams)。

#### 会议

控制成员的 Bot 能否加入 Google Meet、Zoom 和 Microsoft Teams 通话、转录并回报。**会议**（Meetings）开关位于 Grok Bot 页面的 **Bot 能力**（Bot Capabilities）下。会议功能在 Team、Enterprise、Ultra 和 Super 套餐中可用。Enterprise 管理员可以在这里开启会议。关闭时，Bot 无法加入或读取会议。Team Bot 只有在它自己的团队允许时才加入会议。见[让 Bot 加入你的会议](https://docs.x.ai/grok-bot/meetings)。

#### 页面分享

控制成员如何在团队内分享[页面](https://docs.x.ai/grok-bot/files-and-results#pages)。在 Grok Bot 页面的**分享**下找到**页面分享**（Page sharing），选择**团队中的任何人**（Anyone on the team）、**特定队友**（Specific teammates）或**关闭**（Off）。默认是**团队中的任何人**。收紧设置时，已经分享的页面保持分享。页面功能到达你的团队后，该控制才会出现。

#### 智能体邮箱

让成员领取一个 `mail.grokbot.com` 地址，他们的 Bot 可以读取并从该地址发信。开关位于 Grok Bot 页面的 **Bot 能力**下，默认关闭；开启前成员没有邮件工具。当成员在聊天中索要邮箱时，自动审查允许或成员批准后即发送。Bot 自行撰写的邮件（包括来自例程的邮件）会作为草稿等待成员按下**发送**（Send）。新闻通讯和首次联系的邮件包含退订链接，收到的邮件只通过成员设置的例程处理。关闭它会移除 Bot 的邮件工具并停止邮件例程；已有地址会继续收信。见[给你的 Bot 一个邮箱地址](https://docs.x.ai/grok-bot/computer-and-apps#give-your-bots-an-email-address)。

#### 连接器策略

Grok Bot 继承你团队的 Cursor 连接器策略。没有单独的 Grok Bot 连接器列表，成员在 Grok Bot 的**连接应用**（Connect apps）下找到允许的连接器。在仪表盘[插件与 MCP 页面](https://cursor.com/dashboard/plugins)的团队市场中设置成员可以使用哪些服务器，而不是在 Grok Bot 页面。MCP 允许列表仅限 Enterprise；见 [MCP 服务器信任管理](https://cursor.com/docs/enterprise/model-and-integration-management#mcp-server-trust-management)。任何被允许的连接器都可供成员运行的每个 Bot 使用，被阻止的连接器显示为**已被团队管理员禁用**（Disabled by team admin）。向成员推送连接器（无论强制还是默认开启）不可用。如果你的团队使用允许列表网络策略，并希望远程 MCP 服务器也遵守同一列表，请在**网络**下开启**应用于 MCP 服务器**（Apply to MCP servers）；它默认关闭。见 [MCP 服务器与网络策略](https://docs.x.ai/grok-bot/security#mcp-servers-and-the-network-policy)。

#### 在本地计算机上执行

限制 Bot 通过桌面应用在成员自己的机器上可以做什么：打开文件、运行任务。在 Grok Bot 页面上选择**始终允许**（Always allow）、**每次询问**（Ask every time）或**永不允许**（Never allow）。默认的**始终允许**把选择权留给每位成员，成员自己的设置默认在每个任务前询问。**每次询问**会让每个本地任务都请求批准，**永不允许**则为整个团队关闭本地执行。当成员自己的设置比团队更严格时，仍以成员的设置为准。除非 Bot 有特定理由在成员机器上工作，否则选**永不允许**。见[本地执行](https://docs.x.ai/grok-bot/security#local-execution)。

#### 允许本地出口路由

设置 Grok Bot 的 Web 流量是否经过每位成员自己的计算机。在 Grok Bot 页面的 **Bot 计算机**（Bot Computers）下的**本地出口路由**（Local Egress Routing）中选择模式：

* **始终开启**（Always on）要求使用路由。成员无法关闭。当成员的计算机均未连接时，Grok Bot 会拒绝本应路由的站点，而不会改用云端。使用旧版 Grok Bot 桌面端的成员在更新前保留自己的选择。
* **成员决定**（Members decide，默认）让每位成员在 Grok Bot 中选择。
* **始终关闭**（Always off）阻止路由。即使成员的桌面设置已开启，服务器也会停止经该成员的计算机路由。

更改对新连接生效。当你把**始终关闭**改回**成员决定**时，每位成员先前的选择会再次生效。当团队使用**始终关闭**时，组可以为其成员允许路由。见[组设置](#group-settings)和[通过你的桌面转出流量](https://docs.x.ai/grok-bot/settings-and-notifications#route-traffic-through-your-desktop)。

Enterprise 套餐可用。

### 规则与审批

Bot 遵循的指引，以及阻止操作和模型请求的审查层。

#### 团队规则

每位成员的 Bot 都遵循的规则。在 Grok Bot 页面添加，并把每条规则限定为 Cursor、Grok Bot 或两者。应用于 Grok Bot 的规则始终是必需的，成员无法关闭。保持简短、数量少，例如「绝不把公司数据移到个人账户」。规则指引 Bot；审批行为请用[自动审查规则](#auto-review-rules)。属于某一批人的指引，在[组设置](#group-settings)下添加组规则。

#### 强制自动审查

防止成员关闭自动审查。开关在 Grok Bot 页面上，默认关闭。开启后，Bot 总是在执行有风险的操作前检查，需要时请求批准。这包括在无人能回应审批的聊天中的 Team Bot——否则它们会在没有自动审查的情况下运行。在依赖团队自动审查规则之前先开启它。组可以用**不对该组强制**（Don't enforce for this group）为本组成员解除锁定；见[组设置](#group-settings)。

Enterprise 套餐可用。

#### 自动审查规则

团队范围的**先询问**（Ask first）和**自动允许**（Allow automatically）规则，在成员自己的规则之上应用于每位成员的 Bot。在 Grok Bot 页面上用**配置规则**（Configure Rules）添加；更改会自动保存。成员在**设置 → 通用 → 自动审查**下看到团队规则，但无法编辑或删除，规则冲突时**先询问**优先。关闭强制实施会停止应用团队规则。见[审批与 Auto Review](https://docs.x.ai/grok-bot/security#approvals-and-auto-review)。

Enterprise 套餐可用。

#### 推理钩子

把每个 Grok Bot 模型请求签名后发送到你组织运行或通过安全厂商使用的 AI 安全服务器。你的服务器在模型运行前允许或拒绝该请求。从 Grok Bot 页面的**安全与合规**（Security & Compliance）打开[推理钩子](https://cursor.com/dashboard/bot/inference-hooks)。新配置从影子模式（Shadow mode）开始，它把拒绝记录到审计日志而不阻止成员。推理钩子处于 beta，对所有 Enterprise 团队可用。见 [Grok Bot 推理钩子](https://docs.x.ai/grok-bot/inference-hooks)。

Enterprise 套餐可用。

### 计算机与网络

团队计算机如何设置、能访问什么，以及如何重建或终止它们。

#### 网络控制

限制团队计算机可以访问的目的地。在 Grok Bot 页面的**网络**下以 **Grok Bot 网络访问**（Grok Bot Network Access）找到。选择**允许所有网络访问**（Allow All Network Access）、**除这些站点外全部允许**（Allow All Sites Except These）、**默认值 + 团队允许列表**（Defaults + Team Allowlist）或**仅团队允许列表**（Team Allowlist Only）。在允许列表模式下填写域名和 IP 范围，或在**被阻止的站点**（Blocked Sites）下填写要阻止的站点。目录组可以有自己的策略，锁定会让团队策略适用于所有人。没有策略的团队默认全放行。模式以及新策略如何到达运行中的计算机，见[网络策略](https://docs.x.ai/grok-bot/security#network-policy)。

**除这些站点外全部允许**让计算机访问除你列出的站点之外的一切。每行输入一个主机名，例如 `example.com`，不带协议、端口或路径。每个站点也会阻止其子域。一个团队及其各组最多可阻止 50 个站点。阻止是尽力而为的，不是安全边界。它覆盖的范围和限制见[被阻止的站点](https://docs.x.ai/grok-bot/security#blocked-sites)。

在允许列表模式下，**应用于 MCP 服务器**开关出现在目的地列表下方。它默认关闭。开启后，每个已连接应用（包括 GitHub、X 和 Origin 等内置连接器）都必须按其发送请求的主机匹配一个允许的目的地，Bot 与不匹配者的连接会被拒绝。命令服务器不受影响。每个内置连接器需要的主机见 [MCP 服务器与网络策略](https://docs.x.ai/grok-bot/security#mcp-servers-and-the-network-policy)。

Enterprise 套餐可用。

#### 团队安装脚本

在每个团队计算机上运行的安装脚本清单，让相同的工具在所有计算机上都存在。在 Grok Bot 页面的 **Bot 计算机**下找到**团队安装脚本**（Team Setup Scripts）。不要把机密值写进安装脚本；脚本需要凭据时，把它存为[团队密钥](#team-secrets)并从环境变量读取。成员在应用中看不到这些脚本。清单如何运行，以及如何安装连接到私有服务的网络客户端，见[连接到私有网络](https://docs.x.ai/grok-bot/private-networks)。只在某一批人的计算机上运行额外脚本，可在[组设置](#group-settings)下添加。

Enterprise 套餐可用。

#### 团队密钥

团队范围的值，团队安装脚本将其作为环境变量读取，这样脚本可以持有许可证密钥、认证密钥或服务令牌，而值不出现在清单里。在 Grok Bot 页面的**团队密钥**（Team Secrets）下添加：每个密钥是一个环境变量名和一个值。Cursor 加密存储该值，保存后仪表盘不再显示它。团队管理员（包括不付费的管理员）可以添加、替换或删除它们。

它们如何到达计算机：

* 团队安装清单中的每个安装脚本和检查脚本，以及组[安装脚本](#group-settings)中的脚本，都会在其环境中带上团队的密钥运行。按名称引用密钥，例如 `"$MY_LICENSE_KEY"`。
* 密钥只存在于脚本的进程环境中。脚本结束后值就消失，除非脚本把它写到了某处，因此不要在计算机上存放任何你不希望该成员运行的每个 Bot 都能访问的内容。
* 脚本输出在记录日志前会检查是否含密钥值，匹配的会被遮蔽。
* 只有当一台计算机的团队安装恰好来自一个团队时，它才会收到密钥。如果成员的计算机应用了两个或更多团队的安装，则不会从其中任何一个团队获得密钥，因为不同团队的脚本共用一个计算机用户。
* 更改（包括轮换的值）在脚本下次运行时生效：计算机启动时、定期刷新时，或你重建它时。见[推广到现有计算机](https://docs.x.ai/grok-bot/private-networks#roll-out-to-existing-computers)。

限制：每个团队最多 100 个密钥，每个值最多 32 KB，总计最多 96 KB。名称必须是有效的环境变量名，计算机运行时保留的名称（如 `PATH`、`HOME`，以及任何以 `SAND_` 或 `LD_` 开头的名称）在保存时会被拒绝。团队密钥用于你控制的脚本。它们不会让 Bot 直接获得某个值，也与[成员存在 Bot 上的密钥](https://docs.x.ai/grok-bot/vault)分开。它们不能通过管理 API 使用。

Enterprise 套餐可用。

#### 允许在 Bot 计算机上使用 sudo

让 Bot 在自己的计算机上以 root 运行命令。开关在 Grok Bot 页面的 **Bot 计算机**下，默认开启。现有计算机在重启后采用更改。

Enterprise 套餐可用。

#### 管理成员计算机与数据

让管理员一次重建、终止或永久删除许多成员的计算机，或删除他们的所有 Grok Bot 数据，并给出每位成员的结果。在 Grok Bot 页面的**安全与合规**下找到。**重建**（Recreate）把成员迁移到最新镜像和团队安装脚本，同时保留他们的 Bot、文件和登录。**终止**（Terminate）结束成员当前的工作并保留持久磁盘；该成员的下次会话会在其上启动一台新计算机。**删除**（Delete）移除计算机及其存储的文件，该成员的下次会话会启动一台空计算机。要自动删除不活跃的计算机，使用[计算机保留期](#data-retention)。这些都不会移除访问权：要移除访问权，请把成员从团队中移除，或为其组关闭 Grok Bot，并在身份提供商中撤销其会话。见[管理 Grok Bot 计算机](https://docs.x.ai/grok-bot/computers)。

Enterprise 套餐可用。

### 日志与审计

记录什么，以及记录到哪里。

#### 操作记录

记录 Bot 做了什么：每次工具调用及其结果、允许或拒绝它的决定（自动审查、钩子或成员）、连接器（MCP）工具调用、shell 命令、浏览器导航、计算机使用会话、文件传输、Bot 发送的消息、例程运行、护栏干预、它读取的技能，以及交给子智能体或云端智能体的工作。事件是元数据，在存储或导出前经过清理。shell 命令会擦除密钥；浏览器导航保留每个页面的 `scheme://host/path` 和标题，但去掉查询字符串和凭据；计算机使用会话记录操作和截图的次数以及会话时长，不含截图、点击或输入的文字；其他每个事件携带 id、结果和时长，从不含工具参数、文件路径或消息内容。开关在 Grok Bot 页面上，默认关闭。记录的事件不会出现在审计日志页面上。要在自己的收集器中接收它们，请配置 [OpenTelemetry 导出](https://cursor.com/docs/enterprise/opentelemetry-export)，它把每个事件标记为 `cursor.surface=grok_bot` 后投递；[Wire 参考](https://cursor.com/docs/enterprise/opentelemetry-export/wire#shared-grok_bot-attributes)列出每个事件和属性。保留细节见[日志与审计](https://docs.x.ai/grok-bot/security#logging-and-audit)。

Enterprise 套餐可用。

#### 审计日志

管理员、安全和认证事件，以及 Grok Bot 控制平面事件：Bot 创建、成员访问更改、团队安装清单、MCP 认证、Slack 账户关联和例程。每一行都标明执行操作的应用，因此你可以把日志筛选到 Grok Bot。在[审计日志页面](https://cursor.com/dashboard/audit-log)查看，或流式传输到你的 SIEM；见[审计日志](https://cursor.com/docs/enterprise/compliance-and-monitoring#audit-logs)。Bot 执行的操作请用[操作记录](#action-recording)。

Enterprise 套餐可用。

#### OpenTelemetry 导出

把 Cursor 的用量指标和日志（包括记录下来的 Grok Bot 操作）流式传输到你运行的收集器。这是客户获取操作记录事件的路径。在**团队设置 → OpenTelemetry 导出**下配置。端点要求和事件模式见 [OpenTelemetry 导出](https://cursor.com/docs/enterprise/opentelemetry-export)。

Enterprise 套餐可用。

#### 数据保留

在你选择的期限过后自动删除 Grok Bot 数据。这些设置在 Grok Bot 页面的**数据保留**（Data Retention）下。每项都默认关闭。

| 设置 | 删除什么 | 期限 |
| --- | --- | --- |
| **Bot 保留期**（Retention Period for Bots） | 在期限内无人发消息的 Bot，及其对话、记忆、技能和例程。Bot 的所有者在删除前 30 天收到邮件，在该窗口内发一条消息即可保留 Bot。 | 60 至 365 天 |
| **计算机保留期**（Retention Period for Computers） | 成员的计算机及其文件，条件是期限内无人给他们的任何 Bot 发过消息。见[自动删除不活跃的计算机](https://docs.x.ai/grok-bot/computers#delete-inactive-computers-automatically)。 | 30 至 365 天 |
| **消息保留期**（Retention Period for Messages） | 超过期限的 Bot 消息和附件，每天执行。不通知任何人。 | 30 至 365 天 |

打开某项设置或缩短期限会先要求你确认。删除的数据无法恢复。每次更改和删除都记录在[审计日志](https://cursor.com/dashboard/audit-log)中。

Enterprise 套餐可用。

### 组设置

上述控制设定团队范围的基线。要为某一批人放宽该基线，从[成员 > 组](https://cursor.com/dashboard/members?subtab=groups)打开你的团队拥有的组，使用其 **Grok Bot** 标签页。除网络策略外，组设置只会放宽：组可以给成员比团队允许的更多权限，绝不少于此，属于多个组的成员得到最宽松的结果。这与[组模型访问](https://cursor.com/docs/enterprise/model-and-integration-management#how-team-and-group-model-access-combine)的规则相同。组控制若保持团队的值则不会改变任何东西，因此请在 Grok Bot 页面收紧控制，再按组放宽。

该标签页有四部分：

* **Bot 能力。** 当团队关闭或设置更严格时，为组成员允许[云端智能体](#cloud-agents)、[智能体邮箱](#agent-email)或[允许本地出口路由](#allow-local-egress-routing)，或提高[在本地计算机上执行](#execution-on-local-computer)的上限。对于自动审查，**不对该组强制**会解除团队的[强制自动审查](#enforce-auto-review)锁定，让组成员可以关闭自动审查；组自动审查规则与团队的[自动审查规则](#auto-review-rules)合并，规则冲突时**先询问**优先。
* **网络。** 组自己的网络策略，如[网络控制](#network-controls)所述。它替代组员的团队策略，无论更宽松还是更严格，属于多个组的成员得到最严格的一个。锁定的团队策略适用于所有人。**应用于 MCP 服务器**只在团队的 Grok Bot 页面上设置；组继承它，无法关闭。被阻止的站点则累加：选择**团队策略，但除这些站点外**（Team Policy, Except These Sites），在团队策略之上为组员阻止更多站点。团队阻止的站点对组员始终保持阻止，无论组如何设置；组阻止的站点即使团队策略被锁定也保持阻止。
* **组规则。** 该组 Bot 的规则，与[团队规则](#team-rules)合并。成员无法关闭它们。
* **安装脚本。** 与[团队安装脚本](#team-setup-scripts)一起在组员计算机上运行的清单。它们使用相同的结构、以相同方式运行，同样适用不得包含密钥的规则，并读取与团队清单相同的[团队密钥](#team-secrets)；没有组级密钥。见[团队安装如何运行你的脚本](https://docs.x.ai/grok-bot/private-networks#how-team-setup-runs-your-scripts)。

组设置适用于你的团队拥有的组，无论你手工管理成员关系还是通过 [SCIM](https://cursor.com/docs/account/teams/scim#directory-groups) 同步。它们与[组织组](https://cursor.com/docs/enterprise/organization-groups)是分开的。要控制谁可以使用 Grok Bot，请改用 Grok Bot 页面上的**管理组访问权限**；见[为团队启用 Grok Bot](#enabling-grok-bot-for-your-team)。

Enterprise 套餐可用。

## 管理 API

通过[管理 API](https://cursor.com/docs/account/teams/admin-api#grok-bot)启用 Grok Bot 并管理能力、强制自动审查、组访问、网络策略、团队规则和安装脚本。[团队密钥](#team-secrets)只能从仪表盘管理。

要从脚本重建、终止或删除成员的计算机，或删除他们的所有 Grok Bot 数据，请使用[组织 API](https://cursor.com/docs/account/organizations/organization-admin-api#grok-bot-computers)。它需要一个带 `admin:*` 作用域的 Organization API 密钥，因为一台计算机服务于成员所属的每个团队。

## 安全

安全模型、网络策略、审批与 Auto Review、身份、日志、数据处理和认证见 [Grok Bot 安全](https://docs.x.ai/grok-bot/security)。常见评审问题见 [Grok Bot 安全 FAQ](https://docs.x.ai/grok-bot/security-faq)。要让你自己的 AI 安全服务器检查每个模型请求，见 [Grok Bot 推理钩子](https://docs.x.ai/grok-bot/inference-hooks)。

## 推荐配置

对安全敏感的部署，这是推荐的基线。

对管理员：

1. 配置网络控制。仅限 Enterprise。没有策略的团队默认全放行。自助式 Teams 无法设置。如果你选择允许列表模式并希望它也覆盖已连接应用，请把连接器使用的主机（例如 `api.github.com`、`api.x.com`、`api.origin.cursor.com`）加入列表，然后开启**应用于 MCP 服务器**；在你开启之前它是关闭的。见 [Grok Bot 安全](https://docs.x.ai/grok-bot/security#network-policy)。
2. 在启用 Grok Bot 之前审计团队市场中的连接器策略。任何被允许的连接器都可供成员运行的每个 Bot 使用。
3. 在依赖团队规则之前开启强制自动审查。仅限 Enterprise。成员可以在其上添加更严格的个人规则，规则冲突时**先询问**优先。
4. 除非 Bot 需要在成员机器上操作，否则把在本地计算机上执行设为**永不允许**。默认把选择权留给每位成员。
5. 如果不需要委派，禁用云端智能体派生。
6. 除非成员应当把 Bot 模板发布到团队之外，否则保持公开模板分享关闭。
7. 如果 Team Bot 应先经过审核再让队友使用，把 Bot 分享设为**仅管理员**。Team Bot 会带着其所有者的应用、密钥和文件进入每个队友的聊天。
8. 除非 Team Bot 应通过一个管理者的账户为所有使用者行事，否则保持允许共享登录关闭。
9. 添加团队自动审查规则。仅限 Enterprise。覆盖应始终先询问或可自动继续的操作。生产部署、对外邮件、付款和接受法律条款是很好的**先询问**例子。自动规则保持范围窄。
10. 通过身份提供商限制登录到受管设备。Grok Bot 登录使用你的 SSO，因此感知设备的登录策略会作用于它。这限制的是登录，不是托管计算机本身。

对成员：

1. 绝不把凭据粘贴到聊天中。带遮蔽的密钥请求是受支持的路径。
2. 对涉及账户、金钱或共享资源的操作，优先选**允许一次**（Allow once）而不是**始终允许**。
3. 把 Bot 的浏览器登录到与任务规模相称的账户，并退出它不再需要的账户。在源系统支持时使用限定范围的服务账户。
4. 新角色从只读任务和草稿输出开始，把发送、发布、购买、删除和生产变更留在审批之后。
5. 定期检查已连接应用和活跃例程，源系统变化时暂停例程。

## FAQ

### 我可以为团队开启或关闭 Grok Bot 吗？

组织级的**启用 Grok Bot**开关仅限 Enterprise。它位于 Cursor 仪表盘的 Grok Bot 页面。自助式 Teams 没有这个开关。禁用会阻止成员，但不会删除他们的计算机。

### 我可以通过管理 API 管理 Grok Bot 吗？

可以。使用[管理 API](https://cursor.com/docs/account/teams/admin-api#grok-bot)。

### 我可以设置 Grok Bot 支出上限吗？

目前没有单独的 Grok Bot 支出上限。账户级的按需控制适用，按产品划分的用量在仪表盘的用量页面上。

### 为什么成员看到某个应用被团队管理员禁用？

你团队的连接器策略阻止了该服务器。在**团队市场**（Teams Marketplace）中启用它，如果你使用 MCP 允许列表，把其服务器 URL 加入，然后让成员重启应用。如果被允许的应用对普通成员仍然因厂商侧的权限错误而失败，请检查提供商的要求；有些厂商把其 MCP 端点限制为自己的管理员。见[连接应用](https://docs.x.ai/grok-bot/computer-and-apps#connect-an-app)。

### 成员如何请求访问权？

成员可以从应用发送请求。在管理员尚未完成设置的池化（pooled）Enterprise 团队中，成员会看到团队设置消息。下一步是管理员使用仅限 Enterprise 的启用开关。自助式 Teams 不使用该开关。

### 我可以看到团队用 Grok Bot 做了什么类型的工作吗？

可以，在所有 Enterprise 团队中。分析仪表盘的对话洞察（Conversation Insights）页面有一个 **Grok Bot** 来源，按工作类型（Type of Work）和自动化程度（Level of Automation）对 Bot 对话分组。见 [Grok Bot 对话洞察](https://cursor.com/docs/account/teams/analytics#grok-bot-conversation-insights)。

隔离、出口、审批、日志和数据处理的问题见 [Grok Bot 安全 FAQ](https://docs.x.ai/grok-bot/security-faq)。
