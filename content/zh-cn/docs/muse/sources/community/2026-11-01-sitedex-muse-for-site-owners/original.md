来源：https://www.sitedex.dev/guides/meta-muse-for-site-owners
取文：2026-11-05，直接下载

## Meta's Muse agent: what your site can and can't see

Meta [launched Muse](https://www.pbs.org/newshour/nation/meta-launches-personal-ai-agent-muse-to-help-with-everyday-tasks), a personal agent for adults in the US, on September 8. People
message it in the Muse app or in WhatsApp, and Meta says it can "open a browser, fill out forms,
and negotiate on their behalf." Muse is a different thing from Muse Spark, the model behind Meta
AI in WhatsApp, Instagram, Facebook and Messenger.

Meta [has described](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) how the agent browses. It runs "a real up-to-date Chromium based browser"
inside a virtual machine, and the part that reads pages works from "an accessibility tree
snapshot of the page." On identity, Meta says: "When Muse browses the internet, it will appear
as your activity." To your site, a Muse visit can look like your customer.

## What Meta has published about identifying Muse

No user agent, IP range or signature for Muse, as of November 1, 2026. [Meta's page for
website owners](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) lists five crawlers (FacebookExternalHit, Meta-WebIndexer, Meta-ExternalAds,
Meta-ExternalAgent and Meta-ExternalFetcher), and Muse isn't one of them. The page doesn't
mention signed requests.

One thing we can see: a file of five Ed25519 keys is live at
`meta.com/.well-known/http-message-signatures-directory`, the address Web Bot Auth
uses. Meta hasn't said what signs with it, and we haven't observed a signed Muse request.

Sites have gone both ways. Amazon [barred Muse](https://www.engadget.com/2263659/amazon-bars-metas-muse-ai-from-shopping-on-its-site/) in September, and one of its reasons was that
Muse doesn't identify itself as an AI agent while browsing. Walmart is a named Muse shopping
partner, yet users reported Muse failing at its checkout, where a prove-you're-human step turned
it away. Walmart [told TechCrunch](https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/) the blocks weren't intentional.

## What to do now

If you want to be cited in Meta AI, allow Meta-WebIndexer. Meta says it helps "cite and link
to sites in Meta AI responses."

If you want agents to finish a purchase or a signup, walk that flow yourself and look for the
human check that would stop an automated browser.

Label your buttons and form fields. Meta says its browser reads the accessibility tree, so
controls without accessible names give it less to work with.

This page reflects Meta's published pages as read on November 1, 2026.


