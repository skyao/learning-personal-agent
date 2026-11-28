---
title: "文档（docs.x.ai）：Team Bots"
linkTitle: "docs.x.ai：Team Bots"
date: 2026-11-16
originalTitle: "Team Bots"
sourceUrl: "https://docs.x.ai/grok-bot/team-bots"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-16）"
tags: [记忆与上下文, 安全, 交互渠道]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的文档现以 docs.x.ai（SpaceXSI Docs）为准，cursor.com 的文档地址已 308 跳转到这里。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Team Bot 让团队共享同一个 Grok Bot，类似内部工具，可在 Grok Bot、Slack、Microsoft Teams 和通话中使用，需要 Team 或 Enterprise 套餐且团队至少有另一人。角色分为 Owner（可删除）、Manager（改设置、审核所学内容、分享）和 Collaborator（聊天和教导），每人与 Bot 的聊天彼此私密。Bot 从所有人学习，团队记忆和技能对所有人生效，所以 Collaborator 教给它的内容先存为建议，由 Owner 或 Manager 批准或拒绝。Bot 使用所有者添加的应用与密钥，在自己的聊天中也可经 Allow 卡片使用你的应用；共享聊天中则用所有者的应用，使用别人的应用前先询问。文中另有「自己的聊天」与「共享聊天」在电脑、用量、谁回应审批卡片上的对照表，以及共享账号的风险提示。

**保留理由**：给出 Team Bot 的角色、记忆审核、应用与电脑归属规则，是已收的 team-bots 发布稿与 help-shared-bots 之外最系统的权限与归属说明。

---

Team Bot

Team Bot 让你与团队共享一个 Grok Bot。把它想成一个内部工具：构建一个处理真实工作流的 [Bot](https://docs.x.ai/grok-bot/bots)，然后让一位队友或整个团队可以使用它。他们可以在 Grok Bot、Slack、Microsoft Teams，甚至[你的通话](https://docs.x.ai/grok-bot/meetings)中使用它。

你团队中的任何人都可以创建 Team Bot，它带有权限：只有其所有者和管理者（Manager）可以更改它。

[有职责的 Bot](https://docs.x.ai/grok-bot/use-cases#turn-tasks-you-repeat-into-a-bot)承担你反复做的一项任务，而 Team Bot 则为整个团队承担它：一个让活动按计划推进的 Launch Bot、一个用你的品牌语气写作的 Copy Bot，或一个根据客户访谈回答问题的 Research Bot。

Team Bot 需要 Team 或 Enterprise 套餐，并且团队中至少还有一个人。要创建一个，见[创建和分享 Team Bot](https://docs.x.ai/grok-bot/create-a-team-bot)。

## Team Bot 的工作场所

每位队友在桌面端或手机上都有一个与 Team Bot 的私密聊天。它也能在你团队已经在沟通的地方工作。在 Slack 中，在频道或话题中提及它，或给它发私信。

在 Microsoft Teams 中，在频道中提及它、把它加入群聊，或给它发消息。

要连接它，见[把它加到 Slack](https://docs.x.ai/grok-bot/create-a-team-bot#add-it-to-slack)和[在 Microsoft Teams 中使用它](https://docs.x.ai/grok-bot/create-a-team-bot#use-it-in-microsoft-teams)。

当你的团队允许会议时，Team Bot 也可以加入 Google Meet、Zoom 和 Microsoft Teams 通话。见[让 Bot 加入你的会议](https://docs.x.ai/grok-bot/meetings)。

## Team Bot 如何工作

每个人都与同一个 Bot 协作，共用一套应用、密钥、技能和文件。每个人与它的聊天是私密的：所有者和管理者读不到你的聊天，你也读不到他们的。

### 谁能做什么

你团队中的任何人都可以创建和分享 Team Bot，除非团队管理员把分享限制为管理员。一个 Bot 可以有任意数量的管理者，因此整个团队都可以照看它。

| 角色 | 可以做什么 |
| --- | --- |
| 所有者（Owner） | 管理者能做的一切，以及删除 Bot。所有者是创建它的人。 |
| 管理者（Manager） | 更改 Bot 的设置、审核它学到的东西、分享它。 |
| 协作者（Collaborator） | 与 Bot 聊天并教它。 |

### 它学到什么

Team Bot 从每个与它共事的人那里学习：团队的决策、偏好，以及更好的任务做法。团队记忆和技能对所有人生效，因此当一个人教它某件事时，整个团队都受益。

共享记忆正是学习需要审核者的原因：一个人的经验会改变所有人面对的 Bot。当协作者为团队教它某件事时，Bot 会保存一条建议，由所有者或管理者批准或拒绝。所有者或管理者自己所做的更改立即生效。Bot 学到的关于你的内容留在你自己的聊天中。见[审核它学到什么](https://docs.x.ai/grok-bot/create-a-team-bot#review-what-it-learns)。

### 它使用谁的应用

Team Bot 使用其所有者添加的应用和密钥。在你自己的聊天中，它也可以使用你的应用，但会先用一张**允许**（Allow）卡片征求同意。在共享聊天中，它使用其所有者的应用，使用你的应用前会先询问。共享聊天包括 Slack 频道、话题和群组私信，以及 Grok Bot 中的群聊。

你的账户只代表你行事。唯一的例外是共享连接器：管理者让所有人通过一个账户使用某个应用。这省去了每位队友连接该应用的麻烦，但任何与 Bot 交谈的人从此都可以以该账户行事，包括做出更改。只分享不包含任何敏感内容的账户。见[与团队共享一个账户](https://docs.x.ai/grok-bot/create-a-team-bot#share-one-account-with-the-team)。

### 使用谁的计算机和用量

| | 你自己的聊天，或 Slack 私信 | 共享聊天 |
| --- | --- | --- |
| 计算机 | 你的 Grok Bot 计算机 | Bot 自己的一台共享计算机 |
| 用量 | 你的 | 它正在回答的人 |
| 谁回应审批卡片 | 你 | 只有它正在回答的人 |

在共享聊天中，Bot 从不在你的计算机上工作，因此计算机上的任何东西都不会出现在频道中。在 Slack 中回复未关联账户或不在你团队中的人时，使用团队的用量。

## 最佳实践

* 给每个 Team Bot 一项工作，并按其工作命名：Launch Bot、Copy Bot、Research Bot。
* 只添加与你分享对象中所有人都可以使用的应用、密钥和文件。
* 添加第二位管理者，让建议不必等一个人。
* 只在账户不含任何敏感内容时才共享它。
