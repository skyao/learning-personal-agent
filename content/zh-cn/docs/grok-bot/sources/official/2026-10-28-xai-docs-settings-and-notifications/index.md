---
title: "文档（docs.x.ai）：设置与通知"
linkTitle: "docs.x.ai：设置与通知"
date: 2026-10-28
originalTitle: "Settings and notifications"
sourceUrl: "https://docs.x.ai/grok-bot/settings-and-notifications"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：本地出口路由新增管理员锁定：Always off（强制走云端）与 Always on（强制转出，无已连接电脑时拒绝路由站点）；Usage & billing 重写为最多五段，新增 Resets（用量重置）与向 Bot 询问套餐和用量"
tags: [功能更新, 运行环境, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 上的同名页（2026-11-05 收入）与这页大约一半相同，这页是扩充后的版本，多出 Vault 一栏、记忆导入、Auto-review 规则和通知的说明，所以另收一篇。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：设置分 General、Computer、Vault、Usage & billing、Updates 几栏，没有模型选择器。General 里有记忆导入、时区（决定例程的调度时区）和 Auto-review 的自定义规则：个人规则只能比团队规则更严，冲突时 Ask first 优先。Computer 栏可让云端电脑的流量经用户桌面转出，目标网站看到的是用户的 IP；Enterprise 管理员可把它锁为 Always off（流量走云端）或 Always on（没有已连接的电脑时，Grok Bot 的电脑拒绝被路由的站点，不回退到云端）。Usage & billing 最多五段，依次为 My plan、Usage limits、Grok Bot usage、Additional usage、Resets；Use reset 可立即把每周用量清零，用户也可在与 Bot 的私聊中询问套餐和用量。桌面应用默认自动更新，只在屏幕锁定、空闲至少 10 分钟且 Bot 不忙时安装；Bot 需要用户输入时，若用户正在用桌面端则先在桌面提醒，约 3 分钟后才推送到手机。

**保留理由**：补充了设置项的较新版本，尤其是 Auto-review 规则的优先级和通知节奏，可以与 cursor.com 版对照看文档的变化。

---

设置与通知

Grok Bot 设置涵盖应用范围和桌面本地行为。每个 Bot 的名称、图片和标签位于其对话详情中。

## 打开 Grok Bot 设置

打开账户菜单并选择 **设置（Settings）**，或按 `Cmd/Ctrl+,`。其他桌面快捷键，包括 Bot 设置（`Cmd/Ctrl+Shift+,`）和对话详情，见[键盘快捷键](https://docs.x.ai/grok-bot/chat-and-collaboration#keyboard-shortcuts)。

**Grok Bot 设置（Grok Bot settings）** 对话框包含 **通用（General）**、**计算机（Computer）**、**Vault**、**用量与账单（Usage & billing）** 和 **更新（Updates）** 几个面板。分区取决于你的账户和发布范围，因此下面描述的一些选项可能不会出现。

## 通用

### 账户

登录或退出 Grok Bot 使用的 Cursor 账户。账户菜单还包含 **获取移动版 Grok Bot（Get Grok Bot for mobile）**，它会打开 App Store 列表；**支持（Support）→ 关于（About）** 会显示已安装的 Grok Bot 版本。

当桌面上保存了多个账户时，账户菜单会包含 **切换账户（Switch account）**。选择 **添加账户（Add account）** 保存另一个账户。设置中列出同样的账户；非活动行带有 **移除（Remove）**。

### 外观

选择 **跟随系统（Follow system）**、**浅色（Light）** 或 **深色（Dark）**。

**强调色（Accent）** 用每个 Bot 的颜色（**Bot 颜色（Bot color）**，默认值）为你的 1:1 Bot 消息和卡片着色，或让它们保持 **黑色（Black）**。

用 **语言（Language）** 选择 **跟随系统（Follow system）** 或 20 多种应用语言之一，包括英语、西班牙语、法语、德语、日语、韩语、简体中文和繁体中文。在 iPhone 和 Android 上，跟随设备的选项标为 **系统（System）**，列表也更短。见[移动版 Grok Bot](https://docs.x.ai/grok-bot/mobile)。

**输入时检查拼写（Check spelling while typing）** 会在你输入时给拼错的词加下划线。它默认开启。

### 系统

* **麦克风（Microphone）** 选择你与 Grok Bot 说话时它监听的麦克风：**系统默认（System default）** 或某个具体设备。
* **使用硬件加速（Use hardware acceleration）** 让显卡绘制应用。如果窗口闪烁或一直空白，请关闭它，然后选择 **立即重启（Restart now）**。它在 macOS 和 Windows 上默认开启，在 Linux 上默认关闭。

### Bot

配置共享和本地 Bot 行为：

* **时区（Timezone）**，例程用它来安排时间表
* 你的自动审查开关和 **自定义规则（Custom rules）**

Grok Bot 自行管理模型选择，因此没有模型选择器。

### 导入

**将记忆导入 Grok Bot（Import memory to Grok Bot）** 会把你的偏好和上下文从另一个 AI 助理带过来。选择 **开始导入（Start import）**，把提示词复制到与你另一个助理的聊天中，把它的回答粘贴到第二个框里，然后选择 **添加到记忆（Add to memory）**。Grok Bot 会把导入内容发送给你的主 Bot，并打开那段聊天。见[Bot 记得什么](https://docs.x.ai/grok-bot/bots#what-a-bot-remembers)。

### 自动审查

管理你的个人 Auto-review 规则，以及管理员要求的任何团队规则。

Auto-review 规则决定哪些操作会停下来等待你批准。当你的管理员为团队强制启用 Auto-review 时，同一张表还会显示锁定的团队规则，并带有 `Required by your admin. You can't edit or delete this rule.`。你可以在其上添加自己的规则，但这些规则只会让行为更严格；规则冲突时 **先询问（Ask first）** 优先。如果你的管理员关闭强制启用，锁定的团队规则会消失，你自己的规则生效；除非你的团队从 Cursor 仪表盘共享了 Auto-review 指令，此时这些指令会取代你自己的规则适用于你的 Bot，该小节也会这样说明。你的个人规则保存到账户，因此同样的规则会在每台桌面和 iPhone 上生效。更改它们之前，请阅读[审批与 Auto Review](https://docs.x.ai/grok-bot/security#approvals-and-auto-review)。

## 计算机

**计算机** 有两个部分。**你的计算机（Your computer）** 保存登录你账户的桌面的设置。**Bot 的计算机（Bot's computer）** 保存你的 Bot 共用的云计算机的更新和重置控件；见[更新或重置 Bot 的计算机](#update-or-reset-bots-computer)。

**管理设备（Manage devices）** 列出你使用 Grok Bot 的计算机和手机。你可以在那里重命名其中任何一台、更改另一台计算机的执行设置，或在另一台计算机离线时将其移除。手机不能移除。

### 在你的桌面上运行命令

**在本计算机上执行（Execution on this computer）** 控制 Bot 是否可以在桌面上运行命令。**你的计算机** 下每台列出的桌面都有自己的设置。在桌面被列出之前，页面会改为显示 **在本地计算机上执行（Execution on local computer）**。默认是逐条命令审批，该设置仅适用于该桌面。更改前请阅读[审批与 Auto Review](https://docs.x.ai/grok-bot/security#approvals-and-auto-review)。关于本地执行可以触达什么，见[控制对本地计算机的访问](https://docs.x.ai/grok-bot/approvals-security-and-privacy#control-access-to-your-local-computer)。

### 让流量经你的桌面转出

在 **你的计算机** 下，开启 **让流量经此计算机转出（Route traffic through this computer）**，把 Grok Bot 计算机的 Web 流量经当前桌面发送。该路由适用于新连接，目标会看到你桌面的 IP 地址。解析到私有地址或 VPN 地址的站点会被屏蔽，除非你的组织已允许；该设置会显示本次会话屏蔽了多少个。你同一时间只有一台计算机会路由；如果另一台正在路由，从这台计算机发送一条消息即可改为经它路由。如果设置提示你 **更新 Bot 的计算机（Update Bot's computer）**，请先更新。

该设置适用于一台桌面。你的 Enterprise 管理员可以锁定它：

* **始终关闭（Always off）**：开关关闭并锁定。设置显示 `Your team admin has turned off local traffic routing. Grok Bot's computer routes traffic through the cloud.`，开关显示 `Disabled by your admin. You can't turn this on.`。流量经云端。你的选择会被保留，如果管理员把模式改为 **由成员决定（Members decide）**，它会再次生效。（译注：前一句意为「你的团队管理员已关闭本地流量路由。Grok Bot 的计算机通过云端路由流量。」后一句意为「已被你的管理员禁用。你不能开启此项。」）
* **始终开启（Always on）**：开关开启并锁定，显示 `Required by your admin. You can't turn this off.`。当你没有任何计算机连接时，Grok Bot 的计算机拒绝访问被路由的站点。它不会改用云端。如果 Grok Bot 的计算机需要先更新，请选择 **更新 Bot 的计算机**。在更新之前，Grok Bot 的计算机通过云端路由流量。（译注：意为「你的管理员要求开启。你不能关闭此项。」）

关于私有网络选项及其取舍，见[连接到私有网络](https://docs.x.ai/grok-bot/private-networks)。

### 更新或重置 Bot 的计算机

在 **Bot 的计算机** 下，**更新 Bot 的计算机** 会把 Grok Bot 的计算机迁移到最新版本。软件更新只刷新 Grok Bot 的软件并保留已安装应用。计算机更新会重建计算机，保留文件和登录状态，但移除已安装应用和软件包。**更新 Bot 的计算机** 下方的文字会说明正在等待的是哪一种。

**重置 Bot 的计算机（Reset Bot's computer）** 是最后手段。它会根据你最后保存的数据重建计算机，与 **恢复计算机（Recover computer）** 相同；如果无法先连接计算机进行保存，非常近期的更改不会恢复。

有关破坏性最小的恢复顺序，见[更新、恢复或重置计算机](https://docs.x.ai/grok-bot/computer-and-apps#update-recover-or-reset-the-computer)。

## Vault

**Vault** 保存你的 Bot 用来替你登录和结账的登录信息、银行卡和联系信息。用 **新建项目（New item）** 添加一项，选择一项进行编辑或移除，或用 **新建项目 → 导入（Import）** 从另一个密码管理器导入登录信息。见 [Vault 与安全登录](https://docs.x.ai/grok-bot/vault)。

## 已连接应用

应用不在设置中。打开侧边栏中的 **连接应用（Connect apps）** 查找应用和打包技能。选择标题旁已连接数量，以管理已安装应用和私有技能。已安装应用可能仍需要浏览器身份验证，单个应用工具可以启用或禁用。在 Teams 套餐和 Enterprise 套餐中，管理员可以限制成员可以使用哪些应用。见[连接应用](https://docs.x.ai/grok-bot/computer-and-apps#connect-an-app)。

## 用量与账单

**用量与账单** 最多有五个小节，顺序固定：

* **我的套餐（My plan）** 显示你的套餐，以及一个管理或更改套餐的按钮；还有 **账单（Billing）**，其中 **管理账单（Manage billing）** 用于管理支付方式和发票。在 Enterprise 团队中，它显示 **由你的组织管理（Managed by your organization）**。免费试用期间，**取消试用（Cancel trial）** 可以提前结束试用。
* **用量上限（Usage limits）** 显示你已使用多少每周用量，以及何时重置。Enterprise 成员看到的是支出上限。如果你的套餐不包含 Grok Bot 用量，它会显示 **你的套餐不包含 Grok Bot 用量（Your plan doesn't include Grok Bot usage）**。
* **Grok Bot 用量（Grok Bot usage）** 以图表显示你的 Grok Bot 用量，可按 **按 Bot（By Bot）** 或 **按来源（By source）** 查看。
* **额外用量（Additional usage）** 涵盖超过每周上限后的用量：**额度（Credits）**，带有 **购买额度（Buy credits）**、**自动充值（Auto top-up）** 和 **每月额外用量上限（Monthly additional usage limit）**；或视套餐而定显示 **按需每月上限（On-demand monthly limit）**。
* **重置（Resets）** 列出你的用量上限重置；见[使用用量上限重置](#use-a-usage-limit-reset)。

账户菜单还可以一眼显示 **每周用量（Weekly usage）**。如果两个位置都不显示，请从 Cursor 账户页面查看用量，或联系你组织的管理员。

你也可以在与 Bot 的私聊中询问套餐和用量。它会说明你当前的 Grok Bot 用量来自哪里（每周用量上限、试用，或团队的 Enterprise 用量）、已用多少、是否有按需用量，以及何时重置或试用何时结束。只有 Bot 的所有者可以询问，而且只能在私聊中；在其他地方 Bot 会拒绝。出现用量警告时，**查看用量（Review usage）** 会让你的 Bot 替你查看用量。

关于套餐、每周用量和按需支出如何运作，见[套餐与计费](https://grok.com/help/grok-bot/plans)。

### 使用用量上限重置

用量上限重置会立即把你的每周用量恢复到 0%，不必等待常规的每周重置。你拥有的重置列在 **用量与账单** 的 **重置** 下，每条是一行 **用量重置（Usage reset）**，并带有到期日期。点击 **使用重置（Use reset）**，然后 **确认（Confirm）**。使用一次后，需要等待一段时间才能使用下一次。

当你达到每周用量上限时，消息框上方的横幅也会提供 **使用重置（Use Reset）**。如果你没有重置次数且可以邀请朋友，**重置** 会显示 **邀请朋友获得一次免费重置（Refer a friend to get a free reset）**，用量横幅则会提供 **邀请朋友（Invite a Friend）**。两者都会打开推荐对话框。

## 团队设置脚本

**团队设置脚本（Team Setup Scripts）** 仅限 Enterprise。管理员在 Cursor 仪表盘的 Grok Bot 页面管理这些脚本，它们会在每位成员的计算机上运行。成员在设置中看不到它们。见[团队设置脚本](https://docs.x.ai/grok-bot/teams-and-enterprises#team-setup-scripts)。

## 更新

**设置 → 更新** 处理桌面应用的更新。**Grok Bot 更新（Grok Bot updates）** 显示已安装版本；使用 **检查更新（Check for Updates）** 和 **重启以更新（Restart to Update）** 安装新版本。要更新或重置 Grok Bot 的计算机，见[更新或重置 Bot 的计算机](#update-or-reset-bots-computer)。

同一面板中的 **自动更新（Automatic updates）** 默认开启。开启时，下载好的更新会在你离开时安装并重启应用：屏幕已锁定或屏保已开启、计算机已空闲至少 10 分钟，且 Grok Bot 不忙。关闭它则仅在你选择 **重启以更新** 时安装。Linux 的 `.deb` 和 `.rpm` 安装通过系统包管理器更新，不显示此开关。

## 单个 Bot 的设置

点击聊天顶部的 Bot 名称（**查看对话详情（View conversation details）**）打开其详情。点击名称或标签进行编辑，点击 Bot 的图片更改其头像。这些都只属于该 Bot。个人 Bot 没有描述；要更改 Bot 的功能，请在聊天中告诉它。见[编辑 Bot](https://docs.x.ai/grok-bot/bots#edit-a-bot)。

**在本计算机上执行** 按桌面设置，你的个人 Auto-review 规则保存到账户。

## 理解注意状态

侧边栏区分：

* **需要关注（Needs attention）**：有问题、审批或交接
* **未读活动（Unread activity）**：有新结果
* 工作中或正在输入状态

打开对话会将其当前活动标记为已读。使用 Bot 菜单可以手动把对话标记为已读或未读。

## 控制通知

为某个 Bot 开启 **通知（Notifications）**，以便该 Bot 完成或等待你时收到系统或移动通知。在手机上，开关位于 Bot 的配置文件中。在桌面端，请让 Bot 打开或关闭其通知。群聊没有相同的按 Bot 通知开关。

当你在 macOS 或 Windows 上使用桌面应用时，你拥有的 Bot 发出的通知会发到桌面而不是手机。应用处于打开且已登录、屏幕未锁定、你最近使用过计算机，并且系统设置允许 Grok Bot 显示横幅或提醒时，应用就算正在使用中。窗口处于焦点时，只有屏幕上的 Bot 保持安静；其他 Bot 仍会显示桌面通知。已完成的回复不会再推送到手机。当 Bot 需要你输入时，除非你先打开该 Bot、关闭其 **通知**，或把它从侧边栏隐藏，否则手机会在大约 3 分钟后收到通知。

其他时候，以及在 Linux 上始终如此，Grok Bot 处于焦点时通知会被抑制，手机照常收到通知。侧边栏和 Dock 徽章仍会显示未读活动。

iPhone 和 Android 应用在首次运行时也会请求通知权限。设备权限和 Bot 的通知设置都必须允许该通知。在 iPhone 上，推送投递正在逐步推出。

## 处理应用内错误

错误会出现在输入框上方、**通知** 下。你可以关闭一条通知或清空列表。有些通知包含供支持使用的 **复制请求 ID（Copy request ID）**；复制完整 ID 并与[支持](https://docs.x.ai/grok-bot/troubleshooting#before-contacting-support)分享。

清除通知只会移除提示，不会移除底层的外部操作或 Bot 历史记录。
