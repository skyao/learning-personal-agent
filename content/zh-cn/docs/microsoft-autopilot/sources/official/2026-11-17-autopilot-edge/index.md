---
title: "在 Microsoft Edge 浏览器中工作"
linkTitle: "文档：Edge 浏览器"
date: 2026-11-17
originalTitle: "Work in your Microsoft Edge browser with Autopilot"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/edge"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [设备, 安全, 功能更新]
products: [microsoft-autopilot]
updatedAt: "2026-11-17"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-10。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：说明在组织启用的情况下，Autopilot 可在用户设备的 Microsoft Edge 中使用已登录的站点，例如查找它无法直接访问的网站信息或填写网页表单供用户审阅；该功能在预览期间逐步推出。使用前要求 Edge 保持打开、以工作账号登录并连接到 Autopilot，首次使用需用户开启，请求须来自用户的私人对话（Microsoft Copilot 或一对一 Teams 聊天），例程不使用浏览器。Autopilot 只在本次对话涉及的标签页中操作，更改账号、结账付款、输入银行卡信息、永久删除、向外部站点提交个人信息或消息前须经批准，读取的页面内容会发送到云端模型，且不能访问本地文件夹或应用。

**保留理由**：补充云端 Autopilot 如何借用户本机 Edge 触达已登录站点的具体机制与边界，与旧 Scout 桌面应用直接操作本机的做法形成对照。

---

在你的 Microsoft Edge 浏览器中工作

[本文为预发布文档，内容可能变更。]

重要

- 访问 Autopilot（Frontier）需要完成相应的 **[Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)** 注册、预览分配并接受参与条款。仅完成 Frontier 注册并不会启用每一项预览功能。Frontier 预览受你的客户协议中适用的预览条款约束，其可用性与功能可能变化。
- 此功能处于预览阶段。
- 预览功能可能功能受限，并且可能不会正式发布。这些功能在正式发布之前提供，以便客户提前使用并提供反馈。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

在组织启用的情况下，Autopilot 可以在你设备上的 Microsoft Edge 中工作，使用你已经登录的站点。例如，你可以让它去某个它原本无法访问的站点查找信息，或替你填写一份网页表单供你审阅。

注意

浏览器使用功能正在预览期间逐步推出，你可能暂时无法使用。

在 Autopilot 使用你的浏览器之前：

- 你设备上的 Microsoft Edge 必须已打开、以你的工作账户登录，并连接到 Autopilot。如果 Edge 未连接，Autopilot 无法使用你的浏览器。
- 你在首次使用时开启浏览器使用功能。提示会说明 Autopilot 能触及什么、能做什么。
- 请求必须由你在自己的私人对话中提出，无论是在 Microsoft Copilot 中还是在一对一的 Teams 聊天中。例程（routine）不使用你的浏览器。

在你的浏览器中工作时，Autopilot：

- 只在该对话所涉及的标签页中打开、读取和操作。它看不到你的其他标签页。
- 在敏感操作前请求你的批准，例如更改账户、结账或付款、输入银行卡信息、永久删除某物，或向外部站点提交个人信息或消息。
- 把它读取的页面内容发送给其云端模型以完成任务。你的密码和 cookie 留在 Edge 中，但已登录页面上显示的信息可能成为它读取内容的一部分。

你组织的策略、Edge 策略和站点规则仍可能阻止某项操作。在依赖结果之前，请在该站点上核实结果。

Autopilot 无法访问你设备上的本地文件夹或应用。
