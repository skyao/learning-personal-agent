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
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [开放与价格, 模型, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 帮助页「套餐」「模型」与这页部分重合，订阅与试用的规则只在这页集中出现。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Grok Bot 包含在 X 订阅的 Premium、Super、Ultra 中（Plus 和免费版不含），原 Cursor 的 Pro、Pro+、Ultra、Teams 套餐也包含；可以关联 SuperGrok 或 X Premium+ 账号使用。周额度用完后，原 Cursor 套餐可开按需计费，X 订阅用预付额度和自动充值。试用给一笔用量额度和 7 天期限，不会自动转为付费，App Store 的试用则由苹果管理并会转为付费订阅。模型由系统自动选择，不显示也不能选，可能是第一方模型，也可能是子处理方名单中的第三方模型。桌面端支持 macOS、Windows、Linux，手机端要求 iOS 18 以上或 Android 9 以上；删除账号即删除 Cursor 账号，数据在 30 天内清除。

**保留理由**：集中说明了 Grok Bot 经 X 订阅和 Cursor 套餐两条路线收费的规则，以及「模型不可选、可能用第三方模型」的官方表述。

---

常见问题

## Grok Bot 与 AI 助手有何不同？

Bot 可以使用持久化的云端电脑、连接的工具、网站和文件来完成工作，而不只是回答问题。它们可以在后台继续工作、保留角色专属上下文，并与其他 Bot 协作。

## Grok Bot 与 Grok 应用是同一个东西吗？

不是。Grok（SpaceXSI 出品的聊天应用）和 Grok Bot 是两个不同的应用。Grok 应用中的付费墙或**每周 SuperGrok 上限（Weekly SuperGrok Limit）**与 Grok Bot 无关。Grok Bot 使用你的 Cursor 账号登录。参见[登录](https://docs.x.ai/grok-bot/get-started#2-sign-in)。

## 我在哪里与 Grok Bot 对话？

使用 macOS、Windows 或 Linux 上的 Grok Bot 桌面应用，或 iOS 或 Android 上的配套应用。相同的 Bot 和对话会在你登录的设备之间同步。你也可以在 [X Chat](https://docs.x.ai/grok-bot/chat-and-collaboration#chat-in-x-chat) 中与你的 Bot 聊天，在 X 上[标记 @bot](https://docs.x.ai/grok-bot/tag-on-x) 把帖子交给你的 Bot，以及在 Slack 中与[共享 Bot](https://docs.x.ai/grok-bot/shared-bots#how-do-i-add-a-shared-bot-to-slack)对话。

## 我的笔记本电脑合上时 Grok Bot 还会继续工作吗？

会。Bot 的工作在云端电脑上运行。关闭应用、笔记本电脑或手机不会停止后台回合或例程。

## Bot 会使用我自己的电脑吗？

Bot 在它们自己的云端电脑上工作。只有你允许时，Bot 才会在你的桌面上运行命令。该设置位于**设置 → 电脑 → 你的电脑（Settings → Computer → Your computer）**，标签为**在这台电脑上执行（Execution on this computer）**。如果那里还没有列出桌面，同一页面会显示**在本地电脑上执行（Execution on Local Computer）**。默认情况下，它每次都会询问你。参见[在你的桌面上运行命令](https://docs.x.ai/grok-bot/settings-and-notifications#run-commands-on-your-desktop)。

## 我的 Bot 共用一台电脑吗？

是的。你账号上的每个 Bot 都使用一台持久化的云端电脑。它们共享其文件、浏览器会话和登录信息，以便交接工作。

电脑是按用户分配的，而不是按 Bot 分配。不要把单独的 Bot 当作安全边界。

## 多个 Bot 可以同时工作吗？

可以。Bot 可以并行推理、使用连接器、处理文件并协调。每个 Bot 在共享电脑上有自己的屏幕。一个 Bot 一次只能在其屏幕上运行一个计算机使用（computer use）任务。

## Bot 会记住什么？

Bot 可以保留稳定的偏好、角色上下文和先前工作的摘要。它的对话和学到的角色与其他 Bot 分开，但关于你的一些事实（例如你的姓名和时区）会由你所有的 Bot 共享。共享文件、浏览器会话、群组消息和直接交接也可以在它们之间传递上下文。要检查某个 Bot 记住了什么，问它：「你记得关于我的什么？」参见[Bot 记住什么](https://docs.x.ai/grok-bot/bots#what-a-bot-remembers)。

对于重要决定，让 Bot 检查当前来源，而不是依赖记忆。

## Grok Bot 可以使用任何网站吗？

Grok Bot 可以使用许多基于浏览器的工具，包括没有专用连接器的服务。网站仍可能阻止自动化、要求重新登录、显示 CAPTCHA（验证码），或要求人工确认。Bot 应把这些步骤交给你，而不是绕过它们。

有些网站会阻止来自云端电脑的流量。发生这种情况时，Bot 会把该步骤交给你，你可以自己在 Bot 的电脑上登录。你也可以在**设置 → 电脑（Settings → Computer）**的**你的电脑**下开启**通过这台电脑路由流量（Route traffic through this computer）**，让网站看到你自己的连接。如果网站反而超时或显示连接错误，参见[网站超时或无法连接](https://docs.x.ai/grok-bot/troubleshooting#a-website-times-out-or-wont-connect)。

有连接器可用时，使用连接器可获得更结构化、更可靠的集成。

## 哪些操作需要我的批准？

答案取决于工具、操作的风险，以及（在启用强制执行时）你的**自动审查规则（Auto-review rules）**。敏感或后果重大的操作可能停下来等待批准。Bot 使用来自 [Vault](https://docs.x.ai/grok-bot/vault)、已连接的密码管理器或安全表单（Secure Form）的登录信息登录，而看不到其中的值；单点登录、通行密钥、CAPTCHA 以及类似只能由人完成的步骤会使用电脑接管。

告诉每个 Bot 它的长期边界，并让它记住这些边界，同时为发送、发布、删除、购买或更改生产系统等操作添加范围较窄的**先询问（Ask first）**规则。

在你不在场时开始的工作（例如例程或来自另一个 Bot 的消息）的批准会在约 30 分钟后过期。你所在聊天中的批准会等你。参见[批准已过期或被阻止](https://docs.x.ai/grok-bot/troubleshooting#an-approval-expired-or-is-blocked)。

## 我可以选择模型吗？

不可以。Grok Bot 为每个任务选择模型，没有模型选择器。对于每个任务，它使用最有可能带来最佳结果的后端模型。这可能是第一方 SpaceXSI 模型，也可能是来自[子处理方名单（sub-processor list）](https://trust.cursor.com/subprocessors)中提供方的第三方模型，而且选择可能因请求而异。用户无法被路由到或路由离开某个特定模型。

Grok Bot 不会显示某个请求使用的底层模型。你的用量和支出视图会把此活动记为 Grok Bot 用量，而不是按提供方或模型名称记录。把任务路由到 Opus 5.5 不会改变你每 token 的成本；你用量的消耗速度取决于你交给 Grok Bot 的工作类型以及每个任务需要多少工作量。

你团队的 Cursor [模型允许列表或阻止列表](https://cursor.com/docs/enterprise/model-and-integration-management#model-access-control)不适用于 Grok Bot。有模型允许列表的团队在[启用 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises#enabling-grok-bot-for-your-team)时会看到此通知。只有子处理方名单上的提供方才能处理你的数据，而且模型集合会随时间变化。参见[模型与数据](https://docs.x.ai/grok-bot/security#models-and-data)和[哪些 AI 模型为 Grok Bot 提供支持？](https://cursor.com/help/grok-bot/models)。

## Grok Bot 如何处理数据和隐私？

Grok Bot 使用 Cursor 的身份验证和账号数据设置。退出训练遵循适用的 Cursor 账号和隐私设置。

Grok Bot 需要云端数据存储，因此不支持旧版隐私模式（Legacy Privacy Mode）。你所有的 Bot 都可以访问分配给你账号的同一台云端电脑。关于完整边界和当前 Cursor 安全信息的链接，参见[批准、安全与隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy)。

## 我需要单独的 Grok Bot 订阅吗？

不需要。Grok Bot 随 The X Subscription 的 **Premium**、**Super** 和 **Ultra** 提供，也随旧版 **Cursor Pro**、**Pro+**、**Ultra** 和自助 **Teams** 提供。在旧版 Cursor 账号上，你还可以关联个人 **SuperGrok**、**SuperGrok Plus**、**SuperGrok Heavy** 或 **X Premium+** 账号，或使用在自助 **Grok Business** 套餐中分配了席位的 Grok 账号登录。在 Enterprise 上，请咨询你的账号团队。

## Grok Bot 多少钱？

可用性和计费取决于账号和套餐。在 The X Subscription（新客户从这里开始）上，Grok Bot 包含在 Premium、Super 和 Ultra 中，适用于个人和团队席位；Plus 和 Free 不含。在那里，Grok Bot 与 Cursor 和 Grok 应用从同一个每周用量池中扣除，预付额度覆盖池外的用量。Super 和 Ultra 包含比 Premium 更大的每周池。在 [grok.com/dashboard](https://grok.com/dashboard) 的**用量（Usage）**下查看用量。

在旧版 Cursor 套餐上，Grok Bot 包含在每个付费个人套餐和 Cursor Teams 中，你还可以关联个人 SuperGrok、SuperGrok Plus、SuperGrok Heavy 或 X Premium+ 订阅。**Pro** 包含每周用量，**Pro+** 包含充足的每周用量，**Ultra** 包含最高的每周用量。当**每周用量上限（Weekly usage limit）**用完时，如果启用了按需，额外用量会作为**按需用量（On-demand usage）**继续，并通过 Cursor 计费。Grok Bot 用量在你的 Cursor 账号上计量，而不是在 Grok 或 X 上，并且 macOS 和 iOS 共享相同的用量。

参见 [The X Subscription 上的 Grok Bot](https://docs.x.ai/x-subscription/grok-bot)和[套餐与计费](https://cursor.com/help/grok-bot/plans)。Enterprise 客户应联系其 Cursor 账号团队。

## 我可以关联哪些 Grok 套餐？

个人 **SuperGrok**、**SuperGrok Plus**、**SuperGrok Heavy** 和 **X Premium+**。**SuperGrok Lite** 和 **Grok Enterprise** 无法关联。如果你在自助 **Grok Business** 套餐中拥有席位，不要从套餐界面关联。退出登录，然后使用持有该席位的 Grok 账号通过**使用 Grok 登录（Sign in with Grok）**重新登录。在 The X Subscription 上无需关联：Grok Bot 从你套餐的共享每周池中扣除。参见[为 Grok Bot 关联 SuperGrok](https://cursor.com/help/grok-bot/supergrok)。

## 我看不到「关联 Grok 账号（Link Grok Account）」。

**关联 Grok 账号**位于 [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding) 的 **Grok Bot 入门（Get Started with Grok Bot）** 页面，以及手机的付费墙屏幕。如果你已经有访问权限，请打开**设置 → 用量与计费（Settings → Usage & Billing）**，在**管理套餐（Manage Plan）**下查找**通过 Grok 获取访问权限（Get Access with Grok）**。只有当关联会提高你的用量时，它才会出现。

## 我把 SuperGrok 关联到了错误的 Cursor 账号。可以解除关联吗？

不可以。关联是永久的，你无法自行移动它。请带上获得关联的账号和本应获得关联的账号[联系支持](https://docs.x.ai/grok-bot/troubleshooting#before-contacting-support)。关联是一种用量授予，而不是 Cursor 套餐，因此它不会改变或取消任一账号上的 Cursor 套餐。

## Cursor 套餐和 SuperGrok 会相加吗？

不会。在旧版 Cursor 账号上，Grok Bot 使用其中每周用量更多的一个。旧版 **Pro**、**SuperGrok** 和 **X Premium+** 是同一档，**Pro+** 与 **SuperGrok Plus** 同档，**Ultra** 与 **SuperGrok Heavy** 同档。Grok Business 席位的工作方式与 SuperGrok 关联相同。要获得更多用量，请移动到更高档位或开启按需用量。两个订阅各自继续计费；购买一个不会取消另一个。

如果你在关联后升级 SuperGrok，请最多等待 24 小时，让**每周用量上限**移动到新档位。你无需重新关联。

## 为什么我的 SuperGrok 上限与我的 Grok Bot 用量不一致？

它们是两个产品的两个独立计量器。Grok Bot 用量存在于你的 Cursor 账号上。在 Grok Bot 中于**设置 → 用量与计费**下查看，而不是在 Grok 应用中。

## 每周用量用完后，我如何停止收费？

在 The X Subscription 上，保持自动充值关闭，或在 [grok.com/dashboard/billing](https://grok.com/dashboard/billing) 的**额外用量额度**下设置每月额外用量上限。在旧版 Cursor 套餐上，关闭按需或设置上限：在 Grok Bot 中打开**设置 → 用量与计费 → 按需用量每月上限**，或在网页上访问 [cursor.com/dashboard](https://cursor.com/dashboard)，在**支出**下设置**每月上限**。上限不会在运行中途停止 Bot，因此正在运行的任务可能会略微超过它。如果按需关闭，Grok Bot 会在每周用量用完时停止，并在每周用量重置时恢复。

## 有免费试用吗？

部分账号可以在付费前试用 Grok Bot：当访问界面提供**开始试用（Start Trial）**时，选择它。试用是一笔用量额度，7 天窗口也同样适用。它永远不会变成付费套餐。额度按你的智能体完成多少工作扣减，以智能体步骤和 token 衡量，而不是你发送的消息数量，因此请从小处开始、把任务范围收窄，并在运行大型或长时间任务前在套餐界面查看用量。一个大任务可能用掉全部额度，已使用的额度不会恢复。

**取消试用（Cancel Trial）**会出现在免费套餐账号上。取消不收费。在免费套餐上，你可以在桌面端的**设置 → 用量与计费**或 iPhone 和 Android 上的**设置 → 用量（Settings → Usage）**中提前结束试用。这会移除任何剩余的试用额度，并且你无法再次开始试用。在付费套餐或 Teams 席位上，试用会自行结束。

在 iOS 应用中开始的 App Store 免费试用不同：它由 Apple 运营，除非你先取消，否则会变成付费的 Apple 订阅。参见[管理或取消手机订阅](https://docs.x.ai/grok-bot/mobile#manage-or-cancel-a-phone-subscription)。

## Grok Bot 的退款如何运作？

Grok Bot 没有单独的订阅，因此没有单独的退款路径。在 The X Subscription 上，退款遵循[发票与退款](https://docs.x.ai/x-subscription/invoices-and-refunds)，你已花掉的预付额度不可退款。在旧版 Cursor 套餐上，订阅退款遵循 Cursor 的[退款](https://cursor.com/help/account-and-billing/refunds)政策；Grok Bot 已消耗的按需用量和带用量的周期中途降级不可退款。商店购买的退款由 Apple 或 Google 处理。SuperGrok 和 X Premium+ 由 SpaceXSI 或 X 计费，而不是 Cursor；SuperGrok 参见 [Grok 常见问题](https://docs.x.ai/grok/faq#can-i-get-a-refund-for-my-grok-or-supergrok-subscription)，X Premium+ 请联系 X。

## Grok Bot 对团队和企业可用吗？

可以。在自助 Cursor Teams 套餐上，每个成员都会在其 Cursor 账号上获得 Grok Bot，无需 Premium 席位或管理员申请，并且在旧版 Teams 套餐上按需用量默认启用。在 The X Subscription 的团队中，每个付费席位（Premium、Super 或 Ultra）都包含它。在 Cursor Enterprise 上，管理员为团队启用 Grok Bot；请联系你的 Cursor 账号团队。基于申请的 Teams 套餐和 Enterprise 席位不接受个人 SuperGrok 关联。参见[面向团队和企业的 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises)。

## 我可以更改账号上的电子邮件吗？

不可以。Cursor 账号上的电子邮件无法更改。要使用不同的电子邮件，请创建一个新账号。参见[更改你的电子邮件地址](https://cursor.com/help/account-and-billing/change-email)。

## 我可以口述或与 Bot 交谈吗？

可以。在桌面端，按 `Cmd/Ctrl+D` 或选择**开始语音输入（Start voice input）**，向输入框口述。在 iPhone 和 Android 上，使用**开始听写（Start dictation）**进行口述。**开始语音聊天（Start voice chat）**会在桌面端、iPhone 和 Android 上启动实时对话。Bot 还可以发送**语音备忘录（voice memo）**，你可以在对话记录中播放。

## 桌面应用有哪些键盘快捷键？

参见[键盘快捷键](https://docs.x.ai/grok-bot/chat-and-collaboration#keyboard-shortcuts)。听写使用 `Cmd/Ctrl+D`。设置使用 `Cmd/Ctrl+,`。**开始语音聊天**是一个按钮，没有键位绑定。

## 我可以更改应用语言吗？

可以。在桌面端，打开**设置**，进入**通用（General）**，在**外观（Appearance）**下选择**语言（Language）**。**跟随系统（Follow System）**使用你电脑的语言，桌面端有 37 种语言。在 iPhone 和 Android 上，打开**设置**并选择**语言**；**系统（System）**使用你手机的语言，手机应用有 12 种语言。

语言会更改应用的菜单和消息。新 Bot 会用该语言给你写消息，除非你用另一种语言给它们写。语音聊天有自己的**语言**设置。

## 我可以使用多个账号吗？

在桌面端，打开账号菜单并选择**切换账号（Switch account）**或**添加账号（Add account）**。设置中列出相同的账号；非活动行包含**移除（Remove）**。在 iPhone 和 Android 上，打开**设置**，在**切换账号（Switch Account）**下选择一个账号以切换到它，或选择**添加账号（Add Account）**。滑动非活动账号以移除它。

## 支持哪些平台？

* Apple 芯片和 Intel 上的 macOS
* x64 和 Arm64 上的 Windows
* x64 和 Arm64 上的 Linux，以 `.deb` 包、`.rpm` 包或 AppImage 形式提供
* iOS 18 或更高版本上的 iPhone
* Android 9 或更高版本

iOS 应用也可以在搭载 iPadOS 18 或更高版本的 iPad 上运行。从 [cursor.com/dashboard/bot](https://cursor.com/dashboard/bot) 的 Grok Bot 页面获取桌面应用。

## 技能和例程有什么区别？

**技能（skill）**描述如何执行任务。**例程（routine）**把工作流分配给一个 Bot，并告诉它何时运行——按时间表，或在支持的情况下在某个事件之后。

在把技能变成例程之前，先在一个真实的一次性任务上测试它。

## 我可以向 Bot 展示我如何做一项任务吗？

当**教授任务（Teach a task）**可用时，从电脑视图录制一个浏览器工作流。Bot 会把演示转成草稿技能，供你审查和测试。推出可能是渐进的，录制时长限制为十分钟。

## 我可以与别人共享 Bot 吗？

可以。打开 Bot 的详细信息，选择**共享（Share）**，然后选择**创建副本（Create a copy）**。当 Bot 发布模板后，选择**发布（Publish）**，然后选择**复制链接（Copy link）**。任何有链接的人都可以在 [x.ai](https://x.ai) 上预览它，并将副本添加到自己的账号。他们不会得到你的电脑、登录信息或对话历史。如果你的团队限制模板共享，应用不会提供**创建副本**。

链接会暴露 Bot 的配置。在共享前删除密钥和任何机密内容。添加共享 Bot 即接受[第三方 bot 条款](https://x.ai/legal/bot-sharing-terms)。参见[共享 Bot](https://docs.x.ai/grok-bot/bots#share-a-bot)。

要给团队一个大家都与之对话的 Bot，而不是每人各自定制一份副本，请发布[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)。

## 如果我删除一个 Bot 会怎样？

删除会从 Grok Bot 中移除该 Bot 的活动配置文件、对话和例程。由于 Bot 共用一台电脑，该电脑上的文件和登录信息可能保留。后端保留遵循适用的 Cursor 条款。如果你以后可能需要它的工作，请改为隐藏该 Bot。

## 如何删除我的 Grok Bot 账号？

Grok Bot 使用你的 Cursor 账号，因此删除它会删除 Cursor 账号。删除是自助且永久的。退出 Grok Bot 或卸载应用会保留账号，不删除 Cursor 账号就无法删除 Grok Bot。

* **在 iPhone 或 Android 上：** 点击你的账号头像打开**设置**，点击你的账号，然后点击**删除账号（Delete Account）**并确认。在打开的浏览器页面中，登录，输入 **Delete**，然后再次确认。
* **在桌面端或网页上：** 如果订阅处于活动状态，先取消订阅。然后前往 [cursor.com/dashboard](https://cursor.com/dashboard)，打开**设置**，在**更多（More）**中找到**删除账号**，选择**删除（Delete）**，然后确认。桌面版 Grok Bot 可以让你退出登录，但不会删除账号。

删除会移除你的 Cursor 账号和 Grok Bot 访问权限；Grok Bot 智能体、聊天、电脑和连接的应用；以及 Cursor 聊天历史和设置。所有数据会在 30 天内删除。你自己电脑上的文件会留在那里。App Store 或 Google Play 订阅、已关联的 SuperGrok 订阅和已关联的 X Premium+ 订阅是分开的：如果你不再需要，请分别通过 Apple、Google、Grok 或 X 取消。

在 cursor.com 上，**删除账号**会为个人账号显示。如果你在 Cursor Teams 或 Enterprise 席位上，请询问团队管理员或[联系支持](https://docs.x.ai/grok-bot/troubleshooting#before-contacting-support)。
