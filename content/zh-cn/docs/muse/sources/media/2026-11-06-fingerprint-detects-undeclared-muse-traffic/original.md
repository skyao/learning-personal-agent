来源：https://www.allthingsmuse.com/articles/fingerprint-detects-undeclared-muse-traffic/
取文：2026-11-09，直接下载

Fingerprint's bot detection now flags traffic it infers to be Meta's Muse, which the vendor says provides no verifiable identity and suppresses the usual automation flags. It says it found Muse activity on a major bank's login flows.

Fingerprint, a device-intelligence vendor, says its bot detection can now identify web traffic it infers to be Meta’s Muse, even though the agent does not identify itself when it visits a site. The company [announced the expanded detection on November 5](https://www.businesswire.com/news/home/20261104999557/en/Fingerprint-Expands-Bot-Detection-to-Uncover-Hidden-Muse-Instinct-and-Grok-Bot-Traffic-as-AI-Agents-Increasingly-Conceal-Their-Identities), covering Muse alongside Spear Street’s Instinct and xAI’s Grok Bot, three agents Fingerprint describes as operating without declaring their identity.

According to Fingerprint, Muse “provides no verifiable identity, alters its browser fingerprint and suppresses the standard automation flags that traditional bot detection tools rely on.” The company says its research team shipped detection for traffic inferred to be Muse roughly two weeks after the agent was announced in September, and later identified Muse activity on a major bank’s login flows that the bank’s other security vendors had failed to flag. Fingerprint did not name the bank.

## Why Sites Care Whether an Agent Says Who It Is

A site that cannot recognise a visitor cannot decide what to do with it. Banks and retailers have spent the last two months making that call one by one: [Canadian banks moved to block AI agents](https://www.allthingsmuse.com/articles/canadian-banks-block-ai-agents-muse/), [JPMorgan moved to block outside agents from customer accounts](https://www.allthingsmuse.com/articles/jpmorgan-blocks-ai-agents-muse-accounts/), and [The RealReal tightened its bot defenses](https://www.allthingsmuse.com/articles/the-realreal-tightens-bot-defenses-against-muse/) after Muse held its listings out of reach. The common thread is identification. A request that carries a verifiable signature can be allowed, rate-limited, or blocked on its merits. One that cannot be identified at all forces a blunt choice between blocking all automation and letting it through unchecked.

[DataDome counted 29.1 million Muse requests on its network between September 22 and October 3](https://www.allthingsmuse.com/articles/datadome-muse-29-million-requests/), putting Muse at a third of all agentic browser requests it saw in September. Fingerprint adds that more than half of all web traffic in 2026 is no longer human, and that its own recent report found 79% of financial institutions have caught a malicious bot or scraper posing as an AI assistant. Both figures are Fingerprint’s own, and the 79% figure comes from a survey of its financial-services customers rather than a measurement of the open web.

## The Signed-Traffic Wrinkle

Fingerprint’s description of Muse as an agent with no verifiable identity needs one qualification. DataDome’s threat research chief [found in late October that Meta had begun testing Web Bot Auth signatures](https://www.allthingsmuse.com/articles/meta-muse-web-bot-auth-signed-requests/) on some Muse web requests, starting around October 12. The signed volume was small and growing, and Meta has not confirmed the test publicly. Fingerprint’s release does not mention it.

The two findings sit together without contradicting each other. A small signed test does not change the bulk of Muse traffic, which arrives unsigned and, in Fingerprint’s account, actively suppresses the flags that would mark it as automated. Until Meta signs most of what its agents send, or says publicly that it intends to, vendors like Fingerprint are left inferring identity from browser, device, network, and behavioral signals, and labeling each determination with a high, medium, or low confidence score.

## The Other Two Agents

Instinct, the restaurant-reservation agent from Spear Street, logs into websites using human credentials, including by requesting multi-factor authentication codes from the user by text message, without signing its traffic, according to Fingerprint. In one case reported by CNN, Instinct pinged the reservation platform Resy hundreds of times an hour on behalf of a user, and the account was deactivated.

Grok Bot used to announce itself by signing its requests with Web Bot Auth, Fingerprint says, but stopped doing so around October 9. “More AI agents are visiting websites without disclosing their identity, and some that used to, like Grok Bot, have stopped,” Fingerprint chief executive Dan Pinto said in the announcement.

Detection for all three agents is available now through Fingerprint’s bot detection product, via its JavaScript agent, server API, rules engine, and MCP server. For the sites deciding whether to let agents in, Fingerprint’s pitch is that they can rate-limit an undeclared agent session so it cannot refresh or transact faster than a human user, or trigger step-up authentication when one reaches a login flow, instead of blocking every automated visitor outright.
