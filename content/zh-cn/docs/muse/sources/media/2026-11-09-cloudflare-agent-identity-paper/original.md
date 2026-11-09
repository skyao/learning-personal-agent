来源：https://www.allthingsmuse.com/articles/cloudflare-muse-agent-identity-paper/
取文：2026-11-09，直接下载

Cloudflare's November 5 position paper argues websites bear the cost in nearly every case when an AI agent acts for a user, and proposes Web Bot Auth, rate limiting without identifiers, and a new Trusted Agent Delegation coalition to take the problem to standards bodies.

Cloudflare published a position paper on November 5 arguing that when an AI agent acts for a user, the website on the other end sees the agent, not the user, and bears the cost when something goes wrong. The paper, [“Agents aren’t humans (but they kinda are)”](https://blog.cloudflare.com/trusted-agent-delegation) by Bryan Becker, names Meta’s Muse and OpenAI’s dots as its examples of the personal agents now doing this work. It proposes a set of identity standards and a new coalition, Trusted Agent Delegation, to take the problems to standards bodies.

The paper’s core claim is that agents are intermediaries, and the web’s old answers for intermediaries no longer work. A site used to be able to block intermediary traffic and require users to disable the service. Cloudflare argues that stops working once most traffic is agentic, and agentic traffic is growing fast enough that it may eclipse traditional human browsing in the near future.

## Fourteen Problems, One Bill

The paper lists 14 challenges that agents create for websites, and concludes that in nearly every one, the site bears the primary cost. It illustrates the problem with a fictional personal assistant named Ezra, who runs errands for four clients. The corner grocer used to know each client and their preferences; now only Ezra comes in, and the grocer cannot tell whose order is whose. When one client disputes a purchase Ezra made, the store has to prove the client asked for it, but the only person the store ever saw was Ezra.

The same pattern, the paper argues, now plays out with AI agents. A bank sees login attempts from an agent holding a list of passwords and can only ban the agent, which also blocks every legitimate user behind it. A shop that cannot tell whether a purchase was authorized absorbs the dispute. A publisher whose article is summarized by an agent gets no visit and no ad impression. Agents also poll constantly, hit expensive endpoints, and burn through free trials and promotions, because they never tire and never face the friction that limits human users.

## What Cloudflare Proposes

The paper rests on what it calls the Intermediation Principle: the business relationship between users and sites, and each participant’s security responsibilities, must be upheld regardless of intermediation. From that, it proposes a four-level scale of user identity, from nothing, through session and account identifiers, to a unique per-user identifier for high-risk actions, and favors Web Bot Auth as the way for an agent to sign its requests so a site can verify which operator it comes from.

It also calls for rate limiting that works without user identifiers, through a scheme called MOLE, and for a machine-readable way for sites to state what agents may do, on the grounds that robots.txt was not built for the job. The Trusted Agent Delegation coalition would take these problems to standards bodies, including the IETF, although the paper names no members, dates, or governance for it.

Three controls are already live for Cloudflare customers: analytics that break out personal assistants as their own traffic category, per-agent access policies that can block an agent only on pages carrying ads, and Account Abuse Protection in early access, which shows whether a personal agent made a login or sign-up request. Cloudflare sells bot management, so its diagnosis and its product line point the same way, a point [PPC Land](https://ppc.land/cloudflare-says-websites-pay-for-ai-agents-as-metas-muse-learns-to-talk/) noted in its account of the paper.

## Why Muse Is the Test Case

Muse is the agent most sites actually see. HUMAN, the bot-detection company, [found in late September](https://ppc.land/metas-muse-accounts-for-72-of-ai-agent-requests-human-finds/) that Muse accounted for an average of 72% of daily AI-agent requests on its network, running at 5.2 times the volume of ChatGPT Agent, with 84% of Muse requests targeting product and search pages. DataDome’s third-quarter report put Muse at 33% of agentic browser requests in September despite measuring it for only nine days of the month.

The identity question is already live for Muse. Fingerprint said last week that its detection can now [flag traffic it infers to be Muse](https://www.allthingsmuse.com/articles/fingerprint-detects-undeclared-muse-traffic/) on a major bank’s login flows, and DataDome found Meta has been quietly [signing some Muse web requests with Web Bot Auth](https://www.allthingsmuse.com/articles/meta-muse-web-bot-auth-signed-requests/) since around October 12, the same standard Cloudflare prefers. Meanwhile, sites have been answering the same uncertainty with blocks: 37 of 51 large retailers checked in one audit blocked agents by accident through old anti-bot rules, and Canada’s biggest banks [moved within days of each other](https://www.allthingsmuse.com/articles/canadian-banks-block-ai-agents-muse/) to block agents from customer accounts.

## What’s Next

Cloudflare says it will hold side meetings at the IETF and workshops to move the coalition’s work forward, and invites operators, identity companies, payment providers, merchants, and publishers to take part.
