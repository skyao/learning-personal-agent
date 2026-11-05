---
title: "Meta 在上线前不久紧急修复 Muse「VM 逃逸」漏洞"
linkTitle: "404 Media：上线前 VM 逃逸"
date: 2026-10-05
originalTitle: "Meta Rushed to Fix Muse ‘VM Escape' Vulnerability Soon Before Launch"
sourceUrl: "https://www.404media.co/meta-rushed-to-fix-muse-vm-escape-vulnerability-immediately-before-launch/"
author: "Jason Koebler"
publisher: "404 Media"
language: en
fidelity: 全文翻译
translation: 已翻译
collectedAt: 2026-11-04
tags: [安全, 运行环境]
products: [muse]
---

{{< source-info >}}

（译注：原文中征集线索的提示框和文末作者简介未译出。）

404 Media 获悉，在 Muse 上线前的最后几周，Meta 工程师在这款公司爆红的 AI 智能体产品中发现了多个安全漏洞，其中至少一个可能让恶意用户突破 Muse 预定的运行环境，访问 Meta 自己的敏感数据库和服务。这些问题严重到上报给了 Mark Zuckerberg，员工们加班加点修复。

这些具体的漏洞是在产品上线前发现的，但根据 404 Media 看到的一篇 Meta 高管发给其核心基础设施团队的内部帖子，修复它们需要多个团队「疯狂冲刺」（mad dash），以应对「报告的 KVM 逃逸突然激增」（a sudden spike in reported KVM escapes）。为了让 Muse 工作，用户要授予这个 AI 智能体访问自己名下各种重要服务和账户的权限。在 Meta 一侧，每个 Muse 实例都[运行在一台基于内核的虚拟机上](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)，这台虚拟机与 Meta 自己的关键基础设施相连，但本应与之隔离。所谓「KVM 逃逸」，就是一个 Muse 实例借助某个安全漏洞逃出那台虚拟机，与运行它的系统或其他用户的虚拟机发生交互。

据一位 Meta 消息人士以及 404 Media 查阅的内部安全文档和内部帖子，其中至少一个漏洞可能让一名外部攻击者，也就是一名普通的 Muse 用户，访问 Meta 敏感内部数据库中的数据。。至少有一个漏洞[与 7 月在 Linux 基于内核的虚拟机代码中发现的一个漏洞利用有关](https://www.csoonline.com/article/4194085/16-year-old-kvm-flaw-allows-attackers-to-escape-vms-and-take-over-linux-servers.html)。404 Media 允许这位 Meta 消息人士匿名谈论敏感的安全事务。（译注：原文此处有一个多余的句点，照录。）

其中几个漏洞位于 Meta 为 Muse 使用的底层 Linux 虚拟化软件中。这一安全问题被认为严重到需要上报给 Mark Zuckerberg，几个不同的安全团队在上线前夜以继日、连周末都在修复这些问题。在重大产品上线之前进行这类安全冲刺并不一定罕见，但考虑到 Muse 上线以来外部研究人员又发现了其他几个安全问题，以及 OpenAI 等公司的智能体 AI [大肆进行黑客攻击](https://apnews.com/article/ai-hacking-hugging-face-openai-anthropic-452281863a49b18220057e71d4715cf4)的大背景，这一点值得注意。

这位 Meta 消息人士说，他们觉得安全团队被要求以不耽误 Muse 上线的方式尽快为这些漏洞推送热修复，导致了他们所说的「为了让上线成行而仓促推出的半吊子保护。许多资深工程师认为，Hatch 将不可避免地导致一场大规模数据泄露。」Muse 在内部和 Meta 的代码库中被称为「Hatch」。

Meta 核心基础设施副总裁 Surupa Biswas、工程副总裁 Francois Richard 和工程高级总监 Josh Barry 在 Muse 上线 10 天后的 9 月 18 日，向公司核心基础设施团队发布了一篇内部帖子，承认了这次安全冲刺。

帖子写道：「有了 Muse，我们是在直接代表终端用户托管和运行智能体，这是一种根本不同的范式。报告的 KVM 逃逸突然激增，加上对智能体安全问题的关注提高，促使我们集中力量推进一次服务加固。」

帖子提到，这次冲刺从 8 月 27 日开始，持续了「几周外加几个周末」，而 Muse 在 11 天后就发布了。帖子说，这项工作包括采取措施「缩小 Hatch 智能体可访问的攻击面」。各团队还采取措施「限制 Hatch 和 VMVM 主机可以到达的端口和 IP 目的地」。

Muse 的虚拟机逃逸是一个潜在非常严重的安全问题，在 Meta 的漏洞赏金计划中也被如此归类。该公司表示，愿意向发现可导致 VM 逃逸的漏洞的任何安全研究人员[支付 300,000 美元](https://bugbounty.meta.com/payout-guidelines/muse/)，这是其漏洞赏金网站上列出的最高赔付。

该公司在漏洞赏金页面上解释说：「Muse 是 Meta 的一款 AI 产品，让人们创建自己的个性化 AI 智能体，也就是他们的 Muse。每个 Muse 智能体都运行在一台每用户专用的虚拟机中，并连接到该用户自己的服务：电子邮件、日历、消息、浏览以及第三方账户。由于 Muse 智能体掌握着用户最敏感的数据，并且可以代表用户行事，我们把攻破这一边界视为头等的安全风险。」最高风险级别是借助 VM 逃逸「攻破 Meta 生产环境以及 Muse 以外的用户」，它将其描述为「从 Muse 访问 Meta 生产服务或内部网络」。据这位 Meta 消息人士说，至少其中一个漏洞本可能做到这一点。

在给 404 Media 的一份声明中，一位 Meta 发言人说：「Muse 是第一个为所有人打造的个人 AI 智能体，我们为确保它安全、可靠和私密所做的工作感到自豪，它内置的保护措施和用户控制让人们掌控自己如何使用它。我们通过大量的内部试用、智能体式红队测试和我们的漏洞赏金计划加强了 Muse，这项工作还在继续。」

到目前为止，Muse 的推出并不平顺。这款智能体因为能够取消订阅、预订餐厅和预订旅行等事情而大受欢迎，或者至少引起了很大的关注。但安全研究人员 Patrick Wardle [在 Muse 中发现了一个零日漏洞](https://x.com/patrickwardle/status/2102045926474785265)，据他所知，当时公司并不知道这个漏洞，它让应用和终端命令可以控制用户的 Muse。据这位 Meta 消息人士说，另一位 Muse 用户能够让 Muse 导出他的 Instagram 粉丝，以及他粉丝的粉丝，这本不应该做到，Meta 的安全团队对此进行了调查。

谈到潜在的 Muse KVM 逃逸，Wardle 对 404 Media 说：「问题在于，Hatch 把虚拟化边界变成了生产环境的安全边界。我们让拥有 root 权限的用户待在一台虚拟机里，而这台虚拟机本身被放在 Meta 的生产环境中，并且（按设计）被授予了对内部服务的有限访问权限。因此，KVM 中的一次失败（或者甚至是一个内部可达服务中的漏洞或错误配置），就可能把任意用户代码变成生产环境访问权限。我觉得这种设计本质上是有风险的，尤其是在 AI 降低了发现、分析和利用恰恰这类复杂虚拟化漏洞的成本的情况下，风险尤其大。」

他补充说：「我知道一切总是在可用性和安全性之间取舍，但这就是为什么在最高安全级别的环境中，系统是物理隔离的，因为总是假定相互连接的系统可能被利用。当然，没人指望 Meta 做到那一步，但让生产环境与用户只隔着一次 KVM 逃逸，简直是不负责任。」
