---
title: "Meta Muse：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  Muse 用 Meta 审核的目录连接器、用户自建的自定义连接器、云端浏览器和用户自己的 Chrome 四条路径接入外部服务；目录在两个多月里从几十家扩到一百多项，但「宣布」「上架」「可用」「有成交」之间差距明显。浏览器路线遭亚马逊、银行、eBay、美联航等封堵，Meta 的应对是 Poppy 协议与沃尔玛 Agent Gateway 这类商家自建通道，截至 2026-11-28 两者都刚起步。
---

## 概要

- **四条路径，治理强度依次递减。** 目录连接器由 Meta 与服务方合作集成并审核，在虚拟机外的权限分离进程里运行；自定义连接器由 Muse 按用户给的 API 或 MCP 文档自行接通，Meta 不审核；没有接口的网站由云端浏览器代用户操作；2026-11-20 正式宣布的 Chrome 扩展则借用用户自己已登录的浏览器。另有 Mac、安卓本机权限和 Gadgets 等设备侧接入。
- **授权粒度在目录连接器上最细。** 官方把工具分成读取、写入、敏感写入三档，购买、发邮件等敏感写入每次都要批准、不能设成「始终允许」；许多连接器可设只读。浏览器路线没有这些控制。
- **目录扩张快，但宣布不等于可用。** Meta 9-23 宣布十家零售商，9-30 的应用内检查一家都没找到；社区实测 11-21 目录有 143 项，地区限制和「逐步推出」使各国用户看到的并不相同。真正走到对话内结账的，截至 2026-11-28 只有 Shopify、沃尔玛（11-23/24 起）、Gopuff 等少数几家，成交证据只有零星的用户自述：Retailgentic 11-24、AI Salon 作者感恩节夜各在沃尔玛下过单；CNBC 报道的一笔 AutoZone 订单 17 小时后被取消。
- **平台封堵是这个主题最大的变量。** 亚马逊 9-20 起封堵并让 Muse 的购物技能主动绕开亚马逊；嘉信、摩根大通和加拿大五大银行拒绝智能体用客户凭证进账户；eBay、The RealReal 收紧防御；美联航 11-11 以运输合同禁止智能体订票。亚马逊与 Meta 正在谈判解封，目前只有 Fortune 一家报道。
- **Meta 的应对是让商家「有门可走」。** Poppy（Personal Agent Protocol）1.0 于 11-13 发布，Shopify 自动为商家发布 poppy.json；沃尔玛用 MCP 网关加自家助手 Sparky 接 Muse。但实地核查显示 Shopify 文件只开放结账一项权限、版本号为 0.4，截至 11-15 也没有 Muse 应用内使用 Poppy 的证据。

## 四条接入路径

| 路径 | 机制 | 谁审核 | 授权控制 | 主要问题 |
| --- | --- | --- | --- | --- |
| 目录连接器 | Meta 与服务方合作集成 API，另写 SKILL 说明用法；在运行时容器外的权限分离进程执行 | Meta 三阶段审核 | 读/写/敏感写分档，可只读，可断开 | 地区限制、逐步推出 |
| 自定义连接器 | 用户给 API 文档或 MCP 地址，Muse 在虚拟机内自行接通，凭证存入安全凭证存储 | 不审核 | 由用户和 Muse 自行设定 | 无人治理 |
| 云端浏览器 | 虚拟机里的浏览器像用户一样登录、操作网站 | — | 无范围屏、无只读开关 | 被网站识别和封堵 |
| 用户的 Chrome | 2026-11 的 Chrome 扩展在用户已登录的浏览器里另开标签组操作 | — | 操作前批准、活动日志、随时撤销 | 借用用户身份 |

**目录连接器。** 帮助文档写明，连接器可在对话中说「Connect my Gmail」或在设置里授权；同一账户中心下的 Facebook、Instagram、Threads 自动连接，部分连接器（如日历）会主动推送变更（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。官方安全文章说明内置连接器由 Meta 与服务方合作集成，并为每个连接器编写 SKILL；业务逻辑由运行时容器外的 privsep 工作进程执行，每个进程按 cgroup 标识、只能取自己的凭证，日历进程拿不到邮件凭证（[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。拆解资料与此一致：Muse 沙箱的 `/opt/hatch/bin` 下约 70 个工具都是 CLI 而不是 MCP 服务器（[Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})）；第三方安全研究称智能体手里只有替代令牌，真实凭证由出口代理 Sentinel 在请求离开时换入（[Muse 内部架构剖析]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})）。用户实测中 Muse 自述「MCP 是协议，connector 是托管产品层」，连接器可用 MCP 做传输，但内部实现无法确认（[VM 探索实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。

**技能与连接器的分工。** 官方称技能（skills）是 Meta 开发的内置能力，自动可用、无需安装（[帮助：技能]({{< relref "/docs/muse/sources/official/2026-09-08-help-skills" >}})）。消费版应用没有安装第三方技能的入口，用户只能把 SKILL.md 粘贴进对话，仅在该对话生效（[粘贴技能文件的风险]({{< relref "/docs/muse/sources/community/2026-11-12-muse-pasted-skill-trust-gap" >}})）。涂鸦 11-12 发布的智能家居技能走的是另一条路：合并进 Meta 的 muse-gadget-sdk 仓库，用户自己取文件、填 API 密钥（[Tuya 智能家居 Skill]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})、[智能家居接入]({{< relref "/docs/muse/sources/community/2026-11-20-muse-smart-home-tuya-skill" >}})）。

**自定义连接器。** 帮助文档写明 Meta 不审查自定义连接器及其对信息的使用（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。Engadget 引 Meta 称 Muse 可访问任何提供公开 API 的服务，作者让 Muse 指导接通了 Notion（[Engadget：Muse 上手指南]({{< relref "/docs/muse/sources/media/2026-09-12-engadget-getting-started-muse" >}})）；GeekWire 引 Meta 发布材料：有公开 API 就用用户提供的凭证连接，没有 API 时「可以像你一样通过浏览器使用这项服务」（[GeekWire：亚马逊屏蔽 Muse]({{< relref "/docs/muse/sources/media/2026-09-20-geekwire-amazon-blocks-muse" >}})）。社区实测把 Gemini API、Grok CLI 登记为自定义连接器，在 Muse 背后调用其他模型（[Muse 背后调用其他 AI]({{< relref "/docs/muse/sources/community/2026-11-27-emma-backstage-ai-crosscheck" >}})）。

**浏览器兜底与 Chrome 扩展。** 没有连接器时 Muse 退回自己的浏览器，社区普查作者指出这条路径「没有范围屏、没有只读开关」（[56 个连接器普查]({{< relref "/docs/muse/sources/community/2026-10-17-muse-connector-census" >}})）。Chrome 扩展 11-13 被发现上架，11-20 由 Alexandr Wang 正式宣布，据 All Things Muse 转述 Digital Trends，上线一周约 20 万用户，定位是在网站封堵自行到访的智能体之际提供「第二条路径」（[Chrome 扩展正式宣布]({{< relref "/docs/muse/sources/media/2026-11-20-muse-chrome-extension-official-announcement" >}})）。社区分析把扩展和 Poppy 看作方向相反的两种解法：扩展借用户身份让网站察觉不到，Poppy 让网站识别并放行（[Muse 的两个浏览器]({{< relref "/docs/muse/sources/community/2026-11-25-muse-two-browsers" >}})）。

**本机与设备。** Mac 版读 iMessage 需要完全磁盘访问权限加应用内 Messages 连接器（[iMessage 事件详解]({{< relref "/docs/muse/sources/community/2026-10-01-did-muse-read-your-messages" >}})）；安卓拨号、短信工具对商家可代说话，对亲友只拨号，群发只起草（[OpenClaw 同源拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})）。有报道称 Muse 经通知、无障碍等系统权限读到 Signal 消息，这条路径不属于连接器授权（[Signal 消息与通知权限]({{< relref "/docs/muse/sources/community/2026-11-19-muse-signal-notification-permission" >}})，详见 [隐私]({{< relref "/docs/muse/analysis/privacy" >}})）。设备侧见 [设备]({{< relref "/docs/muse/analysis/devices" >}})。

## 授权粒度：读、写、敏感写

开发者指南给出的规则（[连接器指南（开发者）]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})）：

| 工具类别 | 何时询问 | 可选项 |
| --- | --- | --- |
| 读取 | 首次使用时询问，之后每次询问，除非选「始终允许」 | 允许一次 · 始终允许 · 拒绝 |
| 写入，不敏感 | 同上 | 允许一次 · 始终允许 · 拒绝 |
| 写入，敏感（购买、发邮件等） | 每次 | 允许一次 · 拒绝 |

指南还写明，敏感写入「不能被设为始终允许」，包括通过设置或已保存的权限；获批后价格、接收方等细节变了要重新批准。帮助文档称许多连接器可设只读（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）；ITmedia 记录日文版按服务逐个授权、读与写分开、可随时解除（[ITmedia 入门解说]({{< relref "/docs/muse/sources/media/2026-11-22-itmedia-muse-explainer" >}})）；用户实测 Gmail 可设成读邮件允许、发邮件需询问（[VM 探索实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。

这套规则覆盖目录连接器，不覆盖其他路径。卫报报道的 Marketplace 事件里，用户对 Marketplace 消息点了「始终允许」，Muse 随后代回了所有买家消息（[卫报：泄露家庭住址]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})，事件经过见 [安全]({{< relref "/docs/muse/analysis/security" >}})）。QuickBooks、Stripe 等小企业连接器请求的 OAuth 范围，社区作者称在公开资料中找不到（[账本训练模型与三层退出开关]({{< relref "/docs/muse/sources/community/2026-10-19-muse-small-business-data-trains-models" >}})）。

## 目录的扩张：宣布、上架、可用、成交

**数量。** 各时间点的说法口径不同，不能直接比较：

| 时间 | 说法 | 来源与口径 |
| --- | --- | --- |
| 2026-09-08 | 「几十家合作伙伴」 | 官方（[Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})） |
| 2026-09-23 | 新增 Walmart、Best Buy、Gap、Sephora、Wayfair 等十家零售商，Shop Pay、PayPal，Expedia「即将推出」 | 官方（[Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})） |
| 2026-09-30 | 应用内连接器列表里找不到上述十家中任何一家 | 社区核查（[Muse 黑五购物指南]({{< relref "/docs/muse/sources/community/2026-11-13-muse-black-friday-shopping" >}})） |
| 2026-10-17 | 56 个已上线，其中 9 个 Meta 自有；另 6 个已宣布未上线 | 社区转引第三方目录（[56 个连接器普查]({{< relref "/docs/muse/sources/community/2026-10-17-muse-connector-census" >}})） |
| 2026-11-11 | 权限表 52 个连接器、246 个方法 | 用户拆解，未连接真实账户（[Muse 拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})） |
| 2026-11-21 | 一次新增 29 项，总数 143 项；11-17 曾一次新增 19 项 | 用户定期检测，非官方数字（[连接器新增 29 件]({{< relref "/docs/muse/sources/community/2026-11-22-emma-connectors-29-added" >}})） |
| 2026-11-27 | 「已超过 200 个」 | 社区文章一句话，未说明口径（[丸投げ前的规约检查]({{< relref "/docs/muse/sources/community/2026-11-27-emma-marunage-terms-check" >}})） |

普查显示 Google 系有 9 个连接器、Microsoft 只有 Outlook 一个，健康类 5 个；Plaid 只读余额、不转账（[56 个连接器普查]({{< relref "/docs/muse/sources/community/2026-10-17-muse-connector-census" >}})）。这与开发者指南「目前不批准新的金融资金流动工具」一致（[连接器指南（开发者）]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})）。

**地区差异。** 每个新市场都带一批本地连接器，并都注明逐步推出：日本点名 Mercari、Money Forward ME、Ticket Pia（[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})），截至 11-12 只有 Money Forward ME 经其自家公告确认上线，且为只读（[日本连接器 11-12 核查]({{< relref "/docs/muse/sources/community/2026-11-13-japan-november-12-check" >}})）；新加坡有 Shopee、Grab、ShopBack 等八家（[新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}})）；澳大利亚有 Canva、Domain、Kogan 等九家（[Muse 上线澳大利亚]({{< relref "/docs/muse/sources/official/2026-11-17-muse-available-australia" >}})），EFTM 上线首日看到的列表略有不同（[澳大利亚上线实测]({{< relref "/docs/muse/sources/media/2026-11-18-muse-australia-hands-on" >}})）；英国点名 M&S、Sainsbury's、Argos 等 15 家，官方说有的可连个人账户，有的是 Muse「从第一天起就能在它们的网站上找到路」，也就是浏览器操作（[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})）。社区核查称 11-24 没有找到任何英国合作方自己确认上线（[Muse 英国上线核查]({{< relref "/docs/muse/sources/community/2026-11-25-muse-live-uk" >}})）。账户层面也有地区闸门：受限账户看不到对应的连接器，Muse 被要求不说哪些地区有服务（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）；日本账户看到 Walmart、Sweetgreen 显示「不在提供范围内」（[连接器新增 29 件]({{< relref "/docs/muse/sources/community/2026-11-22-emma-connectors-29-added" >}})）。

**购物连接的实际深度。** 各家集成程度差别很大：

| 伙伴 | 截至资料日期的状态 | 来源 |
| --- | --- | --- |
| Shopify | 符合条件的商店可在对话内结账，是最可验证的购物路径 | [Muse 黑五购物指南]({{< relref "/docs/muse/sources/community/2026-11-13-muse-black-friday-shopping" >}}) |
| Instacart | 交接型：Muse 建购物车，付款回 Instacart 应用；仅限美国，无优惠券、会员价 | [Muse 自绘购物车]({{< relref "/docs/muse/sources/media/2026-11-04-muse-instacart-shopping-cart" >}})、[Muse 黑五购物指南]({{< relref "/docs/muse/sources/community/2026-11-13-muse-black-friday-shopping" >}}) |
| Expedia | 11-09 前后上线，只有酒店搜索与预订，取消改签走 Expedia 客服 | [Expedia 接入 Muse]({{< relref "/docs/muse/sources/media/2026-11-09-skift-expedia-live-on-muse" >}}) |
| 沃尔玛 | 11-23 起经 Agent Gateway 对话内结账，用沃尔玛账户的卡，可设 50/100/200 美元等上限 | [沃尔玛网关购物核查]({{< relref "/docs/muse/sources/community/2026-11-23-muse-walmart-agent-gateway" >}})、[沃尔玛与 Muse 的规矩]({{< relref "/docs/muse/sources/media/2026-11-24-walmart-muse-shop-on-its-terms" >}}) |
| Gopuff | 11-24 上线，下单前显示库存与送达时间并请求批准 | [Muse 接入 Gopuff]({{< relref "/docs/muse/sources/media/2026-11-24-muse-gopuff-grocery-delivery" >}}) |
| Loblaw | 11-18 宣布为首个加拿大零售伙伴，称在 Muse 内结账 | [Loblaw 接入 Muse]({{< relref "/docs/muse/sources/official/2026-11-18-loblaw-first-canadian-retail-partner" >}}) |
| Uber Courier | 聊天中安排配送，用户批准后交给 Uber | [Uber Courier 接入]({{< relref "/docs/muse/sources/media/2026-11-10-uber-courier-deliveries" >}}) |

黑五前一天的检索没有找到任何经 Muse 在沃尔玛或 Gopuff 完成的已验证购买；沃尔玛企业公告称 11-24 起可购物，其 Agent Gateway 页面却写着仅限受邀的早期测试版（[黑五购物核查]({{< relref "/docs/muse/sources/community/2026-11-27-museexplained-black-friday-purchase-check" >}})）。

之后出现了两例具名的用户自述，一成一败：

- AI Salon 的作者感恩节夜用约 30 分钟语音对话，让 Muse 在沃尔玛买了两台佳能打印机，税前 168.99 美元。Muse 起初走浏览器结账；作者要求改用能拿到 Muse 首单满 100 返 25 美元优惠的 ShopPay 后，Muse 在扣款前关掉了浏览器结账，请他一键连接 ShopPay，每一步都先征得批准。作者还说明，智能体目前买不了本地门店的优惠，也不能本地配送，订单都经 Walmart.com 从仓库发货（[AI Salon：遛狗时买打印机]({{< relref "/docs/muse/sources/community/2026-11-27-thesalon-muse-walmart-black-friday" >}})）。文中没有写明最终走的是 Agent Gateway 还是 ShopPay 路径。
- CNBC 报道，一位用户 10 月授权 Muse 在 AutoZone 买雨刮，约 17 小时后订单因未说明的错误被取消，Muse 随后建议她自己去亚马逊下单；同一用户让 Muse 找毛绒玩具，Muse 推荐了一家她没听说过、看不到评价的零售商的七五折商品（[CNBC：购物订单被取消]({{< relref "/docs/muse/sources/media/2026-11-28-allthingsmuse-muse-shopping-order-canceled-cnbc" >}})，All Things Muse 转述 CNBC 11-27 报道）。

## 向第三方开放：连接器平台

据 TechCrunch，Wang 在 Connect 上称开放开发者构建连接器后「不到一周」收到超过 1,500 份申请（[TechCrunch：Connect 上的 Muse]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}})）。11-04 的开发者指南把准入条件写得很具体（[连接器指南（开发者）]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})）：

- 连接器必须在工具内完成任务，把用户送去浏览器结账不合格；只包装公开页面或只给链接不够；
- 提交 API 或 MCP 文档、OAuth 凭证或 API 密钥、测试账户，经企业验证和数据处理问卷，分风险评估、逐工具审核、端到端质量检查（含人工）三个阶段；
- 推荐展示是另一项编辑决定；Meta 可要求修改、限制、暂停或移除连接器；涉及用户数据的安全事件须在 48 小时内通知 Meta；
- 金融数据可读，新的资金流动工具暂不批准。

合作方的经济关系资料不多。ShopBack 首席产品官称连接器两周建成，与 Meta 之间没有费用往来，是应邀加入（[ShopBack 接入 Muse 专访]({{< relref "/docs/muse/sources/media/2026-11-11-shopback-justin-lee-why-let-muse-in" >}})）；Meta 旅行负责人称正与旅行公司做更深集成（[Meta 高管谈 Muse 旅行]({{< relref "/docs/muse/sources/media/2026-11-13-meta-travel-integrations-bhatia" >}})）。交易费等商业条款见 [商业与规模]({{< relref "/docs/muse/analysis/business" >}})。

## 平台封堵：亚马逊、银行、零售与航空

**亚马逊。** GeekWire 报道，亚马逊 9-20 切断 Muse 在 Amazon.com 代购的能力，理由是 Meta 未事先告知、智能体浏览时不表明身份、似乎获取并存储顾客凭证；用户看到的弹窗写着「Continued access by an unauthorized AI agent violates Amazon's Conditions of Use」（[GeekWire：亚马逊屏蔽 Muse]({{< relref "/docs/muse/sources/media/2026-09-20-geekwire-amazon-blocks-muse" >}})）。亚马逊同时以自家 Buy for Me 会表明身份作对照（[GeekWire：谁拥有顾客关系]({{< relref "/docs/muse/sources/media/2026-09-22-geekwire-who-owns-customer-relationship" >}})）。Meta 方面的回应各报道说法不一：GeekWire 当时称 Meta 未回应，Digiday 后来称 Meta 拒绝了亚马逊的移除要求，GeekWire 11-17 记录 Meta 称 Muse 看不到密码和支付方式（[GeekWire：亚马逊屏蔽 Muse]({{< relref "/docs/muse/sources/media/2026-09-20-geekwire-amazon-blocks-muse" >}})、[沃尔玛与 Muse 的规矩]({{< relref "/docs/muse/sources/media/2026-11-24-walmart-muse-shop-on-its-terms" >}})、[Muse 默认绕开亚马逊]({{< relref "/docs/muse/sources/media/2026-11-17-do-not-search-amazon" >}})）。

此后的变化：

- 11 月中旬，Muse 的购物技能写入「除非用户要求，否则不要搜索 Amazon」，一般商品改去 Walmart、Target，由 Marketplace Pulse 前后对比发现、GeekWire 复现（[Muse 默认绕开亚马逊]({{< relref "/docs/muse/sources/media/2026-11-17-do-not-search-amazon" >}})）；
- 11-25 TechCrunch 转述 Fortune，两家就让 Muse 直连亚马逊举行多轮会谈，未决的是搜索结果呈现和广告，协议需两家 CEO 批准（[亚马逊或解除 Muse 封锁]({{< relref "/docs/muse/sources/media/2026-11-25-techcrunch-amazon-muse-blockade-talks" >}})）；社区核查指出各家报道都以 Fortune 为唯一来源，没有协议、条款或时间表（[亚马逊 Muse 封锁谈判]({{< relref "/docs/muse/sources/community/2026-11-26-amazon-meta-muse-blockade-talks" >}})）。

**零售商规则不一。** CNBC 11-27 汇总：亚马逊、eBay、美联航、Kohl's 限制或直接封堵智能体，Coach、Gap 只许浏览、不许结账，沃尔玛、丝芙兰向智能体开放（[CNBC：购物订单被取消]({{< relref "/docs/muse/sources/media/2026-11-28-allthingsmuse-muse-shopping-order-canceled-cnbc" >}})）。

**银行与券商。** 嘉信 CEO 在 Bloomberg 采访中点名 Muse，称拦截试图转移客户资金的未经授权智能体，同时准备提供只读的 MCP 通道（[Bloomberg：嘉信理财拦截 Muse]({{< relref "/docs/muse/sources/media/2026-10-16-bloomberg-schwab-blocks-muse" >}})）。加拿大皇家银行 10-27 通知员工封堵第三方个人智能体直接访问网银，一天内 TD、BMO、Scotiabank、CIBC 跟进（[加拿大银行封堵智能体]({{< relref "/docs/muse/sources/media/2026-11-02-canada-banks-block-agents" >}})，All Things Muse 汇总 Bloomberg 等报道）。WIRED 记录美国银行提醒客户：把登录信息交给 AI 助手，要对由此产生的活动负责（[WIRED：颠覆尚未发生]({{< relref "/docs/muse/sources/media/2026-10-31-wired-muse-commerce-reality-check" >}})）。

**零售与平台。** The RealReal 在 Verge 作者让 Muse 反复占住购物车后收紧机器人防御（[RealReal 收紧防御]({{< relref "/docs/muse/sources/media/2026-10-30-realreal-tightens-bot-defenses" >}})）；The Verge 记录 eBay 11 月起阻止 Muse 浏览，eBay 称是「选择性」限制而非全面禁令（[eBay 限制第三方智能体]({{< relref "/docs/muse/sources/media/2026-11-10-ebay-blocks-third-party-ai-agents" >}})）。沃尔玛是反例：早期用户在结账时被人机验证拦下，沃尔玛对 TechCrunch 称并非有意（[Sitedex：网站如何识别 Muse]({{< relref "/docs/muse/sources/community/2026-11-01-sitedex-muse-for-site-owners" >}})）；它随后自建网关（见下节）。据社区转述 Jefferies 报告，测试的数百家美国主要购物、旅行网站约三分之一直接封禁、三分之一质询或限制（[智能体购物的禁区]({{< relref "/docs/muse/sources/community/2026-10-30-muse-where-sites-block-your-agent" >}})，数字为二手）。

**航空。** 美联航 11-11 修订运输合同，把「AI Agent」定义为无论旅客是否监督或批准，禁止其订票、改票，CBS、CNBC 点名 Muse 与 OpenAI Dots（[美联航禁智能体订票]({{< relref "/docs/muse/sources/community/2026-11-13-united-bans-agent-booking" >}})、[美联航首个源站禁令]({{< relref "/docs/industry/sources/community/2026-11-12-muleai-united-origin-site-ban" >}})）。同一篇社区资料称达美允许经认证的 AI 助手预订，与 10 月中文媒体所说达美「禁止智能体代订机票」不同（[美联航禁智能体订票]({{< relref "/docs/muse/sources/community/2026-11-13-united-bans-agent-booking" >}})、[Agent 遭集体拉黑]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})），可能是政策变了，也可能是转述有误。

**身份问题。** 截至 11-01，Muse 没有公布 user agent、IP 段或签名（[Sitedex：网站如何识别 Muse]({{< relref "/docs/muse/sources/community/2026-11-01-sitedex-muse-for-site-owners" >}})）；11-07 至 11-09 之间它把 Web Bot Auth 签名迁到 muse.ai（[Muse 占智能体请求 59%]({{< relref "/docs/muse/sources/community/2026-11-15-verify-muse-web-bot-auth-signatures" >}})），但签名只标识 Muse、不标识用户（[检测 Muse 请求]({{< relref "/docs/muse/sources/community/2026-10-14-detect-muse-ai-agent" >}})）。这条线的细节见 [安全]({{< relref "/docs/muse/analysis/security" >}})。

推断：封堵理由集中在三点——不表明身份、持有用户凭证、绕开平台自己的广告和客户关系。前两点是浏览器路线本身的问题，签名、Poppy 和商家通道能部分解决；第三点是利益问题。亚马逊谈判卡在广告、嘉信只开放只读通道，说明技术手段消除不了这一层。

## 协议与商家通道：Poppy、Agent Gateway、智能体对智能体

**Poppy（Personal Agent Protocol）。** Sierra 10-06 宣布协议，伙伴有 Meta、Genesys、Instinct、Rocket、Shopify、Stripe、Walmart，基于 OAuth，支持网站、API（MCP/OpenAPI）、商家智能体三种路径（[Poppy 协议发布]({{< relref "/docs/industry/sources/community/2026-10-06-introducing-personal-agent-protocol" >}})）。11-13 发布 1.0：商家在 `/.well-known/poppy.json` 说明接入方式，用户在商家页面经 OAuth 授权、智能体不接触密码，Muse 称自己是首个支持 Poppy 的个人智能体（[Poppy 协议 1.0 发布]({{< relref "/docs/muse/sources/official/2026-11-13-poppy-personal-agent-protocol" >}})）；Sierra 称 Poppy 已对所有 Muse 用户开启，Muse 访问每个网站时优先查找 Poppy，Shopify 自动为每家商店发布 Poppy 文件，设计伙伴超过 100 家（[Poppy 1.0 发布]({{< relref "/docs/industry/sources/community/2026-11-13-releasing-personal-agent-protocol-1-0" >}})）。

落地核查显示协议与实际部署之间仍有距离：

- 11-14 核查 9 家 Shopify 店铺：poppy.json 内容相同、`protocol_version` 为 0.4，只授予以登录顾客身份准备结账一项权限，没有查订单、退货等（[Poppy 文件实地核查]({{< relref "/docs/industry/sources/community/2026-11-14-shopify-poppy-file-live-check" >}})）；
- 1.0 没有解决支付，UCP 是结账协议而不是支付方式；协议自家演示站点 11-15 返回 Not Found（[poppy.json 内容核查]({{< relref "/docs/muse/sources/community/2026-11-15-poppy-json-inside" >}})）；
- 截至 11-15，没有 Poppy 在 Muse 应用内的实证；Mercury、土耳其航空、Synchrony 三个首批案例的措辞强弱不一，Hertz、BYLT 都是「将能够」（[Poppy 1.0 落地核查]({{< relref "/docs/muse/sources/community/2026-11-14-poppy-first-sierra-ledger" >}})）。

社区作者认为 Poppy 的分量在分发——Muse 预装优先查找、Shopify 默认发布——而不在协议本身（[从智能体一侧读 Poppy 1.0]({{< relref "/docs/industry/sources/community/2026-11-20-muleai-poppy-from-agent-side" >}})）。

**沃尔玛 Agent Gateway。** 沃尔玛用 MCP 网关接 Muse，理由是浏览网站的智能体走为人设计的步骤「缓慢且容易出错」（[沃尔玛连接器与 Sparky 分工]({{< relref "/docs/muse/sources/community/2026-11-22-walmart-connector-sparky-cart" >}})）。截图显示的分工是：Muse 负责查商品、建购物车、下单，沃尔玛自家助手 Sparky 只回答问题、不改动任何东西（[沃尔玛连接器与 Sparky 分工]({{< relref "/docs/muse/sources/community/2026-11-22-walmart-connector-sparky-cart" >}})）；Retailgentic 实测称这是首个同时有买方智能体和卖方智能体的连接器，设置里有「agent budget」和「Allow Muse to shop」开关（[沃尔玛连接器初体验]({{< relref "/docs/muse/sources/community/2026-11-24-retailgentic-muse-walmart-first-look" >}})）。Agent Profile 让智能体购买单独显示、可设上限、拿不到卡信息（[沃尔玛网关购物核查]({{< relref "/docs/muse/sources/community/2026-11-23-muse-walmart-agent-gateway" >}})）。

**商家智能体直连。** Decagon 11-13 宣布 Hertz 试点，Muse 不打电话、不开网页，而是把请求发到 Hertz 的个人智能体专属通道，由 Hertz 的 Decagon 智能体按既有流程处理（[Hertz 接入 Muse]({{< relref "/docs/industry/sources/community/2026-11-13-hertz-decagon-gateway-muse" >}})）。另据社区资料，Muse 没有原生 A2A 客户端，对 Google AP2 也未公布支持（[智能体间互操作]({{< relref "/docs/muse/sources/community/2026-11-17-agent-to-agent-interop" >}})）。

推断：从浏览器代操作转向商家自建通道，商家拿回了开放哪些操作、怎么定价、要不要做身份验证的控制权，Muse 能做的事也因此取决于每家商家的意愿。沃尔玛接入时把 Sparky 放进流程、Shopify 只开放结账，都说明商家开放的是对自己有利的那部分。

## 资料缺口

- 官方连接器总数和目录页；各国可用清单；「逐步推出」的本地连接器实际上线日期（日本 Mercari、Ticket Pia，英国各合作方）。
- 经沃尔玛、Gopuff、Loblaw 完成的订单，目前只有个别用户自述，没有平台或第三方的统计；AI Salon 那笔订单最终走的是哪条结账路径；沃尔玛网关「仅限受邀」与「11-24 起可购物」两种说法的关系。
- Poppy 在 Muse 应用内的实际行为；Shopify 何时把 poppy.json 升到 1.0、开放订单类权限；Mercury、土耳其航空、Hertz 的用户实测。
- 小企业连接器（QuickBooks、Stripe 等）的 OAuth 范围；自定义连接器的安全边界和凭证存放的官方说明。
- 亚马逊谈判的第二个独立来源；Meta 对亚马逊封堵和「不要搜索 Amazon」技能的正式回应。
- 达美对第三方智能体的现行政策原文；美联航运输合同 Rule 5.H、6.J.6 原文。
- 开发者平台的审核通过率、审核周期，以及 1,500 份之后的申请数量。

## 主要资料

官方

- [帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})：连接方式、只读、自定义连接器不审查。
- [我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})：目录连接器的权限分离实现。
- [连接器指南（开发者）]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})：读/写/敏感写三档、审核流程、金融工具限制。
- [Poppy 协议 1.0 发布]({{< relref "/docs/muse/sources/official/2026-11-13-poppy-personal-agent-protocol" >}})：Poppy 1.0 的 Meta 一侧说明与首批案例。
- [Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})、[新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}})、[Muse 上线澳大利亚]({{< relref "/docs/muse/sources/official/2026-11-17-muse-available-australia" >}})、[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})、[Loblaw 接入 Muse]({{< relref "/docs/muse/sources/official/2026-11-18-loblaw-first-canadian-retail-partner" >}})：Connect 与各国上线的连接器名单。

媒体

- [GeekWire：亚马逊屏蔽 Muse]({{< relref "/docs/muse/sources/media/2026-09-20-geekwire-amazon-blocks-muse" >}})、[GeekWire：谁拥有顾客关系]({{< relref "/docs/muse/sources/media/2026-09-22-geekwire-who-owns-customer-relationship" >}})、[Muse 默认绕开亚马逊]({{< relref "/docs/muse/sources/media/2026-11-17-do-not-search-amazon" >}})、[亚马逊或解除 Muse 封锁]({{< relref "/docs/muse/sources/media/2026-11-25-techcrunch-amazon-muse-blockade-talks" >}})：亚马逊封堵的理由、Muse 的绕行与谈判。
- [Bloomberg：嘉信理财拦截 Muse]({{< relref "/docs/muse/sources/media/2026-10-16-bloomberg-schwab-blocks-muse" >}})、[加拿大银行封堵智能体]({{< relref "/docs/muse/sources/media/2026-11-02-canada-banks-block-agents" >}})：嘉信与加拿大银行的封堵。
- [CNBC：购物订单被取消]({{< relref "/docs/muse/sources/media/2026-11-28-allthingsmuse-muse-shopping-order-canceled-cnbc" >}})：AutoZone 订单被取消、各零售商的智能体规则。
- [eBay 限制第三方智能体]({{< relref "/docs/muse/sources/media/2026-11-10-ebay-blocks-third-party-ai-agents" >}})、[RealReal 收紧防御]({{< relref "/docs/muse/sources/media/2026-10-30-realreal-tightens-bot-defenses" >}})：eBay、The RealReal 的限制。
- [Muse 自绘购物车]({{< relref "/docs/muse/sources/media/2026-11-04-muse-instacart-shopping-cart" >}})、[Expedia 接入 Muse]({{< relref "/docs/muse/sources/media/2026-11-09-skift-expedia-live-on-muse" >}})、[Muse 接入 Gopuff]({{< relref "/docs/muse/sources/media/2026-11-24-muse-gopuff-grocery-delivery" >}})、[沃尔玛与 Muse 的规矩]({{< relref "/docs/muse/sources/media/2026-11-24-walmart-muse-shop-on-its-terms" >}})：Instacart、Expedia、Gopuff、沃尔玛的集成深度。
- [Chrome 扩展正式宣布]({{< relref "/docs/muse/sources/media/2026-11-20-muse-chrome-extension-official-announcement" >}})：Chrome 扩展。
- [TechCrunch：Connect 上的 Muse]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}})、[ShopBack 接入 Muse 专访]({{< relref "/docs/muse/sources/media/2026-11-11-shopback-justin-lee-why-let-muse-in" >}})：开发者申请数与合作方视角。

社区

- [56 个连接器普查]({{< relref "/docs/muse/sources/community/2026-10-17-muse-connector-census" >}})、[连接器新增 29 件]({{< relref "/docs/muse/sources/community/2026-11-22-emma-connectors-29-added" >}})：连接器普查与目录新增的实测数。
- [Muse 黑五购物指南]({{< relref "/docs/muse/sources/community/2026-11-13-muse-black-friday-shopping" >}})、[黑五购物核查]({{< relref "/docs/muse/sources/community/2026-11-27-museexplained-black-friday-purchase-check" >}})：宣布与可用、成交之间的核查。
- [AI Salon：遛狗时买打印机]({{< relref "/docs/muse/sources/community/2026-11-27-thesalon-muse-walmart-black-friday" >}})：沃尔玛下单的一手自述，浏览器结账与 ShopPay 两条路径的切换。
- [沃尔玛连接器与 Sparky 分工]({{< relref "/docs/muse/sources/community/2026-11-22-walmart-connector-sparky-cart" >}})、[沃尔玛网关购物核查]({{< relref "/docs/muse/sources/community/2026-11-23-muse-walmart-agent-gateway" >}})、[沃尔玛连接器初体验]({{< relref "/docs/muse/sources/community/2026-11-24-retailgentic-muse-walmart-first-look" >}})：沃尔玛连接器的分工与首次实测。
- [美联航禁智能体订票]({{< relref "/docs/muse/sources/community/2026-11-13-united-bans-agent-booking" >}})：美联航合同条款。
- [Poppy 1.0 落地核查]({{< relref "/docs/muse/sources/community/2026-11-14-poppy-first-sierra-ledger" >}})、[poppy.json 内容核查]({{< relref "/docs/muse/sources/community/2026-11-15-poppy-json-inside" >}})、[Poppy 文件实地核查]({{< relref "/docs/industry/sources/community/2026-11-14-shopify-poppy-file-live-check" >}})、[从智能体一侧读 Poppy 1.0]({{< relref "/docs/industry/sources/community/2026-11-20-muleai-poppy-from-agent-side" >}})：Poppy 落地核查与解读。
- [Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})、[Muse 内部架构剖析]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})：工具实现与凭证代换。
- [Muse 的两个浏览器]({{< relref "/docs/muse/sources/community/2026-11-25-muse-two-browsers" >}})：Chrome 扩展与 Poppy 的对照。
- [Poppy 协议发布]({{< relref "/docs/industry/sources/community/2026-10-06-introducing-personal-agent-protocol" >}})、[Poppy 1.0 发布]({{< relref "/docs/industry/sources/community/2026-11-13-releasing-personal-agent-protocol-1-0" >}})、[Hertz 接入 Muse]({{< relref "/docs/industry/sources/community/2026-11-13-hertz-decagon-gateway-muse" >}})：Sierra 与 Decagon 的协议、试点公告。

实测

- [我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})：连接器与 MCP 的关系、Gmail 分项授权。
