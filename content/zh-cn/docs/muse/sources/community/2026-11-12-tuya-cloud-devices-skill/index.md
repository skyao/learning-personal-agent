---
title: "Tuya 发布开源 Skill，让 Muse 控制家中智能设备"
linkTitle: "Tuya 智能家居 Skill"
date: 2026-11-12
originalTitle: "Tuya Releases Open-Source Skill Enabling Meta Muse to Control Smart Devices Across 3,000+ Categories"
sourceUrl: "https://www.prnewswire.com/news-releases/tuya-releases-open-source-skill-enabling-meta-muse-to-control-smart-devices-across-3-000-categories-302937689.html"
author: "Tuya Smart"
publisher: "Tuya Smart"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-12
tags: [设备, 连接器]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载 PR Newswire 上的 Tuya 新闻稿全文。删去了页面导航、分享按钮、追踪像素与文末弹窗标题；配图一张已本地化。文中称 Muse 目前仅面向美国与加拿大用户，与 10 月 23 日日本、10 月 27 日新加坡、11 月 5 日墨西哥上线不符，照录原文。本轮核查 GitHub：该 Skill 已于 2026-11-10 以 PR #61（Add Tuya cloud devices skill）合并进 Meta 的 muse-gadget-sdk 仓库（skills/gadget-tuya-cloud-devices/），与个别二手报道所称“仍在审核”不符；新闻稿内链的 Tuya 官方仓库 tuya-openclaw-skills/platforms/muse 为同一 Skill 的另一份副本。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：2026 年 11 月 12 日，Tuya Smart 宣布发布 Tuya Cloud Devices，这是一个官方开源 Skill，让 Meta 的个人 AI 助手 Muse 能用自然语言查询和控制用户 Tuya 账号下的智能设备，通过 Tuya 云端工作，无需本地设备密钥、同网连接或固件改动。该 Skill 名为 gadget-tuya-cloud-devices，由 Tuya 官方开源 AI Skill tuya-smart-control 改编而来，以遵循 Muse Gadgets 规范的纯 Markdown 文件写成；它只需一个在 tuya.ai 免费申请的 API 密钥（以“sk-”开头），可自动从七个数据中心中选择正确接口，发送指令前先读取设备的标准化 Thing Model 以确认读写权限、取值范围与步长。通过该 Skill，Muse 可执行设备开关与状态查询、家庭与房间管理、条件变化通知（短信、语音电话、邮件或应用推送）、摄像头拍照及最长 60 秒的视频回传，以及基于设备属性变化和上下线事件的实时自动化；安全规则包括多设备匹配时列出房间请用户确认、设备离线时只报告状态不下发指令、发令后 1–2 秒回读确认、事件通知间隔至少 30 分钟，且不开放门锁控制、实时视频、固件升级等操作。新闻稿称 Tuya 平台覆盖 3,000+ 智能硬件品类、服务 200+ 国家和地区，截至 2026 年 6 月 30 日注册 AI 开发者超过 209 万；该 Skill 最初为开源助手 OpenClaw 构建，后适配 Muse 规范，Muse 目前面向美国和加拿大用户。

**保留理由**：这是首个大型智能家居平台为 Muse 发布的 Gadgets Skill，把 Muse 的控制范围从 Meta 官方 Gadgets 开源项目覆盖的自制附加设备、以及 Expedia 等服务类连接器，扩展到了用户家中已有的量产联网设备；它还首次在本资料库中记录了“一个 Skill、一个 API 密钥”加 Thing Model 的云端接入方式及其安全边界细节。
