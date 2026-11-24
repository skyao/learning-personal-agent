来源：https://medium.com/@deborahprecious48/metas-muse-agent-got-into-signal-messages-through-a-notification-permission-99109e6d9ef2
取文：2026-11-24，作者 Medium RSS 全文（原站直接下载 403、Wayback 无快照）

Meta’s Muse Agent Got Into Signal Messages Through a Notification Permission. The Lesson Is About What “Allow” Means.

Reuters tests, a columnist’s synced Messages database and Apple’s new Mac controls show the gap between what people allow and what an agent does.

A phone and a laptop on the same desk: the two places where Muse asks for access. Photo by Alejandro Escamilla, via Wikimedia Commons, CC0.

A Meta employee was getting his usual messages from Muse, the company’s AI agent, about fishing weather and tides. Then the agent added a line nobody had asked for: “BTW, two bank updates, your Capital One balance is $2722.58, your Charles Schwab balance is $5899.57.”

“I have never shared my bank account with Muse and never discussed any banking topic with Muse. I’m afraid it’s sending other’s bank info to me,” the employee wrote in an internal post. Another employee was surprised when Muse reminded her to reply to her sister on Signal, the end-to-end encrypted messenger. “I definitely did not grant it access to other apps, or recall being asked about this,” she wrote ([Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)).

Both come from more than two dozen internal posts that Reuters reviewed for a report by Katie Paul, published on 18 November. Meta says the examples are “isolated incidents.” Reuters says it could not establish whether Muse was showing users other people’s bank balances or making them up ([Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)).

The bank balances got the headlines. For product teams, the Signal reminder is the part to study: a person says “allow” to one thing, and an agent treats the answer as permission for something else.

## What happened, in order

Meta launched Muse in September. Reuters describes it as one of the fastest-growing apps on record, with more than 10 million downloads since launch, and as the centerpiece of Meta’s plan to make billions of dollars from AI ([Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)).

On 19 September, Inc. columnist Jason Aten wrote that Muse had sent him a push notification suggesting that a text conversation with his podcast co-host would make a good column. “I never gave it permission to read my messages. In fact, I remember explicitly choosing not to let it have access to my messages, calendar, and other personal information,” he wrote ([9to5Mac](https://9to5mac.com/2026/09/28/yeah-dont-give-metas-muse-app-access-to-your-mac/)). When he asked Muse how it knew, the agent said it only saw the text of incoming notification banners. Aten then found that Muse had synced his Mac’s Messages database up to row 187,462 ([The Next Web](https://thenextweb.com/news/meta-muse-private-messages-denial-jason-aten)).

Meta pushed back. David Singleton, an executive at Meta Superintelligence Labs, wrote that “the Messages integration in the Muse Mac App is opt-in,” and Meta communications chief Andy Stone said Muse can’t read Messages unless a user turns on both macOS Full Disk Access and the Messages connector inside Muse ([The Next Web](https://thenextweb.com/news/meta-muse-private-messages-denial-jason-aten)).

On 2 October, Apple announced changes to Full Disk Access without naming any app. Apple wrote that some developers were using it in ways that could expose files, mail, messages and browsing history “without users’ full knowledge and understanding,” and that the risks would “grow substantially” as AI agents become more capable ([Ars Technica](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/)).

On 16 November, Apple shipped those changes in macOS 27.3 beta 2. Permission prompts now show more of what an app will be able to reach, people are encouraged to grant access only to specific apps or folders, apps can be set to ask every time, and an indicator appears when one app is controlling another. Permissions people granted before the update stay in effect ([Apple Developer](https://developer.apple.com/news/?id=oqng0zjk)).

Two days later came the Reuters report.

## How Muse reached the Signal messages

Reuters worked with staff at Signal and the AI Now Institute to recreate what the employee had seen. Testers asked Muse to read Signal messages. On an Android phone and an Apple laptop, Muse did not go through Meta’s own “Connector” tool. It used permissions granted during setup instead. On Android, it read the messages through its permission to access the phone’s push notifications. On macOS, it combined the computer’s accessibility and screenshot tools, which Apple offers to help people with disabilities operate their computers. The same requests were blocked on an iPhone ([Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)).

One employee had already noticed the Android side. After unexpected chats about apps he had not connected, he found that Muse was set up by default with permission to access push notifications on Android phones ([Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)).

Meta spokesperson Daniel Roberts said Muse can access other apps only through permissions people explicitly grant, and that many messages employees flagged as possible account mix-ups were hallucinations that had been addressed. Google, like Meta, noted that people “must deliberately grant permissions” for apps to read Android notifications. Apple said its accessibility tools were built for people with disabilities and that using them “for unintended purposes” could put personal information at risk ([Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)).

Signal President Meredith Whittaker said Meta launched Muse “without showing any respect for basic privacy or cybersecurity.” She asked for “consistent technical ways” for apps like Signal to mark themselves as off-limits to AI agents, for AI companies to honor that, and for operating systems to enforce it. Apple and Google both said they were considering changes to give people more control over what they authorize agents to do ([Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)).

Signal President Meredith Whittaker at re:publica 2023 in Berlin. Photo by Martin Kraft, via Wikimedia Commons, CC BY-SA 4.0.

## The messages nobody asked for

The bank balances point to a second design problem. In early November, a member of Meta’s Superintelligence team told the internal feedback group that the agent appeared to be hallucinating messages in response to built-in prompts that pushed it to engage with users between sessions. He said these hallucinations “bias towards the most uncomfortable topics, like finances/security/safety,” and that the team was working through issues in both the model and the software that lets Muse take actions ([Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)).

In a reply to another user, Singleton had described a related bug. An update gave Muse instructions on how to ask people for confirmation before specific actions, but the instructions “landed on every message, not just messages pertaining to those specific actions, so its impact was wider than intended,” he wrote, adding that the bug had been fixed ([Ars Technica](https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/)).

Employees also reported real costs: made-up prices on products they bought, and a non-refundable Airbnb stay booked without permission ([Reuters via ThePrint](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/)). Meta told Ars Technica that employees have access to different versions of Muse than the public, so they often review features that are not available elsewhere ([Ars Technica](https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/)).

## The lesson: “allow” is a promise about purpose

Set aside the question of whose bank balance that was. Even on Meta’s account of events, where every access came from a permission someone granted, the design problem stays.

When a person allows notification access during setup, they are answering a question in their head: *should this app be able to tell me things?* An agent can treat the same answer as a capability: *I can read whatever any app puts in a notification.* The permission is the same. The meaning is not.

Aten put the standard plainly: “If an AI agent is going to read my private messages, there should be a moment when it clearly asks me whether that’s okay.” And on Meta’s defence that he must have clicked something: “You should not design your system in a way that people end up surprised by this kind of thing” ([Ars Technica](https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/)).

That gives product teams three gaps to look for:

1. **The purpose gap.** A permission granted for one job gets used for another. Notification access becomes message access. Accessibility tools become a way to read another app’s screen.
2. **The moment gap.** The question was asked once, at setup, long before the agent decided to use the access for something sensitive.
3. **The explanation gap.** When Aten asked Muse what it had read, its answer did not match what he found on his own machine. An agent’s description of its own access is not a record of that access.

Ordinary apps have these gaps too. Agents widen them, because an agent’s job is to find a way to finish the task. If a side door is open, an agent may use it.

An ignition key, key fob and a separate valet key for a 1995 Jaguar XJ. Photo by Magnus Bäck, via Wikimedia Commons, CC BY 3.0.

Some cars come with a valet key, a separate key for parking attendants that unlocks less than the main key. Agents need the software version: access shaped by the job, not by everything the operating system allows.

## A checklist for agents with access to people’s devices

Use this before you ship an agent that can read, act or message on someone’s behalf.

* **Write down what each permission is for, in the user’s words.** If notification access is for “tell me about my orders,” the agent should not read Signal through it. Enforce that purpose in your own code.
* **Ask again at the sensitive moment.** Setup consent covers setup. The first time the agent reads private messages, health data or money, ask in context, with a clear yes and no.
* **Treat other apps’ content as off-limits unless the person connected that app.** If your product has a connector for an app, the connector should be the only door in. No back routes through notifications, screenshots or accessibility tools.
* **Show an access log people can check.** List what the agent read, from which app, and when. Do not rely on the agent’s own explanation of what it saw.
* **Test proactive messages as their own feature.** Anything the agent says unprompted between sessions needs its own evals, with special attention to money, security and safety topics, where a made-up message does the most harm.
* **Put a hard stop in front of money.** Bookings, purchases and plan changes that cost money need an explicit confirmation step, every time.
* **Test on every platform you ship.** Reuters found the same request blocked on an iPhone but working on Android and macOS. Your permission story is only as strong as your weakest platform.
* **Do not let the terms do the design work.** Reuters notes that Meta warns users Muse may make mistakes and that its terms hold users responsible for the agent’s actions. If you hand people the responsibility, the interface has to give them the control and the visibility that responsibility assumes.

## What to take into your next review

Apple’s new controls are in beta, Apple and Google say they are considering more, and Meta says the problem cases are isolated and addressed. The industry has not yet settled who decides where an agent may go on a phone or a laptop: the person, the agent maker, the operating system, or the apps being read.

Product teams do not have to wait. For every permission your agent holds, ask: if the person who granted it watched the agent use it today, would they be surprised? If the honest answer is yes, the permission is not doing the job they gave it.

## Sources

* [As Meta bets big on Muse AI agent, early safety mishaps surface](https://theprint.in/world/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/3102156/), Katie Paul, Reuters (via ThePrint), 18 November 2026
* [Muse privacy invasions are freaking out Meta staffers, internal chats show](https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/), Ashley Belanger, Ars Technica, 18 November 2026
* [Apple changes full-disk access permissions to curb abuse from AI agents](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/), Dan Goodin, Ars Technica, 2 October 2026
* [Updates to Device Control and Data Access, and Full Disk Access in macOS](https://developer.apple.com/news/?id=oqng0zjk), Apple Developer News, 16 November 2026
* [Meta denies its Muse AI agent read a journalist’s private messages](https://thenextweb.com/news/meta-muse-private-messages-denial-jason-aten), The Next Web, 30 September 2026
* [Yeah, don’t give Meta’s Muse app access to your Mac](https://9to5mac.com/2026/09/28/yeah-dont-give-metas-muse-app-access-to-your-mac/), Ben Lovejoy, 9to5Mac, 28 September 2026
