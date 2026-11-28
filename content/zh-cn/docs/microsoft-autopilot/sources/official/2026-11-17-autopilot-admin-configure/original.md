来源：https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure
取文：2026-11-28，直接下载

Configure Autopilot (Frontier) for your organization

[This article is prerelease documentation and is subject to change.]

Important

- Access to Autopilot (Frontier) requires the applicable **[Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)** enrollment, preview assignment, and participation terms. Frontier enrollment alone doesn't enable every preview feature. Frontier previews are subject to the applicable preview terms of your customer agreements, and their availability and capabilities may change.
- This feature is in preview.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

This article is for administrators preparing Autopilot for their organization. Autopilot is off by default. To turn it on, you enroll users in Frontier, set up a spending policy that covers Autopilot, and activate the **Autopilot (Frontier)** agent in the Microsoft 365 admin center. Each step is required; enabling Frontier alone doesn't make Autopilot available.

Autopilot runs in the cloud as part of Microsoft Copilot. Each enabled user can create one Autopilot. For product capabilities, see the [Autopilot overview](https://learn.microsoft.com/en-us/copilot/autopilot/overview).

## Prerequisites

Before you begin, ensure that you:

- Use an organizational account with the appropriate Microsoft 365 administrator role for the setting you intend to change.
- Confirm that the intended users have Microsoft 365 Copilot licenses and work accounts. Availability is initially limited to eligible customers in the United States.
- Confirm that your organization has the required Microsoft Security capabilities, and review the recommended ones. For more information, see [Security requirements and recommendations](https://learn.microsoft.com/en-us/copilot/autopilot/requirements#security-requirements-and-recommendations).
- Identify the users or groups who should have Autopilot.
- Choose a billing method for Copilot Credits, such as an Azure subscription for pay-as-you-go or prepaid Copilot Credits.
- Review the applicable preview terms, approved AI providers, and allowed data and workflows.

For current Frontier roles and prerequisites, see [Get started with the Microsoft Frontier Program](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/get-started-frontier).

## Enable Frontier for the intended users

Use the Microsoft 365 admin center to manage Frontier access.

1. Sign in to the Microsoft 365 admin center.
2. Select **Copilot**, then **Settings**.
3. Select **View all**.
4. In **Search all Copilot settings**, enter `Frontier`.
5. Select **Copilot Frontier**.
6. Choose **No access**, **All users**, or **Specific users and groups**, and apply the intended assignment.

Frontier changes can take time to appear. The [Frontier administration guidance](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/get-started-frontier#enroll-users-in-frontier) describes propagation and additional agent-access controls. Frontier doesn't override a disabled agent or turn on an AI provider on your behalf.

## Set up a spending policy for Autopilot

Autopilot is billed on usage in Copilot Credits. Every user who creates an Autopilot must be covered by a spending policy that includes Autopilot. If a user isn't covered, or the policy runs out of credits, Autopilot doesn't work for that user, and Autopilot doesn't show the user an explanation.

You can create the policy during activation, where the wizard suggests a new Autopilot spending policy, or ahead of time in Cost management:

| Wizard step | What to do |
| --- | --- |
| Open Cost management | In the Microsoft 365 admin center, go to **Copilot** > **Cost management** > **Configuration** > **Spending policies**, and select **Add spending policy**. |
| Policy scope | Name the policy, choose **Identity**, and select **All users** or the groups who will use Autopilot. |
| Agents and services | Under **Microsoft Copilot**, make sure **Autopilot** is selected. |
| Limits and alerts | Set a monthly limit, a per-user limit, or both, and add email alerts if you want them. |
| Billing method | Choose how credits are paid for, such as an Azure subscription for pay-as-you-go or prepaid Copilot Credits. |
| Review and add policy | Check your settings and save the policy. |

Autopilot consumption is charged to the policy's billing method. If a user is in more than one spending policy, the policy with the highest spending limit applies. If users in your organization already have an Autopilot, add a spending policy that covers them. After billing checks are turned on for your tenant, users who aren't covered can't use Autopilot.

For more information about spending policies, see [Managing AI experiences enabled by usage-based billing](https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-credits#add-identity-based-spending-policy).

## Activate Autopilot for users

Activate the agent in the Agent Registry, and choose who can create an Autopilot.

1. In the Microsoft 365 admin center, go to **Agents** > **All agents**.
2. Search for `Autopilot`, select **Autopilot (Frontier)**, and then select **Activate**.
3. Complete the five steps of the activation wizard:

   | Wizard step | What to do |
   | --- | --- |
   | **Select users** | Choose **All users** or the specific groups who can create an Autopilot. Keep this scope aligned with your spending policy. |
   | **Spending policy** | Select your Autopilot spending policy. If you don't have one, keep the new Autopilot spending policy that the wizard suggests, and select **Customize policy** to set limits and the billing method. |
   | **Security policy** | Review the default Microsoft Entra, Microsoft Purview, and Microsoft Defender protections listed for the agent. They're managed in each security product, and they might not be turned on, so check their status there. |
   | **Accept permissions** | Review the agent's permissions and the notice that Autopilot can act without per-step confirmation. |
   | **Memory & personalization** | Review the agent's memory capabilities and user controls. |
   | **Review & activate** | Confirm the agent, spending policy, users and groups, and permissions, and then select **Activate agent**. |

You don't need to select or assign a license on this page.

For details about activation and other agent actions, see [Governance and lifecycle actions for agents available in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions).

## Confirm Autopilot access

Have an enabled user sign in at [copilot.cloud.microsoft](https://copilot.cloud.microsoft) and check that Autopilot appears on the **Home** tab in the left navigation. Autopilot appears only for users who are activated **and** covered by a spending policy that includes Autopilot. Selecting it starts Autopilot creation for a user who doesn't have one yet.

If Autopilot isn't present in the navigation, or Autopilot stops responding, check:

- The user's Frontier assignment.
- The user's Copilot license.
- The activation scope for **Autopilot (Frontier)**.
- Spending policy coverage for the user, and whether the policy has credits remaining.
- Permitted agent and AI provider settings.

Allow time for changes to take effect. Don't have the user repeatedly create an agent to troubleshoot missing access.

For licensing guidance, see [Microsoft Copilot licensing](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-licensing). Use [Autopilot requirements](https://learn.microsoft.com/en-us/copilot/autopilot/requirements) as the user-facing prerequisite checklist.

## Monitor and manage Autopilot instances

After users create their Autopilots, use the agent's details panel to review and govern them.

1. In **Agents** > **All agents**, select **Autopilot (Frontier)**.
2. Select **Instances** to review the Autopilots that users in your organization have created.

To change who can create an Autopilot, update the activation scope. Removing a user from the activation scope doesn't remove an Autopilot they already have. To stop an existing Autopilot, also remove the user from the spending policy, and then block or delete the instance. Blocking a user can take about an hour to reach Autopilot, and work on the owner's behalf can continue longer, so don't rely on it for an immediate stop.

To track the Copilot Credits that Autopilot uses, go to **Copilot** > **Cost management**. Add alerts to your spending policy so that you're notified as limits approach.

Perform governance actions, such as activation, blocking, and assigning users, on the **Autopilot (Frontier)** entry. During rollout, the Agent Registry can temporarily show an additional entry associated with Autopilot. Use it only to list Autopilot instances if **Autopilot (Frontier)** doesn't show all of them.

## Review identity and permissions

Autopilot has a dedicated Microsoft Entra identity. Some operations use that identity and others use authorized access on a user's behalf. Autopilot doesn't expand a user's access to Microsoft 365 data. Review the acting account, resource access, and permitted actions rather than treating agent creation as a grant to all organizational data.

Users can inspect **Agent settings**, including **Computer & Access**. Agent settings don't authorize Autopilot to perform an action.

Autopilot, including its automations, can perform work without a new prompt at each step. Teach users to review saved instructions, recipients, destinations, and permission scope. Learn more in [Set permissions](https://learn.microsoft.com/en-us/copilot/autopilot/approval#set-permissions).

## Review plugins, skills, and browser use

Users can add plugins from the catalog, create or upload their own skills, and share a skill with specific people in your organization. Plugins that your organization's policies block appear as **Blocked by policy** and can't be added. For plugins your organization manages, you handle the connection, so users don't sign in or enter keys. Sharing a skill doesn't transfer the sharer's sign-ins, connections, or permissions. For guidance on managing and governing plugins in your organization, see the [plugins documentation](https://learn.microsoft.com/en-us/plugins).

Where enabled, Autopilot can also work in Microsoft Edge on a user's device, but only for requests the user makes in their private conversation. It asks the user for approval before sensitive actions, such as payments or account changes. Page content it reads is processed by its cloud model. Your organization's policies, Edge policies, and data loss prevention can still block browser actions. For user guidance, see [Customize what Autopilot can do](https://learn.microsoft.com/en-us/copilot/autopilot/plugins) and [Work in your Microsoft Edge browser](https://learn.microsoft.com/en-us/copilot/autopilot/edge).

## Understand automated checks and approvals

Autopilot can carry out multistep tasks and act across connected services on a user's behalf without asking at each step. Like other AI experiences, it can interpret a request more broadly than intended. For example, a request to clean up old project files could affect more content than the user expects. The activation flow includes a notice that Autopilot can act without per-step confirmation. Before you activate Autopilot, review its permissions and consider whether the tasks your users intend are suitable for automated execution.

Autopilot uses an automated review system, a second AI model that reviews actions before they run. This review system compares each action with what the user asked for and any limits they set and then decides whether the action can go ahead or needs the user's approval.

| Type of action | What happens |
| --- | --- |
| Reading, searching, and drafting | Runs without interruption. A small share is spot-checked. |
| Sending, sharing, deleting, or changing content; creating or changing automations | The automated review system decides. Actions that match the request run; others wait for the user's approval. |
| Payments and sensitive browser steps | Always need the user's approval. |

- **Only the owner's requests count.** The automated review system treats only the owner's own messages as requests. Instructions in email, documents, or web pages don't authorize an action.
- **Visibility and settings.** Where available, users can review recently approved actions under **Recent approvals** in the Autopilot panel and give feedback on them. There are no administrator or user settings for the automated review system in this release.

Ask users to check the scope, recipients, files, and data before they allow an action, and to review important results, especially when files, access, or communications are involved. For user guidance, see [Set permissions](https://learn.microsoft.com/en-us/copilot/autopilot/approval#set-permissions).

## Review model governance

Autopilot runs on GPT-6.1 Sol, provided by OpenAI operating as a Microsoft subprocessor. If your organization turns off OpenAI in the AI providers setting, Autopilot automatically uses GPT-5.6 Sol hosted in Azure OpenAI instead. Users can't switch models through a prompt, and there's no separate model selection control for Autopilot.

- **Data processing.** When OpenAI is turned on, Autopilot prompts and related data are processed by OpenAI as a Microsoft subprocessor. Review this setting in the Microsoft 365 admin center under **Copilot** > **Settings** > **AI providers operating as Microsoft subprocessors**.
- **Data residency.** Before you enable Autopilot broadly, confirm that processing by this provider meets your data residency and EU Data Boundary requirements. If it doesn't, turn the provider off, and Autopilot uses the model hosted in Azure OpenAI.

For more information, see [OpenAI as a subprocessor in Microsoft Online Services](https://learn.microsoft.com/en-us/copilot/implement/openai-subprocessor).

## Review memory and personalization

Autopilot remembers information so that it can personalize its help. It keeps conversation memory, personal memory about its owner, and workspace memory for the work it does.

- **Reviewing memory.** Users can see what Autopilot remembers in the Autopilot panel under **Review what [name] knows**, where *[name]* is their Autopilot's name. They can correct, delete, or export memories by asking in chat, for example, "Forget that I'm working on Project X." Forgetting a memory doesn't erase earlier chat messages or exports.
- **No on/off switch.** Memory can't be turned off for Autopilot in this release, and the Microsoft 365 Copilot personalization settings don't apply to it.
- **Separate from conversations.** Deleting a conversation doesn't delete memories.

## Review compliance coverage

Autopilot reaches content in two ways: with its own agent identity, and on behalf of its owner using the owner's access. Most Microsoft Purview, Microsoft Entra, and Microsoft Defender controls apply to the agent identity. Work done on the owner's behalf is only partly covered. The following table describes current coverage.

| Capability | Current status |
| --- | --- |
| Audit | Recorded in the unified audit log. AI and tool calls, and anything Autopilot does with its own identity, such as sending a Teams message to a coworker, appear under the Autopilot. File and mail reads on the owner's behalf appear under the owner's account, with an internal service name and no agent ID. The conversation ID on the Autopilot's records can link them. Session lists can include background automations, so users might see more entries than they expect. |
| Data loss prevention (DLP) for prompts | Being tested in some tenants. Prompts with sensitive information are blocked before they reach the model. Users see a generic error instead of the policy notice, and follow-up prompts in the same chat can still be answered. |
| Sensitivity labels | Labeled email and files aren't excluded. Autopilot can read them with its own identity or on the owner's behalf. |
| eDiscovery, retention, and legal hold | Not available for Autopilot conversations. Conversations in Microsoft Copilot aren't stored where retention and holds apply. |
| Data Security Posture Management for AI and Activity explorer | Autopilot doesn't appear. |
| Microsoft Entra and Microsoft Defender | Conditional Access, ID Protection, and access reviews apply to the agent identity, and changes take about an hour. Policies that target **All users** don't include agent users. Defender lists the agent as a user, not in its agent inventory. |

Displaying a sensitivity label doesn't prove that every generated file inherits it. User activity isn't a complete administrative audit record. Don't infer compliance coverage from feature presence or generic Copilot protections.

During the preview, follow these recommendations:

- **Rely on permissions and encryption.** Permissions and encryption are the controls that reliably keep content away from Autopilot. Share sensitive content only with the people who need it, and use encryption where appropriate.
- **Check Conditional Access coverage.** Policies that target **All users** don't apply to Autopilot's agent identity. If you rely on a policy, make sure it explicitly covers agent identities.
- **Consider users on legal hold.** Because eDiscovery, retention, and legal hold don't cover Autopilot conversations, consider not enabling Autopilot for users who are subject to holds or strict retention requirements.
- **Allow time for changes.** Blocking a user or changing Conditional Access can take about an hour to reach Autopilot, and work on the owner's behalf can continue longer.
- **Set expectations with users.** Establish permitted sources, recipients, and storage destinations, and tell users how to report uncertain results, blocked actions, and suspected information disclosure.

## Help users access, export, and delete their data

Users manage their own Autopilot memory and conversations. For an approved compliance or privacy request, an administrator can export a copy of a user's Autopilot memories and sessions. For more information, see [Export a user's Autopilot data](#export-a-users-autopilot-data). Administrators can't delete this data on a user's behalf. Bulk deletion isn't available, and the My Account privacy page doesn't delete Autopilot data.

| Action | How it works |
| --- | --- |
| Review memory and history | The user opens **Review what [name] knows** in the Autopilot panel, or asks in chat, for example, "What do you remember about me?" |
| Export memory or sessions | The user asks Autopilot in chat. Autopilot saves the export to the user's OneDrive after the user approves the write. For a full copy, the user can run the export script on a Windows PC. For more information, see [Download a full copy of your memories and sessions](https://learn.microsoft.com/en-us/copilot/autopilot/memory#download-a-full-copy-of-your-memories-and-sessions). |
| Export a user's data for a compliance or privacy request | An administrator runs the export script with their own account. For more information, see [Export a user's Autopilot data](#export-a-users-autopilot-data). |
| Delete a memory | The user removes it in the Autopilot panel or asks Autopilot in chat. |
| Delete a conversation | The user selects the **...** menu next to the conversation in the conversation list. |
| Permanently remove a deleted conversation | The user asks Autopilot in chat. |
| Bulk, departing-user, or verified deletion | Contact Microsoft support. |

Share these points with users:

- **Approve the write.** Saving an export writes to OneDrive, so watch for the approval card.
- **Protect exports.** Exported files might not carry a sensitivity label. Handle them according to the most sensitive information they contain.
- **Remove deleted conversations permanently.** A deleted conversation is removed from the list, but the underlying record stays until the user asks Autopilot to remove it. The user asks, "Delete the session titled [name]," and then asks, "Can you permanently delete it now?"
- **Teams edits carry over.** When a user edits or deletes a message in their Teams chat with Autopilot, Autopilot's copy of the conversation is updated too.
- **Address memory separately.** Deleting a conversation doesn't remove information already saved in memory. Users should remove the memory too and confirm that it's gone.

For user-facing prompts, see [Check what Autopilot remembers](https://learn.microsoft.com/en-us/copilot/autopilot/memory).

### Start fresh

A user who wants to clear all Autopilot working data, including conversation history, memory, skills, and automations, should first export anything they want to keep. Contact Microsoft support for a full reset, bulk deletion, cleanup for departing users, or verification of deletion across locations.

## Export a user's Autopilot data

Autopilot stores each user's memories and sessions in a file named `lobster.repo` in the user's OneDrive. For an approved compliance or privacy request, a tenant administrator can download a copy of another user's `lobster.repo` with the Autopilot export script. You sign in with your own administrator account; the script never uses the user's credentials. Nothing in the user's OneDrive is changed, shared, or deleted.

### Before you export

Make sure you have:

- A Windows PC with Windows PowerShell. The script offers to install Git for Windows if it's missing.
- The `Autopilot-Workspace-Export.zip` file [available on GitHub](https://github.com/microsoft/autopilot-resources/blob/main/workspace-export/Autopilot-Workspace-Export.zip). Right-click it, select **Extract All**, and open the extracted `Autopilot-Workspace-Export` folder. Don't run the script from inside the zip file.
- An administrator account that can access the user's OneDrive in the Microsoft 365 admin center.
- An approved request, with a reference you can record as the reason for the export.
- For additional details, consult the [README.md file](https://github.com/microsoft/autopilot-resources/blob/main/workspace-export/README.md) in the [Autopilot-resources GitHub repo](https://github.com/microsoft/autopilot-resources).

### Export the user's data

Follow these steps to give yourself temporary access, run the export, and then remove your access.

1. Grant yourself temporary access to the user's OneDrive in the Microsoft 365 admin center:

   1. Go to [admin.microsoft.com](https://admin.microsoft.com) and sign in with your administrator account. An InPrivate window keeps this sign-in separate from your normal work account.
   2. Select **Users** > **Active users**, and then select the user's name.
   3. On the user's page, select the **OneDrive** tab.
   4. Under **Get access to files**, select **Create link to files**.
   5. Copy the link that appears, for example `https://contoso-my.sharepoint.com/personal/user_contoso_com`. This link is the user's OneDrive address.

   This step makes you an administrator of the user's OneDrive until you remove the access, and the grant is recorded in the audit log. It can take a few minutes to take effect.
2. Open PowerShell in the extracted `Autopilot-Workspace-Export` folder and run the following command. Use the link from step 1 as the `-TargetOneDriveUrl` value.

   ```
   powershell -NoProfile -ExecutionPolicy Bypass -File .\Export-AutopilotWorkspace.ps1 -TargetUser user@contoso.com -Reason "Privacy request 1234" -Account admin@contoso.com -TargetOneDriveUrl "https://contoso-my.sharepoint.com/personal/user_contoso_com"
   ```

   | Parameter | Description |
   | --- | --- |
   | `-TargetUser` | The sign-in name of the user whose data you're exporting. |
   | `-Reason` | The reason for the export, such as the request reference. It's recorded in the export manifest. |
   | `-Account` | Your administrator account. The script preselects it at sign-in. |
   | `-TargetOneDriveUrl` | Optional. The user's OneDrive address from step 1. Without it, the script tries to find the user's OneDrive automatically. |
   | `-OutputFolder` | Optional. A new folder for the export. It must not be synchronized by OneDrive. |
3. When prompted, choose **Yes** to approve administrator access on your PC.
4. Sign in with your administrator account. Only the browser sign-in identifies you as the administrator; your Windows account doesn't matter. If Microsoft Edge signs you in automatically with a different account, copy the sign-in address that the script prints into an InPrivate window (Ctrl+Shift+N).
5. When the browser says you're signed in, return to the PowerShell window and choose **Yes** at the second administrator prompt.
6. The script finds the user's OneDrive and confirms that its owner matches `-TargetUser`. It shows the repository it found and asks you to type the user's sign-in name to confirm. If it finds more than one `lobster.repo`, type the number of the one to download.
7. When the export finishes, record the export manifest's hash that the script prints at the end with the request.
8. Remove your access to the user's OneDrive. The script prints a `Set-SPOUser ... -IsSiteCollectionAdmin $false` command for this, or you can remove it in the SharePoint admin center.

### Review the exported files

The script creates a new folder named `Autopilot export <date time>` in your user profile and opens it in File Explorer. The folder contains:

| Item | Contents |
| --- | --- |
| `Latest files` | A readable copy of the files in the latest version, such as memories and session records. |
| `repository.git` | The full Git repository, including earlier versions and history. |
| `README.txt` | A short description of the copy. |
| `export-manifest.json` | A record of who exported the data, for whom, when, and why, with a SHA-256 hash of every file. |

The export contains the user's personal and organizational information. Store and share it according to your organization's process for the request and the most sensitive information it contains.

### Troubleshoot an export

If the script stops with a message, use the following table to resolve it.

| Message | What to do |
| --- | --- |
| Administrator approval was declined | Run the script again and choose **Yes**, or ask IT support to run it with you. |
| Hosts file already has a different entry | Ask IT support to review the existing `cowork.local.microsoft.com` entry. |
| Browser shows a certificate warning | Don't bypass it. Close the tab and report it to your security team. |
| Your organization has not approved this sign-in | Ask IT support; the sign-in application may need consent in your organization. |
| Could not connect after 3 attempts | Check your network, VPN, or proxy connection, and then run the script again. |
| No Autopilot workspace was found | The user might not have an Autopilot, or its workspace might be stored elsewhere. Contact Microsoft support. |
| Some branch or tag references could not be downloaded | The copy is incomplete. Run the script again into a new folder. |
| Temporary setup could not be removed automatically | The warning names the hosts file line and certificate to remove. Remove them manually. |
| You do not have access to the OneDrive of a user | Complete step 1, wait a few minutes, and then run the script again with `-TargetOneDriveUrl`. |

To see more detail, open PowerShell in the tool's folder and run `.\Export-AutopilotWorkspace.ps1 -Verbose`. Use `-OutputFolder` to choose a different new folder; it must not be synchronized by OneDrive.

If PowerShell reports that running scripts is disabled, use `Export-AutopilotWorkspace.cmd` or the powershell `-ExecutionPolicy Bypass -File` form shown above. If your organization blocks PowerShell entirely, ask IT support.

## Review usage and rollout

Spending policies control who can use Autopilot, set monthly and per-user limits and alerts, and determine the billing method. Track Copilot Credit use in **Copilot** > **Cost management**.

When a user isn't covered by a spending policy, or the policy reaches its limit, Autopilot stops running automations and monitoring work and stops responding to new requests. Autopilot doesn't show the user an explanation, so tell users to contact you if Autopilot stops responding. Review policy limits and alerts before expanding access.

Start with bounded workflows and a limited audience. Check automation outcomes, approvals, failed or uncertain actions, and the final files or messages. Validate changes in your own configuration before expanding access.

## Related content

- [Autopilot requirements](https://learn.microsoft.com/en-us/copilot/autopilot/requirements)
- [Get started with Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)
- [Autopilot overview](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [Use Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/using)
- [Application card for Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card)
- [Governance and lifecycle actions for agents available in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions)

---
