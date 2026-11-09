来源：https://www.allthingsmuse.com/articles/datadome-muse-29-million-requests/
取文：2026-11-09，直接下载

DataDome's Q3 2026 traffic report shows Meta's Muse reaching 33% of September's agentic browser volume, with 99.3% of its requests arriving from cloud

Meta’s Muse generated 29.1 million web requests in its first 12 days of full availability, according to a [report released Thursday by bot-management firm DataDome](https://datadome.co/threat-research/ai-traffic-report-q3-2026/). The volume made Muse one of the largest sources of agentic browser traffic DataDome measured in September, just weeks after the agent’s launch.

Muse accounted for 33% of all agentic browser traffic in September, DataDome found, despite being fully available only from September 22. In September alone, Muse generated 19.5 million requests, about 1.9 times the volume of Claude’s browser extension. DataDome’s Muse figures cover September 22 through October 3, and the firm notes that detection covering only the last nine days of September makes its September numbers a lower bound.

The report, DataDome’s AI Traffic Report for the third quarter of 2026, draws on traffic across the company’s network from July through September. Agents are shifting from reading web pages to acting on them, a change that affects site operators deciding which automated visitors to allow.

## Cloud traffic, not user devices

Beyond volume, what sets Muse apart in DataDome’s data is origin. In a sample of Muse traffic, 99.3% of requests came from cloud and content-delivery infrastructure: Cloudflare accounted for 81.2% and Fastly for 18.1%. Only 0.6%, about 17,500 requests, came from consumer internet providers, spread across eight networks.

That pattern follows from how Muse is built. DataDome notes that Muse is a personal AI agent operating inside its own dedicated cloud virtual machine, which contains a full browser, to complete multi-step tasks on a user’s behalf. A consumer feature therefore shows up on a site’s network as infrastructure traffic, and device or home-IP signals will not separate Muse from other cloud-hosted traffic.

Muse also does not identify itself as an AI agent in its traffic, DataDome says. Site operators cannot rely on a bot name or user-agent string to spot it.

JPMorgan won't let outside AI agents like Muse operate inside customer accounts](https://www.allthingsmuse.com/articles/jpmorgan-blocks-ai-agents-muse-accounts/)

## Agents are reaching forms and checkout

The same sample shows what Muse does once it arrives. Of Muse requests, 8.9% touched sensitive flows: roughly 202,600 form requests, 24,800 login requests, 9,600 payment requests, 6,800 account-creation requests, and 5,200 cart requests. Forms accounted for 81% of that sensitive traffic and ran about eight times higher than logins. DataDome reads that as Muse reaching past browsing and reading into forms and checkout, while mostly acting logged out rather than signing in as the user.

Muse’s volume grew fast. Daily requests rose 4.4 times in nine days, from 800,000 on September 22 to 3.7 million on October 1, roughly 18% growth per day. The peak was 484,000 requests in a single two-hour window on October 3. Volume followed a clear daily cycle, rising from 08:00 UTC and peaking at 16:00 UTC, consistent with traffic following user activity rather than a scheduled crawl.

The broader category is growing with it. Agentic browser traffic jumped 4.7 times in September, from 12.5 million to 58.2 million requests. Even without Muse, volume tripled to 38.7 million. ChatGPT’s cloud browser grew 4.5 times to 27.4 million September requests, making it the largest agentic browser at 47% of volume, while Claude’s extension nearly tripled to 10.5 million. Perplexity’s Comet fell 65% from July to September. Across all AI agent traffic, DataDome’s network processed nearly 25 billion requests in the third quarter, up 41.5% from 17.7 billion in the second quarter.

## Why It Matters

DataDome’s central warning is that policies built around residential or ISP-based traffic will not catch agents like Muse. A site that trusts traffic because it looks like it comes from ordinary infrastructure, or that blocks bots only by user-agent string, has no reliable way to tell Muse’s requests from other cloud traffic, even though a real user’s task sits behind them.

The traffic is landing on the parts of a site that carry fraud and abuse risk. Forms, logins, payments, account creation, and carts are where a mistaken allow decision costs the most, and Muse is already operating there at scale. Site operators now have to decide what AI agents are permitted to do once they arrive.

The finding lands days after [JPMorgan said it would not let outside AI agents like Muse operate inside customer accounts](https://www.allthingsmuse.com/articles/jpmorgan-blocks-ai-agents-muse-accounts/), citing risk to clients and the bank. JPMorgan’s answer was to block. DataDome’s advice is more granular: classify agents by function rather than vendor, set explicit rules for what agents can do on forms, login, account creation, cart, and checkout, validate agent identity beyond the user-agent string, and review policies every quarter as rankings and bot names shift.

DataDome’s figures cover its own network, not the whole web, and its Muse sample reflects the first days of a new product. Still, agents are moving from reading content to acting on sites, and the traffic that carries them no longer looks like a bot or like a person. It looks like cloud infrastructure, because that is where it comes from.
