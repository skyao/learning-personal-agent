来源：https://aihomebuilding.com/stories/muse-connector-census-56-apps-2026.html
取文：2026-11-17，直接下载

Everybody asks what model Muse runs on, which is the wrong question, because the model is the engine and the connectors are the hands: an agent with a genius brain and no hands is a chatbot with good PR, while an agent with fifty-six sets of hands is staff.

There is exactly one document that lists the hands, buried in the app's settings where almost nobody looks, and after a week with the most complete public census of it I can tell you it reads like a resume, and an unusually honest one.

## Fifty-six hands

Drew Mailen maintains [the most complete public census of Muse's connectors](https://www.drewmailen.com/muse-connector-directory), updated weekly, with every entry sourced to Meta, the vendor, or two independent confirmations. As of this week the count stands at 56 connectors live, nine of them Meta-owned, six more announced but not yet shipping, plus more than twenty community-built custom connectors floating around GitHub.

And the shape is the story: email and calendar, 6; docs and productivity, 19; finance and payments, 5; commerce, travel, and events, 6; health, 5; messaging and devices, 4; infrastructure, 2; and nine Meta-owned surfaces sitting on top like a cherry, Facebook, Instagram, Threads, Messenger, the ad accounts, the product catalog, and the browser itself.

9 of 56
Connectors that say Google on the tin: Gmail, Calendar, Contacts, Tasks, Docs, Drive, Sheets, Slides, Forms, while Microsoft gets exactly one (Outlook). The most advanced agent Meta has ever shipped is functionally a Google Workspace front-end wearing a Meta badge.

That is not a criticism, just a statement about where your work lives, which Meta understood perfectly. You do not hire an agent to admire its model weights; you hire it to live in your inbox and your calendar, which happen to belong to Google.

## Your body is the sleeper category

Five connectors touch your health, which is more than payments gets: Function Health reads your lab results and biomarkers, HealthEx reaches your connected health records, Withings syncs weight and vitals, Peloton reads your workouts and schedules, and Apple Health reads activity metrics.

Nobody's keynote led with "your agent reads your bloodwork," but the directory says it can, and the permission screen for a lab-results connector deserves considerably more of your attention than the one for Spotify, because one of these things can see your medications and the other makes playlists.

## Money gets the armored truck

Finance is the small category, and small on purpose: Plaid connects bank accounts and balances, balances not transfers, so read the scope line twice, while payments run through [Stripe Link, which generates a one-time-use card number](https://www.deeplearning.ai/the-batch/how-to-secure-agents-for-the-masses) so the agent never sees your actual card, a design Stripe's Mike Clayville praised when he called Muse the first AI agent covered by Link's purchase protections, with Shop Pay and PayPal rolling out behind it.

Translation: Meta understands that the fastest way to kill an agent is one bad charge, so the money path is the most armored part of the entire system, wrapped in approvals, one-time credentials, and purchase protections, while the email connector next to it gets a toggle. Risk budgets are moral documents, and this one says Meta fears your bank statement more than your inbox. Reasonable.

## Where the gaps are

Now the gaps, because the gaps reveal what the partnerships haven't bought yet: Amazon is not there, the biggest store on earth, and the agent cannot touch it, since Amazon has [reportedly blocked Muse from shopping its store entirely](https://www.techrepublic.com/article/news-meta-muse-ai-agent-us-launch/); Uber Eats is requested by users and unavailable; United Airlines is requested and unavailable; and an entire category, social-media schedulers, simply does not exist in the directory.

Announced but not live: 1Password for credential autofill, Expedia for hotels, Fever for events, Zapier, which would unlock 9,000-plus apps through a single MCP pipe, plus a stack of retailers from the September keynote. Watch Zapier and 1Password, because those two change the math on what is safe to connect, in opposite directions: one multiplies the agent's reach by orders of magnitude, while the other finally gives it a proper vault instead of a browser full of logged-in sessions.

## No permission screen on the fallback

Here is the part nobody puts in a keynote: for everything without a connector, Muse has a fallback, and the fallback is its own browser, which just drives the website the way you would, slower and brittler, logged in as you, clicking around like a very fast intern who never sleeps.

Think about what that means for the permission model, because connectors are the permissioned path, with scopes, approval tiers, read-only toggles, and an activity log, while the browser is the unpermissioned path, with no scope screen, no read-only toggle, and no list of what it touched. Every connector Meta ships moves one more task from the unpermissioned path to the permissioned one, which is genuinely good, but every task without a connector still runs with the keys to the kingdom, so the fancier the directory gets, the more you should ask about the fallback.

## Disconnect is not delete

Meta's own help copy says the quiet part out loud. ["Disconnecting stops Muse from exchanging data with the Connector. Information that Muse previously used to perform tasks with that Connector might still remain in Muse's memories and your conversation history."](https://top5apps.ai/news/how-to-connect-gmail-to-meta-muse-and-build-a-connector/) The off switch stops the future. It does not erase the past.

A real full wipe lives two menus deeper, at Settings, Data Controls, Reset Muse, which permanently deletes all information, chats, files, and active tasks, the works, while Google gets its own revocation at myaccount.google.com/connections, which kills the token regardless of what Muse's UI claims. Two real off-ramps, and neither of them is the button labeled Disconnect.

## An ungoverned door

Then there is the door Meta left open on purpose: don't see your app, ask Muse to build a custom connector, hand it a documented API or an MCP server URL, and it wires itself up, storing your credentials in its Secure Credentials Store, with no review from Meta, a path the directory's maintainer counts at more than twenty working community examples on GitHub already, from LinkedIn to Oura to Jira (see the [community awesome-muse list](https://github.com/cszach/awesome-muse)).

Enterprise security people have noticed, and they are not thrilled, with [one vendor report describing the custom path as ungoverned](https://www.runlayer.com/blog/secure-muse-for-the-enterprise-via-runlayer) and warning it allows risky actions at home or at work. They have a point, and so does the other side, because this is also the most powerful feature in the whole directory: a reviewed connector list is a menu, while an unreviewed build-your-own path is a workshop, and power and audit trails rarely share a room, so decide which one you need before you hand the agent your API keys.

Which brings us to the strongest argument against everything I just wrote: a connector list is a partnership list, not a capability list, since Meta signs deals and the browser does the rest, meaning a logo in the directory proves a business relationship rather than a tested integration, and the failure record says the permissioned path leaks, with enterprise reports of Muse sharing sensitive data without consent and sending unauthorized emails, plus [the Marketplace incident where a permission dialog's "Always" handed a stranger a home address](https://otto365.ai/brief/002-muse-for-small-business). Counting logos is not measuring reliability. The census tells you where the agent is allowed to go; it says nothing about how gracefully it behaves when it gets there.

## Connect in this order

1. **Start with the trio: Gmail, Google Calendar, one payments wallet (Stripe Link).** That combination is roughly eighty percent of the useful agent, and every one of them is a reviewed, first-party path.
2. **Set everything to read-only first.** Connectors support approval tiers, so use the strictest one for a week and escalate to write access per task rather than per lifetime.
3. **Assume connected data is indexed permanently.** If you test with real data, know that disconnecting later does not erase what the agent already used, which is why you test with boring data.
4. **Revoke on both sides.** Disconnect in Muse, then revoke the token at the provider (for Google: myaccount.google.com/connections), because belt and suspenders beats trust.
5. **Skip custom connectors for money and health data.** The unreviewed path is fine for a side project, but it is not fine for your bank or your bloodwork.
6. **Watch two launches: 1Password and Zapier.** Vault autofill closes the session-cookie question while Zapier multiplies reach by thousands of apps, so re-audit your permissions the week either ships.

## What this census cannot prove

Honest accounting: I did not independently connect all 56 integrations or test each one end to end, and the census leans on a third-party directory cross-checked against Meta and vendor announcements, which means it will rot, since availability varies by region and app version, PayPal is still rolling out, several keynote-announced retailers have no live dates at all, the Marketplace home-address incident is cited via secondary reporting, the community custom-connector count comes from the directory's claim rather than my own GitHub audit, and the disconnect semantics are Meta's UI copy as documented by third parties, not language I pulled from the published privacy policy. Treat the numbers as a map drawn this week, not a deed.

Models are engines and connectors are hands, so count the hands before you hire the help.
