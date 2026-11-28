来源：https://www.theneuron.ai/news/microsoft-ignite-2026-copilot-autopilot-today-fusion/
取文：2026-11-28，直接下载

Microsoft wants Copilot to keep work moving between prompts. From Ignite in San Francisco, we unpack Autopilot, the new Today experience, and GitHub Copilot Fusion, including what’s available and where the costs come in.

![Microsoft logo connected to AI assistant, calendar, and coding icons beside the headline “Microsoft Ignite 2026: Everything AI You Need to Know.”](images/img-01.avif)

I’m in San Francisco for Microsoft Ignite, and Microsoft has given us a small novel’s worth of announcements to work through.

Three things deserve most of your attention: Copilot Autopilot, the new Today experience, and GitHub Copilot Fusion. They address different parts of a problem anyone using AI for work will recognize: how much effort it still takes to get useful work out of these tools.

Autopilot can keep projects moving between prompts. Today prepares your priorities and next steps. Fusion handles the increasingly complicated business of choosing which models should do the work.

Microsoft’s pitch is getting more interesting, especially if your company already lives in Outlook, Teams, and Office.

- [Autopilot is Microsoft’s answer to the personal-agent race](#autopilot-is-microsofts-answer-to-the-personal-agent-race)
- [Today gets your next steps ready](#today-gets-your-next-steps-ready)
- [Fusion takes model selection off your plate](#fusion-takes-model-selection-off-your-plate)
- [A few other updates worth knowing](#a-few-other-updates-worth-knowing)
- [Related reading](#related-reading)

## Autopilot is Microsoft’s answer to the personal-agent race

If you’ve been following Muse, Dots, Grok Bot, or Claude Duet, you’ll recognize what Microsoft is going for.

Autopilot is a persistent personal agent with its own memory, tools, and identity inside your organization’s Microsoft environment. It can follow up on conversations, handle recurring work, and continue projects without waiting for you to prompt every step.

It’s [starting to roll out through Frontier](https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/), Microsoft’s early-access program.

The part that stands out is how other people can interact with it. Colleagues will be able to @mention your Autopilot in a Teams channel or group chat to request information or supported actions. Your assistant could help keep shared work moving while you’re occupied elsewhere.

That’s a useful direction for personal agents. Plenty of work stalls because someone needs an update, a follow-up, or information buried in a conversation.

We’ve already explored the appeal of persistent assistants through [Meta Muse](https://www.theneuron.ai/explainer-articles/how-to-get-started-with-meta-muse/) and [OpenAI Dots](https://www.theneuron.ai/explainer-articles/openai-dots-hands-on-review-herman/). Microsoft’s potential advantage is proximity to the work. For companies using Microsoft 365, much of the relevant information is already in its software, along with the permissions that determine who can access it.

Microsoft says Autopilot’s actions are tied to its own agent identity, safety-checked, and visible to administrators. That gives companies a way to distinguish what a person did from what their assistant did.

Useful controls. The remaining question is how much babysitting the assistant needs.

An agent that reliably handles follow-ups could save considerable time. One that needs frequent corrections gives you another thing to manage. I’m interested in how Autopilot performs once it has recurring responsibilities and a few weeks of context.

![Microsoft CEO Satya Nadella delivers his keynote address at Microsoft Ignite 2026 at Chase Center in San Francisco. ](images/img-02.avif)

Microsoft CEO Satya Nadella delivers his keynote address at Microsoft Ignite 2026 at Chase Center in San Francisco. | Corey Noles photo

## Today gets your next steps ready

Today might be the easiest announcement to appreciate immediately.

It pulls together information from emails, calendars, chats, and meetings to show what needs your attention. Then it prepares next steps, including email drafts, chat messages, and proposed scheduling changes, for you to review and approve.

A briefing that tells you you’re behind is only so helpful. Having the reply drafted and the relevant context ready gives you a head start.

There are two parts, with a billing distinction worth knowing:

- **Today Brief** provides a personalized morning briefing and prepares next steps. The daily refresh is included with a Microsoft 365 Copilot license.
- **Today Feed** updates throughout the day as new information arrives. Those recurring updates require Copilot credits.

Today is entering private preview through Frontier in the Copilot app and Outlook, according to Microsoft’s [Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/).

Today helps you catch up and act. Autopilot handles work that continues over time. There’s overlap, but the distinction makes sense: sometimes you want the next step prepared; sometimes you want to hand over an ongoing responsibility.

The feature’s usefulness will depend heavily on what it chooses to surface. If everything needs attention, it’s another inbox. If it consistently identifies the few things that matter and prepares useful responses, it gives people a reason to start their day in Copilot.

## Fusion takes model selection off your plate

GitHub Copilot Fusion deserves attention even if you don’t spend your day writing code. It shows how AI products can handle more complex work without asking users to become experts in every available model.

One timing clarification: **Fusion became generally available on October 28 at GitHub Universe.** Today’s keynote builds on it, adding MAI-Code-2 and MAI-Code-2-Flash to GitHub Copilot and Fusion, according to [Microsoft’s published remarks](https://blogs.microsoft.com/blog/2026/11/17/ignite-2026-building-the-frontier-ecosystem/).

Fusion selects and coordinates models for a task. It can send work to one model, check a draft before escalating to a stronger model, or have several models critique a response before it’s revised. You get a single final answer. [GitHub’s documentation](https://docs.github.com/en/copilot/concepts/models/copilot-fusion) explains the available approaches.

That removes a familiar chore: deciding whether this particular task needs the fast model, the expensive model, or another attempt with something else.

The economics are promising. GitHub reported that Fusion Max scored within two points of Claude Code running Opus 5.5 Max on the Artificial Analysis Coding Agent Index, at roughly half the average API cost per task and about 40% less time. Those are [benchmark results for specific configurations](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/), so your workload may look different.

Fusion charges for the models it uses. Extra review can consume more credits; the benefit depends on choosing that extra work well.

Microsoft is applying a similar idea to workplace Copilot. Auto in Cowork uses Microsoft-Decision-1.1 to help determine how much effort different parts of a task need.

As agents take on larger jobs, these decisions become part of the product’s value. People want good work at a reasonable cost. Most would happily skip the model-selection homework.

![Microsoft AI CEO Mustafa Suleyman announcing 6 new AI models at Microsoft Ignite 2026 in San Francisco. ](images/img-03.avif)

Microsoft AI CEO Mustafa Suleyman announcing 6 new AI models at Microsoft Ignite 2026 in San Francisco. | Corey Noles photo

## A few other updates worth knowing

The [rest of the Ignite announcements](https://news.microsoft.com/events/ignite/2026/book-of-news/) fill in some practical pieces around those experiences:

- **Office in Copilot is generally available.** Word, Excel, and PowerPoint are now inside the Copilot app for editing and collaboration, with existing Microsoft 365 permissions and controls.
- **Microsoft AI introduced six new AI models** including Code 2, Code 2 Flash, Decision 1.1 and more.
- **Copilot Code is headed for general availability in December.** It lets people build apps and dashboards with natural language. Copilot Managed Runtime is available now to host and manage supported apps.
- **Microsoft IQ packages business context for agents.** Reusable guidance, skills, and tools could reduce how often teams have to explain the same company rules.
- **Agent 365 is expanding cost and value tracking.** That matters when assistants are consuming resources throughout the day, including while you’re doing something else.

These support the main pitch: give agents enough context to do useful work, somewhere to do it, and boundaries around their access and spending.

Microsoft has a credible opening here because it already holds so much of the information companies need to act on. Autopilot and Today could make that information more useful with less effort from the person managing it.

The test is straightforward: does the work actually move forward without creating more work for you?

A follow-up handled correctly, a useful draft waiting for review, or a project that advances while you’re busy would make a much stronger case for Copilot than another impressive answer in a chat window.
