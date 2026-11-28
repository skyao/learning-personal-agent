---
title: "文档：推理钩子（Inference hooks）"
linkTitle: "文档：推理钩子"
date: 2026-11-05
originalTitle: "Grok Bot inference hooks"
sourceUrl: "https://docs.x.ai/grok-bot/inference-hooks"
altUrls: ["https://cursor.com/docs/grok-bot/inference-hooks"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-11
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：Validate Tool Calls 新配置默认开启（此前须待 Cursor 为团队开通后手动开启），一个响应的全部工具调用合为一个 tool_call 帧、一次裁决；「不覆盖」清单不再列语音通话"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：推理钩子把每个受管的 Grok Bot 模型请求签名后发给组织自己运行、或经安全厂商提供的 AI 安全服务器，服务器返回允许（allow）或拒绝（deny）。拒绝会终止该轮，成员看到拦截提示；检查失败按所选模式处理：影子模式（Shadow Mode，默认，只记录不拦截）、放行模式（Allow the Request，失败时放行）、拦截模式（Block the Request，失败时拦截）。开启 Validate Tool Calls 后（新配置默认开启，此前保存的配置为关闭），一个响应里的全部工具调用合成一个 tool_call 帧，由服务器一次裁决；Bot 对成员的回复和记忆等少数内部工具不入帧，工具运行后的实际效果也不检查。请求帧含完整对话，不含系统提示、工具定义和模型隐藏推理，也从不带秘密值；范围覆盖 Grok Bot 的子智能体、长对话摘要和例程，不含 Cloud Agents、编辑器内智能体等。该功能为 beta，面向所有 Enterprise 团队，Cursor 声明不保存发往钩子的内容。

**保留理由**：最细的一份企业侧安全控制文档，写明了哪些内容会被检查、哪些不会，以及失败时放行还是拦截，用来评估 Bot 的内容与工具调用审查边界。

---

Grok Bot 推理钩子

推理钩子（Inference hooks）把每个受管的 Grok Bot 模型请求发送给一个 AI 安全服务器——由你的组织自行运行，或通过安全厂商使用。Cursor 为每个请求签名，等待允许（allow）或拒绝（deny）的裁决，并在裁决为拒绝时终止该请求，因此你的策略可以在模型看到之前检查提示词（prompt）和 Grok Bot 收集的内容，也可以在模型请求的工具运行之前检查这些工具。Grok Bot 的其他控制项见 [Grok Bot 安全](https://docs.x.ai/grok-bot/security)。

> **Beta** 推理钩子处于 beta 阶段，面向所有 Enterprise 团队提供。团队管理员可以在控制台中设置。它们只覆盖 Grok Bot。见[覆盖范围](#coverage)。

## 工作方式

* **每个受管的模型请求都会被检查。** 在 Grok Bot 调用模型之前，Cursor 会向你的端点发送一个签名的 `prompt` 帧，内容为此前的对话，并让该请求等待，直到收到裁决或超时。一个轮次中多次调用模型时（例如在工具调用之间），每次调用发送一个帧。
* **由你的服务器决定。** `allow` 让请求发往模型。`deny` 终止请求、结束该轮，发送该消息的成员会看到[拦截提示](#what-members-see)。
* **出错时按你选的模式处理。** 当你的端点超时、返回错误，或返回的不是裁决时，由[模式](#modes)决定请求继续还是被拦截。出错永远不算作拒绝。
* **工具调用可以在运行前被检查。** 开启**验证工具调用（Validate Tool Calls）**后，每个模型响应中的工具调用会等待，Cursor 向你的端点发送一个签名的 `tool_call` 帧，覆盖这些调用的全部。`allow` 让它们运行。`deny` 把它们全部停止并结束该轮。见[工具调用帧](#tool-call-frames)。
* **有些调用从不先被检查。** Grok Bot 对成员的回复，以及记忆等少数内部工具，运行时没有 `tool_call` 帧，所以回复会在任何帧包含它之前就到达成员。关闭**验证工具调用**时，每个工具调用及其结果只在工具运行之后才出现在帧里，拒绝终止的是下一次模型调用，而不是已经发生的操作。

## 设置推理钩子

你必须是 Enterprise 团队的团队管理员。

1. **准备你的安全服务器。** 在安全厂商的控制台中创建推理钩子集成，或自建满足[端点要求](#endpoint-requirements)的服务器。设置对话框的**安全厂商（Security Vendor）**列表里有带设置清单的厂商预设。
2. **打开推理钩子。** 在 Cursor 控制台中选择团队，然后从 Grok Bot 页面的**安全与合规（Security & Compliance）**区域打开 [推理钩子](https://cursor.com/dashboard/bot/inference-hooks)。
3. **添加端点。** 点击**设置端点（Set Up Endpoint）**，选择你的厂商或**自定义端点（Custom Endpoint）**，输入**端点 URL（Endpoint URL）**以及你的服务器需要的**自定义请求头（Custom Headers）**，例如它的 API 密钥。保存时 Cursor 会检查该 URL。
4. **复制签名密钥。** 第一次保存并设置端点时会生成一个以 `whsec_` 开头的签名密钥，并且只显示一次。把它粘贴到厂商的 webhook 密钥字段，或你的服务器配置中，以便服务器验证每个请求。之后保存会沿用当前密钥，它不会再次显示；要换新密钥，请使用**请求签名（Request Signing）**下的**轮换密钥（Rotate Secret）**。
5. **测试连接。** 点击**测试连接（Test Connection）**。Cursor 会发送一个合成请求，开启**验证工具调用**时还会发送一个合成工具调用请求，并显示裁决或检查失败的原因。这里出现拒绝，说明你的策略会拦截测试提示词，请在开始强制执行前修正。
6. **从影子模式开始。** 新配置从**影子模式（Shadow Mode）**开始。打开**强制执行裁决（Enforce Verdicts）**才会开始发送。你的端点会收到每个受管的请求，拒绝会记录在审计日志中，但不会拦截任何请求。确认裁决看起来正确后，把**失败处理（Failure Handling）**下的**模式（Mode）**设为**放行请求（Allow the Request）**或**拦截请求（Block the Request）**。
7. **决定工具调用。** **强制执行裁决**下的**验证工具调用**会在每个模型响应的工具调用运行之前，把它们发送到你的端点。新配置默认开启；在该功能出现之前保存的配置为关闭。**强制执行裁决**关闭时它不生效。

设置变更大约一分钟内生效，已在处理中的请求按旧设置完成。

当端点已保存、**强制执行裁决**已开启、Grok Bot 在覆盖范围内时，无论哪种模式、放量比例为多少，Grok Bot 都会跳过它原本会在轮次开始前做的一些模型调用，因此回复可能开始得更慢。

### 端点要求

* **使用端口 443 上的 `https://` URL。** 主机必须可公开路由，并出示由公共证书颁发机构签发的证书。Cursor 拒绝私有地址、回环地址和运营商级 NAT 地址。
* **重定向和隧道不可用。** Cursor 不跟随重定向，遇到重定向按检查失败处理。反向隧道主机不被接受。
* **不要把密钥放在 URL 里。** URL 不能携带凭据、查询字符串或片段，因为管理员会以明文看到它。把凭据放在自定义请求头中，它们会加密存储。URL 最长 2,048 个字符。
* **对每个请求都返回裁决。** 返回 HTTP 200 和 JSON 裁决，测试连接也一样。见[裁决](#verdicts)。

### 自定义请求头

* **最多可以添加 16 个请求头。** 名称使用字母、数字和连字符，不能用下划线，最长 128 个字符。值为可打印 ASCII，最长 8,192 个字符。
* **值只能写入。** 保存后页面只显示请求头名称。改动任何一个请求头，都要重新输入全部值。
* **换新 URL 会清除已保存的值。** 请求头的值不会发给它们并未为之保存的端点。改动 URL 后，在**编辑（Edit）**中重新输入。在此之前，请求会不带这些值发出。
* **部分请求头由 Cursor 掌管。** 你不能添加 `Host`、`Cookie`、`User-Agent`、`Accept-Encoding`，`Transfer-Encoding` 这类连接请求头，`X-Real-IP` 这类客户端地址请求头，以及任何以 `Content-`、`Proxy-`、`X-Forwarded-`、`Webhook-` 或 `X-Cursor-` 开头的名称。

### 签名密钥

每个请求都带有 [Standard Webhooks](https://www.standardwebhooks.com) 请求头，你的服务器据此拒绝不是 Cursor 发来的内容：

| 请求头 | 值 |
| --- | --- |
| `webhook-id` | 该帧的 `request_id` |
| `webhook-timestamp` | Unix 时间，单位为秒 |
| `webhook-signature` | `v1,` 后接 `{webhook-id}.{webhook-timestamp}.{raw body}` 的 base64 HMAC-SHA256，密钥为密钥中 `whsec_` 之后部分经 base64 解码的结果 |

每个请求只带一个签名。要轮换密钥，点击**请求签名**下的**轮换密钥**。新密钥只显示一次，Cursor 大约一分钟内开始用它签名，因此在此之前请继续接受旧密钥。轮换算作一次设置变更，会影响[熔断器](#circuit-breaker)。

### 测试连接

测试连接会发送一个签名的 `prompt` 帧，其中 `source.application` 为 `config-test`，消息固定、不含用户内容，也没有成员、会话或模型。它用你已保存的密钥签名，并按已保存的裁决超时等待。从端点对话框运行时，它使用表单里的 URL 和请求头；从页面运行时，使用已保存的那些。

开启**验证工具调用**时，测试连接还会发送一个合成的 `tool_call` 帧，结果显示中每项检查各占一行，以 **Prompt request:** 或 **Tool call request:** 开头。

| 结果 | 含义 |
| --- | --- |
| 允许或拒绝 | 你的服务器返回了裁决。开始强制前先解决拒绝 |
| URL 被拒 | URL 不符合端点要求 |
| 私有或内部 IP | 主机不是可公开路由的地址 |
| 超时 | 在裁决超时内没有收到裁决 |
| 传输错误 | DNS、连接或 TLS 失败 |
| 非 200 状态 | 你的服务器返回了 200 以外的状态，包括重定向 |
| 响应无法解析 | 响应体不是 JSON 裁决、被压缩，或大于 64 KiB |
| 需要签名密钥 | 请先保存配置。保存时会生成密钥 |

## 模式

**强制执行裁决**控制是否发送。关闭时，Cursor 什么都不发，并保留你的设置。开启时，由**模式**决定检查无法完成时怎么办：

| 模式 | 遇到拒绝 | 检查失败时 |
| --- | --- | --- |
| **影子模式（Shadow Mode）**（默认） | 放行请求 | 放行请求 |
| **放行请求（Allow the Request）** | 拦截请求 | 未经检查地放行（失败放行） |
| **拦截请求（Block the Request）** | 拦截请求 | 拦截请求（失败拦截） |

在放行和拦截模式下，模型请求会等待裁决。影子模式下，Cursor 在相同时刻发送相同的提示词帧，但在后台进行：模型请求不等待，成员什么都看不到，拒绝和失败记录在审计日志中。负载很重时，Cursor 可能跳过某次影子提示词检查，被跳过的检查不写审计记录。

工具调用在每种模式下都等待裁决，包括影子模式，并使用与提示词相同的失败处理、裁决超时、放量和熔断器。影子模式仍然从不拦截它们，所以在**验证工具调用**开启时，影子模式会在每次工具调用前增加你服务器的延迟。

当你的服务器超时、返回 200 以外的状态、返回的不是 JSON 裁决或大于 64 KiB、返回 `allow` 或 `deny` 以外的 `action`，或无法连接时，检查即失败。大于 64 MiB 的帧也算失败。

一旦 Cursor 拿到你的设置，拦截模式会拦截每个无法完成的检查，包括原因在 Cursor 一侧的情况。如果 Cursor 完全无法加载你团队的推理钩子设置，它就无从知道你选的模式，请求会继续，审计日志将其记为失败放行，原因为 `config_unavailable`。

### 裁决超时

**裁决超时（Verdict Timeout (ms)）**接受 1 至 10,000 毫秒，默认 5,000。它覆盖整个交互：连接、TLS 握手、请求和响应。如果连接失败，Cursor 会在同一超时内重试一次，`webhook-id` 和签名相同，因此你可以按 `webhook-id` 去重。服务器一旦响应，Cursor 就不会重试。在超时之外，Cursor 自身的处理还会增加最多约半秒。

### 放量

**检查比例（Requests Inspected (%)）**让你在接入过程中只把一部分受管请求发送到端点。选择是粘性的，因此一个轮次背后的所有请求（包括子智能体）要么被检查，要么被跳过。比例之外的请求未经检查就继续，拦截模式下也是如此；0% 关闭检查。

### 熔断器

由你的服务器负责的持续失败会触发熔断器，例如超时、错误状态、TLS 错误和格式错误的裁决。DNS 和连接错误、Cursor 拒绝的 URL，以及超过 64 MiB 的帧算作失败，但从不触发熔断。

* **熔断期间，Cursor 停止发送。** 你的模式适用于每个受管请求：拦截模式全部拦截，放行和影子模式让它们未经检查地通过。审计日志每次熔断记录一条 `inference_hooks_circuit_breaker_tripped` 事件，熔断期间不记录逐请求事件。
* **自动恢复。** 从熔断后 10 分钟起，Cursor 定期向你的服务器发送测试连接请求。允许或拒绝都会重置熔断器。
* **任何设置变更都会停止自动恢复。** 这包括轮换密钥。端点修好后，点击**重置（Reset）**，或把**强制执行裁决**关掉再打开。

### Cursor 暂停

紧急情况下，Cursor 可以为一个团队或所有人暂停推理钩子。暂停期间 Cursor 不发送帧，受管请求继续，审计日志把其中大部分记为失败放行，原因为 `kill_switch`。测试连接会显示「推理钩子已被 Cursor 暂时暂停（Inference hooks are temporarily paused by Cursor.）」

## 成员看到什么

当你的服务器拒绝一个请求时，Grok Bot 桌面应用和手机应用会在发送被拦截消息的成员与 Bot 的对话中，向该成员显示拦截提示。在手机上，提示位于消息框上方。它显示：

* 标题**已被你所在组织的策略拦截**。
* 你服务器的 `deny_reason`，随后是你设置的**拦截消息（Blocked Message）**。
* 带**编辑（Edit）**按钮和**重置（Reset）**按钮的说明。**编辑**把被拦截的消息从对话中撤回，并把其文字放进消息框（除非成员已经在那里写了草稿），以便换一条发送。**重置**清空对话。手机应用和较新版本的桌面应用会先请成员确认。当 Cursor 无法把对话回滚到被拦截消息之前时，只显示**重置**。

**拦截消息**最多接受 500 个字符，默认为「你所在组织的安全策略拦截了此请求。」（Your organization's security policy blocked this request.）关闭它则只显示你服务器的 `deny_reason`。用它告诉成员下一步怎么做，例如联系谁。

重置之后，Bot 不再看到该对话中更早的消息，并停止它为这个对话运行的背景助手。它启动的其他工作（例如云智能体和后台命令）继续运行，并可以回报结果。它的记忆、文件、例程和设置都会保留。编辑会把对话回滚到被拦截消息之前。两者都不会撤销 Bot 已经执行的操作，例如它写过的文件。

如果重置后对话立刻又被拦截，提示中没有按钮。它会说明被拦截的内容可能在 Bot 的记忆或文件中，请成员在那里删除或向管理员求助。

在拦截模式下检查失败时，桌面应用显示**你所在组织的策略检查不可用**，以及「你的组织要求模型响应前先做策略检查，而检查没有完成。请稍后再试，如果持续发生请联系管理员。」手机应用显示「你所在组织的策略检查不可用。请稍后再试，如果持续发生请联系管理员。」你设置的拦截消息不显示，也没有编辑或重置。

其他位置的显示更少：

* **Team Bots 只通知发送者。** 在 Team Bot 中，提示及其按钮只发给发送被拦截消息的队友，显示在其与 Bot 的单独聊天中，编辑或重置只改动那个聊天。Bot 的所有者看不到拒绝原因和你设置的拦截消息。房间和群聊没有编辑或重置按钮。
* **Slack 在对话中回复。** Bot 回答「你所在组织的策略拦截了此对话，因此我无法回复」，在一对一私信中还会引用拒绝原因和你设置的拦截消息，而频道线程和群组私信从不显示这些。回复提供**删除被拦截的消息（Remove blocked message）**（作用同编辑）和**重置**（会先请求确认），当 Cursor 无法回滚对话时只提供**重置**。任何能使用该 Bot 并已关联 Cursor 账号的人都可以点击。被删除的消息在 Slack 中仍然可见，但 Bot 不再看到它。重置后立刻又被拦截时没有按钮，拦截模式下检查失败时得到的是 Bot 的通用错误回复，而不是策略提示。
* **其他地方，手机应用只显示普通失败。** 在群聊和非成员本人的对话中，它显示「Bot 回复失败」，以及「已被你所在组织的策略拦截。请发送其他消息，如果持续发生请联系管理员。」，不显示拒绝原因、你设置的拦截消息和按钮。
* **其他 Cursor 应用只显示标题。**
* **较旧的桌面版本没有按钮。** 视版本而定，提示会显示拒绝原因和你设置的拦截消息，加上说明「请发送其他消息，如果持续发生请开新对话」，或只显示「已被你所在组织的策略拦截。请发送其他消息，如果持续发生请联系管理员。」
* **背景助手停止时不显示提示。** 当 Grok Bot 启动的助手被拦截时，Bot 只知道你所在组织的策略阻止了它，拿不到拒绝原因。
* **例程停止并记录拦截。** Cursor 控制台中的运行历史显示**已被你所在组织的策略拦截**，拦截模式下检查失败则显示**你所在组织的策略检查不可用**，附固定说明，不含拒绝原因。Grok Bot 应用的例程列表只显示运行失败。
* **邮件、Linear 及其他已连接的渠道得不到回复。**

被拦截的消息会留在对话中，直到有人撤回它或重置对话。在此之前，Grok Bot 每次后续请求都会带上它，你的服务器因此每次都要重新判断它。扫描整段对话的策略会一直拒绝该对话。只判断最新用户消息的策略，在成员改发其他内容后就会放行。

请求被允许时，或处于影子模式时，成员什么都看不到。影子模式也会把他们的对话发送到你的端点，所以在开启**强制执行裁决**之前，请告知成员你的组织会检查 Grok Bot 请求。

## 覆盖范围

**覆盖：** 你团队成员 Grok Bot 对话背后的模型请求。这包括一个轮次的每一步、子智能体、Grok Bot 为长对话写的摘要，以及例程。Team Bot 或房间遵循其团队的推理钩子。个人 Bot 遵循其所有者所选团队的推理钩子。每个请求都有自己的帧，包含此前的对话。

**不覆盖：**

* **模型响应的文本不被单独检查。** `tool_call` 帧会随工具调用带上响应的文本，但没有被检查的工具调用的响应不发送帧。见[工作方式](#how-it-works)。
* **请求中不属于对话的部分不发送。** 系统提示、工具定义和模型的隐藏推理从不发到你的端点，Cursor 还会略去它为模型添加的大部分文本，例如提醒和时间戳。
* **辅助性模型调用不发送。** 这些调用支持对话而不是延续对话，例如写聊天标题、Auto Review 和保存记忆。
* **其他 Cursor 功能不在覆盖范围内。** 包括 Cloud Agents、编辑器内的智能体、CLI、Agent SDK、Tab、嵌入和本地模型。
* **动作在运行时不被检查。** 开启**验证工具调用**时，你的端点在每个工具调用开始前裁决它，但不裁决工具随后做什么：命令、已连接应用的操作，以及成员 Grok Bot 计算机上的网络流量，只有在它们的输出作为工具结果回到模型、出现在后续帧中时，才会到达你的端点。用[网络策略](https://docs.x.ai/grok-bot/security#network-policy)和 [Auto Review](https://docs.x.ai/grok-bot/security#approvals-and-auto-review) 控制动作。

## 请求格式

Cursor 以 HTTPS `POST` 发送每个帧，请求体为紧凑的 JSON。请求头名称小写。

| 请求头 | 值 |
| --- | --- |
| `content-type` | `application/json` |
| `user-agent` | `cursor-inference-hooks/1` |
| `accept-encoding` | `identity` |
| `webhook-id`、`webhook-timestamp`、`webhook-signature` | 见[签名密钥](#signing-secret) |
| 你的自定义请求头 | 按保存的内容 |

`host` 和 `content-length` 等标准请求头也随每个请求发送。

```json
{
  "type": "prompt",
  "request_id": "req_6b1f0c2e-4d7a-4f1e-9a53-2c8d7e41b9a0",
  "tenant_id": "team_4mQvT8yLcN2pR6",
  "actor": {
    "type": "user",
    "id": "user_8hJw3KzP5sXq1V7nB2cF9mD4tR",
    "email_address": null
  },
  "source": { "application": "grok-bot" },
  "session_id": "3f2c9a71-58e4-4b0d-9c6a-0d1e7b25a4f8",
  "model": "<Cursor model identifier>",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Check the Q3 renewals sheet for accounts at risk and draft a note to the account team."
        },
        {
          "type": "attachment",
          "file_name": null,
          "media_type": "image/png",
          "size_bytes": 184320,
          "text": null
        }
      ]
    }
  ],
  "metadata": {}
}
```

### 帧字段

| 字段 | 值 |
| --- | --- |
| `type` | `prompt`，或[工具调用帧](#tool-call-frames)的 `tool_call` |
| `request_id` | 该请求的唯一 ID。与 `webhook-id` 及审计日志的 `request_id` 一致 |
| `tenant_id` | 你团队的不透明 ID |
| `actor.type` | 恒为 `user` |
| `actor.id` | 发送消息的成员或团队服务账号的不透明 ID。未关联 Cursor 账号的 Slack 发送者为 null |
| `actor.email_address` | 恒为 null |
| `source.application` | `grok-bot`；测试连接和熔断器恢复检查为 `config-test` |
| `session_id` | Bot 的不透明 ID，跨其聊天和成员共享，因此不标识某一段对话 |
| `model` | Cursor 模型标识符。用于报表，不要用于允许列表 |
| `messages` | 此前的对话。见[消息](#messages) |
| `metadata` | 恒为空 |

### 消息

* **角色为 `user` 和 `assistant`。** 工具结果位于 `user` 之下。
* **块为 `text`、`tool_use`、`tool_result` 和 `attachment`。** `tool_use` 块标明工具并持有其 `input`，对应的 `tool_result` 持有输出。Grok Bot 给模型的上下文（例如规则、共享记忆和它可用的已连接应用）通常出现在 `attachment` 块的 `text` 中。图片是带媒体类型和大小的 `attachment`，但不含字节或 URL。
* **每一帧都持有到此刻为止的整段对话。** 帧不是增量，所以每帧都会再次带上更早的消息。长对话中，Grok Bot 写的摘要会取代更早的消息。
* **对成员的回复是工具调用。** Grok Bot 通过一个工具发送成员读到的内容，所以它的回复出现在 `tool_use` 的 input 中，而不在 assistant 的 `text` 中。
* **Cursor 从不添加密钥值。** 上下文可以命名和描述 Bot 可用的密钥，但从不包含它们的值。

### 工具调用帧

开启**验证工具调用**时，模型响应请求使用工具后、其中任何工具运行之前，Cursor 会发送一个 `tool_call` 帧。它的外层结构和请求头与 `prompt` 帧相同，有自己的 `request_id`，`session_id` 与该对话的提示词帧相同，`type` 为 `tool_call`。

* **`messages` 只持有最新的 assistant 消息。** 其中可见的 `text` 块和 `tool_use` 块按模型书写的顺序出现。一个裁决覆盖该帧中的所有调用。
* **`tool_name` 标明实际运行的工具。** 别名会被解析，所以 `bash` 读作 `Shell`。对已连接应用和 MCP 服务器的调用保留模型所调的元工具名称，例如 `CallMcpTool` 或 `CallDynamicTool`，服务器在 `tool_info.toolset_name` 中。提示词帧按模型书写的样子保留每个调用；用 `tool_use` 块的 `id` 匹配两者。
* **`input` 持有工具运行所用的参数。**
* **`tool_info.type` 说明工具在哪里运行。** `platform` 是 Grok Bot 内置工具，带 `tool_type`。`application` 在 Cursor 后端运行。`third_party` 在远程服务上运行，已知时带 `origin`（含其 scheme、host 和 port）；只有当该服务自行连接时 `verified_origin` 才为 true。`client` 在 Cursor 后端之外的计算机上运行，可能带 `tool_type`。可选字段不设置，而不是设为 null。把名称当作标签，而不是信任边界。
* **有些调用被略去。** 对成员的回复、记忆工具、技能加载器、插件和服务器查找、对话记录工具，以及工具发现，从不出现。如果响应中只有被略去的调用，则不发送帧。
* **计算机使用所用的浏览器工具逐个检查。** 每个工具在运行前各自发送只含一个调用的帧。
* **子智能体使用父级的会话。** 它们的响应以父对话的 `session_id` 成帧。

被拒绝时，该轮以同样的[拦截提示](#what-members-see)结束，响应中的每个调用得到结果「在运行前已被你所在组织的策略拦截（Blocked by your organization's policy before it ran）」。如果 Cursor 无法及时加载你的设置，调用会在没有帧的情况下运行，设置加载后审计日志把它们记为失败放行，原因为 `config_unavailable`。

### 为这些帧编写策略

* **验证签名。** 不要依赖 User-Agent 或源 IP。如果推理钩子页面在**请求签名**下列出**源 IP 范围（Source IP Ranges）**，你也可以把它们加入允许列表。
* **把 ID 当作不透明字符串。** 不要解析 `tenant_id` 或 `actor.id`。按 `actor.id` 映射成员，因为帧不携带邮箱。
* **把 `source.application` 当作开放集合。** 覆盖范围扩大时 Cursor 会增加取值。它是提示性的，不是安全控制。
* **在 `tool_call` 帧中匹配工具名称。** 在那里拒绝 `Shell` 的策略也能拦住 `bash`，而提示词帧的记录并非如此。
* **扫描每种块类型，而不只是 `text`。** 上下文通常出现在 attachment 的 `text` 中，对成员的回复和已连接应用的调用出现在 `tool_use` 的 input 中。
* **不要依赖 `tool_result.is_error`。** 大多数失败的工具调用它也是 `false`。

### 裁决

以 HTTP 200 和一个 JSON 对象作答：

```json
{
  "action": "deny",
  "deny_reason": "This message contains a customer account number. Remove it and try again.",
  "reference_id": "policy-7f3c21"
}
```

* **`action`** 为 `allow` 或 `deny`。其他任何值都算检查失败。
* **`deny_reason`** 会在拦截提示中显示给发送该消息的成员。Cursor 会截断到 500 个字符。
* **`reference_id`** 是你对该决定的标识符，记录在 Cursor 审计日志中。最多 50 个字符，取自 `A-Z`、`a-z`、`0-9` 和 `.`、`_`、`:`、`/`、`-`。格式错误的值会被丢弃，拒绝仍然生效。
* **未知字段被忽略。** Cursor 最多读取 64 KiB 的未压缩内容，并忽略 cookie。

对来自测试连接和熔断器恢复的 `config-test` 帧也要返回裁决，并把它们排除在成员流量报表之外。

## 审计日志

推理钩子的活动出现在你团队的[审计日志](https://cursor.com/docs/enterprise/compliance-and-monitoring#audit-logs)中。载荷只带标识符和代码，从不含提示词内容、拒绝原因、签名密钥或请求头值。被允许的请求不写事件。

| `event_type` | 触发时机 | 字段 |
| --- | --- | --- |
| `inference_hooks_config_updated` | 管理员保存设置或重置熔断器，或自动恢复重置了它 | `action`（`update`、`reset_circuit_breaker`、`circuit_breaker_recovered`）、`changed_fields`、`enforce_verdicts`、`mode`、`endpoint_host`、`verdict_timeout_ms`、`rollout_percent`、`enabled_surfaces`、`config_version` |
| `inference_hooks_signing_secret_generated` | 第一次保存并设置端点时生成签名密钥，或管理员轮换它 | `action`（`generate_signing_secret`、`rotate_signing_secret`）、`changed_fields`（恒为空）、`enforce_verdicts`、`mode`、`endpoint_host`、`verdict_timeout_ms`、`rollout_percent`、`enabled_surfaces`、`config_version` |
| `inference_hooks_request_denied` | 你的服务器拒绝了请求 | `request_id`、`reference_id`、`source_application`、`session_id`、`model`、`actor_id`、`mode`、`enforced`（影子模式中为 `false`） |
| `inference_hooks_request_failed_open` | 请求在没有裁决的情况下继续：放行或影子模式下检查失败、Cursor 暂停，或 Cursor 无法加载设置 | `request_id`、`reason`、`source_application`、`session_id`、`model`、`actor_id`、`mode`、`status_code`（未收到响应时为 `0`） |
| `inference_hooks_request_failed_closed` | 拦截模式下检查失败，请求被拦截 | `request_id`、`reason`、`source_application`、`session_id`、`model`、`actor_id`、`mode`、`status_code`（未收到响应时为 `0`） |
| `inference_hooks_circuit_breaker_tripped` | 持续失败触发了熔断器 | `config_version`、`mode`、`failure_count`、`window_seconds`、`last_failure_kind` |

在 `inference_hooks_signing_secret_generated` 中，设置字段显示变更后的状态。轮换会提升 `config_version`。首次生成密钥会与同一次保存产生的 `inference_hooks_config_updated` 事件共享它。

Cursor 在每种模式下都记录请求失败，放行和影子模式记为失败放行，拦截模式记为失败拦截，也记录熔断器的自动恢复。失败放行和失败拦截事件上的 `reason` 是失败原因（`timeout`、`non_200_status`、`unparseable_response`、`oversized_response`、`invalid_action`、`transport_error`、`tls_error`、`endpoint_rejected`、`frame_too_large`）、Cursor 一侧的原因（`endpoint_not_allowlisted`、`config_unavailable`），或仅对失败放行而言的暂停（`kill_switch`）。基于这些事件名和 `reason` 值编写 SIEM 规则。

被拒绝和失败事件上的 `request_id` 与帧的 `request_id` 及 `webhook-id` 一致，因此可以把厂商的记录与审计日志关联起来。

当你的团队可以使用工具调用检查时，被拒绝和失败事件的载荷还会带一个 `event_type` 字段，`prompt` 或 `tool_call`，控制台在工具调用行标注**（Tool Calls）**。

推理钩子页面还显示端点健康状况：状态、裁决延迟、每分钟失败数、24 小时内的拦截率，以及最近错误及其类型和状态码。开启**验证工具调用**时，它把数字拆成**提示词（Prompts）**和**工具调用（Tool Calls）**两行，某项数字拿不到时显示**未报告（Not reported）**。它的数字不覆盖所有流量，因此可能低于厂商的计数。

## 隐私与隐私模式

* **Cursor 不保留发给钩子的内容。** Cursor 通过 HTTPS 把每个帧发送到你的端点，收到裁决后即丢弃。帧内容不写入 Cursor 的数据库、日志、指标或追踪。
* **端点归你，保留策略也归你。** 端点属于你的组织或你的安全厂商。它存什么、存在哪里、存多久，取决于你的配置以及你与该厂商的协议。Cursor 不控制这些数据。
* **隐私模式不变。** 模型请求本身按你团队的隐私模式设置处理，与没有钩子时完全一样，钩子不会增加它的副本。无论隐私模式如何，推理钩子对每个受管成员都运行，因为是你组织的管理员指示 Cursor 把这些请求发送到你自己的端点。
* **帧字段只用不透明 ID 标识人。** `actor.email_address` 恒为 null。

Cursor 只保留运行该功能、向你展示发生了什么所需的内容：

* **你的设置，密钥加密。** 请求头值和签名密钥加密存储。
* **只含标识符和代码的审计日志事件。** 它们包含你服务器的 `reference_id`，如[审计日志](#audit-log)所列。
* **不含内容的健康数据。** 它们只含计数、延迟，以及最近错误的类型和状态码。
* **拦截提示，随被拦截的轮次加密。** 你服务器的 `deny_reason` 和你设置的拦截消息，与 Grok Bot 对该被拦截轮次的记录一起加密存储。

## 故障排查

### 为什么 Grok Bot 页面上看不到推理钩子？

该页面只对 Enterprise 团队的团队管理员显示，并显示控制台中选中的团队。请确认选对了团队。如果页面说「推理钩子尚不可用（Inference hooks aren't available yet）」，请联系你的客户经理。

### 为什么我的端点 URL 被拒？

检查[端点要求](#endpoint-requirements)。常见原因是端口不是 443、URL 中有查询字符串或凭据、使用隧道主机，或主机解析到私有地址。

### 为什么测试连接说需要签名密钥？

Cursor 在第一次保存并设置端点时生成密钥。先保存端点，把密钥复制到厂商控制台，然后再次测试。

### 为什么我的服务器拒绝 Cursor 的请求？

大多数拒绝是签名或凭据不匹配。把当前签名密钥粘贴到你的服务器，如果你的验证器需要，连同 `whsec_` 前缀一起，并确认它按标准 base64 解码密钥。确认 API 密钥请求头已保存。如果你改过端点 URL，请重新输入请求头的值。轮换之后，Cursor 大约一分钟内切换到新密钥。

### 为什么测试连接返回拒绝？

你服务器的策略拒绝了 Cursor 的合成测试提示词。在放行或拦截模式下，这样的策略也会拦截成员。请在开启强制执行之前调整该策略或其默认动作。

### 为什么请求会超时？

你的服务器耗时超过了裁决超时。检查健康面板中的裁决延迟和厂商报表。更轻量的扫描配置响应更快。你可以把**裁决超时（Verdict Timeout (ms)）**提高到 10,000。

### 为什么我的端点收不到请求？

检查端点已保存、**强制执行裁决**已开启、**覆盖范围**包含 Grok Bot、**检查比例**大于 0，且熔断器未触发。只有你团队成员的 Grok Bot 对话在覆盖范围内。如果测试连接报告推理钩子已暂停，说明 Cursor 暂停了它们。

### 为什么成员看到策略检查不可用？

你处于拦截模式且检查失败，或熔断器触发了。查看推理钩子页面上的**最近错误（Recent Errors）**。要在修复端点期间让成员继续工作，请切换到**放行请求**。

### 熔断器触发了，怎么恢复？

修好端点，运行测试连接，然后点击**重置**。任何设置变更后自动恢复都会停止，所以如果你在熔断后编辑过任何内容，不要等它。

### 为什么一次拦截之后，对话中的每条消息都被拦截？

被拦截的消息留在对话中，会随每次后续请求发送到你的服务器，所以扫描整段对话的策略会逐一拒绝它们。在桌面或手机应用的拦截提示上选**编辑**，或在 Slack 中 Bot 回复上选**删除被拦截的消息**，撤回该消息并改发其他内容。**重置**则清空对话。如果重置后对话立刻又被拦截，你的策略匹配到的内容很可能在 Bot 的记忆或文件中，请在那里删除。只判断最新用户消息的策略，在成员改发其他内容后会让对话继续。

### 为什么审计日志筛选器里看不到推理钩子事件？

只有为你的团队启用推理钩子时，这些事件类型才出现在筛选器中。已记录的事件仍会显示在日志里。
