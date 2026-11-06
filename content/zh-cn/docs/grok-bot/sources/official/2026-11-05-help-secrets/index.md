---
title: "帮助：安全保存秘密"
linkTitle: "帮助：保存密钥"
date: 2026-11-05
originalTitle: "Store secrets securely"
sourceUrl: "https://cursor.com/help/grok-bot/secrets"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 隐私, 连接器]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Vault 保存登录、卡和联系信息，让 Bot 能登录、结账而不看到密码、卡号和安全码；它能看到联系信息和保存了哪些登录。Vault 适用于整个账号，保存的内容对所有 Bot 可用，不能限定给某个 Bot，也不支持共享 Bot。新建账号时若让 Bot 自己选密码，由 Vault 生成并保存，Bot 看不到。文中明确：保存卡片后没有设置能要求每次使用都批准，想逐次批准就不要保存卡；API 密钥等通过遮蔽的安全秘密卡输入，不写入聊天；共享 Bot 的秘密仅显示名称与说明，对其所有队友的聊天都生效。保存的值只写不读，Recover、Reset 和计算机更新会清除安装的应用和包，写进文件里的秘密可能随之消失，但用安全卡、Secrets 或 Vault 保存的不受影响。

**保留理由**：清楚给出凭证、卡和 API 密钥的处理方式及限制，尤其是保存卡后不再逐次批准这一点，对研究凭证处理很重要。

---

让密码、卡、API 密钥和其他凭证远离聊天和普通文件。将登录信息、卡和联系信息保存在 **Vault** 中，让你的 Bot 可以为你登录和结账。对于 API 密钥，请使用安全秘密卡（secure secret card）。保存秘密后，Grok Bot 不会再次显示该值。之后字段为空并不能证明秘密已被删除。

## 什么是 Vault？

Vault 保存你的登录信息、卡和联系信息，让你的 Bot 可以登录网站并为你结账，而不会看到秘密值。在桌面和手机上，可在 **设置（Settings）** > **Vault** 中找到它。你可以在那里添加、编辑或移除任何内容。Vault 需要 Grok Bot 0.75.2 或更高版本。

- **登录（Logins）**：一个网站、一个用户名或电子邮件，以及一个密码。你的 Bot 使用已保存的登录信息在该网站登录。
- **卡（Cards）**：卡号、有效期、安全码、持卡人姓名和账单地址。
- **联系信息（Contact info）**：用于配送和账单的姓名、地址、电话号码和电子邮件。

你的 Bot 永远不会看到已保存的密码、卡号或安全码。它可以看到你的联系信息以及你保存了哪些登录信息，因此它可以挑选正确的条目，并为你键入联系信息详情。

Vault 覆盖你的整个账号。你保存的所有内容都可供你账号上的每个 Bot 使用，你无法将某个项目限制为仅一个 Bot 使用。

Vault 不支持[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)。对于共享 Bot，请改为在**秘密（Secrets）**下添加密钥。请参阅[我应该如何添加 API 密钥或秘密？](#how-should-i-add-an-api-key-or-secret)

## 如何添加登录、卡或联系信息？

1. 打开 **设置（Settings）** > **Vault**，选择**新建项目（New item）**。
2. 选择**登录（Login）**、**卡（Card）**或**联系信息（Contact info）**。
3. 填写详细信息并保存。
   - 对于登录，输入**网站（Website）**、**用户名或电子邮件（Username or email）**和**密码（Password）**，然后选择**保存登录（Save login）**。
   - 对于卡，选择**用相机扫描（Scan with camera）**或**上传照片（Upload a photo）**从卡上填充，或手动输入。然后选择**保存卡（Save card）**。
   - 对于联系信息，输入姓名、地址、电话和电子邮件，然后选择**保存联系信息（Save contact info）**。

在**提示（Hints）**下，告诉你的 Bot 何时使用某个条目，例如「用于工作采购」。Bot 在多个条目之间选择时会遵循该提示。

你也可以从聊天中保存：

- 当你的 Bot 通过**安全表单（Secure Form）**请求登录信息、卡或地址时，勾选**安全保存到 Bot 的保管库（Securely save to Bot's vault）**，以便下次使用。如果不勾选，该值只在该次聊天中保留，并会自动过期。
- 当你附上一张卡的照片时，Grok Bot 会提供**保存到 Vault（Save to Vault）**，以便你的 Bot 以后可以用它付款。

## 如何从另一个密码管理器导入登录信息？

在桌面上，你可以从 CSV 导出文件导入登录信息。

1. 从 1Password、Chrome 或 Edge、Safari 或 Apple Passwords、Firefox、Bitwarden 或 LastPass 将密码导出为 CSV 文件。
2. 在 **设置** > **Vault** 中，选择**新建项目**，然后选择**从 CSV 导入…（Import from CSV…）**。
3. 选择**选择 CSV 文件（Choose CSV file）**并选取导出文件。该文件在你的计算机上读取，绝不会上传。它必须小于 5 MB。
4. 查看列表。已在你的 Vault 中的项目会被跳过。包含错误的行（例如缺少密码或网站不是 https）不会被导入。
5. 选择导入按钮，按钮上会显示有多少项目已就绪。

LastPass 的导出还会带上卡。导出的 CSV 以未加密形式保存你的密码，因此导入完成后请删除它。

## 我的 Bot 如何使用 Vault？

- **登录**：你的 Bot 首先使用已保存的登录信息，然后使用已连接的密码管理器，例如 [1Password](https://cursor.com/help/grok-bot/connect-apps#how-do-i-connect-1password)。如果两者都没有该登录信息，它会通过安全表单询问你。
- **新账号**：如果你让 Bot 在注册网站时选择密码，Vault 会生成密码并保存登录信息。你的 Bot 永远不会看到它。
- **结账**：已保存的卡会在结账时填入，联系信息会填入配送和账单详情。请参阅[我的 Bot 在使用已保存的卡之前会询问吗？](#will-my-bot-ask-before-it-uses-a-saved-card)
- **你在聊天中分享的详情**：当你给 Bot 提供姓名、地址、电话号码或电子邮件时，它会在任务完成后将其保存为联系信息，并告诉你它保存了什么。如果你不希望保留某些内容，请告诉它。

你的 Bot 可以在你要求时更改联系信息，以及条目的昵称和提示。密码、用户名、网站、卡号和安全码只能在**设置** > **Vault** 中更改。登录信息和卡也只能在那里移除。

## 我的 Bot 在使用已保存的卡之前会询问吗？

不一定。将卡保存在 Vault 中会让你的 Bot 在结账时填入它，并且没有设置要求每次使用已保存的卡都获得你的批准。

如果你想自己批准每一笔付款，请不要保存该卡：

- 当你的 Bot 在结账时通过安全表单请求卡信息时，不要勾选**安全保存到 Bot 的保管库**。该卡只会在那次聊天中使用。没有该复选框的表单会直接保存到 Vault，因此不要提交它。
- 如果你已经保存了卡，请打开**设置** > **Vault**，选择它，然后选择**移除（Remove）**。之后，Grok Bot 将无法再用它付款。

## 如何更改或删除 Vault 项目？

打开**设置** > **Vault** 并选择该项目进行编辑，或选择**移除**将其删除。移除登录信息后，Grok Bot 将无法再用它登录该网站。移除卡后，Grok Bot 将无法再用它付款。

要更改卡号，请移除该卡并重新添加。在手机上，已保存的卡目前无法编辑。

## 为什么我的 iPhone 上新建登录没有保存按钮？

在 iOS 26 或更高版本上的 Grok Bot for iPhone 1.18.0 中，**设置** > **Vault** > **新建项目** > **登录**只显示一个返回按钮，因此在那里键入的登录信息无法保存。卡和联系信息不受影响。此问题已在 iPhone 1.19.0 中修复，该版本正在 App Store 上逐步推出。当 App Store 向你提供更新时请更新，或打开 App Store 自行更新 Grok Bot。

在 1.19.0 上，**保存（Save）**位于表单顶部，并在你填写**名称（Name）**、**网站（Website）**和**密码（Password）**之前保持关闭。在更新之前，请从你计算机上的 Grok Bot 添加登录信息，或让你的 Bot 登录该网站，并从它在聊天中显示的安全表单保存登录信息。

## 我应该如何添加 API 密钥或秘密？

对于不是登录信息或卡的 API 密钥或其他秘密，请在 Bot 请求时使用**安全秘密卡（secure secret card）**。该字段会被遮蔽。选择**安全保存（Save securely）**。随后卡片会显示**已保存（Saved）**和**已安全保存并保持私密（Saved securely and kept private）**。该值不会写入聊天。

在你拥有或管理的[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)上，你也可以从 Bot 的详情中添加秘密。打开**秘密（Secrets）**，选择**添加秘密（Add secret）**，输入环境变量名称、简短说明和值，然后选择**保存秘密（Save secret）**。说明对 Bot 可见。值不可见。

不要将秘密粘贴到聊天、Shell 或普通文件中。使用**教导任务（Teach a task）**时，不要将其键入演示中。

你保存的秘密属于你。在你拥有或管理的共享 Bot 上，秘密会在每位队友的聊天中使用，因此只添加你愿意让每个能与该 Bot 聊天的人使用的密钥。你公司的安装脚本所需的凭证（例如每台团队计算机上安装的某个工具的许可证密钥）由团队管理员作为[团队秘密（Team Secret）](https://cursor.com/docs/grok-bot/teams#team-secrets)存储在 Enterprise 仪表板上。那些凭证绝不会直接到达你的 Bot。

## 为什么我看不到秘密的值？

这是预期行为。保存的值是只写的。

- 在**设置** > **Vault** 中，已保存的密码保持隐藏，卡只显示最后四位数字。
- 安全秘密卡在**已保存**后不会显示该值。页脚显示**已安全存储，绝不会向你的 Bot 显示（Stored securely, never shown to your Bot）**。
- 在共享 Bot 上，**秘密**只列出名称和说明。它绝不会再次显示该值，包括在 Shell 中。
- 要在那里更改值，请选择**替换（Replace）**，粘贴新值，然后选择**替换值（Replace value）**。你无法读回旧值。

如果某个页面请求了该秘密，已填入的卡片会显示**已填入页面。秘密值从未向你的 Bot 显示（Filled into the page. Secret values were never shown to your Bot.）**。如果显示**无法填入页面（Could not fill into the page）**，该页面可能已经移动。该值仍然没有向 Bot 显示。如果 Bot 再次询问，请提交一张新卡。

如果保存失败，表单会显示**秘密未保存。请重试。（The secret was not saved. Try again.）** 如果共享 Bot 的**秘密**列表显示**出错了。请重试。（Something went wrong. Try again.）**，请选择**重试（Try Again）**。**尚无秘密（No secrets yet）**表示该 Bot 没有已保存的名称，而不是值被隐藏在卡片上。

## 更新是否删除了我的秘密？

**恢复（Recover）**、**重置（Reset）**和计算机更新会移除已安装的应用和包。你键入到计算机上某个文件、shell 配置文件或已安装工具中的秘密可能会随之消失。这与通过安全卡、在**秘密**下或在 **Vault** 中保存的秘密是分开的。

Shell 不打印某个秘密并不意味着它已被清除。在共享 Bot 上，如果名称仍列在**秘密**下，则该值仍然存储着。关于更新、恢复和重置会保留什么，请参阅 [Grok Bot 计算机](https://cursor.com/help/grok-bot/computer-recovery)。

如果共享 Bot 的秘密名称消失了，而你没有选择**移除**：

1. 完全退出 Grok Bot 并重新打开它。在 Mac 上，请从菜单栏选择**退出（Quit）**，而不仅仅是关闭窗口。
2. 在登录同一 Cursor 账号的另一台设备上打开同一个 Bot。
3. 如果列表显示**出错了。请重试。**，请在添加任何内容之前选择**重试**。

如果该名称在所有设备上仍然缺失，请重新添加它。不要为了在计算机上「保留副本」而将其放入文件。如果你没有移除名称但它们持续消失，请[联系支持](https://cursor.com/help/grok-bot/get-help)。请附上你的账号电子邮件和**秘密**的截图。不要发送秘密值。
