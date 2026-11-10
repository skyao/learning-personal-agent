---
title: "在 Microsoft Scout 中使用 Microsoft 365"
linkTitle: "文档：Microsoft 365"
date: 2026-08-21
originalTitle: "Work with Microsoft 365 in Microsoft Scout"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [连接器, 安全]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-08-05"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：文档说明 Microsoft Scout 可处理已连接的 Microsoft 365 账户能访问的会议、邮件、列表和文件：Outlook 邮件、日历、Teams、Microsoft To Do、人员与内容查找、Teams 会议转录、会议室预订、SharePoint Lists、Outlook 收件箱规则以及 OneDrive/SharePoint 文件共享。凡是修改共享信息或影响他人的操作，如发送邮件、发 Teams 消息、创建或更新列表项，均需先经用户批准。文件共享只面向用其自己账号登录的指定人员，不创建匿名或公开链接，可设置查看或编辑权限及可选的到期日。无法完成请求时，文档给出六步排查，并说明 Scout 不会授予账户或组织本来不允许的访问权限。

**保留理由**：这是 Scout 连接 Microsoft 365 各服务时具体能做什么、哪些步骤需批准的官方说明，并包含文件共享边界。

---

在 Microsoft Scout 中使用 Microsoft 365

[本文为预发布文档，可能会变更。]

重要

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能**抢先体验** Microsoft Scout。Frontier 让你直接接触 Microsoft 最新的 AI 创新。Frontier 预览受你客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是一项预览功能。
- 预览功能可能功能受限，且可能不会正式发布。这些功能在正式发布之前提供，以便客户抢先体验并提供反馈。
- 更多信息，请访问我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

Microsoft Scout 可以处理你已连接的 Microsoft 365 账户能够访问的会议、邮件、列表和文件。在聊天中描述你想要的结果。Scout 在完成会更改共享信息或影响他人的操作之前会请求批准。

要连接你的账户，请参阅[连接到 Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/get-started#connect-to-microsoft-365)。

## 使用 Outlook 邮件

让 Scout 读取、发送、回复、转发或整理电子邮件。

例如：

- 「显示我今天未读的邮件。」
- 「回复 Sarah 的邮件并确认会议时间。」
- 「把所有新闻简报移到『存档』文件夹。」

Scout 在发送消息或做出其他影响你邮箱的更改之前会请求批准。

## 使用日历

让 Scout 查看你的日程、创建或更新事件、查找空闲时间并回复邀请。

例如：

- 「我明天日历上有什么？」
- 「下周我和 Alex 什么时候都有空？」
- 「拒绝下午 4 点的会议，并说明我有冲突。」

在 Scout 创建或更改事件之前，请查看事件详情和批准请求。

## 使用 Teams

让 Scout 查看 Teams 聊天、发送消息、在频道中发帖，以及检查某人是否有空。

例如：

- 「显示我最近的 Teams 消息。」
- 「给 Engineering 聊天发条消息，说构建已修复。」
- 「把发布摘要发到 Announcements 频道。」

Scout 在发送或发布消息之前会请求批准。

## 使用 Microsoft To Do

让 Scout 查看、创建和整理任务与列表。

例如：

- 「本周有哪些任务到期？」
- 「把『发送预算草稿』加到我的 Work 列表。」
- 「创建一个 Travel 列表，并为这次旅行添加子任务。」

## 查找人员和内容

Scout 可以在你组织的目录中查找人员，并在你的 Microsoft 365 内容中搜索。

例如：

- 「查找 Jordan 的电子邮件地址。」
- 「查找与 Q4 规划计划相关的所有内容。」
- 「总结本周 Engineering 频道里发生的事。」

## 获取 Teams 会议转录

向 Scout 索取某个特定 Teams 会议或你最近会议的转录。知道会议名称或日期时请一并说明。

例如：

- 「获取我昨天项目评审会议的转录。」
- 「查找我最近的会议转录并总结其中的决定。」

会议转录必须对你账户可访问的会议可用。

## 查找并预订会议室

Scout 可以查找你组织定义的会议室，并为日历事件预订会议室。

例如：

- 「找一个明天下午能容纳六人的会议室，并预订 30 分钟。」
- 「为我周五的设计评审预订一间可用会议室。」

在 Scout 创建或更改事件之前，请查看事件详情和批准请求。

## 使用 SharePoint 列表

Scout 可以查找 SharePoint 网站上的列表、查看其列和项，以及创建或更新列表项。

例如：

- 「显示项目跟踪列表中的未完成项。」
- 「把这个问题加到团队的 SharePoint 列表。」
- 「更新发布检查清单项的状态。」

你的账户需要有权访问该网站和列表。Scout 在创建或更新列表项之前会请求批准。

## 管理 Outlook 收件箱规则

Scout 可以列出、创建、更新、启用、禁用和删除 Outlook 收件箱规则。

例如：

- 「显示我的 Outlook 收件箱规则。」
- 「创建一条规则，把每周摘要的邮件移到我的『存档』文件夹。」
- 「禁用名为 Project alerts 的规则。」

Scout 在创建、更改或删除规则之前会请求批准。

## 共享文件和管理访问权限

让 Scout 与指定人员共享 OneDrive 或 SharePoint 文件或文件夹、查看谁已有访问权限，或把某人的访问权限从查看提升为编辑。存储在 Teams 团队中的文件通过其 SharePoint 位置共享。请指明文件和相关人员。

例如：

- 「把项目简报共享给设计团队，让他们可以编辑。」
- 「谁有权访问预算工作簿？」
- 「给 Priya 发布计划的编辑权限。」

Scout 与使用自己账户登录的指定人员共享文件；它不会创建匿名或公开链接。你可以授予查看或编辑权限并设置可选的到期日期，Scout 可以发送 Microsoft 的共享邀请电子邮件。Scout 可以授予、提升或检查访问权限，但无法移除某人已有的访问权限——请在文件的 Microsoft 365 应用中执行此操作。

在 Scout 做出更改之前，请查看文件、收件人、访问级别和批准请求。可用操作取决于你的访问权限和组织的共享策略。

你也可以让 Scout 在 OneDrive 和 SharePoint 中浏览、读取和上传文件。

## 排查访问问题

如果 Scout 无法完成某项 Microsoft 365 请求：

1. 确认你使用的是预期的工作或学校账户连接。
2. 在其 Microsoft 365 应用中打开该会议、列表、邮箱或文件，确认你可以访问它。
3. 对于转录请求，确认该会议有可用的转录。
4. 对于文件请求，确认文件没有被移动或删除。
5. 在 Scout 中查看并回应任何批准请求。
6. 如果你仍然没有访问权限，请联系内容所有者或管理员。

Scout 不会授予你的账户或组织原本不允许的访问权限。

## 相关内容

- [使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout)
- [开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Microsoft Scout 常见问题](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- [Microsoft Scout 的新功能](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
