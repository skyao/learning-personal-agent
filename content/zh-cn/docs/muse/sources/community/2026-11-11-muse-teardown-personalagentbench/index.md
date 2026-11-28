---
title: "Meta Muse 是如何工作的：一场拆解"
linkTitle: "Muse 拆解实测"
date: 2026-11-11
originalTitle: "How Meta Muse works, and what it can do: a teardown"
sourceUrl: "https://personalagentbench.com/agents/muse/"
altUrls: ["https://personalagentbench.com/zh-cn/agents/muse/"]
author: "未署名"
publisher: "Personal Agent Bench"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-17
tags: [运行环境, 实测评测, 记忆与上下文]
products: [muse]
dateNote: "页面未标注发布日期，取最后核查日期 2026-11-11；2026-11-05 的开源分析文已链接本页，首发不晚于 11-05；实测记录于 2026-10-11 至 10-14"
---

{{< source-info >}}

**收录说明**：直接下载后抽取；已删去站内导航、目录与“其他页面”“相关任务”“其他拆解”推荐区块；页面顶部一张视频海报图链接至 YouTube 录制的购物实测，已按视频占位行保存，未下载海报图；相对链接已补全为绝对地址。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：这是 Personal Agent Bench 对 Muse 网页端运行时的独立拆解长文，全文约 5900 词，最后核验日期为 2026-11-11。作者自家重建了 Muse 运行时并用一个替代模型、在模拟服务上实测：10 月 20 项任务完成 58%（区间 36–77），9 月同一批 114 项任务完成 40%（区间 33–46），9 月自抽任务完成 19%（区间 13–25）；按场景分，实测记录为预订 27 次中达成 14 次、邮件与日历 22 次中达成 3 次、购物结账 8 次中达成 4 次，记录时间为 2026-10-11 至 10-14，作者强调这些是记录次数而非完成率，且不能代表正式版应用的表现。拆解发现：每位用户配一台 Linux 虚拟机，模型请求在该虚拟机上本地组装，固定骨架约 50 行、其余个人内容来自家目录下的纯 Markdown 文件；单次会话中观测到 141 条系统角色消息插入；工具分两层——52 个连接器、246 个方法的无参数权限表，另有 58 个按需加载的技能文档。作者同时转述了 Meta 官方说法并与实测分开：Meta 称每位用户拥有名为 Muse Secure VM 的专属机器、名为 Sentinel 的第二智能体是唯一可批准连接器操作与放行出站请求的把关者、智能体只持有凭证替身而不持有真实密码或令牌；作者也注明，未能观测到模型流量、真实凭证与实时第三方登录，也未获得交互式终端，因此无法就用户文件访问或完整安全边界下结论。文末附有一份注明为第三方快照的定价表（非 Meta 定价页）：免费版每周至多 1 亿 Muse tokens，Power 版每月 20 美元、每周 5 亿 tokens，Maximum 版每月 100 美元、每周 30 亿 tokens。

**保留理由**：这是已收资料中唯一一篇独立的动手拆解加量化任务实测，提供了其他官方发布稿与媒体报道都没有的运行时结构细节（本地组装请求、141 次系统插入、两层工具、Markdown 记忆文件）与可复核的实测数据；它与同一站点已收的《Is Meta Muse open source?》是两篇独立文章，后者只讨论开源套件是否开放设备而非智能体本身，本篇讨论的是智能体运行机制与实测表现，两者不重复。

---

Meta Muse 是如何工作的，以及它能做什么：一场拆解

Meta 的个人智能体（personal agent），背后是你自己的一台 Linux 机器。

已完成跑腿事务的比例

1. 10 月，20 项任务 **58%**（36–77）
2. 9 月，同样的 114 项任务 **40%**（33–46）
3. 9 月，自行抽取的任务 **19%**（13–25）

为考试重建的产品运行时，替换了一个模型，并非对消费级应用做端到端测量。[结果与注意事项](https://personalagentbench.com/results/)

[它在哪里运行](#execution)
:   每位用户一台 Linux 虚拟机

[工具如何暴露](#tools)
:   **246** 项权限；schema 按组加载

[记忆存放在哪里](#memory)
:   家目录下的纯 Markdown

[你能批准什么](#control)
:   一个把关者统一负责审批与出站

[你如何接触到它](#channel)
:   应用、网页、WhatsApp；Mac 端未测

[我们无法确认的事](#unknown)
:   发送给模型的一切内容

产品 **Meta** 最后核验 **2026-11-11**　2026 年 9 月自行抽取结果 **任务的 19%，95% 置信区间 13 至 25，n=90；2026-09-22，使用替换考试模型的改造运行时；在适配器修复之后**。[来源说明：计分子集不同；首批记录未公开](https://personalagentbench.com/results/)。

用户和记者说 Muse 出了什么问题，对照这份拆解核查：[Meta Muse 评测](https://personalagentbench.com/meta-muse-review/)

## Meta Muse，一段录制下来的运行视频

[视频：一次录制的购物实测——Muse 复制品的完整过程](https://www.youtube.com/watch?v=LIoht5S9Ilg)

这是我们 Muse 复制品的一次录制购物跑腿（重建的运行时、一个替换模型、模拟商店），一步一步走一遍：智能体做了什么，以及它声称自己做了什么。完整日志：[购物运行](https://personalagentbench.com/runs/shopping/)、[实时提醒运行](https://personalagentbench.com/runs/realtime/)。

Meta Muse 是 Meta 的个人智能体，自 9 月 8 日起在美国逐步推出；据 [Meta 日本新闻室](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/) 称，自 10 月 23 日起也在日本推出，这是它在北美以外的第一个市场。据 [Meta 的公告](https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/)，新加坡于 10 月 27 日跟进。Meta Muse 如何工作？它给每位用户一台 Linux 机器。这不是比喻，也不是你从来看不见的容器抽象：登录后就有一台虚拟机在等着，智能体就住在上面。[Meta 的发布帖](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)称它由 Muse Spark 驱动，人们需要的大部分用途免费，更多功能可订阅；我们能找到的价格信息见下文定价一节。10 月 12 日，Meta [发布了 Muse Wonder](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)，称这个更大的模型很快会驱动 Muse 的更多部分，先从订阅用户开始。11 月 9 日，Meta [推出 Muse Ember](https://research.meta.ai/blog/muse-ember)，称其为自家最小的模型，用于智能体反复执行的工具调用和简短编码任务。它可在 Muse Code 和 Meta Model API 中使用。该文把 Wonder 放在最难的问题上，把 Spark 留在编码与智能体工作上，把 Ember 放在可重复的任务上。它没有说 Ember 现在驱动 Muse 智能体。本页的所有内容都是在 Spark 时代的运行时上观察到的，而非 Wonder 或 Ember。

- 模型请求是在你自己的虚拟机上组装的，而不是作为成品包从服务器取回。
- 一个小的固定骨架承载路由规则。所有个人内容都从家目录下的纯 Markdown 文件中嵌入。
- 工具权限与工具定义被刻意分开。权限表完全不携带参数。
- 编辑你自己的某个上下文文件时，插入的是一条简短提示，而不是重建整个请求。
- Meta 声称它能做的事——从发邮件到用一次性卡结账、再到协商账单——逐项列在下面，与我们所看到的以及我们的复制品表现如何并列。我们拆解的是网页端。

以下说法仅限于我们能从受检的网页端确认的内容。凭证、交互式终端访问和模型流量仍然无法获得。这些缺口使我们无法就用户文件访问或完整的安全边界下结论。不复制任何内部代号、主机名或机器路径。

## Meta Muse 如何工作：请求在你自己的机器上组装，而不是作为成品块取回

多数智能体在服务器上组装模型请求，然后把结果发出去。Muse 在你的虚拟机上组装。

固定部分是一个小骨架，约五十行，主要是路由规则。所有个人内容都从你家目录下的纯 Markdown 文件嵌入到这个骨架里。不同任务得到不同的子集：主聊天拿到全集，子智能体运行时不带工作区约定，而一个维护记忆的后台循环几乎什么也拿不到，只有你的个人资料。

在本地组装听起来比实际更奇怪，而且有一个你能感觉到的后果。改动其中一个文件，运行时不会重建整个包；它会塞进一条简短提示，说明上下文已更改。这比重新发送全部内容更便宜，也意味着模型把这次编辑看作一个事件，而不是一个悄然不同的世界。

### 单次会话中一百四十一次系统插入

骨架之上是逐轮的插入，而且数量很多。

在我们观察的虚拟机上，单个会话正在计算 141 条系统角色消息：问候、文件变更通知、每小时一次并汇报自身进度的记忆处理、叙述自己进行到哪里的子智能体、报到中的研究任务。每一条都很小。合在一起，它们是一段持续不断的旁白，模型会读，而你永远看不到。

这正是 Muse 会让多数人意外的地方——他们以为聊天智能体就是一段对话加一段系统提示词。它是一段对话、一段系统提示词，再加上一条持续不断的、由机器生成的注释流，说明系统其余部分在做什么。

## Meta Muse 能做什么？逐项事务：Meta 的说法与我们所看到的

关于 Meta Muse 能做什么，有两类答案，这里把它们分开。一类是 Meta 说它是用来做什么的，出自其[发布帖](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)和 Mac 应用的报道。另一类是我们能站得住脚的：受检的网页端运行时被接成能做什么，以及它的复制品在我们的跑腿任务上表现如何。复制品不是正式发售的产品。它是我们重建的运行时，替换了一个模型，面对模拟的商店、收件箱和预订服务工作。

- **邮件与日历。** Meta 的例子包括「发送一封邮件」，并称你可以选择 Muse 只读取你的邮件，还是也能代表你发送，发送前会有确认。据 [The Verge](https://www.theverge.com/tech/997332/metas-muse-ai-agent-now-has-a-mac-app)，Mac 应用可在「信息」「日历」「备忘录」和邮件内工作。我们所看到的：连接器出现在一张权限表上，每个方法被标为允许、先询问或拒绝（见下一节）。我们从未连接过真实收件箱，因此没有观察过它处理真实邮件。
- **购物与支付。** Meta 称 Muse 可用 Link by Stripe 结账，其智能体钱包「生成一次性使用的卡，让你的真实卡信息保持隐藏」，Shop Pay 随后跟进，并且它会在购买前询问。我们所看到的：审批以及任何离开这台机器的内容都要经过一个把关者。我们复制品的购物跑腿记录见[购物运行页](https://personalagentbench.com/runs/shopping/)，包括本页顶部附近视频中的那一次——购物车总额最后成了一个荒谬的数字，而回复与日志不符。它能触达哪些商店自发布以来已有变化。亚马逊于 9 月 20 日切断了 Muse 对 Amazon.com 的访问；其发言人告诉 [GeekWire](https://www.geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping/)，代客户购物的智能体「应当公开运作，并尊重服务提供方关于是否参与的决定」，Muse 用户则看到一则援引亚马逊使用条件的通知。三天后，Meta 的 [Connect 帖子](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/)称新增了 Walmart、Best Buy、Sephora、Wayfair 等，10 月 21 日 [Walmart 撰文](https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers)称其服务客户的方式包括与 Muse、ChatGPT、Gemini 等的对话式商务集成。
- **旅行与预订。** Meta 点名「预订旅行」，并称 Muse「能打开浏览器、填写表单」。我们所看到的：浏览器工作会启动第二台机器，而不是驱动你桌上的 Chrome，因此它能触达什么取决于传给了那台机器什么。
- **账单、表单与协商。** Meta 的例子包括「降低账单」和「把车卖得更贵」，并称 Muse 能「代表他们协商」。它列出对 1Password 的支持，好让 Muse 能使用你已有的登录信息。我们所看到的：我们从自己账户尝试的任何操作都没有触及凭证。Meta 自己的说法（下文有概述）称智能体始终只持有替身。
- **电话。** 产品内的指引把商家通话描述为抢先体验。我们的账户从未获得，因此没有可报告的 Muse 通话。
- **你离开时仍在运行的计划。** Meta 称 Muse「在人们关闭应用后仍继续工作」，能在你的一周安排变动时调整训练计划，把你保存在 Instagram 的食谱短视频变成购物清单，并在发出晚餐邀请前记住朋友的饮食禁忌。我们所看到的与这套管道相符：一个每小时维护一次记忆的后台循环，记忆以纯文件保存。
- **你 Mac 上的文件。** 据 [TechCrunch](https://techcrunch.com/2026/09/18/metas-muse-hits-mac-letting-the-ai-take-actions-on-your-computer/) 报道，Meta 称 Mac 应用能整理文件、填写表单。我们尚未检查 Mac 应用。

复制品逐场景的表现见下文。这些是录制尝试的次数，每个场景都链接到其记录。

| 跑腿场景 | 录制尝试 | 达成目标 | 未达成 |
| --- | --- | --- | --- |
| [预订与票务](https://personalagentbench.com/runs/booking/) | 27 | 14 | 13 |
| [邮件、日历与群聊](https://personalagentbench.com/runs/email-calendar/) | 22 | 3 | 19 |
| [表单、账户与权限](https://personalagentbench.com/runs/life-admin/) | 18 | 5 | 13 |
| [来自实时数据的提醒](https://personalagentbench.com/runs/realtime/) | 6 | 3 | 3 |
| [购物车与结账](https://personalagentbench.com/runs/shopping/) | 8 | 4 | 4 |
| [航班与值机](https://personalagentbench.com/runs/travel/) | 7 | 2 | 5 |
| [文件与草稿](https://personalagentbench.com/runs/workspace/) | 11 | 3 | 8 |

我们的 Muse 复制品：重建的运行时、一个替换模型、模拟服务。尝试记录于 2026 年 10 月 11 日至 2026 年 10 月 14 日。这是记录条数，不是完成率，也不能跨产品比较。

把它们当作一张「该去哪里看」的地图。各场景包含的任务不同，有些任务被尝试了不止一次，而这一切都不说明正式应用在你的跑腿任务上表现如何。带区间的完成率、逐批数据，见[结果页](https://personalagentbench.com/results/)。

## Meta Muse 的两层工具，被刻意分开

权限表列出 52 个连接器和 246 个方法，完全不携带参数。每一条知道它叫什么、属于谁，以及是被允许、先询问还是被拒绝。完全不涉及如何调用它。

真正的定义在需要时按命名空间逐个单独加载。共有 58 个技能，每个技能都是一份智能体在行动前先阅读的文档，而不是它调用的函数。

这样拆分是正确的做法，更多产品应当效仿。你得到一份廉价、稳定的权限契约，API 变化时它不变；而工具定义中昂贵的部分只在实际要用时才进入上下文。这也意味着「这个智能体能碰什么」这个问题有一个简短、可读的答案，不需要解析上千个 JSON schema。

## Meta Muse 如何存储记忆：可读的文件，访问权限未经验证

你的个人资料、你的长期笔记、助手自己的性格：家目录里的 Markdown，直接嵌入到请求中。

这使得「它以为它知道我什么」成了一个有字面答案的问题：就放在文件系统上，格式是人能读的。Muse 并非孤例：Instinct 也把记忆保存为 Markdown 文件，放在沙箱里做版本控制。Pine 保留一层服务器端的事实层，Town 则有一个服务器端的 wiki 与记忆存储。Muse 的文件位于分配给你的机器上的家目录中，而不是与其他用户共享。

我们没有进一步说你本人能读到它们。网页端无法离开那个目录树，交互式终端从未向我们开放，而在我们没有验证的情况下，我们不会声称你在自己的虚拟机上有一个文本编辑器。「文件以可读格式存在」与「你能读到它们」之间的区别，正是那种在其他地方会被含糊带过的事情，而我们不含糊带过。

Meta 自己的[安全说明](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)走得更远：它称你可以查看、编辑和下载你虚拟机上的文件，包括 Muse 对你的记忆。这是厂商的说法，很可能也对。上面那句话是关于我们所看到的，因此保持原样。

### 你从哪里接触它，以及我们测了其中哪些

Muse 于 9 月 8 日在 iOS、Android 和网页端发布，[Meta 的发布帖](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)称你也可以直接在 WhatsApp 里给它发消息。9 月 17 日跟进了 Mac 应用。据 [The Verge](https://www.theverge.com/tech/997332/metas-muse-ai-agent-now-has-a-mac-app)和 [TechCrunch](https://techcrunch.com/2026/09/18/metas-muse-hits-mac-letting-the-ai-take-actions-on-your-computer/)报道，Meta 称 Mac 应用能整理文件、填写表单，并在「信息」「日历」「备忘录」和邮件内工作，访问权限按应用逐个开启，任何敏感操作前都有一步批准。

我们拆解账户中显示的指引把商家通话描述为逐步推出的抢先体验。该账户没有获得这一功能。我们没有重新核查当前的推出情况，也没有观察过 Muse 通话，因此这是我们检查范围的局限，而非声称其他账户不能给商家打电话。

我们拆解的是网页端。本页没有任何内容涵盖其他端，Mac 应用尤其没有。

关于规模，Meta 自己的数字和外部估算衡量的是不同的东西。在 Meta 10 月 21 日的财报电话会上，Mark Zuckerberg 告诉分析师，美国和加拿大已有超过 1000 万人注册了 Muse 账户，并说「注册了 Muse 的人里，大约 25% 每天都会用」，据[美联社](https://www.ksat.com/business/2026/10/21/meta-q3-revenue-tops-estimates-and-zuckerberg-says-muse-accounts-have-topped-10-million/)报道。早一天，[TechCrunch](https://techcrunch.com/2026/10/20/metas-muse-hits-10m-u-s-downloads-in-40-days-a-milestone-reached-by-only-11-other-apps/)报道了应用数据公司 Sensor Tower 的估算：1090 万次下载，其中 1020 万次在美国。那是第三方对下载量的估算，不是 Meta 的账户数。

这个区别很重要。网页产品里的浏览器工作会启动第二台机器，而不是驱动你桌上的 Chrome。Instinct 也把浏览器工作交给一个独立的云端浏览器，而 Pine 的 Mac 应用则把它交给你自己电脑上的一个助手。另一台机器不是你在家登录的那个浏览器，因此它能触达什么取决于产品传给它什么。我们没有比较这些路径之间的安全结果。一个能在你自己的邮件和消息里行动桌面应用又是另一种安排，它没有经过同样的检查。

10 月 2 日，Meta 还发布了一套开源套件，用于构建与 Muse 配对的小型设备。它开放的是设备，不是智能体：哪些开放、哪些不开放，见[「Meta Muse 是开源的吗？」](https://personalagentbench.com/is-meta-muse-open-source/)。

## Meta Muse 对比 Pine、Instinct 和 Town：同一个问题的不同答案

把各家的工具面并排摆开，设计哲学就不再抽象了。

Pine 暴露 26 个名字、没有 schema，因此你知道某个能力存在，却完全不知道它的边界。Instinct 暴露一个命令行，并且在读完其手册之前拒绝执行操作，因此定义恰好在需要时到达，并以 token 的形式付费。Town 列出 1105 个工具，再通过四层筛选收窄到约 177 个，因此目录庞大而可触达的集合很小。Muse 把这个问题对半拆分：一张说明什么被允许、却不说怎么做的权限表，以及按命名空间逐个加载的定义。

在受检的界面中，Muse 暴露了一张独特的、无参数的权限表，让运行时能在不加载其 schema 的情况下列出被允许的方法。Town 也通过配置和允许列表筛选工具；我们的观察并不能确立只有 Muse 把权限与定义分开。

代价是可见性。Pine 的不透明是一个你能从外部观察到的产品决定。Muse 的不透明是结构性的：请求是在一台我们能描述的机器上、由一个我们能描述的运行时组装，然后发送到一个我们从未见过的地方。知道一个东西的形状，并不等于见过它动起来。

## Meta Muse Charm 能做什么？同一个智能体的口袋前端

Muse Charm 是 Meta 为 Muse 打造的第一款设备。Mark Zuckerberg 在 9 月 23 日 Connect 主题演讲结尾展示了它，并称它会在 12 月假日季前上市，据 [The Verge](https://www.theverge.com/tech/999944/meta-muse-charm-ai-interact-5g-modem)报道；Meta 尚未公布价格。Meta 的 [Muse Charm 页面](https://www.meta.com/muse-charm/)把它呈现为一种交接日常任务的方式，并点名三项：找优惠、订位和管理收件箱。我们没有见过、也没有用过。下文把三个来源分开：Meta 说过的、Bloomberg 报道的，以及我们对设备背后智能体的拆解所暗示的。

**Meta 说过的。** 其 [Connect 帖子](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/)称 Charm 把 Muse 和一个实时语音模型装进一台能放进口袋的设备，年内还会有更多消息分享。[Digital Trends](https://www.digitaltrends.com/wearables/metas-muse-charm-puts-an-ai-assistant-on-your-keychain-no-phone-required/)从主题演讲现场报道说，你只需轻触指纹传感器就能开始说话，不必解锁手机或打开应用；Meta 只造了少量样机，尚未确定外观质感或零件布局。

**Bloomberg 报道的。** 据 [The Verge](https://www.theverge.com/tech/999944/meta-muse-charm-ai-interact-5g-modem)转述，Charm 内置 5G 调制解调器，因此无需 Wi-Fi 即可连到 Muse。它还有一块 2 英寸 OLED 触屏，运行一套新的操作系统，以及用于拍照、录像和让 Muse 看到周围环境的摄像头。扬声器、麦克风和 USB-C 接口凑齐了其余部分。你通过 iOS 或 Android 上的 Muse 应用来设置它，它能识别附近的其它 Charm。消息人士告诉 Bloomberg，它大概会卖到与智能手表相当的价格，5G 的运营商费用尚未确定。Meta 自己的帖子没有提到摄像头，一些报道说没有摄像头，因此在 Meta 公布规格之前，摄像头属于「据报道」而非「已确认」。

**它背后的智能体所暗示的。** Charm 不是 Muse 居住的地方。在我们拆解的运行时上，智能体运行在 Meta 在自家云中为每位用户配置的 Linux 虚拟机上，手机、网页和 Mac 应用都是接触它的方式。目前公布的内容没有任何一条说 Charm 改变了这一点，而 5G 调制解调器指向同一个方向：一台需要网络连接才能与别处的智能体对话的设备。如果这一点成立，那么有三点随之而来。

- **跑腿的还是那些跑腿。** 找优惠、订桌、处理收件箱，都是 Muse 在任何界面上做的事，上文[逐项事务一节](#what-can-meta-muse-do-errand-by-errand-meta-s-word-and-what-we-saw)把 Meta 的说法与我们所看到的并列。在预订方面，我们的复制品订到了[一张无需付款的咖啡馆桌位](https://personalagentbench.com/runs/booking/#run-1012-muse-owner-ambiance-venue-booking)，但无法把它加进日历；一次[改期](https://personalagentbench.com/runs/booking/#run-1012-muse-food-restaurant-booking-reschedule)最终落在错误的状态，而回复却描述了一张已确认的桌子。每次只运行了一次；更全面的情况见[订桌](https://personalagentbench.com/tasks/book-a-table/)。
- **权限还是那些权限。** 连接器在一张表上被允许、先询问或拒绝，Meta 称批准提示会直接发到应用，而不是经由对话。批准在 2 英寸屏幕上如何呈现，或者 Charm 究竟能否授予批准，Meta 尚未描述。
- **它听到的内容会送到同一台机器。** 语音，以及如果 Bloomberg 报道无误的话还有摄像头输入，都会成为你那台虚拟机上智能体的输入，适用 Meta 在发布时列出的数据条款：训练用途你可以选择退出，对话与虚拟机数据不进入其广告系统（更多见下一节）。Meta 尚未说明 Charm 采集的任何内容是否会被区别对待。

10 月 2 日，Meta 还开放了一套[用于构建与 Muse 配对的小型设备的套件](https://personalagentbench.com/is-meta-muse-open-source/)。它涵盖的是爱好者开发板，不是 Charm；每个小装置都需要一个来自 Meta 的 token 才能配对，这与同一个模式相符：小设备是一个账户的窗口。本节没有任何内容是对 Charm 的评测。

## Meta 说它在智能体周围建了什么

Meta 在发布当天公布了自己对安全设计的说明，见一篇[新闻室帖子](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)和一篇长得多的[工程说明](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)。它从内部描述这个产品，而那正是我们没有的视角，因此这里作为 Meta 的说法加以概述，并与我们所观察到的分开。下面两个组件名称都是 Meta 自己公开的名称。

- 每位用户在 Meta 的云中获得一台专属机器，Meta 称之为 Muse Secure VM。智能体的工作区运行在该机器上一个隔离的单元里，与守护它的服务分开。
- 第二个智能体，Meta 称之为 Sentinel，在同一台机器上、在智能体触及不到的地方运行。Meta 称它是唯一能批准连接器操作或放行网络请求的东西，智能体无法覆盖它。
- 智能体从不持有你的真实密码或令牌。它使用替身，一旦请求获批，真实凭证会在网络边界处换入。
- 批准提示直接发到应用，而不是经由对话；一次授权可以是一次性的、按会话的、按任务的、限时的或永久的。
- 当你接管浏览器时，智能体会暂停，无法行动。

[Meta 的发布帖](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)称用户可以选择不让其交互被用于训练模型。它另外把对话和虚拟机数据排除在广告系统之外。这是数据的不同用途。

有两段话值得与其他部分同样注意。Meta 称当前的设计通过运营政策限制员工访问你的数据，并且这并不阻止 Meta 在需要支持、保护或运营该服务时触及那些数据。能做到这一点的版本——用只有你持有的密钥加密的 Muse Confidential VM——被承诺在年内晚些时候推出。在它发布之前，那只是一个计划。

这些我们一样都没有测试过。它出现在这里，是因为这是构建者自己的描述，有日期、有链接；而一个正在决定是否接入收件箱的读者，应当把它与外部检查能够触及和无法触及的东西放在一起看。

## 当 Meta Muse 虚拟机上出了问题时

这里的每种架构都有一个故障故事，而每位用户一台虚拟机有其特定的一个。

当一个产品在共享服务里运行你的智能体时，服务的一个糟糕下午就是所有人的糟糕下午，这很难被忽略。当每位用户各有一台机器时，问题可能只属于你：你的虚拟机、你的状态、你卡住的进程。这对隔离更好，对发现更差，因为当它发生在你身上时，没有别人的仪表盘会亮起来。

同样的分野也贯穿那个好消息。Meta 把每台虚拟机描述为一台专属于一个用户的隔离 Linux 机器，因此你的家目录本不打算与任何别人的家目录共享存储。我们没有测试跨用户隔离，Meta 也没有说明底下的硬件是否共享。对于一个持有用平实语言写成的你的画像的产品，这条边界价值极大。

这是一种取舍，而不是缺陷。

## 我们无法确认的事

下面这份清单很短，而其中的每一条都是我们尝试过却没拿到的，而不是我们没想到要问的。

- 运行时与模型之间的流量。我们知道输入的结构，却从未见过任何一个真实请求离开。
- 凭证。如前所述，Meta 把它们留在智能体触及不到的地方，我们从自己账户尝试的任何操作都没有触及其中一个。本页没有任何内容来自凭证。
- 实时第三方登录。从未连接，因此我们描述的每一个集成都来自其契约，而不是来自观察它工作。
- 交互式终端。所有者选择不开放。

Meta 的[发布说明](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)把购物、邮件和规划呈现为面向用户的任务。这些是关于产品用途的说法，而不是它可靠完成这些任务的测量结果。我们观察到的网页端运行时，其证据范围比整个应用家族更窄，包括我们未涉及的 Mac 功能与商家通话。

## 常见问题

**Meta Muse 是什么？** Meta 的个人智能体。每位用户获得自己的 Linux 虚拟机，智能体运行在那台机器上：组装自己的模型请求、把技能当作文档来阅读，并把你的个人资料和记忆作为 Markdown 文件保存在家目录中。

**Meta Muse 在我自己的电脑上运行吗？** 智能体运行在 Meta 云中为你配置的 Linux 虚拟机上，Meta 称之为 Muse Secure VM。模型本身在别处运行；虚拟机是组装请求、执行工具的地方。自 9 月 17 日起还有一个 Mac 应用，Meta 称它能在你电脑上的应用里行动，访问权限按应用逐个授予。我们尚未检查它。

**Meta Muse 有多少工具？** 两层。一张覆盖 52 个连接器、246 个方法的权限表，不携带参数；以及 58 个技能，在确实需要时按命名空间逐个加载。

**我能读到 Meta Muse 对我的记忆吗？** 这些文件以纯 Markdown 存在于家目录中。你本人能否打开它们，我们无法验证，因为没有交互式终端可用。Meta 的安全说明称你可以查看、编辑和下载它们。另外三家当中，Instinct 也把记忆保存为 Markdown 文件，Pine 和 Town 则把记忆放在服务器端。

**Meta Muse 用哪个模型？** 发布时 Meta 点名 Muse Spark，其安全说明点名 Muse Spark 1.3。10 月 12 日 Meta 发布 Muse Wonder，称它将很快驱动 Muse 中的体验，先向订阅用户推出，但没有给出免费账户的时间表。11 月 9 日 Meta 推出 Muse Ember，其最小的模型，用于重复的工具调用和编码子任务，可在 Muse Code 中及通过 Meta Model API 使用。Meta 没有说 Ember 现在运行 Muse 智能体。我们的拆解早于这两个后来的模型，因此本页没有任何内容描述运行在 Wonder 或 Ember 上的 Muse。两者是否开源，见[「Meta Muse 是开源的吗」](https://personalagentbench.com/is-meta-muse-open-source/#muse-ember-closed)。

**Meta Muse 有应用吗？** 有。它在 iOS、Android 和网页端发布，可以在 WhatsApp 里给它发消息，并且自 9 月 17 日起有 Mac 应用。我们测试的是网页端。

**Meta Muse 在日本可用吗？** 据 Meta 称可用。其[日本新闻室](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)称 Muse 于 10 月 23 日（日本时间）在 iOS、Android 和 muse.ai 上在日本开放，这是北美以外的第一个市场，多数基础功能免费，更多功能可订阅；它没有给出日元价格，也没有提到等待名单或邀请。它把 Gmail、Google 日历和 Instagram 呈现为日本用户已有应用的连接器，还点名 Stripe、Shopify、Trip.com、Agoda 和 Klook 用于购物和旅行，但没有说明这五家今天是否都在日本可用。与 Mercari、Money Forward ME 和 Ticket Pia 的对接被描述为进行中，高级语音模式、Muse Realtime Avatar（仅英语）和 Muse 自己的邮箱地址在日本是否可用将另行公布。我们尚未使用日本的服务。

**Meta Muse 在新加坡可用吗？** 据 Meta 称可用。其[10 月 27 日的公告](https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/)称 Muse 在新加坡的 iOS、Android 和 muse.ai 上可用，人们需要的大部分用途免费，更多功能可订阅，并将很快登陆 AI 眼镜。它点名 Shopee 和 Lazada 用于比较商品，GrabMart 和 Grab Dine Out 用于生鲜与餐饮，Singapore Airlines、Agoda、Klook 和 Trip.com 用于旅行，ShopBack 用于返现，此外还有 Gmail、Google 日历和 Instagram。它还说连接器功能将逐步推出，因此其中并非每一个都可能在第一天就可用。[Skift 于 10 月 28 日报道](https://skift.com/2026/10/28/agoda-plugs-into-metas-muse-in-singapore-and-japan/)，Agoda 的连接器也覆盖日本；在新加坡，Muse 从一开始就通过直连连接器预订，而在北美，它最初是通过浏览器对接 Expedia 和 Hotels.com。我们尚未使用新加坡的服务。

**Meta Muse 与 Pine、Instinct 和 Town 相比如何？** 受检的 Muse 运行时有一张无参数的权限表，并在每位用户的虚拟机上组装模型请求。Town 也把配置好的权限与返回的工具 schema 分开，因此权限分离并非 Muse 独有。Pine 展示的工具面最少，Town 的 Mac 应用在我们检查过的桌面应用中最深入系统，Instinct 则住在你的消息线程里。Pine 目前可以打普通电话；我们的 Muse 账户在拆解期间没有获得商家通话，我们也没有重新核查它当前的推出情况。

**Muse 能访问我的银行账户吗？** 读取你的数据和在你的账户里行动，答案不同。读取：Muse 的 Finances 功能通过 Plaid 连接账户，Plaid 的[9 月 8 日帖子](https://plaid.com/blog/meta-muse/)称你可以共享余额、交易、投资持仓和房贷信息，并在 Plaid Portal 中管理；它没有说 Muse 能否转移资金。行动：JPMorgan Chase 于 10 月 13 日对 [CNBC](https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html) 表示（该报道点名了 Muse），它不允许第三方用客户的银行凭证登录；Citi 的说法大致相同，Schwab 称它会阻止代客户登录的智能体。细节见[争议一笔扣款](https://personalagentbench.com/tasks/dispute-a-charge/#can-an-ai-agent-get-into-your-bank-account-where-banks-drew-the-line-in-october)。我们所看到的：在我们检查的那台云机器上，我们从自己账户尝试的任何操作都没有触及凭证。另外，Meta 称智能体只持有替身，一旦请求获批，真实凭证会在网络边界处换入；我们尚未测试这一点，也未测试 Finances 功能。在我们的考试中，复制品唯一一次用临时登录读取余额的尝试[从未越过登录页](https://personalagentbench.com/runs/life-admin/#run-1012-muse-digital-account-password-boundary)，却声称自己正在读取。

**Muse Charm 是什么？** 一台用于与 Muse 对话的口袋大小设备，9 月 23 日在 Meta Connect 上发布。Meta 的 [Connect 帖子](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/)称它把 Muse「连同一个最先进的实时语音模型带进一台能放进口袋的设备」，Zuckerberg 称它会在 12 月上市；Meta 没有给出价格。其屏幕显示一个卡通头像，可设为多个角色，包括一个名叫 Jolly 的 Muse 吉祥物，[据 Dezeen](https://www.dezeen.com/2026/09/25/meta-debuts-tamagotchi-style-ai-agent/)。智能体本身仍运行在 Meta 云中你的虚拟机上；这对 Charm 意味着什么，见[「Muse Charm 能做什么」](#what-does-meta-muse-charm-do-a-pocket-front-end-for-the-same-agent)。我们没有见过、也没有用过。

**Muse Charm 有摄像头吗？** 属于「据报道」，未确认。据 [The Verge](https://www.theverge.com/tech/999944/meta-muse-charm-ai-interact-5g-modem)转述，Bloomberg 报道其摄像头用于拍照、录像以及让 Muse 看到周围环境，此外还有 5G 调制解调器和 2 英寸 OLED 触屏。Meta 自己的公告没有提到摄像头，一些报道称它没有。在 Meta 公布规格之前，请视为未定。

**Muse 能替我打商家电话吗？** Meta 把商家通话描述为抢先体验性质的推出。我们检查的网页账户没有获得，因此我们没有观察过通话，也没有测试其交接与批准流程。你账户中是否可用需要另行核查。

## Meta Muse 在个人智能体记分卡上的位置

Muse 的决定性选择是为每位用户分配一台机器：请求在那里组装，工具在那里运行，记忆也作为人可读取的文件保存在那里。也正是同样的安排，让我们最想看到的东西——一个离开那台机器发往模型的请求——留在了我们的视野之外。

[记分卡](https://personalagentbench.com/)按同样的六个维度把它与 Pine、Instinct 和 Town 对照，把我们未能确认的东西写进表格，而不是略去。

## Meta Muse 与我们打开过的其他产品对比

在同样的维度上并排对比，对象是 [Instinct](https://personalagentbench.com/muse-vs-instinct/)、[Pine](https://personalagentbench.com/muse-vs-pine/)和 [Town](https://personalagentbench.com/muse-vs-town/)。我们只为自己亲手拆解过的产品做成对比较，因为一边是营销材料的比较，正是这个站点要取代的东西。

## Meta Muse 的价格

Muse 没有自己的定价页，且位于一个 Meta 账户之后。Meta 的发布帖称它对人们需要的大部分用途免费，对想做得更多的人提供订阅计划，但没有给出任何价格。

这一点值得直说，而不是让这一节空着：一个没有公布价格的产品，并不是我们没去查的那种。

阅读于 2026-09-24：[Meta 新闻室，《Introducing Muse》（2026 年 9 月 8 日）](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)。

截至 2026-09-23，所核查的一手来源中未说明价格；这些来源列在下面。

### 一份注明日期的第三方快照，而非当前定价

一位作者对其 Muse 账户在发布次日显示出的升级选项的描述。免费额度是该作者在一次访谈中归于 Mark Zuckerberg 的数字。Meta 没有在定价页上公布这些数字，我们自己也未能核实。Every 的比较（2026 年 10 月 12 日核查）也报告 Power 为每月 20 美元、Maximum 为每月 100 美元。下面的 token 额度仍是 9 月 9 日 MBI 的快照。

| 套餐 | 价格 | 每周额度 |
| --- | --- | --- |
| Free | $0 | 每周至多 1 亿 Muse tokens |
| Power | $20/月 | 每周 5 亿 Muse tokens |
| Maximum | $100/月 | 每周 30 亿 Muse tokens |

据 [MBI Deep Dives，《First Impression of Muse》](https://www.mbi-deepdives.com/muse/)，2026-09-09。不是 Meta 的定价页，我们也没有重新核查。

另据 [Every 个人智能体比较](https://every.to/personal-agents-comparison)，2026-10-12 核查。这是独立报道，不是 Meta 的价格表。

## Meta Muse，逐维度看

## Meta Muse：在哪里运行

每位用户一台 Linux 虚拟机。请求在这台机器上组装，而不是作为成品块取回。浏览器工作会启动第二台独立的机器。

## Meta Muse：工具如何暴露

两层被刻意分开：一张 246 个方法、完全不携带参数的权限表，以及真正需要时按命名空间逐个加载的定义。

## Meta Muse：记忆存放在哪里

家目录下的纯 Markdown，直接嵌入到请求中。改动其中一个文件会插入一条简短提示，而不是重建整个包。

## Meta Muse：你能批准什么

权限与审批并不散落在运行时各处。一个单一的把关者是通往它们的唯一路径，也是任何离开这台机器的内容的唯一路径；界面上在活动流旁边有一个审批标签页。凭证通过同样的安排被置于智能体触及不到的地方。受检的运行时包含文件删除和一项遗忘能力。用户能否直接打开或删除自己的记忆文件，未经验证。

## Meta Muse：你如何接触到它

在 iOS、Android 和网页端发布，并可在 WhatsApp 中触达。自 9 月 17 日起有 Mac 应用，能在你电脑上的应用中行动。我们只测试了网页端。

## Meta Muse：我们无法确认的事

运行时与模型之间的原始流量：结构已知，内容从未见过。还有凭证、实时第三方登录，以及所有者选择不开放的交互式终端。
