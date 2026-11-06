---
title: "帮助：群聊"
linkTitle: "帮助：群聊与 Bot 互发消息"
date: 2026-11-05
originalTitle: "Group chats and Bot-to-Bot messages"
sourceUrl: "https://cursor.com/help/grok-bot/group-chats"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [功能更新, 持续执行, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：群聊把用户的多个 Bot 放进同一对话，也可加入队友分享的 Bot，但不能与运行在用户自己计算机上的 Bot 同处一个群。Bot 在群里回复，用户用 @ 指定某个 Bot；Bot 也可私下给用户发消息或给别的 Bot 交接工作，这类消息出现在各 Bot 自己的聊天里而不在群里。没有开关能禁止 Bot 互相发消息，只能在聊天里告诉它们并让每个 Bot 记住；每条 Bot 回复（含 Bot 之间的消息）都计入用量。Bot 只有在代表某一个人行事时才能给其他 Bot 发消息，个人 Bot 在 Slack 频道线程里不能，共享 Bot 在频道或私信里可以交给被提及者自己的 Bot。手机端 1.19.0 起不能新建群聊，只能在电脑上创建；语音聊天一次只能和一个 Bot。

**保留理由**：回答了 Bot 之间交接的实际规则，特别是代表谁行事、在 Slack 与应用中的差异，以及用量计入方式。

---

群聊（group chat）把你的多个 Bot 放进同一个对话。你也可以加入[队友分享给你的 Bot](https://cursor.com/help/grok-bot/shared-bots)，但不能与运行在你自己电脑上的 Bot 同处一群。要创建群聊，见[群聊](https://cursor.com/docs/grok-bot/work#group-chats)。本页讲的是群聊开始运行之后该怎么做。

## Bot 在群聊中在哪里回复？

在群里。当你在群聊中发言时，Bot 会在那里回答。输入 `@` 和某个 Bot 的名称，把请求发送给该 Bot。

Bot 也可以在其自己的聊天中给你发消息，或给另一个 Bot 发消息以交接工作。这些消息出现在各 Bot 自己的聊天中，而不在群里。

## 如何让某个 Bot 的回复留在群聊中？

在群里告诉该 Bot。例如：「在这里的群里回复。不要私下给我发关于这件事的消息。」

要让它成为长期规则，请让每个 Bot 记住它。例如：「记住：在群聊中，在群里回复。」见[如何改变 Bot 的行为？](https://cursor.com/help/grok-bot/edit-bot#how-do-i-change-what-a-bot-does)

## 如何阻止 Bot 互相发消息？

没有用于此事的开关。Bot 之间会互发消息来交接工作，并遵循你对此的指示。

1. 在聊天中告诉这些 Bot。例如：「不要给其他 Bot 发消息。先问我。」
2. 要保留该规则，请让每个 Bot 记住它。
3. 如果某个 Bot 不断开始新工作，打开该 Bot 的聊天并让它停止。

要在不删除助手 Bot 的情况下让它安静，请关闭其通知或隐藏它。见[如何关闭助手 Bot 的通知？](https://cursor.com/help/grok-bot/how-to#how-do-i-turn-off-notifications-for-helper-bots)

每条 Bot 回复都计入你的用量，包括群里的回复和 Bot 之间的消息。群里的 Bot 越少，回复就越少。

## Bot 能从 Slack 给其他 Bot 发消息吗？

只有当 Bot 在该轮中代表某一个人行事时，它才能把工作交给其他 Bot。你在哪里与它交谈，以及它是个人 Bot 还是[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)，决定了这一点：

| Bot | 你在哪里提问 | 能给其他 Bot 发消息吗？ | 代表谁行事 | 回复落在哪里 |
| --- | --- | --- | --- | --- |
| 个人 Bot | 应用，或你自己的 Slack 私信 | 能 | 你 | 应用聊天，不是 Slack |
| 个人 Bot | Slack 频道线程 | 不能 | 无人，线程是共享的 | Bot 说它做不到 |
| 共享 Bot | Slack 频道线程或 Slack 私信 | 能，发给该人自己的 Bot | 提及它的队友 | 同一个 Slack 线程 |

要在 Slack 频道中在 Bot 之间交接工作，请分享一个 Bot 并将其添加到 Slack。共享 Bot 有自己的 Slack 应用和 handle，频道中的任何人都可以给它工作。见[如何把共享 Bot 添加到 Slack？](https://cursor.com/help/grok-bot/shared-bots#how-do-i-add-a-shared-bot-to-slack)

## 如何重命名群聊或更改其用途？

在桌面端重命名，请在侧边栏中右键点击该群组并选择 **重命名聊天（Rename chat）**。你也可以点击聊天顶部的群组名称，然后在详细信息中点击该名称进行编辑。在手机上，点击聊天顶部的群组名称，点击 **编辑（Edit）**，更改 **名称（Name）**，然后点击 **完成（Done）**。

要更改群组的用途，请在群里告诉这些 Bot。

## 我可以在手机上创建群聊吗？

在 1.19.0 或更高版本的手机应用上不行。主屏幕上的 **+** 按钮会打开 **新建 Bot（New Bot）**，不再提供 **新建群聊（New Group Chat）**。请在电脑上从 Grok Bot 创建群组。你已有的群聊会留在手机上的列表中，你可以在那里打开、写入和重命名它们。

## 群聊有通知吗？

群聊没有针对单个 Bot 的 **通知（Notifications）** 开关。见[关注状态与通知](https://cursor.com/docs/grok-bot/settings#attention-states-and-notifications)。

## 我可以在群聊中语音聊天吗？

不能。语音聊天一次只能与一个 Bot 进行。见[与 Bot 语音聊天](https://cursor.com/help/grok-bot/voice-chat)。
