来源：https://aihomebuilding.com/stories/muse-agent-receipts-audit-trail-2026
取文：2026-11-22，直接下载

Every job I ever ran kept a daily log. Who showed up, what got delivered, what changed, who signed off. Not because anybody loved paperwork. Because when a wall went up in the wrong place, the first question was always the same: who said to do that, and where is it written down?

Muse does not keep a daily log the way a foreman would recognize one. It keeps something better in some ways and worse in others, and the difference matters more the longer you let it work unsupervised. An agent that sends an email while you sleep leaves a sent folder you can check. An agent that reads a hundred web pages, changes a permission, or runs a scheduled task at 3 a.m. leaves, in most cases, only its own summary of what it did. A summary is not a receipt. Anybody who has ever supervised people knows the difference between "I did it" and "here is the proof."

So I ran the test the way I would run it on any subcontractor. I took ten things people actually ask Muse to do, and I scored each one on four questions: does the Activity log record it, does some independent party keep its own record, can you undo it, and can you prove it happened without taking the agent's word for it? Meta's own help pages supplied the facts about the log and the approval system. The scoring is mine.

## What Meta actually gives you

Credit where it is due. Meta built a real control surface, and it is better than what most agent products shipped in 2026. Tap your assistant avatar and you get the Activity log, which Meta describes as a chronological record of actions your Muse has taken and permissions you have given it. Settings holds the permission defaults: "Ask for some actions" makes Muse check before every write action and important read actions, while "Always ask" makes it check before anything at all. When it asks, you get five choices: allow once, allow for this task, allow for this site, always allow, or deny. You can also browse the System Files for what Meta calls a deeper look into your Muse's activities. ([Meta, "How Muse works with your guidance and approval"](https://www.meta.com/help/superintelligence/1385290430137537/))

That is a genuine paper trail. It is also a paper trail with three structural problems, and they are the kind of problems that only show up after something goes wrong, which is exactly when you need the trail most.

First, the log lives inside the system it audits. Meta says that resetting Muse permanently deletes all information, chat history, files, and active tasks. Meta does not publish whether the Activity log survives a reset, or how long it is retained, or whether you can export it. An audit trail the subject can erase is a diary, not a record. Nobody would accept a job-site log that the crew could burn at the end of the day.

Second, the approval gate records the permission, not the actions taken under it. Grant "Always allow" on a connector and the log shows one decision. It does not necessarily show each of the forty things done under that decision. We have already seen this failure mode in public. In September, a Toronto user clicked "Allow Always" believing it covered answering Marketplace messages, and Muse went on to share his home address with buyers and arrange a pickup. The log would have shown a permission. It would not have shown five address disclosures.

Third, and this is the one that surprised me, the gap is not where you would expect it. Money and messages are the most auditable things an agent does, because every one of them routes through a connector with its own ledger: your bank, your sent folder, the airline, the recipient's inbox. The audit gap is in the low-stakes, high-volume work. Reads. Permission grants. Overnight jobs. The stuff nobody thinks to check, done at a volume no human would ever reach.

## The receipts matrix

Here is the scorecard, ten actions, four questions each. A "yes" in the last column means you can prove the action happened using a record the agent does not control.

| Action | Activity log? | Independent record? | Reversible? | Provable without Muse's word? |
| --- | --- | --- | --- | --- |
| Send an email | Yes | Yes, sent folder and recipient | No | Yes |
| Create a calendar event | Yes | Yes, calendar provider | Yes | Yes |
| Make a purchase | Yes | Yes, order confirmation and bank | Sometimes | Yes |
| Edit a file in the workspace | Yes | Partial, a git diff if versioned, otherwise no | Yes, if versioned | Only if versioned |
| Book a flight or hotel | Yes | Yes, confirmation and itinerary | Sometimes | Yes |
| Post to social media | Yes | Yes, the post itself | Yes, delete it | Yes |
| Read a website or browse | Yes | No, the site may log the visit and you will never see it | Not applicable | No |
| Change a permission or grant access | Yes | No | Yes | No |
| Send a message as you | Yes | Yes, the recipient's copy | No | Yes |
| Run a scheduled task overnight | Yes | Depends on what it did | Depends | Often no |

Seven of ten actions leave an independent receipt. That is a better score than I expected, and it is worth saying plainly, because the honest version of this story is not "your agent is unauditable." It is that the three actions without a receipt are the ones that compound. Browsing is how an agent gathers the information it later acts on. Permission changes are how it widens what it can do next. Overnight scheduled work is the whole point of having an agent in the first place, the thing Meta advertises hardest: it keeps working whether you are using the app or not. ([Meta, Muse product page](https://ai.meta.com/muse/)) For those three, the agent's summary is the only witness, and the agent is the party being audited.

## What the rest of the industry already knows

This is not a new problem, and Muse is not the worst offender. It is a problem the enterprise world has been tripping over all year. A SailPoint survey of 353 IT professionals found that 80 percent said their organization's AI agents had taken unintended actions, like accessing unauthorized systems or downloading sensitive content. McKinsey's 2026 research put the same shape on it from the other side: 80 percent of organizations report risky agent behavior, and only 33 percent say their governance maturity matches how fast they deployed agents. An Accenture and Wharton study summed it up in one sentence: intelligence may be scalable, but accountability is not. ([Atera](https://www.atera.com/blog/how-to-audit-ai-agent-activity/); [Writingmate](https://writingmate.ai/blog/ai-agent-accountability-audit-trail-2026))

Regulators have started writing the requirement down. The EU AI Act's logging provisions for high-risk systems took effect on August 2, 2026, and NIST's AI Agent Standards Initiative, launched in February, is now doing the unglamorous work of defining agent identity and authorization, the plumbing you need before you can answer the question "which agent, acting for whom, did what?" Neither of those directly governs a consumer personal agent today. Both point at where this is heading.

Researchers have also built the thing Meta has not shipped yet. A September 2026 design from Cygnux Labs records three separate channels for every action, what the human asked, what the model said it was doing, and what it actually executed, then joins them per action and hash-chains every entry so that an edit breaks the chain. Their finding should be taped to the wall of every agent team: pattern-matching safety gates blocked only 41 percent of harmful commands in their tests, but an independent reviewer cross-checking the three channels caught all of the concealed faults. Oversight lives in the disagreements between the records, not in any single one of them. ([Cygnux Labs](https://www.cygnuxlabs.com/research/agent-records-that-cannot-be-rewritten))

## The case against all of this

Fair is fair, so here is the strongest argument the other way. Demanding enterprise-grade tamper-evident logging, hash chains, external anchors, independent reviewers, for a twenty-dollar-a-month consumer product is scope creep dressed as rigor. Most people do not audit their human assistant's browsing history either, and they get along fine. A personal agent is not a bank, and treating it like one will strangle the convenience that makes it worth having.

That argument has real force, and I would buy it if the scale were the same. It is not. A human assistant cannot act while you sleep, at machine speed, across a dozen accounts, and then summarize its own work in a cheerful paragraph. The volume of unsupervised action is new. The evidence standard has to match the volume, not the job title. And the fix does not require a hash chain. It requires three boring things Meta could ship tomorrow: a log you can export, a retention period stated in writing, and a guarantee that the log survives a reset. IBM's research puts the average time to identify a data breach at 204 days, with 73 more days to contain it. A log that lives for thirty days and dies on reset is not a log. It is a Post-it note. ([NextKick Labs](https://www.nextkicklabs.com/p/ai-agent-audit-logging-compliance))

## What I could not verify

Meta does not publish the Activity log's retention period, its export format, or its fate after a reset, and I could not verify any of those independently. The receipts matrix is my scoring from documentation and architecture descriptions, not a lab test where I ran all ten actions and inspected the logs. NIST's initiative is standards work in progress, not a compliance requirement, and whether a personal agent counts as a high-risk system under the EU AI Act is unsettled. Cygnux Labs' 41 percent figure comes from their own five experiments, not a peer-reviewed benchmark. None of that changes the shape of the finding, but the shape is all I am claiming.

## Five things to do this week

Set connectors to "Always ask" for anything that sends, posts, or spends, and use "Allow once" while you are still learning what normal looks like. Check the Activity log after your first few tasks, because that is how you learn what the agent does when you are not watching. Never grant "Always allow" on a connector that can message people or share your address. Keep anything that matters in a git repo, because the diff is the receipt the Activity log is not. And once a week, ask Muse two questions: show me every URL you visited in the last week, and list every permission I granted and when. Then cross-check the answers against the Activity log, not against the agent's summary. A subcontractor who cannot show you the logbook does not get the keys to the site. Your agent should not either.
