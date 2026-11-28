来源：https://learn.microsoft.com/en-us/copilot/autopilot/requirements
取文：2026-11-28，直接下载

Autopilot (Frontier) requirements

[This article is prerelease documentation and is subject to change.]

Important

- Access to Autopilot (Frontier) requires the applicable **[Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)** enrollment, preview assignment, and participation terms. Frontier enrollment alone doesn't enable every preview feature. Frontier previews are subject to the applicable preview terms of your customer agreements, and their availability and capabilities may change.
- This feature is in preview.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

This article describes prerequisites for Autopilot in Microsoft Copilot. You don't need a separately installed agent on your device. Autopilot is off by default. Frontier enrollment alone doesn't make Autopilot available; your administrator also licenses Autopilot, sets up a spending policy, and activates it.

## Account and licensing

The person responsible for the Autopilot, meaning the accountable user to whom the agent is assigned, must have a Microsoft 365 Copilot license and consumption billing turned on. Availability is initially limited to eligible customers in the United States.

| Requirement | Details |
| --- | --- |
| Microsoft 365 work or school account | An account associated with your organization. Personal Microsoft accounts aren't supported. |
| Microsoft 365 Copilot license | An active [Microsoft 365 Copilot license](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-licensing) assigned to the accountable user. |
| Preview access | Your organization must enroll you in Frontier and activate **Autopilot (Frontier)** for you or a group you belong to. Your administrator confirms the assignment. |
| Spending policy | Autopilot is billed on usage in Copilot Credits. Your organization must turn on usage-based billing, and you must be covered by a spending policy that includes Autopilot. If you aren't covered, or the policy reaches its limit, Autopilot doesn't work for you. A Copilot license doesn't include Autopilot usage. Learn more in [Review usage and limits](https://learn.microsoft.com/en-us/copilot/autopilot/using#review-usage-and-limits). |

Each enabled user can create one Autopilot.

## Security requirements and recommendations

Your organization must have the required Microsoft Security capabilities in place before users work with Autopilot. Additional capabilities are highly recommended, and the most secure configuration adds controls that are in limited preview. This licensing and controls guidance applies to the Frontier public preview. Additional requirements and security recommendations might apply at general availability.

### Required security capabilities

The following capabilities are required for Autopilot.

| Capability | Microsoft solution | Licensing |
| --- | --- | --- |
| Identity platform | Microsoft Entra Agent ID | Provisioned automatically. |
| Isolated execution environment | Microsoft local (MXC) | Microsoft Intune Plan 1 or Microsoft 365 E3 |
| Immutable audit logs and cost management | Microsoft 365 audit logs | Any Microsoft 365 commercial license |

### Highly recommended security capabilities

Microsoft highly recommends the following capabilities to govern access, protect data, and detect threats.

| Capability | Microsoft solution | Licensing |
| --- | --- | --- |
| Access and authorization governance | Microsoft Entra ID Governance for least-privileged access, Microsoft Entra Global Secure Access for tool and data inspection, and Microsoft Entra Conditional Access | Microsoft Entra Suite |
| Data security and insider risk | Microsoft Purview Data Loss Prevention and Microsoft Purview Insider Risk Management | Microsoft Purview Suite or Microsoft 365 E5 |
| Threat protection | Microsoft Defender XDR | Microsoft Defender Suite or Microsoft 365 E5 |

### Most secure configuration

For the most secure configuration, add the following agentic security capabilities. These capabilities are in limited preview.

- Microsoft Perception
- Microsoft Entra Conditional Access dynamic controls
- Microsoft Entra ID Governance dynamic permissions

## Access

| Requirement | Details |
| --- | --- |
| Microsoft Copilot | Sign in at [copilot.cloud.microsoft](https://copilot.cloud.microsoft) on the web or in the Microsoft Copilot desktop app with your organizational account. Autopilot appears on the **Home** tab in the left navigation. |
| Microsoft Teams | After setup, Autopilot can reach you in a private one-on-one chat in Teams for updates, questions, and approvals. |
| Mobile apps | On iOS and Android, you can work with Autopilot through the Microsoft 365 Copilot, Microsoft Teams, and Microsoft Outlook apps. Sign in with your work account. |
| Feature and provider access | Required agent and AI-provider settings must permit the experience. Frontier doesn't override these controls. Learn more in [Configure Autopilot for your organization](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure). |
| Task-specific access | The acting account needs permission for the mail, calendar, conversation, files, tools, and destinations used by the task. Skills and routines don't grant access. |
| Microsoft Edge (optional) | To let Autopilot work in your browser, where enabled, Microsoft Edge must be open on your device, signed in with your work account, and connected to Autopilot. See [Work in your Microsoft Edge browser](https://learn.microsoft.com/en-us/copilot/autopilot/edge). |

Autopilot's cloud computer is separate from your local device, and Autopilot can't access your local folders or apps. Don't treat instructions for an earlier desktop preview as setup requirements in the cloud experience.

## Availability

Availability is initially limited to select eligible Frontier customers in the United States, with new Frontier tenants rolling out over time. Supported languages, access methods, and individual features can vary by preview assignment. Autopilot is optimized for English. A localized interface doesn't establish that every language or workflow has been evaluated. Confirm your organization's supported configuration before relying on it.

Background work depends on authorized access and available services. A pending approval, missing permission, or service issue can block a scheduled run. There is no guarantee of uninterrupted execution or completion at a specific time.

For current capability guidance, see the [Autopilot overview](https://learn.microsoft.com/en-us/copilot/autopilot/overview) and [Application card](https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card).

## Related content

- [Get started with Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)
- [Configure Autopilot for your organization](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure)
- [Autopilot overview](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [Autopilot common questions](https://learn.microsoft.com/en-us/copilot/autopilot/faq)

---
