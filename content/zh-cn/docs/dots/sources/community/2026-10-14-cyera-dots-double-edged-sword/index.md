---
title: "dots：职场中的一把双刃剑"
linkTitle: "Cyera：dots 的安全风险"
date: 2026-10-14
originalTitle: "Dots: A Double-Edged Sword in the Workplace"
sourceUrl: "https://www.cyera.com/research/dots-a-double-edged-sword-in-the-workplace"
author: "Yaakov (Fufu) Shpigelman"
publisher: "Cyera Research"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-06
dateNote: "页面显示日期为 2026-10-14；结构化数据 datePublished 为 2026-10-19"
tags: [安全, 运行环境, 连接器]
products: [dots]
---

{{< source-info >}}

**收录说明**：数据安全公司 Cyera 研究团队的文章，归入社区。直接下载，图片收入 images/；文末的目录、相关文章与分享按钮未收。旧笔记 learning-ai-agent 引用过这一篇，2026-11-06 复核后收入。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：作者实际使用了一个 dot，借一个很薄的借口向它索要敏感数据，它没有交出所有者权限以外的内容，但省去了翻找共享盘的工夫。dot 列出的工具约 270 个，涵盖命令行、浏览器、Gmail、Google Drive、Slack、GitHub（近 90 个，包括合并 PR 和开启自动合并）和网站托管，还有修改自身 Custom Rules 的工具，实测改规则时会请求批准。云端电脑是 Debian 13 与 XFCE 桌面，模型以无特权用户 `agent` 运行，容器套在 Kata 虚拟机里，上层还有 bubblewrap 沙箱，出站流量经 HTTP 代理。作者引用 GPT-6 Astra 系统卡中 8.5% 的提示注入成功率和可监控性下降的表述，提醒 dot 能主动给用户发消息却不展示推理，可能被用来做钓鱼，并给出个人和管理员的防护建议。

**保留理由**：独立研究者对 dots 的一手检查，给出了工具清单和云端电脑隔离层次，这些是官方文档没有写的实现细节。
