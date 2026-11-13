---
title: "Meta Muse：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Muse 发布时由自研的 Muse Spark 1.3 驱动；10 月推出的前沿模型 Muse Wonder 先给订阅用户，11 月起所有用户获得「用 Wonder 训练的特化模型」。用户不能自选模型，Meta 未公开各档位实际用的是哪个模型。
---

## 概要

- 发布时（2026-09-08）官方称 Muse 由 Muse Spark 驱动，安全博客点名 Muse Spark 1.3；Muse Spark 是 Meta 自研、也驱动 Meta AI 的模型系列，Muse 是建在它上面的智能体产品，两者不是一回事。
- 2026-10-12 推出前沿模型 Muse Wonder 与 Muse Wonder Full，官方称 Wonder「将很快为 Muse 提供支持，首先面向订阅用户」；据转述的 Q3 财报电话会，免费档运行在 Muse Spark 上，Wonder 在付费方案中提供。
- 2026-11-06 起，Meta 向所有 Muse 与 Meta AI 用户推送「用 Muse Wonder 训练的现有模型特化版本」，带来 Active Memory 与 Active Focus；官方给出的提升数字都是自测，没有说明特化模型的名称和规模。
- 为 Personal Agent 所做的针对性训练，官方资料写得较具体：浏览器操作、零样本工具调用、长轨迹指令遵循、提示注入识别、多智能体协调，以及一张 100 多行、逐项设门槛的上线评测表（据访谈转述）。
- 用户不能选择模型，也没有「快速」「专家」档位；资料中没有按任务、档位切换模型的公开规则。实时语音与视频化身由另外两个专门模型（Muse Realtime Voice、Muse Realtime Avatar）负责。

## Muse Spark、Muse Wonder 与特化模型

| 时间 | 说法 | 资料 |
| --- | --- | --- |
| 2026-09-08 | Muse「由 Muse Spark 驱动」，官方称是 Meta「迄今能力最强的模型，专为此类现实世界的智能体工作而打造」；安全博客称 Muse Spark 1.3 擅长驱动浏览器、提示注入防御「接近最先进水平」 | [推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}}) |
| 2026-09-23 | Connect 发布 Muse Realtime Voice 与 Muse Realtime Avatar，用于实时语音和视频化身 | [让你的 Muse 栩栩如生]({{< relref "/docs/muse/sources/official/2026-09-23-bringing-your-muse-to-life" >}}) |
| 2026-10-12 | 推出 Muse Wonder 与 Muse Wonder Full：Wonder 经 Meta Model API 和 Muse Code 向开发者开放，Wonder Full 只向 Muse Code 订阅用户开放；Wonder「将很快为 Muse 提供支持，首先面向订阅用户」，还将用于 artifact 生成及「需要更高智能的流程」 | [Wonder 发布稿]({{< relref "/docs/muse/sources/official/2026-10-12-introducing-muse-wonder-models" >}})、[Wonder 研究博客]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-research-blog" >}}) |
| 2026-10-15 | Muse Spark Open 发布（开放权重），Meta 未说它是 Muse 所用的模型 | [Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}}) |
| 2026-10-21 | 据转述的 Q3 财报电话会：免费档运行在 Muse Spark，Muse Wonder 在付费方案中提供；扎克伯格还提到能更高效提供 Wonder 智能的较小模型 | [Muse 101]({{< relref "/docs/muse/sources/community/2026-11-04-muse-101-agentic-commerce" >}}) |
| 2026-11-06 | 向所有 Muse 与 Meta AI 用户推送「以 Muse Wonder 训练的现有模型特化版」，带来 Active Memory 与 Active Focus | [特化模型]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}}) |

几篇解读专门澄清命名：Muse 是智能体产品，Muse Spark 是模型，后者同时是 WhatsApp、Instagram、Facebook、Messenger 中 Meta AI 背后的模型（[SiteDex]({{< relref "/docs/muse/sources/community/2026-11-01-sitedex-muse-for-site-owners" >}})、[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）；CodePick 的架构文章强调，产品还包括运行框架（harness）、专用计算环境、工具、状态与权限，模型 API 的示例不等于产品内部协议（[CodePick 架构]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})）。

特化模型的公告只把对比对象称为「当前 Muse 模型」与「上一代 Muse 模型」，没有给出名称和规模，也没有说明哪些地区或账户先获得；dev.to 的解读据此强调推送的「不是前沿的 Muse Wonder 模型本身」（[特化模型解读]({{< relref "/docs/muse/sources/community/2026-11-09-devto-specialized-models-explainer" >}})）。

推断：从 10-12 的「首先面向订阅用户」、财报会的「免费档 Spark、付费 Wonder」和 11-06 的「所有用户获得 Wonder 训练的特化版」三条看，Muse 已形成两层：订阅用户在部分流程中直接用 Wonder，所有用户的主力模型是由 Wonder 蒸馏或后训练而来的较小模型。资料中没有官方对这一分层的完整说明，订阅用户具体在哪些环节用 Wonder 也没有公开。

## 为智能体工作专门训练

官方对 Muse Spark 1.3 训练重点的描述包括：CLI 与 skills 的零样本工具调用、长上下文、长轨迹指令遵循（含对提示注入的内在识别）、多智能体协调；浏览网页由专门的浏览器子智能体完成（[安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。安全层面另有独立于核心模型的模型与分类器（hatch-safety）审查进出核心模型的请求，详见[安全]({{< relref "/docs/muse/analysis/security" >}})。

据 36 氪和链捕手对 David Senra 访谈 Alexandr Wang 的书面整理：团队有一张 100 多行的表，列出 Muse 必须具备的行为和能力，每行都有评测标准和上线门槛；多次检查时「八十项是绿的，二十项还是红的」，直到一个专门训练的模型版本全部达标才发布，36 氪写明这一版本是 Muse Spark 1.3；模型与产品团队合计不到 200 人（[36 氪]({{< relref "/docs/muse/sources/media/2026-10-12-36kr-wang-openclaw-origin" >}})、[链捕手]({{< relref "/docs/muse/sources/media/2026-11-03-wang-how-muse-was-built" >}})）。据 ZFinance 转述，扎克伯格称代理能力「必须在模型预训练的第一天就埋进去」（[ZFinance]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})）。

Muse Wonder 的模型卡写明：输入文本、图像、视频、音频，输出文本，推理时上下文 1M tokens，预期用途是个人与职业智能体任务，不面向 18 岁以下用户；已知局限包括多步推理出错、视觉与三维空间推理，建议对不可逆操作加入人工确认（[Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})）。研究博客称 Wonder 系列建立在 Muse Spark 之上，在 Prometheus 数据中心训练（[Wonder 研究博客]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-research-blog" >}})）。训练目标还包括避免未经许可分享私人信息、拒绝有害请求（[Wonder 发布稿]({{< relref "/docs/muse/sources/official/2026-10-12-introducing-muse-wonder-models" >}})）。

## 官方评测数字都是自测

| 来源 | 指标 | 数字 | 口径 |
| --- | --- | --- | --- |
| Wonder 模型卡（10-12） | Personal Superintelligence Index（PSI，七项内部评估的综合） | Wonder Full 59.1、Wonder 54.3；对照 Opus 5.5 55.2、GPT-6 Astra 54.5、Fable 5.1 49.9 | 均为 max 推理强度，竞品由 Meta 内部「尽力而为」运行 |
| Wonder 模型卡 | OSWorld V2.1（计算机使用） | Wonder Full 78.4、Wonder 72.6，低于 Fable 5.1 80.7、Opus 5.5 81.8 | 同上 |
| 特化模型公告（11-06） | PSI | 当前 Muse 模型 47%，上一代 38% | 未说明与模型卡的 PSI 是否同一量表 |
| 特化模型公告 | Active Memory | 关键信息遗忘减少 2.4 倍；正确使用关键上下文的任务从 76% 升至 90% | 内部评估 |
| 特化模型公告 | Active Focus | 完成会出现意外问题的日常任务「提升了 67%」 | 未给基线 |

出处：[Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})、[特化模型]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})。模型卡中 Wonder Full 并非全面领先：HealthBench Pro 62.3 低于 GPT-6 Astra 与 Opus 5.5，OSWorld 低于两款对照模型。dev.to 解读强调特化模型的数字未经独立验证（[特化模型解读]({{< relref "/docs/muse/sources/community/2026-11-09-devto-specialized-models-explainer" >}})）；DataCamp 也指出 Meta 关于与 OpenAI、Anthropic 持平的说法依赖自己的数据，两款产品目前都没有独立的智能体基准（[DataCamp]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})）。Active Memory 对记忆的影响见[记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})。

社区的评价不一：有讨论者称 Spark 在测评表上「只是中端水平」（[聚 AI 讨论]({{< relref "/docs/muse/sources/community/2026-10-04-juai-muse-discussion" >}})），智消前沿评价「中规中矩——能用，但跟 Claude、GPT 的旗舰还有距离」（[智消前沿：家谱]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}})）；Tom's Guide 的五个提示词测试中作者认为 Muse「感觉非常像是它自己的模型」（[Tom's Guide]({{< relref "/docs/industry/sources/media/2026-09-27-tomsguide-muse-vs-chatgpt-5-prompts" >}})）。这些是个人观点，不是评测。

## 用户不能选模型

雷峰网的实测作者用了半天才发现「根本不用选择模型」，面向普通用户的界面没有模型选择或「快速」「专家」档位（[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})、[OpenClaw 拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})）。社区比较中，Muse、Grok Bot 被归为「绑自家模型」，与可自选模型的 OpenClaw、Hermes 相对（[智消前沿：家谱]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}})、[用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})）。DataCamp 称 Muse 的最高推理模式在发布时因等待安全测试而未开放（[DataCamp]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})）。

订阅额度按「Muse tokens」计量（Power 每周 5 亿，Maximum 每周 30 亿，据 [iThome]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}}) 整理），与模型档位如何对应没有说明，见[开放与价格]({{< relref "/docs/muse/analysis/access-pricing" >}})。

有用户读取到自己 VM 中的文件（2026-09 的泄露 VM 引文核验审查）：用户被告知运行在 Muse Spark 上，会话元数据中的 `model_id` 为 `ipnext/avocado-5.16-v4`，作者推断「Avocado」是 Meta 内部名称；镜像中还有一个与 OpenAI 开源 Codex CLI 字符串相符的二进制，以及一个默认关闭、把发往 api.anthropic.com 的请求改道到 Meta 内部代理的开关，但都没有显示被使用。智能体自己的文档也说，日志和环境变量里的内部标识符指「服务基础设施而非模型身份」（[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。用户自己的 VM 探索看到容器通过 `inference.sock` 调用推理代理，另有 `space-inference` 等 socket（[VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。运行环境细节见[运行环境]({{< relref "/docs/muse/analysis/runtime" >}})。

推断：模型调用经由 VM 内的推理代理转发，实际使用哪个模型由服务端决定，所以 VM 内看到的名字不足以说明主对话、浏览器子智能体、artifact 生成各用什么模型。Codex 二进制与 Anthropic 开关只说明镜像中存在这些路径。

## 实时语音与视频化身是独立模型

Muse Realtime Voice 与 Muse Realtime Avatar 组成一个流式系统：Voice 产出语音令牌流，音频解码器转成语音，Avatar 消费同一个令牌流生成画面，使声音、唇形和表情同步。Avatar 是音频驱动的扩散 Transformer，经蒸馏把每分块的模型评估次数从 120 次降到 2 次。官方给出的服务指标：25 帧/秒、448×768 竖屏，发言结束到响应首字节约 870 毫秒，单个 GB200 支持 12 个并发会话；官方自测中评估者对它相对 Runway Characters 的总体偏好为 78% 比 22%，相对 HeyGen LiveAvatar 为 88% 比 12%（[让你的 Muse 栩栩如生]({{< relref "/docs/muse/sources/official/2026-09-23-bringing-your-muse-to-life" >}})）。Connect 发布时官方称用户可以用描述来设计 Muse 的声音（[Connect 2026 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})）。语音、视频作为交互入口的情况见[交互渠道]({{< relref "/docs/muse/analysis/channels" >}})。

## 开放权重的模型不是 Muse 用的模型

据整理 Meta 模型卡与研究博客的解读：Muse Spark Open（2026-10-15）是 Muse Spark 的开放权重版，MoE 架构，总参数 8160 亿、激活 420 亿，采用非开源的 Muse Model License；更早的 Muse Glimmer 30B（2026-08-09，Apache 2.0）由 Muse Spark 蒸馏而来，面向消费级硬件上的智能体任务。Meta 未说这两个模型是 Muse 所用的模型；Muse Wonder 没有公开权重，Hugging Face 上自称 meta-01 的 muse-wonder 仓库并非 Meta 官方账号（[Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}})）。

## 资料缺口

- 特化模型的名称、规模，以及与 Muse Spark 1.3 的关系；各地区、各账户层级获得的时间。
- 订阅用户在哪些流程中直接使用 Muse Wonder，与 Muse tokens 额度如何对应。
- 主对话、浏览器子智能体、artifact 生成、语音通话分别使用的模型及切换规则。
- 最高推理模式是否已开放、对哪些档位开放（目前只有 DataCamp 一句）。
- 独立第三方对 Muse 智能体能力的评测；PSI 的七项子评估是否公开。
- Q3 财报电话会关于免费档与付费档模型分工的原话（目前为转述）。

## 主要资料

- 官方：[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})（Muse Spark 驱动）；[安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})（Spark 1.3 的训练重点）；[让你的 Muse 栩栩如生]({{< relref "/docs/muse/sources/official/2026-09-23-bringing-your-muse-to-life" >}})（Realtime Voice、Avatar）；[Wonder 发布稿]({{< relref "/docs/muse/sources/official/2026-10-12-introducing-muse-wonder-models" >}})、[Wonder 研究博客]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-research-blog" >}})、[Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})（开放对象、基准）；[特化模型]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})（Active Memory、Active Focus）。
- 媒体：[36 氪]({{< relref "/docs/muse/sources/media/2026-10-12-36kr-wang-openclaw-origin" >}})、[链捕手]({{< relref "/docs/muse/sources/media/2026-11-03-wang-how-muse-was-built" >}})（上线评测表）；[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})（无模型选择）；[DataCamp]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})（最高推理模式、无独立基准）。
- 社区：[Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}})（模型谱系与开放权重）；[特化模型解读]({{< relref "/docs/muse/sources/community/2026-11-09-devto-specialized-models-explainer" >}})；[Muse 101]({{< relref "/docs/muse/sources/community/2026-11-04-muse-101-agentic-commerce" >}})（财报会转述）；[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（VM 内的模型标识）。
- 实测：[VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（推理代理 socket）。
