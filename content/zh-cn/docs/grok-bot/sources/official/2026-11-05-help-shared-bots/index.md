---
title: "帮助：共享 Bot"
linkTitle: "帮助：共享 Bot"
date: 2026-11-05
originalTitle: "Shared Bots"
sourceUrl: "https://cursor.com/help/grok-bot/shared-bots"
altUrls: ["https://docs.x.ai/grok-bot/shared-bots"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
updatedAt: 2026-11-10
dateNote: "文档不标日期，取收集日期；2026-11-10 发现原文更新，按新版覆盖原文存档：共享范围扩到整个组织，新增发布草稿、复制链接、浏览共享 Bot、学到的内容需审核、共享连接器等内容；旧译文对应 11-05 版，已移除，待重新翻译"
tags: [功能更新, 安全, 记忆与上下文]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Bot 分个人和共享两种，共享 Bot 像共享文档一样分享给团队、整个组织或指定的人和组，不会复制，每个人与它的对话保持私有，所有者和管理者也读不到；共享 Bot 总是在云端运行。它使用所有者添加的应用和秘密，在你自己的聊天里还可使用你的应用，但每次要先请求允许（允许一次、始终允许、跳过）。在你自己的聊天或 Slack 私信中它通常使用你的计算机，在 Slack 频道、线程、群聊中用自己的一台共享计算机；回复消耗被答复者的用量。风险动作的批准由被答复的那个人回答，Slack 线程里只有提问者能批准。管理员可设定只有管理员能共享 Bot；Bot 为团队学到的内容要经所有者或 Manager 审核；组织级共享时，Slack 工作区中未关联账号的成员也能在频道中使用，用量记在团队名下；只有所有者能删除共享 Bot，删除会让全队失去它及其对话和例程。手机端可用，但共享 Bot 不能成为主 Bot。

**保留理由**：讲清共享 Bot 的权限归属：谁的账号、谁的计算机、谁的用量、谁来批准，以及对话如何保持私有。

---

Bot 分为个人和共享两种。共享 Bot 就像共享文档一样：可以分享给你的 Cursor 团队、整个组织，或只分享给指定的人和组。共享不会复制 Bot，每个人与共享 Bot 的聊天都是私密的。

共享 Bot 总是在云端运行。运行在你自己的计算机上的 Bot 无法共享。应用在设置和少数消息中仍会显示 **Team Bots**，它们指的是同一件事。

## 谁可以使用共享 Bot？

共享 Bot 面向拥有 Grok Bot 的 Cursor 团队成员。在侧边栏选择 **+**，可以看到 **Create a Bot** 和 **Browse shared Bots**。如果没有 **Browse shared Bots**，说明你不在 Cursor 团队中，或者你的 Grok Bot 应用需要更新。

在 Slack 中，你工作区中不属于该团队的成员有时也能使用共享 Bot。参见[谁可以在 Slack 中与共享 Bot 对话？](#谁可以在-slack-中与共享-bot-对话)。

## 如何为我的团队创建 Bot？

1. 在侧边栏选择 **+**，再选择 **Create a Bot**，并给它起个名字。
2. 告诉这个 Bot 它应该帮助团队做什么。一句话就够了。
3. 按它的设置步骤配置应用、秘密、技能和文件。只添加你愿意让所有共享对象使用的密钥和文件。在你发布之前，它只是一个只有你能看到的草稿。
4. 当 Bot 表示可以共享时，选择 **Publish**。队友随后就能找到它。要更改谁有访问权限，参见[如何与我的团队共享 Bot？](#如何与我的团队共享-bot)。

你也可以共享已有的 Bot。共享不会复制它。共享之前，请检查它的应用、秘密、技能和文件，因为它们会在每位队友的聊天中生效。

## 如何与我的团队共享 Bot？

点击聊天顶部的 Bot 名称，选择 **Share**。在 **Share this Bot** 中：

- 在 **Who has access** 下，选择 **Only you**、**People you invite**、你的团队或你的组织。**People you invite** 只把 Bot 共享给你添加的人和组。限制访问时会要求你通过 **Limit access** 确认。所有者和 Manager 始终可以使用该 Bot。
- 选择 **Add people or groups** 添加成员。在 **Add as** 下，选择 **Collaborator** 让他们与 Bot 聊天，或选择 **Manager** 让他们还能更改 Bot 的工作方式：它的指令、技能、记忆和应用。
- 选择 **Copy link**，把 Bot 的链接发给队友。

要停止共享，再次打开 **Share** 并选择 **Only you**，或移除人们的访问权限。

## 谁可以共享 Bot？

默认情况下团队中的任何人都可以，除非管理员更改了设置。在团队仪表盘的 Grok Bot 页面中，**Sharing** 下的 **Bot sharing** 会设为 **Everyone** 或 **Admins only**。设为 **Admins only** 时，成员的 **Share** 会被禁用，并显示 **Only team admins can share Bots**。已经共享的 Bot 保持共享，其所有者和 Manager 仍可使用它们。请管理员替你共享 Bot，或更改该设置。参见[管理员如何管理共享 Bot？](#管理员如何管理共享-bot)。

## 队友如何找到共享 Bot？

- 在侧边栏选择 **+**，再选择 **Browse shared Bots**。列表会显示共享给你的 Bot，每个都标明创建者。选择 **Add** 把 Bot 留在你的侧边栏中。
- 在 Mac 上按 `Cmd+K`，在 Windows 上按 `Ctrl+K`，然后选择 **Browse shared Bots**。列表以 **Popular** Bot 开头，你可以搜索。
- 问你的 Bot 哪个共享 Bot 能帮忙做某件事。它会搜索你可以使用的共享 Bot，并推荐你尚未打开过的。
- 在手机上点按 **+**，再点按 **Browse shared Bots**。
- 打开队友发给你的链接，然后选择 **Start a chat**。

共享 Bot 的链接对所有人打开的是同一个 Bot。它不同于[共享 Bot 模板](https://cursor.com/docs/grok-bot/work#share-a-bot)，后者会给每个人一份自己的副本。

## 所有者能看到我与共享 Bot 的聊天吗？

不能。每个人与共享 Bot 的聊天都是私密的。所有者和 Manager 无法读取你的聊天，你也无法读取所有者或其他任何人的聊天。

Bot 可以为整个团队学习内容。它从某位队友那里学到的东西，要等所有者或 Manager 在 **Review learnings** 下批准。它不会为团队保存关于你个人的任何内容。它记住的关于与你合作的内容，只保留在你和 Bot 之间。参见[共享 Bot 会为团队学习什么？](https://cursor.com/help/grok-bot/memory#what-does-a-shared-bot-learn-for-the-team)。

## 共享 Bot 使用谁的应用和秘密？

共享 Bot 使用其所有者添加的应用和秘密。这些对每个与它聊天的人都一样。

在你与共享 Bot 自己的聊天中，它也可以使用你的应用。它使用你的某个个人账号前会先询问。卡片上会显示 **Allow**，然后是应用名称：

- **Allow once** 允许它这次使用该账号。
- **Always allow** 记住你的回答。它的菜单中有 **Always allow for your messages to this Bot** 和 **Always allow for your messages to every Team Bot**。
- **Skip** 表示它这次不使用该账号。

在 Slack 频道、线程和群聊中，共享 Bot 只使用其所有者的应用，并在使用你的账号前先询问。

已连接的账号以 Bot 正在答复的那个人的身份行事。某位队友的连接绝不会用于其他人，除非 Manager 把它作为共享连接器共享出来。

要让每个共享 Bot 都重新询问，打开 **Settings** > **General** > **Team Bots**，在 **Clear connector preferences** 旁选择 **Clear**。

## 共享连接器如何工作？

共享连接器让所有人通过一个账号使用某个应用，这样队友不必各自连接。所有者或 Manager 负责设置：打开 Bot 的详情，在 **Setup** 下选择 **Service accounts**。在 **Shared connectors** 下选择一个应用，然后选择 Bot 登录该应用的方式：

- **Use individual accounts**：每位队友连接自己的账号。
- **Share your account**：所有使用该 Bot 的人都通过你的账号行事，包括进行更改。请先为自己连接该应用，并且只共享不包含任何敏感或私密内容的账号。
- Bot 自己的账号：Bot 为团队使用的一个单独账号。有些应用尚不支持这种方式。

共享你的账号需要团队管理员先开启 **Allow Shared Logins**。在此之前，Bot 会显示 **Your admin has turned off sharing logins with Bots**。参见[管理员如何管理共享 Bot？](#管理员如何管理共享-bot)。

该应用所在行会显示 Bot 使用的是谁的账号。要停止，选择 **Stop sharing**，或移除该应用。之后队友会连接自己的账号。

## 共享 Bot 使用哪台计算机？

在你与队友的共享 Bot 自己的聊天中，Bot 通常在你的 Grok Bot 计算机上工作。这意味着它可以使用那里的文件，以及你在那里已登录的网站。有时它会为那次对话单独使用一台计算机，例如当你的隐私模式比所有者的更严格时。

当你在 Slack 中给共享 Bot 发私信时，它也在你自己的计算机上工作。在 Slack 频道、线程、群组私信和群聊中，共享 Bot 会使用它自己的一台共享计算机。

## 共享 Bot 聊天使用谁的用量付费？

共享 Bot 的回复使用它正在答复的那个人的 Grok Bot 用量。在你自己的聊天、Slack 和群聊中都是如此。你自己的限额适用。所有者的用量用于支付所有者自己的消息，以及来自未关联 Cursor 账号的应用或工作流的 Slack 帖子。在 Slack 中回复未关联账号或不属于该团队的人时，使用团队的用量。参见[套餐与计费](https://cursor.com/help/grok-bot/plans)。

## 共享 Bot 上的批准如何工作？

共享 Bot 在采取风险操作前会询问它正在答复的那个人。

- 在你与共享 Bot 自己的聊天中，由你回答它的批准卡片。
- 在 Slack 线程中，Bot 会发一张 **Review an action** 卡片，带有 **Allow once**、**Deny** 和 **View details**。只有提出问题的人可以回答。
- 在群聊中，只有 Bot 正在答复其消息的那个人可以回答。

它使用你的个人账号前也会先询问。参见[共享 Bot 使用谁的应用和秘密？](#共享-bot-使用谁的应用和秘密)。

## 如何把共享 Bot 添加到 Slack？

所有者或 Manager 在共享之后添加它：

1. 点击聊天顶部的 Bot 名称。
2. 找到 **Bring to your team's Slack**，选择 **Connect**。
3. 如果显示 **Awaiting admin approval**，需要由 Slack 工作区管理员批准该应用。

一旦显示 **Connected**，队友就可以直接给 Bot 发消息，或在频道中提及它。

在频道线程或私信中，共享 Bot 代表提及它的那位队友行事。它可以把手头的工作交给那个人自己的 Bot，那些 Bot 的回复会发回同一个线程。个人 Bot 不会从频道线程把工作交给其他 Bot。参见[Bot 可以从 Slack 给其他 Bot 发消息吗？](https://cursor.com/help/grok-bot/group-chats#can-a-bot-message-other-bots-from-slack)。

Bot 会记录它在 Slack 中发布的每条消息是谁请求的，因此线程中的任何人都可以问 Bot 是谁请求的。当共享 Bot 的例程在 Slack 线程中回复时，Bot 会跟进该线程，并在没有 @提及时回答后续回复。

队友第一次给 Bot 发消息时，会关联自己的 Slack 账号。参见[如何在 Slack 中与共享 Bot 聊天？](#如何在-slack-中与共享-bot-聊天)。

## 如何在 Slack 中与共享 Bot 聊天？

在频道中提及 Bot，或给它发私信。Bot 需要知道你是哪个 Cursor 账号才能与你聊天，因此第一次它会请你连接。

1. 选择 **Connect**。浏览器会打开 cursor.com。
2. 用与 Bot 所属团队匹配的 Cursor 账号登录，然后选择 **Link Account**。如果你已经登录，会直接进入该页面。
3. 选择 **Open Slack** 返回 Slack。如果你已在 Bot 所属团队中成功关联 Cursor 账号，Bot 会回答你发送的消息。

每个 Slack 工作区只需连接一次。该关联覆盖该工作区中的所有 Bot，以及你从 Slack 启动的 Cloud Agents。

你也可以在 Bot 询问之前先关联：

- 在桌面端，打开 **Settings** > **General** > **Team Bots**，选择 **Link**。
- 在 Cursor 仪表盘中，打开 [Integrations](https://cursor.com/dashboard/integrations?view=slack-management)，选择 Slack。
  - 如果你的工作区列在 **Workspaces** 下且未标记 **Connection expired**，说明已关联。
  - 如果你的工作区标记为 **Connection expired**，选择 **Reconnect**，然后在 Slack 的对话框中选择你的工作区并允许。
  - 如果列出了其他工作区但没有你的，选择 **Add to another workspace**，然后在 Slack 的对话框中选择你的工作区并允许。
  - 如果显示 **No Slack workspaces linked**，选择 **Install Cursor in Slack**，然后在 Slack 的对话框中选择你的工作区并允许。

连接之后，如果 Bot 没有共享给你，它仍然可以拒绝。参见[谁可以在 Slack 中与共享 Bot 对话？](#谁可以在-slack-中与共享-bot-对话)。

## 谁可以在 Slack 中与共享 Bot 对话？

这取决于 Bot 共享给了谁。

- **你的组织**：Slack 工作区的任何正式成员都可以在频道和线程中提及它，即使没有关联 Cursor 账号或团队席位。未关联账号的人会在每个线程中被告知一次 **some features will be limited**。在私信中，他们仍需要先连接。共享给团队的 Bot，如果该团队不在组织中，或是组织中唯一的团队，也适用同样的规则。
- **你的团队或指定的人**：只有共享对象可以使用。已关联账号但没有访问权限的队友会被告知该 Bot **hasn't been shared with you yet**。在 **Share this Bot** 下把他们添加进来。未关联账号的人会被要求连接账号。参见[如何在 Slack 中与共享 Bot 聊天？](#如何在-slack-中与共享-bot-聊天)。
- **个人 Bot** 只与其所有者聊天。

Slack 访客、Slack Connect 频道和其他 Slack 工作区永远不在范围内。如果你的 Slack 电子邮箱匹配某个已有访问权限的 Cursor 账号，Bot 会请你改为关联该账号。

团队管理员可以为不属于该团队的工作区成员关闭此功能。参见[管理员如何管理共享 Bot？](#管理员如何管理共享-bot)。

## 如何编辑或删除共享 Bot？

所有者和 Bot 的 Manager 可以更改共享 Bot。点击聊天顶部的 Bot 名称打开其详情，或选择右上角的扳手打开 **Bot settings**：

- **Plugins**（Bot 已连接的应用）、**Secrets**、**Skills** 和 **Files** 保存 Bot 为所有人使用的内容。
- 点击名称可以重命名 Bot。在 **About** 下编辑描述。
- **Share** 控制谁可以使用 Bot 以及谁管理它。

所有者还可以在侧边栏右键点击 Bot，选择 **Rename Bot** 来重命名。

只有所有者可以删除共享 Bot。在侧边栏右键点击 Bot，选择 **Delete**。团队管理员也可以从 Cursor 仪表盘的 **Manage Bots** 中删除它。这会为整个团队删除该 Bot。队友会失去它，以及他们在其上的聊天和例程。此操作无法撤销。

## 如何从侧边栏移除共享 Bot？

右键点击 Bot，选择 **Hide from sidebar**。要重新添加，在侧边栏选择 **+**，再选择 **Browse shared Bots**，然后选择它旁边的 **Add**。

如果你的管理员替你把它添加到了侧边栏，它的菜单中不会有 **Hide from sidebar**，你也无法移除它。

## 我可以在手机上使用共享 Bot 吗？

可以。你已添加的共享 Bot 会出现在手机应用中。要查找其他共享 Bot，点按 **+**，再点按 **Browse shared Bots**。你可以与共享 Bot 聊天，并回答它们的 **Allow** 卡片。共享 Bot 不能成为你的主 Bot。

在手机上共享和浏览需要 iPhone 和 Android 上来自 App Store 或 Google Play 的 Grok Bot 1.19.0 或更高版本。更早的版本仍会打开你列表中已有的共享 Bot，其中一些界面仍会显示 **Team Bots**。

## 我可以与队友的共享 Bot 语音聊天吗？

可以，在桌面端。在你与该 Bot 自己的聊天中，选择 **Start voice chat**。参见[与 Bot 语音聊天](https://cursor.com/help/grok-bot/voice-chat)。

## 共享 Bot 可以加入群聊吗？

可以。你可以把队友共享给你的 Bot 加入你自己的群聊。它不能与运行在你自己的计算机上的 Bot 共享同一个群组。参见[群聊与 Bot 之间的消息](https://cursor.com/help/grok-bot/group-chats)。

## 管理员如何管理共享 Bot？

在 [Cursor 仪表盘](https://cursor.com/dashboard/bot)的 Grok Bot 页面中，打开 **Shared Bots** 下的 **Manage Bots**。

- **Access** 显示谁可以使用每个共享 Bot。点击它可以更改谁可以使用该 Bot。
- **Auto-add** 会把 Bot 自动放入成员的侧边栏。选择 **All team** 或一个或多个组。这些成员无法隐藏它。自动添加只适用于有访问权限的组。
- 管理员也可以在这里删除共享 Bot。

在同一页面的 **Sharing** 下：

- **Bot sharing** 决定谁可以共享 Bot：**Everyone** 或 **Admins only**。已经共享的 Bot 保持共享。
- **Allow Shared Logins** 允许 Manager 把自己的应用登录信息作为[共享连接器](#共享连接器如何工作)共享。之后所有使用该 Bot 的人都通过该 Manager 的账号行事。它默认关闭。
- **Slack Workspace Access** 允许你 Slack 工作区中不属于该团队的成员使用共享给你组织的 Bot。它默认开启，在组织中会适用于每个团队。该设置会在到达你的团队时出现。

参见[面向 Teams 和 Enterprise 的 Grok Bot](https://cursor.com/docs/grok-bot/teams#manage-bots)。

## 为什么我看不到或无法使用共享 Bot？

| 你看到的内容 | 含义 |
| --- | --- |
| **+** 下没有 **Browse shared Bots** | 你不在 Cursor 团队中，或者你的 Grok Bot 应用需要更新。 |
| **Team Bots Not Available** | 你的账号没有共享 Bot 的访问权限。 |
| **Only team admins can share Bots** | 你的团队管理员把 Bot 共享限制为仅管理员。**Share** 被禁用，悬停时会显示该消息。请管理员替你共享 Bot，或更改团队仪表盘上的 **Bot sharing**。参见[谁可以共享 Bot？](#谁可以共享-bot)。 |
| **Bot Not Found** | 该 Bot 可能已被移除，或没有共享给你。 |
| **No Access to This Bot** | 该 Bot 只共享给指定的人。请向其所有者或 Manager 请求访问权限。 |
| 队友的 Bot 不在 **Browse shared Bots** 中 | 所有者还没有把它共享给你。 |
| **Your usage limit has been reached** | 你的 Grok Bot 用量已用完。你与队友的共享 Bot 的聊天使用你的用量。参见[套餐与计费](https://cursor.com/help/grok-bot/plans)。 |
| **This Bot's owner has reached their usage limit** | 这条回复计入了所有者的账号，而所有者的用量已用完。请所有者检查其套餐。 |
| **This conversation can't run on your computer because your privacy mode is stricter than the bot owner's.** | 你的隐私模式设置比所有者的更严格，因此这次聊天无法使用你的计算机。 |
| 在 Slack 中显示 **Connect your Grok account to chat with me** | 选择 **Connect**，用 Bot 所属团队的 Cursor 账号登录。Bot 随后会回答你发送的消息。参见[如何在 Slack 中与共享 Bot 聊天？](#如何在-slack-中与共享-bot-聊天)。 |
| 在 Slack 中，你已连接后 Bot 仍要求你连接 | 你用了另一个 Cursor 账号登录，或关联了另一个 Slack 工作区。在 **Settings** > **General** > **Team Bots** 下取消关联，然后用 Bot 所属团队的账号重新选择 **Connect**。 |
| 在 Slack 中显示 **some features will be limited** | Bot 在未关联账号的情况下回答了你。关联一个账号，让它知道你是谁并能使用你的应用。 |
| 在 Slack 中显示 **I haven't been shared with you yet** | 请 Bot 的所有者或 Manager 在 **Share this Bot** 下把你添加进来。 |
| 在 Slack 中，Bot 说它是某人的个人 Bot | 只有其所有者可以与它聊天。 |
| **Your admin has turned off sharing logins with Bots** | 团队管理员需要先开启 **Allow Shared Logins**，Manager 才能把账号作为共享连接器共享。 |

如果以上都不符合，请带上 Bot 名称、确切的消息和你使用的 Grok Bot 版本，[联系支持](https://cursor.com/help/grok-bot/get-help)。
