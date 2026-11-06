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
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [功能更新, 运行环境, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 上的同名页（2026-11-05 收入）与这页大约一半相同，这页是扩充后的版本，多出 Vault 一栏、记忆导入、Auto-review 规则和通知的说明，所以另收一篇。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：设置分 General、Computer、Vault、Usage & Billing、Updates 几栏，没有模型选择器。General 里有记忆导入、时区（决定例程的调度时区）和 Auto-review 的自定义规则：个人规则只能比团队规则更严，冲突时「先询问」优先。Computer 栏可让云端电脑的流量经用户桌面转出，目标网站看到的是用户的 IP；企业关闭这项后，生效中的路由在 5 分钟内停止。桌面应用默认自动更新，只在屏幕锁定、空闲至少 10 分钟且 Bot 不忙时安装。Bot 需要用户输入时，若用户正在用桌面端则先在桌面提醒，约 3 分钟后才推送到手机。

**保留理由**：补充了设置项的较新版本，尤其是 Auto-review 规则的优先级和通知节奏，可以与 cursor.com 版对照看文档的变化。

---

设置与通知

Grok Bot 设置涵盖应用全局和桌面本地的行为。每个 Bot 的名称、
图片和标签位于其会话详情中。

## 打开 Grok Bot 设置

打开账户菜单并选择**设置（Settings）**，或按 `Cmd/Ctrl+,`。其他
桌面快捷键（包括 Bot 设置 `Cmd/Ctrl+Shift+,` 和
会话详情）见[键盘快捷键](https://docs.x.ai/grok-bot/chat-and-collaboration#keyboard-shortcuts)。

**Grok Bot 设置**对话框有**常规（General）**、**计算机（Computer）**、**Vault**、
**用量与计费（Usage & Billing）**和**更新（Updates）**几栏。栏目取决于你的账户和
发布进度，因此下面描述的一些选项可能不会出现。

## 常规（General）

### 账户

登录或退出 Grok Bot 使用的 Cursor 账户。账户菜单还有
**获取移动版 Grok Bot（Get Grok Bot for mobile）**，它会打开 App Store 列表；
**支持 → 关于（Support → About）**会显示已安装的 Grok Bot 版本。

当桌面上保存了多个账户时，账户菜单会包含
**切换账户（Switch account）**。选择**添加账户（Add account）**以保存另一个账户。设置会列出
相同的账户；非活动行包含**移除（Remove）**。

### 外观

选择**跟随系统（Follow System）**、**浅色（Light）**或**深色（Dark）**。

**强调色（Accent）**会用每个 Bot 的颜色（**Bot 颜色（Bot color）**，默认）为你的
一对一 Bot 消息和卡片着色，或让它们保持**黑色（Black）**。

使用**语言（Language）**选择**跟随系统**或 20 多种应用
语言之一，包括英语、西班牙语、法语、德语、日语、韩语、
简体中文和繁体中文。在 iPhone 和 Android 上，跟随设备的选项标为
**系统（System）**，列表也更短。参见
[Grok Bot 移动版](https://docs.x.ai/grok-bot/mobile)。

**输入时检查拼写（Check Spelling While Typing）**会在你输入时给拼错的词加下划线。它
默认开启。

### 系统

* **麦克风（Microphone）**选择你与 Grok Bot 说话时它监听的麦克风：
  **系统默认（System Default）**或特定设备。
* **使用硬件加速（Use hardware acceleration）**让你的显卡绘制应用。如果窗口闪烁或
  持续空白，请关闭它，然后选择**立即重启（Restart Now）**。它在 macOS 和 Windows 上
  默认开启，在 Linux 上关闭。

### Bot

配置共享和本地 Bot 行为：

* **时区（Timezone）**，例程用它来安排日程
* 你的自动审核开关和**自定义规则（Custom Rules）**

Grok Bot 管理模型选择，因此没有模型选择器。

### 导入

**将记忆导入 Grok Bot（Import Memory to Grok Bot）**会从
另一个 AI 助手引入你的偏好和上下文。选择**开始导入（Start Import）**，把提示词复制到与
你的另一个助手的聊天中，将其回答粘贴到第二个框中，然后选择
**添加到记忆（Add to Memory）**。Grok Bot 会把导入内容发送给你的主 Bot 并打开该
聊天。参见 [Bot 记住什么](https://docs.x.ai/grok-bot/bots#what-a-bot-remembers)。

### 自动审核（Auto-review）

管理你的个人自动审核规则，以及你的管理员要求的任何团队规则。

自动审核规则决定哪些操作会停下来等待你的批准。当你的
管理员为团队强制执行自动审核时，同一个表格还会显示锁定的团队
规则，并带有 `Required by your admin. You can't edit or delete this rule.` 你
可以在其之上添加自己的规则，但它们只会让行为更严格；规则冲突时**先询问（Ask
first）**优先。如果你的管理员关闭强制执行，锁定的团队规则会消失，你自己的规则生效，
除非你的团队从 Cursor 仪表盘共享了自动审核说明；那样这些说明会应用于你的
Bot，而不是你自己的规则，并且该部分会说明这一点。你的个人规则
会保存到你的账户，因此同样的规则适用于每台桌面设备和
iPhone。在更改它们之前，请阅读[审批与自动审核](https://docs.x.ai/grok-bot/security#approvals-and-auto-review)。

## 计算机（Computer）

**计算机**有两个部分。**你的计算机（Your computer）**保存登录到你账户的
桌面设备的设置。**Bot 的计算机（Bot's computer）**保存你的 Bot 共享的云计算机的更新和
重置控制项；参见
[更新或重置 Bot 的计算机](#update-or-reset-bots-computer)。

**管理设备（Manage devices）**列出你使用 Grok Bot 的计算机和手机。你
可以在那里重命名其中任何一台、更改另一台计算机的执行设置，或在另一台计算机
离线时移除它。手机不能被移除。

### 在你的桌面上运行命令

**此计算机上的执行（Execution on this computer）**控制 Bot 能否在
桌面上运行命令。**你的计算机**下每个列出的桌面都有自己的设置。在
某个桌面被列出之前，页面会显示**本地计算机上的执行（Execution on Local Computer）**作为替代。
逐命令批准是默认设置，该设置仅适用于该桌面。在更改它之前，请阅读
[审批与自动审核](https://docs.x.ai/grok-bot/security#approvals-and-auto-review)。关于本地执行可以触达什么，参见
[控制对你本地计算机的访问](https://docs.x.ai/grok-bot/approvals-security-and-privacy#control-access-to-your-local-computer)。

### 让流量经你的桌面路由

在**你的计算机**下，开启**让流量经此计算机路由（Route traffic through this computer）**，
把 Grok Bot 计算机的 Web 流量经当前桌面发送。该路由
适用于新连接，目标网站会看到你桌面的 IP 地址。
解析到私有地址或 VPN 地址的站点会被阻止，除非你的
组织允许了它们，并且该设置会显示本次会话阻止了多少个。你的计算机中同一时间只有一台在路由；
如果另一台正在路由，请从这台计算机发送一条消息，改为经它路由。如果
该设置要求你**更新 Bot 的计算机**，请先执行该操作。

该设置适用于一台桌面设备。如果你的企业管理员关闭了**允许本地出口路由（Allow
Local Egress Routing）**，该开关会关闭并锁定。该设置显示
`Your team admin has turned off local traffic routing. Grok Bot's computer routes traffic through the cloud.`
并且开关显示 `Disabled by your admin. You can't turn this on.` 任何
生效中的路由会在五分钟内停止。你的选择会被保留，如果管理员重新允许本地出口，
它会再次生效。

关于私有网络选项及其权衡，参见
[连接到私有网络](https://docs.x.ai/grok-bot/private-networks)。

### 更新或重置 Bot 的计算机

在**Bot 的计算机**下，**更新 Bot 的计算机**会把 Grok Bot 的计算机
迁移到最新版本。软件更新只会刷新 Grok Bot 的软件，
保留已安装的应用。计算机更新会重建计算机，保留文件和
登录信息，但会移除已安装的应用和包。**更新
Bot 的计算机**下方的文字会说明正在等待的是哪一种。

**重置 Bot 的计算机**是最后手段。它会用你最后保存的数据重建计算机，
与**恢复计算机（Recover computer）**相同；如果无法先连接计算机进行保存，
非常近期的更改不会回来。

关于破坏性最小的恢复顺序，参见
[更新、恢复或重置计算机](https://docs.x.ai/grok-bot/computer-and-apps#update-recover-or-reset-the-computer)。

## Vault

**Vault** 保存你的 Bot 用来登录和结账的登录信息、卡和联系信息，
而 Bot 看不到秘密值。使用**新建条目（New item）**添加一个，选择一个条目以编辑或移除它，并用
**新建条目 → 导入（New item → Import）**从另一个密码管理器导入登录信息。参见 [Vault 与安全登录](https://docs.x.ai/grok-bot/vault)。

## 已连接的应用

应用不在设置中。打开侧边栏中的**连接应用（Connect apps）**以查找应用和
打包技能。选择标题旁已连接的数量来管理
已安装的应用和私有技能。已安装的应用可能仍需要浏览器
认证，单个应用工具可以启用或禁用。在
Teams 套餐和 Enterprise 套餐中，管理员可能限制成员可以使用哪些应用。参见[连接应用](https://docs.x.ai/grok-bot/computer-and-apps#connect-an-app)。

## 用量与计费

**用量与计费**会为符合条件的账户显示每周包含用量和按需用量，
账户菜单可以一眼显示**每周用量（Weekly usage）**。如果这两个
界面都没有出现，请从 Cursor 账户页面查看用量，或联系你
组织的管理员。

关于套餐、每周用量和按需支出如何运作，参见
[套餐与计费](https://cursor.com/help/grok-bot/plans)。

## 团队设置脚本

**团队设置脚本**仅限企业版。管理员在 Cursor 仪表盘的
Grok Bot 页面管理这些脚本，它们会在每位成员的计算机上运行。
成员在设置中看不到它们。参见
[团队设置脚本](https://docs.x.ai/grok-bot/teams-and-enterprises#team-setup-scripts)。

## 更新

**设置 → 更新**处理桌面应用的更新。**Grok Bot 更新（Grok Bot Updates）**
显示已安装的版本；使用**检查更新（Check for Updates）**和**重启以
更新（Restart to Update）**安装新版本。要更新或重置 Grok Bot 的计算机，参见
[更新或重置 Bot 的计算机](#update-or-reset-bots-computer)。

同一栏中的**自动更新（Automatic Updates）**默认开启。开启时，
已下载的更新会在你离开时安装并重启应用：你的屏幕
已锁定或屏幕保护程序已开启、计算机已空闲至少 10
分钟，并且 Grok Bot 不忙。关闭它，就只在你选择
**重启以更新**时安装。Linux `.deb` 和 `.rpm` 安装通过
系统包管理器更新，不显示该开关。

## 每个 Bot 的设置

点击聊天顶部的 Bot 名称（**查看会话详情（View conversation details）**）以
打开其详情。点击名称或标签进行编辑，点击 Bot 的
图片更改其头像。这些只属于该 Bot。个人 Bot
没有描述；要改变 Bot 的行为，请在聊天中告诉它。参见
[编辑 Bot](https://docs.x.ai/grok-bot/bots#edit-a-bot)。

**此计算机上的执行**按桌面设置，你的个人
自动审核规则会保存到你的账户。

## 理解关注状态

侧边栏区分：

* **需要关注（Needs attention）**：有问题、批准或交接
* **未读活动（Unread activity）**：有新结果
* 工作或输入状态

打开会话会将其当前活动标记为已读。使用 Bot 菜单
手动将会话标记为已读或未读。

## 控制通知

为一个 Bot 开启**通知（Notifications）**，以便该 Bot 完成或正在等待你时
收到系统或移动通知。在手机上，该开关
在 Bot 的个人资料中。在桌面上，让 Bot 开启或关闭其通知。
群聊没有相同的按 Bot 通知开关。

当你在 macOS 或 Windows 上使用桌面应用时，你拥有的 Bot 的通知
会发到桌面，而不是你的手机。当应用打开并已登录、屏幕
已解锁、你最近使用过计算机，并且你的系统设置允许 Grok Bot 显示横幅或提醒时，
应用被视为正在使用。只有屏幕上处于焦点的 Bot 保持安静；
其他 Bot 仍会显示桌面通知。已完成的回复会跳过你的手机。当 Bot
需要你的输入时，你的手机会在大约 3 分钟后收到通知，除非你先打开
该 Bot、关闭其**通知**，或将其从侧边栏隐藏。

在其他时候，以及在 Linux 上始终如此，Grok Bot 处于焦点时通知会被抑制，
你的手机照常收到通知。侧边栏和程序坞徽标
仍会显示未读活动。

iPhone 和 Android 应用还会在首次运行时请求通知权限。设备权限和
Bot 的通知设置都必须允许该通知。在 iPhone 上，推送投递正在逐步推出。

## 处理应用内错误

错误会显示在输入框上方、**通知**下。你可以关闭一条
提示或清空列表。有些提示包含**复制请求 ID（Copy request ID）**以供支持使用；
请复制完整的 ID 并与[支持](https://docs.x.ai/grok-bot/troubleshooting#before-contacting-support)分享。

清空一条提示只会移除通知，而不会移除底层的外部操作
或 Bot 历史。
