---
title: "帮助：连接应用"
linkTitle: "帮助：连接应用"
date: 2026-11-05
originalTitle: "Connect apps"
sourceUrl: "https://cursor.com/help/grok-bot/connect-apps"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [连接器, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：应用让 Bot 使用外部服务，连接属于登录 Grok Bot 的同一账号，Bot 只能做该账号本来就能做的事，不能提升权限。添加方法是在侧边栏「Connect apps」中授权并在浏览器完成登录；团队管理员可禁用某些应用，显示「Disabled by team admin」。连接 Google 系应用时，Grok Bot 以「Grok」而非 Cursor 的名义登录，公司 Google 管理员需先在 API 控制里将 Grok 设为受信任；Microsoft 365 同样需管理员批准。文中逐个说明 Google Calendar、Sheets、Slack、Gmail、X、Power BI（只读）、BigQuery、Databricks Genie、Asana、Vanta、Shop Pay 的能力与限制，Gmail 同一时间只能连一个邮箱。1Password 集成需批准每次登录，Bot 看不到值，不填支付卡，只提供个人保险库里的登录。文末列出两个已知问题：Zoom 授权报错 4700、SharePoint 应用级权限报错 AADSTS50011，目前无解或只能改用委托权限。

**保留理由**：列出各连接器的具体能力、管理员批准流程和已知问题，对研究连接器的权限边界和落地摩擦有用。

---

连接 Gmail、Notion、Slack、1Password 和其他应用，让你的 Bot 可以在聊天中使用它们。

## 什么是应用？

应用让 Bot 能够使用外部服务。应用连接属于你登录 Grok Bot 时使用的**同一账户**。

**电子邮件（Email）** 应用不同：它让每个 Bot 拥有自己的电子邮件地址，而不是连接你已有的账户。见[给你的 Bot 一个电子邮件地址](https://cursor.com/help/grok-bot/agent-email)。

## 如何添加应用？

1. 在 Grok Bot 中，在侧边栏选择 **连接应用（Connect apps）**，或点击聊天内的 **连接（Connect）** 卡片。在 Grok Bot 移动应用中，点击左上角的头像并选择 **连接应用**。
2. 浏览或搜索该应用，然后添加。
3. 当 Grok Bot 要求你 **授权（Authorize）** 或 **验证身份（Authenticate）** 时，在浏览器中完成提供方的登录。
4. 如果登录没有完成，在应用上选择 **重新连接（Reconnect）**，或在聊天内卡片上选择 **重新打开（Reopen）**，把登录页面带回来。
5. 确认该应用出现在 **已安装（Installed）** 下。

## 为什么某个应用显示「已被团队管理员禁用（Disabled by team admin）」？

如果你通过 Cursor 团队使用 Grok Bot，你的 Cursor 团队管理员控制哪些应用可用。如果某个应用被禁用，请让管理员启用它。

该 Cursor 控制与公司 Google 管理员是分开的。Google 的阻止使用下一节中的界面。

## 如果 Google 说管理员需要审核 Grok 怎么办？

公司 Google 账户可以在 Gmail、Calendar、Drive、Docs、Sheets、Slides 或 BigQuery 完成登录之前阻止连接。Grok Bot 以 **Grok** 的身份登录 Google，而不是 Cursor。由 Google 页面决定下一步。

**你的管理员需要审核 Grok（Your admin needs to review Grok）**

Grok 尚未获得该 Workspace 的批准。如果 Google 页面上有请求访问按钮，请申请访问。等管理员批准 Grok 后，再尝试 **授权**。

IT 管理员在 Google 管理控制台中批准 **Grok**：

1. 打开 **安全（Security）**，然后 **访问和数据控制（Access and data control）**，再打开 **API 控制（API controls）**。
2. 打开 **应用访问控制（App access control）**，然后 **管理第三方应用访问（Manage third-party app access）**。
3. 添加名为 **Grok** 的应用。如果按名称搜索找不到，请使用被阻止页面或管理员审核邮件中的客户端 ID。
4. 为使用 Grok Bot 的人员把 Grok 设置为 **受信任（Trusted）**。

该批准只覆盖这些人连接的 Google 应用。它不会在 Cursor 中重新启用应用。Cursor 团队管理员通过上面的 **已被团队管理员禁用** 控制来做这件事。

**访问被阻止（Access blocked）**

Google 拒绝了登录。个人 Gmail 账户不需要公司管理员。公司账户在 Grok 不在允许列表中，或管理员已阻止第三方应用时，常会遇到这种情况。

请 Google 管理员按上述步骤信任 **Grok**。如果之后页面仍显示访问被阻止，请带上 Google 账户电子邮件和被阻止页面的截图[联系支持](https://cursor.com/help/grok-bot/get-help)。更换浏览器或重新连接应用不会解除 Google 管理员的阻止。

## 如果 Microsoft 说管理员需要批准 Grok Bot 怎么办？

工作或学校的 Microsoft 365 账户可以阻止 **Outlook**、**Outlook Calendar**、**OneDrive** 或 **Teams** 连接，直到组织的 Microsoft 365 管理员批准该应用。重试登录或再次允许权限都没有用。

- 在电脑上，登录页面显示 **你的组织的 Microsoft 365 管理员需要先批准此应用，你才能连接（Your organization's Microsoft 365 admin needs to approve this app before you can connect）**，并显示 **给你的 IT 管理员的批准链接（Approval link for your IT admin）**。把该链接发给你的 IT 管理员。他们批准后，再从 Grok Bot 连接。
- 在 1.19.0 或更高版本的手机应用中，连接卡显示相同内容，并补充 **请你的 IT 管理员批准 Grok Bot，然后重新连接（Ask your IT admin to approve Grok Bot, then connect again）**。手机不显示批准链接，因此如果你的管理员需要它，请先从电脑连接一次以获取。

如果页面改为显示该应用 **被你的组织阻止（blocked by your organization）**，则管理员必须允许该连接。页面会列出连接器、Microsoft Entra 应用程序 ID、错误代码和时间，供你发送给他们。

## 为什么手机提示要在电脑上连接应用？

有些提供方无法从手机浏览器完成登录。在 1.19.0 或更高版本的手机应用中，**Adapter**、**Robinhood** 和 **Intercom** 的 **连接（Connect）**，以及 iPhone 上的 **Postiz**，会显示 **在电脑上连接（Connect on your computer）**，而不是打开登录页面。在电脑上打开 Grok Bot 并在那里连接该应用。之后该连接在你的手机上也能用，因为应用属于你的账户，而不是设备。

**Slack** 仍可在手机上登录。如果你在完成前关闭其登录，手机会提醒你 Slack 的手机登录需要你的工作区密码，并且你可以改从电脑连接 Slack。

## 已连接的应用能做什么？

应用使用你授权的账户。它只能做该账户在该服务中已经能做的事。它不能提升你的访问权限，也不能更改共享设置。

**Google Calendar**

bot 可以读取你能看到的日历、创建和更新事件、查看空闲时间，并在你可编辑的日历上回复邀请。

它不能更改 Google Meet 设置，例如等候室或主持人控制。它也不能向事件添加 Zoom 链接。从 Calendar 网站添加 Zoom 链接使用的是 Google 的 Zoom 附加组件，而该应用无法使用这个附加组件。请自己把 Zoom 链接放入事件地点或描述，或者在 Calendar 中创建事件，再让 bot 更新其他字段。

**Google Sheets**

连接 Sheets 后，bot 可以读取和编辑已连接 Google 账户可编辑的电子表格中的单元格。以查看者（Viewer）身份共享的文件仍然只读。该应用不能更改谁有访问权限。

查找和打开文件使用 **Google Drive** 应用。Drive 可以搜索并读取该账户能打开的文件。编辑单元格内容使用 **Google Sheets**。

**Slack**

Slack 应用以你连接的 Slack 用户身份发帖，而不是作为一个需要被邀请的独立 bot。它只能在该用户可发帖的频道中发帖。它不能在该用户不在的私密频道中发帖，也不能在工作区禁止发帖的频道中发帖。要使用另一个 Slack 工作区，请连接该工作区。这与启动例程的 Slack 消息是两回事。见[例程](https://cursor.com/help/grok-bot/routines#how-do-slack-triggers-work)。

**Gmail**

Gmail 可以在已连接的邮箱中搜索和读取邮件、起草和发送邮件，以及应用标签。

**X**

X 插件需要你的 X 开发者账户中有 X API 额度。见[如果 X 插件已连接但书签、私信或时间线失败怎么办？](https://cursor.com/help/grok-bot/how-to#what-if-the-x-plugin-is-connected-but-bookmarks-dms-or-the-timeline-fail)。

**Microsoft Power BI**

Power BI 使用工作或学校 Microsoft 账户连接。个人 Microsoft 账户无法连接它。bot 可以列出工作区、报表和数据集，并把报表或其某一页渲染为图片。每个 Power BI 工具都是只读的。渲染需要工作区处于 Premium、Embedded 或 Fabric 容量，并且 Power BI 租户设置 **将报表导出为图片文件（Export reports as image files）** 已开启。

**Google BigQuery**

BigQuery 与其他 Google 应用一样，以 **Grok** 的身份登录 Google，因此公司 Google 的阻止会使用[如果 Google 说管理员需要审核 Grok 怎么办？](#what-if-google-says-an-admin-needs-to-review-grok)中的界面。bot 查询已连接 Google 账户可读取的数据集。Cursor 团队管理员可以在仪表盘 [Plugins & MCPs 页面](https://cursor.com/dashboard/plugins)上该插件的团队设置中输入团队自己的 Google OAuth 客户端 ID 和密钥；成员随后改用该客户端登录。

**Databricks Genie**

Databricks Genie 需要 Cursor 团队管理员先设置好，成员才能连接。管理员在 Databricks 账户中注册 OAuth 应用连接，然后在仪表盘 [Plugins & MCPs 页面](https://cursor.com/dashboard/plugins)上该插件的团队设置中输入工作区 URL、客户端 ID 和客户端密钥（公共客户端留空）。之后每位成员用自己的 Databricks 账户登录，bot 针对该账户可查询的数据用自然语言向 Genie 提问。

**Asana**

Asana 不需要管理员设置。用你的 Asana 账户登录，bot 就会在该账户能打开的工作区和项目中工作。

**Vanta**

Vanta 将每个账户保存在一个区域。首次从 **连接应用** 连接 Vanta 时，在登录时选择你的 Vanta 账户所在区域：**United States**、**Europe** 或 **Australia**。在错误区域登录找不到你的账户；请重新登录并选择另一个区域。

**Shop Pay**

Shop Pay 是一个钱包。连接它并登录 Shop 后，bot 可以在 Shopify 商店中使用 Shop Pay 结账，与保存在 [Vault](https://cursor.com/help/grok-bot/secrets#what-is-vault)、Link 或 X Money 中的卡并列。关于 bot 如何在结账时付款，见[接管敏感步骤](https://cursor.com/docs/grok-bot/work#take-over-for-sensitive-steps)。

## 我能连接两个 Gmail 账户吗？

不能。Gmail 一次连接一个邮箱。要使用另一个 Gmail 邮箱，请断开当前邮箱并授权另一个。你不能让个人邮箱和工作邮箱同时连接到 Gmail。

已连接的应用对该 Grok Bot 账户上的每个 bot 可用。如果某个 bot 不应使用该邮箱，请断开 Gmail。队友的[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)在使用你的账户前会先询问。

某些其他应用（例如 Notion）可以连接第二个账户。见[如何为同一个应用添加第二个账户？](https://cursor.com/help/grok-bot/how-to#how-do-i-add-a-second-account-for-the-same-app)

## 应用已添加，但 Bot 说缺少它。我该怎么办？

**已添加（Added）** 表示应用已安装，并不意味着你已登录。如果它显示 **需要验证（Needs auth）** 或 **已断开（Disconnected）**，请打开该应用并选择 **验证身份（Authenticate）**（手机上为 **授权（Authorize）**）。对于始终不出现或毫无反应的连接卡，见[如何重新连接应用？](https://cursor.com/help/grok-bot/how-to#how-do-i-reconnect-an-app)

## 如何连接 1Password？

1Password 让你的 Bot 使用你 1Password 账户中的登录信息，在其计算机上登录网站。你在 1Password 中批准每次登录，由 1Password 填入。你的 Bot 永远看不到这些值。

新的 1Password 集成正在逐步推出。它适用于个人和 Family 1Password 账户，需要 1Password 8.12.42 或更高版本。

1. 选择 **连接应用**，打开 **1Password**。它在 **密码管理器（Password Managers）** 下。
2. 在电脑上，选择 **连接 1Password（Connect 1Password）**。
3. 浏览器会打开。在那里登录 1Password 并批准 Grok Bot。完成后 Grok Bot 会更新。

在手机上，从 **连接应用** 的 **密码管理器** 栏打开 1Password，或搜索它，然后在 1Password 中批准连接。

如果你的手机显示 **1Password 只能在 Mac 上设置（1Password can only be set up on a Mac）**，说明新集成尚未到达你的账户。请改在电脑上从 Grok Bot 设置 1Password。

要停止使用 1Password，在 **连接应用** 中打开它并选择 **断开连接（Disconnect）**。你的 Bot 会停止使用你的 1Password 登录信息，直到你再次连接。

## 我的 Bot 如何用 1Password 登录？

你的 Bot 会先检查 [Vault](https://cursor.com/help/grok-bot/secrets#what-is-vault)。当某个登录信息未保存在那里时，Bot 会在聊天中发送一张卡片，指明网站。

1. 选择 **在 1Password 中审查（Review in 1Password）**。1Password 应用会打开。如果那台计算机上没有安装该应用，1Password 会在浏览器中打开。
2. 在 1Password 中，选择要共享的具体登录信息并批准请求。
3. 1Password 在 Bot 的浏览器中填入登录信息。

你共享的登录信息在之后的聊天中仍然可用。如果 1Password 不再允许，Bot 会再次询问。

1Password 不会填入支付卡。你的 Bot 仍会请你协助完成 1Password 无法填入的步骤，例如通行密钥（passkey）、单点登录（single sign-on），或它无法通过的验证码（captcha）。

## 为什么 1Password 不提供我想要的登录信息？

1Password 只提供你自己个人保险库（Personal vault，在 Family 账户中称为 Private）中的登录信息。它不提供共享保险库中的登录信息。在 1Password 应用中，把该登录信息移动或复制到那个保险库，然后让 Bot 重试。

如果完全没有出现批准提示，请检查你的 1Password 应用是否为 8.12.42 或更高版本，如果不是请更新。

## 我以前在 Grok Bot 中使用过 1Password。为什么需要重新连接？

新的 1Password 集成不再使用服务账户。请按[如何连接 1Password？](#how-do-i-connect-1password)中的步骤重新连接 1Password。

你与旧集成共享的保险库中的登录信息，在你把它们移走之前，Grok Bot 无法使用。**连接应用** 中的 1Password 页面会告诉你有多少个。在 1Password 中，选择这些登录信息并把它们移到你的 Personal 或 Private 保险库。在 Mac 上，你可以改为选择 **移到 Private（Move to Private）**，并在 1Password 提示时批准。旧保险库仍留在 1Password 中。

## Grok Bot 中的 1Password 消息是什么意思？

| 消息 | 该怎么做 |
| --- | --- |
| **1Password 连接未完成（1Password didn't finish connecting）** | 重新开始连接。在手机上，如果你已经有 1Password 账户，选择 **我已经有 1Password（I already have 1Password）** 并用它登录。 |
| **此 1Password 账户已连接到另一个 Grok Bot 账户（This 1Password account is already connected to another Grok Bot account）** | 先断开另一个 Grok Bot 账户上的 1Password，或连接一个不同的 1Password 账户。 |
| **需要重新连接（Reconnect required）** | 1Password 不再接受该连接。选择 **重新连接（Reconnect）**。 |
| **登录你连接到 Grok Bot 的 1Password 账户，然后重试（Sign in to the 1Password account you connected to Grok Bot, then try again）** | 1Password 已退出登录，或登录到了另一个账户。登录你连接的那个账户，然后让 Bot 重试。 |
| **你的 1Password 账户未开启访问请求（Access requests aren't turned on for your 1Password account）** | 请你的 1Password 管理员开启访问请求。 |
| **此请求已在 1Password 中结束（This request already ended in 1Password）** | 让 Bot 重试。它会发送一个新请求。 |
| **无法打开 1Password（1Password could not be opened）** | 自己打开 1Password 应用来审查请求。 |
| 提示你在 1Password 的 **集成（Integrations）** 下撤销 Grok Bot 访问权限的消息 | 在 1Password 的 **集成** 下撤销 Grok Bot 的访问权限，然后重新连接 1Password。 |

## 为什么连接 Zoom 时在授权过程中失败，报错 4700？

这是一个已知问题，我们的工程师正在修复。目前从 Grok Bot 桌面应用进行 Zoom 授权会失败，错误为 4700（Invalid redirect），你这边做任何更改都无法解决。

目前没有变通方法。等 Zoom 可以连接后，我们会更新本文。

## 为什么 SharePoint 管理员同意会因重定向 URI 错误（AADSTS50011）失败？

这是一个已知问题，我们的工程师正在修复。当 Cursor 团队管理员从仪表盘 **集成（Integrations）** 页面连接 SharePoint 并选择 **应用程序级权限（Application-level permissions）** 时，Microsoft 会在同意提示之前显示 AADSTS50011（重定向 URI 不匹配）。错误中提到的 Microsoft 应用属于 Grok，而不是你的组织，因此这不是你的租户中的任何东西导致的，Entra 管理中心里的任何更改也无法清除它。

变通方法：改用 **委派权限（Delegated permissions）** 连接。

1. 在 Cursor 仪表盘中，打开 **集成**，找到 SharePoint 卡片。
2. 选择 **连接团队（Connect team）**（如果你已经开始设置，则选择 **重新连接（Reconnect）**），然后选择 **委派权限**。
3. 输入你的 Microsoft 租户 ID（例如 contoso.onmicrosoft.com，或 Microsoft Entra ID > 概览中的 GUID）。
4. 使用 Microsoft 登录。大多数工作或学校租户需要 Microsoft 管理员一次性同意 Sites.Read.All。
5. 每位团队成员在 bot 首次使用 SharePoint 时用自己的 Microsoft 账户登录。他们只能看到其账户已经能打开的网站。

如果你开始的是应用程序级设置，而成员现在看到「This team does not have the SharePoint integration」，则管理员需要完成上面的委派登录。在该 Microsoft 步骤完成之前，应用一直不可用。

当应用程序级权限可以批准时，我们会更新本文。
