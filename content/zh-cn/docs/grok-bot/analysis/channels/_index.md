---
title: "Grok Bot：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 以自有的桌面和手机应用为主入口，用类似消息应用的聊天线程与多个 Bot 对话，另向外延伸到 X（X Chat 与帖子中 @bot）、Slack 和 Microsoft Teams；Bot 可认领一个永久的 mail.grokbot.com 邮箱，但非用户当场要求的外发邮件一律停在草稿，没有无人值守发送。
---

## 概要

- 主入口是 Grok Bot 自己的应用：桌面端（macOS、Windows、Linux）和 iPhone、Android 应用，界面是类似 iMessage 的聊天线程，用户同时与多个 Bot 及 Bot 群组对话；文字之外有听写、语音聊天和语音备忘（[聊天与协作文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})）。
- 与 X 的结合是 Grok Bot 独有的渠道：可在 X Chat 里与同一批 Bot 聊天，也可在 X 帖子中标记 @bot 把帖子交给自己的主 Bot；后者截至 2026-10-07 的资料不对澳大利亚、英国、欧盟等地区的账号开放（[@bot 文档]({{< relref "/docs/grok-bot/sources/official/2026-10-07-xai-docs-tag-on-x" >}})）。
- 团队场景走 Slack 和 Microsoft Teams：共享 Bot 有自己的 Slack 应用和账号名，可在频道、线程、私信中被提及；Slack 的规则写得最细（账号关联、未关联成员的受限使用、@here 不 ping 人）。
- Bot 可以有自己的邮箱：每个用户可在 mail.grokbot.com 下认领一个永久地址，供所有自己的 Bot 使用；但例程等非用户当场发起的外发邮件一律停在草稿，官方写明「没有无人值守发送的选项」（[Agent Email 帮助]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-agent-email" >}})）。
- 对外沟通默认以草稿为闸门：邮件和 Slack 消息默认先出可编辑草稿卡，群聊中不出现审批卡、密钥请求和草稿。打电话的能力，官方更新日志与 11-10 的用户比较说法不一。

## 自有应用：类似消息应用的多 Bot 聊天

官方 FAQ 列出的入口是桌面应用、iOS/Android 配套应用，以及 X Chat、X 上的 @bot 和 Slack 中的共享 Bot（[FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。第三方汇总写明桌面版覆盖 macOS、Windows、Linux，另有 iOS、Android 应用，支持文字与语音操作（[iThome 五款主动式智能体]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})；[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。WIRED 的横向测试在 iPhone 上完成设置，称 Grok Bot「有自己的应用」（[WIRED]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

交互形态是聊天线程。Claire Vo 2026-08-18 上手时形容其沿用「熟悉的 iMessage 风格聊天体验」，并鼓励为不同工作创建多个专门 Bot（[Claire Vo 上手]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})）。官方文档列出的对话方式包括 @ 提及、回复特定消息、回应（reactions）、工作进行中追加指令；对话记录中与普通消息并列显示工具活动、计算机使用、生成的文件、问题、批准请求和语音备忘（[聊天与协作文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})）。

- **语音**：官方称语音聊天「一次只与一个 Bot 进行，不能在群聊中使用」，桌面端也可与共享 Bot 语音聊天；更新日志记有断线后自动重连、语音通话可利用此前通话和近期聊天（[聊天与协作文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})；[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。
- **附件与分享**：桌面端一条消息最多 20 个附件；iPhone 可通过系统分享面板把照片、文件、链接、文本发进 Grok Bot，Android 分享面板「目前只接受文本」（[文件与结果文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-files-and-results" >}})）。更新日志记 0.70.2 起单条消息附件上限从 6 个升到 20 个，文件最大 250 MB、视频最大 1 GB（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。
- **通知**：用户在 Mac 或 Windows 上使用时，回复通知发到电脑而不是手机（0.70.2 起）；iPhone 上推送投递截至 11-05「正在逐步推出」（[设置文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-settings" >}})）。

工程层面，Peter Piekarczyk 的博客称 Bot 用一个名为 `SendToUser` 的全局工具联系用户，桌面、移动、Slack 各客户端自行决定如何展示（[Peter Piekarczyk]({{< relref "/docs/grok-bot/sources/community/2026-10-14-peterp-what-happens-when-you-message" >}})）。这是个人博客的说法，官方文档未见对应描述。

## 群聊：多个 Bot 在一个线程里分工

用户可把多个 Bot 拉进群组，用 @ 提及、回复或 @everyone 指派任务。官方文档写明「批准请求、密钥和登录请求，以及电子邮件或 Slack 草稿不会出现在群组中」，Bot 发到群里的交接消息只有文本（[聊天与协作文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})）。更新日志记有 Bot 之间可以互发消息，团队管理员可在「Bot 能力」下关闭 Bot 间消息传递（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

用户实例：一位作者展示了 5 个 Bot 组成的群协作写小说，「经过好几小时的折腾，一本小说就写完了」（[archieli]({{< relref "/docs/industry/sources/community/2026-11-11-archieli-grok-bot-work-mode" >}})）。另一种用法是收敛入口：官方博客中的用户设置了 Inbox Manager、Calendar EA、Intel Scout 三个 Bot，再由「作为唯一入口的 Bot Boss」汇总它们的汇报，避免被多个 Bot 分别打扰（[工作中的 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-24-guide-grok-bot-for-work" >}})）。

推断：群聊里不出现审批、密钥和草稿，说明涉及权限与对外发送的操作被收回到一对一线程处理；多 Bot 的设计让入口数量变多，Bot Boss 这类用户自建的汇总 Bot 是对打扰问题的回应。

## X：X Chat 与帖子中的 @bot

- **X Chat**：用户可在 iOS、Android 的 X 应用和 x.com 的 X Chat 中与「在 Grok Bot 应用中使用的 Bot 相同」的 Bot 聊天。官方称该支持「正在逐步推出」，需要最新版 X 应用；方案上需 The X Subscription 的 Premium、Super 或 Ultra，Plus 不包含 Grok Bot（[聊天与协作文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})）。
- **帖子中标记 @bot**：在帖子或回复中标记 @bot，即把该帖（连同被回复帖、引用帖，含静态照片）交给用户自己的 Bot；@bot 只在 X 上发一条确认，结果留在应用中。请求消耗 Grok Bot 用量，首次通过时 X 会通知用户；别人共享的 Bot 不能接收标记请求（[@bot 文档]({{< relref "/docs/grok-bot/sources/official/2026-10-07-xai-docs-tag-on-x" >}})）。
- **地区与沉默条件**：@bot「尚不适用于位于澳大利亚、英国、欧盟、冰岛、列支敦士登或挪威的账号」，按 X 记录的账号国家判断，当前位置和 VPN 都没有影响；帖子同时标记 @grok、含视频或 GIF、未通过内部审核，或每周用量已用完时，@bot 不回应（同上）。

推断：@bot 把社交平台的公开帖子变成任务入口，是 X 平台归属带来的渠道；地区排除名单与欧盟、英国等监管较严的地区重合，但资料没有说明排除原因。

## Slack 与 Microsoft Teams：团队 Bot 的工作区渠道

2026-09-28 的 Team Bots 发布稿称「每个 Team Bot 都有自己的账号名（handle）」，可邀请进 Slack 频道（[Team Bots 发布]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})）。11-05 的共享 Bot 帮助文档给出了接入规则（[共享 Bot 帮助]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})）：

- 所有者或 Manager 通过 **Bring to your team's Slack** 连接；显示 **Awaiting admin approval** 时需 Slack 工作区管理员批准。
- 用户需先把 Slack 关联到 Cursor 账号，每个工作区一次；「Slack 访客、Slack Connect 频道和其他 Slack 工作区永远不在范围内」。
- 共享给整个组织的 Bot，未关联账号的工作区正式成员也可在频道线程中提及它，每个线程提示一次 **some features will be limited**；私信仍须先连接。Teams 文档写明 Slack Workspace Access 默认开启（[Teams 与 Enterprise 文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）。
- 个人 Bot 也可在 Slack 私信中接请求，但回复落在应用聊天而不是 Slack（[聊天与协作文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})）。

更新日志补充了团队 Bot 在 Slack 中的行为：记录每条帖子由谁请求、在共享对话中发送前检查帖子对相应人员是否可见、可提及 Slack 用户组，而「@here 和 @channel 仍不会 ping 任何人」；未关联账号的人不能借所有者的 Bot 使用所有者的登录信息或私人数据。Microsoft Teams 只在更新日志中以修复条目出现（管理员登录失败提示、移除重连后不再留下重复项等，标注 [Teams]），设置清单含「Slack 或 Microsoft Teams」步骤（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

使用例：xAI 内部的 Data Bot 被加入团队 Slack 频道，「回答问题，并主动为进行中的工作做出贡献」（[Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}})）；James Pember 称 Bot 已在 Slack 中替他分流产品问题和 bug，是「生产力第一道防线」（[James Pember]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})）。

## Bot 的邮箱：一人一个永久地址，外发以草稿为闸门

据 [Agent Email 帮助]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-agent-email" >}})（2026-11-05）：

| 方面 | 规则 |
| --- | --- |
| 地址 | `mail.grokbot.com` 下认领，每人只能有一个，不能改名或删除；地址认领后不再给任何其他人，即使原账户被删除 |
| 归属 | 地址属于用户，不属于某个 Bot；用户自己的所有 Bot 可在私聊和例程中使用；Slack 线程和他人聊天中不可用，共享 Bot 没有团队地址 |
| 收信 | 任何人都可以发信；应用中没有收件箱视图和新邮件通知，需问 Bot；新邮件不会自行唤醒 Bot，要靠例程监视 |
| 发信 | 聊天中当场要求的邮件经 Auto-review 放行后发出；例程或非用户发起的邮件只存草稿，「没有无人值守发送的选项」；来信中的指令不算发送许可 |
| 限额 | 每封最多 50 位收件人（含抄送、密送）；附件最多 10 个、单个 10 MB、合计 25 MB，不能附可执行文件；新闻通讯和首次联系邮件每封一位收件人并含一键退订；对新联系人数量另有上限 |
| 团队 | Cursor 团队中默认关闭，需管理员在 Bot Capabilities 下开启 |

更新日志把 Bot 自有邮箱记在 v0.70.2（10-11）（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。用户实测中，作者把邮箱用于接收验证码、收据、新闻简报（[鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。

邮件之外，Bot 发邮件或 Slack 消息时默认也先出可编辑草稿卡，可对单个 Bot 关闭草稿；但 Bot 从自己地址主动发出的邮件「始终会作为草稿等待」（[聊天与协作文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})）。

推断：邮箱给了 Bot 一个独立于用户的对外身份，用来注册服务和收验证码；永久不可改、不可回收、一人一个，加上外发强制草稿和新联系人上限，看起来是为了防止地址被滥用来群发。

## 电话与车载：资料较少的渠道

- **电话**：更新日志 11-06 的条目有「通话卡片」「无人接听」、实时转写，以及「要把文本分享给正在进行的电话，卡片会询问『将此发送到你的通话？』」，说明 Bot 已有对外通话的能力（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。而特工宇宙 11-10 转述的投资人使用比较称 Grok Bot「和 Muse 能力相近，能对话，但不能替人打电话」（[特工宇宙]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。两者并存：官方没有发布稿或帮助文档说明电话功能的开放范围，可能尚未对所有用户开放。
- **车载**：Not a Tesla App 2026-10-15 的报道提到「上个月 Tesla 将 Grok Bot 集成到其车辆中」，只有一句（[Not a Tesla App]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})）。库中没有车载使用方式的资料。

## 资料缺口

- 电话功能的官方说明：开放范围、能否拨打商家或个人、如何向对方披露 AI 身份、是否计入用量；特工宇宙「不能替人打电话」的说法与更新日志不一致。
- X Chat 与 @bot 的使用情况、逐步推出的进度，以及地区排除的原因。
- Microsoft Teams 渠道的帮助文档（目前只在更新日志中出现）。
- Tesla 车载集成的形态与范围（只有 Not a Tesla App 一句转述，其引用的原报道未收）。
- 短信、iMessage、WhatsApp 等渠道：库中未见 Grok Bot 支持的说法，也没有资料说明不支持的原因。
- Android 分享面板只收文本、iPhone 推送逐步推出等移动端限制的后续变化。

## 主要资料

**官方**

- [聊天与协作文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})：对话方式、语音、群聊规则、X Chat、草稿默认
- [@bot 文档]({{< relref "/docs/grok-bot/sources/official/2026-10-07-xai-docs-tag-on-x" >}})：X 帖子标记的规则、地区排除、沉默条件
- [Agent Email 帮助]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-agent-email" >}})：Bot 邮箱的认领、收发规则与限额
- [共享 Bot 帮助]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})、[Teams 与 Enterprise 文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})：Slack 接入、账号关联、默认设置
- [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：邮箱上线版本、Slack 行为细节、Microsoft Teams、通话卡片
- [文件与结果文档]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-files-and-results" >}})、[设置文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-settings" >}})、[FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})：附件、分享面板、通知、入口清单
- [Team Bots 发布]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})、[Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}})、[工作中的 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-24-guide-grok-bot-for-work" >}})：Slack 中的团队 Bot、Bot Boss 单入口用法

**媒体**

- [Not a Tesla App]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})：Tesla 车载集成的一句提及
- [iThome 五款主动式智能体]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})、[WIRED]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})：支持平台与入口

**社区**

- [Claire Vo 上手]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})：iMessage 风格的多 Bot 聊天
- [Peter Piekarczyk]({{< relref "/docs/grok-bot/sources/community/2026-10-14-peterp-what-happens-when-you-message" >}})：`SendToUser` 统一回传
- [James Pember]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})：Slack 中分流问题
- [archieli]({{< relref "/docs/industry/sources/community/2026-11-11-archieli-grok-bot-work-mode" >}})：多 Bot 群聊写小说
- [鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})：Bot 邮箱的用途
- [特工宇宙]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})：「不能替人打电话」的用户说法
- [Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})：平台覆盖
