---
title: "文档（docs.x.ai）：Vault 与安全登录"
linkTitle: "docs.x.ai：Vault 与安全登录"
date: 2026-10-28
originalTitle: "Vault and secure sign-in"
sourceUrl: "https://docs.x.ai/grok-bot/vault"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「Secrets」讲到的密钥管理与这页约一半重合，这页另讲 Vault 的登录、卡和付款。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Vault 存放登录信息、银行卡和联系信息，Bot 看不到密码、卡号和安全码，只能看到联系信息和登录条目的列表；Vault 全账号共享，不能只给某个 Bot。可以从 1Password、Chrome、Safari、Bitwarden 等导出的 CSV 导入，文件只在本机读取。存在 Vault 里的卡会在结账时自动填入，没有「每次批准」的设置；想逐笔批准就不要存卡。也可以连接 Link 或 X Money 作为付款账户，Link 付款会弹出一次性卡，显示商家、商品和总额，由用户选择付款、换方式或拒绝。

**保留理由**：官方对凭证与付款隔离的具体设计：模型看不到密码和卡号，但存卡后付款不再逐笔确认，这一点值得留意。

---

Vault 与安全登录

把密码、卡、API 密钥和其他凭据留在聊天和普通文件之外。将登录信息、卡和联系信息保存在 **Vault** 中，以便你的 Bot 能替你登录和结账，并使用安全秘密卡片（secure secret card）存放 API 密钥。保存秘密后，Grok Bot 不会再次显示该值；之后字段为空并不证明秘密已被删除。

## Vault 保存什么

Vault 保存你的登录信息、卡和联系信息，以便你的 Bot 能登录网站并替你结账，而看不到秘密值。从桌面应用或手机上的**设置 → Vault（Settings → Vault）**打开它，在那里你可以添加、编辑或移除任何内容。Vault 需要 Grok Bot 0.75.2 或更高版本。

* **登录信息（Logins）：** 网站、用户名或电子邮件，以及密码。Bot 使用保存的登录信息在该网站登录。
* **卡（Cards）：** 卡号、有效期、安全码、持卡人姓名和账单地址。
* **联系信息（Contact info）：** 用于配送和账单的姓名、地址、电话号码和电子邮件。

Bot 永远看不到保存的密码、卡号或安全码。它可以看到你的联系信息以及你保存了哪些登录信息，因此它能选择正确的条目并替你输入联系详情。

Vault 覆盖你的整个账号：你保存的所有内容对你账号上的每个 Bot 可用，你无法将某个条目的使用限制在一个 Bot。Vault 不支持[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)；请改为在**秘密（Secrets）**下为共享 Bot 添加密钥。参见 [API 密钥和其他秘密](#api-keys-and-other-secrets)。

## 添加、导入和更改条目

1. 打开**设置 → Vault**并选择**新条目（New item）**。
2. 选择**登录信息（Login）**、**卡（Card）**或**联系信息（Contact info）**。
3. 填写详情并保存。
   * 对于登录信息，输入**网站（Website）**、**用户名或电子邮件（Username or email）**和**密码（Password）**，然后选择**保存登录信息（Save login）**。
   * 对于卡，选择**用相机扫描（Scan with camera）**或**上传照片（Upload a photo）**从卡中填入，或直接输入。然后选择**保存卡（Save card）**。
   * 对于联系信息，输入姓名、地址、电话和电子邮件，然后选择**保存联系信息（Save contact info）**。

在**提示（Hints）**下，告诉你的 Bot 何时使用某个条目，例如「用于工作采购」。Bot 在条目之间选择时会遵循该提示。

你也可以从聊天中保存。当 Bot 通过[安全表单](#secure-forms)请求登录信息、卡或地址时，勾选**安全保存到 Bot 的 Vault（Securely save to Bot's vault）**以便下次保留；如果不勾选，该值仅在那次聊天中保留，并会自行过期。当你附加卡的照片时，Grok Bot 会提供**保存到 Vault（Save to Vault）**，以便你的 Bot 以后用它付款。

要从桌面上的另一个密码管理器移动登录信息：

1. 从 1Password、Chrome 或 Edge、Safari 或 Apple Passwords、Firefox、Bitwarden 或 LastPass 将密码导出为 CSV 文件。
2. 在**设置 → Vault**中，选择**新条目**，然后选择**从 CSV 导入…（Import from CSV…）**。
3. 选择**选择 CSV 文件（Choose CSV file）**并选取导出文件。该文件在你的电脑上读取，从不上传，且必须小于 5 MB。
4. 审查列表。已在你 Vault 中的条目会被跳过。有错误的行（例如缺少密码或网站不是 https）不会被导入。
5. 选择导入按钮，它会显示有多少条目已就绪。

LastPass 导出也会带上卡。导出文件包含未加密的密码，因此导入完成后请删除它。

要更改或删除条目，请在**设置 → Vault**中选择它并编辑，或选择**移除（Remove）**。移除登录信息后，Grok Bot 无法再用它登录该网站；移除卡后，Grok Bot 无法再用它付款。要更改卡号，请移除卡并重新添加。在手机上，保存的卡暂时无法编辑。

当你要求时，Bot 可以更改联系信息，以及条目的昵称和提示。密码、用户名、网站、卡号和安全码只能在**设置 → Vault**中更改，登录信息和卡也只能在那里移除。

## Bot 如何使用 Vault

登录时，Bot 会先使用保存在 Vault 中的登录信息，然后使用已连接的密码管理器（例如 [1Password](https://docs.x.ai/grok-bot/computer-and-apps#connect-1password)），最后用安全表单询问你。来自 Vault 和安全表单的值会被填入页面，Bot 看不到它们。当网站通过电子邮件发送一次性验证码时，Bot 可以从已连接的 Gmail 或 Outlook 账户或从[它自己的收件箱](https://docs.x.ai/grok-bot/computer-and-apps#give-your-bots-an-email-address)读取。

* **新账号：** 如果你让 Bot 在注册网站时选择密码，Vault 会生成密码并保存登录信息，而 Bot 永远看不到它。
* **结账：** 保存的卡会在结账时填入，联系信息会填入配送和账单详情。参见[支付](#pay-for-things)。
* **你在聊天中分享的详情：** 当你给 Bot 姓名、地址、电话号码或电子邮件时，它会在任务完成后将其保存为联系信息，并告诉你它保存了什么。如果你不想保留某些内容，请告诉它。

当表单无法完成该步骤时，Bot 会把电脑交给你，例如单点登录、通行密钥、它无法通过的 CAPTCHA（验证码）、在另一台设备上批准、二维码或银行卡验证。在请求上选择**接管（Take over）**，或打开电脑并选择**取得控制权（Take control）**，只完成该步骤，然后选择**我完成了（I'm done）**并告诉 Bot 继续。已登录的会话会留在电脑上供未来任务使用，并在你的 Bot 之间共享。

## 安全表单

当页面需要只有你才能提供的内容时，Bot 会在聊天中显示**安全表单（Secure Form）**，每个步骤一个表单。表单会说明它填入的网站，例如「永不向你的 Bot 显示。直接填入 example.com。」你的答案会直接进入页面，永远不会显示给 Bot。

如果登录信息、卡或联系信息的表单有**安全保存到 Bot 的 Vault**，勾选它以将值保留在 Vault 中。不勾选则仅将该值用于那次聊天。没有该复选框的表单会直接保存到 Vault。

已填写的表单会显示**已填入页面。秘密值从未向你的 Bot 显示（Filled into the page. Secret values were never shown to your Bot.）**。如果它显示**无法填入页面（Could not fill into the page）**，页面可能在表单填入之前已移动；这些值仍然没有向 Bot 显示。如果 Bot 再次请求，请提交新表单。

## API 密钥和其他秘密

对于 API 密钥或其他不是登录信息或卡的秘密，当 Bot 请求时使用**安全秘密卡片**。该字段会被遮蔽。选择**安全保存（Save securely）**，卡片随后会显示**已保存（Saved）**和**已安全保存并保持私密（Saved securely and kept private）**。该值不会写入聊天，也不会显示给 Bot。

在你拥有或管理的[共享 Bot](https://docs.x.ai/grok-bot/shared-bots)上，你也可以从 Bot 的详细信息中添加秘密。打开**秘密（Secrets）**，选择**添加秘密（Add secret）**，输入环境变量名称、简短描述和值，然后选择**保存秘密（Save secret）**。描述对 Bot 可见；值不可见。共享 Bot 上的秘密会在每个队友的聊天中使用，因此只添加你乐意让每个能与该 Bot 聊天的人使用的密钥。

你公司设置脚本需要的凭据（例如安装在每台团队电脑上的工具的许可证密钥）由团队管理员作为[团队秘密（Team Secret）](https://docs.x.ai/grok-bot/teams-and-enterprises#team-secrets)存储在 Enterprise 仪表板上。这些永远不会直接到达你的 Bot。

绝不要把密码、一次性验证码或 API 密钥粘贴到普通聊天、Shell 命令或电脑上的文件中，也不要在使用[教授任务](https://docs.x.ai/grok-bot/skills-routines-and-automations#teach-a-workflow-by-demonstration)时在演示中输入秘密。

### 为什么你看不到已保存的值

已保存的值是只写的：

* 在**设置 → Vault**中，保存的密码保持隐藏，卡只显示后四位。
* 安全秘密卡片在**已保存**后不会显示值。页脚显示**已安全存储，永不向你的 Bot 显示（Stored securely, never shown to your Bot）**。
* 在共享 Bot 上，**秘密**只列出名称和描述。它永远不会再次显示值，包括在 Shell 中。
* 要在那里更改值，选择**替换（Replace）**，粘贴新值，然后选择**替换值（Replace value）**。你无法读回旧值。

如果保存失败，表单会显示**秘密未保存。请重试。（The secret was not saved. Try again.）**。如果共享 Bot 的**秘密**列表显示**出了问题。请重试。（Something went wrong. Try again.）**，请选择**重试（Try Again）**。**还没有秘密（No secrets yet）**表示该 Bot 没有保存的名称，而不是某个值被隐藏了。

### 更新会删除我的秘密吗？

**恢复（Recover）**、**重置（Reset）**和电脑更新会移除已安装的应用和包，因此你输入到电脑上的文件、shell 配置文件或已安装工具中的秘密可能会随之消失。这与你用安全密钥卡保存在**秘密**下或 Vault 中的秘密是分开的。参见[更新、恢复或重置电脑](https://docs.x.ai/grok-bot/computer-and-apps#update-recover-or-reset-the-computer)。

Shell 没有打印秘密并不意味着它已被清除。在共享 Bot 上，如果名称仍列在**秘密**下，值仍然存储着。如果共享 Bot 的秘密名称消失了，而你没有选择**移除**：

1. 完全退出 Grok Bot 并重新打开。在 Mac 上，从菜单栏选择**退出（Quit）**，而不只是关闭窗口。
2. 在另一台登录同一 Cursor 账号的设备上打开同一个 Bot。
3. 如果列表显示**出了问题。请重试。**，在添加任何内容之前选择**重试**。

如果名称在每台设备上仍然缺失，请重新添加它；不要把它放进文件以在电脑上保留副本。如果名称持续消失，请带上你的账号电子邮件和**秘密**的截图[联系支持](https://docs.x.ai/grok-bot/troubleshooting)，但绝不要提供秘密值。

## 支付

保存在 Vault 中的卡会在结账时填入，而无需每次询问你，也没有任何设置要求每次使用都经你批准。如果你想自己批准每笔付款，就不要保存卡：

* 当 Bot 在结账时通过安全表单请求卡时，不要勾选**安全保存到 Bot 的 Vault**。该卡仅在那次聊天中使用。没有该复选框的表单会直接保存到 Vault，因此不要提交它。
* 如果你已经保存了卡，请打开**设置 → Vault**，选择它，然后选择**移除**。

**设置 → Vault**还会列出**支付账户（Payment accounts）**（你可以连接的钱包，例如 Link 或 X Money）和**默认支付方式（Default payment method）**（Grok Bot 最先用它付款）。

连接 Link 账户后，Bot 可以请求你为单次购买批准一张一次性卡。请求会显示商家、商品和总额。选择显示金额的**支付（Pay）**按钮以批准；选择**换一种方式支付（Pay another way）**跳过该卡，或选择**拒绝（Deny）**。批准后，在打开的 Link 页面上完成授权。如果你拒绝或请求过期，不会收取任何费用。如果卡片显示你的 Link 账户未连接，请重新连接 Link，然后再次询问 Bot。
