来源：https://www.dsebastien.net/microsoft-autopilot/
取文：2026-11-10，直接下载

Microsoft Autopilot

In short

Microsoft Autopilot is Microsoft's "persistent, proactive and personal agent that keeps working even when you're not". You give it a name, a role and a goal, and it works inside your Microsoft 365 tenant without waiting for prompts: it watches channels, follows up on threads, runs recurring work and

## From Scout to Autopilot

| Date | What happened |
| --- | --- |
| Early 2026 | Satya Nadella reportedly dismissed OpenClaw as a security risk akin to "a virus" (secondhand, via GeekWire; original not found) |
| 31 March 2026 | Omar Shahine moves to a new role leading personal assistants for Microsoft 365 |
| 4 May 2026 | GeekWire (Mary Jo Foley) reports "Project Lobster" / "ClawPilot", an OpenClaw-based desktop environment with 3,000+ daily internal users by 1 May, up from 100 a week before |
| 2 June 2026 | Build: Shahine announces Microsoft Scout as the first agent in a new category called "Autopilots", "powered by OpenClaw open-source technology". Experimental Frontier release, private preview |
| June 2026 | The OpenClaw Foundation and the Windows team announce a long-term collaboration to make Windows a first-class OpenClaw platform |
| 8 July 2026 | The OpenClaw Foundation is formally introduced; Microsoft is listed as a partner that "contributes directly upstream" (not as a donor) |
| July-August 2026 | Monthly Scout releases: model and reasoning controls, session history in OneDrive, To Do, SharePoint Lists, Outlook rules, Teams transcripts, room booking |
| 25 September 2026 | Jared Spataro's post "Introducing the new Copilot with Home, Code and Autopilot". Scout becomes Autopilot, private preview "at the end of the month". The same day, the OpenClaw blog: "Microsoft Autopilot is built on OpenClaw. The contributions go both ways." |
| 17-20 November 2026 | Ignite, where Microsoft says it will share more |

The rename changed more than the name. In June, "Autopilot" was a category and Scout its first member. In September, Autopilot became the product. Scout was a desktop app for Windows 11 and macOS 12 or later; Autopilot is cloud-hosted and "keeps working while you sleep". Whether the desktop app survives under the new name isn't documented.

## What it does

**Autopilot (September, cloud).** It lives in your tenant with "its own identity, memory, computer and workspace", grounded in Microsoft's work data (Microsoft IQ). You @mention it in Teams, Outlook, chats, channels and documents "like a colleague". It has an avatar and a name you choose. Fortune's examples: project updates, tracking decisions and deadlines, reminding colleagues of commitments, gathering prep material, reaching out to partners.

**Scout (June, desktop)**, which is what the documentation still describes:

- Schedules meetings across time zones, flags important ones, prepares material, blocks time for deliverables, spots risks like stalled decisions
- Reads and writes files, runs shell commands, automates a browser, and queries Microsoft 365: Outlook mail and calendar, Teams chats, channels, meetings and transcripts, OneDrive, SharePoint, To Do, room booking, inbox rules
- **Heartbeat**: a periodic prompt every 15, 30, 60 or 120 minutes during work hours, with its own, stricter permission policy. **Automations**: scheduled, condition-triggered or one-shot
- Sub-agents (Explore, Task, Code review, Research, General-purpose)
- Bundled skills for Word, Excel, PowerPoint and Loop, plus your own `SKILL.md` skills
- Co-Create: you and the agent edit the same file at the same time
- Memory across conversations, with session history stored per device in OneDrive

## The OpenClaw connection

Scout was "powered by OpenClaw"; the OpenClaw Foundation says Autopilot "runs on OpenClaw". Microsoft's own September post and the Learn docs don't mention OpenClaw at all.

What Microsoft contributed upstream, per the OpenClaw blog:

- **Policy conformance**: a Policy plugin that compares what an operator requires with the actual configuration and records the results. Microsoft committed to it at Build; it's being extended to model providers, networks, MCP servers and secrets
- **Windows**: the `openclaw-windows-node` companion, with guided setup, a native chat with inline approvals, model selection, and a sandbox backend based on [Microsoft eXecution Container (MXC)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Microsoft+eXecution+Container+(MXC)?ref=dsebastien.net)
- **Reliability**: queue prioritization, scheduler and database-recovery fixes, a guard against repeated tool loops after compaction, lower session-store memory, and telling "definitely did not run" apart from "unknown outcome" commands
- **Integrations and safety**: secret redaction in execution-approval prompts, an Azure OpenAI provider, iMessage approvals, native polls, message routing checks

OpenClaw keeps its MIT license and its non-profit foundation. OpenClaw Enterprise (29 September), the control plane for persistent agents that started at OpenAI, doesn't mention Microsoft or Autopilot, and nothing shows Autopilot uses it.

The New Stack's framing, back in June: Microsoft "made the agent runtime free" and "kept everything around it". I think that's the right read. The runtime is open; identity, policy, billing and the Microsoft 365 data stay Microsoft's.

## Where it sits in the new Copilot

The new Copilot has three parts: **Home** (chat plus Cowork, eventually routing to chat, Cowork or Code for you), **Code** (natural-language apps and dashboards built on [GitHub Copilot](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GitHub+Copilot) technology) and **Autopilot**. Nadella called it "a new OS for work". Fortune reads it as Microsoft cleaning up a "sprawling collection of Copilot products". Bloomberg's headline: Microsoft "abandons personal AI chatbot race with Copilot reboot".

Microsoft draws the line with Copilot Cowork like this: Cowork does one task end to end (an RFP response, a close package) and hands back the result. Autopilot holds a role and a goal over time.

## Security, identity and approvals

- **Its own identity.** Each agent runs under its own governed Microsoft Entra identity, not a shared service account. Credentials are scoped to the task and redacted from logs ([AI Agent Identity](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Identity))
- **Organization limits.** Agents reach only resources the organization approved. Sensitive actions can require human sign-off. Purview data loss prevention and sensitivity labels apply before content is sent or written
- **Audit.** Fortune mentions explicit permissions and full audit logs. Nadella: "Everything that you observe should be governable by policy"
- **Scout's approvals**: Approve, Always allow or Deny; three tiers for shell commands (auto-approve, prompt, deny), with auto-approve off by default; sending, sharing and replying need confirmation
- **Prompt injection**: emails, web pages and Teams messages are tagged as untrusted external content
- Microsoft says Scout doesn't use customer data to train models

### The GitHub Copilot caveat

Scout's model calls go through GitHub Copilot, and it inherits GitHub Copilot's model catalog (Microsoft, third-party and open-source models, including China-based providers). The GitHub Copilot admin decides which models are available.

Microsoft's own Responsible AI FAQ spells out the consequence: prompts and content may leave Microsoft 365, and Microsoft 365 protections like **data residency, retention, sensitivity-label enforcement and eDiscovery don't apply** to that processing. Generated content may not inherit labels. That's why admins have to sign an attestation before turning it on.

That sits awkwardly next to the "Purview enforced" language in the launch post. Both can be true (labels enforced on Microsoft 365 actions, not on the model processing path), but you have to read the FAQ to find out. For Autopilot, none of this is documented yet.

## Requirements and licensing

What Scout required:

- Enrollment in Microsoft's Frontier program, an Intune policy that allows sign-in, and an admin attestation
- A Microsoft 365 work or school account and a Microsoft 365 Copilot license
- A GitHub Copilot **Business or Enterprise** seat, with token usage billed through GitHub
- Windows 11+ or macOS 12+, with local admin rights

Not available in government clouds (GCC, GCC High, DoD) or sovereign clouds. Whether Autopilot keeps the GitHub Copilot requirement is **unknown**.

## Pricing and availability

- **Usage-based billing**, alongside Cowork, Code and frontier models. No prices published. Chat and Copilot in the Office apps stay on the per-user license
- Microsoft names "Astra and Fable" as frontier models available under usage-based billing. Which model Autopilot itself uses isn't stated. Fortune says Copilot relies mostly on Anthropic and OpenAI models and also uses xAI's Grok
- **Private preview** from the end of September 2026. Fortune calls it "a more restricted phase of user testing", with no general availability date
- **Regions**: Scout's availability depends on Frontier enrollment, not a country list. There's no EU-specific statement, and given the GitHub Copilot processing path, I wouldn't assume the EU Data Boundary covered Scout's model calls. Nothing published for Autopilot

## Reception

- **The Register**: OpenClaw's poor security reputation, unclear prompt injection defenses (Microsoft didn't respond), reliability questions, an agent "watching your every move", and the extra GitHub Copilot metered cost
- **Gizmodo**: skeptical of Copilot's "litany of short-lived rebrands", the "cutesy" avatar, and the "digital teammate" framing; reads the consolidation as a way to pull more data into Microsoft's ecosystem
- **GeekWire** pointed out the irony of Nadella's "virus" remark, and Microsoft Defender's own guidance that OpenClaw "should be treated as untrusted code execution with persistent credentials"
- **Fortune**: Microsoft's fix for Copilot sprawl, with 30 million paid Microsoft 365 Copilot seats in July
- The name collides with Windows Autopilot, Microsoft's device provisioning service. Good luck searching for it

## Limitations

Documented for Scout: it may misread ambiguous instructions, multi-step tasks may fail, and stale Microsoft 365 data can produce wrong answers. Microsoft says not to use it where accuracy must be guaranteed (legal, medical, financial). Custom skills aren't validated by Microsoft. Background modes run with stricter permissions. Losing the connection pauses work, and sign-in failures don't say why when an admin step is missing.

## How it compares

Autopilot is the odd one among the hosted agents. It's the only one built on an open-source runtime (with contributions going back upstream), the only one where every agent gets its own directory identity (OpenAI's specialist dots, which also get their own identity, are still in enterprise pilots), the only one billed purely on usage, and it lives inside Microsoft 365 surfaces (Teams, Outlook, documents) instead of a separate app. [Dots](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dots+(AI)?ref=dsebastien.net), [Meta Muse](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Meta+Muse), [Grok Bot](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Grok+Bot), [Gemini Task](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemini+Spark) and [Claude Duet](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Duet) all sell to individuals first. The full comparison table is in [Claude Duet](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Duet).

## My take

Microsoft shipping OpenClaw under the hood is the most interesting thing in this whole category. It proves the self-hosted runtime is good enough for an enterprise product, and the contributions (policy checks, a Windows sandbox, reliability fixes) help everybody who runs OpenClaw. Not bad for a project Microsoft's own CEO reportedly compared to a virus.

The per-agent identity is the right call too. An agent that acts under its own account, with its own audit trail, is far easier to govern than one that "acts as you".

But the data path worries me. If the model calls run through GitHub Copilot, outside Microsoft 365's residency and retention commitments, a European company has a real question to answer before it turns this on. Microsoft hasn't published Autopilot's terms yet, and I'd wait for them.

From Belgium, it's one of the few hosted agents with no published exclusion of Europe. In practice, that means an employer with Microsoft 365, the Frontier program and a preview invite.

## Caveats

- The Autopilot facts come from one Microsoft blog post (25 September) plus press. The Learn documentation (updated 21 August) still describes Scout, the desktop app. Requirements, pricing, model and data-residency terms for Autopilot are unpublished
- Only the OpenClaw blog says Autopilot runs on OpenClaw; Microsoft's September post doesn't mention it. I treat it as reliable (the Foundation names the Microsoft engineers) but it's one-sided
- Desktop or cloud: the Scout docs describe a local app, the June post said "across cloud, desktop, and web", and the September post describes a cloud agent. Likely an architecture change at the rename
- Purview: the June post says DLP and labels are enforced; the Responsible AI FAQ says Microsoft 365 protections don't apply to the GitHub Copilot processing
- That Scout is the "Project Lobster" / "ClawPilot" GeekWire described is strongly implied (same team, same leader), never stated by Microsoft
- The Nadella "virus" quote is secondhand; I didn't find the original
- Claims that Autopilot identities are licensed through Agent 365, per-agent price estimates, an October preview start, and a "$30 seat plus a second usage charge" framing all come from aggregators or unfetched snippets. Left out
- "Astra and Fable" as Copilot frontier models: probably the same models as [GPT-6 Astra](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GPT-6+Astra) and Anthropic's Fable, not confirmed
- The New Stack's June article: I only have its headline and a snippet

## References

- Microsoft Official Blog, Jared Spataro, "Introducing the new Copilot with Home, Code and Autopilot" (25 September 2026): [https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)
- Microsoft Copilot Blog, Omar Shahine, "Introducing Microsoft Scout: Your always-on personal agent" (2 June 2026): [https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)
- Microsoft Learn, Microsoft Scout documentation: [https://learn.microsoft.com/en-us/microsoft-scout/](https://learn.microsoft.com/en-us/microsoft-scout/)
- Microsoft Learn, Scout overview: [https://learn.microsoft.com/en-us/microsoft-scout/overview](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- Microsoft Learn, Scout FAQ: [https://learn.microsoft.com/en-us/microsoft-scout/faq](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- Microsoft Learn, Scout what's new: [https://learn.microsoft.com/en-us/microsoft-scout/whats-new](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
- Microsoft Learn, Scout get started: [https://learn.microsoft.com/en-us/microsoft-scout/get-started](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- Microsoft Learn, Scout Responsible AI FAQ: [https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq)
- Microsoft Learn, Scout admin access: [https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)
- OpenClaw blog, Graham McBain, "Microsoft Autopilot is built on OpenClaw. The contributions go both ways." (25 September 2026): [https://openclaw.ai/blog/microsoft-autopilot-openclaw](https://openclaw.ai/blog/microsoft-autopilot-openclaw)
- OpenClaw blog, "Introducing the OpenClaw Foundation" (8 July 2026): [https://openclaw.ai/blog/introducing-openclaw-foundation](https://openclaw.ai/blog/introducing-openclaw-foundation)
- OpenClaw blog, "OpenClaw Enterprise" (29 September 2026): [https://openclaw.ai/blog/openclaw-enterprise](https://openclaw.ai/blog/openclaw-enterprise)
- Thurrott, Build 2026 Scout coverage (2 June 2026): [https://www.thurrott.com/a-i/336926/build-2026-microsoft-unveils-scout-personal-work-agent-and-new-in-house-ai-models](https://www.thurrott.com/a-i/336926/build-2026-microsoft-unveils-scout-personal-work-agent-and-new-in-house-ai-models)
- The Register (3 June 2026): [https://www.theregister.com/a/5250718](https://www.theregister.com/a/5250718)
- Help Net Security (3 June 2026): [https://www.helpnetsecurity.com/2026/06/03/microsoft-scout-personal-agent/](https://www.helpnetsecurity.com/2026/06/03/microsoft-scout-personal-agent/)
- The New Stack, "Microsoft just made the agent runtime free" (7 June 2026): [https://thenewstack.io/microsoft-scout-openclaw-runtime/](https://thenewstack.io/microsoft-scout-openclaw-runtime/)
- Fortune (25 September 2026): [https://fortune.com/2026/09/25/microsoft-unveils-copilot-super-app-targeting-business-users-with-ai-agents/](https://fortune.com/2026/09/25/microsoft-unveils-copilot-super-app-targeting-business-users-with-ai-agents/)
- Gizmodo (25 September 2026): [https://gizmodo.com/microsoft-thinks-its-finally-figured-out-copilot-this-time-2000817460](https://gizmodo.com/microsoft-thinks-its-finally-figured-out-copilot-this-time-2000817460)
- Bloomberg (25 September 2026, paywalled): [https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot](https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot)
- GeekWire, Mary Jo Foley (4 May 2026): [https://www.geekwire.com/2026/microsofts-openclaw-team-takes-on-the-personal-assistant-challenge/](https://www.geekwire.com/2026/microsofts-openclaw-team-takes-on-the-personal-assistant-challenge/)
