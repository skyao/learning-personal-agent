来源：https://timeline.place/guides/grok-bot-symbiosis
取文：2026-11-28，直接下载

I didn't expect to like Grok Bot.

I use agents all day in tools like Codex, T3 Code, and Amp, and they are good. But every one of them waits for me. I have to stop what I am doing, explain where I am and what I need, and type it out. I didn't think I needed a new abstraction over LLMs (especially one powered by Grok), but Grok Bot proved me wrong.

A few weeks ago I wired my phone's arrivals and departures into Grok Bot so it knows when I walk into a place and when I leave. (I build [Timeline](https://timeline.place/), an iPhone location history app, so I already had webhooks and an MCP server running on my own box, though OwnTracks, Home Assistant, or a Shortcuts script can do the same thing.)

I set it up on a Sunday afternoon mostly out of curiosity. Once the bot knew where I was and what time it was, it started handling small things on its own before I thought to ask.

## The lunch walk that changed my mind

The first couple of rules I wrote were boring: a morning summary at the office, living room lights turning on when I got home. They worked fine, and I would have turned them off inside a month.

On Friday I left the office at 12:18 to get a sandwich. Usually when I step out for lunch I forget to change my Slack status, my open branches fall behind `main` while other people merge, and some flaky test sits red until 14:00.

Five minutes down the street my phone buzzed. Timeline had sent a departure event for Work. Because it was 12:18 on a weekday, Grok Bot set my Slack status to "Out for lunch" until 13:15, rebased both of my open PRs onto `main`, and re-ran the flaky CI job. When I got back to my desk everything was green, and I hadn't opened a laptop or typed a word.

Pick a moment from Friday

12:18 · , Stepping out for a sandwich

Grok Bot: Flipped Slack to “Out for lunch” until 13:15, rebased both open PRs onto main and re-ran a flaky test. Everything’s green.

- Slack
- GitHub

One Friday. Tap a stop to see what landed on my lock screen, or didn’t.

The supermarket was where it stuck. I have never managed to keep a shopping list up to date in an app. Half the time what I need is buried in a calendar invite or a text thread from two days earlier.

On Friday afternoon I walked into the supermarket without a list. By the time I had a basket, Grok Bot had checked Saturday's calendar, saw four friends were coming over, noticed from old notes that I made pasta last time, and sent a short list for sea bass with fennel and a bottle of Vermentino. It landed on my lock screen before I got to the vegetables.

I also never log workouts in dedicated apps between sets; at most I scribble a few words on the stop later ("80 kg felt easy"). Walking into the gym now triggers Grok Bot to read that note, check my recovery in Google Health, bump bench press to 82.5 kg, and snooze Slack until I leave. Later, when I get home after 21:00, it writes the weights onto the gym stop, drops a short recap into Notion, and dims the living room lamps.

## Week one was loud enough that I almost deleted it

When I first wired the webhook up, I got greedy and forwarded every `stop.arrived` event into Grok Bot with a loose prompt ("be helpful whenever I go somewhere"). Within a day I wanted to turn the whole thing off.

A four-minute pharmacy run for ibuprofen produced a 140-word pep talk about taking care of myself during a busy week. When I ran back into my apartment at 13:15 for my headphones, it cheerfully asked if I was ready to wind down for the evening. Worse, indoor location drift at a coffee shop next to a hardware store made it dig up a three-month-old note about hallway lightbulbs while I was trying to read.

A bad answer in a chat tab is easy to ignore because you asked for it. A bad notification on your lock screen trains your thumb to swipe Grok Bot away on reflex: even a 20% false-positive rate kills the good pings along with the bad ones. An agent that narrates your movements feels like an ankle monitor with opinions.

Choose which week of instructions to show

6 pings28 silent82% quiet

Only the six moments worth interrupting for. The other 28 disappear.

09131721

Mon

Tue

Wed

Thu

Fri

Sat

Sun

A week of 34 stops from Monday to Sunday, each a dot at its time of day. 6 of them still send a message.

The same 34 stops across three weeks of instructions. Only the bright dots buzzed my phone.

I dropped "be helpful" and wrote a short list of specific routines, ending with one hard rule: if a stop does not match one of those rules with high confidence, emit nothing and do not message me.

I still forward every stop, because I want Grok Bot to recognise an unfamiliar supermarket or an airport in a city I have never saved. Pairing broad input with a strict silence default meant 28 out of 34 stops in a normal week produced zero notifications. Once the count dropped from thirty-something pings a week to five or six, I started reading them again.

## Location automations used to have no judgement

Old location automations from IFTTT and "remind me when I arrive" never stuck because there was no intelligence in the loop. They treated every place like a light switch: cross a line on a map, run the same dumb script.

If I leave the office at 12:18 on a Friday, I am going to lunch, so setting Slack and rebasing open PRs makes sense. If I walk out that same door at 18:35, I am done for the day and do not want a PR report following me onto the train. Coming home at 13:15 usually means I forgot my charger; coming home at 21:10 after the gym means the day is over.

Choose a place

08:5812:1818:35

- 08:58 · Arrived

  Morning brief: 2 Slack drafts ready, 09:30 review doc pinned.

  - Slack
  - Google Calendar
- 12:18 · Left

  Lunch autopilot: Slack set to Out for lunch, 2 PRs rebased, CI green.

  - Slack
  - GitHub
- 18:35 · Left

  Workday over. Stays quiet and leaves code alone until tomorrow.

  Stays quiet

The same coordinates at three different hours. The clock decides what the stop means.

Once there is a model in the loop with access to your notes and calendar, the odd places you would never pre-configure start working too. Walk into a bookshop on a Saturday and it can pull up the two or three titles friends mentioned in chat over the past few months. Land at an airport in a new city and it finds your hotel check-in email, checks the fastest train into town, and lists the wine bars you bookmarked in April while you wait for your bag. On the way up to my parents' driveway, it reminds me of the USB-C charger and the form I promised to bring three weeks ago.

None of that needs pre-drawn geofences. An LLM can read a plain place name, the clock, and a pile of messy notes and usually tell whether something is worth putting in front of you.

## Where I draw the line

Letting an agent wake up on its own with access to Slack, GitHub, Gmail, and your calendar is fun right up until it does something dumb while your phone is in your pocket. After a couple of near-misses in week one, I kept a few hard boundaries.

Reversible prep work is fine; outward-facing actions are not. Grok Bot can change my Slack status, draft replies to overnight messages, rebase a feature branch, log a gym session, or dim a lamp. Every one of those takes two seconds to undo if it misreads a stop. Sending an email to another person, merging to `main`, or spending money still waits for my thumb. Nobody wants a bot emailing a client on their behalf while they are buying milk.

I also stopped trying to use phone visits as smart-home switches. Battery-friendly visit detection waits a few minutes to make sure you stopped somewhere instead of sitting at a red light. Using that to unlock a front door or turn on hallway lights as you step inside leaves you standing in the dark cursing at your phone. Anything with a five-minute grace window works fine: shopping lists once you are in the aisles, CI rebases on the walk to lunch, train times at baggage claim.

The last one is keeping the raw trail off the cloud. Streaming raw GPS coordinates every thirty seconds into an AI service would feel creepy, even to me. I only let resolved stops and notes leave the phone, never raw breadcrumbs, motion samples, or photos, and I keep a plain delivery log of every event that woke the bot up. If I wonder why Grok Bot ran at 14:30, I can check the exact payload that triggered it and revoke access in one click.

## The strange part is when you turn it off

After a month, it stops feeling novel. You carry around fewer tiny background errands in your head, like remembering to change your Slack status before lunch or digging through old chats in the supermarket aisle.

I only noticed how much I leaned on it when I paused my webhooks for two days to debug a server queue. On the second evening I stood in front of the supermarket produce bins staring at a pile of lemons, annoyed that my phone had not told me what I was cooking tomorrow. The next day I walked back from lunch, sat down at my desk, and saw my Slack status had stayed green the whole time while my PR sat behind `main`.

If you want to try any of these routines or combine your own into a single setup prompt, I put an interactive walkthrough together on the [Grok Bot playbook](https://timeline.place/use-cases/grok-bot).
