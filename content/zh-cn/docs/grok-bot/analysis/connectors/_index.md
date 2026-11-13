---
title: "Grok Bot：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 用「应用」（OAuth 连接器）、与 Cursor 通用的 MCP 服务器、插件和技能接入第三方服务，没有应用时退回到云端电脑上的浏览器；令牌留在 Cursor 的连接器后端，Bot 拿不到。连接器面向工作场景，覆盖办公、开发、数据和 CRM，企业管理沿用 Cursor 的团队市场策略。
---

## 概要

- 三条接入路径并存：应用（结构化工具调用，官方称比在网页上点击更可靠）、自行添加的 MCP 服务器（URL 或命令启动）、云端电脑上的浏览器（用于没有应用或 API 的网站）。截至 2026-11 的资料，MCP、插件、技能与 Cursor 通用。
- 连接器偏重工作。安全文档列出的内置连接器包括 Google 与 Microsoft 365 全家、Slack、GitHub、Salesforce、Databricks、BigQuery、Power BI、Workday、QuickBooks、Zoho、Vanta 等；官方案例集中在采购、客服、销售、工程、数据团队。
- 凭证分层：OAuth 令牌存于 Cursor 的连接器后端，Bot 只看到工具结果；网站登录按 Vault、密码管理器（1Password）、安全表单的顺序取用，1Password 新集成每次登录需用户批准，Bot 看不到密码。
- 连接器是账号级的，同一账号下所有 Bot 共用；能力不超出所连账号本身的权限。Teams/Enterprise 管理员沿用 Cursor 团队市场的允许与阻止策略，但不能向成员推送连接器；阻止某应用不会阻止对应网站，堵住网页路径需要 Enterprise 的网络控制。
- 外部阻力主要在购物和社交网站：据报道亚马逊阻止 Grok Bot 下单；Grok Bot 用 Web Bot Auth 签名向网站表明身份，并接入了 Shop Pay、Link、X Money 等智能体付款通道。

## 应用、MCP 与浏览器三条路径

官方文档把「应用（App）」定义为 Bot 与 Gmail、Notion、Slack 等服务协作的结构化方式，「在存在应用时，它比在网站上点击更可靠」；没有应用的服务、或应用不提供的可视化流程，交给浏览器（[文档：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})）。据 Cybernews 引用的 x.ai 发布文章，Bot 被设计为「登录并跨应用、工具和网站工作，包括没有现成 API 或 MCP 的平台」（[Cybernews]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})）。Top5Apps 转述发布帖的概括是：通过 Marketplace 连接器登录用户的工具，「对其他一切使用电脑控制」（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

MCP 一侧与 Cursor 打通。官方指南写明「Grok Bot 支持与 Cursor 相同的 MCP 服务器、插件和技能」（[官方指南：Grok Bot 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})），程序员鱼皮的实测也说两者「是通用的」，内置应用按通信、设计、开发、数据分类，含 Figma、Canva、Vercel、Cloudflare、Supabase、Sentry 等（[鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。Bot 可以自己在目录中搜索并安装应用，也可以通过 URL 或在其电脑上运行的命令添加目录之外的 MCP 服务器，命令启动的服务器对用户的其他 Bot 也可用（[文档：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})）。

更新日志记录了这条路径的逐步完善（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）：

| 版本 / 日期 | 变化 |
| --- | --- |
| v0.53.0（2026-09-15） | Mac 上可从 Marketplace 连接 1Password |
| v0.67.0（2026-10-02） | Marketplace 更名为 Connect Apps，加分类标签与推荐 |
| v0.70.2（2026-10-11） | 不连 X 账户即可搜索 X、读帖子与资料；Figma、Notion、Canva 等可在聊天中显示为交互式卡片；可用 X Money 或 Stripe Link 付款 |
| 之后各版 | 可用技能上限由 24 个提高到 200 个；使用私有证书颁发机构的自定义 MCP 服务器在用户批准后可用；私有 Tailscale 网络上的 MCP 服务器先建议用 Tailscale Funnel 暴露，后改为提示从 Tailscale 插件连接 tailnet；连接器登录可在开始后最长一小时内完成 |

Bot 还可以把编码工作交给 Cursor 的 Cloud Agent，完成后把报告中的截图、视频、文件拷回 Bot 的电脑并附在回复里，手机端卡片可「View PR」或「Open in Cursor」（[文档：文件与结果]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-files-and-results" >}})）。官方称一个工程 Team Bot 引导的 Cursor Project 编排了数百个 Cloud Agents，帮一个五人团队「每天发布超过 100 个 PR」（[Team Bots 发布]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})）。

推断：与其他跟踪产品相比，Grok Bot 的连接器能力很大程度上是 Cursor 已有基础设施的复用（连接器后端、MCP 与插件体系、团队市场策略、Cloud Agent），这解释了它为何从发布起就偏向开发与企业工具。

## 连接器清单偏向工作场景

安全文档按出站主机列出了 Cursor 在「连接应用」下运营的内置连接器：GitHub、X、Gmail、Google Calendar/Drive/Docs/Sheets/Slides/Ads、Outlook 与 Outlook Calendar、OneDrive、Microsoft Teams、Stripe Link、Tailscale、QuickBooks Online、Workday、WhatsApp Business、Zoho CRM/Books/Desk、Power BI、Databricks Genie、BigQuery、Asana、Vanta、Shop Pay 等，其中 QuickBooks、Workday、WhatsApp Business、Zoho 等经 `ah-api.merge.dev` 中转（[文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。帮助中心另提到 Notion、Slack、1Password、Zoom、SharePoint、Adapter、Robinhood、Intercom、Postiz（[帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})）。

官方案例几乎都是团队工作流：

| 场景 | 连接的服务 | 资料 |
| --- | --- | --- |
| 采购 | Slack、Notion、Drive、Gmail、Hex、Ramp，整理出约 125 个在用供应商的工作图 | [采购 Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-04-grok-bot-procurement" >}}) |
| 客服 | Plain（工单）、Linear、Datadog，退款接支付服务商 | [客服 Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-22-grok-bot-customer-support" >}}) |
| 工程、数据 | Notion、Linear、Hex、Datadog、Cursor；Data Bot 用共享只读凭证查询 Databricks | [Team Bots 发布]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})、[Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}}) |
| 销售 | Salesforce、Gong、Ironclad、CPQ 工具 | [销售 Bot]({{< relref "/docs/grok-bot/sources/official/2026-10-27-grok-bot-sales" >}}) |

个人用户的实测给出相似的图景。产品负责人 James Pember 称 Gmail、日历、Drive、Slack、GitHub 五个原生连接器覆盖了他约 80% 的工作场景（[James Pember]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})）。Pat Simmons 的咖啡公司模拟实验中，各智能体通过作者自建的 MCP 服务器连接订单后台，并使用 Notion、HubSpot、Asana、GitHub（[Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。Claire Vo 一周测试后的评价（经 Top5Apps 转引）是「连接器是顶级的」（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

X 是自家平台，单独处理。2026-08-29 官方推出 X 连接器：没有开发者账号的会代为创建，付费用户可获得免费的 X API 额度，可搜索帖子、读时间线、看提及（[Grok Bot 与 X]({{< relref "/docs/grok-bot/sources/official/2026-08-29-grok-bot-and-x" >}})）。截至 10 月底的文档，不连接 X 账户也能只读搜索公开内容；私信、书签、主页时间线需添加 X 插件登录，而 X 插件需要用户 X 开发者账户里有 API 额度（[文档：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})）。

## 各连接器的能力边界

帮助中心写明，应用只能做所连账户在该服务里本来就能做的事，「它不能提升你的访问权限，也不能更改共享设置」，并逐个列出限制（[帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})）：

- Google Calendar 可读、建、改事件，查空闲，回复邀请，但不能改 Meet 设置或加 Zoom 链接。
- Sheets 可编辑有编辑权限的表格，查看者权限的文件只读。
- Slack 以所连 Slack 用户的身份发帖，只能发到该用户能发帖的频道。
- Gmail 同一时间只能连一个邮箱，「你不能让个人邮箱和工作邮箱同时连接到 Gmail」。
- Power BI 全部只读；Databricks Genie 需管理员先配置 OAuth；Vanta 登录时选美国、欧洲或澳大利亚区域。

Gmail 的说法前后不一。Claire Vo 2026-08-18 的上手评测称可以连接「全部四个 Gmail 账户和全部七个 Slack」，并说仅这一点就让产品对她形成产品市场契合（[Claire Vo]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})）；2026-09-11 的官方指南也说「每个服务可以连接多个账号」（[官方指南：Grok Bot 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})）。而 2026-11-05 的帮助中心明确 Gmail 一次一个邮箱。资料没有说明是功能调整还是仅针对 Gmail 应用的限制。

文件可在 Bot 的电脑与 Google Drive、OneDrive、SharePoint、Gmail、Outlook 之间搬运；Google 文档类文件到达时转为 docx、xlsx、pptx 或 png，保存到 Google Drive 总是新建文件，OneDrive、SharePoint 遇同名文件会拒绝，除非要求覆盖（[文档：文件与结果]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-files-and-results" >}})）。

## 授权、凭证与失效处理

**令牌不进电脑。** 应用登录信息不会落在 Bot 的电脑上，OAuth 令牌保存在 Cursor 的连接器后端，Bot 调用工具时不会收到它们（[文档：工作方式]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})、[文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。连接是账号级的，对该账号下所有 Bot 可用；某个 Bot 不该用某邮箱时只能断开 Gmail（[帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})）。推理钩子文档则提醒，模型放进 `AddMcpServer` 调用里的凭据不会被脱敏（[文档：推理钩子]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})）。

**网站登录的顺序。** 先用 Vault，再用已连接的密码管理器，最后用聊天里的安全表单询问用户；单点登录、通行密钥、验证码等交给用户接管（[文档：工作方式]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})）。Vault 可从 1Password、Chrome、Safari、Firefox、Bitwarden、LastPass 等的 CSV 导出导入，文件「在你的电脑上读取，从不上传」且须小于 5 MB（[文档：Vault]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-vault" >}})）。1Password 新集成逐步推出，需 1Password 8.12.42 以上，只适用个人和 Family 账户：每次登录在 1Password 中批准后填入 Bot 的浏览器，Bot 看不到值；只提供个人保险库的登录，不填支付卡；不再使用服务账户，旧用户需重连（[帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})、[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

**企业账户的门槛。** Grok Bot 以「Grok」而不是 Cursor 的身份登录 Google，公司 Google Workspace 管理员需在 API 控制中把 Grok 设为受信任，换浏览器无法绕过；Microsoft 365 的 Outlook、日历、OneDrive、Teams 同样需管理员批准（[文档：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})、[帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})）。

**状态与失效。** 「已添加」只表示应用已安装，不代表已登录，状态还有「需要验证」「已断开」，可重新连接（[帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})）。更新日志记录了一系列失效处理：连接器需要无法请求的权限时，Bot 会说明重新连接也无济于事；Google 限流时保持连接、建议稍后重试（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。帮助中心列出两个未解决的已知问题：Zoom 授权报错 4700，「目前没有变通方法」；SharePoint 应用级权限报 AADSTS50011，只能改用委托权限（[帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})）。

用户侧的感受与此相符。投资人用户 Puranik 提到 Gmail 登录状态「大约两三天就过期」，要重新登录和二次验证（[特工宇宙]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。从上下文看，这指 Bot 浏览器里的网页登录，而不是 OAuth 应用；资料没有区分。

## 团队管理沿用 Cursor 的策略

Teams 与 Enterprise 的连接器策略继承自 Cursor 的团队市场，被阻止的连接器显示为「Disabled by team admin」；目前「无法向成员推送连接器，无论强制还是默认开启」（[文档：Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})、[文档：安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})）。插件在 Team Bot 上可由每个成员各自连接，也可为整个团队配置（[Team Bots 发布]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})）。

连接器策略与网络策略是两层：阻止一个应用不会阻止该服务的网站，关闭网页路径需要仅限 Enterprise 的 Network Controls（[文档：安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})）。在允许列表模式下，另有「Apply to MCP servers」开关（默认关闭），开启后远程 MCP 服务器和内置连接器的出站主机也须在允许列表内（[文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。

推断：由于 Bot 有一台带浏览器的云端电脑，单靠连接器策略管不住数据流向；企业要真正收口，需要 Enterprise 档的网络控制。这也意味着连接器策略在 Teams 档更多起「推荐用法」的作用。

## 模板与市场

官方 Bot 市场中的模板（如 Haggle Bot）可复制导入，但原有插件要重新安装，MCP 服务器、脚本等非标准插件不随模板带走，模板也不含秘密（[官方指南：模板]({{< relref "/docs/grok-bot/sources/official/2026-09-08-guide-templates" >}})）。Puranik 称市场里「几百个 bot，且大多免费」（[特工宇宙]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。资料没有提到面向第三方开发者的上架、审核或分成机制。

## 网站拦截与智能体身份

据 Not a Tesla App 转述一位 X 用户的帖子，亚马逊在阻止 Grok Bot 下单；Musk 此前对屏蔽的回应是让用户的 Bot 去别的商店买，这次回复「Maybe we should start a competitor to Amazon」，文章强调这不是正式宣布（[Not a Tesla App]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})）。36 氪转述 The Verge 称，xAI 的 Grok 与 Muse、Instinct、Dots 一样无法访问亚马逊（[36 氪]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})）。Puranik 也提到 LinkedIn 明文禁止 bot，Zillow、亚马逊会直接把 Agent 挡回（[特工宇宙]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。

在身份上，社区作者 nightd 发现 Grok Bot 的浏览器请求带 Web Bot Auth 签名（`Signature`、`Signature-Input`、`Signature-Agent` 请求头），签名由 Cursor 的 API 提供、通过 CDP 注入 Chrome，`Signature-Agent` 为 `cursorusercontent.com`；作者还引 Cloudflare 博客称，自 2026-09-15 起 Cloudflare 默认允许 AI 爬虫（[nightd]({{< relref "/docs/grok-bot/sources/community/2026-10-07-nightd-impersonating-grok-bot" >}})）。

支付侧，更新日志写明 Bot 可用 X Money、Stripe Link 付款，Link 一次性卡仅在美国和加拿大提供，后续加入 Shop Pay（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。据 All Things Muse 转述 The Defiant，Shopify 的 Shop Pay 智能体结账首批支持 Muse、Claude Duet、Grok Bot、Instinct（[All Things Muse]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}})）。WIRED 记者的午餐测试中，Grok Bot 通过 DoorDash 下单（[WIRED]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

## 资料缺口

- 连接器总数与完整目录；第三方开发者能否上架应用或 Bot 模板，审核与分成规则。
- Gmail 多账户的变化：早期评测和 09-11 官方指南说可连多个，11-05 帮助中心说一次一个，缺官方变更说明。
- 亚马逊拦截的官方回应，以及 xAI 与零售、社交平台（LinkedIn、Zillow 等）是否有合作或授权。
- 连接器调用的失败率、限流、配额（X API 免费额度的具体数量）。
- Web Bot Auth 签名的官方说明；nightd 的发现只是单一社区来源。

## 主要资料

**官方**
- [文档：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})：应用与浏览器的分工、自加 MCP、Google 身份、1Password。
- [帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})：各连接器能力边界、管理员批准、已知问题。
- [文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})、[文档：安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})、[文档：Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})：连接器清单、令牌存放、团队策略与网络策略。
- [文档：工作方式]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})、[文档：Vault]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-vault" >}})、[文档：文件与结果]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-files-and-results" >}})、[文档：推理钩子]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})：登录顺序、文件搬运、Cloud Agent。
- [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：连接器相关功能的版本变化。
- [Grok Bot 与 X]({{< relref "/docs/grok-bot/sources/official/2026-08-29-grok-bot-and-x" >}})、[官方指南：Grok Bot 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})、[官方指南：模板]({{< relref "/docs/grok-bot/sources/official/2026-09-08-guide-templates" >}})：X 连接器、多账户、模板。
- [采购 Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-04-grok-bot-procurement" >}})、[客服 Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-22-grok-bot-customer-support" >}})、[Team Bots 发布]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})、[销售 Bot]({{< relref "/docs/grok-bot/sources/official/2026-10-27-grok-bot-sales" >}})、[Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}})：各团队场景的连接组合。

**媒体**
- [Cybernews]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})：引用发布文章对无 API 平台的说法。
- [Not a Tesla App]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})、[36 氪]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})：亚马逊拦截。
- [All Things Muse]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}})、[WIRED]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})：Shop Pay 首批支持、DoorDash 下单。

**社区**
- [Claire Vo]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})、[James Pember]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})、[鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})：多账户、原生连接器覆盖面、与 Cursor 通用。
- [Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})、[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})、[特工宇宙]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})：实测中的连接用法、登录过期、Bot 市场。
- [nightd]({{< relref "/docs/grok-bot/sources/community/2026-10-07-nightd-impersonating-grok-bot" >}})：Web Bot Auth 签名。
