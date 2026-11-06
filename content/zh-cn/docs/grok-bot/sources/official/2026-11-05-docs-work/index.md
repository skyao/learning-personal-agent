---
title: "文档：使用 Grok Bot 工作"
linkTitle: "文档：使用 Grok Bot 工作"
date: 2026-11-05
originalTitle: "Work with Grok Bot"
sourceUrl: "https://cursor.com/docs/grok-bot/work"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 记忆与上下文, 持续执行, 连接器]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文档按四部分写：Bot、消息与协作、计算机与应用、技能与例程。Bot 是有名字、工作和长期上下文的持久队友，记忆保存稳定偏好、重要事实和工作摘要，但文档提醒记忆不能代替权威来源，安全边界应靠批准和规则而非记忆。同一账号下所有 Bot 共用一台持久云端计算机，工作区为 /workspace；登录时先用 Vault、再用连接的密码管理器、最后用安全表单，单点登录、通行密钥、验证码等交给用户接管。应用（连接器）账号级共用，OAuth 令牌留在后端。群聊可放 2 到 6 个 Bot，Bot 之间异步交接；例程可按时间表或事件触发（如 Slack 消息、GitHub 通知），测试例程会真实执行动作。还介绍了「Teach a task」示范教学（最多记录十分钟，逐步推出），恢复顺序为从最轻的重试到最后的重置。

**保留理由**：这是日常使用层面最全的一篇，覆盖记忆范围、计算机共享、凭证处理、群聊与交接、例程和恢复，可与产品设计文章对照。

---

关于日常使用 Bot 的一切：[创建和管理它们](#bots)、[消息与协作](#messaging-and-collaboration)、[它们共用的电脑](#the-computer-and-apps)，以及[把完成的工作变成技能和例程](#skills-and-routines)。

## Bot

Bot 是一个持久的 AI 队友，有名字、工作、自己的对话，以及随时间发展的工作上下文。当工作有不同目标、工具集、工作方式、批准边界或重复时间表时，创建一个单独的 Bot。像 Talent Scout、Expense Manager 和 Bug Reproduction 这样的岗位会给 Bot 指导，并让其保存的上下文可复用；General Helper 则两者都不提供。用可执行的表述描述角色：

> Own the weekly account-health review. Pull product usage and support
> signals, flag evidence of churn or expansion, and produce a linked watch
> list for the customer-success team. Never contact a customer or change an
> account without approval.

### 创建一个 Bot

1. 在侧边栏选择**新建 Bot（New Bot）**（**+** 按钮），或按 `Cmd+NCtrl+N`。在团队中，**+** 按钮会打开菜单；选择**创建 Bot（Create a Bot）**。给 Bot 命名，选择形状和颜色，然后选择**创建（Create）**。
2. 在你的第一条消息中，给 Bot 它的工作、来源和批准边界，并让它记住它们。发送一个带明确完成标准的真实首个任务；起始提示见[用例](https://cursor.com/docs/grok-bot/use-cases)。
3. 要重命名 Bot、添加标签或更改其图片，点击聊天顶部的 Bot 名称打开其详细信息。参见[更改 Bot 的名称、图片和它的工作](https://cursor.com/help/grok-bot/edit-bot)。

你现有的 Bot 也可以在某个工作应该有长期负责人时，建议或创建一个专注的 Bot。

### 编辑 Bot

当你发现一个应影响未来工作的持久偏好、边界或职责时，告诉 Bot 并让它记住。使用普通消息传达任务特定指令：

- **长期规则。** 「从现在起，未经批准绝不发送外部消息。」
- **任务。** 「为这十二个账号起草跟进消息。」

一个[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)还有描述，其所有者或 Manager 在 Bot 详细信息的**关于（About）**下编辑它。

### 组织你的 Bot 列表

将活跃的 Bot **固定（Pin）**到侧边栏顶部，并用分区按项目、客户或业务分组：右键点击一个 Bot 并选择**移动到新分区（Move to new section）**，或者在已有分区后选择**移动到（Move to）**。分区在桌面端和 iOS 之间同步。**从侧边栏隐藏（Hide from sidebar）**会把 Bot 从主列表中移除，而不删除其工作或暂停其例程；可从**隐藏的 Bot（Hidden Bots）**用**在侧边栏显示（Show in sidebar）**恢复。在 iPhone 上，**复制（Duplicate）**一个 Bot，以将角色复用于不同范围，例如每个地区一个账号健康 Bot：副本会带有配置文件、设置、启用的技能、例程和头像，但不带对话历史、学到的记忆或附件，因此在分配工作前请重命名并赋予新范围。

### 共享 Bot

当其他人应从同一个 Bot 开始时，共享一个公开链接。该链接会暴露共享配置（身份、描述、技能和例程），因此请先移除 API 密钥、内部 URL 和客户数据。接收者会将副本添加到自己的账号；他们永远不会得到你的电脑、登录信息或对话历史，并且添加共享 Bot 即接受当时显示的第三方 bot 条款。要让团队共用一个 Bot 与之聊天，而不是每人一份副本，请[共享该 Bot 本身](https://cursor.com/help/grok-bot/shared-bots)。

在 Teams 套餐和 Enterprise 套餐上，管理员控制成员是否可以公开发布 Bot 模板。参见[模板共享](https://cursor.com/docs/grok-bot/teams#admin-controls)。

### 删除 Bot

删除 Bot 会移除其配置文件、对话和例程。共享电脑上的文件和登录信息不会按 Bot 隔离，可能留在那里；请单独清理它们。如果你以后可能需要这些工作，请改为隐藏 Bot。

### Bot 记住什么

Bot 会保留稳定的偏好、重要事实和其工作的摘要，这使它能够长期保持一个角色，而无需重放此前的每条消息。记忆不能替代权威来源：把变化的事实保留在源系统中，对于后果重大的决定，让 Bot 引用或重新打开当前数据，直接纠正过时的假设，并用批准和[自动审查规则（Auto-review rules）](https://cursor.com/docs/grok-bot/security#approvals-and-auto-review)而不是仅靠记忆来支撑安全边界。

## 消息与协作

Grok Bot 的设计目标是像给队友发消息一样。让请求保持自然，但把结果和决策边界说清楚：Bot 可以更改什么，以及它必须在何处停下来问你。

### 给 Bot 发消息

在对话中，你可以粘贴文本、链接和图片，附加文件，按名称请求已保存的[技能](#skills-and-routines)，用 `@` 提及 Bot、分组、例程或应用，回复或回应消息，并在工作正在进行时发送另一条指令。对话记录会在普通消息旁显示工具活动、电脑使用、创建的文件、问题和批准请求。

来自你的直接消息优先于后台工作，并可以重定向当前回合。当工作应立即结束时，发送「立即停止」；停止不会撤销 Bot 已经完成的动作。

### 附加文件和链接

支持的输入包括图片、音频、视频、PDF、Office 文档、CSV、JSON、YAML、源代码、HTML、电子邮件文件和笔记本。大型、加密、损坏或异常的文件可能无法读取；请将异常格式导出为 PDF、CSV、纯文本或图片。

| 限制 | 值 |
| --- | --- |
| 每条消息的附件数（桌面端） | 20 |
| 图片 | 每个 25 MB，每条消息总计 200 MB |
| 文档、音频和其他文件 | 每个 250 MB |
| 视频 | 每个 1 GB |

告诉 Bot 每个附件是什么以及如何使用它：

> The PDF is the signed policy. The spreadsheet is this month's transactions.
> Reconcile the spreadsheet against the policy, cite the relevant policy
> section for every exception, and return a new spreadsheet plus a short
> summary. Don't modify the originals.

当 Bot 可以从其电脑或连接的应用访问页面时，粘贴链接；如果页面是私有的，[通过电脑登录](#take-over-for-sensitive-steps)或连接该应用。在输入凭据或批准外部操作之前，务必检查链接的目的地。

### 群聊

当多个 Bot 需要一个共享结果和可见的交接时，使用群组。选择**新建聊天（New chat）**，选择两到六个 Bot，并描述结果以及谁负责下一步。正常书写，让 Bot 决定谁回应；输入 `@` 把请求交给一个队友，把 `@everyone` 留给全组更新。一个有用的启动方式是为每个阶段指定一个负责人：

> @Researcher gather the source material and link every claim. @Writer turn
> the findings into a launch draft. @Reviewer check the draft against the
> sources and list only blocking issues. Don't publish anything.

你在群组中的消息可以包含附件。Bot 到群组的交接消息是纯文本，因此当另一个 Bot 必须检查图片时，Bot 应直接将图片发送给该 Bot。

### 在 Bot 之间交接工作

Bot 可以向另一个 Bot 发送异步消息，后者会醒来、处理请求，并可以稍后回复；你会在对话中看到交接。当一个 Bot 拥有源系统而另一个拥有交付物时，或者当一个长期运行的工作应在你无需协调每一步的情况下继续时，交接效果很好。在每个阶段要求单一负责人；并行交接会产生重复工作和嘈杂的更新。

交接需要 Bot 为一个人行事。从应用或你自己的 Slack 私信中，任何 Bot 都可以交接工作。从 Slack 频道线程中，只有[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)可以代表提及它的人进行交接。参见[Bot 可以从 Slack 向其他 Bot 发消息吗？](https://cursor.com/help/grok-bot/group-chats#can-a-bot-message-other-bots-from-slack)

### 要求可审查的结果

指定产物及其验收标准：带来源链接的文档、定义了列的电子表格、一个包含截图和日志的文件夹，或一份尚未发送的草稿。对于后果重大的工作，让 Bot 区分在源系统中发现的事实、假设、已完成的操作、等待批准的操作和未解决的问题。

强结果可独立审查：直接的来源链接、显示相关状态的截图、时间戳、简洁的操作日志，以及 Bot 无法验证的任何内容的明确列表。对于快速变化的数据，不要只依赖截图。生成的文件和链接会以卡片形式出现，你可以预览、保存或带反馈回复；让 Bot 修订已有的产物，而不是制作互不相连的副本。

当反馈针对一个结果或一个批准请求时，在线程中回复；仅将回应用于轻量确认；单独的回应不应承载安全关键的决定。搜索和命令面板会在你的 Bot 中查找先前的消息、文件、链接和例程。搜索的可用性在推出期间可能有所不同；如果跨对话结果不可用，请打开相关 Bot 并使用其对话历史。

## 电脑与应用

你的 Bot 在一台持久化的云端电脑上工作，配有浏览器、命令行和文件系统。即使你的笔记本电脑合上，工作也会继续；文件、登录状态和浏览器会话在任务之间保持。

你账号上的每个 Bot 都使用同一台电脑：浏览器会话、文件和命令行凭据共享，一个 Bot 可以接着另一个 Bot 保存的工作继续。每个 Bot 有自己的屏幕，因此多个 Bot 可以并行使用浏览器和桌面工具（每个屏幕同一时间只能运行一个计算机使用（computer use）任务），但这些屏幕是工作界面，不是安全边界。如果另一个 Bot 不应能使用某项凭据，就不要把它放在电脑上。用户之间是严格隔离的：每个用户的电脑都是专用且硬件隔离的。参见[用户如何隔离](https://cursor.com/docs/grok-bot/teams#how-users-are-isolated)。

### 观看电脑

点击对话右侧面板中的电脑预览，打开电脑并观看点击、输入、导航和当前状态。你可以在工作继续时离开预览；关闭应用不会停止云端工作。

### 接管敏感步骤

登录时，Bot 会先使用保存在 [Vault](https://cursor.com/help/grok-bot/secrets#what-is-vault) 中的登录信息，然后使用已连接的密码管理器（例如 1Password），最后用安全表单（Secure Form）询问你。来自 Vault 和安全表单的值会被填入页面，Bot 看不到它们。当网站通过电子邮件发送一次性验证码时，Bot 可以从已连接的 Gmail 或 Outlook 账户或从其自己的收件箱读取。结账时，它可以使用保存在 Vault 中的卡、你在安全表单中输入的卡，或已连接的钱包（例如 Link、X Money 或 Shop Pay）。

当表单无法完成该步骤时，Bot 会把电脑交给你：单点登录、通行密钥、它无法通过的 CAPTCHA（验证码）、在另一台设备上批准、二维码或银行卡验证。取得控制权，只完成被阻塞的步骤，然后告诉 Bot 继续。已登录的会话会为未来任务保留，并在你的 Bot 之间共享。有些网站会让会话过期或重新验证；请让 Bot 暂停并通知你，而不是绕过检查。

对于 API 密钥或其他秘密，在 Bot 询问时输入到安全秘密卡片（secure secret card）中：该字段会被遮蔽，值不会写入聊天，也不会显示给 Bot。绝不要把密码或一次性验证码粘贴到普通聊天中。参见[安全地存储秘密](https://cursor.com/help/grok-bot/secrets)。

### 连接应用

应用（App）为 Bot 提供了一种结构化的方式来处理 Gmail、Notion 和 Slack 等服务，当存在可用的应用时，它比在网站上点击更可靠。从侧边栏打开**连接应用（Connect apps）**，或跟随聊天内的**连接（Connect）**卡片，然后在浏览器中完成提供方登录；设置步骤和已知问题见[连接应用](https://cursor.com/help/grok-bot/connect-apps)。

- **应用是账户级的。** 已连接的应用对你运行的每个 Bot 可用。队友的[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)在使用你的账号前会先询问。
- **应用登录信息不会落在电脑上。** OAuth 令牌保存在 Cursor 的连接器后端，Bot 调用工具时不会收到它们。
- **团队策略适用。** 被团队连接器策略阻止的应用会显示**已被团队管理员禁用（Disabled by team admin）**。阻止一个应用不会阻止该服务的网站。要关闭这第二条路径，需要**网络控制（Network Controls）**，仅限 Enterprise。参见[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)。

### 文件与工作区

这台电脑有一个位于 `/workspace` 的共享工作区。把持久项目文件放在那里清晰的文件夹中。文件、浏览器状态和支持的登录信息会在正常的电脑更新和恢复后保留；把临时目录、手动安装的包和未提交的应用状态视为可替换，并将重要结果复制到工作区或附加到对话中。

### 更新、恢复或重置

应用和电脑分别更新。当电脑无法连接时，从破坏性最小的选项开始：

1. 从错误状态重试，或重新打开对话。
2. 重启 Grok Bot 应用并检查应用更新。
3. 当无法连接的状态提供**恢复 Grok Bot 的电脑（Recover Grok Bot's Computer）**时，选择它。
4. 在**设置** > **电脑**中，使用**更新 Bot 的电脑（Update Bot's Computer）**移动到最新版本。
5. 仅作为最后手段，在同一部分使用**重置 Bot 的电脑（Reset Bot's Computer）**。

软件更新只会刷新 Grok Bot 的软件，并保留已安装的应用。电脑更新会重建电脑，保留文件和登录信息，但移除已安装的应用和包。恢复和重置都会从你上次保存的数据重建电脑；如果无法连接电脑以先保存，最近的变化不会回来。对话存储在电脑之外，因此即使重置也会保留。参见 [Grok Bot 电脑](https://cursor.com/help/grok-bot/computer-recovery)。

### 你的本地电脑是分开的

云端电脑与你面前的机器是分开的。Bot 仅在本地执行策略下在你的本地电脑上运行命令：默认逐条命令批准，可设置为始终允许、每次询问或从不。该策略是它自己的控制，与管辖云端电脑工作的批准分开。参见[本地执行](https://cursor.com/docs/grok-bot/security#local-execution)。

## 技能与例程

**技能（skill）**是一组可复用的说明，用于如何完成一项任务。**例程（routine）**告诉一个 Bot 何时运行工作流，按时间表或在支持的事件之后。先从一个一次性任务开始，让它可靠，把方法保存为技能，然后才自动化它。

### 保存技能

技能会捕获步骤、决策规则、预期输出和安全边界，并在你的 Bot 之间可用（Bot 可能仍需要相关的应用或登录）。直接请求：

> Save the process we used for this task as a skill called "Weekly account
> health". Include the source systems, risk definitions, output format, and
> the rule that customer contact always requires approval.

一个有用的技能会说明何时使用它、所需输入和访问权限、工作顺序、如何验证结果、返回什么，以及什么需要批准。要使用技能，按名称向 Bot 请求它。如果 Bot 找不到私有技能，请打开侧边栏中的**连接应用**，选择标题旁的已连接计数，并在**私有技能（Private skills）**下为当前 Bot 启用它。

### 通过示范教授工作流

与其描述每一步，不如示范一次浏览器工作流，让 Bot 将其转成草稿技能。从打开电脑视图的一对一对话中，选择**教授任务（Teach a task）**，描述结果，并执行工作流。教学会录制可见的电脑交互，最长十分钟，且不会录制麦克风音频；让秘密远离演示，并使用安全密钥请求获取凭据。学到的技能是草稿：添加决策规则、失败处理和批准边界，然后在安排之前在一个安全输入上测试它。

教授任务正在逐步推出。如果该控件不可见，请让 Bot 根据书面说明和已完成的任务创建技能。

### 创建例程

向应负责该重复工作的 Bot 请求：

> Every weekday at 8:00 AM, run the "Daily customer risk" skill against the
> current account list. Post a linked watch list in this conversation. Don't
> contact customers. If the source data is unavailable, report the failure
> instead of using old data.

确认负责的 Bot、时间表与时区、输入来源、预期结果、批准边界，以及来源缺失时会发生什么。例程在你笔记本电脑合上时在云端运行。删除例程会停止其未来的运行，且无法撤销。

Cursor 账号集成也可以从事件启动例程，例如 Slack 消息或 GitHub 通知；它们与 Slack 或 GitHub 应用是分开的。定义狭窄的匹配规则和清晰的响应，例如「当 `#customer-escalations` 中的消息包含工单链接和短语 'needs repro' 时，在暂存环境中复现该问题，并在此对话中发布复现包」。避免像「每条新消息」这样的宽泛监听器，它们会产生噪音、消耗用量，并对无关输入采取行动。

### 测试和管理例程

在创建或编辑例程后使用**测试（Test）**，并审查它是否选择了当前输入、符合输出格式、保留了来源轨迹、在预期的批准点停止，并明确说明了失败状态。

测试运行会执行真实工作。它可以导航网站、更改文件并调用连接的工具。使用安全的输入，并把写操作置于批准之后。

通过在聊天中询问 Bot 来创建和更改例程。要在桌面端查看它们，点击聊天顶部的 Bot 名称打开其详细信息。例程在**详细信息（Details）**选项卡上。打开一个例程以阅读其**指令（Instruction）**和**运行时机（When to run）**。右键点击例程可**暂停（Pause）**或**恢复（Resume）**、**测试**、在聊天中**编辑（Edit）**或**删除（Delete）**它。Webhook 例程还会在那里显示 **Webhook**。在手机上，Bot 的配置文件会列出其例程及**运行历史（Run history）**。离开很长一段时间后，Grok Bot 可能会询问是否继续运行例程，如果你不回应就暂停它们。关于时间表、Slack 触发器和 Webhook，参见[例程](https://cursor.com/help/grok-bot/routines)。

例程赢得信任的方式与人相同：在执行前自动化准备，把发送、购买、删除、发布和生产环境更改置于批准之后，报告缺失或过时的来源而不是绕过它们，并在网站、应用或来源格式变化后重新测试。
