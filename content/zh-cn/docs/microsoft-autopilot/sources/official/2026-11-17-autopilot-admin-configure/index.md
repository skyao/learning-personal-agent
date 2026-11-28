---
title: "为组织配置 Autopilot（Frontier）"
linkTitle: "文档：管理员配置"
date: 2026-11-17
originalTitle: "Configure Autopilot (Frontier) for your organization"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
tags: [开放与价格, 安全, 隐私, 模型]
products: [microsoft-autopilot]
updatedAt: "2026-11-17"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-17。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。待翻译。

**内容摘要**：面向管理员的配置文档：Autopilot 默认关闭，需让用户加入 Frontier、建立覆盖 Autopilot 的支出策略（按 Copilot Credits 计费），并在 Microsoft 365 管理中心激活 Autopilot (Frontier) 代理；每个启用用户可创建一个 Autopilot，初期仅限美国的合格客户。文档说明自动审查系统（第二个 AI 模型）按动作类型决定放行或需用户批准，付款与敏感浏览器步骤始终需批准。模型为 OpenAI 作为 Microsoft 子处理方提供的 GPT-6.1 Sol，关闭 OpenAI 后改用 Azure OpenAI 托管的 GPT-5.6 Sol。另列出记忆无法关闭、合规覆盖现状（eDiscovery、保留、法律保留不覆盖 Autopilot 会话；提示词 DLP 仍在部分租户测试），以及管理员用脚本导出用户 lobster.repo 的步骤。

**保留理由**：首次给出云端 Autopilot 的管理员视角：激活向导、支出策略、实例管理、合规缺口和数据导出，旧 Scout 文档（Intune 部署桌面应用）与 MC1479277 都没有覆盖这些细节，也首次写明模型型号与回退模型。
