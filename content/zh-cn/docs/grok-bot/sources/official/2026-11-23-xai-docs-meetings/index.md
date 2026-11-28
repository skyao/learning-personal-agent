---
title: "文档（docs.x.ai）：让 Bot 加入你的会议"
linkTitle: "docs.x.ai：会议"
date: 2026-11-23
originalTitle: "Add a Bot to Your Meetings"
sourceUrl: "https://docs.x.ai/grok-bot/meetings"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-23）"
tags: [交互渠道, 功能更新]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的文档现以 docs.x.ai（SpaceXSI Docs）为准，cursor.com 的文档地址已 308 跳转到这里。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。文档列出的可用套餐含 Super，1.0 发布文只写了 Team、Enterprise、Ultra，照录原文。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Bot 可加入 Google Meet、Zoom 或 Microsoft Teams 通话，听取内容、做笔记、在会议聊天中回答问题，结束后发送摘要和待办事项。把会议链接贴给 Bot 并批准卡片后，由主持人放行；Bot 以「Bot 名（某人的 Bot）- transcribing」的名称加入，跟随日历的 Bot 也可自行加入已安排的会议。文档还说明如何在 Upcoming 中管理会议（Disable interactivity、Cancel、Quit）、在会议聊天中按名字呼叫 Bot、Zoom 私聊得到私下回答，以及 Bot 不会在会议中分享用户的凭据。会议功能面向 Team、Enterprise、Ultra 和 Super 套餐；Enterprise 管理员在团队后台 Bot Capabilities 下的 Meetings 开关控制是否允许。

**保留理由**：提供会议功能的操作细节与权限边界，这些在 1.0 发布文章中只有一句话。

---

让 Bot 加入你的会议

Bot 可以加入你的 Google Meet、Zoom 或 Microsoft Teams 通话。它听取内容、做笔记、在会议聊天中回答问题，并在通话结束时给你发送摘要和待办事项。

会议功能在 Team、Enterprise、Ultra 和 Super 套餐中可用。Enterprise 管理员可以在设置中开启会议。见 [Team Bot 可以加入会议吗？](#can-a-team-bot-join-meetings)

## 如何让 Bot 加入会议？

1. 把 Google Meet、Zoom 或 Microsoft Teams 链接粘贴到你与 Bot 的聊天中，让它加入并做笔记。
2. 当 Bot 询问时批准卡片。
3. 会议开始时，由主持人放行 Bot。它以 **Bot 名（你的名字的 Bot）- transcribing** 的身份加入；Team Bot 则以 **Bot 名（Team Bot）- transcribing** 的身份加入。

跟随你日历的 Bot 也可以自行加入已安排的会议。

你也可以让 Bot 创建一个加入你会议的例程。每次运行只加入该例程要求的会议。由例程派出的 Bot 会做笔记，但不在会议聊天中回答。对于单次会议或一个重复系列，请改为让 Bot 加入它；它会在没有例程的情况下安排加入。

不确定该说什么？打开 Bot 详情。如果它以前没有加入过会议，**建议**（Suggested）下的**添加到会议**（Add to meeting）会起草一个问题，询问 Bot 如何把它加到会议中。

## 如何管理 Bot 即将参加的会议？

打开 Bot 详情。它正在加入或参加的会议出现在**即将开始**（Upcoming）下，带有距加入时间的倒计时、已安排会议的下次加入时间，或它在通话中时的**正在做笔记**（Taking notes）。

把鼠标悬停在你安排的会议上并打开其菜单，可以看到**会议操作**（Meeting actions）：

* **禁用交互**（Disable interactivity）让 Bot 继续听取和做笔记，但不在会议中回答。该行显示**已静音**（Muted）。会议仍在计划中时，**启用交互**（Enable interactivity）可以重新开启。一旦 Bot 正在加入或已在通话中，请退出并重新添加它来重新开启。
* **取消**（Cancel）移除一场已安排的会议。
* **退出**（Quit）让 Bot 离开它正在加入或参加的一场会议。

## 会议中如何与 Bot 交谈？

在会议聊天中按名称称呼 Bot，它会在那里回答。

* **Zoom 私聊。** 给 Bot 的私聊消息会得到私下回答。
* **会议室。** 来自会议室设备的请求被视为来自该房间，而不是某一个人。

如果会议中有人索要 Bot 保留未发的内容，Bot 会告诉你谁在问，并提出发送。它不会在会议中分享你的凭据。

## 会议结束后会怎样？

通话结束时，Bot 会在它的聊天中发送摘要和待办事项。如果你有[页面](https://docs.x.ai/grok-bot/files-and-results#pages)，更长的报告会放在一个页面上，链接在聊天中。你可以随时向 Bot 索取过去某次会议的摘要或转录。

会议使用发起会议者的设置。

## Team Bot 可以加入会议吗？

可以，前提是其团队允许会议。在 Enterprise 套餐中，管理员通过团队仪表盘 Grok Bot 页面 **Bot 能力**（Bot Capabilities）下的**会议**（Meetings）为所有人的 Bot 开启或关闭会议。关闭时，Bot 无法加入或读取会议，已安排加入的 Bot 会告诉你会议已不可用。见[面向团队和企业的 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises#meetings)。
