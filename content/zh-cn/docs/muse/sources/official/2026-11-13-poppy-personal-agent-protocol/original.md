来源：https://muse.ai/blog/poppy-personal-agent-protocol
取文：2026-11-13，直接下载

- We’re publishing the first version of the Personal Agent Protocol (“Poppy”), a standard for how personal agents work with businesses.
- Muse is the first personal agent to support Poppy, with businesses already using it to help customers shop, get answers, and manage bookings.
- Any business can implement Poppy today, starting with capabilities that work for them and adding more over time.

People are starting to hand everyday tasks to personal agents, and many of those end at a business: booking a trip, reordering groceries, returning a jacket or just getting a question answered. Businesses want to serve these customers well, and until now there hasn’t been a standard way to recognize personal agents and guide them.

The Personal Agent Protocol is designed to close that gap with an open standard for how personal agents work with businesses, whether through a website, APIs or direct conversations with their own agents. We previewed it last month, and today we’re publishing version 1.0 of the Personal Agent Protocol. Muse is the first personal agent to support Poppy.

We’re developing Poppy along with industry partners at Sierra, Genesys, NiCE, Decagon, Rocket, Shopify, Stripe, and Walmart, as well as additional design partners who have since joined the effort. Our partners bring experience across retail, payments, customer service, and more, to a shared standard that any business or personal-agent provider can build on.

Our goal is to make it easier for people to get things done with Muse and for businesses to serve those same customers.

Poppy is one of the ways that we are building the Muse network - enabling people to do more with Muse as more consumers get their own Muses and more businesses integrate with Muse.

## How to Get Started

Poppy’s technical instructions are openly available. Any business can build support via its website and any systems or APIs it already has. The [company implementation kit](https://personalagentprotocol.org/kit/company) helps teams plan, build, and test their setup.

**Publish your Poppy file and set up the capabilities you choose.** A file called `poppy.json` tells personal agents what your business offers and how to reach you: your website, your APIs or MCP server, or your own agent. A website-only setup can begin with publishing this file without adding customer sign-in. APIs, sign-in and business-agent conversations require the corresponding setup described in the kit.

**Choose, test, and expand.** Start with one customer task (for example, checking an order). Choose the capabilities and permissions to offer through your website, an existing API or your business agent. Test your setup in a test environment using the kit’s validation tool and checklist, then add more over time.

## Guide How Agents Work With Your Business

When a customer asks Muse to work with your business, you should be able to guide how that request is handled. Poppy gives you ways to direct agents and manage their access.

**Recognize real customers instead of turning them away.** Behind every Muse visit is a customer, and today, many businesses can’t easily tell a personal agent acting for a real customer apart from unwanted automated traffic, so they block both. Poppy lets you identify personal agents that use the protocol, starting with Muse, and let them through.

**Guide agents for faster, more accurate results.** Instead of leaving an agent to learn by trial and error, you can point it down the path that works best for each task. That might be your website, an API for searching or placing an order, or your own support agent for questions that need a real answer.

**One view of the customer journey.** Poppy connects their website activity, API calls and business-agent conversations within one session. You see the whole interaction rather than disconnected pieces. When a customer signs in, that activity can also be tied to their account.

**Let customers grant and manage access.** OAuth lets customers sign in on your own page and grant access without the agent handling their password in that flow. You define the permissions available, customers choose what to grant, and access can be revoked.

**Your agent stays the expert**. Muse can now talk to your support or sales agent, or hand the customer to it directly. Your agent gives your authoritative answer, and the customer never has to repeat themselves.

## What This Looks Like in Muse

The businesses below are among the first to put Poppy to work with Muse. Alongside them, many other businesses and partners are helping shape the protocol and develop ways to serve customers through personal agents. We’re excited to welcome more businesses and expand what people can get done through Muse.

- **BYLT.** Soon, Muse can talk directly with BYLT’s agent, built with Meta Business Agent, to help customers find products, ask questions, check availability, and build a cart.
- **Mercury.** Muse can connect with Mercury through Sierra to help customers manage their finances with Poppy. Mercury customers can check business and personal account balances and transactions, categorize spending, request payments or transfers, and more.\*
- **Hertz.** Muse will be able to look up, change, and extend Hertz reservations through the car rental company’s pilot with Decagon’s Personal Agent Gateway, offering renters a new way to manage their booking while delivering a seamless experience.

## An Open Standard That Will Keep Improving

Anyone can get started at [personalagentprotocol.org](https://personalagentprotocol.org/), where you can read about the protocol and find the [company implementation kit](https://personalagentprotocol.org/kit/company). Meta verified connectors will be reviewed for functional, security, and legal requirements, and complete end to end testing: apply at [platform.muse.ai](https://platform.muse.ai/) if you have an agent-ready surface like APIs/MCPs. We’ll keep developing Poppy with feedback from businesses and people using Muse.

\*Mercury is not a bank. Banking services provided through Mercury’s FDIC-insured partner banks.
