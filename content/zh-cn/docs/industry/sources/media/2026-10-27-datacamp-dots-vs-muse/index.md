---
title: "OpenAI Dots 与 Meta Muse：谁赢了？"
linkTitle: "Dots 与 Muse 横评"
date: 2026-10-27
originalTitle: "OpenAI Dots vs. Meta Muse: Which Agent Wins?"
sourceUrl: "https://www.datacamp.com/blog/openai-dots-vs-meta-muse"
author: "Josef Waples"
publisher: "DataCamp"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
tags: [实测评测]
products: [dots, muse]
---

{{< source-info >}}

**收录说明**：直接下载。原站此前对自动访问返回 403，本轮实测已恢复 200，可直接抓取。原文中的两处课程推广句与文末作者简介已去掉；FAQ 的折叠标记已清理。文中价格表称 Muse「仅限美国」，与 10 月 23 日日本、10 月 27 日新加坡上线的时间线不符，照录原文。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文章按模型、架构、安全、集成、定价与可用性六个维度对比 OpenAI Dots 与 Meta Muse。Dots 是 ChatGPT 内的持续性智能体，用 GPT-6 Astra，各自拥有云端电脑与浏览器，可通过 4000 多个应用接入工作场所工具，定位是工作场景；Muse 用 Muse Spark 1.3、运行在 Muse Secure VM 上，定位是生活事务，支持 Stripe 付款并有免费档。两者均无独立基准、无 API，均表示智能体会犯错；作者建议先从一项有边界的周期任务试起，密切检查后再扩大授权。

**保留理由**：两款产品的系统性案头对比，覆盖架构、安全与定价口径，结论区分了「为工作」与「为生活」的不同定位，是已收横评中少有的结构化对照。

---

两家最大的 AI 实验室相隔三周推出了同一个想法：一个不必等待你下一条提示词的 AI 智能体。它不是一次回答一个问题，而是在云端拥有自己的电脑，持续朝着你给它的目标工作，并在需要你做决定时给你发消息。

Meta 率先推出了 [Muse](https://www.datacamp.com/blog/muse-agent)，这是一款被它描述为「为所有人打造」的消费级智能体。OpenAI 随后在 DevDay 上推出了 [Dots](https://www.datacamp.com/blog/openai-dots)，将其宣传为可以 24/7 持续朝着你的目标工作的常驻智能体。

纸面上，两者听起来几乎一样。在实践中，它们对用户是谁、智能体应该住在哪里，以及你需要对它拥有多少控制权，做出了不同的押注。

在本文中，我将从模型、架构、安全、集成、定价和可用性几个方面对它们进行比较。最后会给出先试哪一款的建议。

**简版：** 人们是这样看的：

- Dots 为工作而建。它们接入工作场所工具，提供细粒度的管理规则，并朝着专业企业智能体的方向发展。
- Muse 为生活事务而建：购物、预订和跑腿，通过 Stripe 提供支付保护，并且有免费入口。

## 什么是 OpenAI Dots？

dot 是 ChatGPT 内部的一个持久化智能体。你给它持续性的职责，例如每周一跟踪竞争对手价格、分拣收件箱或准备周报，它会在你们的对话之间继续处理这些事。

关键事实：

- **模型：** [GPT-6 Astra](https://www.datacamp.com/blog/gpt-6-astra)。
- **计算：** 每个 dot 都有自己的云端电脑和浏览器。你可以打开那台电脑观看它正在做什么，也可以选择把 dot 连接到你的笔记本电脑。
- **在哪里使用：** 桌面端、网页端和移动端的 ChatGPT（包括语音通话），以及 Slack 和 Teams。上下文会在它们之间延续。
- **应用：** 通过 OpenAI 的插件生态接入 4,000 多个应用。
- **专业 dot（预览）：** 拥有自己的身份、凭据和系统访问权限的企业智能体。它们正在采购、发票处理、电子邮件营销、客户支持和合同等场景中试点。

## 什么是 Meta Muse？

Muse 是 Meta 的个人 AI 智能体。它被设计用来承接过这样的目标：「找到并预订一次 800 美元以内的周末旅行」或「把这个保存的食谱短视频变成一份杂货订单」，然后在你已连接的应用中执行它们。

关键事实：

- **模型：** [Muse Spark 1.3](https://www.datacamp.com/blog/muse-spark-1-3)，拥有 100 万 token 的上下文窗口。
- **计算：** Meta 云中专用的 Muse Secure VM，拥有自己的浏览器、文件系统和终端。你可以在它工作时观看浏览器。
- **在哪里使用：** iOS 和 Android 上的 Muse 应用、muse.ai 和 WhatsApp。AI 眼镜支持以及 Muse Charm（一款无需手机即可使用 Muse 的小型钥匙扣设备）已于 9 月 23 日宣布。
- **商业合作伙伴：** Stripe、Shopify、Best Buy、Gap、Sephora、Walmart、Wayfair、Expedia、Instacart 等。
- **个性化：** 你可以设置智能体的名称、化身和沟通风格。

## OpenAI Dots 与 Meta Muse：正面对比

让我从几个类别对它们进行比较：

### 模型与智能

Dots 运行在 GPT-6 Astra 上，Muse 运行在 Muse Spark 1.3 上。两家公司都声称达到前沿水平的智能体性能。然而，Meta 关于与 OpenAI 和 Anthropic 持平的说法依赖其自己的数据，而且目前两款产品都没有独立的智能体基准测试。

一个实际差异：Muse 的最高推理模式在发布时因等待安全测试而未开放。Dots 则获得完整的 Astra 模型。

### 架构：两种云端电脑

两款智能体都运行在远程机器上，而不是你的设备上。这使它们可以在你的笔记本电脑合上时继续工作。

- **Dots** 为每个智能体提供自己的云端电脑，除非你主动连接，否则它与你的电脑保持分离。如果监测系统发现安全隐患，它可以暂停或停止某个 dot。
- **Muse** 把智能体*和你的数据*放在专用 VM 上。第二个智能体 Sentinel 运行在同一台机器上，但在系统层面与 Muse 隔离。没有 Sentinel 的批准，Muse 无法访问互联网；Sentinel 在不确定时会询问你。

Muse 的守门人设计是更具特色的想法。

### 安全与权限

Dots 为你提供一个规则引擎：

- **自定义规则（Custom Rules）** 让你允许、要求批准或阻止特定操作。
- **自动审查（Auto-review）** 会检查任何可能影响你的账户或共享信息的操作。你无法关闭它。
- **主动研究（Proactive research）** 默认使用只读工具运行，因此 dot 在后台工作时无法发送消息、更改内容或控制浏览器。

Muse 使用权限模型：

- 你逐个连接应用，并为每个应用选择访问级别。例如，你可以让它读取电子邮件，但不能发送。
- 在发送电子邮件或进行购买等敏感操作之前，它会与你确认。
- 它会保留已完成和计划中操作的审计记录。

两款产品都允许智能体使用已保存的登录信息，而不向模型暴露密码。OpenAI 通过 ChatGPT 的凭据处理来实现这一点，Meta 则通过安全存储。

底线：如果你需要对智能体能做什么进行精确控制，尤其是在团队范围内，Dots 提供更多选项。Muse 一眼看上去更容易理解，但评测者一直要求更细粒度的权限，例如限制对特定 Instagram 账户的访问。

### 集成与使用场景

Dots 存在于知识工作者已经在的地方：ChatGPT、Slack 和 Teams，拥有 4,000 多个应用连接，并正在推进 Microsoft Agent 365 集成。

Muse 存在于消费者已经在的地方：它自己的应用、WhatsApp、Instagram，以及即将支持的 Meta AI 眼镜。它的集成偏向商业。结账通过 Link by Stripe 进行，后者会签发一次性卡，因此智能体永远看不到你的真实卡号。Meta 表示，Muse 是第一个受 Link 购买保护覆盖的 AI 智能体，包括丢失或损坏物品的保障以及免费退货。

对商业的专注也带来了摩擦。9 月 21 日，Amazon 在其零售网站上封堵了 Muse，称该智能体没有表明自己的身份。Meta 对 Amazon 的说法提出异议。

Meta 此后推出了面向小企业的 Muse，将该智能体连接到 Slack、Zoom 和 Salesforce 等工具。

### 记忆与主动性

两款智能体都会记住上下文：

- **Dots** 会从反馈中学习、运行定时检查并进行主动研究。不过在发布时，你无法查看或编辑单条记忆。
- **Muse** 会记住你只提过一次的细节，并主动提出建议。你可以让它「忘记」特定内容。

### 隐私与数据使用

- **Dots：** Business、Enterprise 和 Edu 工作区数据默认不用于训练。个人计划用户可以选择自己的数据是否用于训练。
- **Muse：** 交互默认用于训练，你可以在设置中选择退出。10 月，一个安全团体报告称，共享的 Muse 聊天可以通过公共 DNS 记录被发现，Meta 因此暂停了聊天分享。

对于受监管或敏感的工作，OpenAI 的工作区默认设置目前是更安全的起点。

## 定价与可用性

|  | OpenAI Dots | Meta Muse |
| --- | --- | --- |
| **入门价格** | 包含在 ChatGPT Pro（每月 100 美元起）或 Business Premium（每席位每月 100–125 美元）中 | 免费档（注册时需要支付卡） |
| **付费档** | 包含第一个 dot；更多 dot 和更高容量已计划但尚未定价 | Power：每月 20 美元；Maximum：每月 100 美元 |
| **用量限制** | 第一个月延长限制；后续条款尚未公布。dot 聊天不计入 ChatGPT 限制 | 据报道免费档每周最多 1 亿 token；付费配额未公布 |
| **地区** | 仅限符合条件的市场。发布时 Pro 不含 EEA、瑞士和英国 | 仅限美国，18 岁以上成年人 |
| **平台** | ChatGPT 桌面端/网页端/移动端、Slack、Teams | iOS、Android、muse.ai、WhatsApp；眼镜和 Muse Charm 即将推出 |
| **企业版** | Enterprise/Edu/Healthcare 测试版（由管理员启用）；专业 dot 试点 | Muse for Small Business |
| **API** | 未宣布 | 未宣布 |

定价差距是两者之间最明显的区别。如果你在美国，今天就可以免费试用 Muse。要获得一个 dot，则意味着需要付费购买顶级 ChatGPT 计划。

## 你应该选哪一个？

**在以下情况下选择 OpenAI Dots：**

- 你已经为 ChatGPT Pro 或 Business Premium 付费。
- 你想交出去的工作发生在 Slack、Teams、文档和 SaaS 工具中。
- 你需要详细的审批规则，或者你的组织需要保护工作区内容的管理控制和训练数据默认设置。
- 你在美国以外，但身处符合条件的 OpenAI 市场。

**在以下情况下选择 Meta Muse：**

- 你在美国，想在不购买高级计划的情况下试用智能体。
- 你的待办清单主要是个人事务：购物、预订、旅行和家务。
- 你看重智能体结账时的购买保护和一次性卡。
- 你更多生活在 WhatsApp 和 Instagram 中，而不是 Slack 中。

**在以下情况下两者都不选：**

- 你不希望 AI 智能体代表你行动，无论是点击、购买还是发送消息。
- 你检查智能体工作所花的时间，会和你自己完成任务所花的时间一样多。
- 你不愿意让软件访问你的账户、支付方式或工作区内容。
- 你的任务不频繁或足够简单，一份待办清单、一个日历或一次保存的结账就能完成。

如果你需要按任务控制成本、可复现的评估，或两者都不支持的工作流，可以考虑自己构建智能体。Dots 和 Muse 目前都没有 API。我们的 [OpenAI API 教程](https://www.datacamp.com/code-along/ungated-getting-started-with-the-openai-api-and-chatgpt)和 [Muse Spark 1.3 教程](https://www.datacamp.com/tutorial/muse-spark-1-3-tutorial)是不错的起点。

## 最后想法

OpenAI 押注工作。Dots 存在于你的工作场所工具中，依赖详细的规则，并指向一个企业内拥有自己凭据的专业智能体的未来。Meta 押注日常生活。Muse 存在于你的消息应用中，处理支付，并提供一个免费档，把智能体带到数百万人面前。

两者都还处于早期。两者都没有独立基准测试，两家公司都表示其智能体会犯错，而且两者都有未公布的用量条款，可能会改变价值计算。我的建议是从一项有边界的周期性任务开始，密切审查智能体的工作，只有在它赢得你的信任后才扩大访问权限。

## 常见问题

Meta Muse 免费吗？

是的。Muse 有免费档，但注册需要支付卡。付费的 Power（每月 20 美元）和 Maximum（每月 100 美元）计划会提高你的用量限制。

使用 OpenAI Dots 需要 ChatGPT Pro 吗？

对个人来说，是的。在符合条件的市场，你的第一个 dot 包含在 ChatGPT Pro 或 Business Premium 中。Enterprise、Edu 和 Healthcare 工作区如果管理员开启，可以访问测试版。

我可以在美国以外使用 Muse 或 Dots 吗？

Muse 目前仅限美国。Dots 在 OpenAI 符合条件的市场可用，但在发布时 Pro 计划不含 EEA、瑞士和英国。

哪个智能体更安全？

它们采取不同的方法。Muse 使用 Sentinel，这是一个独立的智能体，任何互联网访问都必须经过它批准。Dots 使用可配置规则、强制的自动审查步骤和只读的后台研究。Dots 为团队提供更多控制，而 Muse 的模型更简单。两者都没有经过独立审计。

Dots 或 Muse 能替我买东西吗？

Muse 就是为此设计的。它通过 Link by Stripe 使用一次性卡结账，并会先征求你的批准。Dots 可以在已连接的应用中行动，但商业不是它们的重点，敏感操作受你的自定义规则和自动审查约束。

Dots 或 Muse 有 API 吗？

目前没有。两家公司都尚未宣布。要自己构建类似的智能体，可以使用 [GPT-6 API](https://www.datacamp.com/tutorial/gpt-6-sol-api-tutorial) 或 [Muse Spark API](https://www.datacamp.com/tutorial/muse-spark-1-3-tutorial)。
