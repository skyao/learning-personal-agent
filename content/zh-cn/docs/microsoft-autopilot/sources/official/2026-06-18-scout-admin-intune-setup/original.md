来源：https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup
取文：2026-11-10，直接下载

Set up Microsoft Scout with Intune

[This article is prerelease documentation and is subject to change.]

Important

- You need to be part of the **[Frontier preview program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** and sign up to accept terms of participation to get **early access** to Microsoft Scout. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
- This is a preview feature.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

This guide is for Frontier customer Intune administrators who need to enable Microsoft Scout for managed users. The most important setting is the Frontier access capability, which appears in the Windows ADMX policy UI as **Allow Microsoft Scout Frontier access** and corresponds to the `AllowScoutFrontierAccess` capability. For background on how Frontier access fits with other admin gates, see [Admin access overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview).

Note

Some pre-release Intune policy templates and screenshots still show the internal product name **Clawpilot**.

## Prerequisites

Before you begin, make sure you have:

- A Microsoft 365 work or school account associated with your organization. Personal Microsoft accounts are not supported.
- Intune tenant administrator credentials.
- Access to the Microsoft Intune admin center at <https://intune.microsoft.com>.
- The latest [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist) (Windows only).
- The Microsoft Scout Windows policy template files:
  - `microsoft-scout.admx`
  - `microsoft-scout.adml`
- The Microsoft Scout macOS configuration profile file:
  - `microsoft-scout.mobileconfig`

You can [download these template and profile files from GitHub](https://github.com/microsoft/scout-resources/tree/main/admins).

## Overview

To enable Microsoft Scout Frontier access for users, configure the following in Intune:

- Import the Microsoft Scout Windows ADMX/ADML templates.
- Create a Windows configuration policy from the imported administrative template.
- Enable **Allow Microsoft Scout Frontier access**.
- Assign the Windows policy to the target managed devices.
- Create and assign the macOS custom configuration profile.

## Part 1: Import the Microsoft Scout ADMX template

This part imports the Microsoft Scout administrative template files so they're available when you create a Windows configuration policy.

### Open the Microsoft Intune admin center

Go to <https://intune.microsoft.com> and sign in with tenant administrator credentials. Confirm that the Microsoft Intune admin center loads for the correct tenant.

![Screenshot of the Microsoft Intune admin center home page after sign-in.](images/img-01-9fc7cf.png)

### Open Devices configuration and Import ADMX

In the left navigation, select **Devices**. Under **Manage devices**, select **Configuration**, then open the **Import ADMX** tab.

![Screenshot of the Import ADMX tab on the Devices Configuration page in Intune.](images/img-02-8bb958.png)

### Start the ADMX import

Select **Import**, then use the file picker icons to upload both Microsoft Scout template files:

- **ADMX file**: `microsoft-scout.admx`
- **ADML file**: `microsoft-scout.adml`

After both files are selected, select **Next**.

![Screenshot of the Intune Import ADMX page with the microsoft-scout ADMX and ADML files selected for upload.](images/img-03-f7d38f.png)

### Review and create the imported template

On **Review + create**, confirm that both template files are listed correctly, then select **Create**.

![Screenshot of the Review and create page for the imported Microsoft Scout ADMX template.](images/img-04-fc4c80.png)

### Wait for the upload to finish

Wait while Intune uploads and processes the Microsoft Scout ADMX template. Don't continue until the import status completes.

![Screenshot of the Microsoft Scout ADMX upload showing an in-progress status in Intune.](images/img-05-b1b3b9.png)

### Confirm the template is available

After the upload completes, confirm that the Microsoft Scout template status is **Available**. You can now use the imported administrative template to create a Windows configuration policy.

![Screenshot of the imported Microsoft Scout ADMX template listed with an Available status in Intune.](images/img-06-74c0aa.png)

## Part 2: Create the Windows Microsoft Scout policy

This part creates a Windows configuration policy that enables Frontier access for assigned devices.

### Create a new configuration policy

Return to **Devices**, then **Configuration**. Open the **Policies** tab, and select **New policy**.

![Screenshot of the Intune Configuration Policies tab with the New policy command highlighted.](images/img-07-efab97.png)

### Select the Windows template profile type

For the new profile, choose:

- **Platform**: Windows 10 and later
- **Profile type**: Templates

![Screenshot of the Create a profile pane with Windows 10 and later platform and Templates profile type selected.](images/img-08-d614d7.png)

### Choose Imported Administrative Templates

In the template list, select **Imported Administrative Templates**. This uses the Microsoft Scout ADMX template imported in the previous section.

![Screenshot of the Imported Administrative Templates option selected in the Intune template list.](images/img-09-6d249b.png)

Then select **Create**.

### Name the Windows policy

Enter a clear policy name, such as **Microsoft Scout - Frontier access**. Optionally, add a description that explains the policy enables Microsoft Scout Frontier access for assigned devices. Select **Next**.

![Screenshot of the Basics page for the Windows policy with the name Microsoft Scout - Frontier access entered.](images/img-10-0c13a3.png)

### Select Microsoft Scout configuration

In **Configuration settings**, select the imported Microsoft Scout configuration template.

![Screenshot of the Configuration settings page with the imported Microsoft Scout configuration template selected.](images/img-11-ad3e25.png)

### Choose the Microsoft Scout policy version

Select the Microsoft Scout policy version from the imported administrative template options, then continue to the available settings.

![Screenshot of the Microsoft Scout policy version selection in the imported administrative template.](images/img-12-082951.png)

### Open the Frontier access setting

Under **Microsoft Scout**, then **Capabilities**, open the setting named **Allow Microsoft Scout Frontier access**.

### Enable Frontier access

Set **Allow Microsoft Scout Frontier access** to **Enabled**, then select **OK**.

Important

This is the key Windows policy setting for Frontier access. It enables the `AllowScoutFrontierAccess` capability on devices that receive this policy. When enabled, users in the tenant can sign in and use Microsoft Scout Frontier builds normally. If the setting is disabled or not configured, Frontier users might see a waitlist screen and be blocked from sign-in.

### Continue through scope tags

On **Scope tags**, keep the default scope tags unless your organization requires a specific Intune RBAC scope tag, then select **Next**.

![Screenshot of the Scope tags page showing the default scope tag for the Windows policy.](images/img-13-9277dd.png)

### Configure assignments

On **Assignments**, choose the groups or devices that should receive the Microsoft Scout Windows policy.

![Screenshot of the Assignments page for the Microsoft Scout Windows policy.](images/img-14-ae648e.png)

### Assign to all devices, if appropriate

For broad Frontier tenant rollout, assign the policy to **All devices**. If you're piloting Microsoft Scout with a smaller device population, assign only the intended pilot group instead.

![Screenshot of the assignment page with All devices selected for the Microsoft Scout Windows policy.](images/img-15-f87dc1.png)

### Review and create the Windows policy

Review the Windows configuration policy summary. Confirm that the policy includes the enabled Frontier access setting, then select **Create**.

![Screenshot of the Review and create summary for the Microsoft Scout Windows policy.](images/img-16-98f016.png)

### Confirm the Windows policy was created

After creation, confirm that the Windows policy appears in the configuration policy list.

![Screenshot of the Intune configuration policy list showing the newly created Microsoft Scout Windows policy.](images/img-17-eb5be6.png)

## Part 3: Create the macOS Microsoft Scout policy

This part creates a macOS custom configuration profile that delivers the same tenant settings to managed Macs.

### Create a policy for macOS

Return to **Devices**, then **Configuration**. Select **New policy** and begin creating a macOS policy.

![Screenshot of the New policy pane for creating a macOS configuration policy.](images/img-18-34ad36.png)

### Select the macOS custom profile type

Choose:

- **Platform**: macOS
- **Profile type**: Templates
- **Template name**: Custom

Then select **Create**.

![Screenshot of the macOS Templates options with the Custom template selected.](images/img-19-44dafc.png)

### Name the macOS profile

Enter a clear profile name, such as **Microsoft Scout - macOS Frontier access**. Optionally, add a description that explains the profile configures Microsoft Scout tenant policy for managed Macs. Select **Next**.

![Screenshot of the Basics page for the macOS profile with the name Microsoft Scout - macOS Frontier access entered.](images/img-20-475373.png)

### Upload the Microsoft Scout mobileconfig profile

On **Configuration settings**, upload `microsoft-scout.mobileconfig` and use these values:

| Setting | Value |
| --- | --- |
| Custom configuration profile name | `macOS` |
| Deployment channel | Device channel |
| Configuration profile file | `microsoft-scout.mobileconfig` |

After the file is uploaded and the profile contents appear, select **Next**.

![Screenshot of the Configuration settings page for the macOS custom profile with microsoft-scout.mobileconfig uploaded.](images/img-21-f34397.png)

### Configure macOS assignments

On **Assignments**, choose the devices or groups that should receive the Microsoft Scout macOS configuration profile.

![Screenshot of the Assignments page for the Microsoft Scout macOS configuration profile.](images/img-22-20c436.png)

### Assign to all devices, if appropriate

For broad Frontier tenant rollout, assign the macOS profile to **All devices**. For a pilot rollout, assign only the intended macOS pilot group.

![Screenshot of the assignment page with All devices selected for the Microsoft Scout macOS profile.](images/img-23-1b53bf.png)

### Review and create the macOS policy

Review the macOS custom profile summary, confirm that the uploaded `microsoft-scout.mobileconfig` file is listed, then select **Create**.

![Screenshot of the Review and create summary for the Microsoft Scout macOS custom profile.](images/img-24-400fc0.png)

### Confirm the macOS policy was created

After creation, confirm that the macOS profile appears in the configuration policy list.

![Screenshot of the Intune configuration policy list showing the newly created Microsoft Scout macOS profile.](images/img-25-90f502.png)

## Validate the deployment

After the Windows and macOS policies are created and assigned:

- Confirm the Windows policy shows the `AllowScoutFrontierAccess` capability as enabled through the **Allow Microsoft Scout Frontier access** setting.
- Confirm that assigned devices are included in the target groups.
- Allow Intune policy sync to complete on target devices.
- On a managed Frontier device, open Microsoft Scout and verify that the user can sign in without seeing the waitlist screen.

## Troubleshoot

| Symptom | What to check |
| --- | --- |
| The Microsoft Scout Windows settings don't appear. | Confirm that `microsoft-scout.admx` and `microsoft-scout.adml` were imported successfully and show **Available**. |
| Users still see a waitlist screen. | Confirm that **Allow Microsoft Scout Frontier access** is set to **Enabled**, the policy is assigned to the device, and the device has synced with Intune. |
| macOS devices don't receive the setting. | Confirm that `microsoft-scout.mobileconfig` was uploaded to a macOS **Custom** profile using the **Device channel** and assigned to the target devices. |
| Policy applies to the wrong audience. | Review the assignment groups for both the Windows and macOS profiles. |

## Related content

- [Admin access overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)
- [Manage admin controls](https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy)
- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Microsoft Scout overview](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [Microsoft Scout common questions](https://learn.microsoft.com/en-us/microsoft-scout/faq)
