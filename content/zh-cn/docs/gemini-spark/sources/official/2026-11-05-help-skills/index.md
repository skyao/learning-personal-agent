---
title: "为 Gemini 应用创建和管理技能"
linkTitle: "帮助：技能"
date: 2026-11-05
originalTitle: "Create & manage skills for Gemini Apps"
sourceUrl: "https://support.google.com/gemini/answer/17094296?hl=en"
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）。2026-10 Spark 改名为 Task 后，帮助页的用词已改为 tasks / task mode"
tags: [持续执行, 连接器]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的默认（Computer）视图；页面中的界面小图标已下载。技能最早是 Spark 的功能，2026-09-30 起扩展到 Gemini 的普通聊天，本页现在同时讲聊天与任务中的技能。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：技能是保存下来的可复用指令，可以在任何聊天或任务线程中使用，多个技能可以组合。可以从聊天、任务或技能页创建：让 Gemini 帮忙写、用预置或空白模板，或上传技能文件或带 SKILL.md 的文件夹。页面列出上传要求：可以附带 .py、.sh、.ipynb、.js 等代码和脚本，但需要联网的脚本暂不支持；技能只在移动应用、Mac 应用和网页版中可用。

**保留理由**：说明了 Spark/Task 的技能机制（可附脚本、文件夹结构、不能联网），可与其他产品的 Skills 对照。

---

你可以使用技能来创建并保存自定义指令，这些指令可在 Gemini 应用中的聊天和任务中通用。无需反复输入你的偏好或上传相同的文件，Gemini 可以自动使用相关技能，你也可以为任务或工作流指定要使用的技能。

借助技能，你可以：

- **节省时间和精力：** 构建一次技能，即可在任何聊天或任务线程中使用。
- **自动化工作流：** 当技能与你当前的提示相关时，Gemini 会自动识别并为你应用。
- **混合搭配技能：** 为单个任务使用多个技能，完全按你的想法处理更复杂的工作。你甚至可以在技能中使用其他技能。

## 你需要什么

要创建和使用技能，你必须：

- **年满 18 岁。**
- **登录 Gemini 应用**。[了解如何登录 Gemini 应用](https://support.google.com/gemini/answer/13278668)。
- **开启 [保留活动记录（Keep Activity）](https://myactivity.google.com/product/gemini?utm_source=help)**。

**重要：** 目前，技能仅在 Gemini 移动应用、Mac 上的 Gemini 应用以及 [gemini.google.com](https://gemini.google.com) 上的 Gemini 网页版中可用。

## 创建技能

你可以从聊天、任务或技能页面创建技能。在技能页面上，你可以在 Gemini 的帮助下创建技能、从预填或空白模板构建技能，或上传技能文件，或上传一个文件夹（其中包含 `SKILL.md` 文件及可选的受支持参考文件）。

**提示：** 你可以在技能指令中引用其他技能，以构建更复杂的工作流。

### 第 1 步：前往技能页面

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏中，点击 **自定义** ![](images/img-02-dc4a4e.png)。
   - 如果找不到「自定义」，请先点击更多 ![](images/img-03-f0faa8.png)。
3. 在顶部，点击 **技能**。

### 第 2 步：选择创建技能的方式

与 Gemini 协作创建技能

1. 在技能页面顶部，点击 **创建** ![然后](images/img-04-bfcdbc.png) **使用 Gemini 创建** ![](images/img-05-99ea29.png)。
2. 按照聊天中的说明操作。

编辑预填模板以创建技能

1. 在技能页面的「推荐」下，点击你想使用的技能模板。
2. 修改名称、说明和指令。
3. 可选：要向技能添加文件，请在顶部点击 **添加**。然后选择上传来源：
   1. 对于设备上的文件，点击 **图片** 或 **文件**。
   2. 对于 Google 应用中的文件，点击来源：**Google 云端硬盘** ![](images/img-06-196795.png)、**Google 相册** ![](images/img-07-3854d6.png) 或 **Notebook** ![Notebook](images/img-08-cd71d2.png)。
   3. 添加文件后，点击 **上传**。
4. 完成后，在顶部点击 **创建**。

**提示：** 要从技能中移除文件，请在技能指令下方找到该文件，然后点击移除 ![](images/img-09-28961f.png)。

使用空白模板创建技能

1. 在技能页面顶部，点击 **创建** ![然后](images/img-04-bfcdbc.png) **手动创建** ![](images/img-10-75ae06.png)。
2. 输入技能的名称、说明其功能的描述，以及它应遵循的指令。
3. 可选：要向技能添加文件，请在顶部点击 **添加**。然后选择上传来源：
   1. 对于设备上的文件，点击 **图片** 或 **文件**。
   2. 对于 Google 应用中的文件，点击来源：**Google 云端硬盘** ![](images/img-06-196795.png)、**Google 相册** ![](images/img-07-3854d6.png) 或 **Notebook** ![Notebook](images/img-08-cd71d2.png)。
   3. 添加文件后，点击 **上传**。
4. 完成后，在顶部点击 **创建**。

**提示：** 要从技能中移除文件，请在技能指令下方找到该文件，然后点击移除 ![](images/img-09-28961f.png)。

上传文件或文件夹以创建技能

**重要：** 目前：

- 不支持需要访问互联网的脚本。
- 你只能通过随技能一起上传来向技能添加参考文件。

要通过上传文件或文件夹创建技能：

1. 在技能页面顶部，点击 **创建** ![然后](images/img-04-bfcdbc.png) 上传 ![](images/img-11-5a2bf9.png)。
2. 选择一个 `SKILL.md` 文件，或选择一个主文件夹中包含 `SKILL.md` 文件的文件夹或 `.zip` 文件。
   - 如果你上传的是文件夹，则会跳过逐个添加文件的选项。
3. 点击 **打开**。
4. 可选：向技能添加文件：
   - 对于设备上的文件，点击 **图片** 或 **文件**。
   - 对于 Google 应用中的文件，点击来源：**Google 云端硬盘** ![](images/img-06-196795.png)、**Google 相册** ![](images/img-07-3854d6.png) 或 **Notebook** ![Notebook](images/img-08-cd71d2.png)。
5. 添加完文件后，点击 **上传**。
6. 查看技能，并进行你想要的任何编辑。
7. 完成后，在顶部点击 **创建**。

### 上传要求

#### 支持的文件类型

你可以上传基于纯文本的文件。如果你能在基本文本编辑器中打开并阅读它，它很可能受支持。

- **支持：**
  - **文档和文本：** `.docx`、`.pdf`、`.rtf`、`.tex`、`.log`、`.md`、`.rst`、`.txt`、`.markdown`、`.odt`
  - **电子表格和数据表：** `.csv`、`.ods`、`.xlsx`
  - **演示文稿和幻灯片：** `.odp`、`.pptx`
  - **照片和图像：** `.jpg`、`.png`、`.svg`、`.gif`、`.heic`、`.ico`、`.jpeg`、`.tif`、`.webp`
  - **代码和脚本：** `.py`、`.sh`、`.ipynb`、`.js`
  - **网页和 UI 文件：** `.css`、`.html`、`.htm`
  - **数据和配置：** `.env`、`.json`、`.toml`、`.xml`、`.yaml`、`.yml`
- **不支持：**
  - **旧版 Microsoft Office：** `.doc`、`.xls`、`.ppt`
  - **照片和图像：** `.raw`
  - **音频和视频文件**
  - **归档和压缩文件**
  - **代码和脚本：** `.cs`、`.kt`、`.kts`、`.php`、`.r`、`.rb`、`.scala`、`.swift`、`.ts`
  - **网页和 UI 文件：** `.jsx`、`.tsx`
  - **数据和配置：** `.sql`

#### 结构与命名

- **技能元数据：** 你的项目必须包含一个位于根（主）文件夹中的 `SKILL.md` 文件。
- **命名约定：** `SKILL.md` 中的技能名称必须全部小写，单词之间用连字符分隔（例如 `my-new-skill`）。
- **大小限制：** 所有上传文件的总大小不得超过 100 MB。

#### 安全限制

- **无外部操作：** 脚本无法在外部网站上执行操作或请求。

**提示：** 上传前，请检查是否有隐藏的二进制文件（例如 `.DS_Store` 或 `.pyc`），它们可能导致上传失败。

在聊天中让 Gemini 创建技能

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在文本框中，请 Gemini 创建技能，并描述你希望该技能做什么。
   - 例如，`Create a skill based on these instructions:` <your instructions>。
3. 点击提交 ![](images/img-12-c4d89f.png)。Gemini 将创建你的技能并将其保存到技能页面。
4. 要修改技能，只需在聊天中描述你的修改。

**提示：** 你无法从聊天或任务线程中启用、停用或删除技能。要执行这些操作，请在侧边栏中点击 **自定义** ![](images/img-02-dc4a4e.png) ![然后](images/img-04-bfcdbc.png) **技能**。

## 探索技能示例

技能可以自动化各种任务和工作流：

- **写作帮助：** 技能可以帮助完成课程作业，并带有不要直接给出答案的特定指令。它可以包含你过去的论文、反馈和分数。
- **头脑风暴：** 技能可以扩展想法，然后基于标准模板生成设计文档。
- **战术支持：** 技能可以帮助完成特定任务，例如将银行对账单转换为格式化电子表格，或为网站生成产品描述。
- **职业指导：** 技能可以根据你的简历提供职业机会建议。

## 为任务使用技能

技能设计为在后台工作，可跨 Gemini 聊天和任务使用。你可以让 Gemini 为任务使用特定技能。当技能与你的任务相关时，Gemini 也可以自动使用它。

- **让 Gemini 使用技能：** 在聊天或任务线程中，输入 `/`（如果你有更新后的快捷方式，则输入 `@`），然后选择技能。
- **Gemini 自动使用技能：** Gemini 可以根据任务的上下文和意图自动使用已启用的技能。
- **组合技能：** 你可以在单个任务中让 Gemini 使用多个技能。这有助于 Gemini 有效完成复杂的多步骤任务。

## 管理你的技能

你可以从技能页面管理你的技能。

管理 Gemini 对技能的自动使用

Gemini 只能自动使用已开启的技能。你可以随时关闭技能。如果某个技能已关闭，而你让 Gemini 使用它，Gemini 会询问你是否要重新开启。

**要让 Gemini 停止自动使用某项技能：**

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏中，点击 **自定义** ![](images/img-02-dc4a4e.png)。
   - 如果找不到「自定义」，请先点击更多 ![](images/img-03-f0faa8.png)。
3. 在顶部，点击 **技能**。
4. 点击你希望 Gemini 停止使用的技能。
5. 在顶部，点击更多 ![](images/img-03-f0faa8.png) ![然后](images/img-04-bfcdbc.png) **停用** ![](images/img-13-c96774.png)。

**要让 Gemini 再次自动使用某项技能**，请按相同步骤操作，然后点击 **启用** ![](images/img-14-0ea28f.png)。

编辑技能

**重要：** 要更新技能中的文件，你需要重新上传整个技能及其参考文件。

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏中，点击 **自定义** ![](images/img-02-dc4a4e.png)。
   - 如果找不到「自定义」，请先点击更多 ![](images/img-03-f0faa8.png)。
3. 在顶部，点击 **技能**。
4. 点击你要编辑的技能。
5. 进行你的编辑。
   - 要直接编辑，请更新「说明」和「指令」字段。
   - 要以对话方式编辑，请点击更多 ![](images/img-03-f0faa8.png) ![然后](images/img-04-bfcdbc.png) **使用 Gemini 编辑** ![](images/img-15-9ea990.png)。
   - 要上传文件来替换技能，请点击更多 ![](images/img-03-f0faa8.png) ![然后](images/img-04-bfcdbc.png) **替换技能** ![](images/img-11-5a2bf9.png)。
6. 管理技能中的文件：
   - 要添加文件，请点击 **添加文件**。
   - 要移除文件，请在技能指令下方找到该文件，然后点击移除 ![](images/img-09-28961f.png)。
   - 要替换文件，请点击更多 ![](images/img-03-f0faa8.png) ![然后](images/img-04-bfcdbc.png) **替换文件** ![](images/img-16-c6f183.png)。
7. 完成后，在顶部点击 **保存**。

**提示：** 你也可以让 Gemini 更新技能及其文件。

删除技能

**重要：** 如果你删除某个技能，将无法撤销。

你只能从技能页面删除技能。

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏中，点击 **自定义** ![](images/img-02-dc4a4e.png)。
   - 如果找不到「自定义」，请先点击更多 ![](images/img-03-f0faa8.png)。
3. 在顶部，点击 **技能**。
4. 将鼠标悬停在要删除的技能上。
5. 点击更多 ![](images/img-03-f0faa8.png) ![然后](images/img-04-bfcdbc.png) **删除** ![](images/img-17-23ae4d.png)。

下载技能

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏中，点击 **自定义** ![](images/img-02-dc4a4e.png)。
   - 如果找不到「自定义」，请先点击更多 ![](images/img-03-f0faa8.png)。
3. 在顶部，点击 **技能**。
4. 将鼠标悬停在要下载的技能上。
5. 点击更多 ![](images/img-03-f0faa8.png) ![然后](images/img-04-bfcdbc.png) **下载** ![](images/img-18-cd655c.png)。这会将你的技能下载为 `.zip` 文件。
   - 为保持实时连接，技能中的任何 Google 云端硬盘文件和笔记本不会包含在下载内容中。

## 常见问题

任务、计划和技能有什么区别？

为了帮助你充分利用任务，了解支撑其逻辑的三个构建块会很有帮助：任务、计划和技能。可以把它们看作做什么、何时做和如何做。

**任务是你的高层目标。** 它代表你希望 Gemini 为你管理的一个完整项目或目标。

- **示例：**「规划并管理我去伦敦的商务旅行。」

**计划让你把任务交给** Gemini，使其在后台自动运行。你告诉 Gemini 要做什么以及何时做。任务可以安排在特定日期和时间运行，或针对某个事件运行。

- **示例：**「每天上午 8 点（条件），给我一份 AI 新闻更新（任务）」
- **示例：**「当我的航班延误时（条件），通知我并提出行程更新建议（任务）。」

**提示：** 任务计划与 Gemini 聊天中的已计划操作不同。[了解如何在 Gemini 应用中安排操作](https://support.google.com/gemini/answer/16316416)。

**技能是一组可复用的指令和补充上下文。** 它教会 Gemini 如何完成特定任务以及使用哪些工具。你可以指定 Gemini 在某个任务或计划操作中应使用的技能。当技能与任务相关时，Gemini 也可以自动使用它。

- **示例：** 同时使用「旅行预订」技能和「Gmail 写作」技能来重新预订房间并发送确认。

总之，你定义任务（你想要什么）、设置计划（应在何时发生），并提供技能（如何完成），以完成工作。

如果我取消或降级 Google AI 订阅会怎样？

如果你取消 Google AI 订阅，或降级到不支持访问 Gemini 中任务功能的订阅，你将失去对 Gemini 中的任务功能、任务和计划的访问权限。你的数据会被保留，但某些功能会暂停或停用：

- **进行中的任务**会完成，但不会被删除。
- **计划**会暂停，但不会被删除。

要重新获得这些功能的访问权限，你需要升级或重新订阅支持 Gemini 中任务功能的 Google AI 订阅。[了解如何管理你的 Google AI 订阅](https://support.google.com/gemini/answer/14517446)。

**提示：** 技能无需 Google AI 订阅即可使用，并可在你的聊天中使用。

如何将我的 Gems 重建为技能？

当我们移除 Gems 时，我们会自动将你的 Gems 重建为技能。如果你想更早开始将 Gems 作为技能使用，可以手动重建它们。[了解如何将你的 Gems 重建为技能](https://support.google.com/gemini/answer/18560919#gem_to_skill)。

## 相关资源

- [在 Gemini 应用中管理任务与工作流](https://support.google.com/gemini/answer/17094507)
- [为 Gemini 应用编写有效的技能](https://support.google.com/gemini/answer/17102773)
