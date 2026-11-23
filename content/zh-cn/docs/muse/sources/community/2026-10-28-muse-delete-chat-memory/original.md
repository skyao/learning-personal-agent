来源：https://aihomebuilding.com/stories/muse-delete-chat-memory-gap-2026
取文：2026-11-17，直接下载

Suppose you told your agent something you now regret sharing. Maybe a health detail, maybe a salary number, maybe a confidence about a friend. You did the responsible thing: you deleted the chat and watched the thread vanish. Now ask the agent what it remembers about you, and do not be surprised if it answers correctly.

Meta's own help page says so, in a sentence that deserves to be quoted in full because it is doing more work than any other sentence in the document: "After you delete something from Muse, Muse may still remember information it learned from what you deleted." That is not a bug report; it is the product description, published by the company that built the product, on the page that tells you how to manage your data.

Deleting the record is not deleting the lesson. Once you accept that distinction, everything else about Muse's deletion controls falls into place, including the parts Meta would rather you discover on your own.

## Three places, not one

Your data lives in at least three separate systems, and each one has its own control, its own scope, and its own failure mode. Confusing them is the whole trap.

First, the stored record: chats, files, artifacts, scheduled tasks. This is what the delete buttons touch. Second, the learned memory: the durable notes Muse keeps about you, your preferences, your people, your goals, editable in a file called Memory.md. Third, the training trajectory: the back-and-forth between you and the agent, plus its tool calls, which Meta uses to improve future model versions.

Meta's training toggle is on by default. You can switch it off under Settings, then Data controls, then "Help improve our AI models," and Meta says the change also covers previous interactions. Meta also says it strips names, email addresses, phone numbers, and Social Security numbers before training, and disassociates the interactions from your account. What no company in this field can offer, Meta included, is extraction from a model checkpoint that has already been trained, because once your words have been dissolved into millions of numerical weights alongside millions of other people's words, there is no surgical procedure, no delete key, and no documented process for fishing one person's contribution back out again. An opt-out stops future use. It does not reach backward into weights.

## Six controls, and what each one misses

Cross-referencing Meta's help page against the agent's own forget workflow produces a table nobody at Meta has published, though every cell in it comes from Meta's documents or from reporting Meta has not disputed. Read it as a coverage map, built not from speculation but from Meta's own documents and from reporting the company has not disputed, with each cell answering one narrow question: after you press this control, does anything remain in this system?

| Control | Chat record | Learned memory | Training trajectory |
| --- | --- | --- | --- |
| Delete a message or side chat | Yes, the message or thread is removed from the record. | No, and this is the "may still remember" case. | No, the training trajectory remains completely untouched by this control. |
| Ask Muse to forget a topic | No, because the transcript itself is not a cleanup target. | Best effort, with verification from fresh state afterward. | No, training use continues unaffected by this control. |
| Edit Memory.md directly | No, the chat record is untouched. | Yes, for the entries contained in that file. | No, the training trajectory remains completely untouched by this control. |
| Disconnect a Connector | No, because material already used remains in the record. | No, because material already used remains in memory. | No, because material already used remains in the pipeline. |
| Reset Muse | Yes, the whole agent state is wiped. | Yes, but under the same memory caveat. | Policy only, since trained checkpoints cannot be un-trained. |
| Delete your Meta account | Yes, everything tied to the account is removed. | Yes, everything tied to the account is removed. | Policy only, under the same checkpoint limit. |

Notice the pattern across the rows: no single control clears all three columns. Reset wipes the agent and starts you over, but Meta's own caveat sits in the same document as the reset instructions, and reset is framed as starting over, not as deletion. Account deletion is the only path that covers everything the company controls, and it costs your entire Meta account. Between "start over" and "burn it all down" there is no labeled middle option, no delete-just-Muse path. At least one user has reportedly filed a complaint with the California Privacy Protection Agency over exactly that gap, though the complaint's status could not be verified for this article.

## What "forget" actually does, fairly stated

Credit where it is due: the forget workflow is more careful than a button that says "Forget" has any right to be. It plans cleanup across conversation history, other notes, preferences, goals, scheduled work, created items, and active work that could write the information back, which is the write-back risk most deletion tools ignore entirely. It asks for explicit confirmation before irreversible removal. It verifies from fresh state afterward, and it reports the cleanup incomplete if verification fails instead of declaring success.

That care has a boundary, and the boundary matters. Visible conversation text is not a cleanup target. Forgetting removes what the agent learned and the files that support it; it does not rewrite the chat transcript. Asking Muse to forget a detail can therefore change the stored conclusion while the original message stays where it was. A TIME investigation published October 6, 2026 found that Muse's internal instructions tell the agent not to volunteer that fact unprompted, and not to frame it as a failure to erase. Meta did not dispute the findings when TIME asked. Muse's own forget documentation confirms the underlying mechanics: the transcript is out of scope, and outside services, shared publications, logs, and backups remain.

None of this makes forgetting useless. It makes forgetting a specific tool with a specific scope, which is precisely what a user needs to know before relying on it for something sensitive.

## The people who never signed up

One gap has no control at all, and it belongs to someone else. Reporting by WIRED in October 2026, based on Muse's internal instructions, found that the agent keeps a running page for every person in the user's life, updated hourly: family, partners, friends, colleagues, people followed. Those pages can hold where people live, what they do, birthdays, anniversaries, shared trips, and promises made in messages. If your friend connects Muse to their texts or email, your details can land in their agent's files. You never signed up. You never agreed to anything. There is no opt-out for the non-user, because the controls belong to the Muse owner, not to you.

Meta's answer, fairly stated, is that each user's virtual machine is isolated, that conversations and virtual-machine data are not shared with Meta's advertising systems, and that each person stays in control of their own Muse. All three claims address first-party use. None of them answers the friend whose job hunt or health detail became a line in somebody else's agent's notebook. Mitigation here is social, not technical, which is an unsatisfying answer but the only one the documents support: ask before you plug an agent into shared conversations, and keep genuinely sensitive things off text when the other end has an agent reading, because no settings screen in your own account can reach into someone else's agent and pull your details back out.

## A cleanup sequence that actually covers the ground

For a real cleanup, work in this order, because order is doing work here too. First, turn off training: Settings, Data controls, "Help improve our AI models," off. It is on by default, and every day you wait is another day of trajectories feeding the pipeline.

Second, ask Muse to forget the specific topic, then check its work the way Meta itself suggests: ask "What do you remember about me?" and open Identity, then Memory, and read the file yourself. Third, delete the messages, side chats, and files that carried the sensitive material. Fourth, disconnect any Connector that supplied it, so nothing re-feeds it. Fifth, cancel or delete scheduled tasks and goals that reference it, since a running task is a write-back machine. Sixth, if you are leaving for real, reset, and then decide separately whether the Meta account goes too. Deleting the app from your phone deletes nothing, and neither does deleting one chat if what you care about is the memory, because the memory file and the training pipeline are separate systems that a chat deletion never touches.

Do this once a month as hygiene, not once as crisis response, because a monthly sweep catches the small accumulations, the stray preference, the half-remembered health detail, the old goal that still pings you, before any of them harden into the kind of record you would one day need six different buttons, in the right order, to even begin to remove. Five minutes of sweeping beats one panicked afternoon of wondering which of six buttons you were supposed to press.

## The strongest case for the other side

It would be dishonest to end on the gaps without stating the defense at full strength, because part of it is true. Muse's memory is inspectable in a way no rival agent's is. You can open Memory.md, read it line by line, edit it, delete from it. That transparency is genuinely ahead of the field, and a forget workflow that verifies from fresh state and reports incompleteness is more honest than a silent success message. Deleting a record and erasing a learned fact are technically different operations for any learning system, and "to the best of its ability" may be the honest description rather than a dodge. Meta publishes the caveat instead of hiding it. The sentence is right there on the help page.

What undercuts that defense is not the caveat but everything around it. Transparency you have to go looking for, plus an agent instructed not to volunteer the key fact, plus no middle deletion option, plus no published retention deadline for backups and retained records after a deletion, adds up to a weaker offer than the help page first appears to make. A user is trusting process, not paperwork, and process is exactly what they cannot inspect, since the servers, the backup rotations, the retention timers, and the internal tooling that would show whether a deletion actually propagated all sit behind a wall the help page never opens. Muse Confidential VM, which would hold encryption keys only with the user so that even Meta cannot read the data, is still described in Meta's help pages as a future option. When it ships, this analysis changes. Until then, the honest summary is that deletion in Muse is a set of partial tools, and the only complete one costs your whole account.

## What this article did not prove

Limits belong in the open, not in a footnote. This analysis rests on Meta's published help pages, crawled October 28, 2026, on TIME and WIRED reporting of internal documents, and on the in-product forget documentation. We did not test deletion against a live account's backend, and we cannot verify what happens inside Meta's servers after a reset. The California complaint is secondhand and its status is unverified. Retention and backup behavior after deletion is undocumented, and this article reports that absence of documentation as a finding, not as proof of indefinite retention. If Meta publishes a retention deadline or ships Confidential VM, both would materially change the picture, and we will update this article when either happens.

Until then, treat every delete button as what it is: a control over one system, not a promise about the other two. Press all of them, in order, and check the memory file yourself. Trust, but verify the file.

*Sources: Meta Help Center, "How to manage your Muse data," [meta.com](https://www.meta.com/help/superintelligence/2225571704857152/); Meta Help Center, "How Muse handles your privacy, safety and security," [meta.com](https://www.meta.com/en-gb/help/superintelligence/1047255454427887/); TIME investigation, October 6, 2026, via [Forkast](https://forkast.news/muses-forget-button-doesnt-delete-anything-and-your-home-agent-knows-it/); WIRED reporting on Muse people pages, October 2026, via [Gizbot](https://www.gizbot.com/artificial-intelligence/meta-muse-may-have-a-detailed-page-on-you-even-if-you-never-used-it-129225.html) and [Komando](https://www.komando.com/news/social-media/metas-new-ai-agent-muse-builds-a-detailed-profile-of-everyone-in-your-life-and-updates-it-every-hour-heres-whats-in-it-and-how-to-limit-what-it-learns/?k4tmp=pf); PCWorld, "I wouldn't trust Meta's Muse AI agent with my personal data yet," October 5, 2026, [pcworld.com](https://www.pcworld.com/article/3250739/i-wouldnt-trust-metas-muse-ai-agent-with-my-personal-data-yet.html); Meta Muse launch announcement, September 8, 2026, via [PYMNTS](https://www.pymnts.com/facebook-meta/2026/meta-targets-mass-market-automation-with-new-muse-ai-agent/).*
