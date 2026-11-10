来源：https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview
取文：2026-11-10，直接下载

Admin access overview for Microsoft Scout

[This article is prerelease documentation and is subject to change.]

Important

- You need to be part of the **[Frontier preview program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** and sign up to accept terms of participation to get **early access** to Microsoft Scout. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
- This is a preview feature.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

Microsoft Scout is available only in Microsoft Frontier, and access requires two separate gates that both must be completed. The first gate enables Frontier for your organization in the Microsoft 365 admin center. The second gate enables the app on user devices through an Intune policy and an admin attestation. A GitHub Copilot license alone doesn't grant Frontier access, and Frontier access alone doesn't work without a Copilot license (business or enterprise). Installing the app grants nothing on its own — sign-in only succeeds after both gates are complete.

## Access flow at a glance

The end-to-end path from an unconfigured tenant to a signed-in user looks like this:

1. Admin enrolls the organization in Frontier and turns on **Copilot Frontier** in the Microsoft 365 admin center.
2. Admin configures the Microsoft Scout Intune policy on target devices.
3. Admin completes the Frontier organization sign-up (attestation) form.
4. User downloads the Microsoft Scout app.
5. User installs the Microsoft Scout app.
6. User confirms they have a GitHub account.
7. User signs in. Sign-in only succeeds if the admin steps are complete.

## Admin gate 1: Frontier access

The first gate turns on Frontier — and therefore Microsoft Scout — for your tenant. You configure it in the Microsoft 365 admin center.

1. Sign in to the Microsoft 365 admin center.
2. In the left navigation, select **Copilot**, then **Settings**, then **View all**.
3. In the search box, enter `Frontier`, then select **Copilot Frontier**.
4. Set access for your organization. Choose one of:
   - **No access**
   - **All users**
   - **Specific users**
5. Select **Save**.

After you save, allow up to about three hours for the change to propagate before Frontier features become available to the selected users.

Note

Completing this gate makes Frontier available to the assigned users, but it doesn't enable Microsoft Scout sign-in on its own. You still need to complete gate 2.

## Admin gate 2: Admin enablement

The second gate has three required admin actions. All must be completed before users can sign in to Microsoft Scout.

### Enable access via an Intune policy

An IT admin must configure an Intune policy for Microsoft Scout that:

- Sets the required registry and device conditions.
- Enables login capability for the app.

Without this policy in place, users can't sign in to Microsoft Scout even if they install the app successfully.

For step-by-step instructions, see [Set up Microsoft Scout with Intune](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup).

### Complete the attestation and opt-in

Because Microsoft Scout can route data outside Microsoft 365 to third-party inference paths (for example, GitHub), admins must explicitly attest and opt in for their organization. This is an additional gating layer beyond Frontier enrollment, and it applies even if gate 1 is already complete.

Complete the [M365 Admin — Frontier organization sign-up form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRyKGkCGRU0tBnsDASQkbqxJUOUROWUI4SFc5MFI5TTZJSU5MWExFRDZDMC4u) to record your attestation.

### Provision GitHub Copilot licenses

Admins must ensure that users have GitHub Copilot licenses assigned. This step is only required if users aren't already licensed.

For more information, see:

- [Setting up GitHub Copilot for your organization](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-organization?versionId=enterprise-cloud%40latest&productId=billing&restPage=how-tos%2Cmanage-plan-and-licenses%2Cmanage-user-licenses)
- [Granting access to GitHub Copilot for members of your organization](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/grant-access)

## Troubleshoot GitHub Copilot access

Microsoft Scout uses the GitHub Copilot app. For a user to sign in and run a task, two GitHub-side conditions must both be true:

- The user has a GitHub Copilot **Business** or **Enterprise** seat assigned.
- Your organization or enterprise policy allows the GitHub Copilot app for that user.

An assigned seat by itself isn't sufficient. If the policy that governs the Copilot app is turned off, a licensed user is still blocked.

Important

A user can have an active, assigned Copilot Business or Enterprise seat and still be blocked if the GitHub Copilot app policy (or, for app versions before 1.1, the Copilot CLI policy) is disabled. Check the policy before concluding it's a licensing problem.

### Symptoms and fixes

Use the message the user sees in Microsoft Scout to identify the cause.

| What the user sees | Likely cause | Admin fix |
| --- | --- | --- |
| A message that GitHub Copilot access is required (for example, "GitHub Copilot access required" or "GitHub Copilot Business or Enterprise required"), or that the account "doesn't have a … license" | No Copilot Business or Enterprise seat is assigned, or the user signed in with a personal GitHub account that only has an individual plan | Assign a Business or Enterprise seat to the user, and have the user sign in with the GitHub account that carries that seat. |
| "You are not authorized to use this Copilot feature" (an HTTP 403), or the access message above even though a seat is assigned | The organization or enterprise policy for the GitHub Copilot app (or **Copilot in the CLI** for app versions before 1.1) is disabled for the user | Enable the policy at the enterprise and organization level. See [Enable the GitHub Copilot app policy](#enable-the-github-copilot-app-policy). |
| Sign-in is blocked before any GitHub prompt appears | A Microsoft Scout admin gate (Frontier access, or the Intune policy and attestation) isn't complete | Verify both admin gates. See [What happens if access isn't configured](#what-happens-if-access-isnt-configured). |

### Enable the GitHub Copilot app policy

Set the policy in your GitHub enterprise and organization. Enterprise settings override organization settings, so enable it at the enterprise level first.

1. In your enterprise settings on GitHub, open the Copilot policies (**AI controls** > **Policies** > **Copilot clients**).
2. Set the **GitHub Copilot app** policy to **Enabled** (or **Let organizations decide** if you delegate to organization admins). For app versions before 1.1, also set **Copilot in the CLI** to **Enabled**, because that policy governs the Copilot app until version 1.1.
3. In each affected organization's Copilot policies, confirm the same policies are enabled.
4. Allow a few minutes for the change to propagate. Then have the user fully quit Microsoft Scout (close the window and quit the tray or menu bar icon) and relaunch.

Note

As of July 27, 2026, the GitHub Copilot app has its own policy, separate from Copilot in the CLI, introduced in app version 1.1. For app versions before 1.1, the Copilot CLI policy continues to govern the app. If you see both policies, enable both. For details, see [Manage GitHub Copilot app access with a dedicated policy](https://github.blog/changelog/2026-07-27-manage-github-copilot-app-access-with-a-dedicated-policy/).

For more information, see:

- [Managing policies and features for GitHub Copilot in your enterprise](https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies)
- [Administering Copilot CLI for your enterprise](https://docs.github.com/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise)

## User requirements

After both admin gates are complete, end users still need to take a few steps before they can use Microsoft Scout.

- [Download and install the Microsoft Scout app](https://aka.ms/scout).
- **Have a GitHub account.** Microsoft Scout uses your GitHub account for token billing, so each user needs one before signing in.
- **Sign in with work credentials.** Sign-in only succeeds after both admin gates (Frontier access and Intune enablement plus attestation) are complete.

Important

If a user tries to sign in before the admin gates are complete, the sign-in attempt is blocked and the app doesn't show a clear in-product indication of why. Confirm with your admin that Frontier access, the Intune policy, and the attestation are all in place before troubleshooting on the client.

## What happens if access isn't configured

Installing the Microsoft Scout app always succeeds because the download isn't heavily gated. Sign-in is where access is enforced. If Frontier isn't turned on for the user, or the Intune policy and attestation aren't complete, sign-in fails and the user doesn't see a clear in-product indication of the cause.

Note

If users report sign-in problems, verify both admin gates before investigating further.

## Next steps

- [Set up Microsoft Scout with Intune](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)
- [Manage admin controls](https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy)

## Related content

- [Microsoft Scout overview](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Set up Microsoft Scout with Intune](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)
- [Microsoft Scout common questions](https://learn.microsoft.com/en-us/microsoft-scout/faq)
