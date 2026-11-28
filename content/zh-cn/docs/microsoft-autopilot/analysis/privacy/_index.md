---
title: "Microsoft Autopilot：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 的数据路径从 Scout 的「经 GitHub Copilot」变为「经 OpenAI（微软子处理方）」：开启 OpenAI 时提示词由 OpenAI 处理，处理位置和承诺可能与 Azure OpenAI 不同，管理员须自行确认数据驻留与 EU Data Boundary，不符就关掉 OpenAI。记忆与会话存用户 OneDrive，不能关闭；eDiscovery、保留、法律保留不覆盖 Autopilot 会话；官方称不用于训练基础模型。
---

## 概要

- 开启 OpenAI（默认）时，Autopilot 的提示词和相关数据由 OpenAI 作为微软子处理方处理，处理位置和适用承诺可能与 Azure OpenAI 托管模型不同；官方要求管理员在广泛启用前确认符合数据驻留和 EU Data Boundary 要求，不符合就关闭 OpenAI，改用 Azure OpenAI 的 GPT-5.6 Sol（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。
- 训练：应用卡转述 Microsoft Copilot 隐私指南，通过 Microsoft 365 服务访问的提示词、响应和组织数据不用于训练基础模型，并要求结合所启用模型的条款核对（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。
- 记忆与会话存在用户 OneDrive 的 lobster.repo，本版本记忆不能关闭；删除报告「已移除」不证明备份和所有副本都已抹除，正式的删除答复要走组织流程（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）。
- Autopilot 对话尚未纳入 eDiscovery、保留或法律保留；带敏感度标签的内容不被排除在可读范围外，生成内容可能不继承标签（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。
- 管理员可为已批准的合规或隐私请求导出用户的 lobster.repo，但不能代用户删除；批量删除、离职用户删除要联系微软支持（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。
- 初期只在美国开放（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})），地区性的数据驻留说明仍只有「自行确认」一句。

## 2026-11：数据经 OpenAI 处理

管理员文档写明，开启 OpenAI 时 Autopilot 的提示词和相关数据由作为微软子处理方的 OpenAI 处理，处理位置与适用承诺可能与 Azure OpenAI 托管的模型不同；「请确认该提供方的处理符合你的数据驻留和欧盟数据边界」要求，不符合就在 Microsoft 365 管理中心 Copilot > 设置 >「作为 Microsoft 子处理方运营的 AI 提供方」中关闭 OpenAI（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。关闭后自动改用 Azure OpenAI 托管的 GPT-5.6 Sol（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})，见[模型]({{< relref "/docs/microsoft-autopilot/analysis/models" >}})）。应用卡说法一致，并称可用性可能受地区和语言限制（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

Edge 模式下，读到的页面内容（含已登录站点上显示的信息）送到云端模型处理，密码和 cookie 留在 Edge（[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})）。

推断：Scout 时期数据离开 Microsoft 365 的路径是 GitHub Copilot；Autopilot 把它换成 OpenAI 子处理方，并给了一个退路（Azure OpenAI）。对数据驻留敏感的组织，前一轮分析中「障碍在 GitHub 一侧」的判断已不成立，取而代之的是默认开启 OpenAI 子处理。

## 存放、删除与导出

| 数据 | 位置与处理 | 来源 |
| --- | --- | --- |
| 记忆、会话 | 用户 OneDrive 中的 lobster.repo（Git 仓库，含历史） | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 交付物、个人工作 | 用户 OneDrive；任务临时文件完成后不保留 | [Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}}) |
| 导出 | 用户可导出 JSON 到 OneDrive 或用脚本下载完整副本；导出是快照，可能不带敏感度标签 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 管理员导出 | 为已批准的合规或隐私请求导出用户 lobster.repo；须记参考编号，用管理员自己的账户临时获取该用户 OneDrive 访问并记入审计日志，脚本「绝不会使用用户的凭据」 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |

删除的口径（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）：

- 删除会话后底层记录保留，直到用户让 Autopilot 永久删除。
- 报告「已移除」不证明受保留策略管理的记录、备份或所有副本都已抹除；正式的访问、保留、删除答复须走组织的数据管理流程。
- 「我的账户」隐私页不删除 Autopilot 数据；管理员不能代用户删除；批量删除、离职用户删除和经核验的删除要联系微软支持。

## 合规覆盖的缺口

消息中心通告列出的合规提示：记忆始终开启，Microsoft 365 Copilot 的个性化设置不适用；数据保护与审计能力有预览限制；「Autopilot 对话尚未纳入 eDiscovery、保留或法律保留的覆盖范围」（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})）。FAQ 与使用页称 Autopilot 识别受支持内容上的敏感度标签，但带标签的邮件和文件不被排除在可读范围外，新文件可能不继承标签；提示词 DLP 在预览期受限（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。安全侧的对应内容见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})。

## 他人的信息

应用卡与场景页写明，Teams 群聊里 Autopilot 发的消息所有人可见，已发布的回复对能看到讨论串的人可见；审批卡把外部收件人标为「外部」（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。首次设置读取过去 30 天用户可访问的邮件、会议、聊天和文件（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})），其中自然包括同事发来的内容。资料没有讨论对同事或外部联系人信息的专门处理。

## 更名前：Scout 的数据路径（2026-06 至 2026-09）

以下为 2026-11-14 分析的内容，描述 Scout 经 GitHub Copilot 处理的条款。11 月的 Autopilot 文档不再提 GitHub。

### 数据离开 Microsoft 365

消息中心通告与管理员访问概览写明：预览体验包含 Microsoft 365 之外的数据路径（如基于 GitHub 的推理），可能涉及对客户数据的额外处理，「要求管理员明确声明」（[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})）。

负责任 AI FAQ 说得更具体：经 GitHub Copilot 处理时，提示、内容及相关数据可能传至第三方模型提供方；「某些 Microsoft 365 保护——例如数据驻留承诺、保留策略、敏感度标签强制执行、eDiscovery 和其他合规控制——不适用于该处理」（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。FAQ 补充这一处理受组织的 GitHub 客户协议和 GitHub 通用隐私声明约束，并适用 GitHub 的贸易管制要求（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。CIAOPS 和 dSebastien 都把这一段作为部署前必须读的条款转述（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

### 数据存放与用途

| 数据 | 存放位置 | 覆盖的条款 | 来源 |
| --- | --- | --- | --- |
| 会话、记忆 | 用户的 OneDrive | Microsoft DPA、Purview 下的 OneDrive 控制 | [负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}}) |
| 自动化指令、工具输出 | 本机设备 | 不受 Microsoft 365 DPA 覆盖 | [负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}}) |
| 本地文件 | 工作区或授权目录，留在本机 | — | [负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}}) |
| 模型处理的提示与内容 | GitHub Copilot 及第三方模型提供方 | GitHub 客户协议 | [Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}}) |
| 诊断日志 | `~/.copilot/m-diagnostics.jsonl`，仅在启用应用内诊断后存在 | — | [托管设备排障]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-01-scout-managed-troubleshoot" >}}) |

负责任 AI FAQ 称「Microsoft Scout 不使用你的数据训练 AI 模型」，支持访问、删除、更正和可移植性请求（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。用户可在设置中查看和删除记忆（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。

### 他人的信息

资料没有说明对方同意机制。可见的设计有：文件共享只给登录的指定人员，不建匿名或公开链接（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）；Heartbeat 外发的消息只用通用内容，「绝不使用私有数据」（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。Command Line 对谈中 Werner 举的难题是：不能在取消会议时把个人信息发给整串邮件的收件人（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。

### 地区与监管

FAQ 写明 Scout 不适用于美国政府云（GCC、GCC High、DoD）及主权和国家云；没有 Scout 专属的支持国家或地区列表，可用性由 Frontier 注册和管理员控制决定，正式发布后可能变化（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。各模型提供方也可能限制某些地区使用（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。

社区作者称，考虑到 GitHub Copilot 的处理路径，「我不会假定 EU Data Boundary 覆盖了 Scout 的模型调用」；Microsoft 365 保护是否适用于 Autopilot、Autopilot 的对应条款都还没有文档（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

推断：对数据驻留有要求的组织（欧盟、受监管行业），Scout 预览版的主要障碍不在 Microsoft 365 一侧，而在 GitHub 一侧的模型处理；9 月转向云端托管的 Autopilot 是否改变这条路径，是判断它能否进入这些组织的关键，目前没有资料。

## 资料缺口

- OpenAI 子处理时的数据保存期限、处理地点；与 Azure OpenAI 承诺的具体差异。
- 美国以外地区的开放计划与数据驻留说明。
- eDiscovery、保留、法律保留覆盖 Autopilot 的时间表。
- 30 天初始熟悉中同事和外部联系人信息的处理。

## 主要资料

- 官方：[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})（数据离开 Microsoft 365、存放位置、不训练）；[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})（GitHub 客户协议、地区）；[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})（管理员声明）；[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})、[托管设备排障]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-01-scout-managed-troubleshoot" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})。
- 社区：[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})（条款解读与欧盟顾虑）。
- 2026-11 新增官方：[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})（OpenAI 子处理、EU Data Boundary、训练、管理员导出）；[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})（存放、删除口径）；[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})（合规覆盖缺口、标签）；[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})。
