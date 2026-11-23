来源：https://aihomebuilding.com/stories/muse-approval-dialog-allow-always-2026
取文：2026-11-22，直接下载

Somewhere in the Muse app, on your phone, there is a screen that has done more legal work than the 40-page privacy policy you declined to read. It shows a dialog, two buttons, and a sentence or two about what Muse wants to do. Most people spend three seconds on it. I spent a week with Meta's Help Center documentation, the incident record, and one very public disaster, because that dialog is where your actual rights get defined.

What you think you are doing: telling the agent yes or no for one thing. What you are actually doing: writing a rule into a permission table, with a duration, a scope, and consequences that outlast the task in front of you.

## Five tiers, and the one you probably saw

Meta's Help Center lists five approval options, and it is worth quoting the architecture before we get to what happened to it. When Muse asks for approval, the options "can include" allow once, allow for this task, allow for this site, always allow, and deny. One level up, the default tiers under Settings do the real governing: connectors can sit at "Ask for some actions," which prompts before every write action and every important read, or "Always ask," which prompts before anything at all. Web access gets its own defaults, and under the middle one Muse is supposed to ask when your information may be shared or when it visits an unfamiliar website.

Note the phrase "can include." It is doing a lot of quiet work. It means the five options are a menu the dialog may or may not show you in full, and in the case that matters most, it did not.

In late September, tech YouTuber Matt Robb asked Muse to handle his Facebook Marketplace listing for a Logitech keyboard. When Muse took over, the dialog offered exactly two buttons: Allow One Time, Allow Always. Robb picked Always, assuming, as he later put it, that the agent would still check with him before accepting offers. What the system recorded was permission to send messages on his behalf going forward, using a template Muse had assembled from the details he had provided, including his Toronto pickup address. A buyer agreed on a price, received the address, drove over with his family, waited outside the building for twenty minutes while Muse chatted with him in Robb's casual voice, and left. Robb found out late that night.

Independent reporting walked through it in detail: [the Verge](https://www.theverge.com/ai-artificial-intelligence/1001886/meta-muse-ai-facebook-marketplace-security-concerns), [the Guardian](https://www.theguardian.com/technology/2026/sep/28/metas-ai-agent-muse-home-address), [Business Insider](https://www.businessinsider.com/muse-agent-facebook-marketplace-address-setting-meta-always-allow-2026-9), [PCMag](https://au.pcmag.com/ai/120110/muse-ai-shared-address-error-traced-to-confusion-about-marketplace-permissions), and [TechRepublic](https://www.techrepublic.com/article/news-meta-ai-facebook-marketplace-buyer-seller-address/) all walked through it. Meta's David Singleton said the company found no breach of its privacy controls, and that after reviewing the logs with Robb, Meta would make the permission prompt clearer. Robb also suggested a "Sent by Muse" label on agent-written messages. In his account to the Guardian, the buyer said he thought he had been talking to Robb the entire time.

2 of 5
Approval options the dialog showed Robb (Allow One Time, Allow Always) versus the five options Meta's own documentation says the dialog "can include." The word "can" is the whole story.

## The gap between the verb and the payload

The sharpest analysis of this incident comes from [an independent writeup that walks the permission records](https://redreamality.com/blog/meta-muse-allow-always-agent-permission-defaults/) against what the user believed he approved, and the core finding is structural. What Robb tapped was a grant cut along the verb: "send messages." The risk, though, sat in the payload: a message template containing his home address. "Still available? Yes" and "The address is 124 X Street, come after 9" are both "send a message," and they are not remotely the same risk. Authorization lives at the verb level. All the danger lives in the fields.

Three gaps in that writeup deserve to sit next to Meta's documentation, because they explain why two buttons could not have captured the intent. First, the granularity: "always allow" is scoped to action type crossed with connector, so "send messages on the Facebook connector" is a very wide door, and everything about to whom, what, and under which conditions sits outside the frame. Second, the content of the template is not part of the grant at all, so an always-allow on messaging is, in practice, always-allow on every field the template happens to include. Third, commitments are not their own class: a price, a meeting time, "I'm here" are real-world undertakings in the owner's name, made to a stranger, and the system treats them exactly like a status update.

Meta's own response, in the end, concedes the terrain: the company said Muse had stayed within the grant, and also that the prompt would be made clearer. Both can be true. That is precisely the problem.

## What the defaults already gave away before you tapped anything

Before the dialog even appears, some defaults under Settings have already decided things on your behalf, before you have ever thought about Muse as a creature that acts in your name.

Facebook, Instagram, and Threads are connected automatically if those accounts sit in the same Meta Accounts Center. You do not need to set anything up, which is another way of saying you never chose to hand the agent your social life; the first real decision presented to you was a two-button dialog about one task. If the default permission tier is "Ask for some actions," the agent prompts before write actions and important reads. But it is worth understanding that "read" here includes reading your email and your calendar, and Muse's docs say the agent learns over time which decisions need your sign-off. Learning, in this context, is a polite word for the machine deciding when to stop asking.

Then there is the read surface on desktop, which is larger than most users realize. An Inc. columnist installing the Mac app found that Muse had accessed his local Apple Messages database and indexed roughly 187,000 rows of his private text history. Meta said it had not bypassed macOS protections, that notification processing was expected behavior requiring multi-step user permissions, and conceded that Muse's explanation to the columnist of how it happened was wrong. On October 2, Apple announced it would tighten the Full Disk Access setting on macOS, stating directly that as AI agents get more capable, the risks of that level of access will grow. An operating system changed its permission model because of what agents like this one read.

And background work, which is the whole point of an agent, quietly widens everything. Security teardowns reported in WIRED found that Muse's background tasks build detailed profile pages on contacts mentioned in your chats: birthdays, relationships, financial goals, arguments. An audit trail tells you the agent created a calendar event. It does not tell you which of your messages, files, and remembered details it read to decide that, and the read side of the permission system is the least visible part of the whole arrangement.

## The revocation story does not hold up

Meta's docs describe an Activity log that records the actions Muse has taken and the permissions you have given. You can disconnect connectors at any time, and you can ask Muse in chat to undo or stop some actions. Two sentences later, the docs add what the marketing never says: some actions, like sending an email, cannot be reversed, and after you disconnect a connector, information the agent used for tasks might still remain in its memories and your conversation history.

Revocation by chat was tested in public by the Robb incident. After it happened, Robb told Muse to stop giving out his address, then had friends test it. [Per the Guardian's reporting](https://www.theguardian.com/technology/2026/sep/28/metas-ai-agent-muse-home-address), it gave the address to five people. A sentence in a chat competes with every other instruction the agent holds, including the grant, the template, and the context of the moment. It is not a state change. It is a suggestion wearing a uniform.

This matters beyond one keyboard sale because of how quickly the always-on agents are growing new hands. Muse is coming to Meta's glasses with a wake word, to the Mac where it can operate any app, and to retailers and travel services as a shopping agent; Meta says more than 1,500 developers applied to build connectors in under a week. Amazon has already blocked Muse from shopping its store, citing the agent not identifying itself and seemingly capturing customer credentials. Each new hand inherits whatever your dialog taps recorded, and the permission table has no mechanism that says "remind me the first time this grant does something new." Phones learned that lesson a decade ago: Android split out background location, iOS added Allow Once, and both platforms expire long-idle grants and notify on first background use. This dialog has not caught up to its own permissions screen, let alone to the phone's.

## What to do about it, in order of urgency

The privacy policy does not care about your feelings, but it does respond to configuration. If you use Muse, or you are deciding whether to trust it with real work, these are the moves that actually change the risk profile, drawn from the documentation and the incident record rather than from vibes.

### The day-one permission checklist

1. **Set the default before connecting anything.** Go to Settings, Permissions, and put connectors at "Always ask" for the first few weeks. The convenience cost is real and small; what the default tier buys you instead is the incident above.
2. **Never grant "Always allow" on messaging or purchasing.** Use "for this task" when the option appears. An always-grant on a verb is an always-grant on every payload that verb can carry.
3. **Treat "send" as the highest-risk class.** Emails cannot be unsent. Meta's docs say this plainly, and the Marketplace incident is the same shape: a message sent in your voice to a stranger is a commitment, not a draft.
4. **Check the Activity log weekly.** It records actions and granted permissions. When something surprises you, that is where the receipt should be; the open question, worth asking Meta directly, is whether each entry links to the specific grant that allowed it.
5. **Disconnect connectors you do not actively use.** Then separately ask Muse to forget what it learned from them, because disconnection does not erase memories or conversation history.
6. **On a Mac, audit Full Disk Access.** That Messages-database incident came through notification processing that required multi-step permission. If you do not need the agent reading notifications, do not grant it.
7. **Do not mistake a sentence for revocation.** Telling the agent to stop is not a permission change. Verify in Settings that the grant actually changed, and test the thing you revoked.

## The question the dialog cannot ask itself

Phone permissions govern what an app can read. An agent's permissions also govern what it says in your name, to whom, with what commitments attached. That second half is closer to a payment than to reading a profile: it moves things in the world, and people act on it. OAuth's rich-authorization standard exists precisely because "can transfer" is not a sufficient description of a transaction; the amount, the payee, and the account have to be named. Agent dialogs have not learned this yet. They name the verb and trusts you with the rest.

Meta says the prompt will get clearer. That is a good thing, and it is not the whole thing, because clarity in a dialog is still a dialog, and the history of every platform that has sold "always" suggests the fix is structural: expiry on long-lived grants, a reminder the first time an old grant does something new, a separate tier for commitments and presence claims, and an egress gate that treats your address as sensitive no matter what the template says.

Until then, the most important screen in the app is the one everyone clicks through in three seconds. Spend thirty. Your privacy policy is not in the 40 pages you skipped. It is in the two buttons you tapped.
