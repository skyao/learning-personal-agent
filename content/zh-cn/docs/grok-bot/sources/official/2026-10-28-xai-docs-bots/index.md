---
title: "文档（docs.x.ai）：创建与管理 Bot"
linkTitle: "docs.x.ai：Bot 的创建与管理"
date: 2026-10-28
originalTitle: "Create and manage Bots"
sourceUrl: "https://docs.x.ai/grok-bot/bots"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：Shared Bots 改称 Team Bots；删除分工建议章节（改指向 How Grok Bot works）；新增删除 Bot 会同时删除其分享的模板；Team Bot 学到的内容需所有者或 Manager 批准"
tags: [记忆与上下文, 功能更新]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 文档「Work」一页讲到 Bot 的部分与这页有重合，这页更细。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Bot 被定义为有名字、职责、独立会话并会积累上下文的长期 AI 队友；何时需要单独的 Bot，文档指向 How Grok Bot works 一页。主 Bot（primary）会主动找用户并协调其他 Bot，Team Bot 不能当主 Bot；个人 Bot 没有描述和 **Bot settings** 页，行为要在聊天里调整，Team Bot 仍有描述，由所有者或 Manager 在 **About** 下编辑。Bot 可以做成模板分享，公开链接带身份、描述、技能和例程，不带电脑、登录和历史；删除 Bot 会清掉它的会话、记忆、例程和附件，同时删除它分享过的模板，使链接失效，共享电脑上的文件和登录则会留下。记忆由 Bot 自行决定何时保存，各 Bot 的记忆相互独立，只有姓名、时区等少数事实全账号共享；没有记忆管理界面，查看、纠正、删除都靠聊天，Team Bot 学到的内容要经所有者或 Manager 批准，也可以在 Settings 里从其他助手导入记忆到主 Bot。

**保留理由**：官方对多 Bot 分工、主 Bot 和记忆范围的说明，尤其是「记忆按 Bot 隔离、少数事实共享、没有记忆界面」这几点。

---

创建与管理 Bot

Bot 是一个持久的 AI 队友，有名字、职责、自己的对话，以及随时间发展的上下文。要判断一份工作何时需要单独的 Bot，见 [Grok Bot 如何工作](https://docs.x.ai/grok-bot/how-grok-bot-works#your-primary-bot-and-bots-with-one-job)。

## 创建 Bot

1. 选择侧边栏顶部的**新建 Bot**（New Bot，即 **+** 按钮），或按 `Cmd/Ctrl+N`。在团队中，**+** 按钮会打开菜单；选择**创建 Bot**（Create a Bot）。
2. 在**创建新 Bot**（Create New Bot）中，输入名称，为它的图片选择形状和颜色，然后选择**创建**（Create）。
3. Grok Bot 会打开与新 Bot 的聊天。
4. 在你的第一条消息中，给 Bot 说明它的职责、资料来源和审批边界，并让它记住。发送一个真实的首个任务，要有清晰的完成标准；起步提示见[用例](https://docs.x.ai/grok-bot/use-cases)。
5. 要重命名 Bot、添加标签或更改图片，点击聊天顶部的 Bot 名称打开其详情。见[更改 Bot 的名称、图片和标签](#change-a-bots-name-picture-and-label)。

当某份工作应当有一个长期的所有者时，你现有的 Bot 也可以建议或创建一个专门的 Bot。如果你想让 Bot 名单保持精简，可以让它在创建多个 Bot 之前先问你。

## 你的主 Bot

主 Bot（primary Bot）是你的主要联系点。它会主动来找你，并与你的其他 Bot 协调工作。

如果你没有主 Bot，Grok Bot 会显示**介绍你的主 Bot**（Introducing your primary Bot）。选择**创建主 Bot**（Create primary Bot）添加一个，或选择**选择现有 Bot**（Choose an existing Bot），选中你的一个 Bot，再选择**确认**（Confirm）。

要以后换一个，在侧边栏中右键点击你的主 Bot，选择**替换为其他 Bot**（Replace with different Bot）。在 iPhone 和 Android 上，使用 Bot 菜单中的**替换主 Bot……**（Replace Primary Bot…）。[Team Bot](https://docs.x.ai/grok-bot/team-bots) 不能作为你的主 Bot。

## 编辑 Bot

当你发现一个应当影响未来工作的持久偏好、边界或职责时，告诉 Bot 并让它记住。任务特定的指令用普通消息即可：

* **长期规则：**「从现在起，未经批准绝不发送外部消息。」
* **任务：**「为这十二个账户起草跟进邮件。」

Bot 把长期规则保存在记忆中。个人 Bot 不再有描述，也没有 **Bot 设置**（Bot settings）页面；要改变 Bot 的行为，在聊天中告诉它。[Team Bot](https://docs.x.ai/grok-bot/team-bots) 仍然有描述，由所有者或管理者在 Bot 详情的**关于**（About）下编辑。

### 更改 Bot 的名称、图片和标签

每个 Bot 有自己的名称、图片和标签。只有 Bot 的所有者可以更改这些；你并不拥有的 Bot 不会出现**重命名 Bot**（Rename Bot）。

要在桌面端重命名 Bot，在侧边栏中右键点击它并选择**重命名 Bot**，或双击侧边栏中的名称。输入新名称并按回车。如果侧边栏已折叠为图标，先展开它。你也可以点击聊天顶部的 Bot 名称打开详情，然后点击名称进行编辑。名称下方的标签用法相同；Bot 没有标签时会显示**添加标签**（Add a label）。

要在桌面端更改图片，打开 Bot 详情并点击其图片，然后选择一个标签页：

* **Bot** 更改 Bot 角色的外观。
* **生成**（Generate）根据简短描述生成图片。描述图片，选择**生成**，然后选择**设置头像**（Set avatar）。
* **上传**（Upload）使用你自己的图片。拖入图片或选择**浏览文件**（Browse files），调整它，然后选择**设置头像**。图片必须小于 25 MB。

在手机上，点击聊天顶部的 Bot 名称打开其资料，点击**编辑**（Edit）。更改**名称**（Name）或**标题**（Title，手机端对标签的称呼）并点击**完成**（Done）。要更改图片，点击图片或**头像**（Avatar），选择**形状**（Shape）、**生成**或**上传**。**上传**提供**从照片中选择**（Choose from Photos）或**拍照**（Take Photo），然后让你裁剪图片；图片最大 25 MB。

在 Grok Bot for Android 1.18.0 上，更改 Bot 的名称、标题或图片后点击**完成**或**放弃**（Discard）可能显示空白或错误页面。你的更改通常已经保存；返回聊天检查。此问题在 Android 1.19.0 中已修复；Google Play 提供更新时请更新 Grok Bot。

## 整理你的 Bot 列表

* **置顶**（Pin）活跃的 Bot，把它们保持在侧边栏顶部。
* 用分区按项目、客户或业务给 Bot 分组：右键点击一个 Bot，选择**移到新分区**（Move to new section），或者在你已有分区后选择**移到**（Move to）。分区在桌面端和 iOS 之间同步。
* **从侧边栏隐藏**（Hide from sidebar）把 Bot 从主列表中移除，但不删除它的工作，也不暂停它的例程。隐藏的 Bot 保持活跃并保留历史。
* 要恢复隐藏的 Bot，打开侧边栏底部的**隐藏的 Bot**（Hidden Bots），从 Bot 菜单中选择**在侧边栏中显示**（Show in sidebar）。在 iPhone 和 Android 上，在隐藏 Bot 列表中选择**取消隐藏**（Unhide）；当所有 Bot 都被隐藏时，主屏幕会显示**显示隐藏的 Bot**（Show Hidden Bots）。

在 iPhone 上，**复制**（Duplicate）Bot 可以把一个角色复用到不同的范围，例如每个区域一个账户健康 Bot。副本带有资料、设置、启用的技能、例程和头像，但不带对话历史、学到的记忆或附件，因此请先重命名并赋予它新的范围，再分配工作。

## 分享 Bot

当别人应当从同一个 Bot 起步时，分享一个模板。

1. 点击聊天顶部的 Bot 名称打开详情，选择**分享**（Share），然后选择**创建副本**（Create a copy）。Bot 会构建一个模板并把它发布到聊天中。
2. 在模板卡片上选择**发布**（Publish），然后选择**复制链接**（Copy link）。
3. 发送链接。接收者在 [x.ai](https://x.ai) 上打开预览，可以选择**添加到 Grok Bot**（Add to Grok Bot）。他们需要 Grok Bot 应用才能完成添加。

在 iPhone 和 Android 上，打开 Bot 菜单并选择**作为模板分享**（Share as Template）。

发布后，同一个**分享**菜单会提供**查看模板详情**（View template details）、**更新模板**（Update template，把你的最新更改推送到共享副本）和**删除模板**（Delete Template，关闭链接）。

新的模板链接是公开的。如果你的团队只允许团队内分享或已关闭模板分享，应用不会提供**创建副本**，发布模板时会显示 `Your team doesn't allow public templates` 或 `Template sharing is turned off`。Enterprise 团队一开始把模板分享限制在团队内；管理员可以在[公开模板分享](https://docs.x.ai/grok-bot/teams-and-enterprises#public-template-sharing)下更改。

公开链接任何拿到的人都能打开，它会暴露 Bot 的共享配置：身份、描述、技能和例程。仅团队链接只对你的团队成员开放。分享前请移除 API 密钥、内部 URL、客户数据，以及任何你不会放进公开文档的内容。

添加共享模板会在接收者的账户上创建一个副本。他们永远不会得到你的计算机、登录信息或对话历史。要让你的团队共用一个可以聊天的 Bot，而不是每人一个副本，请[分享 Bot 本身](https://docs.x.ai/grok-bot/team-bots)。

共享模板由其他用户创建，不是由 Grok Bot 创建。添加模板即接受当时显示的[第三方 bot 条款](https://x.ai/legal/bot-sharing-terms)。

在 Teams 套餐和 Enterprise 套餐中，管理员控制成员能否公开分享 Bot 模板。见[公开模板分享](https://docs.x.ai/grok-bot/teams-and-enterprises#public-template-sharing)。

## 从模板添加 Bot

要浏览 Bot 模板，打开侧边栏中的**连接应用**（Connect apps）并选择 **Bot 模板**（Bot templates）。画廊会在你的浏览器中打开 x.ai。打开一个模板链接，选择**导入 Bot**（Import Bot）添加该 Bot 的副本。

## 删除 Bot

要删除 Bot，在侧边栏中右键点击它并选择**删除**（Delete）。这会清除它的资料、对话、记忆、例程和附件，包括它为你的其他 Bot 保存的共享事实。它还会删除你从这个 Bot 分享的任何模板，使该模板的链接失效。此操作无法撤销。共享计算机上的文件和登录不按 Bot 隔离，可能留在那里；请另行清理。后端保留遵循适用的 Cursor 条款。

如果你以后可能需要它的工作，或想保留 Bot 的记忆，请改选**从侧边栏隐藏**。

## Bot 记住什么

Bot 保留稳定的偏好、重要事实和工作摘要，这让它能长期担任一个角色，而不必重放此前的每条消息。它会保存持久的东西，例如：

* 你喜欢的工作方式和你的偏好
* 你让它遵守的规则，例如「发邮件前总是先问。」
* 关于你的事实，例如你的姓名和时区
* 它与你一起做过什么的有日期记录

登录信息、银行卡和联系信息（如地址和电话号码）应放在 [Vault](https://docs.x.ai/grok-bot/vault)，而不是记忆中。

### Bot 何时保存内容

Bot 自己决定什么值得保留。它不会先问。它通常会在回复中提到一次保存，但并非每次保存都会出现在聊天中。要确保它记住某件事，请让它记住，例如：「记住我每周五都不在。」

### 跨聊天、Bot 和通话

Bot 在一个聊天中保存的内容，会在你与它的所有聊天中记住。每个 Bot 有自己的记忆，但关于你的一些事实（例如你的姓名和时区）由你所有的 Bot 共享。当一个 Bot 学到其中一项时，你的其他 Bot 也会知道。

在[语音聊天](https://docs.x.ai/grok-bot/chat-and-collaboration#start-a-voice-chat)中，Bot 可以利用你早先的通话和最近与它的聊天。挂断后，你可以在聊天中问它关于那通电话的事。

在[群聊](https://docs.x.ai/grok-bot/chat-and-collaboration#start-a-group-chat)中，你的 Bot 可以使用你在私聊中告诉它的内容。如果某些事不应进入群聊，告诉你的 Bot。群中的每个 Bot 保留自己的记忆；你的 Bot 的记忆不会与群中的其他 Bot 共享，但群里的每个人都能读到你的 Bot 说的话。

### 查看、纠正或移除记忆

个人 Bot 没有记忆界面。请在聊天中询问：

* 查看：「你记得关于我的什么？」
* 纠正：「那过时了。我搬到丹佛了。」
* 移除：「忘掉我在发布团队这件事。」

如果所有 Bot 共享的某个事实有误，把正确版本告诉你任意一个 Bot。要彻底移除一条共享事实，请找保存它的那个 Bot。

### 什么会重置或删除记忆

| 你做什么 | 记忆会怎样 |
| -------------------- | --------------------------------- |
| 重置对话 | 记忆保留。 |
| 删除 Bot | 该 Bot 的记忆被删除。 |
| 删除你的账户 | 你所有 Bot 的记忆被删除。 |

当一条消息被阻止时，通知可能会提供**重置**（Reset）。如果你选择它，会看到**重置此对话？**（Reset this conversation?）。对话历史从头开始，Bot 的记忆、文件、例程和设置保留。

### 谁可以查看或更改记忆

个人 Bot 的记忆属于你，只有你能改。[Team Bot](https://docs.x.ai/grok-bot/team-bots) 可以为整个团队学习内容，所有者或管理者批准它从队友那里学到的东西。它不会为团队保存关于你个人的任何内容；它记住的与你共事的内容只存在于你和 Bot 之间。队友的 Team Bot 不会获得你自己的 Bot 共享的关于你的事实。见 [Team Bot 学到什么](https://docs.x.ai/grok-bot/team-bots#what-it-learns)

### 从其他助手导入记忆

要导入另一个 AI 助手对你的了解，打开设置 → **通用**，在**导入**（Import）下选择**开始导入**（Start import）。把提示词复制到与另一个助手的聊天中，把它的回答粘贴到第二个框中，然后选择**添加到记忆**（Add to memory）。Grok Bot 会把它发送给你的[主 Bot](#your-primary-bot) 并打开该聊天。

### 记忆不是事实来源

记忆不能替代权威来源：

* 把变化中的事实留在源系统中
* 对重大决定，让 Bot 引用或重新打开当前数据
* 直接纠正过时的假设
* 用审批和[自动审查规则](https://docs.x.ai/grok-bot/security#approvals-and-auto-review)来支撑安全边界，而不只靠记忆

Bot 有各自的角色和对话，但它们共用计算机。它们可以通过私信、群聊和共享文件传递上下文。要规划 Bot 名单，见[为实现更大目标组建 Bot 团队](https://docs.x.ai/grok-bot/use-cases#build-a-team-of-bots-for-a-bigger-goal)。
