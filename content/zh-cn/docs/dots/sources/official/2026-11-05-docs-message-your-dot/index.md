---
title: "给你的 dot 发消息"
linkTitle: "文档：消息渠道"
date: 2026-11-05
originalTitle: "Message your dot"
sourceUrl: "https://learn.chatgpt.com/docs/dots/channels"
altUrls: ["https://learn.chatgpt.com/codex/dots/channels"]
publisher: "OpenAI（ChatGPT Learn）"
language: en
fidelity: 全文翻译
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期；按规则取收集日期"
tags: [功能更新, 设备, 记忆与上下文]
products: [dots]
---

{{< source-info >}}

**收录说明**：原页面中的通话界面和 Slack 界面是界面示意组件，以下整理为「界面示意」段落。

你通过每一种已连接的联系方式联系到的都是同一个 dot。切换渠道不会重置它的记忆。Slack 和 Teams 中的对话只显示在那里交换的消息；它们不会镜像来自其他渠道的每一条消息。你的 dot 可以跨这些对话使用相关的上下文。在把私人对话中的信息分享给其他人之前，它会确认你是否允许。请参阅[上下文与记忆](https://learn.chatgpt.com/codex/dots/tasks-and-memory#context-and-memory)。

打开你的 dot 的个人资料，选择**添加**（Add），查看并连接你可用的联系方式。应用和你的计算机需要单独连接，才能供你的 dot 工作使用。

## ChatGPT 与语音

在 ChatGPT 移动应用、桌面应用或桌面浏览器中创建你的 dot、给它发消息或打电话。不支持移动端网页。

要给你的 dot 打电话，打开它的对话并选择电话按钮。在桌面应用中，你也可以在它的个人资料中选择**通话**（Call）。你可以口头讲清一个请求、澄清一个决定，或者询问进展。通话时你可以打字发消息，你的 dot 也可以给你发消息，告知进展或提出问题。结束通话会结束语音对话；你分配的工作可以继续进行。由你的 dot 发起的通话计划在发布之后推出。

（界面示意：今天 9:41 AM。用户：「Help me prepare for tomorrow’s launch review.」（帮我准备明天的发布评审。）dot：「I’ll pull together the launch checklist, open issues, and decisions that need your input.」（我会汇总发布检查清单、未解决的问题，以及需要你意见的决定。）用户：「Focus on blockers. Keep the readout to five minutes.」（重点关注阻塞项。汇报控制在五分钟以内。）dot：「The mobile sign-in issue is still open. I’m preparing a short brief with the impact, owner, and decision needed for each blocker.」（移动端登录问题仍未解决。我正在准备一份简短的简报，列出每个阻塞项的影响、负责人和需要做的决定。）输入框：发送消息。通话窗口：**Alfred** 02:34。）

在和你的 dot 通话时，你可以继续在聊天中打字。这是分享链接或图片之类上下文的好方法。

## Slack 与 Teams

你可以在 Slack 和 Microsoft Teams 中给你的 dot 发消息。在你的 dot 的个人资料中连接这种联系方式。在 Slack 中，你可以发送私信，或者把你的 dot 加入一个频道，在某个话题串中提及它。

默认情况下，你的 dot 在 Slack 中只回应你。你可以指示它与其他人互动。现有的权限和安全防护仍然适用于它分享和做的事情。在频道中回复之前，你的 dot 可以私下给你发消息，询问你愿意分享哪些内容。

告诉你的 dot 你希望在哪里收到不同的更新。例如，把例行进展留在 ChatGPT 里，让它把需要决定的事带到 Slack 找你。

对于监控，请指明要检查哪些频道、关注什么，以及什么时候通知你。让你的 dot 确认这个周期性任务。把它加入一个频道并不会建立监控时间表。

（界面示意：Slack 频道。**Alex Chen**，9:12 AM：「Keep an eye out on this and flag launch risks」（盯着这个，标出发布风险）。转发的消息：**Maya Patel** 发布于 #website-launch，昨天 9:05 AM：「Friday launch plan: staging ready Wednesday, QA on Thursday, publish Friday. Owners and dependencies are in the launch checklist.」（周五发布计划：周三预发布环境就绪，周四做 QA，周五发布。负责人和依赖项见发布检查清单。）今天，**achen-alfred**（智能体），9:03 AM：「Staging moved to Thursday, leaving one day for QA. Mobile testing still has no owner. Friday’s launch is at risk. I drafted a follow-up for your review.」（预发布环境推迟到了周四，只给 QA 留了一天。移动端测试仍然没有负责人。周五的发布有风险。我起草了一条跟进消息供你审阅。）2 条回复。话题串：**Alex Chen**，9:08 AM：「can you show me draft and check on who is doing the mobile QA testing」（能给我看看草稿吗，再查一下谁在做移动端 QA 测试）；**achen-alfred**（智能体），9:09 AM：「Added the noon deadline and a request to prioritize sign-in testing. The draft is ready for you to review. I haven’t sent it.」（已加上中午的截止时间，并请求优先测试登录。草稿已准备好供你审阅。我还没有发送。）按钮：审阅跟进草稿。）

把消息直接转发给你的 dot，就可以让它处理任务，或者在话题串中进行后续对话。

## iOS 小组件和快捷指令

从你的 iPhone 主屏幕打开你的 dot，或者用苹果的快捷指令（Shortcuts）选择开始对话的方式。使用最新版本的 ChatGPT iOS 应用，并登录你设置 dot 的那个账户。这些功能随 ChatGPT for iOS 1.2026.279 推出，需要[具备 dot 访问资格](https://learn.chatgpt.com/codex/dots#access)。

### 添加「你的 dot」小组件

![](images/portrait-alfred.webp) Alfred

**你的 dot**（Your dot）小组件在一个小的主屏幕小组件中显示你的 dot 的名字和外观。

1. 长按主屏幕上的空白区域，然后选择**编辑** > **添加小组件**。
2. 找到 **ChatGPT**，选择**你的 dot**，然后选择**添加小组件**。
3. 放置小组件，然后选择**完成**。

轻点你的 dot，就会打开它的对话，消息输入框已经就绪。例如，在一次会议之后打开它，把一个决定补充到你们已经在一起进行的工作中。

要添加消息和通话控件，长按小组件，选择**编辑小组件**，然后打开**显示快捷按钮**。这项设置默认关闭。消息按钮打开输入框。电话按钮在可以通话时出现，用于开始一次通话或回到正在进行的通话。

如果小组件要求你登录或设置你的 dot，打开 ChatGPT 完成这一步。添加小组件并不会让一个本来没有 dot 访问资格的账户获得访问权。

### 创建一个苹果快捷指令

ChatGPT 提供一个**打开你的 dot**（Open your dot）操作，有三种**模式**（Mode）可选：

| 模式 | 作用 |
| --- | --- |
| **消息**（Messaging） | 打开你的 dot 的对话，用于输入消息。这是默认模式。 |
| **听写**（Dictation） | 开始语音转文字输入，用于给你的 dot 发消息。 |
| **通话**（Call） | 开始一次实时语音对话，或回到正在进行的通话。 |

1. 打开苹果的**快捷指令**应用，新建一个快捷指令。
2. 添加一个操作，搜索**打开你的 dot**，然后选择 ChatGPT 的这个操作。
3. 选择你的 dot，并选择一种**模式**。
4. 命名并保存快捷指令，然后运行它，以该模式打开 ChatGPT。

例如，保存一个名为「Talk to my dot」（和我的 dot 说话）、使用**通话**模式的快捷指令，用来口头检查进展。如果是快速口述一条笔记，就改用**听写**。在通话进行中无法使用听写。

在带有操作按钮的 iPhone 上，打开**设置** > **操作按钮**，选择**快捷指令**，然后选择**选取快捷指令**，再选择你保存的快捷指令。你也可以从苹果的快捷指令主屏幕小组件运行已保存的快捷指令。

这个操作会打开 ChatGPT，并需要身份验证。如果你切换了账户，而某个已保存的快捷指令提示这个 dot 已不可用，请登录拥有它的那个账户。

## 短信

通过 iMessage 或 Android 上的 RCS 联系你的 dot。短信支持一对一对话。它正在以测试版的形式向美国的 ChatGPT Pro 用户推出。

你的 dot 可以使用来自你在 ChatGPT 和其他已连接渠道中的对话的相关上下文，以及你已连接的插件。

### 设置短信

1. 在 ChatGPT 移动应用、桌面应用或桌面网页浏览器中打开你的 dot 的个人资料，选择**短信**（Texting）。
2. 输入你的电话号码，并按步骤进行验证。
3. 收到你的 dot 的联系人名片后保存它。给你的 dot 发一条消息即可开始聊天。

对于 iMessage，请确保你是从验证过的电话号码发送消息。在 Android 上，请在你的消息应用中启用 RCS。

你可以发送文字、照片和语音消息。如果你的 dot 需要批准，它会给你发一个链接，让你在 ChatGPT 中查看该请求。

你的 dot 会利用你们对话中的上下文来选择在哪里联系你。你也可以让它使用某个特定渠道，比如在有事情需要你关注时给你发短信，把例行更新留在 ChatGPT 里。

你的 dot 只能给你发短信，也只有你能给你的 dot 发短信。设置短信不会让你的 dot 或 OpenAI 访问你的其他短信对话。

目前短信不支持群聊、电话和 FaceTime。你可以在 ChatGPT 中给你的 dot 打电话。
