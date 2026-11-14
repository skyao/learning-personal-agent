来源：https://www.allthingsmuse.com/articles/building-with-muse-peter-yang/
取文：2026-11-13，直接下载

Creator Peter Yang put Muse to work on 10 real errands, from negotiating his phone and cable bills to tracking a phone-free bedroom goal. Here's each workflow

Creator Peter Yang spent years in product roles at Meta, Reddit, and Roblox. Now he writes the Creator Economy newsletter and publishes practical AI walkthroughs. In a 17-minute video, he put Meta’s Muse through 10 real errands from his own life (negotiating bills, scanning messages, booking a night out) and says the agent saved him over $800 a year on his bills alone. This is a walkthrough of each workflow, what worked, where it fell short, and how to replicate the useful ones.

## 1. Negotiating the AT&T Phone Bill

Yang started a “finances” thread and had Muse log into his AT&T account through its built-in browser. He stored his username and password in Muse’s secure store, and Muse found that switching his billing from a credit card to a bank account would save $10 per line per month. Across his lines, that came to $40 a month off a $200 bill.

When it came time to enter the bank account and routing numbers on AT&T’s site, Muse declined to do it for privacy reasons and Yang typed them in himself. The discount went live, and he says the whole thing took five to ten minutes of conversation for $480 a year in savings.

The interesting part is the division of labor. Muse handled discovery (logging in, reading the account, finding the discount lever) and stopped exactly where it should, at the moment real bank credentials needed to touch a third-party form. That boundary is the whole pitch for an agent with a secure credential store: it can act inside your accounts without you handing it the keys to everything.

## 2. Calling Comcast to Negotiate the Cable Bill

The cable negotiation went further: Muse placed an actual phone call to Xfinity customer support, one of the capabilities of [Muse’s phone-calling beta](https://www.allthingsmuse.com/articles/muse-phone-call-beta/). Yang picked a voice for the call, gave his name and number, and Muse called while he ate breakfast. On the call it introduced itself plainly: “Hey, this is Haley calling on Peter’s behalf.” It did not pretend to be him.

The call surfaced a $60-per-month promotional rate plus another $10 off for autopay, down from $84. One honest wrinkle: the Xfinity agent wanted Yang himself to call back to finalize the discount, so Muse did the research legwork rather than closing the deal. Yang calls the phone calling the killer feature and says every other AI system will copy it.

The value was that Yang ate breakfast while the agent sat on hold, navigated the phone tree, and came back with the exact rate and the exact ask. The ten minutes of hold music are the product.

## 3. Shopping Tesla Insurance

The finances thread did not stop at phone and cable. Yang has Muse gathering quotes to renegotiate his Tesla insurance, pulling in Geico, Progressive, and State Farm. It is still in progress in the video, but the pattern is the same: describe the bill, let the agent do the comparison shopping.

This is the workflow most worth copying even before you watch the video. Insurance repricing is a chore everyone postpones because it means the same conversation three times with three companies. It is exactly the kind of parallelizable, low-stakes research an agent is built for.

## 4. Setting It Up: Avatar and Connected Apps

Before any of the errands, Yang personalized the app. He had Muse generate a red panda avatar (four options, then four cuter ones) with animations for waving and typing. More importantly, he connected his apps. Beyond email and calendar, he points to native connections to Meta’s own apps (Instagram, Threads, Facebook, and Messenger) as the differentiator.

He also notes a limit: Muse could not connect to Linear, and he is fine with that. He reads it as focus. Normal users do not want to deal with API keys, so an agent built around everyday personal apps suits the job.

The setup sequence is the part most people skip and then wonder why the agent feels useless. Yang’s order of operations (personalize, connect apps, then assign errands) is the right one. An agent with no app connections is a chatbot; with them, it is an errand runner.

## 5. Watching His Messages for Anything Urgent

With the apps connected, Yang set up a scheduled task: every day, Muse checks his unread messages across Messenger, WhatsApp, and iMessage and flags anything that needs a follow-up, the same pattern as [Muse’s inbox triage](https://www.allthingsmuse.com/articles/muse-inbox-triage/). In the demo, his Instagram and Threads DMs turned out to be all spam, which is itself the point. One daily scan replaces checking four apps.

This is the easiest workflow on the list to replicate and the one with the best effort-to-value ratio. It takes one instruction to set up, runs on its own, and attacks the specific tax of modern messaging: the repeated checking to find out whether any messages matter.

## 6. Buying and Selling on Facebook Marketplace

Because Muse is connected to Facebook and Messenger, it works as a Marketplace assistant. Yang had it search for single golf clubs near him and got three listings he could open. Going the other direction, listing his old iPhone 13 Pro meant answering Muse’s questions about photos and price while it built the listing. And through Messenger, it can message sellers about availability and negotiate the price, confirming with Yang before it sends anything.

The confirm-before-sending detail is doing real work here. Marketplace negotiation is one of those tasks where autonomy feels risky. You do not want an agent committing you to a price. Yang’s setup keeps the agent in the draft-and-propose role for anything involving money changing hands, which is the right default.

## 7. A Personalized Morning Feed

Yang barely uses Facebook’s own feed anymore. He describes it as ads and AI slop, and instead starts the day with a feed he built inside Muse. He asked for important AI news on the topics he follows, and every morning he skims updates from the major labs, opening anything interesting in the browser. The feed is customizable, so he added personal material like his newsletter. His aside: there are no ads in it yet, and he assumes that changes if Muse gets big enough.

There is a quiet irony here worth naming: the way to fix a feed ruined by engagement optimization is a personal agent that filters for what you actually asked for. Yang is describing the oldest idea in RSS with a modern interface: tell software what you care about, get a clean feed back.

## 8. Breaking the Phone-in-Bedroom Habit

In the Goals tab, Yang built a system around his worst habit: bringing his phone to bed and doomscrolling at 5 a.m. Muse interviewed him about the trigger (scrolling), the replacement (reading books), and his bedtime (10 to 10:30), then made a plan with a visible artifact. Every night near bedtime it reminds him to leave the phone out of the bedroom; every morning it checks whether he did, tracking the streak on a chart.

His record so far: zero for two. He left that in the video, which makes the segment more convincing than a success story would. The same Goals tab also auto-builds a to-do list from his conversations: negotiating the cable bill, booking a Japan flight, making the Muse video itself.

The zero-for-two is the most honest moment in the video. A habit system that only works when you are already disciplined is not a system. The value proposition here is that the agent does the tracking and the reminding without you maintaining anything. Whether that is enough to beat a 5 a.m. doomscroll is, as Yang’s record shows, still an open question.

## 9. Researching a Purchase With Ideas

Yang asked Muse for a side-by-side comparison of electric razors. Five minutes later he had a browsed list of Best Buy product pages with a Panasonic recommendation. His critique is specific and useful: he wished it had checked review sites like Wirecutter instead of only retailer pages. The interesting part is the Ideas tab itself, which proactively suggests things based on his usage: calorie tracking from a meal photo, inbox triage, even reporting a pothole to the city.

The critique is the takeaway. An agent that only browses retailer pages will converge on whatever is in stock and well-listed, not what is actually best. Yang’s fix is simple: check independent review sources before recommending. That’s a good default instruction for any shopping agent, in Muse or anywhere else.

## 10. Booking Restaurants and Shows

Yang had Muse look up Bay Area concerts for a night out, then narrow it to a highly reviewed show at the Magic Theater on September 30, his anniversary, plus a nice dinner spot nearby. Booking two general admission tickets is one more instruction, executed through the browser. He also runs a recurring “weekend scout” that surfaces local events, which is how he found out about a comedy day in Golden Gate Park.

The weekend scout is the sleeper hit of the list. It is a standing instruction (“tell me about interesting local events each week”) that turns the agent from something you consult into something that brings you things. Most agent value lives in that shift, from reactive to proactive, and it costs one sentence to set up.

## The Workflows at a Glance

| # | Workflow | Category | What it demonstrates |
| --- | --- | --- | --- |
| 1 | AT&T bill negotiation | Money | Agent acts inside your accounts; stops at sensitive credentials |
| 2 | Comcast phone call | Money | Real phone calls with honest self-identification |
| 3 | Tesla insurance quotes | Money | Parallel comparison shopping |
| 4 | Avatar + app connections | Setup | Connect apps before assigning errands |
| 5 | Daily message scan | Attention | One instruction replaces checking four apps |
| 6 | Marketplace buy/sell | Money | Draft-and-propose with human confirmation |
| 7 | Morning news feed | Attention | Personal filter over engagement-optimized feeds |
| 8 | Phone-free bedroom goal | Habits | Reminders + tracking; honest about limits |
| 9 | Razor research via Ideas | Shopping | Browse + compare; check review sources as well as retailers |
| 10 | Concert + dinner booking | Planning | Standing “weekend scout” turns reactive into proactive |

## What Didn’t Fully Work

Yang is unusually honest about the gaps, and they are worth collecting in one place. Muse declined to enter bank credentials on AT&T’s site, the right call, but it means high-stakes financial actions still need you at the keyboard. The Xfinity agent wanted Yang himself to call back, so the phone negotiation did the legwork but didn’t close. The razor comparison skipped Wirecutter-style review sources. And the phone-free bedroom record stands at zero for two.

None of these are reasons not to use the agent. They are the current boundary of what it can do unsupervised, and knowing the boundary is what makes the rest trustworthy.

## How to Try It Yourself

Yang’s own advice at the end is the right starting point: pick one postponed errand, connect whatever app it needs inside Muse, and describe the outcome you want. The bill calls are the highest-value first try: a single “finances” thread with your logins stored can surface discounts you have been paying to avoid finding. The daily message scan is the easiest: one scheduled instruction, and four apps collapse into one summary.

Two defaults worth setting from his experience: tell any shopping agent to check independent review sources before recommending, and keep the agent in draft-and-propose mode for anything where money changes hands.

## The Stack It Fits Into

Yang closes by placing Muse in his lineup: ChatGPT for everyday work, Grok for cloud tasks that run without his computer on, and Muse for everything personal. He says Muse was a top-three App Store app within a week of launch, and he is blunt about why he is bullish: Meta can promote it across Facebook, Instagram, and WhatsApp the way it once pushed Stories and Threads.

[视频：Meta’s Muse AI Agent Saved Me $800+ a Year on My Bills (10 Real Use Cases)](https://www.youtube.com/watch?v=eU1ICyI9bCs)

## Frequently Asked Questions

**Who is Peter Yang?**
Peter Yang spent years in product roles at Meta, Reddit, and Roblox. He now writes the Creator Economy newsletter and publishes hands-on AI walkthroughs. His Muse video is a 17-minute tour of 10 real errands he runs through Meta’s personal AI agent.

**How did Muse save Peter Yang over $800 a year?**
Mostly through two bill negotiations. Switching his AT&T billing from credit card to bank account saved $40 a month ($480 a year), and the Comcast call surfaced a $60-per-month promotional rate plus $10 off for autopay, down from $84. Together that is over $800 a year in savings.

**Can Muse really make phone calls on your behalf?**
Yes. In the video, Muse placed a real call to Xfinity customer support, introduced itself as calling on Yang’s behalf without pretending to be him, and navigated the call while he ate breakfast. One caveat: the Xfinity agent wanted Yang himself to call back to finalize the discount.

**Is it safe to give Muse your account logins?**
Muse has a secure credential store for usernames and passwords, and Yang used it for his AT&T login. But there are limits: when the AT&T site needed bank account and routing numbers, Muse declined to enter them and Yang typed them himself. Sensitive financial credentials still stop at the keyboard.

**What apps does Muse connect to?**
Beyond email and calendar, Yang highlights native connections to Meta’s own apps, Instagram, Threads, Facebook, and Messenger, as the differentiator. He notes Muse could not connect to Linear, which he reads as intentional focus on everyday personal apps rather than developer tools.

**What is the easiest Muse workflow to start with?**
The daily message scan. One scheduled instruction replaces manually checking four apps: check unread messages across Messenger, WhatsApp, and iMessage every day and flag anything needing a follow-up. It takes a minute to set up and runs on its own.

**Does Muse work for building habits?**
Yang built a phone-free bedroom system in the Goals tab: nightly reminders, morning check-ins, and a streak chart. His record so far is zero for two, which he left in the video. The agent handles the tracking and reminding reliably; whether that beats the habit itself is still up to you.

**How is Muse different from ChatGPT or Grok for this kind of work?**
Yang’s own lineup: ChatGPT for everyday work, Grok for cloud tasks that run without his computer on, and Muse for everything personal. The differentiator in the video is the combination of connected personal apps, real phone calling, and proactive scheduled tasks.
