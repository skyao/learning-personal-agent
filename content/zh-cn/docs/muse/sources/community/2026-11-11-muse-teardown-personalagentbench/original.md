来源：https://personalagentbench.com/agents/muse/
取文：2026-11-17，直接下载

How Meta Muse works, and what it can do: a teardown

Meta's personal agent, with a Linux machine of your own behind it.

Share of errands completed

1. October, 20 tasks**58%** (36–77)
2. September, same 114 tasks**40%** (33–46)
3. September, own draw**19%** (13–25)

Product runtimes rebuilt for the exam with one substituted model, not the consumer apps measured end to end. [Results and caveats](https://personalagentbench.com/results/)

[Where it runs](#execution)
:   One Linux VM per user

[How tools are exposed](#tools)
:   **246** permissions; schemas loaded per group

[Where memory lives](#memory)
:   Plain markdown in a home directory

[What you get to approve](#control)
:   One gatekeeper for approvals and egress

[How you reach it](#channel)
:   Apps, web, WhatsApp; Mac untested

[What we could not establish](#unknown)
:   Everything sent to the model

Product **Meta**Last verified **2026-11-11**September 2026 own-draw result **19% of tasks, 95% CI 13 to 25, n=90; 2026-09-22, adapted runtime with substituted exam model; after adapter repair**. [Provenance: differing scored subsets; first-batch records unpublished](https://personalagentbench.com/results/).

What users and reporters say went wrong with Muse, checked against this teardown: [Meta Muse review](https://personalagentbench.com/meta-muse-review/)

## Meta Muse, one recorded run on video

[视频：一次录制的购物实测——Muse 复制品的完整过程](https://www.youtube.com/watch?v=LIoht5S9Ilg)

One recorded grocery run of our Muse replica (rebuilt runtime, one substituted model, simulated shop), walked through step by step: what the agent did, and what it said it did. The full logs: [shopping runs](https://personalagentbench.com/runs/shopping/), [real-time alert runs](https://personalagentbench.com/runs/realtime/).

Meta Muse is Meta's personal agent, rolling out in the US since 8 September and, per [Meta's Japanese newsroom](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/), in Japan since 23 October, its first market outside North America. Singapore followed on 27 October, per [Meta's announcement](https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/). How does Meta Muse work? It gives every user a Linux machine. Not a metaphor, not a container abstraction you never see: sign in and there's a VM waiting, and the agent lives on it. [Meta's launch post](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) said it was powered by Muse Spark and is free for most of what people need, with subscription plans for more; what we could find on price is in the pricing section below. On 12 October Meta [announced Muse Wonder](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/), a larger model it says will soon power more of Muse, starting with subscribers. On 9 November Meta [introduced Muse Ember](https://research.meta.ai/blog/muse-ember), which it calls its smallest model, for the tool calls and short coding jobs an agent repeats. It is available in Muse Code and on the Meta Model API. The post puts Wonder on the hardest problems, leaves Spark on coding and agentic work, and puts Ember on the repeatable jobs. It does not say Ember now powers the Muse agent. Everything on this page was observed on the Spark-era runtime, not on Wonder or Ember.

- The model request is assembled on your own VM rather than fetched from a server as a finished package.
- A small fixed skeleton carries the routing rules. Everything personal is embedded from plain markdown files in a home directory.
- Tool permissions and tool definitions are deliberately separated. The permission sheet carries no parameters at all.
- Editing one of your own context files inserts a short note rather than rebuilding the whole request.
- What Meta says it can do, from sending an email to checking out with a one-time card or negotiating a bill, is set out errand by errand below, next to what we saw and how our replica did. The surface we took apart is the web one.

The claims below are limited to what we could establish from the examined web surface. Credentials, interactive terminal access and model traffic remained unavailable. Those gaps prevent conclusions about user file access or the complete security boundary. No internal codename, hostname or machine path is reproduced.

## How Meta Muse works: the request is built on your machine, not fetched as a finished blob

Most agents assemble the model request on a server and ship the result. Muse assembles it on your VM.

The fixed part is a small skeleton, around fifty lines, mostly routing rules. Everything personal gets embedded into that skeleton from plain markdown files in your home directory. Different jobs get different subsets: the main chat gets the full set, subagents run without the workspace conventions, and a background loop that maintains memory gets almost nothing but your profile.

Assembling locally is a stranger choice than it sounds, and it has one consequence you can feel. Change one of those files and the runtime doesn't rebuild the whole package; it slips in a short note saying the context changed. That's cheaper than re-sending everything, and it means the model sees the edit as an event rather than as a silently different world.

### A hundred and forty-one system insertions in a single session

On top of the skeleton sit the per-turn insertions, and there are a lot of them.

On the VM we watched, 141 system-role messages were being computed for one session: greetings, file-change notices, hourly memory passes reporting their own progress, subagents narrating where they've got to, research tasks checking in. Each one is small. Together they're a running commentary that the model reads and you never see.

This is the part of Muse that would surprise most people who assume a chat agent is a conversation plus a system prompt. It's a conversation, a system prompt, and a continuous stream of machine-generated notes about what the rest of the system is doing.

## What can Meta Muse do? Errand by errand, Meta's word and what we saw

There are two kinds of answer to what Meta Muse can do, and they are kept apart here. One is what Meta says it is for, from its [launch post](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) and the Mac app coverage. The other is what we can stand behind: what the examined web runtime is wired to do, and how a replica of it did on our errands. The replica is not the shipping product. It is our rebuilt runtime with one substituted model, working against simulated shops, inboxes and booking services.

- **Email and calendar.** Meta's examples include "sending an email", and it says you choose whether Muse only reads your mail or can also send on your behalf, with a check before it sends. The Mac app, per [The Verge](https://www.theverge.com/tech/997332/metas-muse-ai-agent-now-has-a-mac-app), works inside Messages, Calendar, Notes and mail. What we saw: connectors arrive on a permission sheet where each method is marked allowed, ask first or refused (the next section). We never connected a live inbox, so we have not watched it handle real mail.
- **Shopping and paying.** Meta says Muse can check out with Link by Stripe, whose agent wallet "generates a one-time-use card so your real card details stay hidden", with Shop Pay to follow, and that it asks before a purchase. What we saw: approvals and anything leaving the machine pass through one gatekeeper. Our replica's grocery runs are on the [shopping run page](https://personalagentbench.com/runs/shopping/), including the one in the video near the top of this page, where the cart total ended at an absurd figure and the reply did not match the log. Which shops it can reach has moved since launch. Amazon cut Muse off from Amazon.com on 20 September; its spokesperson told [GeekWire](https://www.geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping/) that agents buying for customers "should operate openly and respect service provider decisions about whether or not to participate", and Muse users saw a notice citing Amazon's Conditions of Use. Three days later Meta's [Connect post](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) said it was adding Walmart, Best Buy, Sephora, Wayfair and others, and on 21 October [Walmart wrote](https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers) that the ways it serves customers include conversational commerce integrations with Muse, ChatGPT, Gemini and others.
- **Travel and bookings.** Meta names "booking travel" and says Muse "can open a browser, fill out forms". What we saw: browser work spawns a second machine rather than driving the Chrome on your desk, so what it can reach depends on what is passed to that machine.
- **Bills, forms and negotiating.** Meta's examples include "lowering a bill" and "selling a car for more", and it says Muse can "negotiate on their behalf". It lists 1Password support so Muse can use logins you already have. What we saw: nothing we tried from our account got to a credential. Meta's own account, summarised further down, says the agent only ever holds stand-ins.
- **Phone calls.** The guidance inside the product described business calling as early access. Our account never received it, so we have no Muse call to report.
- **Plans that run while you are away.** Meta says Muse "keeps working after people close the app", can adjust a training plan as your week shifts, turn a recipe reel you saved on Instagram into a grocery list, and remember friends' dietary restrictions before it sends dinner invites. What we saw fits the plumbing for that: a background loop that maintains memory on an hourly pass, and memory kept as plain files.
- **Files on your Mac.** Meta says, as reported by [TechCrunch](https://techcrunch.com/2026/09/18/metas-muse-hits-mac-letting-the-ai-take-actions-on-your-computer/), that the Mac app can organise files and fill in forms. We have not examined the Mac app.

How the replica did, scene by scene, is below. These are counts of recorded attempts, with each scene linked to its records.

| Errand scene | Recorded attempts | Reached the goal | Did not |
| --- | --- | --- | --- |
| [Bookings and tickets](https://personalagentbench.com/runs/booking/) | 27 | 14 | 13 |
| [Email, calendars and group chats](https://personalagentbench.com/runs/email-calendar/) | 22 | 3 | 19 |
| [Forms, accounts and permissions](https://personalagentbench.com/runs/life-admin/) | 18 | 5 | 13 |
| [Alerts from live data](https://personalagentbench.com/runs/realtime/) | 6 | 3 | 3 |
| [Shopping carts and checkout](https://personalagentbench.com/runs/shopping/) | 8 | 4 | 4 |
| [Flights and check-in](https://personalagentbench.com/runs/travel/) | 7 | 2 | 5 |
| [Files and drafts](https://personalagentbench.com/runs/workspace/) | 11 | 3 | 8 |

Our Muse replica: rebuilt runtime, one substituted model, simulated services. Attempts recorded 11 October 2026 to 14 October 2026. Counts of records, not completion rates, and not comparable across products.

Read them as a map of where to look. The scenes hold different tasks, some tasks were attempted more than once, and none of it says how the shipping app does on your errands. Completion rates with intervals, batch by batch, are on [the results page](https://personalagentbench.com/results/).

## Meta Muse's two tool layers, kept deliberately apart

The permission sheet lists 52 connectors and 246 methods, and it carries no parameters at all. Each entry knows what it's called, what it belongs to, and whether it's allowed, asks first, or is refused. Nothing about how to call it.

The real definitions load separately, one namespace at a time, when something needs them. There are 58 skills, each a document the agent reads before acting rather than a function it calls.

Splitting it this way is the right call and more products should copy it. You get a cheap, stable permission contract that doesn't change when an API does, and the expensive part of a tool definition only enters the context when it's about to be used. It also means the question "what is this agent allowed to touch" has a short, readable answer that doesn't require parsing a thousand JSON schemas.

## How Meta Muse stores memory: readable files, access unverified

Your profile, your long-term notes, the assistant's own personality: markdown in a home directory, embedded straight into the request.

That makes "what does it think it knows about me" a question with a literal answer, sitting on a filesystem, in a format a person can read. Muse is not alone in that: Instinct also keeps markdown memory files, under version control in a sandbox. Pine keeps a server-side fact layer and Town a server-side wiki and memory store. Muse's files sit in a home directory on a machine assigned to you rather than shared with other users.

We stop short of saying you can read them yourself. The web surface can't leave that directory tree, an interactive terminal was never opened to us, and we're not going to claim you have a text editor on your own VM when we didn't verify it. The distinction between "the files exist in a readable format" and "you can read them" is exactly the kind of thing that gets rounded off elsewhere, and we're not rounding it off.

Meta's own [security write-up](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) goes further: it says you can inspect, edit and download the files on your VM, including what Muse remembers about you. That's the vendor's account and it may well be right. The sentence above is about what we saw, so it stays as written.

### Where you reach it, and which of those we tested

Muse launched on 8 September on iOS, Android and the web, and [Meta's launch post](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) says you can also message it directly in WhatsApp. A Mac app followed on 17 September. Meta says, as reported by [The Verge](https://www.theverge.com/tech/997332/metas-muse-ai-agent-now-has-a-mac-app) and [TechCrunch](https://techcrunch.com/2026/09/18/metas-muse-hits-mac-letting-the-ai-take-actions-on-your-computer/), that the Mac app can organise files, fill in forms, and work inside Messages, Calendar, Notes and mail, with access switched on app by app and an approval step before anything sensitive.

The guidance shown in our teardown account described business calling as early access with a gradual rollout. That account did not receive it. We have not rechecked the current rollout or observed a Muse call, so this is a limit of our examination, not a claim that other accounts cannot call businesses.

We took apart the web surface. Nothing on this page covers the others, and the Mac app least of all.

On scale, Meta's own number and the outside estimate are different measures. On Meta's 21 October earnings call, Mark Zuckerberg told analysts that more than 10 million people in the US and Canada had set up Muse accounts, and said "about 25% of people who have set up Muse use it on any given day", as reported by the [Associated Press](https://www.ksat.com/business/2026/10/21/meta-q3-revenue-tops-estimates-and-zuckerberg-says-muse-accounts-have-topped-10-million/). A day earlier [TechCrunch](https://techcrunch.com/2026/10/20/metas-muse-hits-10m-u-s-downloads-in-40-days-a-milestone-reached-by-only-11-other-apps/) reported an estimate from the app-data firm Sensor Tower of 10.9 million downloads, 10.2 million of them in the US. That is a third-party estimate of downloads, not Meta's count of accounts.

That distinction matters. Browser work in the web product spins up a second machine rather than driving the Chrome on your desk. Instinct also sends browser work to a separate cloud browser, while Pine's Mac app hands it to a helper on your own computer. A separate machine is not the browser you are signed into at home, so what it can reach depends on what the product passes to it. We did not compare security outcomes between these routes. A desktop app that acts in your own mail and messages is a different arrangement again, and it hasn't been through the same examination.

On 2 October Meta also published an open-source kit for building small devices that pair with Muse. It opens the devices, not the agent: what is and is not open is on [Is Meta Muse open source?](https://personalagentbench.com/is-meta-muse-open-source/).

## Meta Muse vs Pine, Instinct and Town: different answers to the same question

Put the tool surfaces side by side and the design philosophies stop being abstract.

Pine exposes 26 names and no schemas, so you know a capability exists and nothing about its edges. Instinct exposes a command line and refuses to run an action until its manual has been read, so the definition arrives exactly when it's needed and is paid for in tokens. Town lists 1105 tools and narrows to about 177 through four filters, so the catalogue is enormous and the reachable set is small. Muse splits the question in half: a permission sheet that says what is allowed without saying how, and definitions loaded a namespace at a time.

Muse exposes a distinct parameter-free permission sheet in the examined surface, allowing the runtime to list permitted methods without loading their schemas. Town also filters tools by configuration and allow-lists; our observations do not establish that Muse alone separates permission from definition.

The trade is visibility. Pine's opacity is a product decision you can observe from outside. Muse's opacity is structural: the request is assembled on a machine we can describe, by a runtime we can describe, and sent somewhere we never saw. Knowing the shape of a thing is not the same as having seen it move.

## What does Meta Muse Charm do? A pocket front end for the same agent

Muse Charm is the first device Meta has built for Muse. Mark Zuckerberg showed it at the end of the Connect keynote on 23 September and said it would launch in time for the holidays in December, as reported by [The Verge](https://www.theverge.com/tech/999944/meta-muse-charm-ai-interact-5g-modem); Meta has not announced a price. Meta's [Muse Charm page](https://www.meta.com/muse-charm/) presents it as a way to hand off everyday tasks and names three: finding deals, booking reservations and managing your inbox. We have not seen or used one. What follows keeps three sources apart: what Meta has said, what Bloomberg reported, and what our teardown of the agent behind the device implies.

**What Meta has said.** Its [Connect post](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) says the Charm brings Muse and a real-time voice model into a device that fits in a pocket, with more to share later this year. [Digital Trends](https://www.digitaltrends.com/wearables/metas-muse-charm-puts-an-ai-assistant-on-your-keychain-no-phone-required/) reported from the keynote that you start talking by tapping a fingerprint sensor, without unlocking a phone or opening an app, and that Meta had built only a handful of units and had not settled the finish or the layout of the parts.

**What Bloomberg reported.** As relayed by [The Verge](https://www.theverge.com/tech/999944/meta-muse-charm-ai-interact-5g-modem), the Charm has a built-in 5G modem, so it reaches Muse without Wi-Fi. It also has a two-inch OLED touchscreen running a new operating system, plus cameras for photos and video and for giving Muse a view of its surroundings. Speakers, microphones and a USB-C port round it out. You set it up through the Muse app on iOS or Android, and it can recognise other Charms nearby. Sources told Bloomberg it would likely cost about as much as a smartwatch, with carrier fees for 5G not yet decided. Meta's own posts do not mention cameras and some coverage says there are none, so the camera is reported rather than confirmed until Meta publishes specifications.

**What the agent behind it implies.** The Charm is not where Muse lives. On the runtime we took apart, the agent runs on a Linux VM that Meta provisions for each user in its cloud, and the phone, web and Mac apps are ways of reaching it. Nothing announced so far says the Charm changes that, and a 5G modem points the same way: a device that needs a network connection to talk to an agent somewhere else. If that holds, three things follow.

- **The errands are the same errands.** Finding deals, booking a table and working through an inbox are what Muse does from any surface, and the [errand-by-errand section above](#what-can-meta-muse-do-errand-by-errand-meta-s-word-and-what-we-saw) sets Meta's claims next to what we saw. On reservations, our replica booked [a cafe table that needed no payment](https://personalagentbench.com/runs/booking/#run-1012-muse-owner-ambiance-venue-booking) but could not add it to a calendar, and a [reschedule](https://personalagentbench.com/runs/booking/#run-1012-muse-food-restaurant-booking-reschedule) ended in the wrong final state while the reply described a confirmed table. Each ran once; the wider picture is on [book a table](https://personalagentbench.com/tasks/book-a-table/).
- **The permissions are the same permissions.** Connectors are allowed, ask first or refused on one sheet, and Meta says approval prompts go to the app rather than through the conversation. How an approval appears on a two-inch screen, or whether the Charm can grant one at all, is something Meta has not described.
- **What it hears goes to the same machine.** Voice, and camera input if the Bloomberg report is right, would be inputs to the agent on your VM, under the data terms Meta set out at launch: training use you can opt out of, and conversations and VM data kept out of its ad systems (more in the next section). Meta has not said whether anything captured by the Charm is handled differently.

On 2 October Meta also opened a [kit for building small devices](https://personalagentbench.com/is-meta-muse-open-source/) that pair with Muse. It covers hobby boards, not the Charm, and every gadget needs a token from Meta to pair, which fits the same pattern: small devices as windows onto one account. Nothing in this section is a review of the Charm.

## What Meta says it built around the agent

Meta published its own account of the security design on launch day, in a [newsroom post](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) and a much longer [engineering write-up](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse). It describes the product from the inside, which is the view we didn't have, so it's summarised here as Meta's claim and kept apart from what we observed. Both component names below are Meta's own public ones.

- Each user gets a dedicated machine in Meta's cloud, which Meta calls Muse Secure VM. The agent's workspace runs in an isolated cell on that machine, separate from the services that guard it.
- A second agent, which Meta calls Sentinel, runs on the same machine outside the agent's reach. Meta says it's the only thing that can approve a connector action or let a network request out, and that the agent can't override it.
- The agent never holds your real passwords or tokens. It works with stand-ins, and the real credential is swapped in at the network boundary once a request is approved.
- Approval prompts go straight to the app rather than through the conversation, and a grant can be one-time, per session, per task, time-limited or perpetual.
- When you take over the browser, the agent is paused and can't act.

[Meta’s launch post](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) says users can opt out of interactions being used to train its models. It separately excludes conversations and VM data from its ad systems. Those are different uses of the data.

Two passages deserve the same attention as the rest. Meta says today's design restricts staff access to your data through operating policy, and that it doesn't stop Meta from reaching that data when it needs to support, secure or run the service. The version that would, Muse Confidential VM, encrypted with a key only you hold, is promised for later this year. Until it ships, it's a plan.

We haven't tested any of this. It's here because it's the builder's own description, dated and linked, and a reader deciding whether to connect an inbox should see it next to what an outside examination could and couldn't reach.

## When something goes wrong on a Meta Muse VM

Every architecture here has a failure story, and the per-user VM has a specific one.

When a product runs your agent in a shared service, a bad afternoon for the service is a bad afternoon for everybody, and that is hard to miss. When each user has a machine, a problem can be yours alone: your VM, your state, your stuck process. That's better for isolation and worse for detection, because nobody else's dashboard lights up when it happens to you.

The same cut runs through the good news. Meta describes each VM as an isolated Linux box dedicated to one user, so your home directory is not meant to share a store with anyone else's. We did not test cross-user isolation, and Meta does not say whether the hardware underneath is shared. For a product holding a profile of you written in plain language, that boundary is worth a great deal.

That is a trade rather than a flaw.

## What we couldn't establish

The list below is short, and every line on it is a thing we tried and failed to get rather than a thing we didn't think to ask.

- The traffic between the runtime and the model. We know the structure of what goes in; we never saw a single one of the actual requests leave.
- Credentials. Meta keeps them outside the agent's reach, as described above, and nothing we tried from our own account got to one. Nothing on this page comes from a credential.
- Live third-party sign-ins. Never connected, so every integration we describe is described from its contract rather than from watching it work.
- An interactive terminal. The owners chose not to open one.

Meta's [launch description](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) presents shopping, email and planning as user-facing jobs. These are claims about what the product is for, not measurements that it completes them reliably. Our observed web runtime is narrower evidence than the whole app family, including Mac features and business calling we did not exercise.

## FAQ

**What is Meta Muse?** Meta's personal agent. Each user gets their own Linux VM, and the agent runs on that machine: assembling its own model requests, reading skills as documents, and keeping your profile and memory as markdown files in a home directory.

**Does Meta Muse run on my own computer?** The agent runs on a Linux virtual machine provisioned for you in Meta's cloud, which Meta calls Muse Secure VM. The model itself runs elsewhere; the VM is where the request gets assembled and where the tools execute. Since 17 September there is also a Mac app that Meta says can act in apps on your computer, with access granted app by app. We haven't examined it.

**How many tools does Meta Muse have?** Two layers. A permission sheet covering 52 connectors and 246 methods, which carries no parameters, and 58 skills that load a namespace at a time when something actually needs them.

**Can I read what Meta Muse remembers about me?** The files exist as plain markdown in a home directory. Whether you personally can open them is something we could not verify, because no interactive terminal was available to us. Meta's security write-up says you can inspect, edit and download them. Of the other three, Instinct also keeps markdown memory files, and Pine and Town keep memory server-side.

**Which model does Meta Muse use?** At launch Meta named Muse Spark, and its security write-up names Muse Spark 1.3. On 12 October Meta announced Muse Wonder and said it will soon power experiences in Muse, rolling out to subscribers first, without giving a date for free accounts. On 9 November Meta introduced Muse Ember, its smallest model, for repeated tool calls and coding subtasks, available in Muse Code and through the Meta Model API. Meta did not say Ember now runs the Muse agent. Our teardown predates both later models, so nothing here describes Muse running on Wonder or Ember. Whether either is open is covered on [is Meta Muse open source](https://personalagentbench.com/is-meta-muse-open-source/#muse-ember-closed).

**Is Meta Muse available as an app?** Yes. It launched on iOS, Android and the web, can be messaged in WhatsApp, and has had a Mac app since 17 September. What we tested is the web surface.

**Is Meta Muse available in Japan?** Yes, according to Meta. Its [Japanese newsroom](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/) says Muse opened in Japan on 23 October (Japan time) on iOS, Android and muse.ai, the first market outside North America, with most basic features free and subscription plans for more; it gives no yen prices and does not mention a waitlist or invitations. It presents Gmail, Google Calendar and Instagram as connectors for apps Japanese users already have, and also names Stripe, Shopify, Trip.com, Agoda and Klook for shopping and travel, without saying whether each of those five works in Japan today. Links with Mercari, Money Forward ME and Ticket Pia are described as in progress, and Japanese availability of the advanced voice mode, Muse Realtime Avatar (English only) and Muse's own email address will be announced separately. We have not used the Japanese service.

**Is Meta Muse available in Singapore?** Yes, according to Meta. Its [27 October announcement](https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/) says Muse is available in Singapore on iOS, Android and muse.ai, free for most of what people need with subscription plans for more, and coming soon to AI glasses. It names Shopee and Lazada for comparing products, GrabMart and Grab Dine Out for groceries and dining, Singapore Airlines, Agoda, Klook and Trip.com for travel, and ShopBack for cashback, alongside Gmail, Google Calendar and Instagram. It also says connector features will roll out progressively, so not every one of those may work on day one. [Skift reported](https://skift.com/2026/10/28/agoda-plugs-into-metas-muse-in-singapore-and-japan/) on 28 October that Agoda's connector covers Japan as well, and that in Singapore Muse books through direct connectors from the start, where in North America it first worked Expedia and Hotels.com through a browser. We have not used the Singapore service.

**How does Meta Muse compare with Pine, Instinct and Town?** The examined Muse runtime has a parameter-free permission sheet and assembles the model request on a per-user VM. Town also separates configured permissions from returned tool schemas, so permission separation is not exclusive to Muse. Pine shows the least of its tool surface, Town's Mac app reaches deepest into the system of the desktop apps we examined, and Instinct lives in your message threads. Pine places phone calls today; our Muse account did not receive business calling during the teardown, and we have not rechecked its current rollout.

**Can Muse access my bank account?** Reading your data and acting in your account get different answers. Reading: Muse's Finances feature connects accounts through Plaid, and Plaid's [8 September post](https://plaid.com/blog/meta-muse/) says you can share balances, transactions, investment holdings and mortgage information, managed in Plaid Portal; it does not say whether Muse can move money. Acting: JPMorgan Chase told [CNBC](https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html) on 13 October, in a report that names Muse, that it does not let third parties log in with customers' banking credentials; Citi said much the same, and Schwab said it blocks agents that log in for clients. The detail is on [dispute a charge](https://personalagentbench.com/tasks/dispute-a-charge/#can-an-ai-agent-get-into-your-bank-account-where-banks-drew-the-line-in-october). What we saw: on the cloud machine we examined, nothing we tried from our account reached a credential. Separately, Meta says the agent only holds stand-ins, with the real credential swapped in at the network boundary once a request is approved; we have not tested that, or the Finances feature. In our exam, the replica's one attempt to read a balance with a temporary login [never got past the login page](https://personalagentbench.com/runs/life-admin/#run-1012-muse-digital-account-password-boundary) and said it was reading it.

**What is Muse Charm?** A pocket-sized device for talking to Muse, announced at Meta Connect on 23 September. Meta's [Connect post](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) says it brings Muse "with a state of the art real-time voice model into a device that fits in your pocket", and Zuckerberg said it would launch in December; Meta has given no price. Its screen shows a cartoon avatar that can be set to several characters, including a Muse mascot called Jolly, [according to Dezeen](https://www.dezeen.com/2026/09/25/meta-debuts-tamagotchi-style-ai-agent/). The agent itself still runs on your VM in Meta's cloud; what that means for the Charm is in [what Muse Charm does](#what-does-meta-muse-charm-do-a-pocket-front-end-for-the-same-agent). We have not seen or used one.

**Does Muse Charm have a camera?** Reported, not confirmed. Bloomberg, as relayed by [The Verge](https://www.theverge.com/tech/999944/meta-muse-charm-ai-interact-5g-modem), reported cameras for photos, video and giving Muse a view of its surroundings, alongside a 5G modem and a two-inch OLED touchscreen. Meta's own announcements do not mention a camera, and some coverage says it has none. Until Meta publishes specifications, treat it as open.

**Can Muse make business calls for me?** Meta describes business calling as an early-access rollout. The web account we examined did not receive it, so we have not observed a call or tested its handover and approval flow. Availability in your account needs checking separately.

## Where Meta Muse lands on the personal agent scorecard

Muse's defining choice is a machine assigned to each user: the request is assembled there, the tools run there, and memory is kept there as files a person could read. The same arrangement kept the thing we most wanted to see, a request leaving that machine for the model, out of our view.

The [scorecard](https://personalagentbench.com/) sets it against Pine, Instinct and Town on the same six axes, with what we failed to establish written into the table rather than left out of it.

## Meta Muse compared with the others we opened

Side by side on the same axes, against [Instinct](https://personalagentbench.com/muse-vs-instinct/), [Pine](https://personalagentbench.com/muse-vs-pine/) and [Town](https://personalagentbench.com/muse-vs-town/). We only build these for pairs we have taken apart ourselves, because a comparison with marketing on one side is the thing this site exists to replace.

## What Meta Muse costs

Muse has no pricing page of its own and sits behind a Meta account. Meta's launch post says it is free for most of what people need, with subscription plans for people who want to do more, and it names no prices.

That is worth stating plainly rather than leaving the section empty: a product with no published price is not one we failed to check.

Read on 2026-09-24: [Meta newsroom, Introducing Muse (8 September 2026)](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/).

No price stated in the checked primary sources as of 2026-09-23; those sources are listed below.

### A dated third-party snapshot, not current pricing

A writer's account of the upgrade options shown in their own Muse account the day after launch. The free allowance is the figure the writer attributes to Mark Zuckerberg in an interview. Meta has not published these numbers on a pricing page, and we have not been able to check them ourselves. Every's comparison, checked on 12 October 2026, also reports Power at $20/month and Maximum at $100/month. The token allowances below remain the 9 September MBI snapshot.

| Plan | Price | Weekly allowance |
| --- | --- | --- |
| Free | $0 | up to 100 million Muse tokens a week |
| Power | $20/month | 500 million Muse tokens a week |
| Maximum | $100/month | 3 billion Muse tokens a week |

As reported by [MBI Deep Dives, First Impression of Muse](https://www.mbi-deepdives.com/muse/) on 2026-09-09. Not a Meta pricing page, and not rechecked by us.

Also reported by [Every personal agent comparison](https://every.to/personal-agents-comparison), checked 2026-10-12. This is independent reporting, not a Meta price list.

## Meta Muse, axis by axis

## Meta Muse: where it runs

One Linux VM per user. The request is assembled on that machine rather than fetched as a finished blob. Browser work spawns a second, separate machine.

## Meta Muse: how tools are exposed

Two layers kept deliberately apart: a permission sheet of 246 methods carrying no parameters at all, and the real definitions loaded a namespace at a time when needed.

## Meta Muse: where memory lives

Plain markdown in a home directory, embedded straight into the request. Changing one of those files inserts a short note rather than rebuilding the whole package.

## Meta Muse: what you get to approve

Permissions and approvals are not scattered through the runtime. A single gatekeeper is the only path to them, along with anything leaving the machine, and the interface carries an approvals tab beside the activity feed. Credentials are held outside the agent's reach by the same arrangement. The examined runtime includes file removal and a forget capability. Whether users can directly open or remove their memory files was not verified.

## Meta Muse: how you reach it

Launched on iOS, Android and the web, and reachable in WhatsApp. A Mac app since 17 September can act in apps on your computer. We tested the web surface only.

## Meta Muse: what we could not establish

The raw traffic between the runtime and the model: structure known, contents never seen. Also credentials, live third-party sign-in, and an interactive terminal the owners chose not to open.
