---
title: "我们如何设计 Grok Bot"
linkTitle: "设计 Grok Bot"
date: 2026-09-03
originalTitle: "Designing Grok Bot for a world of persistent agents"
sourceUrl: "https://x.ai/news/designing-grok-bot"
reprintUrl: "https://web.archive.org/web/20261009055356/https://x.ai/news/designing-grok-bot"
author: "未署名"
publisher: "SpaceXAI（xAI）"
language: en
fidelity: 转载全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "x.ai 对自动访问返回 403，依据 Wayback 快照 20261009055356；日期取页面结构化数据的 datePublished"
tags: [功能更新, 记忆与上下文, 持续执行, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：x.ai 对自动访问返回 403，原文依据 Internet Archive 快照存档；去掉了「Back to news」链接、下载与联系销售按钮和文末「Try Grok Bot today」推广区，视频改为一行链接。文中的界面示意图较多（70 张），图中界面文字随图片保存；超过 600 KB 的图片已缩小。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

**收集者摘要**：文章讲 Grok Bot 为了持久存在的智能体，把界面对象从聊天记录改成 Bot 名册：Bot 有名字、头像和头衔，会记住与用户的对话，并有自己的计算机和工具。产品只保留五个概念：Bots、Chats、Prompts、Tools、Artifacts。头像的动作承担状态显示（空闲、思考、工作、等待、阻塞、完成），悬停可看当前动作；Bot 的计算机分状态、预览、接管三级可见度。能力与上下文边界不同：工具和技能（Skills）在账号层面共享，记忆和例程（Routines）属于各个 Bot；群聊提供共享上下文，同时保留各 Bot 的专门记忆。例程可按时间表或事件触发，包括 issue、PR、Slack 消息、webhook 等，并移到 Bot 主界面；每个账号约 50 个 Bot、每个群聊 6 个 Bot 是实际设定的上限。

**保留理由**：这是最完整的产品设计说明，讲清了记忆归属、能力共享边界、计算机可见度和例程触发方式，是理解 Grok Bot 为什么按「长期存在的 Bot」而不是「会话」组织的主要依据。
