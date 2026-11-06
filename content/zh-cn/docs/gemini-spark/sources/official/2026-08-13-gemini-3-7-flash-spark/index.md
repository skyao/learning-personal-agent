---
title: "Gemini 3.7 Flash 发布（改进 Gemini Spark 一节）"
linkTitle: "3.7 Flash 驱动 Spark"
date: 2026-08-13
originalTitle: "Introducing Gemini 3.7 Flash"
sourceUrl: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/"
author: "Tulsee Doshi"
publisher: "Google（The Keyword 博客）"
language: en
fidelity: 节选
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "博客页面显示 2026-08-13；The Verge 同日报道「Gemini Spark is now powered by Google's upgraded Flash model」"
tags: [模型]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：模型发布文，按 tracking.md 的「模型资料的收录原则」只收「Improving Gemini Spark with 3.7 Flash」一节（文章说明该模型用于驱动 Spark）；模型能力、开发者价格、安全与基准各节未收。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：这一节说明 Gemini Spark（当时面向 160 多个国家的 Google AI Pro 和 Ultra 订阅用户）改用 Gemini 3.7 Flash，称新模型让 Spark 更高效地把想法变成行动，例如合并文件、起草邮件、更新状态文档。

**保留理由**：Spark 底层模型从 3.5 换成 3.7 Flash 的官方出处，属于「模型专门用于驱动 Personal Agent」的情形。

---

## 用 3.7 Flash 改进 Gemini Spark

面向 160 多个[国家](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform%3DAndroid&sjid=2353166824601345951-NA#:~:text=Available%20wherever%20Gemini%20Apps%20are%20supported%2C%20except%20in%20the%20European%20Economic%20Area%2C%20Nigeria%2C%20Switzerland%2C%20and%20the%20United%20Kingdom)的 Google AI Pro 和 Ultra 订阅用户可用的 Gemini Spark，将从今天起使用 Gemini 3.7 Flash。我们在 I/O 上发布了 Spark，它是你的个人 AI 智能体，全天候（24/7）运行，在你的指示下代表你采取行动。这次模型更新让 Spark 在处理知识工作时更高效，改进了对 Google Workspace 应用的工具使用，为复杂的多技能工作流带来更高的准确性和输出质量。

借助 3.7 Flash，Gemini Spark 可以通过合并文件、起草电子邮件和更新状态文档，更高效地把想法变成行动。
