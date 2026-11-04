---
title: "Muse 如何与连接器配合工作"
linkTitle: "帮助：连接器"
date: 2026-09-08
originalTitle: "How Muse works with Connectors"
sourceUrl: "https://www.meta.com/help/superintelligence/1687253048996149/"
publisher: "Meta 帮助中心"
language: en
fidelity: 全文翻译
collectedAt: 2026-11-04
dateNote: "帮助文档不标发布日期；日期取页面结构化数据中的最后修改时间，页面创建时间为 2026-07-08，2026-11-04 查看时页面显示 Updated: 8 weeks ago"
tags: [连接器, 隐私]
products: [muse]
---

{{< source-info >}}

你可以选择把 Muse 连接到由 Meta 或第三方提供的应用和服务。我们称之为连接器（Connectors）。当你设置一个连接器时，Muse 会获得新的能力，比如查看你的日历或写一封电子邮件的能力。

## 连接一个连接器

你可以通过向 Muse 提出请求来连接一个连接器（例如：“Connect my Gmail”（译注：意为「连接我的 Gmail」）），或者按照以下步骤操作：

1. 前往「设置」，然后点击「连接器」。
2. 点击你想要的连接器旁边的「连接」（Connect），并阅读相关信息。
3. 点击「继续」（Continue）授权连接。
4. 按照任何额外的登录或授权步骤操作。

在连接期间，你的 Muse 会与连接器交换与你交给它的任务相关的信息。连接器有自己的条款和隐私政策，规定它们如何使用收到的信息。

我们把 Muse 设计为只与连接器交换它们为你工作所需的数据。例如，连接你的电子邮件可以让 Muse 搜索你的电子邮件，但它不会下载你的整个收件箱（除非你让它这样做）。有些连接器还可以主动与 Muse 共享信息。例如，当你的日程发生变化时，日历连接器可以自动通知 Muse。我们会在你连接这类连接器之前标明它们。

## 断开一个连接器

你可以随时在「设置」的「连接器」下断开一个连接器。断开连接会让 Muse 停止与该连接器交换数据。Muse 之前用于通过该连接器执行任务的信息，可能仍然留在 Muse 的记忆和你的对话历史中。

注意：你也可以让 Muse [遗忘](https://www.meta.com/help/superintelligence/2225571704857152/)某些互动。

## 批准连接器操作

默认情况下，未经你的批准，Muse 不会采取许多重要操作，比如发送电子邮件。许多连接器也可以设置为只让 Muse 获取数据，而不能采取行动（比如发送日历邀请）。你可以在「设置」中更改 Muse 何时请求你的批准。了解更多关于[设置批准](https://www.meta.com/help/superintelligence/2225571704857152/)的信息。

## Meta 连接器

有些连接器连接的是 Meta 的产品。其中三个，Facebook、Instagram 和 Threads，如果你的这些账户在同一个账户中心（Accounts Center）中，就会自动连接。你不需要做任何设置。你可以随时在[账户中心](https://accountscenter.facebook.com/)管理你的账户。在 [Muse 隐私政策](https://muse.ai/privacy)中了解更多关于我们如何以及何时跨账户使用信息的内容。

## 自定义连接器

如果你想连接一个尚未出现在连接器列表中的服务，你可以让 Muse 创建一个自定义连接器（Custom Connector）。Muse 会引导你完成这个过程，其中可能包括获取该服务的 API 信息。Muse 会把这些信息存储在它的安全凭证存储（Secure Credentials Store）中。Meta 不审查自定义连接器，也不审查它们如何使用你的信息，所以请谨慎授予访问权限，并查看提供方的隐私政策。

## 说明：

* 设置完成后，你需要在设备设置中管理 Muse 对 Apple Health 或 Android SMS 等连接器的访问。
* 连接 Google 时，对从 Workspace API 接收到的信息的使用，将遵守 [Google 用户数据政策](https://developers.google.com/terms/api-services-user-data-policy)，包括其中的[有限使用要求](https://developers.google.com/terms/api-services-user-data-policy#additional_requirements_for_specific_api_scopes)。
