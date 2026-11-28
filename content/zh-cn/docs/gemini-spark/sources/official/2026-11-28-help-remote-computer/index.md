---
title: "监控和管理 Gemini 任务使用的远程计算机"
linkTitle: "帮助：远程计算机"
date: 2026-11-28
originalTitle: "Monitor & manage the remote computer for tasks in Gemini"
sourceUrl: "https://support.google.com/gemini/answer/18789153?hl=en"
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）"
tags: [运行环境, 安全, 隐私]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的 Computer 视图（浏览器客户端标识）；页面中的界面小图标已下载。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Gemini 可以用远程计算机运行代码、处理复杂任务；开启网络访问后还能安装软件、下载数据、连接在线服务。网络访问默认关闭；开启前页面提示：所有任务共用同一台远程计算机，上面会保存工具、配置、登录令牌、命令历史和文件，访问不受信任的来源可能下载并运行恶意代码、外传任务文件，开启期间不要共享密钥或凭据。关闭网络访问会立即断网并删除远程计算机上保存的文件和工具，也可以在 Task 设置中删除全部远程代码执行数据，并查看已执行代码的快照。

**保留理由**：任务总览页只用一句话提到远程计算机，这篇给出网络访问的默认值、风险提示和关闭后的处理，是 Task 运行环境的一手说明。

---

Gemini 可以使用远程计算机运行代码并处理复杂任务。如果你为远程计算机开启网络访问，Gemini 还可以安装软件、下载数据并连接在线服务，从而做更多事。例如，它可以帮助你：

- **处理文档与数据：** 从 PDF 中提取数字、流式处理并分析大型数据集，以及运行繁重的 CSV 或表格操作。
- **跟踪并为实时公共数据制图：** 直接连接实时数据源（如天气、市场汇率或地震监测），分析实时趋势并生成交互式图表。
- **创建与编辑多媒体：** 即时下载开源视频和音频工具，剪辑录音、生成字幕，以及制作带动画波形的片段。

**重要：**

- 目前，此功能及其设置仅在 Gemini 移动应用和 [gemini.google.com](https://gemini.google.com) 的 Gemini 网页应用中可用。
- 我们正在逐步开放远程计算机的网络访问，因此你可能暂时还不能使用。

## 向 Gemini 分配编程与复杂任务

你可以把需要处理文件或收集数据的编程或复杂任务分配给 Gemini。例如：「下载一篇开放获取的 AI 研究论文，提取其架构图，并在摘要文档中解释它们。」

当任务需要额外的算力或编程工具时，Gemini 会自动使用远程计算机处理该任务。[了解如何向 Gemini 分配任务](https://support.google.com/gemini/answer/17094507)。

## 查看在远程计算机上执行的代码

当 Gemini 使用远程计算机时，你可以查看它运行代码的快照。

1. 在电脑上打开使用远程计算机的任务线程。
2. 在顶部点击 **计算机** ![](images/img-01-944c54.png) ![然后](images/img-02-bfcdbc.png) **查看已执行的代码** ![](images/img-03-a30ec9.png)。
3. 要翻阅快照，在底部点击「查看上一个」![](images/img-04-ace26c.png)、「查看下一个」![](images/img-05-4a00fc.png)或 **查看最新** ![](images/img-06-250a06.png)。
4. 要返回任务线程，在顶部点击「关闭远程浏览器」![](images/img-07-59ce42.png)。

## 管理远程计算机的网络访问

默认情况下，Gemini 用于处理你任务的远程计算机不连接互联网。你可以在任务设置中开启「远程计算机的网络访问」，让 Gemini 可以上网协助处理你的任务。

开启网络访问之前

为远程计算机开启网络访问之前，请查看以下重要细节和风险：

- **你的任务共用一台计算机。** Gemini 在你所有任务中使用同一台远程计算机。
- **了解数据保留多久，以及你的选择。** 为帮你把事情办成，你的计算机会存储一些数据，例如维持工作区运行的核心工具和软件文件、你的个人配置、工具登录令牌、命令历史和文件。其中部分数据会在设定的时间后自动过期，部分会一直保留到你删除。你可以问 Gemini 它存储了哪些数据（包括文件）。你可以随时在[任务设置](https://gemini.google.com/gemini-spark)中删除其中任何数据。[了解如何删除远程代码执行数据](#delete_code_data)。
- **当心不安全的代码。** 当远程计算机连接在线服务或不受信任的来源时，它可能接触到会自动下载并运行的恶意或不安全代码。这类不安全代码可能读取已保存的任务文件并在线分享它们。
- **留意已保存的文件和代码。** 你可以随时在[任务设置](https://gemini.google.com/gemini-spark)中管理或清除代码执行历史和文件。

开启或关闭远程计算机的网络访问

**重要：** 在网络访问开启期间，绝不要分享含敏感或个人信息、密钥、API 密钥或私人凭据的文件。

为远程计算机开启网络访问后，Gemini 可以连接在线网站和服务。它还可以下载软件、安装软件包并调用外部 API。

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-08-bbb6bc.png) ![然后](images/img-02-bfcdbc.png) **任务设置** ![](images/img-09-57eb08.png)。
3. 开启或关闭 **远程计算机的网络访问**。

关闭网络访问后会发生什么

如果你关闭「远程计算机的网络访问」，它会：

- 立即断开远程计算机与互联网的连接
- 删除你在远程计算机上保存的文件和工具

## 删除远程代码执行数据

当 Gemini 使用远程计算机运行代码或执行复杂任务时，它会为方便起见在远程计算机上保存数据供以后的会话使用。你可以随时在任务设置中删除远程计算机上保存的所有数据。这会删除过去会话中保存的所有远程代码执行文件和数据。

1. 在电脑上前往 [gemini.google.com](https://gemini.google.com)。
2. 在底部点击「设置」![](images/img-08-bbb6bc.png) ![然后](images/img-02-bfcdbc.png) **任务设置** ![](images/img-09-57eb08.png)。
3. 在「删除远程代码执行」下点击 **删除** ![](images/img-10-23ae4d.png)。

## 相关资源

- [在 Gemini 应用中管理任务与工作流](https://support.google.com/gemini/answer/17094507)
- [管理 Gemini 中任务的浏览器与应用权限](https://support.google.com/gemini/answer/18766567)
- [为 Gemini 中的任务创建和管理时间表](https://support.google.com/gemini/answer/17094710)
- [为 Gemini 应用创建和管理技能](https://support.google.com/gemini/answer/17094296)
- [查找和管理 Gemini 应用中的任务](https://support.google.com/gemini/answer/17094196)
- [在 Mac 上的 Gemini 应用中分配任务](https://support.google.com/gemini/answer/17208717)
