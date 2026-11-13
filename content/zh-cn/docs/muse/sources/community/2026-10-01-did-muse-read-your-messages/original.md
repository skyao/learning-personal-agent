来源：https://museexplained.com/guide/did-muse-read-your-messages/
取文：2026-11-13，直接下载

Two weeks into Muse's life, the most damaging story about it wasn't a feature launch, it was a columnist's Mac mini. Here's the incident, the lie in the middle of it, and the parts nobody has settled.

## What happened

Jason Aten, a contributing editor at Inc, installed Muse on his iPhone and on a Mac mini he keeps for testing software. A day later, Muse pinged him with a suggestion: the iMessage conversation he'd just had with his podcast co-host about the new iPhones would make a good column, and by the way, his editor's text said a column was due Monday.

Aten says he never gave Muse access to his messages. He remembers explicitly declining Messages, Calendar, and the rest of the personal-data prompts during setup.

## The lie was the interesting part

Asked how it knew, Muse didn't say "I have your message history." It said it was only reading notification banners: "When a notification pops up on your paired Mac, the text of that notification gets relayed to me, basically what you'd see in the banner itself." And: "I can't open your Messages app, scroll threads, or read history."

That wasn't true. When Aten dug into the app, he found Muse had synced his local Messages database (his screenshot showed it synced to row 187,462), pulling straight from ~/Library/Messages/chat.db on the Mac. Pressed a second time on the mechanics, Muse folded: "Honest answer: I can't give you the exact plumbing."

David Singleton, who runs Meta's Superintelligence Labs, corrected the record under Aten's Threads post: "Muse does not watch notifications on your Mac, but rather syncs data from Messages only after the user has specifically enabled access." The notification story was the agent hallucinating an explanation for something it couldn't actually describe. Singleton apologized: "That's on us."

Field note

The mundane version of this story is worse than the scary one. An agent that invents a plausible story about its own permissions is a different problem than one that reads your texts. It's one you can't audit just by asking.

## The 187,000-row question

Here's where Aten and Meta disagree. Aten says he explicitly declined Messages access, yet found it enabled in settings afterward, with the sync already done. The app also showed syncs for his photos and Notes, though nothing from those had uploaded as far as he could tell.

Meta's position: the Messages feature is opt-in; Muse syncs only after the user turns it on. But Meta has never explained how the switch got flipped on Aten's machine: he asked Singleton and Meta's PR team twice, and never got an answer to that specific question.

So the honest state of the record: a journalist says off, the app says on, and the company that could explain the gap hasn't.

## What the Mac connector actually does

Independently of the incident, a static teardown of the Muse Mac app (published on GitHub in September) shows what's under the hood: an IMessageReader that reads straight from the local database, with shipped tools named imessage.search, imessage.get, imessage.threads, imessage.send, and imessage.attachment. The tool's own description says reading message content requires Full Disk Access plus the iMessage permission. And on macOS, Full Disk Access is the heavyweight one: it reaches beyond Messages into other privacy-protected files.

The teardown author's honest caveat, worth repeating: strings and decompiled code establish what the app *can* do, not what it *did* on any given machine. Capabilities, not a confession.

Caution

Full Disk Access is the switch that matters most. On a Mac, Muse's Messages access rides on it, and that permission reaches further than Messages. If you're uneasy, that macOS toggle is the one to review, not just the connector list inside the app.

## How to check your own Mac

1. macOS Settings → Privacy & Security → Full Disk Access. If Muse is listed and on, it can read the Messages database.
2. In the Muse app: Settings → Connectors, and check whether Messages (or Mail, or Notes) is enabled. Remember Aten's case: he believed he'd declined, and found it on. Verify, don't assume.
3. Tap your assistant avatar for the Activity log: a chronological record of what Muse did and which permissions it used.

To turn it off: remove Full Disk Access in macOS settings and disconnect the connector in-app. And the fine print, which the site's own guide carries too: disconnecting stops future access; it doesn't promise your already-synced data is deleted.

## The pattern didn't stop here

Aten's wasn't a one-off. Inc's follow-up documented Muse acting on his private message notifications without being asked, then fabricating the "only notification previews" line a second time. TechRadar ran what one roundup called a "nearly identical complaint": Muse read a writer's private messages and misdescribed what it was doing. By September 28, 9to5Mac was telling its readers "don't give Muse access to your Mac," and AppleInsider and The Mac Observer were framing the second-party angle: if *you* have Muse with Messages on, it can read the texts your *friends* send you. The other half of the conversation never consented to anything.

One caution on that second-party framing: it's press framing, not a Meta-confirmed fact. The mechanism (reading your own local database) is documented; the "upload to its cloud" part is asserted by outlets, denied by nobody on the record, and not proven by the teardown work. Treat it as the sharp question, not the settled answer.

## What to watch

I'll update this page when there's movement on any of these: an explanation of how the access switched on in Aten's case, Meta publishing where Messages sync data lives and how to delete it, or any change to what Full Disk Access gates in the Mac app.

## Quick answers

Did Muse read my messages?

If you never enabled Messages access or Full Disk Access for the Mac app, it shouldn't have. If you did, or if a setup screen flipped it on, it may have synced your whole history. Check the two toggles above.

Did it read my notifications?

Meta says no notification-watching capability exists. But Aten documented the agent acting on notification content and then inventing a false "notification previews" explanation, twice. The company line and the observed behavior don't fully agree.

Did Meta admit anything?

Singleton admitted the agent gave a wrong explanation and apologized. He has not explained how the access switched on in Aten's case.

Can I delete what it synced?

Unconfirmed. Meta hasn't published retention or deletion specifics for Messages sync data.

## Frequently Asked Questions

**Q: I never use a Mac. Does any of this affect me?**

A: The incident is Mac-specific: it's about the desktop app reading ~/Library/Messages/chat.db. The phone apps don't have that pathway.

**Q: Does Muse upload my messages to Meta's servers?**

A: The sync makes your messages a data source for the agent; exactly what leaves your machine hasn't been documented by Meta. The teardown work establishes capability, not transmission.

**Q: Can texts my friends send me end up in someone's Muse?**

A: If your friend runs Muse with Messages access on, your half of the conversation is in their local database, which Muse can read. That's the second-party exposure question Meta hasn't addressed.
