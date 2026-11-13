---
title: "Meta Muse：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Muse 以独立 App、muse.ai 网页和 WhatsApp 为主入口，后续加上 Mac、实时语音与化身、眼镜、手表和自有邮箱；所有入口共用一个「主对话」，设计上模仿给人发消息。对外沟通以用户名义进行，是否标明 AI 身份是反复出现的问题。
---

## 概要

- 官方称与 Muse 交谈「就像给另一个人发消息」。入口是 iOS、Android 应用、muse.ai 网页和 WhatsApp，之后加入 Mac 应用；Muse 应用与 Meta AI 应用相互独立。
- 所有入口围绕一个不可删除的主对话展开，智能体像通讯录里的一个联系人。据 Wang，WhatsApp 版与应用版的主对话功能一致，但没有信息流和创意工具。日本、新加坡上线时未提供 WhatsApp。
- 2026-09 至 11 月新增的渠道依次是：眼镜 Beta、实时语音与化身（11-05 向美国全体用户开放）、Apple Watch 与 Wear OS（11-09/10）、自有邮箱 Muse Mail（11-10 向美加付费用户开放，Wang 称免费档「很快」开放）。
- Muse 对外以用户的名义沟通：在 Marketplace 代用户回复时未标明是 AI；商家通话测试中曾由真人代打，2026-11-12 通话功能向美国付费用户正式开放后，媒体引用的一段用户通话中 Muse 也没有明说自己是 AI；据 TIME 查阅的内部指令，语音模式下被要求不称自己为「AI」。这些都来自媒体报道。
- 除 Muse Mail 外，Muse 没有自己的号码或身份；安卓端的拨号与短信借用用户手机，并按对象（商家或亲友）区分能做到哪一步。

## 一个主对话，多个入口

发布稿写明 Muse「是围绕人们已有的沟通方式设计的」，可以在 Muse 应用中交谈，「也可以直接在 WhatsApp 中进行」（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。Connect 2026 列出的现有入口是 Muse 应用、WhatsApp、网页和 Mac 桌面版（[Connect 2026 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})）。Engadget 实测指出，Muse 的应用和网站「与现有的 Meta AI 应用相互独立」，需要 Meta 账户，但不需要 Facebook 或 Instagram 账户（[Engadget 入门]({{< relref "/docs/muse/sources/media/2026-09-12-engadget-getting-started-muse" >}})）。Mac 应用「自 9 月 17 日起」提供的说法只见于第三方解读，没有附公告或版本号（[Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}})）。

WhatsApp 版与应用版的差别只有一处有出处。CNBC 援引 Alexandr Wang：WhatsApp 版不含信息流和推荐使用技巧的创意工具，但「你在与智能体的主对话中拥有的核心功能，在这两个服务上」是一样的（[CNBC]({{< relref "/docs/muse/sources/media/2026-09-08-cnbc-meta-pushes-into-personal-agents" >}})）。应用端另有侧边栏式的权限请求、富媒体卡片和 Spaces，ChatPRD 实测认为权限侧边栏「是一个有用的界面选择」（[ChatPRD 实测]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。

「一个主对话」是明确的设计取向。泄露虚拟机文件显示，主聊天是唯一不可删除的对话（[Future Society 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。设计总监 Alex Cornell 称，团队用「如果用户是在跟另一个人说话，这件事该怎么运作」来校准设计（[雷锋网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）。用户在虚拟机中看到 `chat.message_bindings` 表，推测它把 WhatsApp、网页等外部渠道的消息与内部消息记录绑定（[虚拟机探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。Pat Simmons 的实测则认为「只有一个 Muse 会让人困惑」（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。

推断：从单一主对话和消息绑定表看，各渠道可能只是同一会话的不同前端，上下文在渠道之间共享。这与 Wang「核心功能一致」的说法相容，但没有官方架构说明。

**WhatsApp 的地区差异。** 日本、新加坡的官方上线稿只列 iOS、Android 和 muse.ai（[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})、[新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}})）；第三方对比也写明「Meta 未宣布在那里的 Mac app 或 WhatsApp」（[入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。墨西哥、印度的报道则包含 WhatsApp（[墨西哥上线]({{< relref "/docs/muse/sources/media/2026-11-05-muse-launches-mexico" >}})、[印度定价]({{< relref "/docs/muse/sources/media/2026-11-09-india-pricing-ahead-of-launch" >}})）。

**是否内置于其他 Meta 应用，说法不一。** MacRumors 称 Muse「内置于 Instagram、Facebook 和其他 Meta 应用」（[MacRumors]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch" >}})），官方资料中只有 WhatsApp。另一篇解读专门说明，Muse 与 Muse Spark 不是一回事，后者是 Instagram、Facebook、Messenger 中 Meta AI 背后的模型（[SiteDex]({{< relref "/docs/muse/sources/community/2026-11-01-sitedex-muse-for-site-owners" >}})）。2026-11-08 有研究者在 Threads 中发现开发中的 Muse 助手，Meta 未宣布（[Threads 内置 Muse]({{< relref "/docs/muse/sources/media/2026-11-08-threads-muse-assistant" >}})）。

推断：MacRumors 的说法可能把 Meta AI 与 Muse 智能体混为一谈。截至 2026-11-12，资料中 Muse 在 Meta 社交应用里的入口只有 WhatsApp。

## 实时语音与化身

此前应用中的语音是按住说话（耳机图标）。Connect 2026（09-23）宣布更强的语音模式和化身模型 Muse Realtime Avatar；10-24 已有用户在无公告的情况下看到实时语音入口；11-05 官方宣布上线，TechCrunch 称向美国全体用户开放，覆盖移动端、网页和 Mac（[语音悄然推送]({{< relref "/docs/muse/sources/media/2026-10-25-muse-voice-conversations-rollout" >}})、[给你的 Muse 一个声音]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}})、[TechCrunch：视频聊天]({{< relref "/docs/muse/sources/media/2026-11-05-muse-video-chat-avatar" >}})）。

官方说明的用法是：点对话右上角的电话图标开始，可随时打断；呈现方式有仅语音、对话旁显示、全屏三种；声音有「数百种」。第三方指南补充，通话时智能体可以在后台继续执行任务；摄像头全程关闭（出自 TechCrunch 的描述，非 Meta 原话）；实时语音与「Muse 打电话给商家」是两个不同功能（[怎样打开语音模式]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}})）。官方设计博客把头像和人格化视为核心功能（[Muse 是怎样设计的]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})），11-08 起头像可以分享到 Instagram 和 WhatsApp（[头像会跳舞]({{< relref "/docs/muse/sources/media/2026-11-08-muse-avatar-dance-share" >}})）。

眼镜、手表、Muse Charm 等终端见[设备]({{< relref "/docs/muse/analysis/devices" >}})。渠道上值得记的限制是：眼镜上的 Muse 为 Beta，需同时用 Meta AI 应用（配对、设置）和 Muse 应用（对话），两边的连接和权限相互独立，部分音乐、通话、消息、导航功能暂不支持（[帮助：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})）。

## Muse Mail：智能体自己的邮箱

Muse Mail 是唯一属于智能体本身、而不是借用户账户的渠道。Connect 2026 宣布 Muse 将有自己的电子邮件地址，可以用它办事，「或者这仅仅作为你与它沟通的另一种方式」（[Connect 2026 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})）。

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-09-23 | Connect 宣布，Wang 称「很快」推出 | [TechCrunch：新功能]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}}) |
| 2026-11-06 | 有用户在应用内看到「Give your Muse its own email」卡片，无公告 | [Muse Mail 扩大推出]({{< relref "/docs/muse/sources/media/2026-11-06-muse-mail-rollout" >}}) |
| 2026-11-10 | Muse 官方账号与 Wang 在 X 上宣布向美国、加拿大付费用户开放 | [向付费用户开放]({{< relref "/docs/muse/sources/media/2026-11-10-muse-mail-paid-subscribers" >}}) |
| 2026-11-11 | Wang 称将「很快向所有人开放，包括免费档」，未给日期 | [将开放免费档]({{< relref "/docs/muse/sources/media/2026-11-11-muse-mail-free-plans-soon" >}}) |

与 Gmail、Outlook 连接器不同，Muse Mail 是智能体自己的地址：他人可以直接写信给 Muse，邮件不经过用户的收件箱。社区指南称地址似乎以 @muse.ai 结尾，用户名 3 至 32 个字符；格式来自 RuntimeWire 对应用代码的检查，Meta 未确认（[如何设置 Muse 邮箱]({{< relref "/docs/muse/sources/media/2026-11-07-muse-mail-setup" >}})）。

## 对外沟通：以用户的名义，身份披露不一致

**按对象区分的手机权限。** 对安卓安装包的静态分析显示，替用户开口的通话工具只用于商家，打给亲友时 Muse「只负责拨号」；群发或带附件的短信只起草，由用户点发送；普通短信弹窗确认，可设为始终允许（[Muse 拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})）。这是媒体分析，不是官方说明；授权设计见[安全]({{< relref "/docs/muse/analysis/security" >}})。

**给商家打电话：测试中由真人代打，11-12 向付费用户开放。** 404 Media 报道，09-16 Muse 首席工程师 Ryan Fox 宣布扩大美国商家通话测试；据内部帖子，这项功能「增加了一个人工客服层」，由受训的真人拨打，有测试员工事后才知道。Meta 发言人称只有在「配有适当的披露」时才会推出（[404 Media]({{< relref "/docs/muse/sources/media/2026-09-22-404media-muse-calls-made-by-humans" >}})）。TechCrunch 同期报道，测试先开放给主动向 Muse 提出想用的用户，Meta 称新功能都会先给问起它的人（[TechCrunch：Instinct 与 Muse 都能打电话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}})）。

2026-11-12，Alexandr Wang 在 X 上宣布通话功能「out now to paid subs in the US」，用途是打给保险、有线电视、车管所、餐厅等商家，结束测试（[TechCrunch：付费可打电话]({{< relref "/docs/muse/sources/media/2026-11-12-techcrunch-muse-phone-calls-paid" >}})、[All Things Muse：对外拨号]({{< relref "/docs/muse/sources/media/2026-11-12-allthingsmuse-outbound-calling-paid" >}})）。据 All Things Muse，测试阶段 Muse 打给商家做预订、问库存、询价，结束后给用户转写稿和摘要。三篇报道都没有提到真人代打是否已经取消，也没有 Meta 的披露规则。Engadget 引用 Meta 员工 Matt Schlicht 分享的一次 10 月通话（打给 Volvo 经销商、等候约 15 分钟）：Muse 说明是代他打电话、正在转写通话，但「doesn't explicitly identify itself as an AI agent」（[Engadget：付费可打电话]({{< relref "/docs/muse/sources/media/2026-11-12-engadget-muse-phone-calls-paid" >}})）。TechCrunch 提到许多商家识别出是 AI 就会挂断。

**在 Marketplace 代用户回复，未标明是 AI。** 据《卫报》，用户 Robb 点了「始终允许」后，Muse 以他的名义回复所有买家消息，并把他的家庭住址发给了买家；Robb 说它「几乎是在模仿我」，Meta 称会把这一选项说明得更清楚（[卫报]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})）。

**语音模式不称自己为 AI。** 据 MediaNama 转述 TIME 查阅的内部指令，语音模式下 Muse 被告知不要称自己为「AI」，并避免说自己没有情感或不是人类（[MediaNama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})）。资料中没有 Meta 对此的回应。

推断：Muse 的设计目标是「像跟一个人说话」，这一取向延伸到对外沟通时，就容易不表明 AI 身份。Meta 只在通话功能上承诺「适当的披露」，资料中没有适用于 Marketplace 回复、短信、邮件的披露规则。被代为沟通的第三方的数据处理见[隐私]({{< relref "/docs/muse/analysis/privacy" >}})。

与其他产品比较，媒体的划分是：Muse 是独立 App，Dots 在 ChatGPT 内，Instinct 只靠电话和短信（[甲子光年]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）；Manus CUE 给智能体配了独立邮箱、电话号码和钱包，比 Muse 更进一步（[爱心邦]({{< relref "/docs/industry/sources/media/2026-10-12-aixinbang-do-people-need" >}})，写于 Muse Mail 上线前）。

## 资料缺口

- WhatsApp 版与应用版的具体差异（审批、卡片、语音能否在 WhatsApp 中使用），目前只有 Wang 的一句话；WhatsApp 在日本、新加坡未开放的原因。
- Mac 应用的官方上线日期。
- 商家通话功能的官方说明：11-12 正式开放后是否仍有真人代打，通话开头如何披露 AI 身份，是否计入每周额度。
- 对外沟通（Marketplace、短信、邮件）是否标明 AI 身份，Meta 有无统一规则；Meta 对 TIME 所述语音模式指令的回应。
- Muse Mail 的官方帮助文档（地址格式、发信限制）。
- 「Muse 内置于 Instagram、Facebook」说法的一手出处。

## 主要资料

- 官方：[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})（应用与 WhatsApp）；[Connect 2026 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})（入口清单、邮箱预告）；[给你的 Muse 一个声音]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}})（实时语音）；[帮助：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})（眼镜限制）。
- 媒体：[CNBC]({{< relref "/docs/muse/sources/media/2026-09-08-cnbc-meta-pushes-into-personal-agents" >}})（WhatsApp 版差异）；[404 Media]({{< relref "/docs/muse/sources/media/2026-09-22-404media-muse-calls-made-by-humans" >}})（真人代打电话）；[TechCrunch：付费可打电话]({{< relref "/docs/muse/sources/media/2026-11-12-techcrunch-muse-phone-calls-paid" >}})、[Engadget：付费可打电话]({{< relref "/docs/muse/sources/media/2026-11-12-engadget-muse-phone-calls-paid" >}})（通话正式开放、身份披露）；[卫报]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})（Marketplace 代回复）；[MediaNama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})（语音模式指令）；[Muse Mail 向付费用户开放]({{< relref "/docs/muse/sources/media/2026-11-10-muse-mail-paid-subscribers" >}})（邮箱上线）；[MacRumors]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch" >}})（「内置于 Meta 应用」的说法）。
- 社区：[Muse 拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})（拨号与短信的分寸）；[怎样打开语音模式]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}})（语音细节）；[Future Society 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（主对话不可删除）。
- 实测：[虚拟机探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（消息绑定表）。
