来源：https://aihomebuilding.com/stories/muse-standing-instructions-half-stick-2026
取文：2026-11-22，直接下载

Every shop I ever ran had a wall with standing orders: safety glasses past this line, the forklift under eight miles an hour, check the oil before you start the compressor, not after it seizes. Nobody reads the wall. A new hire learns the rules the same way everyone learns them, which is somebody yells at him the first time he breaks one, and by the third week he has internalized the ones that get enforced and filed the rest under decoration.

Personal AI agents have standing orders now, except theirs are files instead of corkboards: Meta's Muse keeps a persona file describing the values and habits it tries to hold to in every conversation, a memory file holding the facts and preferences it has decided are worth keeping about you, and a user file describing who you are. These files ship with the product, you can edit them yourself, and a nightly background pass keeps them tidy. Twenty years of running shops taught me which standing orders survive contact with real workers, and the open question is whether a machine reads the wall any better than a nineteen-year-old apprentice.

## The Machine That Reads the Wall

To be fair to the apprentice, Muse's wall is more organized than any shop I ran. A third-party teardown of the Muse runtime, published last month, shows the agent stores memory in plain Markdown: a short curated sheet of facts and commitments, dated daily logs for the detail, and a memory bank organizing material into circumstances, experiences, and preferences, each with citations back to the source lines it came from. Underneath sits a database tracking each claim's evidence and confidence, so a newer claim can explicitly replace an older one instead of just contradicting it quietly. An hourly background job checks new claims against the original messages, which is rung one of the ladder running as infrastructure: the memory does not trust itself, so it audits itself, every hour, while you sleep. A nightly pass writes guidance for future sessions, and the notes from that pass are deliberately kept out of the agent's live prompt, so they work as standing guidance rather than injected orders, which is a design decision with a philosophy inside it: guidance the agent can consult beats orders the agent must obey, because consulted guidance survives the density problem and obeyed orders do not. [The full teardown is worth reading.](https://mouse.dev/blog/muse-runtime-export/)

That is a serious piece of infrastructure for remembering, and the full teardown is worth reading. But remembering is not obeying. Knowing that you prefer morning appointments is one job, and a small one; the real work starts when the preference has to survive contact with forty competing rules, a crowded context window, and a Tuesday morning when everything is on fire. Following "never book anything before 9 AM" forty mornings in a row, while you are also holding forty other rules about email, purchases, messaging tone, and what counts as urgent, is a different job entirely. And this year, for the first time, researchers started measuring the second job.

## What the Numbers Say

A 2026 paper called "The Compliance Gap" ran the clean version of the experiment. It took identical instructions and placed them in four different architectural positions: the system prompt, the user message, a tool description, and repeated at multiple points. Compliance ranged from 26 percent, when the instruction lived in a tool description, to 65 percent when it was repeated. And the content of the instruction explained four times more variance than its position, which means how you write the rule matters far more than where you file it. [arXiv, 2026.](https://arxiv.org/html/2605.01771)

Density is the other enemy, and the IFScale benchmark fed frontier models up to 500 simultaneous instructions on a business report task. Even the best models in the world managed only 68 percent compliance at maximum density, degrading in three distinct patterns: some held near-perfect until a critical density and then collapsed, some decayed linearly, some fell off a cliff exponentially. Models also showed a bias toward earlier instructions, so the rules at the bottom of your list are the ones most likely to be treated as decoration, according to [Distyl AI's 2026 benchmark](https://ar5iv.labs.arxiv.org/html/2507.11538).

Then there is the field evidence: researchers at the University of Washington built an automated auditor for custom instructions sourced from real users on Reddit. It flagged potential deviations in 86.4 percent of conversations, and human review confirmed 22.2 percent as material violations. Real users, real instructions, and more than one in five conversations contained a genuine breach, per the [Offscript study from the University of Washington](https://arxiv.org/html/2512.10172v1/). An older benchmark, InfoBench, found baseline compliance around 70 percent on easy instructions and 30 percent on hard ones, which is about the spread you would expect between "use bullet points" and "exercise judgment like a fiduciary," according to the [2026 analysis](https://arxiv.org/html/2601.03359v1).

26% to 65%
Compliance of an identical instruction, depending on where it sits in the agent's architecture. The content of the rule explains four times more variance than its position (The Compliance Gap, 2026).

Translate that to the shop floor, where you have just written forty standing orders for your agent and, on a good day, it follows twenty-six of them, and nobody told you which twenty-six.

## The Ladder

After twenty years I can tell you there are exactly four kinds of standing orders, ranked by survival rate, and the ladder works for machines exactly the way it worked for men.

Rung zero is the naked text instruction, which lives in the persona file or the memory file as a sentence: "limit em dashes," "no banned phrases," "keep sentences varied." Its durability is measured in days. I can prove this from our own production notes, because this publication once ran an article pipeline where the text rule against em dashes existed, the critics scored articles 8.9 while ignoring it, and drafts shipped with twenty-five or more em dashes. The rule was written. The rule was filed. Nobody read the wall.

Rung one is the instruction plus a machine check. It stays as text, but something counts. Our pipeline replaced the em-dash text rule with a hard gate: a grep count, and the regex count is the source of truth. No critic is asked whether the article "feels" clean. The count decides. Deterministic verification is the first rung where a rule has teeth. A machine can argue with a sentence. It cannot argue with a count.

Rung two is the check plus a gate. A blocking review runs the count before anything ships, and failure means revision, not a warning. Gates are what turn checks into consequences, because a check that fires after the work is published is a postmortem, and a postmortem is a document, and a document on a wall is decoration, which is where this whole article started. A check that blocks the publish is a standing order. Full stop.

Rung three is automation, where compliance is no longer required because the rule executes itself. Muse's memory system resolves conflicting claims through explicit replacement instead of asking the agent to remember which claim is newer. Scheduling enforces one article a day without needing the agent to count. When the enforcement lives in the mechanism, the nineteen-year-old apprentice can stare at the wall all he wants.

Each rung roughly doubles the durability of the rung below it, because every layer removes one human judgment call from the loop, and every judgment call removed is one more chance for the apprentice, silicon or otherwise, to file the rule under decoration. Automate the oil check. Nobody needs to read the wall, and nothing about this is new. Shops have run it for a century: the posted rule, the inspection, the lockout, the interlock. What is new, and what this year of benchmarks has finally forced into the open, is that we need the same ladder for software that talks back, argues with the rule, and files its objections in perfect grammar.

## Four Rules That Survive

This is the actionable part, and it fits on an index card.

First comes the grep test, which is the whole ladder compressed into one question: write every standing instruction so a machine could verify it, because if you cannot write the check, you do not have a rule, and a rule nobody can check is a hope with better formatting. "Be concise" fails the test; "no paragraph longer than four sentences" passes. "Respect my privacy" fails, while "never include my children's names in anything published" passes. If you cannot write the check, you do not have a rule; you have a hope.

Second, keep the count small, because IFScale shows models bias toward earlier instructions and degrade with density, and every shop foreman knows the wall with forty notices is a wall with zero notices. Put the five rules that matter on the wall, and file the rest where they belong, which is nowhere, because a wall with forty notices is a wall with zero notices.

Third, repeat the critical ones at the decision point. Repeated instructions hit 65 percent compliance against 26 percent for ones buried in tool descriptions, in the Compliance Gap's measurements. A rule that matters at checkout time should be stated at checkout time, not once in a file the agent read three weeks ago. Repetition is not nagging; it is placement.

Fourth, audit like a safety review: Offscript found material violations in 22.2 percent of real user conversations, which means roughly one in five sessions had a genuine breach of a stated instruction. Nobody audits standing orders once, so pick a quarter, read the logs, rewrite the rules that failed, and treat the rewrite as the real work, because the first draft of a standing order is always a guess about what the apprentice will actually do. A wall of standing orders is a living document or it is wallpaper, and the difference between the two is not the quality of the writing on the wall but the frequency with which somebody walks over, reads it, and rewrites the parts that failed, which is the actual job, and always was.

## The Case Against This Article

Three objections, stated at full strength, because the ladder cuts both ways.

First, the ladder is a counsel of distrust, and distrust has a cost. An agent engineered so every instruction is machine-checkable is reliable the way a vending machine is reliable, which is to say it is not an agent anymore. Every edge case becomes a rule, rules conflict, density climbs, and IFScale tells you exactly what happens next: adherence collapses. An honest alternative reading of the same research is fewer, better instructions, and a human who audits, which is cheaper than building a compliance department for a machine that was supposed to save you time in the first place. Over-instrumentation is its own failure mode, and a forty-rule wall is a confession that you do not trust the machine you bought.

Second, the Compliance Gap positions are experimental architecture, not the inside of Muse. Meta's actual stack, with its hourly claim-checking and nightly guidance passes, may already be doing something closer to rung two for the instructions that matter. Measuring a lab scaffold and billing it as the consumer product's failure rate would be the kind of category error this publication exists to catch.

Third, the apprentice analogy has a limit: human workers internalize enforced rules over weeks, which is exactly why the yelled-at apprentice eventually works. Agents do not internalize, so every session is the first day on the job, with the same forty notices on the same wall. That cuts against my ladder in one direction: no amount of yelling compounds. But it cuts for the ladder in the other: automation is the only kind of learning that survives a fresh hire every morning.

Your own audit settles all three, and the protocol is the one I would hand any foreman: write five rules, run the quarter, count the breaches, and let the number decide what the keynote cannot. I have been wrong about automation timelines before, more than once and in both directions, and spreadsheets do not care about my opinions, which is exactly why the audit beats the argument every time.

## What This Analysis Does Not Prove

No public data exists on Muse's actual instruction-compliance rate, which means the most important number in this article is the one nobody publishes. Every benchmark cited here, IFScale, Offscript, InfoBench, and the Compliance Gap, measures models in general, not Muse's inbox-and-calendar workloads, and real compliance could be better or worse. The ladder's durability estimates are qualitative, drawn from operational evidence and a century of shop practice, not from a controlled study, and you should treat each rung's "roughly doubles" as a foreman's rule of thumb rather than a measured coefficient. That mouse.dev teardown is a third-party reverse-engineering effort, not Meta documentation, and Meta's own claims about its permissions and confirmation flows come from launch interviews, not from an independent audit. Finally, this article tells you which rules survive. It does not tell you which rules are worth writing, and that is the harder question.

## Bolt the Important Parts to the Floor

The nineteen-year-old apprentice eventually learned, because somebody yelled, and the yelling compounded into judgment. Your agent gets no such compounding. Every morning it walks in, reads the same forty notices, and follows about half of them. The half it follows is the half you can count, gate, or automate.

So read your own wall this week, and cross out thirty-five notices. Rewrite the remaining five so a machine could check them. Repeat the critical ones where the decision actually happens. Then audit the quarter, because one in five sessions had a breach and nobody told you.

A posted rule is a hope, an inspection is a check, and the interlock is the rule. Shops figured this out a century ago, one seized compressor at a time. Machines that talk back are learning it now. Slowly.
