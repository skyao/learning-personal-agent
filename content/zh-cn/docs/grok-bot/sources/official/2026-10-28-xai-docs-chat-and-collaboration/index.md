---
title: "文档（docs.x.ai）：对话与协作"
linkTitle: "docs.x.ai：对话与协作"
date: 2026-10-28
originalTitle: "Message and collaborate"
sourceUrl: "https://docs.x.ai/grok-bot/chat-and-collaboration"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [功能更新, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 文档「Work」和帮助页「群聊」与这页部分重合。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：这页讲用户与 Bot 对话的各种方式：@ 提及、听写、语音通话（一次只能和一个 Bot 通话）、Bot 发来的语音备忘。Bot 发邮件或 Slack 消息前默认先出草稿卡，需用户批准；每个 Bot 可以关掉草稿，但 Bot 从自己邮箱主动发出的邮件（如例程发的）一律先成草稿。在 X Chat 里也能与 Bot 对话，前提是 X 的 Premium、Super 或 Ultra 订阅（Plus 不含），并把 Grok 账号连上 Cursor 账号。群聊可放 2 到 6 个 Bot，群里不出现审批卡和密钥请求，Bot 之间只传文本；每条 Bot 回复都计用量，没有禁止 Bot 互相发消息的开关。

**保留理由**：补充了草稿审批的默认规则、X Chat 入口的条件和群聊的限制，这些是 Grok Bot 对外通信控制的具体做法。

---

发消息与协作

Grok Bot 的设计目标是让人感觉像在给同事发消息。请求可以保持自然，但要明确结果和决策边界：Bot 可以更改什么，以及在哪里必须停下来等你。

## 给 Bot 发消息

从侧边栏打开一个 Bot 并输入消息。你可以：

* 粘贴文本、链接和图片
* 附加本地文件
* 向输入框听写
* 开始语音聊天
* 播放 Bot 发来的语音备忘
* 按名称请求已保存的[技能（skill）](https://docs.x.ai/grok-bot/skills-routines-and-automations)
* 用 `@` 提及 Bot、群组、例程或应用
* 回复某条特定消息
* 对消息作出回应
* 在工作进行中发送另一条指令

对话记录会在普通消息旁显示工具活动、计算机使用、创建的文件、问题、批准请求和语音备忘。

### 听写消息

语音输入会把你的话转成输入框中的文字。你可以阅读、编辑，并像其他消息一样发送，Bot 用文字回复。

在桌面端，在输入框中选择 **开始语音输入（Start voice input）**，或在提示框聚焦时按 `Cmd/Ctrl+D`。你也可以在说话时按住这些键。

在 iPhone 和 Android 上，使用输入框中的 **开始听写（Start dictation）**。开始语音聊天前请先停止听写。见 [Grok Bot for Mobile](https://docs.x.ai/grok-bot/mobile)。

### 播放语音备忘

Bot 可以在对话中用语音备忘回复。选择 **播放语音备忘（Play voice memo）** 收听，选择 **暂停语音备忘（Pause voice memo）** 停止，展开备忘可阅读文字记录。

### 开始语音聊天

语音聊天是与一个 Bot 的实时口头对话：Bot 大声回答，并持续聆听直到你挂断。语音聊天可在桌面应用和手机应用中使用。

1. 打开与该 Bot 的聊天，让输入框保持为空。
2. 选择输入框中的波形按钮 **开始语音聊天（Start voice chat）**。
3. 如果你的电脑或手机询问，请允许麦克风访问。

通话在桌面端显示 **正在连接…（Connecting…）**，在手机上显示 **正在呼叫…（Calling…）**，随后 Bot 开始说话。**开始语音聊天** 只在输入框为空时显示；如果输入框为空却仍看不到它，请更新 Grok Bot。通话期间，应用显示 **语音聊天（Voice chat）**，桌面端侧边栏可显示 **语音聊天进行中（Voice chat in progress）**。

通话中，你可以 **静音（Mute）** 或 **取消静音（Unmute）** 麦克风、**挂断（Hang up）**，或选择 **显示文字记录（Show transcript）** 边听边读。与自己 Bot 通话时，**显示设置（Show settings）** 可更改 **语音（Voice）**、**速度（Speed）** 和 **语言（Language）**；**自动检测（Auto-detect）** 会根据你说的话选择语言。通话进行时你可以打开其他聊天；桌面端选择 **返回语音聊天（Return to the voice chat）** 即可返回。同一时间只能进行一个语音聊天，因此开始另一个会询问 **结束当前语音聊天？（End the current voice chat?）**；选择 **结束并聊天（End and Chat）** 切换。

语音聊天一次只与一个 Bot 进行，不能在群聊中使用；请打开该 Bot 自己的聊天开始通话。桌面端还可以在你与队友[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)的聊天中与其语音通话。

如果连接中断，Grok Bot 会先自行尝试重连，因此短暂中断通常无需你操作就能恢复。如果无法恢复，通话会以 **语音聊天失败（Voice chat failed）** 结束，提示可能是 **连接丢失（Connection lost）**、**无连接（No connection）** 或 **通话意外结束（The call ended unexpectedly）**。选择 **关闭（Dismiss）**，检查网络连接，然后再次选择 **开始语音聊天**。

如果 Grok Bot 说麦克风访问被拒绝，请在系统设置中允许它使用麦克风。如果它说找不到麦克风，请连接一个再试。要选择桌面应用使用哪个麦克风，请打开 **设置（Settings）**，在 **麦克风（Microphone）** 下选择一个。

通话结束时，对话中会出现一张 **语音聊天** 卡片，显示通话时长；打开它可阅读完整文字记录。如果通话留下了要做的工作，Bot 可能会在聊天中跟进后续步骤或结果。Grok Bot 可能会问 **通话怎么样？（How was the call?）**；选择 **好（Good）** 或 **差（Bad）** 发送反馈。

### 发送前审查草稿

当 Bot 为你准备电子邮件或 Slack 消息时，对话中会显示可编辑的草稿。审查收件人和正文，然后选择 **发送（Send）**；桌面应用中的 Slack 草稿则选择 **发送消息（Send message）**。选择 **丢弃（Discard）** 放弃草稿。

默认情况下，Bot 会起草外发消息供你审查。草稿卡显示 **需要批准（Needs approval）**。如果你更希望 Bot 不准备草稿直接发送，请在其某个草稿上打开该菜单并选择 **为此 Bot 禁用草稿（Disable drafts for Bot）**。之后 Bot 会直接发送，但仍受你的[自动审查（Auto Review）](https://docs.x.ai/grok-bot/approvals-security-and-privacy#configure-auto-review)设置约束。该选择只适用于那个 Bot，且只有其所有者能看到；群聊中不提供此选项。来自 Bot [自己的地址](https://docs.x.ai/grok-bot/computer-and-apps#give-your-bots-an-email-address)、且不是你通过聊天请求的电子邮件（例如例程发出的邮件）始终会作为草稿等待。要恢复草稿，请在草稿卡上选择 **需要批准**，或询问 Bot。如果更改未保存，卡片会显示 `Couldn't save. Try again.`；选择 **重试（Retry）**。

### 改变进行中工作的方向

优先级变化时，发送一条新消息。你发来的直接消息优先于后台工作，可以改变当前这一轮的方向。

当工作应立即结束时，发送一条直接的「立即停止」消息。这不会撤销 Bot 已经完成的动作。

### 在 X Chat 中聊天

你也可以在 X Chat 中与你的 Bot 聊天，包括 iOS 和 Android 上的 X 应用以及 x.com。它们与你在 Grok Bot 应用中使用的 Bot 相同。X Chat 支持正在逐步推出，因此即使你的方案包含它，也可能尚未对你显示；它需要最新版本的 X 应用。

你需要一个包含 Grok Bot 的方案。在 [The X Subscription](https://docs.x.ai/x-subscription/overview) 上，即 **Premium**、**Super** 或 **Ultra**；**Plus** 不包含 Grok Bot。包含 Grok Bot 的旧版 Cursor 方案，以及已关联的 SuperGrok 或 X Premium+ 账户，也可以使用。见 [Grok Bot on The X Subscription](https://docs.x.ai/x-subscription/grok-bot)。

你的 Grok 账户还需要连接到 Cursor 账户。从 X Chat 连接只适用于个人账户。如果你的电子邮件位于公司管理的域名下、你的 Cursor 账户属于某个团队，或你的 Cursor 账户处于[旧版按请求计费方案](https://cursor.com/docs/models-and-pricing#legacy-request-based-pricing)，则无法使用。如果某个 Cursor 账户已经使用你的电子邮件，你需要先同意才能连接。

| 情况 | 该怎么做 |
| --- | --- |
| 你的方案不包含 Grok Bot | 在 The X Subscription 上选择 **Premium** 或更高等级。 |
| 你的 Cursor 账户或其团队使用 Privacy Mode (Legacy) | 把你的 Cursor 账户切换到 Privacy Mode。若属于团队，由团队管理员更改团队的隐私设置。 |
| 你的 Cursor 账户处于旧版按请求计费方案 | Grok Bot 在旧版按请求计费方案中不可用。 |
| 你的电子邮件位于公司管理的域名下，或你的 Cursor 账户属于某个团队 | 无法从 X Chat 连接。请改用 Grok Bot 应用中的 Grok Bot。 |
| 你的 Grok 账户电子邮件未验证 | 在 Grok 上验证你的电子邮件，然后重试。 |
| 多个 Cursor 账户使用你的电子邮件 | 带上该电子邮件地址[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。 |
| 你的 Grok Bot 用量已用完 | 见 [Grok Bot 用量如何计算？](https://cursor.com/help/grok-bot/plans#how-does-grok-bot-usage-work) |
| 你的 Bot 没有出现在 X Chat 中 | 把 X 应用更新到最新版本，然后退出并重新打开。 |
| 你看到的不是自己的 Bot 而是一个新 Bot，或点击你的 Bot 显示 **出错了（Something went wrong）** | 你的 X 账户可能连接到了另一个 Grok 账户。请按下面的步骤操作。 |

X Chat 使用你的 X 账户所连接的那个 Grok 账户。如果你有多个 Grok 账户，它可能不是你配合 Grok Bot 使用的那个，重试也没有用。要把你的 X 账户连接到配合 Grok Bot 使用的 Grok 账户：

1. 在浏览器中，用你配合 Grok Bot 使用的 Grok 账户登录 [accounts.x.ai](https://accounts.x.ai)。
2. 在同一浏览器中，用你的 X 账户登录 [x.com](https://x.com)。
3. 打开 [x.com/i/jf/grok/entry](https://x.com/i/jf/grok/entry)。选择关联另一个账户，然后为你登录的 Grok 账户允许访问。
4. 退出并重新打开 X 应用，或重新加载 x.com，然后再次打开你的 Bot。

如果该 Grok 账户已经连接到另一个 X 账户，这样做不会生效。如果这些都不符合，请带上你的 X 用户名和 Grok 账户的电子邮件[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。

## 开始群聊

当多个 Bot 需要同一个共享结果和可见的交接时，请使用群组。你也可以添加队友[与你共享](https://docs.x.ai/grok-bot/shared-bots)的 Bot，但不能与在你自己的计算机上运行的 Bot 放在一起。

1. 选择 **新建聊天（New chat）**，按 `Cmd/Ctrl+Shift+N`，或用 `Cmd/Ctrl+K` 打开命令面板并选择 **新建群聊（New group chat）**。
2. 在 **收件人（To:）** 字段中，添加两到六个 Bot。
3. 打开该群组，然后按需编辑自动生成的名称。
4. 描述共享结果以及下一步由谁负责。

在 iPhone 或 Android 上，使用 **+ → 新建群聊（New Group Chat）**。群成员之后可以编辑。

在桌面端重命名群组，请在侧边栏右键点击它并选择 **重命名聊天（Rename chat）**，或点击聊天顶部的群组名称，再点击详情中的名称进行编辑。在手机上，点击聊天顶部的群组名称，点击 **编辑（Edit）**，更改 **名称（Name）**，然后点击 **完成（Done）**。要改变群组的用途，请告诉群里的 Bot。

群聊没有针对单个 Bot 的 **通知（Notifications）** 开关。见[控制通知](https://docs.x.ai/grok-bot/settings-and-notifications#control-notifications)。

### 指定消息对象

* 正常书写，让参与的 Bot 决定谁应回复。
* 当某位成员负责该请求时，输入 `@` 并选择一个 Bot。
* 在某个 Bot 的消息上选择 **回复（Reply）**，把你的回答直接发给该 Bot。
* 当请求确实需要每个 Bot 参与时，提及多个 Bot。
* 仅在需要全组更新时谨慎使用 `@everyone`。

Bot 可以往群里发消息，并在彼此之间传递工作。一个有用的启动方式是给每个阶段指定一位负责人：

> @Researcher gather the source material and link every claim. @Writer turn the
> findings into a launch draft. @Reviewer check the draft against the sources
> and list only blocking issues. Do not publish anything.


你在群组中的消息可以包含附件。Bot 在群里的回复可以包含文件、问题和表单，就像一对一对话中一样；你对问题或表单的回答会回到提出它的 Bot。批准请求、密钥和登录请求，以及电子邮件或 Slack 草稿不会出现在群组中。Bot 发到群组的交接消息只有文本，因此当另一位成员必须查看图片时，Bot 应直接把图片发给该 Bot。

### 让回复留在群组里

当你在群聊中书写时，Bot 会在那里回答。Bot 也可以在自己的聊天中给你发消息，或给另一个 Bot 发消息交接工作；这些消息会出现在 Bot 自己的聊天中，而不是群组里。

要让某个 Bot 的回复留在群组里，请在群里告诉它：「在群里这里回复。不要就这件事私下给我发消息。」要让它成为长期规则，请让每个 Bot 记住它：「记住：在群聊中，在群里回复。」

### 阻止 Bot 互相发消息

没有用于此的开关。Bot 会互相发消息来交接工作，并遵循你对此的指示。

1. 在聊天中告诉 Bot，例如：「不要给其他 Bot 发消息。先问我。」
2. 要让规则保持，请让每个 Bot 记住它。
3. 如果某个 Bot 不断开始新工作，打开该 Bot 的聊天并要求它停止。

要让某个辅助 Bot 安静下来又不想删除它，可以关闭其通知或隐藏它。每条 Bot 回复都计入你的用量，包括群组中的回复和 Bot 之间的消息，因此群里的 Bot 越少，回复就越少。

## 让 Bot 交接工作

一个 Bot 可以向另一个 Bot 发送异步消息。接收的 Bot 会醒来、处理请求，并可以稍后回复。你可以在对话中看到这次交接。

这在以下情况下有用：

* 一个 Bot 负责源系统，另一个负责交付物
* 专家应审查草稿
* 阻塞项属于另一个角色
* 长时间运行的工作应继续，而无需你协调每一步

在每个阶段要求单一负责人。并行交接会产生重复工作和嘈杂的更新。

一次交接需要某个 Bot 在那一轮代表一个人行事。你在哪里与它对话，以及它是个人 Bot 还是[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)，决定了这一点：

| Bot | 你在哪里请求 | 它能给其他 Bot 发消息吗？ | 代表谁 | 回复落在哪里 |
| --- | --- | --- | --- | --- |
| 个人 Bot | 应用，或你与它的 Slack 私信 | 能 | 你 | 应用聊天，不是 Slack |
| 个人 Bot | Slack 频道话题（thread） | 不能 | 没有人，话题是共享的 | Bot 说它不能这样做 |
| 共享 Bot | Slack 频道话题或 Slack 私信 | 能，发给那个人自己的 Bot | 提及它的队友 | 同一个 Slack 话题 |

要从 Slack 频道在 Bot 之间交接工作，请共享一个 Bot 并将它添加到 Slack。共享 Bot 有自己的 Slack 应用和句柄（handle），频道中的任何人都可以给它工作。见[如何把共享 Bot 添加到 Slack？](https://docs.x.ai/grok-bot/shared-bots#how-do-i-add-a-shared-bot-to-slack)

## 使用话题与回应

当反馈针对某一个结果或某一个批准请求时，请在话题（thread）中回复。这样主对话记录保持聚焦，同时保留决策的上下文。

用回应（reactions）做轻量确认。当 Bot 需要更改后的指令时，请用书面回复；单靠一个回应不应承载安全关键的决定。

## 查找之前的工作

使用搜索或命令面板来：

* 在 Bot 和群组之间切换
* 查找之前的消息
* 查找文件、链接和例程
* 打开设置和常用操作
* 跳回对话中匹配的位置

搜索的可用性在逐步推出期间可能不同。如果跨对话结果不可用，请打开相关 Bot 并使用其对话历史。

按 `Cmd/Ctrl+K` 打开搜索面板，或按 `Cmd/Ctrl+Shift+F` 搜索 Bot。完整的桌面端列表见[键盘快捷键](#keyboard-shortcuts)。

## 键盘快捷键

这些快捷键在 Grok Bot 桌面应用中有效。除非某行另有说明，macOS 上使用 `Cmd`，Windows 和 Linux 上使用 `Ctrl`。

* 跳转到 / 搜索面板：`Cmd/Ctrl+K`
* 搜索 Bot：`Cmd/Ctrl+Shift+F`
* 新建 Bot：`Cmd/Ctrl+N`
* 新建群聊：`Cmd/Ctrl+Shift+N`
* 显示所有键盘快捷键：`Cmd/Ctrl+/`
* 在此聊天中查找：`Cmd/Ctrl+F`
* 紧凑侧边栏：`Cmd/Ctrl+B`
* 聚焦提示框：`Cmd/Ctrl+I`
* 将选中文本添加到聊天：`Cmd/Ctrl+L`，未选中任何内容时会聚焦提示框
* 侧边栏 Bot 1–9：`Cmd/Ctrl+1` 到 `Cmd/Ctrl+9`
* 上一个 / 下一个 Bot：`Alt+↑` / `Alt+↓`
* 在访问历史中后退 / 前进：`Cmd/Ctrl+[` / `Cmd/Ctrl+]`
* 循环切换 Bot：`Control+Tab` / `Control+Shift+Tab`（始终是 Control，macOS 上也是如此）
* 连接应用：`Cmd/Ctrl+Shift+M` 或 `Cmd/Ctrl+Shift+W`
* 切换 Bot 设置：`Cmd/Ctrl+Shift+,`
* 对话详情：macOS 上为 `Cmd+Shift+I` 或 `Cmd+Alt+B`；Windows 和 Linux 上为 `Ctrl+Alt+B`
* 发送：在输入框中按 `Enter`，或在任意位置按 `Cmd/Ctrl+Enter`
* 换行：`Shift+Enter`
* 向输入框听写：提示框聚焦时按 `Cmd/Ctrl+D`
* 开始语音聊天：在输入框中选择 **开始语音聊天**；没有快捷键
* 打开设置：`Cmd/Ctrl+,`
* 放大、缩小或重置缩放：`Cmd/Ctrl+=` / `Cmd/Ctrl+-` / `Cmd/Ctrl+0`
* 全屏：`F11`；macOS 上也可用 `Control+Cmd+F`

要查看应用中的每个快捷键，请打开账户菜单并选择 **支持 → 键盘快捷键（Support → Keyboard shortcuts）**，或按 `Cmd/Ctrl+/`。

## 保持对话有效

* 先说你需要的成果，而不是详细模仿每一次点击。
* 链接到真实来源（source of truth）。
* 说明 Bot 可以更改什么、什么需要批准。
* 要求证据——链接、截图或简短的操作日志。
* 明确纠正长期偏好。
* 当对话已经转为一个不同的长期工作时，请开启话题或新建 Bot。

附件见[文件与结果](https://docs.x.ai/grok-bot/files-and-results)，可重复的工作见[技能与例程](https://docs.x.ai/grok-bot/skills-routines-and-automations)，在授权外部操作前见[批准、安全与隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy)。
