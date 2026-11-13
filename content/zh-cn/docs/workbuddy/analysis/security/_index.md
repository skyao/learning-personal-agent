---
title: "WorkBuddy：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 的安全设计是本机沙箱加分级审批：默认权限下删除、执行脚本、敏感路径写入、越界联网要确认，另有删除保护、自动备份、凭证检测。AI 审查与提示注入防护默认关闭；日志披露过沙箱逃逸、审批被绕过等修复。
---

## 概要

- 两种权限模式：默认权限下高风险动作逐项确认；完全访问权限关闭全部二次确认，是对整个客户端生效的全局开关。权限页建议只在隔离环境短时使用，定时任务页却把它标为「推荐」。
- 本机防护层次多：沙箱规则（路径、命令、域名三类，各分允许、询问、拒绝）、删除保护与批量删除审批、修改前自动备份、凭证类敏感信息检测与加密流转、网络规则。
- 针对模型本身的防护（模型行为审查、工具内容注入防护、AI 智能审批）三个开关默认全部关闭，完全访问模式下也不启用。
- 远程指令做多层来源校验，高风险操作在聊天中确认；邮件内容只作参考输入，不能覆盖安全规则。
- 技能是主要风险点：官方明说非官方 Skill 可能有提示注入、越权、后门，安装前自动扫描。
- 更新日志记录了沙箱逃逸攻击链、通配符绕过规则、子 Agent 与 plan 模式绕过审批等修复；资料中没有外部披露的漏洞、安全事件或漏洞赏金。

## 默认权限与完全访问

权限模式的入口是输入框底部的常驻按钮，日常建议用默认权限（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。默认权限下需要确认的操作（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）：

- 写入受保护或敏感路径；
- 删除受保护文件、重要目录，或批量删除；
- 执行脚本命令或外部程序；
- 命中安全中心规则的网络访问或敏感能力。

取消确认则跳过该步，5.4.4 起拒绝单步权限只跳过当前步骤（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

完全访问权限关闭上述确认，对当前客户端所有已有和新建任务生效；开启时弹窗列出放开的能力：文件操作、终端命令、访问互联网，文件可访问「计算机上任意位置」（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。权限页写明它「并非更安全，只是把确认环节交给 AI 自动通过」，建议只在 Docker、虚拟机、临时目录等隔离环境中短时使用（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。但定时任务页把「完全访问权限」标为推荐，理由是任务可以无人值守（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。两页口径相反，矛盾见[持续执行]({{< relref "/docs/workbuddy/analysis/continuous-execution" >}})。5.9.1 起，视频生成等高积分工具在完全访问模式下也要先征得同意（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

该设置不跨设备生效，每台客户端独立管理（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。

## 沙箱、删除保护与备份

安全中心的「沙箱安全」是总开关，规则分文件路径、命令前缀、域名或 URL 三类，每类可设允许、询问、拒绝（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。其他防护（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）：

- **删除保护**：开启后优先移到回收站；批量删除审批在一次删除达到设定数量（默认 50）时触发，须先开启删除保护。
- **自动备份**：修改已有文件前生成快照，默认开启；所有会话共享备份空间，默认上限 3000 MB，不足时清理最早的备份。页面明说默认权限「不能替代备份」，建议为任务新建文件夹、只放副本。
- **网络规则**：远程 HTTP 请求默认询问，本地 HTTP 请求默认放行，白名单域名不受限；2026-11-09 新增 HTTP 类 MCP 连接同样受域名规则管控，每次重定向后重新判定，规则服务不可用时阻止连接、「不会自动降级放行」。macOS 可开网络严格模式。
- **工具管控**：可按工具、MCP 服务及单个工具启用或禁用，禁用后调用前即被拦截。
- **审计中心**：记录拦截与放行日志，可导出。

## 凭证与敏感信息

敏感保护默认开启，内置规则库覆盖常见凭证类型，用关键词、正则、熵值检测（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。输入侧可选允许访问、允许加密访问（推荐）、禁止访问；选择加密时，明文以密文参与上下文流转，输出时自动还原；执行命令、联网搜索、抓取网页等对外动作前做输出检测（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。

连接器凭据（OAuth Token、API 密钥）由 WorkBuddy 维护（[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})）；自定义模型的 API Key 只存在本地（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）；飞书、钉钉、QQ 机器人的凭证要用户自己保管，QQ 的 AppSecret 不明文保存、二次查看强制重置（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。

## 针对模型的防护：默认关闭

「AI 安全防护」分组有三个开关，默认全部关闭（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）：

| 开关 | 作用 |
| --- | --- |
| 模型行为智能审查 | 执行前用 AI 识别高风险操作 |
| 工具内容注入防护 | 识别工具返回内容中的诱导指令，疑似风险时先经用户确认再进入模型上下文 |
| AI 智能审批 | 由 AI 代为审批，可选仅风险提示或自动审批 |

「允许完全访问」模式下不启用 AI 安全防护（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。

推断：WorkBuddy 的默认防线是规则与人工确认，而不是独立的审查模型。提示注入防护需要用户自己打开，而最容易需要它的无人值守场景（完全访问）恰好不启用它。

## 远程、邮件与技能

- **远程指令**：绑定身份、对每条远程指令做多层来源校验、高风险任务须确认（[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})）；4.9.1 起可在即时通讯中用文字回复审批，同版修复企微机器人把「跳过」高危指令当作「拒绝」处理（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。
- **邮件**：WorkBuddy 以独立助手身份收信，邮件内容仅作参考输入，「不会覆盖 WorkBuddy 的安全规则」，附件经安全扫描；但官方也声明不代为判断邮件内容是否适合发送（[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})）。
- **技能**：官方提示 Skill 可能把输入发往第三方，非官方 Skill「可能存在恶意提示词注入、越权访问、后门程序等隐患」，Skill 以用户本人身份执行，删除、批量写入、资金类操作建议先小范围验证（[帮助：技能]({{< relref "/docs/workbuddy/sources/official/2026-10-16-help-skills" >}})）。4.7.5（03-30）起安装 Skill 前自动扫描恶意脚本与风险行为（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。
- **项目**：公共授权连接器的调用日志只有管理员可见，用于审计；项目权限按角色管控（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

## 更新日志披露的安全修复

日志中与安全直接相关的修复（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）：

| 版本 | 修复 |
| --- | --- |
| 5.1.0（06-13） | `~/.workbuddy/binaries` 写保护缺失导致的沙箱逃逸攻击链；沙箱通配符 `*` 跨目录边界绕过安全规则；完全访问权限会话仍走沙箱；plan 模式下代理调用跳过审批 |
| 5.1.1（06-14） | binaries 目录加写保护阻断逃逸攻击链 |
| 5.2.6 | 文件下载接口缺少安全响应头带来的潜在 XSS 风险 |
| 5.3.3（07-21） | 子 Agent 编辑文件未走沙箱审批 |
| 4.21.0（04-28） | 新增连接器代理的 DNS Rebinding 防护与 Bearer 强校验 |

这些都是厂商自述的修复，没有披露发现者、影响范围或是否被利用。资料中没有 WorkBuddy 的外部漏洞报告、安全事件或漏洞赏金计划。

第三方只有泛指的观点：阿言er 强调「权限由软件执行，而不是由模型自行宣布」（[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）；易论AI 对谈嘉宾称提示注入「次数一多，总会有一次中招」（[易论AI 对谈]({{< relref "/docs/industry/sources/community/2026-11-03-yilun-ai-personal-agent-overhyped" >}})）。

## 资料缺口

- 外部安全审计、渗透测试、漏洞赏金；5.1.0 沙箱逃逸问题的发现经过与影响。
- 微信支付插件的支付确认与限额设计。
- 云端沙箱的隔离方式。
- 三个 AI 安全防护开关实际使用的模型与误报率。

## 主要资料

- 官方：[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})（权限模式、沙箱、备份、敏感保护、AI 安全防护）、[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})（定时任务对完全访问的推荐）、[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})、[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})（远程校验与凭证保管）、[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})（邮件防操控）、[帮助：技能]({{< relref "/docs/workbuddy/sources/official/2026-10-16-help-skills" >}})（技能风险）、[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})、[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})（凭据存放）、[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})（审计）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（安全修复）
- 社区：[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})、[易论AI 对谈]({{< relref "/docs/industry/sources/community/2026-11-03-yilun-ai-personal-agent-overhyped" >}})（通用观点）
