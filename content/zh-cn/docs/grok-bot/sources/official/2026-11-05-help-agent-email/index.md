---
title: "帮助：给 Bot 一个邮箱地址"
linkTitle: "帮助：Bot 邮箱"
date: 2026-11-05
originalTitle: "Give your Bot an email address"
sourceUrl: "https://cursor.com/help/grok-bot/agent-email"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [功能更新, 安全, 连接器, 交互渠道]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：用户可在 mail.grokbot.com 下认领一个邮箱地址，所有自己的 Bot 在自己的聊天和例程中都可以用它收发、搜索邮件，用于注册服务、整理收据和通讯、起草和转发邮件。每人只能有一个地址，不能改名或删除，认领后永不重新发给他人。新邮件不会自己唤醒 Bot，只有用户建立的例程才会处理来信，例程默认只处理通过标准邮件认证的发件人。用户在聊天中要求发送的邮件，在 Auto-review 放行后发出；例程或其他非用户直接发起的邮件只会存为草稿，需要用户点击发送，不提供无人值守发送。收到的邮件被当成信息而不是指令，邮件里的要求不算用户许可；每封最多 50 位收件人，附件最多 10 个、单个 10 MB、合计 25 MB。Cursor 团队里该功能默认关闭，需管理员在 Bot Capabilities 下开启。

**保留理由**：说明 Bot 自有邮箱的权限规则：谁发起的邮件可直接发、谁只能留草稿，以及对来信的处理方式，是研究 Bot 对外沟通边界的一手资料。

---

你可以在 `mail.grokbot.com` 下为你的 Bot 认领一个电子邮件地址，例如 `yourname@mail.grokbot.com`。你的 Bot 随后可以用它接收、阅读、搜索和发送电子邮件。

有了地址，Bot 可以：

- 用自己的地址注册服务，并在你同意的情况下获取验证码或验证链接。
- 收集收据、新闻通讯和报告，并为你总结。
- 为你起草电子邮件，例如摘要或更新，并起草回复。
- 转发其收件箱中的电子邮件，保留原始格式、图片和附件。转发需要 Grok Bot 0.75.2 或更高版本。
- 在电子邮件到达时运行例程（routine），可选仅限特定发件人。

## 如何为我的 Bot 获取电子邮件地址？

你可以通过两种方式认领：

- **询问你的 Bot。** 说类似「给你自己弄个电子邮件地址」的话。Bot 会询问你想要什么名称，检查它是否可用，并显示一张审批卡。在你批准之前，什么都不会被认领。
- **使用电子邮件应用。** 在桌面端，打开侧边栏中的 **Connect apps** 并选择 **Email**。在手机上，打开 **Settings** > **Connect apps** > **Email**。在 **Email address** 下，在 **Choose a name** 中输入名称，然后选择 **Create address**。

认领后，应用会显示你的地址，并提供一个复制按钮。

如果你通过 Cursor 团队使用 Grok Bot，团队管理员必须先开启 agent email。见[团队管理员如何开启 agent email？](#how-do-team-admins-turn-on-agent-email)

## 我可以选择哪些名称？

- 使用小写字母、数字、点、连字符和下划线。
- 以字母或数字开头和结尾。
- 最多使用 64 个字符。
- 避免使用保留词，例如 support、admin、billing、security、help、info、team、cursor、grok 和 xai。

每个地址都是唯一的。一旦有人认领了某个地址，它就不会再给任何其他人，即使认领它的账户被删除。

## 我可以拥有多个地址，或更改我的地址吗？

你只能拥有一个地址。你不能重命名或删除它，所以请谨慎选择名称。

## 我的哪些 Bot 可以使用我的地址？

该地址属于你，而不属于某一个 Bot。你所有的 Bot 都可以在你与它们的私人聊天中，以及在你设置的例程中使用它。

Bot 不能在 Slack 线程或其他人正在与 Bot 交谈的聊天中使用你的地址。[共享 Bot](https://cursor.com/help/grok-bot/shared-bots) 没有团队地址。

## 谁可以给我的 Bot 发邮件，我在哪里查看邮件？

任何人都可以向你的地址发送电子邮件。未通过垃圾邮件或病毒扫描的邮件会被保留，但不含正文或附件，并且永远不会启动例程。

应用中不提供收件箱视图，你也不会收到新邮件通知。要查看邮件，请询问你的 Bot，例如「你的收件箱今天收到了什么？」或「找到上周的收据。」最近一分钟内到达的邮件可能还不会出现在搜索结果中。

每条消息最多可包含 10 个附件，每个最大 10 MB，总计 25 MB。超出这些限制的附件会被跳过。

## 如何让我的 Bot 对收到的电子邮件采取行动？

设置一个例程。新邮件不会自行启动聊天或唤醒 Bot。Bot 只会通过你创建的例程对收到的邮件采取行动。

例程可以阅读邮件、总结邮件并起草回复。它想发送的任何电子邮件都会作为草稿等待，直到你批准。

在聊天中询问你的 Bot，例如「当收到来自 [billing@example.com](mailto:billing@example.com) 的电子邮件时，总结它并告诉我。」例程可以监视：

- 来自任何人的邮件。
- 来自特定地址的邮件，例如 `billing@example.com`。
- 来自整个域的邮件，例如 `*@example.com`。

默认情况下，例程只对通过标准电子邮件身份验证检查的发件人邮件运行。例程不能按主题过滤。见[例程](https://cursor.com/help/grok-bot/routines)。

## 我的 Bot 发送电子邮件需要我的批准吗？

这取决于是谁提出的。当你在聊天中要求 Bot 发送电子邮件时，一旦自动审查（Auto-review）允许，它就会发出。如果自动审查需要你，你会先看到一张审批卡。

来自例程的电子邮件，或来自并非由你以该请求发起的任何其他轮次的电子邮件，都会作为草稿等待。你的 Bot 会向你显示完整草稿，在你按下 **Send** 之前什么都不会发送。Bot 收到的电子邮件中的指令永远不算你的发送许可。

如果你还连接了 Gmail 或 Outlook，当两者都可能可用时，你的 Bot 会询问从哪个账户发送。

## 为什么我的例程留下草稿而不是发送？

这是预期行为。打开草稿并按下 **Send**。没有无人值守发送的选项。

## 我的 Bot 可以发送的内容有限制吗？

- 每封电子邮件最多 50 位收件人，包括收件人、抄送和密送。
- 最多 10 个附件，每个最大 10 MB，总计 25 MB。不能附加可执行文件。
- 新闻通讯和首次联系的电子邮件每条消息只发给一位收件人，并包含一键退订链接。
- 如果邮件退回，或有人退订或将其标记为垃圾邮件，你的 Bot 会停止向该地址发送电子邮件，并告诉你它跳过了谁。

对于 Bot 可以向多少新联系人发送电子邮件也有限制，以保护该地址不被标记为垃圾邮件。

## 电子邮件内容如何保持安全？

你的 Bot 将来自他人的电子邮件视为信息，而不是指令。它读取的每条消息都会标记为来自你或来自其他人，电子邮件中的请求不会让它自行发送任何内容或采取其他行动。

如果你删除 Grok Bot 账户，你的邮件和附件会被删除。地址本身会被停用，永远不会再给任何其他人。见[删除你的 Grok Bot 账户](https://cursor.com/help/grok-bot/delete-account)。

## 团队管理员如何开启 agent email？

对于 Cursor 团队，agent email 默认关闭。团队管理员在 [Cursor 仪表盘](https://cursor.com/dashboard/bot) 中开启它：在 **Grok Bot** 页面的 **Bot Capabilities** 下，开启 **Agent Email**。之后成员就可以认领地址。

如果管理员之后关闭 agent email，Bot 会失去其电子邮件工具，电子邮件例程会停止运行。发送到现有地址的邮件仍会被接收并保留，成员也保留其地址。

## 为什么我不能认领地址？

| 你看到的内容 | 该怎么做 |
| --- | --- |
| **Agent email is not enabled for this account.** | Agent email 尚未在你的账户上可用。 |
| **Your team admin has turned off Grok Bot agent email, so this account cannot claim or use an agent email address.** | 请你的团队管理员开启 **Agent Email**。见[团队管理员如何开启 agent email？](#how-do-team-admins-turn-on-agent-email) |
| **That address is taken, and addresses are never reissued, so retrying it cannot succeed. Choose a different name.** | 选择其他名称。 |
| 关于允许的字符、长度或保留词的消息 | 选择一个遵循[名称规则](#what-names-can-i-choose)的名称。 |
| **You can have one agent email address.** | 你已经有地址。询问你的 Bot 它是什么，或打开 **Email** 应用。 |
| **Couldn't create your email address. Try again.**（手机） | 检查[名称规则](#what-names-can-i-choose)，或在桌面端重试，桌面端会显示确切原因。 |
| **Too many email addresses checked in the last minute.** | 等一分钟，然后重试。 |

如果这些都不匹配，请带上你的 Cursor 账户电子邮件和确切消息[联系支持](https://cursor.com/help/grok-bot/get-help)。
