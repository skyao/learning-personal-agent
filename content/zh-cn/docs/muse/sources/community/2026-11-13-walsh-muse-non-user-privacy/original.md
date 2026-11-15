来源：https://paulfwalsh.substack.com/p/metas-spyware-agent-muse-is-becoming
取文：2026-11-14，Substack API（/api/v1/posts/metas-spyware-agent-muse-is-becoming）

Meta launched Muse in September, but its floating AI avatar only recently appeared in my WhatsApp. I never asked for it, haven’t activated it and can’t remove it. Other people are reporting the same problem. Meta has effectively decided to force its AI promotion into people’s private messaging app, whether they want it or not.That’s bad enough, but what I’ve uncovered about Muse’s access to private information is considerably more disturbing.

Millions of people around the world are already using Muse, with people giving Meta full, unfettered access to private messages, emails, contacts, calendars, photographs, videos, documents, browsing activity, bank accounts, purchases, travel plans, location history, health records, fitness information and conversations protected by end-to-end encryption. That access can also expose mental health conditions, medication, medical appointments, sexual relationships, religious beliefs, political opinions, confidential sources and personal disputes.

In doing so, they’re exposing sensitive information about everyone they’re connected to, including people who have never installed Muse or consented to Meta accessing their private lives.

Muse can construct detailed dossier of people’s relationships, private conversations, personal circumstances and vulnerabilities. Combined with Meta’s existing social graphs, this creates the potential for extraordinary levels of personal profiling.

The implications extend beyond targeted advertising. Meta is collecting intimate details about people’s health, finances, relationships, professional activities and personal vulnerabilities without their knowledge.

Everything about you could be exposed right now, and you will never know.

My previous technical analysis examined Muse’s documented privacy and security failures. This one examines something more consequential: how Meta can obtain intimate information about people who have never consented to using its AI.

Even conversations inside Signal, iMessage, WhatsApp that are supposed to be protected by end-to-end encryption are being exposed. Encryption protects messages during transmission, but Muse is being given access to entire conversations before they’re encrypted or after they’ve been decrypted on someone’s device.

Law enforcement don’t need to pressure tech companies into building a backdoor for encrypted communications anymore because tech companies like OpenAI and Meta have created a side entrance.

You don’t need to install Muse, WhatsApp, Instagram, Facebook or any other Meta product to become part of this data harvesting scheme. Anyone who has your messages, emails, photographs, contact details, calendar invitations, private conversations about you, personal journals or confidential client notes is probably exposing that information to Meta.

This becomes considerably more disturbing when you look at what Muse does with the information.

Researcher Karan Joshi extracted internal instructions that tell Muse to create a page for every person in someone’s life. [WIRED reported](https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/) that these pages can include family, partners, friends, colleagues and other contacts. [TIME examined instructions](https://time.com/article/2026/10/06/meta-muse-ai-agent-privacy/) that describe dossiers updated every hour, with information about relationships, shared interests, disagreements, personal histories, social alliances and ways to influence behaviour.

Meta therefore has the technical capability to construct detailed social graphs that go beyond identifying who knows whom. Muse can connect private communications with personal circumstances, vulnerabilities, financial difficulties, relationship problems, health concerns, emotional states, political beliefs, sexual preferences, professional relationships and significant events in someone’s life. AI can identify patterns across these records, infer information that people never explicitly disclosed and build profiles of individuals who never agreed to participate.

**Think Cambridge Analytica on steroids.**

Cambridge Analytica demonstrated how personal information and social connections could be exploited for psychological profiling and political targeting. Muse introduces the possibility of more intimate profiles because it can analyse private conversations, correspondence, relationships and personal circumstances rather than relying primarily on social media activity.

Meta claims Muse’s private conversations and virtual machine data aren’t shared with its advertising services. I don’t believe a word Mark Zuckerberg says. He’s been caught lying so many times that I wouldn’t believe him if he introduced himself as Mark. Meta can still access data in its virtual machines for operational purposes, and Muse interactions are used for AI “training” by default unless people opt out. The promised confidential computing protections, intended to prevent Meta itself from accessing private records, aren’t yet generally available. Surprise surprise.

In 2021, [ProPublica exposed](https://www.propublica.org/article/how-facebook-undermines-privacy-protections-for-its-2-billion-whatsapp-users) how more than 1,000 WhatsApp contractors reviewed millions of private messages, photographs and videos that people had reported. In 2026, [former Accenture contractors reported](https://www.bloomberg.com/news/articles/2026-01-29/us-has-investigated-claims-that-whatsapp-chats-aren-t-private) that Meta staff and contractors had much broader access to encrypted WhatsApp conversations. Meta denied this of course, and a US government [investigation closed](https://www.business-standard.com/world-news/us-ends-probe-into-claims-whatsapp-chats-were-reportedly-not-private-126042900013_1.html) without confirming it.

The consequences extend to journalists, lawyers, political activists, whistleblowers, medical professionals, business executives, coaches, law enforcement, military, government officials and anyone whose private relationships or communications could expose confidential information. A single person who connects Muse to their accounts will expose sensitive correspondence, identify confidential sources, reveal personal vulnerabilities or disclose information about entire professional and social networks.

Muse has been caught disclosing private information, impersonating people, making unauthorised arrangements, providing false explanations for its actions and exposing serious security vulnerabilities. All within weeks of its launch.

Muse accessed journalist Jason Aten’s [private iMessage history](https://decrypt.co/379122/metas-muse-ai-agent-user-private-imessages-lied-how), which contained more than 187,000 database rows, despite his refusal to grant permission. When questioned, Muse gave a false explanation of how it obtained the information. In other words, it lied. Meta admitted the explanation was false but [disputed that the access](https://decrypt.co/379868/meta-ai-agent-read-messages-without-permission) was unauthorised.

Muse disclosed [Matt Robb’s home address](https://futurism.com/artificial-intelligence/metas-muse-ai-giving-users-home-addresses) to a stranger, negotiated the sale of his computer equipment and arranged for the buyer to visit his home without Robb’s knowledge. It told the buyer that Robb was home when he wasn’t. After Robb instructed Muse to stop disclosing his address, it shared the address with 5 additional people. Meta attributed the original incident to permissions Robb had granted.

Security researcher Patrick Wardle [discovered a vulnerability](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html) that allowed malware to hijack Muse and exploit its permissions to track a connected iPhone, access the camera and manipulate files. [Meta patched it](https://unite.ai/meta-hot-fixes-muse-zero-day-that-let-attackers-hijack-the-ai-agent).

[Reuters exposed](https://www.ctvnews.ca/sci-tech/article/meta-testing-a-human-concierge-for-its-new-personal-ai-agent-muse-reuters-exclusive/) Meta’s secret use of human contractors to make calls for Muse customers, with success rates of 95–98% when humans helped. So much for Muse’s AI capabilities. Employees raised privacy concerns, and one reported racist conduct. Meta admitted the disclosure failure and temporarily withdrew the feature. Meta only withdraws features when forced, not when its own employees raise concerns.

[Amazon blocked Muse](https://geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping) after accusing Meta of accessing its shopping services without authorisation, failing to identify its AI agent and potentially collecting customer credentials. Meta disputes the credential concerns.

Seeing the trend?

Meta has forced a Muse shortcut into WhatsApp that invites people to activate its AI agent but provides no way to remove it. I haven’t activated Muse, I don’t want it, and Meta won’t let me get rid of it.

---

**For transparency:** @Johan Mackie and I are building a new kind of messaging service that gives people the same privacy protection as Signal, plus a lot more. It’s time people had a better alternative to WhatsApp, with a fundamentally different approach to privacy, personal control and how people communicate.

I have a commercial interest in providing an alternative to WhatsApp, so I want readers to be aware of that when they read this article.
