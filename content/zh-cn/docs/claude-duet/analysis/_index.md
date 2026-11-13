---
title: "Claude Duet 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Claude Duet 是 Anthropic 2026-10-21 推出的研究预览：一款独立的手机应用，让 Claude 作为主动型智能体在云端工作，沿用用户 Claude 账号的上下文，面向专业人士和小企业主；分析覆盖截至 2026-11-12 收集的 12 篇 Duet 资料和 17 篇涉及 Duet 的行业资料。
---

## 概要

- Duet 不另起炉灶，而是把用户已有的 Claude 账号变成一个主动型智能体：记忆、技能、6,000 多个连接器和插件、历史聊天都直接沿用，「从第一条消息起就已就位」。评测者认为它晨报和会议准备做得好，主要靠这些继承来的上下文；但本地技能、本地 Claude Code 会话和本机文件够不到。（[记忆与上下文](memory/)、[连接器](connectors/)）
- 在云端自己的计算机上工作，浏览器另放在一台专用虚拟机里，智能体只能用固定命令操作它。用户看不到、也不能接管这个浏览器，这是它与 Muse、Dots 最明显的差别。（[运行环境](runtime/)）
- 「主动」是每天一份晨报加每隔几小时一次巡检，官方称这是与 Claude 的核心区别。巡检频率受套餐限额约束，评测者普遍认为它发现问题好、跟进偏安静。（[持续执行](continuous-execution/)）
- 安全设计是官方资料中写得最细的部分：三层审批，模型之外有两个分类器，凭证不进入智能体所在的机器，付款用一次性卡，证券交易和转账即使批准也不做。官方自承审批疲劳是「严重问题」，实测中它请求权限确实比别家多。截至 2026-11-12 没有漏洞或事件报道。（[安全](security/)）
- 开放面最窄：研究预览，只通过候补名单开放给美国的 Pro、Max、Ultra 订阅者。不另收费，但后台工作与聊天共用限额，官方为此发放限额重置，口径在 11 月改过一次。（[开放与价格](access-pricing/)）
- 入口只有独立应用（以手机为主），不打电话、不发短信，对外只能经批准从用户账号发邮件。界面被 WIRED 评为六款中最好，但只能单人使用。（[交互渠道](channels/)）
- 实测评价多在中游：读、起草、发现问题强，动作推进、个人杂事和购物弱，速度慢，上下文稀薄时会编造。多名评测者没有把它当作主力智能体。（[实际效果与可靠性](reliability/)）

## 定位

官方称 Duet 让 Claude「作为主动型智能体（proactive agent）工作」：把需要关注的事带给用户，完成交代的任务，用户离开后继续工作，代表用户行动前先确认；它是为「工作繁忙、事情多到难以追踪的专业人士和小企业主」打造的，核心功能围绕工作构建（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。产品页用一句话说明与 Claude 的区别：「Claude 等你打开对话，Claude Duet 会来找你」（[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})）。安全文章称研究预览的目的是了解用户在个人智能体中看重什么，Anthropic 团队自己每天在用（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。

Duet 是独立应用，与主 Claude 应用分开；官方称早期用户的反馈将决定两者如何协同（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。它也不同于 9 月 16 日并入主 Claude 应用的 Cowork（[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

官方示例和合作方都偏经营：查未付发票并起草提醒、准备薪资、发合同、做简报和仪表盘；试用者包括房产经纪人、约 110 名员工的餐饮店店主（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})、[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})）。Stripe 新闻稿同样面向「小企业主和专业人士」（[Stripe 新闻稿]({{< relref "/docs/claude-duet/sources/official/2026-10-21-stripe-link-and-stripe-mcp" >}})）。

与其他跟踪产品相比，第三方资料中的主要差异是：

| 对比对象 | 差异 | 资料 |
| --- | --- | --- |
| OpenAI Dots | 形态最接近（常驻智能体、云电脑、已用应用的记忆），差别在谁发起对话、能看到什么：Duet 按日程主动找人，Dots 的电脑可打开接管 | [LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}}) |
| Meta Muse | 都会先给用户发消息、都用 Link 一次性卡付款；Duet 为工作而造、需付费 Claude 套餐、仅美国受邀，Muse 偏生活杂事、免费起步、多国开放、可接管浏览器 | [LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}}) |
| Grok Bot | Duet 是一个线程而不是一队 Bot，不能接管；多名评测者认为 Grok Bot 仍是更强的工作智能体 | [LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})、[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}}) |
| Instinct | Instinct 能发短信、打电话，被认为更主动，Aakash 仍首选它 | [Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}}) |

国内资料把 Duet 与 Dots、Grok Bot 归为「大模型公司」一类，与依托自有生态的平台型产品（Muse 等）相对；AIX财经认为模型公司做 Personal Agent 是为了避免退化为后台供应商，从工作场景切入是因为工作软件多开放接口（[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。中国新闻周刊称 Duet「瞄准的是日常公务」（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）。Aakash 则把 Duet 归为兼顾工作和生活的「统一型智能体」，他的建议是「生活在 Claude 里」的人用 Duet（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。多位作者的选择原则相同：选已经拥有你数据的那一款（[Freistyle AI：小企业六款对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-09-16 | Cowork 并入主 Claude 应用（Duet 之前 Anthropic 的相关动作） | [aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) |
| 2026-10-21 | 发布研究预览：候补名单，美国订阅者，iOS、Android 与 claude.ai，Claude Opus 5.5；Stripe 同日宣布 Link 智能体钱包与 Stripe MCP 集成进 Duet | [推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})、[发布说明]({{< relref "/docs/claude-duet/sources/official/2026-10-21-relnotes-claude-duet-research-preview" >}})、[Stripe 新闻稿]({{< relref "/docs/claude-duet/sources/official/2026-10-21-stripe-link-and-stripe-mcp" >}}) |
| 2026-10-23 | 发布安全、隐私与安全性文章；发布稿文首加注 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})、[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}}) |
| 2026-10-27 | WIRED 刊出六款智能体同日测试，称在 Duet 发布约一天后测试，评为「最佳界面」 | [WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}}) |
| 2026-10-28 | Shopify Fall '26 版把 Shop Pay 结账开放给智能体，Duet 为首批四个之一（转述 The Defiant） | [All Things Muse：Shop Pay]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}}) |
| 2026-10-29 | 首批候补名单用户陆续收到邀请（Alarcon 加入后等了八天） | [Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}}) |
| 2026-10-30 | Max 5x 改名为 Max、Max 20x 改名为 Ultra，价格不变 | [Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}}) |
| 2026-11-04 | Link、Shop Pay 两篇帮助页最后修改（页面不标发布日期） | [帮助：Link]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-link-by-stripe-with-claude-duet" >}})、[帮助：Shop Pay]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-shop-pay-with-claude-duet" >}}) |
| 2026-11-10 前后 | 帮助文档更新：限额重置改为 Pro 三次、Max 与 Ultra 各一次，12-15 过期；Duet 中不提供 Personal Finance | [帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}}) |
| 已宣布未上线 | 1Password 登录、Shopify 可视化编辑器（「即将推出」）；Team 与 Enterprise、美国以外地区（无日期） | [推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}}) |

## 整体架构

用户在手机上的 Duet 应用里与它交流：一个主线程加多个频道，频道共享同一份记忆，打字或语音输入（[交互渠道](channels/)）。上下文全部来自用户的 Claude 账号：记忆、技能、连接器、历史聊天，Duet 自己保留对话历史和记忆直到用户删除或重置（[记忆与上下文](memory/)）。智能体在 Anthropic 云端自己的计算机上运行，用户设备可以关着；需要上网时操作另一台专用虚拟机里的浏览器，只能下固定命令，网站 Cookie 和解密后的密码都只在那台机器上（[运行环境](runtime/)）。

它每天早上发晨报，每隔几小时巡检已连接的账号，在任务标签页跟踪进行中的工作（[持续执行](continuous-execution/)）。外部服务走 Claude 的连接器和插件，没有连接器的网站走云端浏览器，付款走 Link 或 Shop Pay 的一次性卡（[连接器](connectors/)）。每次操作都经过模型之外的意图检查，每条外发消息经过敏感信息分类器；发送、付款、删除等动作出审批卡，部分动作每次都要再问，证券交易和转账一律不做（[安全](security/)）。用量全部计入用户的 Claude 套餐限额（[开放与价格](access-pricing/)）。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境](runtime/) | 云端计算机加一台专用浏览器虚拟机，模型只能用固定命令驱动浏览器；用户看不到、不能接管，Duet 也看不到本机；规格与持久化未公布 |
| [记忆与上下文](memory/) | 直接沿用 Claude 账号的记忆、技能、连接器和历史聊天；断开应用不删除已了解的内容；本地技能和 Claude Code 会话带不过来 |
| [持续执行](continuous-execution/) | 晨报加每隔几小时巡检，等待批准时先做完其余部分；发现问题好，跟进偏安静 |
| [连接器](connectors/) | 沿用 Claude 的 6,000 多个连接器和插件，付款走只在 Duet 中提供的 Link 与 Shop Pay；Microsoft 365 尚不可用；Claude 连接器之外基本停住 |
| [交互渠道](channels/) | 独立应用，以手机为主，主线程加频道；不打电话、不发短信；界面评价最好，只能单人用 |
| 设备 | —。资料不足：官方列出 iOS、Android 与 claude.ai，候补名单要选手机类型；桌面端说法不一（TestFlight 版没有，另有用户提到桌面应用和本地主机访问）；没有专用硬件。见[交互渠道](channels/)、[运行环境](runtime/) |
| 模型 | —。资料不足：官方称由 Claude Opus 5.5 驱动、围绕它设计，用户不能选模型，也不能选投入程度，由 Duet 自己决定（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})、[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。有用户觉得它在 Duet 里比在其他 Claude 界面快，推测做了调优（[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})）；有评测者认为固定 Opus 对习惯用 Sonnet 跑大量任务的人是「一项不幸的成本」（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})） |
| [安全](security/) | 三层审批、模型之外的两个分类器、凭证不进智能体机器、一次性卡；官方自承审批疲劳，实测请求权限偏多；无事件报道 |
| 隐私 | —。资料不足：对话历史和记忆保留到用户删除或重置，删除账号清除全部（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）；官方 Duet 资料没有说明是否用于训练、保存多久，第三方称遵循 Claude 账户的训练设置（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})），也有作者写「Duet 页面未说明」（[Freistyle AI：小企业六款对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）；对他人信息只有外发分类器一项说明。见[记忆与上下文](memory/)、[安全](security/) |
| [开放与价格](access-pricing/) | 美国 Pro、Max、Ultra 订阅者候补名单；不另收费但共用限额；限额重置口径 11 月改过；预览后定价未公布 |
| 商业与规模 | —。资料不足：官方没有公布用户数、邀请人数、付费或成本数据，资料库中也没有第三方估算。商业上可见的只有目标用户（专业人士和小企业主）和支付合作（Stripe Link 已为 200 多个个人智能体提供支付，Shopify Shop Pay），见[连接器](connectors/)。生活有变量认为工作场景更容易建立付费理由（[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})） |
| [实际效果与可靠性](reliability/) | 六七份早期实测，多在中游；晨报、会议准备、发现问题、编程好，推进、跟进、购物差，慢，会编造 |

## 资料缺口

- **媒体报道**：资料库中没有任何一篇以 Duet 为主题的媒体报道，`media/` 目录为空，Duet 只在 WIRED、AIX财经、中国新闻周刊等的多产品文章中出现。
- **用户实测**：没有 `exploration/` 资料；运行环境的规格、持久化、用量消耗都没有第一手数据。
- **规模与商业**：用户数、邀请发放进度、留存，研究预览后的定价。
- **隐私条款**：训练数据、保存期限、他人信息的处理，Duet 专门的隐私说明。
- **安全**：外部渗透测试结论、分类器误判率、选择阻止 Duet 的网站名单；独立研究者的测试。
- **产品演进**：1Password 登录、Team 与 Enterprise、美国以外地区、Microsoft 365 的上线；Duet 与主 Claude 应用、Cowork 的关系如何演变。
- **长期使用**：发布一个月以上的体验和复测。

## 主要资料

- 官方：[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})、[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})、[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})、[帮助：Link]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-link-by-stripe-with-claude-duet" >}})、[帮助：Shop Pay]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-shop-pay-with-claude-duet" >}})、[Stripe 新闻稿]({{< relref "/docs/claude-duet/sources/official/2026-10-21-stripe-link-and-stripe-mcp" >}})、[发布说明]({{< relref "/docs/claude-duet/sources/official/2026-10-21-relnotes-claude-duet-research-preview" >}})
- 媒体：[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})、[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})、[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})、[财经网科技]({{< relref "/docs/industry/sources/media/2026-11-06-caijingwang-transaction-management" >}})、[All Things Muse：Shop Pay]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}})
- 社区：[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})、[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})、[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})、[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})、[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[Freistyle AI：小企业六款对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})、[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})、[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})
