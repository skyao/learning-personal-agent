来源：https://aihomebuilding.com/stories/muse-two-browsers-2026
取文：2026-11-25，直接下载（article.article-body 容器）

Two hundred thousand people were already using it before Meta said a word about it, which tells you most of what you need to know about how fast this product moves and how little its launch resembled a launch at all.

On November 20, 2026, Meta chief AI officer Alexandr Wang posted on X that the Muse Chrome extension was available now. He called the announcement belated, and he was right to. TestingCatalog had spotted the listing on the Chrome Web Store a week earlier, on November 13, when it showed 126 users. Seven days later it showed 200,000. Somebody at Meta forgot to announce a product, and a fifth of a million people found it anyway.

That is the news. What follows is the part that actually matters to you, because Muse now has two browsers, and they are not two versions of the same thing. One belongs to Meta. One belongs to you. Picking the wrong one for a job costs you either a login wall or your entire signed-in identity, and there is no undo button on the second mistake.

## Browser one: the remote window in Meta's cloud

Since launch day, September 8, Muse has done its web work in a real Chromium browser running on Muse Secure VM, a private Linux computer Meta gives every user. Meta's Help Center calls it a web browser inside your chat, one that works similarly to browsers you are familiar with like Chrome and Safari. You tap Open browser to watch it work, Take control of the browser to pause it and do a step yourself, or Stop the task to end it.

Logins in this browser live in a Secure Credentials Store that the AI model never sees, Muse may accept essential cookies on third-party sites, and it asks before important actions such as a purchase, using a one-time card number at checkout so the site never sees your real card. On paper, this is the careful browser, and it keeps your identity at arm's length from every site it touches.

In practice, it has a problem that keeps getting worse. Sites block it. Amazon blocked Muse outright on September 20, 2026, twelve days after launch, and other sites block agents the same way, because they cannot tell a personal agent from a bot. Muse does not sign its requests or identify itself as an agent, so to most security tools it looks like a person browsing, and it still gets stopped at the door. A browser that belongs to Meta is a browser that sites can recognize, fingerprint, and refuse.

There is a second annoyance, quieter but just as real: every site needs its own sign-in inside the remote browser, and every sign-in is a small negotiation involving credentials from the store, an approval card from you, and maybe a code sent to your phone. Approval cards expire after about 30 minutes, which can silently kill a browser task mid-run while you are doing something else. None of this is fatal. All of it is friction, and friction is what the new browser exists to remove.

## Browser two: Muse in your own Chrome

Muse from Meta is the official extension, offered by Meta Platforms, Inc., live on the Chrome Web Store. It puts Muse in Chrome's side panel, open it from any page or press Alt+Shift+C, and it needs Chrome 137 or later. It is 2.37 MiB, in 42 languages, and the listing's own description is blunt about the job: your personal AI agent in Chrome, hand off tasks, take busywork off your plate, and stay in control.

What it does is the same list Muse has always claimed: fill out forms, compare prices, follow up on refunds, sell a car, negotiate a bill, plan and book a trip, track a price drop. What changed is whose session does the work: Muse opens its own tabs in a group and acts only inside those tabs, while the sites see you, not an agent, because you are already logged in. No fresh login, no agent block, no approval card expiring while a checkout waits.

That last sentence is the whole pitch, and you should read it twice, because it cuts both ways: zero login steps means zero friction between Muse and every account open in your Chrome. Your bank, your email, your work accounts, all of them one instruction away the moment you connect the extension, and nothing in the setup asks you which ones you meant.

## What it can see, and what it cannot

Meta's Help Center draws the line plainly, and the line is the opposite of what most people assume. Muse cannot see your saved passwords, your browsing history, or your Chrome settings, and passwords that appear on a webpage are removed from the text before Muse reads it, which means your saved credentials and your history are not part of what Muse can see, even when it is working inside your browser.

Everything else is on the table. Muse can use every site you are already logged into, without asking for login details again, and the store listing's data disclosure says so in the broadest terms: personally identifiable information, health information, financial and payment information, authentication information, personal communications, location, web history, user activity, and website content. Meta declares the data is not sold to third parties, not used for purposes unrelated to the extension, and not used for creditworthiness, so read that list again, slowly, because it is the honest shape of an agent that works in your browser: to do the job, the agent has to see the job.

Controls exist, and they are better than the remote browser's: you approve actions before they happen, a full activity log records what Muse did, and you can revoke any connector at any time and uninstall the extension whenever you like. Mid-task, you click the page, press Esc, or drag the tab out of the Muse group, and control comes back to you, and when Muse finishes, it hands Chrome back on its own, because your other tabs are never touched: the agent's workspace is the tab group and everything outside it is yours.

But the tradeoff is stated just as plainly, and you should not skip it: websites Muse visits may collect information based on its activity and attribute it to you, and that activity may show up in your Google account and your browsing history, where it may affect the ads, recommendations, and content you see on and off Meta products. That is the price of using your own browser, and it is not a footnote: sites let you in because they see you, and seeing you means they can track you.

## Three numbers worth doing the math on

First, the growth. From 126 users on November 13 to 200,000 on November 20 is a 1,587-fold increase in seven days, an average of about 28,550 new users a day. Nobody at Meta published that rate; the raw numbers come straight off the store listing. A product that grows that fast without an announcement is a product people were already waiting for.

Second, the share: Meta reports more than 10 million Muse users since the September launch, which makes two hundred thousand extension users about 2 percent of that, and your own Chrome is not yet a main way people use Muse. It is an early-adopter surface, four days past its official announcement, and the rough edges are still being found in public.

Third, the rating, where a 4.6-star score sounds reassuring until you count the raters: 237 of them, out of 200,000 users, which is 0.12 percent, roughly one rater per 844 users. Treat the score as a weak signal, not a verdict, because early adopters who bother to rate an extension they hunted down themselves are not a representative sample of anything.

## Which browser for which job

Use the remote browser when the job is low-trust or high-stakes and you want distance between the agent and your identity. Price checks on a site you have never visited. A booking on a service you barely use. Anything where getting blocked is an annoyance and a mistaken purchase would be worse. Its logins stay in the credential store, its mistakes happen on Meta's machine, and its worst failure mode is a task that stops.

Use the extension when the job lives inside an account you already trust and already keep open: a refund follow-up with an airline you fly every month, a price drop on a store where you are signed in, a bill negotiation on a utility account you pay from the same browser every month. Its advantage is exactly that nothing needs signing in, and its danger is exactly the same thing.

Never use the extension for a job you would not do yourself while logged in as you, because that is literally what is happening. And never install it before doing the one setup step that matters most: log out of every account you do not want Muse to use. If there is a bank, a work email, or a health portal you would rather keep out of reach, close that session first, because the extension will use whatever you are signed in to, and it will not ask which ones you meant.

## The lookalikes are already here

Within days of a popular product comes the imitation, and this one arrived before the announcement. Muse AI Companion, by Yahor Besarab, and Muse AI Assistant are both third-party products on the Chrome Web Store, and neither is Meta's. Official means one thing: the developer line says Meta Platforms, Inc., 1 Meta Way, Menlo Park, CA, with the contact email [[email protected]](/cdn-cgi/l/email-protection). If the listing does not say that, it is not Meta's extension, and it should not get the permissions an agent in your browser asks for. Check the name and the offered-by line before you click Add to Chrome. The lookalikes ask for the same access and come from nobody you know.

## The third way nobody has shipped yet

There is a third answer to the blocking problem, and it points in the opposite direction from the extension. Poppy standardizes how Muse identifies itself to a site, so the site can tell the agent from a bot and let it through on purpose. The extension borrows your identity so the site never notices an agent at all. Poppy is the agent introducing itself. The extension is the agent wearing your face.

Both solve the same problem, and they solve it in opposite ways: for now, the extension is the one that works on the sites that block agents today, and Poppy is the one that will work on the sites that adopt the standard tomorrow. If Poppy wins, the remote browser stops getting blocked and the extension's identity loan becomes unnecessary, while if it loses, your own Chrome stays the only browser that gets through, and the question of what Muse may touch in it only gets sharper.

## What to do in the next ten minutes

Four steps, in order, before the first task. First, log out of accounts you do not want Muse to use, because the extension inherits every open session and will not ask which ones you meant. Second, open Settings, then Permissions, and set your web access defaults before the first task, not after. Third, use Allow once for approvals while you are learning, which is the safest choice until you know what a given site's tasks look like. Fourth, after the first task finishes, read the activity log, because it is the only record of what Muse did in your browser, and reading it once teaches you more about the agent than any announcement will.

Then watch the first few tasks the way the store listing tells you to: check in to keep it on track, hand it over, watch the first steps, and take over the moment it looks wrong. An agent in your browser is powerful because it uses your session, and risky for the same reason, which is why the controls exist, and they work, but only if you use them.

## The honest accounting

We did not install the extension or test it hands-on for this piece. Extension facts here come from the Chrome Web Store listing and Meta's Help Center as read by the guides cited below on November 20, 2026, and version numbers move fast: 2.1.3 on November 18 became 2.1.9 on November 19. Country availability is not stated anywhere, so we will not claim it works everywhere Muse does. No price or plan requirement is stated either, so we will not claim it is free. Meta's 10 million user figure is the company's own claim, not an audited number, and the growth and adoption math in this piece is our calculation from the listing's published figures, not Meta's.

One date wrinkle is worth noting and not resolving: one report dates its story November 12, 2026, while the listing was first spotted November 13, so we treat November 13 as the first sighting and November 20 as the official announcement, and we do not assert an earlier launch.

None of that changes the decision in front of you. Muse spent its first ten weeks with one browser, a careful one that sites kept shutting out. It now has a second browser that gets through everywhere, because it is yours. That is a genuine improvement and a genuine risk in the same box, and the box is already on 200,000 computers. Install it with your eyes open, log out first, and read the log after.

*Sources: [Meta Help Center, how Muse works with your guidance and approval](https://www.meta.com/help/superintelligence/1385290430137537/); [Built with Muse, Muse Chrome Extension: How to Use Muse in Your Own Browser (2026)](https://builtwithmuse.com/blog/muse-chrome-extension), read in full November 24, 2026; [Muse Explained, Muse's Chrome Extension Is Live With 200,000 Users Already](https://museexplained.com/guide/muse-chrome-extension/); [All Things Muse, Wang Officially Announces Muse Chrome Extension](https://www.allthingsmuse.com/articles/muse-chrome-extension-official-announcement/); [i10X News, Meta Muse Chrome Extension: AI Agent in Your Sidebar](https://i10x.ai/news/meta-muse-chrome-extension-ai-agent-sidebar); [The Outpost, Meta's Muse AI agent moves into Chrome's sidebar](https://theoutpost.ai/news-story/meta-s-muse-ai-agent-is-now-living-in-chrome-s-sidebar-and-200-000-people-are-already-using-it-33944/); [AIModelWaddle, Meta Muse: Features, Pricing, and Privacy Tradeoffs](https://www.aimodelwaddle.com/meta-muse).*
