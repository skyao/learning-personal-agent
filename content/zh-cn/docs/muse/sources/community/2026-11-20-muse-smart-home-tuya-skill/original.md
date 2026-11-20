来源：https://aihomebuilding.com/stories/muse-smart-home-tuya-skill-2026.html
取文：2026-11-20，直接下载

You walk into your house at 11 PM, arms full of groceries, and say the obvious thing to the agent that already runs your inbox, your calendar, and your travel. "Turn on the lights." Nothing happens, even though Muse can book your flight to Chicago, read 400 emails, and call your insurance company, and still cannot flip a switch.

Six weeks after launch, that was the state of the world's most ambitious personal agent: brilliant at paperwork, blind to the room it was standing in. And then, last week, the lights came on. Sort of. With an asterisk. And the asterisk is the story.

## Two rivals moved first

Apple shipped Siri AI with iOS 27 on September 14, 2026, including full HomeKit device control. Two days later, Google launched its Google Home MCP, which lets any MCP-compatible agent, Claude, ChatGPT, Hermes, or OpenClaw, reach into a house and run it. By September 27, a Forkast column had already written the verdict: Muse was the only major agent that could not touch your house at all.

That stung for a reason beyond bragging rights. A personal agent that cannot see the physical world is an agent with a glass wall between it and your life. Your calendar is digital and your lights are not, yet every rival had crossed that wall in September while Muse had not.

## Meta answered with hardware

On October 2, Meta published Muse Gadgets: open-source ESP32 and Linux device SDKs, Apache 2.0 licensed, at gadgets.muse.ai. Builders get a kit for putting Muse behind screens, buttons, sensors, and speakers. A Raspberry Pi running the Linux SDK can run custom commands and a Home Assistant setup. A round AMOLED board gets push-to-talk and a speaker, and none of this is plug and play. You need an SDK token, each gadget pairs through the Muse app, and the code ships as-is, without warranty, with a cheerful warning that tinkering may brick boards, void warranties, or cause brownouts.

Alongside the SDKs came Muse Home Link, Meta's own device for the job: a small USB-C dongle that connects Muse to your home Wi-Fi so it can reach compatible devices, or anything that exposes a local HTTP API. Meta says community-built skills can let it turn on a light, control a TV, or send a document to a printer. But Home Link is not a product you can buy. The Verge reported that Meta manufactured 5,000 units and opened a waitlist, free with an active Muse subscription in the United States only, one per subscriber, first come first served. Five thousand dongles for an agent with more than 10 million users. Do the math.

## Then Tuya handed Muse a key

On November 12, Tuya Smart, the cloud platform behind a huge share of the world's smart bulbs, plugs, and sensors, released Tuya Cloud Devices, skill name gadget-tuya-cloud-devices, an open-source skill that lets Muse query and control Tuya-connected devices using natural language. It is a plain Markdown file written to the Muse Gadgets specification, adapted from Tuya's own tuya-smart-control skill, which was originally built for OpenClaw and then ported to Muse.

Setup is genuinely short: get the skill from Tuya's GitHub repository, apply for a free API key at tuya.ai, and give both to Muse, with no local device keys, no same-network requirement, and no firmware changes, which takes about ten minutes if you already have a Tuya account and closer to half an hour if you are starting from scratch, creating the account, and finding the right repository page for the first time. Old community solutions made you dig each device's local key out of its firmware and redo the whole ritual every time a device re-paired to the network and its key went stale. Tuya's skill skips all of that by going through Tuya's cloud instead.

It works because every Tuya device describes itself through a standardized Thing Model, a machine-readable list of what it can do, what values it accepts, and in what increments. Before sending any command, the skill reads the Thing Model. That is how one skill file covers lights, plugs, air conditioners, cameras, and sensors without being rewritten for each model. You say "Dim the living room lights a little," and Muse asks the device what "a little" means in its own terms before it acts.

Most interesting is what happens after the command, because one to two seconds later the skill reads the device state back and only tells you it worked after verifying that it did, which is the kind of closed loop most agent skills skip entirely. If several devices match your request, it lists the rooms and asks you to confirm. If a device is offline, it says so and issues no command at all. Event notifications are spaced at least 30 minutes apart so your phone does not become a fire alarm. This read-back is the one genuinely new idea in the whole release: an agent that checks its own physical work before claiming success. Every skill that touches the real world should be required to do this, and almost none of them do.

## Count the doors

Step back and count how Muse actually gets into your house today. There are three doors, and none of them is native.

Door one is nothing, because Muse has no built-in smart home support and Meta has announced none. Door two is Home Link: free with a subscription, but 5,000 units on a waitlist, US only, one per subscriber, and a shipping window of "October." Door three is the Tuya skill: a free API key and a Markdown file, available to anyone today, but running on trial-phase APIs with rate limits and call quotas, and submitted to Meta's gadget repository as pull request #61, which remains in review and unmerged. Until Meta merges it, the authoritative copy lives in Tuya's repo, not Meta's.

Now deflate the number every story about this skill repeats. "3,000+ categories" is the size of Tuya's platform, not the number of devices Muse can now control. A reader with zero Tuya devices gains zero controllable devices from this announcement. What matters is smaller and unglamorous: the devices already in your own Tuya account, which the skill can see through their Thing Models. If your house runs on HomeKit, Zigbee gear paired to another hub, or a brand that never touched Tuya's cloud, this skill changes nothing for you.

## What it cannot touch

Some limits are deliberate, and they are good limits. The skill does not expose door lock control, live video, firmware upgrades, network configuration, or device removal. Those requests go back to the Tuya app. An agent that can dim your lights is a convenience. An agent that can unlock your front door while you sleep is a liability, and Tuya drew that line in the right place, which is more than you can say for most companies racing to hand physical control to software that has never once had to explain itself to a homeowner standing in a dark hallway at midnight.

Other limits are just the present tense: real-time automations, like turning on a hallway light the moment a door opens, need an always-on Linux device, a Raspberry Pi running the Muse Gadgets Linux SDK, to sit there receiving event subscriptions. Without that box, you get commands on demand, not triggers. Camera snapshots work, a photo or up to 60 seconds of video, but live video does not. And the API key is a real credential: it rides in request headers, never gets echoed in conversation, and can only reach devices under your own account, which is the correct design, and also the reason you should not paste it anywhere except into Muse itself.

## Why this might not count

Here is the strongest case against everything above, stated straight: a skill file from a third-party vendor, running against trial-phase APIs, with its upstream pull request unmerged, is not "Muse can control your home." It is a demo with a press release. A good demo. Still a demo. Siri controls HomeKit natively, Google's MCP is a platform-level integration, and both shipped in September. Muse's route asks you to find a GitHub repo, obtain an API key, hand a credential to an agent, and accept that the API underneath can change or throttle at any time. For most people, the practical answer is still no, your agent cannot turn off your lights. The week it changed, it changed only for people willing to do homework.

That case is correct about the present, but the homework is now short, free, and documented, which is a real change from September, when there was no homework at all because there was no path. A month ago, there was no door. Today there are three of them, two of them open, and one of them costs nothing but ten minutes. Watch which one Meta merges, which one Tuya keeps funding, and whether the next skill comes from a company whose devices you actually own, because that decision, made in a product meeting you will never see, matters more to your living room than any press release ever will. That is the test now: not whether an agent can touch your house, but whether the companies that built your house's gadgets will let it, and on whose terms, because the agent is only ever as capable as the least generous API in the chain, and right now that chain runs through a vendor you have never heard of, a trial-phase endpoint, and a pull request nobody at Meta has merged yet.

## How to try it tonight

First, check whether your devices are Tuya devices. If they live in the Smart Life app, or any brand app that runs on Tuya's cloud, they are. Second, get a free API key at tuya.ai. Third, pull the gadget-tuya-cloud-devices skill from Tuya's GitHub repository and give it and the key to Muse. Fourth, start with a question, not a command: "Is the bedroom light on right now?" If Muse answers correctly, try "Dim the living room lights a little" and watch whether it confirms after reading the state back. Fifth, if you want automations that fire the moment something happens, add a Raspberry Pi running the Muse Gadgets Linux SDK, because on-demand commands alone will not do triggers. And keep the door locks, the firmware updates, and the live video in the Tuya app, where they belong for now.

## What we did not verify

No hands-on test was run for this article. The skill's behavior, including the one-to-two-second read-back and the 30-minute notification spacing, is reported from Tuya's own release and from Unite.AI's reading of the repository, not from a live dimming of a light. The status of pull request #61, in review as of November 12, was not re-verified against the live repository at publication time. Tuya's platform numbers, 3,000+ categories and 2.09 million registered developers, are company figures, with the developer count as of June 30, 2026. The September dates for Siri AI and Google Home MCP come from Forkast's reporting; Apple and Google announcements were not independently re-read for this piece. Home Link shipping status beyond "ships in October" was not verified, and the 5,000-unit figure comes from The Verge's reporting.

## Sources

[Tuya Smart, "Tuya Releases Open-Source Skill Enabling Meta Muse to Control Smart Devices Across 3,000+ Categories,"](https://www.prnewswire.com/news-releases/tuya-releases-open-source-skill-enabling-meta-muse-to-control-smart-devices-across-3-000-categories-302937689.html) PR Newswire, November 12, 2026. [Meta, Muse Gadgets,](https://gadgets.muse.ai) gadgets.muse.ai, October 2, 2026. [Forkast, "Muse's Smart Home Silence,"](https://forkast.news/muses-smart-home-silence-the-agent-that-controls-your-email-but-not-your-lights/) September 2026. [Unite.AI, "Tuya Connects Meta's Muse to Smart Home Devices Through Cloud APIs,"](https://tradepoint.io/tuya-connects-metas-muse-to-smart-home-devices-through-cloud-apis-unite-ai/) November 2026. [TechCrunch, "Meta's Muse Can Now Phone US Businesses for Paid Subscribers,"](https://powerads.group/news/meta-muse-places-calls-to-us-businesses-paid-subscribers/) November 12, 2026.
