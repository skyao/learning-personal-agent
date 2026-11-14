来源：https://mc.merill.net/message/MC1479277
取文：2026-11-14，直接下载（第三方存档站 mc.merill.net；消息中心原文需管理员登录）

MC1479277 - Microsoft Copilot: New ways to work across Microsoft Copilot and Microsoft 365

Message Center

### Summary

Microsoft Copilot updates include a new Home experience, enhanced Office integration, Code and Autopilot features with usage-based billing, Copilot Managed Runtime for enterprise code, and general availability in SharePoint and OneDrive. Admins must configure spending policies and manage access via the Microsoft 365 admin center.

[Discussion](#discussion)powered by zap.ms

[### Message ID

MC1479277

View in Message Center](https://admin.microsoft.com/#/MessageCenter/:/messages/MC1479277)

### Last Updated

Nov 9, 2026

Published Sep 25, 2026

[View version history](#version-history)

### Service

Microsoft Copilot (Microsoft 365)

### Tag

Updated message

New feature

User impact

Admin impact

[### Roadmap ID

501451

View roadmap details](/message/RM501451)

### Platforms

Web

### More information

Updated November 9, 2026: We update the Copilot app UI updates section with new details. Thank you for your patience.

**What and why:**

We are evolving Microsoft Copilot to better connect the tools people rely on with the capablities they need to build, customize, and scale AI across work. Updates include a new Home experience and enhanced Office capabilities in the Copilot app; Code and Autopilot for building solutions and automating work; an enterprise-grade platform for running code; and updates to Copilot Notebooks, Copilot in SharePoint and OneDrive, and Work IQ.

**Impact on your organization:**

**Home in the Copilot app:**

- When users open the Copilot app, they will land in Home, which brings Chat and Cowork together on one screen. Users can switch between Chat and Cowork in the prompt box. Read more in the [blog](https://aka.ms/AA13g7uq). These updates will roll out to Frontier in October for all Microsoft 365 users with access to the Copilot app.
- As part of this update, we are making the following updates to the left navigation pane: 1) Agents & Plugins will replace the standalone Agents entry point (called Agents & Skills for some preview users) from Chat and the Customize entry point from Cowork. 2) For users with access to Cowork, Automations from Cowork will move to the Home navigation pane. These updates will roll out to Frontier in October for all Microsoft 365 users with access to the Copilot app.
- Researcher and Analyst will no longer be pinned by default in the Copilot app navigation pane. Users can continue to access these agents from Plugins and can pin them to the navigation pane based on their preferences. Organizations that want these agents to remain pinned for their users can [pre-pin them through the Microsoft 365 admin center](https://learn.microsoft.com/microsoft-365/admin/manage/agent-registry?view=o365-worldwide#manage-pinned-agents).
- Chat can complete long-running, multi-step knowledge work, including drafting email, managing meetings, working in Teams, managing OneDrive and SharePoint files, finding people, and creating Word, PowerPoint, Excel, PDF, and HTML files. Sensitive actions require user approval. Users can track and manage their long-running activity from Chat in the Tasks view, accessible in the upper right of the Copilot app navigation pane. These capabilities will roll out to Frontier later this month and are available to users with a Microsoft 365 Copilot license.
- Chat will begin surfacing Skills that are used while generating responses, giving users greater transparency into how Copilot responds. This update will begin worldwide rollout in October and is available to users with a Microsoft 365 Copilot license.

**Code:**

- The new Code experience gives users a dedicated place in the Copilot app to create trackers, dashboards, and apps using natural language. Users can access Code by going to the Code tab in the Copilot app navigation pane. Read more in the [blog](https://aka.ms/AA13g7uq).
- Code uses usage-based billing. Eligible users require a Microsoft 365 Copilot license and spending policy.
- Code is rolling out to Frontier later this month.
- To prepare: To enable Copilot Code for your tenant, admin must [deploy the unified app](https://learn.microsoft.com/windows/client-management/deploy-unified-copilot-app) and [set the target channel to beta](https://learn.microsoft.com/windows/client-management/copilot-update-policy-control#targetchannel-copilot).

**Autopilot:**

- Autopilot, previously called Scout, is an always-on personal agent in the Copilot app with persistent context, identity, and memory. Users can access Autopilot by going to the Autopilot tab in the Copilot app navigation pane. Read more in the [blog](https://aka.ms/AA13g7uq).
- Autopilot uses usage-based billing. Eligible users require a Microsoft 365 Copilot license and spending policy.
- We will update this message with rollout timing and admin control details when available.

**Copilot app UI updates:** Please refer to [MC1546354](https://admin.cloud.microsoft/?#/MessageCenter/:/messages/MC1546354) for more detail.

**Full Office capabilities in the Copilot app:**

- Users can use full Word, Excel, and PowerPoint creation, editing, and collaboration capabilities in the Copilot app, side by side with Copilot. Users can also access recent Word, Excel, and PowerPoint files from Library in the Copilot app navigation pane. Read more in the [blog](https://aka.ms/AA13g7uq).
- Capabilities accessed through Chat are included with the Microsoft 365 Copilot user subscription license. Capabilities accessed through Cowork use usage-based billing.
- These capabilities are rolling out to Frontier later this month.

**Copilot Managed Runtime:**

- Copilot Managed Runtime is an enterprise-grade platform for running code within the Microsoft 365 tenant boundary under IT governance. It supports apps built in Code, Cowork, Copilot Studio, and supported command-line and SDK experiences. Admins can manage these apps in the Microsoft 365 admin center. Read more in the [blog](https://aka.ms/CopilotManagedRuntime-Blog).
- Managed Runtime is starting to roll out now into public preview.

**Copilot Notebooks updates:**

- Copilot Notebooks will add task delegation, full Office editing and collaboration, interactive report creation, audio overview updates, model selection, and an updated user experience in the Copilot app and OneNote.
- These updates will roll out to Frontier later this month.

**SharePoint and OneDrive updates:**

- We are announcing the general availability of Copilot in SharePoint. The everyday AI capabilities that have been in public preview stay included with a Microsoft 365 Copilot user subscription license (USL). New agentic capabilities and the ability to work at greater scale than was possible in preview will be available through usage-based billing (UBB) and consume Copilot Credits. We are also introducing general availability of Copilot in OneDrive, which follows the same licensing structure as SharePoint. Read more about Copilot in SharePoint and OneDrive in the [blog](https://aka.ms/CopilotinSP/blog/GA).
- General availability begins rolling out later this month. Tenant availability may follow as rollout progresses.
- To prepare: No action is required to continue using capabilities included with the Microsoft 365 Copilot user subscription license (USL). Admins can control who can access advanced SharePoint capabilities through UBB by going to Microsoft 365 admin center > Copilot > Cost Management. Existing cost management policies may automatically include newly available services. Existing PowerShell opt-out settings for the Public Preview of Copilot in SharePoint will continue to be honored until November 1st; after that, manage availability through SharePoint site AI settings.

**Business Applications in Work IQ:**

- Work IQ now includes Dynamics 365 Sales, Dynamics 365 Customer Service, and Power Platform data, enabling Copilot to ground responses and tasks on business and productivity data. Read more in the [blog](https://aka.ms/BizAppsInWorkIQ/Blog).
- These updates will start rolling out in public preview later this month.
- To prepare: Admins can configure Dynamics 365 and Power Platform data sources for Copilot in the Power Platform admin center. Admins can also manage the availability of business applications in Copilot in the Microsoft 365 admin center under Copilot > Settings, and access through the Work IQ Model Context Protocol (MCP) under Agents > Tools.

**Action required / Recommendations:**

In addition to the guidance listed in the individual updates above:

- A spending policy is required for users to access capabilities available through Usage-based billing. Enable Copilot Credit consumption and configure spending policies in the Microsoft 365 admin center under Copilot > Cost management. Educate users about usage-based billing scenarios and how to request access through IT. Learn more about spending policy and usage-based billing in the [blog](https://aka.ms/Sept25/EvolvingModel) and message center post titled: **Evolving Copilot pricing and new FinOps capabilities for AI**.
- Monitor this post for updated availability and deployment details.
