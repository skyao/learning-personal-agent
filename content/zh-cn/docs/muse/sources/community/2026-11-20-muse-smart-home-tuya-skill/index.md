---
title: "Muse 终于能调灯了，但要借别人的钥匙"
linkTitle: "智能家居接入"
date: 2026-11-20
originalTitle: "Muse Can Finally Dim Your Lights. It Just Has to Borrow Someone Else's Key to Do It."
sourceUrl: "https://aihomebuilding.com/stories/muse-smart-home-tuya-skill-2026"
author: "Jake Kowalski"
publisher: "AI Home Building"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-20
tags: [设备, 连接器]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载。首图为装饰性配图，未收录。作者在文末声明未做一手实测，技能行为（1–2 秒回读、30 分钟通知间隔）据涂鸦发布材料与 Unite.AI 的仓库解读，PR #61 状态发表时未重新核对；文中称 PR #61 仍未合并，与本库 11-12 轮次的核查（PR #61 已于 11-10 合并进 Meta 的 muse-gadget-sdk 仓库）不符，照录原文。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：上线六周后，Muse 仍无法直接控制家中的智能设备；作者先回顾对手：苹果 9 月 14 日随 iOS 27 推出带完整 HomeKit 控制的 Siri AI，两天后谷歌推出 Google Home MCP，到 9 月 27 日 Forkast 专栏已称 Muse 是唯一完全碰不到家居的大型智能体。Meta 于 10 月 2 日发布开源的 Muse Gadgets SDK，同期推出自家 USB-C 配件 Home Link，据 The Verge 报道仅生产 5000 台、凭有效订阅免费候补、仅限美国、每人一台，而 Muse 用户已超 1000 万。11 月 12 日涂鸦智能发布开源技能 gadget-tuya-cloud-devices，让 Muse 能用自然语言查询与控制涂鸦云上的设备：从 GitHub 取技能文件、在 tuya.ai 申请免费 API 密钥并交给 Muse 即可，已有账号约需 10 分钟；技能先读设备的 Thing Model 再下发命令，执行后 1–2 秒回读状态、确认后才告知用户成功，多设备匹配时请用户确认、设备离线时不下命令，事件通知间隔至少 30 分钟。文章数出三扇门——无内置支持、Home Link、Tuya 技能——并指出后者走试用阶段 API、有调用限额，其上游 PR #61 仍在审核；「3000+ 品类」是涂鸦平台的规模，并非 Muse 能控制的设备数。技能不开放门锁、实时视频、固件升级、网络配置与设备移除，实时触发需另配运行 Muse Gadgets Linux SDK 的常驻设备；作者在文末声明未做一手实测，技能行为据涂鸦发布材料与 Unite.AI 的仓库解读，PR #61 状态发表时未重新核对。

**保留理由**：这是资料库中第一篇系统梳理 Muse 智能家居接入路径的独立分析，把 Gadgets SDK、Home Link 与 Tuya 技能三条路线并列核对，并点出命令后回读确认的闭环设计与「3000+ 品类」数字的口径问题；作者的未实测声明与 PR 状态已在收录说明中限定。
