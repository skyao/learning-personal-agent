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
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [记忆与上下文, 功能更新]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 文档「Work」一页讲到 Bot 的部分与这页有重合，这页更细。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Bot 被定义为有名字、职责、独立会话并会积累上下文的长期 AI 队友，官方建议每个 Bot 负责一个完整结果。主 Bot（primary）会主动找用户并协调其他 Bot，共享 Bot 不能当主 Bot；个人 Bot 没有单独的设置页，行为要在聊天里调整。Bot 可以做成模板分享，公开链接只带身份、描述、技能和例程，不带电脑、登录和历史。记忆由 Bot 自行决定何时保存，各 Bot 的记忆相互独立，只有姓名、时区等少数事实全账号共享；没有记忆管理界面，查看、纠正、删除都靠聊天，也可以在设置里从其他助手导入记忆到主 Bot。删除 Bot 会清掉它的会话、记忆和例程，但共享电脑上的文件和登录会留下。

**保留理由**：官方对多 Bot 分工、主 Bot 和记忆范围的说明，尤其是「记忆按 Bot 隔离、少数事实共享、没有记忆界面」这几点。

---

创建与管理 Bot

Bot 是一位长期的 AI 队友，有名字、有职责、有自己的会话，还有随时间发展的工作上下文。

## 给每个 Bot 一个明确的职责

当工作具有以下某项明显不同的特征时，就创建一个单独的 Bot：

* 目标或负责领域
* 一组工具和来源
* 工作风格
* 审批边界
* 重复性日程

像 **Talent Scout**、**Expense Manager** 和 **Bug Reproduction** 这样的职责，能给 Bot 提供指引，并让它保存的上下文可复用；而 **General Helper** 两样都做不到。

用可操作的表述描述角色：

> Own the weekly account-health review. Pull product usage and support signals,
> flag evidence of churn or expansion, and produce a linked watch list for the
> customer-success team. Never contact a customer or change an account without
> approval.


## 创建 Bot

1. 在侧边栏顶部选择**新建 Bot（New Bot）**（**+** 按钮），或按
   `Cmd/Ctrl+N`。在团队中，**+** 按钮会打开一个菜单；选择**创建 Bot（Create a Bot）**。
2. 在**创建新 Bot（Create New Bot）**中，输入名称，为其图片选择形状和颜色，
   然后选择**创建（Create）**。
3. Grok Bot 会打开一个与新 Bot 的聊天。
4. 在你的第一条消息中，给 Bot 说明它的职责、来源和审批
   边界，并让它记住这些内容。发送一个带有明确完成标准的真实首个任务；
   入门提示见[使用场景](https://docs.x.ai/grok-bot/use-cases)。
5. 要重命名 Bot、添加标签或更改其图片，点击聊天顶部
   的 Bot 名称以打开其详情。参见[更改 Bot 的名称、
   图片和标签](#change-a-bots-name-picture-and-label)。

当你现有的 Bot 发现某项工作应当有一个长期负责人时，它们也可以建议或创建一个专注的 Bot。如果你想保持名单精简，在创建多个 Bot 之前先询问。

## 你的主 Bot

你的主 Bot（primary Bot）是你的主要联系人。它会主动与你联系，并与你的其他 Bot 协调工作。

如果你没有主 Bot，Grok Bot 会显示**介绍你的主 Bot（Introducing your primary Bot）**。选择**创建主 Bot（Create primary Bot）**添加一个，或**选择现有 Bot（Choose an existing Bot）**，选中你的一个 Bot，然后选择**确认（Confirm）**。

之后要选择另一个，右键点击侧边栏中的主 Bot，然后
选择**替换为其他 Bot（Replace with different Bot）**。在 iPhone 和 Android 上，使用 Bot 菜单中的**替换主 Bot…（Replace Primary Bot…）**。[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)不能
成为你的主 Bot。

## 编辑 Bot

当你发现一个应当影响未来工作的长期偏好、边界或职责时，告诉 Bot 并让它记住。任务特定的指令请用普通消息：

* **长期规则：**「从现在起，未经批准绝不发送外部消息。」
* **任务：**「为这十二个账户起草跟进消息。」

Bot 会把长期规则保存在它的记忆中。个人 Bot 不再有描述或 **Bot 设置（Bot settings）**页面；要改变 Bot 的行为，请在聊天中告诉它。[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)仍有描述，由其所有者或 Manager 在 Bot 详情的**关于（About）**下编辑。

### 更改 Bot 的名称、图片和标签

每个 Bot 都有自己的名称、图片和标签。只有 Bot 的所有者可以更改这些；对于你不拥有的 Bot，不会出现**重命名 Bot（Rename Bot）**。

要在桌面上重命名 Bot，右键点击侧边栏中的它并选择**重命名 Bot（Rename Bot）**，或双击侧边栏中的名称。输入新名称并按
Enter。如果侧边栏已折叠为图标，请先展开。你也可以点击
聊天顶部的 Bot 名称打开其详情，然后点击名称
进行编辑。名称下方的标签用法相同；当 Bot 没有标签时，它会显示**添加标签（Add a label）**。

要在桌面上更改图片，打开 Bot 的详情并点击其图片，
然后选择一个标签页：

* **Bot** 更改 Bot 角色的外观。
* **生成（Generate）**根据简短描述生成图片。描述图片，
  选择**生成**，然后选择**设置头像（Set avatar）**。
* **上传（Upload）**使用你自己的图片。拖入图片或选择**浏览文件（Browse files）**，
  调整它，然后选择**设置头像**。图片必须小于 25 MB。

在手机上，点击聊天顶部的 Bot 名称打开其个人资料，
然后点击**编辑（Edit）**。更改**名称（Name）**或**标题（Title）**（手机对标签的称呼），然后点击**完成（Done）**。要更改图片，点击图片或**头像（Avatar）**，
并选择**形状（Shape）**、**生成**或**上传**。**上传**提供**从照片中选择（Choose from Photos）**或**拍照（Take Photo）**，然后让你裁剪图片；图片最大可为
25 MB。

## 整理你的 Bot 名单

* **固定（Pin）**活跃的 Bot，让它们保持在侧边栏顶部。
* 用分区按项目、客户或业务对 Bot 分组：右键点击一个 Bot
  并选择**移到新分区（Move to new section）**，或者在有分区后选择**移到（Move to）**。
  分区会在桌面和 iOS 之间同步。
* **从侧边栏隐藏（Hide from sidebar）**会把 Bot 从主列表中移除，但不会删除其
  工作或暂停其例程。隐藏的 Bot 保持活跃并保留其历史。
* 要恢复隐藏的 Bot，打开侧边栏底部的**隐藏的 Bot（Hidden Bots）**，
  并从 Bot 菜单中选择**在侧边栏中显示（Show in sidebar）**。在 iPhone 和 Android 上，在
  隐藏 Bot 列表中选择**取消隐藏（Unhide）**；当所有 Bot 都被隐藏时，主屏幕
  会显示**显示隐藏的 Bot（Show Hidden Bots）**。

在 iPhone 上，**复制（Duplicate）** Bot 可以把一个角色复用到不同的范围，比如每个区域一个
账户健康 Bot。副本会带上个人资料、设置、启用的
技能、例程和头像，但不带会话历史、学到的记忆或
附件，因此在分配工作之前要重命名它并给它新的范围。

## 分享 Bot

当其他人应当从同一个 Bot 开始时，分享一个模板。

1. 点击聊天顶部的 Bot 名称打开其详情，选择
   **分享（Share）**，然后选择**创建副本（Create a copy）**。Bot 会构建一个模板并
   将其发布在聊天中。
2. 在模板卡片上选择**发布（Publish）**，然后选择**复制链接（Copy link）**。
3. 发送链接。接收者在 [x.ai](https://x.ai) 上打开预览，并可以
   选择**添加到 Grok Bot（Add to Grok Bot）**。他们需要 Grok Bot 应用才能完成添加。

在 iPhone 和 Android 上，打开 Bot 的菜单并选择**作为模板分享（Share as Template）**。

发布之后，同一个**分享**菜单会提供**查看模板详情（View template details）**、
**更新模板（Update template）**（把你的最新更改推送到共享副本）以及
**删除模板（Delete Template）**（关闭链接）。

新的模板链接是公开的。如果你的团队只允许团队内分享，或
已关闭模板分享，应用不会提供**创建副本**，并且
发布模板会显示 `Your team doesn't allow public templates` 或
`Template sharing is turned off`。企业团队初始的模板分享
仅限于团队；管理员可以在
[公开模板分享](https://docs.x.ai/grok-bot/teams-and-enterprises#public-template-sharing)下更改。

任何拿到公开链接的人都能打开它，并会暴露 Bot 的共享
配置：它的身份、描述、技能和例程。仅限团队的
链接只对你的团队成员打开。在分享之前，请移除 API 密钥、内部 URL、
客户数据，以及任何你不会放进公开文档的内容。

添加共享模板会在接收者的账户上创建一个副本。他们永远不会
得到你的计算机、登录信息或会话历史。如果要让你的团队共用一个 Bot
来聊天，而不是每人一个副本，请[分享 Bot
本身](https://docs.x.ai/grok-bot/shared-bots)。

共享模板由其他用户创建，而不是由 Grok Bot 创建。添加一个
即表示接受当时显示的[第三方 bot 条款](https://x.ai/legal/bot-sharing-terms)。

在 Teams 套餐和 Enterprise 套餐中，管理员控制成员是否可以
公开分享 Bot 模板。参见[公开模板
分享](https://docs.x.ai/grok-bot/teams-and-enterprises#public-template-sharing)。

## 从模板添加 Bot

要浏览 Bot 模板，打开侧边栏中的**连接应用（Connect apps）**并选择
**Bot 模板（Bot templates）**。图库会在你的浏览器中打开 x.ai。打开一个模板
链接并选择**导入 Bot（Import Bot）**，添加该 Bot 的你自己副本。

## 删除 Bot

要删除 Bot，右键点击侧边栏中的它并选择**删除（Delete）**。这会
抹除它的个人资料、会话、记忆、例程和附件，包括
它为你的其他 Bot 保存的共享事实。此操作无法撤销。共享计算机上的文件和
登录信息不按 Bot 隔离，可能仍留在那里；
请单独清理它们。后端保留遵循适用的 Cursor 条款。

如果你之后可能需要这些工作，或想保留 Bot 的记忆，请改为选择
**从侧边栏隐藏**。

## Bot 记住什么

Bot 会保留稳定的偏好、重要事实和来自工作的摘要，
这使它能够长期保持一个角色，而不必重放此前的每条消息。它会
保存持久的内容，例如：

* 你喜欢的工作方式，以及你的偏好
* 你要求它遵守的规则，比如「发送电子邮件前一定要先询问。」
* 关于你的事实，比如你的姓名和时区
* 一份带日期的、它与你一起做过什么的日志

登录信息、卡和联系信息（比如地址和电话号码）属于
[Vault](https://docs.x.ai/grok-bot/vault)，而不是记忆。

### Bot 何时保存内容

Bot 自行决定什么值得保留。它不会先询问。
它通常会在回复中提到一次保存，但并非每次保存都会显示在聊天中。
要确保它保留某些内容，请让它记住，例如：「记住我每周五都不在。」

### 跨聊天、Bot 和通话

Bot 在一个聊天中保存的内容，会在你与它的所有聊天中记住。每个 Bot
有自己的记忆，但少数关于你的事实（比如你的姓名和时区）
由你所有的 Bot 共享。当一个 Bot 得知其中一项时，你的其他 Bot
也会知道。

在[语音聊天](https://docs.x.ai/grok-bot/chat-and-collaboration#start-a-voice-chat)中，Bot
可以利用你之前的通话以及你最近与它的聊天。挂断后，
你可以在聊天中询问它那次通话的情况。

在[群聊](https://docs.x.ai/grok-bot/chat-and-collaboration#start-a-group-chat)中，你的
Bot 可以使用你在私聊中告诉它的内容。如果有内容应当留在
群聊之外，请告诉你的 Bot。群中的每个 Bot 保留自己的记忆；你的
Bot 的记忆不会与那里的其他 Bot 共享，但群里的每个人
都能读到你的 Bot 说的话。

### 查看、纠正或移除记忆

个人 Bot 没有记忆界面。请改为在聊天中询问：

* 查看：「你记得关于我的什么？」
* 纠正：「那已经过时了。我搬到 Denver 了。」
* 移除：「忘掉我在发布团队这件事。」

如果所有 Bot 共享的某项事实有误，告诉你的任意一个 Bot 正确
版本。要彻底移除一项共享事实，请让保存它的 Bot 处理。

### 什么会重置或删除记忆

| 你做什么          | 记忆会怎样            |
| -------------------- | --------------------------------- |
| 重置会话 | 记忆会保留。                   |
| 删除 Bot         | 该 Bot 的记忆会被删除。     |
| 删除你的账户  | 你所有 Bot 的记忆都会被删除。 |

当消息被阻止时，通知可能会提供**重置（Reset）**。如果你选择它，你会
看到**重置此会话？（Reset this conversation?）** 会话历史会重新开始，而
Bot 的记忆、文件、例程和设置会保留。

### 谁可以查看或更改记忆

个人 Bot 的记忆属于你，只有你能更改它。[共享
Bot](https://docs.x.ai/grok-bot/shared-bots)可以保存它为整个团队学到的东西，并且
它会在这样做时告诉你。它不会把关于你个人的任何内容保存给
团队；它记住的关于与你共事的内容只保留在你和该
Bot 之间。队友的共享 Bot 不会得到你自己的 Bot 共享的关于
你的事实。

### 从另一个助手导入记忆

要导入另一个 AI 助手对你的了解，打开设置 →
**常规（General）**，并在**导入（Import）**下选择**开始导入（Start Import）**。把提示词复制到
与你的另一个助手的聊天中，将其回答粘贴到第二个框中，然后
选择**添加到记忆（Add to Memory）**。Grok Bot 会把它发送给你的
[主 Bot](#your-primary-bot) 并打开该聊天。

### 记忆不是事实来源

记忆不能替代权威来源：

* 把变化中的事实保存在源系统中
* 对于重要决策，让 Bot 引用或重新打开当前数据
* 直接纠正过时的假设
* 用审批和
  [自动审核规则（Auto-review rules）](https://docs.x.ai/grok-bot/security#approvals-and-auto-review)来支撑安全边界，
  而不是仅靠记忆

Bot 有各自的角色和会话，但它们共享计算机。它们
可以通过私信、群聊和共享文件传递上下文。

## 组织一个 Bot 团队

从最小可用的名单开始：

1. 让一个 Bot 负责一个端到端结果。
2. 只有当工作有一个稳定的专家角色时，才添加另一个 Bot。
3. 当交接本身需要可见时，把 Bot 放进一个[群聊](https://docs.x.ai/grok-bot/chat-and-collaboration)。
4. 把外部操作留在明确的审批边界之后。

例如，一个 Website Launch 群可能包括一位发布协调者、一位
内容编辑和一位分析审核者。协调者可以分配工作，
而群会把交接保留在一个会话中。
