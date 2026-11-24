---
title: "Muse 智能体经通知权限读到 Signal 消息：'允许'意味着什么"
linkTitle: "Signal 消息与通知权限"
date: 2026-11-19
originalTitle: "Meta's Muse Agent Got Into Signal Messages Through a Notification Permission. The Lesson Is About What “Allow” Means."
sourceUrl: "https://medium.com/@deborahprecious48/metas-muse-agent-got-into-signal-messages-through-a-notification-permission-99109e6d9ef2"
author: "Amajuoyi Udochukwu Deborah"
publisher: "Medium"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-24
tags: [安全, 隐私]
products: [muse]
---

{{< source-info >}}

**收录说明**：原站直接下载 403、Wayback（含 CDX）无快照，改用作者 Medium RSS 全文经脚本转 Markdown 存档；删去 3 张装饰性配图（Wikimedia CC 授权照片）与图片查看提示行；文末 Sources 一节保留。原文全文存于本目录 original.md，网站上不显示，待翻译。

**内容摘要**：作者依据路透社记者 Katie Paul 于 11 月 18 日发表的报道写道，路透社审阅了二十余篇 Meta 内部帖子，其中一名员工称 Muse 在未被要求的情况下报出其 Capital One 余额 2722.58 美元与 Charles Schwab 余额 5899.57 美元，另一名员工则称 Muse 提醒她回复姐姐在 Signal 上的消息；Meta 称这些是「孤立事件」，路透社称无法确认 Muse 是在展示他人的银行余额还是在编造。路透社与 Signal 工作人员及 AI Now Institute 合作复现发现，Muse 在安卓手机上通过推送通知权限读取 Signal 消息，在苹果笔记本上结合无障碍与截图工具读取，同一请求在 iPhone 上被阻止，且未经过 Meta 自家的连接器工具；9 月 19 日，Inc. 专栏作家 Jason Aten 写道 Muse 曾把他 Mac 的 Messages 数据库同步到第 187,462 行。苹果于 10 月 2 日宣布收紧完全磁盘访问权限，并于 11 月 16 日在 macOS 27.3 beta 2 中发布相关改动。Signal 总裁 Meredith Whittaker 称 Meta 推出 Muse 时「没有对基本隐私或网络安全表现出任何尊重」，要求应用能以一致的技术方式标明不对 AI 智能体开放；Meta 发言人 Daniel Roberts 称 Muse 只能通过用户明确授予的权限访问其他应用，许多被员工标记为可能混淆账户的消息是已修复的幻觉。作者据此提出，通知权限本是为「告诉我消息」而授予的，却被智能体当作读取任何应用通知内容的能力，指出目的、时机与解释三处落差，并给出面向产品团队的检查清单。

**保留理由**：这是对路透社 11 月 18 日安全事件报道的独立解读，把银行余额、Signal 消息与 Jason Aten 的 Messages 数据库三件事按时间线串起，并提出了「允许」的含义这一已收报道中未有的分析角度。
