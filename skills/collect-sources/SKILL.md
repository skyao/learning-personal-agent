---
name: collect-sources
description: 为 Personal Agent 学习笔记收集资料：检索各跟踪产品与行业综合的新资料，去重后按原文全文（外文翻译为中文）保存到对应的 sources 目录，按来源类型分目录、按固定词表打主题标签。用于定期收集、补录某篇资料、或检查资料完整性。只收集，不分析、不总结。
---

# 收集 Personal Agent 资料

这个 skill 负责笔记的「资料收集」一侧。核心原则：**素材归素材，分析归分析。** 收集阶段只保证信息准确、完整、可追溯，不写任何理解、判断或摘要。

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
          index.md
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
- 不在跟踪清单中的产品：不建目录，写入本轮报告的「候选产品」，由用户决定是否纳入。

## 每轮收集的流程

1. **读现状。** 读 `references/tracking.md` 和本轮要收集的产品 skill；列出已有资料的 `sourceUrl` 与 `altUrls`：
   ```bash
   grep -rhE "^(sourceUrl|altUrls):" content/zh-cn/docs --include=index.md | sort
   ```
2. **检索。** 按产品 skill 列出的渠道，先查官方，再查媒体与社区，时间范围从「最后收集日期」前三天起（覆盖时区与延迟收录）。首次收集不限起始日期。行业综合按 tracking.md 中的关键词检索。
3. **筛选。** 逐条判断：
   - 是否与 Personal Agent 相关（标准见 tracking.md）。模型类资料按 tracking.md 的「模型资料的收录原则」判断：只收明确与 Personal Agent 相关的。
   - 是否重复：同一 URL、`altUrls` 中的地址、同一文章的转载、同一内容的不同语言版本，都算重复。发现已收资料的新地址时，补进它的 `altUrls`。已有转载版而找到原文时，用原文替换，更新 `fidelity`。
   - 是否可信：按 source-types.md 判断；SEO 聚合站、内容农场、无署名的搬运站直接放弃。
   - 是否有实质内容：只复述官方公告、没有新信息的媒体稿不收；同一事件优先收官方原文和一手报道。
4. **取全文。** 按 source-page.md 的「取全文」一节和产品 skill 中的抓取方法读取原文全文。原文无法读取（付费墙、反爬）时，找完整转载并在 `fidelity` 注明；只能取得部分内容时标为节选。取不到可信全文的资料不收，记入本轮报告。
5. **保存。** 按 [references/source-page.md](references/source-page.md) 的模板和翻译规则写页面，放入对应类型目录，打标签，图片下载到页面目录的 `images/`。
6. **校验。** 运行 `npm run build`，退出码必须为 0；确认新页面出现在 `sources/` 清单中。
7. **更新状态。** 在产品 skill 中更新「最后收集日期」；行业综合的日期在 tracking.md 中更新。收集中发现的新渠道、抓取方法或页面结构问题，补进产品 skill 的对应小节。
8. **提交。** 资料收集单独提交，不与其他修改混在一起。提交信息写明产品与篇数，例如 `collect: muse 3 篇，industry 2 篇`。
9. **报告。** 向用户输出本轮报告：
   - 新收资料：产品、类型、日期、标题、标签。
   - 放弃的资料及原因（重复、不可信、取不到全文、无新信息）。
   - 候选产品。
   - 词表无法覆盖的主题：列出资料和建议的新标签，由用户决定是否加入词表。

## 不做的事

- 不在资料页写摘要、按语、「我的理解」、要点提炼或评价。
- 不改写中文原文的表述，不纠正原文的事实错误；原文明显笔误也照录。
- 不合并多篇资料为一页，不把一篇资料拆成多页。
- 不修改 `analysis/` 下的任何页面。
- 不使用词表以外的标签。
- 不为了凑数收录低质量资料；一轮没有新资料是正常结果。
