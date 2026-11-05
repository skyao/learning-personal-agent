---
title: "Muse 为你所有的朋友和家人建立详细档案"
linkTitle: "WIRED：亲友人物档案"
date: 2026-10-03
originalTitle: "Muse Creates Detailed Profiles of All Your Friends and Family"
sourceUrl: "https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/"
author: "Lily Hay Newman, Matt Burgess"
publisher: "WIRED（Kernel Panic 通讯）"
language: en
fidelity: 全文翻译
translation: 已翻译
collectedAt: 2026-11-04
dateNote: "页面显示 Oct 3, 2026 8:00 AM（美国东部时间）"
tags: [记忆与上下文, 隐私]
products: [muse]
---

{{< source-info >}}

（译注：文末征集线索的提示未译出。）

数百万人下载了 Meta 的 AI 智能体 Muse。但让它听你使唤，是有隐私代价的。

![Meta 的 AI 智能体 Muse 的一个头像，在美国加利福尼亚州门洛帕克的 Meta Connect 活动上显示在屏幕上……](images/hero.jpg)

照片插图：WIRED 员工；Getty Images

*欢迎阅读 [Kernel Panic!](https://www.wired.com/newsletter/exclusive/kernel-panic)，这是 [Lily Hay Newman](https://www.wired.com/author/lily-hay-newman/) 和 [Matt Burgess](https://www.wired.com/author/matt-burgess/) 从隐私和数字安全新世界的内部发出的每周通讯。想每周在收件箱中收到这份通讯，请[在这里订阅](https://www.wired.com/newsletter/exclusive/kernel-panic)。*

Meta 的新个人助手 [Muse](https://www.wired.com/story/meta-releases-muse-a-personal-ai-agent-with-privacy-built-into-it/) 已经成为爆款，数百万人下载了这个 AI 智能体，把它连接到银行账户、消息或健康数据，并允许它替自己完成任务。但随着 Muse 在消费者中[迅速流行](https://www.wired.com/story/ai-agents-dots-devday-muse-battling-it-out/)，来自应用内部的数据正在让人们了解它是如何组织和呈现信息给用户的。

最近几天，多名研究人员[提取了](https://mouse.dev/blog/muse-runtime-export/) Muse 的内部文件，并转储了这个智能体的运行指令，让人得以一窥这个系统是如何构建的、如何运作的。Meta 一直坚称，它是出于透明的考虑而有意让这些文件可以被访问的，而这些文件也确实揭示了 Muse 如何回应提示和问题，例如关于高度政治化或敏感话题的提示和问题。

独立的 AI 安全研究员 Karan Joshi 通过普通的聊天界面，基本上就是请 Muse 复制并分享它自己的软件文件，从而提取出了大量 Muse 的指令和系统提示。随后，Joshi 与 WIRED 分享了他的发现。

Muse 的指令之一似乎是让它能够为「用户生活中的每一个人建立一个页面」（a page for every person in the user’s life）。指令说，这个[每小时运行一次](https://futuresociety.ch/muse-findings/#finding-relationship-pages)的过程会汇编关于家人、伴侣、朋友、同事、「合作者」以及你「关注」的人的数据。

总体思路是，Muse 可以利用它的「[记忆](https://www.wired.com/story/i-am-begging-ai-companies-to-stop-naming-features-after-human-processes/)」（也就是结构化的文本文件）来收集关于你的人际关系和你生活中重要的人的信息。然后它可以提出建议，比如就如何改善某段特定关系给出指点，或者，比方说，带一位爱喝咖啡的朋友去哪里吃早餐。当然，AI 聊天机器人追踪一般的社交信息并不稀奇，人们向 ChatGPT 寻求[感情建议](https://www.wired.com/story/please-stop-asking-chatbots-for-love-advice/)已经好几年了。但考虑到 Meta 的[历史](https://www.wired.com/story/facebook-data-leak-contact-import-flaws/)及其对社交网络数据的庞大访问权限，看看 Muse 是如何设置的，还是很有意思的。

「从所有这些提示、系统技能数据，以及他们喂给 Muse 的东西来看，我的感觉是，他们想要了解你与真实的人之间的关系，」Joshi 说。「他们试图像朋友一样了解你，说实话，这挺让人毛骨悚然的。」

Muse 的文档说，一个页面可能一开始「很单薄」（sparse），然后随着时间推移逐渐充实，可能包括「事实」（Facts）、「历史」（History）、「这段关系」（The relationship）、「共同点」（In common）、「未了之事」（Open threads）和「加强」（Strengthening）等部分。Meta 的指令说，Muse 应该只使用它掌握的「证据」，编造的细节比空白的页面更糟糕。

「他们住在哪里，做什么，反复出现的话题（搬公寓、共同的储蓄目标）」，指令写道。指令还补充说，模型可以记录「重要的日子」，比如生日或纪念日。一个人的历史可以包括诸如「三月的那次旅行、那次已经化解的争吵、上周的那个里程碑」之类的背景故事。

这些指令还侧重于记录关系细节，比如「他们有多亲近，这段关系建立在什么基础上，他们彼此如何相处，以及它现在似乎需要什么」。「加强」部分提出了改善一段关系的方法，包括「一个打电话的理由，一个值得记住的日子，一件他们说过、值得回头再提的事，一种以对他们重要的方式陪在他们身边的办法」。

「我们给 AI 系统的关于我们的信息，远远多于我们从它们那里得到的信息，」牛津大学 AI 伦理研究所副教授 Carissa Véliz 说。「这不仅是我们明确告诉它们的东西，还有它们能从我们身上推断出的东西（无论推断得对还是不对，两者都令人担忧，理由各不相同），以及它们能从其他数据来源拼凑出来的东西。」

Muse 的架构使每个用户都有自己的专用虚拟机，用来存储用户数据和上下文。其他智能体无法访问这台虚拟机，用户可以随时清除记忆或断开外部服务。Meta 说，Muse 还被设计为在完成发送电子邮件或购物等操作之前寻求人工确认，并且它有一个审计日志，用户可以在其中看到智能体的所有活动和未来计划。

「任何智能体要想有用、真正帮助你实现目标，都需要了解关于你以及与你互动的人的上下文，」Meta 发言人 Daniel Roberts 在给 WIRED 的一份声明中说。「Muse 根据公开信息以及你选择分享的内容来收集这些上下文，正是这样，它才能记住给你发发票的那个人其实就是你之前雇来修浴室的水管工，或者你的配偶说过最喜欢哪种花。」

AI 助手加入某种记忆功能、以便在回答和活动中实现[更高程度的个性化](https://www.wired.com/story/how-to-use-memory-in-chatgpt/)，已经变得很普遍。民主与技术中心（Center for Democracy and Technology）AI 治理实验室主任 Miranda Bogen 说，与竞争对手的系统相比，Muse 似乎更加强调人际关系和个人联系人。总的来说，这些工具往往会提供一定的透明度和编辑能力，[Muse 也是如此](https://www.meta.com/en-gb/help/artificial-intelligence/995796179982326/)。不过，Bogen 指出，如果说有什么区别的话，那就是智能体和助手鼓励人们主动与它们分享更多数据，而不是着重于精简数据。

「这些［AI 助手］工具正在积极地诱导用户把自己的整个生活都接进来，他们的电子邮件、日历、金融机构，一切都接进来，以便提供有用的帮助，」Bogen 说。「这比人们原本可能会给这些公司的信息要多得多。这些工具能够访问的信息之广，将导致它们对用户的了解急剧膨胀。（译注：原文此处引号未闭合，照录。）
