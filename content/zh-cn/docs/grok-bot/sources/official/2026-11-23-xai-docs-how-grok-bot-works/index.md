---
title: "文档（docs.x.ai）：Grok Bot 如何工作"
linkTitle: "docs.x.ai：工作原理"
date: 2026-11-23
originalTitle: "How Grok Bot Works"
sourceUrl: "https://docs.x.ai/grok-bot/how-grok-bot-works"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-23）"
tags: [记忆与上下文, 运行环境, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的文档现以 docs.x.ai（SpaceXSI Docs）为准，cursor.com 的文档地址已 308 跳转到这里。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：文档以一个请求「报名与去年相同的会议并报销」为例，按五步说明 Grok Bot 如何工作：从记忆取回上一年的票和用卡规则，在 Gmail 找收据，在云端电脑上用浏览器登录并付款（登录凭据依次来自 Vault、1Password、Secure Form），发邮件给财务前由 Auto Review 拦下询问，最后把费用记入 Google Drive 的表格并回报。每个 Bot 有自己的记忆（偏好、规则、带日期的工作日志），姓名和时区等少量信息在所有 Bot 之间共享；所有 Bot 共用同一台云端电脑，各有自己的屏幕。Bot 没有自己的账号或凭据，所做的一切以用户身份进行，但各 Bot 之间并不隔离。文末还说明主 Bot 与单一职责 Bot 的分工和一组最佳实践。

**保留理由**：从一个任务串起记忆、连接器、云端电脑、凭据、审批和安全边界，是已收文档中对整体运行机制最集中的说明，尤其交代了所有 Bot 共用电脑和登录态这一点。

---

Grok Bot 如何工作

Grok Bot 是配有电脑的 AI 队友。每个 Bot 在你的应用里、也在云端的一台电脑上工作，所以你不在时它仍能继续。

Bot 可以通过插件和自定义 MCP 服务器使用其他服务。它们也可以把编码工作交给 Cursor Cloud Agents，并把结果附在自己的回复里。

本页通过跟踪一个常见请求从开始到结束，来说明 Grok Bot 如何工作。假设你有一个负责差旅与报销的 Bot，你给它发这句：

> 帮我报名与去年相同的会议，并报销。

1. **记得去年的通行证和该用哪张卡** —— 记忆。

2. **找到去年的收据** —— Gmail。

3. **登录并购买通行证** —— 电脑、安全表单（Secure Form）和 Vault。

4. **在把收据发给财务之前问你** —— 自动审核（Auto Review）。

5. **记录这笔费用并回报** —— Google Drive。

## 1. 它先查自己的记忆

你的消息没说清是哪个会议、哪种通行证、用哪张卡。你的报销 Bot 会从记忆里补上这些细节。它的工作日志里有去年的 2 日通行证，你还给过它一条规则：会议用工作卡。问它用了什么，它会给你看。

每个 Bot 有自己的记忆。它保存你的偏好、你让它遵守的规则，以及一份带日期的工作日志。关于你的少量信息，比如姓名和时区，由你所有的 Bot 共享。

* **由你所有 Bot 共享** —— 关于你：你的姓名和时区。

* **你的报销 Bot** —— 规则：会议使用工作卡。工作日志：购买了去年的 2 日通行证，$749。

* **你的主 Bot** —— 偏好：晨间简报保持简短。工作日志：起草了你的异地会议议程。

所以你只需要说一次。把时区告诉任何一个 Bot，你所有的 Bot 都会知道。告诉报销 Bot 收据放在哪里，就只有那个 Bot 知道。

Bot 自己决定记什么。你也可以让它记住某事、修正它或忘掉它。记忆会过时，所以对于会变的数字，比如价格，让 Bot 重新查一遍。登录信息和卡不要放进记忆，放进 [Vault](https://docs.x.ai/grok-bot/vault)。见 [Bot 记得什么](https://docs.x.ai/grok-bot/bots#what-a-bot-remembers)。

## 2. 它在 Gmail 里找到去年的收据

接下来，Bot 在 [Gmail](https://x.ai/bot/plugin/45893410) 里搜索去年的收据。[Gmail](https://x.ai/bot/plugin/45893410) 是已连接的应用，所以 Bot 直接在应用里工作，而不是打开网站。这比在浏览器里一页页点击更可靠。

### 添加你自己的工具

如果某个应用不在目录里，让 Bot 连接该应用的 MCP 服务器，这是 AI 工具连接服务的标准方式。如果服务有 API 但没有 MCP 服务器，[tinkabot](https://x.ai/bot/marketplace/bots/tinkabot) 可以做一个。它把 API 包装成一个由 MCP 服务器和技能组成的插件，测试它，并且只在你说可以时才发布。见[连接应用](https://docs.x.ai/grok-bot/computer-and-apps#connect-an-app)。

## 3. 它登录并购买通行证

会议网站没有应用，所以 Bot 在它云端电脑上的浏览器里打开它。你所有的 Bot 共用那台电脑。它还有命令行和在任务之间保留的文件。每个 Bot 有自己的屏幕，所以多个 Bot 可以同时工作，你也可以实时观看任一屏幕。当一个 Bot 登录某个网站时，你的其他 Bot 也就登录了。

网站要求输入密码。Bot 按以下顺序查找登录信息：

1. **Vault** —— 你为 Bot 保存的登录信息

2. **1Password** —— 你在 1Password 中批准的登录信息

3. **安全表单** —— 问你，然后直接填入页面

对这家网站，Vault 和 1Password 里都没有登录信息，所以 Bot 发来一张安全表单。

无论用哪一种，登录信息都直接进入页面，你的 Bot 从来看不到它。

付款时，Bot 使用你保存在 Vault 里的工作卡。已保存的卡在结账时自动填入，不必每次都问你。如果你希望每笔付款都自己批准，就不要保存卡。见[付款](https://docs.x.ai/grok-bot/vault#pay-for-things)。

如果任务需要 API 密钥，Bot 会给你发一张安全密钥卡。密钥保持隐藏，不进入聊天。

有些步骤需要你，比如单点登录、通行密钥，或者 Bot 无法解决的验证码。遇到这些，Bot 会把电脑交给你。在请求上选择 **打开电脑（Open computer）**，然后选择 **接管控制（Take control）**。完成那一步，再告诉 Bot 继续。见 [Vault 与安全登录](https://docs.x.ai/grok-bot/vault) 和[连接 1Password](https://docs.x.ai/grok-bot/computer-and-apps#connect-1password)。

## 4. 它在给财务发邮件之前先问

通行证买好后，Bot 准备把收据邮件发给财务。你定过一条先批准邮件的规则，所以它停下来问你。

在 Bot 运行命令、使用应用或在它的电脑上操作之前，自动审核会检查该操作。自动审核默认开启，大多数操作会自行进行。当某个操作需要你时，Bot 会显示一张批准卡，写明操作及其细节，然后等待。

你也可以添加自己的规则。在 **设置 → 常规** 中，**Bot** 下打开 **自定义规则（Custom rules）**。用平实的语言描述一个操作，比如「发送邮件」，然后选择 **先询问（Ask first）** 或 **自动允许（Allow automatically）**。**先询问** 规则总会拦下匹配的操作。就是这条规则拦下了这封邮件。

被 **先询问** 规则拦下的卡片会显示 **编辑规则（Edit rule）**，打开你的自定义规则。其他卡片可能显示 **始终允许（Always allow）**，它会保存一条规则，让类似的操作下次自行运行。

只有你自己的消息才算指令。假设会议页面藏有文字，让 Bot 给你的联系人发邮件。自动审核不会把它当成来自你的请求。这些检查降低了有害内容带来的风险，但并没有消除它。对任何无法撤销的操作都保持 **先询问** 规则。见[配置自动审核](https://docs.x.ai/grok-bot/approvals-security-and-privacy#configure-auto-review)。

## 5. 它记录这笔费用并回报

最后，Bot 把这笔费用加到 [Google Drive](https://x.ai/bot/plugin/45893413) 里你的 Finance 表格中，那是另一个已连接的应用。然后它回复说明做了什么。如果你那时已经合上笔记本电脑，它会继续做，并在完成后通知你。

聊天会随着 Bot 工作显示每一步，从你的消息到它的回复。

## 安全

你的报销 Bot 是以你的身份做完这一切的。Bot 没有自己的账号或凭据，所以它做不到你做不到的事，每个操作都能追溯到你这。唯一的例外是由你的团队管理的连接器，它可以使用团队或服务账号的凭据。

* **你的 Bot 的电脑** —— 你所有的 Bot 都在这里工作，共用它的文件和浏览器登录状态。

从不向你的 Bot 显示：

* **应用登录信息** —— 它们留在 Cursor 的服务器上。Bot 使用你的应用，却从不会拿到它们。

* **Vault** —— 已保存的登录信息和卡会填入页面，你的 Bot 看不到它们。

你的 Bot 之间并不隔离。你的其他 Bot 现在也登录了会议网站，也能使用 Vault 里的工作卡。不再需要的服务要及时退出登录，工作完成后删除敏感文件。Enterprise 团队还可以设置网络策略和推理钩子。见 [Grok Bot 安全](https://docs.x.ai/grok-bot/security)。

## 你的主 Bot 与只有一项职责的 Bot

大多数 Bot 最适合只有一项明确的职责，就像你的报销 Bot。你的[主 Bot](https://docs.x.ai/grok-bot/bots#your-primary-bot)不一样。它是你的主要联系人。它会主动与你联系，并协调你的其他 Bot。你可以把会议这个请求发给主 Bot，它可以转交给你的报销 Bot。

用主 Bot 开始新工作。当同一类请求不断出现，并且有自己的来源、规则或时间表时，就给它一个自己的 Bot，或让主 Bot 创建一个。只有一项职责的 Bot 会为那项职责积累记忆，你只需要解释一次。

## 最佳实践

* 从你的主 Bot 开始。当某项工作有自己的来源、时间表或审批需求时，给它一个自己的 Bot。要一次建立多个 Bot，可以从 [dr eggbot](https://x.ai/bot/marketplace/bots/dr-eggbot-v2) 开始。
* 让 Bot 记住长期有效的规则。单个任务的细节放在消息里。
* 对于会变的数字，比如价格或预算，让 Bot 去查，而不是依赖记忆。
* 为你常用的每个服务连接一个应用。如果服务没有应用，添加它的 MCP 服务器，或让 [tinkabot](https://x.ai/bot/marketplace/bots/tinkabot) 从它的 API 做一个。
* 绝不要把密钥粘贴到聊天里。密码走 Vault、1Password 或安全表单。卡走 Vault 或安全表单。API 密钥走安全密钥卡。
* 把一个任务跑通一次，然后[把它保存为技能](https://docs.x.ai/grok-bot/skills-routines-and-automations#save-a-skill)。接着[创建例程](https://docs.x.ai/grok-bot/skills-routines-and-automations#create-a-routine)，按计划运行它，或在某事发生时运行，比如一条 Slack 消息或一封发给你的 Bot 的邮件。
* 为发送、发布和删除添加具体的 **先询问** 规则。要批准每笔付款，就不要把卡保存在 Vault 里。
* 把电脑上的任何东西都视为你所有 Bot 都能访问。
* 在[群聊](https://docs.x.ai/grok-bot/chat-and-collaboration)中，让一个 Bot 负责每一个步骤。

- [dr eggbot](https://x.ai/bot/marketplace/bots/dr-eggbot-v2) —— 问你几个问题，然后替你建好这些 Bot，每个负责一项工作。

* [tinkabot](https://x.ai/bot/marketplace/bots/tinkabot) —— 把 API 包装成由 MCP 服务器和技能组成的插件，测试它，并且只在你说可以时才发布。
