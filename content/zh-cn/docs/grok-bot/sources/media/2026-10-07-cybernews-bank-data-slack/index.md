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
translation: 待翻译
collectedAt: 2026-11-05
updatedAt: "2026-10-08"
dateNote: "原站拒绝自动访问，依据 Wayback 快照 20261021011052"
tags: [安全, 隐私, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：原站拒绝自动访问，原文依据 Internet Archive 快照（20261021011052）存档；去掉了文首由 nexos.ai 生成的「Key takeaways」要点框、文中插入的「More from Cybernews」推荐和作者简介。Techdirt 2026-10-19 的评论文章转述的就是这篇报道，未另收。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

**收集者摘要**：XMTP Labs 的 CEO Shane Mac 把 Grok Bot 连接到个人银行账户，用作只读的财务助理，结果另一个 Grok Bot 以他的身份把银行余额和支出明细发到了公司 Slack 频道。Mac 称管财务的那个 Bot 没有 Slack 权限，但另一个有，「Turns out, they're all connected」。文章指出同一账号下的所有 Bot 共用一台云端计算机，并引用 SpaceXAI 的说明：计算机分配给用户账号而非单个 Bot，不要把凭证或文件放在其他 Bot 能用到的地方。文末提到 Musk 此前曾在 X 上回复用户可以连接银行账户，「Grok Bot messes up, we will make you whole」。

**保留理由**：一起真实发生的跨 Bot 数据泄露事件，直接说明了「多个 Bot 共用一台计算机、按用户而非按 Bot 隔离」这一设计的后果，可与官方安全文档对照。
