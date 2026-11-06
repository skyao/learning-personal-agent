---
title: "How I AI：我对 GrokBot、Cursor Origin 和 Grok 4.6 模型的上手评测"
linkTitle: "Claire Vo：GrokBot 上手"
date: 2026-08-18
originalTitle: "How I AI: My Hands-On Review of GrokBot, Cursor Origin, and the Grok 4.6 Model"
sourceUrl: "https://www.chatprd.ai/how-i-ai/how-i-ai-my-hands-on-review-of-grokbot-cursor-origin-and-the-grok-46-model"
author: "Claire Vo"
publisher: "ChatPRD「How I AI」"
language: en
fidelity: 节选
translation: 已翻译
collectedAt: 2026-11-05
tags: [实测评测, 连接器]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：播客「How I AI」该期节目的文字版。全文评测 GrokBot、Cursor Origin 和 Grok 4.6 模型三项，这里只收导语、GrokBot 一节和结语，Cursor Origin 与 Grok 4.6 两节未收。原文多处把 Grok 写作「Groq」，照录。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Claire Vo 在 Grok Bot 发布一周后上手评测，把它描述为面向知识工作、托管式的轻量版 OpenClaw。她认为最大的亮点是插件和连接器的处理：可以同时连接多个邮箱和 Slack 账号，这是她用过的其他工具做不到的。新建 Bot 只需给出说明，例如让它当管理个人邮箱和日历的「家庭管理 Bot」，它会自行识别所需连接器；她已建了产品经理、承诺追踪、催款、案例写作、数据监控等多个专用 Bot，每个 Bot 都有带 Chrome、终端和文件系统的虚拟计算机。她认为 Grok Bot 开箱即用、上手顺畅，但可控性较低，不能选择底层模型，也不能深入配置。

**保留理由**：Grok Bot 发布初期的一手上手评测，指出了多账号连接和多 Bot 分工这两个特点，以及不能选模型的局限。

---

我在测试整个 Grok 生态，从 GrokBot 的多智能体工作区到 Cursor Origin 的智能体原生代码托管，并让 Grok 4.6 模型接受我个人的设计与编程基准测试。

![Claire Vo 的个人头像](images/img-01-c8e842.img)

Claire Vo

2026 年 8 月 18 日·阅读时长 10 分钟

## 工作流 1：用 GrokBot 进行多账户知识工作

首先是 GrokBot，一个以桌面和移动应用形式提供的聊天式智能体。可以把它看作类似 OpenClaw 的东西的更简单、托管式的替代品，专为知识工作设计。界面干净、简洁，沿用了那种熟悉的 iMessage 风格聊天体验。但我真正欣赏的是它对多智能体理念的坚持。GrokBot 不是用一个智能体统治一切，而是鼓励你为特定工作创建专门的智能体，每个都有自己的名称和用途。

![我的自定义 GrokBot 列表，包括 Prody McProd、commitment tracker 和 money maker bot](images/img-02-fb096f.img)

### 杀手级功能：每个连接器支持多个账户

如果我必须指出 GrokBot 里的一处魔法，那就是插件——具体来说，是它处理插件的方式。我一直认为 Cursor 拥有连接我技术栈中不同服务的最佳客户端，而他们把这种专长带到了 GrokBot，并带来了一项改变游戏规则的改进：你可以为一个服务连接多个账户。

这非常重要。我有一打不同的电子邮件地址和 Slack 账户，似乎没有其他工具理解这一现实。有了 GrokBot，我可以连接我全部四个 Gmail 账户和全部七个 Slack，我的智能体可以跨所有这些账户工作。仅这一项功能就能与我形成产品市场契合（product-market fit）。

![GrokBot 连接器设置，显示配置并激活了多个 Gmail 账户](images/img-03-73b38c.img)

### 我如何使用 GrokBot

设置一个新 bot 非常简单。你只需创建一个 bot 并给它指令。例如，我即兴创建了一个新的：

> I want you to be a family manager bot that keeps track of my personal email and personal calendar.


它立刻理解了，识别出必要的连接器，并开始工作。我已经设置了几个专门的智能体：

- **Prody McProd：** 我的产品经理 bot，接入了 ChatPRD。
- **Commitment Tracker：** 一个开箱即用的 bot，让我对自己的承诺保持诚实。
- **Money Maker：** 催收发票、付款和销售交易。
- **Case Study Buddy：** 帮我处理我正在写的一大批案例研究。
- **Data Monitor：** 监视我的 ChatPRD 数据中的重要趋势。

每个 GrokBot 还自带一台虚拟计算机，配有 Chrome、终端和文件系统。它就像 OpenClaw 的轻量版，让智能体能够浏览网页并执行命令。

![GrokBot 虚拟机界面，显示 Chrome 浏览器、Terminal 和 Files 图标](images/img-04-a574f9.img)

### 我的评价：简单、强大，但不适合黑客

GrokBot 最大的优点是它就是能用。上手引导顺畅，连接器属于顶级，多智能体方式也很直观。然而，这种简单对我来说也是它最大的缺点。我喜欢我那混乱、高维护成本的 OpenClaw 智能体，因为我可以无休止地调整和折腾它们。

> 「乐趣在于挑战。而我告诉你，GrokBot 没有挑战我，因为它运行简单，开箱即用。」

使用 GrokBot，你的控制更少。你不能选择底层模型，也无法深入其配置的细节。它所用模型的个性还有我称之为「Claude Slop」的东西——就是没有感觉。它不是那种我想与之相处的 bot。如果你在寻找一个高度可调、透明的智能体设置，你最好选择 OpenClaw 或 Hermes 之类的东西。但如果你想要一个强大、多账户、易于设置的智能体，GrokBot 确实令人印象深刻。

## 结语：是时候关注 Groq 了

在花了一周使用这些新产品之后，我的主要结论是 Groq 模型是一个真正的竞争者。GrokBot 对于任何想要一个简单但强大的多账户智能体、且不需要深度可折腾性的人来说，是一个极好的工具。Cursor Origin 是对未来的一个有趣押注，不过现在下结论还为时过早。而 Groq 4.6 模型本身确实很好，尤其是在创意设计任务上。

我仍然把大部分时间花在 Codex 和 GPT-5.6 模型上，但这次体验说服我更频繁地启动 Cursor 来编程。似乎可能是时候让我们所有人，至少在某种程度上，成为一个 Groq boy（或者 girl，或者 person）了。

我很想听听你的看法。你试过 GrokBot 吗？你认为 Origin 能取代 GitHub 吗？你有没有在任何编程任务中转向 Groq？在评论中告诉我吧。

---

### 赞助商的话

非常感谢我们的赞助商让本期节目得以实现。

- **bolt.new**：本期节目由 [bolt.new](http://bolt.new/howiai) 赞助，它是面向有想法并想将其交付的人的 AI 应用构建器。你描述想构建什么，Bolt 会在几分钟内生成生产就绪的代码。连接 Stripe，接上你的域名，然后在线部署。你只需要一个想法和一个周末。请在 [bolt.new/howiai](http://bolt.new/howiai) 查看。
- **Jira by Atlassian**：本期节目由 Jira by Atlassian 赞助。Jira 中的团队协作图（teamwork graph）能让智能体结果的准确率提高百分之四十四，同时 token 用量减少百分之四十八。团队协作图会从你的整个技术栈——从 Jira 和 Confluence 到 GitHub——拉取上下文，并在智能体写下任何一行之前直接提供给它们。同样的团队，更聪明的智能体。请在 [jira.dev](http://jira.dev) 免费试用。拼写是 J-I-R-A 点 D-E-V。

---
