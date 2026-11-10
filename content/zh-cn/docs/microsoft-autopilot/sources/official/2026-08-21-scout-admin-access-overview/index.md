---
title: "Microsoft Scout 管理员访问概述"
linkTitle: "文档：管理员访问概述"
date: 2026-08-21
originalTitle: "Admin access overview for Microsoft Scout"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [安全, 隐私, 运行环境]
products: [microsoft-autopilot]
updatedAt: "2026-08-21"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-08-21"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。已翻译。

**内容摘要**：Microsoft Scout 仅在 Microsoft Frontier 中提供，访问需要两道关口都完成。第一道在 Microsoft 365 admin center 的 Copilot Frontier 中设置 No access、All users 或 Specific users，保存后约需三小时生效；第二道包括 Intune 策略、Frontier 组织注册（attestation）表单，以及按需分配 GitHub Copilot 许可。由于数据可能经 GitHub 流向第三方推理路径，管理员必须明确声明并选择加入。用户登录要求 GitHub Copilot Business 或 Enterprise 席位，并且组织或企业策略允许 GitHub Copilot app；自 2026 年 7 月 27 日起该 app 有独立策略（app 1.1 版本引入）。文档还给出报错信息与对应的管理员处理方法。

**保留理由**：这是两道管理员关口、GitHub Copilot 策略前提以及数据可能流向 GitHub 的出处，用来解释用户为何无法登录。

---

Microsoft Scout 的管理员访问概述

[本文为预发布文档，内容可能变更。]

重要事项

- 你需要加入 **[Frontier 预览计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)** 并注册接受参与条款，才能获得 Microsoft Scout 的**早期访问**。Frontier 让你直接接触 Microsoft 最新的 AI 创新。Frontier 预览受客户协议中现有预览条款的约束。由于这些功能仍在开发中，其可用性和能力可能随时间变化。
- 这是一项预览功能。
- 预览功能的功能可能受限，且可能不会正式发布。这些功能在正式发布之前提供，以便客户提前访问并提供反馈。
- 更多信息，请参阅我们的 [Microsoft 产品条款](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA)。

Microsoft Scout 仅在 Microsoft Frontier 中提供，访问需要两道彼此独立的关口，且两者都必须完成。第一道关口在 Microsoft 365 admin center 中为你的组织启用 Frontier。第二道关口通过 Intune 策略和管理员声明（attestation）在用户设备上启用该应用。仅有 GitHub Copilot 许可证并不能获得 Frontier 访问权，而仅有 Frontier 访问权、没有 Copilot 许可证（Business 或 Enterprise）也无法使用。安装应用本身不会授予任何权限——只有在两道关口都完成后，登录才会成功。

## 访问流程一览

从未配置的租户到用户成功登录，端到端路径如下：

1. 管理员在 Microsoft 365 admin center 中为组织注册 Frontier，并开启 **Copilot Frontier**。
2. 管理员在目标设备上配置 Microsoft Scout Intune 策略。
3. 管理员完成 Frontier 组织注册（声明）表单。
4. 用户下载 Microsoft Scout 应用。
5. 用户安装 Microsoft Scout 应用。
6. 用户确认自己拥有 GitHub 账户。
7. 用户登录。只有在管理员步骤全部完成后，登录才会成功。

## 管理员关口 1：Frontier 访问

第一道关口为你的租户开启 Frontier——因而也开启 Microsoft Scout。你在 Microsoft 365 admin center 中配置它。

1. 登录 Microsoft 365 admin center。
2. 在左侧导航中依次选择 **Copilot**、**Settings**、**View all**。
3. 在搜索框中输入 `Frontier`，然后选择 **Copilot Frontier**。
4. 为你的组织设置访问权限。选择以下之一：
   - **No access**
   - **All users**
   - **Specific users**
5. 选择 **Save**。

保存后，请最多等待约三小时让更改传播，之后 Frontier 功能才会向所选用户提供。

注意

完成这道关口会让 Frontier 向已分配的用户提供，但它本身不会启用 Microsoft Scout 登录。你仍需要完成关口 2。

## 管理员关口 2：管理员启用

第二道关口有三项必需的管理员操作。在用户能够登录 Microsoft Scout 之前，所有操作都必须完成。

### 通过 Intune 策略启用访问

IT 管理员必须为 Microsoft Scout 配置一项 Intune 策略，用于：

- 设置所需的注册表和设备条件。
- 为应用启用登录能力。

如果没有这项策略，即使用户成功安装了应用，也无法登录 Microsoft Scout。

有关分步说明，请参阅 [使用 Intune 设置 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)。

### 完成声明与选择加入

由于 Microsoft Scout 可能将数据从 Microsoft 365 路由到第三方推理路径（例如 GitHub），管理员必须为其组织明确作出声明并选择加入。这是在 Frontier 注册之外的额外关口，即使关口 1 已完成，它也仍然适用。

填写 [M365 管理员——Frontier 组织注册表单](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRyKGkCGRU0tBnsDASQkbqxJUOUROWUI4SFc5MFI5TTZJSU5MWExFRDZDMC4u) 以记录你的声明。

### 预配 GitHub Copilot 许可证

管理员必须确保为用户分配了 GitHub Copilot 许可证。仅当用户尚未获得许可证时，才需要这一步。

更多信息，请参阅：

- [为你的组织设置 GitHub Copilot](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-organization?versionId=enterprise-cloud%40latest&productId=billing&restPage=how-tos%2Cmanage-plan-and-licenses%2Cmanage-user-licenses)
- [为组织成员授予 GitHub Copilot 访问权限](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/grant-access)

## 排查 GitHub Copilot 访问问题

Microsoft Scout 使用 GitHub Copilot 应用。用户要登录并运行任务，必须同时满足两个 GitHub 侧条件：

- 用户已被分配 GitHub Copilot **Business** 或 **Enterprise** 席位。
- 你的组织或企业策略允许该用户使用 GitHub Copilot 应用。

仅分配席位还不够。如果管控 Copilot 应用的策略处于关闭状态，已获许可的用户仍会被阻止。

重要事项

用户可以拥有一个活动且已分配的 Copilot Business 或 Enterprise 席位，但如果 GitHub Copilot 应用策略（对于 1.1 之前的应用版本，则是 Copilot CLI 策略）被禁用，仍可能被阻止。在得出结论认为是许可证问题之前，请检查策略。

### 症状与修复方法

使用用户在 Microsoft Scout 中看到的消息来判断原因。

| 用户看到的内容 | 可能原因 | 管理员修复 |
| --- | --- | --- |
| 一条提示需要 GitHub Copilot 访问权限的消息（例如「GitHub Copilot access required」或「GitHub Copilot Business or Enterprise required」），或提示账户「doesn't have a … license」 | 未分配 Copilot Business 或 Enterprise 席位，或者用户使用仅有个人计划的个人 GitHub 账户登录 | 为用户分配 Business 或 Enterprise 席位，并让用户使用带有该席位的 GitHub 账户登录。 |
| 「You are not authorized to use this Copilot feature」（HTTP 403），或者即使已分配席位仍出现上述访问提示 | 针对该用户的 GitHub Copilot 应用（或应用版本低于 1.1 时的 **Copilot in the CLI**）的组织或企业策略被禁用 | 在企业级和组织级启用该策略。请参阅 [启用 GitHub Copilot 应用策略](#enable-the-github-copilot-app-policy)。 |
| 在任何 GitHub 提示出现之前登录就被阻止 | Microsoft Scout 的管理员关口（Frontier 访问，或 Intune 策略与声明）未完成 | 核查两道管理员关口。请参阅 [如果未配置访问会发生什么](#what-happens-if-access-isnt-configured)。 |

### 启用 GitHub Copilot 应用策略

在 GitHub 企业和组织中设置策略。企业设置会覆盖组织设置，因此请先在企业级启用。

1. 在 GitHub 的企业设置中，打开 Copilot 策略（**AI controls** > **Policies** > **Copilot clients**）。
2. 将 **GitHub Copilot app** 策略设为 **Enabled**（如果你将权限下放给组织管理员，则设为 **Let organizations decide**）。对于 1.1 之前的应用版本，还需将 **Copilot in the CLI** 设为 **Enabled**，因为在 1.1 版本之前由该策略管控 Copilot 应用。
3. 在每个受影响组织的 Copilot 策略中，确认已启用相同的策略。
4. 等待几分钟让更改传播。然后让用户完全退出 Microsoft Scout（关闭窗口，并退出托盘或菜单栏图标）再重新启动。

注意

截至 2026 年 7 月 27 日，GitHub Copilot 应用在 1.1 版本中引入了独立于 Copilot in the CLI 的自有策略。对于 1.1 之前的应用版本，Copilot CLI 策略继续管控该应用。如果你同时看到这两项策略，请将两者都启用。详情请参阅 [使用专用策略管理 GitHub Copilot 应用访问](https://github.blog/changelog/2026-07-27-manage-github-copilot-app-access-with-a-dedicated-policy/)。

更多信息，请参阅：

- [在你的企业中管理 GitHub Copilot 的策略和功能](https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies)
- [为你的企业管理 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise)

## 用户要求

两道管理员关口都完成后，最终用户仍需采取几个步骤才能使用 Microsoft Scout。

- [下载并安装 Microsoft Scout 应用](https://aka.ms/scout)。
- **拥有 GitHub 账户。** Microsoft Scout 使用你的 GitHub 账户进行令牌计费，因此每位用户在登录前都需要一个账户。
- **使用工作凭据登录。** 只有在两道管理员关口（Frontier 访问，以及 Intune 启用加声明）都完成后，登录才会成功。

重要事项

如果用户在管理员关口完成之前尝试登录，登录会被阻止，并且应用不会在产品内明确提示原因。在客户端排查之前，请向管理员确认 Frontier 访问、Intune 策略和声明都已就位。

## 如果未配置访问会发生什么

安装 Microsoft Scout 应用总是会成功，因为下载没有受到严格限制。访问是在登录时强制执行的。如果没有为用户开启 Frontier，或者 Intune 策略和声明未完成，登录就会失败，用户不会在产品内看到明确的原因提示。

注意

如果用户报告登录问题，请先核查两道管理员关口，再进一步调查。

## 后续步骤

- [使用 Intune 设置 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)
- [管理管理员控制项](https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy)

## 相关内容

- [Microsoft Scout 概述](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [开始使用 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [使用 Intune 设置 Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)
- [Microsoft Scout 常见问题](https://learn.microsoft.com/en-us/microsoft-scout/faq)
