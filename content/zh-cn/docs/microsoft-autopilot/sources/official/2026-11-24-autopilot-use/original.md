来源：https://learn.microsoft.com/en-us/copilot/autopilot/using
取文：2026-11-28，直接下载

Use Autopilot (Frontier)

[This article is prerelease documentation and is subject to change.]

Important

- Access to Autopilot (Frontier) requires the applicable **[Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)** enrollment, preview assignment, and participation terms. Frontier enrollment alone doesn't enable every preview feature. Frontier previews are subject to the applicable preview terms of your customer agreements, and their availability and capabilities may change.
- This feature is in preview.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Use Autopilot to delegate a task, repeat work on a schedule, and review results. To create your Autopilot first, see [Get started with Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started).

In Microsoft Copilot, select **Home**, and then select your Autopilot's name in the left navigation to open its overview. Use **Plugins** to enable additional capabilities, or select your Autopilot’s name in the left navigation, expand the pane on the right, and select the **Routines** tab, where you can pause, edit, run, or delete recurring work. Controls can vary during the preview.

## Work from the Autopilot view

After clicking on Autopilot on the left navigation, use the expand panel icon in the top right hand side to open your Autopilot’s management panel.
The **Overview** tab shows files, recent chats, Teams and Outlook conversations with your Autopilot. The plus sign enables you to start a new chat.

1. On the **Home** tab, select your Autopilot's name in the left navigation.
2. Open the management panel and use the plus sign to start a new chat.
3. Describe the outcome you want, the sources to use, and limits on actions.
4. Submit the message using the send control.
5. Answer clarifying questions.
6. Check the completed result and ask for changes if needed.

For example: "Review this week's launch discussion and draft a status update. List unresolved decisions and their owners. Don't send the update."

Provide a source link or attach supported context when it helps identify the right file or conversation. Autopilot can only use sources allowed by the acting account, available tools, and organizational policy.

### Review sensitivity labels

Autopilot can recognize labels on supported Microsoft 365 content and display a conversation label. Labeled content isn't excluded from what Autopilot can read, and a new file might not inherit the label. Data loss prevention coverage is limited during the preview. Check the final file's classification, access, and destination before sharing it.

### Track work on the timeline

Use the **Activity** view to follow work; don't treat it as a complete administrative audit log.

1. Use the filter to select the type of activity you want to see.
2. Choose **Type** (Chats, Routines, Files, Approvals), **Source** (Teams, Outlook), or **Status** (Needs you, In progress, Didn’t finish, Completed).
3. Open the relevant item to review its conversation, decisions, and activity.
4. Confirm any external effect in its destination, such as the saved file, sent message, or calendar event.

You can also redirect or stop work in progress by replying in its conversation.

## Set up a routine

Use natural language to tell Autopilot what you want to achieve, and Autopilot suggests the relevant routines.
Your routines are private to you.

Autopilot decides how to handle a request:

| Request | How Autopilot handles it |
| --- | --- |
| Work it can finish now, such as drafting a reply | A task in the current conversation |
| Timed work with an outcome or time/ event-based trigger. | A routine |

If an existing routine already does exactly what you asked, Autopilot reuses it. Otherwise, it creates a new routine rather than changing an existing one.

### Manage routines

Use **Routines** in the right panel to find your active and paused routines. Each **Routine** shows its schedule and a switch that turns scheduled runs on or off. Select the three dots for these options:

| Option | What it does |
| --- | --- |
| **Run now** | Starts the routine immediately, including any actions in its instructions. |
| **Edit** | Enables you to edit the routine. |
| **Delete** | Removes the routine. |

Pausing future runs doesn't reverse work already completed. When instructions change, review the saved instructions and permissions rather than assuming an earlier conversation updated them.

## Save and verify deliverables

Specify the OneDrive or SharePoint destination you intend Autopilot to use. The acting account needs access to that location.

| Work | Where it's saved |
| --- | --- |
| Your conversations and personal work | Your OneDrive |
| Temporary files used during a task | Not kept after the task finishes |

Check that the final file exists where requested, opens under the intended account, and has appropriate access and labeling. A file in Autopilot's working environment isn't necessarily uploaded or shared. Reported partial completion, such as a created file whose access couldn't be verified, needs review before retrying.

## Review usage and limits

Autopilot is billed on usage in Copilot Credits through a spending policy that your administrator manages. The **Credits in use** indicator at the top of the Autopilot page shows that credits apply. Select it for details. Autopilot doesn't show a count of credits used or remaining; ask your administrator for usage information.

If you aren't covered by a spending policy, or the policy reaches its limit:

- Autopilot can't run automations, monitor work, or respond to new requests.
- Autopilot doesn't show you an explanation. If it stops responding, contact your administrator.
- Automations can show as paused until credits are available.

For licensing and access, see [Autopilot requirements](https://learn.microsoft.com/en-us/copilot/autopilot/requirements).

## Provide feedback

Your feedback helps Microsoft improve Autopilot.

1. Under a response, select **I like something** or **I don't like something**.
2. If you select **I don't like something**, describe what happened and what you expected. Include a screenshot if it helps.
3. Review the prompts, responses, and diagnostic data that are included before you submit. Don't include sensitive information.

You can also ask Autopilot to log a bug and describe the problem. For more information, see [Providing feedback about Microsoft Copilot with Microsoft 365 apps](https://support.microsoft.com/topic/c481c26a-e01a-4be3-bdd0-aee0b0b2a423).

## Related content

- [Autopilot overview](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [Get started with Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)
- [Autopilot scenarios](https://learn.microsoft.com/en-us/copilot/autopilot/scenarios)
- [Autopilot common questions](https://learn.microsoft.com/en-us/copilot/autopilot/faq)
- [Application card for Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)

---
