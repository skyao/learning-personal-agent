---
title: "文档（docs.x.ai）：电脑与应用"
linkTitle: "docs.x.ai：电脑与应用"
date: 2026-10-28
originalTitle: "Use the computer and apps"
sourceUrl: "https://docs.x.ai/grok-bot/computer-and-apps"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：Shared Bots 改称 Team Bots；新增自定义连接器、Stripe/Power BI/BigQuery 说明、Microsoft 365 管理员批准流程、1Password 的 @ 用法；钱包增 Shop Pay"
tags: [运行环境, 连接器, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「连接应用」「Bot 邮箱」与这页部分重合。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：每个用户有一台云端电脑，名下所有 Bot 共用，Cookie、文件和命令行凭据都共享；每个 Bot 有自己的屏幕，但屏幕不是安全边界，不同用户之间则是硬件隔离。登录依次尝试 Vault、1Password 和 Secure Form，遇到 SSO、通行密钥、验证码和银行卡验证时请用户接管；付款可以用 Vault 中的卡、Secure Form 中输入的卡，或 Link、X Money、Shop Pay 钱包。应用连接的 OAuth 令牌存在连接器后端，不落到电脑上；授权页登录要在约 10 分钟内完成；桌面端可用 **Add a custom connector** 添加 **Remote HTTPS** 或 **Command** 类型的连接器，团队管理员的 MCP 策略拦截时无法保存。文档还逐个说明了 Stripe（连接过一段固定时间后会断开）、Microsoft Power BI（只读，需工作或学校账号）、Google BigQuery 等应用，以及 Microsoft 365 管理员未批准应用时的处理。Bot 邮箱地址形如 `name@mail.grokbot.com`，每人一个，不能改名或删除；例程发出的邮件都先成草稿，没有无人值守的发送；文档还给出工作目录 `/workspace` 的持久化规则，以及 **Update**、**Recover**、**Reset** 三种恢复操作的对照。

**保留理由**：这是 Grok Bot「一人一台共享电脑」运行模型最集中的说明，连带讲清了登录、付款和邮箱的边界。

---

使用电脑与应用

你的 Bot 在一台持久的云端电脑上工作，配有浏览器、命令行和文件系统。合上笔记本电脑后工作仍会继续，文件、登录状态和浏览器会话会在任务之间保留。

## 一台电脑，由你所有的 Bot 共用

你账号上的每个 Bot 都使用同一台电脑：

* 浏览器 Cookie 和已登录的会话是共享的
* 每个 Bot 都能看到文件
* 命令行凭据是共享的
* 一个 Bot 可以接着另一个 Bot 保存的工作继续做

这台电脑分配给你的用户账号，而不是某个 Bot。如果账号上的另一个 Bot 不应该能使用某个凭据或文件，就不要把它放在上面。

每个 Bot 在这台共享电脑上有自己的屏幕。因此多个 Bot 可以并行使用浏览器和桌面工具，不过一个 Bot 在同一时间只能在自己的屏幕上运行一个电脑操作任务。屏幕是彼此分开的工作面，不是彼此分开的安全边界。

用户之间则是严格隔离：每个用户的电脑是专用的，并做了硬件隔离。见[用户如何隔离](https://docs.x.ai/grok-bot/teams-and-enterprises#how-users-are-isolated)。

## 观看电脑上的操作

点击对话右侧面板里的电脑预览，可以打开电脑，观看点击、输入、导航和当前状态。

工作继续时你可以离开预览。关闭 Grok Bot 应用或合上笔记本电脑，都不会让云端的工作停止。

## 接手敏感步骤

登录时，Bot 先使用保存在 [Vault](https://docs.x.ai/grok-bot/vault) 里的登录信息，然后使用已连接的密码管理器，例如 [1Password](#connect-1password)，最后用安全表单问你。来自 Vault 的登录信息和来自安全表单的值会在 Bot 看不到的情况下填入。当网站通过邮件发送一次性验证码时，Bot 可以从已连接的 [Gmail](https://x.ai/bot/plugin/45893410) 或 [Outlook](https://x.ai/bot/plugin/57302029) 账号读取，或从[它自己的收件箱](#give-your-bots-an-email-address)读取。结账时，它可以使用保存在 Vault 中的卡、你在安全表单中输入的卡，或已连接的钱包，例如 Link、X Money 或 Shop Pay；见[付款](https://docs.x.ai/grok-bot/vault#pay-for-things)。

表单无法完成的步骤，Bot 会把电脑交给你：

* 单点登录或通行密钥
* 它无法通过的验证码
* 在另一台设备上批准，或扫描二维码
* 银行卡验证
* 明确要求真人的网站

打开电脑、接管控制、只完成被卡住的那一步，然后告诉 Bot 继续。绝不要把密码或一次性验证码粘贴到普通聊天里。对于 API 密钥或其他密钥，在 Bot 询问时输入到安全密钥卡中：输入框是掩码的，值不会写进聊天，也不会给 Bot 看到。见 [API 密钥与其他密钥](https://docs.x.ai/grok-bot/vault#api-keys-and-other-secrets)。

## 登录一次

浏览器会话会保留，所以通常不需要为每个任务登录。由于浏览器是共享的，为一个 Bot 登录后，会话对你其他的 Bot 也可用。

有些网站会让会话过期、强制较短的超时，或再次要求验证。让 Bot 暂停并通知你，而不是试图绕过检查。

## 连接应用

应用给 Bot 提供一种结构化的方式，来处理 [Gmail](https://x.ai/bot/plugin/45893410)、[Notion](https://x.ai/bot/plugin/404) 和 [Slack](https://x.ai/bot/plugin/674) 这类服务，比在网站上逐页点击更可靠。对于没有应用的服务，或应用没有暴露的可视化流程，就使用浏览器。应用连接归属于你登录 Grok Bot 所用的同一个账号。

1. 从侧栏打开 **连接应用（Connect apps）**，或点击聊天内的 **连接（Connect）** 卡片。在移动应用中，点击左上角的头像，选择 **连接应用**。
2. 浏览或搜索该应用，然后添加它。
3. 当 Grok Bot 要你 **授权（Authorize）** 或 **认证（Authenticate）** 时，在浏览器里完成提供方的登录。
4. 如果登录没有完成，在应用上选择 **重新连接（Reconnect）**，或在聊天内卡片上选择 **重新打开（Reopen）**，把登录页调回来。在大约 10 分钟内完成登录，否则就从卡片重新开始。
5. 确认应用出现在 **已安装（Installed）** 下。

在聊天中输入 `@`，把应用附加到任务上。

**已添加（Added）** 表示应用已安装，不表示你已登录。如果 Bot 说缺少某个应用，打开该应用，在它显示 **需要认证（Needs auth）** 或 **已断开（Disconnected）** 时选择 **认证**（手机上是 **授权**）。

你也可以让 Bot 替你做这件事，例如「添加 Linear 应用。」[把 Linear 添加到 Grok Bot](https://x.ai/bot/plugin/512) Bot 会搜索目录，把应用安装到你的账号上，并在应用需要你登录时显示一张 **连接** 卡片。从你的下一条消息起，该应用的工具就绪。Bot 也可以添加不在目录里的 MCP 服务器，方式是 URL，或一条在它电脑上运行的命令；由命令启动的服务器对你其他的 Bot 也可用。在私有网络上添加服务器，或添加使用私有证书颁发机构的服务器，会先征求你的批准。

要在桌面应用中自己添加，在 **连接应用** 底部选择 **添加自定义连接器（Add a custom connector）**。输入 **名称（Name）**，然后选择 **类型（Type）**：**远程 HTTPS（Remote HTTPS）** 需要 **服务器 URL（Server URL）**，可选 **HTTP 头（HTTP headers）** 和 OAuth **客户端 ID（Client ID）**（输入后会显示 **客户端密钥（Client secret）** 字段）；**命令（Command）** 需要 **命令** 及其 **参数（Arguments）**。选择 **添加插件（Add plugin）** 保存。如果团队管理员的 MCP 策略阻止该服务器，就无法保存。

当 Bot 访问一个有应用的网站的登录页时，如果该应用已连接，它会使用该应用；否则会提供该应用的 **连接** 卡片，让你连接它，而不是通过浏览器登录。

当 Bot 替你移除一个应用时，该应用添加的一切都会随之移除，你也会退出登录，所以重新安装它意味着要再次登录。团队要求安装的应用无法移除。

* **应用是账号级的。** 已连接的应用对你运行的每个 Bot 都可用。队友的[团队 Bot](https://docs.x.ai/grok-bot/team-bots)在使用你的账号前会先询问。
* **应用登录信息不留在电脑上。** OAuth 令牌保存在 Cursor 的连接器后端，Bot 调用工具时不会收到它们。
* **团队策略适用。** 被团队[连接器策略](https://docs.x.ai/grok-bot/teams-and-enterprises#connector-policy)阻止的应用会显示 **被团队管理员禁用（Disabled by team admin）**；请让管理员启用它。阻止一个应用并不会阻止该服务的网站。关闭这第二条路径需要 **网络控制（Network Controls）**，它仅限 Enterprise。见[网络策略](https://docs.x.ai/grok-bot/security#network-policy)。

**邮件（Email）** 应用不同：它给你的 Bot [它们自己的邮件地址](#give-your-bots-an-email-address)，而不是连接你已有的账号。

### 已连接的应用能做什么

应用使用你授权的账号。它只能做该账号在该服务里本来就能做的事。它不能提升你的访问权限，也不能更改共享设置。

* **Google Calendar：** Bot 可以读取你能看到的日历，创建和更新事件，查看空闲时间，并在你能编辑的日历上回复邀请。它不能更改 Google Meet 设置，例如等候室或主持人控制，也不能添加 Zoom 链接，因为 Google 的 Zoom 附加组件不提供给该应用。你可以自己把 Zoom 链接放进事件的地点或描述，或在 [Google Calendar](https://x.ai/bot/plugin/45893411) 中创建事件，再让 Bot 更新其他字段。
* **Google Sheets：** Bot 可以读取和编辑已连接 Google 账号可编辑的表格中的单元格。以查看者身份共享的文件保持只读。查找和打开文件使用 [Google Drive](https://x.ai/bot/plugin/45893413) 应用，它可以搜索和读取该账号能打开的文件。
* **Google Docs：** 就地编辑文档内容使用 [Google Docs](https://x.ai/bot/plugin/45893412) 应用。如果只连接了 [Google Drive](https://x.ai/bot/plugin/45893413)，Bot 会先添加 Google Docs（需要登录时给你一张 **连接** 卡片），然后才转向浏览器。
* **Slack：** 应用以你连接的 [Slack](https://x.ai/bot/plugin/674) 用户身份发帖，而不是作为一个需要被邀请的独立 bot。它只能在该用户能发帖的频道里发帖。要使用另一个 Slack 工作区，就连接那个工作区。这与[触发例程](https://docs.x.ai/grok-bot/skills-routines-and-automations#trigger-work-from-an-event)的 Slack 消息是两回事。
* **Gmail：** 应用可以在已连接的邮箱上搜索和读取邮件、起草和发送、应用标签。一张 [Gmail](https://x.ai/bot/plugin/45893410) 草稿卡片会在消息下方显示你的 Gmail 签名，而 Bot 保存在 Gmail 里的草稿会保留该签名，所以落款由它代劳。Gmail 一次连接一个邮箱；要换另一个，先断开当前邮箱再授权另一个。如果某个 Bot 不应该使用那个邮箱，就断开 Gmail。其他一些应用，比如 [Notion](https://x.ai/bot/plugin/404)，可以[连接第二个账号](#connect-a-second-account)。
* **Stripe：** Stripe 会在登录后固定一段时间结束每个连接，无论使用多频繁，所以你需要不时重新连接。如果你最近用过 Stripe，Bot 会在需要重新连接时告诉你。
* **X：** [X](https://x.ai/bot/plugin/49086599) 插件需要你的 X 开发者账号上有 X API 额度。
* **Microsoft Power BI：** 用工作或学校 Microsoft 账号连接；个人 Microsoft 账号无法连接。Bot 可以列出工作区、报表和数据集，并把一份报表或其中某一页渲染成图片。所有 Power BI 工具都只读。渲染需要该工作区处于 Premium、Embedded 或 Fabric 容量，并开启 Power BI 租户设置 **将报表导出为图像文件（Export reports as image files）**。
* **Google BigQuery：** Bot 查询已连接 Google 账号可读取的数据集。它像其他 Google 应用一样以 **Grok** 身份登录 Google，所以公司的 Google 阻止使用[下面的步骤](#if-google-says-an-admin-needs-to-review-grok)。团队管理员可以在仪表盘[插件与 MCP 页面](https://cursor.com/dashboard/plugins)的插件团队设置中输入团队自己的 Google OAuth 客户端 ID 和密钥；成员随后在该客户端下登录。
* **Databricks Genie：** 需要团队管理员先设置好，成员才能连接。管理员在 Databricks 账号中注册一个 OAuth 应用连接，然后在仪表盘[插件与 MCP 页面](https://cursor.com/dashboard/plugins)的插件团队设置中输入工作区 URL、客户端 ID 和客户端密钥（公共客户端留空）。每位成员随后用自己的 Databricks 账号登录，Bot 用自然语言就该账号可查询的数据向 Genie 提问。
* **Asana：** 无需管理员设置。Bot 在你的 Asana 账号能打开的工作区和项目中工作。
* **Vanta：** 每个账号只在一个区域。第一次连接时，在登录时选择你账号所在的区域：**美国（United States）**、**欧洲（Europe）** 或 **澳大利亚（Australia）**。在错误区域登录找不到你的账号；重新登录并选择另一个区域。
* **Shop Pay：** 一个钱包。连接它并登录 Shop，Bot 就能在 Shopify 商店用 Shop Pay 结账。见[付款](https://docs.x.ai/grok-bot/vault#pay-for-things)。

### 连接第二个账号

有些应用可以连接多个账号，比如两个 [Notion](https://x.ai/bot/plugin/404) 工作区。

1. 在侧栏选择 **连接应用**，打开该应用。
2. 在 **账号（Accounts）** 下选择 **添加另一个账号（Add Another Account）**。
3. 给账号起个标签，比如工作或个人。
4. 选择 **授权** 并登录第二个账号。

在手机上，从 **连接应用** 打开该应用，选择 **添加账号（Add account）**。

用标签告诉 Bot 该用哪个账号，例如「用我的工作 Notion」。你 Grok Bot 账号上的每个 Bot 都能使用每个已连接的账号。如果你看不到 **添加另一个账号**，说明该应用一次只连接一个账号。

### 如果 Google 说管理员需要审核 Grok

公司 Google 账号可以在 [Gmail](https://x.ai/bot/plugin/45893410)、[Google Calendar](https://x.ai/bot/plugin/45893411)、[Google Drive](https://x.ai/bot/plugin/45893413)、[Google Docs](https://x.ai/bot/plugin/45893412)、Sheets、[Google Slides](https://x.ai/bot/plugin/45893415) 或 BigQuery 完成登录之前就阻止连接。Grok Bot 以 **Grok** 身份登录 Google，而不是 Cursor。这与 Cursor 的 **被团队管理员禁用** 控制是两回事。

如果 Google 页面显示 **你的管理员需要审核 Grok（Your admin needs to review Grok）**，说明 Grok 还没有为该 Workspace 获批。如果有请求访问的按钮，就申请访问，然后等管理员批准 Grok 后再重试 **授权**。IT 管理员在 Google 管理控制台中批准 **Grok**：

1. 打开 **安全（Security）**，然后 **访问与数据控制（Access and data control）**，然后 **API 控制（API controls）**。
2. 打开 **应用访问控制（App access control）**，然后 **管理第三方应用访问（Manage third-party app access）**。
3. 添加名为 **Grok** 的应用。如果按名称搜索找不到，就用被阻止页面或管理员审核邮件中的客户端 ID。
4. 把使用 Grok Bot 的人对 Grok 的访问设为 **受信任（Trusted）**。

该批准覆盖这些人连接的 Google 应用。它不会在 Cursor 中重新启用某个应用。

如果页面显示 **访问被阻止（Access blocked）**，是 Google 拒绝了登录。个人 [Gmail](https://x.ai/bot/plugin/45893410) 账号不需要公司管理员；公司账号经常在 Grok 不在允许列表中，或管理员阻止了第三方应用时遇到这种情况。请 Google 管理员按上面的步骤信任 **Grok**。换浏览器或重新连接应用都不能解除 Google 管理员的阻止。如果页面仍说访问被阻止，请带上 Google 账号邮箱和被阻止页面的截图[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。

### 如果 Microsoft 说管理员需要批准 Grok Bot

工作或学校 Microsoft 365 账号可以在组织的 Microsoft 365 管理员批准该应用之前，阻止 [Outlook](https://x.ai/bot/plugin/57302029)、[Outlook Calendar](https://x.ai/bot/plugin/57302030)、[OneDrive](https://x.ai/bot/plugin/57302028) 或 **Teams** 连接。重试登录或再次允许权限都没有用。

* 在你的电脑上，登录页会显示 **你的组织的 Microsoft 365 管理员需要先批准此应用，你才能连接（Your organization's Microsoft 365 admin needs to approve this app before you can connect）**，并给出 **给你的 IT 管理员的批准链接（Approval link for your IT admin）**。把这个链接发给你的 IT 管理员。他们批准后，从 Grok Bot 重新连接。
* 在 1.19.0 或更高版本的手机应用上，连接卡片会说同样的话，并加上 **请你的 IT 管理员批准 Grok Bot，然后重新连接（Ask your IT admin to approve Grok Bot, then connect again）**。手机不显示批准链接，所以如果你的管理员需要它，就先从电脑连接一次拿到链接。

如果页面改为说该应用 **被你的组织阻止（blocked by your organization）**，管理员必须允许该连接。页面会列出连接器、Microsoft Entra 应用程序 ID、错误码和时间，供你发给他们。

### 如果手机提示在电脑上连接

有些提供方无法从手机浏览器完成登录。在 1.19.0 或更高版本的手机应用上，**Adapter**、**Robinhood** 和 **Intercom** 的 **连接**，以及 iPhone 上 **Postiz** 的 **连接**，会显示 **在电脑上连接（Connect on your computer）**，而不是打开登录页。在电脑上打开 Grok Bot 并在那里连接该应用。连接随后在手机上也能用，因为应用属于你的账号，而不是设备。

[Slack](https://x.ai/bot/plugin/674) 仍可在手机上登录。如果你在完成前关闭了它的登录，手机会提醒你 [Slack](https://x.ai/bot/plugin/674) 的手机登录需要你的工作区密码，并提示你可以改从电脑连接 Slack。

### 连接 1Password

1Password 让你的 Bot 用你 1Password 账号里的登录信息，在它们的电脑上登录网站。你在 1Password 中批准每次登录，由 1Password 填入；你的 Bot 从来看不到这些值。新的 1Password 集成正在逐步推出。它适用于个人和 Family 版 1Password 账号，需要 1Password 8.12.42 或更高版本。

1. 选择 **连接应用**，在 **密码管理器（Password managers）** 下打开 **1Password**。
2. 在你的电脑上选择 **连接 1Password（Connect 1Password）**。
3. 浏览器会打开。在那里登录 1Password 并批准 Grok Bot。完成后 Grok Bot 会更新。

在手机上，从 **连接应用** 的 **密码管理器（Password Managers）** 栏打开 1Password，或搜索它，然后在 1Password 中批准连接。如果你的手机显示 **1Password 只能在 Mac 上设置（1Password can only be set up on a Mac）**，说明新集成还没有推送到你的账号；改从电脑上的 Grok Bot 设置。要停止使用 1Password，在 **连接应用** 中打开它并选择 **断开（Disconnect）**。

1Password 连接后，在消息框中输入 **@** 并选择 **1Password**，让 Bot 使用你的 1Password 登录信息。

当某个登录信息没有保存在 Vault 中时，Bot 会在聊天中发一张卡片，写明网站名称：

1. 选择 **在 1Password 中查看（Review in 1Password）**。1Password 应用会打开；如果那台电脑上没有安装应用，1Password 会在浏览器中打开。
2. 在 1Password 中选择要分享的确切登录信息，并批准请求。
3. 1Password 在 Bot 的浏览器中填入登录信息。

你分享过的登录信息在之后的聊天中仍然可用。如果 1Password 不再允许，Bot 会再次询问。1Password 不会填入支付卡，你的 Bot 仍会请你在它填不了的步骤上帮忙，比如通行密钥、单点登录或验证码。

1Password 只提供你自己个人保险库（在 Family 账号中叫 Private）里的登录信息，不提供共享保险库里的。把登录信息移动或复制到那个保险库，再让 Bot 重试。如果完全没有出现批准提示，把 1Password 应用更新到 8.12.42 或更高版本。

新集成不再使用服务账号，所以如果你以前在 Grok Bot 中用过 1Password，请重新连接。你与旧集成共享的保险库里的登录信息，在你把它们移到个人或 Private 保险库之前不可用；**连接应用** 中的 1Password 页面会告诉你有多少条。在 Mac 上，你可以改为选择 **移到 Private（Move to Private）**，如果它询问，就在 1Password 中批准。旧保险库会留在 1Password 里。

| 消息 | 该怎么做 |
| --- | --- |
| **1Password 未能完成连接（1Password didn't finish connecting）** | 重新开始连接。在手机上，如果你已经有 1Password 账号，选择 **我已有 1Password（I already have 1Password）** 并用它登录。 |
| **这个 1Password 账号已连接到另一个 Grok Bot 账号（This 1Password account is already connected to another Grok Bot account）** | 先从另一个 Grok Bot 账号断开 1Password，或连接另一个 1Password 账号。 |
| **需要重新连接（Reconnect required）** | 1Password 不再接受该连接。选择 **重新连接**。 |
| **登录你连接到 Grok Bot 的那个 1Password 账号，然后重试（Sign in to the 1Password account you connected to Grok Bot, then try again）** | 登录你连接过的账号，然后让 Bot 重试。 |
| **你的 1Password 账号未开启访问请求（Access requests aren't turned on for your 1Password account）** | 请你的 1Password 管理员开启访问请求。 |
| **这个请求在 1Password 中已经结束（This request already ended in 1Password）** | 让 Bot 重试。它会发送一个新请求。 |
| **无法打开 1Password（1Password could not be opened）** | 你自己打开 1Password 应用来查看请求。 |
| 一条要你在 1Password 的 **集成（Integrations）** 下撤销 Grok Bot 访问权限的消息 | 在 1Password 的 **集成** 下撤销 Grok Bot 的访问权限，然后重新连接 1Password。 |

### 已知的应用问题

* **Zoom 错误 4700：** 从 Grok Bot 桌面应用授权 Zoom 目前会以错误 4700（Invalid redirect）失败。目前没有变通办法，你这边也无法通过改动解决。
* **SharePoint AADSTS50011：** 当 Cursor 团队管理员从仪表盘 **集成（Integrations）** 页面以 **应用级权限（Application-level permissions）** 连接 SharePoint 时，Microsoft 会在同意提示之前显示重定向 URI 不匹配。你的租户里没有任何东西导致这个问题。改用 **委托权限（Delegated permissions）** 连接：在 SharePoint 卡片上选择 **连接团队（Connect team）**（或 **重新连接**），选择 **委托权限**，输入你的 Microsoft 租户 ID，并用 Microsoft 登录。大多数工作或学校租户需要一名 Microsoft 管理员一次性同意 Sites.Read.All。之后每位成员在 Bot 首次使用 SharePoint 时用自己的 Microsoft 账号登录，并且只能看到其账号本来就能打开的站点。如果成员看到「这个团队没有 SharePoint 集成」（This team does not have the SharePoint integration），管理员需要完成委托登录。

更多设置帮助见[连接插件](https://grok.com/help/grok-bot/connect-plugins)。

## 给你的 Bot 一个邮件地址

你可以在 `mail.grokbot.com` 上认领一个邮件地址，例如 `yourname@mail.grokbot.com`，供你的 Bot 使用。你的 Bot 随后可以用它接收、读取、搜索和发送邮件。有了地址，Bot 可以：

* 用自己的地址注册服务，并在你同意后取回验证码或链接
* 收集收据、新闻简报和报告，并为你汇总
* 为你起草邮件，比如摘要或更新，以及起草回复
* 转发它收件箱里的邮件，保留原来的格式、图片和附件，这需要 Grok Bot 0.75.2 或更高版本
* 在邮件到达时运行例程，可选只在来自特定发件人时运行

要认领地址，让 Bot 去做，例如「给你自己弄个邮件地址。」它会问你想要什么名字，检查名字是否可用，并显示一张批准卡；在你批准之前不会认领任何东西。你也可以打开 **连接应用**，选择 **邮件（Email）**，在 **邮件地址（Email address）** 下的 **选择一个名字（Choose a name）** 中输入名字，然后选择 **创建地址（Create address）**。在 iPhone 和 Android 上，打开 **设置 → 连接应用 → 邮件**。认领之后，应用会显示你的地址，并带一个复制按钮。

名字使用小写字母、数字、点、连字符和下划线，以字母或数字开头和结尾，最长 64 个字符。support、admin、billing、security、help、info、team、cursor、grok 和 xai 等保留字不允许使用。

你的地址也接受加号别名。发往 `yourname+receipts@mail.grokbot.com` 的邮件会进入与 `yourname@mail.grokbot.com` 相同的收件箱，所以你可以给每个服务一个自己的别名，而不必再认领地址。Bot 也可以用别名发送；监视某个别名的例程只对发往该别名的邮件运行，而针对裸地址的例程会对所有邮件运行。别名是标签，不是锁：任何人都能往它写邮件，所以如果例程只应对某些发件人采取行动，就要保留发件人过滤。

* **一个地址，永久使用。** 你得到一个地址，且不能改名或删除。地址永不重新发放，即使认领它的账号被删除。
* **是你的，不是某个 Bot 的。** 你所有的 Bot 都可以在你自己的聊天和例程中使用这个地址。它不会用在 Slack 话题串中，也不会用在别人与 Bot 对话的聊天中，[团队 Bot](https://docs.x.ai/grok-bot/team-bots)没有团队地址。
* **读取邮件。** 任何人都可以往这个地址发邮件。未通过垃圾邮件或病毒扫描的邮件会被保留，但不带正文和附件，也永远不会触发例程。没有收件箱视图，也没有新邮件通知，所以要问 Bot，例如「你的收件箱今天收到了什么？」最近一分钟内到达的邮件可能还不会出现在搜索里。每条收到的邮件最多可含 10 个附件，每个最大 10 MB，总计 25 MB；超出限制的附件会被跳过。
* **对邮件采取行动。** 新邮件不会自行开启聊天或唤醒 Bot。要据此行动，请设置一个[例程](https://docs.x.ai/grok-bot/skills-routines-and-automations#trigger-work-from-an-event)，监视来自任何人、特定地址或整个域（例如 `*@example.com`）的邮件。默认情况下，例程只对通过标准邮件认证检查的发件人的邮件运行，且例程不能按主题过滤。
* **发送邮件。** 当你在聊天中让 Bot 发邮件时，在[自动审核](https://docs.x.ai/grok-bot/approvals-security-and-privacy#configure-auto-review)允许后它就会发出；如果自动审核需要你，你会先看到一张批准卡。来自例程的邮件，或任何不是由你这句请求发起的轮次中的邮件，会作为草稿等待你按 **发送（Send）**，没有无人值守发送的选项。如果你也连接了 [Gmail](https://x.ai/bot/plugin/45893410) 或 [Outlook](https://x.ai/bot/plugin/57302029)，当两者都可用时，Bot 会问从哪个账号发送。
* **安全。** Bot 把来自他人的邮件当作信息，而不是指令。它读取的每条消息都会标记为来自你或来自他人，邮件里的指令永远不算你允许它发送或行动的授权。

发送限制：

* 每封邮件最多 50 个收件人（To、Cc 和 Bcc 合计）
* 最多 10 个附件，每个最大 10 MB，总计 25 MB；不能附加可执行文件
* 新闻简报和初次联系的邮件每封只发一个收件人，并包含一键退订链接
* 如果邮件退回，或有人退订、标记为垃圾邮件，Bot 会停止向该地址发邮件，并告诉你它跳过了谁
* Bot 能给多少新联系人发邮件也有限制，以避免该地址被标记为垃圾邮件

如果你删除 Grok Bot 账号，你的邮件和附件会被删除，地址也会被收回。

在 Cursor 团队中，agent 邮件默认关闭；管理员先开启 [Agent 邮件（Agent Email）](https://docs.x.ai/grok-bot/teams-and-enterprises#agent-email)，成员才能认领地址。如果管理员之后关掉它，Bot 会失去邮件工具，邮件例程停止运行，但发往现有地址的邮件仍会被接收和保留，成员也保留他们的地址。

| 你会看到 | 该怎么做 |
| --- | --- |
| **此账号未启用 agent 邮件（Agent email is not enabled for this account.）** | 你的账号还无法使用 agent 邮件。 |
| **你的团队管理员已关闭 Grok Bot agent 邮件，因此此账号无法认领或使用 agent 邮件地址（Your team admin has turned off Grok Bot agent email, so this account cannot claim or use an agent email address.）** | 请团队管理员开启 **Agent 邮件**。 |
| **该地址已被占用，且地址永不重新发放，所以重试不会成功。请换一个名字（That address is taken, and addresses are never reissued, so retrying it cannot succeed. Choose a different name.）** | 换一个名字。 |
| 一条关于允许的字符、长度或保留字的提示 | 选一个符合上述名字规则的名字。 |
| **你只能有一个 agent 邮件地址（You can have one agent email address.）** | 你已经有地址了。问你的 Bot 它是什么，或打开 **邮件** 应用。 |
| **无法创建你的邮件地址。请重试（Couldn't create your email address. Try again.）**（手机） | 检查名字规则，或在桌面端重试，桌面端会显示确切原因。 |
| **最近一分钟检查的邮件地址过多（Too many email addresses checked in the last minute.）** | 等一分钟再试。 |

## 搜索和阅读 X

无需连接 X 账号，Bot 就能搜索和阅读 X 上的公开内容。让 Bot 搜索帖子、从其链接打开帖子、读取某个账号的帖子和提及、查看谁引用了或转发了某条帖子、统计某个话题的近期帖子数，或查看趋势和新闻。

这种访问是只读的，不会以你的身份登录。要访问你的私信、书签、主页时间线，或谁赞了你的帖子，请从 **连接应用** 添加 X 插件并用 X 登录。[把 X 添加到 Grok Bot](https://x.ai/bot/plugin/49086599)

## 处理文件

电脑在 `/workspace` 有一个共享工作区。把需要长期保留的项目文件放在那里，用清晰的项目文件夹。

文件、浏览器状态和受支持的登录状态能在正常的电脑更新和恢复后保留。把临时目录、手动安装的包和未提交的应用状态视为可替换的。把重要结果复制到共享工作区，或附加到对话中。

对话历史保存在电脑之外，所以在电脑里删除文件（包括 `rm -rf`）不会删除聊天。Grok Bot 会保留同步电脑数据的持久副本，重新打开电脑时会从该副本恢复，所以已同步的文件通常能回来。`node_modules` 或 Python 虚拟环境等项目文件夹不会被保存；在电脑更新、**恢复（Recover）** 或 **重置（Reset）** 之后要重新安装它们。只存在于你的 Mac 或 Windows 机器上的文件不在此列，请自行备份那些文件。

当电脑快满时，你的 Bot 会在聊天中提醒你一次，列出最大的文件或文件夹及其大小，并提出删除它们。除非你说可以，否则不会删除任何东西。磁盘空间不足不是数据丢失，清理只针对电脑文件，不涉及聊天。

## 更新、恢复或重置电脑

从 **设置 → 电脑** 的 **Bot 的电脑** 下打开电脑控制项。当应用提供时，你也可以从重连界面获得 **恢复**。应用和电脑分别更新。

| 操作 | 作用 | 保留什么 | 移除什么 |
| --- | --- | --- | --- |
| **更新（Update）** | 把电脑移到最新版本。有些更新只刷新 Grok Bot 的软件；有些会替换整台电脑，后者可能可以安排到之后进行。**更新 Bot 的电脑** 下方的文字会说明在等待的是哪一种。 | 软件更新：全部，包括已安装的应用。电脑更新：Bot、文件和登录信息。 | 软件更新：无。电脑更新：已安装的应用和包。 |
| **恢复（Recover）** | 尽可能保存，然后用你的已保存数据在最新版本上构建一台新电脑。正在运行的工作会中断。 | 已保存的 Bot、文件和登录信息 | 已安装的应用和包；如果无法连接电脑来保存，还会丢失非常近期的改动 |
| **重置（Reset）** | 用你最后保存的数据在最新版本上构建一台新电脑。正在运行的工作会中断。 | 已保存的 Bot、文件和登录信息 | 已安装的应用和包；如果无法连接电脑来保存，还会丢失非常近期的改动 |

对话保存在电脑之外，所以即使重置也能保留。如果 Bot 最近消失了，或保存失败，在使用 **恢复** 或 **重置** 之前先[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。

当电脑无法连接时，从破坏性最小的选项开始：

1. 先等一等，如果电脑显示 **正在重新连接（Reconnecting）** 或 **无法连接 Grok Bot 的电脑（Couldn't reach Grok Bot's computer）**，就选择 **重试（Retry）**，或重新打开对话。重连期间 Bot、文件和登录信息是安全的。此时不要 **重置**。
2. 完全退出 Grok Bot 再重新打开，并检查应用更新。在 Mac 上，从菜单栏选择 **退出（Quit）**，而不只是关闭窗口。
3. 如果提供了更新，在 **设置 → 电脑** 中使用 **更新 Bot 的电脑**。
4. 如果它仍然无法重连，或更新看起来卡住了并且显示了 **恢复电脑（Recover computer）**，就选择 **恢复电脑**（确认对话框里叫 **恢复 Grok Bot 的电脑（Recover Grok Bot's computer）**）。更新较慢时，**继续等待（Keep waiting）** 是安全的默认选择。
5. 只有在这些步骤之后才使用 **重置 Bot 的电脑（Reset Bot's computer）**。

不要在更新或重置已经在运行时再启动第二个；反复重置会打断仍在完成的恢复。**正在重新连接** 和 **恢复** 通常需要几分钟，你可以选择 **在后台继续（Continue in Background）**。**更新** 也可能需要几分钟；如果它显示 **更新仍在运行（Update still running）**，就继续等待。如果 **恢复** 或 **重置** 失败，使用一次 **重试恢复（Retry Recovery）** 或 **重试重置（Retry Reset）**，然后停下来[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。

如果电脑的文件还没有备份好，**更新** 会说它们尚未就绪，且不会发生任何改动；等一会儿再试，而不是重置。如果设置显示 **有一个 agent 未能及时暂停，因此电脑未更新（An agent couldn't pause in time, so the computer was not updated）**，让那个 Bot 完成，然后再次选择 **更新**。

当电脑显示 **正在重新连接** 或 **无法连接 Grok Bot 的电脑** 时，Bot 无法完成一轮。用上面的步骤修复连接，然后重新发送消息。关于聊天丢失以及何时联系支持，见[故障排查](https://docs.x.ai/grok-bot/troubleshooting)。

## 你的本地电脑是分开的

Grok Bot 的云端电脑与你面前的 Mac 或 Windows 电脑是分开的。只有在启用该能力，并且你按本地电脑策略批准后，Bot 才会在你的本地电脑上运行命令：逐条命令批准，默认是 **每次都询问（Ask every time）**，或者 **始终允许（Always allow）**、**从不允许（Never allow）**。该策略与管辖云端电脑工作的批准是分开的。

在[批准、安全与隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy#control-access-to-your-local-computer)中查看本地电脑权限。
