---
title: "如何检测 Meta 的 Muse AI 智能体"
linkTitle: "检测 Muse 请求"
date: 2026-10-14
originalTitle: "How to detect Meta's Muse AI agent"
sourceUrl: "https://arcjet.com/learn/how-to-detect-metas-muse-ai-agent"
author: "Arcjet"
publisher: "Arcjet"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-21
tags: [运行环境, 安全]
products: [muse]
updatedAt: 2026-11-16
dateNote: "页面标注发表 2026-10-14、更新 2026-11-16。"
---

{{< source-info >}}

**收录说明**：直接下载；代码示例中的行号为网页渲染残留，已去掉；文末 Arcjet 产品推广一节已删去；发布方为机器人检测厂商 Arcjet，文中检测数据来自其自家平台流量，产品相关章节据此理解。

**内容摘要**：文章介绍两种验证 Muse 请求的方法：Web Bot Auth（密钥目录位于 muse.ai/.well-known/http-message-signatures-directory）与 Personal Agent Protocol（Poppy，client_id 为 https://muse.ai/poppy/agent.json），Arcjet 将验证通过的请求报告为机器人 META_MUSE，证据为 SIGNATURE，Poppy 会话的 delegated 字段为 true。未带签名或会话的 Muse 请求与普通 Chrome on Linux 请求无异：User-Agent 称 Chrome 154 on Linux（2026 年 9 月 22 日进入稳定版），无智能体名称，观测到的请求来自美国移动网络而非云厂商，须结合 SwiftShader 软件渲染与 ARM 架构客户端提示两项浏览器环境信号识别，且单凭其中一项不足以判定。Arcjet 平台流量的分析显示，Muse 浏览器典型配置为 Chrome 154、client-hint 架构 arm、经 ANGLE 的 SwiftShader 渲染、6 个逻辑 CPU、约 16 GB 设备内存（有时 8 GB）、通常 1920×1080 屏幕，作者提醒不要按 CPU 核数、内存或屏幕尺寸写规则，因为这些值并不稳定。网站可通过发布 /.well-known/poppy.json 接受 Muse 会话：Muse 经授权服务器以 OAuth 登录，Arcjet 验证 Poppy-Session 令牌后报告 delegated 为 true，但会话只证明请求来自 Muse 且代表某位用户，不表明该用户批准了具体操作，购买等不可逆操作仍需网站自行核对。作者建议把仅供真人使用的表单拒之门外并引导智能体走 API，同时保持速率限制，Arcjet 以 console.dev 订阅表单为例演示了以 detectBot 规则拒绝表单提交并返回 API 指引的做法。

**保留理由**：提供了识别与接纳 Muse 请求的完整技术方法，包括签名验证、浏览器指纹组合与 Poppy 会话处理，是已收资料中唯一系统讲解服务端如何检测 Muse 的实操指南。

---

**简而言之：** Meta 的 Muse 使用 Web Bot Auth 对请求签名，密钥位于 https://muse.ai/.well-known/http-message-signatures-directory；在发布了 /.well-known/poppy.json 的站点上，它还会提交 Personal Agent Protocol（Poppy）会话，client_id 为 https://muse.ai/poppy/agent.json。Arcjet 把验证通过的 Muse 请求报告为 META_MUSE，kind 为 AI_AGENT、evidence 为 SIGNATURE、operator 为 muse.ai，并对 Poppy 会话把 delegated 置为 true。不带签名或会话的 Muse 请求看起来就像 Linux 上的 Chrome，因此要用 SwiftShader 渲染加上 ARM 架构客户端提示来识别，拒绝仅供真人使用的表单，并把智能体引导到你的 API。

## Meta 的 Muse 是什么？

[Meta 的 Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) 是一个个人智能体，它通过云端托管的 Chromium 浏览器代替个人浏览网页。要检测 Meta 的 Muse AI 智能体，请验证它的签名：Muse 用 [Web Bot Auth](/learn/web-bot-auth) 对请求签名，并提交 [Personal Agent Protocol](/learn/personal-agent-protocol)（Poppy）会话，Arcjet 会把两者都报告为机器人 `META_MUSE`，证据为 `SIGNATURE`。对于不带签名或会话的 Muse 请求，则退回到浏览器信号：SwiftShader 软件渲染，加上 Chrome 精简版 `X11; Linux x86_64` user agent 上的 ARM 架构客户端提示。

Meta 于 2026 年 9 月 8 日推出 Muse。Muse 会打开浏览器、读取页面、[填写表单并完成购买](https://www.meta.com/help/artificial-intelligence/2124746764949121/)。每个人在云端获得一台 Linux 虚拟机，其中运行一个基于 Chromium 的浏览器，用户可观看并接管它。该浏览器发送标准的 Chrome-on-Linux `User-Agent` 请求头，不含智能体名称，因此这个请求头不能告诉你请求是 Muse 发出的；签名或会话可以。

截至 2026 年 11 月，Muse 有两种表明身份的方式，你可以任选其一或两者都用：

- **Web Bot Auth。** Muse 在 `https://muse.ai/.well-known/http-message-signatures-directory` 发布密钥目录，并用匹配的密钥为请求签名。验证通过的签名证明请求来自 Muse 的基础设施。
- **Personal Agent Protocol。** Muse 在 `https://muse.ai/poppy/agent.json` 发布 Poppy `client_id`。在发布了 `/.well-known/poppy.json` 的站点上，Muse 发送 `Poppy-Session` 令牌，证明请求来自 Muse，且 Muse 代表其某位用户行事。Meta 的 [Poppy 公告](https://muse.ai/blog/poppy-personal-agent-protocol)称 Muse 是「第一个支持 Poppy 的个人智能体」。

[console.dev](https://console.dev/) 是一份每周开发者工具简报，它展示了两种方法分别适用于哪里。console.dev 的订阅表单是给真人用的，智能体使用 console.dev 的 [API 与 MCP 服务器](https://console.dev/developers)。Arcjet [Advanced Signals](/blog/announcing-advanced-bot-signals-to-detect-automation-without-captchas) 保护该表单，使自动注册进不了邮件列表，智能体转而使用 API。验证通过的 Muse 身份让同一个站点可以在其他路由上直接指名该智能体，而不必从浏览器环境去推断。

关于具名智能体与请求签名的更多信息，见[如何识别 AI 智能体与机器人](/learn/identify-ai-agents-and-bots)。关于对提交到你表单的智能体进行分类的更多信息，见 [AI 智能体机器人管理](/learn/ai-agent-bot-management)。

## 如何检测 Muse 的签名请求？

你通过对照 `muse.ai` 上的密钥目录验证 Web Bot Auth 签名，来检测 Muse 的签名请求。Arcjet 在 `detectBot` 规则内部完成这件事，把验证通过的 Muse 请求报告为机器人 ID `META_MUSE`，kind 为 `AI_AGENT`、evidence 为 `SIGNATURE`、operator 为 `muse.ai`。签名标识的是 Muse，而不是让 Muse 行事的那个用户。

一条带签名的 Muse 请求携带三个 Web Bot Auth 请求头。`Signature-Agent` 指明 `https://muse.ai` 源，`Signature-Input` 列出被签名的组件并带有 `web-bot-auth` 标签，`Signature` 承载签名字节。你的验证器从 Muse 的目录获取密钥，并对收到的请求校验签名。2026 年 11 月 16 日，Muse 的目录里有两把 Ed25519 密钥，设置了 `Cache-Control: must-revalidate, max-age=3600`，并用 `http-message-signatures-directory` 标签为自己的响应签名。

下表列出 Muse 以各种方式到达你的站点时，Arcjet 报告的机器人身份字段：

| 请求 | `botId` | `kind` | `evidence` | `operator` | `delegated` |
| --- | --- | --- | --- | --- | --- |
| Web Bot Auth 签名验证通过 | `META_MUSE` | `AI_AGENT` | `SIGNATURE` | `muse.ai` | `false` |
| Poppy 会话验证通过 | `META_MUSE` | `AI_AGENT` | `SIGNATURE` | `muse.ai` | `true` |
| 无签名或会话，且 Signals 检查未通过 | 空 | `AUTOMATION` | `FINGERPRINT` | 空 | `false` |
| 无签名或会话，且 Signals 检查通过 | 无身份 | None | None | None | None |

`META_MUSE` 位于开源的 [well-known-bots](https://github.com/arcjet/well-known-bots) 目录中，属于 `CATEGORY:AI`、`CATEGORY:AI_AGENT` 和 `CATEGORY:META`。Arcjet 信任 Muse 的目录与 `client_id`，是因为目录里列出了它们，而不是因为某个请求提到了它们。包含 `CATEGORY:AI_AGENT` 或 `META_MUSE` 的允许列表会放行验证通过的 Muse 请求，指名其中任一者的拒绝列表会拒绝它。

验证通过的签名，其价值取决于你的框架交给 Arcjet 的路径。覆盖 `@path` 的签名需要原始请求路径，而某些适配器（例如 Next.js App Router）不提供该路径。具体清单见[哪些框架保留被签名的路径](/learn/web-bot-auth#arcjet-adapters)。

### 在 JavaScript 中检测 Muse

下面的 Express 应用在产品页上允许搜索引擎与 Muse，并记录每条验证通过的 Muse 请求的身份：

```
import arcjet, {

detectBot,

type ArcjetBotIdentity,

type ArcjetDecision,

} from "@arcjet/node";

import { isAiAgent, isSpoofedBot } from "@arcjet/inspect";

import express from "express";

const aj = arcjet({

key: process.env.ARCJET_KEY!,

rules: [

detectBot({

mode: "LIVE",

allow: ["CATEGORY:SEARCH_ENGINE", "META_MUSE"],

}),

],

});

// Return the identity of a verified Muse request, if any

function verifiedMuse(decision: ArcjetDecision): ArcjetBotIdentity | undefined {

for (const result of decision.results) {

if (isAiAgent(result) && result.reason.isBot()) {

const identity = result.reason.identity;

if (

identity?.botId === "META_MUSE" &&

identity.evidence === "SIGNATURE"

) {

return identity;

}

}

}

return undefined;

}

const app = express();

app.get("/products/:id", async (req, res) => {

const decision = await aj.protect(req);

if (decision.isDenied() || decision.results.some(isSpoofedBot)) {

res.status(403).json({ error: "Forbidden" });

return;

}

const muse = verifiedMuse(decision);

if (muse) {

// For example: META_MUSE SIGNATURE muse.ai false

console.log(muse.botId, muse.evidence, muse.operator, muse.delegated);

}

res.json({ id: req.params.id });

});

app.listen(3000);
```

`isAiAgent` 对 kind 为 `AI_AGENT` 且未被伪造的 `LIVE` 结果为 true。它不检查 evidence，因此辅助函数自行检查 `SIGNATURE`。

### 在 Python 中检测 Muse

下面的 FastAPI 路由用 `is_ai_agent` 与 `reason_v2` 做同样的事：

```
import os

from arcjet import (, is_spoofed_bot

BotCategory,

BotIdentity,

Decision,

Mode,

arcjet,

detect_bot,

is_ai_agent,

)

from fastapi import FastAPI, Request

from fastapi.responses import JSONResponse

aj = arcjet(

key=os.environ["ARCJET_KEY"],

rules=[

detect_bot(

mode=Mode.LIVE,

allow=[BotCategory.SEARCH_ENGINE, "META_MUSE"],

),

],

)

app = FastAPI()

def verified_muse(decision: Decision) -> BotIdentity | None:

"""Return the identity of a verified Muse request, if any."""

for result in decision.results:

reason = result.reason_v2

if is_ai_agent(result) and reason.type == "BOT":

identity = reason.identity

if (

identity is not None

and identity.bot_id == "META_MUSE"

and identity.evidence == "SIGNATURE"

):

return identity

return None

@app.get("/products/{product_id}")

async def product(request: Request, product_id: str):

decision = await aj.protect(request)

if decision.is_denied() or any(

is_spoofed_bot(r) for r in decision.results

):

return JSONResponse({"error": "Forbidden"}, status_code=403)

muse = verified_muse(decision)

if muse is not None:

# For example: META_MUSE SIGNATURE muse.ai False

print(muse.bot_id, muse.evidence, muse.operator, muse.delegated)

return {"id": product_id}
```

### 在 Go 中检测 Muse

下面的 `net/http` 处理器从 `result.Reason.Bot.Identity` 读取身份：

```
package main

import (

"log"

"net/http"

"os"

"github.com/arcjet/arcjet-go"

)

// verifiedMuse returns the identity of a verified Muse request, if any.

func verifiedMuse(decision arcjet.Decision) *arcjet.BotIdentity {

if !decision.IsAIAgent() {

return nil

}

for _, result := range decision.Results {

bot := result.Reason.Bot

if bot == nil || bot.Identity == nil {

continue

}

id := bot.Identity

if id.BotID == "META_MUSE" && id.Evidence == arcjet.BotEvidenceSignature {

return id

}

}

return nil

}

func main() {

aj, err := arcjet.NewClient(arcjet.Config{

Key: os.Getenv("ARCJET_KEY"),

Rules: []arcjet.Rule{

arcjet.DetectBot(arcjet.BotOptions{

Mode:  arcjet.ModeLive,

Allow: []string{arcjet.BotCategorySearchEngine, "META_MUSE"},

}),

},

})

if err != nil {

log.Fatal(err)

}

http.HandleFunc("GET /products/{id}", func(w http.ResponseWriter, r *http.Request) {

decision, err := aj.Protect(r.Context(), r)

if err != nil {

http.Error(w, "Internal Server Error", http.StatusInternalServerError)

return

}

if decision.IsDenied() || decision.IsSpoofedBot() {

http.Error(w, "Forbidden", http.StatusForbidden)

return

}

if muse := verifiedMuse(decision); muse != nil {

// For example: META_MUSE SIGNATURE muse.ai false

log.Println(muse.BotID, muse.Evidence, muse.Operator, muse.Delegated)

}

w.Write([]byte("ok"))

})

log.Fatal(http.ListenAndServe(":3000", nil))

}
```

只有 Arcjet Cloud 才计算身份。SDK 在本地做出的决策（例如由其本地机器人检测给出的拒绝）没有身份。

## 不带签名的 Muse 请求在你的服务器看来是什么样？

从服务器角度看，不带签名或会话的 Muse 请求就是一次普通的 Chrome-on-Linux 表单提交。以下各节讨论这种回退情形：到达某条路由、但没有 Web Bot Auth 签名或 Poppy 会话的请求，包括所有发往不发布 `poppy.json`、且 Muse 也不签名的站点的 Muse 请求。Muse 的 `User-Agent` 自称是 Linux 上的 Chrome 154，随附的请求头与真实浏览器的 `POST` 相符：

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)

Chrome/154.0.0.0 Safari/537.36
```

根据 [Chromium 发布日程](https://chromiumdash.appspot.com/schedule)，Chrome 154 于 2026 年 9 月 22 日进入稳定渠道。这个日期与 Meta 所说的「真正最新的、基于 Chromium 的浏览器」相符。请求头、IP 地址与页面自动化指纹仍然无法指名 Muse，因此识别取决于浏览器环境信号。

### 不带签名的 Muse 请求头能识别该智能体吗？

不能。Muse 的请求头不标识该智能体。Muse 为 Chromium 154 发送 `Sec-CH-UA`，`Sec-CH-UA-Platform` 为 `"Linux"`，`Sec-Fetch-*`、`Origin` 与 `Referer` 的值与真实表单提交相符。Muse 的 user agent 没有智能体名称，未签名的请求也没有 `Signature-Agent` 或 `Poppy-Session` 请求头，因此[识别 AI 智能体的常见方法](/learn/identify-ai-agents-and-bots)都不适用。

据 Meta 所说，「当 Muse 浏览互联网时，它会表现为你的活动。」2026 年 9 月 Amazon [在其商店中封禁 Muse](https://www.geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping/) 时，Amazon 表示 Muse 不表明自己的身份。[Cloudflare Radar](https://radar.cloudflare.com/bots/directory/muse) 列出了一个 user agent 前缀为 `muse-` 的 Muse 客户端，但我们观测到的不带签名的 Muse 浏览器请求发送的是标准 Chrome user agent。

### Muse 的 IP 地址或页面指纹能识别它吗？

Muse 的 IP 地址不能识别该智能体。我们观测到的不带签名的 Muse 请求来自美国移动网络，而不是云厂商。据 Peter James 对 [Muse 浏览器技术栈的拆解](https://mouse.dev/blog/muse-browser/)，Muse 通过用户所在地附近的住宅出口路由浏览器流量，因此封禁数据中心 IP 地址的规则并不适用。

Muse 的页面指纹也不能识别该智能体。Meta 描述了一个浏览器子智能体，它基于无障碍树快照工作，不能在页面中运行 JavaScript，并通过一个关闭了 DevTools 的独立代理驱动 Chromium。在那种 Muse 浏览器环境中，`navigator.webdriver` 为 `false`，页面没有自动化全局变量，也没有被改写的浏览器 API。要识别 Muse，请看 Muse 浏览器运行的环境。

## 为什么单一信号不够？

单靠 SwiftShader 不足以检测 Muse，因为真实机器上也会出现软件渲染。Muse 的 WebGL 渲染器是 [SwiftShader](https://chromium.googlesource.com/chromium/src/+/main/docs/gpu/swiftshader.md)，即 Chromium 对 Vulkan 与 OpenGL ES 图形 API 的 CPU 实现：

```
ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (LLVM 10.0.0) (0x0000C0DE)),

SwiftShader driver)
```

Chrome 过去在 Chromium 无法使用 GPU 时会自动回退到 SwiftShader。自 2025 年末起，Chrome [不再这样做](https://groups.google.com/a/chromium.org/g/blink-dev/c/yhFguWS_3pM)。现在只有命令行标志或 [`EnableUnsafeSwiftShader`](https://chromeenterprise.google/policies/enable-unsafe-swift-shader/) 企业策略打开 SwiftShader 时，SwiftShader 才会渲染 WebGL。Chromium 把该标志的用途记载为在没有 GPU 的服务器上测试，该企业策略则面向受管理的虚拟机和远程桌面。仅凭软件渲染就拒绝的规则会挡住真实的订阅者。

Advanced Signals 把 SwiftShader 当作信誉证据。每个信号都会加分，只有足够多相互独立的信号一致时，Signals 才会拒绝请求。关于 Arcjet 为何这样评分的更多信息，见[机器人检测并不完美](/blog/bot-detection-isnt-perfect)。要识别 Muse，Signals 需要第二个不依赖渲染器的信号。

## CPU 架构客户端提示有什么帮助？

CPU 架构客户端提示有助于检测 Muse，因为 Muse 浏览器报告 `arm`，而精简版 Linux user agent 却写着 `X11; Linux x86_64`。这些值描述的是 ARM Linux 上的 Chromium，而不是伪造的架构标记。

Chromium 通过 [User-Agent Client Hints](https://developer.mozilla.org/en-US/docs/Web/API/User-Agent_Client_Hints_API) 暴露真实架构。自 Chrome 107 起，[User-Agent 精简](https://www.chromium.org/updates/ua-reduction/)冻结了平台标记。在 Linux 上，[精简后的 user agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/User-agent_reduction) 无论 CPU 是什么，总是写着 `X11; Linux x86_64`。客户端提示是真实架构唯一出现的地方。

ARM Linux Chromium 的用户既包括真人也包括智能体。第一，树莓派用户，除非选择 Firefox，其[默认浏览器是 Chromium](https://www.raspberrypi.com/documentation/computers/configuration.html#change-default-browser)。第二，在 ARM 笔记本上运行 Linux 的人。第三，在 Apple 芯片 Mac 上运行 Linux 虚拟机的人。Windows on ARM 笔记本也会报告 `arm`，但 Windows 的 user agent 写着 `Windows NT 10.0; Win64; x64`，Signals 对这些笔记本会忽略架构。

### 两个信号如何结合？

软件渲染意味着 Muse 浏览器没有 GPU。架构提示意味着 Muse 机器运行 ARM Linux。两者合起来描述了一台没有 GPU 的 ARM Linux 机器。Meta 没有公布 Muse 浏览器运行的硬件。根据浏览器技术栈拆解，Muse 浏览器运行在一台独立的虚拟机上，该虚拟机从为浏览器任务构建的机器池中租用。

最可能同时匹配两个信号的人，是在没有 GPU 直通的 ARM Linux 虚拟机中运行 Chromium 的开发者。在面向真人的表单上，Arcjet 接受这一权衡。Advanced Signals 给架构检查的权重高于渲染器，但不足以仅凭架构就拒绝请求。当 Muse 提交 console.dev 订阅表单时，Signals 拒绝了该 Muse 请求并报告了两个信号。

### 如何自己读取这些信号？

在浏览器中用 [`navigator.userAgentData.getHighEntropyValues(["architecture"])`](https://developer.mozilla.org/en-US/docs/Web/API/NavigatorUAData/getHighEntropyValues) 读取类似 Muse 的信号以获取 CPU 架构，用 [`WEBGL_debug_renderer_info`](https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_debug_renderer_info) 扩展获取渲染器字符串。把这两个值发送到服务器，并与其他机器人信号一起评分。例如，下面的函数在浏览器中读取架构与渲染器：

```
async function browserEnvironment() {

// User-Agent Client Hints are Chromium-only and need a secure context.

const uaData = navigator.userAgentData;

const { architecture = "" } = uaData

? await uaData.getHighEntropyValues(["architecture"])

: {};

const gl = document.createElement("canvas").getContext("webgl");

const debug = gl?.getExtension("WEBGL_debug_renderer_info");

const renderer = debug ? gl.getParameter(debug.UNMASKED_RENDERER_WEBGL) : "";

return { userAgent: navigator.userAgent, architecture, renderer };

}
```

下面的函数检查本文描述的 ARM Linux 加 SwiftShader 组合：

```
function looksLikeArmLinuxVm({ userAgent, architecture, renderer }) {

const linuxUserAgent = userAgent.toLowerCase().includes("linux x86_64)");

const arm = architecture === "arm" || architecture === "arm64";

const softwareGpu = /swiftshader/i.test(renderer);

return linuxUserAgent && arm && softwareGpu;

}
```

浏览器可以伪造它报告的任何东西。把这些值当作评分的一项输入，并检查遥测数据中是否有篡改迹象。Advanced Signals 两者都做。Firefox 与 Safari [不支持 User-Agent Client Hints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-UA-Arch#browser_compatibility)，因此缺少架构值不能作为任何证据。要在不用 JavaScript 的情况下读取架构，可返回一个包含 `Sec-CH-UA-Arch` 的 [`Accept-CH`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-CH) 响应头。Chromium 随后会在之后发往你源的请求中带上 [`Sec-CH-UA-Arch`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-UA-Arch) 请求头。

## Muse 在生产环境中报告什么？

我们对 Arcjet 全球平台流量的分析发现，Muse 浏览器通常报告 `X11; Linux x86_64` 上的 Chrome 154、客户端提示架构 `arm`、经 Vulkan 上 ANGLE 的 SwiftShader、6 个逻辑 CPU，以及约 16 GB 设备内存。把这些 Muse 硬件值视为不稳定；持久的信号是没有 GPU 的 ARM Linux。

Muse 的浏览器在这部分流量中报告一致的配置：

| 属性 | 值 |
| --- | --- |
| User agent | `X11; Linux x86_64` 上的 Chrome 154 |
| 客户端提示品牌 | 只有 `Chromium`，没有 `Google Chrome` |
| 客户端提示架构 | `arm` |
| WebGL 渲染器 | 经 Vulkan 上 ANGLE 的 SwiftShader |
| 逻辑 CPU 核数 | 6 |
| 设备内存 | 16 GB，有时 8 GB |
| 屏幕 | 通常 1920×1080 |
| 语音合成声音 | 无 |
| 时区 | 不固定 |

### 哪些 Muse 取值应当避免匹配？

浏览器会对 Muse 环境的某些值做舍入。例如，`navigator.deviceMemory` 报告 2 的幂，且[自 Chrome 147 起](https://developer.chrome.com/release-notes/147)桌面版 Chrome 最多报告 32 GB。这些 Muse 值描述的是运行浏览器的机器，而不是运行智能体的虚拟机。

据 Rohan Adwankar 对 [Muse 智能体虚拟机的拆解](https://rohanadwankar.github.io/posts/sandbox2.html)，该智能体 VM 在 x86 主机上有 2 个虚拟 CPU 和 8 GB 内存。浏览器技术栈拆解还发现了一条回退路径：如果 Muse 租不到浏览器机器，Muse 就在智能体自己的虚拟机内运行浏览器。走这条回退路径的浏览器运行在 x86 上，因此不会报告 `arm`。

不要写匹配 Muse 核心数、内存或屏幕尺寸的规则。Meta 可以随时更改这些虚拟机设置，而且每个值在真实设备上都很常见。Muse 的环境——一台没有 GPU 的 ARM Linux 机器——是更可靠的信号。Meta 也可能改变这一点，例如改用 x86 主机或增加 GPU。

## 如何把智能体引导到正确的接口？

通过拒绝真人表单并返回指向你的智能体接口的响应，把 Muse 和其他浏览器智能体引导到你的 API。Advanced Signals 告诉你的应用有浏览器智能体正在提交表单；接下来做什么由你的应用决定。

在 console.dev，这个决定来自每个接口的用途。console.dev 的订阅表单是给真人的。智能体使用 console.dev 的 [API 或 MCP 服务器](https://console.dev/developers)，而代表真人行事的智能体仍有受支持的方式为其订阅。拒绝自动表单提交可以让批量注册远离邮件列表，同时不关闭这条路径。

据 Meta 关于[个人智能体与企业](https://www.facebook.com/business/news/a-new-way-for-businesses-and-personal-agents-to-work-together)的文章，企业应当能够「把智能体引导到在规模化时效果更好的技能与连接器」，以便 Muse 能「遵循企业偏好的路径」。Meta 与 Sierra 为此发起了作为开放标准的 [Personal Agent Protocol](https://sierra.ai/blog/introducing-personal-agent-protocol)，[规范](https://personalagentprotocol.org/docs/1.0/spec) 1.0 版于 2026 年 11 月 14 日发布。发布 `poppy.json` 的站点就给了 Muse 这条偏好路径，[如何接受 Muse 的 Poppy 会话？](#accept-poppy)一节会讲到。

### 如何用 Arcjet 强制执行？

要用 Arcjet 强制执行 Muse 检测，拒绝该表单提交并返回指向你的 API 的响应。下面的路由处理器使用 Arcjet Next.js SDK：

```
import arcjet, { detectBot } from "@arcjet/next";

import { NextResponse } from "next/server";

const aj = arcjet({

key: process.env.ARCJET_KEY!,

rules: [

detectBot({

mode: "LIVE",

allow: [], // deny every detected bot on this form

}),

],

});

export async function POST(req: Request) {

const decision = await aj.protect(req);

if (decision.isDenied()) {

return NextResponse.json(

{

error: "This form is for people. Agents can use the API.",

docs: "https://example.com/developers",

},

{ status: 403 },

);

}

// Add the subscriber.

return NextResponse.json({ status: "accepted" });

}
```

Arcjet 把 Signals 拒绝的请求报告为以 `ARCJET_SIGNALS` 为机器人原因，机器人身份 kind 为 `AUTOMATION`、evidence 为 `FINGERPRINT`。空的 `allow` 列表也会拒绝验证通过的 `META_MUSE` 请求，在面向真人的表单上这正是本意。要在强制执行之前查看智能体多久访问一次表单，先把 `mode` 设为 `"DRY_RUN"`。智能体也可以自我表明身份。ChatGPT 的云端浏览器用 [HTTP 消息签名](/learn/identify-ai-agents-and-bots#signatures)[为 ChatGPT 请求签名](https://help.openai.com/en/articles/11845367-chatgpt-works-cloud-browser-allowlisting)，因此站点可以验证该智能体，而不必从浏览器环境推断。

要在你的表单上识别未签名的 Muse 请求与其他浏览器智能体，请把 [Signals 脚本](https://docs.arcjet.com/bot-protection/advanced-signals)加到通往这些表单的页面，并在路由处理器中配置 `detectBot`。[Advanced Signals 文档](https://docs.arcjet.com/bot-protection/advanced-signals)包含 Next.js、Python 及其他框架的示例。Signals 与签名在同一条规则中生效：带签名的 Muse 请求获得具名身份，未签名的仍会经过浏览器检查。

## 如何接受 Muse 的 Poppy 会话？

要接受 Muse 的 Personal Agent Protocol 会话，请从你的授权服务器发布 `/.well-known/poppy.json`，其中包含 Muse 登录所用的 OAuth 端点，然后在路由处理器中检查机器人身份上的 `delegated`。Arcjet 验证 `Poppy-Session` 令牌，并报告 `META_MUSE`、evidence 为 `SIGNATURE`、`delegated` 为 `true`。你的授权服务器负责校验访问令牌及其 scope。

验证通过的会话证明两件事：请求由 Muse 发出，且 Muse 代表其某位用户行事。它不会告诉你用户是谁。用户的 `sub` 是一个假名 ID，每家企业的值不同，Arcjet 不记录也不存储它。它也不能证明该用户批准了这个具体操作，因此购买与账户变更仍需要你自己的检查。关于该协议的更多信息，见[什么是 Personal Agent Protocol？](/learn/personal-agent-protocol)。

### 接受 Muse 的会话涉及哪些步骤？

接受 Muse 的会话涉及以下步骤：

1. **发布 `poppy.json`。** 你的授权服务器提供 `/.well-known/poppy.json` 及其 OAuth 端点。Muse 只向发布该文件的站点发送会话。
2. **决定你接受哪些智能体。** 根据[规范](https://personalagentprotocol.org/docs/1.0/spec)第 4.1 节，由企业决定接受哪些智能体。Muse 的 `client_id` 是 `https://muse.ai/poppy/agent.json`。
3. **让 Muse 通过 OAuth 登录。** Muse 通过你的授权服务器登录，使用由该用户批准的 scope，而不是使用该用户的密码。
4. **在每个请求上验证会话。** 在 Muse 使用的路由的 `detectBot` 规则中加入 `META_MUSE` 或 `CATEGORY:AI_AGENT`，并从身份中读取 `delegated`。
5. **授权该操作。** 检查访问令牌及其 scope，并对购买及其他不可逆操作施加你自己的限制。

我们于 2026 年 11 月 16 日获取的 Muse 元数据文档将 `https://muse.ai/poppy/jwks.json` 列为它的 `jwks_uri`，授权类型为 `authorization_code` 与 `refresh_token`，在你的令牌端点使用 `private_key_jwt` 客户端认证，访问令牌绑定 DPoP。请按这些值配置你的授权服务器，或在依赖它们之前重新检查该文档。

### 如何在代码中检查 Muse 会话？

要在代码中检查 Muse 会话，读取[如何检测 Muse 的签名请求？](#signed-muse)中辅助函数返回的身份上的 `delegated`。下面的 JavaScript 示例扩展了 Express 路由：

```
const muse = verifiedMuse(decision);

if (muse?.delegated) {

// A verified Poppy session: META_MUSE SIGNATURE muse.ai true.

// Check the access token and its scopes with your authorization server.

}
```

在 Python 中检查 `muse is not None and muse.delegated`。在 Go 中检查 `muse != nil && muse.Delegated`。

Arcjet 只为在 well-known-bots 目录中经过审查的智能体验证会话，Muse 的 `client_id` 就在该目录中。它不会按请求提供的 `client_id` 去抓取，因此请求无法让 Arcjet 抓取发送者选定的 URL。Arcjet 针对请求校验会话——委托关系、签名、方法与 URL、以及新鲜度——而不针对 `aud` 或访问令牌。验证失败的会话不会改变身份：请求回退到 Web Bot Auth 签名（如果有），然后回退到本文前面各节描述的浏览器信号。

### 什么样的策略适合被委托的 Muse 请求？

在其 OAuth scope 覆盖的路由上，被委托的 Muse 请求可以有理由获得与已登录用户相同的待遇。会话使 Muse 成为代表真实账户持有人行事的已知智能体，访问令牌告诉你该用户批准了什么。请保留以下限制：

- **把仅限真人的表单留给真人。** 新闻简报表单（例如 console.dev 订阅表单）仍可拒绝所有机器人并把智能体引导到 API。
- **保持速率限制开启。** 按机器人 ID 或账户来设置键，这样一个智能体就无法占用真人所需要的容量。
- **在你自己的流程中确认不可逆操作。** 会话不能证明用户批准了某笔具体购买。

关于代表用户行事的智能体策略的更多信息，见 [AI 智能体的代表身份](/learn/ai-agent-on-behalf-of-identity)。同样的方法应用于 OpenAI 的已签名云端浏览器，见[如何检测 ChatGPT 智能体](/learn/how-to-detect-chatgpt-agent)。

## 常见问题

Muse 会对它的请求签名吗？

会。Muse 在 https://muse.ai/.well-known/http-message-signatures-directory 发布 Web Bot Auth 密钥目录，并用这些密钥为请求签名。Arcjet 验证签名并把该请求报告为 META_MUSE，evidence 为 SIGNATURE，operator 为 muse.ai。

Muse 支持 Personal Agent Protocol 吗？

支持。Muse 发布 Poppy client_id https://muse.ai/poppy/agent.json，Meta 称 Muse 是第一个支持 Poppy 的个人智能体。在发布了 /.well-known/poppy.json 的站点上，Muse 发送 Poppy-Session 令牌，Arcjet 把验证通过的会话报告为 delegated 置为 true。

验证通过的 Muse 会话能识别用户吗？

不能。验证通过的 Poppy 会话证明请求由 Muse 发出且 Muse 代表其某位用户行事。用户的 sub 是一个假名 ID，每家企业的值不同，会话也不能证明该用户批准了某个具体操作。

Muse 会在 User-Agent 请求头中表明身份吗？

不会。Muse 的浏览器发送标准的 Chrome-on-Linux User-Agent，不含智能体名称。Cloudflare Radar 为某个 Muse 客户端列出了 muse- 前缀，但我们观测到的不带签名的 Muse 浏览器请求并未使用它。请改用签名或 Poppy 会话识别 Muse。

如何检测未签名的 Muse 请求？

组合浏览器信号。未签名的 Muse 请求在 Chrome 精简版 X11; Linux x86_64 user agent 上报告 SwiftShader 软件渲染和 arm 架构客户端提示。单一信号都不够，因此要把它俩作为评分的输入——Arcjet Advanced Signals 就是这么做的。

能用 IP 地址封禁 Muse 吗？

不能可靠地按 IP 地址封禁 Muse。观测到的 Muse 浏览器流量来自住宅移动网络，而对 Muse 浏览器技术栈的拆解发现 Muse 通过用户附近的住宅出口路由浏览器出口流量。要拒绝带签名的 Muse 请求，在拒绝列表中指名 META_MUSE。

我应该在每条路由上都拒绝 Muse 吗？

不应该。拒绝面向真人的表单，并把智能体引导到你的 API 或 MCP 服务器。在 Muse 的 OAuth scope 覆盖的路由上，被委托的 Muse 请求可以获得与已登录用户相同的待遇，同时保留速率限制和你自己对购买的检查。

**技术审校：** Arcjet 安全工程团队会对照一手标准、当前厂商文档以及文中描述的强制执行行为审校本指南。反映 Arcjet 工程判断的建议会标注出来。要报告错误或提出更正，请发邮件至 [support@arcjet.com](mailto:support@arcjet.com)。

你代码中的应用安全
