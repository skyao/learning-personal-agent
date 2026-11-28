---
title: "管理 Gemini 任务的浏览器与应用权限"
linkTitle: "帮助：任务权限"
date: 2026-11-28
originalTitle: "Manage browser & app permissions for tasks in Gemini"
sourceUrl: "https://support.google.com/gemini/answer/18766567?hl=en"
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）"
tags: [安全, 连接器, 设备]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的 Computer 视图（浏览器客户端标识）；页面中的界面小图标已下载。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：任务需要使用浏览器、在应用中操作或向网站和应用共享信息时，Gemini 会在任务线程中请求许可，选项有 Don't allow、Allow once、Allow for this chat 和 Always allow；选 Always allow 会同步写入 Connected Apps 设置。Connected Apps 设置里每个应用动作可设为 Always allow 或 Always ask，部分 Google 日历动作按设计自动执行。Mac 上可在 Computer use 设置中用「Blocked apps」「Allowed apps」控制 Gemini 能用的应用；有 Google AI 订阅时还可以选择 Gemini 用哪种浏览器完成任务。页面说明即使选了 Always allow，内置保护仍会对部分动作要求确认。

**保留理由**：讲清了任务权限选项与各处设置的联动，以及 Mac 上 computer use 的应用权限，是理解 Task 审批机制最细的一层说明。

---

当你给 Gemini 分配任务时，它可能需要某些权限才能处理你的任务。如果任务需要，Gemini 会请求你的许可来执行操作，例如：

- 使用浏览器与网站交互
- 在 Google 或第三方应用中执行操作
- 与网站或应用共享信息

你可以在任务线程中授予或拒绝权限，也可以在设置中管理它们，例如[浏览器设置](https://gemini.google.com/browser-settings)或[连接应用设置](https://gemini.google.com/customize/connectors)。

**重要提示：** 这些设置可在 Gemini 移动应用、[gemini.google.com](http://gemini.google.com) 的 Gemini 网页版以及 Mac 上的 Gemini 应用中使用。

## 在任务线程中授予或拒绝权限

Gemini 的设计是：在使用浏览器、在应用中做出更改，或执行你可能觉得敏感的操作、分享此类信息之前，先在任务线程中请求你的许可。你可以允许该操作一次，也可以保存你的偏好，让 Gemini 不必每次都询问。

**提示：** 对于删除数据、在 Google 应用中发送消息或邮件，或处理敏感的第三方任务（例如付款或分享敏感信息）这类操作，Gemini 的设计是先请求你的许可。

### 权限选项

当 Gemini 请求你许可执行某项操作时，可选项会因所使用的功能或服务而异。它们的含义如下：

- **不允许**（Don't allow）：拒绝该操作。Gemini 会停下，不会继续执行该操作。
- **允许**或**仅允许一次**（Allow once）：仅批准这一步的操作。Gemini 下次还会再问。
- **在此聊天中允许**（Allow for this chat）：在当前线程的后续过程中自动批准该操作，且不改变你的连接应用设置。
  - 此选项仅适用于已连接的 Google 产品。
  - 要重置聊天权限，请删除该任务线程或新建一个。
- **始终允许**（Always allow）：批准当前线程以及未来所有任务线程中的该操作。选择此项会自动把你在设置中的偏好更新为「始终允许」。

## 管理连接应用操作的权限

把应用连接到 Gemini 应用后，你可以控制 Gemini 能执行哪些操作，例如在该应用中读取、创建或删除信息的操作。你可以随时在[连接应用设置](https://gemini.google.com/customize/connectors)中更新应用操作的权限。这些权限适用于你所有的任务线程。

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏点击 **自定义** ![](images/img-02-dc4a4e.png) ![然后](images/img-03-bfcdbc.png) **连接器**。
   - 如果没有找到「自定义」，请先点击「更多」![](images/img-04-f0faa8.png)。
3. 点击你想管理权限的连接应用。
4. 在「应用操作」下，点击该操作旁的下拉菜单，选择你的权限偏好：
   - **始终允许：** Gemini 不经询问就执行该操作。
   - **每次都询问：** Gemini 在执行该操作前询问。

任务线程中的权限与你的连接应用设置如何配合

- **默认偏好：** 你的连接应用设置决定你在所有任务线程中的默认值（「始终允许」或「每次都询问」）。
  - 部分 Google 日历操作（包括更新活动和发送邀请）按设计会自动执行，Gemini 只在需要时确认。你可以随时在[连接应用设置](https://gemini.google.com/customize/connectors)中断开 Google Workspace。
- **线程特定的选择：** 如果你在任务线程中选择「仅允许一次」或「在此聊天中允许」，它只对那一步或那个聊天生效。你设置中的值在未来线程中仍为「每次都询问」。要重置聊天权限，请删除该任务线程或新建一个。
- **已保存的偏好：** 如果你在任务线程中选择「始终允许」，它会在你的连接应用设置中把该操作更新为「始终允许」。

## 管理 Mac 上应用的权限

当你让 Gemini 在你的 Mac 上工作时，可以在「计算机使用」设置中控制 Gemini 可以打开和使用哪些应用。[了解 Gemini 如何与 Mac 上的应用协作](https://support.google.com/gemini/answer/17208717)。

1. 在 Mac 上打开 Gemini 应用 ![](images/img-05-d2c18f.png)。
2. 在屏幕顶部点击 **Gemini** ![然后](images/img-03-bfcdbc.png) **设置**，或按 **⌘** + **,**。
3. 在侧边菜单点击 **计算机使用** ![](images/img-06-ecf11b.png)。
4. 要阻止 Gemini 访问某个应用：
   1. 在「已屏蔽的应用」下，点击「添加应用」![](images/img-07-1f3129.png)。
   2. 点击你绝不想让 Gemini 打开或使用的应用 ![然后](images/img-03-bfcdbc.png) **打开**。
5. 要允许 Gemini 访问某个应用：
   1. 在「已允许的应用」下，点击「添加应用」![](images/img-07-1f3129.png)。
   2. 点击你允许 Gemini 打开和使用的应用 ![然后](images/img-03-bfcdbc.png) **打开**。

要把某个应用从「已屏蔽的应用」或「已允许的应用」列表中移除，请将鼠标悬停在该应用上，然后点击「移除」![](images/img-08-23ae4d.png)。

任务线程中的权限与你的计算机使用设置如何配合

- **线程特定的选择：** 如果你在任务线程中选择「不允许」或「仅允许一次」，它只对那一步或那个聊天生效，不会改变你的计算机使用设置。
- **已保存的设置：** 如果你在任务线程中选择「始终允许」，它会把该应用添加到你的计算机使用设置中的「已允许的应用」列表。

## 管理浏览器偏好与设置

**重要提示：** 对于 Mac 上的 Gemini 应用，你可以在「计算机使用」设置中管理 Gemini 可以使用哪些浏览器。[了解如何管理应用的权限](#mac_app_permissions)。

你可以选择 Gemini 在打开浏览器处理你的任务前是否必须先请求许可。如果你有 Google AI 订阅，还可以选择 Gemini 以哪种方式浏览网页来完成任务。

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-09-bbb6bc.png) ![然后](images/img-03-bfcdbc.png) **浏览器** ![](images/img-10-23186a.png)。
3. 如果你有 Google AI 订阅，请在「偏好」下选择 Gemini 浏览网页的方式：
   - **让 Gemini 决定：** Gemini 会根据可用情况，为每项任务使用你设备上的 Chrome 或远程浏览器。
   - **仅使用远程浏览器：** 当你外出、设备不可用时，这种方式可用。
4. 要选择 Gemini 打开浏览器时是否请求许可，请点击「权限」旁的下拉菜单，选择你的偏好：
   - **始终允许：** Gemini 不经询问就使用网络。
   - **每次都询问：** Gemini 在使用网络前询问。

## 删除远程浏览器数据

当 Gemini 使用远程浏览器完成任务时，浏览器数据（例如包含你网站身份验证信息（即登录详情）的 Cookie）会为你保存下来，供之后的会话使用。你可以随时删除过去会话中保存的全部浏览器数据。Gemini 会在设定的不活动时间后自动代你删除已保存的浏览器数据，直到你手动删除为止，届时你可能需要重新登录网站。

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-09-bbb6bc.png) ![然后](images/img-03-bfcdbc.png) **浏览器** ![](images/img-10-23186a.png)。
3. 在「删除远程浏览器数据」旁，点击 **删除** ![](images/img-08-23ae4d.png)。

## Gemini 如何与你协作保护你和你的信息安全

为帮助防止意外操作并保护你的数据，Gemini 的设计会启用内置保护措施，即使你把某项权限设为「始终允许」，也会就部分操作与你确认。[进一步了解相关风险和 Gemini 的保护措施](https://support.google.com/gemini/answer/17094507#risks_safety)。

## 相关资源

- [在 Gemini 应用中管理你的任务与工作流](https://support.google.com/gemini/answer/17094507)
- [在 Mac 上的 Gemini 应用中分配任务](https://support.google.com/gemini/answer/17208717)
