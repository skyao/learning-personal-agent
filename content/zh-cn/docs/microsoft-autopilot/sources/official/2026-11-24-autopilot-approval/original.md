来源：https://learn.microsoft.com/en-us/copilot/autopilot/approval
取文：2026-11-28，直接下载

How Autopilot reviews actions

[This article is prerelease documentation and is subject to change.]

Important

- Access to Autopilot (Frontier) requires the applicable **[Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)** enrollment, preview assignment, and participation terms. Frontier enrollment alone doesn't enable every preview feature. Frontier previews are subject to the applicable preview terms of your customer agreements, and their availability and capabilities may change.
- This feature is in preview.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Autopilot uses a second AI model that reviews Autopilot's actions before they run. It compares each action with what you asked for, including the steps your request clearly implies and any limits you set, such
as "view-only" or "don't send it yet." The same rules apply whether Autopilot acts as you or with its own identity.

| Type of action | What happens |
| --- | --- |
| Reading, searching, and drafting | Runs without interruption. A small share of these actions is spot-checked. |
| Sending, sharing, deleting, or changing mail, calendars, files, chats, or content in other apps; creating or changing an automation | The automatic review system decides. If the action matches your request, it runs without an approval request. If it doesn't match, or the automatic review system can't check it, you get an approval card. |
| Payments and other sensitive browser steps | Always need your approval, even if you asked for the action. |

Only your own messages count as requests. Instructions that appear in an email, a document, or a web page don't authorize an action, even if they claim to come from you. Autopilot doesn't ask you to confirm actions by replying in chat. If you approve a draft on your own, for example by writing "Looks good, send it," the system treats that as your request.

When you set up an automation, the automatic review system checks the automation against your request. During a run, it checks each step against the automation's saved instructions. If a step doesn't fit, the approval card appears in the automation's delivery chat. Some recurring permissions always need your review, even if the check recommends approval.

There are no user or administrator settings for the automatic review system in this release.

### Set permissions

Your instructions, authorized accounts, action permissions, and organizational policy constrain what Autopilot can do. Autopilot can complete tasks without asking you at each step. Before it takes an action, an
automated check decides whether the action can go ahead or needs your approval.

### Respond to an approval card

An approval card appears in your one-on-one Teams chat with Autopilot. If you made the request in Microsoft Copilot, the card also appears there, and answering it in one place updates the other. If you don’t respond before the approval request expires, the action waiting for that approval doesn’t run. The rest of the task continues while it waits. One card can cover several related actions.

Each card shows:

- What will happen and who it reaches, with each person's name and email address. People outside your organization are marked **External**.
- A read-only preview of any message that will be sent.
- Your request, or the name of the automation.
- **See more**, which shows technical details such as the app used and whether Autopilot acts as you or with its own identity.
- Why you're being asked, except for payments and other actions that always need approval.

| Reason on the card | What it means |
| --- | --- |
| "This action may go beyond what you asked for. Only allow it if it's what you intended." | The action doesn't fit your request. For example, it includes an extra step or a recipient you didn't mention. |
| "Please confirm this action matches what you asked for before allowing it." | The system isn't sure that the action fits your request. This is common for broad requests, such as "Clean up my inbox." |
| "The security check couldn't finish. Please review this action before allowing it." | The system couldn't check the action. |

To respond:

1. Check the actions, recipients, destination, and acting account. Select **See more** for details.
2. Select **Allow** to run everything on the card once, or **Deny** to cancel it. There's no option to always allow an action, so a similar action later is checked again.
3. Review the result after it runs. If you denied the card or the action was blocked, don't treat the request as completed.

Open the management panel and select **Activity** to review approval events alongside other actions. Entries can identify actions approved automatically or approved by you. An approval isn't proof of completion; verify the result in its destination.

Autopilot can interpret a request more broadly than you intended. For example, a request to clean up old project files could affect more content than you expect. Before you allow an action, check exactly which files, data, people, and communications are involved.

### Review Autopilot settings

Open the management panel and select **Settings**. Here you can find **Name and appearance**, review **Memory**, and view listed devices under **Computers**, including their connection status.

---
