---
title: "Microsoft Autopilot：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 默认由 OpenAI 作为微软子处理方处理提示词和数据，处理位置和承诺可能与 Azure OpenAI 不同，管理员须自行确认数据驻留与 EU Data Boundary，不符就关掉 OpenAI。记忆与会话存用户 OneDrive，本版本不能关闭；eDiscovery、保留、法律保留不覆盖 Autopilot 会话；官方称不用于训练基础模型。初期只在美国开放。
---

## 概要

- 默认开启 OpenAI 时，提示词和相关数据由 OpenAI 作为微软子处理方处理，处理位置和适用承诺可能与 Azure OpenAI 托管模型不同；官方要求管理员在广泛启用前确认数据驻留和 EU Data Boundary 要求，不符合就关掉 OpenAI，改用 Azure OpenAI 的 GPT-5.6 Sol。
- 训练：应用卡转述 Microsoft Copilot 隐私指南，通过 Microsoft 365 服务访问的提示词、响应和组织数据不用于训练基础模型。
- 记忆与会话存在用户 OneDrive 的 lobster.repo，本版本记忆不能关闭；删除报告「已移除」不证明备份和所有副本都已抹除。
- Autopilot 对话尚未纳入 eDiscovery、保留或法律保留；带敏感度标签的内容不排除在可读范围外，生成内容可能不继承标签。
- 管理员可为已批准的合规或隐私请求导出用户数据，但不能代用户删除；批量删除、离职用户删除要联系微软支持。
- 首次设置读取过去 30 天的邮件、会议、聊天和文件，其中包括同事的信息，资料没有讨论对他人信息的专门处理。

## 数据经 OpenAI 处理

管理员文档写明，开启 OpenAI 时 Autopilot 的提示词和相关数据由作为微软子处理方的 OpenAI 处理，处理位置与适用承诺可能与 Azure OpenAI 托管的模型不同；「请确认该提供方的处理符合你的数据驻留和欧盟数据边界」要求，不符合就在 Microsoft 365 管理中心 Copilot > 设置 >「作为 Microsoft 子处理方运营的 AI 提供方」中关闭 OpenAI，之后自动改用 Azure OpenAI 托管的 GPT-5.6 Sol（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})，见[模型]({{< relref "/docs/microsoft-autopilot/analysis/models" >}})）。应用卡说法一致，并称可用性可能受地区和语言限制（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

Edge 模式下，读到的页面内容（含已登录站点上显示的信息）送到云端模型处理，密码和 cookie 留在 Edge（[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})）。

训练方面，应用卡转述 Microsoft Copilot 隐私指南：通过 Microsoft 365 服务访问的提示词、响应和组织数据不会被用于训练基础模型，并要求结合所启用模型的条款核对（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。FAQ 在训练问题上只指向应用卡（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。

推断：默认路径把数据交给 OpenAI 子处理，对数据驻留敏感的组织（欧盟、受监管行业）需要主动关掉 OpenAI；官方没有给出两种路径的具体差异，判断成本落在管理员身上。初期只对美国客户开放（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})），这一问题在美国以外开放前可能不突出。

## 存放、删除与导出

| 数据 | 位置与处理 | 来源 |
| --- | --- | --- |
| 记忆、会话 | 用户 OneDrive 中的 lobster.repo（Git 仓库，含历史） | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 交付物、个人工作 | 用户 OneDrive；任务临时文件完成后不保留 | [Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}}) |
| 用户导出 | JSON 存到 OneDrive，或用脚本下载完整副本；导出是快照，可能不带敏感度标签 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 管理员导出 | 为已批准的合规或隐私请求导出用户 lobster.repo；须记参考编号，用管理员自己的账户临时获取该用户 OneDrive 访问并记入审计日志，脚本「绝不会使用用户的凭据」 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |

删除的口径（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）：

- 删除会话后底层记录保留，直到用户让 Autopilot 永久删除。
- 报告「已移除」不证明受保留策略管理的记录、备份或所有副本都已抹除；正式的访问、保留、删除答复须走组织的数据管理流程。
- 「我的账户」隐私页不删除 Autopilot 数据；管理员不能代用户删除；批量删除、离职用户删除和经核验的删除要联系微软支持。

## 合规覆盖的缺口

消息中心通告列出：记忆始终开启，Microsoft 365 Copilot 的个性化设置不适用；数据保护与审计能力有预览限制；「Autopilot 对话尚未纳入 eDiscovery、保留或法律保留的覆盖范围」（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})）。FAQ 与使用页称 Autopilot 识别受支持内容上的敏感度标签，但带标签的邮件和文件不被排除在可读范围外，新文件可能不继承标签；提示词 DLP 在预览期受限（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。安全侧的对应内容见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})。

## 他人的信息

Teams 群聊里 Autopilot 发的消息所有人可见，已发布的回复对能看到讨论串的人可见；审批卡把外部收件人标为「外部」（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。首次设置读取过去 30 天用户可访问的邮件、会议、聊天和文件（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})），其中自然包括同事发来的内容。资料没有讨论对同事或外部联系人信息的专门处理。

发布前的官方对谈已点出难点：「如果我把我的智能体派给你，它不应该告诉你关于我的一切」（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。社区作者 2026-11-04 指出，不能假定 EU Data Boundary 覆盖这类智能体的模型调用（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 资料缺口

- OpenAI 子处理时的数据保存期限、处理地点；与 Azure OpenAI 承诺的具体差异。
- 美国以外地区的开放计划与数据驻留说明。
- eDiscovery、保留、法律保留覆盖 Autopilot 的时间表。
- 30 天初始熟悉中同事和外部联系人信息的处理。

## 主要资料

- 官方：[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})（OpenAI 子处理、EU Data Boundary、训练、管理员导出）；[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})（存放与删除）；[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})（合规覆盖缺口、标签）；[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})；[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})。
- 社区：[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})。
