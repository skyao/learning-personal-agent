---
title: "文档（docs.x.ai）：审批、安全与隐私"
linkTitle: "docs.x.ai：审批、安全与隐私"
date: 2026-10-29
originalTitle: "Approvals, security, and privacy"
sourceUrl: "https://docs.x.ai/grok-bot/approvals-security-and-privacy"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-29T00:00:00Z）"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 的安全文档面向管理员，这页面向用户，重合不多。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Auto Review 默认开启，用模型判断哪些操作需要用户确认；审批卡有「允许一次」「总是允许」「拒绝」三种选择，「总是允许」会存成规则，拒绝后 Bot 在用户发新消息前不会再尝试。从聊天发起的审批卡一直等待，由例程或后台任务发起的卡 30 分钟后过期。自定义规则「自动允许」「先询问」各最多 20 条。在用户本地电脑上执行命令默认每次询问，每台桌面单独设置，团队管理员可设上限。文档明确说云端电脑由用户名下所有 Bot 共用，分享 Bot 也不是安全边界；删除 Bot 不会清除共享电脑上的文件。

**保留理由**：给出了用户侧审批机制的具体规则（超时、规则数量、默认值），以及官方自己承认的安全边界。

---

审批、安全与隐私

Grok Bot 的设计目标是在完成工作的同时，让敏感输入和影响重大的操作始终处于你的控制之下。请把审批、安全交接和明确的 Bot 边界结合起来使用。

## 在请求中设定边界

告诉 Bot 它可以采取哪些操作，以及必须在何处停下：

> 核对活动数据，并起草一份建议的预算变更。不要修改活动，也不要联系代理机构。在展示当前值、建议值和预期影响后请求批准。

以下情况宜设定明确边界：

* 发送消息或邀请
* 发布内容
* 购买和资金转账
* 删除或覆盖数据
* 更改权限
* 生产环境变更
* 接受法律条款

审批控制的是拟议的操作。它不会撤销已经完成的工作。

## 审查操作

Auto Review（自动审查）会检查你的 Bot 即将采取的每个操作，例如在它运行命令、使用已连接的应用或使用其计算机之前。大多数操作会自行运行。当某个操作需要你的同意时，Bot 会在你的聊天中显示一张审批卡，包含拟议的操作及其输入，并等待你的回答。匹配你某条 **Ask first** 规则的操作总会显示卡片。批准前请审查目标、范围和值。

Auto Review 会考虑你在自己消息中要求的内容。来自其他地方的文本，例如电子邮件或网页，不算作你的请求。有些卡片带有警告，例如 **This can't be undone**、**This changes sign-in or security settings** 或 **This shares your data outside this chat**。

* **Allow once：** Bot 现在就执行该操作。不会保存规则。
* **Always allow：** Bot 现在就执行该操作，并把一条 Allow 规则保存到你的 Custom Rules，使类似操作自行运行。卡片会显示 **Saved to Custom Rules**。
* **Deny：** Bot 不执行该操作。在你发送另一条消息之前，它不会再次尝试该操作，也不会就此事询问你。

有些卡片使用其他标签。终端命令的卡片显示 **Allow** 和 **Skip**，以及 **Manage settings**（打开你的 Auto Review 设置）。被你的某条 **Ask first** 规则暂停的卡片显示 **Allow** 和 **Not now**，**Edit rule** 会打开你的 Custom Rules。当卡片没有可提供的规则时，你会看到 **Allow** 而不是 **Allow once**，也没有 **Always allow**。在手机上，点击卡片可查看完整请求及其所有按钮。

对于 Bot 从[它自己的地址](https://docs.x.ai/grok-bot/computer-and-apps#give-your-bots-an-email-address)发送的电子邮件：

* 当你在聊天中要求发送电子邮件时，一旦 Auto Review 允许，它就会发出。如果 Auto Review 需要你处理，你会先看到一张审批卡。
* 来自例程、收到的消息，或其他并非由该请求启动的工作的电子邮件，会作为草稿等待，直到你按下 **Send**。
* 转发，或带有 Auto Review 无法完整读取的附件的电子邮件，总是等待你的同意。

不要批准你无法确定其目标或效果的操作。请让 Bot 用通俗语言解释，或先产出一份草稿。

### 如果你不回答

当工作由聊天消息启动时，卡片会等待回答，不会按计时器过期。当卡片由例程、收到的消息或其他后台工作触发时，它会在 30 分钟后过期。如果你不回答而是发送新消息，该聊天中任何打开的卡片都会关闭；更改你的 Auto Review 设置也会关闭打开的卡片。

已关闭的卡片会显示 **Expired**，并说明 Bot 未执行该操作。如果卡片提供了规则，你仍然可以按 **Always allow next time**；Bot 会保存该规则，并在下次继续执行。要现在完成任务，请让 Bot 重试。

### 共享 Bot 与群聊

在[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)上，每位队友在各自与 Bot 的聊天中回答自己请求的卡片。在 Slack 线程中，卡片有 **Allow once**、**Deny** 和 **View details**，只有提出请求的人可以回答。在群聊中，只有 Bot 正在回答其消息的人可以批准；其他人会看到卡片正在等待谁，而群聊卡片不提供 **Always allow**。

审批卡询问 Bot 是否可以采取某个操作。[Secure Form](https://docs.x.ai/grok-bot/vault#secure-forms) 收集密码、密钥或其他机密，而连接卡要求你登录一个[应用](https://docs.x.ai/grok-bot/computer-and-apps#connect-an-app)，以便 Bot 可以使用它。

## 配置 Auto Review

Auto Review 默认开启。对于每个操作，它要么允许操作运行，要么让 Bot 先询问你；你的 Custom Rules 可以针对你在意的操作更改这一选择。无论你的规则如何，内置安全检查始终适用。

**Auto-review** 开关位于 **Settings → General** 下的 **Bot** 中；在 iPhone 和 Android 上，它位于 **Settings** 的 **Bot** 组中。关闭 Auto Review 后，Bot 会不经检查就运行操作，你的 Custom Rules 会被隐藏且不被使用，但会保留；重新开启即可再次使用它们。

Auto Review 开启时，桌面端会在开关下方显示 **Custom Rules**；在手机上，点击 **Bot** 组中的 **Custom Rules**。要添加规则：

1. 在 **When Grok Bot wants to:** 下，用通俗的话描述一个操作，例如「替我回复电子邮件」。
2. 在 **It should:** 下，选择 **Allow automatically** 或 **Ask first**。
3. 按 **Add Rule**。

在桌面端，使用规则旁的编辑按钮，进行更改后按 **Save Rule**，或按 **Cancel** 保持原样；使用删除按钮将其移除。在手机上，点击规则打开它，然后按 **Save Rule** 或 **Delete Rule**。

* **Ask first** 规则总会为你拦截匹配的操作。
* **Allow automatically** 规则仅在自动审查未发现其他阻止理由时，才让匹配的操作继续。
* 如果两类规则都匹配，**Ask first** 优先。

你最多可以有 20 条 **Allow automatically** 规则和 20 条 **Ask first** 规则，每条规则最长 1,000 个字符。如果你已经有 20 条 Allow 规则，卡片上的 **Always allow** 会移除你最早的一条 Allow 规则以腾出空间，并告诉你移除了哪条规则。

如果你的管理员要求启用 Auto Review，开关会保持开启，并显示 **Required by your admin. You can't turn this off.** 团队规则会出现在同一张表中，带有 **Required by your admin. You can't edit or delete this rule.** 团队规则始终适用；你自己的规则只适用于你，叠加在团队规则之上，并且只能让行为更严格。你的团队还可以分享适用于你的 Bot 的规则，以替代你自己的规则；内置安全检查仍然适用。参见[自动审查规则](https://docs.x.ai/grok-bot/teams-and-enterprises#auto-review-rules)。

为每个操作写一条简短、范围窄的规则，围绕已知的操作和范围：

* 在发送任何外部电子邮件之前先询问。
* 在更改生产仪表盘之前先询问。
* 在 `/workspace/reports` 中运行 `git status` 时自动允许。

避免宽泛的规则，例如「允许浏览器中的一切」。网站和工具行为会随时间变化。Auto Review 基于模型，应当补充而非替代最小权限原则和明确的审批边界。

个人 Auto-review 规则会保存到你的账户，因此会从每台桌面和移动应用生效。

## 让密码和支付信息远离聊天

Bot 在看不到机密值的情况下登录和结账。Bot 会优先使用保存在 [Vault](https://docs.x.ai/grok-bot/vault) 中的登录信息，然后使用已连接的密码管理器（例如 1Password），最后才通过 Secure Form 询问你。来自 Vault 和 Secure Form 的值会被填入页面，而不会展示给模型。

当表单无法完成该步骤时，例如单点登录、通行密钥（passkey）、CAPTCHA、在另一台设备上批准，或银行卡验证，Bot 会把计算机交给你：

1. 在对话中的请求上选择 **Take over**，或打开计算机并选择 **Take control**。
2. 完成敏感步骤。
3. 选择 **I'm done**，然后告诉 Bot 继续。

不要在普通聊天中发送密码、一次性验证码或 API 密钥。对于 API 密钥或其他机密，请在 Bot 询问时在安全机密卡中输入；该值会被遮蔽，从对话记录中排除，也不会展示给模型。

保存在 Vault 中的卡片会在结账时填入，无需每次单独批准。如果你想批准每一笔支付，就不要保存卡片：在 Secure Form 中输入时，不勾选 **Securely save to Bot's vault**，或在 **Settings → Vault** 中将其移除。

如果你使用硬件安全密钥（例如 YubiKey）登录，在 **Settings → General → Security Key** 下的 **Use hardware security keys** 开启时，Bot 的浏览器可以使用插入你桌面的密钥。该设置在 macOS 和 Windows 上默认开启，在 Linux 上尚不支持；每次使用都会先要求你批准。

## 控制对你本地计算机的访问

共享的 Grok Bot 计算机运行在云端。对你面前的 Mac 或 Windows 计算机的访问是一项单独的能力。

在 **Settings → Computer → Your computer** 中，在 **Execution on this computer** 下选择 **Ask every time**、**Always allow** 或 **Never allow**。每台列出的桌面都有自己的设置；在桌面被列出之前，页面会改为显示 **Execution on Local Computer**。

默认是 **Ask every time**。除非 Bot 有特定理由处理你的本地文件，否则请使用 **Never allow**。你的团队管理员可以为整个团队设定此设置的上限；当团队策略比你的更严格时，以团队策略为准。这些设置不会阻止 Bot 使用其云端计算机。

当 Bot 使用你手机上的应用时，团队的上限同样适用。参见[让 Bot 使用你手机上的应用](https://docs.x.ai/grok-bot/mobile#let-a-bot-use-your-phones-apps)。

当 Bot 第一次请求在你的计算机上运行命令时，对话会显示 **Allow Grok Bot and all Bots to run commands on your local computer?**，并带有 **Always allow**、**Allow once**、**Never** 和 **Deny once**（Esc）。**Always allow** 和 **Never** 会为每个 Bot 设置 **Execution on Local Computer**，你可以稍后在 Settings 中更改该设置。如果你团队的管理员设定了更严格的上限，**Always allow** 将不可用。

## 理解共享计算机的边界

你的所有 Bot 共用一个分配给你用户账户的云计算机。该计算机上的文件、浏览器会话和命令行凭据在你的整个 Bot 阵容中都可访问。

* 不要把不同的 Bot 当作安全边界。
* 当某个服务不应再可用时，请退出登录。
* 工作完成后移除敏感的临时文件。
* 不再需要访问时，删除连接器或在源服务中撤销其授权。

不要把这套用户分配机制当作比 Cursor 已发布的安全文档更宽泛的保证。请在那里查看当前的基础设施和加密控制。

## 分享 Bot 不是安全边界

公开分享链接让他人可以复制 Bot 的配置。它不会分享你的计算机或登录信息。尽管如此，不要在你分享的 Bot 中放入机密、客户数据或内部 URL。参见[分享 Bot](https://docs.x.ai/grok-bot/bots#share-a-bot)和[第三方 bot 条款](https://x.ai/legal/bot-sharing-terms)。

[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)不同：队友与同一个 Bot 聊天，其所有者添加的应用、机密、技能和文件会在每位队友的聊天中生效。只添加你乐于让所有与你分享它的人使用的密钥和文件。

## Cursor 账户与数据设置

Grok Bot 使用 Cursor 的身份验证和账户数据设置。

* Grok Bot 需要数据存储，不支持旧版隐私模式（Legacy Privacy Mode）。
* 隐私和数据共享选择通过 Cursor 账户设置管理，并在需要时通过 Grok Bot 访问流程管理。
* 训练退出（opt-out）遵循适用的 Cursor 账户和隐私设置。
* 请查看当前的 [Cursor 隐私政策](https://cursor.com/privacy)和[安全信息](https://cursor.com/security)，了解合同细节。

组织管理员可以限制本地计算机执行，并可能为云计算机提供托管设置。可用的控制取决于组织的推出情况和套餐。

## 移除访问权限和工作数据

当某个项目或登录不应再可用时：

1. 暂停或删除相关的例程。
2. 在共享计算机上退出网站登录。
3. 卸载连接器，并在源服务中撤销其授权。
4. 从 `/workspace` 中移除敏感项目文件。
5. 隐藏或删除不应再出现在 Grok Bot 中的 Bot。
6. 如果需要删除 Cursor 账户，请使用账户设置流程。

删除 Bot 不会移除共享计算机上的文件或浏览器会话。后端保留和账户删除遵循适用的 Cursor 条款。

## 使用最小权限设置

* 只连接工作流需要的工具。
* 在源系统支持的情况下，使用范围受限的服务账户。
* 从只读任务和草稿输出开始。
* 让发送、发布、购买、删除和生产变更保持在审批之后。
* 定期审查已安装的连接器和活跃的例程。
* 当例程的源系统或预期工作流发生变化时，暂停该例程。
* 为重要决策保留来源链接和操作日志。

有关在 X Chat 中使用 Grok Bot 的信息，参见[在 X Chat 中使用 Grok Bot](https://help.x.com/using-x/about-grok#grok-bot)。
