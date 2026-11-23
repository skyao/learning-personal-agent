来源：https://aihomebuilding.com/stories/muse-verify-before-trust-2026
取文：2026-11-22，直接下载

Twenty years of running operations taught me one sentence that explains most workplace disasters: the crew said it was done, and nobody checked. Nobody is lying. In their heads, the work was finished. Belief is just a terrible inspection method. That is why every trade I have ever worked with keeps a punch list, and why the foreman walks the site after the crew leaves. Trust is what you give people. Inspection is what you give work.

Your personal AI agent is a crew of one that reports its own punch list. When Muse tells you the bill is paid, the flight is booked, or the form is filed, it is reporting with complete confidence and zero accountability. In August, researchers at Princeton measured exactly how wide that gap gets. I spent this week reading their paper and the studies around it, and I will tell you plainly: the confidence is the product. Accuracy is a separate property, and it is not keeping up.

## Capability and reliability are not the same thing

A Princeton team (Rabanser, Kapoor, Kirgis, Liu, Utpala and Narayanan, ICML 2026) ran 15 models across two agent benchmarks and measured reliability as its own dimension for the first time. Not task accuracy. Reliability: consistency, meaning the agent gets the same result when you run the same task twice; robustness, meaning it degrades gracefully when conditions change; predictability, meaning it knows when it is likely to fail; and safety, meaning the outcome is survivable when it does fail. Their headline finding is a sentence every manager should tape to a wall: 24 months of rapid capability gains have produced only small improvements in reliability. Models that are substantially more accurate remain inconsistent across runs, brittle to small rewordings of the request, and often unable to tell when they are likely to succeed.

Outcome consistency, the rate at which an agent reaches the same result on the same task twice, ranged from 0.58 to 0.84 on one benchmark and 0.52 to 0.90 on the other. Read that slowly. At the bottom of the range, models hand you a different answer on nearly half of all repeated runs. Even the steadiest ones diverge on roughly one run in ten. And here is the detail that should change how you handle money tasks: on the financial benchmark, the single most common failure was agents getting a transaction wrong while sounding certain they got it right. Sounding certain is free. Being right costs effort, and the agent does not spend its own money.

## The math of long jobs

Agents fail the way relay teams fail. Every handoff is a chance to drop the baton. An analyst at WithTai worked out the arithmetic that every operations person knows in their bones: if each step of a task succeeds 95 percent of the time, a 30-step task completes cleanly only about 21 percent of the time. Thirty multiplications of 0.95 leave you at 0.21. Nearly four out of five long jobs contain at least one error.

You can run the equation backward, which is the more useful direction. Suppose you want 95 percent of ten-step tasks to come out right. Every single step has to clear 99.5 percent. Twenty steps at 90 percent end-to-end needs 99.5 percent per step too. And at 95 percent reliability per step, a task drops below a coin flip at fourteen steps. Fourteen. That is not a long request. That is "find the cheapest direct flight next month, check my calendar, hold the seat, and add the hotel." Every step was fine. Multiplication was the problem.

On a longer axis, METR's time-horizon research shows the task duration an agent can complete with roughly 50 percent reliability has been doubling about every seven months, which is genuine progress. But success on tasks longer than four hours is still under 10 percent. Capability extends how far the agent can reach. Compounding decides how often it arrives.

## How the failures actually look

UC Berkeley built the first systematic taxonomy of multi-agent failures (Cemri, Pan and colleagues, NeurIPS 2025 Spotlight): 1,642 annotated execution traces across seven production frameworks, with task failure rates ranging from 41 to 86.7 percent. Fourteen failure modes in three buckets. System design issues accounted for 44.2 percent: disobeying the task spec, repeating steps, losing track of when to stop. Misalignment between agents was 32.3 percent. Verification failures, declaring success prematurely or verifying the wrong thing, were 23.5 percent. Step repetition alone showed up in nearly 16 percent of all traces.

Note what that 44.2 percent means. Nearly half of the failures are not a smarter-model problem. They are a better-checklist problem. They proved it with interventions. In one framework, simply giving the coordinator agent unambiguous final decision authority, with no model change at all, lifted task success 9.4 points. Adding a single verification step lifted it 15.6 points. Nothing measured in this literature beats it for cheapness: one person, or one routine, asking "prove it."

Then there is the quiet kind of failure, the kind that never announces itself. A Queen's University audit of 856 real-world agent tools found that 97.1 percent of the tool descriptions had at least one significant flaw: unstated limitations, missing usage guidance, opaque parameters. It reads the description, guesses at how the tool works, and guesses wrong with full confidence. Google Research found that independent agents amplified errors by up to 17.2 times as mistakes crossed agent boundaries, while centralized coordination held that to 4.4 times. And the failure signature of the personal-agent world is the silent one: the agent reports success, every step "succeeded," and the underlying data is wrong. That error then propagates through ten downstream steps before anyone notices, because every step was measured by its status code, not by the quality of its result.

## What the enterprises already decided

A February survey of 188 enterprise AI architects found that 58.5 percent require mandatory human approval on agent work. Only 11.7 percent let agents run with no human gate at all. Stakes decide the ratio: roughly one human to eighteen agents for IT support, tightening to one to two for code generation. Cascading state errors across tool calls topped the failure list at 61.2 percent.

I am not an enterprise architect, and neither are you, probably. But notice what the people with the most money at stake have converged on. They do not trust the confident report. They budget for the inspector. One operator per two agents, on the hard jobs. You, with one agent handling your bills and bookings, are running a 1:1 ratio, which sounds luxurious until you realize you are also the operator, the inspector, and the person who pays when it goes wrong.

## The five rules

So here is the verification habit, written the way I would write it for a crew. Five rules. Laminate them if you like.

**Rule one: the invoice rule.** Never accept "done" on a money task without a receipt you did not generate. Pull up the bank statement, the booking confirmation, the carrier's own page. Financial-accuracy errors are the single most common agent failure in the benchmarks, and they arrive wearing certainty. Independent confirmation is the only confirmation.

**Rule two: the fourteen-step rule.** If your request chains more than about fourteen tool calls, your end-to-end success at typical per-step reliability is a coin flip. Break long jobs into inspectable chunks. Ask for the flight options before you ask it to book. Review the draft email before it sends. Each checkpoint resets the multiplication.

**Rule three: the verification tax.** Make the agent show its work: what it clicked, what it typed, what came back. Berkeley's result says one verification step buys 15.6 points of success. That is the best return on investment in the entire reliability literature, and it costs you thirty seconds of reading.

**Rule four: the three-bucket triage.** Failures come in three kinds, and each demands a different response. Transient failures, timeouts, rate limits, network blips, clear up on retry. Permanent failures, bad input, a missing resource, a rejected login, will fail the same way forever; retrying is theater, so fall back to a simpler method or a human. Critical failures, a budget overrun, a destructive side effect, an action outside its scope, mean save state, alert a human, and stop. Retrying a critical failure is how databases get deleted. Know which bucket you are in before you tell the agent to try again.

**Rule five: the gate goes outside the agent.** Approval gates must be enforced by the platform, not by the agent asking itself whether it should ask. NVIDIA's agent-infrastructure team states the principle as "above proposes, below decides": nothing in the stack grants itself authority. A control the agent can decline to invoke is not a control. When you set up permissions for your agent, you are not giving it suggestions. You are building the fence it cannot move.

## Inspection is the job

None of this is an argument against using the agent. I run a punch list on every job because the work matters, not because the crew is untrustworthy. Read the right way, the Berkeley finding is genuinely encouraging: the largest share of failures is fixable system design. Clear authority, a verification step, a defined stopping condition. Those are management disciplines, not model breakthroughs. They are available to you right now, on the model you already have.

Expect capability to keep climbing, and expect reliability to improve more slowly. That is what the research says. Between what it can do and what you can trust it to do unsupervised lies the permanent frontier, and you are the one who lives on it. Walk the site after the crew leaves. Check the receipts. Count the steps. It is thirty seconds of reading for fifteen points of success, and in twenty years of operations I have never found a better trade.
