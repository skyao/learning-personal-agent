---
title: "在受管环境中排查 Microsoft Scout 问题"
linkTitle: "文档：受管环境排障"
date: 2026-09-01
originalTitle: "Troubleshoot Microsoft Scout in managed environments"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/managed-troubleshoot"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [运行环境, 安全]
products: [microsoft-autopilot]
updatedAt: "2026-09-01"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-08-31"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：文档面向在加固 Windows 环境（代理、SSL/TLS 检查、Microsoft Defender、AppLocker/WDAC、VDI/RDP、非管理员用户）中部署 Scout 的 IT 和桌面工程师，以症状表开头。要点包括：Scout 有两个可执行文件（Scout app 与捆绑的 copilot.exe），许可和排除都要覆盖两者；Copilot 组件使用 githubcopilot.com 而非 github.com；代理解密 Copilot 端点会导致登录失败，需排除 TLS 检查。"Unable to verify access" 是因为读不到 AllowScoutFrontierAccess，而不是许可问题，可用 reg.exe 或 tenant-policy.json 回退方式处理。其余涉及 Defender/AppLocker 规则、VDI 下的 --disable-gpu、Citrix HDX、非持久 VDI、工作区位置和日志采集；若干做法为当前版本的变通办法。

**保留理由**：这是加固环境中登录失败、启动崩溃等问题的官方排障手册，含网络域名、AppLocker 规则和日志采集方法。

---

在受管环境中排查 Microsoft Scout 问题

[本文为预发布文档，内容可能变更。]

重要

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能获得 Microsoft Scout 的**早期访问**权限。Frontier 让你直接接触 Microsoft 最新的 AI 创新。Frontier 预览受你客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是预览功能。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布前提供，以便客户提前访问并提供反馈。
- 有关详细信息，请访问我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

本指南帮助 IT 和桌面工程师让 Microsoft Scout 在加固的 Windows 环境中正常工作：这些机器带有代理、SSL/TLS 检查、Microsoft Defender、AppLocker/WDAC、VDI/RDP，或使用非管理员用户。

**如何使用本指南：** 先看症状表，然后只遵循适用于你所在环境的章节。大多数步骤是 IT/安全团队的一次性配置。

注意

本文中的若干项目是针对当前版本的变通办法。在注明的地方，未来的 Scout 版本会自动处理该情况，不再需要变通办法。

## 快速参考

| 你看到的现象 | 可能的原因 | 参考 |
| --- | --- | --- |
| 登录窗口打开但从不返回应用 | 应用以错误的账户（提权/SYSTEM）运行，或协议处理程序未为用户注册 | [以登录用户身份运行 Scout](#run-scout-as-the-signed-in-user)、[非管理员登录回调（协议处理程序）](#non-admin-sign-in-callback-protocol-handler) |
| GitHub 登录或授权无法完成 | 策略未为 GitHub 企业或组织启用 Copilot CLI | [为你的企业或组织启用 GitHub Copilot CLI](#enable-github-copilot-cli-for-your-enterprise-or-organization) |
| 登录时出现 `fetch failed` / `Network request failed` | 代理阻止或解密 GitHub Copilot 端点 | [网络——加入允许列表并排除 TLS 检查](#network--allow-list-and-exclude-from-tls-inspection) |
| `copilot login exited with code 1: fetch failed` | 捆绑的 Copilot 组件无法访问 Copilot 端点 | [网络——加入允许列表并排除 TLS 检查](#network--allow-list-and-exclude-from-tls-inspection) |
| 登录后出现 HTTP 403 /「GitHub Copilot Business or Enterprise required」 | 代理正在检查（解密）Copilot 端点 | [网络——加入允许列表并排除 TLS 检查](#network--allow-list-and-exclude-from-tls-inspection) |
| 「Unable to verify access」/ 卡在候补名单 | 无法读取访问策略（`reg.exe` 被阻止或注册表 ACL 限制）——**不是**许可问题 | [「Unable to verify access」/ 候补名单界面](#unable-to-verify-access--waitlist-screen) |
| 启动时崩溃 | Defender 或 AppLocker/WDAC 阻止了可执行文件 | [应用无法启动——Microsoft Defender 与 AppLocker/WDAC](#app-wont-launch--microsoft-defender-and-applockerwdac) |
| 仅在 Citrix 会话中启动时崩溃 | Citrix HDX 钩子注入 | [Citrix Virtual Apps and Desktops (HDX)](#citrix-virtual-apps-and-desktops-hdx--only-if-you-use-citrix) |
| 在 VDI/RDP 中启动时崩溃 | GPU 不可用 | [VDI 和 RDP——以 `--disable-gpu` 启动](#vdi-and-rdp--launch-with---disable-gpu) |
| 在 VDI 上每个会话都必须重新登录 | 凭据在非持久桌面上不漫游 | [非持久和池化 VDI](#non-persistent-and-pooled-vdi--only-if-your-desktops-are-non-persistent) |
| 日志中出现「Failed to resolve documents path」 | 工作区位于重定向/受保护的文件夹 | [工作区与缓存位置](#workspace-and-cache-location) |

**始终需要记住的两件事：**

- Scout 附带**两个**可执行文件，两者都需要网络和安全许可：**Scout 应用**和一个**捆绑的 GitHub Copilot 组件**（`copilot.exe`）。每一份允许列表和排除项都必须**同时**包含两者。
- Copilot 组件使用 **`githubcopilot.com`**，这是一个与 `github.com` **不同的域**。只把 `github.com` 加入允许列表是最常见的错误。

## 以登录用户身份运行 Scout

以**正常的登录用户**运行 Scout，而不是用其他凭据「以管理员身份」运行，也不要作为 SYSTEM 或服务运行。当它用不同账户运行时，登录回调永远不会返回应用，Scout 会从错误的配置文件读取其每用户配置。

- 提前用管理员权限做机器级准备（在下一节说明），但**以用户身份启动应用**。
- 用户不需要是本地管理员。

## 为你的企业或组织启用 GitHub Copilot CLI

Scout 的 GitHub 登录和授权流程依赖 **Copilot CLI** 客户端策略。如果你的 GitHub 管理员没有为企业或用户所属的组织启用 Copilot CLI，登录和授权流程就无法完成。这个原因与允许列表或 TLS 检查无关（参见[网络——加入允许列表并排除 TLS 检查](#network--allow-list-and-exclude-from-tls-inspection)），因此登录失败时也要检查它。

**修复（GitHub 管理员）：** 为企业或用户所属的组织启用 Copilot CLI。

1. 导航到你的企业。例如，在 GitHub.com 上转到 **Enterprises** 页面（`https://github.com/settings/enterprises`）。
2. 在页面顶部，选择 **AI controls**。
3. 要管理 Copilot 策略，在边栏中选择 **Copilot**。
4. 在 **Features & clients** 下，选择 **Configure features & clients**。
5. 在 **Clients** 部分，为 **Copilot CLI** 选择你偏好的策略。

在一个已报告的客户案例中，为所有组织启用 Copilot CLI 解决了该问题。

有关详细信息，请参阅以下 GitHub 文档：

- [为你的企业管理 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise#enabling-or-disabling-copilot-cli)
- [企业或组织的 GitHub Copilot 策略](https://docs.github.com/copilot/concepts/policies)
- [在你的企业中管理 GitHub Copilot 的策略和功能](https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies)

## 网络——加入允许列表并排除 TLS 检查

仅把主机加入允许列表还不够。如果你的代理**解密**（SSL/TLS 检查）GitHub Copilot 端点，登录就会失败（`fetch failed`，或登录后 HTTP 403），因为拦截证书破坏了受信任的连接。

**要做的：**

1. 把 GitHub Copilot 端点**加入允许列表**。权威且始终最新的列表：**<https://gh.io/copilot-firewall>**（包含 Business/Enterprise API 变体）。
2. 同时允许 Scout 自身的服务流量（Microsoft 365 / Graph、应用内服务、遥测以及更新主机）。
3. **把 Copilot 端点排除在 TLS/SSL 检查之外**（SSL 绕过），而不仅仅是不阻止它们。
4. 对 **Scout 应用**和捆绑的 Copilot 组件**都**应用该配置。

**针对解密代理的自检：**

```
curl.exe -v https://api.githubcopilot.com
```

如果证书**颁发者是贵公司的内部 CA**（而不是公共 CA），说明代理正在解密该主机，必须将它排除在检查之外。

**代表性端点**（当前列表以 `gh.io/copilot-firewall` 为准）：

```
github.com
api.github.com
api.githubcopilot.com
*.githubcopilot.com
copilot-proxy.githubusercontent.com
*.githubusercontent.com
```

注意

*未来版本：* Scout 可以使用你的代理并信任企业根 CA，因此检查可以保持开启，并且应用内连接检查会指出失败的主机。

## 「Unable to verify access」/ 候补名单界面

在管理员启用 Scout 访问策略之后，设备上的应用仍然需要**读取**该策略值（`AllowScoutFrontierAccess`）。如果读取失败，Scout 会显示 **「Unable to verify access」**。此消息意味着*策略无法被读取*——**不是**你的组织缺少许可证。存在两种常见原因。

**A. `reg.exe` 被阻止**（AppLocker/WDAC/EDR）：Scout 通过启动 `reg.exe` 来读取策略。如果 `reg.exe` 被阻止，即使以提权方式运行，读取也会失败。

**B. 非管理员注册表读取被拒绝：** 安全策略限制对 `HKLM\SOFTWARE\Policies` 的非管理员读取。

**诊断（以非管理员最终用户身份运行）：**

```
reg query "HKLM\SOFTWARE\Policies\Scout" /v AllowScoutFrontierAccess
```

- 返回一个值 → 注册表访问正常；问题在别处（通常是 AppLocker，参见[应用无法启动——Microsoft Defender 与 AppLocker/WDAC](#app-wont-launch--microsoft-defender-and-applockerwdac)）。
- 「Access is denied」→ 对 `HKLM\SOFTWARE\Policies\Scout` 上的 **Users** 组授予**读取**权限。

**修复，任选其一：**

**选项 A：预置策略并让 Scout 读取它（推荐）：**

1. 通过 GPO/Intune 部署：`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Scout`，值 **`AllowScoutFrontierAccess`** = **`1`**（REG\_DWORD）。
2. 允许 Scout 启动 **`reg.exe`**（添加必要的 AppLocker/WDAC/EDR 例外）。此操作也会让 Scout 读取你通过注册表下发的其他设置。

**选项 B：基于文件的回退方式（仅当你无法解除对 `reg.exe` 的阻止时）：**

创建一个小文件，直接授予访问权限。它适用于 Windows 和 Mac。

- **路径：** `%USERPROFILE%\.scout\tenant-policy.json`（Mac：`~/.scout/tenant-policy.json`）——位于 Scout 实际运行所用账户的配置文件中（参见[以登录用户身份运行 Scout](#run-scout-as-the-signed-in-user)）。
- **内容（完全一致）：** `{"allowScoutFrontierAccess": true}`——布尔值 `true`，而不是 `"true"`。
- **编码：不带 BOM 的 UTF-8。** 字节顺序标记会让文件被静默忽略，所以在 Windows PowerShell 5.1 上不要使用 `Set-Content -Encoding utf8` 或 `Out-File`。

Windows（BOM 安全）：

```
$dir = "$env:USERPROFILE\.scout"
New-Item -ItemType Directory -Force -Path $dir | Out-Null
[IO.File]::WriteAllText("$dir\tenant-policy.json", '{"allowScoutFrontierAccess": true}')
```

Mac / Linux：

```
mkdir -p ~/.scout
printf '{"allowScoutFrontierAccess": true}' > ~/.scout/tenant-policy.json
```

注意

*未来版本：* Scout 直接读取策略（不使用 `reg.exe`），因此两种选项都会消失——管理员只需通过 GPO/Intune 预置该值。

## 非管理员登录回调（协议处理程序）

如果登录在浏览器中完成，但非管理员机器上的应用没有收到认证回调，可能是用户没有注册认证回调协议（`ms-clawpilot://`）。作为临时变通办法，按用户注册它（通过 Intune 或 GPO 以 `.reg` 文件部署，或为每个用户运行一次）：

```
[HKCU\SOFTWARE\Classes\ms-clawpilot]
@="URL:ms-clawpilot"
"URL Protocol"=""

[HKCU\SOFTWARE\Classes\ms-clawpilot\shell\open\command]
@="\"C:\\Program Files\\Microsoft Scout\\Microsoft Scout.exe\" \"%1\""
```

注意

*未来版本：* 安装程序会在机器范围注册此协议，因此无需手动步骤。（某些预发布界面仍显示内部名称 **Clawpilot**。此名称是预期的，指的就是 Microsoft Scout。）

## 应用无法启动——Microsoft Defender 与 AppLocker/WDAC

安全控制可能阻止 Scout 的可执行文件，导致**启动时崩溃**。

**Microsoft Defender：** 把 **Scout 应用**和捆绑的 Copilot 组件**都**加入 Defender 允许列表（受控文件夹访问的「允许的应用」以及任何必需的 ASR 排除项）。

- 通过你的 **Intune/中心策略**做这些许可，而不是在本地做——本地的 `Add-MpPreference` 排除项可能被 Intune 覆盖，而且篡改防护（Tamper Protection）可能会静默忽略本地更改。

**AppLocker / WDAC：** Scout 会生成多个可执行文件，它们都需要被允许：

| 可执行文件 | 位置（位于 `C:\Program Files\Microsoft Scout\` 下） |
| --- | --- |
| `Microsoft Scout.exe` | 根目录 |
| `copilot.exe` | 根目录 |
| `node-runner.exe` | `resources\app.asar.unpacked\node_modules\@github\copilot-win32-x64\` |
| `node.exe` | `resources\node\` |
| `workiq.exe`（可选，M365 功能） | `%USERPROFILE%\.copilot-dev\bin\` |

**推荐——单条发布者规则**（覆盖所有二进制文件并在更新后仍然有效）：
`Publisher: O=Microsoft Corporation, Product: Microsoft Scout`

**替代——路径规则：** `%PROGRAMFILES%\Microsoft Scout\**`（Allow，Everyone）。*注意：不会覆盖 `workiq.exe`。*

**验证（以非管理员最终用户身份运行）：**

```
Get-AppLockerPolicy -Effective | Test-AppLockerPolicy -Path "C:\Program Files\Microsoft Scout\Microsoft Scout.exe" -User "DOMAIN\username"
```

注意

*未来版本：* 如果安全软件阻止它，Scout 会解释这一情况，而不是崩溃。

## VDI 和 RDP——以 `--disable-gpu` 启动

在 VDI 和 RDP 会话中，GPU 通常不可用，图形进程可能无法启动，导致 Scout 在启动时崩溃。

- 在 VDI 和 RDP 部署中，以 **`--disable-gpu`** 开关启动 Scout。
- **不要添加 `--no-sandbox`**——它会削弱安全性，且不是受支持的变通办法。

注意

*未来版本：* Scout 会检测到不可用的 GPU 并自动恢复。

## Citrix Virtual Apps and Desktops (HDX)——仅当你使用 Citrix 时

Citrix HDX 会把用户模式钩子 DLL 注入其他进程。这些 DLL 与 Scout 的浏览器引擎沙箱不兼容，并会在 Citrix 会话中**导致 Scout 启动时崩溃**。请把 Scout 排除在 Citrix 的用户模式挂钩之外。

1. 把 Scout 的可执行文件加入 Citrix 的**排除映像名称**值（`CtxHook\ExcludedImageNames`）。
2. 使用**不含空格的可执行文件名**（或 8.3 短名称）。Citrix 排除列表以空格分隔，因此包含空格的名称永远不会匹配。
3. 结合 Defender 允许列表（参见[应用无法启动——Microsoft Defender 与 AppLocker/WDAC](#app-wont-launch--microsoft-defender-and-applockerwdac)），并在 VDI 和 RDP 上结合 `--disable-gpu`（参见 [VDI 和 RDP——以 `--disable-gpu` 启动](#vdi-and-rdp--launch-with---disable-gpu)）。
4. 内核模式排除（`CtxUvi\UviProcessExcludes`）通常不需要。只作为回退使用。它对每个名称有较短的长度限制，并且需要重新启动。

注意

*未来版本：* Scout 默认附带不含空格的可执行文件名，并在失败时给出指引而不是崩溃。

## 非持久和池化 VDI——仅当你的桌面为非持久时

在非持久（池化）VDI 上，注销会清除每个会话的更改。

1. **把所有机器级更改烘焙进黄金母版映像**：Defender 允许列表、AppLocker 规则、Citrix 排除项、`--disable-gpu` 快捷方式以及访问策略。
2. **登录状态默认不会持久化**（凭据在每个会话都会丢失）。使用 **FSLogix**（或等效的凭据或配置文件漫游），使登录状态跨会话保留。

## 工作区与缓存位置

如果你把**文档**文件夹重定向到 OneDrive（Known-Folder-Move），或用受控文件夹访问保护它，Scout 可能无法解析或写入其工作区。日志会显示错误*「Failed to resolve documents path」*。

- 确保你没有强制把 Scout 的工作区或缓存放在 OneDrive 重定向或受 CFA 保护的路径上。本地配置文件路径（例如位于 `%LOCALAPPDATA%` 下的路径）通常是安全的。
- 如果你把**文档**重定向到 OneDrive，请把 Scout 的工作文件夹排除在 CFA 之外，或将其工作区指向其他位置。

注意

*未来版本：* Scout 会自动选择一个安全的默认位置。

## 如何采集日志（包括登录和预认证）

当你从终端启动 Scout 时，所有主进程启动日志都会实时流式输出，包括登录流程，并无条件捕获全部内容。当登录很早就失败，或应用内诊断未启用时，请使用此方法。

**开始之前，请完全退出 Scout。** 它使用单实例锁，因此如果它已在运行，第二次启动只会把控制权交给正在运行的实例并退出，没有任何有用的输出。这是采集不到内容最常见的原因。

- Windows：关闭窗口**并**右键单击系统托盘图标 → **Quit**。
- macOS：按 **Cmd+Q**。

Scout 运行期间终端会保持连接；在你关闭 Scout 或按 Ctrl+C 之前，输出会实时流式传输。通过管道输出的内容是纯文本，非常适合分享。

**Windows 每用户安装（默认）：** `%LOCALAPPDATA%\Programs\Microsoft Scout\Microsoft Scout.exe`

```
& "$env:LOCALAPPDATA\Programs\Microsoft Scout\Microsoft Scout.exe" 2>&1 | Tee-Object -FilePath "$env:USERPROFILE\Desktop\scout-log.txt"
```

**Windows 每机器安装（所有用户）：** `C:\Program Files\Microsoft Scout\Microsoft Scout.exe`

```
& "C:\Program Files\Microsoft Scout\Microsoft Scout.exe" 2>&1 | Tee-Object -FilePath "$env:USERPROFILE\Desktop\scout-log.txt"
```

**macOS：** 直接运行应用包内的二进制文件。不要使用 `open -a`（它会与终端分离，采集不到任何内容）。

```
"/Applications/Microsoft Scout.app/Contents/MacOS/Microsoft Scout" 2>&1 | tee ~/Desktop/scout-log.txt
```

**不确定 Windows 路径？** 从卸载条目中发现它，并使用 `DisplayIcon`（或 `UninstallString` 中的路径）作为启动目标：

```
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*','HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*' | Where-Object { $_.DisplayName -like '*Scout*' } | Select-Object DisplayName, DisplayIcon, UninstallString
```

**渲染器 / Chromium 日志**默认隐藏。仅在支持人员要求时，在启动前设置 `ELECTRON_ENABLE_LOGGING=1`（Windows：`$env:ELECTRON_ENABLE_LOGGING = "1"`；macOS：在命令前加上 `ELECTRON_ENABLE_LOGGING=1`）。

把控制台输出或 `scout-log.txt` 文件分享给支持人员。两个平台上的数据/日志目录都是 `~/.copilot`；持久日志（`~/.copilot/m-diagnostics.jsonl`）只在启用应用内诊断后存在。上面的终端方法即使在启用之前也可用。

## 管理员自检命令

```
netsh winhttp show proxy
curl.exe -v https://api.githubcopilot.com    # corporate CA in the cert issuer = the proxy is decrypting this host
reg query "HKLM\SOFTWARE\Policies\Scout" /v AllowScoutFrontierAccess
```

## 相关内容

- [Microsoft Scout 管理员访问概述](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)
- [使用 Intune 设置 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)
- [在 Intune 中管理 Microsoft Scout 的管理员控制项](https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy)
- [开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Microsoft Scout 常见问题](https://learn.microsoft.com/en-us/microsoft-scout/faq)
