---
title: "Muse 学会说话了，它的脸比声音做了更多工作"
linkTitle: "语音化身设计分析"
date: 2026-11-18
originalTitle: "Muse Learned to Talk. Its Face Is Doing More Work Than Its Voice."
sourceUrl: "https://aihomebuilding.com/stories/muse-voice-mode-2026"
author: "Elena Vasquez"
publisher: "AI Home Building"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-18
tags: [功能更新, 安全, 隐私]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载后用 extract.py 抽取全文；首图为装饰性照片，未收入。作者声明未亲自使用语音功能，结论来自 Meta 官方公告、9 月 23 日研究文章与当日报道；文中 GPU 并发算术为作者按公开数字所做的估算，非 Meta 公布数字。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Meta 于 11 月 5 日在美国上线 Muse 实时语音与表情化身：点应用右上角电话图标即可通话，可随时打断对方，化身随对话语气做出表情与手势；语音只听不见看——Muse 听得到用户说话，但看不到用户。技术来自 9 月 23 日研究文章介绍的 Muse Realtime Voice 与 Realtime Avatar：教师模型每视频块需 120 次模型评估，蒸馏后的学生模型只需 2 次；延迟约 870 毫秒，视频为 448×768、25fps，带 Meta Video Seal 水印；作者按公开数字估算，量化后一块 Nvidia GB200 可跑 12 路并发化身会话。作者指出三处官方未说明之处：语音模式下如何完成发送与消费前的审批、语音音频是否保存及是否用于训练、语音何时扩展到美国以外；并认为非人形 furry 化身的设计与纽约州与加州关于拟人化聊天机器人的法律有关。

**保留理由**：对语音与化身功能做了已收官方公告与报道之外的独立技术与设计分析，给出 870 毫秒延迟、GB200 并发估算、审批与录音政策缺口、非人形化身的法律解读，是已收资料中没有的分析角度；作者明确标注了未实测与估算性质。
