来源：https://optimuslabs.io/research/briefings/meta-muse-dictation-endpoint-hijack
取文：2026-11-27，直接下载（main 容器抽取；攻击链示意图按页面原文位置补回）

First a user-writable dictation setting redirected Muse's audio and session. Then a SKILL update rewrote its memory and cut a saved password into an attacker's page. Both borrowed trust Muse already gave.

![Two Muse attack chains. Chain 1, September 2026: code running as the Mac user rewrites the hidden dictation setting, voice and session go to an attacker, who sends back instructions Muse acts on. Chain 2, November 2026 update: a clean-looking SKILL sets up a background git pull, a later update rewrites AGENTS.md and MEMORY.md, Muse treats Ctrl+X as clear the field, and a saved password is pasted into an attacker page. Both spend the reach Muse was already granted. attacker.tld is illustrative, not an indicator.](images/img-01-6d5523.png)

## Key takeaways

- Patrick Wardle demonstrated a local proof of concept against Meta Muse for macOS. A same-user process could change an undocumented dictation endpoint, capture the agent's session material, and return instructions for Muse to execute with its existing reach. Meta hot-fixed the issue. This was not a remote exploit or a confirmed breach. In November 2026, Harsha Gundala reported a second chain: a SKILL update rewrote Muse's memory files, and the agent then cut a saved password into an attacker's page. Meta blocked keyboard shortcuts in its managed browser; the researcher says related variants are still unpatched.
- Blast radius: The proof of concept required code already running in the logged-in user's macOS session. From that foothold, the attacker could redirect Muse's dictation and potentially use the agent's approved access to files, mail, calendar, WhatsApp, microphone, camera, location, and a linked iPhone. The reachable scope depends on each user's grants and connections; this is not evidence of exploitation in the wild.
- HIGH · AGENT HIJACK

## Timeline

1. Meta Muse launches for macOS

   Early September 2026
2. Wardle publishes the local proof of concept

   2026-09-21
3. Meta hot-fixes the affected setting

   After disclosure

   The supplied brief describes the response as within hours; no fixed version is specified.
4. Gundala describes a second, patched chain: a SKILL update poisons Muse's memory and a cut shortcut leaks a saved password

   2026-11-16

Blast radius
:   The proof of concept required code already running in the logged-in user's macOS session. From that foothold, the attacker could redirect Muse's dictation and potentially use the agent's approved access to files, mail, calendar, WhatsApp, microphone, camera, location, and a linked iPhone. The reachable scope depends on each user's grants and connections; this is not evidence of exploitation in the wild.

## Summary

An undocumented preference named endo\_voyager\_dictation\_endpoint determined where Muse sent spoken requests for cloud transcription. Wardle showed that another process running as the same user could rewrite it without admin privileges. A redirected endpoint could receive voice audio, a transcript, and Muse session material, then return attacker-chosen text that Muse treated as a user instruction. The weakness sits at the boundary between local configuration and a broadly permissioned agent, not in a remote server breach. Meta issued a hotfix after the September 21 disclosure; the supplied brief reports no CVE or formal advisory.

## Am I affected?

Any single yes means treat this as an incident.

- ?Was Meta Muse for macOS installed before the September 2026 hotfix?
- ?Could untrusted code run in the same logged-in user's session, including through a malicious download or social-engineering lure?
- ?Was Muse's dictation endpoint preference changed to a host you do not recognize?
- ?Which device, account, and macOS permissions did the affected Muse installation hold?

Not affected if

- This proof of concept does not establish a remote, unauthenticated entry point into an otherwise clean Mac.
- A fully updated Muse install with no suspicious preference changes is outside the demonstrated pre-hotfix path.

The source documents do not identify a safe version number. Confirm the update through Meta's current release channel.

Update · Nov 16, 2026

## A second Muse chain: a SKILL update rewrote the agent's memory

A new chain, reported by Harsha Gundala, reached a saved password through a SKILL update.

In November 2026, researcher [Harsha Gundala described](https://x.com/harshagundal/status/2122383197602537960) a separate chain he reported to Meta, found the month before. It needed no local malware. A user installed an MCP server or SKILL that looked clean at review. Its installer faked the user's consent and quietly set up a background git pull.

A later update to that repository rewrote AGENTS.md and MEMORY.md. Muse loads both files on every turn as the user's own preferences. Owning them let the attacker invent "user" permissions without touching the web content that Muse's prompt-injection filters scan.

From there, the poisoned memory told Muse's browser helper that Ctrl+X meant "clear the field". When Muse filled in a saved password, the helper cut it to the clipboard, pasted it into a page the attacker controlled, then finished the login normally. Neither the agent nor the user saw a password move. Meta patched this path by blocking keyboard shortcuts in its managed browser. The researcher says related variants are still unpatched and has not published them.

Our view: both Muse chains borrow trust the agent already gives. The first rewrote a setting, the second rewrote memory. In both, the attacker didn't need to beat Muse's sandbox. Changing what Muse treats as the user's own word was enough. Any SKILL, MCP server or installer that can write to an agent's memory or instruction files deserves the same review as code that can run commands. Our [5-minute SKILL and plugin check](/guides/owasp-top-10-for-agentic-skills#check-a-plugin) is a starting point.

[See how Optimus Labs secures SKILLs](/use-cases/secure-skills-hub).

## The local foothold came first

The attack starts with a process already running as the Mac user. Wardle's not-a-mused proof of concept did not remotely break into Muse or require an administrator prompt. A ClickFix-style lure or local malware is a plausible entry path, not a reported delivery campaign in this case.

That process rewrites endo\_voyager\_dictation\_endpoint, an undocumented Muse preference controlling the cloud dictation destination. The attacker-controlled address in the diagram is illustrative, not a live indicator.

## The agent crossed the trust boundary

When the user spoke to Muse, the redirected endpoint could receive the audio, transcription data, and session material. The attacker could return text for the agent to interpret as the user's request, rather than gaining each macOS permission individually.

The permission set is the multiplier: files, microphone, camera, location, connected accounts, and a linked iPhone were in scope of the demonstrated agent capabilities. Actual access depends on what the user had approved and connected.

## What the demonstration does and does not prove

The researcher demonstrated a working attack path against a privileged client. The supplied reporting does not establish a customer breach, an in-the-wild campaign, or a remote zero-click compromise. Meta described the practical risk as low because same-user code must be present and issued a hotfix.

The lasting lesson is narrower and more useful than 'the cloud failed': a local setting can redirect an agent that already has trusted access. Inventorying installed agents and their grants matters alongside cloud isolation and connector controls.

## Remediation

Contain now · 0-24h

- Confirm the Muse hotfix is installed on managed Macs; remove unsanctioned installations.
- Check Muse's endo\_voyager\_dictation\_endpoint preference for an unexpected host. Preserve evidence before changing a suspicious setting.

Investigate · 24-72h

- Review local preference-change telemetry and outbound dictation connections for affected Macs. Investigate the process that made a suspicious change rather than treating the preference alone as the entry point.
- If redirection is confirmed, revoke Muse sessions, re-authenticate connected services, and review the linked iPhone and account activity in scope of that installation.

Harden the agent surface

- Inventory desktop agents, their connected accounts, device links, and approved macOS permissions by owner.
- Limit unnecessary grants and manage local agent configuration where the vendor and device-management tooling allow it.
- Monitor destination changes and unusual agent actions as behavior, not only as known CVEs or malware hashes.

## Indicators

- `Configuration key: endo_voyager_dictation_endpoint`
- `Behavior: Muse dictation endpoint changed to an unexpected host`
- `Behavior: outbound dictation traffic to an unrecognized destination following a Muse preference write`
- `Research proof of concept: not-a-mused (not an indicator of malicious activity by itself)`
- `No CVE assigned in the supplied September 2026 research brief`
- `Behavior (second chain): a SKILL, MCP server or installer that schedules background git pulls in the agent workspace`

## Sources

- [Patrick Wardle: not-a-mused proof of concept](https://github.com/pwardle/not-a-mused)
- [The Verge: Meta patches Muse zero-day exploit](https://www.theverge.com/tech/998679/meta-muse-patch-zero-day-exploit-ai-agent)
- [Malwarebytes: Muse assistant zero-day analysis](https://www.malwarebytes.com/blog/bugs/2026/09/metas-muse-ai-assistant-has-a-zero-day-that-can-turn-it-into-a-mac-backdoor)
- [The Hacker News: undocumented Muse setting](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html)
- [Harsha Gundala: memory poisoning and Ctrl+X password capture in Muse](https://x.com/harshagundal/status/2122383197602537960)

## Sourcing & confidence

Confirmed by the vendor

- Patrick Wardle's public not-a-mused proof of concept demonstrates the local same-user attack path; Meta's hotfix and its low-practical-risk characterization are covered by The Verge and the reporting linked below.
- The supplied Civilizations deck and one-page diagram describe the agent permissions and containment sequence. The diagram's attacker.tld address is illustrative.

Assessed by Civilizations

- The second chain is described by the researcher who found it. Meta's patch (blocking keyboard shortcuts in its managed browser) is as he reports it; we have not seen a Meta advisory for it.
- The broader enterprise blast radius depends on each installation's granted permissions and connected services. It is not a measured victim count.
- No known in-the-wild use is reported by the supplied brief. Absence of a CVE is a tracking gap, not proof of exploitation.

Related use cases

- [Shadow agent discovery](/use-cases/shadow-agent-discovery)
- [Secure SKILLs](/use-cases/secure-skills-hub)
- [Detect undesired activity](/use-cases/detect-undesired-activity)
