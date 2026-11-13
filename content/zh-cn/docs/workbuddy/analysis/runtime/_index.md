---
title: "WorkBuddy：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 主要在用户自己的电脑上执行任务，手机和即时通讯软件只负责下指令和审批；电脑休眠或离线，远程任务就中断。云端沙箱只用于部分定时任务和移动端，规格未公开。
---

## 概要

- WorkBuddy 是 macOS 和 Windows 桌面客户端。经手机或即时通讯软件发起的任务也在用户电脑上执行，文件、命令行、已登录的网站、插件和 MCP 都来自本机。
- 前提是电脑在线：电脑休眠、断网或关闭客户端时，远程访问中断。官方给的办法是开启锁屏运行，或准备一台专属常开的主机。
- 本机执行受沙箱约束：默认以工作空间为边界，命令优先在沙箱中运行，可以按路径、命令前缀、域名配置允许、询问、拒绝三种规则。
- 云端是补充：云端定时任务在云端沙箱运行，电脑关机也能执行，但访问不到本机文件；移动端 App 有「云端工作」模式。更新日志中出现过「云电脑」「云助理」，没有任何资料说明其规格。
- 第三方普遍据此把 WorkBuddy 归为「桌面端 Agent」，与有自己云端电脑的 Personal Agent 区分开。

## 任务在用户自己的电脑上执行

2026-03-04 的 4.5.0 正式版就是一款支持 macOS 与 Windows 的桌面助手，能读写文件、执行终端命令（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。帮助中心把「在获得授权后读取和处理本地文件」列为核心能力（[帮助：简介]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-overview" >}})）。运行依赖逐步补齐：4.6.3 起自动检测并安装缺失的 Python、Node.js；4.22.4 起为 CLI 类连接器按需托管 Node.js 运行时，5.3.11 补上 Python 类连接器运行时；4.22.4 加入实验性的 computer-use 工具，仅限 macOS；5.4.0（08-20）加入 Worktree 任务、Git 分支切换和后台命令面板（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

远程使用时分工很明确。接入指南写明，手机微信「仅发送指令、批准操作和后续消息」，项目文件、Shell 命令、已登录的网站与云服务凭证、插件、MCP、浏览器扩展、Computer Use 都来自电脑（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。助理（远程任务）与普通任务的环境不同：助理固定使用专属文件夹，只有一个会话，所有远程指令集中处理，历史不可清空；普通任务可以自选工作目录、多任务并行（[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})）。

## 电脑离线即中断：锁屏运行与专属主机

官方对这个限制的说法很直接：电脑休眠、断网或关闭 WorkBuddy 时，「远程访问将暂时中断」（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。本地定时任务执行期间也不能关机或退出客户端（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。

官方给出的缓解办法（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）：

- Mac 笔记本保持打开并接电，合盖使用须外接显示器以防休眠。
- 「锁屏远程」自 5.0.0（06-03）起提供；5.5.4（09-08）的「允许锁屏运行」分为关闭、熄屏后继续运行、保持屏幕常亮三种模式。
- 定时巡检、持续集成监控这类长期任务，建议用一台专属常开的 Mac 或 Windows 主机，装好依赖、凭证和插件，主电脑离线时微信助理仍能访问它。
- 5.9.1（10-22）起可以从同账号的其他电脑导入任务、空间和定时任务，5.9.3 把导入上限调到 100 GB。

长时间运行的稳定性问题在日志中反复出现：5.8.3（10-19）修复「长期运行后内存膨胀导致的卡死」，5.3.12 修复本地助理内存快速增长导致白屏或崩溃，5.9.3（10-27）修复 Windows 升级后沙箱初始化失败、所有工具执行报错（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

## 工作空间与沙箱

默认权限以工作空间为边界，即新建任务时选择的目录或自动创建的任务目录；命令优先在沙箱约束下执行，被拦截时再按风险决定是否请用户确认（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。安全中心的「沙箱安全」是总开关，规则按文件路径、命令前缀、域名或 URL 三类配置；另有默认开启的安全网关（工作空间的出入流量统一经过）和本地与云端之间的端到端加密通道（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。权限细节见[安全]({{< relref "/docs/workbuddy/analysis/security" >}})。

首次打开含 `.codebuddy` 等开发配置目录的工作区时，会弹出信任确认；选「受限模式」则不加载其中的规则、命令和脚本（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。项目功能读取的 `.codebuddy/` 配置与 CodeBuddy Code 行为一致（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})），说明 WorkBuddy 与腾讯的编程助手共用同一套本地执行框架。

## 云端沙箱与云电脑：有入口、无规格

云端只在少数地方出现：

- **云端定时任务**：在云端沙箱执行，电脑关机或离线也能按时运行；但云端沙箱访问不到本机文件，提示词里不能引用本地路径，编辑时不选工作空间和权限，也不支持推送企业微信（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。
- **移动端 App**：有「云端工作」和「连接电脑」两种模式（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。
- **项目**：项目级 Skill 在云端统一管理；Web 端与客户端的个人 Skill 库互不相通，云上任务选不到客户端个人库里的 Skill（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})）。
- **云电脑、云助理**：只在更新日志的修复项中出现，例如 5.7.6 修复云助理发消息后无回复、5.11.0 修复云电脑若干问题（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

推断：从这些零散说法看，云端环境是为「电脑不在线也要跑」的场景补的一条路，能力比本机弱（不能碰本地文件、不能推企业微信）。云电脑、云助理是否为每个用户分配独立环境、是否持久、有什么额度，资料没有说明。

## 第三方的分类：桌面端 Agent

第三方普遍以运行环境区分 WorkBuddy 和 Personal Agent。程序员鱼皮称 WorkBuddy 这类桌面端 Agent「更像一个用你的电脑干活的实习生」，干活期间电脑要一直开着，也提到不少桌面端 Agent 支持把部分任务放到云端（[程序员鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。易论AI 对谈中，嘉宾认为二者的区别一是会不会主动做事，二是「有没有自己的电脑」（[易论AI 对谈]({{< relref "/docs/industry/sources/community/2026-11-03-yilun-ai-personal-agent-overhyped" >}})）。阿言er 提醒，桌面与云端并行的产品不等于「本地文件操作在电脑离线时仍能继续」（[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。

《中国新闻周刊》则把 WorkBuddy 与 Muse、Dots、Claude Duet 并列为「关掉电脑仍在干活」的个人智能体（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})），但文中没有单独说明 WorkBuddy 的运行位置。按官方帮助文档，这一说法只适用于云端定时任务。

## 资料缺口

- 云电脑、云助理、云端沙箱的规格、持久化、并发和超时；是否每个用户一台。
- 本地定时任务和远程任务的并发上限、最大执行时长（定时任务页只说「受任务频率、最大执行时长与系统并发控制限制」，未给数值）。
- 本机沙箱的实现方式（macOS、Windows 各用什么隔离技术）。

## 主要资料

- 官方：[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})（本机执行与远程分工、锁屏与专属主机）、[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})（助理的专属文件夹与单一会话）、[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})（本地与云端定时任务）、[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})（工作空间、沙箱、信任确认）、[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})（`.codebuddy` 配置、Web 端与客户端的差异）、[帮助：简介]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-overview" >}})（本地文件操作）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（运行时、computer-use、Worktree、内存问题）
- 媒体：[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})（把 WorkBuddy 列为个人智能体）
- 社区：[程序员鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})、[易论AI 对谈]({{< relref "/docs/industry/sources/community/2026-11-03-yilun-ai-personal-agent-overhyped" >}})、[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})（桌面端 Agent 的分类）
