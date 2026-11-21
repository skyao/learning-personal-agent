来源：https://www.allthingsmuse.com/articles/signal-restricts-screenshots-ai-agents-muse/
取文：2026-11-21，直接下载

Signal is switching on screenshot restrictions by default to stop AI agents from reading private chats, calling the protections incomplete and urging Apple, Google, and Microsoft to give developers a real opt-out. The move follows Reuters reporting on Muse reading Signal messages.

Signal will restrict screenshots in its app to stop AI agents from reading private chats on phones, the encrypted messaging service [said on November 20](https://dukecountry.fm/2026/11/20/exclusive-signal-restricts-screenshots-to-block-ai-agents-from-reading-messages/). Reuters, which reported the announcement exclusively, said the new restrictions switch on by default. Users will get pop-up windows offering them the option to disable the blocks when Signal detects a screenshot attempt or an AI assistant trying to access the screen, depending on the device.

Signal called its own protections “incomplete” and urged the operating system providers, Apple, Google, and Microsoft, to give app developers more concrete ways to block agents from accessing sensitive data, and to provide more information about how their agents function. “Right now, these agentic AI integrations are changing this environment in a way that’s making it increasingly hostile to privacy. This is an existential threat to Signal, and our ability to responsibly uphold our mission,” the company said in a blog post provided to Reuters ahead of publication.

## What the Restrictions Cover, Platform by Platform

Signal identified the AI capabilities built directly into operating systems, such as Apple’s Siri AI and Google’s Gemini Intelligence, as particularly worrisome because of how deeply they are integrated into people’s devices.

The protections vary by platform because each system gives an app developer different tools. Signal said in its blog post, [as The Register reported](https://www.theregister.com/security/2026/11/20/signal-slams-door-on-prying-ai-agents-to-protect-privacy/5311466), its iOS app now blocks screenshots inside Signal by default and adds a setting called “Block Siri AI,” and that its Android app switches on its existing Screen Security feature when it detects an AI assistant trying to read the screen. Signal blocked Microsoft’s Recall AI from taking screenshots on Windows last year. On macOS, Signal says it cannot reliably offer the same protection and advises users to exclude Signal from Siri in the Mac’s System Settings instead.

Blocking screenshots closes one route into a chat, but it does not stop an agent that reaches content through other permissions a user granted during setup, including accessibility permissions. Signal said developers should have straightforward ways to opt their apps out of AI data processing entirely, covering screen reading, notifications, and file system access.

## The Muse Findings Sit Behind the Change

Signal’s announcement follows [Reuters reporting earlier this week that Muse could read Signal messages](/articles/reuters-muse-safety-mishaps/) on a Mac and on an Android phone, in tests Reuters ran with Signal staff and the AI Now Institute. In both cases Muse bypassed Meta’s official Connector tool and used broad operating system permissions granted during the app’s initial setup. On the Mac it used a combination of accessibility and screenshot tools to navigate to Signal, capture chats, extract the text from the images, and reproduce the messages inside the Muse app. The same requests were blocked on iPhone.

An Apple operating system update this week effectively closed that specific Mac pathway, Reuters reported, while also introducing a new set of permissions aimed at agents that offers similar capabilities with additional user warnings. Meta said in response to the reporting that agents need to see and interact with people’s computers to work on their behalf, and that Muse can access other apps only through permissions users explicitly grant.

Signal is not the first service to put up a barrier. [Websites have been blocking Muse and other agents at the network level](/articles/muse-websites-blocking-agents/), and [Apple has already moved to tighten Mac permission prompts after a Muse privacy dispute](/articles/apple-mac-muse-privacy/). Signal’s step moves the same fight onto the phone screen itself: the messages stay end-to-end encrypted in transit, but an agent that can read the screen can pull them out of that protected environment and into its own servers, which is the exposure Signal is now trying to close by default.
