---
title: "指南：Grok Bot 入门 101"
linkTitle: "指南：Grok Bot 101"
date: 2026-09-11
originalTitle: "Grok Bot 101"
sourceUrl: "https://x.ai/bot/guides/grok-bot-101"
reprintUrl: "https://web.archive.org/web/20261017234251/https://x.ai/bot/guides/grok-bot-101"
author: "Matt Palmer"
publisher: "SpaceXAI（xAI）"
language: en
fidelity: 转载全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "x.ai 对自动访问返回 403，依据 Wayback 快照 20261017234251；日期取页面结构化数据的 datePublished"
tags: [实测评测, 运行环境, 安全, 连接器]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：x.ai 对自动访问返回 403，原文依据 Internet Archive 快照存档；去掉了「Back to news」链接、下载与联系销售按钮和文末「Try Grok Bot today」推广区，视频改为一行链接。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Matt Palmer 以 SpaceXSI 开发者关系岗位的使用方式介绍 Grok Bot：它是带云端计算机的智能体，有桌面、文件系统、终端和应用，可当远程桌面操作。Bot 的设置只有名称、头衔、描述三项；遇到验证码或 2FA 时把桌面交还给用户，也可发安全表单收密码或 API 密钥。权限用自然语言写在设置里，另有一个审查智能体对提议的动作选择允许、阻止或升级给用户；他提醒在一个 Bot 里登录的网站，其他 Bot 也能访问。他演示多 Bot 链、个人 CRM（用 Notion）、健身教练 Bot、用外层智能体给 Cursor 云端智能体写提示，以及跨 Slack、Notion、GitHub 的搜索。

**保留理由**：以第一人称写出实际搭建流程和日常用法，尤其是权限用提示而非代码配置、共享登录的说明，是理解个人用法的好材料。

---

Grok Bot 是一个带计算机的智能体（agent）。了解如何把它搭建起来、串联专家 Bot，并运行我实际使用的工作流。

---

![Grok Bot 入门](images/img-01-254631.img)

Grok Bot 是一个带计算机的智能体。

使用它就像给同事发消息，只不过这位同事有一台真实、持久的桌面。它能做你能做的事：使用应用、浏览网页、编写和运行代码。

我在 SpaceXSI 做开发者关系（DevRel）。我一天中的很多时间都在写代码、制作内容，或做典型的知识工作：传递信息、整理和规划。我以前会写一次性脚本、用编码智能体构建软件，或者把工作流拼凑起来。现在我把这些工作交给一个 bot。搭建一个只需 10 或 15 分钟。之后我可以调整它、复用它，并在我合上笔记本电脑后让它继续运行。

我录制了一段[演示](https://x.com/mattyp/status/2092286281266962681)，如果你想看看我是如何设置这些的。

## 什么是 Grok Bot？

Grok Bot 是一个可以在计算机上执行任何操作的个人助理。

这台计算机位于云端。它有桌面、文件系统、终端和应用。如果我点击 bot 的窗口，我就可以像使用远程桌面一样使用那台机器。bot 拥有和我相同的访问权限。

![Grok Bot 的云端计算机](images/img-02-57456f.img)Grok Bot 的云端计算机

因为它有一台真实的计算机，我可以通过录制任务或编写提示词来教它一个工作流。我让它查看 Costco 和 Amazon，把商品加入我的购物车，然后比较价格、运费和时间。

当某个流程需要我时，bot 可以像远程计算机那样把桌面交还给我。我来填写 CAPTCHA 或完成 2FA 登录。它也可以给我发送一个安全表单，用于输入密码或 API 密钥。

它也在云端运行，所以我在手机和桌面上得到的是同一台计算机。我的 Marketplace bot 可以在 Facebook 上搜索*斑叶 Monstera Albo*，因为 Facebook 已经处于登录状态。

## Bot 的解剖结构

我喜欢从语音笔记开始。bot 是一组指令，所以你可以按自己思考的方式定义它。

在幕后，设置是三个字段：

```
Name: Tech Demos
Title: Daily X tech scout
Description: Look at my bookmarks each weekday, pick one technology worth demoing, draft a prompt in my style, wait for approve or deny, then kick a Cursor cloud agent.
```

text

你可以在对话中或右上角的 Settings 中设置这些。

尽可能具体。像你自己会做的那样准确描述一个工作流，或者在屏幕上录制一段演示。然后假定这个 bot 能做 AI 通常做不到的难事。

![Bot 的解剖结构，Grocery](images/img-03-7e09e7.img)Bot 的解剖结构，Grocery

我把 Tech Demos 称为我的*开发者关系* bot。

每个工作日，它会在我 X 的书签中搜寻新技术，为一个原型起草提示词，并请我批准。

我调整提示词、批准它，bot 就会通过 Cursor 连接启动一个 Cloud Agent。我可以立即在 Cursor 中打开构建结果。

完成后，bot 会发送截图或一段视频片段，并打开一个 PR。

![Bot 设置](images/img-04-12e5e9.img)Bot 设置

Grok Bot 支持与 Cursor 相同的 MCP 服务器、插件和技能。我接了 Gmail、Google Calendar、Google Drive 等。每个服务可以连接多个账号，所以我可以查看个人和工作电子邮件，或检查多个 Slack。

如果你想知道自己能不能做某件事，问它。

## 使用 Grok Bot

有三种方式与 bot 交流。

1. **聊天（Chat）：** 给它发一条消息。
2. **例程与触发器（Routines and triggers）：** bot 可以设置自己的时间表，或监听来自其他应用的事件。它可以监视一个 Slack 线程或一个 GitHub PR。
3. **其他 bot：** bot 之间可以互相发消息、互相触发。

![例程与触发器](images/img-05-c1809d.img)例程与触发器

## 权限与共享计算机

如果你在智能体可以使用的计算机上登录 Amazon，从技术上讲，它就能买任何它想买的东西，就像人一样。

Bot 受到权限、一个审查者（reviewer）以及允许/阻止列表的约束。你在 Settings > General > Agent 中用自然语言编写规则。一个独立的审查智能体会检查提议的动作，并可以允许、阻止或升级给你。允许和阻止列表会引导该审查者。你是在信任模型遵循你写下的内容。工作仍在隔离环境中进行。

我们大多数人习惯用代码或 JSON 定义智能体规则。在 Grok Bot 中，规则就是一段提示词。

![允许和拒绝规则](images/img-06-22061a.img)允许和拒绝规则

还有一点：如果你用某个 bot 登录了一个网站，其他每个 bot 也都能访问那个网站。

## 多 Bot 链

我把 bot 当作专家。因为它们可以互相交流，一个专家可以向另一个求助。

你可以把几个放进一个群聊。一个工作日例程可以把请求依次交给不同的 bot，直到任务完成。

我的 Marketplace bot 在 Facebook Marketplace 和 Craigslist 上留意浓缩咖啡机。

当它需要做判断时，它可以问我的 Chief of Staff bot。

![链中的 Marketplace bot](images/img-07-d5c362.img)链中的 Marketplace bot

## 我喜欢的四个 Bot 工作流

**个人 CRM**

我在手机上用 10 到 15 分钟搭好了它。

提示词是：把我已经在 X 上关注的人变成一个位于 Notion 的私人个人 CRM，只使用公开的个人资料信息。

我大约关注了 800 到 900 人。这个看板包含头像、描述，以及每个公开个人资料的返回链接。

我出差时，可以用它和我已经认识的人重新联系，问他们要不要一起喝杯咖啡。

我就是那个爱约咖啡的烦人家伙。

任何我会在 LinkedIn 或 X 上手动做的事，我都交给 bot。任何我会不好意思让实习生做的事，我也交给 bot。

![Notion 中的 X 关注者](images/img-08-1a4536.img)Notion 中的 X 关注者

**Arnold，我的健身 bot**

我已经有一个自己凭感觉写（vibe-coded）的力量训练应用。它花了几周的工作。它有用，但耗时，而且仍然经常坏。有一天我问：「如果这是一个 bot 会怎样？」

我把它搬进了对话。

**Arnold** 是我的力量和肌肥大训练计划教练。我通过和 Grok 聊天，把旧应用拆成了 MCP 服务器、技能和插件。

Grok Bot 从……Grok Bot 内部构建了这套基础设施。

核心功能相同，但最终状态精简得多：更少维护、更少 bug、零烦恼。

反馈循环也比旧应用更快。现在对逻辑或行为的更新只是和 bot 聊天：与使用应用本身相同的界面。

如果你能把一个应用分解为输入、逻辑和数据存储，你可能就能把它变成一个 bot。你可能会发现这比凭感觉写出来的软件更好的解决方案。

![Arnold，对话中的个人训练软件](images/img-09-9d4bdc.img)Arnold，对话中的个人训练软件

**用 Grok Bot 写代码**

我的外层循环（outer loop）智能体从 Slack、Notion、GitHub 和文档收集上下文，然后把干净的提示词交给 Cursor 云端智能体，由后者在内层循环（inner loop）中实际构建软件。

如果你让一个智能体读取文件、讨论要构建什么，然后立即委派修复，那个智能体会携带一堆脏上下文。

在「外层循环」中使用一个智能体，是把脏上下文挡在实际干活儿的「内层循环」执行者之外的一种方法。

我的这个智能体是 Cursor 代码库、文档和营销仓库的专家。它使用我的 Cursor 技能来写提示词，包括 Lauren 的 **pstack** 插件。

一个重要区别：Grok Bot 并不写代码。它是在创建*我会写的*那些提示词，然后把它们发送给位于 Cursor 内部的一个专用编码运行框架（coding harness）。

![外层循环接入 Cursor](images/img-10-7824f9.img)外层循环接入 Cursor

**跨 Slack、Notion、GitHub 搜索**

如果你的公司有 Notion、Slack 和一个 wiki，一边回邮件一边找东西是很难的。

我用 **Cursor Product Expert** 来回答产品问题以及公司如何运作的问题。

我经常问 Grok Bot，Grok Bot 是怎么工作的。它会阅读代码库、查看 Slack 上的讨论、浏览 Notion 中的设计文档，然后给我答案。

我现在问 Grok Bot 的问题比问同事的还多！这感觉很好，因为我可以尊重他们的时间，并减少 Slack 疲劳。

![跨 Slack、Notion、GitHub 搜索](images/img-11-56103f.img)跨 Slack、Notion、GitHub 搜索

### 接下来会怎样

Grok Bot 是一个在云端拥有计算机的智能体。它可以编写和运行代码、运行软件、执行工作流，并像我一样控制计算机。

与许多其他个人智能体相比，主要区别是零设置。越来越多的时候，我只需问 Grok Bot 就能复现一个工作流。

所以，我的创造不取决于 Grok Bot 能做什么，而取决于我能想象给它什么。试一试吧。我很期待看到你会构建什么。

—

作者：Matt Palmer
