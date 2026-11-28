---
title: "dots 的安全与防护"
linkTitle: "文档：企业安全指南"
date: 2026-11-05
originalTitle: "Safety and security in dots"
sourceUrl: "https://learn.chatgpt.com/docs/enterprise/dots-security"
altUrls: ["https://learn.chatgpt.com/codex/enterprise/dots-security"]
publisher: "OpenAI（ChatGPT Learn）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
dateNote: "文档不标日期；按规则取收集日期。文中评估数据引自 2026-10-26 的 GPT-6.1 Terra 系统卡附录；2026-11-28 发现原文更新：旧版「OpenAI 如何评估模型安全防护」整节（GPT-6 系列各模型的提示注入、越狱、欺骗评估图表）已删去；数据存储驻留加入阿联酋（推理驻留仍不含），并说明测试期创建的 dots 会在正式可用日（2026-11-04）后 30 天内迁移到工作区指定区域；Microsoft Teams 全部删去；新增 Wallet 付款须成员逐笔生物识别批准的说明"
tags: [安全, 隐私, 商业与规模]
products: [dots]
---

{{< source-info >}}

**收录说明**：OpenAI 在 ChatGPT Learn 上发布的 dots 文档，文档不标日期，页面日期取第一轮收集日期 2026-11-05。第一轮收集时直接翻译，原文未单独存档；2026-11-28 按新流程重新抓取（直接下载），原文存于本目录的 original.md（网站上不显示）：7 处结构示意图和设置界面示意（设置开关、权限地图、dots 架构、登录表单、主动研究、自动审查、云端计算机开关）整理为「（界面示意：……）」段落，并去掉抽取后重复出现的方框文字；删去头像图；页内相对链接改为绝对地址。新版有新增和改写，旧译文已删去（由 git 保留），待翻译。

**内容摘要**：这是面向管理员和安全团队的 dots 安全指南：个人 dot 只能由所有者指挥，只能使用所有者已授权的应用连接，数据默认不用于训练。云端计算机的浏览器、网络和计算机操作可以分别开关，另有自动审查、安全监控和活动视图；本地电脑访问要管理员另行开启，委派任务按 Agent Security 策略执行。文中列出数据驻留（存储驻留含阿联酋，推理驻留只有美国和欧洲）、EKM、HIPAA，并说明不提供零数据保留、不适用 FedRAMP。使用 Wallet 时，即使管理员开启且成员给过长期指示，每笔付款仍须成员用生物识别批准。另有保留与删除表、用 Compliance API 的 `client_id = DOTS` 追踪记录的方法，以及成员离职的处理流程。

**保留理由**：这是 dots 在企业侧的数据边界、控制层次与审计方法的官方说明；新旧版对照可以看出模型评估数据被撤下、Wallet 与阿联酋驻留加入。
