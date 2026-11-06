---
title: "Grok Bot 把一位 CEO 的银行数据泄露到公司 Slack"
linkTitle: "Cybernews：银行数据泄露到 Slack"
date: 2026-10-07
originalTitle: "Grok Bot leaks CEO’s bank data across company Slack"
sourceUrl: "https://cybernews.com/ai-news/grok-bot-leaks-bank-information/"
reprintUrl: "https://web.archive.org/web/20261021011052/https://cybernews.com/ai-news/grok-bot-leaks-bank-information/"
author: "Niamh Ancell"
publisher: "Cybernews"
language: en
fidelity: 转载全文
translation: 已翻译
collectedAt: 2026-11-05
updatedAt: "2026-10-08"
dateNote: "原站拒绝自动访问，依据 Wayback 快照 20261021011052"
tags: [安全, 隐私, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：原站拒绝自动访问，原文依据 Internet Archive 快照（20261021011052）存档；去掉了文首由 nexos.ai 生成的「Key takeaways」要点框、文中插入的「More from Cybernews」推荐和作者简介。Techdirt 2026-10-19 的评论文章转述的就是这篇报道，未另收。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：XMTP Labs 的 CEO Shane Mac 把 Grok Bot 连接到个人银行账户，用作只读的财务助理，结果另一个 Grok Bot 以他的身份把银行余额和支出明细发到了公司 Slack 频道。Mac 称管财务的那个 Bot 没有 Slack 权限，但另一个有，「Turns out, they're all connected」。文章指出同一账号下的所有 Bot 共用一台云端计算机，并引用 SpaceXAI 的说明：计算机分配给用户账号而非单个 Bot，不要把凭证或文件放在其他 Bot 能用到的地方。文末提到 Musk 此前曾在 X 上回复用户可以连接银行账户，「Grok Bot messes up, we will make you whole」。

**保留理由**：一起真实发生的跨 Bot 数据泄露事件，直接说明了「多个 Bot 共用一台计算机、按用户而非按 Bot 隔离」这一设计的后果，可与官方安全文档对照。

---

**一位 CEO 让 Elon Musk 的 Grok Bot 当他的首席财务官，结果发现自己的个人财务信息散落在 Slack 上，供员工观看。**

科技创业者、软件开发公司 XMTP Labs 的 CEO Shane Mac 决定把 Grok Bot 连接到他的个人银行账户。

令人费解的是，Grok Bot 把他的财务信息和银行余额发到了公司的 Slack 频道。更糟的是，Grok Bot 是在冒充 Mac 的情况下泄露这些信息的。

Mac 分享的截图显示一份「每月财务审计」，其中包含健身房会员、装修和信用卡还款等个人支出。

尽管 Mac「不好意思分享」自己曾是泄露个人信息的关键一环，他还是详细说明了自己如何陷入这种情况，以便其他人能「小心主动型智能体（proactive agents）的阴暗面」。

## 他为什么把 Grok Bot 连接到银行？

这位忙碌的 CEO 兼科技创业者设置了一个智能体来管理个人财务。看起来像是一个随意的 CFO 设置，用来帮他了解自己的支出。

「我真的很好奇它能不能就帮我盯着这些事情，」Mac 说。

随后一位队友提醒他，他的银行信息和交易记录对公司可见。作为一家科技公司的 CEO，这可不怎么好看。

Mac 为自己让一个自主智能体访问财务数据的决定辩护，因为 Grok Bot 本应是只读的、特定的，而且没有对其他应用的明确访问权。

他不知道的是，Grok Bot 的智能体都在一起工作。

广告

## 这位 CEO 没有读细则

「我为什么连接我的银行？它是只读的，这个特定的 Grok Bot 智能体没有 Slack。但另一个有。结果发现，它们全都连在一起。」

虽然 Mac 只设置了一个管理个人财务的智能体，但他声称另一个智能体——大概是处理 Slack 通信的那个——正在与他个人的 CFO 智能体通信。

根据 [SpaceXAI](https://x.ai/news/introducing-grok-bot) 的说法，Grok Bot 的智能体被设计为「登录并跨应用、工具和网站工作，包括没有现成 API 或 MCP 的平台，并带着完成的工作回来」。

Grok Bot 的吸引力之一在于，这些智能体都在一台基于云的计算机上工作。

这虽然有用，也带来了 Mac 所面对的那类问题，因为所有智能体共用一台计算机，因此彼此并不完全独立。

SpaceXAI 特别指出：「计算机分配给你的用户账号，而不是单个 Bot。如果你的账号上另一个 Bot 不应能使用某项凭证或文件，就不要把它放在上面。」

## 但 Musk 承诺过……

Grok Bot 于 2026 年 8 月 11 日发布，是一组「始终在线」的智能体，被分配任务并独立完成。

其吸引力在于，Grok Bot 像一个单独的同事那样运作，这意味着用户不需要手动创建供 AI 智能体遵循的工作流或例程。

用户只需像给人类同事发消息一样给他们特定的 Bot 发消息，Bot 就会完成。

Grok Bot 最初是为 SpaceXAI 内部使用而创建的，让 AI 智能体处理对外销售、市场活动、办公运营和缺陷修复等事务。

发布大约一周后，X 上一个支持 Musk 的账号讨论是否要把自己的银行账户连接到 Grok Bot，尽管其女友强烈反对。

Musk 回应说「试试看」，并说不用担心「Grok Bot 搞砸了，我们会补偿你」。

Mac 把这话套到自己身上，承认「Elon 甚至说过把你的银行账户连接到 Grok Bot，并承诺如果它弄丢了我们的钱，会补偿我们」。
