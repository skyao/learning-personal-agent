来源：https://learn.microsoft.com/en-us/microsoft-scout/faq
取文：2026-11-10，直接下载

Microsoft Scout common questions

[This article is prerelease documentation and is subject to change.]

Important

- You need to be part of the **[Frontier preview program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** and sign up to accept terms of participation to get **early access** to Microsoft Scout. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
- This is a preview feature.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Find answers to common questions about Microsoft Scout, the AI desktop application for Windows and macOS.

## What is Microsoft Scout?

Microsoft Scout is a desktop AI application that takes action on your behalf across your files, shell, browser, and Microsoft 365. It reads and writes files in your workspace, runs shell commands, controls a browser, queries your Microsoft 365 data, and works autonomously in the background. You describe what you need in a conversation, and Microsoft Scout carries out the work - with your approval before sensitive actions.

## What can Microsoft Scout do for me?

Microsoft Scout can:

- Read, write, and search files in your workspace directory.
- Run shell commands, builds, tests, and scripts on your machine.
- Explore codebases, apply patches, run linters, and debug failures using git, gh, curl, and PowerShell.
- Automate browser interactions - navigate pages, fill forms, take snapshots, and inspect network traffic.
- Search your workspace with fast pattern-matching tools.
- Search the internet for real-time information.
- Read and manage your email, calendar, Teams chats and channels, OneDrive files, To Do tasks, and meetings.
- Query across Microsoft 365 services using WorkIQ for complex questions.
- Create and edit Word documents, Excel spreadsheets, PowerPoint presentations, and diagrams.
- Run autonomously in the background on a schedule (heartbeat mode).
- Execute scheduled or condition-triggered automations.
- Delegate complex work to specialized sub-agents for parallel execution.
- Remember preferences, decisions, and context across conversations.

For a full breakdown by category, see [What is Microsoft Scout?](https://learn.microsoft.com/en-us/microsoft-scout/overview#what-can-microsoft-scout-do)

## Is Microsoft Scout secure?

Yes. Microsoft Scout operates within your Microsoft 365 security boundaries:

- Authentication uses your organization's Microsoft 365 credentials on Windows.
- Microsoft Scout accesses only services and data your account is permitted to use.
- Shell commands are gated by a permission system that you control.
- You can mark sensitive paths to require explicit approval before access.
- Microsoft Scout tags external content (emails, web pages, Teams messages) as untrusted and treats it as data, not instructions.

## How is Microsoft Scout different from Copilot Chat?

Microsoft Scout is a local desktop AI application that acts on your machine and your Microsoft 365 data, while Copilot Chat is a cloud-based conversational application that generates content and insights.

| Feature | Copilot Chat | Microsoft Scout |
| --- | --- | --- |
| What it is | Cloud-based AI for drafting, summarizing, answering questions | Desktop AI application that acts on your files, shell, browser, and Microsoft 365 |
| Best for | Fast, focused, single-task support | Multi-step workflows, local development, autonomous background tasks |
| Access to local files | No (cloud-based) | Yes (full workspace access) |
| Shell commands | No | Yes (with three-tier permissions) |
| Browser control | No | Yes (browser automation) |
| Autonomous modes | No | Yes (heartbeat and automations) |
| Top scenarios | Quick drafts, Q&A, summarizing documents | Building projects, running tests, browser automation, multi-step workflows, scheduled tasks |

Microsoft Scout runs locally on your desktop and can interact with your development environment, file system, and shell, making it ideal for software development, automation, and tasks that require local access.

## What skills does Microsoft Scout have?

Microsoft Scout includes the following bundled skills:

- Word (docx) — Creates, reads, and edits Word documents.
- Excel (xlsx) — Creates, reads, and edits Excel spreadsheets and CSV files.
- PowerPoint (pptx) — Creates, reads, and edits PowerPoint presentations.
- Loop — Edits Microsoft Loop documents by using browser automation.
- Web Artifacts Builder — Builds interactive HTML dashboards and data visualizations.

You can also create your own custom skills by placing `SKILL.md` files in your skills directory (`~/.copilot/skills/`). Microsoft Scout automatically discovers custom skills.

For detailed descriptions, see [Microsoft Scout skills](https://learn.microsoft.com/en-us/microsoft-scout/overview#bundled-skills).

## Can I create my own custom skills?

Yes. Create custom skills by adding folders with `SKILL.md` files to your skills directory:

- **Bundled skills**: `~/.copilot/bundled-skills/` (shipped with the app, not user-editable).
- **Workspace skills**: `~/.copilot/m-skills/` (synced across your devices).
- **Global user skills**: `~/.copilot/skills/` (available on this machine in all conversations).

Each `SKILL.md` file contains a YAML frontmatter block with a description, followed by the skill instructions in Markdown. Microsoft Scout automatically discovers your custom skills at the start of each conversation.

For step-by-step instructions, see [Create a custom skill](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#create-a-custom-skill).

## What is heartbeat mode?

Heartbeat is an autonomous background mode where Microsoft Scout periodically runs a prompt without waiting for you to send a message. You configure:

- **Prompt**: What Microsoft Scout does on each check-in (for example, triage your inbox or check for schedule conflicts).
- **Interval**: How often it runs (every 15 minutes, 30 minutes, 1 hour, or 2 hours).
- **Work hours**: The days and hours when heartbeat is active.
- **Permissions**: A separate permission policy that controls what heartbeat can do without your presence.

Heartbeat is useful for recurring maintenance tasks, inbox triage, schedule monitoring, and other background workflows that don't require constant attention.

For details, see [Use heartbeat mode](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#use-heartbeat-mode).

## What are automations?

Automations are scheduled or condition-triggered tasks that run independently. Unlike heartbeat (which uses a single repeating prompt), automations are discrete tasks with their own schedule, prompt, and optional multi-step workflows.

- **Schedule-triggered**: Run at specific times (for example, "Every Monday at 9 AM").
- **Condition-triggered**: Run when a condition you define becomes true.
- **One-shot**: Run once and then deactivate.

You create, edit, pause, and delete automations from the Automations panel.

For details, see [Create automations](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#create-automations).

## How do shell command permissions work?

Microsoft Scout uses a three-tier permission system for shell commands:

| Tier | Behavior | Examples |
| --- | --- | --- |
| Auto-approve | Runs without prompting | `ls`, `cat`, `grep`, `git log`, `git diff`, `docker ps`, `npm list`, `gh pr list`, `kubectl get` |
| Prompt | Pauses for your approval | `npm install`, `git push`, `curl`, network requests, file writes |
| Deny | Blocked entirely | Destructive commands like `rm -rf /`, `format` |

You can customize which commands auto-approve and which commands are blocked from **Settings** > **Permissions**. You can also mark directories as sensitive paths that always require approval before access.

For details, see [Manage permissions](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#manage-permissions).

## Can Microsoft Scout delegate work to sub-agents?

Yes. Microsoft Scout can launch specialized sub-agents that run in the background and report results when finished:

| Agent type | What it does |
| --- | --- |
| Explore | Fast codebase research across multiple files and modules |
| Task | Runs builds, tests, lints, and installations |
| Code review | Analyzes code changes for bugs and security issues |
| Research | Thorough web and repository searches with citations |
| General-purpose | Full toolset for complex multi-step work |

By using sub-agents, Microsoft Scout can parallelize complex investigations, run long-running tasks in the background, and handle work that benefits from isolated execution contexts.

For details, see [Delegate to sub-agents](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#delegate-to-sub-agents).

## How do I start using Microsoft Scout?

Getting started takes just a few steps:

1. Download and install Microsoft Scout for Windows or macOS.
2. Sign in with your Microsoft 365 credentials.
3. Configure your workspace directory (where Microsoft Scout reads and writes files).
4. Optionally, connect to Microsoft 365 for email, calendar, Teams, and OneDrive access.
5. Type what you want done in the chat and send your message.

For detailed instructions, see [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started).

## Does Microsoft Scout work on mobile devices?

No. Microsoft Scout is a desktop application for Windows and macOS. It requires local file system access, shell access, and browser control capabilities that aren't available on mobile platforms.

## What file types does Microsoft Scout support?

Microsoft Scout can read and create a wide variety of file types:

- **Word**: `.doc`, `.docx`, `.docm`, `.dot`, `.dotx`, `.odt`, `.rtf`
- **Excel**: `.csv`, `.xls`, `.xlsm`, `.xlsx`, `.ods`
- **PowerPoint**: `.odp`, `.ppt`, `.pptm`, `.pptx`
- **PDF**: `.pdf`
- **Markdown**: `.md`, `.markdown`, `.mdx`
- **Image**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.bmp`, `.svg`, `.ico`
- **Text**: `.txt`, `.log`
- **Code**: `.js`, `.ts`, `.py`, `.java`, `.c`, `.cpp`, `.go`, `.rb`, `.rs`, and others
- **Config**: `.json`, `.yaml`, `.yml`, `.toml`, `.ini`, `.xml`, `.env`
- **Audio**: `.mp3`, `.wav`, `.m4a`, `.ogg`, `.aac`, `.flac`
- **Video**: `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm`, `.wmv`
- **Archive**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`

## Can I preview files without downloading them?

Yes. Microsoft Scout displays results directly in the conversation using rich markdown rendering. Images appear inline, code blocks have syntax highlighting, and tables and diagrams render natively. You can open files saved to your workspace in their native applications.

## How does action approval work?

Before Microsoft Scout takes a sensitive action (such as sending an email, posting in Teams, or running a command that requires approval), it pauses and shows you exactly what it plans to do. Your choices are:

- **Approve**: Let Microsoft Scout proceed with the action.
- **Always allow**: Approve and add this pattern to the auto-approve list for future actions.
- **Deny**: Block the action.

You can also view the technical details of any action before deciding. For shell commands, Microsoft Scout shows the exact command it wants to run.

For details, see [Approve actions](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#have-a-conversation).

## Can I pause or stop Microsoft Scout while it's working?

Yes. You can send follow-up messages at any time to steer Microsoft Scout in a different direction, provide additional context, or ask it to stop. Messages are queued and processed in order.

## What happens if I lose my connection?

If Microsoft Scout loses connection to its backend, work in progress pauses. When the connection is restored, Microsoft Scout resumes automatically. Work done before the disconnection is preserved.

## Where are my files saved?

Files that Microsoft Scout creates are saved to your workspace directory (the folder you configured during setup). You can access these files at any time through your file manager or by asking Microsoft Scout to show you what's in your workspace.

## Can I download all output files at once?

Your workspace directory already saves files locally. You don't need to download them because they're on your machine.

## Can an administrator disable Microsoft Scout?

Administrators manage Microsoft Scout in managed environments through Group Policy and Microsoft Intune. The Microsoft Scout administrative templates let them control who can use Scout and turn off specific capabilities, including background modes like automations. For more information, see [Manage Microsoft Scout with Group Policy](https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy) and [Admin access overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview).

## Are there known limitations?

Yes. The following limitations are by design:

- Microsoft Scout operates within your workspace directory. It can't access files outside that directory unless you explicitly grant permission.
- Shell commands are subject to the three-tier permission system. Dangerous commands are blocked by default.
- Browser control is included with Microsoft Scout.
- Microsoft Scout can only access Microsoft 365 data that your account is authorized to use.
- Microsoft doesn't validate custom skills created by users. Review custom skill outputs carefully.
- Background modes (heartbeat and automations) use a more restrictive permission policy than interactive conversations.

## How do I give feedback?

Share feedback in the following ways:

- **Thumbs up or thumbs down**: Rate any response from Microsoft Scout directly in the conversation.
- **Report issues**: Use the feedback option in the app menu to report problems or suggest improvements.

## Does Microsoft Scout connect to external models for processing?

Yes. Microsoft Scout processes your prompts and content through GitHub Copilot, which connects to AI models from Microsoft and from third-party providers, including open-source models. Scout inherits its model catalog from GitHub Copilot, and your GitHub Copilot admin determines which models are available for Scout to use. You can find details about model providers and related information in the Microsoft GitHub Copilot documentation. Supported models can include third-party and open-source models, including models from China-based providers. Because this processing occurs through GitHub Copilot, it is governed by your organization's [GitHub Customer Agreement](https://github.com/customer-terms) and the [GitHub General Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Are there unsupported countries or regions?

Microsoft Scout is currently available through the Frontier preview program. Availability is determined by enrollment in that program rather than by a Scout-specific list of supported countries or regions, and your organization's administrator controls whether Scout is enabled for you.

Because Microsoft Scout processes prompts and content through GitHub Copilot, GitHub's terms and restrictions apply to that processing, including applicable trade control and sanctions requirements. For details, see [GitHub and Trade Controls](https://docs.github.com/site-policy/other-site-policies/github-and-trade-controls).

Individual model providers might restrict use of their models from certain countries or regions. Your organization is responsible for ensuring that its use of Microsoft Scout, and of the models made available through GitHub Copilot, complies with those restrictions. Administrators can restrict which models and model providers are available. For details, see [Manage admin controls in Intune for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy).

Microsoft Scout isn't available in US Government cloud environments (including GCC, GCC High, and DoD) or in sovereign and national cloud environments.

Regional availability might change as Microsoft Scout moves from preview to general availability.

## Can I sign in with GitHub Enterprise Cloud on ghe.com?

Yes. On the sign-in screen, turn on **Use a GitHub Enterprise host**, enter your enterprise host (for example, `your-org.ghe.com`), and select **Sign in to GitHub**. For sign-in steps, see [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started#sign-in).

## A user has a GitHub Copilot license but still can't sign in to Microsoft Scout. What should I check?

Microsoft Scout needs two GitHub-side conditions, not just a license:

- The user has a Copilot **Business** or **Enterprise** seat assigned.
- Your organization or enterprise policy allows the GitHub Copilot app for that user. An assigned seat alone isn't enough.

If the user has a seat but sees a "GitHub Copilot access required" message or a "You aren't authorized to use this Copilot feature" error, enable the **GitHub Copilot app** policy (and, for app versions before 1.1, the **Copilot in the CLI** policy) at the enterprise and organization level. Enterprise settings override organization settings. Also confirm the user signed in with the organization GitHub account that holds the seat, not a personal account. Allow a few minutes for the change to propagate, and then have the user quit and relaunch Microsoft Scout.

For the full checklist, see [Admin access overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview#troubleshoot-github-copilot-access).

## Can Microsoft Scout retrieve Teams meeting transcripts and book rooms?

Yes. Microsoft Scout can retrieve available Teams meeting transcripts, find meeting rooms, and book rooms. For more information, see [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365).

## Can Microsoft Scout work with SharePoint Lists?

Yes. Microsoft Scout can work with SharePoint Lists. For more information, see [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365).

## Can Microsoft Scout manage Outlook inbox rules?

Yes. Microsoft Scout can manage Outlook inbox rules. For more information, see [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365).

## Can Microsoft Scout share Microsoft 365 files and manage access?

Yes. Microsoft Scout can share OneDrive and SharePoint files with specific people, set view or edit access, and show who currently has access. Files stored in Teams are shared through their SharePoint location. Scout shares with people who sign in—it doesn't create anonymous links—and it can't remove existing access. For more information, see [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365#share-files-and-manage-access).

## Where can I store a Co-Create workspace?

You can store a Co-Create workspace locally, or back it with OneDrive or SharePoint. To add a cloud-backed workspace, open the **Workspace** menu at the top of the Co-Create panel and select **Add workspace**, then choose OneDrive or SharePoint. Cloud-backed workspaces are available by default for Microsoft 365 organization accounts; you can turn the **OneDrive & SharePoint Workspaces** capability on or off in **Settings**. For more information, see [Use Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#co-create-files-with-microsoft-scout).

## Related content

- [Microsoft Scout overview](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Use Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout)
- [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)
- [What's new in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
