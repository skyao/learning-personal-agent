来源：https://learn.microsoft.com/en-us/microsoft-scout/get-started
取文：2026-11-10，直接下载

Get started with Microsoft Scout

[This article is prerelease documentation and is subject to change.]

Important

- You need to be part of the **[Frontier preview program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** and sign up to accept terms of participation to get **early access** to Microsoft Scout. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
- This is a preview feature.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Microsoft Scout is a desktop AI application that takes action across your files, shell, browser, development tools, and Microsoft 365 data. This article walks you through installation, sign-in, and your first conversation.

## Prerequisites

Before you begin, make sure you have:

- **A supported platform**: Windows 11 or macOS 12 (Monterey) or later.
- **A Microsoft 365 work or school account** associated with your organization: Personal Microsoft accounts are not supported.
- **Microsoft 365 Copilot access**: An active [Microsoft 365 Copilot license](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-licensing) assigned to your account.
- **Microsoft Visual C++ redistributable (Windows only)**: The latest [Microsoft Visual C++ redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist) library.
- **Local Administrator permissions**: Permission to install applications on your machine, including an Intune-enabled account.
- **A GitHub Copilot Business or Enterprise license**: Enables access to a Copilot subscription. Learn how to [set up GitHub Copilot for your organization](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-organization).

Your IT admin also needs to complete the Microsoft Scout access setup before you can sign in. For details, see [Admin access overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview).

## Install Microsoft Scout

[Download and install the Microsoft Scout installer](https://aka.ms/msscout) appropriate for Windows or macOS.

Run the installer and follow the on-screen prompts. After installation, Microsoft Scout appears in your applications menu.

## Sign in

1. Open Microsoft Scout.
2. Select **Sign in to Microsoft 365**.
3. Authenticate with your organizational Microsoft 365 credentials.
4. Grant the requested permissions when prompted.
5. If your organization uses GitHub Enterprise Cloud, turn on **Use a GitHub Enterprise host** and enter your enterprise host (for example, `your-org.ghe.com`). Leave this off to sign in on github.com.
6. Select **Sign in to GitHub** and sign in with a GitHub account that has a Business or Enterprise GitHub Copilot license. Complete the sign-in in your browser when prompted.

Microsoft Scout signs you in securely using your organization's Microsoft 365 identity. Your organization's identity provider manages your credentials.

## Configure your workspace

After signing in, Microsoft Scout asks you to set a workspace directory. This folder is where Microsoft Scout reads and writes files.

1. Select a workspace directory or accept the default location.
2. Review the initial permissions configuration.

You can change your workspace directory later in **Settings**.

Tip

Choose a directory you use for active projects. Microsoft Scout operates within this directory, so it can create documents, run scripts, and organize files.

## Choose a personality (optional)

Microsoft Scout offers personality presets that change its conversational style. The default personality is helpful and professional - suitable for most users. You can switch at any time using the application icon next to the prompt entry field.

## Connect to Microsoft 365

To access your Microsoft 365 data (email, calendar, Teams, and OneDrive):

1. Open **Settings**.
2. Select **Sign in to Microsoft 365** and complete the authentication flow.

Once connected, Microsoft Scout can help you work across your Microsoft 365 content. It can read, draft, and manage email, calendar events, Teams chats, and OneDrive files. Actions that send, share, reply, forward, or update information visible to others require your confirmation before they run.

## Start your first conversation

1. Select the chat input at the bottom of the window.
2. Type what you want done. For example:
   - "Create a Word document summarizing my emails from this week."
   - "Find an open time tomorrow for a 30-minute meeting with Alex."
   - "Prepare a brief for my meetings tomorrow."
   - "Search my workspace for files mentioning quarterly review."
3. Press **Enter** or select **Send**.

Microsoft Scout begins working and shows progress in the conversation, including actions, permission prompts, created files, and final results.

Tip

Be specific about what you want. Instead of "Help me with email," try "Draft a reply to Sarah's email about the budget review, thanking her and confirming I'll attend the Thursday meeting."

## Review default settings

Scout is configured with the following defaults:

- **WorkIQ connectivity: ON**  
  Enables search across your Microsoft 365 data out of the box.
- **Shell access: ON**  
  Allows Microsoft Scout to request execution of terminal commands. Actions still follow the permission system and may require approval.
- **Auto-approve: OFF**  
  All actions require user confirmation. Auto-approve must be explicitly enabled per capability.

## Understand permissions

As Microsoft Scout works, it might need your approval for certain actions. The permission system has three levels:

| Level | What happens |
| --- | --- |
| Auto-approve | The action runs automatically if explicitly allowed by configuration. |
| Prompt | Microsoft Scout pauses and shows you what it wants to do. You approve or deny. |
| Deny | The action is blocked. Dangerous commands use this level by default. |

When an approval prompt appears:

1. Review what Microsoft Scout wants to do.
2. Select **Approve** to allow the action or **Deny** to block it.
3. Optionally, select **Always allow** to auto-approve similar actions in the future.

You can customize permissions in **Settings** > **Permissions** at any time.

## Review results

Microsoft Scout renders results directly in the conversation using rich markdown: headings, tables, code blocks with syntax highlighting, Mermaid diagrams, and inline images. Files that Microsoft Scout creates are saved to your workspace directory.

To find files Microsoft Scout created:

1. Check your workspace directory for new files.
2. Images and visual artifacts might appear inline in the conversation and are also saved to your workspace when created as files. If you view the raw message, inline images might appear as markdown image links that point to the saved file.
3. Documents (Word, Excel, PowerPoint) are saved to your workspace and can be opened in their native applications.

## Explore settings

Open **Settings** to configure Microsoft Scout. Settings is a single, grouped window with a search box at the top, so you can find an option by typing its name. Key groups include:

- **Appearance**: Theme (light, dark, or system)
- **Default model**: Choose which AI model to use
- **Default reasoning effort**: Set how much the model reasons by default
- **Workspace directory**: Change where files are saved
- **Permissions**: Control tool access and shell commands
- **Integrations**: Connect the services Microsoft Scout works with
- **Memory**: View and manage stored preferences
- **Privacy, Cloud sync, Power management, Window behavior**: Additional customization options

For detailed configuration instructions, see [Configure tool groups](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout#configure-tool-groups).

## Next steps

- [Use Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout) — Comprehensive guide to all capabilities
- [Work with Microsoft 365](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365) — Use meetings, mail, lists, and files
- [Microsoft Scout overview](https://learn.microsoft.com/en-us/microsoft-scout/overview) — Feature summary and product overview

## Related content

- [Microsoft Scout overview](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [Microsoft Scout common questions](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- [What's new in Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
- [Responsible AI overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview)
