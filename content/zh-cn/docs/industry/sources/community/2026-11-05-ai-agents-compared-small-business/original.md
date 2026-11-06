来源：https://freistyle.ai/blog/ai-agents-compared-small-business
取文：2026-11-06，直接下载

AI Agents Compared: Which One Should a Small Business Try First? (2026)

Six always-on agents from OpenAI, Anthropic, Google, Meta, xAI and Microsoft: what they do, who can use them today, what they do with your data, and how to set one up safely.

By Dominic Frei · November 5, 2026 · 16 min read

Key Takeaways

- Six always-on AI agents launched or reached small businesses in 2026: ChatGPT dots (OpenAI, September 29), Claude Duet (Anthropic, October 21), Tasks in Gemini (Google, formerly Spark), Muse and Muse for Small Business (Meta, September), Grok Bot (xAI, August) and Copilot Cowork (Microsoft, June). All six run on their own cloud computer and keep working when you close your laptop.
- Most of them aren't available to most small businesses yet. Duet is a US waitlist for Claude Pro and Max. Muse is US only. Tasks in Gemini needs a personal account and isn't offered in the EEA, Switzerland, the UK or Nigeria. Dots start with ChatGPT Pro and Business Premium in eligible markets. Cowork needs a Microsoft 365 Copilot licence.
- Every vendor says its agent asks before sending, paying or deleting. They differ on what happens to your data: OpenAI and Microsoft don't train on business-workspace content by default, Meta lets you opt out, Google's Tasks require Keep Activity, and xAI's Bot page makes no data statement at all.
- The right first agent is the one that lives where your business already lives: Gmail and Google Workspace point to Tasks in Gemini, Instagram and WhatsApp to Muse, Microsoft 365 to Cowork, ChatGPT to dots. Start with one read-only job and keep every send behind your approval.

An AI agent is an assistant that works on its own cloud computer, connects to your apps and keeps going while you do something else, instead of answering one question at a time. In 2026 every major AI company shipped one: OpenAI's dots, Anthropic's Claude Duet, Google's Tasks in Gemini, Meta's Muse, xAI's Grok Bot and Microsoft's Copilot Cowork. For a small business the useful question is which one you can use at all, because region, account type and plan rule most of them out today, and which jobs are safe to hand over first. The short answer: pick the agent that lives where your business already lives, give it one read-only job for a week, and keep every send, payment and deletion behind your approval.

I read each company's own announcement, help pages and pricing pages between October 27 and 28, 2026. Six products from six companies, so some of it changed while I was reading, and some of it will change again by the time you read this.

## What is an AI agent, and how is it different from a chatbot?

A chatbot answers. An agent does, and it does it while you're away. Four things separate the agents in this article from the chat windows most people use:

- Its own computer. OpenAI's dots, Claude Duet, Muse and Grok Bot each run on a cloud machine with its own browser. Tasks in Gemini and Copilot Cowork run in the cloud too. Your laptop can be closed.
- Connected apps. The agent reads your inbox, calendar, files, shop or CRM once you connect them, and it can act inside them.
- Goals instead of questions. You hand over "watch my inbox and draft replies" or "book the three suppliers for next week", and it works through the steps.
- Approvals. Every vendor says its agent stops before sensitive actions, such as sending, paying or deleting, and asks you.

That last point is the whole risk picture. An agent that reads your email is exposed to whatever is in your email, including instructions a scammer hid in a message. OWASP ranks prompt injection as the number one risk for AI applications ([OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)), and Google's own help page warns that a website, email or document can contain hidden instructions that make the agent share your private information or send your emails to an outside service ([Google Help](https://support.google.com/gemini/answer/17094507?hl=en)). Keep that in mind in every section below.

## The six agents at a glance

| Agent | Maker | Launched | Who can use it today | What you pay |
| --- | --- | --- | --- | --- |
| dots | OpenAI | September 29, 2026 | ChatGPT Pro, Business Premium and Enterprise (admin-enabled) in eligible markets | First dot included: Pro from $100 a month; Business Premium $125 per user a month, or $100 billed annually |
| Claude Duet | Anthropic | October 21, 2026, research preview | Claude Pro and Max subscribers in the US, by waitlist | Included in the plan's usage: Pro $20 a month ($17 annually), Max from $100 |
| Tasks in Gemini | Google | May 2026 as Spark, renamed Task | Personal Google Accounts on AI Pro or Ultra; not in the EEA, Switzerland, the UK or Nigeria | Google AI Pro $19.99 a month, Ultra from $99.99 |
| Muse and Muse for Small Business | Meta | September 8 and September 29, 2026 | US only; message it in the Muse app or WhatsApp | Free for most uses; paid plans Power $20 and Maximum $100 a month |
| Grok Bot | xAI | August 11, 2026, beta | Premium, Super, Ultra and Teams plans; apps for macOS, Windows, Linux and iOS | Premium $30 a month, Super $100, Ultra $200, Teams from $30 per user |
| Copilot Cowork | Microsoft | June 16, 2026 | Businesses with a Microsoft 365 Copilot licence, switched on by an admin | On top of the licence: billed per task in Copilot Credits at $0.01 each |

Prices are US prices from each company's own pricing or announcement page, checked October 27 and 28, 2026. xAI renamed its plans in October, so the names may differ from what you've seen elsewhere.

## What each one does for a business

### ChatGPT dots

OpenAI describes dots as always-on agents with their own cloud computer and browser that can connect to more than 4,000 apps through plugins, and that you can message or call from ChatGPT, Slack or Teams. A dot learns your preferences over time and does what OpenAI calls proactive research in the background, using read-only tools that can't send messages or change content. It starts with built-in rules for when to act and when to ask, you can add your own with Custom Rules, and an auto-review step checks actions that could affect your accounts. OpenAI's own example is an early tester whose dot noticed an unsent invoice, prepared it and sent it after approval ([OpenAI, September 2026](https://openai.com/index/introducing-dots/)).

Your first dot is included in a ChatGPT Pro or Business Premium plan, and conversations with it don't count against your usage limits. Business Premium seats cost $125 per user a month, or $100 billed annually, with five times the usage of a standard $25 seat ([OpenAI, August 2026](https://openai.com/index/premium-seats-chatgpt-business/)). If you're on Plus, you have "agent mode" for one-off browsing tasks, but not a dot. OpenAI's own warning applies: dots can still make mistakes, so review consequential work.

### Claude Duet

Claude Duet is a separate app in which Claude works as a proactive agent: a morning brief, your inbox, calendar and follow-ups, larger jobs like building a dashboard, and a message when it needs a decision. It runs on its own cloud computer, uses the apps you've connected (Anthropic lists more than 6,000 connectors and plugins, including Gmail, Google Calendar, Slack and Stripe), and asks for approval before sensitive actions such as sending messages or making payments. Logins and approvals happen on the cloud computer, so the model doesn't see your credentials ([Anthropic](https://claude.com/product/claude-duet)).

It's a research preview by waitlist for Claude Pro and Max subscribers in the US, on iOS, Android and claude.ai, powered by Opus 5.5, and its usage comes out of your existing plan. Team and Enterprise plans aren't included yet. Anthropic's own caveats are that it may misread a thread or misjudge what's urgent. For a business outside the US, it's a watch item, not an option.

### Tasks in Gemini

Google's agent started as Spark in May 2026 and is now Task, behind a Chat/Task toggle in the Gemini app. It handles email, calendar, Docs and Drive, can run up to 15 tasks at once on a schedule, and since July can browse in Chrome in the US. It requires a Google AI Pro or Ultra plan, a personal Google Account, Keep Activity switched on and an opt-in to Personal Intelligence, and it isn't available in the EEA, Nigeria, Switzerland or the UK ([Google Help](https://support.google.com/gemini/answer/17094507?hl=en)). It asks before sending, changing or deleting data, buying, paying or submitting forms, and hands passwords and payment details back to you.

The personal-account rule is the catch for a business on Google Workspace. I went through the conditions, the data terms and a 7-day test in my [guide to Tasks in Gemini](https://freistyle.ai/blog/gemini-spark-for-small-business), and the separate business hub Google added in October in [Gemini's new business hub](https://freistyle.ai/blog/gemini-business-hub-small-business).

### Meta Muse and Muse for Small Business

Muse is Meta's personal agent, launched in the US on September 8, 2026 for iOS, Android, muse.ai and WhatsApp. It runs on what Meta calls a Muse Secure VM, a dedicated cloud computer with its own browser, next to a separate Sentinel agent that has to approve anything Muse sends to the internet. Muse checks with you before sensitive actions such as sending an email or making a purchase, keeps an audit trail, and can't see your passwords or payment methods. You can opt out of your interactions being used to train Meta's models ([Meta, September 8, 2026](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)).

Three weeks later Meta launched Muse for Small Business: you give it a goal such as finding new customers, and it works toward it using your Facebook and Instagram business accounts, your Meta ad account and connectors for Shopify, QuickBooks, Stripe, Canva, Klaviyo, Notion, Slack, Zoom and others. Meta's examples are a growth plan built from sales and campaign data, a sorted inbox, a drafted campaign from ad performance, and a monthly check of the books for unusual expenses. It doesn't publish, send or spend anything without your approval, and Meta says it's free for most needs, with subscription plans for heavier use ([Meta, September 29, 2026](https://about.fb.com/news/2026/09/introducing-muse-small-business/)). Meta's help page lists the paid plans as Power at $20 and Maximum at $100 a month ([Meta Help Center](https://www.meta.com/help/subscriptions/1021145227643680/)). If your customers find you on Instagram and message you on WhatsApp, this is the agent built for you, once it reaches your country.

### Grok Bot

Grok Bot, from xAI, is the most "coworker" of the six. You create Bots with defined jobs, each on its own cloud computer, and they sign into your tools and operate websites and apps through their interfaces, including ones with no official connection. Show a Bot a workflow once and it saves it as a routine; several Bots can share a thread, pass work to each other and escalate decisions to you. xAI's own examples are sales outreach, CRM updates from call notes, processing invoices from email and reproducing bugs ([xAI, August 2026](https://x.ai/news/introducing-grok-bot)). Desktop apps exist for macOS, Windows and Linux, plus iOS ([xAI](https://x.ai/bot)).

On xAI's pricing page, Grok Bot is included from the Premium plan at $30 a month, with Super ($100) and Ultra ($200) adding usage and Teams from $30 per user with centralised billing and single sign-on ([xAI](https://x.ai/pricing)). Two cautions. The Bot page makes no statement about how your data is handled, which is unusual among the six, and a Bot that signs into websites with your credentials is the most powerful and the least constrained setup here. I'd keep it away from anything with customer data until xAI publishes the data terms.

### Microsoft Copilot Cowork, and Autopilot

Cowork is Microsoft's agent for multi-step work inside Microsoft 365: you describe the job, it runs in the cloud across your files, mail and connected apps, and it returns a finished result. It became generally available worldwide on June 16, 2026, runs on Anthropic's models at launch, and sits inside the Microsoft 365 trust boundary with audit logs, sensitivity labels and eDiscovery. It's off by default, an admin switches it on, and it's billed per task in Copilot Credits at $0.01 per credit on top of a Microsoft 365 Copilot licence, with spending limits per tenant, group and user ([Microsoft, June 2026](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)).

Microsoft's always-on personal agent, introduced as Scout on June 2, 2026 and renamed Autopilot in September, schedules meetings, flags stalled decisions and blocks time for deliverables across Teams and Outlook. It's in private preview for Frontier organisations and built on the open-source OpenClaw project ([Microsoft, June 2026](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)). For a small business on Microsoft 365, Cowork is the one you can use now, and its billing needs a spending limit before anyone presses go.

## Who can actually use them today?

Fewer businesses than the launch posts suggest. This is the table I'd check before reading anything else.

| Agent | Region | Account type | Plan |
| --- | --- | --- | --- |
| dots | "Eligible markets", not listed by OpenAI | Personal Pro, or a Business or Enterprise workspace | Pro, Business Premium, Enterprise beta |
| Claude Duet | US, waitlist | Personal Claude account | Pro or Max |
| Tasks in Gemini | Not in the EEA, Switzerland, the UK or Nigeria | Personal Google Account only, no Workspace accounts | AI Pro or Ultra |
| Muse | US | Personal; small-business version connects business accounts | Free or paid |
| Grok Bot | Not stated by xAI | Personal, or Teams | Premium and up |
| Copilot Cowork | Worldwide | Microsoft 365 business tenant | Microsoft 365 Copilot licence, admin-enabled |

A Swiss or EU business is left with Copilot Cowork, Grok Bot and, in eligible markets, dots. That's not an accident: the agents that read your email and act on your behalf are the ones the EU rules on AI transparency and data protection touch most, and three of the six vendors have chosen to wait.

## What happens to your data?

This is where the six differ most, and where a business should spend its reading time.

| Agent | Training on your data | Approval before acting | Where your passwords live |
| --- | --- | --- | --- |
| dots | Business, Enterprise and Edu workspaces not used for training by default; on personal plans you control it in settings; no direct training on proactive research | Built-in rules plus Custom Rules and auto-review; password changes always stay with you | Saved passwords used for sign-in without exposing them to the model |
| Claude Duet | Not stated on the Duet page; consumer Claude plans ask you to choose whether chats train the model | Asks before sensitive actions such as sending or paying | Logins happen on the cloud computer, not in the model |
| Tasks in Gemini | Keep Activity required: Google uses activity to improve services including training, with some human review, reviewed chats kept up to 3 years | Confirmation for sending, deleting, buying, paying, forms and Sign in with Google | You enter sign-in and payment details in the browser yourself |
| Muse | You can opt out of training; Meta says Muse data isn't shared with its ad systems | Sentinel approves internet access; Muse asks before sending or buying | Stored on the Secure VM; Muse can't see them |
| Grok Bot | Not stated on the Bot page or the announcement | "Asks for approval when needed" | Bots sign into your tools; no detail published |
| Copilot Cowork | Governed by Microsoft 365 controls: audit, retention, sensitivity labels, eDiscovery | Not described in the GA post; admin spending limits and off by default | Inside your Microsoft 365 tenant |

Sources: the vendor pages linked in the sections above. "Not stated" means I couldn't find it on the vendor's own pages on October 28, 2026, not that the vendor does something bad with your data.

My read, after 15 years in corporate security: the two that spell out the most are Microsoft (because enterprise customers demand it) and OpenAI's dots page, with Meta close behind thanks to the Sentinel design. Google is clear too, but what it's clear about is that Keep Activity means training and human review. xAI has published the least. For a business, that order is also the order I'd trust with customer data, and the never list applies to all six: customer personal and payment details, passwords, contracts and anything a client gave you in confidence stay out.

## How to set up an AI agent, in plain English

The product names differ; the setup doesn't. Six steps, about an hour, for any of the six:

1. Pick the account, not the agent. Use a business plan or workspace where one exists (ChatGPT Business, Microsoft 365, a Claude Team plan once Duet supports it), because those are the plans that don't train on your data by default. Where only a personal account works, as with Tasks in Gemini, use one that isn't tied to your private life.
2. Connect one app, read-only if the agent allows it. Email is the usual first app. Meta lets you grant reading only, or reading and sending; OpenAI's proactive research is read-only by design. Don't connect your accounting software or your ad account on day one.
3. Set the rules before the first task. Every agent has a settings page for what it may do alone. Write the same three rules you'd write for a new assistant: draft but don't send, never pay, never delete. OpenAI calls these Custom Rules; Meta's Sentinel and Google's confirmations do part of it for you.
4. Give it one job with a clear finish line. "Every morning, summarise new customer emails and draft replies for me to send" is a job. "Help with my business" is a wish.
5. Check the log every day for a week. All six keep a record of what the agent did (OpenAI's Activity View, Meta's audit trail, Microsoft's audit log, Google's task thread). Read it. Count the drafts you rewrote, the things it got wrong and anything it did that you didn't ask for.
6. Widen one step at a time, or stop. If the week was clean, add the calendar. If it sent, changed or spent anything without you, disconnect it the same day and go back to drafts only.

Quick Win

Before you connect anything, open your sent folder and count this week's routine emails: confirmations, scheduling, "thanks, got it". Under half an hour a day, you don't need an agent yet, and a good prompt will do. Over that, a drafts-only trial on the agent that matches your account is worth a week.

## What should an agent never do without your approval?

Send, publish, pay, sign, delete, and change anything a customer sees. All six vendors say their agents stop for most of these, so the setting to check is that nobody has switched the stops off. Reading, sorting, summarising and drafting are safe to hand over on day one. Sending and booking come after a clean week on drafts, one change at a time. Payments, signatures, bank details and customer data under NDA stay with a person, and every vendor hands the payment step back to you anyway. Section 5 of the [one-page AI policy template](https://freistyle.ai/blog/ai-policy-template-small-business) turns that into a rule your team can sign.

## Which agent should a small business try first?

The one that already has your data, because connecting it is the whole job.

| If your business lives in... | Try first | Because |
| --- | --- | --- |
| Gmail, Calendar and Docs on a personal account, outside the EU and the UK | Tasks in Gemini | It's already inside your apps, and Google's confirmation rules are the clearest |
| Google Workspace (a work account) | Wait, or Copilot Cowork if you also run Microsoft 365 | Tasks don't support work accounts yet |
| Microsoft 365 with a Copilot licence | Copilot Cowork, with a spending limit set | Inside your tenant's existing controls |
| ChatGPT Business or Pro | dots | First dot included; workspace content isn't used for training by default |
| Instagram, Facebook, WhatsApp and a Shopify or Stripe shop, in the US | Muse for Small Business | Built around those connectors, approval before any send or spend |
| Claude Pro or Max, in the US | Join the Duet waitlist | A research preview; not for the EU yet |
| A sales team that lives in a CRM and wants autonomy | Grok Bot, after the data terms are published | The most capable, the least documented |

If none of the rows fits, you don't need an agent yet. A clear prompt in the assistant you already pay for will cover most routine replies, and my [five prompts for entrepreneurs](https://freistyle.ai/blog/ai-prompts-for-entrepreneurs) are the place to start.

The wider list of tools with vendor-checked prices is in [the best AI tools for small business in 2026](https://freistyle.ai/blog/best-ai-tools-small-business-2026).

## Frequently asked questions

### What is the difference between an AI agent and a chatbot?

A chatbot answers one question at a time. An agent runs on its own cloud computer, connects to your apps, works toward a goal while you're away and asks you before sensitive actions. ChatGPT dots, Claude Duet, Tasks in Gemini, Muse, Grok Bot and Copilot Cowork are all agents in that sense.

### Which AI agent is best for a small business?

The one that already has your data. Tasks in Gemini for a Gmail business outside the EU and UK, Muse for Small Business for an Instagram and WhatsApp business in the US, Copilot Cowork for Microsoft 365, dots for ChatGPT Pro or Business Premium. Claude Duet is a US waitlist and Grok Bot hasn't published its data terms.

### Can I use ChatGPT dots on the Plus plan?

Not as of October 2026. Dots are rolling out to Pro, Business Premium and admin-enabled Enterprise workspaces in eligible markets. Plus includes "agent mode" for one-off browsing tasks. Your first dot is included in Pro and Business Premium at no extra cost.

### Is Claude Duet available in Europe?

No. Anthropic opened a research preview on October 21, 2026 by waitlist for Claude Pro and Max subscribers in the US, on iOS, Android and claude.ai. Team and Enterprise plans aren't included yet.

### Do AI agents use my business data for training?

It depends on the vendor and the plan. OpenAI doesn't use Business, Enterprise or Edu workspace content for training by default. Microsoft Cowork stays inside your Microsoft 365 controls. Meta lets you opt out. Google's Tasks require Keep Activity, which allows training and some human review. xAI's Grok Bot pages don't say.

### How much do AI agents cost?

From nothing to a few hundred dollars a month. Muse is free for most uses. Tasks in Gemini comes with Google AI Pro at $19.99. Grok Bot starts with xAI's $30 Premium plan. Claude Duet uses a $20 Pro or $100-plus Max plan. Dots need ChatGPT Pro from $100 or a $125 Business Premium seat. Copilot Cowork bills per task at $0.01 per credit on top of a Copilot licence.

### What should an AI agent never do without approval?

Send, publish, pay, sign, delete, or change anything a customer sees. Every vendor says its agent stops for most of these. Keep those stops switched on, start with drafts only, and check the agent's activity log daily for the first week.

## Where to go from here

Find your row in the "try first" table, set up that one agent on a business account with one read-only app, and run it on drafts for a week before it sends anything. If the week is clean, widen one step. If you want the rules written down for your team first, the policy template above takes about an hour.

Disclosure: Freistyle AI is part of Anthropic's startup program, which gives the business free Claude credits. Prices and features above come from each company's own pages.

*Researched with AI tools, written and fact-checked by [Dominic](https://freistyle.ai/about).*

### Sources

1. [OpenAI, Introducing dots (Sep 29, 2026)](https://openai.com/index/introducing-dots/)
2. [OpenAI, Premium seats for ChatGPT Business (Aug 10, 2026, updated Aug 25, 2026)](https://openai.com/index/premium-seats-chatgpt-business/)
3. [OpenAI, ChatGPT pricing](https://chatgpt.com/pricing/)
4. [Anthropic, Claude Duet | Your personal AI assistant (accessed Oct 28, 2026)](https://claude.com/product/claude-duet)
5. [Anthropic, Claude pricing](https://claude.com/pricing)
6. [Google Gemini Apps Help, Manage your tasks & workflows in Gemini Apps (accessed Oct 28, 2026)](https://support.google.com/gemini/answer/17094507?hl=en)
7. [Google, Google AI plans and pricing](https://gemini.google/subscriptions/)
8. [Meta, Introducing Muse, a personal AI agent (Sep 8, 2026)](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
9. [Meta, The Future Is for Everyone: Muse for Small Business (Sep 29, 2026)](https://about.fb.com/news/2026/09/introducing-muse-small-business/)
10. [Meta Help Center, About Muse subscriptions (accessed Oct 28, 2026)](https://www.meta.com/help/subscriptions/1021145227643680/)
11. [xAI, Introducing Grok Bot (Aug 11, 2026)](https://x.ai/news/introducing-grok-bot)
12. [xAI, AI teammates that finish the work | Grok Bot (accessed Oct 28, 2026)](https://x.ai/bot)
13. [xAI, Pricing (accessed Oct 28, 2026)](https://x.ai/pricing)
14. [Microsoft, Copilot Cowork is now generally available (Jun 16, 2026)](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)
15. [Microsoft, Introducing Microsoft Scout: Your always-on personal agent (Jun 2, 2026; renamed Autopilot Sep 25, 2026)](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)
16. [OWASP GenAI Security Project, LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
