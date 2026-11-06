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
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [功能更新, 安全, 记忆与上下文]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Bot 分个人和共享两种，共享 Bot 像共享文档一样分享给整个团队或指定的人和组，不会复制，每个人与它的对话保持私有，所有者和管理者也读不到；共享 Bot 总是在云端运行。它使用所有者添加的应用和秘密，在你自己的聊天里还可使用你的应用，但每次要先请求允许（允许一次、始终允许、跳过）。在你自己的聊天或 Slack 私信中它通常使用你的计算机，在 Slack 频道、线程、群聊中用自己的一台共享计算机；回复消耗被答复者的用量。风险动作的批准由被答复的那个人回答，Slack 线程里只有提问者能批准。管理员可在控制台设置谁可使用、是否自动加入侧边栏，只有所有者能删除共享 Bot，删除会让全队失去它及其对话和例程。手机端可用，但共享 Bot 不能成为主 Bot。

**保留理由**：讲清共享 Bot 的权限归属：谁的账号、谁的计算机、谁的用量、谁来批准，以及对话如何保持私有。

---

Bot 分为个人（personal）和共享（shared）两种。把 Bot 分享给 Cursor 团队的方式，就像分享文档一样：可以分享给团队里的每个人，也可以只分享给特定的人和组。分享不会产生副本，每个人与共享 Bot 的对话都是私密的。

共享 Bot 始终在云端运行。在自己计算机上运行的 Bot 无法共享。

## 谁可以使用共享 Bot？

共享 Bot 面向拥有 Grok Bot 的 Cursor 团队成员。在侧边栏选择 **+**，可以看到 **Create a Bot** 和 **Browse shared Bots**。如果没有 **Browse shared Bots**，说明你不在 Cursor 团队中，或者你的 Grok Bot 应用需要更新。

## 我如何为团队创建一个 Bot？

1. 在侧边栏选择 **+**，然后选择 **Create a Bot**，并给它起个名字。
2. 告诉这个 Bot 它应该帮团队做什么。一句话就够了。
3. 按照它的设置步骤配置应用（apps）、机密（secrets）、技能（skills）和文件（files）。只添加你愿意让所有共享对象使用的密钥和文件。
4. 分享它。参见[我如何与团队共享 Bot？](#how-do-i-share-a-bot-with-my-team)

你也可以共享已有的 Bot。共享不会复制它。共享前，请检查它的应用、机密、技能和文件，因为它们会在每位队友的对话中生效。

## 我如何与团队共享 Bot？

点击对话顶部的 Bot 名称，然后选择 **Share**。在 **Share this Bot** 中：

- 在 **Who has access** 下，选择你的团队可将 Bot 共享给团队中的每个人，或选择 **People you invite** 只共享给你添加的人和组。限制访问范围时会要求你通过 **Limit access** 确认。所有者和 Manager（管理者）始终可以使用该 Bot。
- 选择 **Add people or groups** 添加人员。在 **Add as** 下，选择 **Collaborator** 让他们能与该 Bot 对话，或选择 **Manager** 让他们还能更改它的工作方式：它的指令、技能、记忆和应用。

要停止共享，再次打开 **Share** 并移除访问权限。

## 队友如何找到共享 Bot？

- 在侧边栏选择 **+**，然后选择 **Browse shared Bots**。列表显示共享给你的 Bot，每个都会显示制作者。选择 **Add** 可将某个 Bot 保留在侧边栏。
- 在手机上，点按 **+**，然后点按 **Browse shared Bots**。
- 打开队友发给你的链接，然后选择 **Start a chat**。

共享 Bot 的链接对每个人打开的是同一个 Bot。这与[共享 Bot 模板](https://cursor.com/docs/grok-bot/work#share-a-bot)不同，后者会给每个人各自的副本。

## 所有者能看到我与共享 Bot 的对话吗？

不能。每个人与共享 Bot 的对话都是私密的。所有者和 Manager 无法读取你的对话，你也无法读取所有者或其他任何人的对话。

该 Bot 可以把它学到的东西保存下来供整个团队使用，并在这样做时告诉你。它不会把关于你个人的任何内容保存给团队。它记住的与你共事的内容只存在于你和该 Bot 之间。

## 共享 Bot 使用谁的应用和机密？

共享 Bot 使用其所有者添加的应用和机密。这些对每个与它对话的人都一样生效。

在你与共享 Bot 自己的对话中，它也可以使用你的应用。在使用你的某个个人账号之前，它会先询问。卡片上写着 **Allow**，后面是应用名称：

- **Allow once** 允许它这一次使用该账号。
- **Always allow** 会记住你的选择。它的菜单中有 **Always allow for your messages to this Bot** 和 **Always allow for your messages to every Shared Bot**。
- **Skip** 表示它这一次不使用该账号。

在 Slack 频道、线程和群聊中，共享 Bot 只使用其所有者的应用，并在使用你的账号前先询问。

已连接的账号始终代表该 Bot 正在答复的那个人行事。一位队友的连接绝不会被用于其他人。

要让每个共享 Bot 都重新询问，请打开 **Settings** > **General** > **Shared Bots**，然后在 **Clear connector preferences** 旁选择 **Clear**。

## 共享 Bot 使用哪台计算机？

在你与队友共享 Bot 自己的对话中，该 Bot 通常在你的 Grok Bot 计算机上工作。这意味着它可以使用那里的文件以及你在那里已登录的网站。有时它会为那次对话单独使用一台计算机，例如当你的隐私模式比所有者的更严格时。

当你在 Slack 中私信共享 Bot 时，它也在你自己的计算机上工作。在 Slack 频道、线程、群组私信和群聊中，共享 Bot 使用它自己的一台共享计算机。

## 共享 Bot 对话消耗谁的用量？

共享 Bot 的回复消耗它所答复的那个人的 Grok Bot 用量。在你自己的对话、Slack 和群聊中都是如此。你自己的限额适用。所有者的用量支付所有者自己发送的消息，以及未关联 Cursor 账号的应用或工作流发布的 Slack 帖子。参见[套餐与计费](https://cursor.com/help/grok-bot/plans)。

## 共享 Bot 的批准如何运作？

共享 Bot 在执行风险动作前会询问它正在答复的那个人。

- 在你与共享 Bot 自己的对话中，你回答它的批准卡片。
- 在 Slack 线程中，该 Bot 会发布一张 **Review an action** 卡片，带有 **Allow once**、**Deny** 和 **View details**。只有提问者能回答。
- 在群聊中，只有 Bot 正在答复其消息的那个人能回答。

它在使用你的个人账号前也会先询问。参见[共享 Bot 使用谁的应用和机密？](#whose-apps-and-secrets-does-a-shared-bot-use)

## 如何把共享 Bot 添加到 Slack？

所有者或 Manager 在共享之后添加它：

1. 点击对话顶部的 Bot 名称。
2. 找到 **Bring to your team's Slack**，选择 **Connect**。
3. 如果显示 **Awaiting admin approval**，则需要一位 Slack 工作区管理员批准该应用。

一旦显示 **Connected**，队友就可以直接给该 Bot 发消息，或在频道中提及它。

在频道线程或私信中，共享 Bot 代表提及它的那位队友行事。它可以把工作交给那个人自己的 Bot，而它们的回复会发回同一线程。个人 Bot 不会从频道线程把工作交给其他 Bot。参见[Bot 能从 Slack 给其他 Bot 发消息吗？](https://cursor.com/help/grok-bot/group-chats#can-a-bot-message-other-bots-from-slack)

Bot 会记录它在 Slack 中发布的每条消息是谁请求的，因此线程中的任何人都可以问该 Bot 是谁请求的。当共享 Bot 的例程（routine）在 Slack 线程中回复时，该 Bot 会跟进该线程，并在没有 @提及 的情况下回答后续回复。

每位队友都需要先关联自己的 Slack 账号。打开 **Settings** > **General** > **Shared Bots** 并选择 **Link**。如果你在关联前给该 Bot 发消息，它会回复关联账号的步骤。

## 如何编辑或删除共享 Bot？

所有者和该 Bot 的 Manager 可以更改共享 Bot。点击对话顶部的 Bot 名称打开其详情，或选择右上角的扳手打开 **Bot settings**：

- **Plugins**（该 Bot 连接的应用）、**Secrets**、**Skills** 和 **Files** 保存该 Bot 供所有人使用的内容。
- 点击名称可重命名该 Bot。在 **About** 下编辑描述。
- **Share** 控制谁可以使用该 Bot 以及谁管理它。

所有者还可以在侧边栏右键点击该 Bot，选择 **Rename Bot** 来重命名。

只有所有者可以删除共享 Bot。在侧边栏右键点击该 Bot，选择 **Delete**。这会为你的整个团队删除该 Bot。队友会失去它，以及他们在它上面的对话和例程。此操作无法撤销。

## 如何从侧边栏移除共享 Bot？

右键点击该 Bot，选择 **Hide from sidebar**。要重新添加，在侧边栏选择 **+**，然后选择 **Browse shared Bots**，并在它旁边选择 **Add**。

如果你的管理员替你将该 Bot 添加到了侧边栏，它的菜单中就没有 **Hide from sidebar**，你也无法移除它。

## 我可以在手机上使用共享 Bot 吗？

可以。你已添加的共享 Bot 会出现在手机应用中。要查找其他共享 Bot，点按 **+**，然后点按 **Browse shared Bots**。你可以与共享 Bot 对话并回答它们的 **Allow** 卡片。共享 Bot 不能成为你的主 Bot。

在手机上共享和浏览需要 iPhone 和 Android 上来自 App Store 或 Google Play 的 Grok Bot 1.19.0 或更高版本。更早的版本仍可打开你列表中已有的共享 Bot，其中一些界面仍显示 **Team Bots**。

## 我可以与队友的共享 Bot 语音聊天吗？

可以，在桌面端。在你与该 Bot 自己的对话中，选择 **Start voice chat**。参见[与 Bot 语音聊天](https://cursor.com/help/grok-bot/voice-chat)。

## 共享 Bot 可以加入群聊吗？

可以。你可以把队友共享给你的 Bot 添加到你自己的群聊中。它不能与运行在你自己计算机上的 Bot 共处一个群。参见[群聊与 Bot 之间的消息](https://cursor.com/help/grok-bot/group-chats)。

## 管理员如何管理共享 Bot？

在 [Cursor 控制台](https://cursor.com/dashboard/bot)的 Grok Bot 页面上，打开 **Shared Bots** 下的 **Manage Shared Bots**。

- **Access** 显示谁可以使用每个共享 Bot。点击它可以更改谁可以使用该 Bot。
- **Auto-add** 会把该 Bot 自动放入成员的侧边栏。选择 **All team** 或一个或多个组。这些成员无法隐藏它。自动添加只适用于有访问权限的组。

参见[面向 Teams 和 Enterprise 的 Grok Bot](https://cursor.com/docs/grok-bot/teams#manage-shared-bots)。

## 为什么我看不到或无法使用共享 Bot？

| 你看到的内容 | 含义 |
| --- | --- |
| **+** 下没有 **Browse shared Bots** | 你不在 Cursor 团队中，或者你的 Grok Bot 应用需要更新。 |
| **Shared Bots Not Available** | 你的账号没有共享 Bot 的访问权限。 |
| **Bot Not Found** | 该 Bot 可能已被移除，或者没有共享给你。 |
| **No Access to This Bot** | 该 Bot 只共享给特定的人。向它的所有者或 Manager 申请访问权限。 |
| 队友的 Bot 不在 **Browse shared Bots** 中 | 所有者还没有把它共享给你。 |
| **Your usage limit has been reached** | 你的 Grok Bot 用量已用完。你与队友共享 Bot 的对话消耗的是你的用量。参见[套餐与计费](https://cursor.com/help/grok-bot/plans)。 |
| **This Bot's owner has reached their usage limit** | 这条回复计入了所有者的账号，而所有者的用量已用完。请所有者检查其套餐。 |
| **This conversation can't run on your computer because your privacy mode is stricter than the bot owner's.** | 你的隐私模式设置比所有者的更严格，因此这次对话无法使用你的计算机。 |
| 在 Slack 中，Bot 要求你关联 Cursor 账号 | 在 **Settings** > **General** > **Shared Bots** 下关联你的 Slack 账号，使用该 Bot 所在团队的 Cursor 账号。 |

如果这些都不符合，请携带 Bot 名称、确切消息和你使用的 Grok Bot 版本[联系支持](https://cursor.com/help/grok-bot/get-help)。
