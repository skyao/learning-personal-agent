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
collectedAt: 2026-11-28
updatedAt: 2026-11-28
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）。2026-10 Spark 改名为 Task 后，帮助页的用词已改为 tasks / task mode；2026-11-10 发现原文更新：「What you need」删去了「选择加入 Personal Intelligence」一条，原文存档与译文同步删除，其余未变；2026-11-28 发现原文更新：不再要求 Google AI Pro 或 Ultra 订阅，地区改为免费六国与其他地区的订阅用户两层；新增邮件创建任务的提示、用 Google Password Manager 登录、可用服务加入 Google Pay 与 Google Wallet；需要确认的动作中「修改数据」改为「分享敏感信息」；远程计算机数据的删除步骤改为链接到单独的帮助页；「Keep Activity」改称「History」；删去「取消或降级订阅」一节。原文存档已覆盖，旧译文删除，已重新翻译"
tags: [持续执行, 运行环境, 安全, 开放与价格]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的默认（Computer）视图；页面中的界面小图标已下载。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：使用任务须年满 18 岁、个人 Google 账号、开启 History，不再要求订阅：无订阅可用于澳大利亚、加拿大、印度、日本、韩国、美国，其他地区（欧洲经济区、尼日利亚、瑞士、英国除外）需要 Google AI Pro 或 Ultra。Gemini 可以在本地或远程浏览器中操作，用户可随时接管；遇到登录页时会请求确认使用「Sign in with Google」或 Google Password Manager 中的凭据，否则请用户接管；也可以通过邮件创建任务。最多同时运行 15 个任务。需要逐次确认的动作包括发送消息、删除数据、分享敏感信息、购物、金融交易、提交网页表单，以及用 Sign in with Google 或 Password Manager 登录；可用服务中新增 Google Pay 与 Google Wallet。

**保留理由**：Task 功能最完整的官方说明，包括准入条件、本地与远程浏览器、并发上限和确认机制。

---

现在可以在发起对话的同一处启动任务。为 Gemini 分配任务，可以自动执行复杂的工作流，并管理持续性任务的时间表。Gemini 可以借助已连接应用（Connected Apps）、技能（skills）、对话、你已登录的网站、Personal Intelligence、位置等来源的信息来帮助处理任务。你只需告诉 Gemini 具体目标，以及希望任务在什么时候完成。

例如，你可以创建任务让 Gemini 帮助：

- **节省时间：** Gemini 可以通过汇总或归档简报来整理收件箱、在你休假后生成一份紧急待办清单，以及退订邮件列表。
- **节省开支：** Gemini 可以监控航班和酒店价格，在价格降到你的预算内时提醒你。
- **深入研究主题并创建文件：** Gemini 可以检索带引用来源的研究资料，并把结果打包成可下载的文件，如 PDF、文档、电子表格和演示文稿。

**提示：** 任务中的时间表与对话中的时间表不同。[了解对话中的时间表如何工作](https://support.google.com/gemini/answer/16316416)。

## 你需要什么

要为 Gemini 分配任务，你必须：

- **年满 18 岁**。
- **使用个人 Google 账号登录 Gemini 应用。** 目前，如果你使用工作或学校 Google 账号登录，此功能不可用。[了解如何登录 Gemini 应用](https://support.google.com/gemini/answer/13278668)。
- **开启 [History](https://myactivity.google.com/product/gemini)**。

**重要：** 目前，Gemini 中的任务：

- 在澳大利亚、加拿大、印度、日本、韩国和美国，无需 Google AI 订阅即可使用。
- 在 Gemini 应用支持的其他所有地区，需要 Google AI Pro 或 Ultra 订阅，欧洲经济区、尼日利亚、瑞士和英国除外。
- 仅在 Gemini 移动应用、Mac 上的 Gemini 应用，以及 [gemini.google.com](https://gemini.google.com) 的 Gemini 网页应用中可用。

## 为 Gemini 分配任务之前

注意直接在任务线程中输入信息

不要直接在任务线程中输入登录信息、支付详情或你认为敏感的信息。如有需要，接管 Gemini 的浏览器或本地浏览器，然后直接在网页上输入相关信息。

避免安排你认为敏感的任务

Gemini 仍在学习，可能会出错。为帮助保护你的信息安全并防止意外操作，请避免安排使用你认为敏感的信息、或执行你认为敏感的操作的任务或时间表。这些任务可能需要你的监督和输入。

如果时间表在你离线时运行，你可能无法阻止 Gemini 完成意外的操作。某些任务可能需要你确认后 Gemini 才会完成。[详细了解任务与时间表](https://support.google.com/gemini/answer/17094710)。

Gemini 中的任务如何使用浏览器

你可以让 Gemini 完成涉及与网站交互的任务，例如购物、预订旅行或预订晚餐。为处理你的任务，Gemini 会使用来自已连接应用、技能、对话、任务、你已登录的网站、Personal Intelligence、位置[等来源](https://support.google.com/gemini?p=lm_agent_sources)的信息。

为与网站交互，Gemini 可以连接你桌面上的本地 Chrome 浏览器，或使用云端单独的远程浏览器。目前，Chrome 自动浏览仅在桌面端可用。

**如果你使用本地浏览器：** Gemini 可以访问与你相同的所有网站，包括你已登录的网站。在代表你操作时，Gemini 会与第三方分享必要的信息。这可能包括你的姓名、联系信息、文件、偏好以及你认为敏感的信息。经你许可，它还可以使用你保存在 Password Manager（密码管理工具）中的登录信息，登录会员计划和在线账户。

要让 Gemini 使用你的本地浏览器处理任务，你需要保持设备和 Google Chrome 唤醒并运行。如果你在任务完成前关闭或关掉设备，或设备不可用，Gemini 可能会改用远程浏览器完成任务。

**如果你使用远程浏览器：** 即使你关闭设备，Gemini 也会继续处理你的任务，且仅在移动设备上使用远程浏览器。对于某些步骤，例如登录网站，任务会暂停，直到你接管并完成该步骤。

**注意：**

- Gemini 首次需要在某台设备上为你浏览网页时，Chrome 会请你允许将 Chrome 自动浏览连接到 Gemini。
- 此后，对于每个涉及网页浏览的任务，Gemini 都会先请求确认。
- 你可以在某台设备上关闭 Gemini 的自动浏览能力。点击「更多」![](images/img-01-53995d.png) ![然后](images/img-02-bfcdbc.png) **设置** ![然后](images/img-02-bfcdbc.png) **AI 创新** ![然后](images/img-02-bfcdbc.png) **Chrome 中的 Gemini**。

#### 跟踪任务

你可以打开任务线程，查看 Gemini 是否为该任务使用浏览器。任何时候你都可以阻止 Gemini 浏览网页。在 Chrome 中的 Gemini 侧边面板中，点击「停止」![](images/img-03-440b63.png)。这样做之后，Gemini 会尝试找出继续任务的下一步，这可能涉及使用远程浏览器浏览网页，或启用其他工具；也可能意味着 Gemini 放弃该任务。

如果你想自己完全取消任务，在 Gemini 文本框中点击「停止」![](images/img-03-440b63.png)。

## 开始使用 Gemini 中的任务

你可以通过对话方式获得设置首个技能和任务方面的帮助。只需在任务中输入 "set up"、"get started" 或 "interview me"。

（译注：三句提示语分别为「帮我设置」「开始吧」「采访我」之意。）

[了解 Gemini 可以为你的任务使用什么](#sources)。

## 创建任务

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-04-4a5c21.png)。
2. 在文本框下方点击 **任务**。
3. 在文本框中描述你希望 Gemini 管理的任务。
   - 你可以告诉 Gemini 何时运行任务，例如某个具体时间前后，或某个事件之后。[详细了解时间表](https://support.google.com/gemini/answer/17094710)。
   - 要指定使用某个已有技能，输入 `@`，然后选择该技能。[详细了解技能](https://support.google.com/gemini/answer/17094296)。
   - 你可以让 Gemini 生成文件，如 PDF、文档和演示文稿。[了解 Gemini 可以创建的文件](#created_files)。
   - 在某些 Gemini 应用中，你还可以让 Gemini 使用自定义已连接应用。[了解如何连接自定义应用](https://support.google.com/gemini/answer/17209137)。
   - 要更改 Gemini 模型或思考级别，点击顶部的模型菜单。[了解模型与思考级别](https://support.google.com/gemini/answer/18648722)。
4. 要向任务添加文件，点击「上传与工具」![](images/img-05-72d6a4.png)，然后选择以下选项之一：
   - **上传文件** ![](images/img-06-0940a6.png)
   - **从 Drive 添加** ![](images/img-07-196795.png)
   - **添加 Notebook** ![Notebook](images/img-08-cd71d2.png)
5. 点击「提交」![](images/img-09-c4d89f.png)。
6. 要在任务运行期间改变 Gemini 的做法，只需在文本框中输入补充指令。
   - Gemini 会更新其工作，不会丢失已有进度。
   - 如果 Gemini 此前为你的任务使用了某项功能或已连接应用，可能需要几秒钟才能完全停止。
7. 定期查看任务，看 Gemini 是否需要你提供输入。例如，如果 Gemini 需要你在其浏览器中执行某些操作，它会请你接管任务。

**提示：** 在 Mac 上的 Gemini 应用中，如果已设置任务，你可以从另一台设备让 Gemini 在你的 Mac 上执行操作。[了解如何远程控制 Mac 上的 Gemini 应用](https://support.google.com/gemini/answer/17208717#remote_control)。

**提示：** 你还可以设置「邮件与 Gemini」，从收件箱创建任务。[了解如何设置邮件与 Gemini](https://support.google.com/gemini/answer/18745518)。

### 示例任务

- 整理收件箱：汇总或归档简报，并退订邮件列表。
- 获得定制新闻摘要：深入研究你关心的报道，并跟踪其发展。

## 查看与管理任务

要查看和管理任务，包括相关权限和时间表，请打开任务线程及其工作面板。

打开任务线程并查看任务进度

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-04-4a5c21.png)。
2. 在侧边栏中点击要查看或管理的任务的线程。
3. 要给 Gemini 更多指令或修改指令，在任务线程中告诉 Gemini。
4. 要显示该任务线程的工作面板，在线程顶部点击进度标签。这里可以找到线程中任务的步骤和进度。

   |  |  |
   | --- | --- |
   |  | 已完成的步骤  当前步骤  计划中的步骤 |

查看 Gemini 读取或更新的文件

在任务线程的工作面板的「文件」下，你可以查看 Gemini 为线程中的任务读取或更新的文件。点击文件即可打开。

暂停和恢复线程中的时间表

1. 在任务线程中，点击已安排任务的标签。
2. 在顶部点击「更多选项」![](images/img-01-53995d.png) ![然后](images/img-02-bfcdbc.png) **暂停** ![](images/img-10-ba979f.png) 或 **恢复** ![](images/img-11-1de8b2.png)。

**提示：** 在 Gemini 网页应用中，你也可以在「已安排」页面暂停和恢复时间表。[了解如何管理你的时间表](https://support.google.com/gemini/answer/17094710)。

查看、编辑或下载 Gemini 创建的文件

当 Gemini 作为任务的一部分创建文件时，你可以直接在任务线程中访问它们。

- 对于 Markdown 和纯文本文件，Gemini 会在 Canvas 中显示文件，你可以直接编辑。
- 对于其他文件，Gemini 会给出文件链接，你可以打开并通过对话方式编辑。

#### 从 Canvas 导出文件

1. 在任务线程中，找到包含该文件的 Canvas 编辑器。
2. 在顶部点击 **导出** ![然后](images/img-02-bfcdbc.png) **.txt**、**.md** 或 **Drive**。

#### 打开并下载链接文件

1. 在任务线程中找到该文件。
2. 在文件旁点击 **打开**。
3. 要下载文件，在顶部点击「下载」![](images/img-12-cd655c.png)。

#### 编辑生成的文件

在任务线程中：

- 告诉 Gemini 你想更新生成文件中的哪些内容。
- 对于某些文件类型，可以直接在任务线程中编辑。

#### Gemini 可以创建的文件

Gemini 可以在任务中生成以下文件格式：

- **文本与标记语言：** .json、.md、.tex、.txt
- **文档：** .pdf、.docx
- **电子表格与表格数据：** .csv、.tsv、.xlsx
- **演示文稿：** .pptx
- **代码：** .py、.js、.ts、.cpp、.cc、.c、.h、.java、.go、.rs、.cs、.php、.rb、.swift、.kt、.dart、.sql、.sv、.sh
- **网页与 UI：** .html、.jsx、.tsx（React）、Angular
- **图像与图形：** .png、.jpg 或 .jpeg、.svg
- **音频与视频：** .mp3、.mp4、
- **归档与压缩文件：** .tar、.tar.gz、.gz、.zip

**提示：** Gemini 也可以创建 Google 文档、演示文稿和电子表格。[详细了解 Google Workspace 相关操作](#workspace_actions)。

## 监控与接管任务

Gemini 可以在本地或远程浏览器中完成你的部分任务。例如，它可以导航到某个网站并与页面交互，如将商品加入购物车。你可以随时接管浏览器。对于某些操作，Gemini 会请你接管任务。

登录网站

当 Gemini 遇到登录页面时，它会请你确认使用「使用 Google 账号登录」（若可用），或使用保存在 Google Password Manager（密码管理工具）中的凭据。如果你不确认，它会请你接管并手动登录。

接管远程浏览器任务

1. 在任务线程中，在「Gemini 正在使用 Chrome」旁点击 **查看实时画面**。这会在远程计算机上打开 Gemini 的浏览器。
2. 将鼠标悬停在 Gemini 的浏览器上。
3. 点击 **接管任务** ![](images/img-13-f3ad3c.png) ![然后](images/img-02-bfcdbc.png) **接管任务**。
4. 完成你的操作步骤。
5. 要将控制权交还 Gemini，在顶部点击 **返回 Gemini**。

接管本地浏览器任务

[了解如何管理通过 Chrome 自动浏览完成的任务](https://support.google.com/gemini/answer/16821166)。

## 删除远程浏览器与计算机数据

删除本地浏览器数据

你可以随时删除设备上 Chrome 浏览器中的数据。[了解如何在 Chrome 中删除本地浏览器数据](https://support.google.com/chrome/answer/2392709)。

删除远程浏览器数据

当 Gemini 使用远程浏览器完成任务时，浏览器数据（例如包含你网站身份验证信息（登录详情）的 Cookie）会为你保存下来，供以后的会话使用。你可以随时删除过去会话中保存的所有浏览器数据。Gemini 会自动在一段设定的不活动时间后代你删除保存的浏览器数据，或一直保留到你手动删除；你可能需要重新登录网站。

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-14-bbb6bc.png) ![然后](images/img-02-bfcdbc.png) **浏览器** ![](images/img-15-23186a.png)。
3. 在「删除远程浏览器数据」旁点击 **删除** ![](images/img-16-23ae4d.png)。

删除远程代码执行数据

当 Gemini 在远程计算机上运行代码或执行复杂任务时，它会保存数据供以后的会话使用，你可以随时在任务设置中删除这些数据。[了解如何删除远程代码执行数据](https://support.google.com/gemini/answer/18789153#delete_code_data)。

## 关闭任务模式

**重要：** 关闭任务模式时：

- 你的远程浏览器数据和远程代码执行数据会被删除。
- 你的 Chrome 浏览数据不会被清除。[了解如何在 Chrome 中删除本地浏览器数据](https://support.google.com/chrome/answer/2392709)。
- 只要任务模式处于关闭状态，或你的设备关机，时间表就不会运行。
- Gemini 更新或创建的任务、线程、时间表或任何相关文件不会被删除。

在 Gemini 网页应用中

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-14-bbb6bc.png) ![然后](images/img-02-bfcdbc.png) **任务设置** ![](images/img-17-57eb08.png)。
3. 在「使用任务模式交办工作」下点击 **关闭**。

在 Mac 上的 Gemini 应用中

1. 在 Mac 上打开 Gemini 应用 ![](images/img-04-4a5c21.png)。
2. 在屏幕顶部点击 **Gemini** ![然后](images/img-02-bfcdbc.png) **设置** ![然后](images/img-02-bfcdbc.png) **任务** ![](images/img-17-57eb08.png)。
3. 关闭 **使用任务模式交办工作**。

**提示：**

- 关闭任务模式不会删除时间表、任务、线程，也不会删除 Gemini 更新或创建的文件的历史记录。
- 你的时间表与任务会被暂停，而不会被删除。
- 你的对话不会被删除，你可以随时在 Gemini 历史记录中管理它们。

### 重新开启任务模式

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-04-4a5c21.png)。
2. 在文本框下方点击 **任务**。
3. 按屏幕上的说明操作。

## Gemini 可以为你的任务使用什么

当你让 Gemini 处理任务时，它会使用来自可用来源（如下列功能）的信息，以及来自它所交互的网站的信息，包括你已登录的网站。

技能与时间表

Gemini 可以使用：

- **技能：** 带有额外上下文、可重复使用的指令。[了解如何创建和管理技能](https://support.google.com/gemini/answer/17094296)。
- **时间表：** 任务的自动触发器，告诉 Gemini 何时执行你的指令。[了解如何创建和管理时间表](https://support.google.com/gemini/answer/17094710)。

已连接应用与其他 Google 服务

Gemini 可以为你的任务使用部分已连接应用和某些 Google 服务，包括：

- 自定义应用。[了解如何连接自定义应用](https://support.google.com/gemini/answer/17209137)。
- 这些 Google 已连接应用和服务：
  - 联系人，包括 Google 通讯录和来自你已登录设备的联系信息。
  - Gemini Notebook。
  - Google Pay 和 Google Wallet。
  - Google 相册。[了解 Gemini 中的 Google 相册任务](https://support.google.com/gemini/answer/18116629)。
  - Google Workspace，包括日历、文档、云端硬盘、Gmail、Keep、表格、幻灯片和 Tasks。[了解支持哪些操作](#workspace_actions)。
  - Google 搜索服务，包括搜索、财经、航班、酒店和地图。
  - YouTube。
- 若干第三方应用。
- 使用 Google 账号登录或 Google Password Manager，需经你确认。

要查看哪些已连接应用可用于任务，[查看已连接应用列表](https://support.google.com/gemini/table/17434654)。

远程浏览器与计算机

Gemini 可以为你的任务使用带有自动保存信息的远程浏览器，以及带有代码执行数据的远程计算机。[了解如何删除远程浏览器与计算机数据](#delete_data)。

Personal Intelligence

Gemini 可以为你的任务使用 Personal Intelligence，其中包括：

- [对你过去 Gemini 对话的记忆](https://support.google.com/gemini/answer/16598469)
- [给 Gemini 的指令](https://support.google.com/gemini/answer/16598625)
- [与 Personal Intelligence 配合使用的 Google 已连接应用](https://support.google.com/gemini/answer/16598406)

Gemini 的其他功能

以下是 Gemini 可以用来处理你的任务的其他一些功能。

**用于 Google 文档的 Canvas 面板：**

- 在 [gemini.google.com](https://gemini.google.com) 的 Gemini 网页应用中，你可以在 Canvas 面板中编辑 Gemini 为你的任务创建的 Google 文档。[详细了解 Canvas](https://support.google.com/gemini/answer/16047321)。
- 当 Gemini 为你的任务使用 Canvas 时，Canvas 中的「创建」菜单和某些快速编辑选项不可用。

**Nano Banana：** Gemini 可以使用 Nano Banana 模型为你的任务生成和编辑图像。[详细了解 Nano Banana](https://support.google.com/gemini/answer/14286560)。

## 你分配给 Gemini 的任务的限制

Gemini 应用有基于算力的用量限制，决定你可以与 Gemini 工具和功能交互的程度。Google AI 订阅档位越高，这些用量限制越高。你分配给 Gemini 的任务会消耗多少用量，取决于你每天分配多少任务，以及每个任务有多复杂。如果你接近上限，Gemini 会告诉你。[详细了解 Gemini 应用的限制](https://support.google.com/gemini/answer/16275805)。

同一时间最多可以有 15 个任务在运行。你需要等待任务完成，才能再提出请求。另外，如果已经有 15 个任务在运行，时间表就不会运行。

## Gemini 如何与你协作保护你和你的信息安全

Gemini 处理任务的能力仍处于实验阶段。在我们持续改进它的过程中，你的监督很重要，有助于防止意外和可能有害的操作。

关于使用智能体式 AI 的可能风险

为 Gemini 部分能力提供支持的智能体式 AI（agentic AI）技术是有用而强大的工具，但了解一些可能的风险很重要。请记住，Gemini 可能出错，也可能做出意料之外的事。

#### 关于提示注入

提示注入（prompt injection）是试图让 Gemini 等 AI 工具作出非预期或有害回应的一种手段。当网站、邮件、文档、.md 文件或多媒体等内容中包含恶意指令或代码，且这些内容可能对你隐藏、但对 AI 智能体可见时，就会发生这种情况。

如果 AI 智能体在执行任务时读到这些指令，可能会被误导去做非预期的事。例如，恶意指令可能告诉智能体：

- 从你的邮件或文档中取出你的私人信息，并发布到公开网站上。
- 在你不知情的情况下，把你在 Gmail 中的邮件发送到外部服务。
- 根据你已连接应用中的数据，泄露关于你的洞察。
- 运行可能具有恶意或会安装被篡改软件的指令，通过任意代码执行实现持久的数据外泄。为帮助防范这一点，你可以删除远程浏览器数据，并在任务设置中清除代码执行历史和文件。

#### Gemini 可能与网站分享你的信息

当你给 Gemini 分配任务时，Gemini 在使用本地或远程浏览器期间，可能会把你的对话以及来自其他可用来源（如已连接应用和 Personal Intelligence）的信息分享给网站。这可能包括你的姓名、联系信息、文件、偏好以及你认为敏感的信息。这会带来隐私风险，例如当 Gemini 使用 Google Workspace 这类允许 Gemini 访问你私人信息的已连接应用时。Gemini 可以选择访问哪些网站来满足你的请求。

#### Gemini 可以访问你本地的浏览状态

使用本地浏览器 Chrome 时，Gemini 可以访问与你相同的网站，包括你已登录的网站。

Gemini 如何帮助你保护信息安全

为帮助降低使用 AI 智能体带来的[相关可能风险](#agentic_risks)，Gemini 内置了一些旨在支持更安全使用、减少非预期或可能有害操作发生可能性的功能。虽然这些功能不能保证防范所有风险，但包括：

- **请求用户确认的提示：** 即使你更新了权限偏好，非常敏感的操作每次都需要你的许可。Gemini 被设计为在完成某些操作前始终请你审阅并确认，例如：
  - 发送通信、删除你的数据、分享敏感信息、购物、完成金融交易，以及填写并提交网页表单。
  - 使用 Google 账号登录或 Google Password Manager 登录网站。
- **针对敏感信息的内置安全检查：** 即使你把某项操作或浏览器权限设为「始终允许」，Gemini 也会使用内置安全检查来帮助保护你的隐私。在向网站或已连接应用分享你可能认为敏感的信息（如健康信息、财务详情或政府证件号码）之前，Gemini 会暂停并请求你的许可。
- **禁止任务识别：** Gemini 有旨在帮助它识别并拒绝执行某些可能有害或超出其预期用途的请求的防护措施，包括某些可能违反[生成式 AI 禁止使用政策](https://policies.google.com/terms/generative-ai/use-policy)的任务。
- **「接管控制」模式：** Gemini 可能会暂停并请你「接管控制」浏览器，以完成特定操作，包括输入特定类型的信息（如密码或支付详情）。
- **计划信息：** Gemini 被设计为在你提交提示后展示它计划做什么、处理任务时的进度，以及所用或所创建的相关技能、已连接应用和文件。
- **网站与操作限制：** Gemini 会把浏览活动限制在与你的任务相关的网站和操作上。这有助于保护你在其他无关网站上的数据，并帮助防止不符合你任务的操作。这些只是我们防范提示注入的部分方式。

为什么你的监督很重要，以及如何停止 Gemini

上述 Gemini 的防护措施不能保证防范所有风险。

#### 监督重要和敏感的任务

当你给 Gemini 分配任务时，你主动的监督是防范风险最重要的方式。请仔细审阅确认请求和澄清问题。谨慎、安全地给 Gemini 分配任务，只交给它你放心的任务。当 Gemini 出现以下情况时，请格外留意：

- 处理重要任务
- 登录了具有敏感访问权限或含你认为敏感信息的网站
- 做任何一旦出错就可能成为问题的事
- 使用已连接应用，如 Google Workspace
- 需要分享你认为敏感的数据。

#### 控制权在你手中

- **停止或接管任务：** 如果 Gemini 正在做你不喜欢的事，你可以在对话中选择「停止回应」![](images/img-18-34a5d7.png) 来停止它，或**接管控制**（![](images/img-13-f3ad3c.png)）Gemini 的浏览器。
- **拒绝或不允许某项操作：** 如果你在任务线程中拒绝某项操作，Gemini 会停止，不会尝试用其他方式完成它。
- **删除已保存的浏览器数据：** Gemini 的防护措施并不旨在取代你的主动监督。你还可以在敏感会话之后删除本地或远程浏览器数据以及远程计算机数据，帮助保护你的信息安全。

## 常见问题

任务、时间表和技能有什么区别？

为帮助你充分利用任务，了解支撑其逻辑的三个构件会很有帮助：任务、时间表（schedules）和技能（skills）。可以把它们理解为「做什么」「什么时候做」和「怎么做」。

**任务是你的高层目标。** 它代表你希望 Gemini 为你管理的一个完整项目或目标。

- **示例：**「规划并管理我去伦敦的出差。」

**时间表让你把任务交给** Gemini，使其在后台自动运行。你告诉 Gemini 做什么、什么时候做。任务可以安排为在某个具体日期和时间运行，或响应某个事件运行。

- **示例：**「每天上午 8 点（条件），给我一份 AI 新闻更新（任务）」
- **示例：**「当我的航班延误时（条件），通知我并提出行程调整建议（任务）。」

**提示：** 任务的时间表与 Gemini 对话中的定时操作不同。[了解如何在 Gemini 应用中安排定时操作](https://support.google.com/gemini/answer/16316416)。

**技能是一组可重复使用的指令和额外上下文。** 它教 Gemini 如何完成某个特定任务，以及使用哪些工具。你可以指定 Gemini 为某个任务或时间表的操作使用哪个技能。Gemini 也可以在技能与任务相关时自动使用它。

- **示例：** 同时使用「旅行预订」技能和「Gmail 写作」技能，重新预订房间并发送确认。

总之，你定义任务（你想要什么），设置时间表（什么时候做），并提供技能（怎么做），以完成工作。

Spark 去哪了？我找不到它。

从 5 月起，我们一直在面向订阅用户测试 Spark 的测试版。随着人们使用它，他们非常希望 Gemini 直接帮他们完成「任务」（tasks）。这个词不断出现，所以我们把它改名为 Task，以便更容易理解。你可以在提示文本框旁的「对话」与「任务」切换开关中找到它。你已有的任务和时间表仍然存在，可以在侧边栏中找到。

Gemini 可以为任务执行哪些 Workspace 操作？

**重要：**

- 要让 Gemini 连接你在 Google Workspace 服务中的数据，Google Workspace 需要连接到 Gemini 应用。[了解如何在 Gemini 中使用和管理已连接应用](https://support.google.com/gemini/answer/13695044)。
- 要撤销 Gemini 的操作，请点击 Gemini 确认信息中的链接，并在相应的 Workspace 服务中做出更改。

Gemini 可以在 Workspace 中为你的任务执行以下操作：

#### 日历

- **管理你的日程：** 查看日历、回复邀请，以及安排新活动。
- **改期与清理：** 更新会议时间、更改地点或取消活动。
- **智能排程：** 查看你的日历，并提出适合所有人空闲时间的空档建议。

#### Gmail

- **搜索与汇总邮件：** 在你的邮件线程中搜索，找到特定主题或汇总对话。
- **起草与回复：** 撰写邮件草稿、转发邮件，或回复已有的邮件线程。
- **使用标签：** 用标签整理收件箱。

#### 文档、表格、幻灯片与云端硬盘

**重要：** 要编辑共享的文档、电子表格和演示文稿，你需要审阅并确认 Gemini 计划的编辑。

- **搜索和管理你的 Google 云端硬盘文件：** 搜索文件、读取文件内容、重命名或删除文件、查看元数据，以及查看最近的文档。
- **撰写和编辑文档：** 在 Google 文档中创建文档或编辑已有文档——添加摘要、注释，或编辑特定章节。
- **读取评论：** 读取 Google 文档、电子表格和演示文稿中的评论。
- **创建和编辑电子表格：** 在 Google 表格中用数据、表格和公式构建、格式化并编辑自定义电子表格。
- **生成和编辑演示文稿：** 根据提示在 Google 幻灯片中创建演示文稿，并编辑、添加和删除演示文稿中的幻灯片。
- **向文档和演示文稿添加图片：** 把图片添加到你的提示中，让 Gemini 将其加入文档或演示文稿。
- **添加 Google 表格图表：** 把电子表格中的图表添加到文档和演示文稿中。

#### Google Keep

- **查找笔记和清单：** 在 Google Keep 中搜索并获取笔记和清单。
- **创建笔记和清单：** 在 Google Keep 中创建私密清单和笔记。

#### Google Tasks

**重要：** Gemini 可以在无需你确认的情况下对 Google Tasks 中的私密任务执行批量操作。请在提交前审阅你的请求，或直接在 Google Tasks 中管理。

- **查找提醒和任务：** 从 Google Tasks 中搜索并获取提醒和任务。
- **管理提醒和任务：** 在 Google Tasks 中添加、更新和删除提醒与任务。

## 相关资源

- [查找和管理 Gemini 应用中的任务](https://support.google.com/gemini/answer/17094196)
- [为 Gemini 应用创建和管理技能](https://support.google.com/gemini/answer/17094296)
- [为 Gemini 中的任务创建和管理时间表](https://support.google.com/gemini/answer/17094710)
