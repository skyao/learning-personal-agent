---
title: "为 Gemini 应用连接和管理自定义应用"
linkTitle: "帮助：自定义 MCP 应用"
date: 2026-11-05
originalTitle: "Connect & manage custom apps for Gemini Apps"
sourceUrl: "https://support.google.com/gemini/answer/17209137?hl=en"
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）。2026-10 Spark 改名为 Task 后，帮助页的用词已改为 tasks / task mode"
tags: [连接器, 安全, 隐私]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的默认（Computer）视图；页面中的界面小图标已下载。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：可以用 MCP 服务器地址把个人或第三方应用接入 Gemini，在任务中构建定制工作流，或在聊天中快速执行动作。条件是年满 18 岁且在美国、使用个人 Google 账号、开启 Keep Activity，MCP 服务器须符合标准规范；目前只支持英语。页面提醒，使用自定义应用时 Gemini 可能把聊天内容以及 Connected Apps、Personal Intelligence、技能、任务和已登录网站中的信息分享给该应用，并说明怎样断开、解除关联和删除。

**保留理由**：自定义 MCP 的准入条件和数据分享范围，是 Spark/Task 开放连接能力的边界。

---

你可以将个人应用或第三方应用连接起来，在任务中构建高度定制的工作流，或在聊天中快速执行操作。为此，请在 Gemini 网页应用中添加自定义应用，并填写其模型上下文协议（Model Context Protocol，MCP）服务器 URL。连接后，你可以在 Gemini 移动应用和 Gemini 网页应用中使用这个已连接的自定义应用。

**面向开发者：** 你可以使用新的 [Connected Apps Platform](https://developers.google.com/connected-apps) 将自己的应用和 MCP 服务器与 Google 的智能体产品（如 Gemini 应用）集成。你还可以使用 [Gemini Developer Mode](https://developers.google.com/connected-apps/mcp/dev-mode) 调试、验证架构并测试你的自定义应用。

## 你需要什么

要将自定义应用连接到 Gemini 应用，你必须：

- **年满 18 岁，且身处美国。**
- **使用个人 Google 账号登录 Gemini 应用。** 目前，如果你使用工作或学校 Google 账号登录，此功能不可用。[了解如何登录 Gemini 应用](https://support.google.com/gemini/answer/13278668)。
- **开启 [Keep Activity](https://myactivity.google.com/product/gemini?utm_source=help)。** 关闭此设置时，自定义应用不可用。
- **拥有自定义应用的 MCP 服务器 URL。** MCP 服务器必须遵循标准 MCP 规范。

**重要：** 目前，自定义已连接应用（Connected Apps）：

- 仅提供英语版本。
- 仅在 Gemini 移动应用和 [gemini.google.com](https://gemini.google.com) 上的 Gemini 网页应用中可用。

## 连接自定义应用之前

Google 不控制、不监控也不保护第三方 MCP 服务器。你有责任监督该 MCP 服务器。在将 MCP 服务器连接到 Gemini 应用之前，请确保你了解它支持哪些操作，并信任其提供方。

[进一步了解连接自定义应用的风险](#risks)。

## 连接自定义应用

**重要：** 你只能在 Gemini 网页应用中连接自定义应用。连接后，它们会在 Gemini 移动应用和 Gemini 网页应用中同时可用。

你可以在[已连接应用设置](https://gemini.google.com/apps)中链接自定义应用的 MCP 服务器来添加它。

1. 在电脑上访问 [gemini.google.com](https://gemini.google.com)。
2. 在页面底部，依次点击「设置」![](images/img-01-1c0260.png) ![](images/img-02-bfcdbc.png) **已连接应用** ![](images/img-03-aa3481.png)。

   - 如果找不到「已连接应用」，请先点击 **Personal Intelligence** ![](images/img-02-bfcdbc.png) **已连接应用**。[了解 Personal Intelligence 和已连接应用](https://support.google.com/gemini/answer/16598406)。
3. 在「自定义应用」下，找到「添加自定义应用链接以开始使用」字段；如果你已经连接过自定义应用，请点击 **添加自定义应用** ![](images/img-04-e8b4c8.png)。
4. 输入该应用的 MCP 服务器 URL。
   - 如果服务器不支持动态客户端注册（Dynamic Client Registration），请在「高级功能」旁点击 **显示更多**，然后输入你的凭据。
5. 点击 **下一步**。
6. 按屏幕上的说明操作。

**提示：**

- 为确保 Gemini 针对某个提示使用你已连接的自定义应用，请输入 `@` 并选择该自定义应用。
- 要调试、验证架构并测试自定义应用，请试用 [Gemini Developer Mode](https://gemini.google.com/devmode)。[进一步了解 Gemini Developer Mode](https://developers.google.com/connected-apps/mcp/dev-mode)。

## 断开自定义应用

1. 在电脑上访问 [gemini.google.com](https://gemini.google.com)。
2. 在页面底部，依次点击「设置」![](images/img-01-1c0260.png) ![](images/img-02-bfcdbc.png) **已连接应用** ![](images/img-03-aa3481.png)。

   - 如果找不到「已连接应用」，请先点击 **Personal Intelligence** ![](images/img-02-bfcdbc.png) **已连接应用**。[了解 Personal Intelligence 和已连接应用](https://support.google.com/gemini/answer/16598406)。
3. 在「自定义应用」下，找到要断开的应用并将其关闭 ![](images/img-05-923460.png)。
4. 按屏幕上的任何说明操作。

## 从 Google 账号解除 MCP 服务器的关联

你可以在[已连接应用设置](https://gemini.google.com/apps)中从 Google 账号解除 MCP 服务器的关联并撤销其权限。这也会断开该自定义应用，使 Gemini 无法使用它，但不会将其从你的已连接应用设置中移除。你可以随时重新链接该 MCP 服务器以重新连接自定义应用。

1. 在电脑上访问 [gemini.google.com](https://gemini.google.com)。
2. 在页面底部，依次点击「设置」![](images/img-01-1c0260.png) ![](images/img-02-bfcdbc.png) **已连接应用** ![](images/img-03-aa3481.png)。

   - 如果找不到「已连接应用」，请先点击 **Personal Intelligence** ![](images/img-02-bfcdbc.png) **已连接应用**。[了解 Personal Intelligence 和已连接应用](https://support.google.com/gemini/answer/16598406)。
3. 在「自定义应用」下，找到你想断开连接的自定义应用。
4. 点击 **更多详情** ![](images/img-02-bfcdbc.png) **断开连接**。

**提示：** 你也可以从 [Google 账号的已关联应用页面](https://myaccount.google.com/linkedapps)解除 MCP 服务器的关联。[了解如何管理已关联的应用](https://support.google.com/accounts/answer/13533235#link_account)。

## 移除已连接的自定义应用

如果你不再希望 Gemini 使用某个已连接的自定义应用，可以将其移除。移除自定义应用时，也会从你的 Google 账号解除该 MCP 服务器的关联。

1. 在电脑上访问 [gemini.google.com](https://gemini.google.com)。
2. 在页面底部，依次点击「设置」![](images/img-01-1c0260.png) ![](images/img-02-bfcdbc.png) **已连接应用** ![](images/img-03-aa3481.png)。

   - 如果找不到「已连接应用」，请先点击 **Personal Intelligence** ![](images/img-02-bfcdbc.png) **已连接应用**。[了解 Personal Intelligence 和已连接应用](https://support.google.com/gemini/answer/16598406)。
3. 在「自定义应用」下，找到你想移除的自定义应用。
4. 点击 **更多详情** ![](images/img-02-bfcdbc.png) **移除应用**。
5. 按屏幕上的说明操作。

## 了解连接自定义 Connected Apps 的风险

自定义第三方模型上下文协议（Model Context Protocol，MCP）服务器，即自定义已连接应用，可扩展 Gemini 的能力。但重要的是，要了解相关风险和数据隐私方面的考量：

- **不受 Google 控制：** Google 不控制、不监控也不保护自定义第三方 MCP 服务器。你的数据离开 Gemini 并发送到自定义已连接应用后，将受该应用的隐私做法约束。目前，Gemini 对任何写入操作都要求手动确认，但 Gemini 也可能出错。因此，在连接之前，了解并信任该自定义第三方 MCP 服务器非常重要。
- **你的责任：** 由于自定义第三方 MCP 服务器在 Google 控制范围之外运行，我们建议你除非信任底层应用，否则不要连接它们。请密切监督这些服务器。在连接之前，务必确认你信任其提供方，并查看其隐私政策和服务条款，这些文件会说明他们将如何使用你的数据。
- **过度索取数据：** 自定义应用可能请求超出你请求严格所需的数据。其中可能包括你认为敏感的数据，因此请注意哪些数据正被写入这些服务器。
- **数据共享：** 当你使用自定义已连接应用时，Gemini 可能会分享你聊天中的信息以及其他可用来源的信息，例如 Connected Apps、Personal Intelligence、技能、任务和已登录的网站。这会带来意外泄露数据或账号被未经授权访问的风险，即使服务器并非恶意也是如此。

## 你可以如何保护自己的数据

- **仔细审查：** 确保你信任该第三方。连接前请阅读应用的隐私政策、服务条款和可用文档，以便了解其工作方式。
- **监控并移除：** 定期检查你的自定义 Connected Apps。如果你不再需要某个自定义已连接应用，请断开并将其从 Gemini 中移除，以撤销访问权限。

[了解 Google 如何通过 Google 账号关联帮助你安全地分享数据](https://support.google.com/accounts/answer/13867826)。

如需更多一般隐私信息，请查看 [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961#extensions)。

## 相关资源

- [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961)
- [在 Gemini 应用中管理你的任务和工作流](https://support.google.com/gemini/answer/17094507)
- [管理你的 Google 账号与其他开发者应用之间的关联](https://support.google.com/accounts/answer/13533235)
- [在 Gemini 中使用和管理 Connected Apps](https://support.google.com/gemini/answer/13695044)
