来源：https://openclaw.ai/blog/microsoft-autopilot-openclaw/
取文：2026-11-10，直接下载

Microsoft Autopilot is built on OpenClaw. The contributions go both ways.

From policy conformance and native Windows support to more reliable everyday interactions, Microsoft contributors are helping build OpenClaw for everyone.
![A friendly paperclip character with lobster claws beside a laptop, offering to help with your work.](images/img-01-036b49.png) 

Microsoft today introduced Autopilot as part of its new Copilot experience: a persistent, proactive personal agent that keeps working even when you’re not. Its foundation is OpenClaw.

Omar Shahine, who leads the team building it, [put it directly](https://x.com/OmarShahine/status/2103480227561079264):

> “We are building Autopilot on @openclaw, working with @steipete and the OpenClaw Foundation to make it a fantastic enterprise grade runtime.”

> Today we announced the preview of Microsoft Autopilot is rolling out to our first customers - "Autopilot is a persistent, proactive and personal agent that keeps working even when you’re not"  
>   
> It's been a while since I updated you all on what we are building. First Scout is now… [pic.twitter.com/ZdGHQDn7Ll](https://t.co/ZdGHQDn7Ll)
>
> — Omar Shahine (@OmarShahine) [September 25, 2026](https://x.com/OmarShahine/status/2103480227561079264?ref_src=twsrc%5Etfw)

Autopilot is the new name for Microsoft Scout, announced earlier this year. Microsoft’s [launch post](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/) says Autopilot is expanding to private preview at the end of this month.

For the OpenClaw community, there is another part of the story worth highlighting: the improvements coming back upstream.

Microsoft’s commitment is visible in both its public announcements and the work of contributors across the project. That work ranges from checking an agent’s security configuration to building a native Windows experience and making everyday agent interactions more dependable.

## Making an agent’s configuration checkable

An organization adopting a personal agent needs to answer practical questions. Which communication channels are enabled? Which model providers can it use? What can it access? Does its configuration still match the rules the organization intended?

In its [original Scout announcement](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/), Microsoft made an explicit commitment:

> “We are contributing policy conformance directly upstream to OpenClaw.”

Gio Della-Libera’s upstream work gives that commitment a concrete form. OpenClaw’s [Policy plugin](https://github.com/openclaw/openclaw/pull/80407) lets an operator describe requirements, compare them with the actual configuration, and produce a record of the result. Subsequent contributions extend those checks across [model providers, networks and MCP servers](https://github.com/openclaw/openclaw/pull/80783), [secret and authentication configuration](https://github.com/openclaw/openclaw/pull/81974), and other parts of an agent’s environment.

Omar also contributed [message-routing checks](https://github.com/openclaw/openclaw/pull/111087), so operators can test whether representative incoming conversations reach the intended agent.

These checks let operators verify an agent’s configuration and detect when it no longer matches their requirements.

## A first-class home on Windows

The Foundation and Microsoft’s Windows team have also described a [long-term collaboration](https://openclaw.ai/blog/introducing-openclaw-foundation) to make Windows a premier platform for OpenClaw.

You can see that collaboration in the [native Windows companion](https://github.com/openclaw/openclaw-windows-node).

Scott Hanselman’s contributions include a [guided setup experience](https://github.com/openclaw/openclaw-windows-node/pull/201), alongside ongoing reliability and release work. Régis Brid contributed [native WinUI chat](https://github.com/openclaw/openclaw-windows-node/pull/315) and [inline command approvals](https://github.com/openclaw/openclaw-windows-node/pull/751). Barbara Kudiess has worked across the native interface, [model selection](https://github.com/openclaw/openclaw-windows-node/pull/877), approvals and sandbox integration. Caleb Eden’s contributions help the native chat [display user and agent media](https://github.com/openclaw/openclaw-windows-node/pull/1119) properly.

There is important work underneath that interface, too. Paul Campbell contributed the [MXC sandbox backend](https://github.com/openclaw/openclaw/pull/97086) for supported Windows environments. Alongside the companion’s own sandbox integration, it gives operators another way to constrain agent command execution using Microsoft’s execution-container technology.

These practical improvements drive easier setup, clearer interaction, and more control over what an agent can do.

## Reliability for agents that keep working

An always-on agent has to handle more than a successful demo. It has to stay useful through background jobs, restarts, long conversations and failures.

Galin Iliev’s contributions include [prioritizing queued user requests over background work](https://github.com/openclaw/openclaw/pull/82765), fixing [scheduler behavior that could hang the Gateway](https://github.com/openclaw/openclaw/pull/142741), and improving [responsiveness during database recovery](https://github.com/openclaw/openclaw/pull/151581). His recent [streamed-completion fix](https://github.com/openclaw/openclaw/pull/156144) prevents the same Codex reply from appearing twice in conversation history when its streaming and completion identifiers differ.

Eduardo Piva contributed a [guard against repeated tool loops after context compaction](https://github.com/openclaw/openclaw/pull/77555) and work to [reduce session-store memory retention](https://github.com/openclaw/openclaw/pull/84693).

Omar’s contributions include another subtle but important distinction: [a command that definitely never ran is different from a command whose outcome is unknown](https://github.com/openclaw/openclaw/pull/117276). When an agent cannot tell whether an action executed, blindly repeating it can make the problem worse. The upstream change preserves that uncertainty and tells the agent not to rerun it automatically.

These are the details that help turn an agent from something impressive into something people can depend on.

## Better integrations, safer everyday interactions

Even the smallest contributions make noticeable improvements in daily use.

Gio’s [Microsoft Teams reaction fix](https://github.com/openclaw/openclaw/pull/151382) lets an agent react to the message it is currently answering without having to copy an internal message ID. The change retains the boundary between the current conversation and another conversation.

Pengfei Ni contributed [secret redaction in execution-approval prompts](https://github.com/openclaw/openclaw/pull/64790), helping keep recognizable API keys, tokens and passwords out of command text displayed in chat. Asking for permission should not unnecessarily expose a credential.

Kunal Karmakar improved [Azure OpenAI provider support](https://github.com/openclaw/openclaw/pull/50851), wiring Azure endpoints to the appropriate Responses implementation so configured agents and tools can use them correctly.

Together with Eduardo’s memory-retention work and Galin’s duplicate-reply fix, these marginal improvements pack a mighty punch in the user experience.

## Improvements that reach beyond one product

One of the most human parts of this contribution story is Omar’s work on messaging. His upstream changes include [iMessage approvals](https://github.com/openclaw/openclaw/pull/85952), [native polls](https://github.com/openclaw/openclaw/pull/98421), and [keeping replies in the right conversation](https://github.com/openclaw/openclaw/pull/133499).

That work benefits OpenClaw users on Apple devices, too. It is a reminder that a shared project can improve across platforms even while companies build distinct products on top of it.

Not every contribution by someone at Microsoft is necessarily an Autopilot feature or a company-sponsored project. What the public record shows is a substantial body of work contributed back to OpenClaw, alongside Microsoft’s explicit commitment to upstream collaboration.

Peter Steinberger welcomed that collaboration when it was announced in June:

> Such a privilege to work with Microsoft to bring claws to enterprises! <https://t.co/1psejBcL7S>
>
> — Peter Steinberger 🦞 (@steipete) [June 2, 2026](https://x.com/steipete/status/2061874084649025728?ref_src=twsrc%5Etfw)

Thank you to Omar, Gio, Scott, Barbara, Paul, Galin, Eduardo, Pengfei, Kunal, Régis, Caleb, and the other contributors and maintainers building this together.

OpenClaw remains an open infrastructure for building and customizing powerful agents, both for personal and organizational use. Microsoft’s Autopilot is a promising example of the possibilities, and we’re grateful to the contributors whose upstream work makes this platform more useful for everyone.
