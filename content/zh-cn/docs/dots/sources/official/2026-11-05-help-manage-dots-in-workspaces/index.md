---
title: "在 ChatGPT 工作区中管理 dots"
linkTitle: "帮助：工作区管理"
date: 2026-11-05
originalTitle: "Manage dots in ChatGPT workspaces"
sourceUrl: "https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces"
reprintUrl: "https://web.archive.org/web/20261027000449/https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces"
publisher: "OpenAI 帮助中心"
language: en
fidelity: 转载全文翻译
translation: 已翻译
collectedAt: 2026-11-05
updatedAt: 2026-10-21
dateNote: "help.openai.com 对自动访问返回 403，依据 Internet Archive 2026-10-27 00:04:49（UTC）的快照；快照中页面显示「Updated: 6 days ago」，据此推算更新日期约为 2026-10-21。发布日期未知，暂取收集日期"
tags: [安全, 开放与价格, 运行环境]
products: [dots]
---

{{< source-info >}}

（收集说明：帮助中心文章会持续更新，本页对应上述快照时的版本。原文一级标题在此降为二级，二级降为三级。设置项名称保留英文原文，以便与界面对照。）

了解如何在你的 Enterprise 工作区中管理 dots 的访问权限、计算机能力、已连接的应用和消息功能。

## 概览

### 工作区所有者可以控制什么？

工作区所有者可以控制谁能使用 dots，以及他们可以使用哪些能力。这些设置适用于 dots 测试期间符合条件的 ChatGPT Enterprise 工作区。

## 访问与权限

### 如何为成员启用 dots？

为工作区设置权限，或使用自定义角色为特定成员或群组提供不同的访问权限。

1. 打开 **Workspace settings > Permissions & roles**（工作区设置 > 权限与角色）。
2. 进入 **Permissions > Workspace default > Workspace capabilities**（权限 > 工作区默认 > 工作区能力）。
3. 找到 **Use dots (Beta)**（使用 dots（测试版）），然后查看下文的 dots 权限和计算机能力。
4. 保存设置。检查适用于你想启用的成员的所有自定义角色。

Enterprise 的 dots 访问默认关闭。下文的其他 dots 权限只在成员拥有 dots 访问权限时才生效。

### dots 权限控制什么？

| **设置** | **控制内容** |
| --- | --- |
| **Use dots (Beta)**（使用 dots（测试版）） | 允许成员使用 dots。Enterprise 默认关闭。 |
| **Add dots to Slack and Microsoft Teams**（将 dots 添加到 Slack 和 Microsoft Teams） | 在可用的情况下，允许 dot 加入受支持的 Slack 或 Microsoft Teams 工作区，并以自己的身份发帖。启用权限后，成员须自行完成设置。 |
| **Allow local computer access**（允许本地计算机访问） | 允许 dot 使用成员的本地文件，并在其计算机上运行命令。成员还必须连接自己的计算机、保持其在线，并保持 ChatGPT 应用打开。Enterprise 默认关闭。 |
| **Use custom rules for dots**（为 dots 使用自定义规则） | 允许成员添加或编辑规则，以引导其 dot 的操作和确认。Enterprise 默认关闭。 |

如果工作区设有针对特定操作系统的 Codex 或 ChatGPT Work 策略，则本地计算机访问不可用。在相关云端能力已启用时，dots 仍可以在其云端计算机上工作。

自定义规则不可用时，默认的操作规则仍然适用。自定义规则不能凌驾于内置防护措施之上，禁用自定义规则也不会让每项操作都需要批准。

## 云端计算机与密码管理器

### 云端计算机设置控制什么？

在 **Workspace capabilities**（工作区能力）下，可以在 **Cloud computer capabilities**（云端计算机能力）中找到三项云端控制。**Use password manager**（使用密码管理器）作为一项单独的控制出现。

| **设置** | **控制内容** |
| --- | --- |
| **Cloud browser use**（云端浏览器使用） | 允许 dots 和 Work Cloud 任务使用浏览器打开网站并与之交互。 |
| **Cloud network access**（云端网络访问） | 允许 dots 和 Work Cloud 任务在云端计算机上运行的代码和 shell 命令访问互联网。 |
| **Cloud computer use**（云端计算机使用） | 允许 dots 和 Work Cloud 任务与云端计算机上的桌面和应用程序交互。 |
| **Use password manager**（使用密码管理器） | 允许成员在 dots 和 Work Cloud 中使用密码管理器。此设置独立于 Cloud browser use。 |

这些控制同时适用于 dots 和 Work Cloud 中的任务。即使 Work 或 Work Cloud 被禁用，它们也适用于 dots。已有的工作区默认设置和自定义角色中关于浏览器和网络访问的设置会沿用。

dot 的云端计算机不会自动继承成员本地的 VPN、浏览器登录状态或设备策略。访问某个网站还可能需要成员在云端计算机上登录。

## 已连接的应用

### 应用访问和批准如何运作？

启用 dots 并不会授予对所有应用或网站的访问权限。成员已在 ChatGPT 中使用的受支持应用连接，可能可供其 dot 使用。

- 插件控制决定哪些应用可用，以及它们可以执行哪些操作。
- 应用权限决定某项应用操作何时需要批准。
- 每项已连接服务自身的授权，也会限制 dot 可以访问或执行的内容。

请将这些设置与 dots 访问分开检查。设置详情请参阅[管理应用能力](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors#step-2-manage-capabilities)。

## 消息

### 如何允许在 Slack 和 Microsoft Teams 中使用 dots？

**Add dots to Slack and Microsoft Teams** 权限允许成员在可用的情况下，把自己的 dot 连接到受支持的沟通渠道。开启它并不会安装 Slack 应用，也不会连接成员的 dot。

对于 Slack，必须为该成员同时启用 **Use dots (Beta)** 和 **Add dots to Slack and Microsoft Teams**。如果 Slack 工作区要求应用审批，则须由 Slack 工作区所有者或应用管理员批准安装及相关权限。之后由每位成员完成其 dot 的 Slack 设置。

只有 dot 的所有者可以指挥它。其他人的私信或提及不会让那个 dot 开始工作。当 dot 在频道中发帖时，其他频道成员可以看到它的消息。

在发布时，Enterprise 不支持通过 iMessage、RCS 或 WhatsApp 进行手机消息。

## 管理访问

### 如何移除某位成员的 dots 访问权限？

要移除某位成员的访问权限，请检查工作区默认设置中的 **Use dots (Beta)**，以及直接分配给该成员或通过群组分配的所有角色，然后移除每一项适用的授权。只要有一个角色授予了访问权限，即使另一个角色关闭了该权限，该成员仍可能使用 dots。

应用授权和网站会话是单独管理的。如需帮助检查成员的角色和权限，请参阅[在 ChatGPT 中使用基于角色的访问控制管理功能访问](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt)。

### 工作区的模型设置适用于 dots 吗？

不适用。Enterprise 的模型控制和默认模型设置不适用于 dots。
