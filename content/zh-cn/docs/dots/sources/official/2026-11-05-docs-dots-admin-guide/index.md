---
title: "管理 dots 的权限和能力"
linkTitle: "文档：企业管理指南"
date: 2026-11-05
originalTitle: "Manage dots permissions and capabilities"
sourceUrl: "https://learn.chatgpt.com/docs/enterprise/dots-admin-guide"
altUrls: ["https://learn.chatgpt.com/codex/enterprise/dots-admin-guide"]
publisher: "OpenAI（ChatGPT Learn）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
dateNote: "文档不标日期；按规则取收集日期；2026-11-28 发现原文更新：新增「Enterprise preview and billing」一节（预览期按角色启用，2026-11-18 起成员默认可用，除非工作区选择退出；预览免费，委派给 Work 或 Codex 的任务按标准费率计费）；权限步骤与控制表新增 Wallet（企业工作区默认关闭）；Microsoft Teams 全部删去"
tags: [开放与价格, 安全, 商业与规模]
products: [dots]
---

{{< source-info >}}

**收录说明**：OpenAI 在 ChatGPT Learn 上发布的 dots 文档，文档不标日期，页面日期取第一轮收集日期 2026-11-05。第一轮收集时直接翻译，原文未单独存档；2026-11-28 按新流程重新抓取（直接下载），原文存于本目录的 original.md（网站上不显示）：页内相对链接改为绝对地址，没有其他需要清理的网页元素。新版有新增和改写，旧译文已删去（由 git 保留），待翻译。

**内容摘要**：这一页面向工作区所有者，说明如何配置和管理 dots。预览期管理员可以为选定角色启用 dots，2026-11-18 起成员默认可用，除非工作区选择退出；预览本身免费，dot 委派给 Work 或 Codex 的任务按标准费率另计。设置步骤包括在自定义角色中开通「使用 dots」、Slack 参与、本地电脑访问、云端计算机能力和 Wallet，Wallet 在企业工作区默认关闭。只要有一个角色授予了访问，关闭另一个角色不会移除访问。管理员可以在 Admin Console 查看、暂停、恢复、删除 dots，用量看 Analytics API，记录用 Compliance API 的 `client_id = DOTS` 查询。

**保留理由**：这是 dots 在企业工作区中如何授权、如何计费、记录到哪里查的官方说明；新版加入了默认开启日期、预览计费和 Wallet 开关。
