---
title: "通过邮件给 Gemini 分配和跟踪任务"
linkTitle: "帮助：邮件派任务"
date: 2026-11-28
originalTitle: "Assign & track Gemini tasks through email"
sourceUrl: "https://support.google.com/gemini/answer/18745518?hl=en"
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）"
tags: [交互渠道, 持续执行]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的 Computer 视图（浏览器客户端标识）；页面中的界面小图标已下载。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：在设置的 Channels 中开启邮件后，向 gemini@google.com 发邮件即可创建任务，任务作为新线程出现在侧栏。要求有 Tasks 权限、美国的个人 Google 账号、Gemini 与 Gmail 登录同一账号，可以从 Gmail、支持「Sign in with Google」的邮件应用或使用官方 Gmail API 的应用发送。限制包括：附件不超过 10 个；邮件只能创建任务，询问进度会新建任务；自动转发、gemini@google.com 不在收件人栏、从工作或学校账号发送、带后缀的地址都不支持。

**保留理由**：给出邮件渠道的准入条件与限制，是博客与发布说明中「转发邮件派任务」的操作层细节。

---

你可以为 Gemini 设置电子邮件，直接从收件箱快速创建任务。通过邮件创建的任务会作为新的任务线程出现在 Gemini 应用的侧边面板中。

## 用电子邮件联系 Gemini 需要什么

要用电子邮件联系 Gemini，你必须：

- 符合条件并拥有 Gemini 中任务的访问权限。[进一步了解 Gemini 中的任务](https://support.google.com/gemini/answer/17094507)。
- 拥有一个位于美国的个人 Google 账号。
- 在 Gemini 应用和 Gmail 中登录同一个个人 Google 账号。
- 开启「用电子邮件联系 Gemini」。
- 使用以下方式之一，给 Gemini 发邮件至 [gemini@google.com](mailto:gemini@google.com)：
  - Gmail 应用或 [gmail.com](https://gmail.com)
  - 带有「使用 Google 登录」选项的邮件应用，例如用你的个人 Gmail 账号设置的 Apple Mail 或 Microsoft Outlook。
  - 使用官方 Gmail API 的应用。

## 开启或关闭「用电子邮件联系 Gemini」

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-01-a69c1b.png) ![然后](images/img-02-bfcdbc.png) **渠道** ![](images/img-03-828384.png)。
3. 在「用电子邮件联系 Gemini」旁，点击 **开启** 或 **关闭**。
4. 按屏幕上的说明操作。

开启「用电子邮件联系 Gemini」后，你就可以[给 Gemini 发邮件](mailto:gemini@google.com)来创建任务。任务创建后，你会收到一封回复，其中包含该任务的链接。

## 发给 Gemini 的邮件中不支持的情况

- **超过 10 个邮件附件：** 如果邮件附件超过 10 个，Gemini 不会创建任务。内嵌图片计入此上限，但 Google 云端硬盘链接不计入。
- **进度更新与讨论：** 目前，通过邮件只支持创建任务。如果你发邮件给 Gemini 讨论某个任务或询问其进展，它会创建一个新任务，你会收到一封包含新任务链接的回复。
- **不支持的邮件：**
  - 自动转发到 gemini@google.com 的邮件。
  - gemini@google.com 不在「收件人」字段中的邮件。
  - 由委托人从 Gmail 账号发送的邮件、从非 Gmail 账号发送的邮件，或从工作或学校账号发送的邮件。
  - 发送到 gemini@google.com 修改版地址的邮件，例如 gemini+urgent@google.com。

## 删除与 Gemini 的邮件时会发生什么

- 如果你删除了与 Gemini 的某封邮件，它不会从你的 Gemini 历史记录中删除。[了解如何管理你的 Gemini 历史记录](https://support.google.com/gemini/answer/13278892)。
- 如果你从 [Gemini 历史记录](https://myactivity.google.com/product/gemini)中删除活动，它不会从 Gmail 中删除该邮件。

## 关于你的位置数据

当你通过电子邮件创建任务时，Gemini 会综合使用多种位置信号，为与位置和时区相关的查询提供相关回复。这包括：

- 你保存在 Google 账号中的家庭和单位地址。
- 仅在[连接应用设置](https://gemini.google.com/apps)中已连接时，才使用你来自于搜索服务的近期活动。

## 相关资源

- [在 Gemini 应用中管理你的任务与工作流](https://support.google.com/gemini/answer/17094507)
