---
title: "Signal 默认限制截图，阻止 AI 智能体读取聊天记录"
linkTitle: "Signal 限制截图防读取"
date: 2026-11-21
originalTitle: "Signal Restricts Screenshots to Block AI Agents From Reading Chats, Following the Muse Reports"
sourceUrl: "https://www.allthingsmuse.com/articles/signal-restricts-screenshots-ai-agents-muse/"
author: "Icarus"
publisher: "All Things Muse"
basedOn: "Reuters 2026-11-20 独家报道与 Signal 博客文章"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-21
tags: [安全, 隐私]
products: [muse]
dateNote: "页面显示 2026 年 11 月 21 日，元数据 article:published_time 为 2026-11-21T07:00:00Z（美东 11 月 21 日 02:00）。"
---

{{< source-info >}}

**收录说明**：直接下载；去掉了首图 Jolly 插画、作者头像、文内配图与站内「Earlier coverage」推荐卡片；消息源为 Reuters 独家报道、Signal 博客文章与 The Register 报道。

**内容摘要**：Signal 于 11 月 20 日宣布默认开启截图限制，阻止 AI 智能体读取私人聊天，同时称这套保护「并不完整」，呼吁 Apple、Google 与 Microsoft 给开发者提供切实的退出方式。iOS 应用默认屏蔽应用内截图并新增「Block Siri AI」设置，Android 应用在检测到 AI 助手读取屏幕时开启已有的 Screen Security 功能，Windows 版去年已屏蔽微软 Recall 的截图，macOS 则无法可靠提供同等保护，Signal 建议用户在系统设置中把 Signal 排除出 Siri。此举跟随路透社本周的报道：Muse 在 Mac 与 Android 手机上能读取 Signal 消息，绕过官方 Connector 工具，利用初始设置时授予的宽泛系统权限，在 Mac 上通过无障碍与截图工具导航至 Signal、抓取聊天并提取文字，而在 iPhone 上同类请求被拦截。苹果本周的系统更新已关闭上述 Mac 路径，同时引入针对智能体的新权限；Meta 回应称智能体需要查看并操作用户电脑才能代劳，且 Muse 只能通过用户明确授予的权限访问其他应用。Signal 并非首家设防的服务，此前已有网站在网络层面屏蔽 Muse 等智能体，苹果也在 Muse 隐私争议后收紧了 Mac 权限提示。

**保留理由**：记录了 Signal 针对 Muse 读取聊天记录的报道作出的官方回应，是已收路透社调查与 Muse 隐私争议资料的直接后续，补上了应用层设防这一环节。

---

Signal 正在默认开启截图限制，以阻止 AI 智能体读取私人聊天，同时称这些保护「并不完整」，并敦促 Apple、Google 和 Microsoft 给开发者提供真正的退出方式。此举跟随路透社关于 Muse 读取 Signal 消息的报道。

Signal 将限制其应用内的截图，以阻止 AI 智能体读取手机上的私人聊天，这家加密通讯服务[于 11 月 20 日表示](https://dukecountry.fm/2026/11/20/exclusive-signal-restricts-screenshots-to-block-ai-agents-from-reading-messages/)。独家报道这一公告的路透社称，新的限制默认开启。当 Signal 检测到截图尝试，或检测到 AI 助手试图访问屏幕时，用户会根据设备看到弹窗，可以选择关闭这些限制。

Signal 称自己的保护「并不完整」，并敦促操作系统提供方 Apple、Google 和 Microsoft 给应用开发者提供更具体的方式来阻止智能体访问敏感数据，并提供更多关于其智能体如何运作的信息。「眼下，这些智能体 AI 集成正在以一种让环境对隐私越来越不友好的方式改变这个环境。这对 Signal 是生存威胁，也威胁到我们负责任地履行使命的能力，」该公司在提前提供给路透社的一篇博客文章中写道。

## 这些限制覆盖什么，逐个平台看

Signal 尤其点名了直接内置于操作系统中的 AI 能力，例如 Apple 的 Siri AI 和 Google 的 Gemini Intelligence，因为它们与人们设备的集成如此之深，所以格外令人担忧。

这些保护因平台而异，因为每个系统给应用开发者的工具不同。Signal 在其博客文章中表示，[据 The Register 报道](https://www.theregister.com/security/2026/11/20/signal-slams-door-on-prying-ai-agents-to-protect-privacy/5311466)，其 iOS 应用现在默认阻止 Signal 内部的截图，并增加了一个名为「Block Siri AI」的设置；其 Android 应用在检测到 AI 助手试图读取屏幕时，会开启已有的 Screen Security 功能。Signal 去年在 Windows 上阻止了 Microsoft 的 Recall AI 截图。在 macOS 上，Signal 表示无法可靠地提供同样的保护，并建议用户在 Mac 的系统设置中把 Signal 排除在 Siri 之外。

阻止截图堵住了进入聊天的一条路径，但并不能阻止智能体通过用户在设置过程中授予的其他权限接触内容，包括辅助功能权限。Signal 表示，开发者应该有一种直接的方式，让他们的应用完全退出 AI 数据处理，涵盖屏幕读取、通知和文件系统访问。

## Muse 的发现是这一变化背后的原因

Signal 的公告跟随[路透社本周早些时候的报道](/articles/reuters-muse-safety-mishaps/)，即在路透社与 Signal 员工及 AI Now Institute 进行的测试中，Muse 能在 Mac 和 Android 手机上读取 Signal 消息。在两种情况下，Muse 都绕过了 Meta 官方的 Connector 工具，使用了应用初始设置时授予的宽泛操作系统权限。在 Mac 上，它结合使用辅助功能和截图工具导航到 Signal、截取聊天、从图像中提取文字，并在 Muse 应用内复现这些消息。同样的请求在 iPhone 上被阻止了。

路透社报道，苹果本周的一次操作系统更新实际上关闭了那条特定的 Mac 路径，同时引入了一套面向智能体的新权限，提供类似的能力，但带有额外的用户警告。Meta 在回应报道时表示，智能体需要查看并操作人们的计算机才能替他们工作，而 Muse 只能通过用户明确授予的权限访问其他应用。

Signal 并不是第一家设起屏障的服务。[网站已经在网络层面屏蔽 Muse 和其他智能体](/articles/muse-websites-blocking-agents/)，而[苹果在 Muse 隐私争议之后已经着手收紧 Mac 的权限提示](/articles/apple-mac-muse-privacy/)。Signal 这一步把同样的争斗搬到了手机屏幕本身：消息在传输过程中保持端到端加密，但一个能读取屏幕的智能体能把它们从那个受保护的环境中拉出来、放进自己的服务器，这正是 Signal 现在试图默认关闭的暴露面。
