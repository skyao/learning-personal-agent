---
title: "我花 50 美元自制了一个 Muse Charm"
linkTitle: "50 美元自制 Muse Charm"
date: 2026-10-31
originalTitle: "I built an AI Tamagotchi before Meta could"
sourceUrl: "https://www.theverge.com/gadgets/1013375/muse-charm-gadgets-preview-waveshare-esp32-claude-vibe-code"
author: "Sean Hollister"
publisher: "The Verge"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-08
tags: [设备, 实测评测]
dateNote: "发表日期 2026-10-31 在本轮检索窗口之外，本轮经 allthingsmuse 周记线索发现。"
---

{{< source-info >}}

**收录说明**：直接下载。去掉了页首话题标签、作者栏与文末「Related」栏目、推荐与广告；文中的嵌入视频未在静态页面中找到地址，未收录；五张作者实拍图已本地化到 images/。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：作者花 50 美元买了一块 1.75 英寸触屏开发板 Waveshare ESP32-S3 1.75C，自制 Muse Charm 平替；这款开发板是 Meta 官方推荐的 Muse Gadget 搭建方案之一，使用 Meta 的开源代码与令牌直连 Muse 云端。初始安装后设备基本不可用：Muse 会把语音当作待转录的音频片段而非指令，回复缓慢且不出声，屏幕一次只显示几个词，Meta 自带版本只有一个 Jolly 形象，也不会自动发现智能家居设备。经过几轮 Claude Code 改造，作者补上了对话历史页、ElevenLabs 英式语音朗读、远程拍照快门与蓝牙低清取景，还做了多个 Meta Connect 风格的形象和带饥饿、无聊、肮脏四档状态的电子宠物小游戏，以及真正走时的三针怀表表盘（耗时 15 分钟）。作者自述没有编程经验，也不知道这些代码质量如何，并表示不信任 Meta 或 Muse 接触自己的邮箱与家庭网络，因此把设备放在访客 Wi-Fi 上；他最后认为，专用硬件的意义在于做手机做不到的事，而不是 Muse 本身。

**保留理由**：这是一手实测，记录了 Muse Gadgets 官方示例开箱即用的实际短板（转录误判、无语音回复、单形象、无智能家居发现），以及用 Claude Code 逐项补齐的过程与具体改动，是官方文档之外的真实可用性证据。
