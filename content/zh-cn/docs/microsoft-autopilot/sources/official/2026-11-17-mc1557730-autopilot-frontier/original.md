来源：https://mc.merill.net/message/MC1557730
取文：2026-11-28，直接下载（第三方存档站 mc.merill.net；消息中心原文需管理员登录）

MC1557730 - Autopilot availability in Frontier

Message Center

### Summary

Autopilot will roll out in Frontier Public starting November 17, 2026, as an always-on cloud agent requiring admin enablement and Microsoft 365 Copilot licensing. It features its own identity, security controls, and compliance considerations. Admins must configure access and billing; users create Autopilots via Copilot Home.

[Discussion](#discussion)powered by zap.ms

[### Message ID

MC1557730

View in Message Center](https://admin.microsoft.com/#/MessageCenter/:/messages/MC1557730)

### Published

Nov 17, 2026

### Service

Microsoft Copilot (Microsoft 365)

### Tag

New feature

User impact

Admin impact

### More information

**What and why:**

Autopilot will begin a phased roll out within Frontier Public on November 17, 2026. We will give Admins 24 hours notice prior to enabling Autopilot in a tenant.

Autopilot is an always-on, cloud-based personal agent that takes work off your plate and keeps delegated goals moving over time, rather than working one prompt at a time.

Autopilot has its own account and identity, storage and mailbox, and its own remote computer. Access controls, approval guardrails and supported information-protection and compliance capabilities help keep delegated work within approved boundaries.

**Rollout schedule:**

- Frontier Public roll out begins November 17, 2026.
- Autopilot rolls out in phases to eligible customers.
- General availability timing will be confirmed separately.

**Impact on your organization:**

**Who is affected**

- Organizations enrolled in Frontier
- Microsoft 365 admins
- End users who meet licensing and admin configured prerequisites

**Platforms / Services**

- Microsoft 365
- Microsoft Copilot

**What will happen**

- Autopilot becomes available to tenants enrolled in Frontier on a rolling basis
- Autopilot is OFF by default and not available unless admins complete required enablement steps
- Users are unable to create an Autopilot unless all admin prerequisites are met

**Action required / Recommendations:**

**Pre-requisites**

The person responsible for the Autopilot (i.e., the accountable user to whom the agent is assigned) is required to have a Microsoft 365 Copilot license and consumption billing enabled. Availability is initially limited to eligible US customers.

 In addition, the following controls are required:

- **Identity platform:** Microsoft Entra Agent ID. Provisioned automatically.
- **Isolated runtime environment:** Microsoft local (MXC)
- **Immutable audit logs and cost management:** Microsoft 365 audit logs and Agent 365 cost management.

The following controls are highly recommended:

- **Access and authorization governance:** Microsoft Entra ID Governance (least-privileged access), Microsoft Entra Global Secure Access (tool, MCP, and data inspection), and Microsoft Entra Conditional Access.
- **Data security and insider risk:** Microsoft Purview Data Loss Prevention and Microsoft Purview Insider Risk Management.
- **Threat protection:** Microsoft Defender XDR and Dynamic Agent Risk.

For the most secure configuration, the following controls are also recommended:

- **Agentic security:** Microsoft Perception (limited preview), Microsoft Entra Conditional Access dynamic controls (limited preview), Microsoft Entra ID Governance dynamic permissions (limited preview)

This licensing and controls guidance applies to Frontier Public Preview. Additional requirements and security recommendations may apply at General Availability.

 How do I get these required and highly recommended capabilities from Microsoft?

1. **Required Microsoft Security capabilities:** Intune P1/ME3, Any Microsoft 365 commercial license
2. **Highly recommended Microsoft Security capabilities:** Entra Suite, Purview Suite/ME5, Defender Suite/ME5, Agent 365 paid license
3. **Most secure configuration:** User-based billing

**Admin actions (required)**

- Admin turns on access to Autopilots in MAC
- Admin sets up a Copilot Credits billing policy
- Admins enable Autopilot for a security group

**User actions**

- Navigate to the Autopilot in the left-hand panel of the Copilot Home experience and select 'Create Your Autopilot'
- Communicate with your Autopilot in Teams, the Copilot app or Outlook

**Recommendations**

- Review this change with security and compliance stakeholders before enabling

**Compliance considerations**

Autopilot is off by default. Administrators control access through the Microsoft 365 admin center and security-group assignments. Autopilot has its own identity; work performed on a user’s behalf uses that user’s permissions. Automated checks review consequential actions, but some actions can proceed without a separate confirmation.

 Before enabling this Frontier preview, review the Autopilot documentation with your security and compliance teams. Memory is always on in this release, and Microsoft 365 Copilot personalization settings do not apply. Data-protection and audit capabilities have preview limitations; Autopilot conversations are not yet covered by eDiscovery, retention, or legal hold.
