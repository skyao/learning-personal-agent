---
title: "文档：配置身份与访问"
linkTitle: "文档：身份与访问"
date: 2026-11-05
originalTitle: "Configure identity and access"
sourceUrl: "https://cursor.com/docs/grok-bot/identity"
altUrls: ["https://docs.x.ai/grok-bot/identity-and-access"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：面向使用 Okta 或 Microsoft Entra ID 的管理员。Grok Bot 使用 Cursor 账号，因此没有独立的 Okta 或 Entra 应用，需要把现有 Cursor 应用分配给工程以外的用户组，才能让他们访问；SCIM 仅限 Enterprise。另一项改动是在身份提供方里为 Bot 的计算机浏览器会话增加认证规则，因为这台 Linux 计算机不运行 Okta FastPass 等设备信任代理，也未纳入 MDM。这条规则只影响 Bot 在计算机浏览器里打开的、由身份提供方发放的应用，不影响 Grok Bot 登录或连接应用的登录。撤销用户在身份提供方的权限会终止其计算机内的应用会话，管理员也可随时终止成员的计算机。

**保留理由**：说明托管计算机在企业身份体系里的位置：登录走 Cursor SSO，而计算机内的登录不满足设备信任，因此要单独放行，对理解其与企业身份的关系有用。

---

本指南面向使用 Okta 或 Microsoft Entra ID 的管理员。它涵盖如何通过你的 Cursor 团队，让工程组织之外的人员访问 Grok Bot，以及让成员从 Bot 的计算机登录由身份提供方（IdP）发放的应用。有关更广泛的安全模型，见 [Grok Bot 安全](https://cursor.com/docs/grok-bot/security)。

Grok Bot 使用你的 Cursor 账户，因此 Okta 或 Entra ID 中没有单独的 Grok Bot 应用。本指南中的所有操作都在你已有的 Cursor 应用上进行。Cursor 单点登录（SSO）是 SAML 2.0，可与 Okta、Microsoft Entra、Google Workspace 和 OneLogin 配合使用；本指南详细说明最常需要关注设备信任（device trust）策略的两个。

## 你将更改什么

你将做两项更改，它们的作用不同：

- **分配 Cursor 应用**，让工程组织之外的用户可以通过你的 Cursor 团队访问 Grok Bot。
- **添加一条身份验证规则**，让用户可以从 Bot 的计算机登录由 IdP 发放的应用，该计算机运行 Linux，不运行设备信任代理。

只有第一项更改控制 Grok Bot 登录。第二项绝不会阻止 Grok Bot 登录，也不适用于已连接应用的登录，因为连接应用不经过这台计算机。

## 开始之前

访问 Grok Bot 要求用户是你的 Cursor 团队成员。成员使用其 Cursor 账户登录，因此你现有的 [Cursor SSO](https://cursor.com/docs/account/teams/sso) 适用。开启自动配置（auto-provisioning）后，用户首次登录时加入团队；否则，先配置用户，再让其登录 Cursor 以获取席位，或从 [Cursor 仪表盘](https://cursor.com/dashboard) 邀请他们。

**SCIM 仅限 Enterprise。** 如果你使用 [SCIM](https://cursor.com/docs/account/teams/scim)，配置协议为 SCIM 2.0，取消配置是自动的：在身份提供方中移除用户，就会将其从 Cursor 中移除。

## 分配 Cursor 应用

用户只有拥有 Cursor 账户才能登录，而他们通过被分配到现有的 Cursor SSO 应用（如果你使用 SCIM，还包括 SCIM 应用）来获得账户。如果 Cursor 只分配给工程部门，其他所有人都会遇到 **User is not assigned to this application**，或者其邀请永远无法完成。不要创建第二个 Grok Bot 应用；扩大你已有 Cursor 应用的分配范围。

1. 前往 **Admin Console** > **Applications** > **Applications**，打开你现有的 Cursor 应用。
2. 打开 **Assignments**，选择 **Assign** > **Assign to Groups**。若要改为分配个人，选择 **Assign to People**。
3. 添加所有应获得 Grok Bot 的组，而不只是工程部门。
4. 如果你使用 SCIM，将相同的组分配到 Cursor SCIM 应用并推送。用户只有在被分配到 SCIM 应用后才会出现在 Cursor 中。
5. 确认每个组也被分配到 SAML 应用。只有 SCIM 分配而没有 SSO 分配，仍会阻止首次登录。

如果你在 Cursor 中使用组织级身份，请在目录组同步后将其映射到 Grok Bot 团队；见[组织](https://cursor.com/docs/enterprise/organizations)。应用分配和 Group Push 请使用不同的组。

当以下情况成立时，分配生效：

- 原本不在工程分配范围内的用户可以打开 Grok Bot 并完成 Cursor SSO，而不会遇到 **User is not assigned to this application**。
- 开启自动配置时，该用户在首次登录后出现在 Cursor 团队中，无需手动邀请。
- 关闭自动配置时，该用户在为获取席位登录 Cursor 后，或在你从仪表盘邀请他们后，加入团队。

## 允许从计算机登录 IdP 应用

在托管计算机（hosted computer）内，成员通过浏览器使用你自己的身份提供方登录应用，因此你的会话策略管辖这些会话。该计算机运行 Linux，未加入 MDM，Okta FastPass 等设备信任代理不会在其上运行。任何要求 FastPass、已注册或受管设备、合规设备，或要求只有 FastPass 才能满足的抗钓鱼因素（phishing-resistant factor）的规则，都会在计算机浏览器中失败。

不要为整个公司关闭 FastPass 或设备合规。添加一条优先级更高、作用域限于这个非受管 Linux 会话的规则。此更改只覆盖 Bot 在计算机浏览器中打开的、由 IdP 发放的应用；Grok Bot 登录或已连接应用登录不需要它。

以下登录方法可在计算机浏览器中使用：

- **密码加上在远程浏览器中可用的第二因素**，例如 Okta Verify 推送或身份验证器应用。
- **存储在计算机上密码管理器中的通行密钥（passkey）**；该密码管理器通过 [Team Setup Scripts](https://cursor.com/docs/grok-bot/teams#team-setup-scripts) 安装。Team Setup Scripts 仅限 Enterprise。

要求 Grok Bot 登录本身使用受管设备仍然可行。Grok Bot 使用你的 Cursor SSO，因此身份提供方中感知设备的登录策略会作用于它。该策略在成员设备上限制登录，而不是在托管计算机上。

在 Okta Identity Engine 中，计算机会匹配 **Other Desktop** 设备平台；没有 Linux 复选框。对 Bot 在计算机浏览器中打开的每个由 IdP 发放的应用，重复这些步骤。

1. 前往 **Admin Console** > **Security** > **Authentication Policies**，打开附加到该应用的策略。要找到该策略，请打开 **Applications**，然后打开该应用，再打开 **Sign On**。
2. 在 FastPass、受管设备和拒绝兜底规则之上添加一条规则。给它起一个以后能找到的名字，例如 **Grok Bot computer (Linux)**。
3. 在 IF 条件中，把规则的作用域限定到一个组。如果你不希望规则覆盖全公司，Cursor 分配的组即可。
4. 将 **Device platform** 设为 **Other Desktop**，将 **Device state** 设为 **Any**。不要要求 **Registered**、**Managed**，也不要要求依赖 FastPass 的设备保障策略。
5. 在 THEN 条件中，将访问权限设为 **Allowed after successful authentication**，并使用 **Password + Another factor**。不要要求抗钓鱼或硬件保护因素。
6. 保存规则，并确认它位于非受管设备拒绝兜底规则之上。

如果多个应用共享一条「受管设备上要求 FastPass」的策略，请把 Linux 规则添加到共享策略并按组限定作用域，或给这些应用各自的策略。在 Classic Engine 上，允许 **Other Desktop**，但不要要求 **Device Trust = Trusted**。

当用户可以从 Bot 的计算机登录由 IdP 发放的应用，而不出现 FastPass 或设备合规错误；已连接应用登录与之前一样工作；笔记本登录保持不变时，该更改即生效。

无论哪种方式，撤销权都在你手中：在身份提供方中撤销用户，会结束其在计算机内的应用会话；组织管理员也可以随时[终止该成员的计算机](https://cursor.com/docs/grok-bot/security#identity-and-sign-ins)。

## 限制

- Okta FastPass 不在 Linux 上运行，因此 Bot 的计算机无法满足 FastPass 或受管设备规则。
- 计算机默认不加入 MDM。
- Entra ID 中基于组的分配需要 P1 或 P2，且不包含嵌套组。

## 常见问题

### 我需要在 Okta 或 Entra ID 中为 Grok Bot 单独创建一个应用吗？

不需要。Grok Bot 登录使用 Cursor 账户，因此你现有的 Cursor 应用控制访问。扩大该应用的分配范围，而不是创建新应用。

### 设备信任更改会影响已连接应用的登录吗？

不会。连接应用不经过计算机，因此适用于计算机浏览器的身份验证规则不会作用于它。

### 这些更改会削弱员工笔记本上的登录吗？

不会。把新规则或策略的作用域限定为 Linux 平台和 Cursor 分配的组，笔记本登录会保留你现有的要求。

### 如果我从 Cursor 应用取消分配某个用户，他们会失去访问权吗？

会，他们无法再通过 SSO 登录。使用 SCIM 时，取消分配也会自动将其从 Cursor 中移除；不使用 SCIM 时，请在仪表盘中将其从团队中移除。
