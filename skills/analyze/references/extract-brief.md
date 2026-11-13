# 提取要点的子 agent 任务说明

产品维度第 3 步交给每个提取子 agent 的通用说明（2026-11-13 Muse 分析时使用）。用时把 `<产品>` 换成产品名，另附该子 agent 的任务清单（`inventory.py` 输出的若干行）和笔记的输出路径。

---

# 子 agent 任务：从 <产品> 资料中提取分析要点

仓库根目录：/home/claude2/work/code/learning/learning-personal-agent
资料页文件：`content/zh-cn<路径>/index.md`（没有时读 `_index.md`）。frontmatter 之后是中文正文（外文资料已是译文）。不要读 `original.md`，除非 translation=待翻译。fidelity=仅链接 的资料没有正文，只记基本信息。
主题定义与问题：`skills/analyze/references/topics.md`（先读「各主题要回答的问题」部分）。

你只负责下面「任务清单」中的资料，逐篇读完。industry 资料只提取与 <产品> 有关的内容（含与其他产品的比较）。

## 输出

写一个 Markdown 文件到指定路径。按下列一级小节组织（没有内容的小节写「无」）：

`## runtime` / `## memory` / `## continuous-execution` / `## connectors` / `## channels` / `## devices` / `## models` / `## security` / `## privacy` / `## access-pricing` / `## business` / `## reliability` / `## timeline`（发布、功能更新、开放地区等带日期的事件） / `## positioning`（定位、与其他产品对比、厂商战略） / `## source-issues`（资料页本身的问题：标签不准、日期不对、摘要与正文不符、二手未注出处、内容过时等）

每条要点一行：

```
- <要点，一句话，写清事实、数字、口径、时间点> ｜ <资料路径，如 /docs/muse/sources/official/2026-09-08-introducing-muse> ｜ <证据类型：官方/媒体一手/媒体转述/社区实测/社区观点/用户实测> ｜ 「原文短引，≤40 字」
```

规则：

- 只写资料里有的内容，不加自己的知识；推断标「（作者推断）」或「（资料作者观点）」。
- 数字照抄原文口径，不换算。不同资料矛盾时都记下。
- 媒体资料的 frontmatter 有 basedOn，或正文说明转述自他处时，证据类型写「媒体转述（来源）」。
- 媒体名以资料页 frontmatter 为准，不凭印象写。
- 不回传原文段落；短引不超过 40 字。
- 同一事实多篇资料都说时，可合并为一条并列出多个路径。
- 资料路径每处都写全（以 `/docs/` 开头），不要用 `S=`、`I=` 之类的缩写：主对话用脚本按完整路径核对覆盖与合并笔记（2026-11-13 Manus Cue 分析时一组笔记用了缩写，核对时整组报漏）。
- 要点要具体，宁多勿漏，但不复述与主题无关的背景。
- 完成后只回复一行：文件路径和要点条数。
