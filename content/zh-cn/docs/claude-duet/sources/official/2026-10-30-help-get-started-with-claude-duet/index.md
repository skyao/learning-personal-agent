---
title: "Claude Duet 入门"
linkTitle: "帮助：入门"
date: 2026-10-30
originalTitle: "Get started with Claude Duet"
sourceUrl: "https://support.claude.com/en/articles/17631495-get-started-with-claude-duet"
altUrls: ["https://support.claude.com/zh-CN/articles/17631495-开始使用-claude-duet"]
author: "未署名"
publisher: "Anthropic"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "帮助文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-30T17:08:13Z）"
tags: [开放与价格, 持续执行, 记忆与上下文, 安全]
products: [claude-duet]
---

{{< source-info >}}

**收录说明**：直接下载。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：帮助中心的入门文档，覆盖使用条件、工作方式、加入候补名单、连接应用、局限、价格与用量、隐私与安全。使用条件为 Pro、Max 或 Ultra 套餐、美国的 Claude 账号和候补名单邀请，Team 与 Enterprise 计划以后再支持。它沿用 Claude 账号的记忆、技能和连接器，在云端自己的计算机上工作，有 Tasks 标签页跟踪任务，并可搜索用户在 Claude 中的历史对话（受同一设置控制）。局限包括：不能选模型（固定 Claude Opus 5.5，自行决定投入多少推理）、不能观看或接管其浏览器、按固定间隔检查账号、不打电话不发短信、部分操作即使批准也不允许、Microsoft 365 暂不可用。用量与 Claude 聊天按同等费率计入五小时和每周限额，晨报和检查等后台工作也计入；获准加入预览时可获得一次完整的限额重置，有效期至 2026-11-30。

**保留理由**：列出了发布文中没有的具体限制（不能选模型、不能看浏览器、不能打电话发短信、Microsoft 365 不可用）和用量计算规则，是 Claude Duet 当前能力边界的官方依据。

---

**[Claude Duet](https://claude.com/product/claude-duet)** 是 Claude 的研究预览（research preview），你可以像给一个人发消息那样给它发消息。用文字或语音告诉它你需要什么，它就会在你已连接的应用中工作，在有事需要你处理时通知你，并且被设计为在发送消息、付款、签署文件或删除任何内容之前先征求你的同意。本文介绍 Claude Duet 能做什么、谁可以获得访问权限、如何加入候补名单，以及它目前还做不到什么。

Claude Duet 以研究预览形式向美国的 Pro、Max 和 Ultra 套餐用户开放，需通过候补名单（waitlist）。它使用你的 Claude 账号设置和你的套餐用量限额（usage limits）。它暂不支持 Team 或 Enterprise 套餐，我们计划稍后将其引入这些套餐。访问权限分批开放，功能在研究预览期间可能变化。

## 谁可以获得访问权限

要使用 Claude Duet，你需要：

- Pro、Max 或 Ultra 套餐
- 美国的 Claude 账号
- 候补名单的邀请

## 为什么你可能还没有访问权限

- 邀请分批发出，因此加入候补名单并不保证具体日期。
- 研究预览期间，Claude Duet 仅在美国提供。
- Claude Duet 暂不支持 Team 或 Enterprise 套餐。
- 你在候补名单中使用的电子邮箱与你的 Claude 账号不一致，或与你手机上的 Google 或 Apple 账号不一致。访问权限与你提供给我们的电子邮箱绑定。

## Claude Duet 如何工作

Claude Duet 在你的 Claude 账号上运行，因此你在 Claude 中设置的记忆（memory）、技能（skills）和连接器（connectors）从第一条消息起就已就位。它在云端的自己的计算机上工作，因此你关闭应用后它仍可继续工作。

- **像给人发消息一样给它发消息。** 输入消息或录制语音消息。你的主线程集中在一处，因此 Claude Duet 会从你上次停下的地方继续。你也可以为不同主题开启独立的频道（channels），它们共享同一份记忆。
- **以简报开启一天。** 每天早晨，它会查看你的电子邮件和日历，挑选出最需要你关注的事项，并可以启动最初的几步，例如起草回复供你审阅。一天中，它会发送正在进行的工作的更新，并对已经沉寂的线程进行跟进。
- **交给它更大的任务。** 描述你需要什么，它会判断该使用哪些应用以及这项任务需要多少投入。更大的成果会以你可以审阅和编辑的文件形式返回，例如研究简报、财务模型、幻灯片或仪表盘。完成的工作会出现在 **Make**（制作）标签页中。
- **添加插件。** Claude Duet 支持插件（plugins），例如小企业插件，并可以推荐适合你工作的插件。
- **在没有连接器的网站上工作。** 对于没有连接器的网站，Claude Duet 使用它在云端的自己的浏览器。

### 示例请求

- 「清理我收件箱里所有我不需要读的内容。」
- 「检查 Stripe 中的未付发票，并起草提醒邮件供我批准。」
- 「在下午 2 点会议前整理一份关于这家公司的简报。」

### 跟踪任务

**Tasks**（任务）标签页显示 Claude Duet 正在做什么，并突出显示需要你输入的任务。你的主线程会更安静：当任务完成或需要你做出决定时，Claude Duet 才会在那里发消息。它可能会提示某个任务看起来已经完成，但只有你才能把任务标记为已完成。

## 加入候补名单并获取应用

1. 前往 **[Claude Duet 产品页面](https://claude.com/product/claude-duet)**，选择「Join the waitlist」（加入候补名单）。
2. 输入你的姓名和电子邮箱。如果你已经在使用 Claude，请输入你 Claude 账号对应的电子邮箱。
3. 选择你的 Claude 套餐和手机类型（iPhone 或 Android）。你也可以告诉我们你从事什么工作，以及你会首先把什么交给 Claude Duet。
4. 选择「Submit」（提交）。我们正在逐步添加人员，轮到你会收到一封电子邮件。
5. 轮到你时，在手机上打开邀请邮件，并按照 iPhone 或 Android 的设置步骤操作。请使用与你提供给我们的电子邮箱关联的 Apple 或 Google 账号，因为访问权限与该邮箱绑定。
6. 打开 Claude Duet，用你的 Claude 账号登录。接受邀请后，应用可能需要几分钟才能可用。

## 连接你的应用

Claude Duet 可以使用你已在 Claude 中连接的应用。你可以在 Claude 设置中管理访问权限。它适用于你在 Claude 中连接的连接器，例如 Gmail、Google Calendar、Google Drive、Slack、QuickBooks、HubSpot、Docusign 和 Calendly。每个连接都由你自己发起，你可以随时断开任何应用。断开某个应用会从那一刻起停止 Claude Duet 访问它，但此前对话中关于过往信息的记忆会被保留。

进一步了解 **[使用连接器](https://support.claude.com/en/articles/11176164)**。

### 合作伙伴集成

Claude Duet 还可与少数合作伙伴服务配合使用：

- **Stripe：** 检查你的 Stripe 账号中的未付发票，并起草提醒邮件供你批准。这使用 Stripe 连接器，它与 Link 是分开的。
- **Link：** 使用 Link（Stripe 的数字钱包）为你批准的购买付款。进一步了解 **[如何在 Claude Duet 中使用 Link by Stripe](https://support.claude.com/en/articles/17666484)**。
- **Shop Pay：** 使用 Shop Pay（Shopify 的钱包）为你批准的购买付款。进一步了解 **[如何在 Claude Duet 中使用 Shop Pay](https://support.claude.com/en/articles/17666489)**。

Claude Duet 被设计为在每次购买前征求同意，并且每次购买都使用一张仅对该次购买有效的一次性卡（one-time card）。Link 和 Shop Pay 目前仅在 Claude Duet 中可用，并且你是在 Claude Duet 中连接它们，而不是在连接器目录中。

### 搜索你的历史对话

Claude Duet 可以搜索你的历史对话，以获取此前工作的上下文，这样你就不必重复自己。它会搜索你的 Claude Duet 对话以及你在项目之外的 Claude 对话。当你删除某个对话时，它也会从搜索中移除。

这使用与 Claude 相同的 **[搜索与引用对话（Search and reference chats）](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context#h_a11816bb20)** 设置。要阻止 Claude Duet 搜索你的历史对话，请在 **Settings > Your Claude**（设置 > 你的 Claude）中关闭 **Search and reference chats**（搜索与引用对话）（在旧版设置布局中为 **Settings > Memory**）。

## 局限

研究预览期间，请注意以下限制：

- 你无法选择模型。Claude Duet 运行在 Claude Opus 5.5 上，并自行决定一项任务需要多少投入。
- 你无法观看 Claude Duet 在其浏览器中工作，也无法接管该浏览器。
- 它按固定间隔检查你的账号，因此紧急事项可能在两次检查之间到来。
- 它看不到你的全部项目或你计算机上的文件，它可以读取你在 Claude 中的工作，但无法修改。
- 它不会给其他人打电话或发送短信。经你批准，它可以从你已连接的账号发送电子邮件。
- 某些操作即使经你批准也不允许，例如买卖证券、在账户之间转移资金或访问他人的账号。
- 某些连接器（例如 Slack）在 Claude Duet 中有限制地工作。Microsoft 365 暂不可用。

Claude Duet 也可能出错，例如误读某个线程或误判什么紧急。确认草稿和审批请求之前请先审阅。

## 价格与用量限额

**价格。** 研究预览期间，Claude Duet 包含在 Pro、Max 和 Ultra 套餐中，不另收费。

**用量限额。** Claude Duet 使用你套餐的用量限额，包括任何五小时会话限额和你的每周限额，费率与 Claude 中的聊天相同。它在后台进行的工作，例如晨报和例行检查，也计入，因此你可能比只用聊天更早达到限额。Claude Duet 按固定间隔检查你的账号，以避免这些后台工作耗尽你的限额。进一步了解 **[用量限额](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work#h_673be3815f)**。

**限额重置。** 当你获准加入 Claude Duet 研究预览时，你会获得一次完整的限额重置，它会同时重置你的五小时会话限额和每周限额。此限额重置有效期至 2026 年 11 月 30 日。进一步了解 **[限额重置](https://support.claude.com/en/articles/17007452-what-is-a-limit-reset)**。

## 隐私、安全与控制

Claude Duet 被设计为向你展示它即将做什么，并在发送消息、付款、签署文件或删除任何内容之前等待你的批准。如果你无法立即批准，Claude Duet 会完成任务的其余部分，并在稍后把审批带回给你。当它给你一个数字或一份摘要时，它会告诉你这来自哪封电子邮件、哪个文件或哪张电子表格。

Claude Duet 会读取他人撰写的内容，例如电子邮件和网页，而这些内容可能包含意在误导它的指令。这被称为*提示词注入（prompt injection）*。Claude Duet 被构建为把它读到的内容当作信息，并按照你的要求行事，但没有任何防护是完美的，这也是重要操作需要你批准的原因之一。

在其浏览器中，Claude Duet 力求遵守网站为智能体设定的规则。当网站要求输入密码时，你在自己设备上的单独表单中输入。该表单会将它直接发送到浏览器，浏览器被设计为让它不进入你与 Claude Duet 的对话。

## 使用 Link 和 Shop Pay 购买

遇到购买问题时去哪里寻求帮助取决于具体问题：

- **订单状态、配送、退货或商品退款：** 联系你购买商品的商店。
- **Link 扣款或 Link 账号问题：** 在 Link 应用中选择「Get help」（获取帮助），或访问 **[Link 支持](https://support.link.com/topics/link-agent-wallet)**。
- **Shop Pay 扣款或 Shop Pay 账号问题：** 联系 **[Shop 支持](https://help.shop.app/en/shop/report-issue/contact-the-shop-support-team)**。
- **Claude Duet 选择了与你意图不同的商品、商店或选项：** 联系我们。进一步了解 **[如何获得支持](https://support.claude.com/en/articles/9015913-how-to-get-support)**。

## 发送反馈

你可以直接在对话中通过用平实的语言告诉 Claude Duet 发生了什么来发送反馈或报告任何问题，它会将你的报告转达给我们的团队。
