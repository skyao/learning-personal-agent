---
title: "文档：安全 FAQ"
linkTitle: "文档：安全 FAQ"
date: 2026-11-05
originalTitle: "Grok Bot security FAQ"
sourceUrl: "https://docs.x.ai/grok-bot/security-faq"
altUrls: ["https://cursor.com/docs/grok-bot/security-faq"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-12
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：新增「只屏蔽几个网站」问答（Allow All Sites Except These，至多 50 个主机名，尽力而为）；推理钩子改称只检查模型输入；Shared Bot 改称 Team Bot，xAI 模型改称 SpaceXSI"
tags: [安全, 隐私, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：这是安全评审常问问题的答案汇编。隔离：每个用户一台独立的 Firecracker microVM，同一用户的所有 Bot 共用该计算机；Bot 没有自己的身份，不能超出登录成员的权限。网络：Network Controls 仅限 Enterprise，可设允许列表，也可选 Allow All Sites Except These，列出至多 50 个主机名（含子域），覆盖 shell、浏览器、WebFetch 和 MCP 服务器，但只是尽力而为、不是安全边界；计算机使用共享静态出口 IP，无专用 IP；无法在客户自有边界内部署，也不支持自带镜像，只能运行在 Cursor 托管云端。审批与日志：Auto Review 在开启强制时检查 shell、应用调用、计算机使用、自动化写入和委派；推理钩子（Enterprise beta）只检查模型输入、不检查动作；审计日志、Action Recording（默认关闭）和 OpenTelemetry 导出均为 Enterprise 专有。模型：团队模型允许列表不管 Grok Bot，没有面向客户的模型选择器；计算机位于美国，Anysphere 持有 ISO/IEC 27001 和 42001 认证。

**保留理由**：以问答形式汇总了安全评审的要点，可快速核对哪些控制是 Enterprise 专有、哪些不支持。

---

Grok Bot 安全 FAQ

这些是安全评审最常问的问题。每个答案背后的控制项见 [Grok Bot 安全](https://docs.x.ai/grok-bot/security)。仪表盘设置和推广步骤见[面向团队和企业的 Grok Bot](https://docs.x.ai/grok-bot/teams-and-enterprises)。

## 隔离与访问

### 用户之间如何隔离？

每个用户获得一台专用的 Firecracker microVM，有自己的内核、内存和虚拟设备。一个用户无法访问另一个用户的计算机。在一个用户内部，所有 Bot 共用那台计算机。把计算机上的登录或文件视为该用户运行的每个 Bot 都能访问。当某项工作负载需要自己的计算机和凭据集时，给它单独的 Cursor 用户。队友的 [Team Bot](https://docs.x.ai/grok-bot/team-bots) 在该用户与它自己的聊天中，通常在该用户的计算机上工作。

### Bot 可以访问什么？

只能访问成员或团队授予的账户和已连接应用。Bot 没有自己的身份，不能持有超过已登录成员的访问权。连接器令牌留在 Cursor 后端。保存在 Vault 中的登录信息和银行卡，以及在安全表单中输入的值，由系统填入，模型看不到。表单无法处理的步骤（如单点登录或通行密钥）交给成员。见[身份与登录](https://docs.x.ai/grok-bot/security#identity-and-sign-ins)。

### 如果我们屏蔽某个应用，Bot 还能在浏览器中访问该服务吗？

能。屏蔽应用不会屏蔽该服务的网站。连接器策略和[网络策略](https://docs.x.ai/grok-bot/security#network-policy)是分开的两层。关闭网站这条路径需要**网络控制**（Network Controls），它仅限 Enterprise。

### 管理员可以向成员推送连接器吗？

不能。连接器策略允许或阻止服务器。向成员配置连接器（无论强制还是默认开启）不可用。

## 网络与出口

### 我们可以限制计算机能访问哪些目的地吗？

**网络控制仅限 Enterprise。**管理员在仪表盘 Grok Bot 页面的该面板中设置 Grok Bot 网络策略。自助式 Teams 看不到它，也无法设置目的地允许列表。没有策略的团队默认全放行。见[网络策略](https://docs.x.ai/grok-bot/security#network-policy)。

### 我们可以屏蔽少数站点，而不是用允许列表吗？

可以。在**网络控制**中选择**除这些站点外全部允许**（Allow All Sites Except These），最多列出 50 个主机名；每个主机名也会屏蔽其子域。它覆盖计算机的 shell 和浏览器、WebFetch 以及 MCP 服务器。它是尽力而为，不是安全边界：裸 IP 地址可以穿过，WebSearch 结果不会被过滤。见[被阻止的站点](https://docs.x.ai/grok-bot/security#blocked-sites)。

### 管理控制是按组生效，还是只在整个组织范围生效？

目录组范围是**网络控制**的一部分，后者仅限 Enterprise。组可以设置自己的策略，锁定会让团队策略对所有人生效。组织级启用开关也仅限 Enterprise，作用于整个组织。云端智能体、团队规则和公开模板分享在 Teams 和 Enterprise 上作用于整个团队。强制自动审查和自动审查规则仅限 Enterprise，也作用于整个团队。允许本地出口路由仅限 Enterprise，作用于整个团队。在 Enterprise 上，组的 Grok Bot 标签页可以为其成员放宽云端智能体、智能体邮箱、本地执行、本地出口、自动审查、规则和安装脚本，绝不会收紧。见[组设置](https://docs.x.ai/grok-bot/teams-and-enterprises#group-settings)。

### 为什么有些网站会屏蔽 Bot？

有些服务会标记数据中心 IP 地址。出口范围是共享的静态范围，可从你的客户团队获取；在适当的地方把它们加入你自己服务的允许列表。

### 有专用出口 IP 吗？

没有。计算机使用共享的静态出口 IP 地址。不提供按客户的专用 IP。当前范围可从你的客户团队获取。

### 流量可以经过我们自己的网络吗？

可以。成员可以让 Grok Bot 计算机的 Web 流量经过自己的桌面，使用其网络和 IP 地址。在那条路由上，解析到私有地址或 VPN 地址的站点会被阻止，除非已为你的组织允许。Enterprise 团队还可以通过**团队安装脚本**（Team Setup Scripts）在每台托管计算机上安装网络客户端。见[连接到私有网络](https://docs.x.ai/grok-bot/private-networks)。

### Grok Bot 在我们网络下卡在计算机设置阶段，为什么？

像 Zscaler 这样的 TLS 检查网关放行了 `api2.cursor.sh`，却阻止或检查计算机的嵌套 `cursorvm.com` 主机名。聊天可能还能用，也可能不能；无论哪种情况，计算机连接都会失败。放行 `*.cursorvm.com` 和 `*.*.cursorvm.com`，免除检查，并把更改也应用到非公司网络的配置。见[配置 TLS 检查代理](https://docs.x.ai/grok-bot/proxies)。

## 审批、日志与数据

### Auto Review 检查什么？

开启强制实施后，Auto Review 评估 shell 命令、应用调用、计算机使用、自动化写入，以及云端智能体和子智能体启动等委派。它可以放行动作、要求批准或拒绝。在 Enterprise 上，团队管理员可以从 Grok Bot 页面强制实施自动审查，并添加每个成员都会继承的团队自动审查规则。成员可以在其上添加更严格的个人规则，规则冲突时**先询问**（Ask first）优先。如果管理员关闭强制实施，成员只使用自己的规则。它不审查每个副作用，例如记忆写入和大多数设置更改。

### 我们自己的安全工具能检查 Grok Bot 发送给模型的内容吗？

可以，用推理钩子（inference hooks），这是一个 Enterprise beta。Cursor 把每个 Grok Bot 模型请求签名后发送到你组织运行或通过安全厂商使用的 AI 安全服务器，你的服务器在模型运行前允许或拒绝它。钩子检查模型输入，而不是运行中的动作。任何 Enterprise 团队的团队管理员都可以从仪表盘设置。见 [Grok Bot 推理钩子](https://docs.x.ai/grok-bot/inference-hooks)。

### 我能看到 Bot 代表我的团队做了什么吗？

支出和用量在仪表盘的用量页面上，按产品细分。**审计日志仅限 Enterprise。**它们涵盖管理员、安全和认证事件，以及 Bot 创建、访问更改、团队安装和例程等 Grok Bot 控制平面事件，可按应用筛选，并能流式传输到你的 SIEM。**操作记录（Action Recording）仅限 Enterprise**，是一个单独的设置，默认关闭。启用后，它在内部记录 Bot 的操作。**OpenTelemetry 导出仅限 Enterprise。**配置它，在你自己的收集器中接收这些事件，标记为 `cursor.surface=grok_bot`。它们不会出现在审计日志页面上。

### 我可以限制 Grok Bot 使用哪些模型吗？

不可以。团队模型允许列表不约束 Grok Bot。它使用 SpaceXSI 的第一方模型，也可能使用[子处理方名单](https://trust.cursor.com/subprocessors)上提供商的第三方模型，不受该设置影响。设置模型允许列表的团队在启用 Grok Bot 时会看到这一确认。Grok Bot 管理模型选择，没有面向客户的模型选择器。如果你的合同限制子处理方，请联系你的客户团队。见[我可以选择模型吗？](https://docs.x.ai/grok-bot/faq#can-i-pick-the-model)。

### Grok Bot 的计算机在哪里运行？

在美国。Grok Bot 也受 Cursor 的[仅美国数据驻留](https://cursor.com/docs/enterprise/privacy-and-data-governance#us-data-residency)计划覆盖，该计划为登记客户把推理、数据处理和存储保持在美国。联系你的客户团队登记。见[数据驻留](https://docs.x.ai/grok-bot/security#data-residency)。

### 我们可以在本地运行 Grok Bot，或使用自己的镜像吗？

不可以。Grok Bot 只在 Cursor 托管的云计算机上运行。本地部署、在你自己的边界内部署，以及自带镜像部署目前都不支持。

### 我们可以在团队计算机上安装自己的安全工具吗？

**团队安装脚本仅限 Enterprise。**这些管理员可以在每台团队计算机上安装自己的工具。Grok Bot 不提供内置的面向客户的 EDR 数据源（feed）。

### 为什么成员必须重新登录公司工具？

计算机内的登录会话可能在计算机重建时失效，例如镜像更新后或管理员重建后。会话依赖你的身份提供商，因此你的会话策略也会生效。

### 管理员终止计算机后数据会怎样？

计算机管理仅限 Enterprise。组织管理员和 Enterprise 团队管理员可以终止成员的计算机。持久磁盘保留，该成员的下次会话会在该磁盘上启动一台新计算机。终止计算机与仅限 Enterprise 的启用开关是分开的。

### Grok Bot 适用哪些认证？

Anysphere 持有 Schellman 颁发的 ISO/IEC 27001 和 ISO/IEC 42001 认证，Grok Bot 包含在当前 ISO 范围内。证书和报告可在 [trust.cursor.com](https://trust.cursor.com) 获取。
