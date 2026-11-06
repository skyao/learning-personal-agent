---
title: "文档：开始使用 Grok Bot"
linkTitle: "文档：开始使用"
date: 2026-11-05
originalTitle: "Get started with Grok Bot"
sourceUrl: "https://cursor.com/docs/grok-bot/get-started"
altUrls: ["https://docs.x.ai/grok-bot/get-started"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [功能更新, 开放与价格, 设备, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：此文带用户从安装桌面应用到完成第一个任务：用 Cursor 账号登录，系统自动建立名为 Grok Bot 的第一个 Bot，之后可用「+」添加更多。建议每个 Bot 只给一个主要工作，并在第一条消息里让它记住怎么做，好的请求要写明结果、资料来源、约束、交付物和何处停下来问用户。遇到需要登录的应用，Bot 先用 Vault 中保存的登录或已连接的密码管理器，否则用安全表单（Secure Form）向用户要，Bot 看不到密码；单点登录、通行密钥等表单搞不定的步骤，转交用户点击「Open computer」完成。手机端可发消息、查看和接管计算机、审批动作、暂停或恢复例程，但示范教学、测试例程和更新计算机仍在桌面端。访问权包含在所有付费个人 Cursor 套餐和 Cursor Teams 中，也可经 SuperGrok 链接或自助 Grok Business 席位获得；Privacy Mode (Legacy) 账号需先切换。

**保留理由**：用最短路径说明新用户的上手流程、凭证处理方式和手机与桌面的功能差别，也重复了访问权来源。

---

本指南带你从安装走到第一个完成的任务。你会设置桌面应用、创建一个职责明确的 Bot，并审阅它的工作。若需要更简短帮助中心清单，请遵循[入门引导（Onboarding）](https://cursor.com/help/grok-bot/onboarding)。

Grok Bot 访问权包含在每个付费个人 Cursor 套餐和 Cursor Teams 套餐中，也可通过关联个人 SuperGrok，或以自助式 Grok Business 套餐中的一个席位获得。见[套餐与计费](https://cursor.com/help/grok-bot/plans)。Grok Bot 需要云端数据存储，因此处于 Privacy Mode (Legacy) 的账号会被提示在开始前切换到 Privacy Mode。

1

### 安装桌面应用

从 [Cursor 仪表盘（dashboard）](https://cursor.com/dashboard/bot)的 Grok Bot 页面获取安装程序：**Download Grok Bot** 设置行会安装桌面应用，或复制一个你可以分享的链接。如果你没有仪表盘访问权，向管理员索取下载链接。应用可在 macOS（Apple 芯片与 Intel）、Windows（x64 与 Arm64）和 Linux（x64 与 Arm64）上运行，并自动检查更新。在手机上，从 App Store 或 Google Play 安装 Grok Bot；见[在手机上使用 Grok Bot](#use-grok-bot-on-your-phone)。

2

### 用你的 Cursor 账号登录

在欢迎屏幕选择 **Sign in**，并在浏览器中完成身份验证。Grok Bot 使用你的 Cursor 账号，没有单独的 Grok Bot 登录。如果你的组织使用单点登录（single sign-on），通过你正常的公司流程登录；你现有的 Cursor SSO 配置会生效。登录问题见[登录 Grok Bot](https://cursor.com/help/grok-bot/sign-in)。

3

### 认识你的第一个 Bot

登录后，点击浏览一段简短介绍。Grok Bot 随后会设置你的第一个 Bot，名为 **Grok Bot**，并打开与它的聊天。

要添加更多 Bot，选择侧边栏中的 **+** 按钮，然后选择 **Create a Bot**，给 Bot 命名，并选择 **Create**。在 Cursor 团队中，共享一个 Bot 以便队友与它聊天，并在 **+** 下选择 **Browse shared Bots** 来查找与你共享的 Bot；见[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)。在第一条消息中给每个 Bot 一项主要工作，并让它记住应该如何工作。要重命名它，点击聊天顶部的名称以打开其详情。一个专注的 Bot 比一个包揽一切的助手能建立更有用的上下文。例如：

> 你的工作是产品性能。用我们的可观测性（observability）工具调查产品性能问题。保留链接和截图，把证据与假设分开，并先讲影响最大的问题。永远不要更改生产设置。为未来的工作记住这一点。

4

### 给它第一项任务

一个有力的请求会写明结果、重要的来源、约束、交付物，以及 Bot 应在何处停下来找你。想要五分钟得到第一个结果，可以附上一份文档并尝试：

> 用五个要点总结这份文档。在单独一节中列出每个日期、决策和未决问题，并为每一项引用相应章节。不要更改源文件。

5

### 登录它需要的工具

当 Bot 遇到需要身份验证的应用时，它会使用保存在 [Vault](https://cursor.com/help/grok-bot/secrets#what-is-vault) 中的登录信息或已连接的密码管理器，或者用安全表单（Secure Form）向你索取。Bot 永远看不到密码，登录后的会话会保留在你的计算机上供未来任务使用。对于单点登录、通行密钥（passkey）或表单无法处理的其他步骤，它会把计算机交给你：点击 **Open computer**，完成该步骤，然后交回控制权。对于受支持的服务，你也可以改为[连接一个应用](https://cursor.com/docs/grok-bot/work#connect-apps)。

6

### 审阅结果并让它固定下来

请求修改，并明确说出希望长期保留的偏好，比如你希望重复使用的报告格式。当流程稳定后，把它保存为[技能或例程](https://cursor.com/docs/grok-bot/work#skills-and-routines)。

在你让 Bot 更改外部系统之前，请阅读[审批与自动审阅](https://cursor.com/docs/grok-bot/security#approvals-and-auto-review)。它涵盖审批提示、其背后的审阅模型，以及如何让凭证不出现在聊天中。

## 在手机上使用 Grok Bot

iPhone 应用（iOS 18 或更高版本）和 Android 应用（Android 9 或更高版本）连接到与桌面端相同的 Bot、对话、例程和云端计算机。从 App Store 或 Google Play 安装 Grok Bot，并用同一个 Cursor 账号登录；来自你套餐或 SuperGrok 链接的访问权会延续，无需再次购买。在手机上，你可以给 Bot 发消息、观看并接管计算机、批准动作，以及暂停或恢复例程。

有些流程仍留在桌面端：通过示范教授工作流、测试例程，以及更新计算机。设置细节见[移动端 Grok Bot](https://cursor.com/help/grok-bot/mobile)；如果你的账号不包含访问权，见[从移动应用订阅](https://cursor.com/help/grok-bot/mobile-purchase)。

## 如果某处不工作

大多数设置问题在你完全退出并重新打开应用后会解决。若需按症状查找关于计算机、例程、已连接应用和启动问题的帮助，请见帮助中心的 [Grok Bot How Tos](https://cursor.com/help/grok-bot/how-to#how-do-i-troubleshoot-grok-bot-computer-routine-connector-and-startup-problems)，或[联系支持](https://cursor.com/help/grok-bot/get-help)。
