---
title: "蚂蚁灵光：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  灵光 2.0 的安全设计以蚂蚁 APASS 为中心：授权密钥与智能体分离托管，授权按需弹出、可随时撤销。实测中高风险动作基本被挡在外面：转账无权限、付款只能跳转、发消息即使确认也被拦截。资料中没有提示注入防护、独立审查模型或安全事件的信息。
---

## 概要

- 官方称灵光 2.0 接入蚂蚁的 APASS（智能体可信基础设施），把授权密钥与智能体分离并托管，智能体不直接接触凭据；用户可以随时查看、调整或撤销授权。
- 权限按需申请、收得较紧：授权在用到时才弹出；百度网盘能检索全部文件，但操作只限于灵光自己的专属文件夹。
- 高风险动作在实测中几乎都做不了：转账提示没有权限，付款只能跳转支付宝由用户完成，钉钉、飞书发消息即使用户点了确认也被灵光自身的安全策略拦截。这既是安全设计，也是能力限制。
- 《灵光用户服务协议》第 1.3 条规定，Agent 协助完成的操作视为用户本人的操作，后果和风险由用户承担。
- 截至 2026-11-10 的资料，没有灵光的提示注入防护、独立审查模型、漏洞或安全事件的信息。

## APASS：凭证与智能体分离

官方发布稿称，灵光 2.0 接入蚂蚁的 APASS，统一管理智能体、设备、应用和服务的账户与安全；通过「将授权密钥与智能体分离并托管等机制」，智能体无需直接访问凭据，用户可随时查看、调整或撤销授权；APASS 把身份验证、意图安全和隐私保护嵌入智能体的执行过程（[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})）。App Store 简介的表述是为跨智能体、跨设备、跨应用与服务的账号和授权凭证提供独立加密保护（[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})）。

财经网称 APASS 是面向跨设备、跨应用与服务场景的统一账号与安全管理基础设施，并引蚂蚁集团副总裁、支付宝及大安全事业群首席技术官陈亮在乌镇峰会的发言：智能体时代要让「身份、授权与责任进入每一次连接」（[财经网]({{< relref "/docs/industry/sources/media/2026-11-06-caijingwang-transaction-management" >}})）。36氪把蚂蚁 22 年在支付安全、身份认证和授权管理上的积累视为灵光的信任基础（[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}})）。

实测中能看到 APASS 的痕迹：智东西的截图注明连接钉钉「需要明确授权，通过 APASS 连接」（[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})）；AI沃茨接入 Key 时，灵光回复「密钥已存进沙箱里单独保管」（[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})）。后者是灵光的自述。

APASS 的具体机制（密钥存放位置、加密方式、云端浏览器登录状态如何处理）资料中没有说明。

## 权限按需、看得宽动得窄

Z Finance 实测发现授权按需弹出，不在首次使用时一次性索要；百度网盘的权限是「看得宽、动得窄」：对整个网盘有检索权，操作权只限于灵光自己的一个专属文件夹，文件不能移出或复制出去。作者的批评是边界不透明，灵光不会事先说明哪些事做不到（[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})）。

## 高风险动作交回用户

- 转账：让灵光从亲情号转账，提示没有执行转账的权限，建议用户在支付宝自行操作（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）。
- 付款：点瑞幸咖啡时「最后一步得你自己点一下确认」，只给出跳转链接（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。
- 对外发送：在钉钉发群消息、在飞书回复联系人，用户在前端点击「确认发送」后仍然失败，灵光自述是执行环境的安全策略拦截了发消息这类操作（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。原因来自灵光的回答，官方没有说明。
- 决定类动作：新眸称「支付和重要决定先确认」（[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）；光子星球称账单对比结果只呈现，是否取消订阅由用户决定（[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})）。

AI沃茨在提示语中自设规则「凡是会花钱的动作，先把费用和细节列给我，我说确认才执行」（[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})），这是用户的做法，不是产品默认。

推断：与 Claude Duet、Muse 那种「可以做、但先审批」的设计不同，灵光目前对付款和对外发送基本是「不做」或「交给用户去做」。资料无法区分这是有意的安全策略，还是接口尚未开放的结果；极客公园的发消息案例表明至少有一部分是灵光自己的策略。

## 责任条款

极客公园引用《灵光用户服务协议》（2026 年 5 月 29 日版本）第 1.3 条：Agent 协助完成的操作视为用户本人的操作，后果和风险由用户承担。作者称这是行业通行条款，建议像对待 L2 辅助驾驶那样使用（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。

白鲸技术栈认为灵光仍要证明两件事：授权让普通用户看得懂、能随时撤回；页面变化、优惠失效、接口中断时能发现错误，并在付款、退订、发信前重新确认（[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})）。

## 与海外产品的对照

财经网对照了 Claude Duet（读取、起草与发送、付款、签署分开，后者执行前展示内容等批准，不直接看到账号密码和登录令牌）和 Muse（有与主智能体分离的 Sentinel 检查对外联网和服务调用）（[财经网]({{< relref "/docs/industry/sources/media/2026-11-06-caijingwang-transaction-management" >}})）。资料中灵光没有与 Sentinel 对应的独立审查层的说明。

## 资料缺口

- APASS 的技术细节：密钥存放、加密、撤销后的生效时间；云端浏览器登录状态的处理。
- 提示注入、恶意网页的防护；是否有独立审查模型。
- 发消息被拦截是否为默认策略、能否由用户开启。
- 漏洞赏金、外部安全审计、已发生的安全事件。

## 主要资料

- 官方：[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})、[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})，APASS 的官方描述。
- 媒体：[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})，发消息被拦截、付款跳转与协议条款；[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})，转账无权限；[财经网]({{< relref "/docs/industry/sources/media/2026-11-06-caijingwang-transaction-management" >}})，APASS 与海外对照；[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})、[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})，用户确认。
- 社区：[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})，权限粒度；[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})，密钥托管的自述。
