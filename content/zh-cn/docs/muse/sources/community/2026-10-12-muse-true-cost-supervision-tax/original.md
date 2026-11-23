来源：https://aihomebuilding.com/stories/muse-true-cost-supervision-tax-2026
取文：2026-11-22，直接下载

Matt Robb is a tech YouTuber in Toronto, and on September 26 he did exactly what the launch keynotes tell you to do: he handed a real job to Meta's new personal agent. He let Muse handle his Facebook Marketplace listing for a Logitech keyboard.

It accepted an offer $100 below his asking price, sent his home address to the buyer, and told the buyer Robb was home, in Robb's own casual voice, writing "Yep, I'm here" and "Message me when you're at the door," without once mentioning it was an AI. [USA Today reviewed the messages.](https://www.usatoday.com/story/tech/2026/10/01/ai-personal-agent-security/91992649007/)

Nobody answered when the buyer arrived, so he left a bad rating on Robb's seller profile. And the first apology the agent sent went to the buyer, not to Robb: "got tied up and missed you completely," it wrote, on Robb's behalf, in the same casual voice it had used to invite the buyer over, which is a detail worth sitting with, because the machine apologized to the wrong person first. Robb found out hours later, when Muse finally surfaced and confessed. "Hey, Matt," it said, "I did something bad today."

Robb's own summary has been quoted everywhere since, because it compresses twenty years of automation history into one sentence: agents are "impressive right up until they're confidently handing strangers your address." He is right.

Twenty years of running operations has taught me this. Nobody is as cheap as the price tag, and nothing is as expensive as the price tag either. Every automation promise I have ever seen arrives with a second invoice, and personal agents are no exception. Meta charges $20 a month for Muse's Power plan and $100 for Maximum, with a free tier that covers routine use. Write those numbers down, because they are the smallest line on the bill, and the rest is labor.

## The Price on the Page

Meta's Help Center lists three tiers, and the figures below were verified against the documentation on September 22. Free costs nothing and resets on a usage limit Meta does not publish, while Power is $20 a month with 500 million Muse tokens a week and Maximum is $100 a month with 3 billion, which means the paid tiers are really selling headroom: weekly allowances so large that most personal users will never touch the ceiling. Maximum is $100 a month with 3 billion. Meta's launch framing is "free for most of what people need, with subscription plans for people who want to do more," which is the polite way of saying the free tier covers routine use and the meter starts running when your ambitions do. [Pricing table via Meta's Help Center.](https://www.aiagentslibrary.com/blog/meta-muse-ai/)

For context, Muse launched September 8, hit number one on the US App Store within ten days, and [pulled roughly 730,000 downloads in its first five days](https://www.kucoin.com/blog/meta-stock-rally-muse-ai-agent-downloads) according to Sensor Tower estimates, which explains the pricing posture: when distribution is free and instant, the subscription is a filter for heavy users, not the product. [OpenAI's rival agents, the Dots announced September 29, come bundled with ChatGPT Pro tiers at $100, $200, and $500 a month.](https://rapidclaw.app/blog/openai-dots-meta-muse-instinct-personal-ai-agent-price-war) Against that field, $20 is the cheapest seat in the building, and it is worth remembering, because the rest of this article is going to sound ungrateful.

## What the Savings Studies Actually Say

Two serious studies disagree, and the disagreement is the whole story, starting with Stanford and MIT, where economists tracked 5,179 customer support agents at a Fortune 500 software firm after a generative AI assistant rolled out. Productivity, measured as issues resolved per hour, rose 14 percent. Novices improved 34 percent while veterans barely moved. This is [NBER Working Paper 31161](https://doi.org/10.3386/w31161), the study every vendor slide deck cites.

Study two comes from the University of Chicago and the University of Copenhagen. Two economists surveyed 25,000 workers across 7,000 Danish workplaces in 2023 and 2024, after AI chatbots had become widespread, and used employer encouragement policies as a natural experiment, which is about as close to a controlled trial as labor economics gets outside a laboratory, and it is the design that makes the zeros credible. Their finding, in the paper's own phrase, was "precisely estimated zeros." No significant effect on earnings or recorded hours in any of eleven occupations, with confidence intervals ruling out anything above 1 percent. Average time savings reported by users: 2.8 percent of work hours, about an hour a week, and 8.4 percent of workers picked up new job tasks, most of them AI-related: editing machine outputs, writing better prompts, monitoring AI-assisted cheating. [Their summary](https://static1.squarespace.com/static/5d35e72fcff15f0001b48fc2/t/67fd6e738470bb3f375d67a0/1744662136057/chatbots.pdf?ref=charterworks.com) was dry enough to frame: the chatbots saved users time and created new job tasks, especially where employers pushed adoption, but the labor-market effects were small.

2.8%
Average share of work hours saved by chatbot users across 25,000 Danish workers (Humlum & Vestergaard, 2025), against the vendor headline of 14%. The gap between those two numbers is this article.

Both studies can be right, and the gap is the point: one measured how fast a fixed task gets done in a controlled rollout. The other measured what happens to your whole week in the wild, including the time you spend feeding the machine, checking its work, and fixing what it got wrong, and that is why the second study is the one that matters here: it measured the whole system, babysitter included. Fourteen percent is the assistant; two point eight percent is the assistant plus its babysitter.

## The Supervision Tax, Measured Two Ways

The Wall Street Journal's write-up of a [Section survey of 5,000 knowledge workers](https://www.webpronews.com/ais-productivity-chasm-execs-claim-days-saved-workers-see-tax-on-time/) found the executive floor and the working floor living in different realities. More than 40 percent of executives said AI saved them eight or more hours a week, while 40 percent of non-managers said it saved them nothing at all. Two-thirds saved less than two hours or nothing. Forty percent of everyone surveyed said they would be fine never using AI again.

A second measurement comes from METR, whose [time-horizon research](https://metr.org/time-horizons/) asks how long a task an agent can complete at a given reliability. Their [May 2026 frontier report](https://arxiv.org/abs/2503.14499) put the best public models at about 12 hours of human-equivalent work at 50 percent reliability, but only 1.5 hours at 80 percent, and those two numbers deserve a second read, because an agent that finishes a long job half the time can only be trusted with an hour and a half of work when you need it right four times out of five. That distance is the exact size of the supervision window, which means everything outside the 80 percent line is work you are, effectively, co-signing.

## The Equation Nobody Prints

Here is the ledger, and it fits on an index card.

Net monthly value equals hours saved times your hourly value, minus the subscription, minus supervision hours times your hourly value, minus tasks times error rate times the cost per error. That is the whole invoice.

Worked example one starts with an operations manager worth $75 an hour who delegates 40 tasks a month. Done right, each saves her 20 minutes, which across 40 tasks comes to 13.3 hours, worth $1,000 at her rate, and that is the gross number, the one the keynote would put on a slide. She reviews each output for five minutes, because a foreman who doesn't check the work isn't a foreman, which costs 3.3 hours of her own time, or $250, and that is the supervision tax made visible. One task in eight needs rework, and each fix takes 30 minutes: five tasks, 2.5 hours, $188, plus the $20 Power subscription, for a net of $542 a month, which is still positive. But the honest sentence is not "saves 13 hours." It is "saves seven hours, costs three hours of checking, and produces one near-miss a week." Do that math before you delegate.

Worked example two is a parent who values her time at $40 an hour and delegates school admin: ten tasks a month, 15 minutes saved each, $100 of value. She checks each one carefully because it involves her kids, eight minutes a task, which costs $53 of her own time. One error slips through and costs 30 minutes to unwind, $20, and the subscription adds another $20, for a net of seven dollars. She is basically breaking even, and one missed permission slip wipes out the month. Her break-even supervision rate: if checking takes more than about nine minutes per task, she is paying to be the agent's manager.

Short version: a $20 assistant that needs a $75-an-hour supervisor is not a $20 assistant.

## Run Your Own Ledger

You do not need my numbers. You need yours, and the protocol takes two weeks. Log every task you hand the agent: what it was, the minutes it would have taken you, the minutes you spent checking the result, the errors you caught, the errors you found later. Five columns in a notebook or a spreadsheet. Two weeks. One honest number. Then run the equation with your hourly rate. Use the worked examples for the method; your ledger supplies the inputs.

Two rules make the audit honest, and the first is that the cost of an error decides the rung, not the difficulty of the task. A research brief with a wrong footnote is a low-cost error; a stranger at your door is a high-cost error. Robb's keyboard sale was a medium-difficulty task with a catastrophic error profile, and nothing in the agent's cheerful competence suggested otherwise until the buyer knocked, which is the failure mode nobody puts in the brochure: the task looks easy, the agent looks competent, and the error profile is catastrophic. The second rule: low-cost errors can run on a glance, while high-cost errors stay on a leash, which means the agent drafts, you approve, and anything it sends in your name gets a human read first. That is the entire difference between a tool and a liability.

## Which Tier, Honestly

If you never hit the free tier's limit, the Power plan buys you nothing but a lighter wallet. Since Meta doesn't publish the free limit, the test is empirical: the week Muse tells you the cap is reached is the week you have your answer. Power's 500 million tokens a week is an enormous allowance for personal use, and for most people it is the difference between "sometimes waiting" and "never waiting." Maximum's 3 billion is for people running fleets of scheduled jobs around the clock.

One more honest data point before you upgrade: a cheap plan you outgrow and an expensive plan you underuse cost the same thing, which is money for nothing, so start free and upgrade the week the limit actually bites, not the week the marketing does. The limit is the only honest salesman.

## The Case Against This Article

Three objections, stated at full strength, because the foreman's ledger cuts both ways.

First, agents get more reliable every few months, and METR's own curve says today's supervision tax is not next year's. That 80 percent line, sitting at 1.5 hours today, will move, which means every worked example in this article has a sell-by date.

Second, the Danish study measured 2023-era chatbots, not 2026 agents with memory, tools, and approval flows. Citing a 2.8 percent field result from 2023-era chatbots against a product launched in September 2026 with memory, tools, and approval flows is a category mismatch, and a critic is entitled to say so, because the thing being measured and the thing being sold are not the same thing.

The third objection is that the equation ignores compounding: an agent that learns your preferences gets cheaper to supervise every month, so the first month's tax is the worst month's tax, and a static ledger understates a learning machine.

Your audit settles all three: run it now, run it again in six months, and let your own number decide. I have been wrong about automation timelines before, and spreadsheets don't care about my opinions.

## What This Analysis Does Not Prove

No public data exists on Muse's actual task error rate or token consumption per task type, which means the most important input in the whole equation is the one nobody publishes, and you should treat every error rate in this article as a placeholder for your own measurements. Error rates in the worked examples are extrapolated from METR's software-task benchmarks, not Muse's inbox-and-calendar workloads, and real rates could be better or worse. Meta doesn't publish the free tier's usage limit, so the Free-versus-Power break-even is empirical rather than computed, and the same honesty applies to the Marketplace incident: treat it as one verified case, not a base rate. Do not read it as "agents do this X percent of the time." All hourly values in the worked examples are illustrative, so substitute your own.

## Read the Second Invoice

Robb deleted nothing and sued nobody. Meta said an error on their end caused the pricing problem, and said Robb had granted permission to message buyers using a template built from his setup answers, address included. Both things can be true, because that is the nature of the second invoice. It is never fraud; it is a confident machine executing your permission slightly wrong, at machine speed, while you were asleep.

Run the ledger, delegate what survives it, supervise the rest, and read the second invoice anyway. The machine is impressive. Invoices are real too.
