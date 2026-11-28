来源：https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/autopilot-meet-your-trusted-personal-teammate/4572611
取文：2026-11-28，直接下载

I call my Autopilot Sebastian.

I work with Sebastian in Teams and Outlook. I ask him to help prepare for my day, work through conversations that need a reply, and coordinate meetings. Some jobs are one-time requests. Others run on a routine, without me needing to ask again. And I'm not the only person who can work with him. Other people can, too.

Much of this work is ordinary: checking, coordinating, following up, and making sure nothing gets lost. But it takes real attention. I want to be able to hand more of it over.

That's what we're building with Autopilot: a trusted personal teammate that understands your work, collaborates with other people, and keeps making progress even when you're focused elsewhere. Give it a name, a role, and a goal. Autopilot has its own identity, memory, workspace, and remote computer, with tools to get work done. It runs in the cloud, so the work doesn't depend on keeping your laptop open.

**"Sebastian, get me to Ignite and back"**

Take a request like getting to Microsoft Ignite. Finding a flight is one task. Getting me there, helping me make the most of the event, and getting me back to work is a much bigger responsibility.

Before I go, I need to block time for the event, preparation, and travel. Check it against work and personal commitments. Work through flight and hotel options, including the tradeoffs I care about. Make the bookings once I've approved them. Then sort out registration, ground transportation, and where I need to be.

Once I'm there, the job changes. Help me navigate the schedule and prepare for meetings. Keep my normal work moving, manage out-of-office arrangements, and make sure people can reach me when something needs my attention. Help coordinate a dinner, find a reservation, or organize an after-hours event. Keep track of receipts while they're still easy to find.

And getting home isn't the end. There's the return journey, the conversations I missed, the follow-ups I owe, and the expense report I would otherwise put off.

That's the kind of responsibility I want Sebastian to take on. I don't want to turn every step into a separate prompt or explain the trip again every morning. I want to delegate the outcome, work through the decisions together, and have it carry the context forward.

I've already used Sebastian to protect travel time on my calendar and work through meetings that should come off it before time away. After I selected the meetings, he removed the relevant occurrences while preserving the recurring series. That distinction matters. "Clear next week" shouldn't accidentally become "cancel this meeting forever."

"Get me to Ignite and back" describes the broader ambition. My day-to-day work with Sebastian is helping us understand what it takes to make that ambition dependable.

## How we built Autopilot

**It starts from my work**

Autopilot is built on Microsoft IQ, so it's grounded in where my work already happens: Outlook, meetings, files, chats, and the people and priorities around me. I don't need to connect my tools manually, or explain who everyone is. And because Sebastian has persistent memory, he builds on what he learned last week instead of starting over.

**Sebastian has his own identity**

Sebastian has his own identity. That sounds like a technical detail, but it changes how we work together.

For example, Sebastian sends me my **Sunday Reset by email**. I can reply to that email and continue the conversation with him. It isn't just a report delivered to my inbox. It's an email from my teammate that I can respond to, without opening another app or starting a new chat.

**Other people can schedule time with me by talking to Sebastian in Teams.** He knows my scheduling preferences, so I don't have to explain them every time someone wants to meet. They don't need to ask me to ask my assistant. They can work with him directly.

**I can also delegate work to Sebastian in group chats and channels.** If we're discussing something that needs follow-up, I can bring him into that conversation and give him the job. I don't have to leave the discussion, copy everything into a private chat, and explain who everyone is.

This is an important part of the Ignite example. While I'm in a session or meeting with a customer, people still need time with me. Team conversations still need follow-up. I want Sebastian to help with that coordination, using the preferences and boundaries I've already established.

Getting me to Ignite is useful. Helping me be there without remaining the middleman for everything back at work is the bigger idea.

**Bring me the work that's ready for my attention**

Recently, while out of the office I asked Sebastian to help with unanswered Teams conversations. He prepared **40 reply drafts**, grouped them by priority, and put them in a private, editable queue that I can review and the ask him to help. He can monitor things going on at work and ping me for urgent issues.

That's more useful than telling me I have messages to answer. The work was brought to a point where I could review it and make decisions. The replies stayed as drafts. I remained responsible for what would be sent.

Sometimes the right outcome is a completed task. Sometimes it's a decision prepared well enough that I can make it quickly. A useful personal agent needs to understand the difference.

**Building a dependable coworker**

Using Sebastian every day makes the requirements very concrete.

**It needs to be personal.** A teammate becomes more useful as it understands your priorities, preferences, and working style. Persistent memory and context mean you can build on previous work instead of starting over. Built on Microsoft IQ, Autopilot can draw on organizational context to understand the work behind the request.

**It needs to be proactive.** A morning briefing should arrive without another prompt. A recurring responsibility needs attention over time. But proactive doesn't mean constantly interrupting me. It means doing the work and bringing me the things that deserve my attention.

**It needs to be collaborative.** Its own identity makes two-way email conversations possible. Other people can work with it in Teams. You can delegate work in shared chats and channels. A personal teammate should be useful to the people you work with, not isolated from them.

**It needs to be enterprise grade.** I want Sebastian to work independently, but that doesn't mean he should operate without boundaries. He needs to know what he's allowed to do, when to ask for approval, and how to handle information that shouldn't be shared with everyone. Microsoft is building Autopilot with its own identity, hosted environment, and safeguards around supported actions. Organizations can extend those protections with Microsoft Agent 365 and Security capabilities for governing access, protecting sensitive information, and understanding activity. The goal is straightforward: give Autopilot meaningful responsibility while keeping the organization in control.

**And it needs to be manageable.** I need to set priorities, establish boundaries, decide what requires approval, and change direction. My organization needs to manage access and oversight. Greater autonomy should not mean less accountability.

## What’s next and getting started

We're still building and learning. My experience with Sebastian reinforces that reliability matters as much as capability. Preparing a reply and sending it are different things. Finding a time and confirming a meeting are different things. Completing a task includes knowing which of those actually happened.

That's how an agent earns more responsibility.

**Start with something worth handing over.** You don't have to begin with "get me to Ignite and back."

Start with a responsibility you know well. Prepare me for the quarterly review. Bring me the conversations that need a reply, with drafts ready to review. Take on the follow-up we just discussed in the team chat.

Give Autopilot a clear outcome and boundaries. Review the work. Refine how you want it done.

For me, the value isn't spending more time talking to Sebastian. It's having less to carry around in my head, fewer things to chase, and more time for the work that needs me.

Starting today, Autopilot is rolling out to eligible customers in Frontier. To be considered eligible, customers need to be enrolled in the Frontier program, with a Copilot license, usage-based billing enabled, and required management and security capabilities in place. We’ll use the preview period to validate and refine requirements ahead of broader availability. [Learn more here](https://aka.ms/autopilot-documentation).

And this is just the beginning for a new wave of agents, as we’re making capabilities that power Autopilot available to supported agents across our Microsoft portfolio. These agents come ready to work with their own identity, secured resources, and productivity apps. Microsoft agents like Sales Development Agent, as well as agents from supported platforms like Copilot Studio, can be equipped with their own email address and secured Microsoft 365 resources for ongoing, independent work. [Learn more here](http://aka.ms/microsoft-365-resources-for-agents).
