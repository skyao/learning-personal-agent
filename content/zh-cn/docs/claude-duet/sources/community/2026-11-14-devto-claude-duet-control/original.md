来源：https://dev.to/suraj_khaitan_f893c243958/claude-duet-messages-you-first-that-changes-who-is-in-control-3n74
取文：2026-11-28，直接下载

[#ai](/t/ai)
[#claude](/t/claude)
[#chatgpt](/t/chatgpt)

*On October 21, 2026, Anthropic opened a research preview of Claude Duet, an app where Claude works as a proactive agent: it watches your connected accounts, prepares work while you are away, and messages you when something needs you. The interesting part is not that Claude can now start the conversation. It is how Anthropic moved the most important controls outside the model, and what still depends on a human tapping "approve." Here is how Duet works, what its safety design gets right, where the real risks are, and how I would use it today.*

*Research and product status checked November 14, 2026.*

---

## Twelve Approvals Before Lunch

Imagine it is Monday, 7:40 a.m.

Before you open your laptop, a message is waiting on your phone. Claude has already read your inbox and calendar. Three things need you today: a contract is waiting for signature, a client invoice is overdue, and four emails have draft replies ready to send.

You approve the drafts on the train.

By lunch, Claude has asked for approval twelve times. Send this follow-up. Pay this software renewal with a one-time card. Share the Q3 summary with the finance contact who asked for it. Each request shows exactly what will happen, where it will go, and who will receive it.

By the eighth request, you are no longer reading. You are tapping.

The finance contact who asked for the Q3 summary wrote from a domain that differs from your client's by one letter. The approval card showed the full recipient address, exactly as designed. You just did not look.

This is a hypothetical scenario, not a reported Duet incident. It is also not a story about a careless model. Every safeguard did its job. The agent prepared the work, an independent check judged that sharing a report requested by email matched your intent, and the approval card displayed the destination.

The control that failed was attention.

Anthropic is unusually direct about this risk. In describing Duet's safeguards, the company acknowledged that "approval fatigue is a serious issue, because too many requests teach people to tap through them."

That sentence is the right place to start, because it identifies what really changes when an AI agent messages you first.

A chat assistant waits. You decide when to ask, what to share, and what to do with the answer.

A proactive agent decides when something needs you. It reads content you did not choose to show it, prepares actions you did not explicitly request, and asks for decisions on its schedule, not yours.

> **When an AI agent starts the conversation, consent moves from approving each request to granting standing authority. Claude Duet puts its most important controls outside the model, which is the right architecture. But the final control is still a human approval, and human attention is the scarcest resource in the system.**

---

## TL;DR

- **Claude Duet is a proactive agent app, not a new model.** It runs on Claude Opus 5.5 in a standalone app on iOS, Android, and claude.ai, and launched as a research preview on October 21, 2026.
- **Access is limited.** The preview is for US Claude Pro and Max subscribers through a waitlist. Team and Enterprise plans are not supported yet.
- **It works while you are away.** Duet runs on its own cloud virtual machine with its own browser, checks connected accounts every few hours, prepares a morning briefing, drafts replies, and delivers larger work as files.
- **It inherits your Claude context.** Duet uses the memory, skills, and connectors from your Claude account and can reach more than 6,000 connectors and plugins in the Claude Marketplace.
- **Consequential actions need approval.** Sending potentially sensitive messages, paying, and deleting require you to approve a request showing the action, destination, and content, including every recipient.
- **The intent check runs outside the model.** Anthropic says a separate check, extended from Claude Code's auto mode classifier, judges whether each action matches your intent, so instructions hidden in a page cannot answer it.
- **Credentials never reach the model.** Passwords go through an encrypted form, and sign-in tokens are inserted by a proxy outside the agent's machine. This is the right pattern for any agent.
- **Some actions are blocked even with approval.** Trading securities, moving money between bank accounts, and accessing someone else's account are prohibited.
- **Proactive means the inbox becomes an input channel.** Anyone who can email you can now place text in front of an agent that acts on your behalf. Prompt injection stops being an edge case and becomes the default threat model.
- **Memory outlives connections.** Disconnecting an app stops new access, but what Duet has already learned stays until you reset its memory.
- **Background work is not free.** Duet's periodic checks and tasks draw from the same usage limits as your regular Claude chats.
- **Approval quality is the real bottleneck.** The best use of Duet is to keep approvals rare, meaningful, and carefully read, not to approve faster.

---

## What Claude Duet Actually Is

Most coverage has focused on the headline: Claude now messages you first. The details matter more.

|  | Claude Duet research preview |
| --- | --- |
| **Launched** | October 21, 2026 |
| **Model** | Claude Opus 5.5 |
| **Where** | Standalone app on iOS and Android, plus claude.ai |
| **Who** | US accounts on Pro and Max plans, via waitlist |
| **Not yet** | Team and Enterprise plans |
| **Price** | No extra charge during preview; uses your regular Claude usage limits, including session and weekly caps |
| **Runs on** | Its own cloud virtual machine and browser |
| **Context** | Your Claude memory, skills, and connectors |
| **Integrations** | 6,000+ connectors and plugins, including Gmail, Slack, QuickBooks, HubSpot, Docusign, and Gusto |
| **Purchases** | Through Stripe's Link wallet or Shopify's Shop Pay, using one-time cards |

Anthropic describes the target user as professionals and small business owners with more tasks than they can track. The company has also been clear about what Duet is not for. According to TechCrunch, Anthropic said Duet "isn't good at handling errands or booking tickets, and it can't show you its browser use as it happens."

Other preview limitations reported at launch:

- you cannot choose the model, watch Duet work, or take over its browser;
- it cannot make phone calls or send text messages;
- it does not monitor accounts continuously, only every few hours;
- it does not yet work with Microsoft 365; and
- some connectors, such as Slack, have limitations.

Anthropic's framing of why Duet exists now is about model judgment. Mike Krieger said, "We've found Opus 5.5 was our first model with the judgment to be proactive in the right ways." Anthropic's launch materials say the model's judgment helps it "decide what needs you, what can wait and when to check with you first."

That is a reasonable claim for a product team to make. It is also exactly the kind of claim that should never be the only control. The rest of Duet's design suggests Anthropic agrees.

---

## First, Separate Reactive, Scheduled, and Proactive Agents

"Proactive agent" is easy to blur with features that already exist. They are different things, and the differences determine the risk.

| Mode | Who decides when it acts? | What it reads | Consent model | Main risk |
| --- | --- | --- | --- | --- |
| **Reactive chat** | You, every time | What you choose to share | Per request | Wrong answer |
| **Scheduled routine** | You, by defining a trigger | What the routine is scoped to | Per routine | Wrong action on a schedule |
| **Proactive agent** | The agent, based on what it observes | Everything its connectors can see | Standing authority plus approvals | Wrong judgment about what matters, acting on untrusted input |

The distinction matters.

In reactive chat, the user is the filter. You decide which email to paste, which document to upload, and which answer to act on.

In a proactive agent, the agent is the filter. It reads the inbox, the calendar, the CRM, and the shared drive, decides what deserves your attention, and prepares an action.

That shifts three things at once:

1. **Input selection moves to the agent.** It reads content you never chose to show it, including content written by strangers.
2. **Timing moves to the agent.** It interrupts you when it decides something matters.
3. **Consent becomes standing.** You granted access once. The agent uses it continuously.

Approvals are how you take some of that control back. That is why their design, and their volume, matter so much.

---

## How Duet's Control Architecture Works

Anthropic published an unusually detailed safety, privacy, and security description for Duet on October 23, 2026. Reading it as an architecture, it looks like this:

```
   Connected accounts                     You
   (email, calendar, CRM,           (phone or claude.ai)
    accounting, docs, web)                  ^
            |                               | approval card:
            v                               | action, destination,
+-----------------------+                   | content, recipients
| Claude Duet agent     |                   |
| Opus 5.5 on a cloud   |-------------------+
| VM + isolated browser |  proposed action
| memory, skills        |
+-----------+-----------+
            |
            v
+-----------------------+   +-------------------------+   +---------------------+
| Intent check          |   | Outbound sensitive-info |   | Hard blocks         |
| outside the model     |   | classifier              |   | securities, moving  |
| (from Claude Code     |   | never share / needs     |   | money between       |
|  auto mode classifier)|   | consent / allowed       |   | accounts, others'   |
+-----------+-----------+   +------------+------------+   | accounts            |
            |                            |                +---------------------+
            v                            v
+-------------------------------------------------------------+
| Credential layer outside the agent                          |
| password form encrypted to browser | token proxy injects    |
| sign-in tokens at request time      | one-time payment cards|
+-------------------------------------------------------------+
```

Each layer controls something specific. Each also leaves something uncontrolled.

### Layer 1: Standing access through connectors and memory

Duet uses the memory, skills, and connectors from your Claude account. It checks connected accounts every few hours and prepares work.

This layer controls **what Duet can see**. It does not control **what Duet should trust**. An email from a stranger arrives through the same connector as an email from your manager.

### Layer 2: The approval tier

Before Duet sends a potentially sensitive message, pays, or deletes something, Anthropic says it "shows you the action, the destination, and the content, including every recipient," and waits.

Some steps cannot be covered by a "don't ask again" rule, including paying or sending money, deleting an order, and creating an account. Routines that run while you are away follow the same safeguards.

This layer controls **which actions require a human decision**. It does not control **whether the human actually reads the request**.

### Layer 3: An intent check outside the model

This is the most important design choice in Duet.

Anthropic says a separate automated check, extended from Claude Code's auto mode classifier, assesses whether each action matches your intent. In Anthropic's words: "The check runs outside the model doing the work so instructions hidden in a page cannot affect the outcome."

That is the right boundary. If a malicious email convinces the agent that forwarding a document is part of your task, the agent's own reasoning is compromised. A check that does not read the agent's reasoning, and is not reachable by the injected text in the same way, is far more robust.

This layer controls **whether the action plausibly matches your request**. It does not make the decision deterministic. It is still a classifier, and Anthropic says the safeguards "will occasionally miss something or flag a harmless message."

### Layer 4: Credentials never enter the model

Anthropic says, "Claude Duet never sees your passwords, browser cookies, sign-in tokens, or other credentials."

- Passwords are typed into a form in the Claude app, encrypted with a single-use key, and passed to the browser without being opened.
- Sign-in tokens stay off the agent's machine. A placeholder sits there, and a proxy outside the machine inserts the real value during a request.
- 1Password sign-in is planned, so you can approve credential use there.

This is the credential pattern I recommended in my article on agent identity, now shipped in a consumer product. A prompt-injected agent cannot leak a password it never saw.

This layer controls **credential exposure**. It does not control **what the agent does with the access those credentials grant**.

### Layer 5: An outbound sensitive-information classifier

A separate classifier checks every outgoing message, including files uploaded through the browser, against three tiers:

- **Never share:** sign-in credentials, full card and bank account numbers, and government ID numbers. Anthropic says Duet "is instructed never to share these with anyone, even if you ask."
- **Needs consent:** other private information, such as health or financial details, requires your explicit approval. Your own request counts as consent.
- **Allowed:** everything else.

If a message is blocked, Duet can rewrite it without the sensitive content and present the revised version for approval.

This layer controls **specific categories of data leaving**. It does not control **ordinary business content**, such as a quarterly report, going to the wrong recipient.

### Layer 6: Hard blocks

Some actions remain prohibited even with approval: trading securities, banking actions such as moving money between accounts, and accessing someone else's account.

These are deterministic boundaries, and they are the strongest controls in the system. No judgment, classifier, or tired human can override them.

### Layer 7: Scoped payments

Purchases use a one-time card from a wallet such as Link, limited to one merchant and one amount, and you approve in the Link app. Your real card number is not shared.

That is the task-bound spend pattern from my article on agent payments: scope the credential to the transaction, and put the approval on a surface the agent does not control.

### Layer 8: Identifying itself on the web

Duet identifies itself with a distinct User-Agent header and publishes its IP addresses. Anthropic notes that some websites have opted out of being visited.

That is a small detail with a large implication. Sites can recognize and govern agent traffic instead of guessing whether a browser session belongs to a person.

---

## What Duet Gets Right

From a production architecture perspective, several of Duet's choices are worth copying, whether or not you ever use Duet.

**It moves enforcement outside the model.** The intent check, credential handling, outbound classifier, and hard blocks all sit outside the model doing the work. That is the single most important principle for any agent that reads untrusted content.

**It treats credentials as infrastructure, not context.** Token injection through a proxy, and encrypted password handoff, mean the model never holds secrets.

**It uses non-agentic approval surfaces for money.** Payment approval happens in the wallet app, not in a screen the agent renders.

**It makes some actions unapprovable.** A short list of hard blocks is more trustworthy than any amount of judgment.

**It applies the same rules to background routines.** Many systems relax controls for scheduled work. Duet does not, according to Anthropic.

**It tested against temptation, not just attacks.** Anthropic says its safeguards evaluations used innocent, injected, and "temptation" variants of tasks, alongside shadow traffic, plus red teaming, an external penetration test with source code access, and bug bounty coverage through HackerOne.

**It is honest about limits.** Anthropic says approval frequency, sign-in methods, and classifier accuracy are still being adjusted, and that the safeguards will sometimes miss things.

That candor is more reassuring than a claim of perfect safety would be.

---

## What Duet Does Not Solve Yet

### Approval fatigue is a structural problem

Approvals work when they are rare and meaningful. A proactive agent's value comes from doing many things, so approval volume naturally grows with usefulness.

Anthropic's own statement names the failure: too many requests teach people to tap through them. Showing every recipient is the right design. It only works if someone reads the recipient.

The fix is not faster approvals. It is fewer, higher-quality ones: grouping related actions, highlighting anomalies such as new recipients and lookalike domains, and reserving interruptions for decisions that actually need a human.

### The inbox is untrusted input by default

In chat, prompt injection usually requires you to paste or browse something malicious. A proactive agent reads whatever arrives.

Anyone who can send you an email, share a document, or post in a channel your agent monitors can place text in front of it. Anthropic says Duet uses prompt-injection defenses from its browser-use research, and the intent check is designed so that hidden instructions cannot answer it.

Those defenses reduce risk. They do not change the basic fact: a proactive agent's threat model starts at "attackers can write to my inputs."

### Memory persists after access ends

Anthropic says disconnecting an app stops new access immediately, but "what Claude Duet already learned stays until you reset its memory." Duet also uses memory from your Claude account, so details from earlier chats are visible to it.

That is a reasonable product decision. It is also the exact surface I described in my memory poisoning article. Content read from an untrusted email can shape what the agent remembers, and that memory can outlive the connection that produced it.

If you disconnect an account because you are worried about it, reset memory too.

### "Proactive" does not mean "real-time"

Duet checks connected accounts every few hours, not continuously. Anthropic has acknowledged that it can misunderstand conversations, misjudge priorities, or miss developments between checks.

Do not use a proactive agent as an alerting system for anything time-critical.

### The intent check is still probabilistic

"Outside the model" is a major improvement. It is not the same as deterministic. A classifier deciding whether an action matches your intent will have false negatives and false positives, which Anthropic says directly.

That is why the hard blocks and the human approval remain essential. In my article on Jev and decision models, the principle was: a probability is evidence, not permission. The same applies here.

### Background work spends your budget

Duet's morning briefing, periodic account checks, and tasks draw from the same usage limits as your regular Claude chats, including session and weekly caps. An agent that works while you sleep also spends while you sleep. Anthropic gave each new user one full limit reset, available until November 30, 2026, which acknowledges the point.

### You are still accountable

An email Duet sends with your approval is your email. A purchase you approved is your purchase. A proactive agent does not move accountability. It moves the moment at which you exercise it, often to a phone screen between meetings.

### Enterprise controls are not here yet

Duet is not available on Team or Enterprise plans, and it does not support Microsoft 365. That means organizations do not yet have admin-level controls over it.

It also means some professionals will connect personal Pro or Max accounts to work email and Slack. For IT teams, that is a shadow-agent problem: an autonomous system with standing access to company data, outside company policy, created by an employee trying to be productive.

---

## Duet Is Part of a Category, Not a One-Off

Duet launched into a crowded moment. Coverage at launch positioned it against OpenAI's Dots and Meta's Muse, and TechCrunch listed several other personal and business agents in the same space.

The details differ. The direction is the same: assistants are moving from answering questions to monitoring your accounts and acting on your behalf.

That makes Duet's safety design more important than its feature list. The patterns Anthropic published, including out-of-model intent checks, credential proxies, one-time payment cards, outbound classifiers, and hard blocks, are a reasonable baseline to compare any proactive agent against.

---

## How I Would Use Duet Today

If you are in the preview, here is the setup I would start with.

1. **Connect less than you can.** Start with one email account and one calendar. Add accounting, CRM, or e-signature tools only after two weeks of watching how Duet behaves.
2. **Read every recipient for the first two weeks.** Use that period to learn what normal approval requests look like, so anomalies stand out later.
3. **Avoid "don't ask again" for external email.** Keep approvals for anything leaving your organization.
4. **Treat email content as information, not instructions.** If Duet proposes something because an email asked for it, check who sent that email.
5. **Keep high-risk finance out of scope.** Duet already blocks moving money between accounts. I would also keep payroll and banking connectors disconnected during the preview.
6. **Review memory regularly.** Check what Duet has learned, and reset memory when you disconnect an account.
7. **Watch your usage.** Background checks consume limits. If Duet is spending your weekly cap on low-value briefings, reduce its scope.
8. **Follow your company's policy.** Do not connect work accounts to a personal agent unless your organization allows it.

---

## A Four-Week Trial Plan for Small Teams

Duet is aimed at professionals and small businesses. For a small team trialing it, I would use a short, deliberate plan.

### Week 1: Observe only

- Connect one inbox and one calendar per person.
- Use briefings and drafts, but send nothing through Duet.
- Note which items it flagged correctly, which it missed, and which it overrated.

### Week 2: Approve low-risk sends

- Allow Duet to send internal replies with approval.
- Count approvals per day per person.
- Record any approval that was tapped without reading.

### Week 3: Add one business system

- Connect one system, such as the CRM or accounting tool.
- Let Duet prepare reports and dashboards from it.
- Review whether any outbound message contained data that should not have left.

### Week 4: Decide the boundary

- Decide which actions Duet may prepare, which it may send with approval, and which stay manual.
- Write that boundary down and share it with the team.
- Reset memory for any accounts you disconnect.

At the end of four weeks, you will know whether Duet saves time without creating approval fatigue. That is the only metric that matters for a proactive agent.

---

## Seven Questions to Ask Any Proactive Agent

1. Which checks run outside the model that does the work?
2. Does the model ever see passwords, cookies, or tokens?
3. Which actions can never be approved, regardless of what the user taps?
4. What does an approval request show, and does it highlight anomalies such as new recipients?
5. What happens to memory when I disconnect an account?
6. How often does it check my accounts, and what can it miss between checks?
7. What admin controls, audit logs, and policy settings exist for organizations?

If a product cannot answer the first three, it is asking for trust it has not earned.

---

## Final Take: The Assistant That Speaks First

For most of the history of AI assistants, the human started every conversation. That gave us an invisible control: we chose what the AI saw and when it acted.

Claude Duet changes that. It watches, prioritizes, prepares, and asks. That is genuinely useful, and Anthropic's published safeguards show a serious attempt to make it safe: checks outside the model, credentials outside the model, payments scoped to one merchant and amount, and a short list of actions no approval can unlock.

Those controls handle what machines can handle.

What remains is the moment when a human reads, or does not read, an approval card.

The most important design goal for proactive agents is not speed or autonomy. It is protecting that moment: fewer interruptions, clearer anomalies, and approvals that actually mean someone looked.

Duet speaks first.

Make sure you still have the last word.

---

## Sources and Further Reading

1. Anthropic (Claude), **Claude Duet Safety, Privacy, and Security** (October 23, 2026): <https://claude.com/blog/claude-duet-safety-privacy-and-security>
2. VKTR, **Claude Duet: Anthropic previews an AI agent that messages you first** (October 22, 2026): <https://www.vktr.com/ai-platforms/claude-duet-anthropic-previews-an-ai-agent-that-messages-you-first/>
3. TechCrunch, **Claude Duet app is Anthropic's bet on agents** (October 22, 2026): <https://techcrunch.com/2026/10/22/claude-duet-app-is-anthropics-bet-on-agents/>
4. Help Net Security, **Anthropic details what stops Claude Duet from going rogue** (October 26, 2026): <https://helpnetsecurity.com/2026/10/26/anthropic-claude-duet-security-safeguards>
5. 9to5Mac, **Anthropic takes on ChatGPT Dots and Meta Muse with Claude Duet** (October 21, 2026): <https://9to5mac.com/2026/10/21/anthropic-takes-on-chatgpt-dots-and-meta-muse-with-claude-duet/>
6. Let's Data Science, **Anthropic opens Claude Duet research preview for proactive agent work**: <https://letsdatascience.com/news/anthropic-opens-claude-duet-research-preview-for-proactive-a-16522f5d>

---
