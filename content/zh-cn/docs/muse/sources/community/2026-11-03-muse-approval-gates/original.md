来源：https://aihomebuilding.com/stories/muse-approval-gates-where-your-agent-stops-2026
取文：2026-11-17，直接下载

Picture the moment clearly, because the whole relationship between you and an agent lives inside it. You asked Muse to sort out a trip. It has compared flights, held nothing, spent nothing, and now a small card appears on your screen with a total, a merchant, and three choices. Allow once. Allow for this task. Deny. Your thumb hovers. Everything Muse promised about safety, everything it means to hand real work to a machine that acts while you sleep, narrows to that pause.

Meta's launch announcement of September 8, 2026 made the promise in plain language: Muse "will seek approval for sensitive actions taken on your behalf like signing in, completing a reservation, or making a purchase," and it "comes back when something changes or when it needs approval, like before it sends an email or makes a purchase." ([aicrawlercheck.com](https://aicrawlercheck.com/blog/meta-muse-ai-agent-website-guide), summarizing Meta's launch post) Around that promise sits an architecture meant to make it believable: each person gets a dedicated cloud computer, a Muse Secure VM, and a separate program called Sentinel approves anything that reaches the internet, while passwords and payment methods sit in secure storage the agent itself cannot see. Users also get an audit trail, an Activity log showing what the agent did and which permissions were granted.

That is the brochure. What follows is the map nobody published: which actions actually pause, which ones pause once and then run free, and which never pause at all.

## Tier one: the actions that pause every time

Signing in, completing a reservation, making a purchase, sending an email. Those are Meta's own examples, and they share a quality worth noticing. Each one is irreversible in a practical sense. A sent email cannot be unsent, a charged card cannot be uncharged without a dispute, a reservation holds someone else's inventory. Pausing here is good design, because the cost of being wrong lands on you, not on the model.

Payment carries its own second gate. Muse pays through Link by Stripe, which issues a one-time card number for each purchase, so your real card number stays private and you confirm the amount before Muse pays. ([thisweekinfintech.com](https://www.thisweekinfintech.com/p/the-invisible-invoice)) Meta has since added Shop Pay and PayPal as payment options, and Shop Pay's rollout keeps approval with the buyer: you review the purchase inside Shop Pay and approve it before anything is charged. Two approvals, from two different systems, for one purchase. Redundant on purpose, and that redundancy is the point.

## Tier two: the blanket permission

At each checkpoint, independent setup guides document three choices: Allow once, Allow for this task, or Deny. ([graniteai.co](https://www.graniteai.co/downloads/getting-started-with-muse-guide.pdf)) Allow once is the honest button. Allow for this task is the dangerous one, and it deserves a longer look than it has received.

When you tap it, one approval covers every subsequent step the agent counts as part of that task. But the boundary of "this task" is drawn by the agent's own plan, not by a line you drew. A trip that starts as "find me a flight" can grow legs: a hotel, a rental car, a restaurant reservation, each step arguably part of the same task, each step further from the thing you pictured when your thumb landed. Nothing in Meta's published material defines where a task ends. Until it does, treat that middle button as a signature on a blank page with a polite title.

Use it for research, for drafts, for comparisons. For anything touching money, identity, or an outbound message, tap Allow once and re-approve step by step, because yes, it is slower, and that slowness is the feature.

## Tier three: everything that never pauses

Reading, searching, summarizing, drafting, comparing prices, and scheduled background work never ask at all. Most of that is harmless. Scheduled work is the exception that matters, because it runs while you are away: its approvals queue until you return, which means the work either stalls silently or was pre-approved broadly enough to proceed without you. Our earlier coverage documented scheduled tasks failing quietly overnight and zombie tasks outliving their purpose. Approval gates do not fix that failure mode. They create a version of it, a job waiting on a human who is asleep, or a job that only proceeds because a human approved too much in advance.

There is one more gate, and it belongs to nobody at Meta. On September 21, 2026, Amazon blocked Muse from shopping on Amazon.com, while Shopify and Walmart chose to work with it. ([aicrawlercheck.com](https://aicrawlercheck.com/blog/meta-muse-ai-agent-website-guide)) A merchant's refusal is a boundary your agent cannot talk its way past, and for a user it functions as an accidental safety feature: a store that blocks agents cannot have its checkout driven without you in the room.

## Where the gates broke

In September, security researcher Patrick Wardle of the Objective-See Foundation found an undocumented macOS preference key in the Muse desktop client that set the destination for dictation audio, writable by any unprivileged process running as the logged-in user. His proof of concept rerouted the agent's voice traffic through a server the attacker controlled, capturing the user's Muse authentication token while forwarding traffic so nothing looked broken. ([coderlegion.com](https://coderlegion.com/32498/one-config-key-was-enough-what-the-meta-muse-zero-day-teaches-about-agent-trust-boundaries)) Meta removed the key from production builds within about a day, and Wardle confirmed the fix on September 22, 2026. No CVE was assigned, and Meta's position was that the flaw required prior code execution on the machine, making it a local configuration problem rather than a remote exploit.

That framing is technically defensible and misses the lesson. Gates check the action, not the hand on the keyboard. An attacker holding a valid Muse token drives the agent directly, and the agent does exactly what it was built to do, for whoever holds the token. Every approval card in the world is irrelevant once the credential itself is captured, because the system cannot tell the thief's approval from yours. Approval design and credential design are the same problem, and Muse's launch architecture, a vault the model cannot see, plus a watchdog that approves outbound traffic, is genuinely strong. One writable preference key nearly made it decorative.

Then there is the audit gap. Individual users get an Activity log. Organizations get nothing: reporting on the launch found no SIEM audit export, no IT admin console, and no DLP integration in Muse's documentation or the consumer product tested. ([coderlegion.com](https://coderlegion.com/32498/one-config-key-was-enough-what-the-meta-muse-zero-day-teaches-about-agent-trust-boundaries)) Muse crossed 2.5 million downloads in its first 13 days, according to Sensor Tower figures cited in that reporting. Some of those downloads sit on machines holding corporate data, and nobody centrally can see what those agents did. A household can audit one agent. A company running dozens cannot audit any of them.

## What to do with this map

Choose Link one-time cards over a saved store card, so each purchase is a distinct instrument rather than an open line to your account. Reserve "Allow for this task" for work with no irreversible step in it. Once a month, open the Activity log, revoke permissions you no longer recognize, and check which scheduled tasks are still running, because a task you forgot is a permission you never revoked. If you run Muse on a work machine, assume no central oversight exists yet, and do not connect work accounts you cannot afford to have act unattended. And when a store blocks agents, do not treat it as an inconvenience to route around. Treat it as a store that just told you where its own line is.

## The strongest case against all of this

Approval gates are friction dressed as safety. Every pause drags you back to a task you delegated precisely to avoid thinking about it, and the rational response to dozens of pauses is to start tapping "Allow for this task" without reading. A system that trains its users to approve blindly is less safe than one that picks a small number of genuinely irreversible actions and handles the rest itself. That criticism is fair, and it points to the right fix: fewer gates, not more, with each remaining gate carrying the full consequence in plain language, so the pause earns the interruption it demands.

## What this article did not prove

Meta has not published a complete list of actions that trigger approval. Tier one rests on the launch post's examples, and the word "like" in that sentence means the list is illustrative, not exhaustive. No public data exists on how often users choose "Allow for this task" over "Allow once," or on approval fatigue rates, so the scope-creep warning is a design inference, not a measured frequency. The zero-day account rests on Wardle's proof of concept and secondary reporting; Meta's statement beyond the fix confirmation was not independently verified here. Subscription prices are deliberately omitted: official statements say Muse is free for most uses with paid plans, and no verified price list was used. Those gaps are the next reporting job, and they are stated here so nobody mistakes this map for a finished one.

Interfaces are relationships. A gate is a moment where the agent admits it does not know enough about your life to proceed alone, and asks. That admission is the most trustworthy thing Muse does. Keep it rare, keep it honest, and never let a single tap sign away the whole trip.
