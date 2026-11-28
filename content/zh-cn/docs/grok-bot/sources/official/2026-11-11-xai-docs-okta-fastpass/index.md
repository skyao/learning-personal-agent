---
title: "文档（docs.x.ai）：设置 Okta Verify 与 FastPass"
linkTitle: "docs.x.ai：Okta FastPass"
date: 2026-11-11
originalTitle: "Set up Okta Verify and FastPass"
sourceUrl: "https://docs.x.ai/grok-bot/okta-fastpass"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-11）"
tags: [运行环境, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的文档现以 docs.x.ai（SpaceXSI Docs）为准，cursor.com 的文档地址已 308 跳转到这里。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：面向登录策略要求 Okta FastPass 的 Okta 管理员，说明如何让 Bot 在其电脑的浏览器里登录受 Okta 保护的应用。Okta Verify 通过仅限 Enterprise 的 Team Setup Scripts 安装，使用固定的 Okta Verify 7.1.3.0 版本。步骤依次为：在 Okta 中启用 Okta Verify for Linux 功能并确认 signed_nonce 方法可用；在 Cursor 控制台添加 Team Setup Script，参数带上组织地址；在每台电脑上登记一次 Okta Verify；用系统日志中的 auth_via_mfa 与 user.session.start 事件验证。若团队限制出站流量，须放行 anysphere.okta.com 和自己的 Okta 组织。限制包括：每个电脑用户一个窗口，窗口在 5 分钟无登录后关闭，并且粘贴口令须用右键菜单，Ctrl+V 会使 Linux 版崩溃。

**保留理由**：补充 Bot 电脑在企业身份体系（Okta）下如何登录的具体步骤与限制，已收的 docs-identity 只涉及概述。

---

设置 Okta Verify 与 FastPass

本指南面向登录策略要求 Okta FastPass 的 Okta 管理员。Grok Bot 计算机自带一个设置脚本，用来安装 Okta Verify 并启动 FastPass 所需的服务，使 Bot 能在计算机的浏览器中登录受 Okta 保护的应用。为 Cursor 应用分配权限及其他 Okta 和 Entra ID 设置见[配置身份与访问](https://docs.x.ai/grok-bot/identity-and-access)。

> Okta Verify 通过 [Team Setup Scripts](https://docs.x.ai/grok-bot/teams-and-enterprises#team-setup-scripts) 安装，该功能仅限 Enterprise。

## 开始之前

* 你是 Okta 管理员，也是 Enterprise 套餐上的 Cursor 团队管理员。
* 如果你的团队用[网络控制（Network Controls）](https://docs.x.ai/grok-bot/security#network-policy)限制出站流量，请把 `anysphere.okta.com` 和你自己的 Okta 组织加入允许列表，例如 `yourorg.okta.com`。无论登录哪个组织，每个团队都从 `anysphere.okta.com` 下载 Okta Verify 安装包。

## 1. 配置你的 Okta 组织

请在任何人于 Grok Bot 计算机上使用 FastPass 之前，在 Okta 管理控制台中完成这些设置。

1. 在**设置（Settings）** > **功能（Features）**下启用 **Okta Verify for Linux** 功能（`ftrl2df4GICAJ5xl1QSU`），或用 `POST /api/v1/features/ftrl2df4GICAJ5xl1QSU/enable`。
2. 在**安全（Security）** > **认证器（Authenticators）**下，确认 **Okta Verify** 认证器处于活跃状态，且其 `signed_nonce` 方法处于活跃状态。
3. 确认 Okta Dashboard 以及 Bot 登录的每个应用的身份验证策略允许 FastPass 或 Okta Verify 作为因素。包含 Okta Verify 的双因素保障是常见做法。
4. 保留**邮件（Email）**或**密码（Password）**作为可用因素。每台计算机上的首次 Okta Verify 登记需要用到它。

## 2. 添加 Team Setup Script

该设置脚本是 Grok Bot 计算机镜像的一部分。它安装固定版本的 Okta Verify 7.1.3.0，然后启动 Okta 服务、一个登录会话中间层，以及 `com-okta-authenticator` URI 处理器。当某次登录要求 FastPass 时，该处理器会在正在登录的 Bot 的桌面上打开 Okta Verify 窗口。脚本是幂等的，不包含任何内嵌证书或密钥。

1. 前往 [Cursor 控制台中的 Grok Bot](https://cursor.com/dashboard/bot)，在 **Bot 计算机（Bot Computers）**下找到 **Team Setup Scripts**。

2. 新建一个清单，或打开已有的清单，添加一条脚本条目，例如 ID 为 `okta-verify`。

3. 设置**设置脚本（Setup Script）**和**检查脚本（Check Script）**，两者都传入你的组织 URL：

   ```bash
   # Setup Script
   setup-okta.sh --org-url=https://yourorg.okta.com
   # Check Script
   setup-okta.sh --check --org-url=https://yourorg.okta.com
   ```

4. 选择**保存（Save）**。

该条目写的是命令名而不是路径，因此它可以从任何工作目录运行。计算机在每次启动时和定期刷新时运行它。它启动的服务不会在重启后存活，所以当这些服务停止时，检查脚本会重新运行设置。设置失败会被上报，且绝不会阻塞计算机。见 [Team Setup 如何运行你的脚本](https://docs.x.ai/grok-bot/private-networks#how-team-setup-runs-your-scripts)。

### Okta Verify 设置

脚本把你传入的设置写入 Okta Verify 的管理设置文件 `/etc/okta/adminconfig.json`。请在检查脚本那一行传入相同的选项，以便检查确认它们已生效。常见选项有：

| 选项 | 值 | 作用 |
| --- | --- | --- |
| `--org-url` | `https://yourorg.okta.com` | 在登录 URL 屏幕上预填你的组织。它不会改变安装包的下载来源。 |
| `--enrollment-options` | `Default`、`Enabled`、`SilentEnrollmentDisabled`、`Disabled` | 控制账号如何登记。 |
| `--user-verification-enrollment` | `Disabled`、`Deferred`、`Preferred`、`Required` | 控制登记时的口令设置。`Disabled` 会跳过它，因此如果你的组织要求用户验证，登录会失败。 |
| `--auto-registration` | `DEVICE` | 开启无用户设备注册。 |

完整列表见[设置脚本参考](#setup-script-reference)。

## 3. 登记 Okta Verify

每台计算机登记一次。登记信息保存在计算机的主目录中，重启后仍然有效。

1. 在你的桌面上打开 Okta Verify 窗口。在计算机上的终端中运行 `setup-okta.sh --display :N`，其中 `:N` 是你桌面的显示器（即 `$DISPLAY` 的值）。
2. 选择**开始使用（Get started）**，然后选择**下一步（Next）**。
3. 输入 `https://yourorg.okta.com`，选择**下一步**。
4. 在浏览器中用你的策略允许的方式登录，例如密码加邮件。
5. 创建一个 Okta Verify 口令。请私下保存，绝不要提交它或粘贴到聊天中。
6. 当 Okta Verify 显示**已添加账号（Account added）**且口令确认开启时，完成。

## 4. 验证 FastPass

1. 在计算机上打开一个新的浏览器会话，访问 `https://yourorg.okta.com`。
2. 输入用户名，选择**使用 Okta FastPass（Use Okta FastPass）**。
3. 当 Okta Verify 索要口令时，在大约 30 秒内输入。手动输入，或用右键 > **粘贴（Paste）**。按 Ctrl+V 会让 Linux 版应用崩溃。
4. 在管理控制台中打开**报告（Reports）** > **系统日志（System Log）**，确认两个事件：
   * `user.authentication.auth_via_mfa`，结果为 **SUCCESS**，因素为 **SIGNED\_NONCE**
   * `user.session.start`，针对 Okta Dashboard 的结果为 **SUCCESS**

## 设置脚本参考

该脚本位于每台 Grok Bot 计算机的 `/usr/local/bin/setup-okta.sh`。在计算机上运行 `setup-okta.sh --help` 可打印它支持的所有选项和 Okta Verify 设置及其可接受的值。

## 限制

* Okta Verify 按计算机用户各运行一个窗口。当窗口在某个 Bot 的桌面上打开时，同一台计算机上另一个 Bot 桌面发起的 FastPass 登录会在这个窗口中显示提示。窗口在 5 分钟无登录后关闭。
* Okta 不会从 Grok Bot 计算机收到设备制造商或型号。没有这些信息 FastPass 也能工作。
* 在口令提示中按 Ctrl+V 会让 Linux 上的 Okta Verify 崩溃。请改用右键 > **粘贴**。
