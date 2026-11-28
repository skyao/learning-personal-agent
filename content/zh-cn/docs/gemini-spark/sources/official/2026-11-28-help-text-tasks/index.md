---
title: "通过短信给 Gemini 分配和跟踪任务"
linkTitle: "帮助：短信派任务"
date: 2026-11-28
originalTitle: "Assign & track Gemini tasks through text message"
sourceUrl: "https://support.google.com/gemini/answer/18941404?hl=en"
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）"
tags: [交互渠道, 隐私]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的 Computer 视图（浏览器客户端标识）；页面中的界面小图标已下载。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：在 Channels 设置中为「Text with Gemini」验证手机号后，可以用短信创建、跟踪和讨论任务。条件是美国的个人 Google 账号、账号语言为英语、有 Tasks 权限、美国手机号与合格运营商；Android 需要 Google Messages 并开启 RCS，iPhone 需要开启 RCS Messaging 与 RCS Business Messages。页面说明短信不是端到端加密，运营商可能访问；删除 Gemini 活动不会删除消息应用或运营商处的记录。每个附件上限 15 MB，回复 STOP 退订、START 恢复，换设备或 SIM 卡可能需要重新验证。

**保留理由**：给出短信渠道的准入条件、对 RCS 的依赖以及加密与保留说明，博客与发布说明里没有这些细节。

---

你可以与 Gemini 开通短信通信，用来快速创建、跟踪和讨论你的任务。通过短信创建的任务会在 Gemini Apps 的侧边栏中作为新的任务线程出现。

## 用短信与 Gemini 对话需要什么

要开通与 Gemini 的短信通信，你必须：

- 拥有一个位于美国的个人 Google 账号。
- 把英语设为你的 [Google 账号语言](https://myaccount.google.com/language)。
- 有权在 Gemini Apps 中使用任务。[进一步了解任务的要求](https://support.google.com/gemini/answer/17094507)。
- 拥有一个美国手机号，且运营商在支持范围内。

要在 Android 手机上给 Gemini 发短信，你还必须：

- 安装 Google Messages。[在 Google Play 上获取](https://play.google.com/store/apps/details?id=com.google.android.apps.messaging)。
- 在 Google Messages 设置中开启 RCS 聊天。[了解如何开启](https://support.google.com/messages/answer/7189714)。
- Gemini 和 Google Messages 使用同一个手机号。
- 在 Gemini Apps 和 Google Messages 中登录同一个 Google 账号。

要在 iPhone 上给 Gemini 发短信，你还必须在「信息」设置中开启 RCS Messaging 与 RCS Business Messages。[了解如何开启](#ios_rcs_settings)。

在你的 iPhone 上开启 RCS Messaging 与 RCS Business Messages

1. 在 iPhone 上打开「设置」应用。
2. 依次点按 **Apps** ![然后](images/img-01-bfcdbc.png) **Messages** ![然后](images/img-01-bfcdbc.png) **RCS Messaging**。
3. 开启 **RCS Messaging**。
4. 开启 **RCS Business Messages**。

## 给 Gemini 发短信之前

与 Gemini 的短信不是端到端加密的，你的运营商可能访问这些内容，受其隐私政策和条款约束。删除你的 Gemini Apps 活动不会删除消息应用或运营商处的聊天记录。

## 开通与 Gemini 的短信通信

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-02-a69c1b.png) ![然后](images/img-01-bfcdbc.png) **Channels**（渠道）![](images/img-03-828384.png)。
3. 在「Text with Gemini」旁边点击 **Set up**（设置）。
4. 选择你想用来与 Gemini 收发短信的手机号，或点击 **Add a phone number**（添加手机号）。
5. 如有需要，验证你的手机号。
6. 按屏幕上的其他说明操作。

开通与 Gemini 的短信通信后，你会收到一条来自 Gemini 的短信。在与 Gemini 的短信聊天中，你可以创建任务、获取状态更新，或讨论已有的任务。

## 发给 Gemini 的短信的附件限制

你可以在与任务相关的短信中加入多媒体、文件、位置信息等附件。每个附件上限为 15 MB。

## 从 Gemini 中移除你的手机号

要停止 Gemini 的短信通信，在 Channels 设置中移除你的号码。

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-02-a69c1b.png) ![然后](images/img-01-bfcdbc.png) **Channels**（渠道）![](images/img-03-828384.png)。
3. 在「Text with Gemini」卡片上，找到要移除的手机号，点击「移除」![](images/img-04-f02acc.png) ![然后](images/img-01-bfcdbc.png) **Remove**（移除）。

**提示：** 你可以直接在消息应用中退订或重新订阅 Gemini 的短信。在与 Gemini 的短信聊天中输入「STOP」退订，输入「START」重新订阅。

## 删除与 Gemini 的短信后会发生什么

- 如果你删除了与 Gemini 的短信聊天，它不会从你的 Gemini Apps 活动中删除。[了解如何管理你的 Gemini Apps 活动](https://support.google.com/gemini/answer/13278892)。
- 如果你从 [Gemini Apps 活动](https://myactivity.google.com/product/gemini)中删除记录，消息应用或运营商处的这条短信或聊天不会被删除。

## 解决问题

我收到一条短信，要求我登录 Google 账号

如果你收到 Gemini 发来的要求登录 Google 账号的短信，请确保在 Gemini Apps 和 Google Messages 中登录的是同一个账号。

我收到一条短信，要求我验证号码

如果 Gemini 检测到新设备或 SIM 卡，你可能会收到要求重新验证号码的短信。

要验证你的号码：

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-02-a69c1b.png) ![然后](images/img-01-bfcdbc.png) **Channels**（渠道）![](images/img-03-828384.png)。
3. 在「Text with Gemini」卡片上，点击你需要验证的手机号。
4. 按屏幕上的说明操作。

我收到错误提示，说我的运营商的号码不受支持

目前，部分移动运营商不支持与 Gemini 的短信通信。

我删除了与 Gemini 的短信聊天，Gemini 还能发新短信吗？

如果你从消息应用中删除了与 Gemini 的短信聊天，可以让 Gemini 在 Channels 设置中发起新的短信聊天。

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-02-a69c1b.png) ![然后](images/img-01-bfcdbc.png) **Channels**（渠道）![](images/img-03-828384.png)。
3. 在「Text with Gemini」卡片上点击 **Send text**（发送短信）。

## 相关资源

- [在 Gemini Apps 中管理你的任务与工作流](https://support.google.com/gemini/answer/17094507)
- [在 Google Messages 中开启 RCS 聊天](https://support.google.com/messages/answer/7189714)
