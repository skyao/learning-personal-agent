来源：https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq
取文：2026-11-10，直接下载

Responsible AI FAQ for Microsoft Scout

[This article is prerelease documentation and is subject to change.]

Important

- You need to be part of the **[Frontier preview program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** and sign up to accept terms of participation to get **early access** to Microsoft Scout. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
- This is a preview feature.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

These frequently asked questions (FAQ) describe the AI impact of Microsoft Scout, the AI desktop application.

## What is Microsoft Scout?

Microsoft Scout is a desktop AI application for Windows and macOS that takes action on your behalf across your files, shell, browser, and Microsoft 365 data. You describe what you need in natural language, and Microsoft Scout carries out the work — reading and writing files, running commands, controlling a browser, querying your Microsoft 365 account, and working autonomously in the background. Each action that Microsoft Scout takes is visible in the conversation. Sensitive actions require your explicit approval before they're executed.

## What are Microsoft Scout's capabilities?

Microsoft Scout can:

- Read, write, and search files in your workspace directory.
- Run shell commands, builds, tests, and scripts by using a three-tier permission system (auto-approve, prompt, deny).
- Explore codebases, apply patches, run linters, and debug failures using git, gh, curl, and PowerShell.
- Automate browser interactions — navigate pages, fill forms, take snapshots, inspect console logs and network requests, and upload files.
- Search your workspace with fast pattern-matching tools.
- Search the internet for real-time information.
- Launch specialized research agents for parallel investigations with detailed findings and citations.
- Read and manage your email, calendar, Teams chats, OneDrive files, and meetings.
- Query across Microsoft 365 services using WorkIQ for complex questions.
- Create and edit Word documents, Excel spreadsheets, PowerPoint presentations, Loop documents, and interactive HTML artifacts.
- Run autonomously in the background on a schedule (heartbeat mode).
- Execute scheduled or condition-triggered automations.
- Delegate complex work to specialized sub-agents (explore, task, code review, research, general-purpose).
- Remember preferences, decisions, and context across conversations.
- Search past session history to recall prior work and decisions.

During a conversation, Microsoft Scout loads specialized skills as needed.

## What is Microsoft Scout's intended use?

Microsoft Scout is designed for information workers and developers who want to automate tasks across their local machine and Microsoft 365 account. Typical use cases include:

- Building and testing software projects (running builds, tests, lints, debugging failures).
- Exploring and editing codebases (searching files, applying patches, refactoring).
- Automating web workflows (filling forms, extracting data from portals, interacting with enterprise apps).
- Managing Microsoft 365 data (drafting and sending emails, scheduling meetings, organizing files).
- Running autonomous background tasks (inbox triage, schedule monitoring, recurring reports).
- Creating structured documents from unstructured input (meeting notes → formatted report, data → spreadsheet).

Microsoft Scout isn't intended for use cases that require guaranteed accuracy without human review. Examples are legal filings, medical decisions, or financial transactions that bypass approval processes. Always review AI-generated content before approving actions that send, post, or share information externally. Carefully consider whether optional modes that let the app carry out certain actions without per-step approvals are appropriate for the use case.

## How is Microsoft Scout evaluated, and what metrics are used to measure performance?

Microsoft evaluates Microsoft Scout across several areas:

- **Task completion**: Whether Microsoft Scout successfully carries out the requested action (for example, it creates a file, runs a command, or sends an email).
- **Response quality**: Whether its output meets the user's intent based on the natural language instruction.
- **Safety and compliance**: Ongoing evaluation to ensure Microsoft Scout operates within Microsoft's responsible AI principles.

## What are the limitations of Microsoft Scout, and how can users minimize the impact of these limitations?

Current limitations include:

- Microsoft Scout might misinterpret ambiguous or overly broad instructions, leading to actions that don't match your intent.
- Treat AI-generated documents, messages, and code as drafts. Always review content before sending, sharing, or deploying.
- Microsoft Scout might produce inaccurate information when searching across your workspace or Microsoft 365 account, particularly when source data is incomplete or outdated.
- Complex, multi-step tasks with many dependencies might not always complete as expected, which can introduce risk.
- Shell commands are subject to the three-tier permission system. Dangerous or unexpected commands might be blocked or require approval.
- Microsoft Scout operates within your workspace directory. It can't access files outside that directory unless you explicitly grant permission.
- Microsoft Scout depends on your existing Microsoft 365 permissions. It can't access data or services that your account isn't authorized to use.
- Microsoft doesn't validate custom skills authored by users. Review custom skill outputs carefully, as their quality depends on how the skill was written.
- Background modes (heartbeat and automations) use a more restrictive permission policy than interactive conversations.

To minimize these limitations:

- Provide clear, specific instructions. Include details about what you want done and where. Simpler tasks are more likely to be completed with a higher degree of accuracy. Thoroughly test whether complex or multi-step tasks are being completed as expected.
- Review all generated content such as code, emails, documents, and messages, before approving actions.
- Use the pause and cancel controls to stop work if Microsoft Scout is heading in the wrong direction.
- Customize shell permissions to match your workflow and security requirements.
- Mark sensitive directories or files to require explicit approval before access.
- Tenant admins and users should carefully consider when optional autonomous execution modes that don’t require per-step approval are appropriate to use. Use these modes only for low-risk scenarios after carefully reviewing the task, permissions, and any data or systems that might be affected. Admins can disable or restrict such modes for their organizations.

## How does Microsoft Scout handle action approval?

Before Microsoft Scout performs a sensitive action, such as sending an email, posting in Teams, running a command that writes to disk or accesses the network, or modifying a file outside auto-approved patterns, it presents an approval prompt. You have the following options:

- **Approve**: Allow the action to proceed this one time.
- **Always allow**: Approve and add this pattern to the auto-approve list for future actions.
- **Deny**: Block the action.

For certain actions, such as sending an email or running a shell command, Microsoft Scout displays a preview of the content or the exact command before you approve. Microsoft Scout doesn't execute sensitive actions without your explicit consent.

## How does Microsoft Scout handle my data?

Microsoft Scout operates within the security and compliance boundaries of Microsoft 365 and your local machine, and (in certain cases) external AI services, based on your instructions, permissions, and configuration.

- **Authentication and access controls**: Microsoft Scout uses your existing Microsoft 365 credentials and operates with the same permissions and access controls that apply to your account. It accesses only services and data that your account is permitted to use.
- **Tenant isolation**: Your Microsoft 365 data is isolated to your organization's tenant, subject to your organization's existing security, compliance and governance controls.
- **External AI processing (GitHub Copilot)**: LLM interactions in Microsoft Scout are processed through GitHub Copilot, which operates under separate terms. In those cases, prompts, content, and related data may be transmitted outside Microsoft 365, including to third-party model providers configured through GitHub Copilot. When data is processed through GitHub Copilot, certain Microsoft 365 protections—such as data residency commitments, retention policies, sensitivity labeling enforcement, eDiscovery, and other compliance controls—do not apply to that processing.
- **Local file access**: Microsoft Scout can read, write, and modify data on your local device or within your configured workspace, based on permissions you grant. It does not access files outside that directory unless you explicitly grant permission.
- **Shell command gating**: Shell commands are subject to a three-tier permission system that you control. Dangerous commands are blocked by default.
- **Data subject rights**: Access, deletion, rectification, and portability requests are supported in accordance with Microsoft's privacy standards.
- **File storage and memory**: Files that Microsoft Scout creates are stored in your workspace directory on your local machine. Session and memory data are stored in the user's OneDrive; OneDrive session data and memory stay inside your tenant and are covered by the Microsoft DPA and your standard OneDrive controls per your Purview configuration. Automation instructions and tool output are stored locally on the end user's device, are not covered by the M365 DPA, and are subject to your endpoint management and device controls.
- **External content tagging**: Emails, web pages, and Teams messages are tagged as external content and treated as data, not instructions, to protect against prompt injection.
- **Sensitivity labels**: Microsoft Scout can recognize and display sensitivity labels associated with content it accesses. However, content generated or modified by Microsoft Scout may not automatically inherit or enforce those labels in all scenarios. Users should apply appropriate labeling and controls before sharing or storing content.

Microsoft Scout doesn't use your data to train AI models.

## What operational factors and settings allow for effective and responsible use?

- Microsoft Scout is a desktop application for Windows and macOS, subject to your organization's access policies and licensing.
- Always review AI-generated content before approving actions that send, post, or share information externally.
- Use the conversation controls (pause, resume, cancel) to manage Microsoft Scout's work if it goes off track.
- Customize shell permissions from **Settings** > **Permissions** to match your workflow and security requirements.
- Mark sensitive directories or files to require explicit approval before access.
- Configure heartbeat and automation permissions separately from interactive conversation permissions to control what Microsoft Scout can do without your presence.
- Administrators can manage access to Microsoft Scout through the Intune admin center, including disabling access for specific users or controlling deployment across the organization.

## Related content

- [Responsible AI overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview)
- [Microsoft Scout overview](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Use Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout)
- [Microsoft Scout common questions](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- [Microsoft AI principles](https://www.microsoft.com/ai/responsible-ai)
