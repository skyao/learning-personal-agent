来源：https://aihomebuilding.com/stories/muse-agent-texts-you-first-2026.html
取文：2026-11-17，直接下载

Your phone buzzes at 7:42 in the morning. It is on the nightstand, screen up, the way you left it. You reach for it half-asleep, expecting a person, and find a suggestion instead. Muse noticed a recipe reel you saved last week and turned it into a grocery list. It is thoughtful, and it is also, in the most literal sense, a machine that decided what you should think about before coffee.

That reversal, who addresses whom first, is the entire design problem of the personal agent era, and everything else is plumbing.

## The oldest promise in personal computing

Every assistant since 2014 has promised to be proactive, and the demos always looked the same: software anticipating your needs, surfacing the right thing at the right moment, a life that runs itself. What the demos flattened, every time, was the question of interruption, because being anticipated is lovely in a keynote while being interrupted is a tax, and nobody in those keynotes ever showed the bill.

Muse is the most aggressive attempt yet by a mass-market agent to combine the capability with the surfaces needed to make good on the old promise at scale. [Meta's own help documentation](https://www.meta.com/help/artificial-intelligence/1484325780075655/) describes one-time and location-based reminders ("get a message at a specific date and time or when near a specific location"), recurring scheduled tasks ("you'll receive a message each time the task is due"), and an Upcoming tab where every scheduled item lives. Beyond scheduling, the launch brief says Muse "proactively helps people meet their goals and suggests ideas," keeps working after you close the app, and "comes back when something changes." You talk to it in the Muse app or in WhatsApp, [as if messaging another person](https://www.pymnts.com/facebook-meta/2026/meta-targets-mass-market-automation-with-new-muse-ai-agent/). With Active Memory, announced October 12, it now brings up details from earlier conversations "when they matter."

Notice the direction of every verb in that paragraph: reminds, suggests, comes back, brings up. The agent speaks first now, and nobody has designed the manners for that.

## The proactivity ladder

It helps to name the rungs, because the etiquette question is different on each one.

**Rung one is reactive.** You ask, it answers; the manners here are settled (be accurate, be fast, don't hallucinate), and every chatbot lives on this rung.

**Rung two is scheduled delivery.** You asked earlier and it delivers later: a 9 AM reminder, a Monday timesheet nudge, a ping when you drive past the grocery store. Because the interruption was pre-authorized, its moral character is completely different, and this is the rung Meta has designed best: the help docs give you plain-language setup, an inventory in the Upcoming tab, and cancellation in a sentence.

**Rung three is proactive notification,** where the agent initiates: it saw the recipe reel, so here is a grocery list; it read your email, so here is a reminder you never asked for. [Meta's description](https://builtin.com/articles/meta-muse) is explicit about this tier: Muse can "anticipate a user's needs and act accordingly without any prior guidance," sending reminders based on email content and suggesting purchases from past patterns. Nothing was pre-authorized here; the agent decided this was worth your attention.

**Rung four is proactive action:** the agent does not message you at all, it acts, and you find out later, or never. This rung barely exists in consumer agents yet, which is exactly why the etiquette conversation needs to happen now, while the norms are still wet cement.

Most of the industry's design energy has gone into rungs one and two. Rungs three and four are where relationships get made or broken, and they are where the current controls are thinnest.

## The price of a ping

Here is the calculation nobody has run for personal agents. Gloria Mark's research group at UC Irvine studied what interruptions actually cost knowledge workers: interrupted work was resumed the same day about 82 percent of the time, taking on average 23 minutes and 15 seconds, and workers touched roughly two other tasks before finding their way back. Mark herself has said "there's a cognitive cost to an interruption," and the mechanism is reorientation: new windows open, the desk rearranges itself, the thread of thought has to be rewound.

A note on that number, because rigor matters more than rhetoric: the widely quoted 23:15 comes from Mark's interviews about the work, while the published CHI 2005 paper reports 25 minutes 26 seconds of elapsed time before resumption, and both figures measure when people returned to the task, not when they regained full cognitive depth. During the interval, workers were completing other tasks, not staring at the wall. So treat the number as the cost of a displaced attention cycle, not dead time. Use 23.25 minutes per ping as the working figure below, with that caveat attached.

Six proactive pings a day, each triggering one resumption cycle: 6 x 23.25 minutes = 139.5 minutes, call it 2.3 hours of displaced attention daily. Now batch those six into a single morning digest: one cycle, about 23 minutes. The difference, roughly 1.9 hours a day, is the entire economic argument for digest-style delivery over scattered pings, and it falls straight out of research on notification timing: Shamsi Iqbal and Brian Bailey showed that deferring notifications to natural breakpoints, the pauses between subtasks, measurably reduced frustration and reaction time compared with delivering them immediately. UX researcher Jakob Nielsen, [summarizing recent studies of proactive AI](https://jakobnielsenphd.substack.com/p/ux-roundup-20261002), lands the design principle in one line: proactive AI "should speak first, softly, and be easy to ignore," with user-controlled dials, and "an interruption is a withdrawal from the user's attention, and the balance is smaller than you think."

~1.9 hours
Estimated daily attention saved by batching six proactive agent pings into one digest, using Mark's resumption figures (6 x 23.25 min vs. 1 x 23.25 min). Assumptions: each ping interrupts focused work; the digest is read once. Reality will vary; the direction won't.

Those inputs are doing honest work here. Not every ping interrupts deep work. Some arrive at natural breakpoints and cost nearly nothing. Some pings prevent larger interruptions later, a reminder that saves a missed flight is worth a hundred resumption cycles. The math is a ceiling, not a measurement. But ceilings are useful: they tell you what the design has to beat.

## What bad manners look like

We have a preview of the failure mode, and it is not hypothetical. Owners of electric vehicles with built-in AI assistants [report systems that proactively suggest actions](https://ai.itbrief.co/posts/ai-in-evs-are-smart-assistants-becoming-too-annoying/), changing driving modes or adjusting climate, "often without user initiation or explicit consent." The complaints stack up in a familiar shape: too talkative, too frequent, too hard to customize, an "always on" presence that forces the driver to adapt to the software instead of the reverse. Substitute "calendar and inbox" for "climate control" and you have the exact failure pattern waiting for personal agents that ship rung-three behavior with rung-one manners.

A sharper version of the problem is wrongness. A proactive suggestion built on misremembered context is not a minor annoyance; a grocery list from a misread recipe is funny, but a reminder built on a misread email, or a suggestion that misstates someone's dietary restriction, carries real cost. Active Memory makes the agent more helpful and simultaneously raises the stakes of every proactive ping, because confidence and correctness are not the same thing.

There is also a security dimension worth one paragraph, not more. A proactive agent with broad permissions is a larger attack surface: security researcher Patrick Wardle [reported a macOS vulnerability](https://rocketnews.com/2026/10/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day-6/) in which locally installed software could reach Muse authentication tokens, partly because voice transcription was routed through Meta's cloud rather than handled on-device. That design question, who gets to speak first, has a security twin: who gets to listen.

## The other side of the argument

Now the strongest case against everything above, stated at full strength: proactivity is the entire point, and an agent that never speaks first is a chatbot with a calendar, and we already have those; nobody needed a dedicated virtual machine and a Sentinel security agent to build a faster search box. Rung three matters most to people who are not power users optimizing their mornings: caregivers tracking medication schedules, people managing chronic conditions, anyone drowning in logistics they did not choose. For them, an agent that notices what they didn't ask about is not an interruption; it is relief.

And the off-switch exists: every scheduled task can be cancelled in plain language, and the Upcoming tab shows the full inventory. So the design problem is calibration, not elimination: the right default is not silence, it is graduated, user-controlled proactivity with the dials in the user's hand. Nielsen's studies point the same way: satisfaction with proactive AI averaged 8.2 out of 10 and climbed over the week, when the AI spoke softly and was easy to ignore. People do not hate being helped; they hate being unable to say not now.

## What this accounting leaves out

Honesty requires the ledger of what was not proven. Meta publishes no data on how often Muse's proactive suggestions fire, what fraction users accept, or how suggestion volume changes with more connected data, so the six-pings-a-day figure is illustrative, not measured. Mark's interruption research comes from office-work contexts, not agent-notification contexts, and the 23:15 figure is contested even within her own publications, as noted above. This ladder is a taxonomy, not a tested model; whether users actually experience rungs two and three as morally different is an empirical question nobody has run. And the Wardle vulnerability is cited from secondary reporting, without independent verification.

## A short etiquette for the interim

Until the industry writes the real manners, here is what you can do with the controls that exist today.

## Calibrating your agent's manners

1. **Audit the inventory.** Ask Muse "what reminders do I have?" and open the Upcoming tab. Most people are surprised by what is scheduled, and you cannot calibrate what you cannot see.
2. **Keep rung two generous, rung three on a short leash.** Scheduled delivery you authorized is cheap; proactive suggestions are expensive until the agent has demonstrated a hit rate, so let it earn rung three.
3. **Demand batching.** One morning digest beats six scattered pings; the math above says the difference is worth about 1.9 hours of your attention a day. If a surface won't batch, it doesn't get proactive privileges.
4. **Start with location reminders.** "Remind me when I'm near the store" is the highest-value proactive surface Meta offers and the lowest-interruption one: it fires exactly when the information is actionable.
5. **Test the off-switch before you need it** by cancelling something by voice, then checking the Upcoming tab to confirm it is actually gone; trust the control, not the promise.
6. **Never grant rung four what you haven't audited.** Proactive action without notification should require explicit, narrow, revocable permission, the way financial transactions do. If an agent can act silently, the silence should be your choice.

Meanwhile, the industry is already writing the machine-readable version of this etiquette. Meta and Sierra's Personal Agent Protocol, [introduced October 6](https://chatmaxima.com/blog/meta-muse-ai-agent-businesses-whatsapp-messenger/), standardizes how agents identify themselves to businesses and what they are allowed to do. The human-readable version, the one that governs the 7:42 AM buzz on your nightstand, is still blank.

That blankness is the opportunity, because the norms for proactive agents are being set right now, in shipping defaults and help-center paragraphs, by companies whose business model rewards engagement. An agent that texts first is not a tool you use; it is a relationship you manage. Relationships need manners, and manners, unlike software, are much harder to patch after they calcify. Wet cement dries. Design them now, while the cement is wet.
