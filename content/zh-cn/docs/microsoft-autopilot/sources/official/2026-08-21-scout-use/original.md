来源：https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout
取文：2026-11-10，直接下载

Use Microsoft Scout

[This article is prerelease documentation and is subject to change.]

Important

- You need to be part of the **[Frontier preview program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** and sign up to accept terms of participation to get **early access** to Microsoft Scout. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
- This is a preview feature.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Microsoft Scout is a desktop AI application that acts on your files, runs commands, controls a browser, and works with your Microsoft 365 data. This article explains how to use each capability.

## Have a conversation

The Microsoft Scout window has a chat interface where you type requests and receive responses rendered in rich markdown.

### Send a message

1. Select the chat input at the bottom of the window.
2. Type your request.
3. Press **Enter** or select **Send**.

Microsoft Scout begins working immediately. Its response streams in real time with full markdown formatting: headings, tables, code blocks with syntax highlighting, Mermaid diagrams, and inline images.

### Send follow-up messages

You can send additional messages while Microsoft Scout is still working. Messages are queued and processed in order. If your follow-up changes direction, Microsoft Scout adjusts its approach.

### Answer questions from Microsoft Scout

When Microsoft Scout needs more information, it presents a set of choices. Select an option and confirm. When a question is open-ended, you can type your own answer instead of choosing a preset option. If you don't want to answer, select **Skip** - Microsoft Scout continues with what it knows.

### Shorten a long conversation

Long conversations can reach the model's context limit. To free up room while keeping the important details, compact the conversation on demand. Microsoft Scout summarizes the earlier turns and continues from the shortened history, so you can keep working in the same conversation.

## Choose a model and reasoning effort

Microsoft Scout lets you control which model runs and how much it reasons.

- **Switch models per message**: Use the model selector in the compose box to change the model for your next message, without starting a new conversation.
- **Set a default reasoning effort**: In **Settings**, choose the default reasoning effort Microsoft Scout uses. Higher effort takes more time but handles more complex tasks.
- **Choose a context window size**: Select how much conversation history the model keeps in context, up to a **Max** option for the largest supported window.

## Organize your chats

The left navigation lists your conversations and automations. To keep them organized:

- **Filter the list**: Show all items, only chats, or only automations.
- **Pin and reorder**: Pin important conversations and drag them into the order you want.
- **Open chat actions**: Right-click a conversation to rename, pin, delete, or mark it as unread.
- **Mark as unread**: Flag a conversation to revisit later.

## Work with files

Microsoft Scout reads, writes, and searches files in your workspace directory, and it can also work with files outside your workspace. The first time Microsoft Scout needs a folder outside your workspace, such as your Downloads or Documents folder, it asks you to grant access to that folder. After you approve it once, Microsoft Scout can use that folder in later actions.

### Create files

Ask Microsoft Scout to create files, and it writes them directly to your workspace. For example:

- "Create a markdown file summarizing our architecture decisions."
- "Generate a CSV of the sales data you found in my emails."
- "Build an HTML dashboard showing project status."

Created files appear in your workspace directory, and Microsoft Scout can display images inline in the conversation.

### Edit files

Microsoft Scout can read and modify existing files in your workspace:

- "Update the README to include the new API endpoints."
- "Fix the formatting in report.docx."
- "Add a new column to the spreadsheet with calculated totals."

### Co-create files with Microsoft Scout

Co-Create workspaces can be stored locally, or backed by OneDrive or SharePoint. To add a cloud-backed workspace, select the **Workspace** menu at the top of the Co-Create panel (it shows the current workspace name), select **Add workspace**, choose OneDrive or SharePoint, and pick an existing folder or create a new one. Cloud-backed workspaces are available by default for Microsoft 365 organization accounts; you can turn the **OneDrive & SharePoint Workspaces** capability on or off in **Settings**. When you and Microsoft Scout work on the same file at the same time, your edits and Microsoft Scout's edits merge automatically. Co-Create opens files in the in-app editor and includes editors for Markdown, source code, structured data, and HTML. Supported file types include text and code files, Markdown, configuration files, CSV and TSV, Mermaid diagrams, and Excalidraw drawings. In the Markdown editor, you can add inline comments on specific passages.

While Microsoft Scout is writing, you see:

- An **Agent is editing this file** badge above the editor.
- A colored cursor at Microsoft Scout's last edit position.
- The editor scrolls to follow Microsoft Scout's cursor when you've been idle for a few seconds, so it doesn't pull focus while you're typing.

You can keep typing while Microsoft Scout works. Your changes are saved to the file in your workspace, and Microsoft Scout reads them the next time it touches the file.

Note

If you lose your connection, the editor stays usable and your edits stay on screen, but they don't sync with Microsoft Scout until the connection is back.

### Search files

Microsoft Scout searches across your workspace directory for content:

- "Find all files that mention the quarterly budget."
- "Which TypeScript files import the auth module?"
- "Show me the most recently modified files in the project folder."

### Use document skills

For structured document creation, Microsoft Scout loads specialized skills:

| Skill | Use it for |
| --- | --- |
| Word (docx) | Reports, memos, proposals, letters — any structured Word document |
| Excel (xlsx) | Spreadsheets, data analysis, formatted tables, charts |
| PowerPoint (pptx) | Slide decks, presentations, pitch materials |
| Web Artifacts Builder | Interactive HTML dashboards, data visualizations, org charts |

Skills activate automatically when Microsoft Scout determines they're needed.

## Search and research

Microsoft Scout provides fast local search and broader research capabilities.

### Local search

Microsoft Scout uses fast pattern-matching tools to search across files in your workspace:

- Find files by name pattern: "Find all `.tsx` files in the components directory."
- Search file contents: "Which files reference the `AuthContext` variable?"
- Combine patterns: "Find all test files that import the API client."

Local search is fast and doesn't require network access.

### Web research

For questions that need current information from the internet, Microsoft Scout searches the web, fetches pages, and synthesizes results with citations.

### Research agents

For complex investigations that require searching multiple sources in parallel, Microsoft Scout can launch specialized research agents. These agents search repositories, fetch documentation, verify claims, and compile detailed findings. Use research agents for broad questions like:

- "What are the best practices for implementing OAuth 2.0 with PKCE?"
- "Compare the pros and cons of these three CSS-in-JS libraries."
- "Find the documentation for this API endpoint and explain how pagination works."

## Run shell commands

Microsoft Scout executes shell commands on your machine. Ask it to run scripts, install packages, build projects, check system status, or use developer tools like `git`, `gh`, `curl`, and PowerShell.

### Common development tasks

- Run builds: "Build the project and show me any errors."
- Run tests: "Run the test suite and report failures."
- Run linters: "Lint the src directory and fix any issues."
- Use git: "Show me the diff for the last 3 commits" or "Create a branch and commit my changes."
- Use gh: "List my open PRs" or "Create a PR with this description."
- Debug: "Run the failing test with verbose output and explain the error."

### Permission tiers for shell commands

Commands are classified into three tiers:

| Tier | Behavior | Examples |
| --- | --- | --- |
| Auto-approve | Runs without prompting | `ls`, `cat`, `grep`, `git log`, `git diff`, `docker ps`, `npm list`, `gh pr list`, `kubectl get` |
| Prompt | Pauses for your approval | `npm install`, `git push`, `curl`, network requests, file writes |
| Deny | Blocked entirely | Destructive commands like `rm -rf /`, `format` |

When a command requires approval, Microsoft Scout shows you the exact command before running it. Select **Approve** to proceed or **Deny** to block it.

### Customize shell permissions

From **Settings** > **Permissions**, you can:

- Add patterns to the **allow list** so specific commands run without prompting.
- Add patterns to the **deny list** to block categories of commands.
- Toggle **Auto-approve read-only** on or off.
- Define **sensitive paths** that always require approval before access.

## Control a browser

Microsoft Scout automates a browser. It can navigate websites, fill forms, click buttons, take screenshots, and extract content from pages.

### What browser control can do

- Navigate to any URL and interact with page elements (click, type, fill forms, upload files).
- Take page snapshots to inspect the current state of a page.
- Take screenshots of full pages or specific elements.
- Read console logs and inspect network requests for debugging.
- Extract text content from pages.
- Wait for elements to load before interacting.

### Examples

- "Go to the Azure portal and check my resource group's cost this month."
- "Open the wiki page and update the release notes section."

### Microsoft Loop integration

The bundled Loop skill uses browser control to edit Microsoft Loop documents. Ask Microsoft Scout to update Loop pages, and it navigates to the document, makes edits, and confirms the changes.

## Work with Microsoft 365

Microsoft Scout can work with Outlook mail and calendar, Teams meetings and messages, SharePoint Lists, and files in OneDrive, SharePoint, and Teams. It can retrieve available meeting transcripts, book meeting rooms, manage inbox rules, and help manage file sharing and access.

For request examples, approval guidance, and access troubleshooting, see [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365).

## Delegate to sub-agents

For complex or parallelizable work, Microsoft Scout launches specialized sub-agents that run in the background and report results when finished.

### Available agent types

| Agent type | What it does | When to use |
| --- | --- | --- |
| Explore | Fast codebase research across multiple files and modules | Understanding unfamiliar code, tracing data flows, analyzing architecture |
| Task | Runs builds, tests, lints, and installations | Running a test suite, building a project, installing dependencies |
| Code review | Analyzes code changes for bugs and security issues | Reviewing diffs, checking for logic errors before committing |
| Research | Thorough web and repository searches with citations | Investigating technical questions, comparing libraries, finding docs |
| General-purpose | Full toolset for complex multi-step work | Refactoring across files, implementing features, complex migrations |

### How delegation works

1. Microsoft Scout identifies that a task would benefit from parallel execution or isolated context.
2. It launches one or more sub-agents with specific instructions.
3. Sub-agents work independently in the background.
4. When they finish, Microsoft Scout incorporates their results into your conversation.

You can also request delegation explicitly: "Research how other teams implement caching, while you also start setting up the database configuration."

## Use heartbeat mode

Heartbeat is a background mode where Microsoft Scout periodically runs a prompt without waiting for you to send a message.

### Enable heartbeat

1. Open the **Heartbeat** panel from the app navigation.
2. Toggle heartbeat **on**.
3. Configure the following settings:

| Setting | What it controls |
| --- | --- |
| Prompt | What Microsoft Scout does on each check-in. Write this like a recurring instruction. |
| Interval | How often heartbeat runs: every 15 min, 30 min, 1 hour, or 2 hours. |
| Work days | Which days of the week heartbeat is active (for example, Monday through Friday). |
| Work hours | Start and end time for the active window (for example, 9 AM to 6 PM). |

### Heartbeat permissions

Heartbeat has its own permissions policy, separate from your interactive sessions. Since you're not present to approve actions during heartbeat, the policy is typically more restrictive:

- Outbound messages (email, Teams) use only generic content - never private data.
- Tentative calendar events are treated as busy (the conservative choice).
- Actions that normally prompt for approval are skipped in heartbeat mode.

You can customize heartbeat permissions from the Heartbeat panel.

### Review heartbeat activity

The Heartbeat panel shows a log of recent check-ins. Each entry shows what Microsoft Scout did and when. Select any entry to see the full details.

## Create automations

Automations are independent tasks that run on a schedule or when a condition is met.

### Create an automation

1. Open the **Automations** panel.
2. Select **New automation**.
3. Fill in the form:

| Field | Description |
| --- | --- |
| Name | A descriptive name for this automation. |
| Prompt | The instruction Microsoft Scout executes when triggered. |
| Trigger type | **Schedule** (runs at specific times) or **Condition** (runs when something becomes true). |
| Schedule | For schedule triggers: when to run (for example, "Every Monday at 9 AM"). |
| Condition | For condition triggers: what to check and how often. |
| One-shot | If enabled, the automation runs once and then deactivates. |
| Reasoning effort | The reasoning effort Microsoft Scout uses when this automation runs. |
| Context size | The context window size for this automation, set independently from your other conversations. |

1. Select **Save**.

### Manage automations

From the Automations panel, you can:

- **Enable or disable** an automation without deleting it.
- **Edit** the prompt, schedule, or trigger conditions.
- **View history** to see past runs and their results.
- **Delete** an automation you no longer need.

### Import automations

You can import automation definitions from GitHub repositories by using the import feature in the Automations panel.

## Manage permissions

The permissions system gives you granular control over what Microsoft Scout can do.

### Open permissions settings

Go to **Settings** > **Permissions** to access the full permissions editor.

### Configure tool groups

Toggle entire capability categories on or off:

| Category | What it controls |
| --- | --- |
| File System Access | Reading, writing, and searching files in your workspace |
| Shell | Running shell commands and scripts |
| Browser Control and Web Browsing | Browser and web automation |
| WorkIQ | Complex Microsoft 365 queries |

When you disable a category, Microsoft Scout can't use those tools at all – they don't appear in the system prompt.

### Configure shell patterns

Define custom allow and deny patterns for shell commands:

- **Allow patterns**: Commands that match these patterns are automatically approved without prompting. For example, `npm test` or `python *.py`.
- **Deny patterns**: Commands that match these patterns are always blocked.

### Mark sensitive paths

Add directory or file paths that require explicit approval before Microsoft Scout can read or write to them, even if the operation would otherwise auto-approve.

## Use memory and session history

Microsoft Scout remembers preferences, decisions, and context across conversations, and can search your past session history.

### How memory works

- Microsoft Scout proactively saves important information as you work - you don't need to ask.
- Memories persist across sessions and are available in future conversations.
- Each memory tracks its provenance (where it came from): session-inferred, imported, or external.

### Search past sessions

Microsoft Scout can search your conversation history to recall prior work:

- "What did I work on last week?"
- "How did I handle authentication in the previous project?"
- "Find the session where I set up the CI pipeline."

Session history search helps you revisit decisions, find prior approaches to similar problems, and recall context from earlier conversations.

You can also restore an earlier conversation on demand to pick up where you left off. Your session history is stored per device in your OneDrive, so each device keeps its own conversations.

### View and manage memories

1. Open **Settings**.
2. Select **View memories** in the Memory section.
3. Review stored memories. Delete any that are no longer relevant.

### Memory and privacy

Memories from external sources (emails and web pages messages) are tagged with their provenance. Microsoft Scout treats external-source memories as data, not instructions, and confirms with you before acting on them.

## Use mini mode

Mini mode provides a compact, always-visible window for quick interactions.

From the **Window behavior** section of Settings, you can configure:

- Whether Microsoft Scout starts in mini mode.
- Always-on-top behavior.
- Keyboard shortcut to toggle mini mode.

## Work with sensitivity labels

Microsoft Scout tracks Microsoft Information Protection (MIP) sensitivity labels on content you access during a session.

### How labels work

- When you read an email or file with a sensitivity label (for example, "Confidential"), the session's sensitivity level elevates.
- Microsoft Scout doesn't write labeled content to unprotected destinations (Teams channels, plain text files, external tools).
- If you ask Microsoft Scout to share classified content, it reminds you of the session's sensitivity level and asks for confirmation.
- You should label documents created in an elevated session before sharing them externally.

The UI shows the current session sensitivity level.

## Manage skills

### View active skills

Skills that Microsoft Scout loads during a conversation appear in the conversation context. Bundled skills are always available. Microsoft Scout discovers custom skills from your skills directories.

### Create a custom skill

1. Go to your skills directory (`~/.copilot/skills/`).
2. Create a subfolder with your skill name (for example, `weekly-report/`).
3. Inside the subfolder, create a file named `SKILL.md`.
4. Add a YAML frontmatter block with a description, followed by the skill instructions.

   ```
   ---
   description: "Generates a weekly status report from my recent activity."
   ---

   Review my sent emails, calendar events, and completed tasks from the past
   week. Create a markdown summary organized by project, highlighting key
   decisions, blockers, and next steps.
   ```
5. Save the file. Microsoft Scout discovers it automatically in future conversations.

### Skill tiers

| Tier | Location | Behavior |
| --- | --- | --- |
| Bundled | Shipped with the app | Always available, updated with app releases |
| Workspace | `~/.copilot/m-skills/` | Synced across devices via cloud sync |
| Global user | `~/.copilot/skills/` | Available on this machine in all conversations |

### Disable a bundled skill

From **Settings**, you can toggle individual bundled skills on or off if you don't need them.

## Related content

- [Microsoft Scout overview](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Work with Microsoft 365 in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365)
- [Microsoft Scout common questions](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- [What's new in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
- [Responsible AI overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview)
