---
title: "推出 Muse：全球首个面向所有人打造的个人 AI 智能体"
linkTitle: "推出 Muse"
date: 2026-09-08
originalTitle: "Introducing Muse: The World’s First Personal AI Agent Built for Everyone"
sourceUrl: "https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/"
publisher: "Meta"
language: en
fidelity: 全文翻译
collectedAt: 2026-11-04
updatedAt: 2026-09-30
tags: [发布, 运行环境, 安全, 开放与价格]
products: [muse]
---

{{< source-info >}}

[视频：Introducing Muse（发布视频）](https://about.fb.com/wp-content/uploads/2026/09/Introducing-Muse_Sizzle-Video.mp4)

## 要点

- Muse 是一个个人 AI 智能体。它不只是回答问题，而是真正去做事。它帮助人们掌控各种事务，接手他们手上的任务和项目，并把长期目标转化为行动计划。
- Meta 从零开始打造 Muse，使其成为一个安全、可靠、私密且广泛可用的个人 AI 智能体。
- Muse 运行在 Muse Secure VM 上，这是一台带有自己浏览器的专用安全计算机。Muse 可以在人们日常使用的各个应用中代表他们工作，从对话中学习，思考对他们重要的事情，并在此过程中变得越来越敏锐。
- 每个人都掌控着自己的 Muse，并决定给它多少访问权限。
- 如需深入了解 Muse 是如何设计的，以及安全、防护和隐私是如何构建进去的，请阅读[我们如何将安全构建进 Muse](http://security.muse.ai)和[我们如何设计 Muse](http://introducing.muse.ai)。

今天，Meta 推出 Muse，这是一个安全、私密的个人 AI 智能体，它会主动帮助人们实现目标并提出想法。由于个人智能体需要一种新型的安全计算机，[Muse 运行在 Muse Secure VM 上](http://security.muse.ai)，这是一台专用的虚拟机（VM），同时容纳智能体和个人的数据。Muse 是围绕人们已有的沟通方式设计的，因此与它交谈就像给另一个人发消息一样，可以在 Muse 应用中进行，也可以直接在 WhatsApp 中进行。

它使用起来很简单。人们只需告诉 Muse 需要完成什么，它就会采取行动。驱动它的是 [Muse Spark](https://research.meta.ai/blog/introducing-muse-spark-1-3)，这是 Meta 迄今能力最强的模型，专为此类现实世界的智能体工作而打造。

## 工作方式

与其他智能体不同，[Muse 是为全球数十亿人打造的](http://introducing.muse.ai)，因此没有学习门槛。任何人都可以开箱即用，无需任何技术经验。它可以处理各种任务，比如发送电子邮件或预订旅行，也可以承接宏大的目标。一旦有人与 Muse 分享了一个目标，它就会帮助对方制定个性化的计划，协调时间和资源，然后自行推进这项工作。它可以打开浏览器、填写表单，并代表他们进行谈判。

对于需要更长时间的任务，Muse 会在人们关闭应用后继续工作，并在情况发生变化或需要批准时回来，比如在发送电子邮件或进行购买之前。它以更少的投入获得更好的结果：把车卖出更高的价格，降低一笔账单，在某人生活中其他事情发生变化时调整其训练计划。

到了付款环节，Muse 可以使用 Stripe 打造的 Link 结账，它是首个受 [Link 购买保障](https://support.link.com/questions/what-s-covered-with-protections)覆盖的 AI 智能体：对符合条件的购买，免费保障物品损坏或丢失、价格下降、免手续费退货以及退货保证。Link 面向智能体的钱包会生成一次性使用的卡，让你的真实卡片信息保持隐藏，使你可以在互联网上安全购物。Shop Pay 即将作为另一种付款方式推出，同时还将支持 1Password，让 Muse 能够使用一个人已有的登录信息。

Muse 还会记住对一个人重要的事情，因此它可以在没有提示的情况下提出建议，并根据那个人只提到过一次的细节采取行动。它可以把一个人在 Instagram 上保存的食谱短视频变成一份购物清单，为他们的晚宴建议一份菜单，并在发出邀请之前记住他们朋友的饮食限制。

[视频：Muse_FieldTrip](https://about.fb.com/wp-content/uploads/2026/09/Muse_FieldTrip.mp4)

[视频：Muse_Japan](https://about.fb.com/wp-content/uploads/2026/09/Muse_Japan.mp4)

[视频：Muse_Relationships](https://about.fb.com/wp-content/uploads/2026/09/Muse_Relationships.mp4)

## 为私密、安全与防护而构建

个人智能体需要一种新型的安全计算机，所以 Meta 为每个人打造了一台。Muse Secure VM 内置了首创的隐私、安全与防护保护措施，这是其他任何智能体都没有提供的：

- Muse 运行在云端属于它自己的专用计算机上，经过隔离，其他任何人的智能体都无法触及它。那是 Muse 所在的地方，也是一个人所连接的任何服务的数据和凭证被安全存储的地方。
- 一个独立的 Sentinel 智能体运行在同一台机器上，在系统层面与 Muse 隔开。Muse 所做的任何事情，除非经 Sentinel 批准，否则都不会到达互联网；在需要时，Sentinel 会向本人请求许可。
- Muse 看不到人们的密码或付款方式。一个人与 Muse 分享的任何凭证都会进入安全存储，因此 Muse 可以使用它们而不会看到它们。Muse 也看不到一个人自己在浏览器中输入的密码。
- 在发送电子邮件或进行购买等敏感操作之前，Muse 会先与本人确认。Muse 会向人们展示它已经做过和计划要做的所有事情的完整审计记录。
- 人们选择 Muse 连接哪些应用，以及它确切获得多少访问权限。对于电子邮件之类的事物，人们选择 Muse 可以做什么：是只读取他们的邮件，还是也可以代表他们发送邮件。
- 人们可以随时更改访问权限或断开某项服务。人们也可以选择不让自己的互动被用于训练 Meta 的 AI 模型。
- Muse 不会与 Meta 的广告系统共享一个人的对话或其 VM 中的数据。
- Muse 会记住对一个人重要的事情，而他们随时可以让它「忘记」它所了解到的特定事情。

[视频：Muse_Shopping](https://about.fb.com/wp-content/uploads/2026/09/Muse_Shopping.mp4)

今年晚些时候，Meta 将推出 Muse Confidential VM，届时整个 VM，包括一个人的数据以及与 Muse 的对话，都将用只有本人持有的密钥加密，因此即使是 Meta 也无法访问。

## 展望

Meta 认为，个人超级智能将是一生中最具变革性的技术之一。Muse 是第一步：一个承担更多工作的智能体，让人们可以专注于对自己重要的事情。

Muse 正在美国的 iOS、Android 和 [muse.ai](http://muse.ai) 上陆续推出，并即将登陆 AI 眼镜。它在人们所需的大部分功能上是免费的，并为希望做更多事情的人提供订阅方案。
