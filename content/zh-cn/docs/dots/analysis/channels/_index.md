---
title: "OpenAI Dots：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  dot 没有独立 App，入口是 ChatGPT 应用加 Slack、Teams 和测试中的短信；各渠道共享记忆但对话分开，dot 只对所有者负责，批准仍回到 ChatGPT 完成。
---

## 概要

- dot 内置在 ChatGPT 中，没有独立 App。截至 2026-11-05 的官方文档，入口包括 ChatGPT 移动应用、桌面应用、桌面浏览器（不支持移动端网页），以及 Slack、Teams、短信（iMessage / RCS）、iOS 小组件和快捷指令。
- 「一个 dot，多个渠道」：切换渠道不重置记忆，但各渠道的可见对话互不镜像；把私人信息带到共享频道前会先征求所有者同意。
- 短信从发布时的「即将推出」到 2026-10-28 以测试版向美国 Pro 用户开放，经第三方服务商 Linq 收发，名额有限，Business 与 Enterprise 不可用。
- 在 Slack 与 Teams 中，dot 可以用所有者的账户行事，也可以有自己的 Slack 身份；只有所有者能指挥它。发布时 dot 不能有独立邮箱，也不能主动给用户打电话。
- 需要批准的动作不在短信或 Slack 里完成，而是发链接回到 ChatGPT 审阅。

## 一个 dot，多个入口

官方文档写明，用户可以在 ChatGPT 移动应用、桌面应用或桌面浏览器中创建 dot、发消息或打电话，「不支持移动端网页」；此外可通过 Slack、Teams（私信，或加入频道后在话题串中提及）、短信，以及 iPhone 主屏小组件和苹果快捷指令联系它（[文档：给你的 dot 发消息]({{< relref "/docs/dots/sources/official/2026-11-05-docs-message-your-dot" >}})）。2026-11-04 的更新又加入了 iOS 从通知直接回复、从其他应用分享内容给 dot、用操作按钮打开 dot（[11 月 2–6 日更新]({{< relref "/docs/dots/sources/official/2026-11-04-docs-whats-new-november-2-6" >}})）。

各渠道之间的关系，官方的说法是：切换渠道不会重置 dot 的记忆，但 Slack、Teams 里只显示在那里交换的消息，ChatGPT 中的消息不会自动复制过去（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。用户可以指定哪类更新走哪个渠道，例如例行进展留在 ChatGPT、需要决定的事带到 Slack（[文档：认识 dots]({{< relref "/docs/dots/sources/official/2026-11-05-docs-meet-dots" >}})）。连接消息渠道本身不授予收件箱、其他应用或本地计算机的访问权（[文档：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-getting-started" >}})）。

媒体对「没有独立 App」看法不一。Wired 记者表示更喜欢独立应用，但认为手机小组件是可接受的折中（[Wired 全面实测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）；甲子光年把 Dots 描述为「藏在 ChatGPT 中」，与 Muse、Today 的独立 App 对照（[甲子光年]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）。

推断：OpenAI 选择把 dot 放进已有的 ChatGPT 应用和办公协作工具，而不是另起一个 App，入口依赖 ChatGPT 的既有用户和企业办公场景；短信是唯一面向「不打开 ChatGPT」场景的渠道，目前范围最窄。

## 短信：美国 Pro 测试版，经 Linq 收发

| 时间 | 状态 | 资料 |
| --- | --- | --- |
| 2026-09-29 | 发布稿只列 ChatGPT、Slack、Teams，短信「即将推出」 | [推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}}) |
| 2026-10-28 | 以测试版向美国 Pro 用户推出，iMessage 或 Android RCS，一对一，支持文字、照片、语音消息 | [发布说明：给你的 dot 发短信]({{< relref "/docs/dots/sources/official/2026-10-28-relnotes-texting-your-dot" >}})、[What's new：给你的 dot 发短信]({{< relref "/docs/dots/sources/official/2026-10-28-docs-whats-new-text-your-dot" >}}) |
| 2026-11-05 | 帮助中心补充：Business、Enterprise 工作区不可用，名额有限，「可能并非每位 Pro 用户都能使用」 | [帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}}) |

官方发布说明写明，短信由第三方消息服务商 Linq 收发，OpenAI 为此做过渗透测试；dot 只能给所有者发短信，也只有所有者能给它发，开通短信不会让 dot 或 OpenAI 读到用户的其他短信；短信中的 dot 与应用内的 dot 共享记忆和插件。dot 会主动发短信，渠道由它根据上下文选择，用户可以改变规则。需要批准时，dot 发一个链接，用户在 ChatGPT 中审阅请求。截至 2026-11-05 的文档，短信渠道不支持群聊、电话和 FaceTime；帮助中心提示「可能会产生短信和数据费用」，回复 STOP 可停止 dot 发的短信，未提及 OpenAI 另收费用。

资料中没有短信渠道的第三方一手实测。

## Slack 与 Teams：对所有者负责的同事

在 Slack 中，dot 默认只回应所有者，可按指示与他人互动；在频道回复前，可以先私下问所有者愿意分享什么。仅把 dot 加入频道不会建立监控，需要明确说明频道、关注点和通知时机（[文档：给你的 dot 发消息]({{< relref "/docs/dots/sources/official/2026-11-05-docs-message-your-dot" >}})）。其他成员的私信或提及不会让 dot 开始工作；dot 在频道发帖时其他成员可见（[帮助中心：工作区管理]({{< relref "/docs/dots/sources/official/2026-11-05-help-manage-dots-in-workspaces" >}})）。

Enterprise 工作区要同时开启「Use dots (Beta)」与「Add dots to Slack and Microsoft Teams」两项设置；Slack 工作区要求应用审批时，由 Slack 管理员批准，之后每位成员自行设置。

社区实测中，Claire Vo 的 Slack 回复任务里 Dot 能理解她的偏好，Muse 因未连接 Slack 无法参与这项任务（[ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。

## 身份：可以有 Slack 身份，暂无独立邮箱与号码

管理员指南区分了 Slack 的两种接入方式：通过插件使用成员自己的 Slack 账户，此时 dot 没有自己的身份；或者给 dot 一个自己的 Slack 身份，它的帖子对对话中的人可见。关闭 dot 的 Slack 身份不会移除它通过成员账户获得的访问，两者要分别检查（[管理员指南]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-admin-guide" >}})）。Cyera 的分析提到 dot 有默认形如 `@yourname-dot` 的 handle，设计上更像同事（[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})）。

邮箱方面，帮助中心写明「在发布时，你还不能给你的 dot 一个独立的电子邮件地址」，用户可以把个人邮箱连接给 dot 使用。企业预览中的「专职 dots」才有自己的身份、凭证和 IT 配置的硬件（[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})）。资料中没有 dot 拥有独立手机号码的说法；行业综述把独立邮箱、电话归给 Manus Cue 等产品，而不是 Dots（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。

## 语音通话：用户可以打，dot 暂不能主动打

用户在 dot 对话中点电话按钮即可通话，通话中可同时发文字、链接和图片，结束通话不会停止已分配的工作；由 dot 主动发起的通话「计划在发布之后推出」（[文档：给你的 dot 发消息]({{< relref "/docs/dots/sources/official/2026-11-05-docs-message-your-dot" >}})）。通话使用挑选出的对话上下文，可能与后台任务获得的上下文不同（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。

使用反馈偏负面：Datawhale 的综述转引有用户称语音不如 GPT Live、有评测者称通话在测试中没有接通（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）；一位用户对《中国新闻周刊》称，语音电话有时要反复尝试几分钟才能接通（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）。2026-11-04 官方称已让 dot 在通话中更快开口。

## 不一致的说法

- **移动网页**：发布稿称可「在桌面、网页和移动端的 ChatGPT 中」给 dots 发消息；2026-11-05 的文档明确「不支持移动端网页」。发布稿的「网页」是否只指桌面浏览器，资料没有澄清。
- **独立邮箱**：帮助中心说发布时不能给 dot 独立邮箱；同日收集的隐私常见问题却写到 dot「有了自己的电子邮件或 Slack 账户」时的情形（[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})）。可能是在描述企业预览中的专职 dots，资料没有说明。
- **主动来电**：官方说发布时 dot 不能主动打电话；Datawhale 转述 The Neuron 称 dot「第二天会主动打电话继续聊」。资料无法判断是功能灰度还是转述有误。
- **短信设置入口**：消息渠道文档说移动应用里也能设置短信，帮助中心则说「请在桌面端连接消息渠道」。可能是帮助中心未及时更新。

## 资料缺口

- 短信是否使用独立号码、号码的国别，以及测试名额的分配规则和扩大计划。
- Teams 的行为是否与 Slack 一致；资料只写「也可以在 Teams 发消息」。
- WhatsApp、Telegram、邮件等渠道有无计划；WhatsApp 只在「Enterprise 不支持」一句中出现。
- 短信渠道和 dot 主动来电都没有第三方实测。

## 主要资料

- 官方：[文档：给你的 dot 发消息]({{< relref "/docs/dots/sources/official/2026-11-05-docs-message-your-dot" >}})（渠道清单、Slack 行为、通话、短信设置）；[发布说明：给你的 dot 发短信]({{< relref "/docs/dots/sources/official/2026-10-28-relnotes-texting-your-dot" >}})（Linq、访问边界）；[帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}})（短信范围、邮箱）；[管理员指南]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-admin-guide" >}})（Slack 身份）；[11 月 2–6 日更新]({{< relref "/docs/dots/sources/official/2026-11-04-docs-whats-new-november-2-6" >}})（iOS 通知回复）。
- 媒体：[Wired 全面实测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})（独立 App 之争）；[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})（通话接通问题）。
- 社区：[ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})（Slack 任务实测）；[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})（dot 的 handle）；[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})（通话反馈转引）。
