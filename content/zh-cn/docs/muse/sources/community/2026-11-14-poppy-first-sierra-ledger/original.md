来源：https://museexplained.com/guide/muse-looks-for-poppy-first-sierra-poppy-1-0/
取文：2026-11-15，直接下载

Sierra published Poppy 1.0 on November 13, 2026, and said Poppy is now on for everyone who uses Muse, with Muse looking for Poppy first on every site it visits. Shopify has enabled Poppy for every merchant, and more than 100 companies are now design partners. No in-app sighting, user step, or price has been published.

## Poppy Partner Ledger

Poppy Partner Ledger

A standing box for the Poppy question, placed here so the dated answer sits next to the headline. Last updated November 14, 2026, from the two primary posts listed in Sources, both read in full.

- Confirmed on a primary, November 13, 2026: Poppy 1.0 is published. Sierra, in a post by Bret Taylor and Clay Bavor dated November 13, says Poppy is now on for everyone who uses Muse, and that Muse automatically looks for Poppy first on every site it visits. Shopify has enabled Poppy for every merchant. Muse's own blog post, also covering the November 13 release, calls Muse the first personal agent to support Poppy.
- Going live by name, in Sierra's wording: Mercury, Synchrony, and Turkish Airlines are named as design partners now going live. Sixty new companies join as design partners, for a total of more than 100. The new names Sierra lists include Affirm, Agoda, Delta Air Lines, Hyatt, Salesforce, Wix, and Zoom.
- Named by Muse, in future wording: BYLT and Hertz appear in Muse's own post, not in Sierra's live list. Muse says Muse can soon talk directly with BYLT's agent, and that Muse will be able to look up, change, and extend Hertz reservations through a pilot. Soon and will be able to are the words used. Neither is stated as live.
- Not yet shown, checked November 14, 2026: no in-app sighting of Poppy behaviour in Muse, no announcement from Mercury, Synchrony, or Turkish Airlines in its own name, and no statement from Sierra or Muse about what a Muse user has to do, pay, or connect to use Poppy. November 14 coverage found in this site's checks only restates the November 13 posts.
- Next check: partners going live in their own name, and the first in-app sighting. This site will check again when a partner publishes its own release or a dated user report appears, and will date the result either way.

## What Sierra actually published on November 13

Poppy is Sierra's short name for the Personal Agent Protocol. Sierra first announced the standard last month with an initial set of design partners: Meta, Genesys, Instinct, NiCE, Rocket, Shopify, Stripe, and Walmart. The November 13 post releases version 1.0 of the protocol, at personalagentprotocol.org, after what Sierra describes as five weeks of partners testing drafts against real websites, APIs, and agents.

The protocol itself is a set of rules for how a personal agent connects with a company that has implemented Poppy. Sierra says it gives the agent clear access to what the company offers, and that it is largely built with existing standards: MCP, OpenAPI, and UCP. Authentication runs through OAuth. In Sierra's account, customers control what a personal agent can and cannot do, and can manage that access over time.

The Muse sentence is one bullet in that post, and it deserves to be read at its exact weight. Sierra says Poppy is now on for everyone who uses Muse, Meta's AI agent, which automatically looks for Poppy first on every site it visits. That is a statement about Muse's default behaviour on sites, made by Sierra. It is not a screenshot, not a settings page, and not a user report. No source checked on November 14 shows what a Muse user sees when Muse finds a Poppy file, or what happens on a site that has none.

Sierra also says any company can now implement Poppy on its own and immediately start delivering a better experience for customers who use Muse. An implementation kit at personalagentprotocol.org walks a company through setup and includes a validator to check the work. Companies can adopt the protocol in stages, starting with the basics.

## What Muse's own post adds

Muse's blog post on the release is titled "More Ways for Muse to Work With Businesses." It frames the release as a joint one: Muse says it is publishing the first version of the Personal Agent Protocol, and that Muse is the first personal agent to support Poppy, with businesses already using it to help customers shop, get answers, and manage bookings. That first-agent claim is Muse's own wording, read in full for this post on November 14. It was snippet-level only in this site's November 13 sweep, and it is cited here at full-read weight.

The partner list in Muse's post differs from Sierra's in one name. Muse lists its industry partners as Sierra, Genesys, NiCE, Decagon, Rocket, Shopify, Stripe, and Walmart. Sierra's post names Instinct where Muse's names Decagon. Both posts were read in full, and the difference is printed here as it stands. It does not change the Muse claim, but a reader comparing the two announcements will trip over it, so it belongs in the post.

Muse's post is written for businesses, and its most concrete detail is a file name. A business publishes a file called poppy.json that tells personal agents what the business offers and how to reach it: its website, its APIs or MCP server, or its own agent. A website-only setup can begin by publishing that file, without adding customer sign-in. The post also describes what Poppy lets a business do. A business can identify a personal agent such as Muse and let it through instead of blocking it as unwanted automated traffic. It can guide the agent to the path that works best for each task. It can also let customers sign in on the business's own page and grant access through OAuth, which customers can revoke. In that flow, Muse's post says, the agent does not handle the customer's password.

One line at the end of Muse's post separates two tracks a business could confuse, Poppy support and a Meta verified connector. Muse says Meta verified connectors will be reviewed for functional, security, and legal requirements, with complete end to end testing, and directs businesses with an agent-ready surface to apply at platform.muse.ai. Poppy support and a Meta verified connector are presented as two different things in Muse's own text, and this post keeps them separate.

Field note

Two companies published posts about the same release on the same day, and they do not tell the story the same way. Sierra's post leads with reach: every Muse user, every Shopify merchant, more than 100 partners. Muse's post leads with instructions for businesses and keeps its two named examples, BYLT and Hertz, in future wording. A reader who only saw the coverage that followed, dated November 14 in this site's checks, got Sierra's version repeated. The Muse version is the more cautious document, and it is the one that describes what a business actually has to build.

## The Shopify piece, which is the largest single fact

Shopify has enabled Poppy for every merchant on its platform. That is Sierra's sentence, and the detail under it is specific. Shopify powers businesses in more than 175 countries, and every Shopify store supports the Universal Commerce Protocol, UCP, by default. Every Shopify store now automatically publishes a Poppy file, so merchants do not need to do any extra implementation.

Sierra draws a line between the two protocols, and the line is worth keeping. UCP handles the shopping itself: finding products, filling a cart, and checking out. Poppy handles what happens before that, when an agent arrives at a store, says who it is, and finds out what it is allowed to do. Shopify co-authored Poppy's commerce extension, which links the two. Under that extension, an agent can shop as a guest or sign in with the customer's account, the agent must ask the customer before taking certain actions, and the shopper's agent can talk directly to the store's agent through UCP Ask.

What this means in practice is narrower than the headline. A Shopify merchant has a Poppy file because Shopify put it there, not because the merchant chose Poppy or set anything up. What a Muse user can do at a given Shopify store today, beyond Muse looking for the file first, is not described in either primary post. No Shopify announcement of its own was found in the November 14 checks. The every-merchant claim rests on Sierra's post, checked November 14, and it is labelled that way here.

## The three named cases, read at their own weight

Sierra's post has a section on Poppy in use, and the three cases in it are not written at the same strength. Reading them as one flat list of launches would misstate the record.

Mercury gets the fullest description. Sierra says people who use Mercury for business and personal banking can now ask their personal agent to check balances, review recent transactions, categorize spending, or keep budgets and receipts up to date. A customer can also ask the agent to initiate a payment or transfer, with Mercury ensuring the request goes through the account's approval policy before anything is sent. Muse's own post covers Mercury in one line: Muse can connect with Mercury through Sierra to help customers manage their finances with Poppy. Mercury is a banking services company, not a bank; Sierra's post carries the note that banking services are provided through Mercury's FDIC-insured partner banks.

Turkish Airlines is described as live, with one piece still unfinished. Sierra says personal agents can now check fares, flight status, and stopovers, and pull up a booking with a reference number and surname. Miles&Smiles members can have an agent find business class upgrades, which customers approve before paying. The same paragraph says the airline is now working to let members complete a purchase without leaving the conversation. Read plainly, that means purchase completion inside the conversation is the part still being built.

Synchrony is the weakest of the three, despite sitting in the going live list at the top of Sierra's post. The body text says Synchrony will bring financing and rewards into agent-led shopping, and that the work explores how a personal agent could help customers find the right product while considering affordability and relevant Synchrony offers. Will bring, explores, and could are future and conditional words. Sierra puts the network at more than 500,000 merchant locations. On the body text alone, Synchrony is a partner with a direction, not a described live service, and this ledger records it that way.

Caution

Going live is Sierra's phrase, and it covers three different states in Sierra's own post: a described service at Mercury, a live service with its purchase step still in progress at Turkish Airlines, and exploratory work at Synchrony. None of the three companies had published its own announcement in the checks run on November 14, 2026. If you use one of these services and Poppy behaviour shows up in your Muse app, a dated screenshot is evidence this site will print. Until then, the live column rests on one company's post.

## What a Muse user has to do, pay, or connect

Nothing is stated. That is the honest answer, and it is the answer both primary posts support.

Sierra says Poppy is now on for everyone who uses Muse. On implies no switch is described, and neither post names a settings toggle, a connector screen step, a plan requirement, or a price. The September baseline research this site works from predates Poppy entirely, so it offers no help here, and no later source checked through November 14 fills the gap. If Poppy behaviour depends on a paid plan, neither Sierra nor Muse says so. If it works the same on the free tier, neither says that either.

The one user action either post does describe belongs to individual businesses, not to Poppy as a whole. Where a business offers sign-in, the customer signs in on that business's own page and grants access through OAuth, and can revoke it. That is a per-business permission, described by Muse for businesses setting Poppy up. It is not presented as a step a Muse user takes in the Muse app to turn Poppy on.

## What Poppy is not, on this site's record

Poppy is a third-party protocol that Muse supports. It is not a Meta model. Muse Ember, covered in this site's November 11 post, is Meta's own model, and it has nothing to do with Poppy beyond sharing a busy release week. Poppy is also not a Muse connector launch: no new connector is named in either post, and Muse's own text treats its verified connector review as a separate track.

Three standing items hold flat alongside this release, because Poppy coverage keeps pulling them in. Expedia in Muse is still hotels only on the Skift record of November 9, with flights not verified. Spaces sharing is still not live: Meta's November 6 post describes it as exploring ways to share. Muse calling businesses, published on this site on November 14, is paid and US only on its record. Poppy changes none of those rows.

## Next check, and the question for readers

The open rows in the ledger are the ones with no primary behind them: an in-app sighting, a partner announcement in the partner's own name, and any statement about user steps, plans, or price. This site will check those rows when a source gives a reason to, a partner release, a Meta follow-up post, or a dated user report, and will publish the date of the check either way.

The reader question for this post is the one the partner list raises and cannot answer itself. Which Poppy partner would you actually use first: a Shopify store, a travel partner like Delta, Turkish Airlines, Hyatt, or Agoda, or a finance partner like Mercury, Synchrony, or Affirm? Answers that name the partner and the task you would hand it will shape which of the 100-plus names this site checks first.

## Quick answers

Is Poppy on for Muse users now?

Yes, on Sierra's word. Sierra's post of November 13, 2026 says Poppy is now on for everyone who uses Muse, and that Muse automatically looks for Poppy first on every site it visits. No in-app sighting had been reported in any source checked on November 14, 2026.

What is Poppy?

Poppy is the short name for the Personal Agent Protocol, an open standard published by Sierra with industry partners, including Meta. It defines how personal agents such as Muse connect with companies through their websites, APIs, or their own agents, using OAuth for customer permission. Version 1.0 was published on November 13, 2026.

Is Muse really the first personal agent to support Poppy?

That is Muse's own claim, in its blog post "More Ways for Muse to Work With Businesses," read in full on November 14, 2026. No independent test of the claim was found in the November 14 checks.

What does Shopify enabling Poppy for every merchant mean?

Per Sierra, every Shopify store now automatically publishes a Poppy file, and merchants do not need to do any extra implementation. UCP still handles the shopping itself, such as finding products and checking out. Poppy handles the agent arriving, identifying itself, and learning what it is allowed to do. No Shopify announcement of its own was found on November 14.

Which partners are live?

Sierra names Mercury, Synchrony, and Turkish Airlines as design partners now going live. The body of Sierra's post describes a working service at Mercury, a live service at Turkish Airlines with in-conversation purchase still being built, and exploratory work at Synchrony. None of the three had published its own announcement in the November 14 checks. Muse's own post names BYLT and Hertz in future wording only.

Do I need to do anything, pay anything, or connect anything to use Poppy in Muse?

No step, price, or plan requirement is stated in either primary post. Sierra says Poppy is on for Muse users. Where a business offers sign-in, Muse's post describes the customer signing in on the business's own page and granting access through OAuth, which can be revoked.

How many companies are Poppy design partners?

More than 100 in total, per Sierra: 60 new companies joined with the 1.0 release. Sierra's list of new names includes Affirm, Agoda, Delta Air Lines, Hyatt, Salesforce, Wix, and Zoom, among others.

## Frequently Asked Questions

**Q: Is Poppy a Meta product?**

A: No. Poppy is Sierra's protocol, developed with industry partners. Meta is one of the initial design partners Sierra names, and Muse's own post says Muse is publishing version 1.0 alongside partners at Sierra and elsewhere. The two posts frame the ownership slightly differently, and both are cited in Sources. What neither post says is that Poppy is a Meta model or a Meta-only standard. Sierra says any company can implement it, and Muse says any business or personal-agent provider can build on it.

**Q: How is Poppy different from a Muse connector?**

A: On Muse's own text, they are different tracks. A connector links a specific service into Muse. Poppy is a standard a business implements on its own site, starting with a poppy.json file, so that personal agents can identify themselves and be guided to the right path. Muse's post closes by describing Meta verified connectors as a separate review, with functional, security, and legal requirements and end to end testing, and an application route at platform.muse.ai.

**Q: Why is there no screenshot of Poppy working in Muse?**

A: Because none was found. The November 14, 2026 checks looked for an in-app sighting or user report and found only restatements of the November 13 announcements, including roundups dated November 14 that trace back to Sierra's post. That absence is reported here rather than filled with a description of behaviour nobody has published. If Poppy behaviour appears in your app, a dated screenshot would settle this section.

**Q: Sierra lists Instinct as an initial partner and Muse lists Decagon. Which is right?**

A: Both lists are printed as published. Sierra's November 13 post names Meta, Genesys, Instinct, NiCE, Rocket, Shopify, Stripe, and Walmart as the initial design partners from last month. Muse's post names Sierra, Genesys, NiCE, Decagon, Rocket, Shopify, Stripe, and Walmart as industry partners. The posts were both read in full on November 14, 2026, and the one-name difference stands in the record as a difference between the two announcements. It does not affect the Muse support claim either way.

**Q: Does Poppy change what Muse can buy for me today?**

A: Nothing in either post says that, in those terms. Sierra's Shopify section describes agents shopping as a guest or signed in under the commerce extension, with the agent required to ask the customer before certain actions. Turkish Airlines is still working on letting members complete a purchase without leaving the conversation, per Sierra. A general claim that Muse can now buy across 100-plus partners would go past both sources, and this post does not make it.

**Q: When will this site check Poppy again?**

A: When a source gives a reason to: a release from Mercury, Synchrony, Turkish Airlines, Shopify, or another named partner in its own name, a follow-up post from Meta or Sierra, or a dated in-app sighting. The ledger at the top of this post will carry the new date. No recheck date is promised here, because no source has given one.

## Sources

- Sierra, "Releasing Personal Agent Protocol 1.0," November 13, 2026, by Bret Taylor and Clay Bavor, sierra.ai/blog/releasing-poppy. Read in full on November 14, 2026. Poppy 1.0 now available at personalagentprotocol.org. Poppy now on for everyone who uses Muse, with Muse automatically looking for Poppy first on every site it visits. Shopify has enabled Poppy for every merchant. Design partners going live include Mercury, Synchrony, and Turkish Airlines. Sixty new companies join, for more than 100 in total, with Affirm, Agoda, Delta Air Lines, Hyatt, Salesforce, Wix, and Zoom among the names listed. Protocol built largely with MCP, OpenAPI, and UCP, with OAuth authentication and customer control of access. Shopify detail: every store supports UCP by default and now automatically publishes a Poppy file, merchants need no extra implementation, UCP handles shopping and Poppy handles agent arrival and permissions, commerce extension co-authored by Shopify. Mercury, Synchrony, and Turkish Airlines cases as described in this post, including Synchrony's future wording and Turkish Airlines' in-conversation purchase still in progress. Initial design partners named as Meta, Genesys, Instinct, NiCE, Rocket, Shopify, Stripe, and Walmart. Mercury banking note: Mercury is not a bank, banking services provided through its FDIC-insured partner banks.
- Muse blog, "More Ways for Muse to Work With Businesses," muse.ai/blog/poppy-personal-agent-protocol. Read in full on November 14, 2026. Muse publishing the first version of the Personal Agent Protocol, Muse as the first personal agent to support Poppy, businesses already using it to help customers shop, get answers, and manage bookings. Industry partners named as Sierra, Genesys, NiCE, Decagon, Rocket, Shopify, Stripe, and Walmart. Business setup detail: poppy.json file, website-only setup without customer sign-in, staged adoption, validator in the implementation kit. OAuth sign-in on the business's own page, grant and revoke, agent does not handle the customer password in that flow. Named examples: BYLT in future wording (soon), Mercury through Sierra, Hertz in future wording (will be able to) through a pilot with Decagon's Personal Agent Gateway. Closing note: Meta verified connectors reviewed for functional, security, and legal requirements with complete end to end testing, apply at platform.muse.ai.
- DuckDuckGo checks, November 14, 2026, run for this post. Five queries on the Sierra Poppy launch, Poppy and Shopify, in-app sightings, the three named partners, and any Meta follow-through. November 14 coverage found (Eigenradar, IA News 24, EOGEE, and similar roundups) only restates Sierra's November 13 post. No in-app sighting or user report of Poppy behaviour in Muse was found. No announcement from Mercury, Synchrony, or Turkish Airlines in its own name was found. No Meta primary beyond the Muse blog post was found, and no separate Shopify announcement was found. Dates for the November 14 roundups are as shown in DuckDuckGo results; some linked pages returned errors on spot check, so those dates are snippet-level.
- Editorial checks, November 14, 2026: standing facts held flat from this site's November record. Muse Ember is Meta's own model, covered November 11, and is distinct from Poppy. Expedia in Muse hotels only, per Skift, November 9, with flights not verified. Spaces sharing described by Meta on November 6 as exploring ways to share, not live. Muse calling businesses is paid and US only on the record of this site's November 14 post. The September 2026 baseline research report predates Poppy and contains no Poppy material.
