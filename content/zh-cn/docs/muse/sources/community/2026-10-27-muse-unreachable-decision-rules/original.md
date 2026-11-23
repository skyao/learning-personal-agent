来源：https://aihomebuilding.com/stories/muse-unreachable-decision-rules-2026
取文：2026-11-22，直接下载

Picture a six-hour flight. Somewhere over the middle of it, your agent finishes the research you asked for, finds the better price you hoped for, and reaches the one step it cannot take alone. An approval card waits on a phone that is in airplane mode, in a bag, under a seat. Nothing happens for six hours, which is exactly what the safety design intends, and also exactly the problem.

Approval gates assume a reachable human. Scheduled work, background jobs, and long-running tasks do not. Meta describes Muse as an agent that keeps working after you close the app and comes back when something changes or when it needs approval. That sentence reads as reassurance. Read it again as an operations manager and it becomes a scheduling question: what is the agent supposed to do during the hours when coming back is impossible?

Twenty years of running operations teaches one lesson about this kind of gap. If you do not write the rule before the absence, the system will invent one during it. An invented rule, executed at 3 a.m. on stale facts, is how a good assistant becomes an expensive story.

## What Meta actually promises, and what it leaves open

Start with the part that is documented. Meta says sensitive steps such as sending an email or completing a purchase pause for user approval. It says each user gets a dedicated cloud computer, called the Muse Secure VM, and a second agent, called Sentinel, that must approve every internet-bound action. It says a full audit trail shows everything the agent has done and plans to do. Those are real controls, and they are better than a chatbot with a credit card and no brakes.

Meta also says, in its own words as reported in an October 2026 review of the money features, that Muse is not immune to attack and will sometimes make mistakes. More than 10 million people in the United States and Canada had set Muse up by late October 2026, according to chief executive Mark Zuckerberg, which means this is no longer a question for early adopters. It is a question for anyone whose agent runs while they sleep, fly, operate, or sit in a room where phones are not allowed.

Now note the open space. No published Meta rule was found for how long an approval request stays valid, or for what an agent does when a time-sensitive approval expires. No published fallback order tells a task who to ask second, or what to do when nobody answers at all. That silence is not a criticism of the approval gate. It is the reason you need a rule of your own on top of it.

## Four tiers, decided before you go dark

Sort every task you hand an agent into one of four tiers before you become unreachable. Do it in writing, inside the task itself, because a rule remembered in your head helps nobody at 3 a.m.

**ACT.** Reversible, low-cost, already fully specified. Reading, searching, summarizing, drafting, checking a price without buying, and updating a list all belong here. If the act can be undone with one click and costs nothing to redo, let it run. An agent that cannot do these things without you is not an assistant, it is a pager.

**PREPARE.** Do every step short of the irreversible one, then leave a single decision waiting. Research the flights, fill the form, draft the email, price the options, and stop. When you land, one tap finishes the job instead of one tap starting a forty-minute task. Preparation is the most underused tier in agent work, because it feels like half a job. In operations, half a job done well is what lets the second half happen fast.

**HOLD.** Freeze the task and log the freeze, with a named re-check time. Use HOLD when the facts could move before you return: a price that changes daily, a seat that sells out, a person whose availability you have not confirmed. A held task is not a failed task. It is a task that refused to act on a guess, and that refusal deserves to be visible in the audit trail rather than buried.

**EXPIRE.** Let the window close and say so. Some opportunities should die rather than be acted on late. A discount that ended yesterday, a reply to a message whose context has already moved on, a booking for a date that has passed: acting on any of these after the fact creates a new problem while solving an old one that no longer exists. Expiry is a decision, not an accident, and it should be recorded as one.

Assigning a task is a judgment call, and the test for it is simple. Ask two questions about each task: what happens if this is wrong, and can I undo it? Low harm and easy reversal point toward ACT. High harm or no reversal point toward PREPARE, HOLD, or EXPIRE, in that order of urgency.

## Approvals have a shelf life

One rule governs all four tiers, and it is the one most people skip. An approval has a shelf life. A price, a seat, a deadline, or a person's availability that was true on Monday is evidence on Friday, not permission. Any instruction that outlives its facts needs re-checking, not execution.

Apply a Monday test to every standing instruction before a trip. If you told the agent on Monday to book the cheapest flight under $400, and by Friday the only flight under $400 leaves at 5 a.m. from an airport an hour away, did you approve that flight? You approved a price. You did not approve a 5 a.m. departure, and an agent that treats those as the same instruction has confused your words with your intent.

Write the shelf life into the task. "This approval is valid until Thursday at noon Pacific, and only while the price stays under $400 and the departure stays after 8 a.m." That sentence costs ten seconds to write and saves the argument about what you meant. Standing instructions without expiry dates are how a reasonable agent does an unreasonable thing with a straight face.

## Write the fallback order, or do not run the task

Every task that runs while you are unreachable needs a fallback order, written in advance. First, a named second person, if the task allows one. Second, a prepared draft or a held state. Third, expiry. Never an invented answer.

Consider a bill negotiation. PREPARE the case, gather the bills, and draft the script. If the provider offers a deal while you are unreachable, HOLD it and log the offer with its deadline. If no second person is authorized to accept, the task expires with the offer rather than accepting a deal you never saw. Losing a deal stings. Accepting a two-year contract you never read stings longer.

Consider a message to a client. PREPARE the draft. If the client replies with a question while you are gone, HOLD the reply unless the answer is already in writing somewhere the agent can quote exactly. An agent that improvises an answer to a client on your behalf, while you cannot correct it, is not saving you time. It is spending your credibility.

Security guidance backs this shape. OWASP's LLM06:2025 entry on excessive agency names three root causes: excessive functionality, excessive permissions, and excessive autonomy. Its prevention list starts with scoping what an agent can call and what each extension can do, and only then requires human approval for high-impact actions. Approval is the last layer, not the first. Scoping is the work you do before the flight, and the four tiers are scoping in plain language.

## Do the return audit, every time

Coming back is a job, not a moment. Give it five minutes and a fixed checklist, modeled on a weekly review practice that community guides recommend for Muse users: what the agent did in the window, what it flagged that did not matter, what it got wrong or could not finish, and everything new it saved to memory.

Work the checklist in order. First, what acted without you, and was each act reversible? Second, what waited, and is any wait now urgent? Third, what expired, and does anything expired need re-asking? Fourth, what changed in memory during the window, and does any new memory item deserve deleting or correcting? Fifth, what is still pending, and does it still deserve to run? Run that list before you hand the agent its next job, because an agent carrying stale instructions into a new week is a second absence waiting to happen.

Pay special attention to memory. A one-off request made during a hectic week should not silently become a standing preference, and a preference you changed mid-trip should not be overwritten by an older instruction the agent kept. Memory edits are the quietest way an agent drifts from what you want, and the return audit is the cheapest time to catch the drift.

## What this protocol cannot fix

Honesty requires naming the limits. Four tiers do not fix a wrong premise in the original instruction. If you told the agent the wrong date, the wrong budget, or the wrong person, it will execute your error with admirable efficiency across all four tiers. They do not fix manipulation through retrieved documents either, since an agent can be steered by text it reads on a page or in a message. They do not fix the half-asleep approval tap, the one where you approve a card at midnight in a hotel room without reading it, which is a human failure no tier can prevent.

One practitioner essay draws a harder line than this article does, naming five decisions an agent should never make without a person: financial transactions, data destruction, external communication, self-modification, and agent reproduction. Treat that list as one writer's boundary, not an industry standard. It is useful as a starting argument with yourself, less useful as a rule, because real work lives in the gray area between "never" and "always," and the gray area is exactly where your tiers have to do their work.

## Copy this into your next scheduled task

Use this block, adapted, before any absence. It is deliberately boring. Boring is what you want from a rule that runs while you sleep.

"While I am unreachable: act only on reversible, low-cost steps I fully specified. Prepare everything else and leave one decision waiting. Hold any step whose facts could change before I return, and log the hold with a re-check time. Let time-sensitive windows expire rather than acting on them late, and report each expiry on my return. No step is approved after its facts change. If no fallback applies, hold, do not improvise. On my return, report what acted, what waited, what expired, and what changed in memory."

Agents will keep getting better at acting while you are gone. That progress makes the question sharper, not softer. A faster agent with no decision rules does not save you more time. It makes bigger mistakes while you are not looking. Write the rules before you go dark, and the agent that waits for you will be worth the wait.

*Sources: Meta, Introducing Muse and Muse product descriptions, via [MarkTechPost](https://www.marktechpost.com/2026/09/08/meta-introduces-muse-a-personal-ai-agent-that-runs-on-its-own-dedicated-secure-cloud-computer/), [ToolsFine](https://toolsfine.com/blog/meta-muse-personal-ai-agent-launch-features-safety-privacy.html), and [AgentPedia](https://agentpedia.codes/blog/meta-muse-personal-agent-guide); Yahoo Finance review of Muse money features, October 22, 2026, via [Trade2Spike](https://www.trade2spike.com/ai-in-action/meta-muse-ai-agent-manage-your-money-review-10-million-users-identity-theft-resource-center-too-new); OWASP LLM06:2025 Excessive Agency, via [Safeguard](https://safeguard.sh/resources/blog/human-approval-for-agent-actions-safeguard-desktop-and-mobile-apps-early-access) and [Avesta Labs](https://avestalabs.ai/blog/ai-agent-human-approval); autonomy-boundary practice via [Inteq](https://www.inteqgroup.com/blog/which-decisions-can-an-ai-agent-make-and-which-require-human-approval) and [Zodinet](https://zodinet.com/en/ai-safety-for-agentic-systems-why-autonomy-changes-risk/); weekly review practice via [ZachDoesAI](https://zachdoesai.com/guides/meta-muse/).*
