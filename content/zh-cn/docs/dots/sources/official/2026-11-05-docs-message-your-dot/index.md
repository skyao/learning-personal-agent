---
title: "给你的 dot 发消息"
linkTitle: "文档：消息渠道"
date: 2026-11-05
originalTitle: "Message your dot"
sourceUrl: "https://learn.chatgpt.com/docs/dots/channels"
altUrls: ["https://learn.chatgpt.com/codex/dots/channels"]
publisher: "OpenAI（ChatGPT Learn）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标日期；按规则取收集日期；2026-11-28 发现原文更新：「Slack 与 Teams」一节改为只讲 Slack，全文不再提 Microsoft Teams；短信测试版从美国扩到美国、加拿大、墨西哥；新增「Reply and share on iOS」（从通知回复、用分享表单发送内容）"
tags: [交互渠道, 设备, 功能更新]
products: [dots]
---

{{< source-info >}}

**收录说明**：OpenAI 在 ChatGPT Learn 上发布的 dots 文档，文档不标日期，页面日期取第一轮收集日期 2026-11-05。第一轮收集时直接翻译，原文未单独存档；2026-11-28 按新流程重新抓取（直接下载），原文存于本目录的 original.md（网站上不显示）：删去占位图、头像缩写和格式工具栏残留；通话窗口与 Slack 窗口各整理为一段「（界面示意：……）」；页内相对链接改为绝对地址。新版有新增和改写，旧译文已删去（由 git 保留），已翻译。

**内容摘要**：无论通过哪个渠道联系，面对的都是同一个 dot，切换渠道不会重置它的记忆。可以在 ChatGPT 移动应用、桌面应用和桌面浏览器中给 dot 发消息或打电话，不支持移动端网页。在 Slack 中 dot 默认只回应用户本人，要它监控频道，需要说明频道、关注点和通知时机。iOS 上可以从通知直接回复、用分享表单把内容发给 dot，还有「Your dot」小组件和「Open your dot」快捷指令（消息、听写、通话三种模式）。短信通过 iMessage 或 Android 的 RCS 收发，只支持一对一，正以测试版向美国、加拿大、墨西哥的 ChatGPT Pro 用户推出。

**保留理由**：这一页列出 dots 各联系渠道的可用范围和限制；新旧版对照可以看出 Teams 渠道撤下、短信扩展到加拿大和墨西哥。

---

你通过每一个已连接的联系方式联系到的都是同一个 dot。切换渠道不会重置它的记忆。Slack 对话显示的是在那里交换的消息；它们不会镜像其他渠道的每一条消息。你的 dot 可以在这些对话之间使用相关的上下文。在把私人对话中的信息分享给其他人之前，它会确认你已允许这样做。见[上下文与记忆](https://learn.chatgpt.com/codex/dots/tasks-and-memory#context-and-memory)。

打开你的 dot 的资料页，选择 **Add**，查看并连接你可用的联系方式。应用和你的电脑要分别连接，才能供你的 dot 工作使用。

## ChatGPT 与语音

在 ChatGPT 移动应用、桌面应用或桌面浏览器中创建、给 dot 发消息，或给 dot 打电话。不支持移动端网页。

要给 dot 打电话，打开它的对话并选择电话按钮。在桌面应用中，你也可以在它的资料页选择 **Call**。通过通话说明请求、澄清一个决定，或询问进度。你可以在说话时输入消息，dot 也可以用消息向你汇报进度或提出问题。结束通话即结束语音对话；你已指派的工作可以继续。由 dot 发起的通话计划在正式上线后提供。

（界面示意：通话界面；Today 9:41 AM；帮我准备明天的发布评审。；我会把发布清单、未解决的问题，以及需要你拍板的决定整理出来。；聚焦阻塞项。汇报控制在五分钟内。；移动端登录的问题仍未解决。我正在准备一份简短说明，包含每个阻塞项的影响、负责人和需要的决定。；Alfred 02:34）

在与 dot 通话期间，你可以继续在聊天中输入。这是分享链接或图片等上下文的好办法。

## Slack

在 dot 的资料页连接 Slack。之后你可以给 dot 发私信，或把它加入某个频道并在线程中提及它。

默认情况下，dot 在 Slack 中只回复你。你可以指示它与其他人员互动。共享内容与执行操作仍受现有权限和防护措施约束。dot 可以在频道中回复之前，先私下给你发消息，询问你愿意分享什么。

告诉 dot 你希望不同类型的更新发到哪里。例如，把日常进展留在 ChatGPT，让它把需要决策的事项带到 Slack 找你。

要做监控，需指明检查哪些频道、关注什么，以及何时通知你。请让 dot 确认这项重复任务。把 dot 加入频道并不会建立监控时间安排。

（界面示意：Slack 窗口；achen-alfred；Alex Chen9:12 AM；留意这件事，标出发布风险；Maya PatelPosted in #website-launch · Yesterday at 9:05 AM；周五发布计划：预发布环境周三就绪，周四 QA，周五发布。负责人与依赖项在发布清单里。；1 replyLast reply yesterday；Today；achen-alfred（AGENT）9:03 AM；预发布环境推迟到周四，QA 只剩一天。移动端测试仍没有负责人。周五的发布有风险。我起草了一份跟进消息供你审阅。；2 replies；Message achen-alfred；Thread；achen-alfred（AGENT）9:03 AM；预发布环境推迟到周四，QA 只剩一天。移动端测试仍没有负责人。周五的发布有风险。我起草了一份跟进消息供你审阅。；2 replies；Alex Chen9:08 AM；能把草稿给我看看，并查一下谁在做移动端 QA 测试吗；achen-alfred（AGENT）9:09 AM；加上了中午的截止时间，并请求优先做登录测试。草稿已备好，等你审阅。我还没有发送。；Review draft follow-up；Reply…；Also send as direct message）

你可以把消息直接转发给 dot，让它处理任务或在线程中继续对话。

## 在 iOS 上回复与分享

要从通知回复，按住来自 dot 的通知，输入你的回复，然后点 **Send**。

要和 dot 分享一张照片，打开该照片，点 **Share**，选择你的 dot。在编辑窗口中查看该照片，如果需要可以添加一条消息，然后点 **Send**。你也可以分享其他使用 iOS 分享表单的应用中的内容。

## iOS 小组件与快捷指令

从 iPhone 主屏幕打开你的 dot，或用 Apple 快捷指令选择以何种方式开始一段对话。请使用最新的 ChatGPT iOS 应用，并登录你创建 dot 的那个账户。这些功能随 ChatGPT for iOS 1.2026.279 逐步推出，并且需要 [dot 访问权限](https://learn.chatgpt.com/codex/dots#access)。

### 添加「Your dot」小组件

![](images/portrait-alfred.webp)  Alfred

**Your dot** 小组件在主屏幕的一个小尺寸小组件中显示 dot 的名称和外观。

1. 按住主屏幕的空白区域，然后选择 **Edit** > **Add Widget**。
2. 找到 **ChatGPT**，选择 **Your dot**，然后选择 **Add Widget**。
3. 放置小组件，然后选择 **Done**。

点你的 dot 即可打开它的对话，消息编辑框已就绪。例如，开完会之后打开它，把一项决定加入你们已经在共同进行的工作。

要添加消息和通话控件，按住小组件，选择 **Edit Widget**，然后开启 **Show shortcut buttons**。该设置默认关闭。消息按钮会打开编辑框。通话可用时会出现电话按钮，点它可以发起通话或回到正在进行的通话。

如果小组件要求你登录或设置 dot，请打开 ChatGPT 完成该步骤。添加小组件并不会让一个本没有 dot 访问权限的账户获得该权限。

### 创建 Apple 快捷指令

ChatGPT 提供一个 **Open your dot** 操作，含三个 **Mode** 选项：

| 模式 | 作用 |
| --- | --- |
| **Messaging** | 打开你的 dot 的对话，用于输入消息。这是默认模式。 |
| **Dictation** | 启动语音转文字输入，用于给 dot 发消息。 |
| **Call** | 发起实时语音对话，或回到正在进行的通话。 |

1. 打开 Apple 的 **Shortcuts** 应用，新建一个快捷指令。
2. 添加一个操作，搜索 **Open your dot**，选择 ChatGPT 提供的该操作。
3. 选择你的 dot，并选择一个 **Mode**。
4. 命名并保存该快捷指令，然后运行它，以该模式打开 ChatGPT。

例如，保存一个名为「Talk to my dot」的快捷指令，使用 **Call** 模式做一次口头进度询问。想快速留一段口述笔记，则用 **Dictation**。通话进行中无法使用听写。

在带操作按钮的 iPhone 上，打开 **Settings** > **Action Button**，选择 **Shortcut**，再选 **Choose a Shortcut** 并选择你保存的快捷指令。你也可以从 Apple 的 Shortcuts 主屏幕小组件运行已保存的快捷指令。

该操作会打开 ChatGPT，并且需要认证。如果你切换了账户，而已保存的快捷指令提示该 dot 不再可用，请登录拥有它的账户。

## 短信

通过 iMessage 或 Android 上的 RCS 联系你的 dot。短信支持一对一会话。它正以测试版向美国、加拿大和墨西哥的 ChatGPT Pro 用户推出。

你的 dot 可以使用你在 ChatGPT 和其他已连接渠道中的对话里的相关上下文，以及你已连接的插件。

### 设置短信

1. 在 ChatGPT 移动应用、桌面应用或桌面网页浏览器中打开 dot 的资料页，选择 **Texting**。
2. 输入你的手机号码，按步骤完成验证。
3. 收到 dot 的联系人名片后保存它。给 dot 发一条消息即可开始聊天。

使用 iMessage 时，请确保用你验证过的手机号码发送。在 Android 上，请在你的消息应用中启用 RCS。

你可以发送文字、照片和语音消息。如果 dot 需要审批，它会给你发一个链接，让你在 ChatGPT 中查看该请求。

你的 dot 利用你对话中的上下文来决定在哪里联系你。你也可以让它使用某个特定渠道，例如在有事情需要你关注时给你发短信，而把日常更新留在 ChatGPT。

你的 dot 只能给你发短信，也只有你能给你的 dot 发短信。设置短信不会让你的 dot 或 OpenAI 访问你的其他短信对话。

短信目前不支持群聊、电话通话和 FaceTime。你可以在 ChatGPT 中给 dot 打电话。
