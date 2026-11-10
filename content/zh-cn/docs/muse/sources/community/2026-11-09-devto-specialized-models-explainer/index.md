---
title: "Meta 把 Muse Wonder 的记忆与专注下放给所有人：实际变了什么"
linkTitle: "特化模型解读"
date: 2026-11-09
originalTitle: "Meta Brings Muse Wonder's Memory and Focus to Everyone: What Active Memory and Active Focus Actually Change"
sourceUrl: "https://dev.to/tng_thnhnhn_c933ee88b/meta-brings-muse-wonders-memory-and-focus-to-everyone-what-active-memory-and-active-focus-386p"
author: "Tùng Thành nhân"
publisher: "DEV Community"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-09
tags: [模型, 记忆与上下文]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了作者头像、标签行与文末评论区。作者在 dev.to 的用户名为 tng_thnhnhn。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：11 月 6 日，Meta 开始向所有 Muse 与 Meta AI 用户推送新模型——不是前沿的 Muse Wonder 模型本身，而是用 Muse Wonder 训练的现有模型特化版本，带来 Active Memory 与 Active Focus 两项能力；Meta 未公布特化模型的名称、规模，也未说明哪些地区与账户层级先行获得。10 月 12 日，Meta 推出 Muse Wonder 系列（Muse Wonder 与更大的 Muse Wonder Full），通过 Meta Model API 与 Muse Code 提供，Wonder Full 面向 Muse Code 订阅者；该模型不会成为免费 Muse 与 Meta AI 应用内的模型。Active Memory 方面，Meta 称模型经训练可区分临时信息与永久信息、跨时间推理并判断信息是否过时；在 Muse 中，遗忘达成目标所需关键信息的次数减少 2.4 倍，Meta 的 Active Memory 评测中当前 Muse 模型得分为 90%，高于此前模型的 76%。Active Focus 方面，Meta 称模型在出现意外问题时能继续朝目标努力，在 Muse 中完成出现意外问题的日常任务的能力提升 67%；Meta 的 Personal Superintelligence Index 中当前 Muse 模型为 47%，高于此前模型的 38%。作者同时指出，上述数字均为 Meta 自有测试的结果、未经独立验证，其中 2.4 倍与 67% 两项没有公布基线，Meta 未公布 Personal Superintelligence Index 的逐项衡量方法与 Active Memory 评测所用测试集，四项数字均只描述 Muse、未单独给出 Meta AI 的分数，特化模型也没有名称、参数量、模型卡与定价信息。

**保留理由**：本篇对 Meta 11 月 6 日特化模型推送作了独立梳理，区分了 Muse Wonder 本身与用其训练的特化版本，完整记录了 Active Memory 与 Active Focus 的四项数字及其缺失基线、方法与模型身份等限定条件，这些内容在已收的官方特化模型稿之外提供了可对照的版本。

---

11 月 6 日，Meta 开始向所有使用 Muse 和 Meta AI 的人推送新模型——不是前沿的 Muse Wonder 模型本身，而是 Meta 现有模型的特化版本，这些版本使用 Muse Wonder 训练。此次升级把 Wonder 的两项能力下放到大多数人实际使用的助手中：Active Memory 与 Active Focus。

如果你用 AI 智能体做开发，这一点值得关注，不是因为那些头条数字，而是因为其中的模式：一个前沿模型充当教师，蒸馏后的成果被推送到整个产品线。

## 实际推送了什么

几周前的 10 月 12 日，Meta 推出了 Muse Wonder 系列——Muse Wonder 与更大的 Muse Wonder Full——作为其面向个人与专业智能体任务的最强模型。Wonder 可通过 Meta Model API 与 Muse Code 使用，Wonder Full 面向 Muse Code 订阅者。它从来就不是免费 Muse 和 Meta AI 应用内的那个模型。

11 月 6 日推送的内容不同：Muse 和 Meta AI 背后现有模型的特化版本，使用 Muse Wonder 训练。Meta 称推送正在进行中，但没有说明这些特化模型的名称、规模，也没有说明哪些地区和账户层级会先行获得。公告中的图表只提到「Current Muse Model」与「Previous Muse Model」。

## Active Memory：更少忘记重要的事

Active Memory 是 Meta 给这样一种助手起的名字：它记住重要的事，并能识别早先的信息何时再次变得相关，从而可以基于你过去的对话继续，而不是每次从零开始。

具体而言，Meta 称这些模型经过训练，能区分临时信息与永久信息、跨时间推理，并分辨哪些内容仍然相关、哪些已经过时。在 Muse 中，改进后的模型在遗忘帮助用户达成目标所需关键信息方面减少了 2.4 倍。在 Meta 的 Active Memory 评测中——该评测衡量正确使用关键上下文的任务——当前 Muse 模型的得分为 90%，高于上一代模型的 76%。

这一表述很重要。智能体中的记忆通常被当作存储问题来谈——你能塞进多少上下文。Active Memory 则是一个检索与判断问题：保留什么、何时呈现、何时放手。一个记住一切却在错误的时间呈现错误内容的模型，可以说比一个干净利落地遗忘的模型更糟。

## Active Focus：出问题时仍紧盯目标

Active Focus 是另一半。它描述的是这样一种模型：当意外挑战出现时仍继续朝目标推进——更努力尝试、从挫折中恢复，或寻找替代方案，而不是停滞不前或宣布任务完成。

Meta 称这些模型在各种贴近现实的瓶颈上接受了训练。在 Muse 中，它们在完成会出现意外问题的日常任务方面提升了 67%。特化模型还学会了更好地处理多任务：知道何时独立推进你的目标、何时与你实时协作，并能在运行中的任务中途适应指令与澄清而不被搞糊涂。

在 Meta AI 中，同样的改进被以不同的方式宣传：一个更好的思考伙伴，能把复杂问题拆成清晰的步骤、提出更犀利的追问，并在你于对话中途改变方向时跟上。

Meta 自己的综合评分用一个数字讲述了同样的故事。在其 Personal Superintelligence Index 上，当前 Muse 模型得分为 47%，高于上一代模型的 38%。

## 值得复制的模式：教师模型与产品线模型

剥去产品名称，这份公告描述的是一种正在成为行业标准的部署模式：

1. **训练一个前沿模型**，赋予其昂贵的能力——在此即记忆判断与持久专注。
2. **用它来教特化模型**，这些模型便宜到可以服务所有人。
3. **推送能力，而非模型。** 用户得到的是行为；前沿模型留在 API 和订阅层级之后。

对任何构建智能体的人来说，教训是：记忆与专注是决定一个智能体在数天而非数分钟内是否有用的两项能力。一个忘记你昨天说过的约束、或在第一个意外错误时就放弃的模型，只是演示，不是同事。Meta 押注这两个问题都是可训练的——而且这种训练可以从前沿教师迁移到更小的学生模型。

## 诚实的保留

这份公告中的每一个数字都来自 Meta 自己，是在 Meta 设计的测试上测得的，没有独立验证：

- **四项数字中有两项没有基线。** 2.4 倍的遗忘减少和 67% 的提升没有公布起点，因此无法判断绝对变化有多大。
- **没有公布方法。** Meta 没有解释 Personal Superintelligence Index 逐项衡量什么，也没有说明 Active Memory 评测背后是哪些测试集。
- **没有 Meta AI 的单独数字。** 四个数字都描述 Muse。推送中 Meta AI 这一侧没有公布分数。
- **没有模型身份。** 特化模型未具名，没有参数量、没有模型卡，也没有定价。

47% 对 38% 的指数得分最好理解为一种走势，而不是可以拿来与任何对手比较的基准。有趣的不是这个数字——而是记忆判断与任务持久性可以从一个前沿模型蒸馏到服务所有人的模型中。这一主张将在日常使用中接受检验，在那里唯一重要的评测是：助手是否还记得你上周告诉它的事。

*来源：Meta AI Research，[Bringing Specialized Models to Muse and Meta AI](https://research.meta.ai/blog/specialized-models-for-muse-and-metaai)，发表于 2026 年 11 月 6 日。另见 Meta AI Research，[Muse Wonder: A Frontier Model For Personal & Professional AI Agents](https://research.meta.ai/blog/muse-wonder)，发表于 2026 年 10 月 12 日。*
