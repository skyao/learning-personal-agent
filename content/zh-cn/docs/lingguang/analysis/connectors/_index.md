---
title: "蚂蚁灵光：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  灵光 2.0 内置支付宝账单、会员、出行服务，另通过授权、MCP、CLI 和 Skill 连接钉钉、飞书、邮箱、米家等，2026-11-04 外部连接器增至 40 项。实测中「读」普遍可用，「写」和付款多数做不到：发消息被拦截、转账无权限、付款只能跳转、淘宝进不去。能力半径基本以支付宝生态为界。
---

## 概要

- 官方称灵光 2.0 内置支付宝账单、会员与出行服务，可连接邮箱、钉钉、飞书、米家，并在开放环境中调用 MCP 与 CLI。据亿邦，2026-11-04 升级新增哈啰打车、麦当劳、微信读书等，外部连接器达 40 项。
- 接入方式混杂：扫码授权、授权链接、邮箱授权码、官方 MCP、GitHub 上的 Skill，都在对话中由灵光引导完成。
- 「看」和「盯」做得到，「办」做不到：读账单、群聊、网盘、设备状态基本可用；在钉钉、飞书发消息即使用户点了确认也被拦截，转账没有权限，点咖啡只能给出跳转支付宝的链接，扫拖机器人不能下指令。
- 生态墙是主要限制：蚂蚁与阿里在数据和接口上合规隔离，灵光读不到淘宝购物车，同样的事千问能做；国内多个超级 App 拒绝外部 AI 代操作。
- 资料中没有灵光向第三方开发者开放接入的计划。

## 内置服务与 40 项外部连接器

官方发布稿列出的范围是：内置支付宝账单、会员、出行服务，以及邮箱、钉钉、飞书、米家；开放环境中支持调用 MCP 与 CLI 等工具（[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})）。App Store 简介另提到滴滴出行和智能硬件（[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})）。智东西与新眸补充了车生活（停车、加油、充电）、QQ 邮箱、滴滴、百度网盘，并称开放能力可延伸到理想、蔚来、小鹏、华为汽车、运动手环、体脂秤和 12306，用户也可以自行添加公开 MCP（[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})、[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）。

亿邦称 11 月 4 日灵光完成新一轮升级，新增哈啰打车、麦当劳、微信读书等，外部连接器总数达 40 项；文章把分工概括为「连接器负责打通系统，技能（Skill）赋予执行方法，工作伙伴提供角色分工」（[亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}})）。40 项的完整清单资料中没有。

## 各种接入方式

AI沃茨在内测期把 15 个 App 接进灵光，接入方式各不相同（[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})）：

| 方式 | 例子 |
| --- | --- |
| 扫码授权 | 米家、百度网盘 |
| 授权链接 | 钉钉、支付宝 |
| 邮箱 IMAP/SMTP 授权码 | QQ 邮箱 |
| 官方 MCP | 滴滴（需申请 Key）、瑞幸、麦当劳、高德 |
| Skill 或 GitHub 项目 | 美团跑腿、微信读书、网易云音乐、美图、飞猪 |
| 不绑账号 | 淘宝（只查价、盯价） |

内测期的三哥称，连接应用、安装 CLI、MCP、Skill 都在对话框里告诉灵光即可（[三哥：1.0 与 2.0]({{< relref "/docs/lingguang/sources/community/2026-10-13-chanpinbiji-1-0-vs-2-0" >}})）。正式版在首页右上角有连接入口，分「应用服务」和「系统服务」（[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})）；小象AI 则称在 App 里「翻了半天」没找到连接阿里系应用的入口（[小象AI]({{< relref "/docs/lingguang/sources/community/2026-10-28-xiaoxiang-lingguang-2-hands-on" >}})）。

钉钉的门槛较高：个人绑定账号之外，还需要公司管理员在钉钉开放平台开通「CLI数据访问」权限；连通后体验是该次测试中较顺畅的（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）。

## 读得到，写不进去

| 动作 | 结果 | 资料 |
| --- | --- | --- |
| 支付宝账单梳理、找自动续费 | 可以；看不到签约状态 | [极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})、[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}}) |
| 读钉钉群聊与通讯录、飞书新建云文档 | 可以 | [极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}}) |
| 钉钉发群消息、飞书回复联系人 | 点了「确认发送」仍失败，灵光自述是执行环境的安全策略拦截 | [极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}}) |
| 亲情号转账 | 提示没有执行转账的权限 | [AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}}) |
| 点瑞幸咖啡 | 无法调用支付宝 AI付，只给出跳转支付宝团购券的链接 | [极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}}) |
| 读淘宝购物车 | 云端网页版被风控拦截；千问可以直接列出 | [极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}}) |
| 查医保余额 | 未接入 | [AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}}) |
| 米家扫拖机器人「打扫客厅」 | 只能看状态（蓝牙通道） | [AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}}) |
| 米家空调、小米汽车 | 可远程调温、开关车窗 | [AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}}) |
| 米家自动化 | 只能教用户在米家 App 里建 | [AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}}) |
| ETC、充电 App 订单 | 不能登录拉取，需用户给截图或金额 | [白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}}) |
| 电影、机票 | 推进到选座或给出携程链接，付款交给用户 | [Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}}) |
| 飞猪搜酒店、美团跑腿 | 返回真实套餐和预订链接；可代取号 | [AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}}) |

Z Finance（11 月 1 日）称外卖、网购、打车、淘宝跨店比价、取消订单、退货、联系客服都尚未覆盖，售后只能查快递（[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})）。其中打车在 11 月 4 日新增了哈啰打车连接器，但资料中没有新连接器的实测。AI故事计划在 11 月 5 日仍称灵光无法直接完成支付宝付款和淘宝购物（[AI故事计划：二线厂]({{< relref "/docs/industry/sources/media/2026-11-05-aigushijihua-second-tier-personal-agent" >}})）。

AI故事计划的总结是，灵光「已经能把散落在不同 App 里的信息搬到同一对话框，却还没把这些 App 变成自己的工具」（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）。Z Finance 认为交易能力停留在辅助决策与跳转引导，能力半径「基本仍以支付宝生态为边界」（[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})）。

## 相互矛盾的实测

- 米家：AI沃茨扫码后找到 18 台设备、在线 9 台（[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})）；极客公园授权成功后小米接口连续两次触发限流，设备列表拉取失败（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。账号和时间不同，可能是接口稳定性问题。
- 支付宝：AI沃茨先称个人转账付款、看账单没有通用接口，后文又称测试过程中灵光「原生打通了支付宝全生态」，能梳理三个月账单（[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})）。前后变化说明内测期接入方式在快速迭代；「打通」指读取账单，付款至今各家实测都没有做到。

## 蚂蚁与阿里之间的墙

极客公园解释了淘宝失败的原因：蚂蚁与阿里是两个独立运营的主体，「数据与接口有着严格的合规隔离」；灵光与淘宝之间没有打通底层接口，而千问可以进淘宝购物车、可在 App 内完成点单（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。AI故事计划称「蚂蚁和阿里生态之间的那堵墙，还没有被拆掉」（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）。小象AI 说灵光「背后站着整个阿里生态」（[小象AI]({{< relref "/docs/lingguang/sources/community/2026-10-28-xiaoxiang-lingguang-2-hands-on" >}})），与上述实测不符。

比价时这道墙反而成了中立性的例子：同一问题千问只查淘宝，灵光比对京东和淘宝后建议在京东下单（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。

## 国内超级 App 对外部智能体的态度

- 新眸称豆包手机助手曾被包括微信、淘宝在内的 155 款应用拒绝接入，外部智能体在国内的核心约束从「集成」变成「授权与准入」（[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）。极客公园称 10 月 14 日公示期结束后仍有 155 款主流 App 明确拒绝（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）；AI故事计划称微信、淘宝、支付宝、美团等明确拒绝了豆包手机助手的自动化操作（[AI故事计划：二线厂]({{< relref "/docs/industry/sources/media/2026-11-05-aigushijihua-second-tier-personal-agent" >}})）。
- 亿邦把路线分为平台型助手（自有生态闭环）和独立助手（跨生态整合），称灵光走「平台底子+跨生态连接」的中间路线（[亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}})）。
- 奈势AI 的说法是「Agent 能做什么，最终取决于平台愿不愿意开门」（[奈势AI]({{< relref "/docs/industry/sources/community/2026-10-15-naishi-what-can-it-do" >}})），其例子针对 Dots，不是灵光。

蚂蚁一侧的基础设施：36氪称支付宝 5 月披露 AI 支付已支持 95% 的通用智能体框架、累计完成 3 亿笔智能体支付（[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}})）；新眸的表述是「覆盖超 95% 的通用智能体场景」（[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）。两文都是转述，口径不同。这些支付能力截至 2026-11-10 的实测中还没有向灵光开放（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。

推断：灵光的连接面在数量上增长很快（内测期十几个，11 月初 40 项），但每个连接的写权限很窄。差别不在接了多少，而在支付宝 AI付、淘宝这些近在咫尺的能力是否开放给它。

## 资料缺口

- 40 项连接器的完整清单，以及每项的读写范围。
- 11-04 新增的哈啰打车、麦当劳等连接器能否完成下单和付款。
- 支付宝 AI付 向灵光开放的计划；蚂蚁对「发消息被拦截」的官方说明。
- 是否向第三方开发者开放接入、是否有审核与分成机制。
- 授权失效（如米家限流、令牌过期）时的处理和提示。

## 主要资料

- 官方：[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})、[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})，内置服务与连接范围。
- 媒体：[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})，权限实测与蚂蚁、阿里隔离；[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})，做得到与做不到的清单；[亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}})，40 项连接器与路线判断；[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})、[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})，连接范围；[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})，ETC 与充电订单。
- 社区：[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})，接入方式最全的实测；[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})，交易场景覆盖；[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})，连接入口。
