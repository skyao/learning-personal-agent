---
title: "用脚步取代 cron：我如何把 Grok Bot 的额度消耗降了一半"
linkTitle: "Timeline：脚步省额度"
date: 2026-11-23
originalTitle: "How footsteps cut my Grok Bot quota burn by 50%"
sourceUrl: "https://timeline.place/guides/footsteps-instead-of-cron"
author: "Marcel Marais"
publisher: "Timeline"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
dateNote: "日期取页面元数据的发布日期"
tags: [持续执行, 实测评测]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：直接下载；去掉了作者头像和文首、文末的 Timeline 下载推广框，以及文末的「More guides」列表。作者与「Grok Bot symbiosis」相同，文中的事件来源是自家产品，也提到 Home Assistant、OwnTracks 等替代方案。标题写 50%，正文数据为 568 次降到 274 次（52%）。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：作者的例行任务每周唤醒 VM 近 600 次，周四 15:20 周额度耗尽。改为按所在位置而非时钟驱动后，每周后台运行从 568 次降到 274 次，减少 52%，周日晚间仍剩 40% 以上额度。做法是手机的到达与离开事件只更新 VM 上的 `/state/presence.json`（不消耗 token），各轮询任务由一个 shell 包装脚本在模型之外先检查位置与租约，不符则直接退出；办公室的 Slack 与 GitHub 检查为 45 分钟租约，在家的浏览器检查为 2 小时租约。作者也承认几项不足：手机没电收不到离开事件、在家办公要手动切换、访问检测太慢不能开门、一次性监视任务容易忘记设过期。

**保留理由**：给出 Grok Bot 后台运行消耗周额度的量化数据和把门控放在模型之外的具体做法，是少见的用量实测。
