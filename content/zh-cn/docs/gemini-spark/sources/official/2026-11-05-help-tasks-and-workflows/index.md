---
title: "在 Gemini 应用中管理任务与工作流"
linkTitle: "帮助：任务总览"
date: 2026-11-05
originalTitle: "Manage your tasks & workflows in Gemini Apps"
sourceUrl: "https://support.google.com/gemini/answer/17094507?hl=en"
altUrls: ["https://support.google.com/gemini/answer/17094507?hl=zh-Hans"]
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
updatedAt: 2026-11-10
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）。2026-10 Spark 改名为 Task 后，帮助页的用词已改为 tasks / task mode；2026-11-10 发现原文更新：「What you need」删去了「选择加入 Personal Intelligence」一条，原文存档与译文同步删除，其余未变"
tags: [持续执行, 运行环境, 安全, 开放与价格]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的默认（Computer）视图；页面中的界面小图标已下载。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：使用任务（原 Spark）需要年满 18 岁、个人 Google 账号、Google AI Pro 或 Ultra 订阅、开启 Keep Activity；除欧洲经济区、尼日利亚、瑞士和英国外，凡支持 Gemini 应用的地区都可用，入口为移动应用、Mac 应用和网页版。页面说明怎样创建、查看和接管任务：Gemini 可以在本地或远程浏览器中操作网页，用户可随时「Take over」；远程浏览器会保存 Cookie 等登录信息，远程计算机会保存代码执行数据，都可以在设置里删除。任务可以使用技能、计划、自定义应用和多种 Google 服务；最多同时运行 15 个任务，用量按计算量计、随订阅档位提高。安全部分列出：发送消息、修改删除数据、购物、金融交易、提交表单等动作每次都要确认，有敏感信息检查、禁止任务识别、「Take control」模式和计划展示，并提示提示注入风险。

**保留理由**：Task 功能最完整的官方说明，包括准入条件、本地与远程浏览器、并发上限和确认机制。

---

你现在可以在开始聊天的同一处启动任务。你可以把任务指派给 Gemini，用来自动化复杂工作流，并为持续进行的任务管理计划。Gemini 可以借助关联应用（Connected Apps）、技能、聊天、你已登录的网站、个人智能（Personal Intelligence）、位置等来源的信息来帮助处理任务。只需告诉 Gemini 你的具体目标，以及你希望任务在何时完成。

例如，你可以为 Gemini 创建任务来帮助：

- **节省时间：** Gemini 可以通过汇总或归档新闻邮件来清理你的收件箱、在休假后创建紧急待办清单，以及退订邮件列表。
- **节省开支：** 当航班和酒店价格降到你的预算范围内时，Gemini 可以监控并提醒你。
- **深入研究主题并创建文件：** Gemini 可以查找带引用来源的研究资料，并把结果打包成可下载的文件，例如 PDF、文档、电子表格和演示文稿。

**提示：** 任务中的计划与聊天中的计划不同。[了解聊天中的计划如何运作](https://support.google.com/gemini/answer/16316416?)。

## 你需要什么

要把任务指派给 Gemini，你必须：

- **年满 18 岁**。
- **使用个人 Google 账号登录 Gemini 应用。** 目前，如果你使用工作或学校 Google 账号登录，此功能不可用。[了解如何登录 Gemini 应用](https://support.google.com/gemini/answer/13278668)。
- **拥有 Google AI Pro 或 Ultra 订阅。** [了解如何升级](https://support.google.com/gemini/answer/14517446)。
- **开启 [保留活动记录（Keep Activity）](https://myactivity.google.com/product/gemini?utm_source=help)**。

**重要：** 目前，Gemini 中的任务：

- 在支持 Gemini 应用的所有地区可用，但欧洲经济区、尼日利亚、瑞士和英国除外。
- 仅在 Gemini 移动应用、Mac 上的 Gemini 应用以及 [gemini.google.com](https://gemini.google.com) 上的 Gemini 网页版中可用。

## 在把任务指派给 Gemini 之前

直接在任务线程中输入信息时要小心

不要将登录信息、付款详情或你认为敏感的信息直接输入任务线程。如有需要，接管 Gemini 的浏览器或本地浏览器，然后直接在网页上输入相关信息。

避免安排你认为敏感的任务

Gemini 仍在学习，可能会犯错。为帮助保障你的信息安全并防止非预期的操作，请避免使用你认为敏感的信息或执行你认为敏感的操作的任务或计划。这些任务可能需要你的监督和输入。

如果计划在你离线时运行，你可能无法阻止 Gemini 完成非预期的操作。某些任务可能需要你确认后 Gemini 才会完成。[详细了解任务和计划](https://support.google.com/gemini/answer/17094710)。

Gemini 中的任务如何与浏览器配合工作

你可以让 Gemini 完成涉及与网站交互的任务，例如购物、预订旅行或预订晚餐。为处理你的任务，Gemini 会使用来自关联应用、技能、聊天、任务、你已登录的网站、个人智能、位置[等来源](https://support.google.com/gemini?p=lm_agent_sources)的信息。

要与网站交互，Gemini 可以连接你桌面上的本地 Chrome 浏览器，或在云端使用单独的远程浏览器。目前，Chrome 自动浏览（Chrome auto browse）仅在桌面端可用。

**如果你使用本地浏览器：** Gemini 可以访问与你相同的所有网站，包括你已登录的网站。在代表你行动时，Gemini 会与第三方分享必要的信息。这可能包括你的姓名、联系信息、文件、偏好以及你可能认为敏感的信息。经你许可，它还可以使用你保存在密码管理器（Password Manager）中的登录信息来登录会员计划和在线账户。

要让 Gemini 使用你的本地浏览器处理任务，你需要让设备和 Google Chrome 保持唤醒并运行。如果你在任务完成前关闭或关掉设备，或者设备不可用，Gemini 可能会使用远程浏览器来完成任务。

**如果你使用远程浏览器：** 即使你关闭设备，Gemini 也会继续处理你的任务，并且远程浏览器仅在移动设备上使用。对于某些步骤，例如登录网站，任务会暂停，直到你接管并完成该步骤。

**说明：**

- 当 Gemini 首次需要在某台设备上为你浏览网页时，Chrome 会请求你允许将 Chrome 自动浏览连接到 Gemini。
- 此后，对于每项涉及网页浏览的任务，Gemini 都会先请求确认。
- 你可以关闭 Gemini 在某台设备上的自动浏览能力。点击更多 ![](images/img-01-53995d.png) ![然后](images/img-02-bfcdbc.png) **设置** ![然后](images/img-02-bfcdbc.png) **AI 创新** ![然后](images/img-02-bfcdbc.png) **Chrome 中的 Gemini**。

#### 跟踪任务

你可以打开任务线程，查看 Gemini 是否为该任务使用浏览器。你可以随时阻止 Gemini 进行网页浏览。在 Chrome 中的 Gemini 侧边面板中，点击停止 ![](images/img-03-440b63.png)。如果这样做，Gemini 会尝试找出继续执行任务的后续步骤。这可能涉及使用远程浏览器进行网页浏览，或启用其他工具；也可能意味着 Gemini 放弃该任务。

如果你想自己彻底取消任务，在 Gemini 文本框中点击停止 ![](images/img-03-440b63.png)。

## 开始使用 Gemini 中的任务

你可以通过对话方式获得设置首批技能和任务的帮助。只需在任务中输入「set up」「get started」或「interview me」。

[了解 Gemini 可以为你的任务使用哪些内容](#sources)。

## 创建任务

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-04-4a5c21.png)。
2. 在文本框下方，点击 **任务**。
3. 在文本框中描述你希望 Gemini 管理的任务。
   - 你可以告诉 Gemini 何时运行任务，例如在某个特定时间前后，或在某个事件之后。[详细了解计划](https://support.google.com/gemini/answer/17094710)。
   - 要指定使用现有技能，请输入 `@`，然后选择该技能。[详细了解技能](https://support.google.com/gemini/answer/17094296)。
   - 你可以让 Gemini 生成文件，例如 PDF、文档和演示文稿。[了解 Gemini 可以创建哪些文件](#created_files)。
   - 在某些 Gemini 应用中，你还可以让 Gemini 使用自定义关联应用。[了解如何连接自定义应用](https://support.google.com/gemini/answer/17209137)。
   - 要更改 Gemini 模型或思考级别，点击顶部的模型菜单。[了解模型和思考级别](https://support.google.com/gemini/answer/18648722)。
4. 要向任务添加文件，点击上传和工具 ![](images/img-05-72d6a4.png)，然后选择以下选项之一：
   - **上传文件** ![](images/img-06-0940a6.png)
   - **从云端硬盘添加** ![](images/img-07-196795.png)
   - **添加 Notebook** ![Notebook](images/img-08-cd71d2.png)
5. 点击提交 ![](images/img-09-c4d89f.png)。
6. 要在任务运行期间更改 Gemini 的做法，只需在文本框中输入补充说明。
   - Gemini 会在不丢失进度的情况下更新其工作。
   - 如果 Gemini 当时正在为你的任务使用某项功能或关联应用，完全停止可能需要几秒钟。
7. 定期查看任务，以了解 Gemini 可能需要你提供的任何输入。例如，如果 Gemini 需要你在其浏览器中执行某些操作，它会请你接管任务。

**提示：** 在 Mac 上的 Gemini 应用中，如果已设置任务，你可以从其他设备让 Gemini 在你的 Mac 上执行操作。[了解如何远程控制 Mac 上的 Gemini 应用](https://support.google.com/gemini/answer/17208717#remote_control)。

### 任务示例

- 清理收件箱：汇总或归档新闻邮件，并退订邮件列表。
- 获取定制的新闻摘要：深入了解你关心的新闻，并跟踪其后续发展

## 查看和管理任务

要查看和管理任务，包括任何相关权限和计划，请打开任务线程及其工作面板。

打开任务线程并查看任务进度

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-04-4a5c21.png)。
2. 在侧边栏中，点击你要查看或管理的任务对应的线程。
3. 要给 Gemini 更多指示或更改指示，请在任务线程中告诉 Gemini。
4. 要显示此任务线程的工作面板，请在线程顶部点击进度标签。在这里可以找到线程中任务的步骤和进度。

   |  |  |
   | --- | --- |
   |  | 已完成的步骤  当前步骤  计划中的步骤 |

查看 Gemini 读取或更新的文件

在任务线程的工作面板中，在「文件」下，你可以查看 Gemini 为该线程中的任务读取或更新的文件。你可以点击文件将其打开。

在线程中暂停和恢复计划

1. 在任务线程中，点击已计划任务标签。
2. 在顶部，点击更多选项 ![](images/img-01-53995d.png) ![然后](images/img-02-bfcdbc.png) **暂停** ![](images/img-10-ba979f.png) 或 **恢复** ![](images/img-11-1de8b2.png)。

**提示：** 在 Gemini 网页版中，你也可以从「已计划」页面暂停和恢复计划。[了解如何管理你的计划](https://support.google.com/gemini/answer/17094710)。

查看、编辑或下载 Gemini 创建的文件

当 Gemini 在你的任务中创建文件时，你可以直接在任务线程中访问它们。

- 对于 Markdown 和纯文本文件，Gemini 会在 Canvas 中显示文件，你可以在其中直接编辑。
- 对于其他文件，Gemini 会提供文件链接，你可以打开并以对话方式编辑。

#### 从 Canvas 导出文件

1. 在任务线程中，找到包含该文件的 Canvas 编辑器。
2. 在顶部，点击 **导出** ![然后](images/img-02-bfcdbc.png) **.txt**、**.md** 或 **云端硬盘**。

#### 打开并下载链接的文件

1. 在任务线程中，找到该文件。
2. 在文件旁边，点击 **打开**。
3. 要下载文件，请在顶部点击下载 ![](images/img-12-cd655c.png)。

#### 编辑生成的文件

在任务线程中：

- 告诉 Gemini 你想在生成的文件中更新什么。
- 对于某些文件类型，可直接在任务线程中编辑。

#### Gemini 可以创建的文件

Gemini 可以在你的任务中生成以下文件格式：

- **文本和标记语言：** .json、.md、.tex、.txt
- **文档：** .pdf、.docx
- **电子表格和表格数据：** .csv、.tsv、.xlsx
- **演示文稿：** .pptx
- **代码：** .py、.js、.ts、.cpp、.cc、.c、.h、.java、.go、.rs、.cs、.php、.rb、.swift、.kt、.dart、.sql、.sv、.sh
- **网页和 UI：** .html、.jsx、.tsx (React)、Angular
- **图像和图形：** .png、.jpg 或 .jpeg、.svg
- **音频和视频：** .mp3、.mp4、
- **归档和压缩文件：** .tar、.tar.gz、.gz、.zip

**提示：** Gemini 还可以创建 Google 文档、演示文稿和电子表格。[详细了解 Google Workspace 中的操作](#workspace_actions)。

## 监控和接管任务

Gemini 可以在本地或远程浏览器中完成你的一些任务。例如，它可以导航到某个网站并与页面交互，比如将商品添加到购物车。你可以随时接管浏览器。对于某些操作，Gemini 会请你接管任务。

登录网站

当 Gemini 到达登录页面时，如果可用，它会请你确认使用「使用 Google 登录」。如果不可用，它会请你接管并手动登录。

接管远程浏览器任务

1. 在任务线程中，在「Gemini 正在使用 Chrome」旁边，点击 **查看实时画面**。这会在远程计算机上打开 Gemini 的浏览器。
2. 将鼠标悬停在 Gemini 的浏览器上。
3. 点击 **接管任务** ![](images/img-13-f3ad3c.png) ![然后](images/img-02-bfcdbc.png) **接管任务**。
4. 完成你的步骤。
5. 要将控制权交还给 Gemini，请在顶部点击 **返回 Gemini**。

接管本地浏览器任务

[了解如何管理通过 Chrome 自动浏览完成的任务](https://support.google.com/gemini/answer/16821166)。

## 删除远程浏览器和计算机数据

删除本地浏览器数据

你随时可以从设备上的 Chrome 浏览器中删除数据。[了解如何在 Chrome 中删除本地浏览器数据](https://support.google.com/chrome/answer/2392709)。

删除远程浏览器数据

当 Gemini 使用远程浏览器完成任务时，浏览器数据（例如包含你网站身份验证信息（你的登录详情）的 Cookie）会为你方便而保存，供后续会话使用。你可以随时删除过去会话中保存的所有浏览器数据。为帮助保护你的隐私，Gemini 可能会代你自动删除已保存的浏览器数据，你可能需要重新登录网站。

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部，点击设置 ![](images/img-14-bbb6bc.png) ![然后](images/img-02-bfcdbc.png) **浏览器** ![](images/img-15-23186a.png)。
3. 在「删除远程浏览器数据」旁边，点击 **删除** ![](images/img-16-23ae4d.png)。

删除远程代码执行数据

当 Gemini 使用远程计算机运行代码或执行复杂任务时，它会为你方便而将数据保存在远程计算机上，供后续会话使用。你可以随时在任务设置中删除远程计算机上保存的所有数据。这将删除此前会话中保存的所有远程代码执行文件和数据。

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部，点击设置 ![](images/img-14-bbb6bc.png) ![然后](images/img-02-bfcdbc.png) **任务设置** ![](images/img-17-57eb08.png)。
3. 在「删除远程代码执行」下，点击 **删除** ![](images/img-16-23ae4d.png)。

## 关闭任务模式

**重要：** 关闭任务模式后：

- 你的远程浏览器数据和远程代码执行数据会被删除。
- 你的 Chrome 浏览数据不会被清除。[了解如何在 Chrome 中删除本地浏览器数据](https://support.google.com/chrome/answer/2392709)。
- 只要任务模式处于关闭状态，或你的设备处于关机状态，计划就不会运行。
- Gemini 更新或创建的任务、线程、计划或任何相关文件都不会被删除。

在 Gemini 网页版中

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部，点击设置 ![](images/img-14-bbb6bc.png) ![然后](images/img-02-bfcdbc.png) **任务设置** ![](images/img-17-57eb08.png)。
3. 在「使用任务模式交接工作」下，点击 **关闭**。

在 Mac 上的 Gemini 应用中

1. 在你的 Mac 上，打开 Gemini 应用 ![](images/img-04-4a5c21.png)。
2. 在屏幕顶部，点击 **Gemini** ![然后](images/img-02-bfcdbc.png) **设置** ![然后](images/img-02-bfcdbc.png) **任务** ![](images/img-17-57eb08.png)。
3. 关闭 **使用任务模式交接工作**。

**提示：**

- 关闭任务模式不会删除计划、任务、线程或 Gemini 更新或创建的文件中的任何过往活动。
- 你的计划和任务会暂停，但不会被删除。
- 你的聊天不会被删除，但你可以随时在 Gemini 应用活动记录中管理它们。

### 重新开启任务模式

1. 在电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-04-4a5c21.png)。
2. 在文本框下方，点击 **任务**。
3. 按照屏幕上的说明操作。

## Gemini 可用于处理你任务的内容

当你让 Gemini 处理任务时，它会使用来自可用来源的信息，例如下面列出的功能，以及来自它交互的网站的信息，包括你已登录的网站。

技能和计划

Gemini 可以使用：

- **技能：**带有补充上下文的可复用指令。[了解如何创建和管理技能](https://support.google.com/gemini/answer/17094296)。
- **计划：**任务的自动触发器，告诉 Gemini 何时执行你的指令。[了解如何创建和管理计划](https://support.google.com/gemini/answer/17094710)。

关联应用和其他 Google 服务

Gemini 可以为你的任务使用一些关联应用和某些 Google 服务，包括：

- 自定义应用。[了解如何连接自定义应用](https://support.google.com/gemini/answer/17209137)。
- 以下 Google 关联应用和服务：
  - 通讯录，包括 Google 通讯录和来自你已登录设备的联系人信息。
  - Gemini Notebook。
  - Google 相册。[了解 Gemini 中的 Google 相册任务](https://support.google.com/gemini/answer/18116629)。
  - Google Workspace，包括日历、文档、云端硬盘、Gmail、Keep、表格、幻灯片和 Google Tasks。[了解支持哪些操作](#workspace_actions)。
  - Google 搜索服务，包括搜索、财经、航班、酒店和地图。
  - YouTube。
- 若干第三方应用。
- 使用 Google 登录（经你确认）。

要查看哪些关联应用可用于任务，[查看关联应用列表](https://support.google.com/gemini/table/17434654)。

远程浏览器和计算机

Gemini 可以为你的任务使用带自动保存信息的远程浏览器，以及带代码执行数据的远程计算机。[了解如何删除远程浏览器和计算机数据](#delete_data)。

个人智能

Gemini 可以将个人智能用于你的任务，其中包括：

- [对你过去 Gemini 聊天的记忆](https://support.google.com/gemini/answer/16598469)
- [给 Gemini 的指令](https://support.google.com/gemini/answer/16598625)
- [可与个人智能配合使用的 Google 关联应用](https://support.google.com/gemini/answer/16598406)

Gemini 的其他功能

以下是 Gemini 可用于处理你任务的部分其他功能。

**Google 文档的 Canvas 面板：**

- 在 [gemini.google.com](https://gemini.google.com) 的 Gemini 网页版中，你可以在 Canvas 面板中编辑 Gemini 为你的任务创建的 Google 文档。[详细了解 Canvas](https://support.google.com/gemini/answer/16047321)。
- 当 Gemini 为你的任务使用 Canvas 时，Canvas 中的「创建」菜单和某些快速编辑选项不可用。

**Nano Banana：** Gemini 可以使用 Nano Banana 模型为你的任务生成和编辑图像。[详细了解 Nano Banana](https://support.google.com/gemini/answer/14286560)。

## 指派给 Gemini 的任务上限

Gemini 应用有基于计算量的用量限制，决定你可以与 Gemini 工具和功能交互多少。这些用量限制会随着更高的 Google AI 订阅而提高。你指派给 Gemini 的任务会消耗多少用量，取决于你每天指派多少任务以及每个任务有多复杂。如果你接近上限，Gemini 会告知你。[详细了解 Gemini 应用中的限制](https://support.google.com/gemini/answer/16275805)。

你在任一时刻最多可以有 15 个任务运行。你需要等待任务完成，才能发出另一个请求。此外，如果已有 15 个任务在运行，计划将不会运行。

## Gemini 如何与你协作，保障你和你的信息安全

Gemini 处理任务的能力仍是实验性的。在我们持续改进它的过程中，你的监督对于帮助防止非预期和可能有害的操作非常重要。

关于使用智能体式 AI 的可能风险

智能体式 AI（agentic AI）技术为 Gemini 的部分能力提供支持，是有用且强大的工具，但了解一些可能的风险很重要。请记住，Gemini 可能犯错，也可能做出意想不到的事情。

#### 关于提示注入

提示注入（prompt injection）是一种试图诱导 Gemini 等 AI 工具给出非预期或有害响应的行为。当网站、电子邮件、文档、.md 文件或多媒体等内容中包含恶意指令或代码，而这些内容可能对你隐藏但对 AI 智能体可见时，就会发生这种情况。

如果 AI 智能体在执行任务时读取了这些指令，它可能被误导去做非预期的事情。例如，恶意指令可能告诉智能体：

- 从你的电子邮件或文档中获取你的私人信息，并将其发布到公开网站上。
- 在你不知情的情况下，将你在 Gmail 中的电子邮件发送到外部服务。
- 根据你在关联应用中的数据，泄露关于你的洞察。
- 运行可能具有恶意或安装受损软件的命令，以通过任意代码执行实现持久的数据外泄。为帮助防范这一点，你可以在任务设置中删除远程浏览器数据，并清除代码执行历史和文件。

#### Gemini 可能与网站分享你的信息

当你把任务指派给 Gemini 时，Gemini 在使用本地或远程浏览器时，可以与网站分享来自你的聊天和其他可用来源的信息，例如你的关联应用和个人智能。这可能包括你的姓名、联系信息、文件、偏好以及你可能认为敏感的信息。这可能带来隐私风险，例如当 Gemini 使用 Google Workspace 等关联应用时，这些应用允许 Gemini 访问你的私人信息。Gemini 可以选择要访问的网站来满足你的请求。

#### Gemini 可以访问你的本地浏览状态

使用本地浏览器 Chrome 时，Gemini 可以访问与你相同的网站，包括你已登录的网站。

Gemini 如何帮助保障你的信息安全

为帮助降低与使用 AI 智能体相关的[可能风险](#agentic_risks)，Gemini 包含一些旨在支持更安全使用、降低非预期或可能有害操作发生可能性的功能。虽然这些功能不能保证防范所有风险，但包括：

- **请求用户确认：** 即使你更新了权限偏好，非常敏感的操作每次都需要你的许可。Gemini 的设计是，在完成某些操作前始终请求你审阅并确认，例如：
  - 发送通信、修改或删除你的数据、进行购买、完成金融交易，以及填写并提交网页表单。
  - 使用 Google 登录来登录网站。
- **针对敏感信息的内置安全检查：** 即使你将某项操作或浏览器权限设为「始终允许」，Gemini 也会使用内置安全检查来帮助保护你的隐私。在向网站或关联应用分享你可能认为敏感的信息（例如健康信息、财务详情或政府证件号码）之前，Gemini 会暂停并请求你的许可。
- **禁止任务识别：** Gemini 具有安全防护机制，旨在帮助它识别并拒绝执行某些可能有害或超出其预期用途的请求，包括某些可能违反[生成式 AI 禁止使用政策](https://policies.google.com/terms/generative-ai/use-policy)的任务。
- 「**接管**」模式：Gemini 可能会暂停，并请你「接管」浏览器以完成特定操作，包括输入特定类型的信息（例如密码或付款详情）。
- **规划信息：** Gemini 的设计是，在你提交提示后向你展示它计划做什么、它执行任务时的进度，以及使用或创建的任何相关技能、关联应用和文件。
- **网站和操作限制：** Gemini 会将其浏览活动限制在与你的任务相关的网站和操作上。这有助于保护你在其他无关网站上的数据，并帮助防止与你的任务不符的操作。这些只是我们防范提示注入的部分方式。

为什么你的监督很重要，以及如何让 Gemini 停止

上述 Gemini 的安全防护并不保证能防范所有风险。

#### 监督重要和敏感的任务

当你把任务指派给 Gemini 时，你的主动监督是防范风险最重要的方式。请仔细查看确认请求和澄清问题。谨慎、安全地把任务指派给 Gemini，只交给它你愿意交办的任务。当 Gemini 出现以下情况时，请格外留意：

- 处理重要任务
- 登录了具有敏感访问权限或包含你认为敏感信息的网站
- 做任何出错就可能造成问题的事情
- 使用关联应用，例如 Google Workspace
- 需要分享你认为敏感的数据。

#### 由你掌控

- **停止或接管任务：** 如果 Gemini 正在做你不喜欢的事情，你可以通过在聊天中选择停止响应 ![](images/img-18-34a5d7.png)，或**接管** ![](images/img-13-f3ad3c.png) Gemini 的浏览器来让它停止。
- **拒绝或不允许某项操作：** 如果你在任务线程中拒绝某项操作，Gemini 会停止，并且不会尝试其他方式来完成它。
- **删除已保存的浏览器数据：** Gemini 的安全防护并不旨在替代你的主动监督。你还可以在敏感会话结束后删除本地或远程浏览器数据以及远程计算机数据，来帮助保障你的信息安全。

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

Spark 去哪了？我找不到它。

自 5 月以来，我们一直在与订阅用户一起测试 Spark 的 beta 版。随着人们使用它，他们真的很希望 Gemini 能直接帮他们完成「任务」（tasks）。这个词不断出现，所以我们将其更名为 Task，以便更容易理解。你可以在提示文本框旁的「聊天」和「任务」切换开关中找到它。你现有的任务和计划仍然存在，可以在侧边栏中找到它们。

Gemini 可以为任务执行哪些 Workspace 操作？

**重要：**

- 要让 Gemini 连接你在 Google Workspace 服务中的数据，Google Workspace 需要连接到 Gemini 应用。[了解如何在 Gemini 中使用和管理关联应用](https://support.google.com/gemini/answer/13695044)。
- 要撤销 Gemini 的操作，请点击 Gemini 确认信息中的链接，并在 Workspace 服务中进行更改。

Gemini 可以在 Workspace 中为你的任务执行以下操作：

#### 日历

- **管理你的日程：**查看你的日历、回复邀请，以及安排新活动。
- **重新安排和清理：**更新会议时间、更改地点或取消活动。
- **智能安排：**查看你的日历，并建议适合所有人空闲时间的可用时段。

#### Gmail

- **搜索和汇总邮件：**在你的电子邮件线程中搜索特定主题，或汇总对话。
- **起草和回复：**撰写电子邮件草稿、转发电子邮件，或回复现有电子邮件线程。
- **使用标签：**用标签整理你的收件箱。

#### 文档、表格、幻灯片和云端硬盘

**重要：** 要编辑共享的文档、电子表格和演示文稿，你需要审阅并确认 Gemini 计划的编辑。

- **搜索和管理你的 Google 云端硬盘文件：**搜索文件、读取文件内容、重命名或删除文件、检查元数据，以及查看最近的文档。
- **撰写和编辑文档：**在 Google 文档中创建文档或编辑现有文档——添加摘要、备注，或编辑特定章节。
- **读取评论：**读取 Google 文档、电子表格和演示文稿中的评论。
- **创建和编辑电子表格：**在 Google 表格中构建、格式化和编辑带数据、表格和公式的自定义电子表格。
- **生成和编辑演示文稿：**根据提示在 Google 幻灯片中创建演示文稿，并在演示文稿中编辑、添加和删除幻灯片。
- **向文档和演示文稿添加图像：**向你的提示中添加图像，并让 Gemini 将其添加到文档或演示文稿中。
- **添加 Google 表格图表：**将电子表格中的图表添加到文档和演示文稿中。

#### Google Keep

- **查找笔记和列表：**在 Google Keep 中搜索并获取笔记和列表。
- **创建笔记和列表：**在 Google Keep 中创建私密列表和笔记。

#### Google Tasks

**重要：** Gemini 可以在未经你确认的情况下对 Google Tasks 中的私密任务执行批量操作。请在提交前审阅你的请求，或直接在 Google Tasks 中管理。

- **查找提醒和任务：**从 Google Tasks 中搜索并获取提醒和任务。
- **管理提醒和任务：**在 Google Tasks 中添加、更新和删除提醒和任务。

## 相关资源

- [在 Gemini 应用中查找和管理你的任务](https://support.google.com/gemini/answer/17094196)
- [为 Gemini 应用创建和管理技能](https://support.google.com/gemini/answer/17094296)
- [在 Gemini 中为任务创建和管理计划](https://support.google.com/gemini/answer/17094710)
