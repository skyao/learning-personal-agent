---
title: "文档（docs.x.ai）：常见问题"
linkTitle: "docs.x.ai：常见问题"
date: 2026-10-28
originalTitle: "Frequently asked questions"
sourceUrl: "https://docs.x.ai/grok-bot/faq"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：Shared Bots 改称 Team Bots；新增 Grok Business 席位用量按席位许可（SuperGrok 或 Heavy）计、席位移除即失去访问；Grok 账号已关联他处时联系支持；语言数改为各 38 种"
tags: [开放与价格, 模型, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 帮助页「套餐」「模型」与这页部分重合，订阅与试用的规则只在这页集中出现。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Grok Bot 包含在 X 订阅的 Premium、Super、Ultra 中（Plus 和免费版不含），原 Cursor 的 Pro、Pro+、Ultra、Teams 套餐也包含；可以关联 SuperGrok 或 X Premium+ 账号使用，Grok Business 席位用量按席位许可（**SuperGrok** 或 **SuperGrok Heavy**）计，管理员移除席位后访问即结束。周额度用完后，原 Cursor 套餐可开按需计费，X 订阅用预付额度和 Auto Top-up。试用给一笔用量额度和 7 天期限，不会自动转为付费，App Store 的试用则由苹果管理并会转为付费订阅。模型由系统自动选择，不显示也不能选，可能是第一方模型，也可能是子处理方名单中的第三方模型。桌面端支持 macOS、Windows、Linux，手机端要求 iOS 18 以上或 Android 9 以上，桌面和手机应用各有 38 种语言；删除账号即删除 Cursor 账号，数据在 30 天内清除。

**保留理由**：集中说明了 Grok Bot 经 X 订阅和 Cursor 套餐两条路线收费的规则，以及「模型不可选、可能用第三方模型」的官方表述。

---

常见问题

## Grok Bot 与 AI 助手有什么不同？

Bot 可以使用持久的云计算机、已连接的工具、网站和文件来完成工作，而不只是回答问题。它们可以在后台继续运行，保留角色相关的上下文，并与其他 Bot 协作。

## Grok Bot 和 Grok 应用是同一个东西吗？

不是。Grok（SpaceXSI 的聊天应用）和 Grok Bot 是两个不同的应用。Grok 应用中的付费墙或**每周 SuperGrok 限额**（Weekly SuperGrok Limit）与 Grok Bot 无关。Grok Bot 使用你的 Cursor 账户登录。见[登录](https://docs.x.ai/grok-bot/get-started#2-sign-in)。

## 我在哪里与 Grok Bot 对话？

使用 macOS、Windows 或 Linux 上的 Grok Bot 桌面应用，或 iOS、Android 上的配套应用。相同的 Bot 和对话会在你已登录的设备之间同步。你也可以在 [X Chat](https://docs.x.ai/grok-bot/chat-and-collaboration#chat-in-x-chat) 中与 Bot 聊天，[在 X 上标记 @bot](https://docs.x.ai/grok-bot/tag-on-x) 把一条帖子交给你的 Bot，以及在 [Slack 中与 Team Bot 交谈](https://docs.x.ai/grok-bot/create-a-team-bot#add-it-to-slack)。

## 我合上笔记本电脑后 Grok Bot 还会继续工作吗？

会。Bot 的工作在云计算机上运行。关闭应用、笔记本电脑或手机不会停止后台回合或例程。

## Bot 会使用我自己的计算机吗？

Bot 在自己的云计算机上工作。只有你允许时，Bot 才会在你的桌面上运行命令。该设置位于**设置 → 计算机 → 你的计算机**下，名为**在此计算机上执行**（Execution on this computer）。如果那里还没有列出桌面，同一页面会显示**在本地计算机上执行**（Execution on local computer）。默认每次都会询问你。见[在你的桌面上运行命令](https://docs.x.ai/grok-bot/settings-and-notifications#run-commands-on-your-desktop)。

## 我的多个 Bot 共用一台计算机吗？

是。你账户中的每个 Bot 都使用同一台持久的云计算机。它们共享其文件、浏览器会话和登录，以便交接工作。

计算机按用户分配，而不是按 Bot 分配。不要把不同的 Bot 当作安全边界。

## 多个 Bot 可以同时工作吗？

可以。Bot 可以并行推理、使用连接器、处理文件并协调。每个 Bot 在共享计算机上有自己的屏幕。一个 Bot 一次可以在自己的屏幕上运行一个计算机使用任务。

## Bot 会记住什么？

Bot 可以保留稳定的偏好、角色上下文和先前工作的摘要。它的对话和学到的角色与其他 Bot 分开，但关于你的一些事实（例如你的姓名和时区）由你所有的 Bot 共享。共享文件、浏览器会话、群组消息和直接交接也可以在这些 Bot 之间传递上下文。要检查某个 Bot 记住了什么，问它：「你记得关于我的什么？」见[Bot 记住什么](https://docs.x.ai/grok-bot/bots#what-a-bot-remembers)。

对于重要决定，让 Bot 检查当前来源，而不是依赖记忆。

## Grok Bot 可以使用任何网站吗？

Grok Bot 可以使用许多基于浏览器的工具，包括没有专用连接器的服务。网站仍可能阻止自动化、要求重新登录、显示 CAPTCHA 或要求人工确认。Bot 应把这些步骤交给你，而不是绕过它们。

有些网站会阻止来自云计算机的流量。出现这种情况时，Bot 会把该步骤交给你，你可以自己在 Bot 的计算机上登录。你也可以在**设置 → 计算机**下的**你的计算机**中开启**通过此计算机转出流量**（Route traffic through this computer），让网站看到你自己的连接。如果网站反而超时或显示连接错误，见[网站超时或无法连接](https://docs.x.ai/grok-bot/troubleshooting#a-website-times-out-or-wont-connect)。

有连接器可用时，请使用连接器，以获得更结构化、更可靠的集成。

## 哪些操作需要我批准？

答案取决于工具、操作的风险，以及在启用强制实施时的自动审查（Auto-review）规则。敏感或后果重大的操作可能会停下来等待批准。Bot 使用来自 [Vault](https://docs.x.ai/grok-bot/vault) 的登录信息、已连接的密码管理器或安全表单登录，且看不到这些值；单点登录、通行密钥、CAPTCHA 等只有人才能完成的步骤通过接管计算机完成。

告诉每个 Bot 它的常设边界并让它记住，并为发送、发布、删除、购买或更改生产系统等操作添加范围很窄的**先询问**（Ask first）规则。

来自没有你在场时启动的工作（例如例程或另一个 Bot 的消息）的审批，约 30 分钟后过期。你所参与的聊天中的审批会等你。见[审批已过期或被阻止](https://docs.x.ai/grok-bot/troubleshooting#an-approval-expired-or-is-blocked)。

## 我可以选择模型吗？

不可以。Grok Bot 为每个任务选择模型，没有模型选择器。对每个任务，它使用最有可能带来最佳结果的后端模型。这可能是 SpaceXSI 的第一方模型，也可能是[子处理方名单](https://trust.cursor.com/subprocessors)上某家提供商的第三方模型，而且选择可能因请求而异。用户无法被路由到某个特定模型或远离某个特定模型。

Grok Bot 不显示请求底层使用的模型。你的用量和支出视图把这类活动记为 Grok Bot 用量，而不是按提供商或模型名记录。把任务路由到 Opus 5.5 不会改变你每个 token 的成本；你用完用量的速度取决于你交给 Grok Bot 的工作类型以及每个任务需要多少工作量。

你团队的 Cursor [模型允许列表或阻止列表](https://cursor.com/docs/enterprise/model-and-integration-management#model-access-control)不适用于 Grok Bot。设置模型允许列表的团队在[启用 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises#enabling-grok-bot-for-your-team)时会看到这一提示。只有子处理方名单上的提供商可以处理你的数据，模型集合会随时间变化。见[模型与数据](https://docs.x.ai/grok-bot/security#models-and-data)。

## Grok Bot 如何处理数据和隐私？

Grok Bot 使用 Cursor 的认证和账户数据设置。训练退出遵循适用的 Cursor 账户和隐私设置。

Grok Bot 需要云数据存储，因此不支持旧版隐私模式（Legacy Privacy Mode）。你所有的 Bot 都可以访问分配给你账户的同一台云计算机。完整边界以及指向当前 Cursor 安全信息的链接见[审批、安全与隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy)。

## 我需要单独订阅 Grok Bot 吗？

不需要。Grok Bot 随 The X Subscription 的 **Premium**、**Super** 和 **Ultra** 提供，也随旧版 **Cursor Pro**、**Pro+**、**Ultra** 和自助式 **Teams** 提供。在旧版 Cursor 账户上，你还可以关联个人 **SuperGrok**、**SuperGrok Plus**、**SuperGrok Heavy** 或 **X Premium+** 账户，或用持有自助式 **Grok Business** 套餐席位的 Grok 账户登录。在 Enterprise 上，请询问你的客户团队。

## Grok Bot 多少钱？

可用性和计费取决于账户和套餐。在 The X Subscription 上（新客户从这里开始），Grok Bot 包含在 Premium、Super 和 Ultra 中，适用于个人和团队席位；Plus 和 Free 不包含。在该订阅中，Grok Bot 与 Cursor 及 Grok 应用共用同一个每周用量池，预付额度覆盖超出用量池的部分。Super 和 Ultra 的每周用量池比 Premium 更大。在 [grok.com/dashboard](https://grok.com/dashboard) 的**用量**（Usage）下查看用量。

在旧版 Cursor 套餐上，Grok Bot 随每个付费个人套餐和 Cursor Teams 提供，你可以关联个人 SuperGrok、SuperGrok Plus、SuperGrok Heavy 或 X Premium+ 订阅。**Pro** 包含每周用量，**Pro+** 包含充裕的每周用量，**Ultra** 的每周用量最高。**每周用量限额**（Weekly usage limit）用完后，如果开启了按需用量，额外用量会以**按需用量**（On-demand usage）继续，通过 Cursor 计费。Grok Bot 用量在你的 Cursor 账户上计量，而不是在 Grok 或 X 上，macOS 和 iOS 共用同一用量。

见 [The X Subscription 上的 Grok Bot](https://docs.x.ai/x-subscription/grok-bot) 和[套餐与计费](https://grok.com/help/grok-bot/plans)。Enterprise 客户应联系其 Cursor 客户团队。

## 我可以关联哪些 Grok 套餐？

个人 **SuperGrok**、**SuperGrok Plus**、**SuperGrok Heavy** 和 **X Premium+**。**SuperGrok Lite** 和 **Grok Enterprise** 不能关联。如果你持有自助式 **Grok Business** 套餐的席位，不要从套餐页面关联。先退出登录，再用持有该席位的 Grok 账户通过**使用 Grok 登录**（Sign in with Grok）重新登录。Grok Bot 用量与席位上的许可证一致：**SuperGrok** 许可证获得 SuperGrok 用量，**SuperGrok Heavy** 许可证获得 SuperGrok Heavy 用量。如果管理员移除你的席位，来自该席位的 Grok Bot 访问权即结束。在 The X Subscription 上无需关联：Grok Bot 使用你套餐的共享每周用量池。见[为 Grok Bot 关联 SuperGrok](https://grok.com/help/grok-bot/supergrok)。

如果你看到 Grok 账户已关联到另一个 Cursor 账户的错误，或用正确的 Grok 账户登录后仍然没有访问权，请带上你的 Cursor 账户邮箱和 Grok 账户邮箱[联系支持](https://docs.x.ai/grok-bot/troubleshooting#before-contacting-support)。

## 我看不到「关联 Grok 账户」。

**关联 Grok 账户**（Link Grok Account）位于 [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding) 的 **Grok Bot 入门**页面，以及手机的付费墙页面。如果你已经有访问权，打开**设置 → 用量与计费**（Usage & billing），在**管理套餐**（Manage plan）下查看**通过 Grok 获取访问权**（Get access with Grok）。只有关联会提高你的用量时它才会出现。

## 我把 SuperGrok 关联到了错误的 Cursor 账户，可以取消关联吗？

不可以。关联是永久的，你无法自行迁移。[联系支持](https://docs.x.ai/grok-bot/troubleshooting#before-contacting-support)，告知获得关联的账户和本应获得关联的账户。关联是一种用量授予，不是 Cursor 套餐，因此不会改变或取消任一账户上的 Cursor 套餐。

## Cursor 套餐和 SuperGrok 会叠加吗？

不会。在旧版 Cursor 账户上，Grok Bot 使用两者中授予每周用量更多的一方。旧版 **Pro**、**SuperGrok** 和 **X Premium+** 属于同一档，**Pro+** 对应 **SuperGrok Plus**，**Ultra** 对应 **SuperGrok Heavy**。Grok Business 席位的作用与 SuperGrok 关联相同。要获得更多用量，升级到更高档位或开启按需用量。两个订阅各自保持计费；购买一个不会取消另一个。

如果你在关联后升级 SuperGrok，请最多等待 24 小时，让**每周用量限额**移到新档位。你不需要重新关联。

## 为什么我的 SuperGrok 限额与 Grok Bot 用量不一致？

它们是两个产品、两套独立的计量。Grok Bot 用量在你的 Cursor 账户上。在 Grok Bot 的**设置 → 用量与计费**下查看，而不是在 Grok 应用中。

## 每周用量用完后，我如何停止扣费？

在 The X Subscription 上，保持自动充值（Auto Top-up）关闭，或在 [grok.com/dashboard/billing](https://grok.com/dashboard/billing) 的**额外用量额度**（Additional usage credits）下设置每月额外用量上限。在旧版 Cursor 套餐上，关闭按需用量或设置上限：在 Grok Bot 中打开**设置 → 用量与计费 → 按需月度上限**（On-demand monthly limit），或在网页上前往 [cursor.com/dashboard](https://cursor.com/dashboard)，在**支出**（Spending）下设置**月度上限**（Monthly Limit）。上限不会在运行中途停止 Bot，因此正在运行的任务可能略微超出。如果按需用量关闭，Grok Bot 会在每周用量用完时停止，并在每周用量重置时恢复。

## 有免费试用吗？

有些账户可以在付费前试用 Grok Bot：访问页面提供**开始试用**（Start trial）时，选择它。试用是一笔用量额度，同时有 7 天期限。它永远不会变成付费套餐。额度按你的智能体所做的工作量消耗，以智能体步骤和 token 计量，而不是按你发送的消息数，因此从小处开始、把任务范围收紧，并在运行大型或长时间任务前在套餐页面查看用量。一个大任务可能用掉全部额度，已用额度不会恢复。

**取消试用**（Cancel Trial）出现在免费套餐账户上。取消不收费。在免费套餐中，你可以在桌面端的**设置 → 用量与计费**或 iPhone 和 Android 的**设置 → 用量**（Usage）中用**取消试用**提前结束。这会移除剩余的试用额度，且你无法再次开始试用。在付费套餐或 Teams 席位上，试用会自行结束。

在 iOS 应用中开始的 App Store 免费试用不同：它由 Apple 运营，除非你先取消，否则会变成付费的 Apple 订阅。见[管理或取消手机订阅](https://docs.x.ai/grok-bot/mobile#manage-or-cancel-a-phone-subscription)。

## Grok Bot 如何退款？

Grok Bot 没有单独的订阅，因此没有单独的退款路径。在 The X Subscription 上，退款遵循[发票与退款](https://docs.x.ai/x-subscription/invoices-and-refunds)，已经花掉的预付额度不予退还。在旧版 Cursor 套餐上，订阅退款遵循 Cursor 的[退款](https://cursor.com/help/account-and-billing/refunds)政策；Grok Bot 已消耗的按需用量以及带有用量的周期中途降级不予退款。商店购买的退款由 Apple 或 Google 处理。SuperGrok 和 X Premium+ 由 SpaceXSI 或 X 计费，不是 Cursor；SuperGrok 见 [Grok FAQ](https://docs.x.ai/grok/faq#can-i-get-a-refund-for-my-grok-or-supergrok-subscription)，X Premium+ 请联系 X。

## Grok Bot 对团队和企业可用吗？

可以。在自助式 Cursor Teams 套餐上，每位成员都在自己的 Cursor 账户上获得 Grok Bot，无需 Premium 席位或管理员申请，在旧版 Teams 套餐上按需用量默认开启。在 The X Subscription 的团队中，每个付费席位（Premium、Super 或 Ultra）都包含它。在 Cursor Enterprise 上，由管理员为团队启用 Grok Bot；请联系你的 Cursor 客户团队。按请求计费的 Teams 套餐和 Enterprise 席位不接受个人 SuperGrok 关联。见[面向团队和企业的 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises)。

## 我可以更改账户上的邮箱吗？

不可以。Cursor 账户上的邮箱无法更改。要使用不同的邮箱，请新建账户。见[更改你的邮箱地址](https://cursor.com/help/account-and-billing/change-email)。

## 我可以口述或与 Bot 交谈吗？

可以。在桌面端，按 `Cmd/Ctrl+D` 或选择**开始语音输入**（Start voice input）向输入框口述。在 iPhone 和 Android 上，用**开始听写**（Start dictation）口述。**开始语音聊天**（Start voice chat）在桌面端、iPhone 和 Android 上开始实时对话。Bot 还可以发送**语音留言**（voice memo），你可以在对话记录中播放。

## 桌面应用有哪些键盘快捷键？

见[键盘快捷键](https://docs.x.ai/grok-bot/chat-and-collaboration#keyboard-shortcuts)。听写使用 `Cmd/Ctrl+D`。设置使用 `Cmd/Ctrl+,`。**开始语音聊天**是一个按钮，没有快捷键。

## 我可以更改应用语言吗？

可以。在桌面端，打开**设置**，进入**通用**，在**外观**（Appearance）下选择**语言**（Language）。**跟随系统**（Follow system）使用你计算机的语言。在 iPhone 和 Android 上，打开**设置**并选择**语言**；**系统**（System）使用你手机的语言。桌面端和手机应用各有 38 种语言。

语言会改变应用的菜单和消息。新 Bot 会用该语言给你写信，除非你用另一种语言给它们写信。语音聊天有自己的**语言**设置。

## 我可以使用多个账户吗？

在桌面端，打开账户菜单并选择**切换账户**（Switch account）或**添加账户**（Add account）。设置中列出相同的账户；非活动行包含**移除**（Remove）。在 iPhone 和 Android 上，打开**设置**，在**切换账户**（Switch Account）下选择要切换到的账户，或选择**添加账户**（Add Account）。在非活动账户上滑动即可移除。

## 支持哪些平台？

* Apple silicon 和 Intel 上的 macOS
* x64 和 Arm64 上的 Windows
* x64 和 Arm64 上的 Linux，提供 `.deb` 包、`.rpm` 包或 AppImage
* iOS 18 或更高版本上的 iPhone
* Android 9 或更高版本

iOS 应用也可以在 iPadOS 18 或更高版本的 iPad 上运行。从 [cursor.com/dashboard/bot](https://cursor.com/dashboard/bot) 的 Grok Bot 页面获取桌面应用。

## 技能和例程有什么区别？

**技能**（skill）描述如何执行一项任务。**例程**（routine）把一套工作流分配给一个 Bot 并告诉它何时运行——按计划运行，或在支持的情况下在某个事件之后运行。

在把技能变成例程之前，先在一个真实的一次性任务上测试它。

## 我可以向 Bot 演示如何完成一项任务吗？

**教授任务**（Teach a task）可用时，从计算机视图中录制一个浏览器工作流。Bot 会把演示转成草稿技能，供你审核和测试。该功能可能逐步发布，录制时长限制为十分钟。

## 我可以把 Bot 分享给别人吗？

可以。打开 Bot 的详情，选择**分享**（Share），然后选择**创建副本**（Create a copy）。Bot 发布模板后，选择**发布**（Publish），然后选择**复制链接**（Copy link）。任何拿到链接的人都可以在 [x.ai](https://x.ai) 上预览，并把副本添加到自己的账户。他们不会得到你的计算机、登录信息或对话历史。如果你的团队限制模板分享，应用不会提供**创建副本**。

链接会暴露 Bot 的配置。分享前请清除密钥和任何机密内容。添加 Team Bot 即接受[第三方 bot 条款](https://x.ai/legal/bot-sharing-terms)。见[分享 Bot](https://docs.x.ai/grok-bot/bots#share-a-bot)。

要给团队一个所有人都与之交谈的 Bot，而不是每个人各自定制的副本，请发布 [Team Bot](https://docs.x.ai/grok-bot/team-bots)。

## 如果我删除 Bot 会怎样？

删除会从 Grok Bot 移除该 Bot 的活动配置、对话和例程。由于 Bot 共用一台计算机，该计算机上的文件和登录可能保留。后端保留遵循适用的 Cursor 条款。如果你以后可能需要它的工作，请改为隐藏 Bot。

## 如何删除我的 Grok Bot 账户？

Grok Bot 使用你的 Cursor 账户，因此删除它就是删除 Cursor 账户。删除是自助的，且永久有效。退出 Grok Bot 或卸载应用会保留账户，且无法在不删除 Cursor 账户的情况下删除 Grok Bot。

* **在 iPhone 或 Android 上：** 点击账户头像打开**设置**，点击你的账户，然后点击**删除账户**（Delete Account）并确认。在打开的浏览器页面中，登录，输入 **Delete**，然后再次确认。
* **在桌面端或网页上：** 如果订阅处于活动状态，先取消订阅。然后前往 [cursor.com/dashboard](https://cursor.com/dashboard)，打开**设置**，在**更多**（More）下找到**删除账户**（Delete Account），选择**删除**（Delete）并确认。桌面版 Grok Bot 可以让你退出登录，但不会删除账户。

删除会移除你的 Cursor 账户和 Grok Bot 访问权；Grok Bot 的智能体、聊天、计算机和已连接应用；以及 Cursor 聊天历史和设置。所有数据在 30 天内删除。你自己计算机上的文件会留在那里。App Store 或 Google Play 订阅、已关联的 SuperGrok 订阅和已关联的 X Premium+ 订阅是分开的：如果你不再需要，请分别通过 Apple、Google、Grok 或 X 取消。

在 cursor.com 上，**删除账户**对个人账户显示。如果你使用的是 Cursor Teams 或 Enterprise 席位，请询问团队管理员或[联系支持](https://docs.x.ai/grok-bot/troubleshooting#before-contacting-support)。
