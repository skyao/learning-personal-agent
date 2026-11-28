---
title: "The Neuron：Ignite 2026 的 Autopilot、Today 与 GitHub Copilot Fusion"
linkTitle: "Neuron 11-17"
date: 2026-11-17
originalTitle: "Microsoft Ignite 2026: Autopilot, Today, and the AI Updates That Matter"
sourceUrl: "https://www.theneuron.ai/news/microsoft-ignite-2026-copilot-autopilot-today-fusion/"
altUrls: []
author: "Corey Noles"
publisher: "The Neuron"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [发布, 交互渠道, 商业与规模]
products: [microsoft-autopilot]
---

{{< source-info >}}

**收录说明**：作者在 Ignite 现场撰写。直接下载，取正文；删去了网站导航、作者署名行、正文中插入的 The Neuron Academy 推广块、文末「Related reading」、广告与作者简介；三张配图下载到 images/。全文还写 Today 与 GitHub Copilot Fusion，Autopilot 是第一部分。已翻译。

**内容摘要**：文章从 Ignite 现场介绍 Autopilot、Today 和 GitHub Copilot Fusion 三项发布。Autopilot 被描述为组织 Microsoft 环境内、拥有自己记忆、工具和身份的常驻个人智能体，通过 Frontier 开始推出；同事可在 Teams 频道或群聊中 @mention 它。微软称其操作绑定自己的 agent identity、经过安全检查并对管理员可见。Today 分为 Today Brief（每日刷新含在 Microsoft 365 Copilot 许可内）和 Today Feed（需 Copilot credits），在 Frontier 中以私有预览进入 Copilot app 和 Outlook。文中还提到 Fusion 于 10 月 28 日 GA，以及 Agent 365 扩展成本与价值跟踪。

**保留理由**：Ignite 现场的媒体解读，区分了 Autopilot（承接持续性责任）与 Today（准备下一步）的分工，并给出 Today Brief 与 Today Feed 的计费拆分，已收资料没有。

---

Microsoft 想让 Copilot 在两次提示之间也继续推进工作。从旧金山的 Ignite 现场出发，我们拆解 Autopilot、新的 Today 体验和 GitHub Copilot Fusion，包括哪些已经可用、成本又落在哪里。

![Microsoft 标志与 AI 助手、日历和编码图标相连，旁边是标题「Microsoft Ignite 2026: Everything AI You Need to Know.」](images/img-01.avif)

我在旧金山参加 Microsoft Ignite，Microsoft 给出的发布多到够读一本小小说。

有三件事最值得你注意：Copilot Autopilot、新的 Today 体验，以及 GitHub Copilot Fusion。它们针对的是同一个问题的不同侧面，而任何把 AI 用于工作的人都认得这个问题：要从这些工具里得到有用的产出，仍然要费多少力气。

Autopilot 能让项目在两次提示之间继续推进。Today 准备好你的优先事项与下一步。Fusion 处理的是越来越复杂的一件事：该让哪些模型来做这项工作。

Microsoft 的说辞正变得更有意思，尤其是如果你的公司本来就活在 Outlook、Teams 和 Office 里。

- [Autopilot 是 Microsoft 对个人智能体竞赛的回应](#autopilot-is-microsofts-answer-to-the-personal-agent-race)
- [Today 把你的下一步准备好](#today-gets-your-next-steps-ready)
- [Fusion 替你拿掉模型选择这件事](#fusion-takes-model-selection-off-your-plate)
- [另外几项值得知道的更新](#a-few-other-updates-worth-knowing)
- [相关阅读](#related-reading)

## Autopilot 是 Microsoft 对个人智能体竞赛的回应

如果你一直在关注 Muse、Dots、Grok Bot 或 Claude Duet，你会认出 Microsoft 想做什么。

Autopilot 是一个常驻的个人智能体，在贵组织的 Microsoft 环境中拥有自己的记忆、工具和身份。它能跟进对话、处理周期性工作，并在不需要你逐步提示的情况下继续推进项目。

它正[通过 Frontier 开始推出](https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/)，这是 Microsoft 的早期访问计划。

最引人注意的是其他人如何与它互动。同事将能在 Teams 频道或群聊中 @提及 你的 Autopilot，请求信息或受支持的操作。当你在别处忙时，你的助手可以帮忙让共同的工作继续推进。

对个人智能体来说，这是一个有用的方向。大量工作停滞，就是因为有人需要一份进展、一次跟进，或一条埋在对话里的信息。

我们已经通过 [Meta Muse](https://www.theneuron.ai/explainer-articles/how-to-get-started-with-meta-muse/) 和 [OpenAI Dots](https://www.theneuron.ai/explainer-articles/openai-dots-hands-on-review-herman/) 探讨过常驻助手的吸引力。Microsoft 的潜在优势是与工作的距离近。对使用 Microsoft 365 的公司来说，大量相关信息已经在其软件里，连同决定谁能访问这些信息的权限一起。

Microsoft 说，Autopilot 的操作绑定它自己的 agent 身份，经过安全检查，并对管理员可见。这给公司提供了一种方式，把一个人做了什么与其助手做了什么区分开。

有用的控制。剩下的问题是，这个助手需要多少照看。

一个能可靠处理跟进的 agent 可以省下相当多时间。一个需要频繁纠正的，则是又一件要你操心的事。我感兴趣的是，当 Autopilot 承担起周期性责任、并积累了几周上下文之后，它表现如何。

![Microsoft 首席执行官 Satya Nadella 在旧金山 Chase Center 举行的 Microsoft Ignite 2026 上发表主题演讲。](images/img-02.avif)

Microsoft 首席执行官 Satya Nadella 在旧金山 Chase Center 举行的 Microsoft Ignite 2026 上发表主题演讲。｜Corey Noles 摄

## Today 把你的下一步准备好

Today 可能是最容易立刻体会到价值的一项发布。

它把邮件、日历、聊天和会议中的信息汇集起来，显示哪些需要你注意。然后它准备好下一步，包括邮件草稿、聊天消息和拟议的日程调整，供你审阅和批准。

一份只告诉你「你落后了」的简报，帮助有限。把回复起草好、把相关上下文备好，能让你先跑一步。

它有两个部分，计费上的区别值得了解：

- **Today Brief** 提供个性化的晨间简报并准备下一步。每日刷新包含在 Microsoft 365 Copilot 许可中。
- **Today Feed** 随着新信息到来全天更新。这些周期性更新需要 Copilot credits。

据 Microsoft 的 [Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/)，Today 正通过 Frontier 在 Copilot 应用和 Outlook 中进入私有预览。

Today 帮你追上进度并行动。Autopilot 处理随时间延续的工作。两者有重叠，但这个区分说得通：有时你想要下一步被准备好；有时你想把一项持续的责任交出去。

这个功能有多大用处，很大程度上取决于它选择呈现什么。如果所有事都需要注意，那它只是另一个收件箱。如果它能持续识别出少数真正重要的事并准备好有用的回复，它就给了人们一个理由，从 Copilot 开始一天。

## Fusion 替你拿掉模型选择这件事

即便你不整天写代码，GitHub Copilot Fusion 也值得注意。它展示了 AI 产品如何在不要求用户成为每个可用模型专家的情况下，处理更复杂的工作。

一个时间上的澄清：**Fusion 已于 10 月 28 日在 GitHub Universe 全面可用。** 今天的主题演讲是在此基础上扩展，据 [Microsoft 公布的讲稿](https://blogs.microsoft.com/blog/2026/11/17/ignite-2026-building-the-frontier-ecosystem/)，把 MAI-Code-2 和 MAI-Code-2-Flash 加进了 GitHub Copilot 和 Fusion。

Fusion 为一项任务选择并协调模型。它可以把工作发给一个模型，在升级到更强的模型之前检查草稿，或让几个模型在定稿前批评一个回答。你得到的是一份最终的答案。[GitHub 的文档](https://docs.github.com/en/copilot/concepts/models/copilot-fusion)解释了可用的方式。

这就免掉了一件熟悉的杂活：判断这个具体任务需要的是快模型、贵模型，还是换别的再试一次。

经济账看起来有吸引力。GitHub 报告说，在 Artificial Analysis 编码智能体指数上，Fusion Max 的得分与运行 Opus 5.5 Max 的 Claude Code 相差不到两分，而每任务平均 API 成本约为其一半，时间少约 40%。这些是[针对特定配置的基准结果](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/)，所以你的工作负载可能看起来不同。

Fusion 对它使用的模型收费。额外的审查会消耗更多 credits；收益取决于你是否把这份额外工作用对了地方。

Microsoft 正在把类似的想法用到工作场景的 Copilot 上。Cowork 中的 Auto 使用 Microsoft-Decision-1.1 来帮助判断一项任务的不同部分各需要多少努力。

随着 agent 承担更大的工作，这些决定成为产品价值的一部分。人们想要以合理成本得到好的工作成果。多数人会很乐意跳过模型选择的功课。

![Microsoft AI 首席执行官 Mustafa Suleyman 在旧金山举行的 Microsoft Ignite 2026 上发布 6 个新 AI 模型。](images/img-03.avif)

Microsoft AI 首席执行官 Mustafa Suleyman 在旧金山举行的 Microsoft Ignite 2026 上发布 6 个新 AI 模型。｜Corey Noles 摄

## 另外几项值得知道的更新

[Ignite 其余的发布](https://news.microsoft.com/events/ignite/2026/book-of-news/)为这些体验补上了一些实用拼图：

- **Copilot 中的 Office 已全面可用。** Word、Excel 和 PowerPoint 现在位于 Copilot 应用内，可进行编辑与协作，沿用现有的 Microsoft 365 权限与控制。
- **Microsoft AI 推出了六个新 AI 模型**，包括 Code 2、Code 2 Flash、Decision 1.1 等。
- **Copilot Code 将在 12 月全面可用。** 它让人们用自然语言构建应用与看板。Copilot Managed Runtime 现已可用，用于托管和管理受支持的应用。
- **Microsoft IQ 为 agent 打包业务上下文。** 可复用的指引、技能和工具，可以减少团队反复解释同一套公司规则的需要。
- **Agent 365 正在扩展成本与价值跟踪。** 当助手整天消耗资源、包括在你在忙别的事时，这一点很重要。

这些都在支撑主打的卖点：给 agent 足够的上下文去做有用的工作、一个做事的地方，以及围绕其访问和开支的边界。

Microsoft 在这里有一个可信的开局，因为它已经掌握了公司采取行动所需的那么多信息。Autopilot 和 Today 可能让这些信息更有用，而管理它的人付出的力气更少。

测试很直接：工作是否真的向前推进，而没有给你制造更多工作？

一次被正确处理的跟进、一份等着审阅的有用草稿，或一个在你在忙时向前推进的项目，会比聊天窗口里又一个漂亮的答案，为 Copilot 提供更有力的理由。
