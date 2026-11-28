来源：https://learn.microsoft.com/en-us/copilot/autopilot/memory
取文：2026-11-28，直接下载

Check what Autopilot remembers

[This article is prerelease documentation and is subject to change.]

Important

- Access to Autopilot (Frontier) requires the applicable **[Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)** enrollment, preview assignment, and participation terms. Frontier enrollment alone doesn't enable every preview feature. Frontier previews are subject to the applicable preview terms of your customer agreements, and their availability and capabilities may change.
- This feature is in preview.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Autopilot keeps conversation memory, personal memory about you, and workspace memory for the work it does. To see what it remembers, open the management panel and select **Settings**. Under **Memory**, select **Review what [name] knows**, where [name] is your Autopilot’s name. You can correct or remove memories there.

You can also ask in your private conversation. For example, "What do you remember about me?" or "What do you remember about how I like status updates written?" Ask it to correct or forget a specific preference, such as "Forget what you know about [topic]," then ask it to check the affected memory again. Confirm the outcome; don't treat a natural-language request as proof that a change succeeded.

Memory can't be turned off in this release, and your Microsoft 365 Copilot personalization settings don't apply to Autopilot. Memory, conversation history, and exported files are separate. Deleting a conversation doesn't remove an already saved memory or a separate export, and forgetting a memory doesn't erase earlier chat messages or exports.

### Inspect saved details and their sources

Start in your private conversation. Ask for the saved information and its source rather than relying only on a summary.

- "What do you remember about my status-update preferences? Show the saved notes and where each fact came from."
- "List the memory files you can access. Show the complete contents of the relevant file, without summarizing."

If Autopilot identifies a file such as `MEMORY.md`, `USER.md`, or a daily note, you can name that file in a follow-up. File names and available records can change during the preview. An inaccessible or missing note isn't proof that no copy exists elsewhere.

### Export memory or conversation records

Ask for a defined scope, format, and accessible save location. An export can contain sensitive personal and organizational information.

1. Specify the records you want. For example, "Export everything you remember about me to a JSON file in my OneDrive and tell me where you saved it." For more control, add the folder, ask it to identify the included records and dates, and ask it to list anything it couldn't access.
2. Watch for an approval card to save the file. It's easy to miss, and Autopilot doesn't write the export until you allow it.
3. Ask for the final file name, location, and a summary of included and excluded records.
4. Open the saved file and check that it contains the requested material. Check its access and classification before keeping or sharing it.

For a conversation, try: "Export this conversation as JSON to this OneDrive folder. State which messages and attachments are included or excluded."

For accessible session files, you can request an archive: "Gather all my session files and package them as a ZIP file. Put it in my OneDrive and tell me the exact location." Ask it to list the conversations and dates covered, and any omissions.

An export is a snapshot of what Autopilot could access when it created the file. It doesn't update later, and it might not carry the sensitivity labels of the original content.

A ZIP of accessible session files isn't proof of a complete cross-conversation or Teams history export. A list can include background or automation sessions as well as conversations. If Autopilot can't access another conversation's records, retain that limitation in the export description.

A file created in the working environment still needs to reach the intended save location. Don't assume a direct download link exists because a response mentions one. If a ZIP can't receive the expected sensitivity label, don't treat upload success as successful labeling; consult your administrator and protect it according to the most sensitive material it contains.

### Download a full copy of your memories and sessions

Autopilot keeps your memories and sessions in a file named `lobster.repo` in your OneDrive. You can download a private copy of it to a Windows PC with the Autopilot export script. Nothing in your OneDrive is changed, shared, or deleted.

You need a Windows PC. The script uses Windows PowerShell, which is included with Windows, and Git, which the script offers to install.

1. Download `Lobster-Export.zip` from your organization's approved location. Right-click it, select **Extract All**, and open the extracted `Lobster export` folder. Don't run the script from inside the zip file.
2. Double-click `Get-LobsterRepo.cmd`.
3. If Git is missing, type `Y` to install Git for Windows with Windows Package Manager, and then follow its prompts.
4. Press Enter to continue, and choose **Yes** when Windows asks for administrator approval.
5. Microsoft Edge opens the Microsoft sign-in page. Choose your own work account. Don't use another person's account.
6. When the browser says you're signed in, return to the PowerShell window. Choose **Yes** at the second administrator prompt.
7. If the script finds more than one `lobster.repo`, type the number of the one to download.
8. When the download finishes, File Explorer opens the new folder.

The folder is named `Lobster export <date time>` and is in your user profile. It contains:

| Item | Contents |
| --- | --- |
| `Latest files` | A readable copy of the files in the latest version, such as memories and session records. |
| `repository.git` | The full Git repository, including earlier versions and history. |
| `README.txt` | A short description of the copy. |

The copy can contain sensitive personal and organizational information. Keep it in a protected location.

If something goes wrong, use the following table.

| Message | What to do |
| --- | --- |
| Administrator approval was declined | Run the script again and choose **Yes**, or ask IT support to run it with you. |
| Hosts file already has a different entry | Ask IT support to review the existing `cowork.local.microsoft.com` entry. |
| Browser shows a certificate warning | Don't bypass it. Close the tab and report it to IT support. |
| Your organization has not approved this sign-in | Ask IT support. The Cowork application might need consent in your organization. |
| Could not connect after 3 attempts | Check your network, VPN, or proxy connection, and then run the script again. |
| No `lobster.repo` was found | Your Autopilot workspace might be stored elsewhere. Ask your support team. |
| Some branch or tag references could not be downloaded | The copy is incomplete. Run the script again into a new folder. |
| Temporary setup could not be removed automatically | Send the warning text to IT support. It names the hosts file line and certificate to remove. |

To see more detail, open PowerShell in the script folder and run `.\Get-LobsterRepo.ps1 -Verbose`. To choose a different new folder, add `-OutputFolder`. The folder must not be synchronized by OneDrive.

For an approved compliance or privacy request, your administrator can also export a copy of your Autopilot data. For more information, see [Export a user's Autopilot data](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure#export-a-users-autopilot-data).

### Remove a saved preference

Name the subject and specify removal from saved memory rather than omission from the current reply. You can also remove a memory in **Review what [name] knows**.

1. Ask, "Forget my old status-update format and remove that preference from your accessible memory notes. Tell me which records changed and anything you couldn't remove."
2. Ask Autopilot to inspect the affected notes again and report what it now remembers about that preference.
3. Review separate exports, summaries, or files that might still contain it.

A reported removal doesn't establish that retention-managed records, backups, or all copies were erased. Use your organization's data-management process when you need a formal access, retention, or deletion response.

### Manage conversation history separately

Use the activity route above to find the relevant work. You can also ask, "List the past conversations you can access and distinguish them from background or automation sessions."

To delete a conversation, select the **...** menu next to it in the conversation list. A deleted conversation is removed from the list, but its stored record stays until you ask Autopilot to remove it. To remove it permanently, ask "Delete the session titled [name]," then follow up with "Can you permanently delete it now?" and confirm the outcome. Confirm the selected conversation before a destructive action.

When you edit or delete a message in your Teams chat with Autopilot, Autopilot's copy of the conversation is updated too. Starting a new conversation isn't a memory-deletion operation. Independently saved memory and exports need separate review.

If you want to start over with a new Autopilot, export anything you want to keep first, and then contact your administrator. Don't rename, move, or delete Autopilot's files yourself.

---
