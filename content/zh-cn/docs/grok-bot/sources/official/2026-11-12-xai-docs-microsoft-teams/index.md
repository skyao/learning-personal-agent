---
title: "文档（docs.x.ai）：在 Microsoft Teams 中使用 Grok Bot"
linkTitle: "docs.x.ai：Teams 接入"
date: 2026-11-12
originalTitle: "Use Grok Bot in Microsoft Teams"
sourceUrl: "https://docs.x.ai/grok-bot/microsoft-teams"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-12）"
tags: [交互渠道, 连接器]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的文档现以 docs.x.ai（SpaceXSI Docs）为准，cursor.com 的文档地址已 308 跳转到这里。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Team Bot 可带入 Microsoft Teams，在频道中被提及、私聊或加入群聊，行为与在 Slack 中一致：为提问的人行事、使用其用量、风险操作前询问。前提是 Bot 已发布且用户是所有者或 Manager、团队管理员已在 Grok Bot 页面的 Shared Bots 下启用 Microsoft Teams、有该组织的 Microsoft 账号。接入步骤包括 Bot 所有者点击 Connect Microsoft Teams，再由 Teams 管理员在 Teams admin center 的 Pending approval 中批准，批准后 Teams 自行完成设置最长约一小时。文档还说明账号关联、Bot 能做的事（读取所在线程与频道、读取附件、通过 OneDrive 发送文件）、更新与移除，以及一张常见问题表。

**保留理由**：补充 Teams 接入的管理员批准流程和常见故障，是 Slack 之外的另一个渠道的官方设置说明。

---

在 Microsoft Teams 中使用 Grok Bot

把[团队 Bot（Team Bot）](https://docs.x.ai/grok-bot/team-bots)带入 Microsoft Teams，你的团队就能在频道里提到它、直接与它对话，并把它加入群聊。它的行为与在 Slack 中一致：为提出问题的人行事、使用其用量，并在有风险的操作前先询问。

## 把 Bot 添加到 Microsoft Teams 之前需要什么？

* 一个已发布的团队 Bot。你必须是它的所有者或 Manager。
* 团队管理员已为你的 Cursor 团队开启 Microsoft Teams。见[团队管理员如何开启 Microsoft Teams？](#how-does-a-team-admin-turn-on-microsoft-teams)
* 一个属于使用 Teams 的组织的 Microsoft 账号。

## 团队管理员如何开启 Microsoft Teams？

1. 在团队仪表盘的 Grok Bot 页面，**共享 Bot（Shared Bots）** 下，在 **启用 Microsoft Teams（Enable Microsoft Teams）** 旁选择 **启用（Enable）**。
2. 用 Microsoft Teams 管理员或全局管理员账号登录，接受 Microsoft 显示的权限。

这一行随后会显示 Microsoft Teams 已为你的组织启用。团队里的 Bot 所有者现在可以连接自己的 Bot。**撤销（Revoke）** 会把它关掉。每个 Bot 仍要由 Microsoft Teams 管理员在 Teams 管理中心批准。

## 如何把团队 Bot 添加到 Microsoft Teams？

由所有者或 Manager 在发布后连接：

1. 打开 Bot 的详情，找到 **带到你团队的 Microsoft Teams（Bring to your team's Microsoft Teams）**，或选择 **管理（Manage）**，在 **渠道（Channels）** 下查看。选择 **连接 Microsoft Teams（Connect Microsoft Teams）**。
2. 在弹出的浏览器窗口里完成 Microsoft 登录。确认是正确的账号；如果你属于多个组织，选择一个组织。
3. 当对话框显示 **等待管理员批准（Waiting on admin approval）** 时，需要一名 Microsoft Teams 管理员在 Teams 管理中心的 **Teams 应用（Teams apps）** > **管理应用（Manage apps）** > **待批准（Pending approval）** 中批准这个 Bot。Microsoft 不会通知他们，所以把对话框显示的链接发给他们。他们批准后立刻选择 **再次检查（Check again）**，或选择 **取消请求（Cancel request）** 停止。

批准之后，Microsoft Teams 会自行完成 Bot 的设置，最长可能需要一小时。对话框随后会显示该 Bot 已在 Microsoft Teams 中，并提供 **在 Teams 中打开（Open in Teams）**。要在频道里使用它，请在 Microsoft Teams 中把它添加到一个团队，对话框会列出它已被添加到的团队。

如果 Teams 管理员拒绝了该 Bot，对话框会显示他们的说明。做出修改后选择 **重新提交（Resubmit）**。

## 如何关联我的 Microsoft Teams 账号？

Bot 需要先知道你是谁，才能替你行事。你第一次给它发消息时，它会回复一张只有你能看到的 **关联账号（Link Account）** 卡片。选择它并用你的 Microsoft 账号登录。

你也可以先关联：打开 **设置（Settings）** > **常规（General）** > **团队 Bot（Team Bots）**，在 **Microsoft Teams 账号（Microsoft Teams account）** 旁选择 **关联（Link）**。如果提示你的管理员还没有为组织开启 Microsoft Teams，请让 Cursor 团队管理员开启。

## Bot 在 Microsoft Teams 里能做什么？

* **在频道和聊天中回答。** 在它已加入的团队的某个频道里提到它，把它加入群聊，或直接给它发消息。
* **读取对话。** 它会读取自己所在的话题串，以及它已加入的团队的频道。
* **处理文件。** 它会读取帖子附带的文件，并通过你的 OneDrive 给你发送文件。如果你在频道或群聊里索要文件，它会请你改为直接给它发消息。
* **替你行事。** 它使用你的用量，并在有风险的操作前询问你，与在 Slack 中一样。见[谁的电脑与用量](https://docs.x.ai/grok-bot/team-bots#whose-computer-and-usage)

要让 Bot 加入 Teams 通话并转写，见[把 Bot 加入你的会议](https://docs.x.ai/grok-bot/meetings)。

## 如何更新或移除 Microsoft Teams 中的 Bot？

* **名称或图片。** 修改之后，对话框会显示 Bot 的名称或头像已更改。选择 **在 Teams 中更新（Update in Teams）**。如果改动需要你的 Teams 管理员批准，会显示 **有一项更新正等待你的 Teams 管理员处理（An update is waiting for your Teams admin）**。
* **移除它。** 在同一个对话框里选择 **从 Microsoft Teams 中移除（Remove from Microsoft Teams）**。这会把这个应用从你的 Microsoft Teams 组织中移除，队友在那里就联系不到这个 Bot，直到它被再次添加。
* **断开你的 Microsoft 账号。** 这会把它从你在该组织拥有的每个 Bot 上断开，而不只是这一个。已经在 Teams 里的 Bot 仍会在那里继续回答。
* **删除这个 Bot。** 删除 Bot 也会把它从 Microsoft Teams 中移除。

## 为什么我的 Bot 不在 Microsoft Teams 里？

| 你会看到 | 它的含义 |
| --- | --- |
| 你的团队**未启用 Microsoft Teams（Microsoft Teams isn't enabled）** | 团队管理员需要在团队仪表盘的 Grok Bot 页面上选择 **启用 Microsoft Teams（Enable Microsoft Teams）**。 |
| **请先把这个 Bot 发布到你的团队，再把它添加到 Microsoft Teams（Publish this Bot to your team first, then add it to Microsoft Teams）** | 这个 Bot 还是草稿。选择 **发布（Publish）**，然后连接。 |
| **等待管理员批准（Waiting on admin approval）** | 你的 Teams 管理员还没有批准这个 Bot。把对话框里的链接发给他们，然后选择 **再次检查（Check again）**。 |
| **你的 Teams 管理员拒绝了（Your Teams admin declined）** 这个 Bot | 查看他们的说明，做出修改，然后选择 **重新提交（Resubmit）**。 |
| **Microsoft Teams 没有接受这个应用（Microsoft Teams didn't accept the app）** | 你的组织不允许在 Teams 中使用自定义应用。Teams 管理员可以允许。选择 **下载应用包（Download app package）**，把它发给你的 Teams 管理员上传。 |
| **被组织的 Teams 应用策略阻止（Blocked by your organization's Teams app policy）** | Microsoft Teams 管理员需要在 Teams 管理中心允许这个应用。 |
| **需要管理员批准（Need admin approval）** | Microsoft 登录需要管理员同意。把对话框显示的链接发给 Microsoft Teams 管理员或全局管理员，然后重新连接。 |
| **Microsoft Teams 对你的团队已停止工作（Microsoft Teams stopped working for your team）** | 团队的连接已过期。Cursor 团队管理员需要在仪表盘上选择 **重新连接 Microsoft Teams（Reconnect Microsoft Teams）**。 |
| **正在 Microsoft Teams 中完成设置（Finishing setup in Microsoft Teams）** | 这个 Bot 已获批准，Teams 还在设置它。最长可能需一小时，会自行完成。 |
| 一张 **关联账号（Link Account）** 卡片 | 你的 Microsoft 账号还没有关联。选择它并登录。 |

如果以上都不符合，请带上 Bot 的名称、确切的提示信息和你的 Grok Bot 版本，[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。
