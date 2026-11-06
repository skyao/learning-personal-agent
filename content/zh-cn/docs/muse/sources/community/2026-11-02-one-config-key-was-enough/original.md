来源：https://coderlegion.com/32498/one-config-key-was-enough-what-the-meta-muse-zero-day-teaches-about-agent-trust-boundaries
取文：2026-11-05，直接下载

## One Config Key Was Enough: What the Meta Muse Zero-Day Teaches About Agent Trust Boundaries

#### Meta built Muse with per-account VMs, an isolated credential store, and a broker that keeps real tokens away from the model. A single undocumented preference on the Mac client made most of that irrelevant. Here is why, and what it means for anyone shipping an agent.

Most agent security writing starts with threat models. This one starts with a string:

```
endo_voyager_dictation_endpoint
```

That is an undocumented macOS preference key in Meta's Muse desktop client. It set the destination for dictation audio. It was writable by any unprivileged process running as the logged-in user, which means a shell one-liner could point the agent's voice traffic at a server the attacker controls. Patrick Wardle of the Objective-See Foundation found it and published a proof of concept called not-a-mused. Meta pulled the key from production builds within about a day, and Wardle confirmed the fix on September 22, 2026.

No CVE was assigned. Meta's position was that the issue required prior code execution on the machine, so it was a local configuration problem rather than a remote exploit. That framing is technically correct and practically beside the point, which is the part worth unpacking.

### The payload was not the audio

Redirecting a microphone stream is bad. Redirecting it along with a valid session token is a different category of problem.

The rerouted request carried the user's Muse authentication token. An attacker running a transparent proxy could capture the token, forward the traffic to Meta so nothing looked broken, and then use that token to drive the agent directly. At that point the attacker is not exfiltrating data from an app. They are issuing instructions to an authenticated agent that already holds broad permissions on the host and in the user's connected accounts.

This is the pattern [NeuralTrust calls excessive agency](https://neuraltrust.ai/blog/excessive-agency), and OWASP tracks it as [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm06/) in its GenAI risk list. The agent does not misbehave. It does exactly what it was built to do, for whoever is holding the token.

### Server-side isolation does not cover a client-side trust boundary

Muse's architecture is genuinely more careful than most. Each account gets a dedicated cloud VM. Connected-service credentials live in a separate store outside the agent's runtime. A host-side component called Sentinel approves connector actions and swaps the real credential in at the network boundary, so the model never handles the secret. Meta also runs a bug bounty with awards up to $300,000, including up to $130,000 for a working prompt injection against a single user.

None of that was defeated. It was bypassed, because the vulnerability sat on the other side of the boundary. Wardle himself noted the cloud protections held. The flaw was in the client, and the client is where the identity lives.

If you are building an agent, the lesson generalizes cleanly. Your token broker, policy engine, and sandboxed execution environment are all downstream of whatever process can impersonate the user. A local config file that is world-writable by the user account is part of your attack surface, and on desktop it is usually the weakest part. Practical checks worth running on your own client:

- Can any user-level process modify runtime endpoints, model routes, or connector targets after install?
- Are debug and staging keys stripped from release builds, or just undocumented?
- Does the client pin the endpoints it will send credentialed traffic to, or does it trust configuration?

That last one is the cheap fix. Endpoint selection that carries a session token should not be data. It should be code.

```
ALLOWED_ENDPOINTS = frozenset({
    "https://voice.example-agent.com/v1/stream",
    "https://voice-eu.example-agent.com/v1/stream",
})

def resolve_endpoint(configured_value: str) -> str:
    if configured_value not in ALLOWED_ENDPOINTS:
        raise ConfigurationError(
            f"refusing credentialed request to unpinned endpoint: {configured_value}"
        )
    return configured_value
```

Ten lines. It would have turned a token hijack into a log entry.

### The enterprise gap is telemetry, not patching

The patch shipped fast. What did not ship is any way for a security team to see the agent at all.

VentureBeat's reporting found no SIEM audit export, no IT admin console, and no DLP integration in Muse's launch documentation or in the consumer product it tested. Individual users get an action audit trail. Organizations get nothing. Muse crossed 2.5 million downloads in its first 13 days according to Sensor Tower, so the population of employees running it on machines with corporate data is not hypothetical.

There is a subtler detection problem underneath. When an employee connects a service to Muse using an API key, no OAuth grant is created. If your shadow-AI monitoring works by watching for new OAuth grants against corporate identity providers, which most of it does, the connection is invisible. You would need API key issuance logs from each connected service plus that service's own audit trail to reconstruct what happened.

The practical move is not to chase Muse specifically. It is to treat any agent that can authenticate as a user as an identity in your inventory, with the same expectations you apply to a service account: known credentials, known scope, reviewable action logs. [NeuralTrust's full CISO breakdown of the Muse incident](https://neuraltrust.ai/blog/meta-muse-ai-agent-security) goes into the control mapping in more detail, and [agentsecurity.com](https://agentsecurity.com/) collects the broader pattern library for tool abuse, privilege escalation, and memory poisoning if you want the taxonomy rather than the incident.

### What actually reduces blast radius

Three things, in order of how much they buy you.

**Approval gates on irreversible actions.** Sending email, moving money, and writing to external systems should require a human confirmation that is bound to the specific action, not a blanket session-level grant. An attacker with a token should still hit a wall at the first consequential step.

**Scope your tokens like you mean it.** An agent credential that can read every connected service is a single point of total compromise. Per-connector tokens with narrow scopes and short lifetimes turn one stolen token into one stolen capability.

**Runtime inspection of what the agent is doing.** Static permission review tells you what the agent could do. It does not tell you that the agent is currently being steered by an injected instruction. This is what [runtime agent security](https://neuraltrust.ai/ai-agent-security) exists for: watching the interaction stream and intervening during execution rather than reconstructing it afterward from logs that may not exist.

### The takeaway

The Muse bug was simple, it was patched quickly, and it never had a CVE. It is still the most instructive agent security incident of the year, because it shows that the hard part of agent security is not model behavior. It is identity. An agent is a credential with a planner attached. Protect the credential and constrain the planner, and the model is a much smaller problem than it looks.
