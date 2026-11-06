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
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [运行环境, 连接器, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「连接应用」「Bot 邮箱」与这页部分重合。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：每个用户有一台云端电脑，名下所有 Bot 共用，Cookie、文件和命令行凭据都共享；每个 Bot 有自己的屏幕，但屏幕不是安全边界，不同用户之间则是硬件隔离。登录依次尝试 Vault、1Password 和聊天内的安全表单，遇到 SSO、通行密钥、验证码和银行卡验证时请用户接管；付款可以用 Vault 中的卡、安全表单，或 Link、X Money 钱包。应用连接的 OAuth 令牌存在连接器后端，不落到电脑上。Bot 邮箱地址形如 `name@mail.grokbot.com`，每人一个，不能改名或删除；例程发出的邮件都先成草稿，没有无人值守的发送。文档还给出工作目录 `/workspace` 的持久化规则，以及 Update、Recover、Reset 三种恢复操作的对照。

**保留理由**：这是 Grok Bot「一人一台共享电脑」运行模型最集中的说明，连带讲清了登录、付款和邮箱的边界。

---

使用电脑与应用

你的 Bot 在一台持久化的云端电脑上工作，配有浏览器、命令行和文件系统。即使你的笔记本电脑合上，工作也会继续；文件、登录状态和浏览器会话在任务之间保持。

## 一台电脑，由你的所有 Bot 共用

你账户上的每个 Bot 都使用同一台电脑：

* 浏览器 Cookie 和已登录会话共享
* 文件对每个 Bot 可见
* 命令行凭据共享
* 一个 Bot 可以接着另一个 Bot 保存的工作继续

这台电脑分配给你的用户账户，而不是某个 Bot。如果账户上的另一个 Bot 不应能使用某项凭据或文件，就不要把它放在上面。

每个 Bot 在共享电脑上有自己的屏幕。因此多个 Bot 可以并行使用浏览器和桌面工具，不过一个 Bot 在同一时间只能在其屏幕上运行一个计算机使用（computer use）任务。这些屏幕是彼此独立的工作界面，而不是独立的安全边界。

用户之间是严格隔离的：每个用户的电脑都是专用且硬件隔离的。见[用户如何隔离](https://docs.x.ai/grok-bot/teams-and-enterprises#how-users-are-isolated)。

## 观看电脑上的工作

点击对话右侧面板中的电脑预览，打开电脑并观看点击、输入、导航和当前状态。

你可以在工作继续时离开预览。关闭 Grok Bot 应用或你的笔记本电脑不会停止云端工作。

## 接管敏感步骤

登录时，Bot 会先使用保存在 [Vault](https://docs.x.ai/grok-bot/vault) 中的登录信息，然后使用已连接的密码管理器（例如 [1Password](#connect-1password)），最后通过安全表单（Secure Form）向你询问。来自 Vault 和安全表单的值会被填入页面，Bot 看不到它们。当网站通过电子邮件发送一次性验证码时，Bot 可以从已连接的 Gmail 或 Outlook 账户，或从[它自己的收件箱](#give-your-bots-an-email-address)读取。结账时，它可以使用保存在 Vault 中的卡、你在安全表单中输入的卡，或已连接的钱包（例如 Link 或 X Money）；见[付款](https://docs.x.ai/grok-bot/vault#pay-for-things)。

当表单无法完成某一步时，Bot 会把电脑交给你：

* 单点登录或通行密钥
* 它无法通过的验证码（CAPTCHA）
* 在另一台设备上批准，或扫描二维码
* 银行卡验证
* 明确要求真人的网站

打开电脑，取得控制权，只完成被阻塞的那一步，然后告诉 Bot 继续。绝不要把密码或一次性验证码粘贴到普通聊天中。对于 API key 或其他秘密，在 Bot 询问时输入到安全秘密卡片中：该字段会被遮蔽，值不会写入聊天，也不会显示给 Bot。见 [API keys 和其他秘密](https://docs.x.ai/grok-bot/vault#api-keys-and-other-secrets)。

## 登录一次

浏览器会话会保持，因此你通常不需要为每个任务登录。由于浏览器是共享的，为一个 Bot 登录会让该会话对你的其他 Bot 可用。

有些网站会让会话过期、强制较短的超时，或再次要求验证。请让 Bot 暂停并通知你，而不是尝试绕过该检查。

## 连接应用

应用（App）为 Bot 提供了与 Gmail、Notion 和 Slack 等服务协作的结构化方式；在存在应用时，它比在网站上点击更可靠。对于没有应用的服务，或应用未提供的可视化工作流，请使用浏览器。应用连接属于你登录 Grok Bot 时所用的同一账户。

1. 从侧边栏打开 **连接应用（Connect apps）**，或点击聊天内的 **连接（Connect）** 卡片。在移动应用中，点击左上角的头像并选择 **连接应用**。
2. 浏览或搜索该应用，然后添加。
3. 当 Grok Bot 要求你 **授权（Authorize）** 或 **验证身份（Authenticate）** 时，在浏览器中完成提供方的登录。
4. 如果登录没有完成，在应用上选择 **重新连接（Reconnect）**，或在聊天内卡片上选择 **重新打开（Reopen）**，把登录页面带回来。
5. 确认该应用出现在 **已安装（Installed）** 下。

在聊天中，输入 `@` 把该应用附加到任务。

**已添加（Added）** 表示应用已安装，并不意味着你已登录。如果 Bot 说缺少某个应用，请打开该应用；若它显示 **需要验证（Needs auth）** 或 **已断开（Disconnected）**，选择 **验证身份**（手机上为 **授权**）。

你也可以让 Bot 替你完成，例如「添加 Linear 应用」。Bot 会搜索目录、在你的账户上安装该应用，并在应用需要你登录时显示 **连接** 卡片。该应用的工具从你的下一条消息起就绪。Bot 还可以添加目录中没有的 MCP 服务器，方式是通过 URL 或在其电脑上运行的命令；由命令启动的服务器对你的其他 Bot 也可用。添加私有网络上的服务器，或使用私有证书颁发机构的服务器时，会先请求你的批准。

当 Bot 为你移除应用时，该应用添加的所有内容都会一并移除，你也会退出登录，因此重新安装意味着再次登录。团队要求的应用无法移除。

* **应用是账户级的。** 已连接的应用对你运行的每个 Bot 可用。队友的[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)在使用你的账户前会先询问。
* **应用登录信息不会落在电脑上。** OAuth 令牌保存在 Cursor 的连接器后端，Bot 调用工具时不会收到它们。
* **团队策略适用。** 被团队[连接器策略](https://docs.x.ai/grok-bot/teams-and-enterprises#connector-policy)阻止的应用会显示 **已被团队管理员禁用（Disabled by team admin）**；请让管理员启用它。阻止一个应用并不会阻止该服务的网站。要关闭这第二条路径，需要 **网络控制（Network Controls）**，仅限 Enterprise。见[网络策略](https://docs.x.ai/grok-bot/security#network-policy)。

**电子邮件（Email）** 应用不同：它给你的 Bot [它们自己的电子邮件地址](#give-your-bots-an-email-address)，而不是连接你已有的账户。

### 已连接的应用能做什么

应用使用你授权的账户。它只能做该账户在该服务中已经能做的事。它不能提升你的访问权限，也不能更改共享设置。

* **Google Calendar：** Bot 可以读取你能看到的日历、创建和更新事件、查看空闲时间，并在你可编辑的日历上回复邀请。它不能更改 Google Meet 设置（例如等候室或主持人控制），也不能添加 Zoom 链接，因为该应用无法使用 Google 的 Zoom 附加组件。请自己把 Zoom 链接放入事件地点或描述，或者在 Calendar 中创建事件，再让 Bot 更新其他字段。
* **Google Sheets：** Bot 可以读取和编辑已连接 Google 账户可编辑的电子表格中的单元格。以查看者（Viewer）身份共享的文件仍然只读。查找和打开文件使用 **Google Drive** 应用，它可以搜索并读取该账户能打开的文件。
* **Slack：** 应用以你连接的 Slack 用户身份发帖，而不是作为一个需要被邀请的独立 bot。它只能在该用户可发帖的频道中发帖。要使用另一个 Slack 工作区，请连接该工作区。这与[启动例程](https://docs.x.ai/grok-bot/skills-routines-and-automations#trigger-work-from-an-event)的 Slack 消息是两回事。
* **Gmail：** 应用可以在已连接的邮箱中搜索和读取邮件、起草和发送邮件，以及应用标签。Gmail 一次连接一个邮箱；要使用另一个邮箱，请断开当前邮箱并授权另一个。如果某个 Bot 不应使用该邮箱，请断开 Gmail。某些其他应用（例如 Notion）可以连接第二个账户。
* **X：** X 插件需要你的 X 开发者账户中有 X API 额度。

### 如果 Google 说管理员需要审核 Grok

公司 Google 账户可以在 Gmail、Calendar、Drive、Docs、Sheets 或 Slides 完成登录之前阻止连接。Grok Bot 以 **Grok** 的身份登录 Google，而不是 Cursor。这与 Cursor 的 **已被团队管理员禁用** 控制是两回事。

如果 Google 页面显示 **你的管理员需要审核 Grok（Your admin needs to review Grok）**，说明 Grok 尚未获得该 Workspace 的批准。如果有请求访问按钮，请申请访问；等管理员批准 Grok 后，再尝试 **授权**。IT 管理员在 Google 管理控制台中批准 **Grok**：

1. 打开 **安全（Security）**，然后 **访问和数据控制（Access and data control）**，再打开 **API 控制（API controls）**。
2. 打开 **应用访问控制（App access control）**，然后 **管理第三方应用访问（Manage third-party app access）**。
3. 添加名为 **Grok** 的应用。如果按名称搜索找不到，请使用被阻止页面或管理员审核邮件中的客户端 ID。
4. 为使用 Grok Bot 的人员把 Grok 设置为 **受信任（Trusted）**。

该批准只覆盖这些人连接的 Google 应用。它不会在 Cursor 中重新启用应用。

如果页面显示 **访问被阻止（Access blocked）**，说明 Google 拒绝了登录。个人 Gmail 账户不需要公司管理员；公司账户在 Grok 不在允许列表中，或管理员已阻止第三方应用时，常会遇到这种情况。请按上述步骤让 Google 管理员信任 **Grok**。更换浏览器或重新连接应用不会解除 Google 管理员的阻止。如果页面仍显示访问被阻止，请带上 Google 账户电子邮件和被阻止页面的截图[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。

### 连接 1Password

1Password 让你的 Bot 使用你 1Password 账户中的登录信息，在其电脑上登录网站。你在 1Password 中批准每次登录，由 1Password 填入；你的 Bot 永远看不到这些值。新的 1Password 集成正在逐步推出。它适用于个人和 Family 1Password 账户，需要 1Password 8.12.42 或更高版本。

1. 选择 **连接应用**，在 **密码管理器（Password Managers）** 下打开 **1Password**。
2. 在你的电脑上，选择 **连接 1Password（Connect 1Password）**。
3. 浏览器会打开。在那里登录 1Password 并批准 Grok Bot。完成后 Grok Bot 会更新。

在手机上，从 **连接应用** 的 **密码管理器** 栏打开 1Password，或搜索它，然后在 1Password 中批准连接。如果你的手机显示 **1Password 只能在 Mac 上设置（1Password can only be set up on a Mac）**，说明新集成尚未到达你的账户；请改在电脑上从 Grok Bot 设置。要停止使用 1Password，在 **连接应用** 中打开它并选择 **断开连接（Disconnect）**。

当某个登录信息未保存在 Vault 中时，Bot 会在聊天中发送一张卡片，指明网站：

1. 选择 **在 1Password 中审查（Review in 1Password）**。1Password 应用会打开；如果那台电脑上没有安装该应用，1Password 会在浏览器中打开。
2. 在 1Password 中，选择要共享的具体登录信息并批准请求。
3. 1Password 在 Bot 的浏览器中填入登录信息。

你共享的登录信息在之后的聊天中仍然可用。如果 1Password 不再允许，Bot 会再次询问。1Password 不会填入支付卡，你的 Bot 仍会请你协助完成它无法填入的步骤，例如通行密钥、单点登录或验证码。

1Password 只提供你自己个人保险库（在 Family 账户中称为 Private）中的登录信息，不提供共享保险库中的。把该登录信息移动或复制到那个保险库，然后让 Bot 重试。如果完全没有出现批准提示，请把 1Password 应用更新到 8.12.42 或更高版本。

新集成不再使用服务账户，因此如果你以前在 Grok Bot 中使用过 1Password，请重新连接。你与旧集成共享的保险库中的登录信息，在你把它们移到个人或 Private 保险库之前不可用；**连接应用** 中的 1Password 页面会告诉你有多少个。在 Mac 上，你可以改为选择 **移到 Private（Move to Private）**，并在 1Password 提示时批准。旧保险库仍留在 1Password 中。

| 消息 | 该怎么做 |
| --- | --- |
| **1Password 连接未完成（1Password didn't finish connecting）** | 重新开始连接。在手机上，如果你已经有 1Password 账户，选择 **我已经有 1Password（I already have 1Password）** 并用它登录。 |
| **此 1Password 账户已连接到另一个 Grok Bot 账户（This 1Password account is already connected to another Grok Bot account）** | 先断开另一个 Grok Bot 账户上的 1Password，或连接一个不同的 1Password 账户。 |
| **需要重新连接（Reconnect required）** | 1Password 不再接受该连接。选择 **重新连接**。 |
| **登录你连接到 Grok Bot 的 1Password 账户，然后重试（Sign in to the 1Password account you connected to Grok Bot, then try again）** | 登录你连接的那个账户，然后让 Bot 重试。 |
| **你的 1Password 账户未开启访问请求（Access requests aren't turned on for your 1Password account）** | 请你的 1Password 管理员开启访问请求（access requests）。 |
| **此请求已在 1Password 中结束（This request already ended in 1Password）** | 让 Bot 重试。它会发送一个新请求。 |
| **无法打开 1Password（1Password could not be opened）** | 自己打开 1Password 应用来审查请求。 |
| 提示你在 1Password 的 **集成（Integrations）** 下撤销 Grok Bot 访问权限的消息 | 在 1Password 的 **集成** 下撤销 Grok Bot 的访问权限，然后重新连接 1Password。 |

### 已知应用问题

* **Zoom 错误 4700：** 目前从 Grok Bot 桌面应用进行 Zoom 授权会失败，错误为 4700（Invalid redirect）。尚无变通方法，你这边做任何更改都无法解决。
* **SharePoint AADSTS50011：** 当 Cursor 团队管理员从仪表盘的 **集成（Integrations）** 页面使用 **应用程序级权限（Application-level permissions）** 连接 SharePoint 时，Microsoft 会在同意提示之前显示重定向 URI 不匹配。这并非由你租户中的任何内容引起。请改用 **委派权限（Delegated permissions）** 连接：在 SharePoint 卡片上选择 **连接团队（Connect team）**（或 **重新连接**），选择 **委派权限**，输入你的 Microsoft 租户 ID，并使用 Microsoft 登录。大多数工作或学校租户需要 Microsoft 管理员一次性同意 Sites.Read.All。之后，每位成员在 Bot 首次使用 SharePoint 时用自己的 Microsoft 账户登录，并且只能看到其账户已经能打开的网站。如果成员看到「This team does not have the SharePoint integration」，则管理员需要完成委派登录。

更多设置帮助，见[连接应用](https://cursor.com/help/grok-bot/connect-apps)。

## 给你的 Bot 一个电子邮件地址

你可以在 `mail.grokbot.com` 认领一个电子邮件地址，例如 `yourname@mail.grokbot.com`，供你的 Bot 使用。你的 Bot 随后可以用它接收、读取、搜索和发送电子邮件。有了地址后，Bot 可以：

* 用自己的地址注册服务，并在你同意后取得验证码或链接
* 收集收据、简报和报告，并为你总结
* 为你起草电子邮件，例如摘要或更新，并起草回复
* 从收件箱转发电子邮件，保留原始格式、图像和附件；这需要 Grok Bot 0.75.2 或更高版本
* 在邮件到达时运行例程，可选仅针对特定发件人

要认领地址，请让 Bot 去做，例如「给你自己弄一个电子邮件地址」。它会询问你想要什么名称，检查该名称是否可用，并显示批准卡片；在你批准之前不会认领任何内容。你也可以打开 **连接应用**，选择 **电子邮件**，在 **电子邮件地址（Email address）** 下的 **选择一个名称（Choose a name）** 中输入名称，然后选择 **创建地址（Create address）**。在 iPhone 和 Android 上，打开 **设置 → 连接应用 → 电子邮件**。认领后，应用会显示你的地址，并带有一个复制按钮。

名称使用小写字母、数字、点、连字符和下划线，以字母或数字开头和结尾，最多 64 个字符。support、admin、billing、security、help、info、team、cursor、grok 和 xai 等保留词不允许使用。

你的地址也支持加号别名（plus alias）。发送到 `yourname+receipts@mail.grokbot.com` 的邮件会与 `yourname@mail.grokbot.com` 进入同一个收件箱，因此你可以为每个服务设置单独的别名，而无需再认领一个地址。Bot 也可以从别名发送；监视某个别名的例程只对发送到该别名的邮件运行，而监视普通地址的例程会对所有邮件运行。别名只是一个标签，不是锁：任何人都可以写信给它，因此对于只应针对特定发件人行动的例程，请保留发件人筛选。

* **一个地址，永久有效。** 你只能得到一个地址，且无法重命名或删除它。地址永远不会重新发放，即使认领它的账户被删除。
* **属于你，而不属于某个 Bot。** 你的所有 Bot 都可以在你自己的聊天和例程中使用该地址。它不会用于 Slack 线程或其他人正在与 Bot 交谈的聊天，[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)也没有团队地址。
* **读取邮件。** 任何人都可以往该地址发送邮件。未通过垃圾邮件或病毒扫描的邮件会被保留，但不含正文或附件，也绝不会启动例程。没有收件箱视图，也没有新邮件通知，因此请询问 Bot，例如「你的收件箱今天收到了什么？」最近一分钟内到达的邮件可能还无法在搜索中显示。每封来信最多可包含 10 个附件，每个最大 10 MB，总计最大 25 MB；超出这些限制的附件会被跳过。
* **对邮件采取行动。** 新邮件不会自行启动聊天或唤醒 Bot。要对它采取行动，请设置一个[例程](https://docs.x.ai/grok-bot/skills-routines-and-automations#trigger-work-from-an-event)，监视来自任何人、特定地址或整个域（例如 `*@example.com`）的邮件。默认情况下，例程只对通过标准电子邮件身份验证检查的发件人邮件运行，且例程无法按主题筛选。
* **发送邮件。** 当你在聊天中让 Bot 发送电子邮件时，一旦[自动审查（Auto Review）](https://docs.x.ai/grok-bot/approvals-security-and-privacy#configure-auto-review)允许，它就会发出；如果自动审查需要你，你会先看到批准卡片。来自例程，或来自你未以该请求启动的任何其他轮次的电子邮件，会作为草稿等待，直到你按下 **发送（Send）**，且没有无人值守发送的选项。如果你还连接了 Gmail 或 Outlook，当两者都可用时，Bot 会询问从哪个账户发送。
* **安全。** Bot 把来自其他人的电子邮件视为信息，而不是指令。它读取的每封邮件都会标明来自你还是来自其他人，电子邮件中的指令永远不会被视为你允许发送或采取行动。

发送限制：

* 每封电子邮件最多 50 个收件人，包括「收件人」「抄送」和「密送」
* 最多 10 个附件，每个最大 10 MB，总计最大 25 MB；不能附加可执行文件
* 简报和首次联系邮件每封只发一个收件人，并包含一键退订链接
* 如果邮件退信，或有人退订或将其标记为垃圾邮件，Bot 会停止向该地址发送邮件，并告诉你它跳过了谁
* 对 Bot 可以给多少个新联系人发邮件也有限制，以防止该地址被标记为垃圾邮件

如果你删除 Grok Bot 账户，你的邮件和附件会被删除，地址也会被停用。

在 Cursor 团队中，智能体电子邮件（agent email）默认关闭；管理员需先开启[智能体电子邮件（Agent Email）](https://docs.x.ai/grok-bot/teams-and-enterprises#agent-email)，成员才能认领地址。如果管理员之后将其关闭，Bot 会失去电子邮件工具，电子邮件例程停止运行，但发送到现有地址的邮件仍会被接收和保留，成员也保留其地址。

| 你看到的 | 该怎么做 |
| --- | --- |
| **此账户未启用智能体电子邮件（Agent email is not enabled for this account.）** | 你的账户尚不能使用智能体电子邮件。 |
| **你的团队管理员已关闭 Grok Bot 智能体电子邮件，因此此账户无法认领或使用智能体电子邮件地址（Your team admin has turned off Grok Bot agent email, so this account cannot claim or use an agent email address.）** | 请你的团队管理员开启 **智能体电子邮件**。 |
| **该地址已被占用，且地址永远不会重新发放，因此重试不会成功。请选择其他名称（That address is taken, and addresses are never reissued, so retrying it cannot succeed. Choose a different name.）** | 选择另一个名称。 |
| 关于允许字符、长度或保留词的消息 | 选择符合上述名称规则的名称。 |
| **你只能有一个智能体电子邮件地址（You can have one agent email address.）** | 你已经有一个地址。问你的 Bot 它是什么，或打开 **电子邮件** 应用。 |
| **无法创建你的电子邮件地址。请重试（Couldn't create your email address. Try again.）**（手机） | 检查名称规则，或在桌面端尝试，那里会显示确切原因。 |
| **过去一分钟检查的电子邮件地址过多（Too many email addresses checked in the last minute.）** | 等一分钟，然后重试。 |

## 搜索和阅读 X

无需你连接 X 账户，Bot 就可以搜索和阅读 X 上的公开内容。让 Bot 搜索帖子、通过链接打开帖子、读取某个账户的帖子和提及、查看谁引用了或转发了帖子、统计某个话题的近期帖子数，或查看趋势和新闻。

此访问是只读的，不会以你的身份登录。要访问你的私信、书签、主页时间线，或查看谁喜欢了你的帖子，请从 **连接应用** 添加 X 插件并用 X 登录。

## 处理文件

电脑在 `/workspace` 有一个共享工作区。把需要持久保留的项目文件放在那里，使用清晰的项目文件夹。

文件、浏览器状态和受支持的登录信息在正常的电脑更新和恢复后仍会保留。请把临时目录、手动安装的包和未提交的应用状态视为可替换的。把重要结果复制到共享工作区，或附加到对话中。

对话历史存储在电脑之外，因此在电脑内删除文件（包括 `rm -rf`）不会删除聊天。Grok Bot 会保留已同步电脑数据的持久副本，重新打开电脑时会从该副本恢复，因此已同步的文件通常能回来。`node_modules` 或 Python 虚拟环境等项目文件夹不会被保存；在电脑更新、**恢复（Recover）** 或 **重置（Reset）** 后请重新安装它们。只存在于你的 Mac 或 Windows 机器上的文件不在覆盖范围内，请为这些文件自备备份。

当电脑快满时，你的 Bot 会在聊天中告诉你一次，列出最大的文件或文件夹及其大小，并提出删除它们。除非你同意，否则不会删除任何内容。磁盘空间不足不是数据丢失，清理只针对电脑文件，不涉及聊天。

## 更新、恢复或重置电脑

从 **设置 → 电脑（Computer）** 下的 **Bot 的电脑（Bot's computer）** 打开电脑控制项。当应用提供时，你也可以从重新连接屏幕获取 **恢复**。应用和电脑分别更新。

| 操作 | 作用 | 保留 | 移除 |
| --- | --- | --- | --- |
| **更新（Update）** | 把电脑移到最新版本。有些更新只刷新 Grok Bot 的软件；其他更新会替换整台电脑，你可能可以安排这些更新稍后进行。**更新 Bot 的电脑（Update Bot's Computer）** 下方的文字会说明等待的是哪一种。 | 软件更新：所有内容，包括已安装的应用。电脑更新：Bot、文件和登录信息。 | 软件更新：无。电脑更新：已安装的应用和包。 |
| **恢复（Recover）** | 尽可能保存，然后用已保存的数据在最新版本上构建一台新电脑。正在运行的工作会被中断。 | 已保存的 Bot、文件和登录信息 | 已安装的应用和包，以及如果无法联系电脑进行保存而丢失的非常近期的更改 |
| **重置（Reset）** | 用你上次保存的数据在最新版本上构建一台新电脑。正在运行的工作会被中断。 | 已保存的 Bot、文件和登录信息 | 已安装的应用和包，以及如果无法联系电脑进行保存而丢失的非常近期的更改 |

对话存储在电脑之外，因此即使重置也能保留。如果 Bot 最近消失了，或保存失败，请在使用 **恢复** 或 **重置** 之前[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。

当无法联系电脑时，请从破坏性最小的选项开始：

1. 等待，然后如果电脑显示 **正在重新连接（Reconnecting）** 或 **无法连接 Grok Bot 的电脑（Couldn't Reach Grok Bot's Computer）**，选择 **重试（Retry）**，或重新打开对话。重新连接期间 Bot、文件和登录信息是安全的。在此期间不要 **重置**。
2. 完全退出 Grok Bot 再重新打开，并检查应用更新。在 Mac 上，从菜单栏选择 **退出（Quit）**，而不只是关闭窗口。
3. 如果有可用更新，在 **设置 → 电脑** 中使用 **更新 Bot 的电脑**。
4. 如果仍然无法重新连接，或更新看起来卡住并显示 **恢复电脑（Recover computer）**，选择 **恢复电脑**（确认对话框称之为 **恢复 Grok Bot 的电脑（Recover Grok Bot's Computer）**）。在更新缓慢时，**继续等待（Keep waiting）** 是安全的默认选项。
5. 仅在这些步骤之后才使用 **重置 Bot 的电脑（Reset Bot's Computer）**。

在已有更新或重置运行期间，不要启动第二个；重复重置可能中断仍在完成的恢复。**正在重新连接** 和 **恢复** 通常需要几分钟，你可以选择 **在后台继续（Continue in Background）**。**更新** 也可能需要几分钟；如果显示 **更新仍在运行（Update still running）**，请继续等待。如果 **恢复** 或 **重置** 失败，使用 **重试恢复（Retry Recovery）** 或 **重试重置（Retry Reset）** 一次，然后停止并[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。

如果电脑的文件尚未备份，**更新** 会说明它们尚未就绪，且不会有任何变化；请稍等片刻再重试，而不是重置。如果设置显示 **An agent couldn't pause in time, so the computer was not updated**，请让该 Bot 完成，然后再次选择 **更新**。

当电脑显示 **正在重新连接** 或 **无法连接 Grok Bot 的电脑** 时，Bot 无法完成一轮。请按上述步骤修复连接，然后重新发送消息。关于聊天丢失以及何时联系支持，见[故障排查](https://docs.x.ai/grok-bot/troubleshooting)。

## 你的本地电脑是独立的

Grok Bot 云端电脑与你面前的 Mac 或 Windows 电脑是分开的。只有当该能力已启用，且你根据本地电脑策略批准时，Bot 才会在你的本地电脑上运行命令：默认是 **每次询问（Ask every time）** 的逐命令批准，或者 **始终允许（Always allow）**、**从不允许（Never allow）**。该策略与管辖云端电脑工作的批准是分开的。

在[批准、安全与隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy#control-access-to-your-local-computer)中审查本地电脑权限。
