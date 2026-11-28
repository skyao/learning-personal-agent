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
translation: 待翻译
collectedAt: 2026-11-28
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-11）"
tags: [运行环境, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的文档现以 docs.x.ai（SpaceXSI Docs）为准，cursor.com 的文档地址已 308 跳转到这里。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：面向登录策略要求 Okta FastPass 的 Okta 管理员，说明如何让 Bot 在其电脑的浏览器里登录受 Okta 保护的应用。Okta Verify 通过仅限 Enterprise 的 Team Setup Scripts 安装，使用固定的 Okta Verify 7.1.3.0 版本。步骤依次为：在 Okta 中启用 Okta Verify for Linux 功能并确认 signed_nonce 方法可用；在 Cursor 控制台添加 Team Setup Script，参数带上组织地址；在每台电脑上登记一次 Okta Verify；用系统日志中的 auth_via_mfa 与 user.session.start 事件验证。若团队限制出站流量，须放行 anysphere.okta.com 和自己的 Okta 组织。限制包括：每个电脑用户一个窗口，窗口在 5 分钟无登录后关闭，并且粘贴口令须用右键菜单，Ctrl+V 会使 Linux 版崩溃。

**保留理由**：补充 Bot 电脑在企业身份体系（Okta）下如何登录的具体步骤与限制，已收的 docs-identity 只涉及概述。
