---
title: "文档：安全 FAQ"
linkTitle: "文档：安全 FAQ"
date: 2026-11-05
originalTitle: "Grok Bot security FAQ"
sourceUrl: "https://cursor.com/docs/grok-bot/security-faq"
altUrls: ["https://docs.x.ai/grok-bot/security-faq"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 隐私, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：这是安全评审常问问题的答案汇编。隔离：每个用户一台独立的 Firecracker microVM，同一用户的所有 Bot 共用该计算机；Bot 没有自己的身份，不能超出登录成员的权限。网络：Network Controls 仅限 Enterprise，计算机使用共享静态出口 IP，无专用 IP；无法在客户自有边界内部署，也不支持自带镜像，只能运行在 Cursor 托管云端。审批与日志：Auto Review 在开启强制时检查 shell、应用调用、计算机使用、自动化写入和委派；审计日志、Action Recording（默认关闭，保留 90 天）和 OpenTelemetry 导出均为 Enterprise 专有。模型：团队模型允许列表不管 Grok Bot，没有面向客户的模型选择器；数据位于美国，Anysphere 持有 ISO/IEC 27001 和 42001 认证。

**保留理由**：以问答形式汇总了安全评审的要点，可快速核对哪些控制是 Enterprise 专有、哪些不支持。

---

这些是安全审查中最常被问到的问题。每个答案背后的控制措施见 [Grok Bot 安全](https://cursor.com/docs/grok-bot/security)。仪表盘设置和推出步骤见 [Grok Bot 团队与企业版](https://cursor.com/docs/grok-bot/teams)。

## 隔离与访问

### 用户之间如何隔离？

每个用户获得一台专用的 Firecracker 微虚拟机（microVM），拥有自己的内核、内存和虚拟设备。一个用户无法访问另一个用户的计算机。在同一个用户内部，每个 Bot 共用那台计算机。请把该计算机上的登录信息或文件视为该用户运行的每个 Bot 都可使用。当某个工作负载需要自己的计算机和凭据集时，请为它分配独立的 Cursor 用户。队友的[共享 Bot](https://cursor.com/help/grok-bot/shared-bots)通常在该用户自己与它聊天期间，运行在该用户的计算机上。

### Bot 可以访问什么？

只能访问成员或团队授予的账户和已连接的应用。Bot 没有自己的身份，拥有的访问权限不能超过已登录成员。连接器 token 保留在 Cursor 后端。保存在 Vault 中的登录信息和卡片，以及在 Secure Form 中输入的值，会在不被模型看到的情况下填入。表单无法处理的步骤，例如单点登录或通行密钥（passkey），会交给成员完成。参见[身份与登录](https://cursor.com/docs/grok-bot/security#identity-and-sign-ins)。

### 如果我们阻止了某个应用，Bot 还能在浏览器中访问该服务吗？

能。阻止一个应用并不会阻止该服务的网站。连接器策略和[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)是独立的层。关闭网站访问路径需要 **Network Controls**，它仅限 Enterprise。

### 管理员可以向成员推送连接器吗？

不能。连接器策略只负责允许或阻止服务器。向成员预配连接器（无论是强制还是默认开启）不可用。

## 网络与出口

### 我们可以限制计算机能访问哪些目标吗？

**Network Controls 仅限 Enterprise。** 管理员可在仪表盘 Grok Bot 页面的该面板中设置 Grok Bot 网络策略。自助式（Self-serve）Teams 看不到它，也无法设置目标允许列表。没有策略的团队默认允许全部。参见[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)。

### 管理控制是按组应用，还是仅限整个组织？

目录组（directory-group）范围是 **Network Controls** 的一部分，后者仅限 Enterprise。组可以设置自己的策略，而锁定会使团队策略对所有人生效。组织范围的启用开关也仅限 Enterprise，并适用于整个组织。Cloud Agents、Team Rules 和公开模板分享在 Teams 和 Enterprise 上适用于整个团队。Enforce Auto-review 和 Auto-review rules 仅限 Enterprise，也适用于整个团队。Allow Local Egress Routing 仅限 Enterprise，适用于整个团队。在 Enterprise 上，某个组的 Grok Bot 标签页可以为该组成员放宽 Cloud Agents、智能体电子邮件、本地执行、本地出口、Auto-review、规则和安装脚本，但绝不能收紧它们。参见[组设置](https://cursor.com/docs/grok-bot/teams#group-settings)。

### 为什么有些网站会阻止 Bot？

有些服务会标记数据中心 IP 地址。出口范围是共享的静态范围，可从你的客户团队获取；在适当情况下将它们加入你自己服务的允许列表。

### 提供专用出口 IP 吗？

不提供。计算机使用共享的静态出口 IP 地址。不提供每客户专用的 IP。当前范围可从你的客户团队获取。

### 流量可以经我们自己的网络运行吗？

可以。成员可以让 Grok Bot 计算机的网页流量经其桌面转出，使用该设备的网络和 IP 地址。在该路由上，解析到私有地址或 VPN 地址的站点会被阻止，除非已为你的组织允许。Enterprise 团队还可以通过 **Team Setup Scripts** 在每台托管计算机上安装网络客户端。参见[连接私有网络](https://cursor.com/docs/grok-bot/private-networks)。

### Grok Bot 在我们的网络环境下卡在计算机设置阶段。为什么？

像 Zscaler 这样的 TLS 检查网关放行了 `api2.cursor.sh`，却在阻止或检查计算机嵌套的 `cursorvm.com` 主机名。聊天可能仍能工作，也可能不能；但计算机连接无论如何都会失败。请允许 `*.cursorvm.com` 和 `*.*.cursorvm.com`，将其排除在检查之外，并同样把更改应用到离网（off-network）配置文件。参见[配置 TLS 检查代理](https://cursor.com/docs/grok-bot/proxies)。

## 审批、日志与数据

### Auto Review 检查什么？

开启强制（enforcement）后，Auto Review 会评估 shell 命令、应用调用、计算机使用、自动化写入，以及诸如 Cloud Agent 和子智能体启动之类的委派。它可以允许操作继续、要求审批或拒绝操作。在 Enterprise 上，团队管理员可以从 Grok Bot 页面强制启用 Auto-review，并添加每位成员都会继承的团队 Auto-review 规则。成员可以在其上添加更严格的个人规则，规则冲突时 **Ask first** 优先。如果管理员关闭强制，成员将仅使用自己的规则。它不会审查每一个副作用，例如记忆写入和大多数设置更改。

### 我们自己的安全工具可以检查 Grok Bot 发送给模型的内容吗？

可以，通过推理挂钩（inference hooks），这是 Enterprise 测试版。Cursor 会把每个 Grok Bot 模型请求签名后发送到你组织运行或通过安全供应商使用的 AI 安全服务器，你的服务器在模型运行前允许或拒绝该请求。挂钩检查模型输入。在启用了工具调用检查的团队中，它们还可以在工具调用运行前进行检查，但无法检查操作开始后做了什么。任何 Enterprise 团队的团队管理员都可以从仪表盘设置它们。参见 [Grok Bot 推理挂钩](https://cursor.com/docs/grok-bot/inference-hooks)。

### 我可以查看 Bot 代表我的团队做了什么吗？

支出和使用情况在仪表盘的使用情况页面上，按产品细分。**审计日志（audit logs）仅限 Enterprise。** 它们涵盖管理、安全和身份验证事件，以及 Grok Bot 控制平面事件，例如 Bot 创建、访问更改、Team Setup 和例程，可按应用筛选，并可流式传输到你的 SIEM。**Action Recording 仅限 Enterprise**，是一个单独的设置，默认关闭。启用后，它会在内部记录 Bot 的操作。**OpenTelemetry Export 仅限 Enterprise。** 配置它在你自己的收集器中接收这些事件，标记为 `cursor.surface=grok_bot`。它们不会出现在 Audit Log 页面上。

### 我可以限制 Grok Bot 使用哪些模型吗？

不能。团队模型允许列表不约束 Grok Bot。它使用 xAI 的第一方模型，并且可能使用[子处理者列表](https://trust.cursor.com/subprocessors)上供应商的第三方模型，无论该设置如何。带有模型允许列表的团队在启用 Grok Bot 时会看到这一确认。Grok Bot 管理模型选择，没有面向客户的模型选择器。如果你的合同限制子处理者，请联系你的客户团队。参见[Grok Bot 由哪些 AI 模型驱动？](https://cursor.com/help/grok-bot/models)。

### Grok Bot 计算机在哪里运行？

在美国。Grok Bot 也受 Cursor 的[仅限美国数据驻留](https://cursor.com/docs/enterprise/privacy-and-data-governance#us-data-residency)计划覆盖，该计划为已注册客户把推理、数据处理和存储保留在美国。请联系你的客户团队进行注册。参见[数据驻留](https://cursor.com/docs/grok-bot/security#data-residency)。

### 我们可以在本地部署 Grok Bot，或使用自己的镜像运行吗？

不能。Grok Bot 只在 Cursor 托管的云计算机上运行。本地部署、在你自己的边界内部署，以及自带镜像（bring-your-own-image）部署目前均不受支持。

### 我们可以在团队计算机上安装自己的安全工具吗？

**Team Setup Scripts** 仅限 Enterprise。这些管理员可以在每台团队计算机上安装自己的工具。Grok Bot 不提供内置的面向客户的 EDR 数据流（feed）。

### 为什么成员必须重新登录公司工具？

当计算机被重新创建时，计算机内部的登录会话可能会丢失，例如在镜像更新之后，或管理员重新创建它时。会话依托你的身份提供商，因此你的会话策略也适用。

### 管理员终止一台计算机时，数据会怎样？

计算机管理仅限 Enterprise。组织管理员和 Enterprise 团队管理员可以终止成员的计算机。持久磁盘会被保留，该成员的下一个会话会在该磁盘上启动一台全新的计算机。终止计算机与仅限 Enterprise 的启用开关是分开的。

### Grok Bot 适用哪些认证？

Anysphere 持有由 Schellman 颁发的 ISO/IEC 27001 和 ISO/IEC 42001 认证，Grok Bot 包含在当前 ISO 范围内。证书和报告可在 [trust.cursor.com](https://trust.cursor.com) 获取。
