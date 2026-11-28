---
title: "文档：配置身份与访问"
linkTitle: "文档：身份与访问"
date: 2026-11-05
originalTitle: "Configure identity and access"
sourceUrl: "https://docs.x.ai/grok-bot/identity-and-access"
altUrls: ["https://cursor.com/docs/grok-bot/identity"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-11
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：Okta FastPass 在按 Okta Verify and FastPass 页面设置后可在 Bot 计算机上使用（旧版称计算机不运行设备信任代理）；新增 Okta、Entra ID 各自分步的分配与规则/策略步骤"
tags: [安全, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：面向使用 Okta 或 Microsoft Entra ID 作身份提供方的管理员。Grok Bot 使用 Cursor 账号，因此没有独立的 Okta 或 Entra 应用，需要把现有 Cursor 应用分配给工程以外的用户组，才能让他们访问，文中分别给出 Okta 与 Entra ID 的步骤；SCIM 仅限 Enterprise，Entra ID 的按组分配需要 P1 或 P2。另一项改动是在身份提供方里为 Bot 的计算机浏览器会话增加认证规则（Okta 中设备平台选 **Other Desktop**，Entra ID 中新建条件访问策略放行 Linux），因为这台 Linux 计算机不是托管设备，也未纳入 MDM；Okta FastPass 只有在按 Okta Verify and FastPass 页面设置后才能在计算机上运行，要求托管或合规设备的规则无论如何都会失败。这条规则只影响 Bot 在计算机浏览器里打开的、由身份提供方发放的应用，不影响 Grok Bot 登录或连接应用的登录。撤销用户在身份提供方的权限会终止其计算机内的应用会话，管理员也可随时终止成员的计算机。

**保留理由**：说明托管计算机在企业身份体系里的位置：登录走 Cursor SSO，而计算机内的登录不满足设备信任，因此要单独放行，对理解其与企业身份的关系有用。

---

配置身份与访问

本指南面向以 Okta 或 Microsoft Entra ID 作为身份提供方（IdP）的管理员。它涵盖两件事：让工程组织之外的人通过你的 Cursor 团队访问 Grok Bot；让成员从 Bot 的电脑登录由 IdP 发放的应用。更完整的安全模型见 [Grok Bot 安全](https://docs.x.ai/grok-bot/security)。

Grok Bot 使用你的 Cursor 账号，所以 Okta 或 Entra ID 里没有单独的 Grok Bot 应用。本指南的一切操作都在你已有的 Cursor 应用上进行。Cursor 的单点登录是 SAML 2.0，可与 Okta、Microsoft Entra、Google Workspace 和 OneLogin 配合；本指南详细说明最常需要关注设备信任策略的其中两家。

## 你会改动什么

你会做两处改动，它们作用不同：

* [分配 Cursor 应用](#assign-the-cursor-app)，让工程组织之外的用户能通过你的 Cursor 团队访问 Grok Bot。
* [添加一条认证规则](#allow-sign-in-to-idp-apps-from-the-computer)，让用户能从 Bot 的电脑登录由 IdP 发放的应用；这台电脑运行 Linux，不是受管设备。

只有第一处改动控制 Grok Bot 的登录。第二处从不会阻止它，也不适用于连接应用的登录，因为连接应用不经过这台电脑。

## 开始之前

访问 Grok Bot 要求用户是你 Cursor 团队的成员。成员用他们的 Cursor 账号登录，所以你现有的 [Cursor SSO](https://cursor.com/docs/account/teams/sso) 仍然适用。开启自动配置时，用户首次登录即加入团队；否则先配置用户，再让他们登录 Cursor 获取席位，或从 [Cursor 仪表盘](https://cursor.com/dashboard)邀请他们。

**SCIM 仅限 Enterprise。** 如果你使用 [SCIM](https://cursor.com/docs/account/teams/scim)，配置走 SCIM 2.0，取消配置是自动的：在身份提供方里移除用户，就会把他们从 Cursor 中移除。

## 分配 Cursor 应用

用户只有拥有 Cursor 账号才能登录，而账号来自被分配到现有的 Cursor SSO 应用，如果你使用 SCIM，还要分配到 SCIM 应用。如果 Cursor 只分配给了工程部门，其他人会以 **用户未被分配到此应用（User is not assigned to this application）** 失败，或者他们的邀请永远无法完成。不要另建一个 Grok Bot 应用；在你已有的 Cursor 应用上扩大分配范围。

### 在 Okta 中分配应用

1. 转到 **管理控制台 → 应用 → 应用**（**Admin Console → Applications → Applications**），打开你已有的 Cursor 应用。
2. 打开 **分配（Assignments）**，选择 **分配 → 分配到组**（**Assign → Assign to Groups**）。如果要改为分配给个人，选择 **分配到人员**（**Assign to People**）。
3. 添加每一个应获得 Grok Bot 的组，而不只是工程部门。
4. 如果你使用 SCIM，把同样的组分配到 Cursor SCIM 应用并推送。用户只有在被分配到 SCIM 应用后才会出现在 Cursor 中。
5. 确认每个组也被分配到 SAML 应用。只有 SCIM 分配而没有 SSO 分配，仍然会挡住首次登录。

如果你在 Cursor 中使用组织级身份，在目录组同步后把它映射到 Grok Bot 团队；见[组织](https://cursor.com/docs/enterprise/organizations)。应用分配与 Group Push 要使用不同的组。

### 在 Microsoft Entra ID 中分配应用

1. 转到 **Microsoft Entra 管理中心 → 企业应用**（**Microsoft Entra admin center → Enterprise applications**），打开你已有的 Cursor 企业应用。
2. 打开 **用户和组（Users and groups）**，选择 **添加用户/组（Add user/group）**。
3. 添加每一个应获得 Grok Bot 的组，而不只是工程部门。
4. 如果你使用 SCIM，把同样的组分配到 Cursor 配置应用。开启配置，并把范围限定为已分配的用户和组。
5. 确认该分配授予的是 SSO，而不是仅报告访问。

基于组的分配需要 Entra ID P1 或 P2，且不包含嵌套组。用户必须被明确分配，取消分配会阻止 SSO 登录，如果使用 SCIM，还会把他们从 Cursor 中移除。

对两家提供方来说，分配生效的标志是：

* 原本不在工程分配范围内的用户能打开 Grok Bot 并完成 Cursor SSO，且不会出现 **用户未被分配到此应用**。
* 开启自动配置时，该用户在首次登录后出现在 Cursor 团队中，无需手动邀请。
* 关闭自动配置时，该用户在登录 Cursor 获取席位后，或在你从仪表盘邀请他们之后，出现在团队中。

## 允许从电脑登录 IdP 应用

在托管电脑内，成员通过浏览器经由你自己的身份提供方登录应用，所以你的会话策略管辖这些会话。这台电脑运行 Linux，未加入移动设备管理（MDM）。只有在按[设置 Okta Verify 与 FastPass](https://docs.x.ai/grok-bot/okta-fastpass) 配置后，Okta FastPass 才能在它上面运行。没有这项设置，任何要求 FastPass、或要求只有 FastPass 才能满足的抗钓鱼因素（phishing-resistant factor）的规则，都会在电脑浏览器里失败。要求受管或合规设备的规则无论如何都会失败。

不要为整个公司关掉 FastPass 或设备合规要求。如果你的策略要求 FastPass，就在这些电脑上设置 Okta Verify。否则，添加一条针对这个非受管 Linux 会话的更高优先级规则。这项改动只覆盖 Bot 在电脑浏览器里打开的、由 IdP 发放的应用；Grok Bot 登录和连接应用登录都不需要它。

以下登录方式可在电脑浏览器中使用：

* 密码加上可在远程浏览器中使用的第二因素，例如 Okta Verify 推送或验证器应用。
* 存放在电脑上密码管理器里的通行密钥（passkey），通过[团队设置脚本](https://docs.x.ai/grok-bot/teams-and-enterprises#team-setup-scripts)安装。团队设置脚本（Team Setup Scripts）仅限 Enterprise。
* Okta FastPass，在用团队设置脚本[设置 Okta Verify 与 FastPass](https://docs.x.ai/grok-bot/okta-fastpass)之后可用。FastPass 能满足 FastPass 和 Okta Verify 因素的要求，但满足不了受管设备规则。

> 为 Grok Bot 登录本身要求受管设备仍然有效。Grok Bot 使用你的 Cursor SSO，所以身份提供方中感知设备的登录策略对它适用。该策略约束的是成员设备上的登录，而不是托管电脑。

### 在 Okta 中添加规则

在 Okta Identity Engine 中，这台电脑匹配 **其他桌面（Other Desktop）** 设备平台；没有 Linux 这个勾选项。对 Bot 在电脑浏览器里打开的每个 IdP 发放应用，重复这些步骤。

1. 转到 **管理控制台 → 安全 → 认证策略**（**Admin Console → Security → Authentication Policies**），打开附加到该应用的策略。要找到该策略，打开 **应用**，再打开该应用，然后看 **登录（Sign On）**。
2. 在 FastPass、受管设备和默认拒绝（deny catch-all）规则之上添加一条规则。给它起个名字方便以后找到，例如 **Grok Bot 电脑（Linux）**。
3. 在 IF 条件中，把规则限定到一个组。如果你不希望这条规则覆盖全公司，用分配给 Cursor 的那个组即可。
4. 把 **设备平台（Device platform）** 设为 **其他桌面（Other Desktop）**，**设备状态（Device state）** 设为 **任意（Any）**。不要要求 **已注册（Registered）**、**受管（Managed）**，也不要要求依赖 FastPass 的设备保障策略。
5. 在 THEN 条件中，把访问权限设为 **认证成功后允许（Allowed after successful authentication）**，配合 **密码 + 另一个因素（Password + Another factor）**。不要要求抗钓鱼或硬件保护因素。
6. 保存规则，并确认它位于非受管设备默认拒绝规则之上。

如果多个应用共用一个「受管设备上要求 FastPass」的策略，可以把 Linux 规则加到共享策略里，并按组限定范围，或者给这些应用单独的策略。在 Classic Engine 上，允许 **其他桌面（Other Desktop）**，但不要求 **设备信任 = 受信任（Device Trust = Trusted）**。

### 在 Microsoft Entra ID 中添加策略

Entra ID 没有 FastPass。会挡住电脑浏览器的是这些授予条件：合规设备、混合加入设备、只有平台通行密钥或受管通行密钥才能满足的抗钓鱼认证强度，以及已批准的客户端应用或应用保护策略。

1. 转到 **Microsoft Entra 管理中心 → 保护 → 条件访问 → 策略**（**Microsoft Entra admin center → Protection → Conditional Access → Policies**）。
2. 找出所有把这些授予条件应用到 Bot 所需 IdP 应用的策略。
3. 保留这些策略。为 Linux 上的 Grok Bot 用户添加一条更高优先级的策略，或把他们从阻止性策略中排除。
4. 在新策略中，把用户设为分配给 Cursor 的组，目标设为他们在电脑上必须打开的 IdP 应用。只有在你接受该范围时才选择 **所有资源（All resources）**。
5. 在 **设备平台（Device platforms）** 下，包含 **Linux**，排除 **Windows** 和 **macOS**。
6. 把授予条件只设为 **要求多重身份验证（Require multifactor authentication）**。
7. 先以仅报告模式（report-only mode）启动策略，然后再开启。
8. 在现有的合规设备策略上，排除该组或排除 Linux。

要在没有受管设备的情况下实现抗钓鱼，使用同步通行密钥（synced passkey）可以满足的认证强度，并在强制执行前先从电脑上测试登录。

对两家提供方来说，改动生效的标志是：用户能从 Bot 的电脑登录由 IdP 发放的应用，且不出现 FastPass 或设备合规错误；连接应用的登录与之前一样；笔记本电脑上的登录保持不变。

无论哪种方式，撤销权都在你手上：在身份提供方里撤销用户会终止其在电脑内的应用会话，组织管理员也可以随时[终止成员的电脑](https://docs.x.ai/grok-bot/security#identity-and-sign-ins)。

## 限制

* 只有在按[设置 Okta Verify 与 FastPass](https://docs.x.ai/grok-bot/okta-fastpass) 配置后，Okta FastPass 才能在 Bot 的电脑上运行。
* 这台电脑默认不加入 MDM，所以无法满足受管设备或合规设备规则。
* Entra ID 中基于组的分配需要 P1 或 P2，且不包含嵌套组。

## 常见问题

### 我需要在 Okta 或 Entra ID 里单独建一个 Grok Bot 应用吗？

不需要。Grok Bot 登录使用 Cursor 账号，所以你现有的 Cursor 应用控制访问。在那上面扩大分配范围，而不是新建一个。

### 设备信任的改动会影响连接应用的登录吗？

不会。连接应用不经过这台电脑，所以针对电脑浏览器的认证规则不适用于它。

### 这些改动会削弱员工笔记本电脑上的登录吗？

不会。把新规则或新策略限定到 Linux 平台和分配给 Cursor 的组，笔记本电脑上的登录仍然沿用你现有的要求。

### 如果我把用户从 Cursor 应用取消分配，他们会失去访问权吗？

会，他们不能再通过 SSO 登录。使用 SCIM 时，取消分配也会自动把他们从 Cursor 中移除；不使用 SCIM 时，在仪表盘里把他们从团队中移除。
