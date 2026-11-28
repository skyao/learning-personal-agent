来源：https://learn.microsoft.com/en-us/copilot/autopilot/overview
取文：2026-11-28，直接下载

Autopilot (Frontier) overview

[This article is prerelease documentation and is subject to change.]

Important

- Access to Autopilot (Frontier) requires the applicable **[Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)** enrollment, preview assignment, and participation terms. Frontier enrollment alone doesn't enable every preview feature. Frontier previews are subject to the applicable preview terms of your customer agreements, and their availability and capabilities may change.
- This feature is in preview.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Autopilot is a constant, cloud-based agent in Microsoft Copilot. Describe the outcome you want, the sources it should use, and boundaries for its actions. It can prepare documents, review accessible conversations, follow up on work, and run recurring tasks through automations.

Autopilot has its own workplace identity, memory, computer, and workspace. Each person can have one Autopilot. Saved context helps it continue work beyond a single conversation. It can run scheduled work while your device is off, subject to access, approvals, and service availability.

You work with Autopilot in Microsoft Copilot on the web or desktop, where it appears by name on the **Home** tab in the left navigation. It also uses a private one-on-one chat with you in Microsoft Teams for updates, questions, and approvals. Autopilot doesn't expand the data you can access.

## What can Autopilot do?

Autopilot combines conversation, recurring background work, and connected tools in one place:

- **Prepare work for review.** Request drafts, documents, presentations, or analysis using the tools available to your Autopilot.
- **Follow commitments.** Ask for unresolved decisions, upcoming deliverables, meeting preparation, or draft follow-ups.
- **Repeat a task.** Set up a routine with a schedule, complete instructions, and an intended delivery destination.
- **Work across Microsoft 365.** Use authorized Teams, Outlook, OneDrive, and SharePoint content within the permissions for the task. Autopilot has its own mailbox and calendar alongside yours, and it can share drafts into your existing OneDrive folders. It can also work with shared tasks in Microsoft To Do and Planner to track progress and follow-through.
- **Continue a project.** Use saved preferences and working context, while checking for changes to sources and requirements.
- **Review progress.** Open **Activity** to find running work, requests for your input, and routine results.

**Routines** can run on a schedule or when an event occurs.

## Start with an outcome

Describe the result you need, the people and sources involved, and any restrictions. For example, ask for a daily summary of unresolved launch decisions and draft follow-ups, without sending messages.

Autopilot plans and carries out the work using its available capabilities, without asking you at each step. Before it sends, shares, deletes, or changes something, an automated review compares the action with your request. Actions that match run; others wait for your approval. Review the actual result in its destination rather than treating an approval or progress message as proof of completion.

## Find your work

In Microsoft Copilot, select **Home**. Your Autopilot appears by name in the left navigation, alongside other Copilot areas such as **Plugins**.
You use these areas in the left navigation to work with Autopilot:

| Area | What you use it for |
| --- | --- |
| Your Autopilot's name | Open your main conversation to give instructions, ask questions, and review responses. From there you can also open your Autopilot’s management pane by expanding the icon in the top right corner. |
| **Plugins** | Select your Autopilot’s name to discover capabilities and manage the skills exposed in your experience. |

When you click on your Autopilot, use the expand panel button in the top right hand corner to expose additional areas to work with your Autopilot.

| Area | What you use it for |
| --- | --- |
| Area | What you use it for. |
| Overview | See and open files that your Autopilot has been working on, and your Autopilot Chat history. |
| Activity | Monitor the actions taken by your Autopilot, including active tasks, where it needs your inputs, and historical activities. |
| Routines | Select your Autopilot’s name in the left navigation, expand the pane on the right, and select the Routines tab, where you can pause, edit, run, or delete recurring work. |
| Settings | Edit your Autpoilot’s name and appearance, and review its memory and permissions. |

## Understand identity, context, and access

Autopilot's name, appearance, email address, and Microsoft Entra identity distinguish its contributions from yours. Some operations use that identity; others use authorized access on your behalf. The acting account, the requested resource, and the action all affect access.

Microsoft IQ provides organizational grounding for the connected Copilot experience, with Work IQ supplying work context such as people, projects, and relevant Microsoft 365 information. Grounding and memory don't grant permissions or guarantee accuracy.

Autopilot's cloud workspace can retain working context between sessions. It is separate from your local device; Autopilot can't access your local folders or apps. Where enabled, it can work in Microsoft Edge on your device when you ask it to. For a deliverable you want to keep, specify an accessible save location and verify the resulting file and its sharing settings.

## Extend the work Autopilot can do

Skills provide task instructions; plugins connect capabilities and services and can include skills. Neither grants access to data by itself. Available capabilities depend on your organization's settings.

| Capability | Examples |
| --- | --- |
| Document and presentation skills | Prepare editable deliverables for review. |
| Microsoft 365 tools | Work with authorized mail, calendars, conversations, and files. |
| Plugins | Connect Autopilot to other services and add their skills. |
| Your own skills | Create a skill in a conversation or upload one, use it with `/`, and share it with coworkers. |

For details and skill controls, see [Customize what Autopilot can do](https://learn.microsoft.com/en-us/copilot/autopilot/plugins).

## Keep oversight of background work

Review the scope of authorized actions, automation instructions, recipients, and results. Approval cards explain why an action needs your review, and only your own requests authorize actions; instructions in email, files, or web pages don't. For details, see [Set permissions](https://learn.microsoft.com/en-us/copilot/autopilot/approval#set-permissions). Activity isn't a guarantee of a complete administrative audit record. Sensitivity-label recognition doesn't establish that all generated files inherit labels or that every operation is covered by data loss prevention.

## How Autopilot fits with other Copilot experiences

Home brings together conversational and delegated work in Copilot. Cowork handles delegated tasks and Code focuses on building solutions. Autopilot provides persistent follow-through. The Teams **@Copilot** capability is distinct from your Autopilot. Availability and controls differ across these experiences.

## Related content

- [Get started with Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)
- [Use Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/using)
- [Autopilot scenarios](https://learn.microsoft.com/en-us/copilot/autopilot/scenarios)
- [Autopilot common questions](https://learn.microsoft.com/en-us/copilot/autopilot/faq)
- [Autopilot requirements](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)
- [Application card for Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)

---
