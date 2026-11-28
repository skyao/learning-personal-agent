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
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：Shared Bots 改称 Team Bots；新增：手机语音聊天被来电等打断即结束、邮件草稿可带 Bot 准备的文件、Shop with a Bot 购物卡片与下单卡、搜索面板的 Search older"
tags: [功能更新, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 文档「Work」和帮助页「群聊」与这页部分重合。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：这页讲用户与 Bot 对话的各种方式：@ 提及、听写、语音通话（一次只能和一个 Bot 通话；手机应用 1.18 起，来电、FaceTime 或其他应用占用音频时语音聊天会结束，需重新点 **Start voice chat**）、Bot 发来的语音备忘。Bot 发邮件或 Slack 消息前默认先出草稿卡，需用户批准；Gmail 或 Outlook 草稿可带 Bot 准备的文件，文件在草稿后改动则不发送并重新弹出卡片；Bot 从自己邮箱主动发出的邮件（如例程发的）一律先成草稿。在 X Chat 里也能与 Bot 对话，前提是 X 的 Premium、Super 或 Ultra 订阅（Plus 不含），并把 Grok 账号连上 Cursor 账号。**Shop with a Bot** 让 Bot 回复商品卡片并发出含 **Ship to**、**Pay with**、**Total** 的订单卡，只有 Bot 的所有者能付款。群聊可放 2 到 6 个 Bot，群里不出现审批卡、密钥请求和邮件草稿，Bot 之间只传文本；每条 Bot 回复都计用量，没有禁止 Bot 互相发消息的开关。

**保留理由**：补充了草稿审批的默认规则、X Chat 入口的条件和群聊的限制，这些是 Grok Bot 对外通信控制的具体做法。

---

发消息与协作

Grok Bot 的设计目标是让人感觉像在给队友发消息。请求可以保持自然，但要把结果和决策边界说清楚：Bot 可以改动什么，以及它必须在哪里停下来问你。

## 给 Bot 发消息

从侧边栏打开一个 Bot 并输入消息。你可以：

* 粘贴文本、链接和图片
* 附加本地文件
* 在输入框中听写
* 开始语音聊天
* 播放 Bot 发来的语音备忘
* 按名称请求已保存的[技能](https://docs.x.ai/grok-bot/skills-routines-and-automations)
* 用 `@` 提及 Bot、群组、例程或应用
* 回复某条特定消息
* 对消息表态
* 在工作中途再发一条指令

对话记录会把工具活动、计算机使用、创建的文件、问题、审批请求和语音备忘与普通消息一起显示。

### 听写一条消息

语音输入把你说的话转成输入框中的文字。你可以读一遍、修改，然后像其他消息一样发送，Bot 用文字回复。

在桌面端，选择输入框中的**开始语音输入（Start voice input）**，或在提示词获得焦点时按 `Cmd/Ctrl+D`。你也可以边说边按住这些键。

在 iPhone 和 Android 上，使用输入框中的**开始听写（Start dictation）**。开始语音聊天前先停止听写。见 [Grok Bot 移动版](https://docs.x.ai/grok-bot/mobile)。

### 播放语音备忘

Bot 可以在对话中用语音备忘回复。选择**播放语音备忘（Play voice memo）**收听，选择**暂停语音备忘（Pause voice memo）**停止，展开备忘可阅读文字稿。

### 开始语音聊天

语音聊天是与一个 Bot 的实时口语对话：Bot 出声回答，并持续聆听，直到你挂断。语音聊天在桌面应用和手机应用中可用。

1. 打开与该 Bot 的聊天，让输入框保持为空。
2. 选择**开始语音聊天（Start voice chat）**，即输入框中的波形按钮。
3. 如果你的电脑或手机询问，允许麦克风访问。

通话时桌面端显示**正在连接……（Connecting…）**，手机上显示**正在呼叫……（Calling…）**，随后 Bot 开始说话。**开始语音聊天**只在输入框为空时显示；如果输入框为空却仍看不到它，请更新 Grok Bot。通话期间应用显示**语音聊天（Voice chat）**，桌面端侧边栏还可能显示**语音聊天进行中（Voice chat in progress）**。

通话中你可以**静音（Mute）**或**取消静音（Unmute）**麦克风、**挂断（Hang up）**，或选择**显示文字稿（Show transcript）**边听边读。与自己的 Bot 通话时，**显示设置（Show settings）**可更改**语音（Voice）**、**速度（Speed）**和**语言（Language）**；**自动检测（Auto-detect）**根据你说的话选择语言。通话进行时你可以打开其他聊天；桌面端可选择**返回语音聊天（Return to the voice chat）**回去。同时只能进行一个语音聊天，因此开始另一个时会询问**结束当前的语音聊天？**；选择**结束并聊天（End and Chat）**切换。

语音聊天一次只与一个 Bot 进行，不能在群聊中使用；打开该 Bot 自己的聊天才能开始通话。桌面端还可以在自己与队友 [Team Bot](https://docs.x.ai/grok-bot/team-bots) 的聊天中与它语音聊天。

如果连接中断，Grok Bot 会先自行尝试重连，所以短暂中断通常无需你做任何事就能恢复。如果无法恢复，通话以**语音聊天失败（Voice chat failed）**结束，提示可能说**连接已断开（Connection lost）**、**无连接（No connection）**或**通话意外结束（The call ended unexpectedly）**。选择**关闭（Dismiss）**，检查网络连接，再选择**开始语音聊天**。

在手机应用上（1.18 及更高版本，iPhone 和 Android），当来电、FaceTime 或其他应用占用音频时，语音聊天会结束。这与选择**挂断**效果相同，语音聊天不会自行恢复；结束后再选择**开始语音聊天**。Android 上的短暂打断，例如导航提示，只会暂停对话。

如果 Grok Bot 说麦克风访问被拒绝，请在系统设置中允许它使用麦克风。如果说找不到麦克风，请连接一个再试。要选择桌面应用使用哪个麦克风，打开**设置（Settings）**，在**麦克风（Microphone）**下选一个。

通话结束时，对话中会有一张**语音聊天**卡片，带有通话时长；打开它可以读完整文字稿。如果通话留下了待办工作，Bot 可能在聊天中跟进下一步或结果。Grok Bot 可能会问**这次通话怎么样？（How was the call?）**；选择**好（Good）**或**差（Bad）**提交反馈。

### 发送前审阅草稿

当 Bot 为你准备一封邮件或一条 [Slack](https://x.ai/bot/plugin/674) 消息时，对话中可能显示可编辑的草稿。检查收件人和正文，然后选择**发送（Send）**，桌面应用中的 [Slack](https://x.ai/bot/plugin/674) 草稿则是**发送消息（Send message）**。选择**丢弃（Discard）**放弃草稿。

[Gmail](https://x.ai/bot/plugin/45893410) 或 [Outlook](https://x.ai/bot/plugin/57302029) 草稿可以包含 Bot 准备的文件。卡片会列出它们，并随消息一起发送。如果某个文件在草稿准备之后被改动，则什么都不发送，卡片会重新打开供你检查。

Bot 默认把对外发送的消息先做成草稿供你审阅。草稿卡显示**需要批准（Needs approval）**。如果你希望 Bot 不准备草稿而直接发送，打开它某份草稿上的菜单，选择**为该 Bot 关闭草稿（Disable drafts for Bot）**。此后 Bot 直接发送，受你的 [Auto Review](https://docs.x.ai/grok-bot/approvals-security-and-privacy#configure-auto-review) 设置约束。该选择只对该 Bot 生效，且只有它的所有者能看到；群聊中不提供此项。来自 Bot [自己的地址](https://docs.x.ai/grok-bot/computer-and-apps#give-your-bots-an-email-address)、你并未在聊天中要求的邮件（例如例程发出的邮件）总是先作为草稿等待。要恢复草稿，在草稿卡上选择**需要批准**，或直接要求 Bot。如果改动没有保存，卡片显示 `Couldn't save. Try again.`（译注：意为「无法保存，请重试。」）；选择**重试（Retry）**。

### 改变进行中的工作方向

优先级变化时就发一条新消息。你发的直接消息优先于后台工作，可以改变当前轮次的方向。

工作应立即结束时，发一条直接的「立即停止」消息。这不会撤销 Bot 已经完成的操作。

### 在 X Chat 中聊天

你也可以在 X Chat 中与 Bot 聊天，入口是 iOS 和 Android 上的 X 应用以及 x.com。它们与你在 Grok Bot 应用中使用的是同一批 Bot。X Chat 支持正在逐步推出，所以即使你的套餐包含它，可能暂时还看不到，并且需要最新版本的 X 应用。

你需要一个包含 Grok Bot 的套餐。在 [The X Subscription](https://docs.x.ai/x-subscription/overview) 上，即 **Premium**、**Super** 或 **Ultra**；**Plus** 不含 Grok Bot。包含 Grok Bot 的旧版 Cursor 套餐，以及已关联的 SuperGrok 或 X Premium+ 账号也可以。见 [The X Subscription 上的 Grok Bot](https://docs.x.ai/x-subscription/grok-bot)。

你的 Grok 账号还需要连接一个 Cursor 账号。从 X Chat 连接仅适用于个人账号。当你的邮箱属于公司管理的域名、你的 Cursor 账号属于某个团队，或你的 Cursor 账号处于[旧版按请求计费的套餐](https://cursor.com/docs/models-and-pricing#legacy-request-based-pricing)时，此功能不可用。如果某个 Cursor 账号已经使用你的邮箱，需要先征得同意才能连接。

| 情况 | 怎么办 |
| --- | --- |
| 你的套餐不含 Grok Bot | 在 The X Subscription 上选择 **Premium** 或更高档。 |
| 你的 Cursor 账号或其团队使用隐私模式（旧版） | 把你的 Cursor 账号切换到隐私模式。在团队中，由团队管理员更改团队的隐私设置。 |
| 你的 Cursor 账号处于旧版按请求计费的套餐 | Grok Bot 不适用于旧版按请求计费的套餐。 |
| 你的邮箱属于公司管理的域名，或你的 Cursor 账号属于某个团队 | 从 X Chat 连接不可用。请改在 Grok Bot 应用中使用 Grok Bot。 |
| 你 Grok 账号的邮箱未验证 | 先在 Grok 上验证邮箱，再试一次。 |
| 有多个 Cursor 账号使用你的邮箱 | 带上该邮箱地址[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。 |
| 你的 Grok Bot 用量已用完 | 见 [Grok Bot 用量如何计算？](https://grok.com/help/grok-bot/plans#how-does-grok-bot-usage-work) |
| 你的 Bot 没有出现在 X Chat 中 | 把 X 应用更新到最新版本，然后退出并重新打开。 |
| 你看到的是一个新的 Bot 而不是自己的，或者点开自己的 Bot 显示**出了点问题（Something went wrong）** | 你的 X 账号可能连接到了另一个 Grok 账号。按下面的步骤操作。 |

X Chat 使用你的 X 账号所连接的 Grok 账号。如果你有多个 Grok 账号，那个账号可能不是你在 Grok Bot 中使用的账号，反复重试也没有用。要把 X 账号连接到你在 Grok Bot 中使用的 Grok 账号：

1. 在浏览器中，用你在 Grok Bot 中使用的 Grok 账号登录 [accounts.x.ai](https://accounts.x.ai)。
2. 在同一浏览器中，用你的 X 账号登录 [x.com](https://x.com)。
3. 打开 [x.com/i/jf/grok/entry](https://x.com/i/jf/grok/entry)。选择关联另一个账号，然后为你刚登录的 Grok 账号允许访问。
4. 退出并重新打开 X 应用，或重新加载 x.com，然后再打开你的 Bot。

如果该 Grok 账号已经连接到另一个 X 账号，这样做不起作用。如果这些都对不上，请带上你的 X 用户名和 Grok 账号的邮箱[联系支持](https://docs.x.ai/grok-bot/troubleshooting)。

## 用 Bot 购物

让 Bot 找点东西买，它可以用商品卡片回复。打开一个商品可以看到照片、选项、**为什么合适（Why it fits）**和**在哪里买（Where to buy）**，并直接在那里购买。桌面端每张卡片还有**立即购买（Buy now）**，或显示**缺货（Out of stock）**。如果你打开的商品已售罄，选择**到货通知我（Notify me）**，Bot 会建一个例程，在补货时告诉你。

准备购买时，Bot 会发送一张订单卡，包含店铺、商品、**寄送至（Ship to）**、**付款方式（Pay with）**和**总计（Total）**。如果是送礼物，**礼物（Gift）**一行显示送给谁、你的留言、是否附赠礼收据以及何时送达。核对后，选择显示总额的付款按钮，或选择**取消（Cancel）**。取消不会扣款。下单后，卡片显示**已用……支付（Paid with）**。如果订单卡过期，请让 Bot 重新确认价格。只有 Bot 的所有者能支付它的订单。Bot 可用的卡和钱包见[付款](https://docs.x.ai/grok-bot/vault#pay-for-things)。

## 订酒店

告诉 Bot 你要去哪里、大概什么时候，请它找个住处，它会搜索带实时价格的酒店。在 Grok Bot 应用中，它用一张酒店卡片回复，你可以用网格或地图查看。打开一家酒店可以看到照片、房型和价格，以及入住、退房、取消和付款详情，然后选择**预订（Book）**。Bot 会在酒店自己的网站上为你预订，你像其他购物一样在订单卡上批准付款。应用无法显示酒店卡片的地方，Bot 会在回复中列出酒店；要预订其中一家，回复酒店名称即可。

搜索从不下单或留房，最终价格由酒店网站决定，可能与卡片上的不同。只有 Bot 的所有者能用它搜索酒店。如果预订尚未确认，在重复预订同一行程之前，先查看邮箱中的酒店确认信。

## 让 Bot 打电话

Bot 可以替你给商家打电话，例如订位或询问订单，并告诉你结果如何。电话功能仅在美国提供，桌面和手机版 Grok Bot 应用均可用。

首次使用时，Bot 请你同意通话条款，其中包括你只会在美国拨打已同意接听你电话的商家和个人。选择**接受（Accept）**或**拒绝（Decline）**。每次通话前，Bot 显示它将打给谁；选择**拨打（Call）**或**取消（Cancel）**。

通话进行时，卡片显示状态和实时文字稿：

* 选择**结束通话（End call）**挂断。
* 出现**接管（Take over）**时，选择它可自己加入通话。卡片会显示**正在为你接通……（Connecting you…）**，然后显示**已转接给你（Transferred to you）**。
* 如果对方问了 Bot 答不上来的问题，卡片会显示该问题以及你还有多长时间回应。在**你的回答（Your answer）**中输入并选择**发送（Send）**，或选择**跳过（Skip）**。
* 如果 Bot 想在通话中向对方提供更多细节，它会先问你。

通话结束后，卡片显示**已结束（Ended）**，随后是通话时长。之后打开通话卡可以阅读文字稿并播放录音。桌面端卡片的**通话操作（Call actions）**菜单还有**复制文字稿（Copy transcript）**、**导出文字稿（Export transcript）**和**下载录音（Download recording）**。

无论你的隐私设置如何，Bot 拨打的电话都不会用于训练 SpaceXSI 的模型。

## 开始群聊

当多个 Bot 需要同一个共享结果、且交接过程需要可见时，使用群组。你也可以加入队友[分享给你](https://docs.x.ai/grok-bot/team-bots)的 Bot，但不能与运行在你自己电脑上的 Bot 放在一起。

1. 选择**新聊天（New chat）**，按 `Cmd/Ctrl+Shift+N`，或用 `Cmd/Ctrl+K` 打开命令面板并选择**新建群聊（New group chat）**。
2. 在**收件人（To:）**字段中加入两到六个 Bot。
3. 打开该群组，必要时编辑它自动生成的名称。
4. 说明共享结果以及由谁负责下一步。

在 iPhone 或 Android 上，使用 **+ → 新建群聊（New Group Chat）**。群成员之后可以编辑。

在桌面端重命名群组，右键点击侧边栏中的群组并选择**重命名聊天（Rename chat）**，或点击聊天顶部的群组名称，再点击详情中的名称进行编辑。在手机上，点聊天顶部的群组名称，点**编辑（Edit）**，修改**名称（Name）**，再点**完成（Done）**。要改变群组的用途，直接告诉群里的 Bot。

群聊没有按 Bot 设置的**通知（Notifications）**开关。见[控制通知](https://docs.x.ai/grok-bot/settings-and-notifications#control-notifications)。

### 指定消息的接收者

* 正常书写，让参与的 Bot 自行决定由谁回应。
* 当某位队友负责该请求时，输入 `@` 并选择一个 Bot。
* 在 Bot 的消息上选择**回复（Reply）**，把你的回答定向给该 Bot。
* 当请求确实需要每个 Bot 都参与时，提及多个 Bot。
* 克制使用 `@everyone`，用于面向全组的通知。

Bot 可以在群里发帖，并在彼此之间传递工作。一个好的开场会给每个阶段指派一个负责人：

> @Researcher 收集原始材料，为每个论断附上链接。@Writer 把发现写成发布草稿。@Reviewer 对照来源检查草稿，只列出阻塞问题。不要发布任何内容。

你在群里的消息可以带附件。Bot 在那里回复时可以包含文件、问题和表单，与一对一对话一样，你对问题或表单的回答会回到提问的 Bot。审批请求、密钥和登录请求，以及邮件或 [Slack](https://x.ai/bot/plugin/674) 草稿不会出现在群里。Bot 发往群里的交接消息只有文本，所以当某位队友必须查看图片时，Bot 应直接把图片发给另一个 Bot。

### 让回复留在群里

你在群聊中发言时，Bot 在那里回答。Bot 也可以在自己的聊天中给你发消息，或给另一个 Bot 发消息以交接工作；这些消息出现在 Bot 自己的聊天中，不在群里。

要让某个 Bot 的回复留在群里，就在群里告诉它：「在这个群里回复。不要就这件事私下给我发消息。」要让它成为长期规则，请每个 Bot 记住：「记住：在群聊中，在群里回复。」

### 阻止 Bot 互相发消息

没有这样的开关。Bot 之间会发消息交接工作，它们遵循你对此的指示。

1. 在聊天中告诉这些 Bot，例如：「不要给其他 Bot 发消息。先问我。」
2. 要让规则保留下来，请每个 Bot 记住它。
3. 如果某个 Bot 不断开启新工作，打开该 Bot 的聊天，让它停止。

要让一个辅助 Bot 安静下来又不想删除它，可以关掉它的通知或隐藏它。每条 Bot 回复都计入你的用量，包括群里的回复和 Bot 之间的消息，所以群里的 Bot 越少，回复就越少。

## 让 Bot 交接工作

一个 Bot 可以给另一个 Bot 发送异步消息。接收方 Bot 会醒来、处理请求，并可以稍后回复。你可以在对话中看到这次交接。

以下情况适用：

* 一个 Bot 负责某个源系统，另一个负责交付物
* 应由专家审阅草稿
* 某个阻塞项属于另一个角色
* 长期运行的任务应继续，而无需你协调每一步

要求每个阶段只有一个负责人。并行交接会造成重复工作和嘈杂的更新。

交接需要一个在该轮次中代表某个人行动的 Bot。你在哪里与它对话，以及它是个人 Bot 还是 [Team Bot](https://docs.x.ai/grok-bot/team-bots)，决定了这一点：

| Bot | 你在哪里提出 | 它能否给其他 Bot 发消息？ | 代表谁行动 | 回复落在哪里 |
| --- | --- | --- | --- | --- |
| 个人 Bot | 应用，或你与它的 Slack 私信 | 能 | 你 | 应用中的聊天，不是 Slack |
| 个人 Bot | Slack 频道线程 | 不能 | 不代表任何人，线程是共享的 | Bot 说它做不到 |
| Team Bot | Slack 频道线程或 Slack 私信 | 能，发给他本人自己的 Bot | 提及它的那位队友 | 同一个 Slack 线程 |

要从 Slack 频道在 Bot 之间交接工作，请分享一个 Bot 并把它加入 Slack。Team Bot 有自己的 Slack 应用和用户名，频道中任何人都可以给它工作。见[把 Team Bot 加入 Slack](https://docs.x.ai/grok-bot/create-a-team-bot#add-it-to-slack)。

## 使用线程和表态

当反馈针对某一个结果或某一个审批请求时，在线程中回复。这样主对话记录保持聚焦，同时保留该决定的上下文。

用表态做轻量的确认。当 Bot 需要改变指令时，用文字回复；仅凭一个表态不应承载安全关键的决定。

## 查找先前的工作

用搜索或命令面板来：

* 在 Bot 和群组之间切换
* 查找先前的消息
* 查找文件、链接和例程
* 打开设置和常用操作
* 跳回对话中对应的位置

按 `Cmd/Ctrl+K` 打开搜索面板，或按 `Cmd/Ctrl+Shift+F` 搜索 Bot。搜索面板会跨聊天查找你的消息和文件。当结果显示**已搜索最近的消息（Searched recent messages）**时，选择**搜索更早的（Search older）**继续往前找。完整的桌面端列表见[键盘快捷键](#keyboard-shortcuts)。

## 键盘快捷键

这些快捷键在 Grok Bot 桌面应用中可用。除个别行另有说明外，macOS 用 `Cmd`，Windows 和 Linux 用 `Ctrl`。

* 跳转 / 搜索面板：`Cmd/Ctrl+K`
* 搜索 Bot：`Cmd/Ctrl+Shift+F`
* 新建 Bot：`Cmd/Ctrl+N`
* 新建群聊：`Cmd/Ctrl+Shift+N`
* 显示所有键盘快捷键：`Cmd/Ctrl+/`
* 在此聊天中查找：`Cmd/Ctrl+F`
* 紧凑侧边栏：`Cmd/Ctrl+B`
* 聚焦提示词：`Cmd/Ctrl+I`
* 把选中的文字加入聊天：`Cmd/Ctrl+L`，未选中任何内容时聚焦提示词
* 侧边栏中的第 1–9 个 Bot：`Cmd/Ctrl+1` 到 `Cmd/Ctrl+9`
* 上一个 / 下一个 Bot：`Alt+↑` / `Alt+↓`
* 在访问历史中后退 / 前进：`Cmd/Ctrl+[` / `Cmd/Ctrl+]`
* 循环切换 Bot：`Control+Tab` / `Control+Shift+Tab`（始终用 Control，包括在 macOS 上）
* 连接应用：`Cmd/Ctrl+Shift+M` 或 `Cmd/Ctrl+Shift+W`
* 切换 Bot 设置：`Cmd/Ctrl+Shift+,`
* 对话详情：macOS 上为 `Cmd+Shift+I` 或 `Cmd+Alt+B`；Windows 和 Linux 上为 `Ctrl+Alt+B`
* 发送：在输入框中按 `Enter`，或在任意位置按 `Cmd/Ctrl+Enter`
* 换行：`Shift+Enter`
* 在输入框中听写：提示词获得焦点时按 `Cmd/Ctrl+D`
* 开始语音聊天：在输入框中选择**开始语音聊天**；没有快捷键
* 打开设置：`Cmd/Ctrl+,`
* 放大、缩小或重置：`Cmd/Ctrl+=` / `Cmd/Ctrl+-` / `Cmd/Ctrl+0`
* 全屏：`F11`；macOS 上还有 `Control+Cmd+F`

要查看应用中的全部快捷键，打开账号菜单并选择**支持 → 键盘快捷键（Support → Keyboard shortcuts）**，或按 `Cmd/Ctrl+/`。

## 让对话保持有效

* 先说你需要的结果，而不是详尽模仿每一次点击。
* 链接到事实来源。
* 说明 Bot 可以改动什么，什么需要批准。
* 要求证据——链接、截图或简短的操作日志。
* 明确纠正长期生效的偏好。
* 当对话已转向另一个长期任务时，开一个线程或换一个 Bot。

附件见[文件与结果](https://docs.x.ai/grok-bot/files-and-results)，可重复的工作见[技能与例程](https://docs.x.ai/grok-bot/skills-routines-and-automations)，在授权对外操作之前见[审批、安全与隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy)。
