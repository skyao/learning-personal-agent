---
title: "文档：向组织部署 Grok Bot"
linkTitle: "文档：组织部署"
date: 2026-11-05
originalTitle: "Deploy Grok Bot to your organization"
sourceUrl: "https://cursor.com/docs/grok-bot/deployment"
altUrls: ["https://docs.x.ai/grok-bot/deployment"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：IT 团队用现有设备管理工具部署 Grok Bot 桌面应用：macOS（.dmg）、Windows（Setup .exe，按用户安装，可 /S 静默安装）、Linux（.deb、.rpm、AppImage），iPhone 需 iOS 18 以上，Android 需 9 以上。托管计算机是 Cursor 云端的 Linux 机器，每位成员一台，不加入 MDM，企业版可通过 Team Setup Scripts 安装自有工具。应用无法由管理员关闭更新，成员可关闭自动更新，但仍会收到新版提示；低于最低版本或超过最大期限的旧版会显示「Update required」，两项限制由 Cursor 远程设置且不公布。托管计算机的镜像由 Cursor 维护，新镜像出现时会在后台逐步重建空闲计算机；管理员可以在企业版里批量重建。登录用 Cursor 账号和 SSO，没有单独的 Grok Bot 登录。

**保留理由**：讲清了客户端只是聊天、审核和审批的瘦客户端，工作都在托管计算机上，以及版本与镜像更新的规则，对研究其运行架构和企业落地门槛有用。

---

你的 IT 团队用管理其他软件时已经在用的工具，在成员设备上安装 Grok Bot 桌面应用：下载带版本号的安装程序（installer）、推送，并决定设备何时迁移到新版本。用于开启 Grok Bot 和限定访问范围的仪表盘（dashboard）控制项位于 [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams)，部署 Cursor 编辑器见 [Deployment patterns](https://cursor.com/docs/enterprise/deployment-patterns)。

## 你部署的是什么

| 组件 | 运行于 | 更新方式 |
| --- | --- | --- |
| 桌面应用 | macOS（Apple silicon 和 Intel）、Windows（x64 和 Arm64）、Linux（x64 和 Arm64） | 应用自身，或 Linux `.deb` 和 `.rpm` 安装所用的包管理器 |
| iPhone 应用 | iOS 18 或更高版本 | App Store |
| Android 应用 | Android 9 或更高版本 | Google Play |
| 托管计算机（hosted computer） | Cursor 的云，每位成员一台 | Cursor |

这些应用是用于聊天、审核和审批的客户端。Bot 在成员的托管计算机上完成工作。你的设备管理工具能触达成员设备上的应用，但也仅止于此：托管计算机在 Cursor 的云中运行 Linux，不加入 MDM。要往托管计算机上安装你自己的工具，企业团队使用[团队设置脚本（Team Setup Scripts）](https://cursor.com/docs/grok-bot/private-networks#install-a-networking-client-with-team-setup)。

## 获取安装程序

- **Cursor 仪表盘。** [Grok Bot 页面](https://cursor.com/dashboard/bot)上的**下载 Grok Bot（Download Grok Bot）**设置行会安装应用，或复制一个你可以分享给成员的链接。
- **下载页面。** [cursor.com/download/bot](https://cursor.com/download/bot) 列出各平台和格式的当前安装程序。
- **发布源（release feed）。** 用于脚本化打包时，从下面的源读取当前版本，并下载它指定的文件。

| 平台 | 架构 | 格式 |
| --- | --- | --- |
| macOS | Apple silicon、Intel | `.dmg` |
| Windows | x64、Arm64 | Setup `.exe` |
| Linux | x64、Arm64 | `.deb`、`.rpm`、AppImage |

### 从发布源读取当前版本

每个平台在 `https://api2.cursor.sh/updates/api/download/stable/{platform}/sand` 有一个 JSON 源：

| `{platform}` | 安装程序 |
| --- | --- |
| `darwin-arm64` | macOS，Apple silicon |
| `darwin-x64` | macOS，Intel |
| `win32-x64-user` | Windows x64 |
| `win32-arm64-user` | Windows Arm64 |
| `linux-x64` | Linux x64 |
| `linux-arm64` | Linux Arm64 |

```
curl -s https://api2.cursor.sh/updates/api/download/stable/darwin-arm64/sand
```

你需要的字段：

| 字段 | 值 |
| --- | --- |
| `version` | 当前版本 |
| `commitSha` | 该版本来自的构建。Linux 下载 URL 会包含它。 |
| `downloadUrl` | 安装程序：macOS 上为 `.dmg`，Windows 上为 Setup `.exe`，Linux 上为 AppImage |
| `debUrl`、`rpmUrl` | 仅 Linux。`.deb` 和 `.rpm` 包。 |

响应可能带有其他字段。安装桌面应用不需要它们。

### 构建带版本号的 URL

macOS 和 Windows 安装程序为每个版本保留一个带版本号的 URL。把 `{version}` 替换为你想要的版本：

| 安装程序 | URL |
| --- | --- |
| macOS，Apple silicon | `https://downloads.cursor.com/grokbot/stable/darwin-arm64/{version}/Grok_Bot_{version}.dmg` |
| macOS，Intel | `https://downloads.cursor.com/grokbot/stable/darwin-x64/{version}/Grok_Bot_{version}_x64.dmg` |
| Windows x64 | `https://downloads.cursor.com/grokbot/stable/win32-x64/{version}/Grok_Bot_{version}_Setup.exe` |
| Windows Arm64 | `https://downloads.cursor.com/grokbot/stable/win32-arm64/{version}/Grok_Bot_{version}_Setup.exe` |

Linux 包位于该版本的 `commitSha` 下，在 `https://downloads.cursor.com/grokbot/stable/{commitSha}/linux/x64/` 或 `.../linux/arm64/` 中。从 Linux 源中的 `downloadUrl`、`debUrl` 和 `rpmUrl` 复制准确的文件 URL。

## 用你的设备管理工具推送桌面应用

- **macOS。** 用你现在运行的 Mac 管理工具部署 `.dmg`，例如 Jamf Pro、Kandji 或 Microsoft Intune。
- **Windows。** 用 Intune、Configuration Manager 或其他软件分发工具部署 Setup `.exe`。用 `Grok_Bot_{version}_Setup.exe /S` 静默安装。安装程序按用户安装，装到成员配置文件下的 `%LOCALAPPDATA%\Programs`，因此要在用户上下文中部署，而不是以 SYSTEM 身份部署。推送前先在试点设备上测试安装。
- **Linux。** 用你的配置管理工具安装 `.deb` 或 `.rpm`，例如 Ansible、Puppet 或 Chef。受管设备群优先使用这些包：包安装会按你的时间安排通过包管理器更新。参见 [Linux 包更新](#linux-package-updates)。
- **iPhone。** 成员从 [App Store](https://apps.apple.com/app/grok-bot/id6794501026) 在 iOS 18 或更高版本上安装 Grok Bot。
- **Android。** 成员从 [Google Play](https://play.google.com/store/apps/details?id=ai.x.grok.bot) 在 Android 9 或更高版本上安装 Grok Bot。要推送到受管设备，请在 Intune 或其他 Android 设备管理工具的受管 Google Play 中批准它。

成员通过你正常的 SSO 流程使用其 Cursor 账号登录。Grok Bot 没有单独的登录。要在 Okta 或 Entra ID 中分配 Cursor 应用，参见[配置身份与访问](https://cursor.com/docs/grok-bot/identity#assign-the-cursor-app)。

## 选择版本

- **固定你测试过的版本。** 下载该版本的安装程序，并将其保存在你自己的软件仓库或 MDM 包存储中。从你的副本部署，这样每台新设备都会得到相同的构建。Cursor 不公布旧安装程序可下载多久，而固定的构建只在 Cursor 停止支持它之前有效。参见[桌面更新如何工作](#how-desktop-updates-work)。
- **保存完整的 Linux URL。** Linux 包 URL 包含该版本的 `commitSha`，因此要把 URL 和版本一起记录下来。
- **检查设备运行的是哪个版本。** 在应用中打开账户菜单，选择**支持（Support）**，再选择**关于（About）**。对话框会显示**版本（Version）**，**复制版本信息（Copy version info）** 会复制版本、发布轨道（release track）和操作系统。

### 桌面更新如何工作

| 安装方式 | 更新如何到达 |
| --- | --- |
| macOS `.dmg`、Windows Setup `.exe`、Linux AppImage | 应用会自动检查更新，并向成员提供每个新版本。[设置](https://cursor.com/docs/grok-bot/settings#updates)的**更新（Updates）**部分中的**重启以更新（Restart to Update）**会安装它。开启**自动更新（Automatic Updates）**（默认开启）时，应用还会在成员离开时安装已下载的更新。 |
| Linux `.deb` 或 `.rpm` | 应用不会安装更新。新版本通过你的包管理器到达。 |

对于 macOS、Windows 和 AppImage 安装，没有任何设备策略、安装程序选项或仪表盘设置能关闭桌面应用更新。成员可以关闭**自动更新**，让更新等待**重启以更新**，但应用仍会检查并提供新版本。固定版本决定你安装哪个版本；之后应用仍会提供更新的版本。

旧构建会停止工作。当 Cursor 停止支持某个构建时，应用会用**需要更新（Update required）**覆盖整个窗口，直到成员更新。当构建低于 Cursor 的最低版本，或超过最大期限且有更新的版本可用时，该构建会失去支持。这适用于所有安装，包括 Linux `.deb` 和 `.rpm` 包。Cursor 会远程设置这两项限制且不公布，因此要为设备迁移到当前版本规划固定的节奏。

### Linux 包更新

安装 `.deb` 会在 `/etc/apt/sources.list.d/grok-bot.sources` 添加 Cursor 签名的 apt 仓库。安装 `.rpm` 会在 `/etc/yum.repos.d/grok-bot.repo` 添加签名的仓库。之后设备只要运行包升级，就会获取新的 Grok Bot 版本。

要控制 Linux 设备何时迁移：

- **保持包不升级。** 使用包管理器的 hold，例如 `apt-mark hold grok-bot`，并在你准备好升级时解除。
- **关闭仓库。** 在 `grok-bot.sources` 中设置 `Enabled: no`，或在 `grok-bot.repo` 中设置 `enabled=0`。包会在每次安装和升级时重写这些文件，并保留你的选择。然后由你自己从测试过的包文件发布新版本。

无论采用哪种方式，都要在已安装版本失去支持之前升级。被 hold 的包仍会看到**需要更新**屏幕。

## 更新托管计算机

Cursor 维护托管计算机的镜像，因此没有需要你固定或提供的镜像。计算机通过以下三种方式之一迁移到更新的镜像：

| 触发方式 | 会发生什么 | 由谁启动 |
| --- | --- | --- |
| 新镜像 | Cursor 在后台逐步、没有固定时间表地用新镜像重建空闲计算机。在此之前，计算机停留在当前镜像。成员文件会保留，团队设置会再次运行。 | Cursor，在后台 |
| **更新 Bot 的计算机（Update Bot's Computer）** | 用最新镜像重建成员的计算机。为稍后时间安排此操作并非所有账户都可用。 | 成员，在桌面应用的**设置（Settings）** > **计算机（Computer）** > **Bot 的计算机（Bot's computer）**中 |
| **重建虚拟机（Recreate VMs）** | 用最新镜像和团队设置脚本重建所选成员的计算机 | 企业版管理员，在[管理成员计算机与数据](https://cursor.com/docs/grok-bot/computers)中 |

运行中的计算机大约每天一次获取团队设置清单（manifest）的变更。要更快应用变更，请重建计算机。在企业版中，[审计日志](https://cursor.com/docs/enterprise/compliance-and-monitoring#audit-logs)会把计算机的更新、重置、重建和终止记录为 `grok_bot_vm` 事件，把跨多名成员的操作记录为 `grok_bot_vm_bulk`。

## 打通网络路径

设备从 `cursor.com` 和 `downloads.cursor.com` 下载安装程序和桌面更新，应用会连接 Cursor 的 API 以及成员的托管计算机，所用域名为[允许这些域名模式](https://cursor.com/docs/grok-bot/proxies#allow-these-domain-patterns)中列出的域名。推送应用之前，请允许所有这些域名（包括嵌套的 `*.*.cursorvm.com` 模式），并让它们免于 TLS 检查。

## 部署清单

1

### 退出隐私模式（Legacy）

隐私模式（Legacy）会完全阻止 Grok Bot。参见[推出之前](https://cursor.com/docs/grok-bot/teams#before-you-roll-out)。

2

### 清理你的网络

在你的网关上允许 Cursor 的域名，并让它们免于 TLS 检查。
参见[配置检查 TLS 的代理](https://cursor.com/docs/grok-bot/proxies)。

3

### 在你的身份提供商中分配 Cursor 应用

Grok Bot 登录使用你的 Cursor SSO。参见[分配 Cursor 应用](https://cursor.com/docs/grok-bot/identity#assign-the-cursor-app)。

4

### 开启 Grok Bot 并选择谁获得它

在企业版中，管理员从仪表盘开启 Grok Bot，并用**管理组访问（Manage Group Access）**限定范围。在团队版中，每位成员已经拥有访问权限。
参见[为你的团队启用 Grok Bot](https://cursor.com/docs/grok-bot/teams#enabling-grok-bot-for-your-team)。

5

### 应用推荐配置

在成员开始之前，设置[推荐配置](https://cursor.com/docs/grok-bot/teams#recommended-configuration)中的管理员控制项。

6

### 试点安装程序

在每个平台的几台设备上安装你选定的版本，登录，并确认应用能连接到托管计算机。

7

### 推送到你的设备群

把测试过的安装程序部署到所有者拥有访问权限的每台设备。

8

### 规划更新

为设备迁移到新版本选择一个节奏。对于 Linux，决定设备是从 Cursor 的仓库升级，还是从你发布的包升级。

## 常见问题（FAQ）

### 我可以关闭桌面应用的自动更新吗？

在 macOS、Windows 和 AppImage 安装上，不可以。应用会检查更新并向成员提供。每位成员可以关闭**自动更新**，让更新只在他们选择**重启以更新**时才安装，但没有管理员控制项。Linux `.deb` 和 `.rpm` 安装不会自行更新，因此你用包管理器控制它们。参见[桌面更新如何工作](#how-desktop-updates-work)。

### 有 MSI 或 PKG 安装程序吗？

已发布的安装程序是 macOS 的 `.dmg`、Windows 的 Setup `.exe`，以及 Linux 的 `.deb`、`.rpm` 或 AppImage。如果你的管理工具要求特定包格式，请把 `.dmg` 或 `.exe` 包装成该格式。

### 我的设备管理工具能触达托管计算机吗？

不能。托管计算机在 Cursor 的云中运行 Linux，不加入 MDM。企业团队用[团队设置脚本](https://cursor.com/docs/grok-bot/private-networks)在它上面安装自己的工具。如果你的身份提供商要求受管设备，参见[允许从计算机登录 IdP 应用](https://cursor.com/docs/grok-bot/identity#allow-sign-in-to-idp-apps-from-the-computer)。

### 我可以固定托管计算机的镜像吗？

不可以。Cursor 维护镜像，并在后台把计算机迁移到新镜像。企业版管理员可以在他们选择的时间从[管理成员计算机与数据](https://cursor.com/docs/grok-bot/computers)重建计算机。

### 成员可以在没有 IT 的情况下安装 Grok Bot 吗？

可以，除非你的设备策略阻止。成员可以从管理员分享的仪表盘链接或 [cursor.com/download/bot](https://cursor.com/download/bot) 下载应用。访问权限仍取决于你的套餐，在企业版中还取决于**管理组访问**。
