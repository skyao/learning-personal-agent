---
title: "请 Muse 与我「交换家门钥匙」，当一名 Zaurus 开发者"
linkTitle: "Muse 当 Zaurus 开发者"
date: 2026-11-19
originalTitle: "Museに「僕と“家の鍵”を交換してザウルス開発者になってよ」と頼んでみた"
sourceUrl: "https://pc.watch.impress.co.jp/docs/topic/feature/2157654.html"
author: "劉 尭"
publisher: "PC Watch"
language: ja
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-21
tags: [设备, 实测评测]
products: [muse]
dateNote: "页面 article:published_time 为 2026-11-19T06:08:00+09:00，同日 12:25 更新。"
---

{{< source-info >}}

**收录说明**：直接下载；以 article 容器抽取；删去文末亚马逊推广区块；配图已本地化，截图无替代文本。

**内容摘要**：作者用剩余的 Muse token 做实验，请 Muse 把开发工作搬进自己的电脑：Muse 主动提议用 Tailscale 加 SSH「交换家门钥匙」，从云端虚拟机进入作者 12 核 64GB 的家用电脑，再经 Telnet 进入 2005 年的 Linux Zaurus SL-C1000。Muse 自行写代码、构建、在真机上运行、回传帧缓冲截图自查、再修改，约 30 分钟做出演示、约 3 小时完成 FM 合成器软件；在 2019 年的 Jetson Nano 开发板上部署小型语言模型时反复修改尝试 17 次才成功，途中也曾把收尾交给作者更熟练的 Claude Code。中途两次构建停滞而 Muse 未察觉，作者用 CPU 使用率发现问题并做了看门狗批处理。文末列出家庭网络的安全注意事项：用 Tailscale 的访问控制收窄可进入的机器、用访客网络隔离、给 Muse 建专用 SSH 用户、用完断开 Telnet。

**保留理由**：日本媒体对 Muse 的一手长篇实测：把智能体接入家庭内网真机做开发的完整过程，含具体耗时、失败与人工兜底，是已收资料中少有的「智能体进入用户自有硬件」的实地记录。
