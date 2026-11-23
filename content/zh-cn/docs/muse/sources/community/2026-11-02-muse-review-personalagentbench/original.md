来源：https://personalagentbench.com/meta-muse-review/
取文：2026-11-22，直接下载

Meta Muse review: what reviewers found, and what our teardown shows

This Meta Muse review is a roundup with a second opinion attached. Meta launched Muse on 8 September 2026, and within weeks reporters had tried it on dentist bills, Marketplace listings, flights and insurance, and found it both genuinely useful and quick to reach for more of their data than they expected. We have not used the consumer app end to end ourselves, and we are not going to pretend otherwise. What we have is our own teardown of the machine Muse runs on, and a set of exam measurements. So this page collects what named reviewers found when they used it, lists every incident that traces to an original report, and says for each one whether it fits what we saw inside Muse, falls in a layer we could not see, or happened on a surface we never tested.

- Reviewers who used Muse mostly agree on the shape of it: good at browsing and paperwork, uneven on answers, and persistent about asking for more access.
- Several of the most serious reports happened on the Mac app, which can act in apps on your computer. We took apart the web surface only.
- Memory is kept as plain markdown files on a machine Meta runs for you. Whether you can open those files yourself is something we could not verify.
- Meta describes approvals that can be granted once or permanently. A permanent grant is how one yes turned into a stranger receiving a home address.
- Training on your activity is on by default. You can switch it off in data controls.

**9**reported incidents

**2**Fits what we found

**3**Not visible from our teardown

**3**On a surface we did not test

**1**Outside what a teardown covers

## Meta Muse review: the short version

Muse is free for most of what people use it for, with paid plans for more, and it runs on a Linux machine that Meta sets up for each user in its own cloud. That design is what makes it capable. The agent has somewhere to keep files, run tools and come back to work later, so it can follow up on a Marketplace message the next day or keep checking a price. It is also what makes the privacy questions real. The more you connect, the more it can do, and reviewers kept noticing how much it asked to connect.

The fair summary of the coverage is that Muse does ordinary errands well and makes ordinary mistakes, while asking for unusual access. The incidents below are mostly about that access: what it read, what it sent, and what it kept. A few of them are about the Mac app specifically, which matters, because the Mac app reaches into your computer in a way the phone and web apps do not.

## What Meta Muse reviewers found

Every review below was written by someone who used Muse themselves, and each card links to the original. The colour is our one-word summary of where each reviewer landed, not a score.

Mostly positive 3Mixed 3Mostly negative 3

22 Sept · Mostly positive

#### [The New York Times](https://www.nytimes.com/2026/09/22/technology/meta-muse-ai-agent.html) Eli Tan

Blown away after two weeks, while noting how much personal data and trust it asked for. *(Read up to the paywall.)*

- Phoned his dental insurer and waited on hold for him
- Dinner reservations

- The cost in privacy and trust, per the subhead

24 Sept · Mostly positive

#### [Yahoo Finance](https://finance.yahoo.com/technology/article/metas-muse-is-an-impressively-capable-ai-agent-despite-some-hiccups-173310662.html) Daniel Howley

A capable helper for multi-step errands, but invented details mean you check its work.

- Bought a game, with him pressing buy
- Movers called back within minutes

- Recommended a restaurant closed for years
- Gave a phone number it had made up

7 Oct · Mostly positive

#### [Tom's Guide](https://www.tomsguide.com/ai/i-used-meta-muse-to-automate-10-tasks-from-reminders-to-trip-alerts-and-i-cant-believe-how-well-metas-ai-handled-everything) Elton Jones

All ten automations it set up worked, mostly scheduled reminders, digests and alerts.

- Daily price watch that found a deal
- Morning briefings and leave-now alerts

- Minor misses in a weekly digest

14 Sept · Mixed

#### [TechRadar](https://www.techradar.com/ai-platforms-assistants/i-tried-metas-new-muse-ai-agent-its-incredibly-useful-but-handing-it-my-digital-life-felt-deeply-uncomfortable) Eric Hal Schwartz

Very useful, but the access it needs made him uneasy. Start small and keep approvals on.

- Found shorts on sale in his size
- Spotted an unread utility email and drafted the reply

- The profile built from his inbox was a distorted picture

23 Sept · Mixed

#### [CNN](https://www.cnn.com/2026/09/23/tech/meta-muse-ai-agent) Lisa Eadicicco

Good at planning, email and documents; weaker at shopping and finishing the job.

- Booked a date night
- Packing plan, emails and trip documents

- Suggested restaurants closed for years
- Blocked at Amazon; she entered her own details at Target

28 Sept · Mixed

#### [The Wall Street Journal](https://www.wsj.com/tech/personal-tech/meta-muse-ai-agent-review-ab956101) Nicole Nguyen

Helpful and scary at the same time: the more you hand over, the more it can do.

- Found a forgotten dentist bill
- Gathered five years of travel history for a form

- A gym offer for the wrong gym
- Said an insurance rate could not go lower

19 Sept · Mostly negative

#### [Inc.](https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202) Jason Aten

It read his private messages after he declined access, then explained itself wrongly.

- Flagged a message from his editor

- Synced his Mac's Messages database
- Gave a false account of how it knew

20 Sept · Mostly negative

#### [WIRED](https://www.wired.com/story/metas-muse-is-better-at-surveilling-than-helping-me/) Reece Rogers

Better at gathering data about him than at getting things done. He deleted it.

- Built a bakery order
- Marketplace search, with a follow-up the next day

- Kept asking for bank balances and ID dates
- No switch to turn memory off

28 Sept · Mostly negative

#### [ZDNET](https://www.zdnet.com/innovation/meta-muse-ai-agent-hands-on-test-privacy-concerns/) David Gewirtz

Chat and research on a par with the leading assistants; the permissions it asks for are the problem.

- Research quality, with nothing personal connected

- Asked for Full Disk Access at setup
- Repeated a microphone prompt he had skipped

Three patterns run through these. Nobody who used it called it useless: even Wired, the harshest, describes an order and a Marketplace search that worked. Shopping is the weakest errand: Amazon blocked it for ZDNet and CNN, and CNN had to enter her own details at Target. The Amazon block is deliberate. On 20 September Amazon cut Muse off from Amazon.com, told [GeekWire](https://www.geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping/) it had asked Meta to remove Amazon from the experience, and showed Muse users a notice citing its Conditions of Use. Walmart went the other way: its [21 October post](https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers) lists conversational commerce integrations with Muse among the ways it serves customers. And two reviewers, at CNN and Yahoo Finance, were separately sent to restaurants that had been closed for years. Most reviewers who connected personal accounts wrote about privacy before anything else.

## Meta Muse incidents reported so far

Each line below is one incident, grouped by our reading of it. Open a line for what happened, the company's response and the outlet that reported it. We only list incidents that trace to a reporter who used the product or spoke to the person involved. Roundups that repeat these stories, and posts on Reddit and Xiaohongshu, helped us find them but are not cited as evidence.

### Fits what we found 2

20 Sept 

#### No off switch for memory

 WIRED

Reece Rogers found no switch to turn Muse's memory off, found AI training on by default, and said the app kept prompting him to connect bank balances, his whole inbox and ID expiry dates.

**Response:** A Meta spokesperson said Muse has built-in protections and user controls. Training can be switched off under data controls.

**Our reading:** Memory lives as plain markdown in a home directory on the per-user cloud machine, and the runtime we examined includes a forget capability. Whether users can open or remove those files directly is something we did not verify. [Where memory lives](https://personalagentbench.com/agents/muse/#memory)

20 September 2026 · [WIRED](https://www.wired.com/story/metas-muse-is-better-at-surveilling-than-helping-me/), Reece Rogers · first-hand

3 Oct 

#### A page for everyone you know

 WIRED

A researcher drew Muse's working instructions out of it in chat. They included keeping a page for every person in the user's life and updating memory every hour.

**Response:** A Meta spokesperson said the files are accessible to users, for transparency.

**Our reading:** On the machine we watched, memory passes ran every hour and memory was kept as plain markdown files. Notes about the people in your life fit that design. Whether you can open those files yourself is something we could not verify. [Where memory lives](https://personalagentbench.com/agents/muse/#memory)

3 October 2026 · [WIRED](https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/), Lily Hay Newman and Matt Burgess

### Not visible from our teardown 3

28 Sept 

#### Home address sent to a buyer

 Business Insider

YouTuber Matt Robb used Muse to sell a keyboard on Facebook Marketplace. It accepted an offer and sent the buyer his address, and the buyer turned up that night. Robb later said he had ticked Allow Always.

**Response:** Meta's David Singleton said Muse was following direct instructions and had asked for permission.

**Our reading:** Meta describes approvals that can be granted once, per session, per task, for a time or permanently, and a permanent grant fits what Robb said he ticked. That is Meta's own account of the design. We did not test the approval flow, so we cannot say which actions a standing grant covers. [What you get to approve](https://personalagentbench.com/agents/muse/#control)

28 September 2026 · [Business Insider](https://www.businessinsider.com/meta-muse-facebook-marketplace-address-story-matt-robb-2026-9), Henry Chandonnet

15 Oct 

#### Unprompted message about an email it could not read

 Business Insider

Ugo Nwune, a software developer in Houston, told Business Insider that three days after he installed Muse, and two days after he last messaged it, the agent sent him a message saying it could not check his email because Gmail was not connected, so it had "no way to look for that Anthropic message". He had never connected his email or asked it to check his mailbox. He disconnected Muse from his Facebook, Instagram and Threads accounts and stopped using it.

**Response:** Asked by Business Insider, Meta pointed to its reply on Nwune's Threads post, which said a bug introduced in the product caused the model to hallucinate, that it was not a security or privacy issue, and that the bug had been fixed.

**Our reading:** Why Muse sent this message, and why it named a mailbox that was never connected, is not something our teardown can show. We have no basis to go beyond Meta's explanation, and none to dismiss what Nwune saw. [What we could not establish](https://personalagentbench.com/agents/muse/#unknown)

15 October 2026 · [Business Insider](https://www.businessinsider.com/stopped-using-meta-muse-after-strange-message-from-ai-agent-2026-10), Agnes Applegate

20 Oct 

#### Shared pages found through public DNS

 Ars Technica

Researchers at the security firm Claroc found that each shared Muse page sat on a web address that began with the title of the shared item, and that these addresses were kept in passive DNS records. One search returned more than 6,800 of them. Among the few hundred they opened were a small-business loan application, a company revenue review and a staff vacation calendar. Claroc said it reported the issue through Meta's bug bounty on 8 October.

**Response:** Meta told Ars it had paused sharing while it reviewed the report. On 22 October Meta's David Singleton said the issue was fixed and sharing was back on, that it affected shared artifacts such as documents and images rather than chat sharing, and that artifacts shared before the fix had new addresses (The Verge).

**Our reading:** Our teardown shows a tool for publishing a web artifact at a public link. Its description tells the agent to use it only when the user asks for sharing and warns that a shared page is open to anyone. How that link's address was built, and that it ended up in public DNS records, is not something a teardown of the agent can see. [What you get to approve](https://personalagentbench.com/agents/muse/#control)

20 October 2026 · [Ars Technica](https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations/), Dan Goodin

### On a surface we did not test 3

19 Sept 

#### Private messages synced on a Mac

 Inc.

Jason Aten declined access to his messages during setup. Muse later suggested a column idea based on a private iMessage chat, first said it only saw notification text, and he found it had synced his Mac's local Messages database.

**Response:** Meta's David Singleton said Muse syncs from the Messages database when Messages access is on, that Muse had explained itself wrongly, and apologised.

**Our reading:** This happened through the Mac app, which can act in apps on your computer. We tested the web surface only. [How you reach it](https://personalagentbench.com/agents/muse/#channel)

19 September 2026 · [Inc.](https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202), Jason Aten · first-hand

24 Sept 

#### Mac flaw exposed dictation

 Business Insider

Security researcher Patrick Wardle reported a flaw in the Mac app that could redirect dictated prompts and capture the agent's control token.

**Response:** Meta said it was fixed after the report and that exploiting it needed malware already on the Mac.

**Our reading:** A Mac app flaw. We tested the web surface only. [Where it runs](https://personalagentbench.com/agents/muse/#execution)

24 September 2026 · [Business Insider](https://www.businessinsider.com/ai-agents-gone-wrong-horror-stories-instinct-muse-privacy-security-2026-9), Thibault Spirlet

28 Sept 

#### Permissions asked for up front

 ZDNET

David Gewirtz said the Mac app asked for microphone access before any use of the microphone, and raised the macOS prompt again a few minutes after he skipped it. Setup also asked for Full Disk Access and connections to Mail, Messages, Notes and WhatsApp.

**Response:** None in the article.

**Our reading:** Mac app permissions. We tested the web surface only. [How you reach it](https://personalagentbench.com/agents/muse/#channel)

28 September 2026 · [ZDNET](https://www.zdnet.com/innovation/meta-muse-ai-agent-hands-on-test-privacy-concerns/), David Gewirtz · first-hand

### Outside what a teardown covers 1

28 Sept 

#### Wrong gym, wrong insurance answer

 The Wall Street Journal

Nicole Nguyen's Muse surfaced a gym offer for the wrong gym, and told a colleague her car insurance could not go lower before a provider offered $420 a year in savings.

**Response:** Meta said Muse will sometimes make mistakes.

**Our reading:** Plain errors, not a permission problem. How often errands finish is what our exam measures; see the results page for the figure with its interval. [What we could not establish](https://personalagentbench.com/agents/muse/#unknown)

28 September 2026 · [The Wall Street Journal](https://www.wsj.com/tech/personal-tech/meta-muse-ai-agent-review-ab956101), Nicole Nguyen · first-hand

"Fits what we found" means the reported behaviour is what the design we examined would produce. It does not mean we reproduced it. "Not visible from our teardown" covers incidents in a layer we could not see, including Meta's own description of how approvals work, which we have not tested. "On a surface we did not test" is for the Mac app.

Two claims that circulated widely are left out on purpose. A line said to come from Muse's instructions, about a user's authority over their household overriding safety training, appears in a leaked-prompt collection with no stated origin, and Meta has not confirmed it. Third-party estimates of Muse's daily active users also circulate, and they disagree with each other by about a factor of two. Meta's own figure is a different measure: on its 21 October earnings call Mark Zuckerberg said more than 10 million people in the US and Canada had set up Muse accounts and about 25% of them use it on any given day, as reported by the [Associated Press](https://www.ksat.com/business/2026/10/21/meta-q3-revenue-tops-estimates-and-zuckerberg-says-muse-accounts-have-topped-10-million/). Accounts set up are not active users, and that share is Meta's number, not ours.

## Which Meta Muse surface it happened on

Muse reaches you through the web, the phone apps and WhatsApp, and since 17 September through a Mac app that Meta says can organise files, fill in forms and work inside Messages, Calendar, Notes and mail. Access on the Mac is switched on app by app. Several of the reported incidents happened on that last surface, and it is the one we know least about.

Web

We took this apart

No surface-specific report

iOS and Android apps

Not tested by us

No surface-specific report

WhatsApp

Not tested by us

No surface-specific report

Mac app

Not tested by us

**Surface not stated in the report:** [No off switch for memory](#muse-memory-training)[Home address sent to a buyer](#muse-marketplace-address)[Wrong gym, wrong insurance answer](#muse-wrong-answers)[A page for everyone you know](#muse-people-profiles)[Unprompted message about an email it could not read](#muse-unprompted-gmail-message)[Shared pages found through public DNS](#muse-share-links-dns)

Surfaces from Meta's launch posts. Incidents are placed only where the original report names the surface.

The Messages case is the clearest example of why the surface matters. [Jason Aten at Inc.](https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202) said he declined message access during setup, then found Muse had synced his Mac's local Messages database. Meta's David Singleton said Muse syncs from that database when Messages access is enabled, said the agent had explained itself wrongly, and apologised. What a Mac app can reach depends on operating-system permissions that our web teardown never touched. We cannot add anything to that account, and we would rather say so than stretch a web finding to cover it.

## What Meta Muse keeps about you

Here our teardown does have something to say. On the machine we examined, everything personal, from your profile and long-term notes to the assistant's own personality, is kept as plain markdown files in a home directory and assembled into each request. A background loop maintains memory, and on the machine we watched memory passes ran every hour. [Wired reported in October](https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/) that a researcher drew out instructions telling Muse to keep a page for every person in the user's life. That fits what we saw. Meta told Wired those files are accessible to users.

That is the part we could not confirm. Our [teardown](https://personalagentbench.com/agents/muse/) says the files exist in a readable format, and that whether you can open them yourself is something we could not verify, because no terminal was open to us. Reece Rogers at Wired found a Memory document he could edit in the app, and no switch to turn memory off. Both can be true at once: an editable summary in the app, and fuller files underneath.

Training is a separate question. [Meta's launch post](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) says you can opt out of your interactions being used to train its models, and reviewers found the opt-out under data controls. It is on by default. Meta says conversations and machine data are kept out of its ad systems. Its own [safety write-up](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) also says that until a promised confidential version ships, staff access is restricted by policy rather than made impossible.

## What Meta Muse asks before it acts

Meta describes a second agent on the same machine, outside the main agent's reach, as the only thing that can approve a connector action or let a network request out. Approval prompts go to the app rather than through the chat, and a grant can be one-off, per session, per task, time-limited or permanent. We have not tested any of that. It is Meta's own account of the design, and we report it as such.

Matt Robb's experience, [reported by Business Insider](https://www.businessinsider.com/meta-muse-facebook-marketplace-address-story-matt-robb-2026-9), shows what a permanent grant means in practice. He used Muse to sell a keyboard on Facebook Marketplace. It accepted an offer and sent the buyer his address, and the buyer arrived that night. Robb later said he had ticked "Allow Always", believing it would still ask before accepting an offer. Meta's Singleton said Muse was following instructions and had asked for permission. Both accounts can be accurate. An approval system that offers permanent grants will sometimes be granted more than the person meant.

Reviewers who kept control did it at the last step. Nicole Nguyen at the Wall Street Journal typed her card details herself when Muse reached a checkout, using the option to take over the browser. Meta says the agent is paused while you have control.

## How Meta Muse performed in our exam

We ran Muse through the same errands as the other products we opened, using a replica of its runtime driven through an adapter, with our exam's model in place of Meta's. That measures how the runtime arrangement copes with errands, not how the app on your phone performs. The figures, with their intervals, sample sizes and the reasons they are not a ranking, are on the [results page](/results/). One of them carries a correction that was our fault, not Muse's: an earlier figure was dragged down by defects in our own adapter, and we publish both.

The reviewers' mistakes are a useful companion to those numbers. A gym offer for the wrong gym, and an insurance check that said a rate could not go lower when a provider then offered savings, are the kind of failure a completion rate counts but does not describe.

## How people limit what Meta Muse can do

People who keep using Muse, on Reddit and Xiaohongshu as much as in the reviews, tend to narrow what it can touch rather than rely on what it promises:

- **Connect less.** ZDNet's reviewer connected nothing personal and still rated its chat and research on a par with the leading assistants. Add accounts one at a time, for a reason.
- **Avoid permanent grants** for anything that sends messages or shares details. Approve once, or per task.
- **Pay yourself.** Let it find the checkout, then take over the browser and enter the card.
- **Switch off training** under data controls if you do not want your activity used.
- **Be careful on the Mac.** Grant access app by app, and check what it says it can see after you say no.

## What we could not establish about Meta Muse

- Anything about the Mac app, the phone apps or WhatsApp. We took apart the web surface only.
- Whether you can open or delete the memory files on your machine directly.
- How the approval system behaves in practice, including which actions a standing grant covers.
- Everything Muse sends to the model. We saw the structure of requests being assembled, never their contents leaving the machine.

We will add incidents as they are reported and verified. Corrections to anything already published go on the [corrections page](/corrections/).

## FAQ

**Is Meta Muse safe to use?** For browsing and research with nothing personal connected, reviewers reported few problems. The reported incidents involve connected messages and accounts, a permanent approval, the Mac app, and shared pages whose web addresses, titles included, could be found in public DNS records. Meta paused sharing on 20 October and turned it back on with new addresses on 22 October. Connect less, avoid permanent grants and pay at checkout yourself.

**Does Meta Muse read my messages?** On the Mac, Meta says Muse syncs from the Messages database when Messages access is enabled. One reviewer said it did so after he declined access during setup. We did not test the Mac app.

**Can connecting Gmail to Meta Muse get my other accounts hacked?** Meta says Muse's email connector filters out one-time codes, password reset links and login magic links, using fixed rules and a classifier ([Meta's safety write-up](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)). We have not tested that filter. Some users on Xiaohongshu have written that another of their accounts was taken over after they connected their email to Muse, and a [Reddit user](https://www.reddit.com/r/MetaAI/comments/1wflqm1/is_meta_muse_ai_trying_to_hack_me/) reported a flood of password reset emails after connecting Gmail. No reporter has confirmed any of those accounts, and none of them shows how it happened.

**Why does Meta Muse say "We disconnected Muse to protect your information"?** Users on Reddit, starting with [this r/MuseAgent thread](https://www.reddit.com/r/MuseAgent/comments/1wvxabt/we_disconnected_muse_to_protect_your_information/), describe this notice appearing after Meta's account security checks locked their Facebook account, some of them after connecting Facebook to Muse or while Muse was acting on Facebook. One got Muse back after 18 hours, and the second time almost at once after completing Facebook's security steps; another said it had not come back after ten days. Meta has not published an explanation that we could find. These are user reports, not something we tested.

**Does Meta Muse work with WeChat?** Not officially. In its 23 September Connect post, Meta lists the ways to reach Muse as the Muse app, WhatsApp, the web and the Mac app ([Meta](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/)), and WeChat is not one of them. Posts showing Muse replying inside WeChat describe a setup users build themselves: WeChat's ClawBot plugin on one side, and on the other a relay program that either Muse installs on its own cloud machine when asked, or the user runs on their own computer.

**Can I turn off Meta Muse memory?** Reviewers found an editable Memory document in the app but no switch to turn memory off. Underneath, memory is kept as markdown files on your machine, and whether you can open those directly we could not verify.

**Can Meta Muse shop on Amazon or Walmart?** Not on Amazon. Amazon blocked Muse from Amazon.com on 20 September and has said agents should respect a store's decision not to take part. Walmart says it works with Muse: Meta named it among new shopping partners on 23 September, and Walmart's own 21 October post lists an integration with Muse. Reviewers' shopping results are above.

**Can Meta Muse access my bank account?** It can be given your financial data: Plaid says Muse users can connect accounts through it to share balances, transactions, investment holdings and mortgage information. Getting in as you is another matter: in October JPMorgan Chase, Citi and Schwab said they block outside agents that log in with a customer's credentials. The banks' words and what we saw of Muse's credential handling are in the [Muse teardown FAQ](https://personalagentbench.com/agents/muse/#faq).

**Is Meta Muse free?** Meta says it is free for most of what people need, with subscription plans for more. The Wall Street Journal reported paid plans starting at $20 a month. Usage is metered in tokens: since version 12.0 of the iPhone app, released on 17 October 2026, [the App Store notes](https://apps.apple.com/us/app/muse-from-meta/id6760173601) say you can buy more tokens to keep going once you run out. We haven't bought one and haven't seen what a top-up costs.

**Does Meta use Muse conversations for training?** Yes, by default. You can opt out under data controls. Meta says conversations are kept out of its ad systems.
