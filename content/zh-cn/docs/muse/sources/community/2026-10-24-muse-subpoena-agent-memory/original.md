来源：https://aihomebuilding.com/stories/muse-subpoena-agent-memory-2026
取文：2026-11-22，直接下载

On May 13, 2025, a federal magistrate judge in Manhattan ordered OpenAI to stop deleting things: not corporate memos or training data, but your chats, including the ones you had already deleted yourself.

Magistrate Judge Ona Wang directed the company to preserve and segregate all output log data that would otherwise be deleted on a going-forward basis, regardless of whether deletion was requested by users or mandated by privacy regulations, which means a court order told a company to keep data that privacy law told it to throw away. Then, on November 7, 2025, the court ordered OpenAI to hand over more than 20 million de-identified ChatGPT logs to the New York Times and its co-plaintiffs in the copyright case. Twenty million conversations changed hands, some of them deleted by their authors months before the order existed, which establishes the point this whole article turns on: deletion was a request, not a fact.

## The diary problem

Most people treat an AI like a private diary, but legally it is a record held by a company, with none of the privilege that protects what you tell a lawyer or a doctor, a formulation that belongs to Eamonn Maguire of Proton and remains the cleanest sentence written on this subject.

A DuckDuckGo survey found that 75 percent of respondents did not know their AI chatbot conversations could be subpoenaed by law enforcement, three out of four, while a Washington Post investigation found at least a dozen court cases that have cited AI chatbot logs as evidence, which means the diary is already being read aloud in courtrooms.

But the chatbot frame is too narrow, and that is the part nobody is talking about, because a chatbot keeps transcripts while a personal agent, the kind that runs your calendar, reads your inbox, books your travel, and remembers your children's birthdays, keeps something richer: it does not just log what you said; it keeps what it learned.

## No privilege for machines

In *United States v. Heppner*, a court ruled that a defendant's Claude conversations were not shielded by attorney-client privilege or work-product protection, reasoning that no attorney-client relationship exists, or could exist, between an AI user and a platform such as *Claude*.

This should surprise no one who has read the privilege rules and surprises nearly everyone who uses these tools, because privilege protects communications with a person who owes you fiduciary duties and can be disbarred, while your agent owes you good autocomplete. There is also active surveillance on the provider side: Anthropic's systems flagged a Florida woman's Claude conversations for human review and contacted police, and she was charged, reportedly having used it like a diary, unaware that staff could read it. Some diaries report you.

## Six kinds of records

I mapped what one personal AI agent actually retains, using Meta's own documentation for Muse and checking it against a real, heavily used deployment, and the footprint has six layers, each giving a different answer to the question you actually care about: can I delete this?

**1. Chat transcripts:** The main chat can never be deleted, by the agent or the app; side chats can be archived or deleted; and the only full wipe is Reset, which permanently deletes chat history, files, and active tasks.

**2. The memory graph:** Curated facts, preferences, and relationship profiles, everything the agent decided was worth keeping about your life, deletable but only on a best-effort basis, and the documentation contains a sentence everyone should read twice: clearing a conversation is not private because memory can still be written.

**3. The activity ledger:** Everything the agent does is recorded in the Activity view and the approvals history, none of it secretly erasable: every permission you granted and every action it took on your behalf, timestamped.

**4. Standing permissions:** Website logins, connected accounts, and scheduled-task grants are each listed on a permissions page and removable per site, but the agent cannot revoke them itself; only you, in settings, by hand.

**5. Connected accounts and device data:** Gmail, calendar, and health sync are disconnectable with tokens removed, and health data is erasable per request, though data still on the phone can sync back afterward.

**6. Workspace files and artifacts:** Documents it wrote, media it generated, and data it exported for you, all deletable and downloadable by the user.

In the deployment I checked, those layers held 18 daily memory logs, 263 person profiles, 21 group profiles, and a transcript database, and I am quoting counts rather than content because the point is structural: a subpoena does not need your diary when it can have your filing cabinet.

## The one setting that changes everything

There is a single architectural lever that matters more than all six layers combined: on a standard deployment, the provider may log and review your interactions, conversations are not end-to-end encrypted, and they can contribute to AI training, with an opt-out buried in Settings; on a confidential deployment, the provider cannot access the content at all, with client-owned keys and hardware-protected enclaves, which is why the training opt-out row does not even appear.

Know which one you have, because it is the most consequential privacy setting in the product and most users have never looked at it.

## The counterargument, stated properly

Now the honest objection, because it is strong: discovery is not new and agents are not special, since email has been subpoenaed for decades along with text messages, search histories, and location records, which means every record a company holds about you is producible in litigation, every lawyer already knows it, and a personal agent is the newest instance of an old rule rather than a new danger.

Most users will never be parties to a lawsuit, and the 20 million logs in the Times case belonged mostly to uninvolved strangers swept into someone else's discovery fight, which is genuinely disturbing, though the disturbing part is the sweep rather than the agent. Providers fight these orders, sometimes successfully: OpenAI objected on privacy and burden grounds, and the October 2025 narrowing shows courts can be moved, with normal deletion resuming for new logs and European data carved out entirely.

Deletion rights still matter enormously for the common threats, which are not subpoenas but breaches, brokers, and internal misuse, and the right to erasure does real work every day against those. All true. None of it changes the core fact: the delete button is a request to a company, and a court can overrule the company.

## What this does not prove

Honest accounting is required here, because the subject demands it: I verified Muse's documented controls from its own documentation, but I did not, and cannot, test how any provider behaves under an actual legal order, and retention specifics beyond what is documented are not public. The Times orders concern OpenAI, not Meta; policies differ across providers, and this article generalizes in places where it should specify. One deployment's file counts are illustrative, not representative of a typical user, and I am a journalist who reads like a lawyer rather than a lawyer, so this is not legal advice.

## Six things worth doing

The reader is deciding how much of their life to hand to an AI agent, so here is the practical version.

**Ask your agent what it knows about you.** It will answer from its own memory; audit the answer, because you will find things you forgot you told it.

**Review standing permissions in Settings:** every website login, connected account, and scheduled grant is listed there, so revoke what you no longer use, since grants accumulate like subscriptions.

**Check whether you are on a standard or confidential deployment.** This one setting decides whether the provider can read your content at all.

**On a standard deployment, decide about the training opt-out in Data Controls.** It is your data contributing to someone else's model until you say otherwise.

**Remember that Reset is the only full wipe.** Deleting one chat is tidying; it is not privacy.

**Draw the bright line:** if you would not want it read aloud in a deposition, do not type it into an agent whose infrastructure you do not control.

The law has a simple theory of your agent's memory: if it exists, it can be asked for, which means your agent's memory is not a diary but a filing cabinet, and the court order is already drafted in pencil.

*Sources: Meta Muse documentation on data handling, retention, and permissions (muse.ai/privacy, muse.ai/terms); NYT v. OpenAI docket via [Patent AI Lab's case timeline](https://patentailab.com/nyt-vs-openai-lawsuit-update-2026/), [Thurrott](https://www.thurrott.com/a-i/openai-a-i/330404/openai-must-turn-over-chatgpt-logs-in-new-york-times-case), [Terms.law](http://terms.law/2025/11/12/openai-v-new-york-times-stopped-being-just-a-copyright-case-the-moment-the-court-turned-to-your-chatgpt-logs/), and [Nelson Mullins](https://www.nelsonmullins.com/insights/blogs/corporate-governance-insights/all/from-copyright-case-to-ai-data-crisis-how-the-new-york-times-v-openai-reshapes-companies-data-governance-and-ediscovery-strategy); [TechRadar](https://www.techradar.com/vpn/vpn-privacy-security/you-thought-your-chatgpt-conversations-were-private-the-courts-disagree) on US v. Heppner, the Washington Post investigation, the DuckDuckGo survey, and the Florida/Anthropic referral.*
