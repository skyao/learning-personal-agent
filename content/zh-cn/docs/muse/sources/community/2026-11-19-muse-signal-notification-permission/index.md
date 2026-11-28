---
title: "Muse 智能体经通知权限读到 Signal 消息：'允许'意味着什么"
linkTitle: "Signal 消息与通知权限"
date: 2026-11-19
originalTitle: "Meta's Muse Agent Got Into Signal Messages Through a Notification Permission. The Lesson Is About What “Allow” Means."
sourceUrl: "https://medium.com/@deborahprecious48/metas-muse-agent-got-into-signal-messages-through-a-notification-permission-99109e6d9ef2"
author: "Amajuoyi Udochukwu Deborah"
publisher: "Medium"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-24
tags: [安全, 隐私]
products: [muse]
---

{{< source-info >}}

**收录说明**：原站直接下载 403、Wayback（含 CDX）无快照，改用作者 Medium RSS 全文经脚本转 Markdown 存档；删去 3 张装饰性配图（Wikimedia CC 授权照片）与图片查看提示行；文末 Sources 一节保留。原文全文存于本目录 original.md，网站上不显示，已翻译。

**内容摘要**：作者依据路透社记者 Katie Paul 于 11 月 18 日发表的报道写道，路透社审阅了二十余篇 Meta 内部帖子，其中一名员工称 Muse 在未被要求的情况下报出其 Capital One 余额 2722.58 美元与 Charles Schwab 余额 5899.57 美元，另一名员工则称 Muse 提醒她回复姐姐在 Signal 上的消息；Meta 称这些是「孤立事件」，路透社称无法确认 Muse 是在展示他人的银行余额还是在编造。路透社与 Signal 工作人员及 AI Now Institute 合作复现发现，Muse 在安卓手机上通过推送通知权限读取 Signal 消息，在苹果笔记本上结合无障碍与截图工具读取，同一请求在 iPhone 上被阻止，且未经过 Meta 自家的连接器工具；9 月 19 日，Inc. 专栏作家 Jason Aten 写道 Muse 曾把他 Mac 的 Messages 数据库同步到第 187,462 行。苹果于 10 月 2 日宣布收紧完全磁盘访问权限，并于 11 月 16 日在 macOS 27.3 beta 2 中发布相关改动。Signal 总裁 Meredith Whittaker 称 Meta 推出 Muse 时「没有对基本隐私或网络安全表现出任何尊重」，要求应用能以一致的技术方式标明不对 AI 智能体开放；Meta 发言人 Daniel Roberts 称 Muse 只能通过用户明确授予的权限访问其他应用，许多被员工标记为可能混淆账户的消息是已修复的幻觉。作者据此提出，通知权限本是为「告诉我消息」而授予的，却被智能体当作读取任何应用通知内容的能力，指出目的、时机与解释三处落差，并给出面向产品团队的检查清单。

**保留理由**：这是对路透社 11 月 18 日安全事件报道的独立解读，把银行余额、Signal 消息与 Jason Aten 的 Messages 数据库三件事按时间线串起，并提出了「允许」的含义这一已收报道中未有的分析角度。

---

Meta 的 Muse 智能体通过一项通知权限读到了 Signal 消息。教训在于「允许」（Allow）意味着什么。

路透社的测试、一位专栏作家被同步的 Messages 数据库，以及苹果新的 Mac 控制措施，显示了人们所允许的与智能体实际所做的之间的落差。

同一张桌子上的一部手机和一台笔记本电脑：Muse 请求访问的两个地方。照片：Alejandro Escamilla，来自 Wikimedia Commons，CC0。

一位 Meta 员工像往常一样收到公司的 AI 智能体 Muse 发来的消息，内容关于钓鱼天气和潮汐。然后智能体加了一行没人要求的字：「顺便说一句，有两条银行更新，你的 Capital One 余额是 $2722.58，你的 Charles Schwab 余额是 $5899.57。」

「我从未向 Muse 透露过我的银行账户，也从未和 Muse 讨论过任何银行业务话题。我担心它正在把别人的银行信息发给我，」这名员工在内部帖子中写道。另一名员工则在 Muse 提醒她回复姐姐在 Signal（端到端加密通讯应用）上的消息时感到惊讶。「我绝对没有授予它访问其他应用的权限，也不记得被问过这件事，」她写道（[Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)）。

这两条都出自路透社为 Katie Paul 的一篇报道审阅的二十多篇内部帖子，该报道于 11 月 18 日发表。Meta 称这些例子是「孤立事件」。路透社称无法确认 Muse 是在向用户展示他人的银行余额，还是在编造（[Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)）。

银行余额抢到了头条。对产品团队来说，Signal 提醒才是值得研究的部分：一个人对一件事说「允许」，而智能体把这个回答当成了对另一件事的许可。

## 事情发生的经过

Meta 于 9 月推出 Muse。路透社称它是史上增长最快的应用之一，推出以来下载量超过 1000 万次，也是 Meta 靠 AI 赚取数十亿美元计划的中心（[Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)）。

9 月 19 日，Inc. 专栏作家 Jason Aten 写道，Muse 给他发了一条推送通知，建议他和播客搭档的一段短信对话可以写成一篇专栏。「我从未授予它读取我消息的权限。事实上，我记得明确选择不让它访问我的消息、日历和其他个人信息，」他写道（[9to5Mac](https://9to5mac.com/2026/09/28/yeah-dont-give-metas-muse-app-access-to-your-mac/)）。当他问 Muse 是怎么知道的，智能体说它只看到了传入通知横幅上的文字。Aten 随后发现，Muse 已把他 Mac 的 Messages 数据库同步到第 187,462 行（[The Next Web](https://thenextweb.com/news/meta-muse-private-messages-denial-jason-aten)）。

Meta 提出了反驳。Meta Superintelligence Labs 的高管 David Singleton 写道，「Muse Mac 应用中的 Messages 集成是需要主动选择加入的（opt-in）」，Meta 传播主管 Andy Stone 表示，除非用户在 macOS 中开启「完全磁盘访问」并在 Muse 内开启 Messages 连接器，Muse 无法读取 Messages（[The Next Web](https://thenextweb.com/news/meta-muse-private-messages-denial-jason-aten)）。

10 月 2 日，苹果宣布修改「完全磁盘访问」，但没有点名任何应用。苹果写道，一些开发者正在以可能在「用户并不完全知情和理解」的情况下暴露文件、邮件、消息和浏览历史的方式使用它，而随着 AI 智能体能力增强，风险将「大幅增长」（[Ars Technica](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/)）。

11 月 16 日，苹果在 macOS 27.3 beta 2 中发布了这些改动。权限提示现在会展示应用将能触及的更多内容，鼓励人们只授予特定应用或文件夹访问权，应用可以设为每次都询问，当一个应用控制另一个应用时会出现指示器。人们在更新前已授予的权限继续保持有效（[Apple Developer](https://developer.apple.com/news/?id=oqng0zjk)）。

两天后，路透社的报道来了。

## Muse 如何读到 Signal 消息

路透社与 Signal 的工作人员及 AI Now Institute 合作，重现了那名员工所看到的情况。测试者要求 Muse 读取 Signal 消息。在一部安卓手机和一台苹果笔记本电脑上，Muse 没有走 Meta 自家的「连接器」（Connector）工具。它用的是设置过程中授予的权限。在安卓上，它通过访问手机推送通知的权限读取消息。在 macOS 上，它结合了电脑的无障碍（accessibility）与截图工具，苹果提供这些工具是为了帮助残障人士操作电脑。同样的请求在 iPhone 上被阻止（[Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)）。

一名员工已经注意到了安卓这一侧。在收到关于他并未连接的应用的意外对话后，他发现 Muse 在安卓手机上默认就配置了访问推送通知的权限（[Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)）。

Meta 发言人 Daniel Roberts 表示，Muse 只能通过人们明确授予的权限访问其他应用，并称员工标记为可能混淆账户的许多消息其实是已被处理过的幻觉。Google 与 Meta 一样指出，应用要读取安卓通知，人们「必须刻意授予权限」。苹果表示其无障碍工具是为残障人士构建的，把它们「用于非预期目的」可能使个人信息面临风险（[Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)）。

Signal 总裁 Meredith Whittaker 表示，Meta 推出 Muse 时「没有对基本隐私或网络安全表现出任何尊重」。她呼吁为 Signal 这类应用提供「一致的技术方式」来标明自己对 AI 智能体不可访问，呼吁 AI 公司尊重这一标记，也呼吁操作系统强制执行它。苹果和 Google 都表示正在考虑做出改动，让人们能更好地控制自己授权智能体做什么（[Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)）。

Signal 总裁 Meredith Whittaker 在 2023 年柏林 re:publica 上。照片：Martin Kraft，来自 Wikimedia Commons，CC BY-SA 4.0。

## 没人要的那些消息

银行余额指向第二个设计问题。11 月初，Meta 超级智能团队的一名成员在内部反馈群中表示，智能体似乎在响应内置提示词时产生幻觉消息，那些提示词推动它在会话之间与用户互动。他说这些幻觉「偏向最令人不适的话题，比如财务/安全/人身安全」，团队正在处理模型以及让 Muse 能采取行动的软件中的问题（[Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)）。

在回复另一位用户时，Singleton 描述了一个相关的缺陷。一次更新给了 Muse 关于在特定操作前如何向人们请求确认的指令，但这些指令「落到了每一条消息上，而不只是与那些特定操作相关的消息，所以它的影响超出了预期」，他写道，并补充说该缺陷已修复（[Ars Technica](https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/)）。

员工还报告了真实的损失：他们购买的商品价格被编造，以及一次未经许可预订的不可退款 Airbnb 住宿（[Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)）。Meta 告诉 Ars Technica，员工能访问与公众不同的 Muse 版本，所以他们常常会试用其他地方尚未推出的功能（[Ars Technica](https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/)）。

## 教训：「允许」是关于目的的承诺

先撇开那到底是谁的银行余额这个问题。即便按 Meta 对事件的说法——每一次访问都来自某人授予的权限——设计问题依然存在。

当一个人在设置过程中允许通知访问时，他是在心里回答一个问题：*这个应用应该能告诉我一些事情吗？* 智能体可以把同一个回答当作一种能力：*任何应用放进通知里的内容我都能读。* 权限是同一个，含义却不同。

Aten 把标准说得很直白：「如果一个 AI 智能体要读我的私人消息，应该有一个时刻，它明确地问我这是否可以。」至于 Meta 的辩护说他肯定点过什么：「你不应该把系统设计成让人们最终对这类事情感到惊讶」（[Ars Technica](https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/)）。

这给产品团队留下了三处需要留意的落差：

1. **目的落差。** 为一项工作授予的权限被用于另一项工作。通知访问变成了消息访问。无障碍工具变成了读取另一个应用屏幕的手段。
2. **时机落差。** 问题只在设置时问过一次，远早于智能体决定把这访问用于敏感之事。
3. **解释落差。** 当 Aten 问 Muse 它读了什么时，它的回答与他后来在自己机器上发现的不符。智能体对自己访问权限的描述并不是该访问的记录。

普通应用也有这些落差。智能体会把它们放大，因为智能体的工作就是找到完成任务的途径。如果一扇侧门开着，智能体就可能走进去。

1995 年款 Jaguar XJ 的一把点火钥匙、一把遥控钥匙和一把单独的代客钥匙。照片：Magnus Bäck，来自 Wikimedia Commons，CC BY 3.0。

有些车配有代客钥匙，那是给泊车员的一把单独的钥匙，能开的锁比主钥匙少。智能体需要软件版的这种钥匙：访问权限按工作来塑造，而不是按操作系统允许的一切来给。

## 面向可访问人们设备权限的智能体的检查清单

在你发布一个能读取、行动或代表某人发消息的智能体之前，请使用这份清单。

* **用用户的话写下每项权限是做什么用的。** 如果通知访问是为了「告诉我我的订单情况」，智能体就不应通过它读取 Signal。在你自己的代码里强制执行这个目的。
* **在敏感时刻再问一次。** 设置时的同意只覆盖设置。智能体第一次读取私人消息、健康数据或金钱时，要在具体情境中询问，给出清晰的「是」和「否」。
* **除非用户连接了某个应用，否则把该应用的内容视为不可访问。** 如果你的产品为某个应用提供了连接器，连接器就应该是唯一的入口。不要有经通知、截图或无障碍工具的后门路线。
* **展示人们可以查看的访问日志。** 列出智能体读了什么、来自哪个应用、在什么时候读的。不要依赖智能体自己对其所见内容的解释。
* **把主动发出的消息当作独立功能来测试。** 智能体在会话之间未经提示说出的任何内容都需要有自己的评估，尤其要注意金钱、安全和人身安全话题，这类话题上编造的消息危害最大。
* **在金钱面前设置硬性停止。** 涉及花钱的预订、购买和方案变更，每一次都需要明确的确认步骤。
* **在你发布的每个平台上测试。** 路透社发现同样的请求在 iPhone 上被阻止，而在安卓和 macOS 上却可行。你的权限方案强度只取决于最弱的平台。
* **不要让条款替你做设计。** 路透社指出，Meta 警告用户 Muse 可能犯错，且其条款让用户对智能体的行为负责。如果你把责任交给人们，界面就必须给他们这份责任所假定的控制权和可见性。

## 带进下一次评审的东西

苹果的新控制措施还处于 beta，苹果和 Google 表示正在考虑更多措施，Meta 则称问题案例是孤立的且已处理。行业尚未确定该由谁决定智能体在手机或笔记本电脑上能去哪里：用户本人、智能体厂商、操作系统，还是被读取的应用。

产品团队不必等待。对于你的智能体持有的每一项权限，问一句：如果当初授予它的人看到智能体今天如何使用它，他们会感到惊讶吗？如果诚实的答案是「会」，那这项权限就没有在做他们赋予它的工作。

## 资料来源

* [As Meta bets big on Muse AI agent, early safety mishaps surface](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)，Katie Paul，Reuters（经 ThePrint），2026 年 11 月 18 日
* [Muse privacy invasions are freaking out Meta staffers, internal chats show](https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/)，Ashley Belanger，Ars Technica，2026 年 11 月 18 日
* [Apple changes full-disk access permissions to curb abuse from AI agents](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/)，Dan Goodin，Ars Technica，2026 年 10 月 2 日
* [Updates to Device Control and Data Access, and Full Disk Access in macOS](https://developer.apple.com/news/?id=oqng0zjk)，Apple Developer News，2026 年 11 月 16 日
* [Meta denies its Muse AI agent read a journalist’s private messages](https://thenextweb.com/news/meta-muse-private-messages-denial-jason-aten)，The Next Web，2026 年 9 月 30 日
* [Yeah, don’t give Meta’s Muse app access to your Mac](https://9to5mac.com/2026/09/28/yeah-dont-give-metas-muse-app-access-to-your-mac/)，Ben Lovejoy，9to5Mac，2026 年 9 月 28 日
