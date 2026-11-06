---
title: "Grok、Dot、Muse、Claude Duet：九项任务、四个智能体，没有全能赢家"
linkTitle: "Claire Vo：四个智能体九项任务"
date: 2026-10-29
originalTitle: "Grok vs. Dot vs. Muse vs. Claude Duet: Nine Tasks, Four Agents, No Universal Winner"
sourceUrl: "https://www.chatprd.ai/how-i-ai/grok-vs-dot-vs-muse-vs-claude-duet-nine-tasks-four-agents-no-universal-winner"
author: "Claire Vo"
publisher: "ChatPRD「How I AI」"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-06
tags: [实测评测]
products: [grok-bot, dots, muse, claude-duet]
---

{{< source-info >}}

**收录说明**：播客「How I AI」该期节目的文字版。直接下载，图片收入 images/；文末的收听链接、赞助商列表和 ChatPRD 推广未收，文首的节目章节列表保留。旧笔记 learning-ai-agent 引用过这一篇，2026-11-06 复核后收入。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Claire Vo 用九项自己的真实任务比较 Grok Bot、OpenAI dots、Meta Muse 和 Claude Duet，包括 Slack 回复、剪短视频、修 Sentry 报错、做缩略图、收件箱分诊、家庭小报、物理题、买鞋和产品发布视频。她说明这不是受控评测：各产品接的连接器和记忆不同（Muse 没接 Slack 和 GitHub），最终排名是把她的评语交给 Claude 打的分。结果是 Grok Bot 综合第一，Muse 赢下短视频、家庭小报和物理题，dots 与 Claude Duet 在修报错上并列最好，Claude Duet 做的发布视频最好，但它慢，请求了 4 次权限，其他产品各 1 次。

**保留理由**：同一作者用同一组任务比较四个 Personal Agent 的一手评测，逐项给出了各自的强弱。

---

Grok vs. Dot vs. Muse vs. Claude Duet：九项任务、四个智能体，没有全能赢家

Claire Vo 让四个个人智能体接受九项真实任务的考验。Grok Bot 赢下广泛工作测试，Muse 处理个人和创意工作，而编程方面的热门选择暴露了总体分数的局限。

![Claire Vo 的头像](images/img-01-c8e842.avif)

Claire Vo

2026 年 10 月 29 日·10 分钟阅读

## 观看或收听完整节目

[在 YouTube 上观看](https://youtu.be/hnCoQ5wB-GU)[在 Spotify 上收听](https://open.spotify.com/episode/60sosdBzFCkgB5jSQfcIO8)[在 Apple Podcasts 上收听](https://podcasts.apple.com/us/podcast/grok-vs-dot-vs-muse-vs-claude-duet-which-one-crushes/id1809663079?i=1000798510243)

## 节目章节

6 个章节

1. [2:14 构建基准并检查智能体访问权限：Claire 选择九项真实任务，使用计算机操作（computer-use）操作员，并解释限制这次比较的设置差异。](https://youtu.be/hnCoQ5wB-GU?t=134s)
2. [10:11 Slack 回复、短视频和 bug 修复：Dot 理解 Claire 的偏好，Muse 制作出最强的短视频，代码审查揭示了一处有风险的验证改动。](https://youtu.be/hnCoQ5wB-GU?t=611s)
3. [17:31 Figma 缩略图和可执行的收件箱分拣：Grok 在新缩略图创意和一个让待办事项更易用的文档界面上获胜。](https://youtu.be/hnCoQ5wB-GU?t=1051s)
4. [20:49 家庭报纸、作业和买鞋：Muse 擅长面向家庭的成品和快速解释；Grok 最擅长产品比较。](https://youtu.be/hnCoQ5wB-GU?t=1249s)
5. [26:25 一支发布视频扭转了 Claude 的视频剪辑失败：Claude Duet 在产品简报、品牌和配音工作流方面比其他智能体跟得更好。](https://youtu.be/hnCoQ5wB-GU?t=1585s)
6. [30:14 最终排名和该用哪个智能体：Grok 在总体排名中领先，Muse 在个人任务上突出，Claire 把个人智能体与她偏好的编程工具区分开来。](https://youtu.be/hnCoQ5wB-GU?t=1814s)

## 本期节目的工作流

3

1. [01 用 Meta 的 Muse 制作个性化家庭报纸](/how-i-ai/workflows/create-a-personalized-family-newspaper-with-meta-s-muse)
2. [02 如何用 Claude Duet 制作带品牌的产品发布视频](/how-i-ai/workflows/how-to-create-a-branded-product-launch-video-with-claude-duet)
3. [03 用 Grok 和 Figma 生成新颖的 YouTube 缩略图创意](/how-i-ai/workflows/generate-novel-youtube-thumbnail-ideas-with-grok-and-figma)

[所有工作流](/how-i-ai/workflows)

节目大纲

Claude Duet 不肯下载视频来剪辑一段短片。后来，它却做出了整个测试中最好的产品发布视频，连品牌和 ElevenLabs 配音都齐全。

这个矛盾比排行榜更有用。「制作视频」听起来像一项能力，直到你让智能体去找素材、下载它、选择剪辑点、遵循一项设计技能，或生成旁白。不同的工作暴露出不同的长处——以及非常不同的失败模式。

我让 Dot、Grok Bot、Muse 和 Claude Duet 完成九项我实际需要做完的任务。Grok 赢下总体排名。Muse 是我在若干个人和创意任务上的最爱。Dot 和 Duet 做了最强的编程工作，但这并没有让它们中的任何一个成为我更偏好的通用助手。

我想知道哪个智能体能完成一件有用的工作，而不需要我管理每一步。

## 一个围绕我实际工作构建的基准——以及不完美的访问权限

我先问每个智能体它为我在做的排名前 10 的任务。然后我把这些列表放进 Claude，让它围绕最常见的任务构建一个基准，同时测试不同的能力。

这个基准涵盖九项我实际需要完成的工作：

- 起草一条 Slack 回复。
- 剪辑一段短视频。
- 修复一个 Sentry bug。
- 制作一张 How I AI 缩略图。
- 分拣我的收件箱。
- 制作一份家庭报纸。
- 向我四年级的孩子解释一道物理题。
- 买鞋。
- 制作一支 ChatPRD Product Intelligence 发布视频。

我想要轻量的提示词，按照我实际求助的方式写。我在准备时的指令是：「保持我的口吻。完全做我会做的事。」运行表包括每个提示词、对可能追问的回应，以及推动卡住的智能体的方法。这不是一场精心设计提示词的竞赛。

然后我用智能体来操作智能体。Claude ComputerUse 运行 [Dot](https://chatgpt.com/features/dots/)；[Codex](https://openai.com/codex) 操作 [Grok Bot](https://x.ai/bot)、[Muse](https://ai.meta.com/muse/) 和 [Claude Duet](https://claude.com/product/claude-duet)。并行运行任务确实有用。操作员层（operator layer）则没那么可靠：计算机操作功能坏了，我不得不介入，而我对 Claude ComputerUse 尤其沮丧。

我还让 Codex 使用 BrowserUse 检查连接和技能。即使你从不运行基准，这一点也值得照做。当几个智能体拥有不同的电子邮件账户和连接器时，表面上智能的差异实际上可能是访问权限的差异。

而且我仍然漏掉了东西。Muse 没有连接 Slack 或 GitHub。Claude 做家庭报纸时只有我的工作日历。已有的记忆不同，而使用不同的操作智能体又引入了另一个变量。

所以这是对我在用的配置（setups）的实际比较，而不是受控的模型评估。我公开评判输出，记录我的反应，并把那份记录交给 Claude 做最终排名。报告的 Grok 93% 和 Duet 79% 来自那个评分过程；我没有建立透明的评分公式。把它们当作这次运行的总结，而不是可移植的性能统计数据。

## Grok 的工作优势往往在成品，而不在答案

Slack 回复是一个有用的例子，说明为什么「听起来像我」和「符合我的利益行事」是不同的标准。

一位在 Lovable 的朋友曾请我去做一场演讲。有访问权限的智能体都产出了大致可接受的回复。Grok 听起来最像我。然而 Dot 问了活动是否远程，以及我是否会有报酬。对于一个日程繁忙、宁愿不出门的人来说，这些是重要细节。

Dot 更好地理解了这个决定，即使写作任务本身并不难。Muse 无法参与，因为我没有连接 Slack；那是配置失败，而不是它不能起草回复的证据。

收件箱分拣暴露了另一种区别。智能体们普遍找到了合理的待办事项。Grok 把它们放在一个 Grok 文档里交付：有条理、可读，并配有勾选框。Claude 想用它自己的任务跟进列表。Muse 从 Gmail 出发，找到了万圣节周之前的育儿义务。Dot 返回了一条消息，列了大约五个优先事项。

对我来说，Grok 的文档是最好的工作面（working surface）。一个埋在聊天消息里的列表，比一个我实际能用的成品制造更多工作。这就是为什么 Grok Bot 能充当我的幕僚长：推理完成之后，界面很重要。

Grok 也赢下了缩略图任务。我们已经有好的模板和一个 [Figma](https://www.figma.com/) MCP 连接，所以智能体们并不是从空白画布开始。Dot 和 Claude 成功地把新内容放进现有模板。Grok 产出了我喜欢的新标题和缩略图创意。Muse 做了一个构图，让 Blair 从看起来像诡异窗帘的东西后面探头。那一个被明确否决。

![一场播客节目的 AI 生成缩略图候选方案详细对比，展示设计迭代和相关的项目笔记。](images/img-02-a853df.avif)

买鞋测试强化了 Grok 在浏览导航和比较方面的优势。我想要价格合适的红色 Adidas Tokyo。Grok 找到了不错的选项；Muse 在我的引导下接近了。Claude 反复遇到被封锁的购物网站，搜的是带红条纹的白鞋而不是带白条纹的红鞋，还找到了最贵的选项。Dot 几乎没比较不同选择。

如果你要改编这些任务，我的建议是定义可用的输出：一份可执行的清单、一个缩略图候选，或对正确产品和颜色的比较。这样就更难把一个看似合理的回复误当作已完成的工作。

## Muse 赢下短视频——以及家庭报纸

对于短视频，智能体们可以访问我们与来自 Reddit 的 Blair 那一期节目的文字稿和原始素材。工作是在 [Dropbox](https://www.dropbox.com/) 中找到素材、下载它，并剪出一段短片。我没有手动编辑结果。

Claude Duet 不肯下载视频，所以在编辑开始前就失败了。另外三个都产出了短片，但它们的选择差异足够大，让赢家显而易见。

这三段短片各有不同的问题或长处：

- Grok 的缩放处理得更好，但它的叠加层很丑；有一个落在了 Blair 的额头上。
- Dot 的短片看起来不错，但缺少有力的剪辑。
- Muse 使用了一个简单的 How I AI 标签、熟悉的字幕布局和更强的节奏。它没有缩放效果，但我更喜欢它的短片。

Muse 赢下了一项我以前没有用它做过的工作。我之前已经在用它发布社交内容；这个结果给了我一个理由，考虑也用它来创作那些内容。更好的技能可能进一步改善这些输出，但那是以后测试的机会，而不是这次运行所证明的东西。

家庭报纸让同样的偏好更加明显。这是我为孩子们打印的东西：本周日程、提醒、天气和有趣的新闻。我已经通过我的 Grok 机器人 TradBot 运行一个版本。

Grok 做了一份有用的报纸，包含学校信息、「不要忘记」清单、湾区体育、万圣节内容和天气。Muse 做出了最有吸引力的家庭成品：一个带插图的页眉、一页日程，以及第二页的逐日天气、点子和灵感。它用了两页，我很乐意接受，因为结果很吸引人。

![一瞥「The Cedar Ledger」家庭报纸，展示其带插图的头版、天气预报和详细的活动日程。](images/img-03-c55569.avif)

Dot 的设计很差。Claude 在发现缺少相关日历访问权限后，产出了一份 Markdown 大纲。那个限制是真实的，但制作报纸的说明并不是我要求的报纸。

对于照搬这个工作流的读者，改编很直接：连接相关的家庭信息，并指定一个可打印的成品。然后在打印前检查它。可爱的布局并不能验证日程，而这一期节目的评测重点很大程度在呈现上，而不是逐项准确性审计。

Muse 还以速度赢下作业讲解。四个智能体都正确回答了一道速度随时间变化的问题——答案是 C——并做了足够的解释。据我观察，Muse 在约半秒内回应；它快到无法记录在计时记录中。当正确性实际上打平时，响应速度决定了我想再次使用哪个工具。

## 编程暴露了快速、看似合理的修复的危险

编程任务从 [Sentry](https://sentry.io/) 的一个 bug 开始。Muse 无法处理它，因为我没有给它 GitHub 访问权限。当我建议在 [Linear](https://linear.app/) 中把它分配给 Devin 时，它把 Devin 理解成一个人，而不是一个智能体。

其他智能体花了大约 10 分钟。然后我让 Claude Opus 5.5 给它们的修复打分，我在评测中就是这么描述的。

Dot 使用 Codex，最接近预期的修复。Claude Duet 找到了第二个 bug，并认识到 Dot 已经修复了原来的问题，得出结论说它不需要为那部分再提交更多代码。这种克制很重要：生成另一个改动并不天然比识别已有工作更好。

Grok 的修复才令人担忧。它放宽了验证，通过接受本应被拒绝的东西来实际上回避问题。它很快，但速度并没有让这个改动正确。

这对 Dot 和 Duet 是一场胜利，Claude 因额外的 bug 获得加分。这也提醒我们，总体赢家不应自动获得仓库访问权限和交付代码的责任。

我的实际建议仍然比「用这些个人智能体来编程」更窄。我会直接使用底层的编程工具——Codex 和 Claude。审查仍然需要确定补丁是否保持了需求，而不是仅仅让错误消失。

## Claude 的发布视频挽回了一次非常不均衡的运行

最后一项任务是为 Product Intelligence 制作一支发布视频，那是我正在为 [ChatPRD](https://www.chatprd.ai/) 做的一个功能。与短视频不同，这项任务有一个旨在指导输出的现有技能。

Dot 产出的东西更像一份舒缓的 PowerPoint，而不是我想要的发布视频。Grok 遵循了我的技能，产出了一个可辨认的我们视频风格版本，但有布局问题和内容溢出。

Muse 缺少对我仓库的访问权限，所以我没有把它配置到能成功。它仍然产出了一支雄心勃勃的视频，带英式口音的概述——并且编造了东西。制作上的努力并没有弥补产品依据的缺失。

Claude Duet 交付了最完整的结果。它抓住了价值主张，使用了我们的品牌，并避免了布局问题。它还请求使用 [ElevenLabs](https://elevenlabs.io/) MCP 并生成了配音。我本来更喜欢女声，或我在 ElevenLabs 中自己录制的声音，但底层的成品显然是最好的。

这就是值得保留的区别：Claude 在下载和剪辑一段现有视频上失败了，随后在带品牌的产品演示上成功了。这些不应被合并成一项「视频」能力。

对于可重复的发布视频工作流，我建议的改编是提供产品源材料、现有技能、品牌参考，以及明确的语音选择。前三项反映了这次测试中重要的东西；指定语音则解决了剩余的编辑不匹配。

## 结论：按工作委派，然后检查交接

九项任务之后，我的结论是：

- Grok 赢下缩略图、收件箱待办和买鞋。它是这次运行中我最好的广泛工作智能体。
- Muse 是我在家庭报纸、快速解释和短视频内容上的最爱。缺少商务连接限制了我能测试的东西。
- Dot 在 Slack 回复和代码修复上突出。
- Claude Duet 做了很强的 bug 工作，并制作了最好的发布视频。

Duet 还很慢，并请求权限四次，而其他每一个只请求一次。我想要适当的控制，但反复的批准请求会把委派变成监督。Muse 用于权限请求的侧边栏是一个有用的界面选择。

值得照搬的是方法：在你自己的重复性工作上测试智能体，在评判前检查访问权限，并比较完成的成品。对于广泛的工作协调，我会从 Grok Bot 开始。对于家务任务和轻量创意工作，我会从 Muse 开始。对于编程，我仍然会直接找 Codex 或 Claude。

人的判断仍然留在交接处：检查修复是否保持验证、视频是否编造产品声明、购物结果是否匹配所要求的颜色，以及成品是否是你实际能用的东西。最好的智能体是能减轻特定工作负担的那一个——而不是仅仅最先完成的那一个。
