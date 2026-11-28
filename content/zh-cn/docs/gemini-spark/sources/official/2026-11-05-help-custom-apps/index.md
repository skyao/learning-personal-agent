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
collectedAt: 2026-11-28
updatedAt: 2026-11-28
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）。2026-10 Spark 改名为 Task 后，帮助页的用词已改为 tasks / task mode；2026-11-28 发现原文更新：「What you need」中的「Keep Activity」改称「History」，其余未变；按规则覆盖原文存档。原文存档已覆盖，旧译文删除，已重新翻译"
tags: [连接器, 安全, 隐私]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的默认（Computer）视图；页面中的界面小图标已下载。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：可以用 MCP 服务器地址把个人或第三方应用接入 Gemini，在任务中构建定制工作流，或在聊天中快速执行动作。条件是年满 18 岁且在美国、使用个人 Google 账号、开启 History（11 月前称 Keep Activity），MCP 服务器须符合标准规范；目前只支持英语。页面提醒，使用自定义应用时 Gemini 可能把聊天内容以及 Connected Apps、Personal Intelligence、技能、任务和已登录网站中的信息分享给该应用，并说明怎样断开、解除关联和删除。

**保留理由**：自定义 MCP 的准入条件和数据分享范围，是 Spark/Task 开放连接能力的边界。

---

你可以接入自己的个人应用或第三方应用，在任务中构建高度定制的工作流，或在聊天中快速执行动作。做法是在 Gemini 网页应用里，用应用的模型上下文协议（Model Context Protocol, MCP）服务器地址添加一个自定义应用。连接之后，你可以在 Gemini 移动应用和 Gemini 网页应用中同时使用这个自定义已连接应用。

**面向开发者：** 你可以用新的 [Connected Apps Platform](https://developers.google.com/connected-apps)（已连接应用平台）把你的应用和 MCP 服务器接入 Google 的 agent 类产品，例如 Gemini Apps。你也可以用 [Gemini Developer Mode](https://developers.google.com/connected-apps/mcp/dev-mode)（Gemini 开发者模式）调试、校验 schema 并测试你的自定义应用。

## 需要什么

要把自定义应用连接到 Gemini Apps，你必须：

- **年满 18 岁，且在美国。**
- **用个人 Google 账号登录 Gemini 应用。** 目前，用工作或学校 Google 账号登录时无法使用此功能。[了解如何登录 Gemini Apps](https://support.google.com/gemini/answer/13278668)。
- **开启 [History](https://myactivity.google.com/product/gemini)（历史记录）。** 关闭此设置时无法使用自定义应用。
- **拥有该自定义应用的 MCP 服务器地址。** MCP 服务器必须符合标准的 MCP 规范。

**重要：** 目前，自定义已连接应用：

- 仅支持英语。
- 仅在 Gemini 移动应用和 [gemini.google.com](https://gemini.google.com) 上的 Gemini 网页应用提供。

## 连接自定义应用之前

Google 不控制、不监控、也不为第三方 MCP 服务器提供安全保护。你有责任监管 MCP 服务器。在把它连接到 Gemini Apps 之前，请确保你了解该 MCP 服务器支持哪些操作，并信任其提供方。

[进一步了解连接自定义应用的风险](#risks)。

## 连接自定义应用

**重要：** 你只能在 Gemini 网页应用中连接自定义应用。连接之后，它们在 Gemini 移动应用和 Gemini 网页应用中都可使用。

你可以在[已连接应用设置](https://gemini.google.com/apps)中链接自定义应用的 MCP 服务器来添加它。

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部，依次点击「设置」![](images/img-01-1c0260.png) ![然后](images/img-02-bfcdbc.png) **Connected Apps**（已连接应用）![](images/img-03-aa3481.png)。

   - 如果找不到「Connected Apps」，先点击 **Personal Intelligence**（个人智能）![然后](images/img-02-bfcdbc.png) **Connected Apps**。[了解 Personal Intelligence 与 Connected Apps](https://support.google.com/gemini/answer/16598406)。
3. 在「Custom apps」（自定义应用）下，找到「Add a custom app link to get started」（添加自定义应用链接以开始）输入框；如果已经连接过自定义应用，则点击 **Add a custom app**（添加自定义应用）![](images/img-04-e8b4c8.png)。
4. 输入该应用的 MCP 服务器地址。
   - 如果服务器不支持动态客户端注册（Dynamic Client Registration），在「Advanced features」（高级功能）旁边点击 **Show more**（显示更多），然后输入你的凭据。
5. 点击 **Next**（下一步）。
6. 按屏幕上的说明操作。

**提示：**

- 要确保 Gemini 在处理某个提示时使用你连接的定制应用，输入 `@` 并选择该自定义应用。
- 要调试、校验 schema 并测试你的自定义应用，可以试试 [Gemini Developer Mode](https://gemini.google.com/devmode)（Gemini 开发者模式）。[进一步了解 Gemini Developer Mode](https://developers.google.com/connected-apps/mcp/dev-mode)。

## 断开自定义应用

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部，依次点击「设置」![](images/img-01-1c0260.png) ![然后](images/img-02-bfcdbc.png) **Connected Apps**（已连接应用）![](images/img-03-aa3481.png)。

   - 如果找不到「Connected Apps」，先点击 **Personal Intelligence**（个人智能）![然后](images/img-02-bfcdbc.png) **Connected Apps**。[了解 Personal Intelligence 与 Connected Apps](https://support.google.com/gemini/answer/16598406)。
3. 在「Custom apps」（自定义应用）下，找到你想断开的应用并把它关闭 ![](images/img-05-923460.png)。
4. 按屏幕上的说明操作。

## 从 Google 账号解除 MCP 服务器的关联

你可以在[已连接应用设置](https://gemini.google.com/apps)中把 MCP 服务器从 Google 账号解除关联，并撤销其权限。这也会断开该自定义应用，使 Gemini 无法使用它，但不会把它从你的已连接应用设置中移除。你随时可以重新链接 MCP 服务器来重新连接该自定义应用。

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部，依次点击「设置」![](images/img-01-1c0260.png) ![然后](images/img-02-bfcdbc.png) **Connected Apps**（已连接应用）![](images/img-03-aa3481.png)。

   - 如果找不到「Connected Apps」，先点击 **Personal Intelligence**（个人智能）![然后](images/img-02-bfcdbc.png) **Connected Apps**。[了解 Personal Intelligence 与 Connected Apps](https://support.google.com/gemini/answer/16598406)。
3. 在「Custom apps」（自定义应用）下，找到你想断开的自定义应用。
4. 依次点击 **More details**（更多详情）![然后](images/img-02-bfcdbc.png) **Disconnect**（断开连接）。

**提示：** 你也可以从 [Google 账号的「已关联的应用」页面](https://myaccount.google.com/linkedapps)解除 MCP 服务器的关联。[了解如何管理已关联的应用](https://support.google.com/accounts/answer/13533235#link_account)。

## 移除自定义已连接应用

如果你不再想让 Gemini 使用某个自定义已连接应用，可以把它移除。移除自定义应用时，也会把 MCP 服务器从你的 Google 账号解除关联。

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部，依次点击「设置」![](images/img-01-1c0260.png) ![然后](images/img-02-bfcdbc.png) **Connected Apps**（已连接应用）![](images/img-03-aa3481.png)。

   - 如果找不到「Connected Apps」，先点击 **Personal Intelligence**（个人智能）![然后](images/img-02-bfcdbc.png) **Connected Apps**。[了解 Personal Intelligence 与 Connected Apps](https://support.google.com/gemini/answer/16598406)。
3. 在「Custom apps」（自定义应用）下，找到你想移除的自定义应用。
4. 依次点击 **More details**（更多详情）![然后](images/img-02-bfcdbc.png) **Remove app**（移除应用）。
5. 按屏幕上的说明操作。

## 了解连接自定义已连接应用的风险

自定义的第三方模型上下文协议（MCP）服务器，也就是自定义已连接应用，能扩展 Gemini 的能力。但重要的是要了解随之而来的风险和数据隐私方面的考量：

- **不在 Google 控制之内：** Google 不控制、不监控、也不为自定义第三方 MCP 服务器提供安全保护。你的数据离开 Gemini、发送到自定义已连接应用后，就受该应用的隐私做法约束。目前，Gemini 对任何写入操作都要求手动确认，但 Gemini 也可能出错。正因如此，在连接之前了解并信任该自定义第三方 MCP 服务器非常重要。
- **是你的责任：** 由于自定义第三方 MCP 服务器在 Google 控制之外运行，我们建议你除非信任其底层应用，否则不要连接。请密切监管这些服务器。连接之前，务必确认你信任其提供方，并查阅其隐私政策和服务条款，这些文件解释了他们会如何使用你的数据。
- **过度索取数据：** 自定义应用可能索取超出你的请求所严格需要的数据，其中可能包括你认为敏感的数据，因此请留意有哪些数据被写入这些服务器。
- **数据分享：** 当你使用自定义已连接应用时，Gemini 可能分享你聊天中的信息以及其他可用的来源，例如已连接应用、Personal Intelligence、技能、任务和已登录的网站。这会带来数据意外泄露或账号被未授权访问的风险，即使服务器本身并无恶意也是如此。

## 你可以如何保护自己的数据

- **仔细审查：** 确保你信任该第三方。连接之前阅读应用的隐私政策、服务条款和可获得的文档，以便了解它如何运作。
- **监控并移除：** 定期检查你的自定义已连接应用。如果你不再需要某个自定义已连接应用，请断开并从 Gemini 中移除它，以撤销访问权限。

[了解 Google 如何通过 Google 账号关联帮助你安全地分享数据](https://support.google.com/accounts/answer/13867826)。

更多一般性的隐私信息，请参阅 [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961#extensions)（Gemini Apps 隐私中心）。

## 相关资源

- [Gemini Apps 隐私中心](https://support.google.com/gemini/answer/13594961)
- [在 Gemini Apps 中管理你的任务与工作流](https://support.google.com/gemini/answer/17094507)
- [管理你的 Google 账号与其他开发者应用之间的关联](https://support.google.com/accounts/answer/13533235)
- [在 Gemini 中使用和管理已连接应用](https://support.google.com/gemini/answer/13695044)
