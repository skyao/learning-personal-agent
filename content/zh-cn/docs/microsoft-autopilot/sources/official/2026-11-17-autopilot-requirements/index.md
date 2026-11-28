---
title: "Autopilot（Frontier）要求"
linkTitle: "文档：使用要求"
date: 2026-11-17
originalTitle: "Autopilot (Frontier) requirements"
sourceUrl: "https://learn.microsoft.com/en-us/copilot/autopilot/requirements"
altUrls: []
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
tags: [开放与价格, 运行环境, 安全]
products: [microsoft-autopilot]
updatedAt: "2026-11-17"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-11-17。Autopilot 文档集在 Ignite（2026-11-17）前后首次出现，与旧的 Microsoft Scout 文档集（learn.microsoft.com/en-us/microsoft-scout/）并存"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（新的 Autopilot（Frontier）文档集，页面标为预览功能），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。待翻译。

**内容摘要**：列出在 Microsoft Copilot 中使用 Autopilot 的前提：无需在设备上单独安装代理，默认关闭；责任人须有 Microsoft 365 Copilot 许可证并开启消费计费，需由支出策略覆盖，Copilot 许可证不含 Autopilot 用量，每个启用用户可创建一个 Autopilot。必需的安全能力为 Microsoft Entra Agent ID（自动预配）、Microsoft local (MXC) 隔离执行环境（需 Intune Plan 1 或 Microsoft 365 E3）和 Microsoft 365 审计日志；另有强烈建议与有限预览的能力。可用性初期限于美国的部分 Frontier 客户，针对英语优化，且文档称 Autopilot 的云端计算机与本地设备分离，不应把早期桌面预览的说明当作云端体验的设置要求。

**保留理由**：给出云端 Autopilot 的许可证、计费与安全能力前提清单，并明确区别于早期桌面预览，与 MC1479277 的 UBB 前提和旧 Scout 的 Intune、GitHub Copilot 许可证要求相比，新增了 Entra Agent ID、MXC 等必需安全能力和美国限定。
