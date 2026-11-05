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

新增产品时：用户同意纳入后，按 [product-skill-template.md](product-skill-template.md) 新建 `skills/collect-<product>/SKILL.md`，在上表加一行，再按 section-templates.md 建目录。

## 行业综合（industry）

- 检索词：`personal AI agent comparison`、`AI agent tested`、`个人智能体 对比`、`个人智能体 评测`
- 收录条件：比较或评测两个及以上跟踪产品，或讨论 Personal Agent 整体的形态、架构与安全。
- 最后收集日期：2026-11-05（9 篇「仅链接」占位已补抓原文，CNBC 2026-10-31 仍取不到；新收 Tom's Guide、Engadget 对比文）
