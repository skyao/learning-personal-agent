---
title: "文档（docs.x.ai）：设置与通知"
linkTitle: "docs.x.ai：设置与通知"
date: 2026-10-28
originalTitle: "Settings and notifications"
sourceUrl: "https://docs.x.ai/grok-bot/settings-and-notifications"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：本地出口路由新增管理员锁定：Always off（强制走云端）与 Always on（强制转出，无已连接电脑时拒绝路由站点）；Usage & billing 重写为最多五段，新增 Resets（用量重置）与向 Bot 询问套餐和用量"
tags: [功能更新, 运行环境, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 上的同名页（2026-11-05 收入）与这页大约一半相同，这页是扩充后的版本，多出 Vault 一栏、记忆导入、Auto-review 规则和通知的说明，所以另收一篇。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：设置分 General、Computer、Vault、Usage & billing、Updates 几栏，没有模型选择器。General 里有记忆导入、时区（决定例程的调度时区）和 Auto-review 的自定义规则：个人规则只能比团队规则更严，冲突时 Ask first 优先。Computer 栏可让云端电脑的流量经用户桌面转出，目标网站看到的是用户的 IP；Enterprise 管理员可把它锁为 Always off（流量走云端）或 Always on（没有已连接的电脑时，Grok Bot 的电脑拒绝被路由的站点，不回退到云端）。Usage & billing 最多五段，依次为 My plan、Usage limits、Grok Bot usage、Additional usage、Resets；Use reset 可立即把每周用量清零，用户也可在与 Bot 的私聊中询问套餐和用量。桌面应用默认自动更新，只在屏幕锁定、空闲至少 10 分钟且 Bot 不忙时安装；Bot 需要用户输入时，若用户正在用桌面端则先在桌面提醒，约 3 分钟后才推送到手机。

**保留理由**：补充了设置项的较新版本，尤其是 Auto-review 规则的优先级和通知节奏，可以与 cursor.com 版对照看文档的变化。
