---
title: "文档：开始使用 Grok Bot"
linkTitle: "文档：开始使用"
date: 2026-11-05
originalTitle: "Get started with Grok Bot"
sourceUrl: "https://docs.x.ai/grok-bot/get-started"
altUrls: ["https://cursor.com/docs/grok-bot/get-started"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：全文重排为五步；新增 X 订阅 Premium/Super/Ultra 包含 Grok Bot、Grok 账号链接步骤、Overheard 等四个示例 Bot 与四个起步提示；删去手机端「仍在桌面端」的功能说明"
tags: [功能更新, 开放与价格, 设备, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：此文分五步带用户从安装桌面应用到让第一个任务按计划重复：下载安装、登录、认识第一个 Bot、交给它第一个任务、做成例程。X 订阅的 Premium、Super、Ultra 包含 Grok Bot，旧 Cursor 套餐和已链接的 SuperGrok、X Premium+ 或 Grok Business 席位也可用；Privacy Mode (Legacy) 账号需先切换，需要时用 **Link Grok Account** 链接 Grok 账号。登录后系统建立名为 Grok Bot 的第一个 Bot，也可从 Overheard、Tradbot、Meeting Recap Deck、Pitch Deck Coach 等现成 Bot 起步，之后用 **New Bot**（+）添加更多；建议每个 Bot 在第一条消息里只给一个工作并让它记住怎么做。好的请求要说明想要的结果、用哪些资料、有什么限制、何时来问用户，文中给出四个起步提示（如 Morning briefing）。遇到需要登录的应用，Bot 先用 Vault 中的登录或已连接的密码管理器，否则用 Secure Form 向用户要，它看不到密码；SSO、通行密钥等步骤转交用户点击 **Open computer**，结果满意后让 Bot 按计划重复，即成为例程。手机端要求 iOS 18 以上或 Android 9 以上，可发消息、查看和接管电脑、审批动作、暂停或恢复例程。

**保留理由**：用最短路径说明新用户的上手流程、凭证处理方式和手机的功能范围，也重复了访问权来源。

---

开始使用

Grok Bot 给你一些 Bot，让它们在一台共享的云计算机上为你工作。在本指南中，你将安装应用、登录、把一项真实任务交给你的第一个 Bot，并让它按计划重复这项任务。

## 1. 安装桌面应用

从 [x.ai/bot](https://x.ai/bot) 下载 Grok Bot 并打开。

**其他下载方式与支持的系统**

在团队中，[Cursor 仪表盘](https://cursor.com/dashboard/bot)的 Grok Bot 页面有一行**下载 Grok Bot**（Download Grok Bot），可以安装应用或复制一个可分享的链接。如果你没有仪表盘访问权，向管理员要链接。如果你是管理员，见[将 Grok Bot 部署到你的组织](https://docs.x.ai/grok-bot/deployment)。

该应用运行在 macOS（Apple silicon 和 Intel）、Windows（x64 和 Arm64）以及 Linux（x64 和 Arm64）上。它会自动检查更新。Linux 的 `.deb` 和 `.rpm` 安装则通过你的包管理器更新。

## 2. 登录

在欢迎屏幕选择**登录**（Sign in），然后在浏览器中完成。

**哪些套餐包含 Grok Bot**

The X Subscription 的 Premium、Super 和 Ultra 包含 Grok Bot，适用于个人或团队席位。在旧版 Cursor 套餐上，每个付费个人套餐和自助式 Cursor Teams 都包含它。你也可以关联个人 SuperGrok、SuperGrok Plus、SuperGrok Heavy 或 X Premium+ 订阅，或使用自助式 Grok Business 套餐的席位。见 [The X Subscription 上的 Grok Bot](https://docs.x.ai/x-subscription/grok-bot) 和[套餐与计费](https://grok.com/help/grok-bot/plans)。

Grok Bot 需要云数据存储，因此如果你的账户处于隐私模式（旧版）（Privacy Mode (Legacy)），应用会要求你先切换到隐私模式。在团队中，由团队管理员更改团队的隐私设置。

**单点登录与 Grok 账户**

Grok Bot 使用你的 Cursor 账户，因此没有单独的登录。如果你的公司使用单点登录，照常登录即可；你的 Cursor SSO 设置适用。

如果你的访问权来自自助式 Grok Business 套餐的席位，在浏览器中选择**使用 Grok 登录**（Sign in with Grok），并使用持有该席位的 Grok 账户。

如果你的访问权来自 SuperGrok 或 X Premium+ 订阅，请添加 Grok 账户关联。在桌面端，于 [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding) 的 **Grok Bot 入门**页面选择**关联 Grok 账户**（Link Grok Account）。在 iPhone 和 Android 上，在访问屏幕选择**关联 Grok 账户**，完成 Grok 登录，然后选择**关联完成了？刷新我的状态**（Finished Linking? Refresh My Status）。

如果你已经有访问权，打开**设置 → 用量与计费**（Usage & billing），在**管理套餐**（Manage plan）下查看**通过 Grok 获取访问权**（Get access with Grok）。只有关联会提高你的用量时它才会出现。

如果登录没有完成，见[登录未完成](https://docs.x.ai/grok-bot/troubleshooting#sign-in-does-not-complete)。

## 3. 认识你的第一个 Bot

经过一段简短的介绍后，应用会建立你的第一个 Bot，名为 **Grok Bot**，并打开与它的聊天。

你也可以从已经为某项工作设置好的 Bot 起步。

* [Overheard](https://x.ai/bot/marketplace/bots/overheard) — 监视 Reddit、Hacker News、新闻网站和 X 上关于你的名字、品牌和 URL 的第三方提及，当有内容达到标准时，在工作日发送一份简短摘要。没有动静的日子保持安静，并且从不代表你发帖。

* [Tradbot](https://x.ai/bot/marketplace/bots/tradbot-2) — 监视你的个人邮箱和日历，让学校表格、账单和 RSVP 不再被漏掉。起草回复，发现接送时间冲突，未经你同意绝不发送。

* [Meeting Recap Deck](https://x.ai/bot/marketplace/bots/echo) — 把你的会议笔记变成套用你的幻灯片模板的回顾演示文稿。基于你粘贴或上传的笔记工作，从不编造引语。

* [Pitch Deck Coach](https://x.ai/bot/marketplace/bots/pitch-deck-coach) — 审阅一份路演演示文稿，报告投资人可能理解、相信、质疑和记住什么，然后帮助加强故事、证据和幻灯片。

[浏览市场](https://x.ai/bot/marketplace)

**设置更多 Bot**

选择侧边栏顶部的**新建 Bot**（New Bot，即 **+** 按钮），或按 `Cmd/Ctrl+N`。给 Bot 命名并选择**创建**（Create）。在团队中，**+** 会打开菜单。选择**创建 Bot**（Create a Bot）新建一个，或选择**浏览团队 Bot**（Browse Team Bots）使用队友分享的 Bot。要与队友分享你自己的 Bot，见 [Team Bot](https://docs.x.ai/grok-bot/team-bots)。

要以后重命名 Bot，点击聊天顶部的名称打开详情，然后再次点击名称进行编辑。

在第一条消息中给每个 Bot 一项工作，并让它记住你希望工作如何完成。只有一个职责的 Bot 能建立比什么都做的助手更有用的上下文。见[你的主 Bot 与只做一项工作的 Bot](https://docs.x.ai/grok-bot/how-grok-bot-works#your-primary-bot-and-bots-with-one-job)。

## 4. 交给它第一个任务

像请同事帮忙那样提出请求。说明你想要什么结果、使用哪些来源、有哪些限制，以及何时与你确认。当某个操作需要你同意时，Bot 会显示一张[审批卡片](https://docs.x.ai/grok-bot/approvals-security-and-privacy#review-an-action)并等待。

### 晨间简报

一份关于什么需要你的晨间简报，可直接发布。

**起步提示**

> Sum up what changed since yesterday in my inbox, calendar, Slack, and docs, and flag what needs me. Draft it as a post for #team; don't send it.

### 收件箱管理

紧急话题优先，回复已起草等你确认。

**起步提示**

> Sort my unread email into urgent, needs a reply, and FYI. Draft replies to the urgent ones and don't send anything.

### 竞争情报

竞争对手本周发布或调价了什么，附链接。

**起步提示**

> Check these three competitors for anything they launched or repriced this week. Send me a short list with links and what it means for our messaging.

### 旅行协调

两个最佳航班和酒店，等你挑选。

**起步提示**

> Find flights to Austin for Thursday, back Sunday, with no red-eyes, and a hotel near downtown. Send me the two best options; don't book anything.

**用说的，不用打字**

要听写，在桌面端选择**开始语音输入**（Start voice input，`Cmd/Ctrl+D`），在 iPhone 和 Android 上选择**开始听写**（Start dictation）。要实时对话，选择**开始语音聊天**（Start voice chat）。

**当任务需要登录时**

登录时，Bot 先使用保存在 [Vault](https://docs.x.ai/grok-bot/vault) 中的登录信息，然后是已连接的密码管理器（如 [1Password](https://docs.x.ai/grok-bot/computer-and-apps#connect-1password)），再用[安全表单](https://docs.x.ai/grok-bot/vault#secure-forms)向你询问。它永远看不到密码，会话通常会在 Bot 的计算机上保持登录，供下次使用。对于受支持的服务，你可以改为[连接应用](https://docs.x.ai/grok-bot/computer-and-apps#connect-an-app)。

对于单点登录、通行密钥或表单无法处理的其他步骤，Bot 会把计算机交给你。在请求上选择**打开计算机**（Open computer），然后选择**接管**（Take control），完成该步骤，再让 Bot 继续。

## 5. 把它变成例程

告诉 Bot 要固定什么、保留哪些偏好，例如报告格式。结果正确后，让它按计划执行该任务，它就会变成一个[例程](https://docs.x.ai/grok-bot/skills-routines-and-automations#create-a-routine)。

## 接下来

你的 Bot 现在按计划运行那项任务。接下来，连接更多你使用的应用，把你反复做的任务变成各自独立的 Bot，再把几个 Bot 组成团队去完成更大的目标。

1. [助手](https://docs.x.ai/grok-bot/use-cases#connect-your-apps-and-get-help-with-your-work) — 在你的应用中查找信息并起草工作

2. [有职责的 Bot](https://docs.x.ai/grok-bot/use-cases#turn-tasks-you-repeat-into-a-bot) — 接管你反复做的一项任务

3. [Bot 团队](https://docs.x.ai/grok-bot/use-cases#build-a-team-of-bots-for-a-bigger-goal) — 一起朝着更大的目标工作

在手机上，从 App Store 或 Google Play 安装 Grok Bot，并用同一账户登录。见[手机上的 Grok Bot](https://docs.x.ai/grok-bot/mobile)。

**手机上能做什么**

iPhone 应用需要 iOS 18 或更高版本，Android 应用需要 Android 9 或更高版本。

两个应用都能访问与桌面端相同的 Bot、对话、例程和云计算机。来自你的套餐或 Grok 账户关联的访问权无需再次购买即可延续。在手机上，你可以给 Bot 发消息、查看并接管计算机、批准操作、暂停或恢复例程。

如果某项功能不工作，退出并重新打开应用。如果仍未解决，见[故障排除](https://docs.x.ai/grok-bot/troubleshooting)或[联系支持](https://docs.x.ai/grok-bot/troubleshooting#before-contacting-support)。
