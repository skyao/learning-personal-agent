---
title: "文档：管理成员的计算机与数据"
linkTitle: "文档：管理计算机"
date: 2026-11-05
originalTitle: "Manage Grok Bot computers"
sourceUrl: "https://cursor.com/docs/grok-bot/computers"
altUrls: ["https://docs.x.ai/grok-bot/computers"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 隐私, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：每个团队成员有一台托管计算机，其上的所有 Bot 都在这里工作。企业管理员可在 Cursor 控制台批量重建（Recreate）或终止（Terminate）成员的计算机，删除计算机及数据，或删除成员的全部 Grok Bot 数据；此功能仅限 Enterprise。重建和终止都保留成员的持久磁盘，重建时正在执行的 Bot 会在安全点暂停并在新计算机上继续，终止则让运行中的工作停止，下次发消息会在同一磁盘上新建计算机。删除计算机及数据一次最多 1,000 名成员，删除全部数据一次最多 100 名，均不可撤销并写入审计日志。还可设置保留期，在无人给成员的任何 Bot 发消息达 30 至 365 天后自动删除休眠的计算机，默认关闭且删除前不通知。

**保留理由**：写明了计算机重建、终止、删除的差别和数据保留规则，是了解云端计算机生命周期与持久磁盘的直接材料。

---

你团队中的每位成员获得一台托管计算机（hosted computer），他们运行的每个 Bot 都在这台计算机上完成工作。[Cursor 控制台](https://cursor.com/dashboard/bot)的 Grok Bot 页面中，**Security & Compliance** 下的 **Manage Member Computers and Data** 让管理员可以一次为许多成员重建或终止计算机、[删除计算机及其数据](#delete-vms-and-data)，或[删除某位成员的全部 Grok Bot 数据](#delete-all-grok-bot-data)。**Data Retention** 下的 **Retention Period for Computers** 会为你[删除不活跃的计算机](#delete-inactive-computers-automatically)。其余管理员控制项参见[面向 Teams 和 Enterprise 的 Grok Bot](https://cursor.com/docs/grok-bot/teams)。

**Manage Member Computers and Data 仅限 Enterprise。** 组织管理员和 Enterprise 团队管理员可以使用它。成员永远看不到这个控制项。

## 重建或终止

两种操作都会保留成员的持久磁盘（durable disk），因此他们已同步的 Bot、文件和登录状态会在下一台计算机上恢复。两者都会移除成员自己安装的应用和软件包。你的团队设置脚本（Team Setup Scripts）安装的任何内容都会在新计算机上恢复。

| 操作 | 会发生什么 | 何时使用 |
| --- | --- | --- |
| **Recreate** | 在最新的镜像上构建一台替换计算机，并运行[团队设置脚本](https://cursor.com/docs/grok-bot/private-networks)。当前计算机会保持可用，直到替换计算机就绪，然后 Grok Bot 切换过去。处于回合（turn）中途的 Bot 会在安全点暂停，并在新计算机上继续。如果它无法及时暂停，该成员的重建就不会启动，并显示为失败。 | 一次向许多成员推出新镜像或更新后的团队设置清单（Team Setup manifest）。[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)变更无需重建即可到达计算机。 |
| **Terminate** | 删除成员的计算机，无论运行中还是已休眠。运行中的工作会停止。计算机不会自行重启；该成员的下一条消息会在同一持久磁盘上启动一台新计算机。 | 结束成员当前的工作，或清理卡住的计算机。终止不会移除访问权限；参见[常见问题](#faq)。 |

## 删除虚拟机与数据

**Delete VMs and Data** 会删除成员的计算机及其持久磁盘。他们的 Bot 和对话会保留，他们的下一条消息会启动一台空计算机。

- 每次操作**最多 1,000 名成员**。
- **无法撤销。** 每次操作都会记录在[审计日志](https://cursor.com/dashboard/audit-log)中。

## 删除全部 Grok Bot 数据

**Delete All Grok Bot Data** 会永久删除成员在他们所属的每个团队中的 Bot、对话、记忆、例程和计算机。他们的 Cursor 账号会保留。

- 每次操作**最多 100 名成员**。
- **无法撤销。** 每次操作都会记录在[审计日志](https://cursor.com/dashboard/audit-log)中。

## 执行一次操作

1

### 打开 Manage Member Computers and Data

前往 [Cursor 控制台中的 Grok Bot](https://cursor.com/dashboard/bot)，在 **Security & Compliance** 下找到 **Manage Member Computers and Data**，然后选择 **Manage**。

2

### 选择成员

按姓名或电子邮件搜索，然后勾选你想要的成员。**Select all** 会选中当前结果中的所有人。

3

### 选择操作

打开 **Manage selected**，选择 **Recreate VMs** 或 **Terminate VMs**。确认界面会重述该操作及其影响的成员数量。同一菜单还提供[删除虚拟机与数据](#delete-vms-and-data)和[删除全部 Grok Bot 数据](#delete-all-grok-bot-data)。只有当你希望成员从空环境开始时，才使用这两项。

4

### 确认

选择 **Recreate VMs** 或 **Terminate VMs** 开始。没有计算机的成员会被跳过。

5

### 查看结果

进度卡片会显示排队、运行中、完成、跳过和失败的数量，每位成员所在行会显示其状态。操作完成后，选择 **Done** 清除结果并开始另一次操作。

## 操作如何运行

- **它在 Cursor 一侧运行。** 关闭对话框或浏览器不会停止它。在同一浏览器中重新打开 **Manage** 即可继续查看进度。
- **大型操作需要一段时间。** 成员按批次处理，每次重建都要等替换计算机就绪后才算完成。
- **每个团队一次只能进行一个操作。** 在你于完成的结果上选择 **Done** 之前，操作按钮会一直处于禁用状态。
- **Retry Start 绝不会重复工作。** 当控制台无法确认操作已启动时使用它。

## 被跳过和失败的成员

完成的操作会列出你所选每位成员的结果。

| 结果 | 含义 | 该怎么做 |
| --- | --- | --- |
| **Skipped**，无虚拟机 | 该成员没有运行中或已休眠的计算机。 | 无需处理。 |
| **Skipped**，操作无法完成 | 操作排队期间，该成员离开了团队，或其账号发生了变更。 | 无需处理。 |
| **Failed**，另一次重建正在进行 | 该成员的计算机已经在被重建，原因是更新或另一位管理员。 | 等待其完成，然后为该成员重新运行。 |
| **Failed**，虚拟机扫描不完整 | Cursor 无法确认该成员计算机的状态，因此未做任何更改。 | 几分钟后再次运行该操作。 |
| **Failed**，另一次删除正在进行 | 该成员的 Grok Bot 数据已经在被删除。 | 等待其完成。 |
| **Failed**，Grok Bot 数据无法删除 | 删除未完成。 | 再次运行该操作。如果失败两次，[联系支持](https://cursor.com/help/grok-bot/get-help)。 |
| **Failed**，操作无法完成 | 重建或终止未完成。对于重建，成员计算机上的某个 Bot 可能未能及时暂停，该成员会保留当前计算机。 | 对受影响的成员再次运行该操作，如果可能，等他们的 Bot 空闲后再运行。如果失败两次，请携带该成员的电子邮件和操作时间[联系支持](https://cursor.com/help/grok-bot/get-help)。 |

## 通过 API 运行操作

若要通过脚本在许多团队中推出，可使用[组织 API（Organization API）](https://cursor.com/docs/account/organizations/organization-admin-api#grok-bot-computers)启动相同的操作。你发送一个团队、一份成员列表和一个操作，然后轮询该操作以获取计数和每位成员的结果。

API 和控制台共享「每个团队一次只能有一个操作」的限制。从任一入口启动的操作会阻塞另一个，直到它完成。

## 自动删除不活跃的计算机

已休眠的计算机一直存在，直到有人删除它，即使该成员已经离开或停止使用 Grok Bot。同一控制台页面中 **Data Retention** 下的 **Retention Period for Computers** 会替你完成这项清理。当在你选定的时间段内没有人给某位成员的任何 Bot 发消息时，Cursor 会在该计算机下一次处于睡眠状态时删除它及其持久磁盘。来自应用或 Slack 的消息都计入，无论发送者是该成员还是队友。例程和 Bot 自行启动的其他工作不计入。发送消息会重新开始计时。

该设置默认关闭。可选择 30、60、90、180 或 365 天，或 30 到 365 天之间的自定义时段。开启它或缩短时段时会先弹出确认。

- **删除与[删除虚拟机与数据](#delete-vms-and-data)相同。** 成员的 Bot 和对话会保留。他们的文件、登录状态和已安装的应用会永久消失，他们的下一条消息会启动一台空计算机。
- **没有警告。** 成员的计算机被删除前不会收到任何通知。
- **以最短时段为准。** 一台计算机横跨成员所属的所有团队，因此会遵循其任一 Enterprise 团队设定的最短时段。

每次删除都会记录在[审计日志](https://cursor.com/dashboard/audit-log)中。关闭该设置会停止进一步的删除。

## 成员会看到什么

重建期间，桌面应用会显示 **Updating Grok Bot's Computer**，直到切换完成。正在工作的 Bot 会在安全点暂停，并在新计算机上继续。计算机被重建时，其中的登录会话可能中断，因此成员需要按照你的身份提供商（identity provider）策略重新登录公司工具。

终止之后，该成员的下一条消息会在其持久磁盘上启动一台新计算机。重新连接可能需要几分钟。已同步的 Bot、文件和登录状态会恢复；正在运行的回合会丢失。

## 常见问题

### 我可以从其他团队重建成员的计算机吗？

可以。可以从该成员所属的任一团队中选择该成员。一台计算机会服务该成员所在的每个团队，因此从某个团队重建或终止它，会影响所有地方的同一台计算机。

### 终止会让成员无法使用 Grok Bot 吗？

不会。终止计算机会结束该成员当前的工作。他们的下一条消息会在同一持久磁盘上启动一台新计算机，带有他们的 Bot、文件和登录状态。要移除访问权限，请将该成员从团队中移除，或用 **Manage Group Access** 关闭其访问权限，并在你的身份提供商处撤销其会话。参见[启用 Grok Bot](https://cursor.com/docs/grok-bot/teams#enable-grok-bot)。

### 自动删除会打断仍在工作的 Bot 吗？

不会。Cursor 只删除处于睡眠状态的计算机。因为 Bot 正在工作或成员正在使用 Grok Bot 而处于唤醒状态的计算机，绝不会被此设置删除，即使该成员的 Bot 在整个时段内都没有收到消息。
