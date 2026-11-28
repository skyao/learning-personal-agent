---
title: "文档（docs.x.ai）：创建并分享 Team Bot"
linkTitle: "docs.x.ai：创建 Team Bot"
date: 2026-11-13
originalTitle: "Create and share a Team Bot"
sourceUrl: "https://docs.x.ai/grok-bot/create-a-team-bot"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-13）"
tags: [交互渠道, 记忆与上下文]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的文档现以 docs.x.ai（SpaceXSI Docs）为准，cursor.com 的文档地址已 308 跳转到这里。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文档给出创建 Team Bot 的步骤：在侧边栏选 + 和 Create a Bot、描述职责、按其提示添加插件、密钥、技能和文件，发布前为只有自己可见的 Draft。分享时可选团队、整个组织或指定的人，并可设 Manager；队友在 Browse Team Bots 中查找。Owner 和 Manager 在 Review learnings 里批准或拒绝 Collaborator 教给 Bot 的内容。共享连接器需要团队管理员先开启 Allow Shared Logins。接入 Slack 需先分享，在 Bring to your team's Slack 点 Connect；若分享给整个组织，Slack 工作区的任何正式成员都可提及它，Slack 访客、Slack Connect 频道和其他工作区不能使用。接入 Microsoft Teams 的步骤指向另一页，另说明如何修改与删除（仅 Owner 可删除）。

**保留理由**：是 Team Bot 的操作手册，补充界面步骤、Slack 谁能用的规则和共享账号设置，与概念页 team-bots 互补。

---

创建并分享 Team Bot

创建一个整个团队都能使用的 Bot，然后把它带入 Slack 或 Microsoft Teams。要事先了解角色、记忆和用量如何运作，见 [Team Bot](https://docs.x.ai/grok-bot/team-bots)。

Team Bot 需要 Team 或 Enterprise 套餐，并且你的团队中至少还有一个人。Team Bot 在云端运行，因此在你自己的计算机上运行的 Bot 仍然是个人 Bot。

## 创建 Team Bot

与你共享这个 Bot 的每个人都能使用你添加到其中的内容。只添加他们可以使用的应用、密钥、技能和文件。

1. 在侧边栏选择 **+**，然后选择 **创建 Bot（Create a Bot）**，并给它起名。
2. 告诉它为团队做哪项工作。一句话就够了。
3. 按它的设置流程操作。它会要求插件（即它连接的应用）、密钥、技能和文件。在你发布之前，它是一份只有你能看到的 **草稿（Draft）**。
4. 当 Bot 说准备好了，选择 **发布（Publish）**。队友之后可以在 **浏览 Team Bot（Browse Team Bots）** 下找到它。

## 分享它

1. 选择 Bot 聊天右上角的 **分享（Share）**。
2. 在 **谁有访问权（Who has access）** 下，选择你的团队、**组织中的所有人（Everyone in your organization）** 或 **你邀请的人（People you invite）**。
3. 要邀请某人，在 **添加人或群组（Add people or groups）** 下添加他们。
4. 要把某人设为 Manager，打开其角色并选择 **Manager**。
5. 要发送链接，选择 **复制链接（Copy link）**。

要分享你已有的 Bot，先检查它的应用、密钥、技能和文件，然后选择 **分享**。要停止分享，选择 **仅你（Only you）**。只有所有者可以停止分享。

## 查找并使用 Team Bot

1. 在侧边栏选择 **+**，然后选择 **浏览 Team Bot**。在桌面端，你也可以按 `Cmd/Ctrl+K` 并选择 **浏览 Team Bot**。
2. 选择 **添加（Add）**，把某个 Bot 留在侧边栏中。

列表以 **热门（Popular）** Bot 开头，**团队已批准（Team approved）** 标记团队管理员批准过的 Bot。你也可以问自己的某个 Bot，例如「有负责发布规划的 Team Bot 吗？」，或打开队友发来的链接。

Team Bot 的链接对每个人打开的是同一个 Bot。[分享 Bot 模板](https://docs.x.ai/grok-bot/bots#share-a-bot)则给每个人一份自己的副本。你可以在桌面端与 Team Bot 语音聊天，并把它加入与其他云端 Bot 的群聊。

要让所有 Team Bot 在使用你的应用前都重新询问，请在 **设置** > **通用** > **Team Bot** 中选择 **清除连接器偏好（Clear connector preferences）**。

## 审查它学到什么

所有者和 Manager 审查 Collaborator 为团队教给 Team Bot 的内容。

1. 打开 Bot 的详情，选择 **审查学习内容（Review learnings）**。**知识（Knowledge）** 会打开。
2. 在 **待审查（To review）** 下，为每条建议选择 **批准（Approve）** 或 **拒绝（Reject）**。

批准的建议会出现在 **最近学到（Recently learned）** 下。

## 与团队共用一个账号

共享连接器让每个人通过一个账号使用某个应用。如果你共享自己的账号，与 Bot 对话的每个人都会以该账号行动，包括做出更改。只共享不包含任何敏感内容的账号。

团队管理员先开启 **允许共享登录（Allow Shared Logins）**。然后，作为所有者或 Manager：

1. 打开 Bot 的详情，在 **设置（Setup）** 下选择 **服务账号（Service accounts）**。
2. 在 **共享连接器（Shared connectors）** 下选择一个应用。
3. 选择 **使用个人账号（Use individual accounts）**，让每位队友连接自己的账号；或选择 **共享你的账号（Share your account）**，让所有人通过你的账号行动。

有些应用还允许 Bot 用自己的账号登录，即为团队单独设一个账号。要停止，在应用所在行选择 **停止共享（Stop sharing）**，或移除该应用。只有账号所属的 Manager 可以重新连接它。

## 把它加入 Slack

在连接之前先分享 Bot。然后，作为所有者或 Manager：

1. 打开 Bot 的详情，找到 **带到你团队的 Slack（Bring to your team's Slack）**。
2. 选择 **连接（Connect）**。如果显示 **等待管理员批准（Awaiting admin approval）**，请让 Slack 工作区管理员批准该应用。

一旦显示 **已连接（Connected）**，队友就可以给 Bot 发消息或在频道中提及它。每位队友在每个工作区关联一次自己的 Slack 账号，这样 Bot 就知道他们是谁：在 Bot 要求时选择 **连接**，或在 **设置** > **通用** > **Team Bot** 下选择 **关联（Link）**。在线程中，Bot 代表提及它的队友行动，并可以把工作交给那个人自己的 Bot。

谁能与它对话取决于它分享给了谁：

* 如果分享给你的组织，Slack 工作区的任何正式成员都可以提及它，即使没有关联账号或席位。他们会被告知部分功能受限，并且必须先关联才能私信。
* 如果分享给你的团队或指定的人，只有那些人可以使用它。
* 个人 Bot 只与其所有者对话。

Slack 访客、Slack Connect 频道和其他工作区不能使用 Team Bot。

## 在 Microsoft Teams 中使用它

团队管理员先开启 Microsoft Teams。然后所有者或 Manager 在 **带到你团队的 Microsoft Teams（Bring to your team's Microsoft Teams）** 下连接 Bot，由 Microsoft Teams 管理员批准。队友在频道中提及它，它会在帖子下回答。完整步骤见[在 Microsoft Teams 中使用 Grok Bot](https://docs.x.ai/grok-bot/microsoft-teams)。

## 更改或删除 Team Bot

所有者和 Manager 从 Bot 聊天右侧的详情中更改 Team Bot：**插件（Plugins）**、**密钥（Secrets）**、**技能（Skills）**、**文件（Files）** 和 **关于（About）**。扳手图标打开 **管理（Manage）**，其中有 Bot 的访问权、频道、**知识** 和用量。

删除 Team Bot 会为整个团队移除它，以及每个人与它的聊天。只有所有者可以删除：在侧边栏右键点击它，选择 **删除（Delete）**。

管理员在仪表盘的 Grok Bot 页面控制共享、共享登录，以及团队外部人员的 Slack 访问。见[面向团队和企业的 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises#manage-bots)。如果某项功能不工作，见 [Team Bot 缺失或被阻止](https://docs.x.ai/grok-bot/troubleshooting#a-team-bot-is-missing-or-blocked)。
