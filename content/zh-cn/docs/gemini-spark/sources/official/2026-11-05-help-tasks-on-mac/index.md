---
title: "在 Mac 上的 Gemini 应用中分配任务"
linkTitle: "帮助：Mac 上的任务"
date: 2026-11-05
originalTitle: "Assign tasks in the Gemini app on Mac"
sourceUrl: "https://support.google.com/gemini/answer/17208717?hl=en"
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）。2026-10 Spark 改名为 Task 后，帮助页的用词已改为 tasks / task mode"
tags: [设备, 运行环境, 安全]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的默认（Computer）视图；页面中的界面小图标已下载。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：在 Mac 上，Gemini 可以把桌面上的文件夹当作工作对象：经授权后能查看和编辑下载、桌面、文稿、照片等大多数文件夹，进行分析、编辑、重命名、整理，或找到文件后发邮件。处理本地文件时会创建临时备份，用户可在开始下一个任务前恢复，开始新的请求或任务后备份即被删除。页面还说明了远程控制：用同一账号从手机等设备给 Mac 上的 Gemini 派任务、用语音或文字下指令、查看历史对话、控制媒体播放。

**保留理由**：说明了本地执行路线（Mac 文件权限、临时备份、远程派任务），与云端任务互为补充。

---

你可以把 Gemini 当作伙伴，直接在 Mac 桌面上管理和修改文件。Gemini 可以在你的 Mac 和连接应用（Connected Apps）之间执行多步骤任务。Gemini 只能查看你专门添加到「已连接的文件夹」（Connected folders）工具栏中的文件或目录。[进一步了解 Gemini 中的任务](https://support.google.com/gemini/answer/17094507)。

**重要提示：** 你可以在[支持任务的地方](https://support.google.com/gemini/answer/17094507#reqs)向 Mac 上的 Gemini 应用分配任务。

## 你可以做什么

在 Mac 上，你可以让 Gemini 做各种任务，例如：

- **添加 Mac 文件夹**：从桌面添加文件夹，供 Gemini 分析、编辑、重命名或重新整理。
- **修改文件**：例如打开一个 Google 文档，把审核日期改为今天，然后保存到桌面。
- **找到文件并通过电子邮件发送**：从桌面找到文件，发给你联系人中的某个人。
- 执行[其他任务](https://support.google.com/gemini/answer/17094507)。

当 Gemini 处理你的电脑文件时，它会创建临时备份文件。你可以选择在进入下一个任务前恢复这些备份文件。备份文件会在你开始新的查询或任务时删除，或在 24 小时后删除。

### Gemini 可以访问什么

如果你授予权限，Gemini 可以查看和编辑 Mac 上的大多数文件夹，包括下载、桌面上的文件、文稿和照片。

## 在 Mac 上向 Gemini 分配任务

1. 在 Mac 上打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在文本框下方，点击 **Task**。
3. （可选）要添加供 Gemini 查看的文件或文件夹，请在 **已连接的文件夹** 下点击「添加 Mac 文件夹」![](images/img-02-72d6a4.png)。
   - 你可能需要先授予权限。
   - 如果你误加了项目，请在该项目旁点击「断开连接」![](images/img-03-b97d78.png)。
4. 在文本框中输入提示词，然后点击「发送」![](images/img-04-c4d89f.png)。

### 向 Gemini 分配任务时要小心

- Gemini 仍在学习，可能会犯错。为帮助保护你的信息安全并防止意外操作，请避免那些会使用你视为敏感的信息、或执行你视为敏感的操作的任务与计划。这些任务可能需要你的监督和输入。
- Gemini 会在你的「已连接的文件夹」中完成对电脑文件的操作，也会处理你的个人智能（Personal Intelligence）连接应用中的信息。如果被要求，它默认会修改这些文件。
- 不要加入任何你不想让 Gemini 处理、或一旦丢失就太过敏感的文件。一旦 Gemini 完成对文件的任务或接到删除指令，你可能无法恢复这些文件。
- Gemini 可以用来永久删除文件（Workspace 或电脑文件），也可以用来向第三方发送或共享文件。Gemini 在执行这些操作前会请求你的许可。始终仔细检查文件内容，并在授予 Gemini 向他人共享文件的权限前，确认你信任预期的收件人。
- 向 **已连接的文件夹** 添加公共云盘时要小心。Gemini 将能够访问、编辑、共享和删除其中的文件。Gemini 还能把你的数据共享给该云盘，包括来自其他已连接文件夹中的电脑文件、连接应用、个人智能、你已登录的网站、你的位置等信息，以及[更多内容](https://support.google.com/gemini/answer/17094507#sources)。任何被共享的数据都会对有权访问该公共云盘的人可见。
- 不要直接在任务对话串中输入登录信息、付款详情或你认为敏感的信息。

进一步了解[向 Gemini 分配任务前该做什么](https://support.google.com/gemini/answer/17094507#sensitive_info)、[如何检查和管理任务](https://support.google.com/gemini/answer/17094507#work_panel)，以及 [Gemini 如何与你合作保护你和你的信息安全](https://support.google.com/gemini/answer/17094507#agentic_risks)。

远程控制 Mac 上的 Gemini 应用

你可以从另一台设备（例如手机）要求 Mac 上的 Gemini 应用执行操作。这样你不必触碰 Mac 就能使用 Gemini，无缝融入你的工作流程

#### 你需要什么

- Gemini 应用必须已在你的 Mac 上设置并运行。
- 在 macOS 应用中接受将任务移交给 Gemini 的使用条款。
- 另一台设备已登录 Gemini，且使用的账号与你在 Mac 上使用 Gemini 应用时的账号相同。
- 在你的 Mac 和另一台设备上使用同一个 Wi-Fi 网络，或打开并连接蓝牙。

#### 如何连接到你的 Mac

1. 在你的另一台设备上打开 Gemini ![](images/img-01-4a5c21.png)。
   - 确保你在所有想用于远程控制的设备上登录 Gemini 时使用同一个账号。
2. 在文本框上方或下方，点击 **Task**。
3. 点按「添加」![](images/img-02-72d6a4.png) ![然后](images/img-05-bfcdbc.png) 「计算机」![](images/img-06-c80816.png)。
4. 选择你的 Mac。

#### 你可以做什么

- **向 Gemini 分配任务**：从另一台设备（例如手机）在 Mac 上启动任务。例如，让 Gemini 整理你的「下载」文件夹。
- **语音命令**：使用远程设备的麦克风向 Mac 上的 Gemini 说出命令。
- **输入文字**：在远程设备上输入问题和消息。你会在 Mac 上看到 Gemini 的回答。
- **阅读过去的对话**：用另一台设备轻松浏览过去的 Gemini 对话。
- **快捷操作**：启动常见的 Gemini 操作，例如「删除对话」或「开始对话」。
- **媒体控制**：如果 Gemini 正在播放音乐或视频，你可以用另一台设备播放、暂停或跳过。

## 相关资源

- [在 Mac 上使用 Gemini 应用](https://support.google.com/gemini/answer/17011627)
- [在 Gemini 应用中管理你的任务与工作流](https://support.google.com/gemini/answer/17094507)
- [在 Gemini 应用中查找和管理任务](https://support.google.com/gemini/answer/17094196)
- [在 Gemini 中为任务创建和管理计划](https://support.google.com/gemini/answer/17094710)
