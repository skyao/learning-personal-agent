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
collectedAt: 2026-11-28
updatedAt: 2026-11-26
dateNote: "帮助文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-30T17:08:13Z）；2026-11-10 发现原文更新，按新版覆盖原文存档：每个新用户的额度重置次数改为按套餐区分（Pro 三次，Max 与 Ultra 一次），有效期改到 2026-12-15，另说明 Claude Duet 中不提供 Personal Finance；旧译文对应 11-05 版，已移除，2026-11-10 按新版重新翻译；2026-11-28 发现原文更新（结构化数据 dateModified 为 2026-11-26T19:10:50Z），按新版覆盖原文存档：开放地区由美国扩大到美国、印度、印度尼西亚、巴西和日本，邀请可来自候补名单或现有 Claude Duet 用户，「暂不支持」只剩 Enterprise（不再提 Team），删去「Microsoft 365 暂不可用」一句；旧译文对应 11-10 版，已移除，已重新翻译"
tags: [开放与价格, 持续执行, 记忆与上下文, 安全]
products: [claude-duet]
---

{{< source-info >}}

**收录说明**：直接下载。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：帮助中心的入门文档，覆盖使用条件、工作方式、加入候补名单、连接应用、局限、价格与用量、隐私与安全。使用条件为 Pro、Max 或 Ultra 套餐、美国、印度、印度尼西亚、巴西或日本的 Claude 账号，以及来自候补名单或现有 Claude Duet 用户的邀请，Enterprise 计划以后再支持。它沿用 Claude 账号的记忆、技能和连接器，在云端自己的计算机上工作，有 Tasks 标签页跟踪任务，并可搜索用户在 Claude 中的历史对话（受同一设置控制）。局限包括：不能选模型（固定 Claude Opus 5.5，自行决定投入多少推理）、不能观看或接管其浏览器、按固定间隔检查账号、不打电话不发短信、部分操作即使批准也不允许。用量与 Claude 聊天按同等费率计入五小时和每周限额，晨报和检查等后台工作也计入；研究预览期间按套餐发放完整的限额重置（Pro 三次，Max 与 Ultra 一次），由用户自行选择使用时机，未用的于 2026-12-15 过期；Claude Duet 中不提供 Personal Finance。

**保留理由**：列出了发布文中没有的具体限制（不能选模型、不能看浏览器、不能打电话发短信、Microsoft 365 不可用）和用量计算规则，是 Claude Duet 当前能力边界的官方依据。

---

**[Claude Duet](https://claude.com/product/claude-duet)** 是 Claude 的研究预览版，你可以像给一个人发消息那样与它对话。用打字或语音告诉它你需要什么，它会在你连接的应用中工作，有事情需要你处理时通知你，并且在发送消息、付款、签署文件或删除任何东西之前，它的设计是先征求同意。本文介绍 Claude Duet 能做什么、谁能获得访问权限、如何加入候补名单，以及它目前还做不到什么。

作为研究预览版，Claude Duet 通过候补名单提供给美国、印度、印度尼西亚、巴西和日本使用 Pro、Max 和 Ultra 套餐的用户。它沿用你的 Claude 账号设置和你的套餐用量限额。它目前不支持 Enterprise 套餐，我们计划稍后把它带到这些套餐。访问权限分批开放，研究预览期间功能可能变化。

## 谁能获得访问权限

要使用 Claude Duet，你需要：

- Pro、Max 或 Ultra 套餐
- 一个位于美国、印度、印度尼西亚、巴西或日本的 Claude 账号
- 来自候补名单或某位 Claude Duet 用户的邀请

## 为什么你还没有访问权限

- 邀请分批发出，所以加入候补名单并不保证某个具体日期。
- 研究预览期间，Claude Duet 只在美国、印度、印度尼西亚、巴西和日本提供。
- Claude Duet 目前不支持 Enterprise 套餐。
- 你在候补名单上填的邮箱地址与你的 Claude 账号不一致，或与你手机上登录的 Google 或 Apple 账号不一致。访问权限与你在候补名单上提供的邮箱地址绑定。

## Claude Duet 如何工作

Claude Duet 在你的 Claude 账号上运行，所以你在 Claude 中设置好的记忆、技能和连接器，从第一条消息起就可以使用。它运行在一块属于自己的云端计算机上，所以你关闭应用后它仍能继续工作。

- **像给人发消息一样给它发消息。** 输入消息或录制语音消息。你的主线程集中在一处，所以 Claude Duet 能接着你上次的地方继续。你也可以为不同话题分别建立频道（channel），它们共享同一份记忆。
- **用一份简报开始新的一天。** 每天早上，它会翻看你的邮件和日历，挑出最需要你注意的事，并能开始第一步，比如起草回复供你审阅。一天当中，它会发送关于正在进行的工作的更新，并跟进已经沉寂下来的线程。
- **把更大的活儿交给它。** 描述你需要什么，它会判断该用哪些应用、这项工作要投入多少精力。较大的成果以文件形式返回，你可以审阅和编辑，例如研究简报、财务模型、幻灯片或仪表盘。完成的工作出现在 **Make** 标签页。
- **添加插件（plugin）。** Claude Duet 支持插件，例如小企业插件，并能推荐适合你工作的插件。
- **没有连接器的网站也能用。** 对于没有连接器的网站，Claude Duet 使用它在云端的自有浏览器。

### 请求示例

- 「把我收件箱里不需要读的东西都清掉。」
- 「查一下 Stripe 里有哪些未付发票，起草催款邮件让我批准。」
- 「在我下午 2 点的会议之前，整理一份关于这家公司的简报。」

### 跟踪任务

**Tasks**（任务）标签页显示 Claude Duet 正在做什么，并高亮需要你输入的任务。你的主线程会更安静：任务完成或需要你决定时，Claude Duet 才会在那里发消息。它可以提示某个任务看起来已完成，但只有你才能把任务标记为完成。

## 加入候补名单并获取应用

1. 前往 **[Claude Duet 产品页](https://claude.com/product/claude-duet)**，选择「Join the waitlist」（加入候补名单）。
2. 输入你的姓名和邮箱地址。如果你已经在用 Claude，填你 Claude 账号上的邮箱地址。
3. 选择你的 Claude 套餐和手机类型（iPhone 或 Android）。你也可以告诉我们你的工作内容，以及你最想先交给 Claude Duet 做什么。
4. 选择「Submit」（提交）。我们会逐步添加用户，轮到你了会收到邮件。
5. 轮到你时，在手机上打开邀请邮件，按 iPhone 或 Android 的设置步骤操作。请使用与你提供的邮箱地址关联的 Apple 或 Google 账号，因为访问权限绑定在该地址上。
6. 打开 Claude Duet，用你的 Claude 账号登录。接受邀请后，应用可能需要几分钟才能使用。

## 连接你的应用

Claude Duet 可以使用你已在 Claude 中连接的应用。你可以在 Claude 设置中管理访问权限。它可与你已在 Claude 中连接的连接器配合工作，例如 Gmail、Google Calendar、Google Drive、Slack、QuickBooks、HubSpot、Docusign 和 Calendly。每个连接都由你主动建立，你也可以随时断开任何应用。断开某个应用后，Claude Duet 从那一刻起无法再访问该应用，但来自早先对话的过往信息所形成的记忆会保留。

进一步了解**[使用连接器](https://support.claude.com/en/articles/11176164)**。

### 合作伙伴集成

Claude Duet 还可与几项合作方服务配合使用：

- **Stripe：** 查看你 Stripe 账号中的未付发票，起草催款邮件供你批准。这里用的是 Stripe 连接器，与 Link 是分开的。
- **Link：** 用 Link 支付你批准的购物。Link 是 Stripe 的数字钱包。进一步了解**[如何在 Claude Duet 中使用 Link by Stripe](https://support.claude.com/en/articles/17666484)**。
- **Shop Pay：** 用 Shop Pay 支付你批准的购物。Shop Pay 是 Shopify 的钱包。进一步了解**[如何在 Claude Duet 中使用 Shop Pay](https://support.claude.com/en/articles/17666489)**。

Claude Duet 的设计是在每次购买前征求同意，每次购买都使用一张只对该次购买有效的一次性卡。Link 和 Shop Pay 目前仅在 Claude Duet 中提供，并且你是在 Claude Duet 中连接它们，而不是在连接器目录中。

### 搜索你过去的聊天

Claude Duet 可以搜索你过去的聊天，接续早先工作的上下文，这样你不必重复说明。它搜索你的 Claude Duet 聊天，以及你在项目之外的 Claude 聊天。你删除某个聊天后，它就会从搜索中移除。

这使用与 Claude 相同的**[搜索和引用聊天](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context#h_a11816bb20)**设置。要阻止 Claude Duet 搜索你过去的聊天，在**设置 > Your Claude**（旧版设置布局中为**设置 > Memory**）中关闭**搜索和引用聊天**。

## 局限

研究预览期间，请留意这些限制：

- 你不能选择模型。Claude Duet 运行在 Claude Opus 5.5 上，由它决定一项工作需要投入多少精力。
- 你不能观看 Claude Duet 在其浏览器中工作，也不能接管该浏览器。
- 它按固定间隔检查你的账号，所以紧急的事情可能在两次检查之间到来。
- 它看不到你所有的项目，也看不到你电脑上的文件；它能读取你在 Claude 中的工作，但不能修改。
- 它不打电话，也不向他人发送短信。经你批准，它可以从你已连接的账号发送邮件。
- 有些操作即使你批准也不允许，例如交易证券、在账户之间转账，或访问他人的账号。
- 有些连接器（例如 Slack）在 Claude Duet 中使用时有限制。
- Claude Duet 中不提供 Personal Finance。

Claude Duet 也可能出错，例如误读一个线程，或误判什么算紧急。确认草稿和批准请求之前，请先审阅。

## 价格与用量限额

**价格。** 研究预览期间，Claude Duet 包含在 Pro、Max 和 Ultra 套餐中，不额外收费。

**用量限额。** Claude Duet 使用你套餐的用量限额，包括五小时会话限额和每周限额，费率与 Claude 中的聊天相同。它在后台做的工作（例如晨报和定时检查）也计入用量，所以你可能比只用聊天时更早达到限额。进一步了解**[用量限额](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work#h_673be3815f)**。

**限额重置。** 研究预览期间，我们会往你的账号里加入完整的限额重置，让你有空间试用 Claude Duet。你在网页版或 Claude Desktop 的 **[Settings > Usage](https://claude.ai/settings/usage)** 中选择使用时，每次重置会同时补满你的五小时会话限额和每周限额。能获得几次取决于你的套餐：

- Pro：三次限额重置
- Max 和 Ultra：一次限额重置

未使用的限额重置于 2026 年 12 月 15 日过期。进一步了解**[限额重置](https://support.claude.com/en/articles/17007452-what-is-a-limit-reset)**。

## 隐私、安全与控制

Claude Duet 的设计是向你展示它接下来要做什么，并在发送消息、付款、签署文件或删除任何东西之前等待你批准。如果你无法立刻批准，Claude Duet 会完成任务的其余部分，稍后把批准请求再带回给你。当它给你一个数字或一份摘要时，它会说明这来自哪封邮件、哪个文件或哪张电子表格。

Claude Duet 会读取他人写的内容，例如邮件和网页，这些内容里可能含有意在误导它的指令。这称为*提示注入*（prompt injection）。Claude Duet 被设计为把它读到的东西当作信息，并按照你的要求行事，但没有任何防御是完美的，这也是有后果的操作需要你批准的原因之一。

在其浏览器中，Claude Duet 力求遵守网站为 agent 设定的规则。当网站要求输入密码时，你在自己设备上单独的表单里输入。该表单会把密码直接发送给浏览器，浏览器的设计会使其不出现在你与 Claude Duet 的聊天中。

## 用 Link 和 Shop Pay 购物

遇到购买相关的问题时，去哪里求助取决于问题的类型：

- **订单状态、配送、退货或商品退款：** 联系你购买的那家商店。
- **Link 扣款或 Link 账号问题：** 在 Link 应用中选择「Get help」（获取帮助），或访问 **[Link 支持](https://support.link.com/topics/link-agent-wallet)**。
- **Shop Pay 扣款或 Shop Pay 账号问题：** 联系 **[Shop 支持](https://help.shop.app/en/shop/report-issue/contact-the-shop-support-team)**。
- **Claude Duet 选了你并不想要的商品、商店或选项：** 联系我们。进一步了解**[如何获得支持](https://support.claude.com/en/articles/9015913-how-to-get-support)**。

## 发送反馈

你可以直接在聊天中发送反馈或报告任何问题，用平实的语言告诉 Claude Duet 发生了什么，它会把你的报告转交给我们的团队。
