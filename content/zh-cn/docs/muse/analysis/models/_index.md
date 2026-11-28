---
title: "Meta Muse：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  Muse 只用 Meta 自研模型：发布时是 Muse Spark 1.3，10 月推出前沿模型 Muse Wonder，11 月起推送「用 Wonder 训练的特化模型」。付费档是否直接由 Wonder 运行，官方与第三方说法不一；用户不能自选模型，官方评测数字几乎全是自测，独立基准中 Wonder 位于中游。
---

## 概要

- Muse 只跑 Meta 自研模型，由 Meta Superintelligence Labs 训练。发布时官方点名 Muse Spark 1.3；2026-10-12 发布前沿模型 Muse Wonder 与 Muse Wonder Full，称「很快」为 Muse 提供支持、先给订阅用户；2026-11-06 开始向 Muse 与 Meta AI 推送「用 Muse Wonder 训练的现有模型特化版」。截至 2026-11-24 的英国上线稿，官方仍写「由 Muse Spark 驱动」。
- 免费档与付费档各跑哪个模型没有一手的统一说法：日本用户与 ITmedia 称付费档由 Wonder 运行、免费档用 Spark，官方 11-06 研究博客的措辞是推送特化模型而非 Wonder 本身。
- 模型是按智能体工作训练的：官方列出零样本工具调用、长上下文、长轨迹指令遵循、多智能体协调四个训练重点；Wang 称团队用一张 100 多行的行为表格作为上线门槛，Spark 1.3 的一个版本全部达标才发布。
- 用户不能选模型，也没有「快速」「专家」档位；会话元数据和沙箱二进制显示推理由服务端网关决定，镜像里出现的其他厂商模型名称没有证据显示被 Muse 使用。
- 官方评测几乎都是 Meta 自测。独立结果有限：ShellBench（2026-11-24）中 Wonder Full 总体 47.4%，在 12 个模型中排第 5，低于 GPT-6 Astra、Claude Fable 5.2 等约 14 个百分点；日本用户对 Spark 与 Wonder 的聊天对照实测中两者答案几乎一致。

## 三代模型与 Muse 的关系

| 模型 | 发布 | 定位（官方或转述） | 是否用于 Muse 智能体 |
| --- | --- | --- | --- |
| Muse Spark 1.3 | Spark 系列 2026-04 首发，1.3 于 2026-09 随 Muse 发布 | 「专为此类现实世界的智能体工作而打造」 | 是，发布稿与安全文章点名 |
| Muse Wonder / Wonder Full | 2026-10-12 | Meta 能力最强的模型，面向个人与专业智能体任务；推理时上下文 1M tokens | 官方称「很快」，先向订阅用户；Wonder 经 Meta Model API 与 Muse Code 开放，Wonder Full 只给 Muse Code 订阅用户 |
| 特化模型（未命名） | 2026-11-06 | 用 Muse Wonder 训练的现有模型特化版 | 官方称向 Muse 与 Meta AI 用户推送 |
| Muse Ember | 2026-11-09 | 最小的模型，用于重复工具调用与短编码任务 | Meta 没有说 Ember 驱动 Muse 智能体，只在 Muse Code 与 Meta Model API 提供 |

出处：发布时的模型见 [推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})；Spark 首发日期出自 Muse 自己的系统说明（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})），1.3 的时间据 [Spark 与 Wonder 对比]({{< relref "/docs/muse/sources/community/2026-11-22-emma-spark-vs-wonder" >}}) 转述官方文档。Wonder 见 [推出 Muse Wonder（新闻稿）]({{< relref "/docs/muse/sources/official/2026-10-12-introducing-muse-wonder-models" >}})、[Muse Wonder（研究博客）]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-research-blog" >}})、[Muse Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})；特化模型见 [特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})；Ember 据 [Muse 拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}}) 转述 Meta 研究博客，[Muse 登陆手表核查]({{< relref "/docs/muse/sources/community/2026-11-12-muse-on-apple-watch-wear-os" >}}) 同样称其为开发者模型、没有说明消费者应用推出。

特化模型的官方稿没有给出模型名称、规模、模型卡或推送地区与档位（[特化模型解读]({{< relref "/docs/muse/sources/community/2026-11-09-devto-specialized-models-explainer" >}})、[Wonder 训练模型上线]({{< relref "/docs/muse/sources/community/2026-11-09-museexplained-wonder-trained-models-live" >}}) 核对时指出）。英国上线的官方稿（2026-11-24）仍写 Muse「由 Muse Spark 驱动」，称 Spark 是 Meta Superintelligence Labs 的第一个模型，没有提 Wonder（[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})；转述见 [英国第七个市场]({{< relref "/docs/muse/sources/media/2026-11-24-muse-launches-uk" >}})、[英国上线与监管协商]({{< relref "/docs/muse/sources/community/2026-11-24-muse-uk-launch-and-regulators" >}})、[Muse 英国上线核查]({{< relref "/docs/muse/sources/community/2026-11-25-muse-live-uk" >}})）。

推断：从这一顺序看，Meta 的做法是以前沿模型做「教师」、把能力蒸馏进较小的服务模型推给所有人，[特化模型解读]({{< relref "/docs/muse/sources/community/2026-11-09-devto-specialized-models-explainer" >}}) 把它概括为「推送能力，而非模型」。英国稿仍写 Spark，可能说明特化模型仍属 Spark 系列，也可能只是沿用发布稿的措辞；资料无法区分。

## 免费档与付费档跑哪个模型：说法不一

| 来源 | 说法 | 依据 |
| --- | --- | --- |
| 官方研究博客 2026-10-12 | Wonder「将很快」为 Muse 提供支持，先向订阅用户推出 | [Muse Wonder（研究博客）]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-research-blog" >}}) |
| 官方 2026-11-06 | 向 Muse 推送「用 Muse Wonder 训练的」特化模型 | [特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}}) |
| Muse 101（转述 TNW 与 Q3 电话会） | 免费档运行在 Muse Spark 上，Wonder 在付费方案提供 | [Muse 101：智能体商务]({{< relref "/docs/muse/sources/community/2026-11-04-muse-101-agentic-commerce" >}}) |
| 日本用户 Emma 2026-11-19 | 应用内升级界面上 Power、Maximum 均写「由 Muse Wonder 执行」 | [免费与付费之差]({{< relref "/docs/muse/sources/community/2026-11-19-emma-muse-free-vs-paid" >}})（升级界面截图） |
| Emma 2026-11-22 转述官方文档 | 免费方案由 Spark 驱动；付费方案中 Wonder 负责主要对话、成果物制作、定期执行与后台作业 | [Spark 与 Wonder 对比]({{< relref "/docs/muse/sources/community/2026-11-22-emma-spark-vs-wonder" >}}) |
| ITmedia 2026-11-22 | 免费方案基本使用 Spark，付费方案可用性能更高的 Wonder | [ITmedia 入门解说]({{< relref "/docs/muse/sources/media/2026-11-22-itmedia-muse-explainer" >}}) |

[免费与付费之差]({{< relref "/docs/muse/sources/community/2026-11-19-emma-muse-free-vs-paid" >}}) 与 [ITmedia 入门解说]({{< relref "/docs/muse/sources/media/2026-11-22-itmedia-muse-explainer" >}}) 的收录说明都注明，这一说法与官方 11-06 研究博客的措辞有出入。另有两处与档位相关的说法：DataCamp 称 Muse 的最高推理模式在发布时因等待安全测试没有开放（[Dots 与 Muse 横评]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})）；Meta 用量页称一个任务消耗多少令牌「随功能、请求和模型层级而异」（据 [20 美元四智能体对比]({{< relref "/docs/industry/sources/community/2026-11-22-four-agents-twenty-dollars" >}}) 转述）。用量与档位见 [开放与价格]({{< relref "/docs/muse/analysis/access-pricing" >}})。

推断：「模型层级」影响令牌消耗、升级界面写明 Wonder，两者合起来看，付费档在某些环节调用了比免费档更大的模型，这一点大致可信；但付费档用的是 Wonder 本身还是特化模型，资料不足以判断。

## 为智能体工作专门训练

官方安全文章称，训练时特别关注四方面：用 CLI 和技能做零样本工具调用、长上下文、长轨迹指令遵循（同时内在地意识到提示注入）、多智能体协调；浏览器操作是 Spark 1.3「特别擅长的事情」，配有专门的浏览器子智能体（[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。Muse 的系统提示第一句是「Your purpose is to make your user's life better.」（[我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。

上线门槛按行为而非通用基准设定。据 36 氪整理的 Wang 访谈，团队有一张 100 多行的表格，列出 Muse 必须具备的行为和能力，每行有评测标准与上线门槛；此前的版本满足约 80 项、约 20 项不达标，直到 Spark 1.3 的一个版本全部达标才发布（[Muse 是玩龙虾玩出来的]({{< relref "/docs/muse/sources/media/2026-10-12-36kr-wang-openclaw-origin" >}})）。ChainCatcher 整理的同一访谈称，评测关注模型能否稳定执行任务、过程中与用户沟通、需要指点时回来询问（[Muse 是怎麼做出來的]({{< relref "/docs/muse/sources/media/2026-11-03-wang-how-muse-was-built" >}})）；两篇同源，不是独立证据。

Wonder 的两项核心能力是 Active Memory（跨对话携带上下文、区分临时与永久信息）与 Active Focus（遇到意外困难时继续推进、换方法、从错误恢复）（[Muse Wonder（研究博客）]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-research-blog" >}})、[特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})）。The Verge 报道这两项能力随特化模型进入 Muse 应用（[Muse 定制 Spaces]({{< relref "/docs/muse/sources/media/2026-11-06-theverge-muse-spaces" >}})）。记忆与长任务的产品实现见 [记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})、[持续执行]({{< relref "/docs/muse/analysis/continuous-execution" >}})。

## 评测数字：自测为主，独立结果位于中游

**官方模型卡（2026-10-12，max 推理强度）。** Meta 把 Wonder 与 Claude Fable 5.1、GPT-6 Astra、Claude Opus 5.5 对比，结果有胜有负（[Muse Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})）：

| 基准 | Wonder Full | Wonder | Fable 5.1 | GPT-6 Astra | Opus 5.5 |
| --- | --- | --- | --- | --- | --- |
| Personal Superintelligence Index（Meta 内部） | 59.1 | 54.3 | 49.9 | 54.5 | 55.2 |
| Harvey LAB-AA（法律） | 13.1 | 10.0 | 6.4 | 8.6 | 4.2 |
| AutomationBench-AA（业务流程） | 45.4 | 39.1 | 32.1 | 41.6 | 41.2 |
| OSWorld V2.1（部分分 / 二元分） | 78.4 / 39.4 | 72.6 / 34.3 | 80.7 / 43.1 | 75.8 / 34.3 | 81.8 / — |

模型卡写明，竞品结果为内部运行，「仍属尽力而为」，提示词、工具和运行时未必针对专有模型做过最优调校（[Muse Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})）。Wonder 在 HealthBench Pro、GDP.pdf、JobBench、OSWorld V2.1 上低于对比模型中的最高分。据 [Wonder 与主动记忆]({{< relref "/docs/muse/sources/community/2026-10-20-muse-wonder-active-memory" >}}) 转引 Meta 记分卡，Artificial Analysis 智能指数为 Wonder 52、Wonder Full 56、Claude Opus 5.5 58。

**特化模型（2026-11-06）。** 官方称关键信息遗忘减少 2.4 倍，Active Memory 评估中正确使用关键上下文的任务从 76% 升至 90%，日常任务完成率提升 67%，Personal Superintelligence Index 从上一代的 38% 升至 47%（[特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})）。[特化模型解读]({{< relref "/docs/muse/sources/community/2026-11-09-devto-specialized-models-explainer" >}})、[Wonder 训练模型上线]({{< relref "/docs/muse/sources/community/2026-11-09-museexplained-wonder-trained-models-live" >}}) 指出这四个数字都是 Meta 自测，没有公布方法、样本量和测试集，「2.4 倍」「67%」没有基线，47% 对 38% 只宜看作走势。截至 2026-11-27，Muse Explained 承诺的独立复查仍未出现（[Wonder 训练模型上线]({{< relref "/docs/muse/sources/community/2026-11-09-museexplained-wonder-trained-models-live" >}}) 的 dateNote）。

**独立结果。**

- ShellBench（OpenClaw 等发起，2026-11-24）：100 个任务、12 个模型 × 5 个框架。GPT-6 Astra 以 62.5% 居首，Claude Fable 5.2 61.9%、GPT-6.1 Sol 61.4%；Muse Wonder Full 总体 47.4%（Pi 框架下 56.0%、Claude Code 下 38.1%），Muse Wonder 1.0 总体 39.7%（[ShellBench 基准测试]({{< relref "/docs/industry/sources/community/2026-11-24-openclaw-shellbench" >}})）。同一框架内最高与最低模型的中位差距为 45.7 个百分点，固定模型换框架为 6.2 个百分点。
- SemiAnalysis 基准（2026-11-02）把 Wonder Full 在网络安全任务上排第一，总体落后于竞争对手的前沿模型（据 [Wonder 训练模型上线]({{< relref "/docs/muse/sources/community/2026-11-09-museexplained-wonder-trained-models-live" >}}) 转述，原报告未收）。
- Emma 在 Muse 聊天里对照 Spark 与 Wonder：三道短题答案全部一致（[Spark 与 Wonder 对比]({{< relref "/docs/muse/sources/community/2026-11-22-emma-spark-vs-wonder" >}})）；续篇做 30 件订单的五步处理、含矛盾备忘的长文 4 问、6 个测试用例的 Python 程序，两边也全对，唯一差别是对一处矛盾，Spark 给出倾向性判断，Wonder 只说资料无法决定（[长工作对比]({{< relref "/docs/muse/sources/community/2026-11-22-emma-spark-vs-wonder-long-tasks" >}})）。作者说明这不是纯模型对照，每题只做一次，数小时的自主作业不在测试范围。
- 主观评价：PC Watch 作者把 Muse 与 Claude Code 的 Fable 5.2、Opus 5.5 比较，称 Spark 的表现力有「压倒性的差距」（[Muse 当 Zaurus 开发者]({{< relref "/docs/muse/sources/media/2026-11-19-pc-watch-muse-zaurus-developer" >}})）；AI问消称 Spark「中规中矩」（[AI问消：Agent 家谱与选购]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}})）；橘AI 讨论者称其在测评表上「只是中端水平」（[橘AI：深入讨论 Muse]({{< relref "/docs/muse/sources/community/2026-10-04-juai-muse-discussion" >}})）。Claire Vo 的四智能体测试中 Muse 约半秒内回应，因速度赢下作业讲解（[Claire Vo：四个智能体九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。

推断：ShellBench 中 Wonder Full 在不同框架间相差 17.9 个百分点，远大于该基准 6.2 个百分点的中位差距，可能说明 Muse 模型与 Meta 自己的框架绑定较深，换到第三方框架时表现不稳。这只是对表格的比较，ShellBench 没有这样下结论。

## 用户不能选模型，由服务端路由

雷峰网实测称，面向普通用户的那一层「根本不用选择模型」，也没有「快速」「专家」之类的档位（[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})，同见 [OpenClaw 同源拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})）。Future Society 导出的 Muse 系统说明写明，模型切换界面「今天不向普通用户开放」，有的账户会显示模型选择器，智能体不会自行切换模型（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。

运行时的证据：

- 会话元数据把模型记录为 `ipnext/avocado-5.16-v4`；系统说明告诉智能体，错误、日志、环境变量中的内部标识符指服务基础设施，不是模型身份（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。沙箱剖析者推断 avocado 是 Muse Spark 的内部代号（[Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})）。
- 推理经虚拟机内的推理代理 socket 调用，哪个模型回答由服务端决定（[Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})、[我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。
- 沙箱二进制中出现 claude-opus、gpt-5.5-codex 等其他厂商的模型名，镜像里还有一个 258 MB 的 OpenAI Codex CLI。[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}}) 认为这些只是提供方列表的条目，导出内容中没有证据显示被选用；[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}}) 记录到一条默认开启的功能开关，会把发往 api.anthropic.com 的请求改道到 Meta 内部代理，该虚拟机上为关闭，用途不明。

用户可以在 Muse 的终端里经 CLI 调用 Gemini、Claude 等外部模型（[用 CLI 调用其他 AI]({{< relref "/docs/muse/sources/community/2026-11-25-emma-cli-ai-bridge" >}})），但那是 Muse 调用的外部工具，不是更换 Muse 自身的模型。

## 主模型之外的专用模型

- **安全分类器。** 沙箱里有本地安全分类器 `9b_safety_classifier`、`2b_tool_call_classifier_v0_4`、`pi_3b_prefilter`，以及语音识别、嵌入、重排序小模型（[Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})）；Sentinel 把可疑请求交给 `policyguard-nvfp4` 审查，返回 veto 或 no_finding（据 NebuSec 剖析，[Muse 内部架构剖析]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})）。审查机制见 [安全]({{< relref "/docs/muse/analysis/security" >}})。
- **语音与化身。** Muse Realtime Voice 生成语音，Muse Realtime Avatar 是音频驱动的扩散 Transformer，读取同一串语音 token 驱动唇形与表情，采用四位量化感知训练（[Muse Realtime Avatar]({{< relref "/docs/muse/sources/official/2026-09-23-bringing-your-muse-to-life" >}})）。据 [语音化身设计分析]({{< relref "/docs/muse/sources/community/2026-11-18-voice-avatar-design" >}}) 转引 Meta 研究文章，蒸馏后的学生模型每个视频片段只需 2 次模型评估，教师模型需要 120 次；首字节延迟约 870 毫秒。渠道与设备上的形态见 [交互渠道]({{< relref "/docs/muse/analysis/channels" >}})。
- **媒体生成。** Emma 实测视频每段固定约 10 秒，可附带按文字描述生成的配乐，但没有专门的作曲功能，同日多件因生成基础设施过载失败（[Muse 视频生成实测]({{< relref "/docs/muse/sources/community/2026-11-24-emma-video-generation-test" >}})、[Muse 音乐生成实测]({{< relref "/docs/muse/sources/community/2026-11-24-emma-music-generation-test" >}})）。

## 开放权重与开发者模型不是 Muse 用的模型

Meta 同期发布了几款开发者可用的模型，第三方资料常与 Muse 混为一谈（[Meta Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}}) 专门核对）：

- Muse Spark Open（2026-10-15）：8160 亿参数（420 亿激活）的开放权重版本，采用 Meta 自有的 Muse Model License（非开源许可），年收入合计超过 2000 万美元的模型即服务商须先通知 Meta 并另签协议。Meta 没有说它是 Muse 实际使用的模型。
- Muse Glimmer 30B（2026-08-09）：Apache 2.0 许可，由 Spark 蒸馏，面向消费级硬件。
- Muse Wonder 只经 API 提供，OpenRouter 2026-11-05 的列价为每百万输入 token 4 美元、输出 20 美元；没有公开权重。

AMD 称为 Spark Open 与 Glimmer 提供发布当日支持（据 All Things Muse 转述 AMD 公告，[AMD EPYC 支撑 Muse]({{< relref "/docs/muse/sources/media/2026-10-28-allthingsmuse-amd-epyc-powers-muse" >}})）。Spark Open 在 Hugging Face 上一个月 14,457 次下载（2026-11-17 扫描），这是模型文件下载量，不是 Muse 用户数（[0.8% 份额核查]({{< relref "/docs/muse/sources/community/2026-11-17-muse-wells-fargo-share-figure-check" >}})）。

## 资料缺口

- 付费档与免费档各自实际运行的模型；Meta 所说「Muse 文档」中 Wonder 负责付费档对话与后台作业的原文（目前只有 [Spark 与 Wonder 对比]({{< relref "/docs/muse/sources/community/2026-11-22-emma-spark-vs-wonder" >}}) 转述）。
- 特化模型的名称、规模、模型卡，推送地区与档位，以及 47%、90% 等数字的评测方法；对它的独立测试。
- SemiAnalysis 2026-11-02 基准原文；Personal Superintelligence Index 的定义与题目。
- 发布时未开放的「最高推理模式」后来是否开放、对哪些档位开放。
- 「有的账户会显示模型选择器」指哪些账户；沙箱中 Anthropic 改道开关的用途。
- Muse Ember 官方研究博客原文（目前只有转述）。

## 主要资料

**官方**

- [我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})：Spark 1.3 的训练重点与提示注入抵抗能力。
- [我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})：系统提示第一句。
- [推出 Muse Wonder（新闻稿）]({{< relref "/docs/muse/sources/official/2026-10-12-introducing-muse-wonder-models" >}})、[Muse Wonder（研究博客）]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-research-blog" >}})：Wonder 发布与「先向订阅用户推出」。
- [Muse Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})：Wonder 模型卡与基准对照。
- [特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})：特化模型推送与四个自测数字。
- [Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})：英国上线稿仍写 Muse Spark。
- [Muse Realtime Avatar]({{< relref "/docs/muse/sources/official/2026-09-23-bringing-your-muse-to-life" >}})：Realtime Voice 与 Realtime Avatar。

**媒体**

- [Muse 是玩龙虾玩出来的]({{< relref "/docs/muse/sources/media/2026-10-12-36kr-wang-openclaw-origin" >}})、[Muse 是怎麼做出來的]({{< relref "/docs/muse/sources/media/2026-11-03-wang-how-muse-was-built" >}})：100 多行的行为表格与上线门槛（同一访谈）。
- [雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})：用户端不能选模型。
- [ITmedia 入门解说]({{< relref "/docs/muse/sources/media/2026-11-22-itmedia-muse-explainer" >}})：付费档用 Wonder 的说法。
- [Dots 与 Muse 横评]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})：最高推理模式发布时未开放。
- [Muse 定制 Spaces]({{< relref "/docs/muse/sources/media/2026-11-06-theverge-muse-spaces" >}})：Active Memory 与 Active Focus 进入 Muse 应用。

**社区**

- [ShellBench 基准测试]({{< relref "/docs/industry/sources/community/2026-11-24-openclaw-shellbench" >}})：ShellBench 独立基准。
- [Spark 与 Wonder 对比]({{< relref "/docs/muse/sources/community/2026-11-22-emma-spark-vs-wonder" >}})、[长工作对比]({{< relref "/docs/muse/sources/community/2026-11-22-emma-spark-vs-wonder-long-tasks" >}})：Spark 与 Wonder 对照实测。
- [免费与付费之差]({{< relref "/docs/muse/sources/community/2026-11-19-emma-muse-free-vs-paid" >}})：升级界面写明 Wonder。
- [特化模型解读]({{< relref "/docs/muse/sources/community/2026-11-09-devto-specialized-models-explainer" >}})、[Wonder 训练模型上线]({{< relref "/docs/muse/sources/community/2026-11-09-museexplained-wonder-trained-models-live" >}})：特化模型数字的核查。
- [Muse 拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})：Ember 与各模型分工。
- [Meta Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}})：开放权重模型与 Muse 的区别。
- [Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})、[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})、[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})：沙箱中的模型标识、二进制与分类器。
- [语音化身设计分析]({{< relref "/docs/muse/sources/community/2026-11-18-voice-avatar-design" >}})：化身模型的蒸馏与延迟。

**实测**

- [我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})：虚拟机内的推理代理 socket（2026-10-12 实测）。
