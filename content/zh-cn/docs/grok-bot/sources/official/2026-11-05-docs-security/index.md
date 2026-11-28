---
title: "文档：Grok Bot 安全"
linkTitle: "文档：安全"
date: 2026-11-05
originalTitle: "Grok Bot security"
sourceUrl: "https://docs.x.ai/grok-bot/security"
altUrls: ["https://cursor.com/docs/grok-bot/security"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：网络策略增为四种模式，新增 Allow All Sites Except These（至多 50 个站点）；应用聊天中 Bot 可见 Vault 已存卡的号码和安全码；Shared Bot 改称 Team Bot"
tags: [安全, 隐私, 运行环境, 模型]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文档给出控制路径：网络策略、审批与 Auto Review、推理钩子、身份与登录、日志审计、数据保留、模型、提示注入。网络策略有四种模式（Allow All Network Access、Allow All Sites Except These、Defaults + Team Allowlist、Team Allowlist Only），Enterprise 专有，未设置时默认全放行；屏蔽模式下 Blocked Sites 最多 50 个站点，按主机名匹配并含子域，是尽力而为而非安全边界。批准环节有 Allow once、Always allow、Deny，Auto Review 是独立审查模型，评估 shell 命令、应用调用、计算机使用、自动化写入和委派；Action Recording 为 Enterprise 专有，默认关闭，保留 90 天。Bot 没有自己的身份，连接器令牌留在 Cursor 后端；Vault 中的登录和 Secure Form 的值由系统填入、模型不接收，但在 Grok Bot 应用的聊天中，Bot 能看到已存卡的号码和安全码以便在结账时填写，Vault 不适用于 Team Bots。计算机位于美国，模型由系统自行选择，没有模型选择器，团队模型允许列表不适用；对提示注入采取分层防护，并说明只能降低而不能消除风险。

**保留理由**：这是安全和隐私最系统的一篇，覆盖网络、审批、凭证、日志、数据保留、模型和提示注入，且明确写出哪些不审查，是评估 Bot 信任边界的主要依据。

---

Grok Bot 安全

用这些控制项和部署细节来判断是否允许在组织内使用 Grok Bot，并限制 Bot 可以访问、更改和保留什么。上线步骤和仪表盘设置清单见[面向团队和企业的 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises)。常见审查问题见 [Grok Bot 安全常见问题](https://docs.x.ai/grok-bot/security-faq)。

> **仅 Enterprise**，位于 Grok Bot 仪表盘：组织级启用开关、**网络控制（Network Controls）**、**团队设置脚本（Team Setup Scripts）**、[**团队密钥（Team Secrets）**](https://docs.x.ai/grok-bot/teams-and-enterprises#team-secrets)、**操作记录（Action Recording）**、**允许本地出口路由（Allow Local Egress Routing）**、**允许在 Bot 计算机上使用 sudo（Allow Sudo on Bot Computers）**、**强制自动审查（Enforce Auto-review）**及其团队规则、**推理钩子（Inference Hooks）**，以及面向组织管理员的计算机管理。审计日志、OpenTelemetry 导出、MCP 允许列表和 SCIM 也仅限 Enterprise。自助 Teams 看不到这些设置。完整列表见[管理员控制项](https://docs.x.ai/grok-bot/teams-and-enterprises#admin-controls)。

## 架构

Grok Bot 的桌面和移动应用把每个请求发送到 Cursor 的服务器。从那里，工作在成员的托管计算机上运行，提示词发往模型提供方，工具调用通过已连接应用到达第三方服务。

每条路径上都有一个控制点。每个控制点都链接到本页对应的小节。

## 网络策略

**网络控制仅限 Enterprise。** 管理员在 Cursor 仪表盘的 [Grok Bot 页面](https://cursor.com/dashboard/bot)中，于 **网络（Network）** 下的 **Grok Bot 网络访问（Grok Bot Network Access）** 设置 Grok Bot 网络策略。它控制团队计算机可以到达哪些目标。自助 Teams 看不到这个面板，也不能设置目标允许列表。没有策略的团队默认全部允许。

| 模式 | 效果 |
| --- | --- |
| **允许所有网络访问（Allow All Network Access）** | 所有目标。没有策略的团队会得到这个模式。 |
| **除这些站点外全部允许（Allow All Sites Except These）** | 除你屏蔽的站点外的所有目标。见[被阻止的站点](#blocked-sites)。 |
| **默认站点 + 团队允许列表（Defaults + Team Allowlist）** | Cursor 的默认目标加上你的列表 |
| **仅团队允许列表（Team Allowlist Only）** | 只有你的列表，加上计算机运行所必需的目标 |

* 允许列表模式中的**目标（Destinations）**既包括 Web 域名，也包括用于原始连接的带端口 IP 范围，条目数量不设上限。
* **目录群组。仅限 Enterprise，位于网络控制内。** 群组可以设置自己的网络策略，对该群组成员取代团队策略；锁定后，团队策略对所有人生效。
* **该策略与 Cloud Agent 的网络设置相互独立。** 运行中的计算机会在一分钟左右自动应用更改。休眠中的计算机在下次唤醒时应用更改。你不需要重建计算机。
* **限制出口会限制数据可以发送到哪里。** 要按自己的数据丢失防护策略检查到达模型的内容，请使用[推理钩子](#inference-hooks)。

屏蔽一个应用并不会屏蔽该服务的网站。连接器策略和网络策略是彼此独立的两层，要同时关闭两条路径，需要同时使用这两个控制项。

### 被阻止的站点

**除这些站点外全部允许**让团队计算机可以到达除 **被阻止的站点（Blocked Sites）** 下列出的站点之外的所有目标。群组选择 **团队策略，除这些站点外（Team Policy, Except These Sites）**，在团队策略之上再屏蔽更多站点。团队或群组只能使用允许列表或被阻止站点中的一种，不能同时使用。

* **只接受主机名。** 每行输入一个站点，例如 `example.com`，不带协议、端口或路径。不接受 IP 地址。每个站点也会屏蔽其子域，因此 `example.com` 和 `*.example.com` 是同一条目，列表会把它们保存为一条。
* **最多 50 个站点。** 该上限把团队列表和每个群组的列表合在一起计算。
* **Grok Bot 需要的站点保持开放。** 如果列表指定了计算机运行所必需的站点，或 Grok Bot 通过 Cursor 代理访问的站点，保存会被拒绝。
* **覆盖范围。** 计算机上的 Shell 命令和浏览器、WebFetch，以及已连接应用（MCP 服务器）。位于被屏蔽站点上的远程 MCP 服务器，如果未开启 **应用到 MCP 服务器（Apply to MCP servers）**，会被拒绝。当成员让流量经自己的桌面转出时，被屏蔽的站点在这条路由上仍然被屏蔽。
* **生效时间。** 更改无需重置即可到达计算机。
  * 运行中的计算机通常在一分钟左右应用更改。休眠中的计算机在下次唤醒时应用。
  * 已在运行的任务中的 Web 获取会用旧列表完成。新列表从下一个任务开始适用。
  * 对于 MCP 服务器，更改最多可能需要约一分钟生效。
  * [让流量经成员桌面转出](https://docs.x.ai/grok-bot/settings-and-notifications#route-traffic-through-your-desktop)的计算机，可能会在某个空闲时刻重启一次以应用更改，文件和登录状态会保留。如果你一天内多次更改列表，较晚的更改可能要等到下次重启。要立即应用，请从[管理成员计算机与数据](https://docs.x.ai/grok-bot/teams-and-enterprises#manage-member-computers-and-data)重建计算机。

在依赖它之前，先了解其限制：

* **尽力而为，不是安全边界。** 匹配按主机名进行。发往裸 IP 地址的请求可以通过，一些应用和加密连接也可能通过。
* **WebSearch 不会被过滤。** 搜索结果仍可能列出被屏蔽站点的页面。用 WebFetch 或浏览器打开会被拒绝。
* **WebFetch 会停止渲染页面。** 当列表屏蔽了任何站点时，对所有适用该列表的人来说，WebFetch 都会以纯 HTML 读取页面，不运行其中的脚本。用 JavaScript 构建内容的页面可能返回空白。
* **浏览器中没有拦截页。** 被屏蔽的 HTTPS 站点会显示浏览器安全或连接错误，而不是一个说明站点被屏蔽的页面。Shell 命令会收到 HTTP 403 响应，WebFetch 和 MCP 会返回一条写明被屏蔽站点的消息。

### MCP 服务器与网络策略

网络策略管的是团队计算机把流量发往哪里。已连接应用（MCP 服务器）不同：Bot 从 Cursor 的服务器访问远程 MCP 服务器，所以允许列表模式本身并不覆盖它们。要让它们也遵守同一份列表，请开启 **应用到 MCP 服务器**。该开关位于 **Grok Bot 网络访问** 中 **允许的目标（Allowed destinations）**（旧设置页为 Allowed Destinations）之下、**对所有群组锁定（Lock for all groups）**（Lock for All Groups）之上，并且只在选中 **默认 + 允许列表（Default, plus the allowlist）**（Defaults + Team Allowlist）或 **仅允许列表（Allowlist only）**（Team Allowlist Only）时出现。

* **关闭，这是每个团队的默认值。** 无论网络策略怎么说，Bot 都可以连接连接器策略允许的任何 MCP 服务器。
* **开启。** 远程 MCP 服务器还必须匹配 **允许的目标** 中的某个条目。不匹配的服务器会在 Bot 尝试使用时被拒绝，成员会看到需要请管理员添加哪个目标。在计算机上运行的命令服务器不受影响；网络策略已经适用于它们。

在依赖它之前先打开开关：允许列表模式本身并不限制 MCP 服务器。该开关是团队设置。目录群组会继承它，且不能关闭；锁定的团队策略也包含它。保存它不会重启计算机；它适用于下一次 MCP 连接。它与团队设置中 **MCP 配置（MCP Configuration）** 下的设置相互独立，后者管的是编辑器中的 Cursor；改一个不会改另一个。

**内置连接器也会被检查。** 该开关覆盖 Bot 使用的每个已连接应用，包括 Cursor 在 **连接应用（Connect apps）** 下替你运营的那些，例如 GitHub、X、Origin、Google Workspace 和 Microsoft 365。已连接应用是按它发送请求的主机来检查的，而不是按连接器列表里的名字，所以在打开开关之前，先把那些主机加入 **允许的目标**。主机未全部获准的连接器，会在 Bot 下次使用时被拒绝，并显示消息
`MCP server "<host>" refused: it is not on your team's Grok Bot network allowlist (Grok Bot settings > Network > Allowed destinations). A team admin can add it.`

| 已连接应用 | 需要允许的主机 |
| --- | --- |
| GitHub | `api.github.com` |
| X | `api.x.com` |
| Origin | `api.origin.cursor.com` |
| Gmail | `gmail.googleapis.com`；如果连接器是通过 Google 的托管地址添加的，还需要 `gmailmcp.googleapis.com` |
| Google Calendar | `www.googleapis.com`；如果通过 Google 的托管地址添加，还需要 `calendarmcp.googleapis.com` |
| Google Drive | `www.googleapis.com`、`sheets.googleapis.com`；如果通过 Google 的托管地址添加，还需要 `drivemcp.googleapis.com` |
| Google Docs | `docs.googleapis.com` |
| Google Sheets | `sheets.googleapis.com` |
| Google Slides | `slides.googleapis.com`、`slidesmcp.googleapis.com` |
| Google Ads | `googleads.googleapis.com` |
| Outlook、Outlook Calendar、OneDrive、Microsoft Teams | `graph.microsoft.com` |
| Stripe Link | `api.link.com` |
| Tailscale | `api.tailscale.com`、`login.tailscale.com` |
| QuickBooks Online | `ah-api.merge.dev`、`quickbooks.api.intuit.com`（沙盒公司为 `sandbox-quickbooks.api.intuit.com`）、`oauth.platform.intuit.com`、`developer.api.intuit.com` |
| Workday | `ah-api.merge.dev`，加上连接器设置中填写的你方 Workday 租户的登录和 REST API 主机 |
| WhatsApp Business | `ah-api.merge.dev`、`graph.facebook.com` |
| Zoho CRM、Zoho Books | `ah-api.merge.dev`，加上你的 Zoho 数据中心账号主机和 API 主机，例如美国为 `accounts.zoho.com` 和 `www.zohoapis.com`（`.eu`、`.in`、`.com.au`、`.jp`、`.sa`、`.uk`、`.ae`、`.sg`，加拿大为 `accounts.zohocloud.ca` 和 `www.zohoapis.ca`） |
| Zoho Desk | `ah-api.merge.dev`，加上你所在数据中心的账号主机及其 Desk 主机，例如 `accounts.zoho.com` 和 `desk.zoho.com` |
| Microsoft Power BI | `api.powerbi.com` |
| Databricks Genie | 你的 Databricks 工作区主机，即团队管理员在插件设置中填写的地址，例如 `dbc-a1b2c3d4-e5f6.cloud.databricks.com` |
| Google BigQuery | `bigquery.googleapis.com` |
| Asana | `mcp.asana.com` |
| Vanta | 登录时选择区域对应的主机：`mcp.vanta.com`（美国）、`mcp.eu.vanta.com`（欧洲）或 `mcp.aus.vanta.com`（澳大利亚） |
| Shop Pay | `mcp.shop.com` |

团队市场中的其他连接器，按其服务器地址中的主机检查，该地址显示在仪表盘的[插件与 MCP 页面](https://cursor.com/dashboard/plugins)；请允许该主机。

## 静态出口 IP

托管计算机默认通过共享的静态出口 IP 地址访问互联网。这些范围由 Grok Bot 客户共用，不提供按客户专用的 IP，因此应把这些范围视为标识 Grok Bot 流量，而不是只标识你的团队。当前范围可向你的客户团队索取；产品侧的控制项是目标允许列表，而不是源 IP 编辑器。

如果成员设备位于 Zscaler 或其他检查 TLS 的网关之后，请在所有配置文件中允许 Cursor 的域名并将其排除在检查之外，包括离开网络时。见[配置检查 TLS 的代理](https://docs.x.ai/grok-bot/proxies)。

成员可以让流量经自己的桌面转出，以使用其 IP 地址；解析到私有地址或 VPN 地址的站点在这条路由上仍会被屏蔽，除非已为你的组织允许。**团队设置脚本** 仅限 Enterprise。这些团队还可以在每台团队计算机上安装自己的网络客户端。这两条路径都与共享出口范围相互独立。见[连接到私有网络](https://docs.x.ai/grok-bot/private-networks)。

## 审批与 Auto Review

审批让重要操作保持在成员控制之下。最强的边界是请求本身里的那条边界，所以让成员说明 Bot 可以更改什么、必须在哪里停下：

> Reconcile the campaign data and draft a recommended budget change. Do not change the campaign or message the agency. Ask for approval after showing the current value, proposed value, and expected impact.

（译注：意为「核对营销活动数据，起草一份建议的预算调整。不要更改活动，也不要联系代理机构。在展示当前值、建议值和预期影响后请求批准。」）

当某个操作需要批准时，对话会显示拟执行的操作及其输入。**允许一次（Allow once）** 让 Bot 继续执行该操作，**始终允许（Always allow）** 可以保存一条匹配规则，**拒绝（Deny）** 则停止该操作；在成员发送另一条消息之前，Bot 不会再次尝试。iPhone 上的控制项相同。审批控制的是拟执行的操作，不是已经完成的工作；任何人都不应批准自己无法识别目标或影响的操作。

Auto Review 是这些提示背后的审查层：一个独立的审查模型，在风险操作运行前进行评估，覆盖 Shell 命令、应用调用、计算机使用、自动化写入（对例程和事件触发器的更改），以及 Cloud Agent 和子智能体启动等委派。它可以放行操作、要求批准或拒绝操作。

* **团队管理员可以强制启用 Auto-review。仅限 Enterprise。** 开关位于 Cursor 仪表盘的 Grok Bot 页面。开启后，成员不能关闭 Auto-review，除非其所属群组用 **对此群组不强制（Don't enforce for this group）** 解除锁定；见[群组设置](https://docs.x.ai/grok-bot/teams-and-enterprises#group-settings)。
* **管理员可以添加团队 Auto-review 规则。仅限 Enterprise。** 这些规则也在 Grok Bot 页面上。它们适用于每位成员的 Bot，在成员设置表中显示为锁定行，并在管理员添加、编辑或删除规则时自动保存。如果管理员关闭强制启用，团队规则停止适用，成员回到只使用自己的规则。
* **成员可以添加个人规则**，位置在 **设置（Settings）→ 通用（General）→ Auto-review** 的 **自定义规则（Custom rules）** 中。**先询问（Ask first）** 规则总是拦下匹配的操作，**自动允许（Allow automatically）** 规则只在审查模型没有发现其他阻止理由时，才让匹配的操作继续。成员可以在团队规则之上添加个人规则，但这些规则只会让行为更严格；规则冲突时 **先询问** 优先。规则要保持狭窄，并绑定到已知操作，例如「发送任何外部邮件前先询问」或「在 `/workspace/reports` 中运行 `git status` 时自动允许」。避免「允许浏览器里的一切」这类宽泛规则。个人规则保存到成员账号，因此会从每台桌面和移动应用生效。
* **它不会审查每一个副作用。** 记忆写入和大多数设置更改就是例子。应把它视为明确边界和最小权限的补充，与不依赖模型判断的控制项一起使用：逐操作审批、网络策略和按用户隔离。

## 推理钩子

推理钩子会把每个 Grok Bot 模型请求签名后发送到你组织运行、或通过安全厂商使用的 AI 安全服务器。你的服务器在模型运行前允许或拒绝请求，因此你自己的策略检查会覆盖提示词和 Grok Bot 收集的内容，例如网页和应用结果。新配置从影子模式（Shadow mode）开始，只把拒绝写入审计日志，不阻止任何东西。

推理钩子检查的是模型输入，不是运行中的操作。要继续用网络策略和 Auto Review 控制 Bot 的行为。设置、模式、请求格式和审计事件见 [Grok Bot 推理钩子](https://docs.x.ai/grok-bot/inference-hooks)。

推理钩子处于 beta，面向所有 Enterprise 团队开放。

## 身份与登录

成员用 Cursor 账号登录 Grok Bot，因此你现有的 Cursor SSO 配置会生效。SAML 2.0 单点登录支持 Okta、Microsoft Entra、Google Workspace 和 OneLogin，并且可以要求所有成员使用 SSO（这会阻止密码登录）。**SCIM 仅限 Enterprise：** SCIM 2.0 配置与取消配置。Okta 和 Entra ID 的逐步配置，包括应用分配和计算机浏览器的登录规则，见[配置身份与访问](https://docs.x.ai/grok-bot/identity-and-access)。

在托管计算机内，成员通过你自己的身份提供方在浏览器中登录应用，相当于配置一台新笔记本电脑。你的会话策略管这些会话，在身份提供方中撤销该用户会结束它们。

Bot 没有自己的身份或凭证：

* **Bot 以已登录成员的身份行动。** Bot 永远不会拥有超过其所属个人的访问权，每个操作都可归到具名成员；除你的身份提供方之外，没有单独需要配置、轮换或审计的机器身份。团队管理的连接器是唯一例外：它们可以使用团队或服务账号凭证。
* **连接器令牌留在 Cursor 后端。** Bot 调用工具时不会收到 OAuth 令牌，令牌也从不存储在计算机上。
* **凭证不进入模型。** 登录时，Bot 使用成员保存在 Vault 中的登录信息、已连接的密码管理器，或成员在安全表单（Secure Form）中输入的值。这些值以引用方式填入页面：模型永远不会收到已保存的密码，也收不到成员在安全表单中输入的内容。Bot 可以看到保存了哪些登录信息，以及成员保存的联系信息。在 Grok Bot 应用的聊天中，它还能看到成员保存在 Vault 中的银行卡号码和安全码，以便在结账时输入。对于单点登录、通行密钥（passkey）以及表单无法处理的其他步骤，Bot 会把计算机交给成员。
  对于 API 密钥或其他机密，安全密钥卡会遮蔽其值，并让它不进入对话记录、不接近模型。保存在 Vault 中的卡在结账时直接填入，无需每次单独批准，因此希望逐笔批准付款的成员不应保存该卡。Vault 在 Team Bot 上不可用。密码和一次性验证码永远不应出现在普通聊天中。见[安全存储机密](https://docs.x.ai/grok-bot/vault)。

要结束成员当前的工作，组织管理员从仪表盘终止该成员的计算机；见[管理 Grok Bot 计算机](https://docs.x.ai/grok-bot/computers)。该控制项仅限 Enterprise。它会停止运行中的 Bot，保留持久磁盘，成员的下一个会话会启动一台新计算机。它不会移除访问权。要移除访问权，请把成员从团队中移除，或为其所在群组关闭 Grok Bot，并在身份提供方中撤销其会话。应用会话只保留在成员的计算机上。

当某个项目或登录不应再可用时，成员应直接清理：暂停或删除相关例程，在计算机上退出网站登录，移除已连接应用并在源服务中撤销其授权，从 `/workspace` 中移除敏感文件。删除 Bot 不会移除计算机文件或浏览器会话。

## 日志与审计

审计日志和操作记录使用彼此独立的管道。审计日志覆盖管理和安全事件，包括 Grok Bot 控制平面操作。操作记录捕获 Bot 操作；配置后，OpenTelemetry 导出会把这些事件发送到你的收集器，并标记 `cursor.surface=grok_bot`。

* **审计日志。仅限 Enterprise。** 覆盖管理员、安全和认证事件，以及 Grok Bot 控制平面事件：Bot 创建、成员访问权更改、团队设置清单、MCP 认证、Slack 账号关联和例程。可在仪表盘中按应用过滤，或流式发送到你的 SIEM。自助 Teams 没有这份日志。
* **操作记录。仅限 Enterprise。** 它是 Grok Bot 页面上的设置，默认关闭。团队启用后，Cursor 会把 Bot 操作记录到内部存储中，保留 90 天，其中包括经过清洗的 Shell 命令。操作记录事件不会出现在审计日志页面。要在自己的收集器中接收脱敏事件，请配置 [OpenTelemetry 导出](https://cursor.com/docs/enterprise/opentelemetry-export)，它同样仅限 Enterprise。隐私模式（旧版）（Privacy Mode (Legacy)）会强制关闭记录。

## 端点工具

Grok Bot 不提供内置的、面向客户的遥测或 EDR 数据流。这些计算机是 Cursor 运营的基础设施，Cursor 会为其运行健康状况和滥用行为做监控，遥测有意排除客户数据。**团队设置脚本** 仅限 Enterprise。这些管理员可以在每台团队计算机上安装自己的工具。

## 数据保留与删除

每位成员的计算机把本地文件、浏览器会话以及浏览器中保存的任何内容保存在持久磁盘上，跨会话保留。连接器令牌从不存储在计算机上。

* **空闲计算机会自动休眠。** 休眠不是删除。
* **镜像更新会保留文件。** 使用过期系统镜像的计算机会在新镜像上重建，成员文件会保留。
* **成员重置会保留已保存的数据。** 成员可以从桌面应用重置自己的计算机。与恢复（Recover）一样，重置会从最后一次保存的数据重建计算机；如果无法连上计算机先做保存，非常近期的更改会丢失。见 [Grok Bot 计算机](https://docs.x.ai/grok-bot/computer-and-apps#update-recover-or-reset-the-computer)。
* **删除遵循 DPA。** 根据[数据处理协议（Data Processing Agreement）](https://cursor.com/terms/dpa)，服务结束后，数据会在收到书面指示后 30 天内删除或返还。
* **备份每天运行。** Cursor 的生产控制平面由每日加密备份覆盖，并复制到独立的恢复设施。

目前不提供客户管理的单台计算机时间点恢复。

## 数据驻留

Grok Bot 计算机运行在美国。Grok Bot 也属于 Cursor 的美国数据驻留计划。启用后，Grok Bot 的推理、数据处理和存储都留在美国。请联系你的客户团队加入。支持的模型、排除项和定价见[美国数据驻留](https://cursor.com/docs/enterprise/privacy-and-data-governance#us-data-residency)。

## 模型与数据

Grok Bot 自行管理模型选择。没有面向客户的模型选择器，服务组合可能随时间变化，不保证固定的厂商集合。每个请求会发往 SpaceXSI 的一手模型，或[子处理者列表](https://trust.cursor.com/subprocessors)中某家提供方的第三方模型。用量和支出视图把这类活动记为 Grok Bot 用量，而不是按模型记录。见[我可以选择模型吗？](https://docs.x.ai/grok-bot/faq#can-i-pick-the-model)。

* **团队模型允许列表不管 Grok Bot。** Grok Bot 使用 SpaceXSI 的一手模型，并且可能使用第三方模型，无论你的[模型访问控制](https://cursor.com/docs/enterprise/model-and-integration-management#model-access-control)设置如何。设有模型允许列表的团队在启用 Grok Bot 时会看到这项确认。如果你的合同限制子处理者，请联系客户团队。
* **隐私模式适用。** 成员在团队期间，团队隐私模式管着他们；启用隐私模式时，客户数据不会用于训练。
* **零数据保留（Zero Data Retention）遵循 Cursor 现有的提供方协议。** 模型提供方不保留提示词或输出，Grok Bot 不另加控制项。提供方可能运行滥用和安全分类器，被标记的数据可能被存储用于调查。

## 本地执行

Bot 可以通过桌面应用在成员自己的机器上行动：运行命令、读取文件，以及在云计算机和本地机器之间移动文件。这与托管计算机内的工作相互独立，有自己的控制项，也不同于管托管计算机内工作的 Auto Review。

默认是逐条命令审批，审批卡会显示确切命令。成员在 **设置 → 计算机（Computer）→ 你的计算机（Your computer）** 的 **在本计算机上执行（Execution on this computer）**（桌面尚未列出时为 **在本地计算机上执行（Execution on local computer）**）中选择策略：**每次询问（Ask every time）**、**始终允许（Always allow）** 或 **从不允许（Never allow）**。建议选择 **从不允许**，除非 Bot 有具体理由处理本地文件。管理员可以通过 Grok Bot 页面上的[在本地计算机上执行](https://docs.x.ai/grok-bot/teams-and-enterprises#execution-on-local-computer)为整个团队设定策略上限；成员自己的设置更严格时仍然适用。

## 托管

Grok Bot 只运行在 Cursor 托管的云计算机上。目前不支持本地部署、在你自己的边界内部署，以及自带镜像部署。托管计算机默认使用共享静态出口。成员可以让流量经自己的桌面转出，Enterprise 团队可以用 **团队设置脚本** 安装网络客户端。见[连接到私有网络](https://docs.x.ai/grok-bot/private-networks)。

## 提示注入

Bot 从外部世界读取的内容，例如网页、应用结果和命令输出，可能试图操纵它。Grok Bot 分层防御：强制启用时，Auto Review 会根据成员的请求检查 Bot 操作；在它之下，是不依赖任何模型判断的控制项，包括网络策略、逐操作审批和按用户隔离。外部内容在呈现给模型时会标记为不可信数据。使用[推理钩子](#inference-hooks)时，你自己的安全服务器还可以在下一次模型调用前筛查这些内容。这些控制项会降低但不能消除恶意内容带来的风险，这也是要把重要操作留在审批之后的另一个原因。

## 认证

Cursor 背后的公司 Anysphere 持有 Schellman 颁发的 ISO/IEC 27001 和 ISO/IEC 42001 认证，Grok Bot 在当前 ISO 范围内。ISO/IEC 27001 认证信息安全管理体系，即整个组织的安全计划。ISO/IEC 42001 认证 AI 管理体系，即 Cursor 如何治理它构建和运营的 AI。证书和报告可在 [trust.cursor.com](https://trust.cursor.com) 获取。
