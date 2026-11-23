来源：https://aihomebuilding.com/stories/muse-who-pays-when-your-agent-fails-2026
取文：2026-11-22，直接下载

Jake Moffatt's grandmother died in November 2022. He went to Air Canada's website and asked the chatbot about bereavement fares, the way a grieving person asks anything in those first days, quickly, trusting the answer because there is no energy left for doubt. Its answer was clear: he could book a full-fare ticket and claim the bereavement discount retroactively, within 90 days of the ticket being issued. He booked, he flew, and then the airline told him the policy did not exist: no retroactive claims, ever.

Moffatt took it to the British Columbia Civil Resolution Tribunal. And this is the part worth reading twice, because Air Canada's lawyers stood up and argued, with professional seriousness, that the chatbot was a separate legal entity responsible for its own actions: the machine did it, not us.

On February 14, 2024, in *Moffatt v Air Canada*, 2024 BCCRT 149, Tribunal Member Christopher Rivers called that a remarkable submission and ruled it should be obvious that Air Canada is responsible for everything on its website, chatbot or not: negligent misrepresentation, CA$812.02, comprising $650.88 in damages, $36.14 in interest, and $125 in tribunal fees. [Read the tribunal's full reasoning.](https://www.dww.com/articles/bc-tribunal-finds-air-canada-liable-for-inaccurate-advice-given-by-website-chatbot?amp)

Small dollars, enormous principle: the first known ruling anywhere holding a company liable for what its AI said, and the "AI did it" defense died in a small-claims courtroom in British Columbia. Precedent, priced at CA$812.02.

That was their bot; this story is about yours.

## The Clause You Signed

Meta's terms of service for Muse, the personal agent that has been downloaded some 3.4 million times since its September 8 launch, contain a section most of those users will never read: Section 7, User Representations and Warranties, which has you warrant full legal authority over every account you connect and every person the agent contacts, plus every necessary permission and consent. And then Section 7.4, User Responsibility, lands the sentence that matters: you are solely responsible for the instructions, goals, and guidance you provide, and solely responsible for the actions Muse takes or directs in furtherance of those instructions, "whether they are a result of precise instructions, an identified goal, general guidance or otherwise." [It is all there in Meta's own terms.](https://Muse.ai/terms) Section 7.6 goes further, requiring meaningful human oversight of everything the agent does, with approval workflows for state-changing actions, and assigning full legal responsibility for the results as if you had taken them yourself. Read it twice.

Read the tail of that clause, "general guidance or otherwise": you told it to handle the returns and it accepted store credit instead of a refund, which is yours, and you told it to negotiate the cable bill and it agreed to a two-year contract, which is yours too. Meta's help page says it plainer than the lawyers do: "You're responsible for all transactions your Muse makes on your behalf. Keep an eye out for email confirmations, receipts and statements." [Moneywise flagged the clause weeks after launch.](https://moneywise.com/news/top-stories/meta-muse-ai-assistant-privacy-purchase-responsibility)

Notice the asymmetry: when Air Canada's bot lied, the airline paid, because the bot spoke for the company, and when your agent errs, you pay, because the terms say the agent speaks for you. In both stories, the person on the other end of the screen absorbs the cost; only the name on the receipt changes.

## The $500 Tell

Meta knows the pure version of this story does not hold, which is why the launch coverage contains a quieter mechanism that the keynote never mentioned: insured purchase protection, underwritten through Cover Genius and XCover, with premiums paid by Stripe Link, covering up to $500 per claim for transaction errors. It mirrors the protections credit card networks built over decades. A refund guarantee for when the agent gets it wrong.

That $500 cap is the tell: if user liability were airtight, if "solely responsible" meant what it says in every case, no insurer would need to be in the loop. Insurance is a confession. It exists because Meta's own lawyers understand what the marketing does not say: some agent mistakes will land on Meta anyway, in chargebacks, in regulators' inboxes, in courtrooms, and a capped insurance product is cheaper than finding out where the line is, [as Forkast's comparison of the three launch-week liability models documents](https://forkast.news/three-agent-products-went-live-this-week-each-disclaims-liability-differently-none-has-a-federal-rulebook/).

Meta is not alone in the disclaim-everything posture. OpenAI's rival agent terms put the user on the hook for "all risk of financial loss" and cap the company's liability at $250 or a year's fees, whichever is greater. Apple's Siri AI terms, updated September 9, contain no agent-specific liability framework at all. Target rewrote its terms in March to hold customers fully responsible for purchases its AI shopping agent makes, even when the agent misreads intent. Across the industry, the pattern is unmistakable, and it runs across every agent launch this fall: ship the autonomy, keep the liability with the person who clicked agree, and let the terms of service do the work that customer support used to do. [A comparative review of assistant policies documents the pattern.](https://github.com/dpawlan/ai-assistant-benchmark/blob/HEAD/data/articles/comparing-privacy-policies-of-ai-assistants.md)

$500
The per-claim cap on Muse's insured purchase protection (Cover Genius/XCover, premiums paid by Stripe Link). Everything above that line, the terms say, is yours.

## The Map Nobody Drew

So here is the liability map, drawn cleanly for the first time, because nobody in the launch coverage bothered.

Bucket one: their bot speaks, they pay, as Moffatt proved, because a company that puts a chatbot in front of customers owns what it says and "the AI did it" is not a defense, settled at least once in law.

Bucket two: your agent acts, you pay, because Section 7.4 says you granted the permissions, you set the goals, and the receipt has your name on it. Federal law backs the logic from the other direction: under the E-SIGN Act, a contract cannot be denied legal effect merely because an electronic agent helped form it, so long as the agent's act is attributable to the person being bound. "The AI did it" does not get you out of the transaction. [For the full E-SIGN walkthrough, see the USA Herald's analysis.](https://usaherald.com/metas-muse-ai-agent-can-act-for-you-but-the-legal-risk-may-still-be-yours/)

Bucket three is the disputed middle, and it is where the real fights will happen. Picture the scenario *The Conversation* laid out this summer: you tell your agent to find a shirt for under $30, explicitly not to buy it, and it buys it anyway. You dispute the charge: the retailer shows the order came through your account, the agent provider shows your instruction said not to buy, and the payment service shows the charge. Every record is accurate, yet nothing links the charge to the scope of the task. Three companies, three true stories, no chain of evidence connecting your words to the machine's act, [and that attribution gap is the whole ballgame](https://www.stuff.co.za/2026/08/14/an-ai-agent-spent-your-money-can-anyone-prove-you-authorised-it/).

Senator Warner's AI AGENT Act, S. 5051, introduced in July, tries to close it by defining a "custodial user agent" and directing NIST to build standards for proving who authorized what, with auditable records as the mechanism, but it is not law, nothing at the federal level is, and the gap is open water.

## The Permission Paradox

Now the part nobody puts in the keynote. Every permission you grant the agent is a liability transfer from Meta to you. Inbox access, calendar, payment methods, the authority to message people in your voice: each toggle moves risk off the company's ledger and onto yours. As the agent grows more useful, more of its mistakes become yours. Usefulness and liability grow together, and the setup flow that makes the agent powerful is the same flow that makes you the guarantor, which means the onboarding screens are quietly the most consequential legal documents you will sign this year.

Muse keeps an audit trail of what it did and plans to do. Meta presents this as transparency, but in a dispute, that trail is also the evidence that you authorized the action, timestamped, in your own words. Your receipt and the prosecution's exhibit are the same document. Every toggle is a signature.

## The Law Is Moving, Unevenly

Two weeks ago, on October 1, Connecticut's AI Responsibility and Transparency Act took effect. Its headline doctrine: using an automated system is not a defense against a discrimination claim. If the tool produces a discriminatory outcome, the employer is liable whether or not a human reviewed the output. Enforcement sits with the state attorney general; employers filing mass-layoff notices must now say whether AI played a role, and [the compliance breakdowns are already circulating](https://www.aipolicydesk.com/blog/connecticut-cart-act-october-2026-aedt-warn-enterprise).

What matters more than the coverage is the direction: Connecticut's "AI is not a defense" rule targets employers and hiring tech, not your personal agent, but the principle is migrating, because the machine does not absorb responsibility just by being a machine. Somebody with a name and assets is always on the hook, and right now, for personal agents, that somebody is you.

## The Case Against This Article

Stated at full strength, because the other side deserves it.

Meta's terms are a contract of adhesion: nobody reads them, nobody negotiates them, and courts have a long record of refusing to enforce one-sided disclaimers when the product was defective or the supervision demanded of the user was impractical in the first place. A clause that makes you "solely responsible" for actions taken on "general guidance or otherwise" may not survive contact with a judge who asks what supervision was actually possible at 2 a.m. while you slept.

That $500 of insurance is Meta's own concession, because you do not buy insurance against risks you are certain someone else bears. And the regulators are walking the other way: Connecticut, Warner's bill, the slow churn of liability debates in Brussels all point toward a future where more agent risk sits with the companies that build the agents, not the people who click through their terms. This article's "you pay" framing has a sell-by date, and it might be shorter than anyone at Meta admits.

Both things are true at once: today the receipt is in your name, and tomorrow is being negotiated in statehouses.

## What This Investigation Does Not Prove

No American court has ruled on personal-agent liability. Moffatt is a Canadian small-claims tribunal decision about a corporate chatbot, persuasive but not binding, and a different fact pattern from an agent acting on your own accounts. Quoted terms were live as of October 15, 2026, and terms change. This is journalism, not legal advice, and no attorney was interviewed on the record for this piece. Connecticut's "AI is not a defense" provisions target employment technology; applying the principle to personal agents is inference, labeled as such. Amex's reported agent-purchase coverage is single-sourced, so treat the viral agent-spend horror stories circulating on social media as unverified until a second source confirms them.

## Delegate Like the Receipt Is Yours, Because It Is

Practical rules, from the map above.

Rank tasks by the cost of being wrong, not the difficulty of the task, because those are different axes and the agent's confidence tells you nothing about which one you are on. A research brief with a bad footnote is cheap. A stranger at your door, a contract in your name, a payment from your account: expensive. Its cheerful competence looks identical in both cases. That is the failure mode nobody prints in the brochure.

Keep irreversible actions on a leash: anything the agent sends in your name, anything it buys, anything it agrees to gets human approval every time, and then read the confirmation email yourself. That $500 insurance cap is real money, but it is a ceiling, not a safety net.

Grant permissions like you are handing keys to a temp on day one, because legally that is close to what you are doing. Start narrow. Widen only after the agent has earned it with a clean record. And keep the audit trail switched on: if bucket three ever becomes your dispute, those logs are the only evidence that exists.

Moffatt won because the bot was not his. Your agent is yours. Act like the receipt says what it says.
