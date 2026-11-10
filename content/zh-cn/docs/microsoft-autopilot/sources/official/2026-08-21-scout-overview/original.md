来源：https://learn.microsoft.com/en-us/microsoft-scout/overview
取文：2026-11-10，直接下载

Microsoft Scout (Frontier) overview

[This article is prerelease documentation and is subject to change.]

Important

- You need to be part of the **[Frontier preview program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** and sign up to accept terms of participation to get **early access** to Microsoft Scout. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
- This is a preview feature.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Microsoft Scout is a desktop AI application for Windows and macOS that takes action on your behalf. It reads and writes files, runs shell commands, controls a browser, queries your Microsoft 365 data, and works autonomously in the background. You describe what you need in a chat conversation, and Microsoft Scout carries out the work - with your approval before sensitive actions.

## What can Microsoft Scout do?

Microsoft Scout combines local and cloud capabilities in a single desktop application:

- **Acts on your files**: Creates, edits, and searches documents in your workspace. Works with Word, Excel, PowerPoint, code files, and more.
- **Runs commands**: Executes shell commands, builds, tests, and scripts with a tiered permission system.
- **Automates browsers**: Navigates web pages, fills forms, and interacts with web applications.
- **Connects to Microsoft 365**: Works with Outlook mail and calendar, Teams meetings and messages, SharePoint Lists, and files in OneDrive, SharePoint, and Teams. For more information, see [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365).
- **Works autonomously**: Runs in the background on schedules or triggers you define.
- **Delegates work**: Launches specialized sub-agents for parallel research, code review, and complex tasks.

## How it works

1. **You describe your task** in natural language in the chat interface.
2. **Microsoft Scout selects tools** and works through the steps, showing progress in real time.
3. **You approve sensitive actions** before they execute (sending email, running commands, writing files).
4. **Microsoft Scout delivers results** directly in the conversation or saves files to your workspace.

## Key features

### Local and cloud integration

Microsoft Scout runs on your desktop with permissioned access to your approved file system and shell, while also connecting to your Microsoft 365 account. This means it can edit code in your workspace, run a build, send the results in an email, and schedule a follow-up meeting — all in one conversation.

Microsoft Scout can also retrieve available Teams meeting transcripts, book meeting rooms, work with SharePoint Lists and Outlook inbox rules, and help manage file sharing and access. For more information, see [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365).

### Granular permissions

You control what Microsoft Scout can do through a detailed permission system:

- Enable or disable entire capability categories, such as the file system, shell, browser, and Microsoft 365.
- Define which shell commands auto-approve and which require your permission.
- Mark sensitive directories that always require explicit approval.

### Autonomous modes

- **Heartbeat**: Periodic background check-ins (every 15–120 minutes) that run prompts while you're away.
- **Automations**: Scheduled or condition-triggered tasks that execute independently.

### Co-Create

Co-Create lets you and Microsoft Scout edit the same supported file at the same time, with your changes merged automatically. Co-Create workspaces can be stored in OneDrive or SharePoint. For more information, see [Co-create files with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#co-create-files-with-microsoft-scout).

### Memory and delegation

Microsoft Scout remembers your preferences and decisions across conversations. For complex work, it can launch specialized sub-agents that run in parallel and report results when finished.

## Bundled skills

Microsoft Scout includes bundled skills for common tasks:

| Skill | What it does |
| --- | --- |
| Word, Excel, PowerPoint | Create and edit Microsoft Office documents |
| Loop | Edit Microsoft Loop documents through browser automation |
| Web Artifacts Builder | Build interactive HTML dashboards and visualizations |

You can also create your own custom skills by placing `SKILL.md` files in your skills directory.

## Platforms

Microsoft Scout is available as a desktop application for:

- **Windows** (Windows 11 or later)
- **macOS** (macOS 12 Monterey or later)

## Next steps

- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started) — Install, configure, and run your first task
- [Use Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout) — Comprehensive guide to all capabilities
- [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)
- [Microsoft Scout FAQ](https://learn.microsoft.com/en-us/microsoft-scout/faq) — Answers to common questions

## Related content

- [What's new in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
- [Responsible AI overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview)
