---
title: "文档（docs.x.ai）：Bot 主动提出做事"
linkTitle: "docs.x.ai：主动性"
date: 2026-11-19
originalTitle: "When Your Bot Takes Initiative"
sourceUrl: "https://docs.x.ai/grok-bot/initiative"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-19）"
tags: [持续执行, 功能更新]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的文档现以 docs.x.ai（SpaceXSI Docs）为准，cursor.com 的文档地址已 308 跳转到这里。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文档说明 Bot 不只等待指令，会发现可代劳的工作并主动提出，也会提醒用户需要注意的事。具体包括：主 Bot 主动提出接手任务；Gmail 等应用被登出时在聊天中提示并提出重新连接；在 X Chat 中以自己的话跟进对话。主动联系用户的是在侧边栏标星的主 Bot，Team Bot 不能成为主 Bot，但可在需要时在 Slack 线程中请求用户。Bot 先提出、经用户同意后才做，风险操作前仍会询问。关闭该 Bot 的 Notifications 可减少提醒，但不会关闭主动的检查，需要的话联系支持。

**保留理由**：1.0 发布文章只概括了主动性，这篇补充了哪个 Bot 会主动联系用户、主动行为的范围以及通知开关的边界。

---

当你的 Bot 主动出手时

你的 Bot 不只会等待指令。它会注意到能从你手上接过去的工作并主动提出处理，也会在某件事需要你关注时告诉你。决定权仍在你手里：它先提出，风险操作前先询问。

## 我的 Bot 在未被要求时会做什么？

* **主动提出接手工作。** 你的主 Bot 会发现它能替你处理的任务，并主动提出去做。
* **指出应用的问题。** 当 Gmail 等应用把你登出时，你的主 Bot 会在聊天中告诉你，并提出重新连接。
* **跟进。** 在 [X Chat](https://docs.x.ai/grok-bot/chat-and-collaboration#chat-in-x-chat) 中，Bot 可以用自己的话跟进一段对话。

## 哪个 Bot 会联系我？

你的[主 Bot](https://docs.x.ai/grok-bot/bots#your-primary-bot)，在侧边栏中用星标标记。Team Bot 不能成为你的主 Bot。

Team Bot 仍然可以向你索要它需要的东西。例如，当它的某个例程需要你连接的应用时，它会在自己的 Slack 线程中询问并 @ 你。

## 我的 Bot 是自行行动还是先询问？

它先提出。你说可以后，它会像处理你交给它的任何任务一样完成工作，并在风险操作前询问。见[审批、安全与隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy)。

## 如何减少 Bot 发来的提醒？

关闭该 Bot 的 **通知（Notifications）**。在手机上，开关位于 Bot 的配置文件中。在桌面端，让 Bot 关闭其通知。见[控制通知](https://docs.x.ai/grok-bot/settings-and-notifications#control-notifications)。

通知控制的是提醒，不是检查本身。如果你希望关闭 Bot 的检查，请[联系支持](https://docs.x.ai/grok-bot/troubleshooting#before-contacting-support)。
