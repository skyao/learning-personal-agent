来源：https://museexplained.com/guide/inside-poppy-json-what-a-business-publishes-poppy-1-0/
取文：2026-11-16，直接下载

## Poppy Promise Ledger, Part 2

Poppy Promise Ledger, Part 2

This is Part 2 of this site's Poppy coverage. Part 1, published November 15, 2026, reported the launch claim from Sierra's post of November 13: Poppy is on for everyone who uses Muse, and Muse looks for Poppy first on every site it visits. That post named the check this one runs: read the implementation file itself, on the protocol's own site, and test it against the protocol's own validator.

- Launch claim, November 13, 2026: Sierra's post, read in full. Poppy 1.0 published at personalagentprotocol.org, Shopify enabled for every merchant, Mercury, Synchrony, and Turkish Airlines named as going live, more than 100 design partners in total.
- Implementation kit checked, this post, November 15, 2026: the 1.0 specification, the guides, the extensions pages, and the company implementation kit at personalagentprotocol.org, all read in full, plus the validator in the kit's GitHub repository, run offline against the specification's own example document. Result in the validator section below.
- Still open, checked November 15, 2026: no in-app sighting of Poppy behaviour in Muse, and no announcement from Mercury, Synchrony, Turkish Airlines, or Shopify in its own name. DuckDuckGo checks on November 15 found neither. Synchrony's own Poppy items are both from October 2026, before 1.0: a blog post of October 15 and an 8-K of October 20 about joining as a design partner.
- Next check: November 23, 2026, for the two open rows above, and for a live company poppy.json this site can run through the validator's survey command and print by name.

## The file, and where it has to sit

A company joins Poppy by publishing one JSON document at a fixed address: https://<domain>/.well-known/poppy.json, served over HTTPS as application/json. The specification, section 3, is blunt about the alternative: if the company has no poppy.json, it is not part of the protocol.

The file tells a personal agent four things: who the company is, how to start a Session with it, how sign-in works, and which channels it offers, meaning its website, its APIs, or its own company agent. The agent learns the sign-in issuer a second way, from standard OAuth metadata. The company publishes protected resource metadata at /.well-known/oauth-protected-resource (RFC 9728), whose authorization\_servers list names the issuer, and the agent then follows that issuer's OAuth server metadata (RFC 8414) for endpoints and sign-in methods.

Two rules in section 3 govern everything the file says. First: only what a document declares can be relied on. A personal agent must not assume a service, an endpoint, or a method that the document does not declare. Second, from section 3.1: a field listed as optional can be absent, a required field must be present, a field that is present must be the right type, and a personal agent must ignore unknown fields. That last rule is why the exact forms in the next section are worth printing. A field written in the wrong form is not a style error. It is a field the agent cannot use as written.

## Required: two fields, plus one channel

The section 3.1 field table marks exactly two fields as required, and one group as a choice a company cannot skip.

- protocol\_version. Required. The protocol version this document follows, written as major.minor. For this specification it is "1.0". A personal agent uses the document only if the version is compatible with one it implements, and it must check this field first.
- organization. Required. The company's display name, its domain, and an optional logo\_uri. The domain must be the host that serves the document, after any redirects. That check stops a document copied to another domain from speaking for the company.
- At least one of agent, apis, or web. A company must offer at least one channel. agent lists the company agent's conversation protocols, each with a type, an HTTPS endpoint, and a description. apis lists APIs, each with a type, a url, and a description. web is the company's website, with an optional browser\_session\_endpoint where an agent's browser joins a Session.

That is the whole required list. A website-only company can meet it with protocol\_version, organization, and web. The guides say so in plain terms: if your website already supports sign-in, the cheapest path is to publish a poppy.json that lists only web. A personal agent will then use the website, not the APIs.

## Optional fields in section 3.1: auth, tasks, extensions, and supported\_versions

- supported\_versions. The other protocol versions the company serves, each mapped to the URL of that version's document. It is an object, a map from version to URL, not a list. If omitted, the company supports only protocol\_version. Each URL must sit on the same host that served poppy.json, and every version's document must carry the same organization.domain and the same issuer.
- auth. The company's sign-in details. Its parts are issuer, disabled, scopes, and scope\_hints, each covered below.
- auth.issuer. Conditional, not simply optional. If the domain's protected resource metadata lists more than one authorization server, auth.issuer selects the one personal agents use, and it must be in that list. With one server, the company may leave it out.
- auth.disabled. Defaults to false. Set to true, it tells personal agents the company offers no sign-in even though it has an issuer, and an agent must not start sign-in with that company.
- auth.scopes. Scope descriptions, keyed by scope name. It is an object: each scope name maps to a written description of what that scope allows, in the same form as the scopes of an OAuth 2.0 security scheme in OpenAPI. In the specification's example, orders:read is described as "See your orders, returns, and bookings," and orders:write covers exchanges, returns, and booking changes.
- auth.scope\_hints. Hints about what each scope allows, keyed by scope name, with two named parts: changes and personal\_data. In the example, orders:read carries changes "none" and personal\_data true, and orders:write carries changes "irreversible" and personal\_data true. A business writing its file has to grade its own scopes this way, in public, before any agent asks for them.
- web.disabled. Defaults to false. True means the company asks personal agents not to browse its website, and to use its company agent and APIs instead.
- web.unscoped. Defaults to false. True means the website does not apply the company's other scopes, so the poppy:browser-sign-in scope gives the account's full access there.
- tasks. An endpoint, an HTTPS URL, where personal agents get the tasks the company chose not to offer through the protocol, the skills it publishes, and where to send feedback.
- extensions. The extensions the company supports, keyed by name, with an entry for each version it supports. Section 3.3 adds the form: each name maps to a list of version entries, plain names are reserved for extensions defined with the protocol, and anyone else must start an extension name with a domain they control.

One form warning, because it is the easiest mistake in the file: agent protocols and apis entries do not use the same word for their address. An agent protocol entry carries an endpoint. An apis entry carries a url. The validator's schema check enforces the section 3.1 forms, as the run below shows.

## The specification's own example, in short

Section 3 prints a complete example document for a fictional Example Company at example.com. Its shape, with descriptions shortened here and the full text on the specification page:

- protocol\_version "1.0", and no supported\_versions, so 1.0 is the only version offered.
- organization: name "Example Company", domain "example.com", and a logo\_uri.
- auth with no issuer named, scopes as an object with four entries (orders:read, orders:write, addresses, and poppy:browser-sign-in), and scope\_hints grading the first three.
- agent with one protocol entry, type "poppy", at an HTTPS conversations endpoint.
- web with a browser\_session\_endpoint, tasks with an endpoint, and apis with two entries, one openapi and one mcp, each with a url.
- No extensions entry at all, which the field table allows.

This is the document the validator run below used, copied from the specification page on November 15, 2026.

## The validator is not a web page

Both launch posts point at a validator, and a reader could reasonably expect a form on a website: paste a domain, get a grade. That is not what the kit ships. There is no validator page or form on personalagentprotocol.org. The validator is a command-line program inside the company implementation kit, at validate/index.ts in the kit's skill folder on GitHub. Its README calls it the "Poppy Company validator." It needs Node 22.18 or later, has no dependencies and no install step, and it acts as a test personal agent against a company's live deployment.

Its commands, in the README's terms: survey <url> is read-only, reports what a domain already publishes, and sends only GET requests. check [url] runs the checks and writes results to .poppy/last-results.json. keygen creates the test personal agent identity, including a private key file the README says never to host or commit, plus agent.json and jwks.json files the tester hosts at a public HTTPS address. report drafts an implementation report from the latest results. Exit codes: 0 when no MUST check fails, 1 when one does, 2 for a usage error. A SHOULD that is not met is a warning and does not change the exit code.

What it checks is grouped by the kit's four milestones, and each check quotes the requirement it tests:

- Milestone 1, Foundation: discovery (the poppy.json itself), metadata (the issuer, from the protected resource metadata, and its OAuth server metadata), session (the Session header at resources), and assertion (client assertions at the token endpoint).
- Milestone 2, Interfaces: OpenAPI documents, MCP servers, the conversation endpoint, the tasks endpoint, the feedback endpoint, and the browser-session endpoint.
- Milestone 3, Sign-in: only what needs no real sign-in, such as an unknown sign\_in\_id at the token endpoint. The README states the rest of sign-in is checked by hand against the kit checklist.
- Milestone 4, Extensions: only what a run that declares no extensions sees, meaning no extension content, including operations, in any conversation response.

The safety limits are printed in the same README. The validator never calls an API operation other than the GET named with its probe option, never gets a token, never signs anyone in, and never joins a browser to a Session. Every URL must be HTTPS, a run makes at most 400 requests, and conversation tests carry only the text "Validator test message. Please ignore." It also works against production, the README notes, but it starts real Sessions and sends test messages, so a test environment is preferred.

## The run this site actually did

On November 15, 2026, this site cloned the kit from its GitHub repository and ran the validator in its offline mode, check --file, against the specification's own Example Company document, copied above. Offline mode checks a local poppy.json against the schema and field rules, with no network requests.

The result, Foundation milestone: 7 passed, 0 failed, 0 warnings, 7 skipped. The checks that passed include the document being a JSON object, its fields having the forms section 3.1 describes, the protocol version matching the version this validator checks, at least one of agent, apis, or web being present, and the sign-in and browsing consistency checks. The 7 skipped checks are the network ones: HTTPS serving at the well-known path, redirect behaviour, the supported\_versions documents, and whether organization.domain matches the host that served the file. Offline, there is no host, so the validator says so instead of guessing.

Field note

The pass proves less than it looks like, and this post keeps it at that size. It shows the specification's own example is written in the forms the kit's schema enforces, which was not a given: the file uses endpoint for agent protocols and url for APIs, an object for scopes, and an object for scope\_hints. Any of those written the other way fails the schema check.

It does not show that any real company's deployment passes, because no live company file was checked in this run. The full check mode needs a live deployment and a hosted test-agent identity, and the protocol's own demo addresses gave this site nothing to test against: on November 15, 2026, the demo agent site, its /.well-known/poppy.json, and the protocol inspector site all returned Not Found.

Caution

Third-party web pages that call themselves Poppy validators turned up in the November 15 searches. They are not the kit validator, they are not linked from the specification or the kit page, and this site did not use them. A business checking its own file should run the program from the kit's repository, in a test environment, and read the README's key-handling note before the keygen step, not after it.

## Staged adoption: website first, sign-in last

The guides page for companies orders the work in one sentence: each capability is a separate choice, so start with the website, then add the agent, the APIs, and the sign-in as you need them. The kit turns the same order into four milestones, and tells the implementer to run the validator after each one, since it checks that milestone's requirements and lists what is missing.

1. Foundation. Publish a poppy.json that lists a website and any APIs the company already has. Publish the OAuth server metadata. Verify the Session header at resources.
2. Interfaces. Connect the existing interfaces: OpenAPI, MCP, conversations, tasks, feedback, and the browser session. Test them.
3. Sign-in. Mediated Sign-In, authorization code with PKCE, direct sign-in, and device sign-in. Test sign-in.
4. Extensions. UCP checkout, operations, links, disclosures, and browser control. Test the extensions.

The order has a practical consequence for Muse users. The first stage a business can ship is a file that points at its ordinary website, with no sign-in and no API. That is also the stage with the least for an agent to do beyond browsing. A partner count, including the 100-plus figure in Sierra's post, does not say which milestone any named company has reached, and neither launch post breaks the count down by stage.

## Sign-in and Sessions, as the file declares them

Sign-in is OAuth 2.0. A company uses its existing OAuth server if it has one, and the specification says a company without one can use the server in the kit skill. The personal agent uses the authorization code flow with PKCE, requests the scopes listed in auth.scopes, and signs the user in on the company's own page. Direct Sign-In is the user approving access in their browser. Device Sign-In is a link and a code the agent shows the user, for sign-in on any device. Mediated Sign-In, a first-party app flow, is already marked as retiring: the extension page says it will stop working on March 17, 2027, and the roadmap lists dropping it.

Separate from sign-in, every request carries a Session. A Session is a signed JWT sent in the Poppy-Session header, naming the session and a user ID that is different at each company, signed with a short-lived key. ES256 is the baseline signature and PS384 is recommended, and client assertions must expire at most five minutes after they are issued. Section 11 of the specification opens its security part with a sentence a business should read before it celebrates the file: a company must not trust a personal agent. It verifies Sessions and checks scopes instead.

## The extensions a file can name

Six extensions are published with 1.0, each with its own page, and a company lists the ones it supports under extensions in poppy.json.

- ucp: checkout through the Universal Commerce Protocol. The company declares a checkout endpoint, the agent sends a checkout request, and the company returns a checkout URL. The extension page states the boundary in one line: UCP is a protocol for checkout, not a payment method, and the company must support UCP checkout to use it.
- operations: the company exposes named operations, such as a way to place an order, each with a name, a description, and parameters.
- links: the company provides links to the agent, each with a url and an optional title.
- disclosures: the company discloses information to the agent, such as its terms of service, as items with a url and a title.
- browser-control: the agent can ask the browser to do things, such as click a button or fill in a form.
- mediated-sign-in: the company can ask the user to sign in through Mediated Sign-In. Retiring March 17, 2027, per its own page.

The roadmap adds what 1.0 does not have: signed approvals, self-hosted personal agents, dropping Mediated Sign-In after its retirement date, and payments. Payments being a roadmap topic, in the protocol's own document, is the check on any claim that Poppy 1.0 settles how agents pay.

## Follow-through since November 13: nothing new in its own name

This site checked on November 15, 2026 for the three follow-ups the launch left open, using DuckDuckGo. A Meta primary beyond the Muse blog post: none found. Searches against Meta's own domains returned no Poppy page, and wider results were the Sierra post and secondary coverage. An in-app sighting of Poppy behaviour in Muse: none found. No screenshot, user report, or app interface evidence appeared. One Gate.com result dated November 15 repeats the claim that Muse searches for Poppy by default, but opening it landed on a compliance page, so it is carried here as an unverified snippet and nothing more. A partner announcement in the partner's own name: none found for Mercury, Synchrony, Turkish Airlines, or Shopify since November 13. The live column for Poppy still rests on Sierra's post and Muse's post, both dated November 13, both read in full for Part 1.

Three standing items hold flat beside this post. Expedia in Muse is still hotels only on the Skift record of November 9, with flights not verified. Spaces sharing is still not live: Meta described it on November 6 as exploring ways to share. Muse calling businesses, published on this site on November 14, is paid and US only. A poppy.json on a company's site changes none of those rows for a Muse user today, because no source checked shows what a Muse user sees when Muse finds one.

## The question for readers

If a business you use published a poppy.json tomorrow, what should Muse be allowed to do with it: browse, book, or buy? And what should it never do without asking first? The file itself forces a version of that question on the business, in auth.scope\_hints, where orders:write has to be graded as a change that cannot be undone. Answers that name the action and the line, for a named kind of business, will shape the November 23 recheck more than another partner count will.

## Quick answers

Where does poppy.json live?

At https://<domain>/.well-known/poppy.json, served over HTTPS as application/json. Specification section 3: if the company has no poppy.json, it is not part of the protocol.

Which poppy.json fields are required?

Two: protocol\_version and organization, per the section 3.1 field table. The company must also list at least one of agent, apis, or web. Everything else in the table is optional, except auth.issuer, which is required when the domain's protected resource metadata lists more than one authorization server.

What is the smallest working poppy.json?

One with protocol\_version, organization, and web alone. The guides call a web-only file the cheapest path for a company whose website already supports sign-in, and a personal agent will use the website, not the APIs.

Is the Poppy validator a website?

No. It is a command-line program in the company implementation kit on GitHub, run with Node 22.18 or later. Its commands are survey, check, keygen, and report, and it checks a deployment in four milestone groups: Foundation, Interfaces, Sign-in, and Extensions.

Did the specification's own example pass the validator?

Yes, in the offline run this site did on November 15, 2026: Foundation checks, 7 passed, 0 failed, 7 skipped. The skipped checks need a live host. No live company deployment was validated in this post, and the protocol's demo sites returned Not Found the same day.

Does a poppy.json mean Muse can buy things at that company?

No. The file declares channels and scopes. Checkout exists only through the UCP extension, which the company must support and declare, and the protocol's own roadmap still lists payments as an open topic.

Has any Poppy partner announced 1.0 in its own name?

Not in the November 15, 2026 checks. No announcement from Mercury, Synchrony, Turkish Airlines, or Shopify in its own name was found. Synchrony's own Poppy items are from October 2026, before the 1.0 release.

## Frequently Asked Questions

**Q: Who publishes poppy.json, Sierra, Meta, or the business itself?**

A: The business itself, on its own domain. Poppy is Sierra's Personal Agent Protocol, published with industry partners including Meta. Muse's post, read in full for Part 1, describes the same file from the business side: a business publishes poppy.json to tell personal agents what it offers and how to reach it. The implementation kit is for companies, and the kit page notes a kit for personal agents has not been published yet.

**Q: What happens on a site with no poppy.json?**

A: On the specification's terms, that company is not part of the protocol, and a personal agent must not assume any service, endpoint, or method there. Sierra's launch post says Muse looks for Poppy first on every site it visits. What Muse does next on a site with no file is not described in either launch post, and no in-app sighting had been found by November 15, 2026.

**Q: Why does auth.scopes use descriptions instead of a plain list?**

A: Because that is the form section 3.1 defines: scope descriptions keyed by scope name, in the same form as an OpenAPI OAuth 2.0 security scheme. The validator's schema check enforces that form. A company also lists scopes a second way, in scopes\_supported in its protected resource metadata or its issuer's metadata, and the agent uses the union of the lists.

**Q: What does the validator not check?**

A: Two limits are printed in its own README. Sign-in is checked only where no real sign-in is needed, and the rest is checked by hand against the kit checklist. Extensions are checked only from the outside, as what a run declaring no extensions can see. It also never gets a token, never signs anyone in, and never joins a browser to a Session, by design.

**Q: Can this site run the validator against a named company for me?**

A: The survey command is read-only and sends only GET requests, so it is the safe one to run against a live domain. This post ran no live check, because the November 23 recheck is the dated place for the first named one. The full check mode starts real Sessions and sends test messages, and the README prefers a test environment for it, so it is not a tool to point at a company that has not asked for the test.

**Q: Is poppy.json the same thing as a Muse connector?**

A: No, and Part 1 kept the two apart on Muse's own text. A connector links a specific service into Muse, through Meta's review for verified connectors. poppy.json is a file any company publishes on its own site under an open protocol, with no Meta review named in the specification or the kit. A company can do either, both, or neither.

**Q: When will this site check Poppy again?**

A: November 23, 2026, for the two open ledger rows: an in-app sighting of Poppy behaviour in Muse, and a partner announcement in a partner's own name. The same check will run the validator's survey command against the first live company poppy.json it can name, and publish the result with that date either way.

## Sources

- Personal Agent Protocol specification, version 1.0, personalagentprotocol.org/docs/1.0/spec. Read in full on November 15, 2026. Section 3: poppy.json at /.well-known/poppy.json over HTTPS, no file means not part of the protocol, only what a document declares can be relied on, and discovery through RFC 9728 protected resource metadata and RFC 8414 issuer metadata. Section 3.1 field table: protocol\_version and organization required, at least one of agent, apis, or web, auth.issuer conditional, and the optional fields and forms printed in this post, including scopes as descriptions keyed by scope name and scope\_hints with changes and personal\_data. Section 3.3: extensions keyed by name with an entry for each version. Section 3.4: supported\_versions as a map to each version's document, on the same host, with the same domain and issuer. The complete Example Company document in section 3, used for the validator run. Sections 4 to 6 and 11 as cited: OAuth 2.0 with PKCE, the Poppy-Session JWT header, ES256 baseline and PS384 recommended, and the instruction that a company must not trust a personal agent.
- Personal Agent Protocol guides, personalagentprotocol.org/docs/1.0/guides, and the company implementation kit, personalagentprotocol.org/kit/company. Read on November 15, 2026. Guides: each capability is a separate choice, start with the website, then add the agent, the APIs, and the sign-in; a web-only poppy.json is the cheapest path where the website already supports sign-in. Kit: the four milestones (Foundation, Interfaces, Sign-in, Extensions), run the validator after each milestone, and a kit for personal agents not yet published.
- Poppy Company validator, README and program, github.com/personal-agent-protocol/personal-agent-protocol, skills/implement-personal-agent-protocol/validate. Read and run on November 15, 2026. README: commands survey, check, keygen, and report; checks grouped by milestone as printed in this post; exit codes 0, 1, and 2; Node 22.18 or later, no dependencies; safety limits including no token, no sign-in, no browser join, at most 400 requests, and a preference for test environments. Run by this site, November 15, 2026: check in offline --file mode against the specification's Example Company document, Foundation result 7 passed, 0 failed, 0 warnings, 7 skipped, the skipped checks being the network ones.
- Personal Agent Protocol extensions pages and roadmap, personalagentprotocol.org/docs/1.0/extensions and /docs/roadmap. Read on November 15, 2026. Six 1.0 extensions: ucp, operations, links, disclosures, browser-control, and mediated-sign-in. UCP page: UCP is a protocol for checkout, not a payment method. Mediated Sign-In page: retiring, stops working March 17, 2027. Roadmap: signed approvals, self-hosted personal agents, dropping Mediated Sign-In, and payments.
- Sierra, "Releasing Personal Agent Protocol 1.0," November 13, 2026, by Bret Taylor and Clay Bavor. Re-read in full on November 15, 2026. The starting point for this post only: Poppy now on for everyone who uses Muse, Muse looking for Poppy first, Shopify enabled for every merchant, Mercury, Synchrony, and Turkish Airlines going live, more than 100 design partners, and an implementation kit with a validator at personalagentprotocol.org.
- Muse blog, "More Ways for Muse to Work With Businesses," muse.ai/blog/poppy-personal-agent-protocol. Read in full on November 14, 2026 for Part 1, and carried at that weight here; a fresh fetch on November 15, 2026 did not return the page. Muse as the first personal agent to support Poppy, poppy.json named as the file a business publishes, website-only setup without customer sign-in, OAuth grant and revoke on the business's own page, and Meta verified connectors as a separate review track.
- DuckDuckGo checks, November 15, 2026, run for this post. Queries on a Meta primary beyond the Muse blog post, an in-app sighting of Poppy behaviour, and partner announcements from Mercury, Synchrony, Turkish Airlines, and Shopify in their own names, plus site searches for the kit and validator. None of the three follow-through items was found. The protocol demo addresses (the demo agent site, its /.well-known/poppy.json, and the protocol inspector) returned Not Found on November 15, 2026. One Gate.com result dated November 15 was not opened past a compliance page and is carried as an unverified snippet only.
- Baseline check: this site's September 2026 research file contains no Poppy material, because the protocol was first announced in October 2026. Nothing in this post rests on the baseline file.
- Editorial checks, November 15, 2026: standing facts held flat from this site's November record. Expedia in Muse hotels only, per Skift, November 9, with flights not verified. Spaces sharing described by Meta on November 6 as exploring ways to share, not live. Muse calling businesses is paid and US only, per this site's November 14 post.
