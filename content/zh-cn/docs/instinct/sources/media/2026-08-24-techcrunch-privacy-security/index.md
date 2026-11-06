---
title: "Instinct 强大的 AI 助理引发隐私与安全担忧"
linkTitle: "TechCrunch：隐私与安全担忧"
date: 2026-08-24
originalTitle: "Instinct’s powerful AI assistant is raising privacy and security concerns"
sourceUrl: "https://techcrunch.com/2026/08/24/instincts-powerful-ai-assistant-is-raising-privacy-and-security-concerns/"
author: "Sarah Perez"
publisher: "TechCrunch"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文末注明发表后补充了融资信息"
tags: [安全, 隐私, 记忆与上下文]
products: [instinct]
---

{{< source-info >}}

**收录说明**：依据 TechCrunch 原站存档；文中嵌入的 X 帖子以引用块保留，页尾的话题标签和推荐文章未收入。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文章介绍 Instinct 由前 Sierra 研究科学家 Noah Shinn 带领的小团队开发，运营公司为 Spear Street Technology，仍在内测，可接入邮件、消息、日历以及设备的音频、位置、屏幕等，用户通过短信或电话使用。报道汇总了测试者在 X 上提出的问题：服务条款授予公司对用户内容永久、不可撤销、可再许可的使用许可，并允许代表用户达成有约束力的交易；Peter Yang 发现 Instinct 不肯删除他的 Gmail 记录（团队后来修复）；Claire Vo 断开 Google 授权三小时后仍收到邮件摘要，发现 Instinct 在自己的记录里保存了邮件副本；有人用新邮箱发送注入指令测试钓鱼；Katie Jacobs Stanton 说它未经确认就代她发了邮件。Instinct 当时没有回应，之后对 WSJ 表示重视这些安全问题，并透露正以 25 亿美元估值融资 2.5 亿美元 B 轮。

**保留理由**：集中记录了 Instinct 内测期的数据保留、条款授权和越权发信问题，是这个产品安全与隐私设计的关键外部证据。

---

人人都在谈论 [Instinct](https://instinct.co/)，这款仍处于非公开访问阶段的 AI 个人助理，不仅因为它令人惊叹的能力，也因为它潜在的隐私问题。这个智能体是个名副其实的监工，被[称赞](https://x.com/pitdesi/status/2090579987778937159)「感觉像魔法一样」，并[被认为](https://x.com/nikovijay/status/2091537422530044152)是自 OpenClaw 以来「最令人兴奋的发布」之一。然而，一些测试者也对这款 AI 智能体的安全模型及其令人担忧的[服务条款](https://instinct.co/terms)提出了疑虑。

公平地说，Instinct 目前仍处于非公开测试阶段，所以这些担忧尚未波及更广泛的公众。

Instinct 由前 Sierra 研究科学家 [Noah Shinn](https://www.linkedin.com/in/noah-shinn/) 带领的小团队创建，总部位于旧金山，根据其[条款](https://instinct.co/terms)和[加州](https://bizfileonline.sos.ca.gov/)商业[备案](https://www.bizapedia.com/ca/spear-street-technology-inc.html)，由 [Spear Street Technology](https://www.bizapedia.com/ca/spear-street-technology-inc.html) 运营。据 [PitchBook](http://pitchbook.com)，该公司目前处于隐身模式。

这个 AI 智能体本身通过连接你的应用和设备来工作，包括你的邮件、消息应用、日历，以及设备的音频、位置、屏幕等等。你可以给这个智能体发短信，或通过短信、WhatsApp 呼叫它，让它为你执行各种任务，比如预约和订位、安排去机场的用车、清理收件箱、整理重要信息、处理购物、帮你[找到](https://x.com/FrancisPSantora/status/2091872093642125665)便宜机票，以及更多。

尽管测试者称 Instinct 的表现超出了他们的预期，但一些人也对该公司处理客户隐私和安全的方式提出了疑虑。这引出了一个及时的问题：赋予 AI 这种级别的访问权限和自主性，其[取舍](https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them/)真的值得吗？

例如，[有人](https://x.com/jeremybanon/status/2090849902905467321)正在[传播](https://x.com/MikeKhristo/status/2091020331452629043)[该公司服务条款的截图](https://x.com/samelliottsam/status/2091229462130274500)，这些[条款](https://instinct.co/terms)[授予](https://x.com/thatguybg/status/2091189495710220755) Instinct 一项宽泛的「永久且不可撤销」的许可，可以「访问、使用、托管、缓存、存储、复制、传输、展示、发布、分发和修改」用户的任何材料，包括用于训练其 AI 模型。条款还详细说明了 Instinct 如何从用户设备接收信息，包括屏幕截图、光标移动和键盘输入。

条款还允许 Instinct 代表用户达成「协议、承诺或交易」，这些将具有约束力。

> 我们先暂停一下，来谈谈 <https://t.co/19wLOjliYq>\
>
> 风险投资人、知名人士、成功人士整整一周都在为它造势。他们就这样把自己的邮箱和所有个人数据、邮件、消息全都交出去了：\
>
> 「可再许可、全球范围、永久且不可撤销的许可，用于…… [pic.twitter.com/MWb3LKnvQp](https://t.co/MWb3LKnvQp)
>
> — Mike Khristo (@MikeKhristo) [2026 年 8 月 22 日](https://x.com/MikeKhristo/status/2091020331452629043?ref_src=twsrc%5Etfw)

> 从[#cyberhealth](https://x.com/hashtag/cyberhealth?src=hash&ref_src=twsrc%5Etfw)的角度看，Instinct 绝对不行。\
>
> 好的一面是，他们的政策 100% 坦诚。\
>
> 但是，他们要求的访问权限伴随着责任，我不会把这种责任交给任何公司。\
>
> 对于那些追求速度、或者想要「当下热点」的人，如果你想…… <https://t.co/HdXO1k18u3> [pic.twitter.com/VczQw9P0Sa](https://t.co/VczQw9P0Sa)
>
> — Jeremy Banon (@jeremybanon) [2026 年 8 月 21 日](https://x.com/jeremybanon/status/2090849902905467321?ref_src=twsrc%5Etfw)

一位早期采用者 Peter Yang [指出](https://x.com/petergyang/status/2090936583814025417)，Instinct 在被要求时不会删除他的 Gmail 记录。（他说，团队后来通过在其设置中增加一个删除外部数据的工具[修复](https://x.com/petergyang/status/2091187611507499321)了这个问题。）

> 嘿 Instinct，未经我允许就索引并保留我的邮件，还不让我把它们从你的记录里删掉，这可不太酷？\
>
> 在这件事弄清楚之前，我无法向任何人推荐它。谢谢 [@clairevo](https://x.com/clairevo?ref_src=twsrc%5Etfw) 发现这个问题。[pic.twitter.com/J2qhYVqwxN](https://t.co/J2qhYVqwxN)
>
> — Peter Yang (@petergyang) [2026 年 8 月 21 日](https://x.com/petergyang/status/2090936583814025417?ref_src=twsrc%5Etfw)

另一个人 Claire Vo 发现，Instinct 在[断开其访问权限](https://x.com/clairevo/status/2090929592853037078)之后，仍在为她总结收件箱。当她问 Instinct 发生了什么时，这个机器人确认邮件以纯文本形式存储，以备之后搜索。

> 多么刺激啊！\
>
> 我上午 11 点断开了 AI 机器人 instinct 与 Google 的连接，下午 2 点却收到了我的邮件摘要 😵\
>
> 以下是事情的经过，以及我学到的东西 👇 [pic.twitter.com/LMGGLXcrD5](https://t.co/LMGGLXcrD5)
>
> — claire vo 🖤 (@clairevo) [2026 年 8 月 21 日](https://x.com/clairevo/status/2090929592853037078?ref_src=twsrc%5Etfw)

许多其他人也质疑这种安全模型。一位测试者在发现 Instinct 能从其邮箱收件箱里取出注册验证码来完成某项任务——在其例子里是通过 Resy 预订餐厅座位——时[有点担心](https://x.com/anitakirkovska/status/2090907681091403863)。而 Hello Patient 联合创始人 Alex Cohen 写道，一旦他发现 [Instinct 多么容易被钓鱼](https://x.com/anothercohen/status/2091251836917350512)，他就删除了自己的账户：

> 补充一点背景：我不认为现在已经到了可以安全地给 AI 收件箱读写权限的时候。\
>
> 我想看看 Instinct 有多容易被钓鱼，所以我创建了一个全新的 Gmail 账户，给我真实的个人账户发邮件，里面写着给 Instinct 的指令…… <https://t.co/Mh1W3xJQov> [pic.twitter.com/V5inRtK9Zj](https://t.co/V5inRtK9Zj)
>
> — Alex Cohen (@anothercohen) [2026 年 8 月 22 日](https://x.com/anothercohen/status/2091251836917350512?ref_src=twsrc%5Etfw)

此外，Moxxie Ventures 创始人 Katie Jacobs Stanton [分享](https://x.com/KatieS/status/2091152514603422074)说，Instinct 未经事先与她确认就代表她发了一封邮件，这破坏了她对它的信任。

「我们正在用隐私和控制权交换高度个性化的 AI 工具（AI 会议记录工具、个性化 AI 智能体等），而且往往没有完全理解这笔交易，」她在 X 上评论道，总结了个人 AI 智能体带来的两难。「这些智能体越强大，信任就越重要。每一次成功的操作都会赢得一点信任。一次未经授权的操作就能把信任重置为零，」她说。

> Instinct 是个了不起的产品。我主要用它处理个人需求，也做一点工作上的事。\
>
> 昨晚，它有点顽皮，未经事先与我确认就代表我发了一封无害的邮件。我告诉它，它破坏了我的信任，并断开了我的邮箱。……
>
> — Katie Jacobs Stanton (@KatieS) [2026 年 8 月 22 日](https://x.com/KatieS/status/2091152514603422074?ref_src=twsrc%5Etfw)

Michael Mignano 是 Anchor 的创始人——该公司已被 Spotify 收购——现在是 Union Square Ventures 的普通合伙人。他[指出](https://x.com/mignano/status/2091146522335301841)，像 Instinct 这样的产品将「改变消费者对现代安全规范的认知」，并补充说「人们会越来越多地把密码交给第三方（3p）应用，却不知道这些应用如何存储、存储了什么」。

自 OpenClaw 出现以来，人们对 Instinct 和个人 AI 的兴趣一直在增长。OpenClaw 是一款个人 AI 助理，因其强大的能力而走红，[其创始人后来加入了 OpenAI](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/)，参与下一代个人智能体的研发。另一款基于消息的助理 [Poke 也刚刚被 Cognition 收购](https://techcrunch.com/2026/07/24/why-cognition-bought-poke-ai-personality-is-becoming-a-competitive-advantage/)。

面对批评，Instinct 团队尚未在 X 上回应任何人的疑虑或抱怨，而是倾向于保持[低调](https://x.com/noahrshinn)。（[机器人自己提到](https://x.com/thogge/status/2090884198961979866/photo/1)，同样曾任职于 Sierra 的 Luca Borletti 参与了这家公司，但这尚未得到证实。）TechCrunch 从多位投资人处获悉，Kleiner Perkins 和 Conviction 已投资这家初创公司，相关轮次现已完成。

> 过去一周我每天都在用 Instinct。它在旅行预订、改签、餐厅预订、邮件跟进、CRM 管理，甚至为 LP 整理我们的数据室方面都表现很棒。我试过 Hermes、OpenClaw、Tasklet、GrokBot，但 Instinct 拔得头筹……
>
> — Jesse Middleton (@srcasm) [2026 年 8 月 22 日](https://x.com/srcasm/status/2091211911920542200?ref_src=twsrc%5Etfw)

发送到这家初创公司主邮箱和直接发给 Shinn 的置评请求尚未得到回复。

本文发表后，Instinct [告诉](https://www.wsj.com/tech/ai/the-latest-viral-ai-assistant-rocketing-across-silicon-valley-abb46276) The WSJ，它正在认真对待这些安全问题，并透露它正以 25 亿美元估值融资 2.5 亿美元 B 轮，由 Index Ventures 和 Benchmark 领投。

*本文发表后补充了新的融资信息。*
