来源：https://resources.rework.com/tools/ai-agents/best-personal-ai-agents-2026
取文：2026-11-28，直接下载

OpenClaw and Hermes Agent are the best personal AI agents if you want to own the setup, keep your data on your own machine and pay only for the model, while OpenAI's dots, Claude Cowork and Google's Gemini Spark are the better fit if you'd rather rent a managed agent that sits inside a subscription you already have. Poke and Lindy cover the "just text it" end of the market, and Perplexity's Personal Computer and Manus sit in between with a desktop app plus a cloud brain. We compared nine on the four things that decide whether a personal agent is a good idea: where it runs, how you talk to it, what it remembers, and what happens when someone else tries to talk to it.

A personal agent is a different animal from the tools in our [best autonomous AI agents](https://resources.rework.com/tools/ai-agents/best-autonomous-ai-agents-2026) or [best AI browser agents](https://resources.rework.com/tools/ai-agents/best-ai-browser-agents-2026) roundups. Those are built for a team to run a defined job. A personal agent works for one person: it reads your inbox, touches your files, sits in your messaging apps and keeps working while you sleep. That's why the buying questions are mostly about trust. The agent holds your credentials and your context, so a mistake or a hijacked instruction lands on you personally. For the basic definition, see [what is an AI agent](https://resources.rework.com/libraries/ai-agents/what-is-an-ai-agent). This category also moves fast, with renames, ownership changes and sunsets happening within months, so the product notes below name the owner and the plans each vendor currently lists.

## Key Facts

- Prompt injection, where text the agent reads quietly changes what it does, is ranked LLM01 in the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), the first-listed risk. An agent that reads your email and your messages is exposed to it by design.
- OpenClaw's own security guidance assumes [one trust boundary per gateway](https://docs.openclaw.ai/gateway/security): a single operator, or a team that trusts each other. It says plainly that it isn't built as a hostile multi-tenant boundary.
- Hermes Agent's gateway is fail-closed: per its [security guide](https://hermes-agent.nousresearch.com/docs/user-guide/security), if no allowlist is configured and the allow-all flag isn't set, all messaging users are denied.
- OpenAI's [dots documentation](https://learn.chatgpt.com/docs/dots) says a dot can connect to one personal computer at a time, and that the computer must be online with the ChatGPT app open.
- Perplexity's [Personal Computer help article](https://www.perplexity.ai/help-center/en/articles/14659663-what-is-personal-computer) says that on Mac, cloud models still handle planning, search and reasoning, while a local model processes private files and sensitive steps.

## Quick Comparison Table

| Tool | Best For | Starting Price | Key Strength | Key Limitation |
| --- | --- | --- | --- | --- |
| **OpenClaw** | Tinkerers and teams who want full ownership | Free, MIT licensed; you pay your model provider | Runs on your machine, many chat channels, persistent memory | You own the security hardening |
| **Hermes Agent** | Self-hosters who want a learning agent | Free, MIT licensed; Nous Portal optional | Auto-generated skills, sandbox backends, built-in cron | Terminal-first setup, you operate it |
| **ChatGPT dots** | ChatGPT Pro users who want a managed always-on agent | Included with Pro (Pro 100, 200 and 500 tiers) | Own cloud computer, reachable in ChatGPT, Slack and Teams | Pro only; not offered in the EEA, UK or Switzerland |
| **Claude Cowork** | Knowledge workers who want an agent on their files | Included with Claude Pro, $17/mo billed annually or $20 monthly | Scheduled tasks, phone dispatch, folder-scoped access | Desktop app needed for local files; usage limits |
| **Gemini Spark** | Google Workspace users | Included in eligible Google AI plans; AI Pro $19.99/mo | 24/7 on Google Cloud, asks before spending or sending | Select countries, eligibility changes |
| **Perplexity Personal Computer** | Mac mini or desktop owners wanting a hybrid local/cloud agent | Pro $17/mo billed annually; Max $167/mo billed annually | Local model for private files, runs 24/7 on a Mac mini | Credits meter the cloud work |
| **Manus** | Research and build tasks plus a desktop agent | Free tier; paid tiers with 8,000 or 40,000 credits | Wide Research, My Computer desktop bridge | Credit-based billing; ownership changed in 2026 |
| **Poke** | People who want to text an assistant | Free; Pro $19/mo | Lives in Messages, WhatsApp or Telegram | Self-hosting; read the privacy policy first |
| **Lindy** | Founders and small teams | Free credits; Team from $29.99/mo | iMessage access, inbox and calendar workflows | Positioned as a work teammate more than a personal agent |

## How to Choose a Personal AI Agent in 2026

Most reviews of this category rank the demos. A personal agent is worth judging on four properties that don't show up in a demo.

### 1. Where does it actually run?

There are three models. A **local** agent like OpenClaw or Hermes runs on your own machine or server, and its state lives there. A **managed cloud** agent like dots or Gemini Spark runs on the vendor's computers and keeps working when your laptop is closed. A **hybrid** agent like Cowork, Perplexity's Personal Computer or Manus pairs a cloud brain with a desktop app that reaches your files. Local gives you control and a bigger blast radius if you misconfigure it. Cloud gives you uptime and a smaller footprint on your own device. Hybrid means your phone can start a job, but the desktop has to be on for the parts that touch local files.

| Model | Examples | Works when your laptop is closed | Who patches it |
| --- | --- | --- | --- |
| Local, self-hosted | OpenClaw, Hermes Agent | Only if you host it on an always-on machine | You |
| Managed cloud | ChatGPT dots, Gemini Spark | Yes | The vendor |
| Hybrid | Claude Cowork, Perplexity Personal Computer, Manus | Cloud tasks yes; local-file tasks need the desktop | Shared |
| Text-first assistant | Poke, Lindy | Yes | The vendor |

### 2. Who can talk to it?

A personal agent that listens in a chat app has a new attack surface: anyone who can message it. OpenClaw's defaults answer this with a pairing code for unknown direct-message senders and allowlisted groups. Hermes denies everyone unless you configure an allowlist. The managed products narrow it differently. OpenAI says a dot can only text you, and you're the only one who can text your dot. Whatever you pick, find the setting that decides who the agent will take instructions from, and set it before you connect a single account. Our [AI agent security](https://resources.rework.com/libraries/ai-agents/ai-agent-security) guide covers the threat model, and [AI agent guardrails](https://resources.rework.com/libraries/ai-agents/ai-agent-guardrails) covers hard limits that should hold regardless of what the agent is told.

### 3. What does it remember, and where is that stored?

Memory is the feature that makes a personal agent feel personal, and it's also a data store about you. OpenClaw keeps persistent memory of your preferences, projects and people. Hermes saves conversations, memories and skills between sessions and tells you to back up its data directory if you move machines. Dots combine conversations, ChatGPT memory and their own saved notes. Ask where the memory lives, whether you can read and delete it, and whether it follows you into a group chat. OpenAI's documentation says a dot checks that you've allowed it before sharing information from a private conversation with others.

### 4. What does the bill look like?

Open-source agents are free to download and not free to run. You pay a model provider per token, or a hosting bill, or both, and heavy use of an always-on agent can cost more than a flat subscription. Subscription agents hide the token cost but ration you with credits and usage limits. Model your real daily use before you decide that free or flat-rate is cheaper.

### Sizing and Persona Table

| Tool | Best Fit | Primary Buyer |
| --- | --- | --- |
| OpenClaw | Individuals and small trusted teams comfortable with a terminal | Technical founder, developer, IT lead |
| Hermes Agent | Self-hosters who want an agent that builds its own skills | Developer, researcher |
| ChatGPT dots | Heavy ChatGPT users on a Pro plan | Executive, consultant, power user |
| Claude Cowork | People who live in documents, spreadsheets and research | Analyst, chief of staff, operations manager |
| Gemini Spark | Google Workspace users | Manager, founder, student on Google AI plans |
| Perplexity Personal Computer | Mac and Windows users who want local inference for private files | Researcher, consultant |
| Manus | Research-heavy and build-heavy individual work | Marketer, founder, analyst |
| Poke | Individuals who want a text-message interface | Busy professional |
| Lindy | Small teams who want one assistant across email, calendar and Slack | Founder, sales lead |

## 1. OpenClaw: The Open-Source Default for People Who Want to Own the Agent

OpenClaw is the project most people now mean when they say "personal AI agent." It's an open-source assistant that you run on your own Mac, Windows or Linux machine, and it acts through the messaging apps you already use. Its site lists WhatsApp, Telegram, Discord, Slack, Signal and iMessage among 29 channels, and describes jobs like organizing an inbox, sending email and managing a calendar. State lives on your machine rather than in a vendor cloud, and memory persists across conversations.

Ownership matters here because the project has changed shape. It's maintained by the OpenClaw Foundation, an independent U.S. nonprofit. The site says OpenAI is a donor and that OpenClaw is not an OpenAI product, and that the whole product stays MIT licensed with no enterprise edition and no paid version. You bring your own model, hosted, subscription-backed or local, with Claude and GPT as the listed examples.

The security posture deserves the longest read. OpenClaw's [security guide](https://docs.openclaw.ai/gateway/security) describes conservative defaults: on a standard install the gateway binds to loopback, unknown direct-message senders get a pairing code, and group access is allowlisted. It also tells you that credentials, transcripts and logs are stored on disk, that agents with message-tool access can send across conversations by default, and that an `openclaw security audit` command checks whether you've drifted from safe settings. It's a tool for someone who will actually read that guide.

| What you get | What you don't |
| --- | --- |
| Free, MIT licensed, state on your own machine | A support line; the community and docs are what you have |
| Wide channel coverage and persistent memory | A managed, patched service; hardening is your job |
| Any model you choose, including local ones | A predictable bill; model spend depends on your usage |

**Pricing:** Free. The project states there is no subscription, hosted tier or token. Model access is billed by whichever provider you connect, and hosting costs apply if you run it on a server. Source: [openclaw.ai](https://openclaw.ai).

**Best for:** Technical users and small trusted teams who want a personal agent they fully control.

**Not ideal for:** Anyone who wants a managed service, or who would connect it to work accounts without reading the security guide first.

---

## 2. Hermes Agent: The Self-Hosted Agent That Writes Its Own Skills

Hermes Agent comes from Nous Research and shares OpenClaw's basic bargain: free, MIT licensed, runs where you put it, talks to you through messaging apps. Its site lists Telegram, Discord, Slack, WhatsApp, Signal, email and the command line, and its docs describe one gateway reaching 20 or more platforms, including Microsoft Teams. You can install it locally on macOS, Linux or Windows, use a desktop app on macOS or Windows, or optionally deploy on Nous Portal.

Its pitch is a learning loop. Hermes keeps memory across sessions and generates reusable skills from what it learns, which the docs describe as procedural memory compatible with the open agentskills.io standard. Cron scheduling is built in, with delivery to any connected platform.

The security design is more explicit than most. Risky commands trigger an approval prompt, and if you don't answer in time the command is denied. A hardline blocklist refuses catastrophic commands even in YOLO mode. The Docker, Modal, Daytona and Vercel Sandbox backends use the container as the boundary. The guide is honest about limits, noting that its file-write denylist guards against accidents and does not sandbox a hostile or compromised agent. For a gateway deployment it recommends a container or remote backend, explicit allowlists and a non-root user.

| What you get | What you don't |
| --- | --- |
| Free and MIT licensed, with six built-in execution backends | A hosted product unless you choose Nous Portal |
| Approval gating, fail-closed allowlists and container isolation | Protection from a compromised agent on a local backend |
| Skills and memory that accumulate over time | A polished consumer onboarding flow |

**Pricing:** The agent is free. Model providers and hosted services have their own pricing. If you use Nous Portal, its plans are Free ($0, free models only), Plus ($20/month), Super ($100/month) and Ultra ($200/month), and the paid tiers include monthly credits. Source: [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com).

**Best for:** Developers and researchers who want a self-hosted agent with a real approval model and built-in scheduling.

**Not ideal for:** Non-technical users, or anyone who wants a vendor to carry the operational burden.

---

## 3. ChatGPT Dots: OpenAI's Managed Always-On Agent

OpenAI's answer to the always-on category is the dot. OpenAI describes it as an agent that keeps work moving across your tools and projects and asks for your input when a decision needs you. Each dot has its own cloud computer and browser, so work continues while your devices are off. You can reach the same dot in ChatGPT, Slack, Teams or by phone call, and changing channels doesn't reset its memory. Texting is in beta for ChatGPT Pro users in the U.S.

Control is the interesting part. According to the [dots documentation](https://learn.chatgpt.com/docs/dots), built-in safeguards, your existing ChatGPT app permissions and automatic approval checks apply from the start, and your own instructions can add boundaries but don't override the built-in safety requirements. When a site needs a login, you enter credentials in a private form that sends them to the browser instead of the conversation, and the cloud browser keeps its sessions separate from your computer's browser. Connecting a messaging channel doesn't grant access to your apps or computer. The page also says, without hedging, that a dot can make mistakes, and that stopping a task doesn't reverse actions it already took.

Availability is the catch. Dots are listed for ChatGPT Pro, not Plus: the ChatGPT pricing page shows scheduled tasks on Go, Plus and Pro, and dots on Pro only. OpenAI's documentation names Pro 100, Pro 200 and Pro 500 as eligible plans for users over 18 outside the EEA, UK and Switzerland, with Business Premium and Enterprise rolling out separately.

| What you get | What you don't |
| --- | --- |
| Own cloud computer and browser; works with your devices off | Availability on Plus or Free plans |
| Reachable in ChatGPT, Slack, Teams and by phone | Texting outside the U.S. beta |
| Private-form sign-ins and approval checks | Reversal of actions already taken |

**Pricing:** Included with an eligible ChatGPT Pro plan, at no extra cost for the first dot. Pro 500 is listed at $500/month, and prices for the other Pro tiers vary by country. Sources: [learn.chatgpt.com/docs/dots](https://learn.chatgpt.com/docs/dots), [chatgpt.com/pricing](https://chatgpt.com/pricing/) and [DevDay 2026 notes](https://learn.chatgpt.com/docs/whats-new/devday-2026).

**Best for:** Heavy ChatGPT users on Pro who want a managed agent that keeps working without their laptop.

**Not ideal for:** Buyers in the EEA, UK or Switzerland, or anyone who wants to inspect and self-host the agent.

---

## 4. Claude Cowork: A Folder-Scoped Agent for Knowledge Work

Cowork is Anthropic's agent for non-coding knowledge work: research, analysis and document creation. You give it a goal, it works across the files and tools you choose, and it returns finished work for review. The desktop app is its main home and the only way to reach folders and applications on your own computer. Tasks can also start from your phone and continue in the cloud while your laptop is closed.

What earns it a place on a personal-agent list is scheduling and dispatch. Per Anthropic's [Cowork page](https://claude.com/product/cowork), you can schedule recurring tasks daily, weekly or monthly that run unattended, such as a weekly report, and dispatch tasks from a phone to check or redirect them from anywhere. For web work, Claude opens a separate browser in the side panel so your own browsing and logins stay untouched. Computer use, where it controls your screen, is a research preview, and Claude prefers connectors, then the browser, and uses the screen only as a last resort.

The permission model is built around folders. You choose which folders and tools Claude can reach, deleting anything requires your approval, and with permissions settings on, Claude shows its plan and waits for approval before significant actions. Cowork is less of a "message me on WhatsApp" agent and more of a capable colleague you hand work to.

| What you get | What you don't |
| --- | --- |
| Folder-scoped access and approval before deletions | A chat-app interface; you work in the Claude apps |
| Scheduled recurring tasks and phone dispatch | Local-file access without the desktop app |
| Included in a plan you may already pay for | Unlimited use; it consumes plan limits faster than chat |

**Pricing:** Anthropic lists Cowork on Pro, Max, Team and Enterprise. Pro is $17/month billed annually ($200 up front) or $20 billed monthly, Max is $100/month and Ultra is $200/month, and Team is $20 per standard seat per month billed annually ($25 billed monthly). Usage limits apply. Source: [claude.com/product/cowork](https://claude.com/product/cowork) and [claude.com/pricing](https://claude.com/pricing).

**Best for:** Analysts, chiefs of staff and operations people who want an agent to produce documents, reports and research from their own files.

**Not ideal for:** People who want to run their life from a chat app, or teams that need to self-host.

---

## 5. Gemini Spark: Google's 24/7 Agent for Workspace Users

Spark is Google's personal agent, and Google's own description is a 24/7 personal AI agent that works in the background and keeps running when your laptop is closed or your phone is locked. It runs on Google's cloud infrastructure, connects natively to Workspace tools including Gmail, Docs and Sheets, and accepts recurring instructions, such as checking something every Friday morning.

Control sits with you. Per Google's [Spark launch post for India](https://blog.google/intl/en-in/company-news/technology/introducing-gemini-spark-your-247-personal-ai-agent-in-country/), you decide whether to turn Spark on and which apps it can connect to, and it's designed to ask first before high-stakes actions such as spending money or sending emails. Its drafting examples save emails to drafts for your review instead of sending them, which is the right default for a personal agent.

The honest limits are availability and clarity. Google describes Spark as available to Google AI Pro and Ultra subscribers in select countries, and rollouts have varied by country, so check eligibility for yours. It's also tied to Google's ecosystem: if your work lives in Microsoft 365, this isn't your agent.

| What you get | What you don't |
| --- | --- |
| Runs in Google's cloud with no laptop required | Self-hosting or local control |
| Native Workspace connections you switch on yourself | The same experience outside Google's apps |
| Approval before spending money or sending email | Availability everywhere; it's country-limited |

**Pricing:** Included with eligible Google AI subscriptions. In the US, Google AI Pro is $19.99/month (or $199.99 billed annually) and Google AI Ultra starts at $99.99/month, billed monthly only. Confirm which plan carries Spark in your country. Source: [Google AI plans](https://one.google.com/intl/en_us/about/google-ai-plans/).

**Best for:** Google Workspace users who want a hands-off agent inside Gmail, Calendar and Drive.

**Not ideal for:** Microsoft-centric teams, or buyers who need an agent that runs on hardware they control.

---

## 6. Perplexity Personal Computer: A Hybrid Agent With a Local Model

Perplexity's Personal Computer is its desktop app for Mac and Windows, built around Computer, its web-based agent, with access to your local files and native apps. Its distinctive design choice is privacy-aware routing. Per the [help center article](https://www.perplexity.ai/help-center/en/articles/14659663-what-is-personal-computer), on Mac a privacy gate can mask sensitive details, keep a step local, refuse the action or ask for your consent before protected file information reaches the cloud, while a local model processes private files and sensitive steps. On Windows and Linux, the Portable Computer version asks permission before sending anything from your device to the cloud.

The always-on piece is hardware. Perplexity recommends a Mac mini because it can run Computer 24/7 in the background even when your laptop is closed, with tasks started, paused or adjusted from an iPhone. A Mac mini isn't required. Actions run in an isolated sandbox, with on-device authorization guarding sensitive steps and two-factor authentication on Mac mini sessions. Work handled by the local model doesn't consume Computer credits.

| What you get | What you don't |
| --- | --- |
| A local model for private files and sensitive steps | A fully local agent; the cloud still plans and reasons |
| 24/7 operation on a Mac mini you own | Chat-app channels like WhatsApp or Telegram |
| Isolated sandbox and consent prompts | Unlimited use; cloud work draws credits |

**Pricing:** Perplexity lists Pro at $17/month billed annually and Max at $167/month billed annually, with Max carrying maximum Computer usage and more monthly credits. Source: [perplexity.ai/hub/pricing](https://www.perplexity.ai/hub/pricing).

**Best for:** Researchers and consultants who handle sensitive files and want a local model in the loop.

**Not ideal for:** Anyone who wants to talk to their agent mainly from a messaging app. For research-focused tools, see our [best AI research agents](https://resources.rework.com/tools/ai-agents/best-ai-research-agents-2026) roundup.

---

## 7. Manus: Cloud Agent, Desktop Bridge and a Turbulent Ownership Year

Manus built its name on cloud-based agents for research, slides and websites, then moved toward personal use in 2026. Its blog lists "Manus in Your Chat," a personal agent reachable from messaging apps, in February 2026, and "My Computer," a desktop app, in March 2026. My Computer pairs the cloud agent with a native app for macOS and Windows. During setup you grant access to specific local folders, which creates the bridge between the cloud agent and your files. Tasks can start from the mobile app, but the desktop machine must be on and the Manus Desktop app running, and Manus suggests a dedicated machine such as a Mac mini for 24/7 access.

The ownership story is why it needs a caveat. Manus posted "Manus Joins Meta" on December 29, 2025, and then a post titled "Manus Resumes Independent Operations" on September 1, 2026, which says the founding team continues to lead the company. In that post, Manus says some users had to back up and restore their data and some temporarily lost access. If you're considering it as the home for your personal context, that's a data-continuity signal worth weighing. Read the [post](https://manus.im/blog/manus-resumes-independent-operations) before you connect anything sensitive.

| What you get | What you don't |
| --- | --- |
| Strong research and build tasks, plus a desktop bridge | A stable ownership history across 2026 |
| Mobile-started tasks that run on your desktop | Tasks that run if the desktop is off or the app is closed |
| A free tier to test on | Predictable cost; billing is credit-based |

**Pricing:** Manus lists a free tier and paid plans; the pricing page shows tiers at 8,000 and 40,000 credits per month alongside a lower tier, each with 20 concurrent and 20 scheduled tasks. Dollar amounts and billing terms should be confirmed on the vendor's page. Source: [manus.im/pricing](https://manus.im/pricing).

**Best for:** Individual researchers and marketers who want one agent for web work and a desktop bridge.

**Not ideal for:** Buyers who need a settled corporate owner and a long track record.

---

## 8. Poke: The Assistant You Text

Poke is the simplest tool here. It's made by Interaction, and its site describes a personal AI assistant you use by text, through Messages, WhatsApp or Telegram, by text or voice message. It connects to services like Gmail, Google Calendar, Notion, GitHub, Asana, Linear and Todoist, creates reminders, and can run automations, which it calls Recipes, and proactively help using its memory.

Poke has also announced that NewPoke is joining Cognition, so expect product and policy changes. Read its privacy policy before connecting sensitive accounts. That's the right instinct for any text-first assistant: the interface is a chat thread, and the data behind it is your email and calendar.

| What you get | What you don't |
| --- | --- |
| A chat-thread interface with no install | Certainty about data handling before you read the privacy policy |
| Broad app connections and reminders | A self-hosted option |
| A free tier with Gmail and calendar connections | Certainty about the product's direction after the Cognition move |

**Pricing:** Free ($0, connects to apps, email and calendar); Pro $19/month (frontier models, background automations, higher rate limits, priority support); Ultra $199/month (highest rate limits plus pay-as-you-go usage beyond credits). Yearly billing is also offered. Source: [poke.com](https://poke.com).

**Best for:** Busy individuals who want an assistant in their message thread and don't want to configure anything.

**Not ideal for:** Anyone with strict data-handling requirements.

---

## 9. Lindy: A Work Teammate With a Text Interface

Lindy sits at the edge of this category. Its pricing page lists "iMessage with your assistant 24/7" among included features, along with inbox management, calendar scheduling, meeting notes and daily briefs, but it also positions itself as a Slack-native teammate for business work. It's more a teammate for a founder or a small team than a personal agent in the OpenClaw sense. If you're comparing it to workflow tools, our [Lindy alternatives](https://resources.rework.com/tools/ai-agents/best-lindy-alternatives) page and the [Lindy vs Zapier Agents](https://resources.rework.com/tools/ai-agents/lindy-vs-zapier-agents) comparison go deeper, and our [best no-code AI agent builders](https://resources.rework.com/tools/ai-agents/best-no-code-ai-agent-builders-2026) roundup covers the build-it-yourself side.

Credits meter everything. Everyday asks use 2 to 250 credits, deep work 250 to 1,000, and big builds 1,000 to 2,500, and if credits run out Lindy pauses credit-using actions rather than billing overage.

| What you get | What you don't |
| --- | --- |
| iMessage access plus inbox, calendar and meeting workflows | Unlimited usage; credits meter every task |
| Pause-instead-of-overage when credits run out | Overage billing past your credit allowance |
| Team features and enterprise controls | A consumer-first, personal-agent design |

**Pricing:** Free ($0, with $50 in credits that last 7 days, no card required); Team from $29.99/month for 3,000 credits, with larger tiers up to 1,750,000 credits for $9,999.50 and extra credits at $10 per 1,000; Enterprise custom. Monthly credits reset each cycle and don't roll over. Source: [lindy.ai/pricing](https://www.lindy.ai/pricing).

**Best for:** Founders and small teams who want an assistant in iMessage and Slack for email and scheduling.

**Not ideal for:** People who want a self-hosted or purely personal agent.

---

## Personal AI Agent Buying Mistakes to Avoid

| Mistake | What It Looks Like | What to Do Instead |
| --- | --- | --- |
| Connecting everything on day one | Gmail, calendar, files, bank logins and Slack all linked in an afternoon | Start with one low-stakes app and widen access as the agent earns trust |
| Leaving the sender policy open | A chat-app agent that obeys anyone who can message it | Use pairing codes or allowlists before connecting accounts |
| Treating "runs locally" as "safe" | A local agent with broad file access and no sandbox | Use a container backend and a scoped working directory |
| Ignoring prompt injection | An agent that summarizes a hostile email and then acts on it | Require approval for sends, payments and deletions |
| Buying on a demo | Choosing the agent that looked best on a short task | Pilot a real week of your own work |
| Underestimating the model bill | Assuming free software means a free agent | Track token spend for a week before committing |
| Skipping the ownership check | Building habits on a product that may be acquired, renamed or shut down | Read the vendor's latest ownership and data-continuity notes |

## How to Choose: Decision Framework

Pick where the agent runs first, then pick who it works for.

| If you need... | Pick... | Why |
| --- | --- | --- |
| Full control and your data on your own machine | **OpenClaw** | MIT licensed, local state, any model |
| An open-source agent with a stricter approval model | **Hermes Agent** | Command approval, fail-closed allowlists, container backends |
| A managed agent that works with your laptop closed | **ChatGPT dots** or **Gemini Spark** | Own cloud computer or Google Cloud, approval before risky actions |
| An agent that works on your documents and files | **Claude Cowork** | Folder-scoped access, scheduled tasks, phone dispatch |
| A local model in the loop for private files | **Perplexity Personal Computer** | Privacy gate and local inference |
| An assistant you simply text | **Poke** or **Lindy** | Lives in your message thread |
| Heavy research and build tasks | **Manus** | Wide Research, desktop bridge |
| A team-run agent instead of a personal one | See [best autonomous AI agents](https://resources.rework.com/tools/ai-agents/best-autonomous-ai-agents-2026) | Built for defined, shared jobs |
| A no-cost starting point | See [best free AI agents](https://resources.rework.com/tools/ai-agents/best-free-ai-agents-2026) | Free and open-source options |

If your agent will handle purchases, read our [best AI agent security tools](https://resources.rework.com/tools/ai-agents/best-ai-agent-security-tools-2026) and [best agentic commerce platforms](https://resources.rework.com/tools/ai-agents/best-agentic-commerce-platforms-2026) roundups before you give it a payment method.

## What to Do Next

Pick one agent from the section that matches your hosting preference and run a one-week pilot on a single low-stakes workflow, such as a morning briefing or inbox triage. Connect one account, set the sender policy first, and keep approval on for anything that sends, spends or deletes. At the end of the week, read the agent's logs and your bill, and decide whether to widen access or switch tools.
