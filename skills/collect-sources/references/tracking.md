# 跟踪清单

## 什么算 Personal Agent

长期服务于一个人，理解其上下文，并能受托推进任务的智能体。个人生活与个人工作都在范围内。判断时看五个方面，不要求全部具备：

| 方面 | 问题 |
| --- | --- |
| 个人上下文 | 能否接入个人文件、邮件、日历等数据，保留跨会话的偏好与记忆 |
| 实际执行 | 能否操作应用、浏览器或电脑，交付结果或完成服务 |
| 持续运行 | 用户离开后能否继续工作，是否支持定时或事件触发 |
| 长期委托 | 能否持续跟进目标、处理变化，并在需要时主动联系用户 |
| 用户控制 | 权限、凭证、支付、对外通信与审计如何设计 |

纯编程助手、企业智能体开发平台、纯陪伴产品不在范围内。新产品是否纳入由用户决定。

## 关注重点

这份笔记分析的是 Personal Agent 的技术实现，以及围绕技术实现的产品形态和商业模式。筛选资料时，优先收能说明「它怎么工作、做成什么样、怎么收费和扩张」的内容。

## 不收的资料类型

- 法律类文档：服务条款、隐私政策、开发者或平台条款、隐私声明等，一律不收。帮助文档中引用条款的句子照常保留，链接保留。
- 没有实证的说法：个人在社交媒体或论坛上的说法（如「我的智能体擅自发了邮件」），一手帖子或证据取不到，只能看到聚合站、SEO 站的转述，且厂商未确认的，不收，也不建占位页（用户 2026-11-04 决定）。这一条不影响二手报道的收录：一手出处是可靠媒体、只是无法读取时，仍按 source-page.md 的「二手报道」规则收，填写 `basedOn`。
- 边缘资料：从已收资料中链接出去、只补充操作细节的子页面（如计费、取消订阅等通用帮助页），以及代码仓库子目录的 README，默认不收。确有新信息时在报告中列出，由用户决定。

## 音视频资料

播客、视频、演讲等音视频资料，只有在有官方文字稿（或节目页本身就是完整文字）时才收，按文字稿全文存档，`fidelity` 用「字幕整理」或「全文」。没有文字稿的不收，不自行转写音频。节目页只有导语和要点的，按节目页文字收，并在 `dateNote` 说明不含完整访谈。

## 占位

已知存在、但内容尚未发布或尚未取得的资料（如尚未举行的演讲、待补全的横评），可以先建「仅链接」页面占位，`date` 按已知信息填写并在 `dateNote` 说明，之后取得内容时补全。

## 模型资料的收录原则

这份笔记只关注 Personal Agent，不关注模型本身。模型发布、模型卡、基准评测等资料，只有在明确与 Personal Agent 相关时才收录，例如：

- 文章说明模型为 Personal Agent 做了优化，或专门用于驱动某个 Personal Agent 产品。
- 文章说明 Personal Agent 在运行时如何选择或切换模型，例如按任务类型、订阅档位或设备选用不同模型。

只介绍模型能力、跑分、开放权重、API 价格的文章不收，即使模型与某个 Personal Agent 同名或同属一家厂商。文章只顺带一句提到某个 Personal Agent 的，也不收，在本轮报告中列出，由用户判断。

所有产品都遵循这条原则；产品 skill 只能在此基础上列出具体判断，不能放宽。

## 跟踪的产品

每个产品的来源渠道、抓取方法、收录范围、已知问题和最后收集日期，写在该产品自己的 skill 中。收集某个产品时，先读它的 skill。

| 目录 | 产品 | 厂商 | 产品 skill |
| --- | --- | --- | --- |
| muse | Meta Muse | Meta | `skills/collect-muse/SKILL.md` |
| dots | OpenAI dots | OpenAI | `skills/collect-dots/SKILL.md` |
| claude-duet | Claude Duet | Anthropic | `skills/collect-claude-duet/SKILL.md` |
| grok-bot | Grok Bot | SpaceXAI（xAI），经 Cursor 交付 | `skills/collect-grok-bot/SKILL.md` |
| manus-cue | Manus Cue | Manus（Butterfly Effect） | `skills/collect-manus-cue/SKILL.md` |
| lingguang | 蚂蚁灵光（2.0 起） | 蚂蚁集团 | `skills/collect-lingguang/SKILL.md` |
| today | Today AI | 齐俊元创办的初创公司（汇翮智能 / TODAY AI PTE. LTD.） | `skills/collect-today/SKILL.md` |
| gemini-spark | Gemini Spark（2026-10 起称 Task） | Google | `skills/collect-gemini-spark/SKILL.md` |
| instinct | Instinct | Spear Street Technology（创始人 Noah Shinn） | `skills/collect-instinct/SKILL.md` |
| workbuddy | WorkBuddy | 腾讯（CodeBuddy 团队） | `skills/collect-workbuddy/SKILL.md` |
| microsoft-autopilot | Microsoft Autopilot（原 Scout） | 微软 | `skills/collect-microsoft-autopilot/SKILL.md` |
| poke | Poke | The Interaction Company of California（2026-07 起加入 Cognition） | `skills/collect-poke/SKILL.md` |

新增产品时：用户同意纳入后，按 [product-skill-template.md](product-skill-template.md) 新建 `skills/collect-<product>/SKILL.md`，在上表加一行，再按 section-templates.md 建目录。

## 已评估、未纳入的产品

用户判定不收的产品记在这里，避免重复评估。产品形态有重大变化时再重新判断。

| 产品 | 厂商 | 决定日期 | 原因 |
| --- | --- | --- | --- |
| Super-agent | DeepSeek（Harness 团队） | 2026-11-06 | 研发向的 Agent 架构设计与开源原型（dsh-superagent），面向代码仓库与团队，无个人上下文，非面向个人的产品 |
| 千问Go | 阿里 | 2026-11-06 | 用户决定不收。评估依据为国内综述（搜狐「2026中国个人AI智能体创新企业TOP10」）：内测中，能自动处理航班理赔、购物价保等事务；未查官方资料 |
| DuMate（百度搭子） | 百度 | 2026-11-06 | 用户决定不收。仅在综述（文学城 2026-10-23「个人智能体扎堆上线」）中出现名字，无细节；未查官方资料 |
| 豆包手机助手 | 字节跳动 × 努比亚 | 2026-11-06 | 用户决定不收。系统级手机助手，第一代工程样机 2025-12 上线（据文学城 2026-10-23 综述）；未查官方资料 |
| OpenClaw 及云端托管版 | 开源项目；云端版来自阶跃、智谱、网易有道、月之暗面、字节等 | 2026-11-06 | 用户决定不收。开源本地 Agent 程序及各家 7×24 小时云端托管版，对接微信、飞书；厂商多、版本分散（据搜狐 TOP10 综述）；未查官方资料 |

## 行业综合（industry）

- 检索词：`personal AI agent comparison`、`AI agent tested`、`个人智能体 对比`、`个人智能体 评测`
- 收录条件：比较或评测两个及以上跟踪产品，或讨论 Personal Agent 整体的形态、架构与安全。
- 最后收集日期：2026-11-09（收集 Poke 时补收 TechCrunch 短信类智能体合集 2026-10-24，涉及 Poke 与 Instinct，取自 Wayback 快照）；2026-11-07（本轮补收 Top5Apps 五款个人智能体横评，更新 2026-11-01）；2026-11-06（本轮补收 Enterpret 12 款智能体用户排名，2026-11-03；对照旧笔记补收 ChatPRD 四款智能体九项任务对比、iThome 五款主动型 Agent 比较；本轮补收 DataCamp 10-27 横评、Medium 11-03 六产品横评（仅链接）；本轮补收 freistyle 六产品横评、老张入门成本对比、Kunal 收件箱实测（仅链接））；2026-11-05（9 篇「仅链接」占位已补抓原文，CNBC 2026-10-31 仍取不到；新收 Tom's Guide、Engadget 对比文）；同日另收用户发来的微信公众号文章 4 篇（36氪Pro、灵螺创新、易论AI、AI故事计划），以及中金点睛、特工宇宙、量子位 3 篇，Datawhale、图灵米洛伊、机器之心、AI产品阿颖、AI应用与大模型、明义价值观、甲子光年 7 篇；再收 Z Finance、小王AI课、飞雪谈AI、有味道的黑咖啡、大语言模型、AI站姐 6 篇；第四批 15 篇（程序员鱼皮、AGENT2048、阿里技术、K姐研究社、鲸选AI、生活有变量、周某人随笔、AI新榜、AIX财经、潮涌AI、AppGrowing、PM九筒、湾区OPC指南、奈势AI、大数据分析与应用）
