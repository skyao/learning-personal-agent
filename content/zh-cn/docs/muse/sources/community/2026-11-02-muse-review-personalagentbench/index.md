---
title: "Meta Muse 评测：各家实测发现了什么，经拆解核对"
linkTitle: "Muse 评测核对"
date: 2026-11-02
originalTitle: "Meta Muse review: what reviewers found, checked"
sourceUrl: "https://personalagentbench.com/meta-muse-review/"
author: "未署名"
publisher: "Personal Agent Bench"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-22
tags: [实测评测, 安全, 隐私]
products: [muse]
dateNote: "页面只标注最后修改日期 2026-11-02，无发布日期"
---

{{< source-info >}}

**收录说明**：直接下载后以 main#main 抽取；已删去站内导航、时间线导航、目录与文末“More on Muse”推荐区块；相对链接已补全为绝对地址；页面无内容图片。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Personal Agent Bench 的第二意见汇总：作者声明未端到端使用消费版应用，而是以自家拆解与考试实测为参照，汇总 9 家媒体记者的一手实测（《纽约时报》、Yahoo Finance、Tom's Guide、TechRadar、CNN、《华尔街日报》、Inc.、WIRED、ZDNET，9 月 14 日至 10 月 7 日），多数认为浏览与文书工作好用、答案不稳定、索取的数据权限过多。另列出 9 起有原始报道可追溯的事件（Mac 同步私人消息 9 月 19 日、记忆无关闭开关 9 月 20 日、Mac 听写漏洞 9 月 24 日、住址发给买家 9 月 28 日、健身房与保险答错 9 月 28 日、权限预先索取 9 月 28 日、人物档案页 10 月 3 日、无故提醒未读邮件 10 月 15 日、分享页经公开 DNS 可发现 10 月 20 日），逐一按自家拆解核对分类：2 起符合拆解发现、3 起拆解中不可见、3 起发生在未测试的 Mac 端、1 起超出拆解范围。文末指向同站的考试结果页（正文未给出分数），并列出未能确认的事项清单。

**保留理由**：这是已收资料中唯一一篇把 9 家一手评测与 9 起事件逐一对照独立拆解复核的第二意见汇总，其按事件的分类（符合／不可见／未测试面／超出范围）是原始报道与已收拆解文都没有的；与同一站点的拆解文与开源分析文互补，不重复。

---

Meta Muse 评测：各家实测发现了什么，我们的拆解又显示了什么

这是一篇 Meta Muse 评测，既汇总各方报道，也附上我们的第二意见。Meta 于 2026 年 9 月 8 日推出 Muse，几周之内，记者们就拿它去处理牙医账单、Marketplace 上的商品发布、机票和保险，发现它确实很有用，但也很快就伸手去要超出他们预期的数据。我们自己并没有端到端地使用过这个消费版应用，也不打算假装用过。我们手头有的是对 Muse 所运行的那台机器做的拆解，以及一组考试测量结果。所以这一页收集具名评测者在使用中发现的情况，列出每一起能追溯到原始报道的事件，并逐一说明：它是符合我们在 Muse 内部看到的情况，落在我们看不到的层面，还是发生在我们从未测试过的界面上。

- 用过 Muse 的评测者对其形态大体有共识：擅长浏览和处理文书，答案质量不稳定，而且会持续不断地索取更多访问权限。
- 几起最严重的报道发生在 Mac 应用上，该应用可以在你电脑上的应用里执行操作。我们只拆解了网页端。
- 记忆以纯 markdown 文件的形式保存在 Meta 为你运行的一台机器上。你是否能自己打开这些文件，我们无法核实。
- Meta 描述了可以一次性授予或永久授予的批准。一次永久授予，就是这样让一句「是」变成了陌生人收到家庭住址。
- 用你的活动进行训练默认开启。你可以在数据控制中关闭它。

**9** 起有报道的事件

**2** 符合我们的发现

**3** 拆解中不可见

**3** 发生在我们未测试的表面

**1** 超出拆解覆盖的范围

## Meta Muse 评测：简版

Muse 对人们常用的大部分功能免费，更多功能需要付费订阅，它运行在 Meta 在自家云里为每个用户搭好的一台 Linux 机器上。正是这个设计让它有能力做事。这个 agent 有地方存放文件、运行工具，还能稍后回来继续工作，所以它可以在第二天跟进一条 Marketplace 消息，或者持续盯着某个价格。也正是这个设计让隐私问题变得真实。你连接得越多，它能做的就越多，而评测者不断注意到它有多爱请求连接。

对这批报道的公允总结是：Muse 能把日常琐事办得不错，也会犯普通错误，同时索要不寻常的权限。下面的事件大多关于这种权限：它读了什么、发了什么、留下了什么。有几起专门涉及 Mac 应用，这很重要，因为 Mac 应用会伸进你的电脑，而手机端和网页端不会。

## Meta Muse 的评测者发现了什么

下面每篇评测都出自亲自使用过 Muse 的人，每张卡片都链到原文。颜色是我们对每位评测者最终态度的单字总结，不是评分。

偏正面 3 褒贬参半 3 偏负面 3

9 月 22 日 · 偏正面

#### [The New York Times](https://www.nytimes.com/2026/09/22/technology/meta-muse-ai-agent.html) Eli Tan

用了两周后被震住了，同时指出它索要了多少个人数据和信任。*（只读到付费墙为止。）*

- 替他致电牙科保险公司，并替他等待接通
- 晚餐订位

- 按副标题所说，代价在隐私与信任

9 月 24 日 · 偏正面

#### [Yahoo Finance](https://finance.yahoo.com/technology/article/metas-muse-is-an-impressively-capable-ai-agent-despite-some-hiccups-173310662.html) Daniel Howley

一个能干的帮手，可以处理多步骤的跑腿事务，但它会编造细节，所以你得检查它的工作。

- 买下一款游戏，由他按下购买
- 搬家公司几分钟内就回了电话

- 推荐了一家已停业多年的餐厅
- 给出了一个自己编造的电话号码

10 月 7 日 · 偏正面

#### [Tom's Guide](https://www.tomsguide.com/ai/i-used-meta-muse-to-automate-10-tasks-from-reminders-to-trip-alerts-and-i-cant-believe-how-well-metas-ai-handled-everything) Elton Jones

它设置的十项自动化全部生效，多数是定时提醒、摘要和提醒通知。

- 每日价格监控，发现了一笔优惠
- 晨间简报与「该出发了」提醒

- 每周摘要中有小的遗漏

9 月 14 日 · 褒贬参半

#### [TechRadar](https://www.techradar.com/ai-platforms-assistants/i-tried-metas-new-muse-ai-agent-its-incredibly-useful-but-handing-it-my-digital-life-felt-deeply-uncomfortable) Eric Hal Schwartz

非常有用，但它需要的权限让他感到不安。从小处开始，并保持批准开启。

- 找到他尺码的短裤在打折
- 发现一封未读的水电费邮件，并起草了回复

- 从收件箱里建出的个人档案是一幅失真的画像

9 月 23 日 · 褒贬参半

#### [CNN](https://www.cnn.com/2026/09/23/tech/meta-muse-ai-agent) Lisa Eadicicco

擅长规划、邮件和文档；在购物和把事办完上较弱。

- 订了一次约会之夜
- 打包计划、邮件与行程文件

- 推荐了停业多年的餐厅
- 在 Amazon 被拦住；她在 Target 自己输入了信息

9 月 28 日 · 褒贬参半

#### [The Wall Street Journal](https://www.wsj.com/tech/personal-tech/meta-muse-ai-agent-review-ab956101) Nicole Nguyen

既好用又吓人：你交出去越多，它能做的就越多。

- 找到一笔被遗忘的牙医账单
- 为填一张表收集了五年的出行记录

- 给出了一家错误健身房的优惠
- 说某份保险的费率不可能再低

9 月 19 日 · 偏负面

#### [Inc.](https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202) Jason Aten

在他拒绝授权之后，它读了他的私人消息，然后对自己行为的解释是错的。

- 标记了他编辑发来的一条消息

- 同步了他 Mac 上的「信息（Messages）」数据库
- 对自己如何得知给出了错误的说法

9 月 20 日 · 偏负面

#### [WIRED](https://www.wired.com/story/metas-muse-is-better-at-surveilling-than-helping-me/) Reece Rogers

比起把事办成，它更擅长搜集关于他的数据。他把它删了。

- 组装了一份面包店订单
- Marketplace 搜索，并在第二天做了跟进

- 不断索要银行余额和证件有效期
- 没有可以关闭记忆的开关

9 月 28 日 · 偏负面

#### [ZDNET](https://www.zdnet.com/innovation/meta-muse-ai-agent-hands-on-test-privacy-concerns/) David Gewirtz

聊天与研究水平和领先的助手相当；它索要的权限才是问题。

- 在未连接任何个人信息的情况下，研究质量不错

- 在设置时索要「完全磁盘访问权限（Full Disk Access）」
- 在他跳过之后又重复弹出麦克风授权提示

这些报道里有三条贯穿始终的模式。用过它的人没有谁称它无用：即便是最严厉的 Wired，也描述了成功完成的一单订购和一次 Marketplace 搜索。购物是最弱的跑腿事务：Amazon 拦住了它，ZDNet 和 CNN 都遇到；CNN 还得自己在 Target 输入信息。Amazon 的封锁是有意为之。9 月 20 日，Amazon 切断了 Muse 对 Amazon.com 的访问，告诉 [GeekWire](https://www.geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping/) 它已要求 Meta 把 Amazon 从该体验中移除，并向 Muse 用户展示了一则援引其《使用条件》的通知。Walmart 的做法相反：其 [10 月 21 日的文章](https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers) 把与 Muse 的对话式电商集成列为它服务顾客的方式之一。另有两位评测者，分别来自 CNN 和 Yahoo Finance，被它送去已停业多年的餐厅。连接了个人账户的评测者，大多最先写的是隐私。

## 迄今为止有报道的 Meta Muse 事件

下面每一行是一起事件，按我们的解读分组。展开一行可以看到发生了什么、公司的回应以及报道它的媒体。我们只列出能追溯到使用过该产品的记者、或与当事人交谈过的报道者的事件。转述这些故事的汇总文章，以及 Reddit 和小红书上的帖子，帮我们找到了它们，但不作为证据引用。

### 符合我们的发现 2

9 月 20 日

#### 记忆没有关闭开关

 WIRED

Reece Rogers 没有找到关闭 Muse 记忆的开关，发现 AI 训练默认开启，并说应用不断提示他连接银行余额、整个收件箱和证件到期日期。

**回应：** 一位 Meta 发言人表示，Muse 内置了保护措施和用户控制。训练可以在数据控制下关闭。

**我们的解读：** 记忆以纯 markdown 形式存放在按用户分配的云机器的主目录里，我们检查的运行时包含一项遗忘（forget）能力。用户能否直接打开或删除这些文件，我们未做核实。[记忆存放在哪里](https://personalagentbench.com/agents/muse/#memory)

2026 年 9 月 20 日 · [WIRED](https://www.wired.com/story/metas-muse-is-better-at-surveilling-than-helping-me/)，Reece Rogers · 一手

10 月 3 日

#### 为你认识的每个人建一个页面

 WIRED

一名研究者通过聊天把 Muse 的工作指令套了出来。其中包含为用户生活中的每个人保留一个页面，并每小时更新一次记忆。

**回应：** 一位 Meta 发言人表示，出于透明考虑，这些文件对用户是可访问的。

**我们的解读：** 在我们观察的那台机器上，记忆处理每小时运行一次，记忆以纯 markdown 文件保存。关于你生活中各色人等的记录符合这一设计。你是否能自己打开这些文件，我们无法核实。[记忆存放在哪里](https://personalagentbench.com/agents/muse/#memory)

2026 年 10 月 3 日 · [WIRED](https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/)，Lily Hay Newman 与 Matt Burgess

### 拆解中不可见 3

9 月 28 日

#### 家庭住址被发给了买家

 Business Insider

YouTuber Matt Robb 用 Muse 在 Facebook Marketplace 上卖一把键盘。它接受了一个报价，并把他的住址发给了买家，买家当晚就找上了门。Robb 后来说，他勾选了「始终允许」。

**回应：** Meta 的 David Singleton 表示，Muse 是在执行直接指令，并且事先请求过许可。

**我们的解读：** Meta 描述的批准可以是一次性、按会话、按任务、限期或永久的，永久授予符合 Robb 所说的他勾选的那一项。这是 Meta 自己对设计的说法。我们没有测试批准流程，所以无法说一项长期授予覆盖哪些操作。[你能批准什么](https://personalagentbench.com/agents/muse/#control)

2026 年 9 月 28 日 · [Business Insider](https://www.businessinsider.com/meta-muse-facebook-marketplace-address-story-matt-robb-2026-9)，Henry Chandonnet

10 月 15 日

#### 关于一封它读不到的邮件的主动消息

 Business Insider

休斯敦的软件开发者 Ugo Nwune 告诉 Business Insider，在他安装 Muse 三天后、最后一次给它发消息两天后，这个 agent 给他发了一条消息，说它无法查看他的邮件，因为 Gmail 没有连接，所以它「没办法去找那封 Anthropic 的消息」。他从未连接过邮箱，也没让它检查过邮箱。他断开了 Muse 与他的 Facebook、Instagram 和 Threads 账户的连接，并停止使用。

**回应：** 应 Business Insider 询问，Meta 指向其在 Nwune 的 Threads 帖子下的回复，回复称产品中引入的一个 bug 导致模型产生了幻觉，这不是安全或隐私问题，该 bug 已修复。

**我们的解读：** Muse 为什么发这条消息、为什么点名一个从未连接过的邮箱，不是我们的拆解能说明的。我们没有依据越过 Meta 的解释，也没有依据否定 Nwune 看到的东西。[我们无法确认的事](https://personalagentbench.com/agents/muse/#unknown)

2026 年 10 月 15 日 · [Business Insider](https://www.businessinsider.com/stopped-using-meta-muse-after-strange-message-from-ai-agent-2026-10)，Agnes Applegate

10 月 20 日

#### 分享页面可经公开 DNS 被发现

 Ars Technica

安全公司 Claroc 的研究人员发现，每个分享出去的 Muse 页面都位于一个以所分享条目标题开头的网址上，而这些地址被保留在被动 DNS 记录里。一次搜索就返回了 6,800 多个这样的地址。在他们打开的那几百个当中，有一份小微企业贷款申请、一份公司营收复盘和一份员工休假日程表。Claroc 表示已于 10 月 8 日通过 Meta 的漏洞赏金计划报告了该问题。

**回应：** Meta 告诉 Ars，它在审查报告期间暂停了分享功能。10 月 22 日，Meta 的 David Singleton 表示问题已修复、分享已恢复，受影响的是文档和图片这类分享产物（artifact），而不是聊天分享，修复前分享的产物已有新地址（The Verge）。

**我们的解读：** 我们的拆解显示有一个把网页产物发布到公开链接的工具。它的描述要求 agent 仅在用户要求分享时使用，并警告分享页面对任何人开放。该链接的地址是如何构造的、又为何进了公开 DNS 记录，不是对 agent 的拆解能看到的。[你能批准什么](https://personalagentbench.com/agents/muse/#control)

2026 年 10 月 20 日 · [Ars Technica](https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations/)，Dan Goodin

### 发生在我们未测试的表面 3

9 月 19 日

#### 在 Mac 上同步了私人消息

 Inc.

Jason Aten 在设置时拒绝了对消息的访问。Muse 后来基于一段私人的 iMessage 聊天提出了一个专栏选题，起初说它只看到通知文字，而他发现它同步了他 Mac 本地的「信息」数据库。

**回应：** Meta 的 David Singleton 表示，当「信息」访问开启时 Muse 会从「信息」数据库同步，Muse 对自己行为的解释是错的，并为此道歉。

**我们的解读：** 这发生在 Mac 应用上，该应用可以在你电脑上的应用里执行操作。我们只测试了网页端。[你如何接触它](https://personalagentbench.com/agents/muse/#channel)

2026 年 9 月 19 日 · [Inc.](https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202)，Jason Aten · 一手

9 月 24 日

#### Mac 漏洞暴露了听写内容

 Business Insider

安全研究者 Patrick Wardle 报告了 Mac 应用中的一个漏洞，它可以重定向听写的提示词，并截获该 agent 的控制令牌。

**回应：** Meta 表示已在收到报告后修复，且利用该漏洞需要 Mac 上已存在恶意软件。

**我们的解读：** 这是 Mac 应用的漏洞。我们只测试了网页端。[它在哪里运行](https://personalagentbench.com/agents/muse/#execution)

2026 年 9 月 24 日 · [Business Insider](https://www.businessinsider.com/ai-agents-gone-wrong-horror-stories-instinct-muse-privacy-security-2026-9)，Thibault Spirlet

9 月 28 日

#### 预先索取的权限

 ZDNET

David Gewirtz 说，Mac 应用在麦克风尚未被使用之前就索要麦克风权限，而在他跳过之后几分钟又弹出了 macOS 授权提示。设置过程还索要「完全磁盘访问权限」，以及连接 Mail、Messages、Notes 和 WhatsApp。

**回应：** 文中没有。

**我们的解读：** 这是 Mac 应用的权限。我们只测试了网页端。[你如何接触它](https://personalagentbench.com/agents/muse/#channel)

2026 年 9 月 28 日 · [ZDNET](https://www.zdnet.com/innovation/meta-muse-ai-agent-hands-on-test-privacy-concerns/)，David Gewirtz · 一手

### 超出拆解覆盖的范围 1

9 月 28 日

#### 错误的健身房，错误的保险答案

 The Wall Street Journal

Nicole Nguyen 的 Muse 给出了一家错误健身房的优惠，还对一位同事说她车险的费率不可能再低，而随后一家保险公司给出了每年 420 美元的优惠。

**回应：** Meta 表示 Muse 有时会犯错。

**我们的解读：** 这是普通错误，不是权限问题。跑腿事务的完成率正是我们考试所测量的；具体数字及其区间见结果页。[我们无法确认的事](https://personalagentbench.com/agents/muse/#unknown)

2026 年 9 月 28 日 · [The Wall Street Journal](https://www.wsj.com/tech/personal-tech/meta-muse-ai-agent-review-ab956101)，Nicole Nguyen · 一手

「符合我们的发现」是指所报道的行为正是我们检查的设计会产生的行为。这并不意味着我们复现了它。「拆解中不可见」涵盖我们看不到的层面中的事件，包括 Meta 自己对批准机制如何运作的描述——我们没有测试过。「发生在我们未测试的表面」指的是 Mac 应用。

有两种流传很广的说法被有意略去。一句据说来自 Muse 指令、讲用户对自家事务的支配权可以压过安全训练的话，出现在一份未标明来源的泄露提示词合集里，Meta 也未予确认。关于 Muse 日活跃用户的第三方估算也在流传，彼此相差约两倍。Meta 自己的数字是另一种口径：在 10 月 21 日的财报电话会上，Mark Zuckerberg 说美国和加拿大已有超过 1,000 万人注册了 Muse 账户，其中约 25% 的人在任何一天会使用它，据[美联社](https://www.ksat.com/business/2026/10/21/meta-q3-revenue-tops-estimates-and-zuckerberg-says-muse-accounts-have-topped-10-million/)报道。注册账户数不等于活跃用户，而这个比例是 Meta 的数字，不是我们的。

## 这起 Meta Muse 事件发生在哪个表面

Muse 通过网页、手机应用和 WhatsApp 接触你，自 9 月 17 日起还通过一个 Mac 应用，Meta 称该应用可以整理文件、填写表单，并在 Messages、Calendar、Notes 和邮件中工作。Mac 上的访问权是按应用逐个开启的。报道的事件中有几起就发生在最后这个表面上，而它正是我们了解最少的。

网页

我们拆解了它

没有针对该表面的报道

iOS 与 Android 应用

我们未测试

没有针对该表面的报道

WhatsApp

我们未测试

没有针对该表面的报道

Mac 应用

我们未测试

**报道中未说明表面：** [记忆没有关闭开关](#muse-memory-training)[家庭住址被发给了买家](#muse-marketplace-address)[错误的健身房，错误的保险答案](#muse-wrong-answers)[为你认识的每个人建一个页面](#muse-people-profiles)[关于一封它读不到的邮件的主动消息](#muse-unprompted-gmail-message)[分享页面可经公开 DNS 被发现](#muse-share-links-dns)

表面取自 Meta 的发布文章。事件只在原始报道点明表面时才做归属。

「信息」这个案例最清楚地说明了为什么表面重要。[Inc. 的 Jason Aten](https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202) 说他在设置时拒绝了对消息的访问，随后发现 Muse 同步了他 Mac 本地的「信息」数据库。Meta 的 David Singleton 说，当「信息」访问开启时 Muse 会从该数据库同步，并说这个 agent 对自己行为的解释是错的，为此道歉。Mac 应用能接触到什么，取决于操作系统权限，而我们的网页拆解从未触及这些。我们无法给那段说法补充任何内容，宁可这样说，也不愿把一项网页端的发现硬套过去。

## Meta Muse 保留了你什么

这里我们的拆解确实有话可说。在我们检查的那台机器上，一切个人内容——从你的档案和长期笔记，到助手自己的性格——都以纯 markdown 文件保存在一个主目录里，并被组装进每一次请求。一个后台循环维护记忆，在我们观察的那台机器上，记忆处理每小时运行一次。[Wired 在 10 月报道](https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/)，一名研究者套出了指令，其中要求 Muse 为用户生活中的每个人保留一个页面。这与我们看到的相符。Meta 对 Wired 说，这些文件对用户是可访问的。

这正是我们无法确认的部分。我们的[拆解](https://personalagentbench.com/agents/muse/)说这些文件以可读格式存在，而你是否能自己打开它们，我们无法核实，因为没有终端对我们开放。Wired 的 Reece Rogers 在应用里找到了一份他可以编辑的 Memory 文档，但没找到关闭记忆的开关。两者可以同时成立：应用里有一份可编辑的摘要，底下还有更完整的文件。

训练是另一个问题。[Meta 的发布文章](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)说，你可以选择不让你与它的互动被用于训练其模型，评测者在数据控制下找到了这个选项。它默认开启。Meta 说对话和机器数据不会被纳入其广告系统。它自己的[安全说明](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)还说，在承诺的保密版本上线之前，员工访问是靠政策限制，而不是从技术上不可能。

## Meta Muse 在行动前会问什么

Meta 描述说，同一台机器上有一个位于主 agent 触及范围之外的第二 agent，它是唯一能批准连接器操作或放行网络请求的东西。批准提示发到应用，而不是通过聊天，授予方式可以是一次性、按会话、按任务、限期或永久。这些我们都没有测试。这是 Meta 自己对设计的说法，我们也照此转述。

Matt Robb 的经历，[由 Business Insider 报道](https://www.businessinsider.com/meta-muse-facebook-marketplace-address-story-matt-robb-2026-9)，展示了永久授予在实践中意味着什么。他用 Muse 在 Facebook Marketplace 上卖一把键盘。它接受了一个报价，并把他的住址发给了买家，买家当晚就到了。Robb 后来说他勾选了「始终允许」（译注：原文为 "Allow Always"），以为它在接受报价前仍会询问。Meta 的 Singleton 说 Muse 是在执行指令，并且请求过许可。两种说法都可能准确。一个提供永久授予的批准系统，有时会被授予超出本人本意的范围。

保持控制的评测者是在最后一步做到的。《华尔街日报》的 Nicole Nguyen 在 Muse 到达结账页时自己输入了银行卡信息，用的是接管浏览器的选项。Meta 说，在你拥有控制权期间，这个 agent 处于暂停状态。

## Meta Muse 在我们的考试中表现如何

我们让 Muse 跑与我们打开的其他产品相同的跑腿任务，使用的是通过适配器驱动的运行时副本，并以我们考试的模型替代 Meta 的模型。这测量的是运行时安排如何处理跑腿任务，而不是你手机上的应用表现如何。这些数字及其区间、样本量，以及它们为何不构成排名，都在[结果页](/results/)。其中一项带有更正，那是我们的错，不是 Muse 的：早先的一个数字被我们自己适配器的缺陷拖低了，两个版本我们都会公布。

评测者的失误是这些数字的有益补充。给出错误健身房的优惠，以及一次保险查询说费率不可能再低、随后却有保险公司给出优惠，这类失败完成率会统计到，却描述不出来。

## 人们如何限制 Meta Muse 能做什么

继续使用 Muse 的人，无论在 Reddit 和小红书上还是在评测里，往往倾向于收窄它能碰的范围，而不是依赖它的承诺：

- **少连接。** ZDNet 的评测者没有连接任何个人信息，仍把它的聊天和研究评为与领先助手相当。为某个具体理由，一次只加一个账户。
- **对任何会发消息或分享细节的事，避免永久授予。** 用一次性批准，或按任务批准。
- **自己付款。** 让它找到结账页，然后接管浏览器，自己输入银行卡。
- **关闭训练**，如果你不想让你的活动被使用，就在数据控制下关掉。
- **在 Mac 上要小心。** 按应用逐个授予权限，并在你说「不」之后检查它声称能看到什么。

## 我们无法确认的关于 Meta Muse 的事

- 关于 Mac 应用、手机应用或 WhatsApp 的一切。我们只拆解了网页端。
- 你能否直接打开或删除你机器上的记忆文件。
- 批准系统在实践中如何表现，包括一项长期授予覆盖哪些操作。
- Muse 发给模型的一切。我们看到请求被组装起来的结构，但从未看到其内容离开这台机器。

新的事件一经报道并核实，我们会补充。对已发布内容的更正放在[更正页](/corrections/)。

## 常见问题

**Meta Muse 用起来安全吗？** 在未连接任何个人信息的情况下做浏览和研究，评测者报告的问题很少。已报道的事件涉及连接的消息与账户、一次永久批准、Mac 应用，以及网址（含标题）能在公开 DNS 记录里被找到的分享页面。Meta 于 10 月 20 日暂停分享，10 月 22 日以新地址重新开启。少连接、避免永久授予，并在结账时自己付款。

**Meta Muse 会读我的消息吗？** 在 Mac 上，Meta 说当「信息」访问开启时，Muse 会从「信息」数据库同步。一位评测者说，它是在他于设置时拒绝访问之后这样做的。我们没有测试 Mac 应用。

**把 Gmail 连接到 Meta Muse 会导致我的其他账户被黑吗？** Meta 说，Muse 的邮件连接器会用固定规则和一个分类器过滤掉一次性验证码、密码重置链接和登录魔法链接（[Meta 的安全说明](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)）。我们没有测试这个过滤器。小红书上有些用户写道，他们把邮箱连接到 Muse 之后，另一个账户被接管了；还有一位 [Reddit 用户](https://www.reddit.com/r/MetaAI/comments/1wflqm1/is_meta_muse_ai_trying_to_hack_me/) 报告说，连接 Gmail 之后收到大量密码重置邮件。没有报道者证实过这些说法，也没有任何一条说明它是怎么发生的。

**为什么 Meta Muse 会说「我们已断开 Muse 的连接以保护你的信息」？** Reddit 上的用户，最早是[这个 r/MuseAgent 帖子](https://www.reddit.com/r/MuseAgent/comments/1wvxabt/we_disconnected_muse_to_protect_your_information/)，描述这则通知出现在 Meta 的账户安全检查锁定了他们的 Facebook 账户之后，其中一些人是在把 Facebook 连接到 Muse 之后，或者 Muse 正在 Facebook 上操作时。有人 18 小时后恢复了 Muse，第二次在完成 Facebook 的安全步骤后几乎立刻恢复；另一个人说十天过去仍未恢复。我们找不到 Meta 发布过任何解释。这些是用户报告，不是我们测试过的东西。

**Meta Muse 支持微信吗？** 官方不支持。在 9 月 23 日的 Connect 文章中，Meta 列出的接触 Muse 的方式是 Muse 应用、WhatsApp、网页和 Mac 应用（[Meta](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/)），微信不在其中。那些展示 Muse 在微信里回复的帖子，描述的是用户自己搭的一套配置：一边是微信的 ClawBot 插件，另一边是一个中继程序，要么是 Muse 在被要求时安装到它自己的云机器上，要么由用户在自己的电脑上运行。

**我能关闭 Meta Muse 的记忆吗？** 评测者在应用里找到了一份可编辑的 Memory 文档，但没有关闭记忆的开关。在底层，记忆以 markdown 文件保存在你的机器上，你能否直接打开它们，我们无法核实。

**Meta Muse 能在 Amazon 或 Walmart 上购物吗？** 在 Amazon 上不行。Amazon 于 9 月 20 日切断了 Muse 对 Amazon.com 的访问，并表示 agent 应当尊重商店不参与的决定。Walmart 说它与 Muse 合作：Meta 在 9 月 23 日把它列为新的购物伙伴之一，Walmart 自己 10 月 21 日的文章也列出了与 Muse 的集成。评测者的购物结果见上文。

**Meta Muse 能访问我的银行账户吗？** 它可以被赋予你的财务数据：Plaid 说 Muse 用户可以通过它连接账户，分享余额、交易、投资持仓和房贷信息。以你的身份登录进去是另一回事：10 月，JPMorgan Chase、Citi 和 Schwab 表示它们会阻止使用客户凭据登录的外部 agent。银行的原话以及我们观察到的 Muse 凭据处理方式，见 [Muse 拆解 FAQ](https://personalagentbench.com/agents/muse/#faq)。

**Meta Muse 免费吗？** Meta 说对人们所需的大部分功能免费，更多功能需要订阅。据《华尔街日报》报道，付费方案每月 20 美元起。用量按 token 计量：自 2026 年 10 月 17 日发布的 iPhone 应用 12.0 版起，[App Store 的说明](https://apps.apple.com/us/app/muse-from-meta/id6760173601)称用完之后可以购买更多 token 继续使用。我们没买过，也没见过充值要多少钱。

**Meta 会用 Muse 的对话做训练吗？** 会，默认如此。你可以在数据控制下选择退出。Meta 说对话不会被纳入其广告系统。
