来源：https://www.allthingsmuse.com/articles/agent-blocking-guide/
取文：2026-11-08，直接下载

Banks and retailers are shutting AI agents like Meta's Muse out of accounts and checkouts, but most retail blocks are accidents of old anti-bot rules. Here is who is blocking, what agents can still do, and what authorized access should look like.

Banks say agents cannot touch customer money. Retailers say agents cannot check out. An audit of 51 large American retailers found that most of the blocking was never decided at all.

## The Banks Drew the First Lines

[JPMorgan Chase](/articles/jpmorgan-blocks-ai-agents-muse-accounts/), the largest bank in the United States, moved first. Chief executive Jamie Dimon told analysts on the bank’s third-quarter earnings call on October 13 that the bank would not let “just any … outside agent” operate inside its systems. A spokeswoman confirmed the bank blocks external agents from taking actions for retail customers, though balances stay visible through authorized Plaid and open-banking connectors. Sending money, paying bills, or taking any action inside an account is off limits.

[Charles Schwab](/articles/charles-schwab-blocks-muse-client-money/) followed days later. Chief executive Rick Wurster told Bloomberg TV that Schwab blocks major outside agents, including Muse, from moving client money, and that the firm stops “tens and twenties” of attempts each week. Schwab is not cutting outside AI off entirely: the brokerage plans to connect external models through its own Model Context Protocol servers, with firm-set authentication rules, for balance checks and research, but nothing that moves money.

Canada’s biggest banks then moved in step. Royal Bank of Canada acted first, telling employees on October 27 that it would block third-party personal AI agents from online banking and other authenticated properties, in a memo calling agents an “unacceptable customer risk.” Toronto-Dominion, Bank of Montreal, Scotiabank, and CIBC followed within a day; National Bank of Canada said it is monitoring the issue. The full sequence, bank by bank, is in [our account of the Canadian banks’ move](/articles/canadian-banks-block-ai-agents-muse/).

## The Retailers That Said No on Purpose

Amazon blocked Muse from shopping on its site in September, saying the agent’s access was inconsistent with its customers’ terms of use, and citing security and privacy concerns about agents handling customer credentials. Amazon later asked Meta to remove Amazon from the Muse shopping experience, CNBC reported, and chief executive [Andy Jassy told investors](/articles/amazon-jassy-shopping-agents-not-great/) on the October 29 earnings call that outside shopping agents are “still not great.” Amazon runs its own shopping agent, Alexa for Shopping, while blocking others.

Kohl’s and Neiman Marcus are the other two retailers CNBC names as explicitly restricting agents, in [an audit of 51 large American retailers by Billions Network, an identity-verification company, that CNBC reported on November 1](/articles/banks-retailers-block-ai-agents-cnbc-audit/). The audit found five retailers that explicitly restrict agents; CNBC names three of them. The Wall Street Journal, summarized by Gizmodo, reports Tapestry and Kohl’s refuse to let agents complete purchases and Chewy and Neiman Marcus block some agents. Delta does not let agents buy tickets, [according to TechCrunch’s reporting](/articles/muse-websites-blocking-agents/).

## What a Blocked Agent Can Still Do, and What It Cannot

Every institution in this guide draws the same line: looking is allowed, acting is not. A blocked agent can check a balance through an authorized connector, research products, and browse, but it cannot move money, send money, pay a bill, execute a transaction, or complete a purchase. At Schwab, agents can see balances and do research through the firm’s own channels, and only the institution acts. JPMorgan draws the same line through Plaid. Across the 51 retailers in the Billions Network audit, none had a verified route for an agent to complete a purchase at all.

## Most Retail Blocks Are Accidents

Of the 51 large American retailers whose published access rules Billions Network examined, 37 block shopping agents largely by accident, through older bot rules written to stop scrapers and automated traffic rather than through an explicit AI-agent policy. Only 11 of the 51 had taken an explicit position on AI agents at all. Evin McMullen, Billions Network’s co-founder and chief executive, told CNBC that most of the retailers in the audit have not made a decision about AI agents at all.

Human-verification checks, the “click to prove you’re human” buttons that protect sites from spam, can fail an agent mid-checkout and boot it from the transaction. Walmart told TechCrunch its blocks of Muse were not intentional: the company is partnered with Muse. Agents are also hard to spot: [Cequence found](/articles/cequence-muse-agent-traffic-identity-study/) that Muse does not identify itself in its traffic, and [DataDome found](/articles/datadome-muse-29-million-requests/) that 99.3% of Muse requests in its sample came from cloud infrastructure, so a site blocking bots only by user-agent string cannot reliably tell a Muse request from other cloud traffic.

The audit reads published rules, not proof of technical enforcement: a published restriction does not by itself prove how completely agents are blocked in practice.

## What Authorized Access Should Look Like

McMullen’s answer is a verification method so legitimate agents can be identified, rather than blanket bot blocks that catch agents and scrapers alike. Michael Abbott, Accenture’s global banking lead, told CNBC that banks and retailers that try to block agents risk losing customers who want agent-assisted shopping and banking, and should instead develop secure ways for authorized agents to interact with them.

Cequence chief executive Ameya Talwalkar put the middle path in one sentence: “Blocking agents outright will turn customers away, and letting them all through is a risk most security teams can’t defend.” His firm’s answer is Agent Trust, which verifies an agent’s identity against trusted issuer registries and applies policies request by request. DataDome’s advice runs the same way: classify agents by function rather than vendor, set explicit rules for forms, logins, carts, and checkout, and validate identity beyond the user-agent string.

Working models already exist. Schwab’s Model Context Protocol servers put the firm in charge of authentication while letting outside agents read balances and research. Walmart works with OpenAI and others on agent shopping through approved routes, and it is letting users create dedicated agent profiles so purchases made by AI agents stay separate. Meta’s answer is the open agent-to-agent standard it is developing with Sierra and partners including Walmart, Stripe, and Shopify. Even JPMorgan says through a spokeswoman that it supports secure data sharing through open-banking providers and is committed to enabling agentic connections securely.

One number shows how far there is to go: zero of the 51 retailers in the audit offers a verified way for an agent to complete a purchase.
