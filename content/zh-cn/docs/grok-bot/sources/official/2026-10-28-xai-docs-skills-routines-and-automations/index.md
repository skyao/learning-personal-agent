---
title: "文档（docs.x.ai）：技能与例程"
linkTitle: "docs.x.ai：技能与例程"
date: 2026-10-28
originalTitle: "Skills and routines"
sourceUrl: "https://docs.x.ai/grok-bot/skills-routines-and-automations"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-19
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：新增两点：团队成员可让 Bot 把技能只存给自己（Bot 日后被共享时技能随之共享）；Team Bot 的例程菜单新增 Who can use this routine?，可选 Only me 或 Everyone with access"
tags: [持续执行, 功能更新]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「例程」和 cursor.com 文档「Work」与这页部分重合。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：技能是跨 Bot 共享的私有库，可以发布给团队；团队成员也可以让 Bot 把技能只存给它自己，该 Bot 日后被共享时技能随之共享。Teach a task 可以录屏演示一个流程（最长 10 分钟、不录麦克风），生成技能草稿。例程可以按定时触发，也可以由 Slack、GitHub、Linear、Sentry、PagerDuty、邮件或 webhook 事件触发；在 Team Bot 上，例程菜单还可选 Only me 或 Everyone with access，决定例程只为自己运行还是为所有能使用该 Bot 的人运行。每个 Bot 最多 50 个例程，调度间隔至少 5 分钟，所有例程合计每小时最多运行 300 次、单个例程最多 200 次，超限不自动重试。新建例程不会立即运行，用 Test 试跑会真实执行并消耗用量；文档提醒高频例程一天就可能耗尽一周用量。

**保留理由**：给出了 Grok Bot 持续执行的触发方式和配额数字，可以和其他产品的定时、事件机制对照。

---

技能与例程

把一次成功的任务变成可重复的流程。Grok Bot 使用两个构件：

* **技能（skill）** 是一组可复用的指令，说明如何完成一项任务。
* **例程（routine）** 告诉某个 Bot 何时运行一个工作流：按时间表，或在某件事发生时，例如收到 Slack 消息，发生 GitHub、Linear、Sentry 或 PagerDuty 事件，收到邮件，或收到 webhook 调用。

从一次性任务开始。先让它可靠，把方法保存为技能，然后才自动化它。

## 保存技能

技能会记录步骤、决策规则、预期输出和安全边界。技能在你的各个 Bot 之间可用，不过 Bot 可能需要相应的应用或登录才能使用某个技能。

可以这样要求：

> Save the process we just used as a skill called "Weekly account health." Include the source systems, risk definitions, output format, and the rule that customer contact always requires approval.

（译注：意为「把我们刚用过的流程保存为一个叫『每周账户健康』的技能。包含来源系统、风险定义、输出格式，以及联系客户始终需要批准的规则。」）

一个有用的技能会写明：

1. 何时使用
2. 所需输入和访问权
3. 工作顺序
4. 如何验证结果
5. 返回什么
6. 什么需要批准

使用侧边栏中的 **连接应用（Connect apps）** 发现并安装受支持的应用和打包技能。要使用某个技能，按名称向 Bot 请求；用 `@` 引用 Bot、群组、例程和应用。

私有技能是你的所有 Bot 共用的一个库。如果 Bot 找不到某个私有技能，请打开侧边栏中的 **连接应用**，选择标题旁的已连接数量，然后在 **私有技能（Private skills）** 下为当前 Bot 启用它。

如果你在团队中，也可以让 Bot 把技能只保存给它自己。如果你之后分享那个 Bot，技能会随之共享。

### 与团队分享技能

如果你属于某个团队，可以发布私有技能，让队友也能使用。在桌面端，打开 **连接应用**，选择标题旁的已连接数量，然后打开该技能。在其标题栏中选择 **发布（Publish）**。如果你属于多个团队，在 **发布到（Publish to）** 下选择团队。

技能需要先有描述才能发布，因为队友和他们的 Bot 会用描述来判断何时适用。发布后，按钮显示 **已发布（Published）**。其菜单提供 **同步（Sync）**，把你之后的编辑推送到团队副本；还有 **复制链接（Copy link）** 和 **取消发布（Unpublish）**。

如果发布被拒绝，消息会说明原因：你需要先加入团队，或者你的团队管理员关闭了成员发布功能，此时请让管理员发布该技能。随应用或 Bot 模板附带的技能不能发布。

## 通过演示教一个工作流

当 **教一个任务（Teach a task）** 可用时，你可以演示一个浏览器工作流，而不必描述每一步。

1. 打开一个一对一 Bot 对话及其计算机视图。
2. 选择 **教一个任务**。
3. 描述你即将演示的结果。
4. 把工作流完整执行一次。
5. 停止录制，检查 Bot 创建的技能。
6. 在把它安排成例程之前，先用一个安全的例子测试。

教学会录制可见的计算机交互，最长十分钟。它不录制麦克风音频。演示期间避免暴露机密；凭证请使用安全交接流程。

学到的技能是一份草稿。请补充仅凭一个例子可能看不出来的决策规则、失败处理和审批边界。

演示教学可能逐步开放。如果看不到该控件，请让 Bot 根据书面指令和已完成的任务创建一个技能。

## 创建例程

向应当拥有这项重复工作的 Bot 提出：

> Every weekday at 8:00 AM, run the Daily customer-risk skill against the current account list. Post a linked watch list in this conversation. Do not contact customers. If the source data is unavailable, report the failure instead of using old data.

（译注：意为「每个工作日上午 8:00，对当前账户列表运行『每日客户风险』技能。在这个对话中发布一份带链接的观察清单。不要联系客户。如果来源数据不可用，报告失败，不要使用旧数据。」）

确认：

* 拥有该例程的 Bot
* 时间表和时区
* 输入来源
* 预期结果
* 审批边界
* 来源缺失时应该怎么做

Bot 会创建例程，它会出现在该 Bot 的例程中。例程在你的笔记本电脑合上时仍在云端运行。

在手机上，你也可以打开 Bot 的配置文件，在 **例程（Routines）** 下点击 **添加例程（Add routine）**。Grok Bot 会开始一条以「Set up a routine to」开头的消息；补完这句话并发送。

### 时间表与时区

时间表使用 **设置** 中 **Bot** 下的时区，标签为 **时区（Timezone）**。**自动检测（Auto-detect）** 跟随这台计算机。当例程应遵循另一个时区时，例如工作所属的办公室所在时区，请选择那个时区。

用平实的语言要求时间表，例如「每个工作日上午 8:00」或「每 2 小时」。然后打开例程并检查 **何时运行（When to run）**，它会用文字显示已保存的时间表。如果与你原本的意思不符，选择 **编辑（Edit）** 并告诉 Bot 要改什么。

新例程会等待下一个计划时间；创建时不会运行。如果你在 8:05 设置「每天上午 8:00」，第一次运行是明天上午 8:00。要马上试，请使用 **测试（Test）**。

## 由事件触发工作

例程可以在某件事发生时启动，而不是按时间表：收到 Slack 消息，发生 GitHub、Linear、Sentry 或 PagerDuty 事件，收到发往[Bot 自己的地址](https://docs.x.ai/grok-bot/computer-and-apps#give-your-bots-an-email-address)的邮件，或收到 webhook 调用。Cursor 账户集成会启动这些例程；它们与 [Slack](https://x.ai/bot/plugin/674) 或 GitHub 应用相互独立，可能需要单独连接。向 Bot 提出你想要的触发器；例程的 **何时运行** 会用文字显示它，例如「当创建 Linear 问题时」。只有新活动才算数：触发器存在之前的事件不会启动运行。

定义一条狭窄的匹配规则和一个明确的响应：

> When a message in `#customer-escalations` contains a support ticket link and the phrase "needs repro," open the ticket, reproduce the issue in staging, and post a repro pack in this conversation. Never post back to Slack without approval.

（译注：意为「当 `#customer-escalations` 中的消息包含支持工单链接和『needs repro』这句话时，打开工单，在预发环境复现问题，并在这个对话中发布一份复现包。未经批准绝不在 Slack 回帖。」）

避免「每条新消息」这类宽泛监听。它们会制造噪音、消耗用量，并增加对无关输入采取行动的机会。

### Slack 触发器

Slack 触发器是例程的一部分，不是 [Slack](https://x.ai/bot/plugin/674) 应用。应用让 Bot 以你连接的 [Slack](https://x.ai/bot/plugin/674) 用户身份发布和读取；触发器则在 Slack 中发生某事时启动例程。在依赖它之前，请在拥有该 Bot 的 Cursor 账户上连接 Slack。

例程可以在 Bot 被提及时、某个词或短语被提及时、你对消息作出回应时，或任何消息出现时启动。它可以监视一个频道或整个 Slack，**何时运行** 会用文字显示触发器，例如某个短语和某个频道。频道和短语要保持狭窄：在繁忙频道中对任何消息设触发器会频繁运行，并把用量花在不需要 Bot 的消息上。

### Webhook

让 Bot 给例程添加 webhook 触发器，然后在桌面端打开该例程。**Webhook** 部分显示三个字段：

* **POST 到（POST to）** 是 URL。
* **密钥（key）** 是机密。发送方以 `Authorization: Bearer <key>` 的形式包含它。
* **请求头（header）** 是完整的该请求头，可直接复制。

点击字段即可复制。向该 URL 发送 HTTP POST，带上请求头和可选的 JSON 正文；Bot 会收到正文和例程指令。`200` 响应表示 Grok Bot 接受了调用并启动了一次运行，不代表 Bot 已完成；请在 Bot 的聊天中查看结果。其他任何响应都表示运行没有启动，因此请确认例程没有暂停，并确认请求使用了当前密钥。

## 启用前测试

如果例程显示 **测试**，请在创建或编辑例程后使用它：在桌面端打开例程并选择 **测试**。运行结束前按钮显示 **运行中…（Running…）**，结果显示在 Bot 的聊天中。如果测试无法启动，你会看到 **无法启动测试运行（Couldn't start a test run）**，或一条解释原因的消息。

有些例程不显示 **测试**；它们仍会按时间表或触发器运行。对于这些例程，在依赖它之前，先在聊天中让 Bot 用安全输入做一次同样的工作，然后检查第一次按计划运行的结果。

> 测试运行会执行真实工作。它可能浏览网站、更改文件并调用已连接工具。请使用安全输入，并把写入操作留在审批之后。

检查：

* 它是否选择了当前输入
* 输出是否符合要求的格式
* 每个操作是否都有来源或审计轨迹
* 它是否在预期的审批点停下
* 失败状态是否明确

## 管理例程

通过在聊天中请求 Bot 来创建和更改例程。要在桌面端查看它们，点击聊天顶部的 Bot 名称打开其详情。例程位于 **详情（Details）** 选项卡。每一行显示例程名称和运行时间，或 **已暂停（Paused）**；使用行上的开关暂停或恢复它。如果 Bot 没有例程，你会看到 **在聊天中要求设置例程（Ask in chat to set a routine）**。

打开一个例程，阅读其 **指令（Instruction）**（Bot 在每次运行时做什么）和 **何时运行**（时间表以及启动它的事件）。由 webhook 调用启动的例程还会显示 **Webhook**。底部的按钮是：

* **暂停（Pause）** 或 **恢复（Resume）**
* **测试**，当例程提供时
* **编辑**，它会启动一条发给 Bot 的消息，以「Edit your routine:」加例程名称开头；补上需要更改的内容并发送
* **删除例程（Delete routine）**（垃圾桶图标），会要求你确认

你也可以右键点击例程来 **暂停** 或 **恢复**、**测试**、**在聊天中编辑** 或 **删除**。在 Team Bot 上，同一菜单还可能显示 **谁可以使用这个例程？（Who can use this routine?）**：选择 **仅我（Only me）** 让例程只供你自己使用，或选择 **所有有访问权的人（Everyone with access）** 为所有能使用该 Bot 的人运行它。

在手机上，打开 Bot 的配置文件并找到 **例程**。点击一个例程可查看 **活动（Active）**、**时间表（Schedule）**、**下次运行（Next run）**、**指令** 和 **运行历史（Run history）**。关闭 **活动** 可暂停例程，向左滑动例程行可删除它。**运行历史** 把每次近期运行显示为 **运行中（Running）**、**成功（Succeeded）** 或 **失败（Failed）**，失败运行会附原因；**尚无运行（No runs yet）** 表示还没有任何东西启动过该例程。

一个 Bot 最多可以拥有 50 个例程，应用会为每个例程保留最近 20 条运行记录。例程的时间表间隔至少五分钟。删除例程会停止其未来的运行，且无法撤销。删除 Bot 也会移除该 Bot 拥有的例程。

### 如果例程没有运行

* 例程没有处于 **已暂停**。在手机上，**活动** 是开启的。
* **何时运行** 显示了预期的时区中的时间表或触发器。
* 新的时间表会等待下一个时间点。使用 **测试** 立即运行。
* 对于 Slack，消息是新的、位于触发器监视的频道中，并匹配其短语。
* 对于 webhook，调用返回了 `200` 并使用了当前密钥。

### 速率限制

例程有每小时限制：你的所有例程合计每小时最多运行 300 次，单个例程每小时最多 200 次。超过任一限制的运行会失败，并显示 `Automation run rate limit exceeded`。如果某个例程持续触及上限，请让 Bot 收窄其触发器或放宽其时间表。

有些运行也可能因为所有 Grok Bot 例程共享的一个限制而报这个错误，即使你自己的例程运行次数低于该限制。这是一个已知问题，正在修复。因该错误失败的运行不会自动重试，所以请自行重跑例程：使用 **测试** 立即运行，或对于 webhook，重新发送调用。

### 例程与用量

每次运行都会消耗用量，所以运行频繁的例程比运行稀少的例程花费更多。每小时的时间表、很短的间隔，或在繁忙频道上的 Slack 触发器，可能一天就用掉一周的用量。如果你的 **每周用量上限（Weekly usage limit）** 消耗得比预期快，请暂停不需要的例程，然后让 Bot 放宽时间表、收窄 Slack 触发器，再考虑升级套餐或提高按需上限。从不运行的例程不消耗用量；**测试** 会消耗，因为它执行工作。每周用量和按需每月上限见[套餐与计费](https://grok.com/help/grok-bot/plans)。

为了控制无人值守用量，Grok Bot 可能会在长时间离开后询问是否继续保持例程运行，如果没有回应就暂停它们。回来后请检查已暂停的例程。

## 为信任而设计例程

* 自动化执行之前的准备工作。
* 让 Bot 先起草、核对或建议。
* 发送、购买、删除、发布或更改生产系统需要批准。
* 包含无数据和数据过期的策略。
* 尽可能让重试具备幂等性。
* 告诉 Bot 在哪里报告部分完成。
* 在网站、应用或来源格式变化后重新测试。

关于时间表、Slack 触发器和 webhook 的更多内容，见[例程](https://grok.com/help/grok-bot/routines)。时区和用量控制见[设置与通知](https://docs.x.ai/grok-bot/settings-and-notifications)，自动化边界见[审批、安全与隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy)。
