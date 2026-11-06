---
name: collect-sources
description: 为 Personal Agent 学习笔记收集资料：检索各跟踪产品与行业综合的新资料，去重并判断是否值得保留；保留的资料把原文全文存档，资料页只写来源信息、简短摘要和保留理由，外文翻译交给另外的翻译 agent。按来源类型分目录、按固定词表打主题标签。用于定期收集、补录某篇资料、或检查资料完整性。不做分析。
---

# 收集 Personal Agent 资料

这个 skill 负责笔记的「资料收集」一侧。核心原则：**素材归素材，分析归分析。** 收集阶段只保证信息准确、完整、可追溯。资料页上收集者自己写的内容只有两小节：简短的摘要和保留理由，都标明是收集者所写，不写分析或评价。

**收集与翻译分开（用户 2026-11-05 决定）。** 收集 agent 负责检索、抓取、判断和写资料页，不做翻译；原文全文由脚本存为资料目录下的 `original.md`（网站上不可见）。外文资料的翻译由另外的翻译 agent 按 [references/translator.md](references/translator.md) 完成。

## 站点结构

```
content/zh-cn/docs/
  <product>/                   每个跟踪产品一个目录，例如 muse
    _index.md                  产品概览
    sources/                   资料收集（本 skill 只写这里）
      _index.md                资料清单，由 {{< source-list >}} 自动生成
      official/                官方
      media/                   媒体
      community/               社区
      exploration/             实测
        YYYY-MM-DD-<slug>/     一篇资料一个目录
          index.md             资料页：来源信息、摘要、保留理由（翻译后在分隔线下加译文）
          original.md          外文原文全文存档；不生成页面，网站上不可见
          images/
    analysis/                  资料分析和总结（本 skill 不写；以后按标签分目录）
  industry/                    行业综合：涉及多个产品的比较、评测、综述
    sources/                   与产品目录相同的四个类型子目录
```

- 资料按**来源类型**放入子目录，每篇只属于一类。类型的判断标准见 [references/source-types.md](references/source-types.md)。
- 资料按**主题**打标签，一篇可以有多个标签。标签只能从 [references/tags.md](references/tags.md) 的词表中选，不得自造。
- 跟踪哪些产品见 [references/tracking.md](references/tracking.md)。每个产品另有自己的 skill（`skills/collect-<product>/`），记录该产品的来源渠道、抓取方法、收录范围、已知问题和最后收集日期。本 skill 的通用规则与产品 skill 冲突时，以产品 skill 为准。
- 新建产品目录或类型子目录时，用 [references/section-templates.md](references/section-templates.md) 中的 `_index.md` 模板。

## 资料放在哪里

- 只涉及一个产品：放在 `<product>/sources/<类型>/`。
- 比较或评测两个及以上产品，或讨论 Personal Agent 整体：放在 `industry/sources/<类型>/`，frontmatter 的 `products` 列出涉及的产品。只存这一份，不在各产品目录下复制。
- 用户自己的上手实测：放在 `exploration/`。实测记录只能来自用户提供的原始记录或用户明确要求执行的操作，不得自行编写或补全观察结果。
- 新建产品目录时，先问用户是否已有该产品的实测材料（包括旧笔记 learning-ai-agent 中的原创记录）需要迁入 `exploration/`；迁入时正文原样保留，图片和附件一并复制，`fidelity: 实测记录`，在 `dateNote` 写明迁移来源。
- 不在跟踪清单中的产品：不建目录，写入本轮报告的「候选产品」，由用户决定是否纳入。

## 每轮收集的流程

1. **读现状。** 读 `references/tracking.md` 和本轮要收集的产品 skill；列出已有资料的 `sourceUrl` 与 `altUrls`：
   ```bash
   grep -rhE "^(sourceUrl|altUrls):" content/zh-cn/docs --include=index.md | sort
   ```
2. **检索。** 按产品 skill 列出的渠道，先查官方，再查媒体与社区，时间范围从「最后收集日期」前三天起（覆盖时区与延迟收录）。首次收集不限起始日期，并对照旧笔记 learning-ai-agent（`../learning-ai-agent/content/zh-cn/agents/personal/<产品>/`，尤其是资料索引页）中引用过的来源，逐条判断是否收录：旧笔记常引用通用帮助页里的产品小节、应用商店页和厂商的另一套文档站（如 Grok Bot 在 cursor.com 之外还有 docs.x.ai），单靠检索容易漏掉（用户 2026-11-05 建议）。行业综合按 tracking.md 中的关键词检索。
3. **筛选。** 逐条判断：
   - 是否与 Personal Agent 相关（标准见 tracking.md）。模型类资料按 tracking.md 的「模型资料的收录原则」判断：只收明确与 Personal Agent 相关的。
   - 是否重复：同一 URL、`altUrls` 中的地址、同一文章的转载、同一内容的不同语言版本，都算重复。发现已收资料的新地址时，补进它的 `altUrls`。已有转载版而找到原文时，用原文替换，更新 `fidelity`。
   - 是否可信：按 source-types.md 判断；SEO 聚合站、内容农场、无署名的搬运站直接放弃。
   - 是否有实质内容：只复述官方公告、没有新信息的媒体稿不收；同一事件优先收官方原文和一手报道。
4. **取全文并判断。** 按 source-page.md 的「取全文」一节和产品 skill 中的抓取方法取得原文全文，抽取结果直接由脚本写入临时文件，再决定收不收（读法见「省用量的做法」）。原文无法读取（付费墙、反爬）时，找完整转载并在 `fidelity` 注明；只能取得部分内容时标为节选。取不到可信全文的资料不收，记入本轮报告。
5. **保存。** 资料页的结构所有产品一致：来源信息块，收录说明、内容摘要、保留理由三段，分隔线，正文（见 source-page.md 的「页面正文」）。按 [references/source-page.md](references/source-page.md) 的规则：外文原文由脚本整理后存为 `original.md`，图片下载到 `images/`；写 `index.md`（frontmatter、收录说明、摘要、保留理由），`translation` 填「待翻译」。放入对应类型目录，打标签。
6. **校验。** 运行 `npm run build`，退出码必须为 0；确认新页面出现在 `sources/` 清单中。
7. **更新状态。** 在产品 skill 中更新「最后收集日期」；行业综合的日期在 tracking.md 中更新。收集中发现的新渠道、抓取方法或页面结构问题，补进产品 skill 的对应小节。
8. **提交。** 资料收集单独提交，不与其他修改混在一起。提交信息写明产品与篇数，例如 `collect: muse 3 篇，industry 2 篇`。
9. **报告。** 向用户输出本轮报告：
   - 新收资料：产品、类型、日期、标题、标签、是否待翻译。
   - 放弃的资料及原因（重复、不可信、取不到全文、无新信息）。
   - 候选产品。
   - 词表无法覆盖的主题：列出资料和建议的新标签，由用户决定是否加入词表。

## 省用量的做法

收集的开销主要不在检索和抓取，而在主对话：上下文越长，每一轮重读的代价越高；输出的单价又是输入的数倍，全文翻译的输出量最大。因此收集阶段不翻译（用户 2026-11-05 决定），并按下面的方法读写：

- **原文不经过模型输出。** 抽取、清理、存为 `original.md` 都用脚本和 shell 完成（`extract.py` 输出重定向到文件、`sed` 删改网页残留），不在对话中逐段写出原文。
- **原文不整篇进入主对话。** 判断收不收时，先看标题结构、字数、元数据，用 `grep` 定位产品名与关键词所在段落，用 `sed -n` 只读需要判断的段落。大多数资料这样就能判断；长文确实需要通读时，可以交给使用较便宜模型的子 agent 读完回报要点（例如有无一手实测、是否只转述官方说法），子 agent 不回传原文。
- **摘要与保留理由要短。** 摘要 3–5 句，保留理由 1–2 句，见 source-page.md。
- **按批次开新会话。** 一个产品的官方、媒体与社区资料可以分批，每批一个新会话。进度、渠道和逐篇判断都记在产品 skill 里，新会话读 skill 即可接续，不依赖之前的对话。

## 不做的事

- 不在资料页写摘要与保留理由以外的内容：不写按语、「我的理解」、要点提炼或评价；摘要只复述原文已有的信息。
- 收集阶段不翻译；翻译由翻译 agent 按 references/translator.md 完成。
- 不改写中文原文的表述，不纠正原文的事实错误；原文明显笔误也照录。
- 不合并多篇资料为一页，不把一篇资料拆成多页。
- 不修改 `analysis/` 下的任何页面。
- 不使用词表以外的标签。
- 不为了凑数收录低质量资料；一轮没有新资料是正常结果。
