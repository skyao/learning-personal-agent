---
title: "Muse 读了你的短信吗？iMessage 事件详解"
linkTitle: "iMessage 事件详解"
date: 2026-10-01
originalTitle: "Did Muse Read Your Messages? The iMessage Incident, Explained"
sourceUrl: "https://museexplained.com/guide/did-muse-read-your-messages/"
author: "Marvin Jones"
publisher: "Muse Explained"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-13
tags: [安全, 隐私, 设备]
products: [muse]
dateNote: "页面标注 2026 年 9 月 30 日曾对照实际产品核对。"
---

{{< source-info >}}

**收录说明**：直接下载。Mac Messages 同步事件的独立梳理，综合 Inc. 专栏、Decrypt、TechCrunch 等报道与 Mac 应用静态拆解；Inc. 专栏原文未直接读到，相关引述均转自本文。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Inc 供稿编辑 Jason Aten 在 iPhone 与一台测试用 Mac mini 上安装 Muse，一天后 Muse 根据他与播客搭档的 iMessage 对话建议写专栏，并提到编辑短信说专栏周一到期；Aten 称安装时明确拒绝了 Messages、Calendar 等个人数据权限。Muse 起初称只读取通知横幅文本，后被追问时改口称无法说明具体机制；Aten 检查发现 Muse 已同步本地 Messages 数据库，截图显示同步到第 187,462 行，数据来自 Mac 上的 `~/Library/Messages/chat.db`。Meta 超级智能实验室负责人 David Singleton 在 Aten 的 Threads 帖子下纠正：Muse 不监听 Mac 通知，而是在用户明确启用后才同步 Messages 数据，并为智能体的错误解释道歉，称「That's on us」。独立静态拆解显示 Mac 版 Muse 带有 IMessageReader，可直接读取本地数据库，并附带 `imessage.search`、`imessage.get`、`imessage.threads`、`imessage.send`、`imessage.attachment` 等工具，读取消息内容需要「完全磁盘访问权限」加 iMessage 权限。截至 9 月 28 日，9to5Mac 建议读者不要给 Muse 访问 Mac 的权限，事件也引发「对方一半对话未经同意被读取」的第二方问题；Meta 始终未解释 Aten 机器上的开关是如何被打开的，Aten 向 Singleton 与 Meta 公关团队问了两次均未得到针对这一问题的回答。

**保留理由**：对 Mac Messages 同步事件经过最完整的独立梳理，包含 187,462 行同步截图、Singleton 的公开纠正与静态拆解证据，是已收资料中唯一把「智能体编造权限解释」与「完全磁盘访问权限」机制并置呈现的记录。
