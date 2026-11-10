来源：https://commandline.microsoft.com/project-lobster-openclaw-personal-ai-assistant-enterprise-secure/
取文：2026-11-10，直接下载

Microsoft Scout: From personal project to enterprise-ready personal agent

Omar Shahine and Jakob Werner talk shop about building an always-on, enterprise-secure, personal AI agent.

By [![](images/img-01-0c9134.webp)Command Line team](https://commandline.microsoft.com/author/command-line-team)![](images/img-01-0c9134.webp)Command Line editorial team

2026.06.02

Early this year, [OpenClaw](https://openclaw.ai/) demos were seemingly everywhere, though many seemed to amount at best to a cool party trick (“Look, my agent ordered a pizza”). But it got long-time Microsoft employee Omar Shahine thinking: How useful could claws actually be?

Very, it turned out. In his spare time, Shahine created [Lobster](https://www.omarknows.ai/p/meet-lobster-my-personal-ai-assistant), a personal AI assistant built on OpenClaw. It has its own Apple ID and email address, so he can text with it from any device with iMessage. He initially split Lobster into a trio of agents, each with its own security profile and tool access (eight weeks in, that number had increased to nine always-on agents). Lobster handles travel logistics, proactively sends family reminders ahead of time, and generally helps Shahine and his family stay organized and get things done. And after presenting Lobster to Microsoft’s AI Accelerator group, it landed Shahine a [new job](https://www.omarknows.ai/p/lobster-got-hired): bringing OpenClaw to [M365](https://www.office.com/) and the cloud as CVP of what was deemed “Project Lobster.”

At the same time, Microsoft Member of Technical Staff Jakob Werner was pursuing a similar idea with a twist: a desktop app-based agent inspired by OpenClaw. The goal was to deliver a powerful enterprise-secure personal AI assistant that anyone within Microsoft could use. In just a couple weeks, what was referred to internally as “Clawpilot” had already been downloaded by thousands of Microsoft employees, and that community continues to grow.

When Shahine started assembling a small team of enthusiastic builders—Ocean’s 11, naturally—Werner quickly joined their ranks. The two recently caught up in Redmond, Washington, to compare notes on building these always-on, autonomous agents and navigating the worlds of enterprise security, agentic memory, and more.

[视频：Microsoft Scout: From personal project to enterprise-ready personal agent](https://www.youtube.com/watch?v=nyhXB9Y7uLM)

## Embracing the spirit of open source

The Project Lobster team is representative of a new way of working within Microsoft, fueled by AI advancements. It’s a tight-knit group that prefers to collaborate asynchronously. There’s a general consensus against meetings. Everyone contributes to the codebase, including Shahine. And there’s no traditional executive assistant among their ranks: Each team member actively uses prototypes throughout the day to fully immerse themselves in the tech as they’re building it. There’s even a growing open-source community around the team that mirrors what’s found with open-source projects outside Microsoft’s walls.

“I’ve never seen a project inside the company where so many people showed up with their ideas and their code and did the work to produce a PR,” says Shahine.

> >
> I’ve never seen a project inside the company where so many people showed up with their ideas.

In fact, internal excitement around Project Lobster has been such that the team fielded pull requests (PRs) left and right during the early building phase, which they reviewed to determine whether they met the bar to make it into the product. Even some of Shahine’s changes didn’t make the cut. The focus had to remain on the central goal of the product: Creating an always-on personal agent for work. An AI helper that learns your goals, adapts to your daily work patterns, and acts with context, identifying issues before they surface, keeping projects on track and driving outcomes without constant input. An agent that can detect when a calendar is overbooked and propose specific changes before the week begins or identify when a decision is stalled and draft a targeted follow-up to unblock it.

“We have to determine if a given PR changes the central idea of the product or not—and the speed of that review is human speed, not AI speed,” notes Werner. “Anyone can make a PR super quickly now. We’re trying to help the community and teach contributors how to review PRs.”

While the work began as an internal experiment, it quickly turned into a customer-focused effort that’s culminated with the introduction of [Microsoft Scout](https://aka.ms/ProjectLobster-Blog)—an always-on personal agent powered by OpenClaw open-source technology.

## From experiment to enterprise-ready product

Microsoft Scout operates autonomously—with its own identity—acting on your behalf. It works across cloud, desktop, and web browser, so it can connect across the surfaces you use—Teams, Outlook, OneDrive, and SharePoint—and the systems where work lives, including email, calendar, and contacts.

Unlike your average claw in the wild, Microsoft Scout combines OpenClaw code with enterprise identity, governance, and security. Every package is ingested through a curated, signed Microsoft supply chain, and every tool call, model request, and network hop is mediated by a zero-trust runtime—the agent’s container is treated as untrusted, with Microsoft-controlled identity, tokens, and policy sitting outside it. With Agent 365, admins get a single control plane, and Microsoft Purview gives security teams the same compliance and DLP signal they already get from other M365 surfaces.

“It’s a super powerful tool,” acknowledges Werner. “And to be enterprise secure, we needed to make sure the data governance was right, that the privacy was right, and that it doesn’t cancel a meeting and send all your personal information to that email chain. If I send my agent to you, it shouldn’t tell you everything about me. These areas are possible to contain, but we also had to do it in a balanced way that doesn’t restrict the possibilities down to nothing.”

It’s a tradeoff worth making. And with Microsoft’s tried and trusted enterprise security offerings and ongoing research and innovation in the space, the team had a solid foundation from which to address the challenge.

## The role of agentic memory

In order for an always-on personal AI agent to be truly useful, it needs to be proactive—and that requires context powered by Work IQ. Over time, Microsoft Scout understands the way you work, uses the same productivity tools you use, and takes things off your plate without the need for constant prompts. It learns your goals, adapts to your daily work patterns, and acts with intent. Unlike previous technological waves, this is software that’s truly personalized. That’s transformative, but it’s not without tradeoffs.

“OpenClaw, Claude Code, GitHub Copilot CLI, these are agentic coding harnesses that are basically remembering—writing things down just like people do,” Shahine notes. “They write things down like a diary. But just like it needs to remember things, it needs to forget some things, too.”

> >
> Just like it needs to remember things, it needs to forget some things, too.

As an example, Shahine points back to the introduction of memory to ChatGPT. He spent some time telling ChatGPT that his daughter was 17 while his son was 13. But a year later, that information remained static. The system didn’t have a concept that some facts need to change over time, while other pieces of information—like your name—will stay exactly the same.

“In the design phase, I was thinking about the human and how humans memorize things,” says Werner. “I forget things that are irrelevant because I didn’t use them. So I built a system where, if I’m going to use it repeatedly, it’s going to stick. But if I’m not going to use it regularly, I want the system to forget. I don’t want to have an infinite diary of things, right? So there’s kind of layers of memory, and it kind of disappears over time if it’s not used. Meanwhile, the relevance of other pieces of memory grows as you use them more.”

## Forming a new center of gravity

When they first joined forces, Werner introduced Shahine to the concept of gravity—the framework around which he operated.

“To build a truly great product, I don’t think I can make it myself,” Werner explains. “We need to collaborate with other people. But how do we influence other people to collaborate with us? And the mindset I use and try to instill in my team is gravity. We build something and make it so big in influence—not in the number of features, but in its influence—that when exciting new ideas pop up, they want to try and join the gravity of our work rather than dissolve focus.”

“And I didn’t really know what you were talking about until my new role was announced,” admits Shahine. “But since then, I’ve received hundreds if not thousands of messages from people who want to help, people who want to learn, people who want to show me what they did, and customers who want to know ASAP when they’re going to get their hands on what we’re building. There are a lot of other words for that—user pull, signal—but your mantra of gravity really resonates with me now.”

---

Microsoft employees have already been using an early Microsoft Scout desktop experience. We built this to learn how always-on agents show up in real work, and we’re seeing it take on coordination, surface risks earlier, and keep work moving without constant prompting.

We’re now extending that early experience to Frontier organizations. Microsoft Scout is available as an experimental release through [Frontier](https://www.microsoft.com/en-us/microsoft-365-copilot/frontier-program), giving customers a chance to explore how it can fit into their own workflows.

Access requires Frontier enrollment, Intune policy configuration, and an opt-in attestation. Users with a GitHub Copilot license can then download and install the experience. [Learn more](https://aka.ms/ProjectLobster-Blog).
