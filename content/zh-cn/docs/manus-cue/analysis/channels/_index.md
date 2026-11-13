---
title: "Manus Cue：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Cue 的核心卖点是给每个智能体一套对外可寻址的身份：@bot.cue.im 邮箱和可选的付费电话号码，以智能体自己的名义对外沟通；用户在像即时通信软件的 Cue 应用里与智能体单聊或拉群，也可以经 iMessage、Telegram、LINE、Slack 联系，或扫商家二维码生成专用智能体。
---

## 概要

- Cue 是独立应用，界面像即时通信软件：联系人是一个个智能体，可以单聊，也可以拉进群聊分工。同一个智能体还可以接入 iMessage、Telegram、LINE、Slack（截至 2026-10-08 的帮助文档）。
- 每个智能体有自己的邮箱（`名字@bot.cue.im`）和可选的电话号码，对外以智能体身份沟通。这是各类资料把 Cue 称为「最激进」「走得最远」的主要原因。
- 身份并不隐藏：邮件自动带「Powered by Manus. Sent on behalf of 用户名」的页脚。电话号码收费，美国号码只支持语音、不能收发短信。
- 线下入口是扫商家服务二维码，为该服务生成一个专用智能体，代为点单或排队，付款由用户确认。
- 多智能体群聊是官方主推的用法，但唯一一份详细实测显示，前几轮需要用户自己分工、补信息，群聊和私聊的记忆不互通。

## 像即时通信软件的独立应用

Cue 是独立应用，与 Manus 分开，Manus 侧边栏的「Agents (Cue!)」标签提供下载二维码（[帮助：Manus 2.0 新功能]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-what-is-new-in-manus-2-0" >}})）。硅星人描述注册引导：先给智能体起名，分配专属邮箱和云电脑，可选按月租专属号码；整个界面像即时通信软件，有联系人、聊天、头像和群组（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）。

xiangxiang103 记录了新建智能体的流程：第一句问它主要负责什么，给出三个方向（整理消息、记录和截止日期；调研并比较选项；拆目标并跟踪卡点），另有邮件助手、财务助手、研究助理三个模板（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。硅星人看到每个助手有自己的资料页，指令、记忆、文件、自动化以及邮箱、电话、支付、电脑入口都按助手组织（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）。

硅星人把这种结构与 Muse 对比：Muse 强调一个长期了解用户的主助手，Cue「把多个固定职责的助手放到了前台」（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）。

## 也可以经 iMessage、Telegram、LINE、Slack 联系

帮助文档写明，同一个智能体可以连接多个消息平台，可以切换，也可以同时开启；目前支持 iMessage、Telegram、LINE、Slack 四种。路径是 Agent Info > Integration > Messenger > Connect，每个平台一个开关。首次 OAuth 登录失败多与应用内浏览器有关，受限的公司网络下可能要改用移动数据（[帮助：多个消息平台]({{< relref "/docs/manus-cue/sources/official/2026-10-08-help-multiple-messaging-platforms" >}})）。

这篇帮助页是资料库中唯一提到这四个渠道的资料，发布文、应用商店介绍和各篇实测都没有写，也没有人实测过。

## 智能体自己的邮箱：身份并不隐藏

xiangxiang103 填完邀请码后，智能体自动获得 `名字@bot.cue.im` 邮箱（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。作者认为独立邮箱的价值是「你不用把自己的邮箱地址交出去」（同上）。

实测发出的邮件自动带页脚：Manus 的 logo、「Powered by Manus. Sent on behalf of 你的名字」、一排社交图标和退订链接，进了收件方 Gmail 的推广栏。作者提醒，对方一看就知道是 AI 代发，邮箱地址虽然没暴露，身份并没有藏住（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。

## 电话号码：收费、仅语音、绑定地区

发布文称智能体可以替用户接听电话，并在 Cue 里留下摘要（[Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})）。电话默认不开，要在设置里添加；xiangxiang103 选美国（+1）号码时弹窗写明「仅支持语音通话；无法发送短信」，作者据此提醒不要指望用它收验证码；国内电话能否转入没有测到（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。作者转述官网示例：用户在飞机上或倒时差时，来电由智能体接听、问清来意，急事推送到用户的 Slack（同上）。

电话号码单独收费，订阅与 Manus 会员分开购买，用量计入 Cue 的每周额度（[帮助：会员定价]({{< relref "/docs/manus-cue/sources/official/2026-10-23-help-membership-pricing" >}})）。价格说法不一，见[开放与价格](../access-pricing/)。App Store 内购列出美国、英国、以色列、新加坡、加拿大号码（[App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})），说明到 11 月初号码已不止美国一地。

Datawhale 转述用户反馈：电话像「后挂上去的」，部分热门国家收不到短信，号码国家跟智能体当前的代理 IP 绑定，换区要先换 VPN（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）；鸿煊重述了这一点（[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。

硅星人在发布次日对比：Cue 可配置专属号码和邮箱、代接电话；Muse 同样在发展电话能力，但当时仍是代理使用用户的号码（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）。硅星人推断，先面向美国市场、主打电话代接，是因为美国有大量需要打电话交涉的场景（同上）。

## 扫商家二维码生成专用智能体

应用商店介绍称，扫描商家的服务二维码（如点单二维码）会为该服务创建一个专用的 Cue，它浏览菜单、按用户口味挑选并下单，付款由用户确认（[Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})）。发布文的例子是在餐厅代为点餐或排队占位（[Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})）。硅星人称「扫码连接 Agent」在发布视频中有展示，并设想以后每个智能体都可以有二维码，顾客扫码后让自己的 Cue 与店铺的智能体沟通（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）。资料库中没有这一功能的实测。

## 多智能体群聊：官方主推，实测要用户当项目经理

发布文的示例是纽约发布活动：一个智能体调研场地，一个整理候选清单，一个起草演示文稿，「你定方向，并做最终决定」（[Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})、[帮助：Manus 2.0 新功能]({{< relref "/docs/manus-cue/sources/official/2026-10-01-help-what-is-new-in-manus-2-0" >}})）。肖弘在社交媒体上设想「很多人和 bot 的群」，称有独立手机号、邮箱、支付、电脑且足够智能的东西「也许可以称之为‘人’」（据[财经涂鸦]({{< relref "/docs/manus-cue/sources/media/2026-09-29-caijingtuya-xiaohong-on-cue" >}})转述）。

两份实测：

| 测试者 | 任务 | 结果 |
| --- | --- | --- |
| xiangxiang103（2026-09-29） | 三个智能体规划东京亲子游 | 三个都回复但没人开始干活；研究员同一问题问了两遍；群聊与私聊记忆不互通；最后由「秘书」主动分工。作者结论：「前面几轮你得先当项目经理」 |
| 硅星人（2026-09-29） | 「行程规划」「预算核查」两个助手规划家庭出游 | 多轮对话，可在群里看它们交流；因未接支付权限，没有让它下单 |

资料来源：[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})、[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})。

## 资料缺口

- iMessage、Telegram、LINE、Slack 渠道的实测；这些渠道上能否用群聊、电话摘要如何送达。
- 电话的官方说明：可选国家、是否能拨出、通话时长限制、对通话对象如何披露 AI 身份。
- 邮件页脚能否关闭；智能体邮箱的收件规则与垃圾邮件处理。
- 扫码点单在真实商家中的覆盖与实测。

## 主要资料

官方
- [Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})：独立身份、接电话留摘要、群聊、扫码
- [帮助：多个消息平台]({{< relref "/docs/manus-cue/sources/official/2026-10-08-help-multiple-messaging-platforms" >}})：iMessage、Telegram、LINE、Slack
- [帮助：会员定价]({{< relref "/docs/manus-cue/sources/official/2026-10-23-help-membership-pricing" >}})：电话单独订阅、计入每周额度
- [Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})、[App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})：扫码专用智能体；各国号码

媒体
- [硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})：界面、助手资料页、群聊实测、与 Muse 对比
- [财经涂鸦]({{< relref "/docs/manus-cue/sources/media/2026-09-29-caijingtuya-xiaohong-on-cue" >}})：肖弘「人和 bot 的群」

社区
- [xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})：邮箱、邮件页脚、电话弹窗、群聊实测
- [Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})：电话与 IP 绑定、收不到短信（转述）
