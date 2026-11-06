---
title: "文档（docs.x.ai）：在 X 上 @bot"
linkTitle: "docs.x.ai：在 X 上 @bot"
date: 2026-10-07
originalTitle: "Tag @bot on X"
sourceUrl: "https://docs.x.ai/grok-bot/tag-on-x"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-07T00:00:00Z）"
tags: [功能更新, 开放与价格]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 文档没有对应页。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：用户在 X 上发帖或回复时 @bot，就把这条帖子交给自己的主 Bot，在它的云端电脑上执行；X 上只回一句确认，结果留在 Grok Bot 的会话里。Bot 能读到用户的帖子、被回复的帖子和其中引用的帖子。前提是 Grok 账号已连接 X 账号、有 Grok Bot 权限、自己至少有一个 Bot。这项功能在澳大利亚、英国、欧盟、冰岛、列支敦士登和挪威不可用，按 X 记录的国家判断。帖子同时 @grok、含视频或 GIF、或用量已用尽时，@bot 不会回应。

**保留理由**：Grok Bot 独有的入口：从社交平台的公开帖子直接把任务交给个人智能体，并有地区限制。

---

在 X 上 @bot

在 X 的帖子或回复中标记 [@bot](https://x.com/bot)，就把那条帖子作为任务交给你的 Grok Bot。例如，回复一个讨论串：

> @bot 总结这个讨论串，并把要点发到我的 Slack

@bot 会在 X 上用一条简短回复确认你的 Grok Bot 已收到请求，然后你的主 Bot 开始在其云端计算机上工作。工作及其结果留在 Grok Bot 应用中该 Bot 的对话里；@bot 只在 X 上发布确认。

你的 Bot 会收到你的帖子、你回复的帖子，以及两者中任一所引用的任何帖子，包括静态照片。请求第一次通过时，X 会向你发送通知，说明带标记的请求会自动开始工作，并消耗你的 Grok Bot 用量。

## 开始之前

你需要：

* 一个已连接你的 X 账号的 Grok 账号。在 grok.com 上，打开 **Settings → Account**，在 **𝕏 Account** 旁选择 **Connect**。
* 同一个 Grok 账号上的 Grok Bot 访问权。从 [x.ai/bot](https://x.ai/bot) 下载应用；如果你的访问权来自 SuperGrok 订阅，按[开始使用](https://docs.x.ai/grok-bot/get-started#2-sign-in)中所述进行关联。
* 至少一个你自己的 Bot。别人与你共享的 Bot 不能接收带标记的请求。
* 一个位于标记功能可用地区的 X 账号。

X for Grok Bot 插件（plugin）是可选的。它让你的 Bot 搜索帖子、读取时间线、查看提及，并使用趋势和书签；无论有没有它，@bot 都会转发请求。关于 X 自己对 @bot 的说明，见 X 帮助中心的[关于 @bot](https://help.x.com/en/using-x/about-bot)。

## 标记功能在哪里可用

标记 @bot 对位于大多数国家的 X 账号有效。它尚不适用于位于澳大利亚、英国、欧盟、冰岛、列支敦士登或挪威的账号。

@bot 依据 X 记录的你的账号所在国家，因此你当前的位置和任何 VPN 都没有影响。如果 X 只为你的账号列出更宽泛的地区，例如「South Asia」，或完全没有国家，那么标记功能也尚不可用。在所有这些情况下，@bot 都不会回复。

## @bot 的回复意味着什么

| @bot 回复 | 含义 | 该怎么做 |
| --- | --- | --- |
| 一行短句，说它已把你的请求发给你的 Grok Bot | 你的主 Bot 已拿到任务。 | 打开 Grok Bot 跟进工作并审阅结果。 |
| 「Sign up for Grok Bot: https://x.ai/bot」 | 你发帖所用的 X 账号没有连接任何 Grok 账号。 | 在 grok.com 上连接你的 X 账号，设置 Grok Bot，然后再次标记 @bot。 |
| 「Grok Bot isn't set up yet. Open https://x.ai/bot」 | 你的账号已连接，但你还没有自己的 Bot。 | 打开 Grok Bot，创建一个 Bot，然后再次标记 @bot。 |

## 当 @bot 保持沉默

如果 @bot 不回复，说明你的 Bot 没有收到请求。常见原因：

* 你的 X 账号所在地区[尚不支持标记](#where-tagging-is-available)。
* 你在一个已经包含 @bot 的讨论串中回复，但你自己没有标记 @bot。
* 帖子还标记了 @grok。
* 帖子、它所回复的帖子或引用的帖子包含视频或 GIF。
* 帖子未通过内部审核。
* Grok Bot 未关联到你的 Grok 账号，或你的每周用量已用完。
