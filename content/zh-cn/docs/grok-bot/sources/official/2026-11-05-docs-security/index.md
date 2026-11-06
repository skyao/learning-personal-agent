---
title: "文档：Grok Bot 安全"
linkTitle: "文档：安全"
date: 2026-11-05
originalTitle: "Grok Bot security"
sourceUrl: "https://cursor.com/docs/grok-bot/security"
altUrls: ["https://docs.x.ai/grok-bot/security"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 隐私, 运行环境, 模型]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文档给出控制路径：团队策略、网络策略、零数据保留、连接器令牌留在后端、Auto Review。网络策略有三种模式（全部放行、默认加团队允许列表、仅团队允许列表），Enterprise 专有，未设置时默认全放行；MCP 服务器需另开「Apply to MCP servers」才受同一名单约束。批准环节有允许一次、始终允许、拒绝，Auto Review 是独立审查模型，评估 shell 命令、应用调用、计算机使用、自动化写入和委派，但不审查记忆写入等副作用。Bot 没有自己的身份，只能做到所属成员能做的事；连接器令牌留在 Cursor 后端，保存在 Vault 的登录和卡由系统填入而不让模型看到。计算机为每用户一个 Firecracker microVM，位于美国；模型由系统自行选择，没有模型选择器，团队模型允许列表不适用。对提示注入采取分层防护，并说明只能降低而不能消除风险。

**保留理由**：这是安全和隐私最系统的一篇，覆盖隔离、网络、审批、凭证、日志、数据保留、模型和提示注入，且明确写出哪些不审查，是评估 Bot 信任边界的主要依据。

---

使用这些控制和部署细节，来判断是否允许 Grok Bot 进入你的组织，并限制 Bot 可以访问、更改和保留的内容。推广步骤和仪表板设置清单见[面向 Teams 和 Enterprise 的 Grok Bot](https://cursor.com/docs/grok-bot/teams)。常见审查问题见 [Grok Bot 安全常见问题](https://cursor.com/docs/grok-bot/security-faq)。

Grok Bot 仪表板上**仅限 Enterprise** 的项：组织范围的启用开关、**网络控制（Network Controls）**、**团队安装脚本（Team Setup Scripts）**、**团队秘密（Team Secrets）**、**操作记录（Action Recording）**、**允许本地出口路由（Allow Local Egress Routing）**、**允许在 Bot 计算机上使用 Sudo（Allow Sudo on Bot Computers）**、**强制自动审查（Enforce Auto-review）**及其团队规则、**推理钩子（Inference Hooks）**，以及面向组织管理员的计算机管理。审计日志、OpenTelemetry 导出、MCP 允许列表和 SCIM 同样仅限 Enterprise。自助式 Teams 看不到这些设置。完整清单见[管理员控制](https://cursor.com/docs/grok-bot/teams#admin-controls)。

## 架构

Grok Bot 的桌面和移动应用将每个请求发送到 Cursor 的服务器。从那里开始，工作在该成员的托管计算机上运行，提示词发往模型提供商，工具调用通过连接的应用到达第三方服务。

客户侧

Grok Bot

桌面与移动端

团队策略

Cursor 云

托管计算机

每位成员一个 microVM，位于美国

Cursor 服务器

Cursor 选择模型

工具调用，不传令牌

连接的应用

网络策略

零数据保留（Zero Data Retention）

自动审查（Auto Review）

第三方

Web 应用与 SaaS

Bot 以已登录成员的身份行事

网络策略

模型提供商

零数据保留

MCP 服务器

Slack、Google、GitHub 等

自动审查

每条路径上都有一项控制。每一项都链接到本页中对应的章节。

1团队策略

Cursor 云

托管计算机

每位成员一个 microVM，位于美国

2网络策略

Cursor 服务器

Cursor 选择模型

1团队策略3零数据保留

4工具调用，不传令牌

连接的应用

5自动审查

2网络策略

3零数据保留

5自动审查


1. 1

   [团队策略](https://cursor.com/docs/grok-bot/teams#admin-controls)

   团队规则适用。网络和自动审查控制项在 Grok Bot 页面上设置。
2. 2

   [网络策略](#network-policy)

   管理员控制托管计算机可以访问哪些域名。
3. 3

   [零数据保留](#models-and-data)

   开启隐私模式后，模型提供商不会保留你的数据。
4. 4

   [令牌保留在连接的应用中](#identity-and-sign-ins)

   OAuth 令牌存储在服务器端；模型只能看到工具结果。
5. 5

   [审批与自动审查](#approvals-and-auto-review)

   自动审查可以在执行可能有风险的操作之前请求用户批准。成员可以添加「先询问」规则，Enterprise 管理员可以强制实施审查。

## 网络策略

**网络控制仅限 Enterprise。** 管理员在 Cursor 仪表板的 [Grok Bot 页面](https://cursor.com/dashboard/bot)上，在**网络（Network）**下的 **Grok Bot 网络访问（Grok Bot Network Access）**中设置 Grok Bot 网络策略。它控制团队计算机可以访问哪些目标。自助式 Teams 看不到此面板，也无法设置目标允许列表。没有策略的团队默认允许全部。

| 模式 | 效果 |
| --- | --- |
| **允许所有网络访问（Allow All Network Access）** | 所有目标。没有策略的团队会得到此模式。 |
| **默认值 + 团队允许列表（Defaults + Team Allowlist）** | Cursor 的默认目标加上你的列表 |
| **仅团队允许列表（Team Allowlist Only）** | 仅你的列表，加上计算机运行所需的目标 |

- **目标（Destinations）**涵盖 Web 域名，以及用于原始连接的带端口的 IP 范围，条目数量不设上限。
- **目录用户组（Directory groups）。仅在 Enterprise 的「网络控制」内可用。** 用户组可以设置自己的网络策略，对其成员取代团队策略；锁定后，团队策略会对所有人生效。
- **该策略与 Cloud Agent 网络设置相互独立。** 运行中的计算机会在约一分钟内自动应用更改。休眠的计算机会在下次唤醒时应用更改。你无需重建计算机。
- **限制出口会限制数据可以发送到何处。** 若要按照你自己的数据丢失防护策略检查哪些内容会到达模型，请使用[推理钩子](#inference-hooks)。

阻止一个应用并不会阻止该服务的网站。连接器策略和网络策略是分开的层，要关闭两条路径需要同时使用两项控制。

### MCP 服务器与网络策略

网络策略管辖团队计算机将流量发送到何处。连接的应用（MCP 服务器）有所不同：Bot 从 Cursor 的服务器访问远程 MCP 服务器，因此允许列表模式本身并不覆盖它们。若要让它们也受同一列表约束，请开启 **Apply to MCP servers**。该开关位于 **Grok Bot 网络访问**中的 **允许的目标（Allowed destinations）**（旧设置页面上为 Allowed Destinations）下方、**为所有用户组锁定（Lock for all groups）**（Lock for All Groups）上方，并且仅在选择了**默认值，加上允许列表（Default, plus the allowlist）**（Defaults + Team Allowlist）或**仅允许列表（Allowlist only）**（Team Allowlist Only）时才会出现。

- **关闭，这是每个团队的默认值。** 无论网络策略怎么说，Bot 都可以连接到你的连接器策略允许的任何 MCP 服务器。
- **开启。** 远程 MCP 服务器还必须匹配**允许的目标**中的某个条目。不匹配的服务器在 Bot 尝试使用时会被拒绝，成员会看到需要请管理员添加哪个目标。在计算机上运行的命令服务器不受影响；网络策略已经适用于它们。

在你依赖它之前请先开启该开关：允许列表模式本身并不会限制 MCP 服务器。该开关是团队设置。目录用户组会继承它，且无法将其关闭；锁定的团队策略也包含它。保存它不会重启计算机；它会应用于下一次 MCP 连接。它与团队设置中 **MCP 配置（MCP Configuration）**下的设置相互独立，后者管辖编辑器中的 Cursor；更改其中一个不会更改另一个。

**内置连接器也会被检查。** 该开关覆盖 Bot 使用的每个连接的应用，包括 Cursor 在**连接应用（Connect apps）**下为你运营的应用，例如 GitHub、X、Origin、Google Workspace 和 Microsoft 365。连接的应用按其发送请求的主机进行检查，而不是按连接器列表中的名称检查，因此在开启开关之前，请将这些主机添加到**允许的目标**中。如果某个连接器的主机未全部被允许，Bot 下次使用它时会被拒绝，并显示消息 `MCP server "<host>" refused: it is not on your team's Grok Bot network allowlist (Grok Bot settings > Network > Allowed destinations). A team admin can add it.`

| 连接的应用 | 需要允许的主机 |
| --- | --- |
| GitHub | `api.github.com` |
| X | `api.x.com` |
| Origin | `api.origin.cursor.com` |
| Gmail | `gmail.googleapis.com`；如果连接器是通过 Google 的托管地址添加的，还需 `gmailmcp.googleapis.com` |
| Google Calendar | `www.googleapis.com`；如果通过 Google 的托管地址添加，还需 `calendarmcp.googleapis.com` |
| Google Drive | `www.googleapis.com`、`sheets.googleapis.com`；如果通过 Google 的托管地址添加，还需 `drivemcp.googleapis.com` |
| Google Docs | `docs.googleapis.com` |
| Google Sheets | `sheets.googleapis.com` |
| Google Slides | `slides.googleapis.com`、`slidesmcp.googleapis.com` |
| Google Ads | `googleads.googleapis.com` |
| Outlook、Outlook Calendar、OneDrive、Microsoft Teams | `graph.microsoft.com` |
| Stripe Link | `api.link.com` |
| Tailscale | `api.tailscale.com`、`login.tailscale.com` |
| QuickBooks Online | `ah-api.merge.dev`、`quickbooks.api.intuit.com`（沙箱公司使用 `sandbox-quickbooks.api.intuit.com`）、`oauth.platform.intuit.com`、`developer.api.intuit.com` |
| Workday | `ah-api.merge.dev`，加上你在连接器设置中输入的 Workday 租户的登录和 REST API 主机 |
| WhatsApp Business | `ah-api.merge.dev`、`graph.facebook.com` |
| Zoho CRM、Zoho Books | `ah-api.merge.dev`，加上你的 Zoho 数据中心的账号主机和 API 主机，例如美国的 `accounts.zoho.com` 和 `www.zohoapis.com`（`.eu`、`.in`、`.com.au`、`.jp`、`.sa`、`.uk`、`.ae`、`.sg`，或加拿大的 `accounts.zohocloud.ca` 和 `www.zohoapis.ca`） |
| Zoho Desk | `ah-api.merge.dev`，加上你的数据中心的账号主机及其 Desk 主机，例如 `accounts.zoho.com` 和 `desk.zoho.com` |
| Microsoft Power BI | `api.powerbi.com` |
| Databricks Genie | 你的 Databricks 工作区主机，由团队管理员在插件设置中输入，例如 `dbc-a1b2c3d4-e5f6.cloud.databricks.com` |
| Google BigQuery | `bigquery.googleapis.com` |
| Asana | `mcp.asana.com` |
| Vanta | 登录时选择区域对应的主机：`mcp.vanta.com`（美国）、`mcp.eu.vanta.com`（欧洲）或 `mcp.aus.vanta.com`（澳大利亚） |
| Shop Pay | `mcp.shop.com` |

团队市场中的其他连接器按其服务器地址中的主机进行检查，该地址显示在仪表板的 [Plugins & MCPs 页面](https://cursor.com/dashboard/plugins)上；请允许该主机。

## 静态出口 IP

默认情况下，托管计算机通过共享的静态出口 IP 地址访问互联网。这些范围由 Grok Bot 客户共享，不提供按客户专用的 IP，因此请将这些范围视为标识 Grok Bot 流量，而不是仅标识你的团队。当前范围可向你的客户团队获取；产品层面的控制手段是目标允许列表，而不是源 IP 编辑器。

如果成员设备位于 Zscaler 或其他 TLS 检查网关之后，请在所有配置文件（包括离线网络）中放行 Cursor 的域名并将其排除在检查之外。请参阅[配置 TLS 检查代理](https://cursor.com/docs/grok-bot/proxies)。

成员可以通过其桌面路由流量，以使用桌面的 IP 地址；解析到私有或 VPN 地址的站点在该路由上仍会被阻止，除非它们已为你的组织被允许。**团队安装脚本仅限 Enterprise。** 这些团队还可以在每台团队计算机上安装自己的网络客户端。这两条路径都与共享出口范围分开。请参阅[连接到私有网络](https://cursor.com/docs/grok-bot/private-networks)。

## 审批与自动审查

审批让重要操作保持在成员的控制之下。最强的边界来自请求本身所设定的范围，因此请让成员说明 Bot 可以更改什么以及必须在哪里停止：

> 核对活动数据，并起草一份建议的预算变更。不要更改活动，也不要给代理机构发消息。在显示当前值、建议值和预期影响后请求批准。

当某个操作需要批准时，对话会显示提议的操作及其输入。**允许一次（Allow once）**让 Bot 继续执行该操作，**始终允许（Always allow）**可以保存一条匹配规则，**拒绝（Deny）**会停止该操作；在成员发送另一条消息之前，Bot 不会再次尝试。iPhone 上的控制项相同。审批控制的是提议的操作，而不是已经完成的工作；任何人都不应批准自己无法识别目标或效果的操作。

Auto Review 是这些提示背后的审查层：一个独立的审查模型，在 Bot 的有风险操作运行之前进行评估，涵盖 shell 命令、应用调用、计算机使用、自动化写入（对例程和事件触发器的更改），以及 Cloud Agent 和子智能体启动等委派。它可以允许操作继续、要求批准或拒绝操作。

- **团队管理员可以强制实施 Auto-review。仅限 Enterprise。** 该开关位于 Cursor 仪表板的 Grok Bot 页面。开启后，成员无法关闭 Auto-review，除非其所属的某个用户组用**不对此用户组强制（Don't enforce for this group）**解除锁定；请参阅[用户组设置](https://cursor.com/docs/grok-bot/teams#group-settings)。
- **管理员可以添加团队自动审查规则。仅限 Enterprise。** 这些也位于 Grok Bot 页面。它们适用于每位成员的 Bot，在成员设置表中显示为锁定行，并在管理员添加、编辑或删除规则时自动保存。如果管理员关闭强制实施，团队规则将停止适用，成员只能回到自己的规则。
- **成员可以在「设置（Settings）」>「通用（General）」>「自动审查（Auto-review）」的「自定义规则（Custom Rules）」下添加个人规则。** **先询问（Ask first）**规则总会阻止匹配的操作，**自动允许（Allow automatically）**规则仅在审查者没有发现其他阻止理由时，才让匹配的操作继续。成员可以在团队规则之上添加个人规则，但只会使行为更严格；规则冲突时「先询问」优先。保持规则狭窄并绑定到已知操作，例如「在发送任何外部电子邮件前先询问」或「在 `/workspace/reports` 中运行 `git status` 时自动允许」。避免「允许浏览器中的一切」这类宽泛规则。个人规则保存到成员的账号，因此会从每台桌面设备和移动应用生效。
- **它不会审查每一个副作用。** 记忆写入和大多数设置更改就是例子。应将它视为显式边界和最小权限的补充，与不依赖模型判断的控制项协同工作：逐操作审批、网络策略和按用户隔离。

## 推理钩子

推理钩子将每个 Grok Bot 模型请求签名后发送到你的组织运行或通过安全供应商使用的 AI 安全服务器。你的服务器在模型运行之前允许或拒绝该请求，因此你自己的策略会检查提示词以及 Grok Bot 收集的内容，例如网页和应用结果。新配置从影子模式（Shadow mode）开始，会在审计日志中记录拒绝，但不阻止任何操作。

推理钩子检查模型输入。开启 **Validate Tool Calls** 后，它们还会在工具调用运行之前进行检查，但不检查操作开始后做了什么。请保留网络策略和 Auto Review，以控制 Bot 的行为。设置、模式、请求格式和审计事件见 [Grok Bot 推理钩子](https://cursor.com/docs/grok-bot/inference-hooks)。

推理钩子处于 beta 阶段，所有 Enterprise 团队均可使用。

## 身份与登录

成员使用其 Cursor 账号登录 Grok Bot，因此你现有的 Cursor SSO 配置会适用。SAML 2.0 单点登录可与 Okta、Microsoft Entra、Google Workspace 和 OneLogin 配合使用，并且可以要求所有成员使用 SSO（这会阻止密码登录）。**SCIM 仅限 Enterprise：** SCIM 2.0 配置与取消配置。有关 Okta 和 Entra ID 的分步配置，包括应用分配和计算机浏览器的登录规则，请参阅[配置身份与访问](https://cursor.com/docs/grok-bot/identity)。

在托管计算机内，成员通过浏览器中的你自己的身份提供商登录应用，类似于配置一台新笔记本电脑。你的会话策略管辖这些会话，在身份提供商中撤销该用户会结束这些会话。

Bot 没有自己的身份或凭证：

- **Bot 以已登录成员的身份行事。** Bot 永远不能拥有比其所属人员更多的访问权限，每个操作始终可归因于具名成员，并且除了你的身份提供商之外没有单独的机器身份需要配置、轮换或审计。团队管理的连接器是唯一的例外：它们可以使用团队或服务账号凭证。
- **连接器令牌保留在 Cursor 后端。** Bot 调用工具时不会收到 OAuth 令牌，令牌也绝不会存储在计算机上。
- **凭证不进入模型。** 登录时，Bot 使用成员保存在 Vault 中的登录信息、已连接的密码管理器，或成员在安全表单（Secure Form）中输入的值。这些值通过引用填入页面：模型永远不会收到已保存的密码、卡号或安全码，也不会收到成员在安全表单中输入的内容。Bot 可以看到保存了哪些登录信息以及成员保存的联系信息。对于单点登录、通行密钥和其他表单无法处理的步骤，Bot 会将计算机交给成员。对于 API 密钥或其他秘密，安全秘密卡（secure secret card）会遮蔽该值，使其不进入对话记录，也不让模型看到。保存在 Vault 中的卡会在结账时填入，无需每次都单独批准，因此希望逐笔批准付款的成员不应保存该卡。Vault 在共享 Bot 上不可用。密码和一次性验证码绝不应放在普通聊天中。请参阅[安全存储秘密](https://cursor.com/help/grok-bot/secrets)。

若要结束成员当前的工作，组织管理员从仪表板终止该成员的计算机；请参阅[管理 Grok Bot 计算机](https://cursor.com/docs/grok-bot/computers)。该控制仅限 Enterprise。它会停止运行中的 Bot，保留持久磁盘，成员的下一个会话会启动一台新计算机。它不会移除访问权限。要移除访问权限，请将成员从团队中移除，或为其用户组关闭 Grok Bot，并在你的身份提供商中撤销其会话。应用会话只保留在成员的计算机上。

当某个项目或登录信息不应再可用时，成员应直接清理：暂停或删除相关例程，在计算机上退出网站登录，移除连接的应用并在源服务中撤销其授权，并从 `/workspace` 中移除敏感文件。删除 Bot 不会移除计算机文件或浏览器会话。

## 日志与审计

审计日志和操作记录使用不同的管道。审计日志涵盖管理和安全事件，包括 Grok Bot 控制平面操作。操作记录捕获 Bot 操作，OpenTelemetry 导出在配置后将那些事件发送到你的收集器，并标记为 `cursor.surface=grok_bot`。

- **审计日志。仅限 Enterprise。** 它们涵盖管理员、安全和身份验证事件，以及 Grok Bot 控制平面事件：Bot 创建、成员访问权限更改、团队安装清单、MCP 身份验证、Slack 账号关联和例程。在仪表板中按应用程序筛选它们，或将其流式传输到你的 SIEM。自助式 Teams 不会获得此日志。
- **操作记录。仅限 Enterprise。** 它是 Grok Bot 页面上的一个设置，默认关闭。当团队启用它时，Cursor 会在内部存储中记录 Bot 操作（包括已擦除秘密的 shell 命令），保留 90 天。操作记录事件不会出现在审计日志页面上。要在你自己的收集器中接收经过清理的事件，请配置 [OpenTelemetry 导出](https://cursor.com/docs/enterprise/opentelemetry-export)，它也仅限 Enterprise。隐私模式（旧版）会强制关闭记录。

## 端点工具

Grok Bot 不提供面向客户的内置遥测或 EDR 数据流。这些计算机是 Cursor 运营的基础设施，Cursor 会对其进行运营健康和滥用监控，而该遥测有意排除客户数据。**团队安装脚本仅限 Enterprise。** 这些管理员可以在每台团队计算机上安装自己的工具。

## 数据保留与删除

每位成员的计算机都会在持久磁盘上跨会话保留本地文件、浏览器会话以及浏览器中保存的任何内容。连接器令牌绝不会存储在计算机上。

- **空闲计算机会自动休眠。** 休眠不是删除。
- **镜像更新会保留文件。** 位于过时系统镜像上的计算机会在保留成员文件的情况下，用新镜像重建。
- **成员重置会保留已保存的数据。** 成员可以从桌面应用重置自己的计算机。与「恢复（Recover）」一样，「重置（Reset）」会从最后保存的数据重建计算机；如果无法连接计算机以保存数据，最近的更改可能会丢失。请参阅 [Grok Bot 计算机](https://cursor.com/help/grok-bot/computer-recovery)。
- **删除遵循 DPA。** 根据[数据处理协议（Data Processing Agreement）](https://cursor.com/terms/dpa)，服务结束后，数据会在收到书面指示后的 30 天内删除或返还。
- **备份每天运行。** Cursor 的生产控制平面由每日加密备份覆盖，并复制到单独的恢复设施。
- **Enterprise 管理员可以设置保留期。** 不活动的 Bot、不活动的计算机和旧消息可以被自动删除。请参阅[数据保留](https://cursor.com/docs/grok-bot/teams#data-retention)。

不提供客户管理的单台计算机时间点还原。

## 数据驻留

Grok Bot 计算机在美国运行。Grok Bot 也受 Cursor 仅限美国的数据驻留计划覆盖。启用后，Grok Bot 的推理、数据处理和存储都会留在美国。请联系你的客户团队以注册。关于支持的模型、排除项和定价，请参阅[美国数据驻留](https://cursor.com/docs/enterprise/privacy-and-data-governance#us-data-residency)。

## 模型与数据

Grok Bot 管理模型选择。没有面向客户的模型选择器，服务组合可能随时间变化，不保证固定的供应商集合。每个请求都会发往 xAI 的第一方模型，或发往[子处理者列表](https://trust.cursor.com/subprocessors)中某个提供商的第三方模型。用量和支出视图会将此活动记录为 Grok Bot 用量，而不是按模型记录。请参阅[哪些 AI 模型为 Grok Bot 提供支持？](https://cursor.com/help/grok-bot/models)。

- **团队模型允许列表不约束 Grok Bot。** 无论你的[模型访问控制](https://cursor.com/docs/enterprise/model-and-integration-management#model-access-control)设置如何，Grok Bot 都会使用 xAI 第一方模型，并可能使用第三方模型。设置模型允许列表的团队在启用 Grok Bot 时会看到此确认。如果你的合同限制子处理者，请联系你的客户团队。
- **隐私模式适用。** 当成员在你的团队中时，团队的隐私模式管辖该成员；启用隐私模式后，客户数据不会被用于训练。
- **零数据保留遵循 Cursor 现有的提供商协议。** 模型提供商不会保留提示词或输出，Grok Bot 也没有添加单独的控制项。提供商可能会运行滥用和安全分类器，被标记的数据可能会被存储以供调查。

## 本地执行

Bot 可以通过桌面应用在成员自己的机器上操作：运行命令、读取文件，以及在云计算机和本地机器之间移动文件。这与托管计算机中的工作分开，有自己的控制项，也不同于管辖托管计算机内部工作的 Auto Review。

逐命令审批是默认值，审批卡会显示确切的命令。成员在 **设置（Settings）** > **计算机（Computer）** > **你的计算机（Your computer）**下的**在此计算机上执行（Execution on this computer）**（在桌面应用列出之前为 **Execution on Local Computer**）中选择策略：**每次都询问（Ask every time）**、**始终允许（Always allow）**或**从不允许（Never allow）**。除非 Bot 有具体理由处理本地文件，否则建议选择**从不允许**。管理员可以通过 Grok Bot 页面上的[在本地计算机上执行](https://cursor.com/docs/grok-bot/teams#execution-on-local-computer)为整个团队限制该策略；当成员自己的设置更严格时，仍以成员自己的设置为准。

## 托管

Grok Bot 仅在 Cursor 托管的云计算机上运行。目前不支持本地部署、在你自己的边界内部署以及自带镜像部署。托管计算机默认使用共享静态出口。成员可以通过其桌面路由流量，Enterprise 团队可以用**团队安装脚本**安装网络客户端。请参阅[连接到私有网络](https://cursor.com/docs/grok-bot/private-networks)。

## 提示注入

Bot 从外部世界读取的内容（例如网页、应用结果和命令输出）可能会试图操纵它。Grok Bot 分层防御：启用强制实施时，Auto Review 会根据成员的请求检查 Bot 操作；其下还有不依赖任何模型判断的控制项，包括网络策略、逐操作审批和按用户隔离。外部内容在呈现给模型时会被标记为不可信数据。使用[推理钩子](#inference-hooks)时，你自己的安全服务器还可以在下一次模型调用之前筛查这些内容。这些控制会降低但不能消除恶意内容带来的风险，这也是应将重要操作保持在审批之后的另一个原因。

## 认证

Cursor 背后的公司 Anysphere 持有由 Schellman 颁发的 ISO/IEC 27001 和 ISO/IEC 42001 认证，Grok Bot 包含在当前 ISO 范围内。ISO/IEC 27001 认证信息安全管理体系，即整个组织的安全计划。ISO/IEC 42001 认证 AI 管理体系，即 Cursor 如何治理其构建和运营的 AI。证书和报告可在 [trust.cursor.com](https://trust.cursor.com) 获取。
