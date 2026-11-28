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
collectedAt: 2026-11-28
updatedAt: 2026-11-19
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：应用聊天中 Bot 能看到已存卡的号码和安全码；新增 Team Bot 自有登录、Shop Pay、一张订单卡批量最多 500 笔支付、iPhone 1.18.0 无法保存登录的问题"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签，以及文末的相关页面列表。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「Secrets」讲到的密钥管理与这页约一半重合，这页另讲 Vault 的登录、卡和付款。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Vault 存放登录信息、银行卡和联系信息，Bot 看不到已存的密码，能看到联系信息和有哪些登录条目；在 Grok Bot 应用的聊天中，Bot 还能看到已存卡的号码和安全码，在用户点订单卡上的 Pay 之后填入结账。Vault 全账号共享，不能只给某个 Bot，也不适用于 Team Bots；Team Bot 的所有者或管理者可在 Bot's accounts 下为它添加专属登录，只有管理者能看到和修改。可导入 1Password、Chrome 或 Edge、Safari 或 Apple Passwords、Firefox、Bitwarden、LastPass 导出的 CSV（须小于 5 MB，文件只在本机读取）。存在 Vault 里的卡会在结账时自动填入，没有「每次批准」的设置；想逐笔批准就不要存卡。也可连接 Link、X Money 或 Shop Pay 作为付款账户，一张订单卡可批量覆盖最多 500 笔卡支付；Link 付款会弹出一次性卡，显示商家、商品和总额，由用户选择付款、换方式或拒绝。

**保留理由**：官方对凭证与付款隔离的具体设计：模型看不到密码，但应用聊天中能看到卡号和安全码，存卡后付款不再逐笔确认，这几点值得留意。

---

Vault 与安全登录

把密码、银行卡、API 密钥和其他凭据挡在聊天和普通文件之外。把登录信息、银行卡和联系信息保存在 **Vault** 中，让你的 Bot 能替你登录和结账；API 密钥则用安全密钥卡。保存密钥后，Grok Bot 不会再显示它的值；之后看到字段为空，并不能证明密钥已被删除。

## Vault 里存什么

Vault 保存你的登录信息、银行卡和联系信息，让 Bot 能替你登录网站和结账，而看不到你的密码。在桌面应用或手机上从**设置 → Vault（Settings → Vault）**打开，你可以在那里添加、编辑或移除任何内容。Vault 需要 Grok Bot 0.75.2 或更高版本。

* **登录信息：** 一个网站、一个用户名或邮箱、一个密码。Bot 用已保存的登录信息在该网站登录。
* **银行卡：** 卡号、有效期、安全码、持卡人姓名和账单地址。
* **联系信息：** 用于配送和账单的姓名、地址、电话号码和邮箱。

Bot 永远看不到已保存的密码。它能看到你的联系信息以及你保存了哪些登录信息，因此能挑对条目并替你填写联系信息。

在 Grok Bot 应用的聊天中，Bot 还能看到已保存银行卡的卡号和安全码。你在订单卡上点**支付（Pay）**之后，它把这些填入结账表单；你询问时，它也会告诉你某张卡的详情。

Vault 覆盖你的整个账号：你保存的一切对你账号上的每个 Bot 都可用，你不能把某一项限定给某个 Bot。你的 Vault 不适用于 [Team Bots](https://docs.x.ai/grok-bot/team-bots)：Team Bot 不能使用你保存的登录信息、银行卡或联系信息。请改为在**密钥（Secrets）**下为 Team Bot 添加密钥。见 [API 密钥和其他密钥](#api-keys-and-other-secrets)。

Team Bot 可以有自己的登录信息。如果你是它的所有者或管理者，点击扳手图标、**管理（Manage）**，在**常规（General）**下找到 **Bot 的账号（Bot's accounts）**。选择**添加（Add）**，再选 **Bot 的 Vault 登录（Bot's vault login）**，输入**网站（Website）**、**用户名或邮箱（Username or email）**和**密码（Password）**，然后选择**保存登录（Save login）**。该 Bot 可以用这些登录信息为你团队中的任何人登录，只有管理者能查看或修改它们。要修改或移除某一条，打开它的**更多操作（More actions）**菜单，选择**编辑（Edit）**或**移除（Remove）**。Team Bot 的登录信息不会出现在你自己的**设置 → Vault**中。

## 添加、导入和修改条目

1. 打开**设置 → Vault**，选择**新建项目（New item）**。
2. 选择**登录（Login）**、**银行卡（Card）**或**联系信息（Contact info）**。
3. 填写详情并保存。
   * 登录信息需输入**网站**、**用户名或邮箱**和**密码**，然后选择**保存登录**。
   * 银行卡可选择**用相机扫描（Scan with camera）**或**上传照片（Upload a photo）**从卡片填写，也可以手动输入。然后选择**保存银行卡（Save card）**。
   * 联系信息需输入姓名、地址、电话和邮箱，然后选择**保存联系信息（Save contact info）**。

在 iOS 26 或更高版本的 Grok Bot for iPhone 1.18.0 上，**新建项目** > **登录**只显示一个返回按钮，因此在那里输入的登录信息无法保存。银行卡和联系信息不受影响。此问题已在 iPhone 1.19.0 中修复；请从 App Store 更新 Grok Bot。

在**提示（Hints）**下，告诉你的 Bot 何时使用某个条目，例如「用于工作采购」。Bot 在条目之间选择时会遵循该提示。

你也可以从聊天中保存。当 Bot 通过[安全表单](#secure-forms)索要登录信息、银行卡或地址时，勾选**安全保存到 Bot 的 Vault（Securely save to Bot's vault）**可留作下次使用；如果不勾选，该值只保留在那次聊天中，并会自行过期。当你附加一张银行卡照片时，Grok Bot 会提供**保存到 Vault（Save to Vault）**，以便你的 Bot 之后用它付款。

要在桌面端从其他密码管理器迁移登录信息：

1. 从 1Password、Chrome 或 Edge、Safari 或 Apple Passwords、Firefox、Bitwarden 或 LastPass 把密码导出为 CSV 文件。
2. 在**设置 → Vault**中，选择**新建项目**，然后选择**从 CSV 导入……（Import from CSV…）**。
3. 选择**选择 CSV 文件（Choose CSV file）**并挑出导出文件。文件在你的电脑上读取，从不上传，且必须小于 5 MB。
4. 检查列表。已在 Vault 中的条目会被跳过。出错的行（例如缺少密码或网站不是 https）不会被导入。
5. 选择导入按钮，按钮上显示有多少条已就绪。

LastPass 的导出文件也会带上银行卡。导出文件中的密码是未加密的，导入完成后请删除它。

要修改或删除某个条目，在**设置 → Vault**中选中它并编辑，或选择**移除**。移除登录信息后，Grok Bot 无法再用它登录该网站；移除银行卡后，Grok Bot 无法再用它付款。要更改卡号，请移除该卡并重新添加。在手机上，已保存的银行卡暂时无法编辑。

你提出要求时，Bot 可以更改联系信息，以及条目的昵称和提示。在 Grok Bot 应用的聊天中，当你给出新信息时，它还可以更改已保存银行卡的卡号、安全码、持卡人姓名、有效期和账单地址。密码、用户名和网站只能在**设置 → Vault**中更改，登录信息和银行卡也只能在那里移除。

## Bot 如何使用 Vault

登录时，Bot 先使用保存在 Vault 中的登录信息，然后是已连接的密码管理器（例如 [1Password](https://docs.x.ai/grok-bot/computer-and-apps#connect-1password)），最后通过安全表单问你。来自 Vault 的登录信息和安全表单中的值在填入时都不让 Bot 看到。当网站发送一次性验证码邮件时，Bot 可以从已连接的 [Gmail](https://x.ai/bot/plugin/45893410) 或 [Outlook](https://x.ai/bot/plugin/57302029) 账号，或从[它自己的收件箱](https://docs.x.ai/grok-bot/computer-and-apps#give-your-bots-an-email-address)读取。

* **新账号：** 如果你让 Bot 在为某个网站注册时选择密码，Vault 会生成密码并保存登录信息，Bot 始终看不到它。
* **结账：** 已保存的银行卡在结账时填入，联系信息填入配送和账单详情。见[付款](#pay-for-things)。
* **你在聊天中分享的详情：** 当你把姓名、地址、电话号码或邮箱给 Bot 时，它在任务完成后将其保存为联系信息，并告诉你保存了什么。如果你不希望保留某项，请告诉它。

当表单无法完成某一步时，Bot 会把电脑交给你，例如单点登录、通行密钥、它无法通过的验证码、需要在另一台设备上批准、二维码或银行卡验证。在请求上选择**接管（Take over）**，或打开电脑并选择**接管控制（Take control）**，只完成那一步，然后选择**我完成了（I'm done）**并让 Bot 继续。已登录的会话会留在电脑上供后续任务使用，并在你的各个 Bot 之间共享。

## 安全表单

当页面需要只有你才能提供的内容时，Bot 会在聊天中显示**安全表单（Secure Form）**，每一步一张。表单会说明它填入哪个网站，例如「从不向你的 Bot 显示。直接填入 example.com。（Never shown to your Bot. Filled directly to example.com.）」你的回答直接进入页面，从不向 Bot 显示。

如果登录信息、银行卡或联系信息的表单带有**安全保存到 Bot 的 Vault**，勾选它可把值保留在 Vault 中。不勾选则只在那次聊天中使用该值。没有该复选框的表单会直接保存到 Vault。

已填写的表单显示**已填入页面。密钥值从未向你的 Bot 显示。（Filled into the page. Secret values were never shown to your Bot.）** 如果显示**无法填入页面（Could not fill into the page）**，可能是页面在表单填入前已经跳转；这些值仍然没有向 Bot 显示。如果 Bot 再次询问，请提交一张新表单。

## API 密钥和其他密钥

对于不是登录信息或银行卡的 API 密钥或其他密钥，在 Bot 索要时使用**安全密钥卡**。字段是遮蔽的。选择**安全保存（Save securely）**，卡片随后显示**已保存（Saved）**和**已安全保存并保持私密（Saved securely and kept private）**。该值不会写入聊天，也不会向 Bot 显示。

在你拥有或管理的 [Team Bot](https://docs.x.ai/grok-bot/team-bots) 上，你也可以从 Bot 的详情中添加密钥。打开**密钥**，选择**添加密钥（Add secret）**，输入环境变量名、简短描述和值，然后选择**保存密钥（Save secret）**。描述对 Bot 可见，值不可见。Team Bot 上的密钥会用于每位队友的聊天，所以只添加你愿意让每个能与该 Bot 聊天的人使用的密钥。

你公司的设置脚本需要的凭据，例如安装在每台团队电脑上的某个工具的许可证密钥，由团队管理员改为在企业版控制台上存为 [Team Secret](https://docs.x.ai/grok-bot/teams-and-enterprises#team-secrets)。这些凭据从不直接到达你的 Bot。

绝不要把密码、一次性验证码或 API 密钥粘贴进普通聊天、Shell 命令或电脑上的文件，也不要在我用[示范教一个任务](https://docs.x.ai/grok-bot/skills-routines-and-automations#teach-a-workflow-by-demonstration)时把密钥输进演示里。

### 为什么看不到已保存的值

已保存的值只能写入：

* 在**设置 → Vault**中，已保存的密码始终隐藏，银行卡只显示后四位。
* 安全密钥卡在**已保存**之后不再显示该值。页脚显示**已安全存储，从不向你的 Bot 显示（Stored securely, never shown to your Bot）**。
* 在 Team Bot 上，**密钥**只列出名称和描述。它不再显示该值，在 Shell 中也是如此。
* 要在那里更改某个值，选择**替换（Replace）**，粘贴新值，再选择**替换值（Replace value）**。你无法读回旧值。

如果保存失败，表单显示**密钥未保存。请重试。（The secret was not saved. Try again.）** 如果 Team Bot 的**密钥**列表显示**出了点问题。请重试。（Something went wrong. Try again.）**，选择**重试（Try Again）**。**暂无密钥（No secrets yet）**表示该 Bot 没有已保存的名称，而不是某个值被隐藏了。

### 更新会不会删掉我的密钥？

**恢复（Recover）**、**重置（Reset）**和计算机更新会移除已安装的应用和软件包，所以你输入到电脑上的文件、shell 配置文件或已安装工具中的密钥可能随之消失。这与用安全密钥卡保存的、保存在**密钥**下的或 Vault 中的密钥是两回事。见[更新、恢复或重置计算机](https://docs.x.ai/grok-bot/computer-and-apps#update-recover-or-reset-the-computer)。

Shell 没有打印某个密钥，并不代表它已被清除。在 Team Bot 上，如果名称仍列在**密钥**下，说明值仍然保存着。如果 Team Bot 的密钥名称不见了，而你没有选择**移除**：

1. 完全退出 Grok Bot 再重新打开。在 Mac 上，从菜单栏选择**退出（Quit）**，而不只是关闭窗口。
2. 在另一台登录同一 Cursor 账号的设备上打开同一个 Bot。
3. 如果列表显示**出了点问题。请重试。**，在添加任何内容之前先选择**重试**。

如果每台设备上该名称都仍然缺失，请重新添加；不要把它写进文件以在电脑上留一份副本。如果名称持续消失，请带上你的账号邮箱和一张**密钥**的截图[联系支持](https://docs.x.ai/grok-bot/troubleshooting)，但绝不要带密钥值。

## 付款

保存在 Vault 中的银行卡在结账时自动填入，不会每次都问你，也没有任何设置要求每次使用都需你批准。如果你想自己批准每一笔付款，就不要保存银行卡：

* 当 Bot 在结账时通过安全表单索要银行卡，不要勾选**安全保存到 Bot 的 Vault**。该卡只在那次聊天中使用。没有该复选框的表单会直接保存到 Vault，所以不要提交它。
* 如果你已经保存了银行卡，打开**设置 → Vault**，选中它，选择**移除**。

**设置 → Vault**还会列出**付款账户（Payment accounts）**——你可以连接的钱包，例如 Link、X Money 或 Shop Pay——以及 **默认付款方式（Default payment method）**，即 Grok Bot 优先使用的方式。在手机上，已连接的钱包位于**设置 → Vault**中的**付款（Payments）**下：已连接的钱包显示**已连接（Connected）**及其登录的账号，未连接的显示**连接（Connect）**。

当 Bot 通过订单卡替你购物时，它用保存在 Vault 中的银行卡付款。如果你没有保存过卡，Bot 先通过安全表单索要一张。你没有在那里保存的卡不会生成订单卡；Bot 改为在聊天中请你批准确切的总额。

Bot 还可以为一批最多 500 笔银行卡付款发送一张订单卡，用已保存的银行卡支付。付款不超过 10 笔时卡片逐笔列出，超过时在列表上方显示一行汇总。你用**支付**按钮批准后，Bot 逐笔付款，遇到银行卡被拒就停止。随后它告诉你哪些已付、哪些失败，并可以为失败的付款提供一张新订单卡。一次批准覆盖 24 小时内的付款；此后 Bot 会为剩余部分发送一张新订单卡。Link 或 X Money 这类钱包每笔付款需要一张订单卡，一批货物发往一个地址。

连接 Link 账号后，Bot 可以请你为单笔购买批准一张一次性卡。请求中显示商家、商品和总额。选择显示金额的**支付**按钮批准；选择**换一种方式付款（Pay another way）**跳过该卡，或选择**拒绝（Deny）**。批准后，在打开的 Link 页面完成授权。如果你拒绝或请求过期，不会扣款。如果卡片说你的 Link 账号未连接，请重新连接 Link，然后再让 Bot 试一次。
