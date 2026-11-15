来源：https://aihomebuilding.com/stories/muse-spaces-describe-once-keep-it-2026
取文：2026-11-15，直接下载

Picture a kitchen counter in December. A gift list lives there in three places at once: a note on the fridge, a spreadsheet nobody has opened since October, and a chat thread where you explained the whole thing to Muse four times, once per shopping trip, because every new conversation starts from zero. You retype the names, the budgets, and which niece already got the art set. Muse is brilliant at the list and useless at remembering it exists.

On November 6, 2026, Meta offered a different shape for that problem. In a Newsroom post titled ["Design the Muse App, Just for You,"](https://about.fb.com/news/2026/11/introducing-spaces-customize-muse-app/) the company introduced Spaces, and the definition is one sentence long: "A space is a custom experience you create inside Muse by describing your idea, like a holiday gift tracker, a daily word game, or a planning board for your next DIY project." Describe it, Muse builds it, and the thing stays where you put it. Pin it to the sidebar, move it into your main tabs, or hide it until Saturday, and schedule the work planner to sit up front on weekdays and swap in the weekend plans when the week ends.

This is the biggest interface change Muse has had since it launched on September 8, and it matters more than the voice feature that arrived the day before, because a new way to talk to an agent changes the conversation while a new place to keep the agent's work changes what the agent is for. Voice arrived the day before, on November 5, letting United States users talk to an expressive avatar instead of typing. Spaces arrived the day after, and it changes something more basic than input. A chat is a corridor you walk down once and never revisit. A space is a room. You furnish it, you leave things in it, and you come back to find them where you left them.

## Nine examples, three kinds of promise

Meta lists nine ideas in the announcement, and the pitch treats them as equal, but they are not equal: some need nothing from the outside world, some need to read your email, and one or two need to touch money and other people's data. Here is the audit nobody published, sorted by what each space actually requires.

| Meta's example space | What it needs to work | Where it can go wrong |
| --- | --- | --- |
| Trivia game, podcast studio | Nothing live: Muse already knows movies, music, and your episode notes. | Low stakes, since a wrong trivia answer costs nothing more than a shrug. |
| Gift tracker, music tracker, wedding planner, trip planner | Read access to connected apps: prices, release dates, show dates, flight and hotel details. | Stale data looks identical to fresh data, so a price that moved yesterday still shows on a tidy card. |
| School dashboard | Reads school emails, finds the events relevant to your kids, adds them to your calendar. | One misread date means a missed recital, because email is messy and a dashboard hides the mess. |
| Small-business order tracker, freelance client hub | Reads customer messages and orders, tracks invoices, deadlines, and what ships today. | Highest stakes. A misread customer message is a missed shipment, and an invoice error is real money. |

What the table makes visible is that four of the nine examples are games and planners that cannot hurt you. Three depend on background data staying fresh, which Meta promises without saying how often anything refreshes or what happens when a connection breaks. Two touch other people's money and messages, which is exactly the territory where Muse's approval gates have always been strictest. Yet the announcement says nothing about whether a Space's background updates pass through those gates at all.

## What you actually buy: an amortized instruction

Strip away the furniture metaphor and a Space is an instruction you pay for once instead of renting it forever. Count it. A gift tracker you check three times a week costs about 150 re-descriptions a year in chat, because every visit begins with reminding the agent what the list is, who is on it, and what you already bought. Each re-description is a fresh chance for the agent to misunderstand you. A Space pays the description cost once, then charges you nothing per visit.

That arithmetic is the real product, not a prettier chat but an instruction with a shelf life of months instead of minutes, bought once and used all year. Paid once. Used forever.

But the same arithmetic cuts the other way, and it is worth sitting with, because an instruction you write once and never revisit is an instruction that goes stale silently: your niece outgrows the art set, a vendor changes its invoice format, a school switches email systems, and the Space keeps showing the old version with the same calm confidence. In chat, staleness announces itself, because you re-explain the job every time and notice when the facts have moved. In a Space, staleness hides behind a screen that still looks finished. This is why the background-update promise matters so much, and why its failure modes deserve naming: a price that stops updating, a connection that quietly dies, a date that was right in October and wrong in December, all displayed with the same calm confidence.

## Eight days in, the evidence is thin by design

Meta says Spaces are available "everywhere Muse is available," starting November 6. Muse itself is live in five countries as of that week: the United States, Canada, Japan, Singapore, and Mexico. One outlet noted it could not confirm Spaces actually appearing on every account yet. Version 14.3 of the iPhone app, released November 6, describes Spaces in its release notes, which confirms iOS. Sources checked say nothing separate about Mac, the web, or Android, and nothing about Spaces inside WhatsApp.

Mark Zuckerberg, posting about the launch, said he had built three Spaces of his own, a barbecue game, an event tracker, and a home control dashboard, and it is a telling list: two of the three are toys, and the third is a dashboard for the house, which is to say a man with a smart home used the feature to watch his smart home. Nobody has published a hands-on test of a Space doing consequential work, like the order tracker or the client hub, under real load.

Meanwhile the same Newsroom post carries a second announcement that deserves a skeptical read. Meta says it is rolling out specialized versions of its models to Muse, trained with learnings from Muse Wonder, its frontier model family introduced October 12. In a separate research post the same day, Meta reported that Muse now forgets critical information 2.4 times less often, uses key context correctly in 90 percent of tasks, up from 76 percent, and scores 47 percent on Meta's Personal Superintelligence Index, up from 38 percent. Active Focus, the companion feature, supposedly delivers a 67 percent improvement in completing everyday tasks where unexpected issues arise.

Every one of those figures comes from Meta's own evaluations, published without methodology, without task counts, and without independent verification, which means the numbers describe what Meta measured about its own system on its own tests, not what any outside party has confirmed in the wild. And the most honest reading of "2.4 times less forgetting" is that forgetting still happens, just less often, which is a strange foundation for a feature whose entire pitch is "describe it once and trust it forever." A Space built on a model that forgets 10 percent of critical context is a Space you still need to check.

## The permission paragraph that is missing

Here is the gap that should bother anyone who has followed Muse since launch. The whole Spaces announcement runs under 600 words. When Muse launched on September 8, Meta published a long technical account of Sentinel, the separate system that must approve every internet-bound action, and the permission scopes a user can grant: one-time, session, task, time-bounded, or perpetual. That account exists because an agent that acts on your behalf is a security problem, and Meta knew it.

Spaces gets no such paragraph. Nothing in the announcement says what a Space may read or write, which connector scopes apply to background updates, what happens when a connection breaks, or whether a Space that reads your email in the background is approval-gated the way a chat request to read your email would be. Our own earlier reporting on this site found no published Meta rule for how long an approval stays valid or what an agent does when a time-sensitive approval expires. Spaces inherits that silence and extends it to a screen that updates while you are not looking.

A feature that reads your email in the background deserves the permission paragraph the launch got. Until it has one, the careful move is to treat a Space's background updates as a convenience you verify, not a feed you trust.

## The lock-in ledger

There is one more cost, and it is the one Meta will never put in an announcement. What you build in Muse stays in Muse. Sharing does not exist yet; Meta says only that it is exploring ways for you to share spaces with others. Export does not exist either. Nothing in the announcement mentions taking a Space out, embedding it elsewhere, or reaching it through an API.

Compare that with the chat era, when a good prompt could be copied anywhere, pasted into any tool, and carried to a competitor in seconds, while a good Space cannot leave the app it was built in at all. Every hour you spend refining a Space, every connection you wire into it, every habit you build around it, raises the cost of leaving. That is not a reason to refuse Spaces. It is a reason to build the first one deliberately, with open eyes, knowing that the room you furnish is rented, not owned.

## The case against Spaces, at full strength

Fairness demands the strongest version of the skeptical case. Spaces may be a prettier trap. Chat at least made the agent's work visible, step by step, with an audit trail you could read. A Space hides the work behind a tidy screen, and a tidy screen showing a wrong price or a missed date looks exactly like a correct one. "Describe once" is also "trust once," a demand made by a system whose own maker admits it still forgets critical context one time in ten. And the nine examples are curated to flatter the feature: a trivia game cannot fail in a way that matters, so leading with it tells you nothing about the order tracker. If Spaces mostly get used for games and gift lists while the serious tools stay in chat, where the audit trail lives, then the feature will have succeeded as a toy and failed as infrastructure, and Meta will still call it a revolution.

That case is strong, and it is not answered by enthusiasm. It is answered only by using Spaces for real work, watching them fail, and reporting the failures honestly, which is the job this site exists to do.

## What I could not verify

Honesty requires the gaps stated plainly. No hands-on test was possible for this article: no Muse account was used, so I could not confirm that Spaces appears on every account, on which platforms, or how background updates behave when a connector disconnects. All Active Memory and Active Focus figures are Meta's internal evaluations with no published methodology and no third-party testing. Pricing and plan gating for Spaces are unconfirmed; the announcement states no price and no usage limits. Which connector permissions a Space inherits, read versus write, update intervals, stale-data warnings, and failure behavior are all unstated in the sources checked. Treat this article as a reading of a launch announcement that is eight days old, not as a settled account of how Spaces behave.

## Build one Space, the right way

None of this means you should wait. It means you should start with the space that cannot hurt you and learn the tool before you trust it with money. Pick the pure-display tier from the audit: a trivia game, a music tracker, a reading list. Build it, then check it once a week for a month. Note what goes stale, what the agent misread, and how often you had to correct it. Write the shelf life into the description itself, the way you would write it into any standing instruction: "This list is valid while the prices are from this month; re-check before buying."

Then, and only then, try the school dashboard or the order tracker, with one rule attached: the Space is a draft, not a decision. Check the date against the email. Check the price against the store. Check the shipment against the customer message. Keep doing that until the Space has earned a month without a correction. A room you live in should be inspected like a room, not admired like a picture.

Muse spent its first two months as a conversation, a corridor you walked down once and never revisited, while Spaces make it a place, with rooms you furnish and return to, and that difference, between a hallway and a home, is the whole story of this launch. Places are more useful than corridors, and they are also easier to stop noticing. Furnish the first room carefully, check the wiring every week, and remember who owns the building. You are renting a room inside someone else's house. Make it comfortable, but keep the exit in mind.
