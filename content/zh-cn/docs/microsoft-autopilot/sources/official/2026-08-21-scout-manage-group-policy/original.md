来源：https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy
取文：2026-11-10，直接下载

Manage admin controls in Intune for Microsoft Scout

[This article is prerelease documentation and is subject to change.]

Important

- You need to be part of the **[Frontier preview program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** and sign up to accept terms of participation to get **early access** to Microsoft Scout. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
- This is a preview feature.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Microsoft Scout supports enterprise management through Windows Group Policy and Microsoft Intune by using Administrative Template (ADMX/ADML) files. These policies are device-scoped and are stored under `HKLM\SOFTWARE\Policies\Scout`. Because the policies are managed at the device level, standard users can't modify them.

## Available admin controls

Administrators can use these policies to manage Microsoft Scout features and capabilities, including:

- Requiring approval for tool actions
- Blocking specific tool servers
- Restricting permission types
- Disabling AI models or providers
- Disabling Heartbeat and Automations
- Limiting file system access to the workspace
- Blocking browser egress destinations
- Controlling Frontier access

## Policy reference

The following policy settings are available.

| Policy setting | Registry value | Type | Description |
| --- | --- | --- | --- |
| Policy version | `PolicyVersion` | `REG_DWORD` | Stores the policy schema version for diagnostics and future migrations. |
| Disabled tool servers | `DisabledServers` | `REG_SZ` | Comma-separated list of tool server keys to block, such as `filesystem`, `playwright`, or `WorkIQ`. |
| Disabled permission kinds | `DisabledPermissions` | `REG_SZ` | Comma-separated list of permission types to deny, such as `shell`, `write`, `mcp`, `url`, or `custom-tool`. |
| Force human approval for all non-read actions | `ForcePrompt` | `REG_DWORD` | Requires user approval for every non-read tool action, regardless of local approval settings. |
| Disabled AI models | `DisabledModels` | `REG_SZ` | Comma-separated list of model IDs to block. |
| Disabled AI model providers | `DisabledProviders` | `REG_SZ` | Comma-separated list of provider names to block, such as `anthropic` or `openai`. |
| Disable Heartbeat | `DisableHeartbeat` | `REG_DWORD` | Disables the Heartbeat monitoring feature. |
| Disable Automations | `DisableWorkflows` | `REG_DWORD` | Prevents users from creating or running automations. |
| Restrict file system access to workspace | `RestrictToWorkspace` | `REG_DWORD` | Limits file system and shell access to the current workspace directory. |
| Blocked browser egress origins | `BrowserEgressBlockedOrigins` | `REG_SZ` | Comma-separated list of HTTP or HTTPS origins that are blocked from browser automation traffic. |

## Related content

- [Admin access overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)
- [Set up Microsoft Scout with Intune](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)
- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Microsoft Scout common questions](https://learn.microsoft.com/en-us/microsoft-scout/faq)
