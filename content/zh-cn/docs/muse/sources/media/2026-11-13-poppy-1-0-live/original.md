来源：https://www.allthingsmuse.com/articles/poppy-personal-agent-protocol-1-0/
取文：2026-11-13，直接下载

Sierra released Poppy 1.0 on November 13. Muse now looks for Poppy first on every site it visits, every Shopify store publishes a Poppy file automatically, and more than 100 companies are now design partners.

The Personal Agent Protocol, known as Poppy, [reached version 1.0](https://sierra.ai/blog/releasing-poppy) on Thursday. Poppy is now on for everyone who uses Muse, and Muse automatically looks for Poppy first on every site it visits. Shopify has enabled Poppy for every merchant on its platform.

Poppy defines how a personal agent acting for one person connects with a company, through its business agent, website, or APIs. Sierra and Meta first announced the standard last month with design partners including Genesys, Instinct, NiCE, Rocket, Shopify, Stripe, and Walmart, a preview covered in [the October announcement of the personal agent protocol](https://www.allthingsmuse.com/articles/meta-sierra-personal-agent-protocol/).

## What Changed in Version 1.0

Version 1.0 follows five weeks of design partners testing drafts against real websites, APIs, and agents. Companies can now adopt the protocol in stages, starting with the basics and adding capabilities over time. The release refines how Poppy uses existing standards such as MCP, OpenAPI, and UCP. It expands how a company can give guidance to an agent and collect feedback from it, and it introduces extensions so industries can build on the core protocol without changing it. Shopify co-authored the commerce extension.

A company publishes a poppy.json file at its domain’s /.well-known/poppy.json path under the specification. Authentication runs through OAuth, so customers control what a personal agent can and cannot do, and can manage that access over time. Sierra published an implementation kit with a validator that companies can use to check their setup.

Any company can now implement Poppy on its own. Sixty new companies joined as design partners with this release. The total is now more than 100. The new partners include Affirm, Agoda, Cisco, Delta Air Lines, Hyatt, Intuit, Salesforce, Twilio, Wayfair, Wix, and Zoom.

## Shopify Stores Get Poppy Automatically

Shopify operates in more than 175 countries, and every Shopify store now automatically publishes a Poppy file, so merchants need no extra implementation work. Every Shopify store already supports Universal Commerce Protocol, or UCP, by default.

The two protocols handle different parts of a visit. UCP handles shopping itself, such as finding products, filling a cart, and checking out. Poppy handles what happens before that, when an agent arrives at a store, identifies itself, and learns what it is allowed to do. The commerce extension lets an agent shop as a guest or sign in with the customer’s account. It requires the agent to ask the customer before certain actions, and it connects to UCP Ask so a shopper’s agent can talk directly to a store’s agent.

## The First Live Uses

Mercury, Synchrony, and Turkish Airlines are among the partners now live with Poppy. Mercury customers can ask a personal agent to check balances, review recent transactions, categorize spending, and keep budgets and receipts up to date. A customer can also ask an agent to initiate a payment or transfer, and Mercury runs the request through the account’s approval policy before anything is sent.

Turkish Airlines lets personal agents check fares, flight status, and stopovers, and pull up a booking with a reference number and surname. Miles&Smiles members can have an agent find business class upgrades, which customers approve before paying. The airline is working on letting members complete a purchase without leaving the conversation.

Synchrony’s work is exploratory. It looks at how a personal agent could help customers find a product while considering affordability and relevant Synchrony offers and financing, with potential use across a network of more than 500,000 merchant locations.

## Why Identification Matters for Muse

Agent access has run into resistance where businesses cannot tell who an agent is or what it is allowed to do. That problem has produced outright blocks elsewhere, including [Canadian banks blocking AI agents from customer accounts](https://www.allthingsmuse.com/articles/canadian-banks-block-ai-agents-muse/) and [JPMorgan keeping outside agents out of customer accounts](https://www.allthingsmuse.com/articles/jpmorgan-blocks-ai-agents-muse-accounts/). Poppy gives a business a standard way to answer those questions before an agent acts: the agent identifies itself, the business states what is available, and the customer authorizes account access through OAuth.

The practical change for Muse users is immediate and quiet. Muse now checks for Poppy first on every site it visits, so a visit to a Shopify store or another Poppy site starts with identification and stated permissions instead of an agent browsing as an unidentified visitor.
