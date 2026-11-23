来源：https://aihomebuilding.com/stories/muse-where-sites-block-your-agent-2026
取文：2026-11-22，直接下载

Here is a stunt a human would get bored doing in twenty minutes.

Picture this: the Verge took Meta's Muse, gave it a The RealReal listing for a designer bag, and told it to keep the item in the cart. On The RealReal, anything sitting in your cart is on hold for twenty minutes, unavailable to everyone else. So the agent did what an agent does: when the hold expired, it re-added the item. When it expired again, it re-added it again. For hours. A human would get tired. An agent, in the Verge's words, "does not care."

The RealReal cared. On October 26, its CTO told the Verge the company had updated its bot defenses, and that the new configuration makes it "much more difficult for all agents to log in, add items to cart, and check out." Another door, closed. And just like that, The RealReal joined a blocklist that is growing almost daily, and it is the one thing you should know before you hand your shopping to an AI agent.

## Blocklist status: this week

Amazon went first. On September 20, twelve days after Meta launched Muse, Amazon started blocking it. Amazon told reporters that Meta never disclosed the agent would be browsing its store, and that Muse was not identifying itself as an AI while it shopped. One reviewer watched Muse try Amazon for camping gear and get, in the reviewer's words, "roundly blocked, complete with a spicy message about AI agents violating terms of service."

Then came the rest. Yelp will only admit agents that pay for its data-licensing program. Delta will not let third-party agents buy tickets. JPMorgan Chase and Charles Schwab drew a line around customer money. Schwab's CEO told Bloomberg TV on October 16 that the bank stops dozens of AI agent attempts to reach client accounts every single week, and he named Muse specifically. JPMorgan's CEO said the same thing on the bank's earnings call three days earlier.

Retailers followed. Per the Wall Street Journal, Tapestry, which owns Coach and Kate Spade, and Kohl's refuse to let AI agents complete purchases. Chewy and Neiman Marcus block some agents. Users report Adidas sites turning Muse away. Newest name on the list, as of this week: The RealReal.

Put it together and you get the Jefferies number, which is the most important number in this whole story. Jefferies tested Muse against several hundred major US shopping, airline, travel, hotel, and reservation sites. About one-third blocked the agent outright. Another third challenged or restricted it. Only one-third were easy to navigate. And Jefferies added the line that should end the debate: "new restrictions were appearing almost daily."

## What it actually looks like when the door is closed

I love this part, because the failure mode is so polite. Muse does not announce that it cannot do its job. It just does a smaller job and hopes you don't notice.

Tom's Guide asked Muse for the cheapest copy of a Batman hardcover. It came back with a winner: $74.99, new, in stock, 40% off list. Buried eight words deep at the end of its answer was the sentence that changed everything: "and Amazon wouldn't cooperate with the automated check." The reviewer bought the $74.99 copy anyway. But read it again: the price comparison that made the recommendation was missing the biggest bookstore on the planet, and the agent mentioned it the way you would mention rain in a forecast.

An independent reviewer at firstfrost.news ran the same experiment this month with Sony WH-1000XM6 headphones. Asked Muse and ChatGPT for the lowest US price right now. Both agents skipped Amazon. Neither said so until asked directly. Then came the part I find genuinely wild: asked point-blank for a list of the stores it cannot shop, Muse replied, "I don't have a list of other blocked stores to share." Your agent cannot see the doors. It cannot even list the doors it cannot see.

A separate hands-on test of eleven Muse tasks on a real free account, published at metamuseai.site, hit the same wall. Amazon price check: Muse reported that Amazon had blocked its browsing, refused to solve the bot check, and suggested other retailers. To its credit, it stopped to ask before sending an email, with an approval prompt offering Allow, Always allow for this recipient, or Deny. Denying worked cleanly. The agent is not reckless. It is just working a beat that keeps shrinking.

## Why the stores are doing this

Three reasons, all honest.

Money. Amazon makes a fortune on sponsored listings, and a sponsored listing only pays when a human scrolls past it and clicks. An agent does not scroll. It goes straight to the best match. As one analysis put it, an AI shopper skips the sponsored placement entirely, which deletes the revenue the whole marketplace is built on. Amazon, meanwhile, is happy to sell you its own shopping agent, Alexa for Shopping.

Abuse. The RealReal story is the template. A 20-minute cart hold is a feature when humans use it, because humans have better things to do than re-add a bag for six hours. An agent has nothing better to do. It is awake at 3 AM, it never gets bored, and it can hold inventory hostage indefinitely. One afternoon was all it took the Verge to prove it. Every retailer with a cart hold, a flash sale, or a limited drop just did the same math.

Credentials. Banks are not worried about shopping. They are worried about passwords. "We don't want someone just giving their password to Muse, and letting Muse come in and take action on that client's behalf," is how the Schwab framing goes. Dozens of attempts a week, blocked at the door. Meta's answer is that Muse never sees your passwords or payment methods, that credentials live in separate secure storage, and that a watchdog program called Sentinel approves everything the agent does before it touches the internet. So far, the banks are not convinced.

## Meta's side of the argument

Give Meta its due. The company says blocking the agent punishes the customer, not the robot: "Turning away a personal agent means turning away the customer behind it." And it has receipts for the other side of the ledger. Muse has live partnerships with Walmart, Best Buy, Gap, Sephora, and Wayfair, plus a Shopify default that turns on Meta checkout for eligible stores. When the agent works, it works through front doors that are held open, not windows that are pried.

The company also says shopping is the most common Muse use case so far, with average purchases over $200, and that 10 million people in the US downloaded the app in its first 40 days. That is a lot of people handing a very young product a lot of money. The blocks, from this angle, are not a verdict on Muse. They are a negotiation about who gets to be the intermediary between you and the store.

## The one stat that decides everything

Jefferies said it plainly: "website access, rather than model quality," is the thing holding these agents back. Sit with that for a second. It means the race everyone is watching, whose model is smarter, is not the race that matters right now. The bottleneck is doors.

And the doors are a moving target. One-third blocked, one-third restricted, one-third open, with new restrictions "appearing almost daily." That means a task Muse could do last month might fail this month, silently, with a smaller job and a hope you don't notice. The Tom's Guide Batman story is what that failure looks like in the wild: a confident recommendation built on an incomplete map, with the gap disclosed in eight words at the end.

This is the honest version of the personal-agent pitch. Muse is a genuinely useful errand-runner on a free plan, as long as you check its work. It handled research, reminders, and a recurring background check without fuss in independent testing, and it asks before sending or buying. But a price comparison is only as good as the list of stores, and that list now changes daily, and your agent will not volunteer what it skipped.

## What to actually do about it

Four rules, from the evidence.

First, treat every agent price comparison as a partial list. If Amazon, Delta, or your bank would obviously be in the comparison, check them yourself. The agent will not tell you they were missing unless you ask.

Second, ask the direct question: "Which stores did you check?" The firstfrost test shows Muse answers honestly when pressed. Make pressing a habit.

Third, keep purchase approvals on. Meta says the agent always asks before completing a purchase or sending an email, and independent testing confirms the approval prompt works, including the deny path. That gate is the difference between a blocked agent and an expensive mistake.

Fourth, learn the partner list. Walmart, Best Buy, Gap, Sephora, Wayfair, and Shopify-powered stores are the doors held open today. If most of your shopping lives at Amazon or the blockers, the agent is not your shopper yet. It is a researcher with a clipboard and a shrinking map.

## What this article did not prove

Limits in the open. This article is built on The Verge's original reporting (the October 17 blocklist story and the October 26 RealReal story, read directly), the aiweekly.co and notebookcheck.net summaries of the Oct 16-17 Bloomberg and earnings-call statements, firstfrost.news's hands-on tests and Jefferies figures via Proactive, the metamuseai.site 11-test review on a real free-plan account, and kaupr.io and bitcomme.com reporting citing the Wall Street Journal on additional retailers. We did not test Muse against Amazon ourselves, because the blocks are documented by people who did. We did not verify the uncorroborated social-media claim of a Muse-for-Mac zero-day, and we do not present it as fact. The Jefferies "one-third" figures come via Proactive's report on the bank's note, not from the note itself. If Amazon or the banks change policy, or Meta signs a major new partner, the blocklist in this article changes, and we will update it.

An agent that can go anywhere is a fantasy. An agent that can go somewhere specific, with permission, and tells you honestly where it cannot go, that is a tool. Muse is halfway there. The half it is missing is the honesty about the map.

*Sources: The Verge, "The RealReal won't let AI agents hog designer clothing," Mia Sato, Oct 26, 2026, via [theverge.com](https://www.theverge.com/news/1018713/meta-muse-agentic-shopping-ai-the-realreal) (read directly); The Verge's Oct 17, 2026 blocklist reporting via [AI Weekly](https://aiweekly.co/alerts/amazon-yelp-delta-join-banks-blocking-third-party-ai-agents) and [Notebookcheck](https://www.notebookcheck.net/US-banks-and-Amazon-are-blocking-AI-agents-like-Meta-s-Muse.1427833.0.html); Jefferies figures and hands-on price tests via [firstfrost.news](https://firstfrost.news/p/lowest-price-some-exclusions-apply); 11-test hands-on review via [metamuseai.site](https://metamuseai.site/muse/review/); retailer expansions and WSJ citations via [kaupr.io](https://www.kaupr.io/en/news/online-stores-are-shutting-the-door-on-metas-shopping-agent) and [Bitcomme](https://bitcomme.com/online-shopping-platforms-turn-against-third-party-ai-agents/).*
