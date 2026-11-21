来源：https://arcjet.com/learn/how-to-detect-metas-muse-ai-agent
取文：2026-11-21，直接下载

**In short:** Meta's Muse signs requests with Web Bot Auth, using keys at https://muse.ai/.well-known/http-message-signatures-directory, and presents Personal Agent Protocol (Poppy) sessions with the client\_id https://muse.ai/poppy/agent.json on sites that publish /.well-known/poppy.json. Arcjet reports a verified Muse request as META\_MUSE with kind AI\_AGENT, SIGNATURE evidence, and operator muse.ai, and sets delegated to true for a Poppy session. Muse requests with no signature or session look like Chrome on Linux, so detect them from SwiftShader rendering plus an ARM architecture client hint, deny human-only forms, and point agents at your API.

## What is Meta's Muse?

[Meta's Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) is a personal agent that browses the web for a person from a cloud-hosted Chromium browser. To detect Meta's Muse AI agent, verify its signatures: Muse signs requests with [Web Bot Auth](/learn/web-bot-auth) and presents [Personal Agent Protocol](/learn/personal-agent-protocol) (Poppy) sessions, and Arcjet reports both as the bot `META_MUSE` with `SIGNATURE` evidence. For a Muse request that carries no signature or session, fall back to browser signals: SwiftShader software rendering plus an ARM architecture client hint on Chrome's reduced `X11; Linux x86_64` user agent.

Meta launched Muse on September 8, 2026. Muse opens a browser, reads pages, [fills in forms, and completes purchases](https://www.meta.com/help/artificial-intelligence/2124746764949121/). Each person gets a Linux virtual machine in the cloud, with a Chromium-based browser that the person can watch and take over. The browser sends a standard Chrome-on-Linux `User-Agent` header with no agent name, so the header doesn't tell you that Muse sent the request. A signature or a session does.

As of November 2026, Muse identifies itself in two ways, and you can use either or both:

- **Web Bot Auth.** Muse publishes a key directory at `https://muse.ai/.well-known/http-message-signatures-directory` and signs requests with the matching keys. A verified signature proves that the request came from Muse's infrastructure.
- **Personal Agent Protocol.** Muse publishes a Poppy `client_id` at `https://muse.ai/poppy/agent.json`. On sites that publish `/.well-known/poppy.json`, Muse sends a `Poppy-Session` token that proves the request comes from Muse and that Muse acts for one of its users. Meta's [Poppy announcement](https://muse.ai/blog/poppy-personal-agent-protocol) calls Muse "the first personal agent to support Poppy".

[console.dev](https://console.dev/), a weekly developer tools newsletter, shows where each method fits. The console.dev subscribe form is for people. Agents use the console.dev [API and MCP server](https://console.dev/developers). Arcjet [Advanced Signals](/blog/announcing-advanced-bot-signals-to-detect-automation-without-captchas) protects the form so automated signups stay off the mailing list and agents use the API instead. A verified Muse identity lets the same site name the agent on its other routes instead of inferring it from the browser environment.

For more information about named agents and request signatures, see [How to identify AI agents and bots](/learn/identify-ai-agents-and-bots). For more information about classifying agents that hit your forms, see [AI agent bot management](/learn/ai-agent-bot-management).

## How do you detect Muse's signed requests?

You detect Muse's signed requests by verifying the Web Bot Auth signature against the key directory on `muse.ai`. Arcjet does this inside the `detectBot` rule and reports a verified Muse request as the bot ID `META_MUSE`, with kind `AI_AGENT`, evidence `SIGNATURE`, and operator `muse.ai`. The signature identifies Muse, not the person who asked Muse to act.

A signed Muse request carries the three Web Bot Auth headers. `Signature-Agent` names the `https://muse.ai` origin, `Signature-Input` lists the signed components with the tag `web-bot-auth`, and `Signature` carries the bytes. Your verifier fetches the keys from Muse's directory and checks the signature over the request it received. On November 16, 2026, Muse's directory held two Ed25519 keys, set `Cache-Control: must-revalidate, max-age=3600`, and signed its own responses with the tag `http-message-signatures-directory`.

The following table lists the fields of the bot identity that Arcjet reports for each way that Muse can reach your site:

| Request | `botId` | `kind` | `evidence` | `operator` | `delegated` |
| --- | --- | --- | --- | --- | --- |
| Web Bot Auth signature verified | `META_MUSE` | `AI_AGENT` | `SIGNATURE` | `muse.ai` | `false` |
| Poppy session verified | `META_MUSE` | `AI_AGENT` | `SIGNATURE` | `muse.ai` | `true` |
| No signature or session, and the Signals check fails | Empty | `AUTOMATION` | `FINGERPRINT` | Empty | `false` |
| No signature or session, and the Signals check passes | No identity | None | None | None | None |

`META_MUSE` is in the open source [well-known-bots](https://github.com/arcjet/well-known-bots) catalog, in `CATEGORY:AI`, `CATEGORY:AI_AGENT`, and `CATEGORY:META`. Arcjet trusts Muse's directory and `client_id` because the catalog lists them, not because a request names them. An allow list that includes `CATEGORY:AI_AGENT` or `META_MUSE` allows a verified Muse request, and a deny list that names either one denies it.

A verified signature is only as useful as the path your framework hands Arcjet. Signatures that cover `@path` need the original request path, which some adapters, such as the Next.js App Router, don't supply. For the list, see [which frameworks preserve the signed path](/learn/web-bot-auth#arcjet-adapters).

### Detect Muse in JavaScript

The following Express app allows search engines and Muse on product pages, and logs the identity of each verified Muse request:

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

`isAiAgent` is true for a `LIVE` result with kind `AI_AGENT` that isn't spoofed. It doesn't check evidence, so the helper function checks for `SIGNATURE` itself.

### Detect Muse in Python

The following FastAPI route does the same with `is_ai_agent` and `reason_v2`:

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

### Detect Muse in Go

The following `net/http` handler reads the identity from `result.Reason.Bot.Identity`:

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

Only Arcjet Cloud computes the identity. A decision that the SDK makes locally, such as a denial from its local bot detection, has no identity.

## What does an unsigned Muse request look like to your server?

A Muse request that carries no signature or session is an ordinary Chrome-on-Linux form submission from the server's point of view. The following sections cover that fallback case: requests that reach a route without a Web Bot Auth signature or a Poppy session, including every Muse request to a site that doesn't publish `poppy.json` and that Muse doesn't sign. The Muse `User-Agent` claims Chrome 154 on Linux, and the accompanying headers match a real browser `POST`:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)

Chrome/154.0.0.0 Safari/537.36
```

According to the [Chromium release schedule](https://chromiumdash.appspot.com/schedule), Chrome 154 reached the stable channel on September 22, 2026. That date fits Meta's description of "a real up-to-date Chromium based browser". Headers, IP addresses, and page automation fingerprints still do not name Muse, so recognition depends on browser environment signals.

### Do unsigned Muse headers identify the agent?

Unsigned Muse request headers don't identify the agent. Muse sends `Sec-CH-UA` for Chromium 154, `Sec-CH-UA-Platform` as `"Linux"`, and `Sec-Fetch-*`, `Origin`, and `Referer` values that match a real form submission. The Muse user agent has no agent name, and an unsigned request has no `Signature-Agent` or `Poppy-Session` header, so the [usual ways to identify an AI agent](/learn/identify-ai-agents-and-bots) don't apply.

According to Meta, "When Muse browses the internet, it will appear as your activity." When Amazon [blocked Muse from its store](https://www.geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping/) in September 2026, Amazon said Muse doesn't identify itself. [Cloudflare Radar](https://radar.cloudflare.com/bots/directory/muse) lists a Muse client with the user agent prefix `muse-`, but the unsigned Muse browser requests that we observed sent the standard Chrome user agent instead.

### Do Muse IP addresses or page fingerprints identify it?

Muse IP addresses don't identify the agent. The unsigned Muse request that we observed came from a US mobile network, not a cloud provider. According to Peter James's [teardown of Muse's browser stack](https://mouse.dev/blog/muse-browser/), Muse routes browser traffic through residential exits near the person's location, so a rule that blocks data center IP addresses doesn't apply.

Muse page fingerprints do not identify the agent either. Meta describes a browser sub-agent that works from an accessibility tree snapshot, can't run JavaScript in the page, and drives Chromium through a separate broker with DevTools turned off. In that Muse browser environment, `navigator.webdriver` is `false`, and the page has no automation globals or patched browser APIs. To recognize Muse, look at the environment that the Muse browser runs in.

## Why isn't one signal enough?

SwiftShader alone is not enough to detect Muse, because software rendering still appears on real machines. Muse's WebGL renderer is [SwiftShader](https://chromium.googlesource.com/chromium/src/+/main/docs/gpu/swiftshader.md), Chromium's CPU implementation of the Vulkan and OpenGL ES graphics APIs:

```
ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (LLVM 10.0.0) (0x0000C0DE)),

SwiftShader driver)
```

Chrome used to fall back to SwiftShader automatically when Chromium couldn't use a GPU. Since late 2025, Chrome [no longer does that](https://groups.google.com/a/chromium.org/g/blink-dev/c/yhFguWS_3pM). SwiftShader now renders WebGL only when a command-line flag or the [`EnableUnsafeSwiftShader`](https://chromeenterprise.google/policies/enable-unsafe-swift-shader/) enterprise policy turns SwiftShader on. Chromium documents that flag for testing on servers without a GPU, and the enterprise policy exists for managed virtual machines and remote desktops. A rule that denies on software rendering alone blocks real subscribers.

Advanced Signals treats SwiftShader as reputation evidence. Each signal adds to a score, and Signals denies a request only when enough independent signals agree. For more information about why Arcjet scores this way, see [Bot detection isn't perfect](/blog/bot-detection-isnt-perfect). To recognize Muse, Signals needs a second signal that doesn't depend on the renderer.

## How do CPU architecture client hints help?

CPU architecture client hints help detect Muse because the Muse browser reports `arm` while the reduced Linux user agent says `X11; Linux x86_64`. Those values describe Chromium on ARM Linux, not a spoofed architecture token.

Chromium exposes the real architecture through [User-Agent Client Hints](https://developer.mozilla.org/en-US/docs/Web/API/User-Agent_Client_Hints_API). Since Chrome 107, [User-Agent reduction](https://www.chromium.org/updates/ua-reduction/) freezes the platform token. On Linux, the [reduced user agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/User-agent_reduction) always says `X11; Linux x86_64`, whatever the CPU. The client hint is the only place where the real architecture appears.

ARM Linux Chromium includes people as well as agents. First, Raspberry Pi owners, whose [default browser is Chromium](https://www.raspberrypi.com/documentation/computers/configuration.html#change-default-browser) unless Firefox is chosen. Second, people who run Linux on ARM laptops. Third, developers who run a Linux virtual machine on an Apple silicon Mac. Windows on ARM laptops also report `arm`, but the Windows user agent says `Windows NT 10.0; Win64; x64`, and Signals ignores architecture for those laptops.

### How do the two signals combine?

Software rendering means that the Muse browser has no GPU. The architecture hint means that the Muse machine runs ARM Linux. Together those signals describe an ARM Linux machine without a GPU. Meta doesn't publish the hardware that the Muse browser runs on. According to the browser stack teardown, the Muse browser runs on a separate virtual machine leased from a pool of machines built for browser tasks.

The people most likely to match both signals are developers who run Chromium in an ARM Linux virtual machine without GPU passthrough. On a form that's meant for people, Arcjet accepts that tradeoff. Advanced Signals weights the architecture check more heavily than the renderer, but not enough to deny a request on architecture alone. When Muse submitted the console.dev subscribe form, Signals denied the Muse request and reported both signals.

### How do you read the signals yourself?

Read Muse-like signals in the browser with [`navigator.userAgentData.getHighEntropyValues(["architecture"])`](https://developer.mozilla.org/en-US/docs/Web/API/NavigatorUAData/getHighEntropyValues) for the CPU architecture and the [`WEBGL_debug_renderer_info`](https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_debug_renderer_info) extension for the renderer string. Send both values to your server and score those values with your other bot signals. For example, the following function reads the architecture and renderer in the browser:

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

The following function checks for the ARM Linux plus SwiftShader combination that this article describes:

```
function looksLikeArmLinuxVm({ userAgent, architecture, renderer }) {

const linuxUserAgent = userAgent.toLowerCase().includes("linux x86_64)");

const arm = architecture === "arm" || architecture === "arm64";

const softwareGpu = /swiftshader/i.test(renderer);

return linuxUserAgent && arm && softwareGpu;

}
```

A browser can forge anything that the browser reports. Treat these values as one input to a score, and check the telemetry for signs of tampering. Advanced Signals does both. Firefox and Safari [don't support User-Agent Client Hints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-UA-Arch#browser_compatibility), so a missing architecture value isn't evidence of anything. To read the architecture without JavaScript, respond with an [`Accept-CH`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-CH) header that includes `Sec-CH-UA-Arch`. Chromium then sends a [`Sec-CH-UA-Arch`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-UA-Arch) header on later requests to your origin.

## What does Muse report in production?

Our analysis of Arcjet global platform traffic found that the Muse browser typically reports Chrome 154 on `X11; Linux x86_64`, client-hint architecture `arm`, SwiftShader through ANGLE on Vulkan, 6 logical CPUs, and about 16 GB of device memory. Treat those Muse hardware values as unstable; the durable signal is ARM Linux without a GPU.

Muse's browser reports a consistent profile across that traffic:

| Property | Value |
| --- | --- |
| User agent | Chrome 154 on `X11; Linux x86_64` |
| Client hint brands | `Chromium` only, with no `Google Chrome` |
| Client hint architecture | `arm` |
| WebGL renderer | SwiftShader through ANGLE on Vulkan |
| Logical CPU cores | 6 |
| Device memory | 16 GB, sometimes 8 GB |
| Screen | Usually 1920×1080 |
| Speech synthesis voices | None |
| Time zone | Varies |

### Which Muse values should you avoid matching?

Browsers round some Muse environment values. For example, `navigator.deviceMemory` reports a power of two, and [since Chrome 147](https://developer.chrome.com/release-notes/147) desktop Chrome reports up to 32 GB. These Muse values describe the machine that runs the browser, not the virtual machine that runs the agent.

According to Rohan Adwankar's [teardown of the Muse agent virtual machine](https://rohanadwankar.github.io/posts/sandbox2.html), the agent VM has 2 virtual CPUs and 8 GB of memory on an x86 host. The browser stack teardown also found a fallback: if Muse can't lease a browser machine, Muse runs the browser inside the agent's own virtual machine. A browser on that fallback path runs on x86, so that browser doesn't report `arm`.

Don't write a rule that matches the Muse core count, memory, or screen size. Meta can change those virtual machine settings at any time, and each value is common on real devices. The Muse environment, an ARM Linux machine without a GPU, is a more reliable signal. Meta could change that too, for example by moving to x86 hosts or adding GPUs.

## How do you send agents to the right interface?

Send Muse and other browser agents to your API by denying the human form and returning a response that points to your agent interface. Advanced Signals tells your application that a browser agent is submitting the form; your application decides what to do next.

On console.dev, the decision follows from what each interface is for. The console.dev subscribe form is for people. Agents use the console.dev [API or MCP server](https://console.dev/developers), and an agent that acts for a real person still has a supported way to subscribe them. Denying automated form submissions keeps bulk signups off the mailing list without closing that path.

According to Meta's [post on personal agents and businesses](https://www.facebook.com/business/news/a-new-way-for-businesses-and-personal-agents-to-work-together), a business should be able to "refer the agent to skills and connectors that work better at scale", so that Muse can "follow the business's preferred path". Meta and Sierra started the [Personal Agent Protocol](https://sierra.ai/blog/introducing-personal-agent-protocol) as an open standard for this, and version 1.0 of the [specification](https://personalagentprotocol.org/docs/1.0/spec) was published on November 14, 2026. A site that publishes `poppy.json` gives Muse that preferred path, which [How do you accept Muse's Poppy sessions?](#accept-poppy) covers.

### How do you enforce this with Arcjet?

To enforce Muse detection with Arcjet, deny the form submission and return a response that points to your API. The following route handler uses the Arcjet Next.js SDK:

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

Arcjet reports requests that Signals denies with `ARCJET_SIGNALS` as the bot reason, and with a bot identity of kind `AUTOMATION` and `FINGERPRINT` evidence. The empty `allow` list also denies a verified `META_MUSE` request, which is the intent on a form that's meant for people. To see how often agents reach a form before you enforce anything, set `mode` to `"DRY_RUN"` first. Agents can also identify themselves. ChatGPT's cloud browser [signs ChatGPT requests](https://help.openai.com/en/articles/11845367-chatgpt-works-cloud-browser-allowlisting) with [HTTP message signatures](/learn/identify-ai-agents-and-bots#signatures), so a site can verify the agent instead of inferring the agent from the browser environment.

To recognize unsigned Muse requests and other browser agents on your forms, [add the Signals script](https://docs.arcjet.com/bot-protection/advanced-signals) to the pages that lead to those forms, and configure `detectBot` in the route handler. The [Advanced Signals documentation](https://docs.arcjet.com/bot-protection/advanced-signals) includes examples for Next.js, Python, and other frameworks. Signals and signatures work in the same rule: a signed Muse request gets a named identity, and an unsigned one still meets the browser checks.

## How do you accept Muse's Poppy sessions?

To accept Muse's Personal Agent Protocol sessions, publish `/.well-known/poppy.json` from your authorization server with the OAuth endpoints that Muse signs in through, then check `delegated` on the bot identity in your route handler. Arcjet verifies the `Poppy-Session` token and reports `META_MUSE` with `SIGNATURE` evidence and `delegated` set to `true`. Your authorization server checks the access token and its scopes.

A verified session proves two things: Muse sent the request, and Muse acts for one of its users. It doesn't tell you who the user is. The user's `sub` is a pseudonymous ID that's different for each business, and Arcjet doesn't log or store it. It also doesn't prove that the person approved this specific action, so purchases and account changes still need your own checks. For more information about the protocol, see [What is the Personal Agent Protocol?](/learn/personal-agent-protocol).

### What does accepting Muse's sessions involve?

Accepting Muse's sessions involves the following steps:

1. **Publish `poppy.json`.** Your authorization server provides `/.well-known/poppy.json` along with its OAuth endpoints. Muse sends a session only to sites that publish this file.
2. **Decide which agents you accept.** Under section 4.1 of the [specification](https://personalagentprotocol.org/docs/1.0/spec), the business decides which agents it accepts. Muse's `client_id` is `https://muse.ai/poppy/agent.json`.
3. **Let Muse sign in with OAuth.** Muse signs in through your authorization server with scopes that the person approves, instead of with the person's password.
4. **Verify the session on each request.** Add `META_MUSE` or `CATEGORY:AI_AGENT` to the `detectBot` rule on the routes that Muse uses, and read `delegated` from the identity.
5. **Authorize the action.** Check the access token and its scopes, and apply your own limits to purchases and other irreversible actions.

Muse's metadata document, which we fetched on November 16, 2026, lists `https://muse.ai/poppy/jwks.json` as its `jwks_uri`, the `authorization_code` and `refresh_token` grant types, `private_key_jwt` client authentication at your token endpoint, and DPoP-bound access tokens. Configure your authorization server for those values, or check the document again before you rely on them.

### How do you check for a Muse session in code?

To check for a Muse session in code, read `delegated` on the identity that the helper functions in [How do you detect Muse's signed requests?](#signed-muse) return. The following JavaScript example extends the Express route:

```
const muse = verifiedMuse(decision);

if (muse?.delegated) {

// A verified Poppy session: META_MUSE SIGNATURE muse.ai true.

// Check the access token and its scopes with your authorization server.

}
```

In Python, check `muse is not None and muse.delegated`. In Go, check `muse != nil && muse.Delegated`.

Arcjet verifies sessions only for agents vetted in the well-known-bots catalog, where Muse's `client_id` is listed. It doesn't fetch a `client_id` that a request supplies, so a request can't make Arcjet fetch a URL of the sender's choosing. Arcjet checks the session against the request – the delegation, the signatures, the method and URL, and freshness – and not against `aud` or the access token. A session that fails verification doesn't change the identity: the request falls back to the Web Bot Auth signature, if there is one, and then to the browser signals that the earlier sections of this article describe.

### What policy fits a delegated Muse request?

A delegated Muse request can reasonably get what a signed-in person gets on the routes that its OAuth scopes cover. The session makes Muse a known agent acting for a real account holder, and the access token tells you what that person approved. Keep the following limits:

- **Keep human-only forms for people.** A newsletter form, like the console.dev subscribe form, can still deny every bot and point agents at an API.
- **Keep rate limits on.** Key them by bot ID or by account, so that one agent can't use capacity that people need.
- **Confirm irreversible actions in your own flow.** A session doesn't prove that the person approved a specific purchase.

For more information about policy for agents that act for a user, see [AI agent on-behalf-of identity](/learn/ai-agent-on-behalf-of-identity). For the same approach applied to OpenAI's signed cloud browser, see [How to detect ChatGPT agent](/learn/how-to-detect-chatgpt-agent).

## Frequently asked questions

Does Muse sign its requests?

Yes. Muse publishes a Web Bot Auth key directory at https://muse.ai/.well-known/http-message-signatures-directory and signs requests with those keys. Arcjet verifies the signature and reports the request as META\_MUSE with SIGNATURE evidence and the operator muse.ai.

Does Muse support the Personal Agent Protocol?

Yes. Muse publishes the Poppy client\_id https://muse.ai/poppy/agent.json, and Meta calls Muse the first personal agent to support Poppy. On sites that publish /.well-known/poppy.json, Muse sends a Poppy-Session token, and Arcjet reports a verified session with delegated set to true.

Does a verified Muse session identify the user?

No. A verified Poppy session proves that Muse sent the request and acts for one of its users. The user's sub is a pseudonymous ID that's different for each business, and the session doesn't prove that the person approved a specific action.

Does Muse identify itself in the User-Agent header?

No. Muse's browser sends a standard Chrome-on-Linux User-Agent with no agent name. Cloudflare Radar lists a muse- prefix for a Muse client, but the unsigned Muse browser requests that we observed didn't use it. Identify Muse by its signature or Poppy session instead.

How do I detect Muse requests that aren't signed?

Combine browser signals. An unsigned Muse request reports SwiftShader software rendering and an arm architecture client hint on Chrome's reduced X11; Linux x86\_64 user agent. Neither signal is enough alone, so use them as inputs to a score, which is what Arcjet Advanced Signals does.

Can you block Muse by IP address?

You can't reliably block Muse by IP address. Observed Muse browser traffic came from a residential mobile network, and a teardown of Muse's browser stack found that Muse routes browser egress through residential exits near the person. To deny signed Muse requests, name META\_MUSE in a deny list.

Should I deny Muse on every route?

No. Deny forms that are meant for people and point agents at your API or MCP server. On routes that Muse's OAuth scopes cover, a delegated Muse request can get what a signed-in person gets, with rate limits and your own checks on purchases.

**Technical review:** Arcjet Security Engineering reviews this guide against primary standards, current vendor documentation, and the enforcement behavior described in the article. Recommendations that reflect Arcjet's engineering judgment are identified as such. To report an error or suggest a correction, email [support@arcjet.com](mailto:support@arcjet.com).

Application security in your code
