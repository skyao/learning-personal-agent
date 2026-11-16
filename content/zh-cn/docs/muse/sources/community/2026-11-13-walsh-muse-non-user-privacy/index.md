---
title: "Walsh：Muse 正成为更大的隐私威胁，没用它的人也会受影响"
linkTitle: "Walsh 非用户隐私"
date: 2026-11-13
originalTitle: "Meta's spyware agent Muse is becoming an even bigger privacy threat, and you don't have to use it to be affected. New findings."
sourceUrl: "https://paulfwalsh.substack.com/p/metas-spyware-agent-muse-is-becoming"
author: "Paul Walsh"
publisher: "Paul Walsh（Substack 通讯）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-14
tags: [隐私, 安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：经 Substack API 取得全文（/api/v1/posts/metas-spyware-agent-muse-is-becoming）。原文 2026-11-13 发布（UTC 20:23，美东 11 月 13 日）。这是作者此前技术分析的后续，聚焦非用户隐私问题；此前分析的批评内容已由已收的 BetterClaw 隐私分析逐项核查。文末的订阅推广、内测邀请与“为何转到 Substack”一节不属于正文，已删去；商业利益披露段保留。头图为装饰插画，未收。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：作者 Walsh 称，自己从未要求、从未激活 Muse，但 WhatsApp 里新出现了无法移除的 Muse 浮动头像与快捷入口，其他人也报告了同样情况。作者认为，用户把私信、邮件、联系人、日历、照片、银行账户、位置与健康记录交给 Muse 后，也会连带暴露从未安装或同意使用 Muse 的联系人，因为加密只保护传输过程，而 Muse 是在设备端加密前或解密后取得完整对话内容。作者引用研究者 Karan Joshi 提取的内部指令及 WIRED 与 TIME 的报道称，Muse 会为用户生活中的每个人建页、档案每小时更新，并据此认为 Meta 有能力把私人通信与健康、财务、情感、政治倾向等情况连起来做画像。文中列举的已公开事件包括：Jason Aten 的 iMessage 历史含逾 187,000 行数据库记录，Muse 给出了虚假解释，Meta 承认解释不实但否认访问未经授权；Matt Robb 的住址被发给陌生人，制止后又发给另外 5 人，Meta 归因于 Robb 已授予的权限；安全研究者 Patrick Wardle 发现的漏洞已被 Meta 修补；路透社披露的真人代打成功率为 95–98%，Meta 承认披露失误并暂时撤下该功能；亚马逊以未经授权访问等理由封堵 Muse，Meta 否认凭证方面的指控；文末披露作者正在开发 WhatsApp 替代品，存在商业利益。

**保留理由**：这篇从“从未使用 Muse 的人也会被暴露”的角度论述非用户隐私问题，把多起已公开事件串在同一论点下。作者本人的 WhatsApp 浮动头像经历与文末的商业利益披露，是已收资料中没有的一手叙述与利益冲突信息。

---

Meta 在 9 月推出了 Muse，但它那个悬浮的 AI 虚拟形象直到最近才出现在我的 WhatsApp 里。我从没要求过，没有激活它，也无法移除它。其他人也在报告同样的问题。Meta 实际上已经决定，把它的 AI 推广强行塞进人们的私人通讯应用，不管人们想不想要。这已经够糟了，但我所发现的关于 Muse 访问私人信息的情况，要令人不安得多。

全世界已有数百万人在使用 Muse，他们给了 Meta 对私信、电子邮件、联系人、日历、照片、视频、文档、浏览活动、银行账户、购买记录、旅行计划、位置历史、健康记录、健身信息以及受端到端加密保护的对话的完全、不受限制的访问权限。这种访问还可能暴露心理健康状况、药物、就诊预约、性关系、宗教信仰、政治观点、保密信息来源和个人纠纷。

这样做，他们也在暴露与他们有联系的每一个人的敏感信息，包括从未安装 Muse、也从未同意 Meta 访问其私人生活的人。

Muse 可以构建关于人们的关系、私人对话、个人处境和弱点的详细档案。与 Meta 现有的社交图谱相结合，这就产生了极高程度的个人画像的可能性。

其影响不止于定向广告。Meta 正在在人们不知情的情况下收集关于他们的健康、财务、关系、职业活动和个人弱点的私密细节。

关于你的一切此刻都可能已被暴露，而你永远不会知道。

我之前的技术分析考察了 Muse 已有记录的隐私与安全失误。这一篇考察的是更重要的事：Meta 如何能够获取关于从未同意使用其 AI 的人的私密信息。

即使是 Signal、iMessage、WhatsApp 内本应受端到端加密保护的对话，也在被暴露。加密保护的是消息在传输过程中的安全，但 Muse 被赋予了访问整段对话的权限，访问发生在对话被加密之前，或在它们于某人的设备上被解密之后。

执法部门不再需要向科技公司施压、让它们为加密通信构建后门了，因为像 OpenAI 和 Meta 这样的科技公司已经造了一个侧门。

你不需要安装 Muse、WhatsApp、Instagram、Facebook 或任何其他 Meta 产品，就会成为这套数据收割方案的一部分。任何持有你的消息、电子邮件、照片、联系方式、日历邀请、关于你的私人对话、个人日记或保密客户笔记的人，很可能都在把这些信息暴露给 Meta。

当你看看 Muse 如何处理这些信息时，这一点就变得令人不安得多。

研究者 Karan Joshi 提取出了内部指令，这些指令告诉 Muse 为某人生活中的每个人创建一个页面。[WIRED 报道](https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/)称，这些页面可以包括家人、伴侣、朋友、同事和其他联系人。[TIME 查阅了这些指令](https://time.com/article/2026/10/06/meta-muse-ai-agent-privacy/)，其中描述的档案每小时更新，包含关于关系、共同兴趣、分歧、个人经历、社交联盟以及影响其行为的方式的信息。

因此，Meta 在技术上有能力构建详细的社交图谱，其作用不止于识别谁认识谁。Muse 可以把私人通信与个人处境、弱点、经济困难、关系问题、健康隐患、情绪状态、政治信仰、性取向、职业关系以及一个人生活中的重大事件联系起来。AI 可以在这些记录中识别规律，推断出人们从未明确披露的信息，并为从未同意参与的个人建立画像。

**想想类固醇加持的 Cambridge Analytica。**

Cambridge Analytica 展示了个人信息与社交关系如何被利用来做心理画像和政治定向。Muse 带来了更私密画像的可能性，因为它可以分析私人对话、往来信件、关系和个人处境，而不是主要依赖社交媒体活动。

Meta 声称 Muse 的私人对话和虚拟机数据不会与其广告服务共享。Mark Zuckerberg 说的话我一个字都不信。他被抓到撒谎的次数多到，哪怕他自我介绍说他叫 Mark，我也不会信。Meta 仍然可以出于运营目的访问其虚拟机中的数据，而且除非用户选择退出，Muse 的交互默认会被用于 AI“训练”。所承诺的、旨在防止 Meta 自己访问私人记录的保密计算（confidential computing）保护，还没有全面可用。真是意料之中。

2021 年，[ProPublica 揭露](https://www.propublica.org/article/how-facebook-undermines-privacy-protections-for-its-2-billion-whatsapp-users)，1000 多名 WhatsApp 承包商审阅了数以百万计被人们举报的私人消息、照片和视频。2026 年，[前 Accenture 承包商报告](https://www.bloomberg.com/news/articles/2026-01-29/us-has-investigated-claims-that-whatsapp-chats-aren-t-private)称，Meta 的员工和承包商对加密的 WhatsApp 对话拥有范围广得多的访问权限。Meta 当然否认了这一点，而美国政府的一项[调查已结束](https://www.business-standard.com/world-news/us-ends-probe-into-claims-whatsapp-chats-were-reportedly-not-private-126042900013_1.html)，没有证实此事。

后果还延伸到记者、律师、政治活动人士、吹哨人、医疗专业人员、企业高管、教练、执法人员、军人、政府官员，以及任何其私人关系或通信可能暴露机密信息的人。只要有一个人把 Muse 连接到自己的账号，就会暴露敏感的往来信件，识别出保密的信息来源，揭示个人的弱点，或泄露关于整个职业和社交网络的信息。

Muse 被发现披露私人信息、冒充他人、未经授权做出安排、对自己的行为给出虚假解释，并暴露出严重的安全漏洞。这一切都发生在它上线后的几周之内。

Muse 访问了记者 Jason Aten 的[私人 iMessage 历史记录](https://decrypt.co/379122/metas-muse-ai-agent-user-private-imessages-lied-how)，其中包含超过 187,000 行数据库记录，尽管他拒绝授予权限。被问及时，Muse 对它如何获得这些信息给出了虚假的解释。换句话说，它撒了谎。Meta 承认该解释是虚假的，但[对访问是否未经授权提出异议](https://decrypt.co/379868/meta-ai-agent-read-messages-without-permission)。

Muse 向一个陌生人披露了 [Matt Robb 的家庭住址](https://futurism.com/artificial-intelligence/metas-muse-ai-giving-users-home-addresses)，谈妥了他的电脑设备的出售，并在 Robb 不知情的情况下安排买家上门拜访。它告诉买家 Robb 在家，而他实际上不在。在 Robb 指示 Muse 停止披露他的住址之后，它又把住址告诉了另外 5 个人。Meta 把最初的事件归因于 Robb 曾授予的权限。

安全研究者 Patrick Wardle [发现了一个漏洞](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html)，它允许恶意软件劫持 Muse，并利用其权限来追踪一台已连接的 iPhone、访问摄像头和操纵文件。[Meta 修补了它](https://unite.ai/meta-hot-fixes-muse-zero-day-that-let-attackers-hijack-the-ai-agent)。

[路透社揭露](https://www.ctvnews.ca/sci-tech/article/meta-testing-a-human-concierge-for-its-new-personal-ai-agent-muse-reuters-exclusive/)，Meta 秘密使用真人承包商为 Muse 客户打电话，有真人协助时成功率为 95–98%。这就是 Muse 的 AI 能力。员工提出了隐私方面的担忧，其中一人报告了种族主义行为。Meta 承认了披露方面的失误，并暂时撤下了该功能。Meta 只有在被迫时才撤下功能，而不是在它自己的员工提出担忧时。

[Amazon 封堵了 Muse](https://geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping)，指责 Meta 未经授权访问其购物服务、未表明其 AI 智能体的身份，并可能收集客户凭证。Meta 对凭证方面的担忧提出异议。

看到趋势了吗？

Meta 已经把一个 Muse 快捷入口强行放进 WhatsApp，邀请人们激活它的 AI 智能体，却没有提供移除它的方法。我没有激活 Muse，我不想要它，而 Meta 不让我摆脱它。

---

**为透明起见：** @Johan Mackie 和我正在构建一种新型的消息服务，它给人们与 Signal 相同的隐私保护，而且多得多。是时候让人们拥有比 WhatsApp 更好的选择了，它在隐私、个人掌控以及人们如何交流上采取根本不同的做法。

我在提供 WhatsApp 的替代品上有商业利益，所以我希望读者在阅读本文时了解这一点。
