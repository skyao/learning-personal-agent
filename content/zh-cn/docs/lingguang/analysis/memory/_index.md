---
title: "蚂蚁灵光：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  灵光 2.0 的记忆以「一件事」为单位：每个事务在「我的生活」中生成一张卡片，保存目标、偏好和进展；个人数据以授权后的支付宝账单为核心，另接邮箱、钉钉、网盘和手机系统服务。用户如何查看、编辑、删除记忆，资料没有说明。
---

## 概要

- 官方把「跨会话记忆」列为 2.0 的三项升级之一。实际呈现方式是事务卡片：每件交给灵光的事在「我的生活」（「帮我管」）中生成一张卡片，目标、条件、清单和进展都留在这件事的上下文里。
- 个人数据的核心是支付宝账单：官方的第一个例子就是授权后梳理消费、找出被遗忘的自动续费。此外可接邮箱、钉钉、飞书、百度网盘、米家，以及手机的日历、提醒事项、闹钟、健康、位置、文件、短信。
- 实测中记忆的延续性评价较好：设定的预算、出行偏好在之后的对话和任务中会被沿用。
- 账单数据有明显边界：只能看到扣款记录，看不到签约状态；微信支付、银行卡等其他渠道的开支不在其中。评论者提醒「账单不等于一个人」。
- 用户能否查看、修改、删除记忆，断开连接后数据如何处理，官方资料都没有写。

## 以事务为单位的记忆

官方发布稿称，灵光 2.0 的主动能力依靠跨会话记忆、长程任务调度和工具调用的升级（[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})）。新眸的说法是，跨会话记忆解决「不用每次从头解释」，历史进展保留在事务上下文里（[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）。App Store 简介写「帮我管」会围绕同一件事统筹安排，「记住你的偏好，让每次沟通都接得上」，计划、清单和记录随进展更新（[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})）。

在界面上，2.0 新增「我的生活」tab，每一个事项都会生成一张事务卡片长期跟进（[三哥：1.0 与 2.0]({{< relref "/docs/lingguang/sources/community/2026-10-13-chanpinbiji-1-0-vs-2-0" >}})）；Z Finance 测试时首屏是「帮你盯」，进行中的事务以卡片陈列（[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})）。三哥认为身份、长期记忆、云端自主规划三项特征灵光都具备，但「不是以显性的方式呈现」，而是体现在任务执行中。

36氪举例：家庭出游时说过「带老人、不赶早班机、酒店离地铁近」，几天后再聊机票和酒店，灵光仍能沿用这些要求（[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}})）。这是文章举例，不是实测。

推断：与 Muse、Claude Duet 那种账号级的记忆库相比，灵光资料中的记忆几乎都挂在具体事务上。是否另有跨事务的用户画像，资料没有提到。

## 接入的个人数据

| 类别 | 内容 | 资料 |
| --- | --- | --- |
| 支付宝 | 账单、会员、出行记录；梳理消费、找被遗忘的自动续费 | [官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})、[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}}) |
| 邮箱 | QQ、网易 163 与 126、新浪、搜狐；暂不支持阿里邮箱 | [AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}}) |
| 办公 | 钉钉群聊与通讯录、文档、日程、审批、考勤；飞书 | [AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})、[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}}) |
| 文件与设备 | 百度网盘、米家设备列表 | [AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}}) |
| 手机系统服务 | 日历、提醒事项、闹钟、健康；位置、文件、短信 | [小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})、[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}}) |

连接入口在首页右上角，分「应用服务」和「系统服务」两类，支付宝点加号后授权即可（[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})）。授权是按需弹出的，不在首次使用时一次性索要（[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})）。连接方式详见[连接器]({{< relref "/docs/lingguang/analysis/connectors" >}})。

亿邦转述灵光公布的数据：用户请求中，财务与消费场景占 23.83%，健康与习惯占 21.46%（[亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}})）。未说明统计时段和分类方法。

## 实测中的记忆效果

- AI故事计划让灵光分析支付宝账单；告知打车是工作需要、改签不可避免后，灵光重新分析，结论是一个月大概能省 30 到 50 元。作者称「长对话的记忆力也没什么可挑剔」，但认为这类能力豆包、千问早已够用（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）。
- 小朱设置每日预算提醒后，点外卖时灵光记得预算，建议「17元的最稳妥，28.8元的能吃得更饱」（[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})）。
- 白鲸技术栈做双十一宠物囤货时，灵光先复盘历史消费记录，识别出常购品类、淘宝渠道与 88VIP 权益、多宠家庭；养车记账的范围、待办状态和数据缺口都写进项目，保留在「我的生活」中（[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})）。
- 光子星球用邮箱授权让灵光找回一封没有备份的邮件，灵光还主动总结了最近一周的邮件（[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})）。

## 账单不等于一个人

极客公园实测中，灵光明确提示「账单只能看到扣款记录，看不到当前的签约状态」（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})），也就是说它能发现扣过钱的续费，但无法确认订阅是否仍然有效。AI故事计划指出，微信支付、银行卡等其他渠道的开支没有进入支付宝账单分析（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）。白鲸技术栈认为账单「替家人付款、报销和线下消费都可能造成误判」，数据越靠近生活，授权和校正越重要（[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})）。

## 记忆的查看、修改与删除

资料没有说明用户如何查看、编辑或删除灵光的记忆，也没有说明断开某个连接后已读取的数据如何处理。潜在工作室资料页的内容摘要写有「灵光断开应用不删除记忆」，但正文中这一点说的是 OpenAI Dots，不是灵光（[潜在工作室]({{< relref "/docs/industry/sources/community/2026-11-10-qianzai-answer-to-follow-up" >}})），本页不采用；该问题已记入 `progress.md`。

## 资料缺口

- 记忆的存放形态（是否有独立的记忆列表或用户画像）、查看与编辑入口、删除与遗忘机制。
- 断开支付宝、邮箱等授权后，已读取的数据和事务卡片如何处理。
- 记忆是否在 App、网页版之间同步；与支付宝、阿宝等蚂蚁其他产品是否共享。
- 「23.83%」等请求分类数据的统计口径。

## 主要资料

- 官方：[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})，跨会话记忆与支付宝账单示例；[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})，「帮我管」的说明。
- 媒体：[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})，事务上下文；[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}})，偏好沿用的例子；[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})、[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})，账单分析实测与局限；[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})，看不到签约状态；[亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}})，请求分类占比。
- 社区：[三哥：1.0 与 2.0]({{< relref "/docs/lingguang/sources/community/2026-10-13-chanpinbiji-1-0-vs-2-0" >}})，事务卡片；[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})、[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})，连接入口与预算记忆实测。
