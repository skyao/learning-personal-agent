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
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-29T00:00:00Z）；2026-11-28 发现原文更新：Shared Bots 改称 Team Bots；已有 20 条允许规则时「总是允许」改为替换最旧一条；新增聊天中 Bot 可看到 Vault 所存银行卡的号码和安全码以便结账"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 的安全文档面向管理员，这页面向用户，重合不多。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Auto Review 默认开启，用模型判断哪些操作需要用户确认；审批卡有 **Allow once**、**Always allow**、**Deny** 三种选择，**Always allow** 会存成规则，拒绝后 Bot 在用户发新消息前不会再尝试。从聊天发起的审批卡一直等待，后台任务发起的卡 30 分钟后过期。自定义规则「Allow automatically」「Ask first」各最多 20 条，每条最多 1,000 字符；已有 20 条允许规则时，卡上的 **Always allow** 会替换最旧的一条。Vault 中的登录和 Secure Form 的值填入页面时不给模型看，但在 Grok Bot 应用的聊天里，Bot 能看到 Vault 中所存银行卡的号码和安全码，用于结账。在用户本地电脑上执行命令默认 **Ask every time**，每台桌面单独设置，团队管理员可设上限。文档明确说云端电脑由用户名下所有 Bot 共用，分享 Bot 也不是安全边界；Team Bot 里所有者添加的应用、密钥、技能和文件对每位队友的聊天都生效；删除 Bot 不会清除共享电脑上的文件。

**保留理由**：给出了用户侧审批机制的具体规则（超时、规则数量、默认值），以及官方自己承认的安全边界。

---

审批、安全与隐私

Grok Bot 的设计目标是完成工作，同时让敏感输入和重要操作保持在你控制之下。请把审批、安全交接和清晰的 Bot 边界一起使用。

## 在请求中设定边界

告诉 Bot 它可以采取哪些操作，以及必须在哪里停下：

> Reconcile the campaign data and draft a recommended budget change. Do not change the campaign or message the agency. Ask for approval after showing the current value, proposed value, and expected impact.

（译注：意为「核对营销活动数据，起草一份建议的预算调整。不要更改活动，也不要联系代理机构。在展示当前值、建议值和预期影响后请求批准。」）

以下情况尤其要使用明确边界：

* 发送消息或邀请
* 发布内容
* 购买和资金转账
* 删除或覆盖数据
* 更改权限
* 生产环境变更
* 接受法律条款

审批控制的是拟执行的操作，不会逆转已经完成的工作。

## 审查操作

Auto Review 会检查你的 Bot 即将采取的每个操作，例如在它运行命令、使用已连接应用或使用其计算机之前。大多数操作会自行运行。当某个操作需要你同意时，Bot 会在聊天中显示审批卡，写明拟执行的操作及其输入，并等待你的回答。匹配你某条 **先询问** 规则的操作总会弹出卡片。批准前请检查目标、范围和值。

Auto Review 会考虑你在自己消息中提出的要求。来自别处的文字，例如邮件或网页，不算你的请求。有些卡片会带警告，例如 **此操作无法撤销（This can't be undone）**、**这会更改登录或安全设置（This changes sign-in or security settings）** 或 **这会把你的数据分享到本聊天之外（This shares your data outside this chat）**。

* **允许一次（Allow once）：** Bot 现在执行该操作。不保存规则。
* **始终允许（Always allow）：** Bot 现在执行该操作，并向你的自定义规则保存一条允许规则，让类似操作以后自行运行。卡片会显示 **已保存到自定义规则（Saved to Custom Rules）**。
* **拒绝（Deny）：** Bot 不执行。在你发送另一条消息之前，它不会再次尝试该操作，也不会再问你。

有些卡片使用其他标签。终端命令的卡片显示 **允许（Allow）** 和 **跳过（Skip）**，还有 **管理设置（Manage settings）**，它会打开你的 Auto Review 设置。被你的某条 **先询问** 规则暂停的卡片显示 **允许** 和 **暂不（Not now）**，**编辑规则（Edit rule）** 会打开你的自定义规则。当卡片没有可提供的规则时，你会看到 **允许** 而不是 **允许一次**，也没有 **始终允许**。在手机上，点击卡片可查看完整请求及其所有按钮。

对于 Bot 从[自己的地址](https://docs.x.ai/grok-bot/computer-and-apps#give-your-bots-an-email-address)发出的邮件：

* 当你在聊天中要求发邮件时，Auto Review 允许后它就会发出。如果 Auto Review 需要你，你会先看到一张审批卡。
* 来自例程、收到的消息，或其他不是你用该请求发起的工作的邮件，会作为草稿等待你按下 **发送（Send）**。
* 转发，或带有 Auto Review 无法完整读取的附件的邮件，总是等待你同意。

不要批准你无法识别目标或影响的操作。请 Bot 用平实的语言解释，或先产出一份草稿。

### 如果你没有回答

当工作从聊天消息开始时，卡片会等待回答，不会按计时器过期。当例程、收到的消息或其他后台工作升起卡片时，它会在 30 分钟后过期。如果你不回答而是发送新消息，该聊天中任何打开的卡片都会关闭；更改 Auto Review 设置也会关闭打开的卡片。

关闭的卡片显示 **已过期（Expired）**，并说明 Bot 没有执行该操作。如果卡片提供过规则，你仍然可以按 **下次始终允许（Always allow next time）**；Bot 会保存规则，下次可以继续。要现在完成任务，请让 Bot 重试。

### Team Bot 与群聊

在 [Team Bot](https://docs.x.ai/grok-bot/team-bots) 上，每位队友在自己的聊天中为自己发起的请求回答卡片。在 Slack 线程中，卡片有 **允许一次**、**拒绝** 和 **查看详情（View details）**，只有提出问题的人可以回答。在群聊中，只有 Bot 正在回答其消息的那个人可以批准；其他人会看到卡片在等谁，而且群聊卡片不提供 **始终允许**。

审批卡问的是 Bot 是否可以采取某个操作。[安全表单（Secure Form）](https://docs.x.ai/grok-bot/vault#secure-forms)收集密码、密钥或其他机密，连接卡则要求你登录一个[应用](https://docs.x.ai/grok-bot/computer-and-apps#connect-an-app)，以便 Bot 使用它。

## 配置 Auto Review

Auto Review 默认开启。对于每个操作，它要么让操作运行，要么让 Bot 先问你；你的自定义规则可以对你关心的操作改变这一选择。无论你的规则怎么说，内置安全检查始终适用。

**Auto-review** 开关位于 **设置 → 通用** 的 **Bot** 下；在 iPhone 和 Android 上，它位于 **设置** 的 **Bot** 组中。关闭 Auto Review 后，Bot 运行操作前不再检查，你的自定义规则会隐藏且不再使用，但会保留；重新开启即可再次使用。

Auto Review 开启时，桌面上开关下方会出现 **自定义规则**；在手机上，点击 **Bot** 组中的 **自定义规则**。添加规则的方法：

1. 在 **当 Grok Bot 想要：（When Grok Bot wants to:）** 下，用平实的语言描述一个操作，例如「替我回复邮件」。
2. 在 **它应该：（It should:）** 下，选择 **自动允许（Allow automatically）** 或 **先询问**。
3. 按 **添加规则（Add Rule）**。

在桌面端，使用规则旁的编辑按钮，做出更改，然后按 **保存规则（Save Rule）**，或按 **取消（Cancel）** 保持原样；使用删除按钮移除规则。在手机上，点击规则打开它，然后按 **保存规则** 或 **删除规则（Delete Rule）**。

* **先询问** 规则总是为你拦下匹配的操作。
* **自动允许** 规则只在自动审查没有发现其他阻止理由时，才让匹配的操作继续。
* 如果两种规则都匹配，**先询问** 优先。

你最多可以有 20 条 **自动允许** 规则和 20 条 **先询问** 规则，每条规则最多 1,000 个字符。如果你已经有 20 条允许规则，卡片上的 **始终允许** 会替换你最旧的一条允许规则。

如果你的管理员要求 Auto Review，开关会保持开启，并显示 **你的管理员要求开启。你不能关闭此项。（Required by your admin. You can't turn this off.）** 团队规则会出现在同一张表中，并带有 **你的管理员要求此项。你不能编辑或删除此规则。（Required by your admin. You can't edit or delete this rule.）** 团队规则始终适用；你自己的规则只适用于你，叠在团队规则之上，而且只能让行为更严格。你的团队也可以共享规则，取代你自己的规则适用于你的 Bot；内置安全检查仍然适用。见 [Auto-review 规则](https://docs.x.ai/grok-bot/teams-and-enterprises#auto-review-rules)。

为每个操作写一条简短、狭窄的规则，围绕已知的操作和范围：

* 发送任何外部邮件前先询问。
* 更改生产仪表盘前先询问。
* 在 `/workspace/reports` 中运行 `git status` 时自动允许。

避免「允许浏览器里的一切」这类宽泛规则。网站和工具行为会随时间变化。Auto Review 基于模型，应补充而不是取代最小权限和明确的审批边界。

个人 Auto-review 规则保存到你的账户，因此会从每台桌面和移动应用生效。

## 让密码和支付信息远离聊天

Bot 登录时看不到你的密码。Bot 会先使用保存在 [Vault](https://docs.x.ai/grok-bot/vault) 中的登录信息，然后使用已连接的密码管理器，例如 1Password，最后才用安全表单问你。来自 Vault 的登录信息和来自安全表单的值会填入页面，不会展示给模型。在 Grok Bot 应用的聊天中，Bot 可以看到你保存在 Vault 中的银行卡号码和安全码，以便在结账时输入。见 [Vault 保存什么](https://docs.x.ai/grok-bot/vault#what-vault-holds)。

当表单无法完成某一步时，例如单点登录、通行密钥（passkey）、CAPTCHA、在另一台设备上批准或银行卡验证，Bot 会把计算机交给你：

1. 在对话中的请求上选择 **接管（Take over）**，或打开计算机并选择 **取得控制（Take control）**。
2. 完成敏感步骤。
3. 选择 **我完成了（I'm done）**，然后告诉 Bot 继续。

不要在普通聊天中发送密码、一次性验证码或 API 密钥。对于 API 密钥或其他机密，在 Bot 要求时输入到安全密钥卡中；其值会被遮蔽、排除在对话记录之外，也不会展示给模型。

保存在 Vault 中的卡在结账时会直接填入，无需每次单独批准。如果你想逐笔批准付款，就不要保存该卡：在安全表单中输入时，让 **安全保存到 Bot 的 Vault（Securely save to Bot's vault）** 保持未勾选，或在 **设置 → Vault** 中移除它。

如果你使用硬件安全密钥（例如 YubiKey）登录，当 **设置 → 通用 → 安全密钥（Security key）** 下的 **使用硬件安全密钥（Use hardware security keys）** 开启时，Bot 的浏览器可以使用插在你桌面上的密钥。该设置在 macOS 和 Windows 上默认开启，Linux 尚不支持；每次使用都会先请求你批准。

## 控制对本地计算机的访问

共享的 Grok Bot 计算机运行在云端。对你面前这台 Mac 或 Windows 计算机的访问，是一项单独的能力。

在 **设置 → 计算机 → 你的计算机** 中，于 **在本计算机上执行** 下选择 **每次询问（Ask every time）**、**始终允许（Always allow）** 或 **从不允许（Never allow）**。每台列出的桌面都有自己的设置；在桌面被列出之前，页面会改为显示 **在本地计算机上执行（Execution on local computer）**。

默认是 **每次询问**。除非 Bot 有具体理由处理你的本地文件，否则请使用 **从不允许**。你的团队管理员可以为整个团队设定此设置的上限；当团队策略比你的更严格时，团队策略适用。这些设置不会阻止 Bot 使用其云计算机。

当 Bot 使用你手机上的应用时，团队的上限同样适用。见[让 Bot 使用你手机上的应用](https://docs.x.ai/grok-bot/mobile#let-a-bot-use-your-phones-apps)。

当 Bot 第一次请求在你的计算机上运行命令时，对话会显示 **允许 Grok Bot 和所有 Bot 在你的本地计算机上运行命令吗？（Allow Grok Bot and all Bots to run commands on your local computer?）**，并带有 **始终允许**、**允许一次**、**从不（Never）** 和 **拒绝一次（Deny once）**（Esc）。**始终允许** 和 **从不** 会为所有 Bot 设置 **在本地计算机上执行**，你之后可以在设置中更改。如果你的团队管理员设定了更严格的上限，**始终允许** 不可用。

## 理解共享计算机边界

你的所有 Bot 共用分配给你用户账号的一台云计算机。那台计算机上的文件、浏览器会话和命令行凭证，在你的整个 Bot 列表中都可以使用。

* 不要用分开的 Bot 当作安全边界。
* 当某个服务不应再可用时，退出登录。
* 工作完成后，移除敏感的临时文件。
* 当不再需要访问权时，删除连接器或在源服务中撤销其授权。

不要把这套用户分配当作比 Cursor 公开安全文档更宽泛的保证。请在那里查看当前的基础设施和加密控制。

## 分享 Bot 不是安全边界

公开分享链接会让别人复制 Bot 的配置。它不会分享你的计算机或登录信息。尽管如此，不要在你分享的 Bot 中放入机密、客户数据或内部 URL。见[分享 Bot](https://docs.x.ai/grok-bot/bots#share-a-bot)和[第三方 Bot 条款](https://x.ai/legal/bot-sharing-terms)。

[Team Bot](https://docs.x.ai/grok-bot/team-bots) 不同：队友与同一个 Bot 聊天，其所有者添加的应用、机密、技能和文件会在每位队友的聊天中生效。只添加你乐于让所有共享对象使用的密钥和文件。

## Cursor 账户与数据设置

Grok Bot 使用 Cursor 的认证和账户数据设置。

* Grok Bot 需要数据存储，不支持旧版隐私模式（Legacy Privacy Mode）。
* 隐私和数据共享选择通过 Cursor 账户设置管理，必要时也通过 Grok Bot 的访问流程管理。
* 训练退出遵循适用的 Cursor 账户和隐私设置。
* 合同细节请查看当前的 [Cursor 隐私政策](https://cursor.com/privacy)和[安全信息](https://cursor.com/security)。

组织管理员可以限制本地计算机执行，并可为云计算机提供受管设置。可用控制项取决于组织的发布范围和套餐。

## 移除访问权与工作数据

当某个项目或登录不应再可用时：

1. 暂停或删除相关例程。
2. 在共享计算机上退出网站登录。
3. 卸载连接器，并在源服务中撤销其授权。
4. 从 `/workspace` 中移除敏感项目文件。
5. 隐藏或删除不应再出现在 Grok Bot 中的 Bot。
6. 如果需要删除 Cursor 账户，请使用账户设置流程。

删除 Bot 不会移除共享计算机上的文件或浏览器会话。后端保留和账户删除遵循适用的 Cursor 条款。

## 使用最小权限设置

* 只连接工作流需要的工具。
* 在源系统支持时，使用有范围限制的服务账号。
* 从只读任务和草稿输出开始。
* 把发送、发布、购买、删除和生产变更留在审批之后。
* 定期检查已安装的连接器和活动例程。
* 当源系统或预期工作流变化时，暂停例程。
* 为重要决定保留来源链接和操作日志。

关于在 X Chat 中使用 Grok Bot，见[在 X Chat 中使用 Grok Bot](https://help.x.com/using-x/about-grok#grok-bot)。
