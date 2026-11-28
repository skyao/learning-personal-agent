来源：https://learn.microsoft.com/en-us/copilot/autopilot/faq
取文：2026-11-28，直接下载

Autopilot (Frontier) FAQ

[This article is prerelease documentation and is subject to change.]

Important

- Access to Autopilot (Frontier) requires the applicable **[Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)** enrollment, preview assignment, and participation terms. Frontier enrollment alone doesn't enable every preview feature. Frontier previews are subject to the applicable preview terms of your customer agreements, and their availability and capabilities may change.
- This feature is in preview.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

This article answers frequently asked questions about Autopilot. For more information about Autopilot, see [Autopilot overview](https://learn.microsoft.com/en-us/copilot/autopilot/overview).

## Understand Autopilot

These questions explain what you can delegate to Autopilot and how it relates to other Copilot experiences.

### What is Autopilot?

Autopilot is a always-on, cloud-based agent in Microsoft Copilot. You describe the outcome you want and set boundaries, and it helps carry work forward across Microsoft 365. It can prepare documents, follow up on work, and run recurring tasks through routines. It has a dedicated identity, memory, computer, and workspace so work can continue beyond a single conversation. Its actions remain subject to the permissions and policies that apply to the task. For more information, see the <overview>.

### How is Autopilot different from Copilot Chat?

Use Copilot Chat for questions and conversational work. Use Autopilot when you want ongoing follow-through, recurring work, and continuity across conversations. Autopilot can keep working in the background without you prompting each individual step.

### How does Autopilot relate to Home, Today, Cowork, and Code?

Home is the starting point for work in the Copilot app. Today is a separate, personalized experience for work that needs your attention. Cowork handles delegated, multi-step tasks, and Code focuses on building software and solutions. Autopilot focuses on persistent work and follow-through. Availability differs across these experiences during the preview.

Office integration in Copilot doesn't mean every Office capability is available in Autopilot. Likewise, software tasks and parallel agents described for Code or GitHub Copilot aren't automatically Autopilot features. Use the controls available in your experience rather than assuming a task can be handed between them.

### Does Autopilot keep working when I close the app?

Yes. Autopilot runs in the cloud, so it can keep working and complete tasks even if you close the Copilot app or your laptop is closed or turned off. A routine can run without you being present, using its configured instructions and permissions. You can also check on progress, add instructions, or change direction from your phone.

Background operation doesn't guarantee uninterrupted execution or completion at a particular time. Missing access, a required approval, or an unavailable service can prevent work from completing.

## Delegate and follow through on work

Give Autopilot an outcome, the information it should use, and limits on what it may do. Use routines for work that needs to repeat.

### What is a routine?

A routine is work Autopilot runs on a schedule, such as a morning briefing or a weekly status summary. Specify what it should do, when it should run, and where you want the result delivered. Include the sources, recipients, and constraints it needs; don't assume a scheduled run inherits everything discussed in the conversation where you created it.

Review the schedule, instructions, and requested permissions before enabling recurring work.

### Can Autopilot monitor channels, follow up on threads, and flag risks?

You can ask Autopilot to review accessible conversations for open questions, commitments, and changes. Use a routine for checks on a fixed schedule. For example, ask it to summarize unresolved launch decisions each morning and draft follow-ups for your review. Tell it which conversations to use, what counts as a risk or opportunity, and whom to notify.

### Can Autopilot pick up a project in a later conversation?

Saved preferences, decisions, and working context help Autopilot continue work over time. Tell it which project or earlier work you mean and provide any changed requirements. Memory isn't a complete record of every conversation, and it doesn't grant access to sources or authorize new actions.

### Can Autopilot help with meetings, deadlines, and time blocking?

You can ask Autopilot to prepare a meeting brief, find meeting times, draft an invitation, review upcoming deliverables, or create calendar time for a task. Specify the people, date range, time zone, and calendar you intend it to use. The available operations depend on its access and your organization's settings.

Finding a time, drafting an invitation, and sending it are different actions. Check the organizer, attendees, and calendar before approving a change. Asking for a deadline summary doesn't automatically authorize invitations or calendar changes.

## Identity, memory, and work data

Autopilot uses organizational context and saved working information within the access allowed for each task and conversation.

### Why does Autopilot have its own name and email address?

Its workplace identity lets teammates recognize its contributions in Teams and Outlook and distinguish them from yours. Review the identity presented during setup. Its Microsoft Entra identity also lets your organization manage access for the agent.

### How do I add my Autopilot as my Assistant in my Microsoft 365 profile?

1. Open your Microsoft 365 profile. Alternatively, open Microsoft 365 Copilot, select your account at the bottom left, then select My Microsoft 365 profile.
2. Select **Update your profile** in the profile header.
3. Open **Contact**, in the **Assistant** field, select your Autopilot.
4. Select **Save changes**.

Your administrator controls whether this profile field is available and editable. If it's missing or read-only, ask your administrator for help. Setting your profile's Assistant doesn't by itself grant Autopilot permissions or enable collaboration.

### Does Autopilot always act through its own identity?

No. Its identity and the account used for an operation are related but different. Some operations use Autopilot's own identity; others use authorized access on your behalf to read or work with your Microsoft 365 resources. For example, it may read your calendar using your permissions while communicating with coworkers under its own identity.

Having a separate identity doesn't give Autopilot unrestricted access to your data. Permissions apply to the acting account, the resource, and the requested action.

### What can Autopilot access?

Autopilot can work with authorized Microsoft 365 content, including Teams conversations, email, calendar, and files in OneDrive and SharePoint, through the capabilities available to it. Access depends on the account used, resource permissions, and organizational policy. Adding a skill doesn't grant additional access.

### How does Autopilot use Microsoft IQ and Work IQ?

Microsoft IQ is the broader organizational intelligence described for the connected Copilot experience. Work IQ provides work context, such as people, projects, and relevant Microsoft 365 information. That context helps Autopilot ground its work in your organization rather than relying only on the current prompt.

Grounding doesn't grant access to information or guarantee that an answer is correct. Review the sources, dates, and conclusions that matter to your task.

### Does Autopilot remember things between conversations?

Yes. Autopilot keeps conversation memory, personal memory about you, and workspace memory for the work it does. To see what it remembers, open **Review what [name] knows** in the Autopilot panel, where *[name]* is your Autopilot's name. You can also ask, "What do you remember about me?" in your private conversation, or ask it to correct, forget, or export a specific memory. Confirm the result rather than assuming a change succeeded.

Memory can't be turned off in this release, and your Microsoft 365 Copilot personalization settings don't apply to Autopilot. Memory and conversation history are separate: deleting a conversation doesn't remove a memory already saved from it. For more information, see [Check what Autopilot remembers](https://learn.microsoft.com/en-us/copilot/autopilot/memory#).

### What are Autopilot's computer and workspace?

Autopilot has a Microsoft-managed cloud environment where it can work with files and carry out tasks. Its workspace can retain working context between sessions. Temporary files it uses only to complete a task aren't kept after the task finishes.

This cloud computer is separate from your device. Autopilot can't access your local folders or installed apps. Where enabled, it can work in Microsoft Edge on your device when you ask it to.

### Can Autopilot use my web browser?

Where your organization enables it, Autopilot can work in Microsoft Edge on your device, using sites you're already signed in to. You turn on browser use the first time, and only requests you make in your private conversation can use it. Automations and shared conversations don't use your browser.
Autopilot works only in the tabs it uses for that conversation, and it asks for your approval before sensitive actions such as payments, account changes, or permanent deletions. Browser use is rolling out during the preview. For more information, see [Work in your Microsoft Edge browser](https://learn.microsoft.com/en-us/copilot/autopilot/edge).

### Where are my files and Autopilot's work saved?

Your conversations and personal work are saved in your OneDrive.

Distinguish a file created in Autopilot's workspace from a file saved where you and your coworkers can open it. For a deliverable you want to keep, specify a OneDrive folder or SharePoint location that the acting account can access, and ask Autopilot for the saved location or link.

Don't assume a successful file-creation step means the file was uploaded, shared, or labeled. Verify that you can open the final file and that its access and sensitivity label are appropriate.

### How do I export or delete my Autopilot data?

Ask Autopilot in your private conversation. For example, "Export everything you remember about me to a JSON file in my OneDrive and tell me where you saved it." To remove a conversation, ask it to delete the session by name, then ask, "Can you permanently delete it now?" Removing a conversation from the list doesn't necessarily delete its stored record.

If an approval card appears when Autopilot saves an export, review it before you allow it. An export is a snapshot and might not carry the original sensitivity labels. For more prompts and details, see [Check what Autopilot remembers](https://learn.microsoft.com/en-us/copilot/autopilot/memory).

To download a full copy of your memories and sessions to a Windows PC, use the Autopilot export script. For more information, see [Download a full copy of your memories and sessions](https://learn.microsoft.com/en-us/copilot/autopilot/memory#download-a-full-copy-of-your-memories-and-sessions). For an approved compliance or privacy request, your administrator can export a copy of your Autopilot data. For more information, see [Export a user's Autopilot data](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure#export-a-users-autopilot-data).

### Can I start over with a new Autopilot?

Export anything you want to keep first, and then contact your administrator. Don't rename, move, or delete Autopilot's files yourself.

### How do skills and plugins extend Autopilot?

Skills provide instructions for a type of task. Plugins connect Autopilot to tools and services and can make additional skills available. Neither a skill nor a plugin grants permission to use data or take an action on its own.

| Capability | What it helps you do |
| --- | --- |
| Document and presentation skills | Prepare editable work for review. |
| Microsoft 365 tools | Work with authorized mail, calendars, conversations, and files. |
| Plugins | Connect Autopilot to other services and add their skills. |
| Your own skills | Teach Autopilot a repeatable way to do a task. |

On **Plugins**, you can add plugins from the catalog, create or upload a skill, and find skills that coworkers shared with you. Type `/` in the composer to use a skill, or let Autopilot choose a relevant one. Items marked **Blocked by policy** aren't available in your organization. For more information, see [Customize what Autopilot can do](https://learn.microsoft.com/en-us/copilot/autopilot/plugins) and the [plugins documentation](https://learn.microsoft.com/en-us/plugins).

### Can I share a skill with coworkers?

Yes. You can share a saved skill with specific people in your organization. They open the link, add the skill, and use it in their own Autopilot. Sharing doesn't share your sign-ins, connections, or permissions. For more information, see [Share a skill](https://learn.microsoft.com/en-us/copilot/autopilot/plugins#share-a-skill).

## Review actions and apply organizational controls

Background work still needs oversight. Check what Autopilot plans to do, the authority it uses, and the actual result.

### Will Autopilot send messages or change things without asking each time?

It can. Autopilot can complete tasks without asking you at each step. Before it sends, shares, deletes, or changes something, or creates or changes an routine, an automated check compares the action with what you asked for. If the action matches your request, it runs. If it doesn't match, or the check can't finish, you get an approval card in Teams, and in Microsoft Copilot if you asked there. Payments and other sensitive browser steps always need your approval.

Only your own messages count as requests. Instructions in email, documents, or web pages don't authorize an action. On an approval card, **Allow** runs the listed actions once, and **Deny** cancels them. Review the recipients, destination, and acting account before you allow an action. For more information, see [Set permissions](https://learn.microsoft.com/en-us/copilot/autopilot/approval#set-permissions).

### How do I track work and intervene?

Open the management panel and select the **Activity** tab to review actions and updates. See **Working now** to review work in progress or **Needs your input** to find requests for your attention. You can look below that under Today and beyond to see completed activity and routines that have run.
Select **Overview** to browse conversations, or **Routines** to review scheduled work. Open a conversation to clarify or change the task, or ask Autopilot to stop it. Review or pause recurring work when it no longer matches your intent.

A request to stop doesn't prove that an action already in progress was canceled or reversed. Check what completed before retrying a send, invitation, or file change.

### How should I validate a result?

Check the result in its destination: open the saved document, review the calendar event, or confirm the sent message and its recipients. An approval authorizes an action; it isn't proof that the action completed. Review AI-generated content for accuracy and suitability before relying on it.

### What governance and audit controls apply?

Your organization controls access to the preview and to Microsoft 365 resources. Autopilot's identity, permissions, and automated approval checks constrain the work it can do.

User-facing activity helps you follow a task, but it isn't a guarantee of a complete administrative audit record. Ask your administrator which auditing, retention, and compliance controls cover your enabled Autopilot experience. For configuration guidance, see [Configure Autopilot for your organization](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure).

### Does Autopilot support sensitivity labels and data loss prevention?

Autopilot can recognize sensitivity labels on supported Microsoft 365 content. However, labeled email and files aren't excluded from what Autopilot can read, and content it generates might not inherit the label. Data loss prevention (DLP) for prompts is limited during the preview, so don't assume uniform Microsoft Purview DLP coverage across all tools and destinations. If a prompt is blocked, you might see a generic error.

Before using Autopilot with sensitive information, confirm the applicable protections with your administrator. Check the destination file's label and access before sharing it.

### Is my data used to train AI models?

For information about how Autopilot handles your data and the models it uses, see the [Application card for Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card).

## Access and availability

Autopilot remains a preview. Access and individual capabilities can vary by organization and rollout.

### Do I need to install anything?

The cloud Autopilot experience runs in Microsoft Copilot and doesn't require a separately installed agent on your device. To let Autopilot work in your browser, where enabled, you need Microsoft Edge connected to Autopilot. For supported ways to access it, see [Autopilot requirements](https://learn.microsoft.com/en-us/copilot/autopilot/requirements).

### What happens when Autopilot runs out of credits?

Autopilot is billed on usage in Copilot Credits through a spending policy that your administrator sets up. If you aren't covered by a spending policy, or the policy reaches its limit, Autopilot stops running automations and monitoring work and stops responding to new requests. Autopilot doesn't show you an explanation when this happens. If Autopilot stops responding, contact your administrator. For more information, see [Review usage and limits](https://learn.microsoft.com/en-us/copilot/autopilot/using#review-usage-and-limits).

### How do I get access?

Autopilot is off by default. Your organization must enroll you in Frontier, and your administrator must license Autopilot, cover you with a spending policy for usage-based billing, and activate Autopilot for you. Enrolling in Frontier doesn't mean every announced capability is enabled for your account. To learn about joining Frontier, see the [Frontier program](https://adoption.microsoft.com/copilot/frontier-program/). For prerequisites, see [Get started with Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started#prerequisites).

### Can I use Autopilot on my phone?

Yes. Autopilot is available on iOS and Android through the Microsoft 365 Copilot, Microsoft Teams, and Microsoft Outlook apps. Sign in with your work account. You can check on progress, add instructions, or change direction for existing tasks from your phone.

### How many Autopilots can I have?

One. Each enabled user can create one Autopilot.

### How long does setup take?

After you complete the setup steps, provisioning can take 10 to 30 minutes. You can leave the page; you receive an email and a Teams notification when your Autopilot is ready. For the steps, see [Create your Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started#create-your-autopilot).

### Which languages and regions are supported?

Availability is initially limited to eligible customers in the United States. Autopilot is optimized for English. For current availability, see [Autopilot requirements](https://learn.microsoft.com/en-us/copilot/autopilot/requirements).

### How do I give feedback?

Under a response, select **I like something** or **I don't like something**. You can also ask Autopilot to log a bug. For more information, see [Provide feedback](https://learn.microsoft.com/en-us/copilot/autopilot/using#provide-feedback).

## Related content

- [Autopilot overview](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [Use Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/using)
- [Autopilot requirements](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)
- [Configure Autopilot for your organization](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure)
- [Application card for Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)

---
