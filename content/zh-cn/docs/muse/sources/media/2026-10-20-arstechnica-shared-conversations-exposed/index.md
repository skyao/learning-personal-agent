---
title: "Meta Muse 在用户分享对话时暴露其个人和商业机密"
linkTitle: "Ars Technica：分享链接泄露"
date: 2026-10-20
originalTitle: "Meta Muse exposes users’ personal and business secrets when they share conversations"
sourceUrl: "https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations/"
author: "Dan Goodin"
publisher: "Ars Technica"
language: en
fidelity: 全文翻译
translation: 已翻译
collectedAt: 2026-11-04
dateNote: "页面时间为 2026-10-20 08:33（美国东部时间）"
tags: [安全, 隐私]
products: [muse]
---

{{< source-info >}}

**收录说明**：这是 Ars Technica 记者 Dan Goodin 的报道，全文翻译。页面时间为 2026-10-20 08:33（美国东部时间）。原文的阅读设置控件、作者简介和评论入口未译出，已在页首译注中说明。早期收集时直接翻译，原文未单独存档。

**内容摘要**：安全公司 Claroc 的研究人员报告，Muse 用户分享对话生成的链接很容易被发现，他们枚举出了 6,800 个链接。原因是所有链接都用 cf.metaaiusercontent.com 域名，并把对话标题放在子域名里，被动 DNS 记录会把它们保存下来。打开其中几百个后，研究人员发现了招聘通话笔记、营收审查、贷款申请、银行欺诈警报等不打算公开的内容。Claroc 称这类页面为 GhostShares，并说他们于 10 月 8 日通过漏洞赏金计划报告，两边都没有得到回复。Meta 表示已暂停分享功能，正在审查并考虑改变链接被发现的方式。

**保留理由**：这篇记录了分享功能被暂停的原因和链接设计上的具体缺陷，也提供了 Claroc 的发现时间线和 Meta 的回应。

---

GHOSTSHARES

Meta 正在暂停分享功能，同时调查其隐私问题。

![](images/hero.jpg)

图片来源：Getty Images

研究人员周一报告称，Meta 新推出的通用 AI 智能体 Muse，在用户通过网页链接分享对话时，可能会暴露敏感信息。在回应 Ars 就这一行为提出的问题时，Meta 表示，它正在暂停分享功能，同时对其进行审查并考虑做出修改。

和许多在线服务一样，Muse 允许用户与其他人分享搜索、对话、图片和类似内容。这类分享功能通常是点击一个选项来生成一个唯一的 URL，任何人都可以用它加载托管该内容的页面。为了防止潜在的敏感信息被不相干的人访问，这类 URL 通常包含一长串不容易猜到的文本。

## 只需要一次查询

Meta 首席执行官 Mark Zuckerberg [上个月曾说](https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/)，Muse「从零开始就是为隐私和安全而构建的」，它似乎也采取了同样的预防措施。但一个关于如何构造 URL 的核心设计决定，让这些链接很容易被发现。结果，安全公司 Claroc 的研究人员[说](https://blog.claroc.io/ghostshares-muse-passive-dns/)，他们得以枚举出 6,800 个 Muse 用户为与他人分享对话而创建的链接。在打开其中几百个之后，研究人员发现了显然不打算公开的信息，包括：

- 一位候选人为与一家前沿 AI 实验室进行的机密高管招聘通话所做的准备笔记，其中写明了该实验室的内部联系人和会议时间
- 一家全国性营销公司的内部营收审查，标注给其首席执行官
- 一位小企业主的贷款申请，附有申请金额
- 一份待办清单，其中包括一条银行欺诈警报，附有部分账号以及一笔交易的金额和时间
- 一位房地产投资者的内部业绩报告，附有两处房产地址以及确切的回报、收入和抵押贷款数字
- 一个工作场所全年的员工休假日历，列出了几十名员工各自休假的那一周

研究人员写道：「如果你事先问我们，我们会猜收集这些需要花真功夫。结果只用了一次查询。」

在回应 Ars 提问的一份电子邮件声明中，Meta 说：

> 我们开放了 Muse 漏洞赏金计划，以便研究人员可以提出各种场景，帮助我们持续改进产品。人们能够分享特定的 Muse artifacts，这会创建一个持有链接的人可以访问的页面。不过，在我们审查这份报告、考虑改变这些链接被发现的方式期间，我们已经暂停了这项功能。

Claroc 联合创始人兼首席技术官 Asaf Aprozper 说，他于 10 月 8 日通过 Meta 的漏洞赏金计划报告了这些发现，还尝试在 LinkedIn 上联系 Meta 的人，但两边都没有得到回复。

发现这些 URL 最简单的方法，是通过众多现成的商业服务之一进行被动 DNS 搜索。[被动 DNS 记录](https://www.spamhaus.com/resource-center/what-is-passive-dns-a-beginners-guide/)存储了域名到 IP 地址的历史解析记录，以及随时间变化的域名服务器和邮件服务器记录。被动 DNS 系统通常从部署在递归 DNS 解析器或其他基础设施处的传感器收集 DNS 响应。一条被动 DNS 记录通常在监控系统观察到一个 DNS 响应时生成。在这里的情形中，一旦预定的接收方点击了分享链接，DNS 信息就会被记录在一个可搜索的数据库中。

Claroc 的研究人员之所以能发现 Muse 的分享链接，是因为所有这些链接都使用 cf.metaaiusercontent.com 这个域名。把对话名称连同一长串文本加进 URL 的决定，让发现变得更加容易。这类链接的简化示例有 home-sale-budget-9f21c8a3.cf.metaaiusercontent.com、q3-revenue-review-7b1e42f0.cf.metaaiusercontent.com 和 loan-application-draft-a4c9e2.cf.metaaiusercontent.com。正是最后这个设计决定，把对话标题放在子域名里而不是 URL 路径里，让公开发现成为可能。

Claroc 说：「很多 AI 助手都通过公开链接分享。让 Muse 的分享容易被找到的，是标题就放在网址里，而公共 DNS 会把它记录下来，供任何人搜索。我们把这些称为 GhostShares：那些会为从未拿到过链接的人打开、并且这些人能够自己找到的页面。」

Muse 迅速蹿升到苹果 App Store 的榜首位置之一。这个助手会自主地填写表单、预约、购物、创建文档，以及执行各种其他操作。为了按预期工作，Muse 需要访问用户的大部分账户。Meta 大力宣传这个助手是一个值得它为正常工作所需的那种非同寻常的信任的平台。

Muse 上线三周后，macOS 安全专家 Patrick Wardle [发现了一个零日漏洞](https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/)，让安装在同一设备上的任何其他应用都能完全控制用户的 Muse 账户。Meta 淡化了这个漏洞的严重性，理由是除非设备已经被攻破，否则无法利用它。该公司没有承认 Wardle 的发现：只需一次简单的 [ClickFix 攻击](https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/)就足以劫持一个账户。分享链接如此容易被发现，进一步让人有理由质疑 Muse 是否配得上它所要求的访问权限。

随着 Meta 暂停这项功能，Muse 用户至少目前不再面临这一特定威胁。
