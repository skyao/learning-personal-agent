---
title: "我向 Meta 的 Muse 要它的文件系统，它给我发来了 6.8 GB"
linkTitle: "Peter James：文件系统导出"
date: 2026-09-22
originalTitle: "I asked Meta’s Muse for its filesystem and it sent me 6.8 GB"
sourceUrl: "https://mouse.dev/blog/muse-runtime-export/"
author: "Peter James"
publisher: "Mouse（mouse.dev 博客）"
language: en
fidelity: 全文翻译
translation: 已翻译
collectedAt: 2026-11-04
tags: [运行环境, 记忆与上下文, 持续执行, 安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：作者 Peter James 在 Mouse（mouse.dev）博客发表这篇文章，是他对自己 Muse 会话环境的梳理。原文页面末尾作者所在产品 Mouse 的测试邀请未译出。原文的「文件系统地图」是可点击的交互组件，译文整理为表格，各条说明照录，包括其中重复的说明。早期收集时直接翻译，原文未单独存档。

**内容摘要**：作者让 Muse 把它能看到的文件打包发到他的 Google Drive，Muse 照做了。压缩后约 2.7 GB，解压后 6.8 GB，似乎包含分配给他会话的 Linux 根文件系统，其中有 Muse 内部文档、集成代码、记忆文件、智能体日志和 SSH 密钥文件。文中描述了其中的内容：Hatch 是 Meta 内部对 Muse 的称呼，约 68 个技能目录，记忆用 Postgres 存储，每晚有「梦」的回顾，还有实验性的 Meta Home Link 文档。作者通过 Meta 漏洞赏金计划提交了报告，被标为「不适用」。他没有确认 SSH 密钥是否有效，也没有演示容器逃逸。

**保留理由**：这篇是对 Muse 运行环境内部结构的一手描述，涉及记忆机制、技能和未发布连接器。作者也写明了哪些事他没有核实。

---

2026 年 9 月 22 日 · Peter James · 6 分钟阅读

- 安全
- 智能体
- 沙箱

本文目录

1. [导出](#导出)
2. [我报告了什么](#我报告了什么)
3. [运行时及其手册](#运行时及其手册)
4. [技能与集成](#技能与集成)
5. [容器搭建](#容器搭建)
6. [Spaces 与文件生成器](#spaces-与文件生成器)
7. [镜像中的 Codex](#镜像中的-codex)
8. [记忆与定时工作](#记忆与定时工作)
9. [Home Link](#home-link)
10. [披露与回应](#披露与回应)

## 导出

我让 Muse 把它能看到的文件打包归档，然后发到我的 Google Drive。它照做了。

下载的文件压缩后约 2.7 GB，解压后 6.8 GB。它似乎包含了分配给我这个会话的 Linux 环境的根文件系统，包括 Ubuntu 系统文件、Muse 的内部文档、集成代码、应用模板、记忆文件和智能体日志。里面还有 SSH 密钥文件。

![Muse 报告正在构建归档](images/fig1.webp)

图 1。Muse 描述了一个更早的归档，其中包含它的代码、文档、记忆和二进制文件。这里的文件数量和大小是聊天中的说法，指的是那次更早的导出。

![Muse 报告已把根目录归档发送到 Google Drive](images/fig2.webp)

图 2。Muse 的交付消息链接到 muse-full-root.zip，称其大小为 2.86 GB。我的笔记记录的是压缩后约 2.7 GB；我还没有核对这两个数字。它上面那条消息对容器逃逸做了一个未经证实的说法。我并没有演示出逃逸。

## 我报告了什么

我通过 Meta 的漏洞赏金计划提交了这些发现，并联系了几位员工。我不会公开这个归档、密钥或会话日志。这是一份关于我发现了什么、以及我能从中确定什么的梳理。

我报告的问题是：内部运行时文件和敏感材料，可以通过一次普通的对话和一个已连接的导出目的地离开那个环境。我还没有确定这些 SSH 密钥是否有效，或者它们能提供什么访问权限。

## 运行时及其手册

大多数有意思的文件都在 `/home/hatch`、`/opt/hatch` 和 `/opt/hatch-image` 下。Hatch 是 Meta 对 Muse 使用的内部名称，运行时文件中通篇使用这个名字。

| 路径 | 说明 |
| --- | --- |
| `/home/hatch` | 智能体的主目录包含 SOUL.md、IDENTITY.md、USER.md、MEMORY.md、AGENTS.md 和 TOOLS.md。 |
| `/home/hatch/SOUL.md` | 智能体的主目录包含 SOUL.md、IDENTITY.md、USER.md、MEMORY.md、AGENTS.md 和 TOOLS.md。 |
| `/home/hatch/IDENTITY.md` | 智能体的主目录包含 SOUL.md、IDENTITY.md、USER.md、MEMORY.md、AGENTS.md 和 TOOLS.md。 |
| `/home/hatch/USER.md` | 智能体的主目录包含 SOUL.md、IDENTITY.md、USER.md、MEMORY.md、AGENTS.md 和 TOOLS.md。 |
| `~/MEMORY.md` | ~/MEMORY.md 是一张简短的事实、偏好和承诺清单。 |
| `/home/hatch/AGENTS.md` | 智能体的主目录包含 SOUL.md、IDENTITY.md、USER.md、MEMORY.md、AGENTS.md 和 TOOLS.md。 |
| `/home/hatch/TOOLS.md` | 智能体的主目录包含 SOUL.md、IDENTITY.md、USER.md、MEMORY.md、AGENTS.md 和 TOOLS.md。 |
| `agents/` | 一个 agents/ 目录包含 113 条带有 JSONL 轨迹的子智能体记录。 |
| `docs/` | 大约 20 个 Markdown 文件描述了浏览器使用、连接器、支付、凭证、数据处理、生成的文件、语音、目标和定时安排。 |
| `docs/devices/home_link.md` | docs/devices/home_link.md 描述了一个名为 Meta Home Link 的实验性集成，使用一块带 Wi-Fi 和低功耗蓝牙的 ESP32-C5。 |
| `~/memory/` | ~/memory/ 下按日期命名的文件保存日常细节。智能体可以在对话过程中写入这些文件。 |
| `memory/bank/` | memory/bank/ 下的文件把这些材料整理为境况、经历和偏好，并附有指向源文本行的引用。 |
| `~/dreams/` | 每晚的一次「梦」会回顾最近的对话，并为以后的会话写下指导。 |
| `workspace/self_improvement/` | 这些运行会在 workspace/self_improvement/ 下留下回执，而它们实际做出的修改会写入相关的记忆和工作区文件。 |
| `/opt/hatch` | 大多数有意思的文件都在 /home/hatch、/opt/hatch 和 /opt/hatch-image 下。Hatch 是 Meta 对 Muse 使用的内部名称，运行时文件中通篇使用这个名字。 |
| `/opt/hatch/skills/` | 在 /opt/hatch/skills/ 下，我数到大约 68 个技能目录。它们一般把一个 SKILL.md 说明文件与一个命令行工具或支持代码配成一对。 |
| `/opt/hatch/runtime-cell/` | /opt/hatch/runtime-cell/ 包含 18 个文件，包括构建根文件系统、用 systemd-nspawn 启动它，以及运行启动钩子和守护进程的脚本。 |
| `/opt/hatch-image` | 大多数有意思的文件都在 /home/hatch、/opt/hatch 和 /opt/hatch-image 下。Hatch 是 Meta 对 Muse 使用的内部名称，运行时文件中通篇使用这个名字。 |
| `/opt/hatch-image/bin/codex` | Codex CLI 安装在 /opt/hatch-image/bin/codex，报告的版本是 0.149.0。我没有找到 Muse 把它用作编程智能体的证据。 |
| `/opt/hatch-image/bin/codex-resources/bwrap` | 这个二进制文件位于 codex-resources/bwrap 下，自称是「bubblewrap built for Codex」。 |

智能体的主目录包含 `SOUL.md`、`IDENTITY.md`、`USER.md`、`MEMORY.md`、`AGENTS.md` 和 `TOOLS.md`。旁边还有文档、记忆、工作区项目、频道（channels）、钩子（hooks）和订阅（subscriptions）的目录。一个 `agents/` 目录包含 113 条带有 JSONL 轨迹的子智能体记录。

这些文档对理解这个系统异常有用。大约 20 个 Markdown 文件描述了浏览器使用、连接器、支付、凭证、数据处理、生成的文件、语音、目标和定时安排。另有针对 WhatsApp、配对的 Mac、Tailscale 以及一个名为 Home Link 的设备集成的单独指南。

![muse.md 产品手册](images/fig3.webp)

图 3。muse.md 的开头描述了为每位用户提供的一台持久的智能体计算机，并指向该产品的其他指南。这些是导出文档中的陈述。

## 技能与集成

在 `/opt/hatch/skills/` 下，我数到大约 68 个技能目录。它们一般把一个 `SKILL.md` 说明文件与一个命令行工具或支持代码配成一对。它们涵盖 Google Workspace、Meta 的社交应用、Outlook、旅行、购物、健康服务、家庭设备和媒体生成。

![「分享想法」技能的说明](images/fig4.webp)

图 4。一个 SKILL.md 文件的例子：share_ideas 规定了智能体应该在什么时候使用它，并描述了一个随公开页面打包的 INSTALL.md 文件。

两个配置文件 `skill-scopes.conf` 和 `bin-scopes.conf` 暗示了 Meta 正在筹备的未发布连接器。其中包括 Slack、Dropbox、Polymarket、Canva 和 Klaviyo 等名字，外加一个 internal-facebook-cLI。

## 容器搭建

容器的搭建也包含在内。`/opt/hatch/runtime-cell/` 包含 18 个文件，包括构建根文件系统、用 `systemd-nspawn` 启动它，以及运行启动钩子和守护进程的脚本。一个单独的 `runtime-cell.kdl` 清单描述了镜像中的软件包和 systemd 单元。

这些文件让我对分配给我的 Linux 环境是如何组装起来的有了相当清楚的了解。但它们不足以审计整个服务，也无法证明那个环境之外的基础设施的任何情况。

## Spaces 与文件生成器

我找到的最大的代码项目是 Spaces 框架，Muse 用它来构建和提供应用。它的 TypeScript 起步模板包括一个 React 客户端、服务端操作（server actions）、一个 Drizzle SQLite schema、SQL 迁移和 Bun 配置。还有一个较小的静态模板，以及位于名为 `worker`、`sdk`、`cloudflare` 和 `cvm` 的目录中的运行时代码。

![Spaces 运行时目录](images/fig5.webp)

图 5。Spaces 目录包含模板和一个 TypeScript 运行时，包括 worker、sdk、cloudflare 和 cvm 文件夹。目录列表展示的是结构，而不是完整的实现。

导出的内容还包括文档、PDF、演示文稿、电子表格和 Markdown 的生成器。另有一个单独的 `magic-moment` 技能，包含用于合成卡片和视频的代码，以及浏览器截取脚本、字体和品牌素材。

还有大量图标！

![导出内容中包含的图标](images/fig6.webp)

图 6。导出文件中包含的部分 WebP 图标。

## 镜像中的 Codex

Codex CLI 安装在 `/opt/hatch-image/bin/codex`，报告的版本是 `0.149.0`。我没有找到 Muse 把它用作编程智能体的证据。

Hatch 确实使用了它捆绑的 **bubblewrap** 副本，这是一个 Linux 沙箱工具。这个二进制文件位于 `codex-resources/bwrap` 下，自称是 `bubblewrap built for Codex`。

Muse 用它为 `ffmpeg` 和 `ffprobe` 提供沙箱，用于视频处理、生成缩略图和检查文件。这些任务在没有网络访问、没有额外权限的情况下以用户 `nobody` 的身份运行，沙箱中暴露 `/input` 和 `/output` 目录。如果缺少 bubblewrap，它们会以 `failed to prepare ffmpeg sandbox` 失败。

我没有找到调用 Codex 本身的代码。临时的 Codex 文件来自我们做的版本检查，而 Hatch 二进制文件中的 `codex` 和 `gpt-5.5` 字符串是提供方列表中的条目，导出内容中没有任何东西显示它们被选用。

就我能确定的范围而言，Meta 随镜像附带了 Codex CLI，但只使用了它捆绑的沙箱。

## 记忆与定时工作

![Muse 记忆的工作方式](images/memory-diagram.webp)

Muse 把记忆存储在纯 Markdown 文件中。`~/MEMORY.md` 是一张简短的事实、偏好和承诺清单。`~/memory/` 下按日期命名的文件保存日常细节。智能体可以在对话过程中写入这些文件。

一个每小时运行的后台任务会把新的说法与原始消息进行核对，并记录一段引文、消息 ID 和一个说法 ID。它决定哪些内容属于精选清单，哪些留在每日日志里。`memory/bank/` 下的文件把这些材料整理为境况、经历和偏好，并附有指向源文本行的引用。

Postgres 让这些文件可以被搜索。`memory.entries` 存储文本块和行引用，`memory.embeddings` 保存 384 维的向量，`memory.claims` 跟踪证据、置信度和状态。较新的说法可以通过 `supersedes_claim_id` 取代较旧的说法。智能体可以用 `memory_search` 搜索这个存储，并用 `memory_explain` 查看某个结果背后的证据。

其他后台任务负责维护人际关系页面、回顾反复出现的工作流，以及准备想法或目标简报。这些运行会在 `workspace/self_improvement/` 下留下回执，而它们实际做出的修改会写入相关的记忆和工作区文件。

每晚的一次「梦」（dream）会回顾最近的对话，并为以后的会话写下指导。在我的这份里，它注意到我喜欢简短的回复、不喜欢反复的追问，而且我没有要求过它主动推送 NFL 比分。按日期命名的梦保存在 `~/dreams/` 下；一个单独的 `ALIGNMENT_SYNTHESIS.md` 把这些观察转化为长期有效的指导。这些梦的文件带有 `prompt_hoisted: false`，所以其文字本身并没有被注入到提示中。

![一条关于 Pete 的、按日期命名的梦的记录](images/fig7.webp)

图 7。一条 9 月 21 日的梦的记录，描述了我的沟通风格和偏好。截图中包含它的 dream_path 和综合（synthesis）元数据。它展示的是一条写下的记忆记录。

遗忘不只是删除一条笔记。遗忘流程会把要撤回的说法 ID 暂存起来，删除关联的材料，并重建索引，这样后续的任务就不会把它重建出来。这就是系统随时间适应的方式：更新以后的会话可以读取的文件、可搜索的记录和说明。模型的权重保持不变。

## Home Link

硬件文档是最大的意外。`docs/devices/home_link.md` 描述了一个名为 Meta Home Link 的实验性集成，使用一块带 Wi-Fi 和低功耗蓝牙的 ESP32-C5。它涵盖了设备配对、本地网络发现，以及通过一个代理、经过单独批准步骤的智能体访问。还已经有了通过 IPP 连接 Brother 打印机和连接 Lutron 网桥的集成指南。

![Meta Home Link 文档](images/fig8.webp)

图 8。Home Link 指南称这一集成是实验性的，并列出了 ESP32-C5 硬件、Wi-Fi，以及用于首次设置的低功耗蓝牙。

这表明 Meta 正在开发让 Muse 访问家庭网络上设备的功能。我不知道它是一个内部原型、一次有限的实验，还是 Meta 计划推出的东西。

## 披露与回应

我通过 Meta 的漏洞赏金计划提交了报告和发现。Meta 把这份报告标记为「不适用」（Not Applicable）。我也联系了几位员工，并收到了回复。

![Meta 的漏洞赏金回复](images/fig9.webp)

图 9。Meta 把这份报告标记为「不适用」。回复列出了作出这一决定的几种可能理由，但没有说明具体适用哪一条，并欢迎提供更多关于安全或隐私影响的证据。

我轻度试探了一下容器边界，想让 Muse 逃逸出来，但在我的测试中它似乎守住了；我开始去试探发现的那 80 个套接字，但出于这是生产系统的性质，老实说也因为我在这方面缺乏经验，我停了下来。

如果你想了解更多信息，可以联系我。pete at mouse.dev

-Pete

[@heypeterjames](https://x.com/heypeterjames)
