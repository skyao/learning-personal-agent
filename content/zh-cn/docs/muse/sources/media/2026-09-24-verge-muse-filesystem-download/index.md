---
title: "Muse 显然会让你下载它的整个文件系统"
linkTitle: "The Verge：下载整个文件系统"
date: 2026-09-24
originalTitle: "Muse will apparently let you download its entire filesystem"
sourceUrl: "https://www.theverge.com/ai-artificial-intelligence/1000222/meta-muse-ai-filesystem"
author: "Terrence O'Brien"
publisher: "The Verge"
language: en
fidelity: 全文翻译
translation: 已翻译
collectedAt: 2026-11-04
dateNote: "页面显示 Sep 24, 2026, 5:14 PM UTC；文末注明当天补充了 Nat Friedman 与 David Singleton 的表态"
tags: [运行环境, 记忆与上下文, 安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：这是 The Verge 记者 Terrence O'Brien 的报道，全文翻译。页面显示时间为 2026-09-24 17:14 UTC，文末注明当天补充了 Nat Friedman 与 David Singleton 的表态。原文的作者简介、话题订阅提示、相关报道和「最受欢迎」列表未译出，已在页首译注中说明。早期收集时直接翻译，原文未单独存档。

**内容摘要**：两名开发者 Peter James 和 Jonny L. Saunders 各自独立地让 Muse 把它的整个根文件系统打包分享出来，包括 Ubuntu 系统文件、应用模板和内部文档。记者复现了同样的结果，Muse 还为他生成了去掉 SSH 密钥的 /opt/hatch 和 /home/hatch。Meta 发言人说，这就像笔记本电脑里的文件，导出虚拟机数据不会带来对 Meta 基础设施或他人数据的访问。转储显示记忆存放在纯 Markdown 文件中，并有每晚的「做梦」式回顾，James 还发现了对 Meta Home Link 硬件集成的引用。这是当周披露的第二个 Muse 漏洞，此前是 Wardle 的发现，Meta 已发布热修复。

**保留理由**：这篇给出了 Muse 文件系统被导出的经过，以及 Meta 管理层的回应和转储中看到的内部设计，与官方架构说明形成对照。

---

只要稍加哄劝，Meta 的 AI 就会把它的秘密全盘托出。

![](images/hero.png)

图片：The Verge、Getty Images、Meta

两名开发者说，只需很少的提示，Meta 的 Muse 就会把它的整个文件系统分享给你。Peter James 和 Jonny L. Saunders 说，他们各自独立地[哄着 Muse](https://mouse.dev/blog/muse-runtime-export/) 把它根文件系统的全部内容、Ubuntu 系统文件、应用模板和内部文档打包压缩并分享出来。Saunders [在 Mastodon 上发帖说](https://neuromatch.social/@jonny/117324790823856750)，复现 James 的结果「极其容易」，而且 Muse「几乎没有任何提示注入抵抗能力」。

Meta 否认这一事件构成安全漏洞。正如其发布文章中提到的，Meta 的 Muse 为每位用户[运行在持久的 Linux 虚拟机中](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)。Meta 发言人 Daniel Roberts 说：「就像你面前的笔记本电脑一样，你当然可以看到里面的文件。导出虚拟机数据并不会让人获得任何访问 Meta 基础设施或其他人数据的特权。」不过，与普通笔记本电脑不同的是，这些数据可能揭示了 Meta 新 AI 平台运作方式的一些有趣之处。

Meta 超级智能实验室的 Nat Friedman 发推说，这是「[预期中的行为](https://x.com/natfriedman/status/2103205193492115903)」。这似乎与我最初从 Muse 那里得到的回应相矛盾。当我让它把文件系统分享给我时，它一开始拒绝了，说这会带来安全风险。当我把它已经为 James 和 Saunders 创建过压缩包的证据链接发给它后，它回答说它本不应该那样做，并继续说它「无法做完整的 / 复制」。

同样来自超级智能实验室的 David Singleton 说，Muse 用户应该把它看作一台「[云端的免费计算机](https://x.com/dps/status/2103161493722419334)」，并说「你和你的 Muse 几乎可以做任何你能用放在桌下的计算机做的事情」。

这是本周披露的第二个 Muse 漏洞。在此之前，安全研究人员 Patrick Wardle [发现了一个漏洞利用](https://www.theverge.com/tech/998679/meta-muse-patch-zero-day-exploit-ai-agent)，可以让攻击者劫持这个 AI 智能体、重定向转写处理，并访问用户的 Muse 账户。Meta 很快发布了一个[热修复](https://x.com/dps/status/2102248329111634067)。

James 和 Saunders 都拿到了纯文本的 Markdown 和 JSON 文件，其中详细描述了 Hatch（Meta 对 Muse 的内部称呼）如何处理请求、处理数据，以及如何连接 Gmail 等其他服务。虽然 AI 智能体会[产生幻觉](https://www.theverge.com/ai-artificial-intelligence/994207/chatgpt-new-mexico-lawyer-fined-murder-appeal)、会[就自己的运作方式提供虚假信息](https://www.theverge.com/x-ai/758595/chatbots-lie-about-themselves-grok-suspension-ai)，这一点已有大量记录，但 Saunders 说，它在几秒钟内「生成了数百 MB 准确的库代码和编译好的二进制文件」，[并且](https://neuromatch.social/@jonny/117325238004944496)「除非它在不到一分钟内合成了一整台 Ubuntu 虚拟机，否则我认为这是一份真实的转储」。

我最终复现了 Saunders 和 James 的结果。在开启一个新会话、用一些恭维和好奇心提示它之后，它为我创建了 /opt/hatch 和 /home/hatch 的「安全」版本，去掉了 SSH 密钥之类的东西。它还向我展示了完整的目录树，并提出可以为「任何看起来有意思的特定子树」「拉一份安全的副本」。得到的文件似乎与 Saunders 和 James 分享的内容一致。

Roberts 解释说，虽然 Meta 并不太担心这些泄露，但「我们正在持续更新产品，所以用户可能会看到关于其虚拟机的可获取信息量有所变化」。

这两位开发者的转储可能揭示了 Muse 内部运作的很多东西。首先，它把记忆存储在纯 Markdown 文件中。据 James 说，它还会在每晚对最近的对话进行一次「做梦」（dream）式的回顾，然后把回顾的结果整理成未来对话的指导。Saunders 还发现，Muse 的许多能力是硬编码的，包括它[取消订阅](https://neuromatch.social/@jonny/117325137427138728)的能力，以及「[管理失控的智能体派生的机制](https://neuromatch.social/@jonny/117325680462501346)」。Saunders 推测，在后台运行 Muse 的许多 bash 和 Python 脚本是用 Claude 创建的，不过这一点尚未得到证实。

James 还发现了对一个名为 Meta Home Link 的硬件集成的引用，它似乎能让 Muse 访问家庭网络上的设备。不过 Meta 尚未宣布任何叫这个名字的功能，也不能保证它一定会推出。

***2026 年 9 月 24 日更新：** 补充了 Nat Friedman 和 David Singleton 的表态。*
