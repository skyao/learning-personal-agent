---
title: "你的账本正在训练 Meta 的模型，退出开关藏在三层之下"
linkTitle: "账本训练模型与三层退出开关"
date: 2026-10-19
originalTitle: "Your Books Are Training Meta's Models. The Opt-Out Is Three Taps Deep."
sourceUrl: "https://aihomebuilding.com/stories/muse-small-business-data-trains-models-default-2026"
author: "Catherine Chen"
publisher: "AIHomeBuilding"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-22
tags: [隐私, 安全, 连接器, 商业与规模]
products: [muse]
---

{{< source-info >}}

## 收录说明

本页收录的文章于 2026-10-19 发布在 AIHomeBuilding。直接下载后以 article.article-body 抽取全文，未做删改。头图为装饰图，未收。原文全文存于本目录的 original.md，网站上不显示，已翻译。

作者限定：未能独立核实 Meta 的脱敏流程，也无法确认“某些类别”除四类之外还覆盖什么；QuickBooks 与 Stripe 连接器请求的 OAuth 范围未见公布；未在真实应用中测试数据控制开关；订阅定价引自一家媒体，未经 Meta 确认。

## 内容摘要

文章以小店主 Tom Mulholland（每周工作 65 小时，Meta 9 月 29 日小企业发布会的代言人）开篇，指出 Muse for Small Business 在 9 月 8 日发布的个人智能体上新增 15 个第三方连接器：Asana、Box、Canva、Dropbox、Figma、Granola、HighLevel、Intuit QuickBooks、Klaviyo、Lovable、Notion、Shopify、Slack、Stripe、Zoom。关键在 9 月 17 日生效的《Muse 隐私政策》：训练开关“首次使用 Muse 时即开启”，关闭需三步；政策原文称与 Muse 的互动可包含来自连接器的信息，同一开关控制这些信息能否用于改进 Meta 的 AI。Meta 列出的清除类别为姓名、邮箱、电话与社保号等四类，作者对照 QuickBooks 实际携带的数据（客户购买历史、营收与毛利、供应商银行路由与账号、员工薪资金额、客户地址）指出，毛利、供应商银行账户、客户购买频次均不在清除之列。政策明确写明开关变更“亦适用于此前的互动”，但未承诺已训练进模型权重的数据可被抽出；连接 QuickBooks 的是店主，未点击任何东西的是其客户、员工与供应商。

## 保留理由

这是唯一一篇逐句精读隐私政策原文并对照 QuickBooks 实际数据字段做缺口分析的文章；“训练开关默认开启、9 月 17 日生效、清除清单仅四类、变更追溯既往互动但不承诺从已训模型中抽出”四点是已收资料里没有的政策细节。

---

Tom Mulholland 每周在他的杂货店工作六十五小时，而 Meta 选他作为其小企业宣传的门面：「有太多事情，只有我能做，」他在[9 月 29 日的发布公告](https://www.techceodaily.com/ai/meta-muse-for-small-business-ai-agent)中说。Meta 的提议很简单。把 Muse 连接到 QuickBooks、Stripe、Shopify、Klaviyo 和 Slack，让智能体读账本、标记异常支出、起草广告。发布时没人提到十二天前生效的第二份文件。

Muse for Small Business 为 Meta 9 月 8 日推出的个人智能体新增了十五个第三方连接器：Asana、Box、Canva、Dropbox、Figma、Granola、HighLevel、Intuit QuickBooks、Klaviyo、Lovable、Notion、Shopify、Slack、Stripe 和 Zoom，以及 Facebook 公共主页、Instagram 专业账户分析和 Meta 广告账户，[Reuters 报道](https://kwsn.com/2026/09/29/meta-expands-muse-ai-agent-for-small-businesses/)。Meta 建议的提示词直白地讲述了故事：分析一年的销售和广告活动并写一份增长计划；审阅本月的账本，找出看起来不对的支出。没有所有者的批准，什么都不会发布、发送或花钱，这是每家媒体都重复的保障，[以及 Meta 从未确认的定价](https://ecommerceparadise.com/meta-muse-small-business/)。

自 9 月 17 日起生效的 [Muse 隐私政策](https://muse.ai/privacy) 是一份值得完整阅读的短文件，而它最短的一句话承担了最多工作：「此设置在你首次使用 Muse 时即开启。」该设置决定你的互动是否用于训练 Meta 的模型。关掉它需要三次点击——设置、数据控制、开关——这至少算诚实。

然后是大多数店主永远不会读到的那句，全文引用：「你与 Muse 的互动还可以包含 Muse 用来为你执行任务的服务的信息，包括连接器。你设置中的同一个开关控制这些信息能否被用于改进 Meta 的 AI。」再慢慢读一遍：账本、客户名单、工资发放，数据一流入就默认可用于训练。

Meta 用一句话列出了移除清单：它会剥离「某些类别的个人可识别信息，如姓名、电子邮件地址、电话号码和社会安全号码」，然后把其余信息与你的账户解关联，总共四个具名类别。现在盘点一个 QuickBooks 连接实际携带什么：客户购买历史、收入和利润率数字、供应商的银行路由号码和账号、员工薪资金额、客户地址；然后划掉 Meta 点名的那些，你保留下姓名、邮箱和电话；你的利润率、你供应商的银行账户、以及每位客户买了什么、多久买一次，在那句话里都没有出现。「如」让这份清单保持开放，意味着它可能比陈述的更长，尽管它也可能恰好如所写的那样短，所以按短的版本假设。

追溯性是其中表述得令人钦佩地清楚的一部分：「对此设置的更改也适用于此前的互动。」政策从未说明的是，对于一个已经用你的数据训练过的模型会发生什么。文件中没有任何内容承诺从训练权重中抽除，因为目前没有公司能干净地做到这一点，而一旦模型看过你的利润率，开关就是在卡车离开后才关上的门。

然后还有那个从未点击过任何东西的人：你连接了 QuickBooks，但你的客户没有，你的员工没有，你的供应商没有，因为它的措辞是「你的互动」，而一个企业主的互动是由其他人的信息构成的。同意恰好只穿透一个人深，政策对另外两个人无话可说。另外两个人从未注册。

Meta 的反方观点值得以全力获得公平的聆听。负责 Meta Superintelligence Labs 的副总裁 Tarek Sheasha [告诉 WIRED，这一默认是有意为之](https://www.webpronews.com/metas-muse-sets-record-for-data-appetite-as-privacy-fears-mount/)：每个用户都因为所有用户共同教会它「人类生活的复杂之处」而得到更好的智能体。他说得对，改善是真实的，而小企业会是受益者之一。Meta 还把对话和 VM 数据与其广告系统隔开，即使在共享的 Accounts Center 内部也是如此，这是它历史上大多不会提供的结构性隔离，而 Sentinel 和审批关卡意味着智能体没有所有者就无法发布、发送或花钱。拿它跟现状比，而不是跟一个不存在的完美私密智能体比：每周六十五小时、用邮件发到个人地址的电子表格、记在共享笔记本里的密码、离职时把客户名单拷到个人手机上的员工。一个有审计轨迹的智能体胜过一张便利贴，但前提是你在数据流入之前设好关卡，这正是所承诺的最终状态为何重要：Confidential VM，「一个我们正在设计、以让个人信息即使对 Meta 也保持私密的环境」。注意时态。设计中，不是已设计。它尚未交付。在那之前，保证是一套 Meta 对自己执行的政策，而不是你持有的加密。

### 五个动作，按顺序，第一个发生在你连接任何东西之前

1. **先拨动训练开关。** 设置、数据控制、「帮助改进我们的 AI 模型」、关闭，因为连接器数据一流入就变得可用于训练，而且没有已记录的路径能离开一个已经训练过的模型。
2. **让 Muse 远离你的个人 Accounts Center。** 用单独的邮箱注册，因为政策允许把一个 Accounts Center 内多个资料的信息合并，而分离是注册时的一次性选择。
3. **先连接最窄的范围。** 在提供只读连接器模式的地方使用它，先接分析和销售摘要，再接工资和供应商银行信息，因为智能体不需要你的路由号码就能找到一笔异常支出。
4. **把连接视为对第三方的披露。** 你的客户和员工从未同意，所以像你刚把数据电邮给一个供应商那样阅读你的合同、你所在州的隐私法和你的职业伦理规则，因为从功能上说，你确实这么做了。
5. **审计智能体记住了什么，并相信动词。** 问 Muse 它记得你什么，并对特定主题使用 Forget 技能。政策自己的措辞是，Muse 会「尽其所能」忘记，而在你删除某样东西之后，Muse 可能仍然「记得」它从你删除的内容中学到的信息。那是文件中两段最诚实的句子。

## 本文没有证明什么

以下是诚实的交代。我无法独立核实 Meta 的脱敏流程，也无法确认「某些类别」除政策点名的四类之外还覆盖什么，所以缺口分析建立在文本如所写之上，而不是对管道的审计。Meta 之外没人能说实践中哪些字段会过线，因为 QuickBooks 和 Stripe 连接器请求的 OAuth 范围在我找到的任何来源中都未公布，我也没有在真实应用中测试数据控制开关，而一家媒体报道的订阅定价未经 Meta 确认。六周过去，不存在对训练管道的独立审查，而 Confidential VM 除了「我们正在设计」之外没有公开的交付日期。

这种宽慰是真实的。默认也是真实的。在你连接账本之前，检查那个开关。
