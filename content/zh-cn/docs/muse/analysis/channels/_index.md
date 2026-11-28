---
title: "Meta Muse：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  所有入口都通向同一个「主对话」，用户和 Muse 说话的方式模仿给人发消息。入口从发布时的 App、网页、WhatsApp 三个，到 11 月底扩展到 Mac、Chrome 扩展、实时语音与化身、自有邮箱、商家电话和 Instagram 私信。Muse 对外沟通有两种身份：用自己的邮箱和电话时是智能体，代发短信、WhatsApp、Messenger 时是用户本人。后一种怎么向对方披露 AI 身份，是本主题最大的问题。
---

## 概要

- **一个智能体，多个入口。** 发布时（2026-09-08）的入口是 Muse App、muse.ai 网页和 WhatsApp，三处共用同一个主对话。到 11 月底，又陆续加上 Mac 应用、Chrome 扩展、实时语音与化身、Muse Mail，以及仅限美国付费用户的商家电话。11-24 起，美、加、墨、日、新五国还可以在 Instagram 私信里使用 Muse。设计上的参照是「给另一个人发消息」。
- **各市场能用的渠道不一样。** 英国稿把 WhatsApp 列为上线渠道，澳大利亚官方稿没有列。日本一开始没有语音、化身和邮箱，邮箱到 11 月中旬才开放。Instagram 私信的五国名单不含英国和澳大利亚。实时语音截至 11-28 只公布了美国的推送。
- **Muse 有了自己对外的身份。** Muse Mail 的 @muse.ai 地址是智能体自己的地址，不连接用户的收件箱，发信前要用户批准。11-10 先向美国、加拿大的付费用户开放，11-20 扩展到所有支持市场，免费档也能用。商家电话的来电显示为 META，社区报告称 Muse 会自报是 AI。
- **代发消息时，Muse 的身份就是用户本人。** 短信、WhatsApp、Messenger、Marketplace 回复以及社交平台发帖，都以用户的号码或账号发出，对方无从分辨。资料里有过 Marketplace 透露住址、群聊代发内容错误等事件。Meta 没有公布群聊消息是否会标明由智能体发送。
- **电话功能的透明度最低。** 单价、次数上限、来电号码、开场白是否每次都说明是 AI、商家能否退出，截至 11-14 都没有官方说明。用户报告的开场白前后不一。早期内部测试曾用真人承包商代打，路透社报道后 Meta 撤下了这种做法。

## 一个主对话，入口逐步增加

官方发布稿称，与 Muse 交谈「如同发消息」，可以在 Muse 应用中进行，「也可以直接在 WhatsApp 中进行」（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。设计总监 Alex Cornell 对雷峰网说，团队用「如果用户是在跟另一个人说话，这件事该怎么运作？」来校准设计；Muse 只有一个主对话，像通讯录里的一个联系人（[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）。复杂话题可以另开侧边对话。英国上线稿写明，App 和 WhatsApp 两个入口的记忆「始终一致」（[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})）。

各入口的出现时间与范围如下（截至 2026-11-28 的资料）：

| 入口 | 时间 | 范围与限制 | 资料 |
| --- | --- | --- | --- |
| iOS、Android App，muse.ai 网页 | 2026-09-08 | 发布时的入口。需要 Meta 账户，不需要 Facebook 或 Instagram 账户 | [推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[Engadget：Muse 上手指南]({{< relref "/docs/muse/sources/media/2026-09-12-engadget-getting-started-muse" >}}) |
| WhatsApp | 2026-09-08 | 核心功能与 App 相同，但没有信息流、创意工具等 App 功能（Wang 对 CNBC 的说法）。BBC 记者称，除了与用户之间的单独聊天，Muse 无法访问 WhatsApp 的内容 | [CNBC：Muse 发布报道]({{< relref "/docs/muse/sources/media/2026-09-08-cnbc-meta-pushes-into-personal-agents" >}})、[BBC 一周试用]({{< relref "/docs/muse/sources/media/2026-11-24-bbc-week-with-muse-uk-launch" >}}) |
| Mac 应用 | 2026-09-17 起 | 需要通知权限，任务完成时提醒用户。截至 11-22 没有 Windows 版 | [Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[帮助：Mac 文件与应用]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})、[ITmedia 入门解说]({{< relref "/docs/muse/sources/media/2026-11-22-itmedia-muse-explainer" >}}) |
| 实时语音与化身 | 2026-11-05 美国 | 在手机、网页和 Mac 上点电话图标开始；见下节 | [语音与表情化身]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}}) |
| Muse Mail | 2026-11-10 付费；11-20 全部 | 智能体自己的 @muse.ai 地址；见下节 | [帮助：Muse 邮箱地址]({{< relref "/docs/muse/sources/official/2026-11-16-help-email-addresses" >}})、[Muse Mail 全面开放]({{< relref "/docs/muse/sources/media/2026-11-21-muse-mail-rolls-out-to-everyone" >}}) |
| 商家电话 | 2026-09-16 Beta；11-12 付费开放 | 仅限美国付费用户拨打美国商家；见下节 | [Muse 对外拨号开放]({{< relref "/docs/muse/sources/media/2026-11-12-allthingsmuse-outbound-calling-paid" >}})、[Muse 电话代打上线]({{< relref "/docs/muse/sources/media/2026-11-12-techcrunch-muse-phone-calls-paid" >}}) |
| Chrome 扩展 | 2026-11 | 在 Chrome 侧边栏打开，快捷键 Alt+Shift+C，需要 Chrome 137 以上；在用户自己的浏览器里、单独的标签组中操作 | [Chrome 扩展正式宣布]({{< relref "/docs/muse/sources/media/2026-11-20-muse-chrome-extension-official-announcement" >}}) |
| Instagram 私信 | 2026-11-24 起陆续推出 | 美、加、墨、日、新五国，iOS 与 Android。私信里的对话会作为侧聊出现在主应用中 | [Muse 进 Instagram 私信]({{< relref "/docs/muse/sources/media/2026-11-24-techcrunch-muse-instagram-dms" >}}) |
| 手表、眼镜 | 11 月 | 属于设备主题，见 [设备]({{< relref "/docs/muse/analysis/devices" >}}) | [Muse 登陆手表核查]({{< relref "/docs/muse/sources/community/2026-11-12-muse-on-apple-watch-wear-os" >}})、[眼镜端 Muse beta 解析]({{< relref "/docs/muse/sources/community/2026-11-09-muse-on-glasses-beta" >}}) |

几个市场的渠道并不相同。澳大利亚官方稿列出 iOS、Android、muse.ai 和 Mac 应用，没有提 WhatsApp（[Muse 上线澳大利亚]({{< relref "/docs/muse/sources/official/2026-11-17-muse-available-australia" >}})）；但 EFTM 的作者在澳大利亚上线前试用了一周，称 WhatsApp 是他「最喜欢的 Muse 差异点」，Muse 会在 WhatsApp 而不是电脑应用里主动给他发消息（[澳大利亚上线实测]({{< relref "/docs/muse/sources/media/2026-11-18-muse-australia-hands-on" >}})）。英国稿把 WhatsApp 列为上线渠道（[英国第七个市场]({{< relref "/docs/muse/sources/media/2026-11-24-muse-launches-uk" >}})）。日本上线时，官方称高级语音、Realtime Avatar 和专属邮箱在日本的提供情况「将另行通知」（[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})）。Instagram 私信的推送名单不含英国，有社区作者 11-25 早上查看自己的日本账号，私信里还没有出现 Muse（[Instagram 私信 Muse]({{< relref "/docs/muse/sources/community/2026-11-25-emma-instagram-dm" >}})、[Muse 英国上线核查]({{< relref "/docs/muse/sources/community/2026-11-25-muse-live-uk" >}})）。

推断：从 9 月的三个入口到 11 月底的八类入口，Muse 的渠道扩张主要分布在两个方向：一是 Meta 自家的应用（WhatsApp、Instagram 私信，以及开发中的 Threads），二是 Meta 不掌控的终端（Mac、Chrome、邮件、电话）。社区作者指出，在 LINE 比 WhatsApp 更强的日本，WhatsApp 入口的优势要打折扣（[Muse 的名字与头像]({{< relref "/docs/muse/sources/community/2026-11-26-emma-muse-identity-name-avatar" >}})）。

## Meta 应用里的入口

Instagram 私信是第一个嵌进 Meta 社交应用私信界面的入口：可以就看到的帖子、地点、商品提问，汇总错过的私信，或把帖子交给 Muse 处理（[Muse 进 Instagram 私信]({{< relref "/docs/muse/sources/media/2026-11-24-techcrunch-muse-instagram-dms" >}})、[Instagram 私信 Muse]({{< relref "/docs/muse/sources/community/2026-11-25-emma-instagram-dm" >}})）。同一批改动还在 Facebook 和 Instagram 的保存、分享界面以及应用内浏览器里加了 Muse 入口；保存帖子时提示交给 Muse 整理，这一功能起初只在美国和加拿大提供（[Muse 跟进广告后行动]({{< relref "/docs/muse/sources/media/2026-11-24-mediapost-muse-post-ad-actions" >}})）。据 CNBC 引述知情人士，约 20% 的 Instagram 日活用户每天至少收藏一篇帖子，其中不少是可购物的商品或广告（[Muse 助推 Instagram 广告]({{< relref "/docs/muse/sources/media/2026-11-24-cnbc-muse-instagram-ad-boost" >}})）。商业层面的分析见 [商业与规模]({{< relref "/docs/muse/analysis/business" >}})。

Threads 的 Muse 集成截至 11-08 只是应用研究者看到的开发中功能，Meta 没有宣布（[Threads 开发 Muse 助手]({{< relref "/docs/muse/sources/media/2026-11-08-threads-muse-assistant" >}})）。还有一种不受欢迎的入口：有作者称，自己的 WhatsApp 里出现了无法移除的 Muse 浮动头像，他「从没要求过」（[Walsh 非用户隐私]({{< relref "/docs/muse/sources/community/2026-11-13-walsh-muse-non-user-privacy" >}})）。

Muse 与 Meta AI 是两个产品。Meta AI 是已经内置在 WhatsApp、Instagram、Facebook 中的助手，马恩岛信息专员特意区分了两者（[信息专员谈代理式 AI]({{< relref "/docs/muse/sources/community/2026-11-27-isle-of-man-commissioner-agentic-ai" >}})）。有中文综述称 Muse「也可以在 Meta 的各种社交软件中使用」，资料页已加注，说明截至该文时官方只提到 WhatsApp（[飞雪谈AI：对比分析与趋势]({{< relref "/docs/industry/sources/community/2026-10-16-feixue-personal-agent-comparison" >}})）。

## 实时语音与化身

Connect 大会（09-23）发布了 Muse Realtime Voice 和 Realtime Avatar。Meta 的技术文章给出的指标是：化身输出 25 fps、448×768 竖屏，从用户说完到收到首字节约 870 毫秒；盲测中，评估者对 Runway Characters 的偏好比为 78% 对 22%，对 HeyGen LiveAvatar 为 88% 对 12%（[Muse Realtime Avatar]({{< relref "/docs/muse/sources/official/2026-09-23-bringing-your-muse-to-life" >}})）。这些都是厂商自评。社区作者指出，870 毫秒是化身的数字，不是语音延迟（[打开 Muse 语音模式]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}})）。

推送经过：10-24 起有用户看到语音功能逐步推送，官方没有公告（[语音悄悄上线]({{< relref "/docs/muse/sources/media/2026-10-25-muse-voice-conversations-rollout" >}})）；11-05 官方宣布在美国的移动端、网页和 Mac 推出，通话中可以随时打断，Muse 一边说话一边在后台处理任务，有「数百种」声音可选，化身有仅语音、并排、全屏三种显示（[语音与表情化身]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}})）。TechCrunch 称语音向「美国所有人」开放，化身听得见用户但「看不见」（[TechCrunch：语音视频聊天]({{< relref "/docs/muse/sources/media/2026-11-05-muse-video-chat-avatar" >}})）。The Verge 实测觉得响应快，但 Muse 查信息时偶尔会停顿（[The Verge：语音上手]({{< relref "/docs/muse/sources/media/2026-11-05-muse-voice-mode-hands-on" >}})）。社区作者引用 ParseMyApp 11-09 的统计：抽样的近期 Google Play 评论中，约 5% 称自己的账户用不了实时语音（[语音化身设计分析]({{< relref "/docs/muse/sources/community/2026-11-18-voice-avatar-design" >}})）。英国稿称声音里有多种英国口音（[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})）。

用户可以给 Muse 改名、换形象、选声音、定性格，默认形象是毛绒角色 Jolly（[OpenClaw 同源拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})、[TechCrunch：语音视频聊天]({{< relref "/docs/muse/sources/media/2026-11-05-muse-video-chat-avatar" >}})）。Wang 宣布了头像跳舞分享，可以把头像发到 Instagram、WhatsApp、Facebook 的 Feed 或 Story（[Muse 头像跳舞分享]({{< relref "/docs/muse/sources/media/2026-11-08-muse-avatar-dance-share" >}})）。

## Muse Mail：智能体自己的邮箱

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-09-23 | Connect 大会预告，Wang 称「很快」推出，没有给日期 | [TechCrunch：Connect 上的 Muse]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}}) |
| 2026-11-06 | 用户看到应用里出现设置卡片，Meta 没有公告 | [Muse Mail 开始推出]({{< relref "/docs/muse/sources/media/2026-11-06-muse-mail-rollout" >}}) |
| 2026-11-10 | Muse 官方账号与 Wang 宣布向美国、加拿大的付费用户开放，免费档不在内 | [Muse Mail 付费开放]({{< relref "/docs/muse/sources/media/2026-11-10-muse-mail-paid-subscribers" >}}) |
| 2026-11-11 至 12 | 日本用户陆续领到地址，Meta 没有就日本发布公告 | [Muse 邮箱日本可用]({{< relref "/docs/muse/sources/media/2026-11-12-muse-mail-japan-itmedia" >}}) |
| 2026-11-20 | 向所有支持市场开放，免费档也能用 | [Muse Mail 全面开放]({{< relref "/docs/muse/sources/media/2026-11-21-muse-mail-rolls-out-to-everyone" >}})、[Moka 的 Muse 邮箱]({{< relref "/docs/muse/sources/community/2026-11-21-moka-muse-mail-address" >}}) |

官方帮助页写明（[帮助：Muse 邮箱地址]({{< relref "/docs/muse/sources/official/2026-11-16-help-email-addresses" >}})）：

- **只是智能体自己的地址。** @muse.ai 地址与个人邮箱分开，设置它不会让 Muse 获得 Gmail、Outlook 等收件箱的访问权限。邮件默认以智能体身份发出，也可以让 Muse 用某个已连接的账户发。
- **可以用邮件下指令。** 用户验证一个自己拥有的外部地址后，Muse 会把来自该地址的邮件识别为本人的指令。帮助页同时提醒，任何能访问该账户的人都能借此给 Muse 下指令。Muse 可能拒绝通过邮件处理财务、健康、凭证等敏感话题。
- **有发送限制。** 发信数量有上限，不能用于批量营销。

Qiita 的作者实测确认：地址 handle 为 3 到 32 位，确定后不能更改，只能改发件人姓名；每封邮件发出前会显示收件人、主题和正文，用户不点批准就不发送；未验证的地址发来的邮件不会被当作指令执行（[实测 Muse 邮箱]({{< relref "/docs/muse/sources/community/2026-11-13-muse-mail-hands-on-imafumu" >}})）。

推断：Muse Mail 让 Muse 有了一个以智能体名义对外的固定地址，收件人不需要 Muse 账户也能回复（[帮助：Muse 邮箱地址]({{< relref "/docs/muse/sources/official/2026-11-16-help-email-addresses" >}})）。这样 Muse 对外联系时不必借用用户的个人邮箱，与下文以用户名义代发的那些渠道正好相反。

## 以用户名义代发：短信、WhatsApp、Messenger 与社交平台

多个渠道上，Muse 以用户本人的身份发出内容：

- **短信与 WhatsApp。** 有用户实测，Muse 可以通过 SMS 和 RCS 以用户身份给人发短信，Android 上暂时处理不了群聊（[凌晨 3 点的定时任务]({{< relref "/docs/muse/sources/community/2026-10-10-muse-scheduled-tasks-work-while-asleep" >}})）。一篇社区文章依据路透社报道和连接器文档写道：Muse 的消息从用户自己的手机号发出，署用户的名字，每次发送前先停在审批卡上；发出后不能编辑，也不能对所有人删除。作者说明没有做真实发送测试，并指出 Meta 没有公布群聊消息是否会标明由智能体发送（[Muse 冒名发消息]({{< relref "/docs/muse/sources/community/2026-11-24-muse-messages-as-you-group-chat" >}})）。雷峰网对安卓安装包做了静态分析：群发或带附件的短信，Muse 只起草，由用户按发送；替用户在通话里开口的工具只用于商家，打给家人朋友时 Muse 只负责拨号（[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）。
- **Messenger。** 拆解文件显示，Messenger Companion「以用户的身份发送，而不是以 Muse」（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。
- **Marketplace 与社交发帖。** 据卫报报道，Muse 在 Facebook Marketplace 上以用户身份回复买家，没有标注 AI；当事人原以为同属 Meta 的几个产品会明确标记由 Muse 发送（[卫报：泄露家庭住址]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})）。事件经过见 [安全]({{< relref "/docs/muse/analysis/security" >}})。11-20 官方演示的 Marketplace 代卖，要卖家批准后才发布（[Marketplace 代卖上线]({{< relref "/docs/muse/sources/media/2026-11-21-muse-sell-facebook-marketplace" >}})）。有用户让 Muse 以自己的账号在 X、Threads、Instagram 发帖，Threads 每次发布都要点确认卡（[Web3 村长：7 天自动化实测]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})）。

官方给出的唯一披露手段是：在 Muse 代发的邮件、短信和 artifacts 中，用户可以「让 Muse 加一条说明」，表明内容由 AI 智能体生成（[帮助：开始使用]({{< relref "/docs/muse/sources/official/2026-09-08-help-get-started" >}})）。这是用户自选的设置，不是默认行为。

推断：以用户名义发消息时，收件人能看到的只有用户的号码或账号，有没有披露全看用户的设置。这也是隐私主题中「非用户」问题的来源，见 [隐私]({{< relref "/docs/muse/analysis/privacy" >}})。

## 商家电话：从 Beta 到付费开放

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-08 | 内部测试 | [Muse 对外拨号开放]({{< relref "/docs/muse/sources/media/2026-11-12-allthingsmuse-outbound-calling-paid" >}}) |
| 2026-09-16 | 首席工程师 Ryan Fox 和 Wang 宣布扩大 Beta，范围是拨打美国商家，先开放给提出过需求的用户 | [404 Media：电话任务背后的真人]({{< relref "/docs/muse/sources/media/2026-09-22-404media-muse-calls-made-by-humans" >}})、[Instinct 与 Muse 通话]({{< relref "/docs/industry/sources/media/2026-09-17-techcrunch-instinct-muse-phone-calls" >}}) |
| 2026-09 至 10 | 据 CNBC、404 Media 报道，内部测试曾由真人承包商代打电话 | [CNBC：智能体背后的真人]({{< relref "/docs/industry/sources/media/2026-10-31-cnbc-humans-behind-ai-agents" >}})、[404 Media：电话任务背后的真人]({{< relref "/docs/muse/sources/media/2026-09-22-404media-muse-calls-made-by-humans" >}}) |
| 2026-11-12 | 结束 Beta，向美国付费订阅用户开放；Wang 举的例子有有线电视、车管所和不提供在线预订的餐厅 | [Muse 对外拨号开放]({{< relref "/docs/muse/sources/media/2026-11-12-allthingsmuse-outbound-calling-paid" >}})、[Muse 电话代打上线]({{< relref "/docs/muse/sources/media/2026-11-12-techcrunch-muse-phone-calls-paid" >}}) |

使用方式：用户提出需求，Muse 拨打电话，事后在应用里交付通话文字记录和摘要（[电话代打 beta 首报]({{< relref "/docs/muse/sources/media/2026-10-05-muse-phone-call-beta" >}})）。

- **用户报告。** 社区站汇总的说法是：来电显示为 META，Muse 开场会说明自己是代用户打电话的 AI、正在做记录；但另一批 Reddit 报告称开场白每次都不一样，有时只报一个人名、不提 AI；Muse 会拒拨个人号码；同一号码约每天两通上限；Muse 没有自己的号码，不能接听来电（[电话代打能做什么]({{< relref "/docs/muse/sources/community/2026-10-12-builtwithmuse-call-customers" >}})）。
- **实测案例。** Peter Yang 的 Beta 实测中，Muse 自称「我是 Haley，代表 Peter 打来电话」，谈到每月 60 美元的促销价，但客服要求 Yang 本人回电才能成交（[Peter Yang 十个工作流]({{< relref "/docs/muse/sources/community/2026-10-14-peter-yang-ten-workflows" >}})）。
- **未公布的信息。** 截至 11-14，单次价格、时长和次数上限、来电号码、是否每次都披露 AI 身份、录音如何保存，都没有官方说明（[电话代打台账]({{< relref "/docs/muse/sources/community/2026-11-14-muse-phone-calls-paid-rollout" >}})）。Meta 发言人此前说，只会在准备就绪并「附带适当披露」时推出（[电话代打 beta 首报]({{< relref "/docs/muse/sources/media/2026-10-05-muse-phone-call-beta" >}})）。社区作者也承认，没有公布不等于没有披露（[电话代打披露缺口]({{< relref "/docs/muse/sources/community/2026-11-08-phone-calls-disclosure-gap" >}})）。

成功率只有一组二手数字：有真人协助时为 95% 至 98%（据路透社，经社区文章转述，[电话代打披露缺口]({{< relref "/docs/muse/sources/community/2026-11-08-phone-calls-disclosure-gap" >}})）。正式开放后的成功率没有公布。TechCrunch 指出，许多商家一认出对方是 AI 就会挂断（[电话代打台账]({{< relref "/docs/muse/sources/community/2026-11-14-muse-phone-calls-paid-rollout" >}})）。

## 渠道之外的读取路径

渠道主题关心的是用户从哪里和 Muse 说话。路透社的复现揭示了另一面：Muse 可以不经连接器，借操作系统权限读取别的通讯应用。在 Android 上它借推送通知权限，在 macOS 上借无障碍功能加截图读取 Signal 消息，在 iPhone 上被阻止（[Signal 消息与通知权限]({{< relref "/docs/muse/sources/community/2026-11-19-muse-signal-notification-permission" >}})）。Signal 11-20 默认开启截图限制，称这类集成对它是「生存威胁」（[Signal 限制截图防读取]({{< relref "/docs/muse/sources/media/2026-11-21-signal-screenshots-block-ai-agents" >}})）。详见 [隐私]({{< relref "/docs/muse/analysis/privacy" >}}) 和 [安全]({{< relref "/docs/muse/analysis/security" >}})。

## 资料缺口

- 各市场的渠道对照没有官方出处：澳大利亚能不能用 WhatsApp，实时语音在美国以外何时推出，Instagram 私信何时扩展到英国和澳大利亚。
- 商家电话正式开放后的官方说明：单价、上限、来电号码、AI 身份披露的固定话术、商家退出办法、成功率。
- 群聊、短信、WhatsApp 代发时，是否有默认的 AI 身份标注；「加一条说明」这项设置的默认值和实际效果。
- Instagram 私信入口的官方公告原文，以及上线后的实测。
- Chrome 扩展的官方帮助页；Threads 集成是否上线。

## 主要资料

**官方**

- [推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})：发布稿，App 与 WhatsApp 两个入口
- [语音与表情化身]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}})：实时语音与化身在美国推出
- [Muse Realtime Avatar]({{< relref "/docs/muse/sources/official/2026-09-23-bringing-your-muse-to-life" >}})：Realtime Avatar 的技术指标与评估
- [帮助：Muse 邮箱地址]({{< relref "/docs/muse/sources/official/2026-11-16-help-email-addresses" >}})：Muse Mail 帮助页
- [帮助：开始使用]({{< relref "/docs/muse/sources/official/2026-09-08-help-get-started" >}})：代发内容可附 AI 生成说明
- [日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})、[Muse 上线澳大利亚]({{< relref "/docs/muse/sources/official/2026-11-17-muse-available-australia" >}})、[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})：日本、澳大利亚、英国各自的渠道

**媒体**

- [CNBC：Muse 发布报道]({{< relref "/docs/muse/sources/media/2026-09-08-cnbc-meta-pushes-into-personal-agents" >}})、[BBC 一周试用]({{< relref "/docs/muse/sources/media/2026-11-24-bbc-week-with-muse-uk-launch" >}})：WhatsApp 版的功能范围
- [雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})：一个主对话的设计，以及安装包里的发送规则
- [Muse Mail 付费开放]({{< relref "/docs/muse/sources/media/2026-11-10-muse-mail-paid-subscribers" >}})、[Muse Mail 全面开放]({{< relref "/docs/muse/sources/media/2026-11-21-muse-mail-rolls-out-to-everyone" >}})、[Muse 邮箱日本可用]({{< relref "/docs/muse/sources/media/2026-11-12-muse-mail-japan-itmedia" >}})：Muse Mail 的开放过程
- [Muse 对外拨号开放]({{< relref "/docs/muse/sources/media/2026-11-12-allthingsmuse-outbound-calling-paid" >}})、[Muse 电话代打上线]({{< relref "/docs/muse/sources/media/2026-11-12-techcrunch-muse-phone-calls-paid" >}})、[电话代打 beta 首报]({{< relref "/docs/muse/sources/media/2026-10-05-muse-phone-call-beta" >}})、[CNBC：智能体背后的真人]({{< relref "/docs/industry/sources/media/2026-10-31-cnbc-humans-behind-ai-agents" >}})：商家电话
- [Muse 进 Instagram 私信]({{< relref "/docs/muse/sources/media/2026-11-24-techcrunch-muse-instagram-dms" >}})、[Muse 跟进广告后行动]({{< relref "/docs/muse/sources/media/2026-11-24-mediapost-muse-post-ad-actions" >}})、[Muse 助推 Instagram 广告]({{< relref "/docs/muse/sources/media/2026-11-24-cnbc-muse-instagram-ad-boost" >}})：Instagram 私信与保存入口
- [Chrome 扩展正式宣布]({{< relref "/docs/muse/sources/media/2026-11-20-muse-chrome-extension-official-announcement" >}})：Chrome 扩展
- [卫报：泄露家庭住址]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})：Marketplace 以用户身份回复
- [Signal 限制截图防读取]({{< relref "/docs/muse/sources/media/2026-11-21-signal-screenshots-block-ai-agents" >}})：Signal 的截图限制

**社区**

- [电话代打能做什么]({{< relref "/docs/muse/sources/community/2026-10-12-builtwithmuse-call-customers" >}})、[Peter Yang 十个工作流]({{< relref "/docs/muse/sources/community/2026-10-14-peter-yang-ten-workflows" >}})、[电话代打台账]({{< relref "/docs/muse/sources/community/2026-11-14-muse-phone-calls-paid-rollout" >}})、[电话代打披露缺口]({{< relref "/docs/muse/sources/community/2026-11-08-phone-calls-disclosure-gap" >}})：商家电话的用户报告、实测与未公布事项
- [实测 Muse 邮箱]({{< relref "/docs/muse/sources/community/2026-11-13-muse-mail-hands-on-imafumu" >}})、[Moka 的 Muse 邮箱]({{< relref "/docs/muse/sources/community/2026-11-21-moka-muse-mail-address" >}})：Muse Mail 实测
- [Muse 冒名发消息]({{< relref "/docs/muse/sources/community/2026-11-24-muse-messages-as-you-group-chat" >}})、[凌晨 3 点的定时任务]({{< relref "/docs/muse/sources/community/2026-10-10-muse-scheduled-tasks-work-while-asleep" >}})、[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})：以用户名义发消息
- [语音化身设计分析]({{< relref "/docs/muse/sources/community/2026-11-18-voice-avatar-design" >}})、[打开 Muse 语音模式]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}})：语音推送范围与延迟口径
- [Instagram 私信 Muse]({{< relref "/docs/muse/sources/community/2026-11-25-emma-instagram-dm" >}})、[Muse 的名字与头像]({{< relref "/docs/muse/sources/community/2026-11-26-emma-muse-identity-name-avatar" >}})：日本用户视角的入口
- [Signal 消息与通知权限]({{< relref "/docs/muse/sources/community/2026-11-19-muse-signal-notification-permission" >}})：经通知权限读取 Signal
