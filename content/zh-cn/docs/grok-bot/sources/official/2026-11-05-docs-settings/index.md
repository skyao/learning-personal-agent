---
title: "文档：设置"
linkTitle: "文档：设置与通知"
date: 2026-11-05
originalTitle: "Settings and notifications"
sourceUrl: "https://cursor.com/docs/grok-bot/settings"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [功能更新, 运行环境, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：设置分四栏：General、Computer、Usage & Billing、Updates。General 里有 Bot 的时区、Auto-review 开关和自定义规则；因为系统自行选择模型，没有模型选择器。Computer 栏中，可设定在用户桌面上执行命令的策略（默认每次询问），并可开启「Route traffic through this computer」把 Bot 云端计算机的网络流量经当前桌面转出，若企业管理员关闭本地出口，该选项锁定且生效中的路由在五分钟内停止。更新分两部分：桌面应用可自动更新（用户离开、屏幕锁定且空闲至少 10 分钟时安装），云端计算机用「Update Bot's Computer」更新，计算机更新会重建并保留文件和登录，但移除已装应用；「Reset」是最后手段。侧边栏区分需要注意、未读和工作中三种状态，可按 Bot 开启通知。

**保留理由**：补充了用户侧可调的设置项，尤其是本地执行、流量路由、更新与重置的行为，以及通知和状态显示。

---

Grok Bot 设置涵盖应用范围和桌面本地行为。设置面板包括 **General**、**Computer**、**Usage & Billing** 和 **Updates**。每个 Bot 的名称、图片和标签位于其对话详情中。从账户菜单或使用 `Cmd+,Ctrl+,` 打开设置。

设置分区取决于你的账户和发布范围，因此下面有些选项可能不会出现在你的界面中。

## General

- **Account.** 登录或退出 Grok Bot 使用的 Cursor 账户。账户菜单还包含 **Get Grok Bot for mobile**，而 **Support** > **About** 会显示已安装的版本。
- **Appearance.** 跟随系统（Follow System）、浅色（Light）或深色（Dark）。
- **Bot.** [例程（routine）](https://cursor.com/help/grok-bot/routines#how-do-schedules-and-time-zones-work)用于时间表的时区，以及你的自动审查（Auto-review）开关和 **Custom Rules**，还有管理员要求的任何团队规则。Grok Bot 管理模型选择，因此没有模型选择器。

自动审查规则决定哪些操作会停下来等待你批准。当你的管理员为团队强制实施自动审查时，同一张表还会显示锁定的团队规则，并带有 `Required by your admin. You can't edit or delete this rule.`。成员可以在其上添加自己的规则，但这些规则只会让行为更严格；规则冲突时 **Ask first** 优先。如果你的管理员关闭强制实施，你只会看到并使用自己的规则。你的个人规则会保存到账户，因此相同的规则会应用于每台桌面和 iPhone。更改它们之前，请阅读[审批与 Auto Review](https://cursor.com/docs/grok-bot/security#approvals-and-auto-review)。

## Computer

**Computer** 有两个部分。**Your computer** 包含已登录你账户的桌面设置。**Bot's computer** 包含你的 Bot 共享的云计算机的更新和重置控件；见[更新](#updates)。

### 在你的桌面上运行命令

**Execution on this computer** 控制 Bot 是否可以在桌面上运行命令。**Your computer** 下每台列出的桌面都有自己的设置。在桌面被列出之前，页面会显示 **Execution on Local Computer**。默认是逐条命令审批，该设置仅适用于该桌面。更改前请阅读[审批与 Auto Review](https://cursor.com/docs/grok-bot/security#approvals-and-auto-review)。

### 通过你的桌面转出流量

在 **Your computer** 下，开启 **Route traffic through this computer**，让 Grok Bot 计算机的 Web 流量经当前桌面转出。该路由适用于新连接。目的地会看到你桌面的 IP 地址。解析到私有地址或 VPN 地址的站点会被阻止，除非已为你的组织允许；该设置会显示本次会话中有多少站点被阻止。

该设置适用于一台桌面。如果你的 Enterprise 管理员关闭 **Allow Local Egress Routing**，该开关会关闭并锁定，显示 `Disabled by your admin. You can't turn this on.`。任何生效中的路由会在五分钟内停止。你的选择会被保留，如果管理员重新允许本地出口，它会再次生效。

有关私有网络选项及其权衡，见[连接到私有网络](https://cursor.com/docs/grok-bot/private-networks)。

## Connected apps

应用不在设置中。打开侧边栏中的 **Connect apps** 查找应用和打包技能。选择标题旁已连接数量，以管理已安装应用和私有技能。已安装应用可能仍需要浏览器身份验证，单个应用工具可以启用或禁用。在 Teams 套餐和 Enterprise 套餐中，管理员可以限制成员可以使用哪些应用。见[连接应用](https://cursor.com/help/grok-bot/connect-apps)。

## Usage and billing

**Usage & Billing** 显示符合条件账户的每周包含用量和按需用量，账户菜单可以一眼显示每周用量。有关套餐、每周用量和按需支出如何运作，见[套餐与计费](https://cursor.com/help/grok-bot/plans)。

## Team Setup Scripts

**Team Setup Scripts** 仅限 Enterprise。管理员在仪表盘的 Grok Bot 页面管理这些脚本，它们会在每位成员的计算机上运行。成员不会在设置中看到它们。见[面向 Teams 和 Enterprise 的 Grok Bot](https://cursor.com/docs/grok-bot/teams#admin-controls)。

## 更新

Grok Bot 应用和 Grok Bot 的计算机分开更新：

- **Check for Updates** 和 **Restart to Update**，位于 **Updates** 面板，更新桌面应用。
- **Automatic Updates**，位于同一面板，默认开启。开启时，下载的更新会在你离开时安装并重启应用：你的屏幕已锁定或屏保已开启、计算机已空闲至少 10 分钟，且 Grok Bot 不忙。关闭它则仅在你选择 **Restart to Update** 时安装。Linux 的 `.deb` 和 `.rpm` 安装不会显示此项。
- **Update Bot's Computer**，在 **Settings** > **Computer** 下的 **Bot's computer** 中，把云计算机迁移到最新版本。软件更新只刷新 Grok Bot 的软件并保留已安装应用。计算机更新会重建计算机，保留文件和登录状态，但移除已安装应用和软件包。**Update Bot's Computer** 下方的文字会说明正在等待的是哪一种。
- **Reset Bot's Computer**，位于同一部分，是最后手段，它会根据你最后保存的数据重建计算机，效果与 Recover 相同；如果无法先连接计算机进行保存，非常近期的更改不会恢复。

有关破坏性最小的恢复顺序，见[使用 Grok Bot](https://cursor.com/docs/grok-bot/work#update-recover-or-reset)。

## 单个 Bot 的设置

点击聊天顶部的 Bot 名称（**View conversation details**）打开其详情。点击名称或标签进行编辑，点击 Bot 的图片更改其头像。这些只属于该 Bot。个人 Bot 没有描述；要更改 Bot 的功能，请在聊天中告诉它。见[更改 Bot 的名称、图片和功能](https://cursor.com/help/grok-bot/edit-bot)。

## 注意状态与通知

侧边栏区分需要关注的 Bot（有问题、审批或交接）、未读活动（有新结果）和工作状态。打开对话会将其当前活动标记为已读，Bot 菜单可以手动将对话标记为已读或未读。

为某个 Bot 开启 **Notifications**，以便该 Bot 完成或等待你时收到系统或移动通知。在手机上，开关位于 Bot 的配置文件中。在桌面端，请让 Bot 打开或关闭其通知。群聊没有相同的按 Bot 通知开关。Grok Bot 处于焦点时通知会被抑制；侧边栏和 Dock 徽章仍会显示未读活动。在 iPhone 上，设备权限和 Bot 的通知设置都必须允许该通知，推送投递正在逐步推出。

## 应用内错误

错误会出现在输入框上方、**Notifications** 下。有些通知包含供支持使用的 **Copy request ID**；复制完整 ID 并与[支持](https://cursor.com/help/grok-bot/get-help)分享。清除通知只会移除提示，不会移除底层操作或历史记录。
