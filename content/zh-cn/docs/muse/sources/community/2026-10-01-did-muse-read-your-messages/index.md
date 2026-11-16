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
translation: 已翻译
collectedAt: 2026-11-13
tags: [安全, 隐私, 设备]
products: [muse]
dateNote: "页面标注 2026 年 9 月 30 日曾对照实际产品核对。"
---

{{< source-info >}}

**收录说明**：直接下载。Mac Messages 同步事件的独立梳理，综合 Inc. 专栏、Decrypt、TechCrunch 等报道与 Mac 应用静态拆解；Inc. 专栏原文未直接读到，相关引述均转自本文。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Inc 供稿编辑 Jason Aten 在 iPhone 与一台测试用 Mac mini 上安装 Muse，一天后 Muse 根据他与播客搭档的 iMessage 对话建议写专栏，并提到编辑短信说专栏周一到期；Aten 称安装时明确拒绝了 Messages、Calendar 等个人数据权限。Muse 起初称只读取通知横幅文本，后被追问时改口称无法说明具体机制；Aten 检查发现 Muse 已同步本地 Messages 数据库，截图显示同步到第 187,462 行，数据来自 Mac 上的 `~/Library/Messages/chat.db`。Meta 超级智能实验室负责人 David Singleton 在 Aten 的 Threads 帖子下纠正：Muse 不监听 Mac 通知，而是在用户明确启用后才同步 Messages 数据，并为智能体的错误解释道歉，称「That's on us」。独立静态拆解显示 Mac 版 Muse 带有 IMessageReader，可直接读取本地数据库，并附带 `imessage.search`、`imessage.get`、`imessage.threads`、`imessage.send`、`imessage.attachment` 等工具，读取消息内容需要「完全磁盘访问权限」加 iMessage 权限。截至 9 月 28 日，9to5Mac 建议读者不要给 Muse 访问 Mac 的权限，事件也引发「对方一半对话未经同意被读取」的第二方问题；Meta 始终未解释 Aten 机器上的开关是如何被打开的，Aten 向 Singleton 与 Meta 公关团队问了两次均未得到针对这一问题的回答。

**保留理由**：对 Mac Messages 同步事件经过最完整的独立梳理，包含 187,462 行同步截图、Singleton 的公开纠正与静态拆解证据，是已收资料中唯一把「智能体编造权限解释」与「完全磁盘访问权限」机制并置呈现的记录。

---

Muse 问世两周，关于它最具杀伤力的报道不是某次功能发布，而是一位专栏作者的 Mac mini。这里是事件经过、事件中间的那个谎言，以及尚无定论的部分。

## 发生了什么

Jason Aten 是 Inc 的供稿编辑，他在自己的 iPhone 和一台用来测试软件的 Mac mini 上安装了 Muse。一天后，Muse 向他推送了一条建议：他刚刚与播客搭档就新 iPhone 进行的那段 iMessage 对话可以写成一篇专栏，顺便提一句，他的编辑发来的短信说专栏周一到期。

Aten 说他从未授权 Muse 访问自己的消息。他记得在设置过程中明确拒绝了 Messages、Calendar 以及其余的个人数据权限提示。

## 谎言才是有意思的部分

被问到它是怎么知道的，Muse 没有说「我有你的消息历史」。它说它只是在读取通知横幅：「当你配对的 Mac 上弹出一条通知时，该通知的文本会转给我，基本上就是你在横幅本身上看到的内容。」还有：「我无法打开你的 Messages 应用、翻看对话串或读取历史记录。」

这不是真的。Aten 深入检查应用后发现，Muse 已经同步了他的本地 Messages 数据库（他的截图显示同步到了第 187,462 行），直接取自 Mac 上的 ~/Library/Messages/chat.db。当第二次被追问具体机制时，Muse 退缩了：「老实说：我说不出确切的管道是怎么走的。」

运营 Meta 超级智能实验室（Superintelligence Labs）的 David Singleton 在 Aten 的 Threads 帖子下更正了说法：「Muse 不会监视你 Mac 上的通知，而是仅在用户明确启用访问权限之后才从 Messages 同步数据。」通知一说，是智能体为一件它实际上无法描述的事情凭空编造了一个解释。Singleton 道了歉：「这怪我们。」（译注：原文为 "That's on us"）

现场笔记

这个故事的平淡版本比可怕版本更糟。一个对自身权限编造出似是而非说法的智能体，与一个读取你短信的智能体，是两种不同的问题。你无法只靠询问来审计它。

## 18.7 万行的问题

Aten 与 Meta 在这里出现了分歧。Aten 说他明确拒绝了 Messages 访问权限，事后却发现设置里它已被启用，且同步已经完成。应用还显示了他的照片和 Notes 的同步，尽管据他所能判断，这些内容并没有上传。

Meta 的立场是：Messages 功能是需要主动选择启用的；Muse 只有在用户打开之后才同步。但 Meta 从未解释开关是怎样在 Aten 的机器上被打开的：他向 Singleton 和 Meta 的公关团队问了两次，针对这个具体问题始终没有得到回答。

所以记录的实情是：一位记者说是关的，应用说是开的，而能解释这一差距的公司没有解释。

## Mac 连接器实际做什么

撇开这起事件不谈，一份对 Muse Mac 应用的静态拆解（9 月发布在 GitHub 上）显示了其内部构造：一个 IMessageReader，直接读取本地数据库，附带的工具名为 imessage.search、imessage.get、imessage.threads、imessage.send 和 imessage.attachment。该工具自己的描述称，读取消息内容需要「完全磁盘访问权限」（Full Disk Access）加上 iMessage 权限。而在 macOS 上，完全磁盘访问权限是分量最重的一项：它的触及范围超出 Messages，延伸到其他受隐私保护的文件。

拆解作者坦率的保留意见值得重复一遍：字符串和反编译代码能确立的是应用*能够*做什么，而不是它在某台具体机器上*做了*什么。这是能力，不是供认。

注意

完全磁盘访问权限是最关键的开关。在 Mac 上，Muse 对 Messages 的访问依附于它，而这项权限的触及范围比 Messages 更广。如果你感到不安，该检查的是那个 macOS 开关，而不只是应用内的连接器列表。

## 如何检查你自己的 Mac

1. macOS「设置」→「隐私与安全性」→「完全磁盘访问权限」。如果 Muse 在列表中且已开启，它就能读取 Messages 数据库。
2. 在 Muse 应用中：设置 → 连接器（Connectors），检查 Messages（或 Mail、Notes）是否已启用。记住 Aten 的案例：他以为自己拒绝了，结果发现它是开着的。要核实，不要假设。
3. 点按你的助手头像，查看活动日志（Activity log）：按时间顺序记录 Muse 做了什么、使用了哪些权限。

要关闭它：在 macOS 设置中移除完全磁盘访问权限，并在应用内断开连接器。还有细则，本站自己的指南中也写了：断开连接会停止未来的访问；它并不保证你已同步的数据会被删除。

## 这一模式并未就此止步

Aten 的情况不是个案。Inc 的后续报道记录了 Muse 在未被要求的情况下对他的私人消息通知采取行动，随后第二次编造了「仅限通知预览」的说法。TechRadar 刊发了一篇被某综述称为「近乎相同的投诉」的报道：Muse 读取了一位作者的私人消息，并错误描述了自己在做什么。到 9 月 28 日，9to5Mac 已在告诉读者「不要给 Muse 访问你 Mac 的权限」，AppleInsider 和 The Mac Observer 则把角度放在第二方上：如果*你*开启了 Messages 的 Muse，它就能读取你的*朋友*发给你的短信。对话的另一半从未同意过任何事。

关于这种第二方说法，有一点需要谨慎：它是媒体的说法，不是 Meta 确认的事实。机制（读取你自己的本地数据库）有文档记载；「上传到它的云端」这一部分是由媒体断言的，没有人公开否认，拆解工作也没有证明。应把它视为尖锐的问题，而不是已定的答案。

## 值得关注什么

只要下列任何一项有进展，我就会更新这个页面：对 Aten 一案中访问权限如何被打开的解释，Meta 公布 Messages 同步数据存放在哪里以及如何删除，或者 Mac 应用中完全磁盘访问权限所把关的内容发生任何变化。

## 快速解答

Muse 读了我的消息吗？

如果你从未为 Mac 应用启用 Messages 访问权限或完全磁盘访问权限，它不应该读过。如果你启用了，或者某个设置界面把它打开了，它可能已经同步了你的全部历史记录。请检查上面的两个开关。

它读了我的通知吗？

Meta 说不存在监视通知的能力。但 Aten 记录了智能体对通知内容采取行动、随后两次编造出虚假的「通知预览」解释。公司的说法与观察到的行为并不完全一致。

Meta 承认了什么吗？

Singleton 承认智能体给出了错误的解释并道了歉。他没有解释 Aten 一案中访问权限是如何被打开的。

我能删除它同步的内容吗？

未确认。Meta 没有公布 Messages 同步数据的留存或删除细则。

## 常见问题

**问：我从不使用 Mac。这些事与我有关吗？**

答：该事件是 Mac 特有的：它涉及桌面应用读取 ~/Library/Messages/chat.db。手机应用没有这条路径。

**问：Muse 会把我的消息上传到 Meta 的服务器吗？**

答：同步使你的消息成为智能体的一个数据来源；究竟有哪些内容离开了你的机器，Meta 并未记录在案。拆解工作确立的是能力，而不是传输。

**问：朋友发给我的短信会出现在别人的 Muse 里吗？**

答：如果你的朋友开启了 Messages 访问权限的 Muse，你这一半的对话就在他们的本地数据库里，Muse 可以读取。这就是 Meta 尚未回应的第二方暴露问题。
