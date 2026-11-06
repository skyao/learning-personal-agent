来源：https://discuss.google.dev/t/gemini-spark-cannot-write-to-any-google-sheets-sheets-agent-call-blocked-by-policy-check/404155
取文：2026-11-06，直接下载

[vailon](https://discuss.google.dev/u/vailon)

October 13, 2026, 4:49pm

1

Hello,

I am experiencing a persistent issue with Gemini Spark where all write operations to existing Google Sheets fail. Spark can read spreadsheet content, but it cannot append a row or otherwise modify any tested spreadsheet.

This does not appear to be limited to a particular spreadsheet or file-sharing configuration.

What I have tested:

- The issue affects all Google Sheets I have tested.
- I have confirmed that I can manually edit and save the spreadsheets using my personal Google Account.
- I also tested a spreadsheet that was temporarily configured as “Anyone with the link can edit.” The Spark write operation still failed.
- I turned the Google Workspace connection in Gemini off and back on, but the issue persists.
- Spark can successfully read the spreadsheet content. The failure occurs only when Spark attempts a write operation.
- This is a personal Google Account, not managed by a Google Workspace organization.
- I am located in Hong Kong.

The failing internal tool shown by Gemini Spark is:

sheets\_agent:call

The reported error is:

tool “sheets\_agent:call” failed: InvokeTool stream for “sheets\_agent:call” failed: generic::aborted: Failed to verify file permissions: Blocking policy check failed for event: “” [PERMISSION\_DENIED]

Error summary:

Failing tool: sheets\_agent:call

Error status: generic::aborted

Error category: PERMISSION\_DENIED

Failure location: InvokeTool stream for “sheets\_agent:call”

Occurrence time: 2026-10-13, [insert exact time] HKT (UTC+8)

The issue does not look like a standard Google Sheets API authorization error. I did not receive a Google Sheets API HTTP 403 response such as “insufficientPermissions” or “The caller does not have permission.” Instead, the request appears to be aborted during Spark’s pre-execution file-permission verification and blocking-policy check, before the actual Sheets write operation is executed.

I also found a publicly indexed Gemini Community report involving Gemini Spark failing to edit Google Slides with the closely similar error:

“Blocking policy check failed for event: ‘’ [PERMISSION\_DENIED]”

That report described normal Drive access continuing to work while an advanced Spark sub-agent used for file editing failed. My case concerns Google Sheets and the failing tool is sheets\_agent:call, so I am not assuming the incidents are identical. However, the matching error pattern may indicate a broader Gemini Spark sub-agent, feature-policy, account-eligibility, or rollout issue rather than a spreadsheet-specific sharing-permission problem.

Could anyone confirm or help clarify the following?

1. Is Gemini Spark’s ability to write to existing Google Sheets through sheets\_agent:call currently supported for personal Google Accounts?
2. Is this capability available in Hong Kong, or is it subject to regional, account-level, or staged-rollout restrictions?
3. What type of policy can trigger the error “Blocking policy check failed for event” for a personal, unmanaged Google Account?
4. Is there any user-side remediation, such as a specific reauthorization process, permission reset, account setting, or reconnection procedure?
5. If this is a known issue or service incident, is there an issue tracker entry, status page, or recommended support channel?

I can provide the complete event ID, exact timestamps, screenshots, and a minimal non-sensitive test case privately if a Google representative requests them. I will not post OAuth tokens, passwords, private spreadsheet links, or health data publicly.

Thank you.

[Abel](https://discuss.google.dev/u/Abel)

October 14, 2026, 5:19am

2

I am getting the same error.  
tool “sheets\_agent:call” failed: InvokeTool stream for “sheets\_agent:call” failed: generic::aborted: Failed to verify file permissions: Blocking policy check failed for event: ‘…’ [PERMISSION\_DENIED]

[DHolloway](https://discuss.google.dev/u/DHolloway)

October 14, 2026, 12:44pm

3

The wording is telling, since “blocking policy check” sits within Gemini’s pre execution layer rather than the Sheets API itself. That tends to point toward an account eligibility or rollout restriction rather than something reauthorising would fix. Regional availability may also play a part in Hong Kong. Checking the Gemini status page for known incidents is worthwhile, and if nothing appears, filing a report with the event ID attached would be the next step.

[Desmond\_Lang](https://discuss.google.dev/u/Desmond_Lang)

October 14, 2026, 8:55pm

4

Same permission denied started for me yesterday…as they rolled out Argon…bad launch smh. I’m located in the US.

[vailon](https://discuss.google.dev/u/vailon)

October 15, 2026, 1:32am

5

This all kicked off when Spark was integrated into Chat. The sidebar’s become an absolute mess since the merge—regular chats and Spark tasks are all jumbled together, with no folders or labels to tell them apart.

[vailon](https://discuss.google.dev/u/vailon)

October 15, 2026, 1:34am

6

I’ve already sent a help request to Google, but with so many issues coming in, I doubt they’ll get back to me.

[vailon](https://discuss.google.dev/u/vailon)

October 15, 2026, 1:36am

7

“report with the event ID attached” , it has been done.

[Jeremy\_LaKosh](https://discuss.google.dev/u/Jeremy_LaKosh)

October 15, 2026, 8:14pm

8

This happened to me too. I’m in the US. I’m hoping it can get fixed soon.

[Edward\_Chu](https://discuss.google.dev/u/Edward_Chu)

October 15, 2026, 11:13pm

9

I had exactly the same issue and sent a help request. This is the response (See below). Am I missing something? This completely breaks the agentic capability, no? I am on a paid plan AND this worked before, now it doesn’t.

I have an update from our engineering team regarding your case.

According to their investigation, edits and assistance within Google Sheets should be done using the Gemini side panel rather than the standalone Gemini app. Using the side panel directly inside Sheets will provide the intended functionality for your workflows.

[vailon](https://discuss.google.dev/u/vailon)

October 16, 2026, 2:24am

10

Blocking Policy Check regression resolved + Feature Suggestion for automated telemetry dispatch

Hi everyone,

Following up on the recent incidents regarding `sheets_agent:call` returning `generic::aborted [PERMISSION_DENIED]` due to internal “Blocking Policy Check” failures (which started around early October 2026), I would like to report that the backend regression appears to be **fully resolved**.

### Verification Update

- **Tested at:** 2026-10-16 10:14 HKT
- **Environment:** Gemini Spark / Tasks mode appending rows directly into Google Sheets and updating Google Docs changelogs.
- **Result:** Direct write operations are now executing seamlessly without triggering policy intercept blocks. Temporary workarounds (such as forcing Markdown/CSV output via custom skills) can now be safely deactivated.

### Feature Suggestion: Automated In-Session Telemetry & Escalation for Agent Failures

During this outage, the biggest pain point was the friction in bug reporting: when an autonomous sub-agent encounters a platform-level intercept, it simply returns a cold trace/error to the end user, relying entirely on the user to manually capture logs, draft bug tickets, and submit them to community forums.

As Gemini Agents take on deeper, multi-step production workflows, I would like to propose a built-in feedback loop:

1. **Automated Incident Telemetry**: When a sub-agent tool call terminates on unexpected platform-level gates (e.g., policy aborts with Event IDs), the agent should be able to capture sanitized system traces automatically.
2. **One-Click Escalation Prompt**: The UI can prompt the user directly in-chat: *“A server-side tool execution failed (Event: ID). Would you like to submit this sanitized technical log directly to Google Cloud / Workspace engineering?”*
3. **Resolution Notification**: Once a platform hotfix is deployed, the agent or sidebar could notify affected workflows that automated actions have resumed, rather than requiring users to periodically run blind test writes.

This would drastically reduce the mean-time-to-detect (MTTD) for regressions in the agent toolchain and build stronger developer confidence in autonomous agent workflows.

Thanks to the engineering team for rolling out the hotfix!
