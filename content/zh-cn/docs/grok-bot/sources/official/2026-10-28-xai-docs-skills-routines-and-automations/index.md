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
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [持续执行, 功能更新]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「例程」和 cursor.com 文档「Work」与这页部分重合。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：技能是跨 Bot 共享的私有库，可以发布给团队；「Teach a task」可以录屏演示一个流程（最长 10 分钟、不录麦克风），生成技能草稿。例程可以按定时触发，也可以由 Slack、GitHub、Linear、Sentry、PagerDuty、邮件或 webhook 事件触发。每个 Bot 最多 50 个例程，调度间隔至少 5 分钟，所有例程合计每小时最多运行 300 次、单个例程最多 200 次，超限不自动重试。新建例程不会立即运行，用 Test 试跑会真实执行并消耗用量；文档提醒高频例程一天就可能耗尽一周用量。

**保留理由**：给出了 Grok Bot 持续执行的触发方式和配额数字，可以和其他产品的定时、事件机制对照。

---

技能与例程

把一项成功的任务变成可重复的流程。Grok Bot 使用两个
构建块：

* **技能（skill）**是一组可复用的指令，说明如何完成一项任务。
* **例程（routine）**告诉一个 Bot 何时运行一个工作流：按日程，或在
  某事发生时，例如 Slack 消息，GitHub、Linear、Sentry 或
  PagerDuty 事件，一封电子邮件，或一次 webhook 调用。

从一次性任务开始。让它可靠，把方法保存为技能，然后
再自动化它。

## 保存技能

技能会记录步骤、决策规则、预期输出和安全边界。
技能在你的所有 Bot 之间可用，不过某个 Bot 可能需要相关的
应用或登录才能使用某项技能。

可以这样要求：

> Save the process we just used as a skill called “Weekly account health.”
> Include the source systems, risk definitions, output format, and the rule that
> customer contact always requires approval.


一项有用的技能会说明：

1. 何时使用它
2. 所需的输入和访问权限
3. 工作的顺序
4. 如何验证结果
5. 返回什么
6. 什么需要批准

使用侧边栏中的**连接应用（Connect apps）**发现并安装受支持的应用和
打包技能。要使用一项技能，按名称向 Bot 请求它；用 `@` 提及 Bot、
群组、例程和应用。

私有技能是一个由你所有 Bot 共享的库。如果 Bot 找不到某个
私有技能，打开侧边栏中的**连接应用**，选择标题旁已连接的
数量，并在**私有技能（Private skills）**下为当前 Bot 启用它。

### 与团队分享技能

如果你属于某个团队，可以发布一项私有技能，让队友也能
使用。在桌面上，打开**连接应用**，选择标题旁已连接的
数量，然后打开该技能。在其标题栏中选择**发布（Publish）**。如果你属于
多个团队，在**发布到（Publish to）**下选择团队。

技能需要有描述才能发布，因为队友和
他们的 Bot 会用描述来判断何时适用。发布之后，
按钮会显示**已发布（Published）**。其菜单提供**同步（Sync）**（把你之后的编辑推送到
团队的副本）、**复制链接（Copy link）**和**取消发布（Unpublish）**。

如果发布被拒绝，消息会说明原因：你需要先加入一个团队，
或者你的团队管理员已关闭成员的发布权限，这种情况下请让
管理员发布该技能。随应用或 Bot 模板附带的技能
不能发布。

## 通过演示教一个工作流

当**教一个任务（Teach a task）**可用时，你可以演示一个浏览器工作流，
而不必描述每一个步骤。

1. 打开一对一的 Bot 会话及其计算机视图。
2. 选择**教一个任务**。
3. 描述你即将演示的结果。
4. 执行一次该工作流。
5. 停止录制，并查看 Bot 创建的技能。
6. 在安排它之前，在一个安全的示例上测试它。

教学会录制可见的计算机交互，最长十分钟。它
不会录制麦克风音频。演示期间避免暴露秘密；
凭据请使用安全交接流程。

学到的技能是一份草稿。请补充仅凭一个示例可能
不明显的决策规则、失败处理和审批边界。

演示教学可能会逐步启用。如果看不到该控件，
请让 Bot 根据书面说明和已完成的任务创建一项技能。

## 创建例程

向应当负责该重复性工作的 Bot 提出：

> Every weekday at 8:00 AM, run the Daily customer-risk skill against the
> current account list. Post a linked watch list in this conversation. Do not
> contact customers. If the source data is unavailable, report the failure
> instead of using old data.


确认：

* 负责的 Bot
* 日程和时区
* 输入来源
* 预期结果
* 审批边界
* 来源缺失时应当发生什么

Bot 会创建该例程，它会出现在 Bot 的例程中。例程在你的笔记本电脑
关闭时也在云端运行。

在手机上，你也可以打开 Bot 的个人资料，并在
**例程（Routines）**下点击**添加例程（Add routine）**。Grok Bot 会开始一条以「Set up a routine to」开头的消息；
补完这句话并发送。

### 日程和时区

日程使用**设置（Settings）**中 **Bot** 下标记为
**时区（Timezone）**的时区。**自动检测（Auto-detect）**跟随这台计算机。当
例程应当遵循另一个时区时（例如工作所属的办公室），请选择一个时区。

用平实的语言要求日程，例如「每个工作日早上 8:00」或「每 2
小时」。然后打开例程并检查**何时运行（When to run）**，它会用文字显示已保存的
日程。如果它与你的意思不符，选择**编辑（Edit）**并告诉
Bot 要修正什么。

新例程会等待其下一个预定时间；它不会在创建时运行。如果你在 8:05
设置了「每天 8:00」，第一次运行是
明天早上 8:00。要立即试用，请使用**测试（Test）**。

## 由事件触发工作

例程可以在某事发生时启动，而不是按日程启动：一条 Slack
消息，GitHub、Linear、Sentry 或 PagerDuty 事件，一封发到你
[Bot 自己的地址](https://docs.x.ai/grok-bot/computer-and-apps#give-your-bots-an-email-address)的电子邮件，
或一次 webhook 调用。Cursor 账户集成会启动这些例程；它们
与 Slack 或 GitHub 应用分开，可能需要自己的连接。向
Bot 要求你想要的触发器；例程的**何时运行**会用
文字显示它，例如「创建 Linear 问题时」。只有新活动才算：
触发器存在之前的事件不会启动运行。

定义一个狭窄的匹配规则和明确的响应：

> When a message in `#customer-escalations` contains a support ticket link and
> the phrase “needs repro,” open the ticket, reproduce the issue in staging,
> and post a repro pack in this conversation. Never post back to Slack without
> approval.


避免宽泛的监听器，例如「每条新消息」。它们会产生噪音、消耗
用量，并增加对无关输入采取行动的机会。

### Slack 触发器

Slack 触发器是例程的一部分，而不是 Slack 应用的一部分。应用让 Bot 以你连接的 Slack 用户身份发布
和读取；触发器会在 Slack 中发生某事时启动例程。在依赖它之前，请在拥有该
Bot 的 Cursor 账户上连接 Slack。

例程可以在 Bot 被提及时、某个词或短语被
提及时、你对某条消息做出反应时，或任何消息上启动。它可以监视一个
频道或整个 Slack，**何时运行**会用文字显示触发器，例
如一个短语和一个频道。保持频道和短语狭窄：在繁忙频道中对任何
消息的触发器会频繁运行，并把用量花在不需要该 Bot 的消息上。

### Webhook

让 Bot 为例程添加一个 webhook 触发器，然后在
桌面上打开该例程。**Webhook** 部分显示三个字段：

* **POST to** 是 URL。
* **key** 是密钥。发送方以 `Authorization: Bearer <key>` 的形式包含它。
* **header** 是完整的该请求头，可直接复制。

点击字段即可复制。向该 URL 发送一个带该请求头和
可选 JSON 正文的 HTTP POST；Bot 会收到正文和例程
指令。`200` 响应表示 Grok Bot 接受了调用并启动了
运行，而不是表示 Bot 已完成；请在 Bot 的聊天中查看结果。任何
其他响应表示运行没有启动，因此请确认例程没有
暂停，并且请求使用的是当前密钥。

## 启用前先测试

如果例程显示**测试**，在创建或编辑例程后使用它：
在桌面上打开例程并选择**测试**。运行完成前按钮会显示**运行中…（Running…）**，
结果显示在 Bot 的聊天中。如果测试
无法启动，你会看到**无法启动测试运行（Couldn't start a test run）**，或一条说明
原因的消息。

有些例程不显示**测试**；它们仍会按日程或触发器运行。
对于这些，请先让 Bot 在聊天中用安全输入做一次同样的工作，
然后再依赖该例程，并检查第一次预定运行。

> 一次测试运行会执行真实工作。它可以浏览网站、更改文件，并
> 调用已连接的工具。请使用安全输入，并让写操作留在审批之后。

检查：

* 它是否选取了当前的输入
* 输出是否符合要求的格式
* 每个操作是否有来源或审计轨迹
* 它是否在预期的审批点停下
* 失败状态是否明确

## 管理例程

通过在聊天中要求 Bot 来创建和更改例程。要在桌面上查看它们，
点击聊天顶部的 Bot 名称以打开其详情。
例程在**详情（Details）**标签页上。每一行显示例程的名称和运行时间，
或**已暂停（Paused）**；使用行上的开关暂停或恢复它。如果
Bot 没有例程，你会看到**在聊天中要求设置例程（Ask in chat to set a routine）**。

打开一个例程以阅读其**指令（Instruction）**（Bot 在每次运行时做什么）和
**何时运行**（日程以及启动它的事件）。由 webhook 调用启动的例程
还会显示 **Webhook**。底部的按钮是：

* **暂停（Pause）**或**恢复（Resume）**
* **测试**，当例程提供它时
* **编辑**，它会启动一条发给 Bot 的消息，以「Edit your routine:」
  和例程名称开头；添加应更改的内容并发送
* **删除例程（Delete routine）**（垃圾桶图标），它会要求你确认

你也可以右键点击例程来**暂停**或**恢复**它、**测试**它、
在聊天中**编辑**它，或**删除**它。

在手机上，打开 Bot 的个人资料并找到**例程**。点击一个例程以查看
**活动（Active）**、**日程（Schedule）**、**下次运行（Next run）**、**指令**和**运行历史（Run history）**。
关闭**活动**以暂停例程，滑动例程的行以删除
它。**运行历史**会把每次近期运行显示为**运行中（Running）**、**成功（Succeeded）**或
**失败（Failed）**，并显示失败运行的原因；**尚无运行（No runs yet）**表示还没有任何东西
启动过该例程。

一个 Bot 最多可以拥有 50 个例程，应用会为每个例程保留最近 20 条运行
记录。例程日程之间必须至少间隔五分钟。删除例程会停止其未来的
运行，且无法撤销。删除 Bot 也会移除该 Bot 拥有的例程。

### 如果例程没有运行

* 例程没有处于**已暂停**。在手机上，**活动**是开启的。
* **何时运行**在正确的时区显示了你预期的日程或触发器。
* 新日程会等待其下一个时间。使用**测试**立即运行它。
* 对于 Slack，消息是新的、位于触发器监视的频道中，并且
  匹配其短语。
* 对于 webhook，调用返回了 `200` 并使用了当前密钥。

### 速率限制

例程有每小时限制：你的所有例程合计每小时最多运行 300
次，每个例程每小时最多 200 次。超过任一限制的运行
会失败并显示 `Automation run rate limit exceeded`。如果某个例程不断达到
其限制，请让 Bot 缩小其触发器范围或放宽其日程。

有些运行也可能因为所有 Grok Bot 例程共享的一个限制
而以此错误失败，即使你自己的例程运行次数低于该限制。这是一个已知问题，
正在修复中。以此错误失败的运行不会自动重试，
因此请自行重新运行该例程：使用**测试**立即运行它，或者对于
webhook，再次发送调用。

### 例程与用量

每次运行都会消耗用量，因此运行频繁的例程比运行稀少的例程
消耗更多。每小时日程、短间隔，或在繁忙频道上的 Slack 触发器
可能一天就用掉一周的用量。如果你的**每周用量限制（Weekly usage limit）**
比你预期的更快用完，请暂停不需要的例程，然后让
Bot 放宽日程并缩小 Slack 触发器，再考虑提高套餐或
按需限制。从不运行的例程不消耗用量；**测试**会消耗，
因为它会执行工作。关于每周用量和
按需月度限制，参见[套餐与
计费](https://cursor.com/help/grok-bot/plans)。

要控制无人值守的用量，Grok Bot 可能会在一段长时间离开后询问是否继续运行例程，
如果没有响应就暂停它们。你回来时请检查已暂停的
例程。

## 为信任而设计例程

* 在执行之前自动化准备工作。
* 让 Bot 先起草、核对或推荐。
* 发送、购买、删除、发布或更改生产系统需要审批。
* 包含无数据和过期数据的策略。
* 尽可能让重试具有幂等性。
* 告诉 Bot 在哪里报告部分完成。
* 在网站、应用或来源格式变化后重新测试。

关于日程、Slack 触发器和 webhook 的更多内容，参见
[例程（Routines）](https://cursor.com/help/grok-bot/routines)。关于时区和
用量控制，参见[设置与通知](https://docs.x.ai/grok-bot/settings-and-notifications)，关于自动化边界，参见[审批、安全与
隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy)。
