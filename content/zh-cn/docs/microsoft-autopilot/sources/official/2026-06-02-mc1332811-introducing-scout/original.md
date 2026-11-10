来源：https://mc.merill.net/message/MC1332811
取文：2026-11-10，直接下载（第三方存档站 mc.merill.net；消息中心原文需管理员登录）

MC1332811 - Microsoft 365 Copilot: Introducing Microsoft Scout, an always-on personal agent

Message Center

This announcement expired on **Oct 30, 2026** and is no longer active in Message Center.

### Summary

Microsoft Scout is an always-on personal Autopilot agent integrated across Microsoft 365 apps, acting autonomously within organizational policies. Available now in Frontier preview on Windows and macOS, it requires admin enablement, Intune policy configuration, and GitHub Copilot licensing. It respects security and compliance guardrails.

[Discussion](#discussion)powered by zap.ms

[### Message ID

MC1332811

View in Message Center](https://admin.microsoft.com/#/MessageCenter/:/messages/MC1332811)

### Last Updated

Aug 21, 2026

Published Jun 2, 2026

### Service

Microsoft Copilot (Microsoft 365)

### Tag

New feature

User impact

Admin impact

### More information

****What and Why****

We are introducing a new category of agents called Autopilots—always-on agents that work autonomously, with their own identity, and act on your behalf within the permissions and policies you set. **Microsoft Scout** is our first Autopilot. Integrated across the Microsoft 365 apps your users rely on every day and powered by Work IQ, Microsoft Scout stays connected to user priorities, monitors what matters, and moves work forward across Teams, Outlook, OneDrive, and SharePoint—while respecting the security, identity, and governance guardrails defined by your organization.

Built on OpenClaw open-source technology and enterprise-grade controls, Microsoft Scout is available today through Frontier as an early desktop experience on Windows and macOS—the same experience Microsoft employees have been using—giving enrolled customers a chance to explore how Autopilots fit into their workflows.

Learn more at [Introducing Microsoft Scout: Your always-on personal agent | Microsoft 365 Blog](https://aka.ms/microsoftscout) and [Microsoft Scout (Frontier) documentation | Microsoft Learn](https://aka.ms/MicrosoftScout-Learn-docs)

****Rollout Schedule****

- **Frontier (Preview):** Available now for enrolled customers on Windows and macOS
- **General availability**: Broader rollout timing will be communicated at a later date

****Impact on Your Organization****

*Who is affected*

- Organizations enrolled in Frontier
- IT admins managing Intune, identity, and access controls
- Microsoft 365 admins
- End users who meet licensing and admin-configured prerequisites

*Platforms / Services*

- Microsoft 365
- Microsoft Scout desktop app (Windows, macOS)
- Microsoft Intune (policy configuration)
- GitHub Copilot (required for AI credit billing)

*What will happen*

- A Microsoft Scout desktop app will be available to tenants enrolled in *Frontier*.
- The feature is **OFF by default** and requires admin enablement.
- Users cannot sign in until all required admin prerequisites are completed.
- The Scout app runs locally on the user’s device and uses the user’s identity to operate.
- Access is gated by admin configuration, enrollment, and attestation.

****Action Required / Recommendations****

Admin actions (required)

- Configure required device and access policies in [Intune](https://intune.microsoft.com/#home).
- Complete the required admin opt-in and attestation (to be provided during setup) before enabling Microsoft Scout. This step is required due to data flows outside Microsoft 365.
- Ensure eligible users have appropriate [GitHub Copilot licensing](https://docs.github.com/billing/get-started/introduction-to-billing).

User actions

- Download and install the Microsoft Scout app (Frontier).
- Download Microsoft Scout: <https://aka.ms/msscout>
- Sign in with a work account (after admin enablement).
- Sign in with a GitHub account.

Recommendations

- Review this feature with security and compliance stakeholders before enabling.
- Inform helpdesk teams that sign-in failures typically indicate missing prerequisites.
- Share enablement guidance with pilot users to set expectations for the Frontier experience.

Learn more:

- [Introduction to billing and licensing | Get started | Billing and payments | GitHub Docs](https://docs.github.com/billing/get-started/introduction-to-billing)
- [Introducing Microsoft Scout: Your always-on personal agent | Microsoft 365 Blog](https://aka.ms/microsoftscout)
- [Microsoft Scout (Frontier) documentation | Microsoft Learn](https://learn.microsoft.com/microsoft-scout/)
- [Step 1: Set up Microsoft Intune | Microsoft Intune | Microsoft Learn](https://learn.microsoft.com/intune/fundamentals/deploy-setup-step-1)

****Compliance considerations****

|  |  |
| --- | --- |
| **Question** | **Answer** |
| Does the change store new customer data? If so, where, and is the data cached or permanently stored? | Yes. The preview experience includes data paths outside Microsoft 365 (for example, GitHub-based inference), which may involve additional handling of customer data and requires explicit admin attestation. |
| Does the change introduce or significantly modify AI or agent capabilities that interact with or provide access to customer data? | Yes. This change introduces a proactive, agentic experience that can act on behalf of users across content and tasks within defined organizational guardrails. |
| Does the change add any integration to third-party software products? | Yes. Microsoft Scout requires integration with GitHub Copilot for AI credit consumption and billing. |
| Does the change include an admin control, and can it be controlled through Entra ID group membership? | Yes. Access is gated through administrative controls, including Intune configuration, Frontier enrollment, and required admin opt-in and attestation. |
| Does the change allow a user to enable and disable the feature themselves? | Yes. Users can install the application, but they cannot successfully use it unless administrators complete the required enablement and attestation steps. |
