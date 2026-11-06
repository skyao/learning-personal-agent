---
title: "文档：推理钩子（Inference hooks）"
linkTitle: "文档：推理钩子"
date: 2026-11-05
originalTitle: "Grok Bot inference hooks"
sourceUrl: "https://cursor.com/docs/grok-bot/inference-hooks"
altUrls: ["https://docs.x.ai/grok-bot/inference-hooks"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：推理钩子把每个受管的 Grok Bot 模型请求签名后发给组织自己运行、或经安全厂商提供的 AI 安全服务器，服务器返回允许（allow）或拒绝（deny）。拒绝会终止该轮，成员看到拦截提示；检查失败按所选模式处理：影子模式（Shadow，默认，只记录不拦截）、放行模式（失败时放行）、拦截模式（失败时拦截）。开启 Validate Tool Calls 后，服务器还会在工具调用运行前检查，但不检查工具运行后的实际效果，也不检查 Bot 回复成员的内容。请求帧含完整对话，不含系统提示和模型隐藏推理，也永远不带秘密值；范围覆盖 Grok Bot 的子智能体、长对话摘要和例程，不含云端智能体、语音通话等。该功能为 beta，面向所有 Enterprise 团队，Cursor 声明不保存发往钩子的内容。

**保留理由**：最细的一份企业侧安全控制文档，写明了哪些内容会被检查、哪些不会，以及失败时放行还是拦截，用来评估 Bot 的内容与工具调用审查边界。

---

推理钩子（Inference hooks）会把每个受管的 Grok Bot 模型请求发送到组织自行运行、或通过安全厂商使用的 AI 安全服务器。Cursor 为每个请求签名，等待允许（allow）或拒绝（deny）的裁决，并在拒绝时停止该请求，因此你的策略可以在模型看到提示和 Grok Bot 收集的内容之前对其进行检查。开启[校验工具调用（Validate Tool Calls）](#validate-tool-calls)后，服务器还会在每个响应的工具调用运行之前对其进行检查。关于 Grok Bot 的其他控制措施，见 [Grok Bot security](https://cursor.com/docs/grok-bot/security)。

Beta

推理钩子处于 Beta 阶段，面向所有 Enterprise 团队提供。团队管理员可以在仪表盘中设置。它们只覆盖 Grok Bot。见[覆盖范围](#coverage)。

## 工作方式

- **每个受管的模型请求都会被检查。** 在 Grok Bot 调用模型之前，Cursor 会向你的端点发送一个带签名的 `prompt` 帧，其中包含到目前为止的对话，并暂缓该请求，直到收到裁决或超时。一轮中如果多次调用模型（例如在工具调用之间），每次调用都会发送一个帧。
- **由你的服务器决定。** `allow` 让请求发往模型。`deny` 停止请求、结束该轮，发送消息的成员会看到[拦截提示](#what-members-see)。
- **失败按你的模式处理。** 当端点超时、返回错误，或返回裁决之外的内容时，由[模式](#modes)决定请求是继续还是被拦截。失败永远不算拒绝。
- **只有在开启校验工具调用时，工具调用才会在运行前被检查。** `prompt` 帧携带的是即将发给模型的内容，因此工具调用及其结果只有在该工具运行之后才会出现在其中。[校验工具调用](#validate-tool-calls)会增加一个 `tool_call` 帧，由你的服务器在调用运行前裁决。Grok Bot 给成员的回复在发出前永远不会被检查。拒绝不会撤销已经发生的操作。

## 设置推理钩子

你必须是 Enterprise 团队的团队管理员。

1

### 准备你的安全服务器

在你的安全厂商控制台中创建推理钩子集成，或自行托管一个满足[端点要求](#endpoint-requirements)的服务器。设置对话框的 **安全厂商（Security Vendor）** 列表中包含带设置清单的厂商预设。

2

### 打开推理钩子

在 Cursor 仪表盘中，选择团队，然后从 Grok Bot 页面的 **安全与合规（Security & Compliance）** 部分打开[推理钩子](https://cursor.com/dashboard/bot/inference-hooks)。

3

### 添加端点

点击 **设置端点（Set Up Endpoint）**，选择你的厂商或 **自定义端点（Custom Endpoint）**，然后输入 **端点 URL（Endpoint URL）** 以及服务器需要的任何 **自定义标头（Custom Headers）**，例如它的 API key。保存时 Cursor 会检查该 URL。

4

### 复制签名密钥

首次保存并设置端点时会生成一个以 `whsec_` 开头的签名密钥（signing secret），并且只显示一次。把它粘贴到厂商的 webhook 密钥字段，或你的服务器配置中，以便验证每个请求。

5

### 测试连接

点击 **测试连接（Test Connection）**。Cursor 会发送一个合成请求，并显示裁决或检查失败的原因。此处出现拒绝，说明你的策略会拦截测试提示，因此在开始强制执行前先解决这个问题。

6

### 从影子模式开始

新配置以 **影子模式（Shadow Mode）** 启动。开启 **执行裁决（Enforce Verdicts）** 才开始发送。你的端点会收到每个受覆盖的请求，拒绝会记录在审计日志中，但不会拦截任何内容。如果团队已启用工具调用检查，新配置还会默认开启 **校验工具调用（Validate Tool Calls）**。此后即使在影子模式下，工具调用也会等待每个裁决。裁决结果看起来正确后，把 **失败处理（Failure Handling）** 下的 **模式（Mode）** 设为 **放行请求（Allow the Request）** 或 **拦截请求（Block the Request）**。

设置更改约一分钟内生效，已在处理中的请求会按旧设置完成。

在已保存端点、**执行裁决** 已开启且 Grok Bot 在覆盖范围内时，无论处于哪种模式、检查比例是多少，Grok Bot 都会跳过一些原本会在某一轮开始前进行的模型调用，因此回复可能启动得更慢。

### 端点要求

- **使用 443 端口上的 `https://` URL。** 主机必须可公开路由，并出示由公共证书颁发机构签发的证书。Cursor 会拒绝私有地址、回环地址和运营商级 NAT 地址。
- **重定向和隧道不可用。** Cursor 不跟随重定向，并将其视为检查失败。反向隧道主机不被接受。
- **不要把秘密放进 URL。** URL 不能携带凭据、查询字符串或片段，因为管理员会以明文看到它。把凭据放进自定义标头，它们会加密存储。URL 限制为 2,048 个字符。
- **对每个请求都用裁决作答。** 返回 HTTP 200 和一个 JSON 裁决，包括对测试连接。见[裁决](#verdicts)。

### 自定义标头

- **最多可以添加 16 个标头。** 名称使用字母、数字和连字符，不能使用下划线，最长 128 个字符。值为可打印 ASCII，最长 8,192 个字符。
- **值只可写入，不可读回。** 保存后，页面只显示标头名称。更改任何标头都意味着重新输入所有值。
- **更换 URL 会清除已保存的值。** 标头值永远不会发往并非为其保存的端点。更改 URL 后，在 **编辑（Edit）** 中重新输入它们。在此之前，请求会在不带这些标头的情况下发出。
- **部分标头由 Cursor 掌控。** 你无法添加 `Host`、`Cookie`、`User-Agent`、`Accept-Encoding`，`Transfer-Encoding` 等连接类标头，`X-Real-IP` 等客户端地址标头，或以 `Content-`、`Proxy-`、`X-Forwarded-`、`Webhook-`、`X-Cursor-` 开头的任何名称。

### 签名密钥

每个请求都带有 [Standard Webhooks](https://www.standardwebhooks.com) 标头，以便你的服务器拒绝任何不是 Cursor 发送的内容：

| 标头 | 值 |
| --- | --- |
| `webhook-id` | 帧的 `request_id` |
| `webhook-timestamp` | Unix 时间（秒） |
| `webhook-signature` | `v1,`，然后是 `{webhook-id}.{webhook-timestamp}.{raw body}` 的 base64 HMAC-SHA256，以 `whsec_` 之后那部分密钥的 base64 解码结果为密钥 |

每个请求只带一个签名。要轮换密钥，在 **请求签名（Request Signing）** 下点击 **轮换密钥（Rotate Secret）**。新密钥只显示一次，Cursor 会在约一分钟内开始用它签名，因此在那之前请继续接受旧密钥。轮换会被视作[断路器](#circuit-breaker)的一次设置更改。

### 测试连接

测试连接会发送一个带签名的 `prompt` 帧，其中 `source.application` 设为 `config-test`，消息固定且不含用户内容，也没有成员、会话或模型。它使用你保存的密钥签名，并等待你保存的裁决超时时间。从端点对话框运行时，它使用表单中的 URL 和标头；从页面运行时，使用已保存的 URL 和标头。

开启 **校验工具调用** 后，测试连接还会发送一个 `tool_call` 帧，其中包含一个名为 `config_test` 的合成调用。它会显示两个结果：**提示请求（Prompt request）** 和 **工具调用请求（Tool call request）**。只要提示请求得到裁决，工具调用结果就会出现。此处的允许只表示你的服务器作出了应答，并不表示它检查了该调用。

| 结果 | 含义 |
| --- | --- |
| 允许或拒绝 | 你的服务器返回了裁决。在强制执行前先解决拒绝 |
| URL 被拒绝 | 该 URL 不满足端点要求 |
| 私有或内部 IP | 该主机不是可公开路由的地址 |
| 超时 | 在裁决超时时间内未收到裁决 |
| 传输错误 | DNS、连接或 TLS 失败 |
| 非 200 状态 | 你的服务器返回了 200 之外的状态，包括重定向 |
| 无法解析的响应 | 响应体不是 JSON 裁决、被压缩，或大于 64 KiB |
| 需要签名密钥 | 先保存配置。保存会生成密钥 |

## 模式

**执行裁决** 控制是否发送。关闭时，Cursor 不发送任何内容，并保留你的设置。开启时，由 **模式** 决定检查无法完成时会发生什么：

| 模式 | 遇到拒绝时 | 检查失败时 |
| --- | --- | --- |
| **影子模式（Shadow Mode）**（默认） | 放行请求 | 放行请求 |
| **放行请求（Allow the Request）** | 拦截请求 | 未经检查地放行请求（失败开放） |
| **拦截请求（Block the Request）** | 拦截请求 | 拦截请求（失败关闭） |

在放行和拦截模式下，模型请求会等待裁决。在影子模式下，Cursor 在相同的时机发送相同的 `prompt` 帧，但仅在后台进行：模型请求不等待，成员看不到任何内容，拒绝和失败会记录在审计日志中。在高负载下，Cursor 可能跳过影子模式的 `prompt` 检查，被跳过的检查不会写入审计记录。[工具调用](#validate-tool-calls)在所有模式下都会等待裁决，包括影子模式。

当服务器超时、返回 200 之外的状态、返回不是 JSON 裁决或大于 64 KiB 的响应体、返回 `allow` 或 `deny` 之外的 `action`，或无法连接时，检查即失败。大于 64 MiB 的帧也算作失败。

一旦 Cursor 获取了你的设置，拦截模式会拦截每一个无法完成的检查，包括原因在 Cursor 一侧的情况。如果 Cursor 完全无法加载你团队的推理钩子设置，它就无法判断你选择了哪种模式，因此请求会继续，审计日志将其记录为失败开放，原因为 `config_unavailable`。工具调用也会继续，但 Cursor 只会在设置加载完成并显示这些调用本应被检查后才记录它们。

### 裁决超时

**裁决超时（毫秒）（Verdict Timeout (ms)）** 接受 1 到 10,000 毫秒，默认 5,000。它覆盖整个交互过程：连接、TLS 握手、请求和响应。如果连接失败，Cursor 会在同一超时时间内重试一次，使用相同的 `webhook-id` 和签名，因此你可以按 `webhook-id` 去重。服务器响应后 Cursor 绝不会重试。它自身的处理会在超时之上再增加最多约半秒。

### 检查比例（Rollout）

**检查的请求比例（%）（Requests Inspected (%)）** 在你逐步上线端点期间，只把一部分受覆盖的请求发送到端点。选择是粘性的，因此一轮背后的所有请求（包括子智能体和工具调用）要么全部被检查，要么全部被跳过。不在比例内的请求即使处于拦截模式也会不经检查地继续，0% 表示关闭检查。

### 断路器

由你的服务器负责的持续失败（例如超时、错误状态、TLS 错误和格式错误的裁决）会触发断路器（circuit breaker）。DNS 和连接错误、Cursor 拒绝的 URL，以及超过 64 MiB 的帧算作失败，但绝不会触发断路器。

- **触发期间，Cursor 停止发送。** 你的模式适用于每个受覆盖的请求：拦截模式全部拦截，放行和影子模式让其不经检查地通过。审计日志每次触发记录一个 `inference_hooks_circuit_breaker_tripped` 事件，触发期间不记录逐请求事件。
- **恢复是自动的。** 从触发后 10 分钟开始，Cursor 会定期向你的服务器发送测试连接请求。允许或拒绝都会重置断路器。
- **任何设置更改都会停止自动恢复。** 包括轮换密钥。端点修复后，点击 **重置（Reset）**，或者把 **执行裁决** 关闭再打开。

### Cursor 暂停

在紧急情况下，Cursor 可以为一个团队或所有人暂停推理钩子。暂停期间，Cursor 不发送任何帧，受覆盖的请求和工具调用继续，审计日志将其中大部分记录为失败开放，原因为 `kill_switch`。测试连接会显示「Inference hooks are temporarily paused by Cursor.」

## 校验工具调用

**校验工具调用** 会在每个调用了工具的模型响应之后，向端点发送一个 `tool_call` 帧。该响应中的每个调用都会等待裁决。该开关位于 **执行裁决** 下方，在执行裁决关闭时不生效，约一分钟内生效。

- **需要主动开启。** 当 Cursor 为你的团队开启工具调用检查时，该开关才会出现，逐请求审计事件开始标明其帧类型。其他方面没有变化。在此之前保存的配置会保持校验工具调用关闭，直到管理员开启。之后首次保存的配置则会默认开启。
- **一个帧、一个裁决覆盖一个响应。** 帧按模型发起调用的顺序列出该响应中的每个调用，但从不入帧的工具（例如回复）除外。`allow` 会运行它们全部。你不能允许部分调用而拒绝另一些。
- **拒绝会拒绝每一个调用。** 包括未列入帧的调用，例如回复。每个被拒绝的调用都会得到结果「Blocked by your organization's policy before it ran」，并且该轮以与被拒绝的提示相同的[拦截提示](#what-members-see)结束。
- **它共用你的设置。** 工具调用帧使用与提示帧相同的端点、签名密钥、模式、裁决超时、检查比例、断路器和拦截消息（Blocked Message）。没有单独的模式，因此为工具调用选择 **拦截请求** 也会拦截检查失败的提示。
- **工具调用在所有模式下都会等待。** 每个带帧调用的响应都会增加一次到端点的往返。在影子模式下，调用会等待裁决，最长到裁决超时，然后无论允许还是拒绝都会运行。影子模式的失败会计入断路器。
- **子智能体和计算机使用也会被检查。** 子智能体的响应会得到同样的检查。在计算机使用期间，每个浏览器操作都会单独检查，拒绝会停止该次计算机使用运行。鼠标和键盘操作不入帧。

只有在你的安全服务器能够处理 `tool_call` 帧之后，才开启校验工具调用。协议要求服务器对无法识别的帧类型回答 `allow`，因此不支持该类型的服务器会让每个调用都运行，而检查看起来仍在强制执行。对这类帧报错的服务器会在拦截模式下停止所有工具调用，这些失败会计入与提示帧共用的断路器。

## 成员看到什么

当你的服务器拒绝请求时，Grok Bot 桌面应用和移动应用会在发送被拦截消息的成员与 Bot 自己的对话中向其显示拦截提示（block notice）。在移动端，提示位于消息框上方。它会显示：

- 标题 **被你的组织策略拦截（Blocked by your organization's policy）**。
- 你服务器返回的 `deny_reason`，其后是你设置的 **拦截消息（Blocked Message）**。
- 附带 **编辑（Edit）** 按钮和 **重置（Reset）** 按钮的指引。**编辑** 会把被拦截的消息从对话中撤回，并把它的文本放入消息框（除非成员已在其中存有草稿），以便他们发送不同的内容。**重置** 会清空对话。移动应用和较新版本的桌面应用会先请成员确认。当 Cursor 无法把对话回滚到被拦截消息之前的位置时，只显示 **重置**。

**拦截消息** 最多接受 500 个字符，默认值为「Your organization's security policy blocked this request.」。关闭后只显示你服务器的 `deny_reason`。用它告诉成员接下来该做什么，例如联系谁。

重置后，Bot 不再看到该对话中较早的消息，并停止它为这个对话运行的后台助手。它启动的其他工作（例如云端智能体和后台命令）会继续，并可以回报结果。它的记忆、文件、例程（routine）和设置都会保留。编辑会把对话回滚到被拦截消息之前的位置。两者都不会撤销 Bot 已经执行的操作，例如它写入的文件。

如果重置后对话立刻又被拦截，提示中不会有按钮。它会说明被拦截的内容可能位于 Bot 的记忆或文件中，并请成员在那里移除它，或向管理员求助。

当拦截模式下检查失败时，桌面应用会显示 **你的组织策略检查不可用（Your organization's policy check is unavailable）** 以及「你的组织要求模型响应前先进行策略检查，但检查没有完成。请稍后重试；如果持续出现，请联系管理员。」移动应用会显示「你的组织策略检查不可用。请稍后重试；如果持续出现，请联系管理员。」此时不会显示你的拦截消息，也没有编辑或重置。

其他地方显示得更少：

- **共享 Bot 只通知发送者。** 在共享 Bot 中，提示及其按钮只发给发送被拦截消息的队友，出现在其与 Bot 自己的聊天中，编辑或重置只改变那个聊天。Bot 的所有者看不到拒绝原因或你的拦截消息。房间和群聊没有编辑或重置按钮。
- **Slack 在对话中回复。** Bot 会回答「你的组织策略拦截了此对话，因此我无法回复」；在一对一私信中，它还会引用拒绝原因和你的拦截消息，而频道线程和群组私信从不显示这些内容。回复中提供 **移除被拦截的消息（Remove blocked message）**（作用类似编辑）和 **重置**（会先请求确认），当 Cursor 无法回滚对话时只提供 **重置**。任何能使用该 Bot 且已关联 Cursor 账户的人都可以点击它们。被移除的消息在 Slack 中仍然可见，但 Bot 不再看到它。重置后立刻再次被拦截时不会显示按钮；拦截模式下检查失败时，Bot 会给出通用错误回复，而不是策略提示。
- **在其他场合，移动应用只显示普通失败。** 在群聊和并非成员本人的对话中，它会显示「Bot 未能响应」，并附上「被你的组织策略拦截。请发送不同的消息；如果持续出现，请联系管理员。」，且不显示拒绝原因、你的拦截消息或按钮。
- **其他 Cursor 应用只显示标题。**
- **较旧的桌面版本不显示按钮。** 视版本而定，提示会显示拒绝原因和你的拦截消息，并附指引「请发送不同的消息；如果持续出现，请开始新聊天」，或者只显示「被你的组织策略拦截。请发送不同的消息；如果持续出现，请联系管理员。」
- **后台助手会停止，但没有提示。** 当 Grok Bot 启动的助手被拦截时，Bot 会得知是你的组织策略阻止了它，但不会得到拒绝原因。
- **例程会停止并记录拦截。** Cursor 仪表盘中的运行历史会显示 **被你的组织策略拦截**，若拦截模式下检查失败则显示 **你的组织策略检查不可用**，并附固定说明，不显示拒绝原因。Grok Bot 应用的例程列表只显示该次运行失败。
- **电子邮件、Linear 和其他已连接渠道不会收到回复。**

被拦截的消息会留在对话中，直到有人撤回它或重置对话。在此之前，Grok Bot 会在之后的每个请求中发送它，因此你的服务器每次都会重新裁决。扫描整个对话记录的策略会持续拒绝该对话。只裁决最新用户消息的策略则会在成员发送不同内容后允许其继续。

请求被允许或处于影子模式时，成员看不到任何内容。影子模式也会把他们的对话发送到你的端点，因此在开启 **执行裁决** 之前，请告知成员你的组织会检查 Grok Bot 请求。

## 覆盖范围

**覆盖：** 团队成员 Grok Bot 对话背后的模型请求。这包括一轮中的每个步骤、子智能体、Grok Bot 为长对话撰写的摘要，以及例程。共享 Bot 或房间遵循其所属团队的推理钩子。个人 Bot 遵循其所有者所选团队的推理钩子。每个请求都有自己的帧，包含到目前为止的对话。

**不覆盖：**

- **模型响应不会被检查。** 开启[校验工具调用](#validate-tool-calls)后，其中的工具调用会被检查，但从不入帧的工具除外。见[工作方式](#how-it-works)。
- **请求中不属于对话的部分不会发送。** 系统提示、工具定义和模型的隐藏推理永远不会到达你的端点，Cursor 还会略去大部分它为模型添加的文本，例如提醒和时间戳。
- **辅助性模型调用不会发送。** 这些调用用于支撑对话而非延续对话，例如编写聊天标题、自动审查（Auto Review）和保存记忆。
- **其他 Cursor 功能不在覆盖范围内。** 包括云端智能体（Cloud Agents）、编辑器中的智能体、CLI、Agent SDK、Tab、嵌入（embeddings）和本地模型。
- **工具运行后做了什么不会被检查。** 校验工具调用只裁决每个入帧调用运行前的情况，不检查其后的行为，例如脚本运行的命令、已连接应用的副作用，或来自成员 Grok Bot 计算机的网络流量。工具的输出只会作为之后某个 `prompt` 帧中的工具结果到达你的端点。使用[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)和[自动审查](https://cursor.com/docs/grok-bot/security#approvals-and-auto-review)来控制操作。
- **语音通话不在覆盖范围内。** 其提示和工具调用都不会到达你的端点。

## 请求格式

Cursor 以 HTTPS `POST` 发送每个帧，正文为紧凑的 JSON。标头名称均为小写。

| 标头 | 值 |
| --- | --- |
| `content-type` | `application/json` |
| `user-agent` | `cursor-inference-hooks/1` |
| `accept-encoding` | `identity` |
| `webhook-id`、`webhook-timestamp`、`webhook-signature` | 见[签名密钥](#signing-secret) |
| 你的自定义标头 | 按保存值发送 |

`host` 和 `content-length` 等标准标头也会随每个请求发送。

```
{  "type": "prompt",  "request_id": "req_6b1f0c2e-4d7a-4f1e-9a53-2c8d7e41b9a0",  "tenant_id": "team_4mQvT8yLcN2pR6",  "actor": {    "type": "user",    "id": "user_8hJw3KzP5sXq1V7nB2cF9mD4tR",    "email_address": null  },  "source": { "application": "grok-bot" },  "session_id": "3f2c9a71-58e4-4b0d-9c6a-0d1e7b25a4f8",  "model": "<Cursor model identifier>",  "messages": [    {      "role": "user",      "content": [        {          "type": "text",          "text": "Check the Q3 renewals sheet for accounts at risk and draft a note to the account team."        },        {          "type": "attachment",          "file_name": null,          "media_type": "image/png",          "size_bytes": 184320,          "text": null        }      ]    }  ],  "metadata": {}}
```

### 帧字段

| 字段 | 值 |
| --- | --- |
| `type` | `prompt`，或用于[工具调用帧](#tool-call-frames)的 `tool_call` |
| `request_id` | 请求的唯一 ID。与 `webhook-id` 及审计日志中的 `request_id` 一致 |
| `tenant_id` | 你团队的不透明 ID |
| `actor.type` | 始终为 `user` |
| `actor.id` | 发送消息的成员或团队服务账号的不透明 ID。对未关联 Cursor 账户的 Slack 发送者为 null |
| `actor.email_address` | 始终为 null |
| `source.application` | `grok-bot`；测试连接和断路器恢复检查为 `config-test` |
| `session_id` | Bot 的不透明 ID，在其所有聊天和成员之间共享，因此不能标识某一个对话 |
| `model` | Cursor 模型标识符。用于报表，不要用于允许列表 |
| `messages` | 到目前为止的对话，或工具调用帧中的最新响应。见[消息](#messages) |
| `metadata` | 始终为空 |

### 消息

- **角色是 `user` 和 `assistant`。** 工具结果位于 `user` 下。
- **块类型是 `text`、`tool_use`、`tool_result` 和 `attachment`。** `tool_use` 块指明工具并保存其 `input`，与之匹配的 `tool_result` 保存输出。Grok Bot 提供给模型的上下文（例如规则、共享记忆和它可以使用的已连接应用）通常出现在 `attachment` 块的 `text` 中。图像是一个 `attachment`，带有其媒体类型和大小，但不含字节或 URL。
- **每个 `prompt` 帧都包含到目前为止的整个对话。** 帧不是增量，因此每个帧都会再次携带较早的消息。在长对话中，Grok Bot 撰写的摘要会取代较早的消息。
- **给成员的回复是工具调用。** Grok Bot 通过一个工具发送成员读到的内容，因此其回复出现在 `tool_use` 的 input 中，而不是 assistant 的 `text` 中。
- **Cursor 绝不会加入秘密值。** 上下文可以指明并描述 Bot 可以使用的秘密，但绝不包含它们的值。

### 工具调用帧

`tool_call` 帧具有与 `prompt` 帧相同的标头和字段，`type` 设为 `tool_call`，有自己的 `request_id`，并使用该轮 `prompt` 帧的 `session_id`。其 `messages` 数组包含响应的 `assistant` 消息，模型的文本在 `text` 块中，每个入帧调用对应一个 `tool_use` 块。请读取 `messages` 的最后一项，因为协议允许在它之前出现较早的消息。

| `tool_use` 字段 | 值 |
| --- | --- |
| `id` | 模型为本次调用指定的 ID。之后的 `prompt` 帧使用相同的 ID |
| `tool_name` | 运行的工具 |
| `input` | 模型写入的参数；不是有效 JSON 时为 null |
| `tool_info` | 工具是什么以及在哪里运行。永不为 null。可选字段会被省略，而不是 null |

| `tool_info.type` | Grok Bot 为其发送的场景 | `toolset_name` |
| --- | --- | --- |
| `client` | Bot 电脑上的 `Shell`、`Read` 和 `AwaitShell` | `grok-bot-computer` |
| `client` | 成员电脑上的相同工具，以及两台电脑之间的文件复制 | `user-computer` |
| `client` | 手机和设备工具 | `user-phone`、`user-device` 或 `user-computer` |
| `client` | 浏览器工具 | `browser` |
| `client` | 计算机使用 | `computer-use` |
| `client` | 运行在 Bot 电脑上的模型上下文协议（Model Context Protocol，MCP）服务器 | 服务器名称 |
| `third_party` | 通过 HTTP 访问的 MCP 服务器，以及 Slack 和 Microsoft Teams 工具 | 服务器或应用 |
| `application` | 在 Cursor 后端运行的工具，例如网络搜索、电子邮件、子智能体和发往其他 Bot 的消息 | 已知时为该功能 |

- **`tool_name` 指明运行的内容。** `bash` 调用显示为 `Shell`。MCP 调用保留模型使用的工具名 `CallMcpTool` 或 `CallDynamicTool`，服务器在 `toolset_name` 中，参数在 `input` 中。
- **Cursor 知道时，`third_party` 调用会带有 `origin`。** 它是服务的 scheme、host 和 port，并带有 `verified_origin: true`，因为 Cursor 自己连接该服务。缺少 `origin` 表示未知，而不是安全。Grok Bot 不发送 `platform`。
- **输入不会被脱敏。** `input` 携带模型放入调用中的任何内容，例如粘贴到命令中的令牌，或 `AddMcpServer` 调用中的凭据。之后的 `prompt` 帧会携带相同的输入。Cursor 唯一会裁剪的值是它作为 `origin` 添加的服务器 URL，只保留 scheme、host 和 port。
- **`text` 块是叙述。** 它们保存模型在调用之间说的话，Grok Bot 不会把它们发送给任何人。成员从 `SendToUser` 调用读取回复，而工具调用帧从不包含这些调用。

```
{  "type": "tool_call",  "request_id": "req_3b1f8c2e-9a4d-4e7b-8f20-6c5d1a9e7b42",  "tenant_id": "team_4mQvT8yLcN2pR6",  "actor": {    "type": "user",    "id": "user_8hJw3KzP5sXq1V7nB2cF9mD4tR",    "email_address": null  },  "source": { "application": "grok-bot" },  "session_id": "3f2c9a71-58e4-4b0d-9c6a-0d1e7b25a4f8",  "model": "<Cursor model identifier>",  "messages": [    {      "role": "assistant",      "content": [        { "type": "text", "text": "I'll check the build log, then file the bug." },        {          "type": "tool_use",          "id": "call_01",          "tool_name": "Shell",          "input": { "command": "tail -n 50 build.log" },          "tool_info": { "type": "client", "toolset_name": "grok-bot-computer" }        },        {          "type": "tool_use",          "id": "call_02",          "tool_name": "CallMcpTool",          "input": {            "server": "tracker",            "toolName": "create_issue",            "arguments": { "title": "Nightly build fails at the link step" }          },          "tool_info": {            "type": "third_party",            "toolset_name": "tracker",            "origin": "https://mcp.tracker.example",            "verified_origin": true          }        }      ]    }  ],  "metadata": {}}
```

用与 `prompt` 帧相同的[裁决](#verdicts)来应答 `tool_call` 帧。此示例中的拒绝会拒绝两个调用。

### 为这些帧编写策略

- **验证签名。** 不要依赖 User-Agent 或源 IP。如果推理钩子页面在 **请求签名** 下列出了 **源 IP 范围（Source IP Ranges）**，你也可以将它们加入允许列表。
- **把 ID 当作不透明字符串。** 不要解析 `tenant_id` 或 `actor.id`。按 `actor.id` 映射成员，因为帧不携带电子邮件。
- **把 `source.application` 当作开放集合。** 随着覆盖范围扩大，Cursor 会添加值。它只是提示性的，不是安全控制。
- **扫描每一种块类型，而不只是 `text`。** 上下文通常出现在 attachment 的 `text` 中，给成员的回复和已连接应用的调用出现在 `tool_use` 的 input 中。
- **不要依赖 `tool_result.is_error`。** 对大多数失败的工具调用它也是 `false`，包括你的服务器拒绝的调用。
- **按 `tool_info` 而不是名称来裁决工具调用。** 用 `tool_info.type` 和 `origin` 判断调用去往哪里，并接受你无法识别的 `type` 值。

### 裁决

以 HTTP 200 和一个 JSON 对象作答：

```
{  "action": "deny",  "deny_reason": "This message contains a customer account number. Remove it and try again.",  "reference_id": "policy-7f3c21"}
```

- **`action`** 为 `allow` 或 `deny`。其他任何值都算检查失败。
- **`deny_reason`** 会显示在发送消息的成员看到的拦截提示中。Cursor 会将其截断至 500 个字符。
- **`reference_id`** 是你为该决定设置的标识符，会记录在 Cursor 审计日志中。最多 50 个字符，可取 `A-Z`、`a-z`、`0-9` 以及 `.`、`_`、`:`、`/`、`-`。格式错误的值会被丢弃，拒绝仍然生效。
- **未知字段会被忽略。** Cursor 最多读取 64 KiB 的未压缩内容，并忽略 Cookie。

对来自测试连接和断路器恢复的 `config-test` 帧也要用裁决作答，并把它们排除在成员流量的报表之外。

## 审计日志

推理钩子活动会出现在你团队的[审计日志](https://cursor.com/docs/enterprise/compliance-and-monitoring#audit-logs)中。载荷只携带标识符和代码，绝不包含提示内容、拒绝原因、签名密钥或标头值。被允许的请求不会写入事件。

| `event_type` | 触发时机 | 字段 |
| --- | --- | --- |
| `inference_hooks_config_updated` | 管理员保存设置或重置断路器，或自动恢复将其重置 | `action`（`update`、`reset_circuit_breaker`、`circuit_breaker_recovered`）、`changed_fields`、`enforce_verdicts`、`mode`、`endpoint_host`、`verdict_timeout_ms`、`rollout_percent`、`enabled_surfaces`、`config_version`、`validate_tool_calls` |
| `inference_hooks_signing_secret_generated` | 首次保存设置端点时生成签名密钥，或管理员轮换它 | `action`（`generate_signing_secret`、`rotate_signing_secret`）、`changed_fields`（始终为空）、`enforce_verdicts`、`mode`、`endpoint_host`、`verdict_timeout_ms`、`rollout_percent`、`enabled_surfaces`、`config_version`、`validate_tool_calls` |
| `inference_hooks_request_denied` | 你的服务器拒绝了请求 | `request_id`、`reference_id`、`source_application`、`session_id`、`model`、`actor_id`、`mode`、`enforced`（影子模式下为 `false`）、载荷 `event_type` |
| `inference_hooks_request_failed_open` | 请求在没有裁决的情况下继续：放行或影子模式下检查失败、Cursor 暂停，或 Cursor 无法加载设置 | `request_id`、`reason`、`source_application`、`session_id`、`model`、`actor_id`、`mode`、`status_code`（未收到响应时为 `0`）、载荷 `event_type` |
| `inference_hooks_request_failed_closed` | 拦截模式下检查失败，因此请求被拦截 | `request_id`、`reason`、`source_application`、`session_id`、`model`、`actor_id`、`mode`、`status_code`（未收到响应时为 `0`）、载荷 `event_type` |
| `inference_hooks_circuit_breaker_tripped` | 持续失败触发了断路器 | `config_version`、`mode`、`failure_count`、`window_seconds`、`last_failure_kind` |

有两个字段同名 `event_type`。表格第一列是审计事件自身的类型。拒绝、失败开放和失败关闭事件载荷中的 `event_type` 指明被检查的帧，即 `prompt` 或 `tool_call`。它会在 Cursor 为你的团队开启工具调用检查后出现，两个设置事件上的 `validate_tool_calls` 也是如此。没有载荷 `event_type` 的拒绝或失败事件来自提示检查。

在 `inference_hooks_signing_secret_generated` 上，设置字段显示更改后的状态。轮换会提升 `config_version`。首次生成密钥时会与同一次保存产生的 `inference_hooks_config_updated` 事件共用同一个版本。

Cursor 在每种模式下都会记录请求失败：放行和影子模式记为失败开放，拦截模式记为失败关闭；它还会记录断路器的自动恢复。失败开放和失败关闭事件上的 `reason` 是某种失败（`timeout`、`non_200_status`、`unparseable_response`、`oversized_response`、`invalid_action`、`transport_error`、`tls_error`、`endpoint_rejected`、`frame_too_large`）、Cursor 一侧的原因（`endpoint_not_allowlisted`、`config_unavailable`），或（仅限失败开放）暂停（`kill_switch`）。请基于这些事件名称和 `reason` 值构建 SIEM 规则。

拒绝和失败事件上的 `request_id` 与帧的 `request_id` 和 `webhook-id` 一致，因此你可以把厂商的记录与审计日志关联起来。

推理钩子页面还会显示端点健康状况：状态、裁决延迟、每分钟失败数、24 小时拦截率，以及带有类型和状态码的近期错误。开启校验工具调用后，它会把这些数字拆分为提示和工具调用。其数字并不覆盖所有流量，因此可能低于厂商的统计。

## 隐私与隐私模式

- **Cursor 不保留发往钩子的内容。** Cursor 通过 HTTPS 把每个帧发送到你的端点，并在收到裁决后丢弃它。帧内容不会写入 Cursor 的数据库、日志、指标或追踪。
- **你的端点，你的保留策略。** 端点属于你的组织或你的安全厂商。它存储什么、存储在哪里以及存储多久，取决于你的配置和你与该厂商的协议。Cursor 不控制这些数据。
- **隐私模式（Privacy Mode）不变。** 模型请求本身完全按没有钩子时的方式处理，遵循你团队的隐私模式设置，钩子不会为其增加副本。无论隐私模式如何，推理钩子都会对所有受覆盖的成员运行，因为你的管理员指示 Cursor 把这些请求发送到你自己的端点。
- **帧字段只用不透明 ID 标识人员。** `actor.email_address` 始终为 null。

Cursor 只保留运行该功能以及向你展示发生了什么所需的内容：

- **你的设置，秘密已加密。** 标头值和签名密钥会加密存储。
- **仅含标识符和代码的审计日志事件。** 其中包括你服务器的 `reference_id`，如[审计日志](#audit-log)中所列。
- **不含内容的健康数字。** 它们包含计数、延迟，以及近期错误类型和状态码。
- **拦截提示，与被拦截的那一轮一起加密。** 你服务器的 `deny_reason` 和你的拦截消息会与 Grok Bot 对被拦截那一轮的记录一起加密存储。

## 故障排查

### 为什么我在 Grok Bot 页面上看不到推理钩子？

该页面会向 Enterprise 团队的团队管理员显示，并且显示仪表盘中选中的团队。请确认选对了团队。如果页面显示「Inference hooks aren't available yet.」，请联系你的客户经理。

### 为什么我的端点 URL 被拒绝？

检查[端点要求](#endpoint-requirements)。常见原因是端口不是 443、URL 中包含查询字符串或凭据、使用了隧道主机，或主机解析到私有地址。

### 为什么测试连接提示需要签名密钥？

Cursor 会在首次保存设置端点时生成密钥。保存端点，把密钥复制到厂商控制台，然后再次测试。

### 为什么我的服务器拒绝 Cursor 的请求？

大多数拒绝是签名或凭据不匹配。把当前签名密钥粘贴到你的服务器，如果你的验证器需要 `whsec_` 前缀就一并包含，并确认它按标准 base64 解码该密钥。确认你的 API key 标头已保存。如果更改了端点 URL，请重新输入标头值。轮换后，Cursor 会在约一分钟内切换到新密钥。

### 为什么测试连接返回拒绝？

你服务器的策略拒绝了 Cursor 的合成测试提示。在放行或拦截模式下，这样的策略也会拦截成员。在开启强制执行之前调整策略或其默认动作。

### 为什么请求超时？

你的服务器耗时超过了裁决超时时间。在健康面板和厂商报表中检查裁决延迟。较轻量的扫描配置（scan profile）响应更快。你可以把 **裁决超时（毫秒）** 提高到最多 10,000。

### 为什么我的端点没有收到请求？

检查是否已保存端点、**执行裁决** 是否开启、**覆盖范围** 是否包含 Grok Bot、**检查的请求比例（%）** 是否大于 0，以及断路器是否未被触发。只有你团队成员的 Grok Bot 对话在覆盖范围内。如果测试连接报告推理钩子已暂停，说明 Cursor 已将其暂停。

### 为什么成员看到策略检查不可用？

你处于拦截模式且检查失败，或断路器已触发。检查推理钩子页面上的 **近期错误（Recent Errors）**。要在修复端点期间让成员继续工作，请切换到 **放行请求**。

### 为什么开启校验工具调用后工具调用停止了？

在拦截模式下，当你的服务器无法应答 `tool_call` 帧时，工具调用会停止。在推理钩子页面的 **近期错误** 中检查 **工具调用（Tool Calls）** 下的错误，并确认你的厂商支持工具调用帧。在支持之前，请关闭 **校验工具调用**。

### 断路器触发了。如何恢复？

修复端点，运行测试连接，然后点击 **重置**。任何设置更改后自动恢复都会停止，因此如果你在触发后编辑过任何内容，就不要等待自动恢复。

### 为什么一次拦截后对话中的每条消息都被拦截？

被拦截的消息会留在对话中，并随之后的每个请求发送到你的服务器，因此扫描整个对话记录的策略会逐条拒绝它们。在桌面或移动应用的拦截提示上选择 **编辑**，或在 Slack 中 Bot 回复上的 **移除被拦截的消息**，撤回该消息并发送不同的内容。**重置** 则会清空对话。如果重置后对话立刻又被拦截，你的策略匹配到的内容很可能在 Bot 的记忆或文件中。请在那里移除它。只裁决最新用户消息的策略会在成员发送不同内容后允许对话继续。

### 为什么审计日志筛选器中没有推理钩子事件？

只有在你团队启用推理钩子期间，这些事件类型才会出现在筛选器中。已记录的事件仍会显示在日志中。
