来源：https://learn.microsoft.com/en-us/microsoft-scout/managed-troubleshoot
取文：2026-11-10，直接下载

Troubleshoot Microsoft Scout in managed environments

[This article is prerelease documentation and is subject to change.]

Important

- You need to be part of the **[Frontier preview program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** and sign up to accept terms of participation to get **early access** to Microsoft Scout. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
- This is a preview feature.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

This guide helps IT and desktop engineers get Microsoft Scout working on hardened Windows environments: machines with proxies, SSL/TLS inspection, Microsoft Defender, AppLocker/WDAC, VDI/RDP, or non-admin users.

**How to use it:** Start with the symptom table, then follow only the sections that apply to your environment. Most steps are one-time configurations for your IT/security team.

Note

Several items in this article are workarounds for the current release. Where noted, a future Scout build handles the situation automatically and the workaround isn't needed.

## Quick reference

| What you see | Likely cause | Go to |
| --- | --- | --- |
| Sign-in window opens but never returns to the app | App running as the wrong account (elevated/SYSTEM), or protocol handler not registered for the user | [Run Scout as the signed-in user](#run-scout-as-the-signed-in-user), [Non-admin sign-in callback (protocol handler)](#non-admin-sign-in-callback-protocol-handler) |
| GitHub sign-in or authorization doesn't complete | Copilot CLI not enabled by policy for the GitHub enterprise or organization | [Enable GitHub Copilot CLI for your enterprise or organization](#enable-github-copilot-cli-for-your-enterprise-or-organization) |
| `fetch failed` / `Network request failed` at sign-in | Proxy blocking or decrypting the GitHub Copilot endpoints | [Network -- allow-list and exclude from TLS inspection](#network--allow-list-and-exclude-from-tls-inspection) |
| `copilot login exited with code 1: fetch failed` | The bundled Copilot component can't reach Copilot endpoints | [Network -- allow-list and exclude from TLS inspection](#network--allow-list-and-exclude-from-tls-inspection) |
| HTTP 403 / "GitHub Copilot Business or Enterprise required" after sign-in | Proxy is inspecting (decrypting) the Copilot endpoints | [Network — allow-list and exclude from TLS inspection](#network--allow-list-and-exclude-from-tls-inspection) |
| "Unable to verify access" / stuck on waitlist | The access policy couldn't be read (blocked `reg.exe` or registry ACL) — **not** a licensing problem | [Unable to verify access / waitlist screen](#unable-to-verify-access--waitlist-screen) |
| Crash on launch | Defender or AppLocker/WDAC blocking the executables | [App won't launch — Microsoft Defender and AppLocker/WDAC](#app-wont-launch--microsoft-defender-and-applockerwdac) |
| Crash on launch specifically in a Citrix session | Citrix HDX hook injection | [Citrix Virtual Apps and Desktops (HDX)](#citrix-virtual-apps-and-desktops-hdx--only-if-you-use-citrix) |
| Crash on launch in VDI/RDP | GPU unavailable | [VDI and RDP — launch with `--disable-gpu`](#vdi-and-rdp--launch-with---disable-gpu) |
| Must sign in again every session on VDI | Credential not roaming on non-persistent desktops | [Non-persistent and pooled VDI](#non-persistent-and-pooled-vdi--only-if-your-desktops-are-non-persistent) |
| "Failed to resolve documents path" in logs | Workspace on a redirected/protected folder | [Workspace and cache location](#workspace-and-cache-location) |

**Two things to remember throughout:**

- Scout ships **two** executables that both need network and security allowances: the **Scout app** and a **bundled GitHub Copilot component** (`copilot.exe`). Every allow list and exclusion must include **both**.
- The Copilot component uses **`githubcopilot.com`**, a **different domain** from `github.com`. Allow listing only `github.com` is the most common mistake.

## Run Scout as the signed-in user

Run Scout as the **normal signed-in user**, not "as administrator" with other credentials, and not as SYSTEM or a service. When it runs under a different account, the sign-in callback never returns to the app and Scout reads its per-user config from the wrong profile.

- Do machine-level prep (described in the next section) ahead of time by using admin rights, but **launch the app as the user**.
- The user doesn't need to be a local admin.

## Enable GitHub Copilot CLI for your enterprise or organization

Scout's GitHub sign-in and authorization flow depends on the **Copilot CLI** client policy. If your GitHub administrator doesn't enable Copilot CLI for the enterprise, or for the organization the user is associated with, the sign-in and authorization flow doesn't complete. This cause is separate from allow-listing or TLS inspection (see [Network -- allow-list and exclude from TLS inspection](#network--allow-list-and-exclude-from-tls-inspection)), so check it when sign-in fails.

**Fix (GitHub administrator):** Enable Copilot CLI for the enterprise, or for the organization the user is associated with.

1. Navigate to your enterprise. For example, go to the **Enterprises** page (`https://github.com/settings/enterprises`) on GitHub.com.
2. At the top of the page, select **AI controls**.
3. To manage Copilot policies, in the sidebar, select **Copilot**.
4. Under **Features & clients**, select **Configure features & clients**.
5. In the **Clients** section, for **Copilot CLI**, select your preferred policy.

In a reported customer case, enabling Copilot CLI for all organizations resolved the issue.

For more information, see the following GitHub documentation:

- [Administering Copilot CLI for your enterprise](https://docs.github.com/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise#enabling-or-disabling-copilot-cli)
- [GitHub Copilot policies for enterprises and organizations](https://docs.github.com/copilot/concepts/policies)
- [Managing policies and features for GitHub Copilot in your enterprise](https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies)

## Network — allow-list and exclude from TLS inspection

Allow-listing the hosts isn't enough. If your proxy **decrypts** (SSL/TLS-inspects) the GitHub Copilot endpoints, sign-in fails (`fetch failed`, or HTTP 403 after signing in) because the intercepting certificate breaks the trusted connection.

**Do:**

1. **Allow-list** the GitHub Copilot endpoints. Authoritative, always-current list: **<https://gh.io/copilot-firewall>** (include the Business/Enterprise API variants).
2. Also allow Scout's own service traffic (Microsoft 365 / Graph, in-app services, telemetry, and the update host).
3. **Exclude the Copilot endpoints from TLS/SSL inspection** (SSL bypass), not just from blocking.
4. Apply the config to **both** the Scout app and the bundled Copilot component.

**Self-check for a decrypting proxy:**

```
curl.exe -v https://api.githubcopilot.com
```

If the certificate **issuer is your corporate/internal CA** (instead of a public CA), the proxy is decrypting that host and must be excluded from inspection.

**Representative endpoints** (defer to `gh.io/copilot-firewall` for the current list):

```
github.com
api.github.com
api.githubcopilot.com
*.githubcopilot.com
copilot-proxy.githubusercontent.com
*.githubusercontent.com
```

Note

*Future release:* Scout can use your proxy and trust a corporate root CA, so inspection can stay on, and an in-app connectivity check names the failing host.

## "Unable to verify access" / waitlist screen

After an admin enables the Scout access policy, the app on the device still needs to **read** that policy value (`AllowScoutFrontierAccess`). If the read fails, Scout shows **"Unable to verify access."** This message means *the policy couldn't be read* — **not** that your organization lacks a license. Two common causes exist.

**A. `reg.exe` is blocked** (AppLocker/WDAC/EDR): Scout reads the policy by launching `reg.exe`. If `reg.exe` is blocked, the read fails even when run elevated.

**B. Non-admin registry read is denied:** the security policy restricts non-admin reads of `HKLM\SOFTWARE\Policies`.

**Diagnose (run as the non-admin end user):**

```
reg query "HKLM\SOFTWARE\Policies\Scout" /v AllowScoutFrontierAccess
```

- Returns a value → registry access is fine; the issue is elsewhere (usually AppLocker, see [App won't launch — Microsoft Defender and AppLocker/WDAC](#app-wont-launch--microsoft-defender-and-applockerwdac)).
- "Access is denied" → grant **Read** to the **Users** group on `HKLM\SOFTWARE\Policies\Scout`.

**Fix, choose one:**

**Option A: provision the policy and let Scout read it (preferred):**

1. Deploy via GPO/Intune: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Scout`, value **`AllowScoutFrontierAccess`** = **`1`** (REG\_DWORD).
2. Allow Scout to launch **`reg.exe`** (add the necessary AppLocker/WDAC/EDR exception). This action also lets Scout read your other registry-delivered settings.

**Option B: file-based fallback (only if you can't unblock `reg.exe`):**

Create a small file that grants access directly. It works on Windows and Mac.

- **Path:** `%USERPROFILE%\.scout\tenant-policy.json` (Mac: `~/.scout/tenant-policy.json`) - in the profile of the account Scout actually runs as (see [Run Scout as the signed-in user](#run-scout-as-the-signed-in-user)).
- **Contents (exactly):** `{"allowScoutFrontierAccess": true}` - boolean `true`, not `"true"`.
- **Encoding: UTF-8 without BOM.** A byte-order mark makes the file silently ignored, so don't use `Set-Content -Encoding utf8` or `Out-File` on Windows PowerShell 5.1.

Windows (BOM-safe):

```
$dir = "$env:USERPROFILE\.scout"
New-Item -ItemType Directory -Force -Path $dir | Out-Null
[IO.File]::WriteAllText("$dir\tenant-policy.json", '{"allowScoutFrontierAccess": true}')
```

Mac / Linux:

```
mkdir -p ~/.scout
printf '{"allowScoutFrontierAccess": true}' > ~/.scout/tenant-policy.json
```

Note

*Future release:* Scout reads the policy directly (no `reg.exe`), so both options go away - admins just provision the value via GPO/Intune.

## Non-admin sign-in callback (protocol handler)

If sign-in finishes in the browser but the app on a non-admin machine doesn't get the auth callback, the user might not be registered for the auth callback protocol (`ms-clawpilot://`). As a temporary workaround, register it per user (deploy as a `.reg` file via Intune or GPO, or run once per user):

```
[HKCU\SOFTWARE\Classes\ms-clawpilot]
@="URL:ms-clawpilot"
"URL Protocol"=""

[HKCU\SOFTWARE\Classes\ms-clawpilot\shell\open\command]
@="\"C:\\Program Files\\Microsoft Scout\\Microsoft Scout.exe\" \"%1\""
```

Note

*Future release:* the installer registers this protocol machine-wide, so no manual step is needed. (Some prerelease screens still show the internal name **Clawpilot**. This name is expected and refers to Microsoft Scout.)

## App won't launch — Microsoft Defender and AppLocker/WDAC

Security controls can block Scout's executables and cause a **crash on launch**.

**Microsoft Defender:** Add **both** the Scout app and the bundled Copilot component to the Defender allow list (Controlled Folder Access "allowed apps" and any required ASR exclusions).

- Make these allowances through your **Intune/central policy**, not locally — a local `Add-MpPreference` exclusion can be overridden by Intune, and Tamper Protection can silently ignore local changes.

**AppLocker / WDAC:** Scout spawns several executables that all need to be permitted:

| Executable | Location (under `C:\Program Files\Microsoft Scout\`) |
| --- | --- |
| `Microsoft Scout.exe` | root |
| `copilot.exe` | root |
| `node-runner.exe` | `resources\app.asar.unpacked\node_modules\@github\copilot-win32-x64\` |
| `node.exe` | `resources\node\` |
| `workiq.exe` (optional, M365 features) | `%USERPROFILE%\.copilot-dev\bin\` |

**Recommended — single publisher rule** (covers all binaries and survives updates):
`Publisher: O=Microsoft Corporation, Product: Microsoft Scout`

**Alternative — path rule:** `%PROGRAMFILES%\Microsoft Scout\**` (Allow, Everyone). *Note: won't cover `workiq.exe`.*

**Verify (run as the non-admin end user):**

```
Get-AppLockerPolicy -Effective | Test-AppLockerPolicy -Path "C:\Program Files\Microsoft Scout\Microsoft Scout.exe" -User "DOMAIN\username"
```

Note

*Future release:* if security software blocks it, Scout explains that instead of crashing.

## VDI and RDP — launch with `--disable-gpu`

In VDI and RDP sessions, the GPU is often unavailable, and the graphics process can fail to start, crashing Scout at launch.

- Launch Scout with the **`--disable-gpu`** switch in VDI and RDP deployments.
- **Don't add `--no-sandbox`** - it weakens security and isn't a supported workaround.

Note

*Future release:* Scout detects the unusable GPU and recovers automatically.

## Citrix Virtual Apps and Desktops (HDX) — only if you use Citrix

Citrix HDX injects user-mode hook DLLs into other processes. These DLLs are incompatible with Scout's browser-engine sandbox and **crash Scout at launch** in a Citrix session. Exclude Scout from Citrix's user-mode hooking.

1. Add Scout's executable to the Citrix **excluded image names** value (`CtxHook\ExcludedImageNames`).
2. Use a **space-free executable name** (or the 8.3 short name). The Citrix exclusion list is space-delimited, so a name containing a space never matches.
3. Combine with the Defender allow-list (see [App won't launch — Microsoft Defender and AppLocker/WDAC](#app-wont-launch--microsoft-defender-and-applockerwdac)) and, on VDI and RDP, `--disable-gpu` (see [VDI and RDP — launch with `--disable-gpu`](#vdi-and-rdp--launch-with---disable-gpu)).
4. The kernel-mode exclusion (`CtxUvi\UviProcessExcludes`) is usually not required. Use only as a fallback. It has a short per-name length limit and needs a reboot.

Note

*Future release:* Scout ships a space-free executable name by default and fails gracefully with guidance instead of crashing.

## Non-persistent and pooled VDI — only if your desktops are non-persistent

On non-persistent (pooled) VDI, logoff wipes per-session changes.

1. **Bake all machine-level changes into the golden master image**: Defender allow-list, AppLocker rules, Citrix exclusion, `--disable-gpu` shortcut, and the access policy.
2. **Sign-in doesn't persist** by default (the credential is lost each session). Use **FSLogix** (or equivalent credential or profile roaming) so sign-in survives across sessions.

## Workspace and cache location

If you redirect your **Documents** folder to OneDrive (Known-Folder-Move) or protect it by Controlled Folder Access, Scout can fail to resolve or write its workspace. The log shows the error *"Failed to resolve documents path"*.

- Ensure that you don't force Scout's workspace or cache onto a OneDrive-redirected or CFA-protected path. A local profile path, such as one under `%LOCALAPPDATA%`, is normally safe.
- If you redirect **Documents** to OneDrive, exclude Scout's working folder from CFA or point its workspace to another location.

Note

*Future release:* Scout automatically picks a safe default location.

## How to capture logs (including sign-in and pre-auth)

When you launch Scout from a terminal, you stream all main-process startup logging live, including the sign-in flow, and capture everything unconditionally. Use this method when sign-in fails early or in-app diagnostics aren't enabled.

**Before you start, quit Scout completely.** It uses a single-instance lock, so if it's already running, a second launch just hands off to the running instance and exits with no useful output. This condition is the most common reason capture produces nothing.

- Windows: close the window **and** right-click the system-tray icon → **Quit**.
- macOS: press **Cmd+Q**.

The terminal stays attached while Scout runs; output streams live until you close Scout or press Ctrl+C. Piped output is plain text, ideal for sharing.

**Windows per-user install (the default):** `%LOCALAPPDATA%\Programs\Microsoft Scout\Microsoft Scout.exe`

```
& "$env:LOCALAPPDATA\Programs\Microsoft Scout\Microsoft Scout.exe" 2>&1 | Tee-Object -FilePath "$env:USERPROFILE\Desktop\scout-log.txt"
```

**Windows per-machine install (all users):** `C:\Program Files\Microsoft Scout\Microsoft Scout.exe`

```
& "C:\Program Files\Microsoft Scout\Microsoft Scout.exe" 2>&1 | Tee-Object -FilePath "$env:USERPROFILE\Desktop\scout-log.txt"
```

**macOS:** run the binary inside the app bundle directly. Don't use `open -a` (it detaches from the terminal and captures nothing).

```
"/Applications/Microsoft Scout.app/Contents/MacOS/Microsoft Scout" 2>&1 | tee ~/Desktop/scout-log.txt
```

**Not sure of the Windows path?** Discover it from the uninstall entries and use `DisplayIcon` (or the path in `UninstallString`) as the launch target:

```
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*','HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*' | Where-Object { $_.DisplayName -like '*Scout*' } | Select-Object DisplayName, DisplayIcon, UninstallString
```

**Renderer / Chromium logs** are hidden by default. Only if support asks, set `ELECTRON_ENABLE_LOGGING=1` before launching (Windows: `$env:ELECTRON_ENABLE_LOGGING = "1"`; macOS: prefix the command with `ELECTRON_ENABLE_LOGGING=1`).

Share the console output or the `scout-log.txt` file with support. The data/log directory is `~/.copilot` on both platforms; a persistent log (`~/.copilot/m-diagnostics.jsonl`) exists only after in-app diagnostics are enabled. The terminal method above works even before that.

## Admin self-check commands

```
netsh winhttp show proxy
curl.exe -v https://api.githubcopilot.com    # corporate CA in the cert issuer = the proxy is decrypting this host
reg query "HKLM\SOFTWARE\Policies\Scout" /v AllowScoutFrontierAccess
```

## Related content

- [Admin access overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)
- [Set up Microsoft Scout with Intune](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)
- [Manage admin controls in Intune for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy)
- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Microsoft Scout common questions](https://learn.microsoft.com/en-us/microsoft-scout/faq)
