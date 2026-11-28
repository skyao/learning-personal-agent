---
title: "文档：向组织部署 Grok Bot"
linkTitle: "文档：组织部署"
date: 2026-11-05
originalTitle: "Deploy Grok Bot to your organization"
sourceUrl: "https://docs.x.ai/grok-bot/deployment"
altUrls: ["https://cursor.com/docs/grok-bot/deployment"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：Linux 的 .deb/.rpm 安装在 Update required 界面直接给出 apt/dnf 升级命令；仓库暂无新版时改提示下载最新包；其余主要是措辞与版式调整，并新增相关页面列表"
tags: [运行环境, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：IT 团队用现有设备管理工具部署 Grok Bot 桌面应用：macOS（.dmg）、Windows（Setup .exe，按用户安装，可 /S 静默安装）、Linux（.deb、.rpm、AppImage），iPhone 需 iOS 18 以上，Android 需 9 以上。托管计算机是云端的 Linux 机器，每位成员一台，不加入 MDM，Enterprise 团队可通过 Team Setup Scripts 安装自有工具。应用无法由管理员关闭更新，成员可关闭 **Automatic updates**，但仍会收到新版提示；低于最低版本或超过最大期限的旧版会显示 **Update required**，两项限制远程设置且不公布；Linux 的 .deb/.rpm 安装由包管理器更新，该界面会显示升级命令（apt 或 dnf），仓库没有新版时改为提示下载最新包。托管计算机的镜像由系统维护，新镜像出现时会在后台逐步重建空闲计算机；Enterprise 管理员可以批量重建。登录用 Cursor 账号和 SSO，没有单独的 Grok Bot 登录。

**保留理由**：讲清了客户端只是聊天、审核和审批的瘦客户端，工作都在托管计算机上，以及版本与镜像更新的规则，对研究其运行架构和企业落地门槛有用。

---

向组织部署 Grok Bot

你的 IT 团队用它在其他软件上已经在用的工具，把 Grok Bot 桌面应用装到成员设备上：下载带版本号的安装程序、推送它，并决定设备何时升级到新版本。开启 Grok Bot 和限定访问范围的仪表盘控制见[面向团队与企业的 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises)，部署 Cursor 编辑器的内容见[部署模式](https://cursor.com/docs/enterprise/deployment-patterns)。

## 你部署什么

| 组件 | 运行于 | 更新方式 |
| --- | --- | --- |
| 桌面应用 | macOS（Apple 芯片和 Intel）、Windows（x64 和 Arm64）、Linux（x64 和 Arm64） | 由应用自身更新；Linux 的 `.deb` 和 `.rpm` 安装由你的包管理器更新 |
| iPhone 应用 | iOS 18 或更高版本 | App Store |
| Android 应用 | Android 9 或更高版本 | Google Play |
| 托管电脑 | 云端，每位成员一台 | 自动，在后台 |

这些应用是用于聊天、审核和批准的客户端。Bot 在成员的托管电脑上工作。你的设备管理工具只能触达成员设备上的这些应用，到此为止：托管电脑在云端运行 Linux，不加入 MDM。要在托管电脑上装自己的工具，Enterprise 团队使用[团队设置脚本](https://docs.x.ai/grok-bot/private-networks#install-a-networking-client-with-team-setup)。

## 获取安装程序

* 仪表盘 [Grok Bot 页面](https://cursor.com/dashboard/bot)上的 **下载 Grok Bot（Download Grok Bot）** 行会安装应用，或复制一个可以分享给成员的链接。
* [下载页](https://cursor.com/download/bot)列出各平台和格式当前的安装程序。
* 用于脚本化打包时，从[发布源](#read-the-current-release-from-the-feed)读取当前版本，并下载它指定的文件。

| 平台 | 架构 | 格式 |
| --- | --- | --- |
| macOS | Apple 芯片、Intel | `.dmg` |
| Windows | x64、Arm64 | Setup `.exe` |
| Linux | x64、Arm64 | `.deb`、`.rpm`、AppImage |

### 从发布源读取当前版本

每个平台有一个 JSON 发布源，地址为 `https://api2.cursor.sh/updates/api/download/stable/{platform}/sand`：

| `{platform}` | 安装程序 |
| --- | --- |
| `darwin-arm64` | macOS，Apple 芯片 |
| `darwin-x64` | macOS，Intel |
| `win32-x64-user` | Windows x64 |
| `win32-arm64-user` | Windows Arm64 |
| `linux-x64` | Linux x64 |
| `linux-arm64` | Linux Arm64 |

```bash
curl -s https://api2.cursor.sh/updates/api/download/stable/darwin-arm64/sand
```

你需要的字段：

| 字段 | 值 |
| --- | --- |
| `version` | 当前版本 |
| `commitSha` | 该版本来自的构建。Linux 下载 URL 中包含它。 |
| `downloadUrl` | 安装程序：macOS 上是 `.dmg`，Windows 上是 Setup `.exe`，Linux 上是 AppImage |
| `debUrl`、`rpmUrl` | 仅 Linux。`.deb` 和 `.rpm` 包。 |

响应可能带有其他字段；安装桌面应用不需要它们。

### 构造带版本号的 URL

macOS 和 Windows 安装程序为每个版本保留一个带版本号的 URL。把 `{version}` 替换为你想要的版本：

```text
# macOS, Apple silicon
https://downloads.cursor.com/grokbot/stable/darwin-arm64/{version}/Grok_Bot_{version}.dmg

# macOS, Intel
https://downloads.cursor.com/grokbot/stable/darwin-x64/{version}/Grok_Bot_{version}_x64.dmg

# Windows x64
https://downloads.cursor.com/grokbot/stable/win32-x64/{version}/Grok_Bot_{version}_Setup.exe

# Windows Arm64
https://downloads.cursor.com/grokbot/stable/win32-arm64/{version}/Grok_Bot_{version}_Setup.exe
```

Linux 包位于该版本的 `commitSha` 之下，路径为 `https://downloads.cursor.com/grokbot/stable/{commitSha}/linux/x64/` 或 `.../linux/arm64/`。从 Linux 发布源的 `downloadUrl`、`debUrl` 和 `rpmUrl` 中复制确切的文件 URL。

## 用你的设备管理工具推送桌面应用

* 在 macOS 上，用你现在运行的 Mac 管理工具部署 `.dmg`，例如 Jamf Pro、Kandji 或 Microsoft Intune。
* 在 Windows 上，用 Intune、Configuration Manager 或其他软件分发工具部署 Setup `.exe`，并用 `Grok_Bot_{version}_Setup.exe /S` 静默安装。安装程序按用户安装，装到成员配置文件下的 `%LOCALAPPDATA%\Programs`，所以要在用户上下文中部署，不要以 SYSTEM 身份部署。推送前先在一台试点设备上测试安装。
* 在 Linux 上，用你的配置管理工具安装 `.deb` 或 `.rpm`，例如 Ansible、Puppet 或 Chef。受管机群优先用这些包：包安装会按你的计划、通过你的包管理器更新。见 [Linux 包更新](#linux-package-updates)。
* 在 iPhone 上，成员从 [App Store](https://apps.apple.com/app/id6794501026) 安装 Grok Bot，需 iOS 18 或更高版本。
* 在 Android 上，成员从 [Google Play](https://play.google.com/store/apps/details?id=ai.x.grok.bot) 安装 Grok Bot，需 Android 9 或更高版本。要推送到受管设备，在受管 Google Play 中通过 Intune 或其他 Android 设备管理工具批准它。

成员通过你正常的 SSO 流程用 Cursor 账号登录；Grok Bot 没有单独的登录。要在 Okta 或 Entra ID 中分配 Cursor 应用，见[分配 Cursor 应用](https://docs.x.ai/grok-bot/identity-and-access#assign-the-cursor-app)。

## 选择版本

固定你测试过的版本。下载该版本的安装程序，保存在你自己的软件仓库或 MDM 包存储中，从你的副本部署，让每台新设备都得到同一个构建。旧安装程序还能下载多久没有公布，而固定的构建只在失去支持之前可用；见[桌面应用如何更新](#how-desktop-updates-work)。

Linux 包 URL 包含该版本的 `commitSha`，所以要把完整 URL 和版本号一起记下。

要查看某台设备运行的是哪个版本，打开应用里的账号菜单，选择 **支持（Support）**，然后选择 **关于（About）**。对话框会显示 **版本（Version）**，**复制版本信息（Copy version info）** 会复制版本、发布轨道和操作系统。

### 桌面应用如何更新

| 安装方式 | 更新如何到达 |
| --- | --- |
| macOS `.dmg`、Windows Setup `.exe`、Linux AppImage | 应用自动检查更新，并向成员提供每个新版本。在设置的[更新](https://docs.x.ai/grok-bot/settings-and-notifications#updates)部分选择 **重启以更新（Restart to Update）** 即可安装。**自动更新（Automatic updates）** 开启时（默认如此），应用还会在成员离开时安装已下载的更新。 |
| Linux `.deb` 或 `.rpm` | 应用不安装更新。新版本通过你的包管理器到达。 |

对于 macOS、Windows 和 AppImage 安装，没有任何设备策略、安装程序选项或仪表盘设置能关掉桌面应用更新。成员可以关闭 **自动更新**，让更新等待 **重启以更新**，但应用仍会检查并提供新版本。固定版本决定你安装哪个版本；之后应用仍会提供更新的版本。

旧构建会停止工作。当某个构建失去支持时，应用会用 **需要更新（Update required）** 盖住整个窗口，直到成员更新。构建在低于最低支持版本，或超过最长时限且有更新版本可用时失去支持。这适用于所有安装，包括 Linux 的 `.deb` 和 `.rpm` 包。两项限制都由远程设置且不公布，所以要为设备升级到当前版本安排固定的节奏。

### Linux 包更新

安装 `.deb` 会在 `/etc/apt/sources.list.d/grok-bot.sources` 添加一个已签名的 apt 仓库，安装 `.rpm` 会在 `/etc/yum.repos.d/grok-bot.repo` 添加一个已签名的仓库。设备随后在运行包升级时获取新的 Grok Bot 版本。

要控制 Linux 设备何时升级，可以：

* 用你的包管理器固定住这个包，例如 `apt-mark hold grok-bot`，准备好升级时再放开。
* 关掉仓库：在 `grok-bot.sources` 里设 `Enabled: no`，或在 `grok-bot.repo` 里设 `enabled=0`。包在每次安装和升级时会重写这些文件，并保留你的选择。然后由你自己从测试过的包文件发布新版本。

无论哪种方式，都要在已安装版本失去支持前升级。被固定住的包仍会看到 **需要更新** 界面。

在 `.deb` 或 `.rpm` 安装上，**需要更新** 界面会显示要运行的命令，并提供 **复制命令（Copy command）**：

* `.deb`：`sudo apt update && sudo apt install --only-upgrade grok-bot`
* `.rpm`：`sudo dnf upgrade --refresh grok-bot`

当仓库还没有新版本时，例如因为你把它关掉了，界面会改为提示成员下载并安装最新的包，并附上链接。完成任一步骤后，成员重启 Grok Bot。

## 更新托管电脑

托管电脑的镜像由系统维护，所以没有需要你固定或提供的镜像。电脑会通过以下三种方式之一切换到更新的镜像：

| 触发方式 | 会发生什么 | 由谁发起 |
| --- | --- | --- |
| 新镜像 | 空闲电脑会在后台逐步、没有固定时间表地用新镜像重建。在此之前，电脑停留在当前镜像。成员文件会保留，团队设置会再次运行。 | 自动，在后台 |
| **更新 Bot 的电脑（Update Bot's computer）** | 用最新镜像重建成员的电脑。为之后某个时间安排这项工作尚未对所有账号开放。 | 成员，在桌面应用的 **设置 → 电脑** 中，**Bot 的电脑** 下 |
| **重建虚拟机（Recreate VMs）** | 用最新镜像和团队设置脚本重建所选成员的电脑。 | Enterprise 管理员，从[管理成员电脑与数据](https://docs.x.ai/grok-bot/computers) |

运行中的电脑大约每天获取一次团队设置清单的变更；要更早应用变更，就重建这些电脑。在 Enterprise 上，[审计日志](https://docs.x.ai/grok-bot/teams-and-enterprises#audit-logs)会把电脑的更新、重置、重建和终止记录为 `grok_bot_vm` 事件，把涉及多个成员的操作记录为 `grok_bot_vm_bulk`。

## 打通网络路径

设备从 `cursor.com` 和 `downloads.cursor.com` 下载安装程序和桌面更新，应用会在[允许这些域名模式](https://docs.x.ai/grok-bot/proxies#allow-these-domain-patterns)列出的域名上访问其 API 和成员的托管电脑。推送应用之前，允许所有这些域名，包括嵌套的 `*.*.cursorvm.com` 模式，并让它们免于 TLS 检查。

## 上线清单

1. 退出会完全阻止 Grok Bot 的隐私模式（Legacy）。见[上线之前](https://docs.x.ai/grok-bot/teams-and-enterprises#before-you-roll-out)。
2. 打通网络：在网关上允许 Grok Bot 的域名，并让它们免于 TLS 检查。见[配置做 TLS 检查的代理](https://docs.x.ai/grok-bot/proxies)。
3. 在身份提供方中分配 Cursor 应用，因为 Grok Bot 登录使用你的 SSO。见[分配 Cursor 应用](https://docs.x.ai/grok-bot/identity-and-access#assign-the-cursor-app)。
4. 开启 Grok Bot 并选择谁能用。在 Enterprise 上，管理员从仪表盘开启 Grok Bot，并用 **管理组访问权限（Manage Group Access）** 限定范围；在 Teams 上，每位成员都已经有访问权。见[为你的团队启用 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises#enabling-grok-bot-for-your-team)。
5. 应用推荐的配置：在成员开始使用前，设置[推荐配置](https://docs.x.ai/grok-bot/teams-and-enterprises#recommended-configuration)中的管理员控制项。
6. 试点安装程序：为每个平台在几台设备上安装你选定的版本，登录，并确认应用能连接到托管电脑。
7. 推送到你的机群：把测试过的安装程序部署到所有者有访问权的每台设备。
8. 规划更新：为设备升级到新版本选定一个节奏。对 Linux，决定设备是从 Grok Bot 仓库升级，还是从你发布的包升级。

## 常见问题

### 我能关掉桌面应用的自动更新吗？

在 macOS、Windows 和 AppImage 安装上，不能。应用会检查更新并提供给成员。每位成员可以关闭 **自动更新**，让更新只在他们选择 **重启以更新** 时安装，但没有管理员控制项。Linux 的 `.deb` 和 `.rpm` 安装不会自行更新，所以你可以用包管理器控制它们。见[桌面应用如何更新](#how-desktop-updates-work)。

### 有 MSI 或 PKG 安装程序吗？

发布的安装程序是 macOS 的 `.dmg`、Windows 的 Setup `.exe`，以及 Linux 的 `.deb`、`.rpm` 或 AppImage。如果你的管理工具需要特定包格式，把 `.dmg` 或 `.exe` 包进它的格式里。

### 我的设备管理工具能触达托管电脑吗？

不能。托管电脑在云端运行 Linux，不加入 MDM。Enterprise 团队用[团队设置脚本](https://docs.x.ai/grok-bot/private-networks)在它上面安装自己的工具。如果你的身份提供方要求受管设备，见[允许从电脑登录 IdP 应用](https://docs.x.ai/grok-bot/identity-and-access#allow-sign-in-to-idp-apps-from-the-computer)。

### 我能固定托管电脑的镜像吗？

不能。镜像由系统维护，电脑会在后台切换到新镜像。Enterprise 管理员可以在自己选定的时间，从[管理成员电脑与数据](https://docs.x.ai/grok-bot/computers)重建电脑。

### 成员能在没有 IT 的情况下安装 Grok Bot 吗？

能，除非你的设备策略阻止。成员可以从管理员分享的仪表盘链接或[下载页](https://cursor.com/download/bot)下载应用。访问权仍取决于你的套餐，在 Enterprise 上还取决于 **管理组访问权限**。
