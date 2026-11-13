---
title: "WorkBuddy：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 的连接器以腾讯自家办公服务为主，海外版另有 Gmail、Outlook；用户可以接自定义 MCP。外围是技能市场、插件市场和专家等扩展生态，并兼容 OpenClaw 生态的 Skill。
---

## 概要

- 连接器有两种实现：MCP + CLI 与 Skill + CLI。内置的以腾讯系为主：QQ 邮箱、腾讯文档、腾讯乐享、腾讯会议、TAPD、腾讯网盘；海外版 10 月加入 Outlook、Gmail。用户可以安装自定义 MCP。
- 授权规则：每个连接器单独授权，不主动定时抓取，不超出用户已有权限；凭据由 WorkBuddy 保管以便代为调用。只有连接器明确返回授权失效时才提示重新连接，重连后同一步只自动重试一次。
- 项目里分公共授权（管理员配一次、全员共用）和个人授权（票据只存在成员本地）；协作任务中只能用公共授权。
- 连接器之外是技能（Skill）市场、插件市场、专家和行业 Buddy 应用，兼容 Vercel、OpenClaw 生态的 Skill，企业可以自建市场。
- 支付走微信支付内置插件，在对话里直接发起 AI 支付。

## 两种实现、以腾讯服务为主

帮助中心写明，连接器授权后访问和操作第三方服务，实现分「MCP + CLI（标准化协议）」和「Skill + CLI（内置脚本）」两种，数据收集与权限边界的原则一致（[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})）。当前支持 QQ 邮箱、腾讯文档、腾讯乐享、腾讯会议、TAPD、腾讯网盘，并支持安装自定义 MCP 服务（[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})）。

更新日志中连接器的增加顺序（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）：

| 版本（日期） | 连接器或集成 |
| --- | --- |
| 4.6.0（03-19） | MCP 服务集成面板、插件市场 |
| 4.7.2（03-27） | QQ 邮箱 |
| 4.7.3（03-28） | MCP 标准 OAuth 授权；连接器独立为菜单项 |
| 4.21.0（04-28） | 腾讯文档资料库；产物一键上传腾讯文档 |
| 5.1.1（06-14） | 微信支付内置插件 |
| 5.3.3（07-21） | 腾讯文档深度集成（含 MCP 本地服务） |
| 5.5.0、5.5.5（09） | 微信聊天记录经系统分享发给 WorkBuddy；企业微信转发的聊天记录中的文档、日程、会议纪要可自动读取 |
| 5.6.0（09-19） | 恢复直接编辑 `mcp.json`；「应用管理」可一键撤销第三方授权 |
| 5.7.5、5.7.6（10-03、10-04） | Outlook、Gmail（海外版） |

腾讯官网面向国际用户的文章则称，WorkBuddy 通过内置连接器或 MCP 访问共享盘、团队笔记和消息，支持的服务「包括 Canva、GitHub、Morningstar、Notion 等」（[腾讯官网文章]({{< relref "/docs/workbuddy/sources/official/2026-10-12-tencent-six-apps" >}})）。这份清单与国内帮助中心的清单没有重合。

## 授权粒度与失效处理

权限边界（[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})）：

- 每个连接器独立授权，不主动定时抓取，不超出用户已有权限；自定义连接器的访问范围由用户配置决定。
- 收集 OAuth Access/Refresh Token 或用户手填的 API 密钥，「凭据由 WorkBuddy 维护以便代您调用」。
- 连接器自身的读写不消耗积分，对外部数据的理解和汇总才消耗。

以 QQ 邮箱为例，扫码授权后申请的权限是账号信息、读取收件箱近一个月的邮件、发送邮件，以及可选的删除邮件（移入「已删除」）（[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})）。

使用中有三种接入方式：从连接器页「去对话」、创建任务时启用、执行中按需连接（输入框上方出现引导卡片，授权后自动继续）。授权失效时，只有连接器明确返回授权失效才弹出「连接器需要重新连接」；重连后自动重试失败那一步，同一步只重试一次；网络超时、服务异常、无权限不提示重连（[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})）。日志中相关修复包括 5.9.x 修复「连接器 Token 失效无修复入口」、无效 Key 误提示已连接，5.6.0 优化 MCP 探活、网络恢复后自动重连（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

## 项目里的公共授权与个人授权

项目连接器有两种授权（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})）：

| 方式 | 做法 | 可见性 |
| --- | --- | --- |
| 公共授权 | 管理员配置一次，全员共用同一套票据 | 调用日志只有管理员可见 |
| 个人授权 | 成员各自授权，票据不共享 | 只保存在成员本地 |

协作任务中只能用公共授权，个人授权的连接器全部禁用；同一连接器（如飞书）可以两种方式并存（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})）。

## 技能、插件、专家：扩展生态

技能封装脚本与工作流，能发邮件、订外卖、查股价、读写文件、调第三方 API。技能市场按推荐、SkillHub、套件分类，显示使用量与安装量；可以在对话里搜索安装、上传技能包，或让 WorkBuddy 创建技能（[帮助：技能]({{< relref "/docs/workbuddy/sources/official/2026-10-16-help-skills" >}})）。技能开关多端同步，关闭不等于卸载（[帮助：技能]({{< relref "/docs/workbuddy/sources/official/2026-10-16-help-skills" >}})）。

更新日志中的生态建设（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）：4.5.12、4.6.1 兼容 Vercel、OpenClaw 生态安装 Skill；4.6.2 接入 SkillHub 市场；4.7.5 安装前自动做安全扫描；5.0.0 支持企业自建 Skill 与插件市场；5.5.0 推出行业 Buddy 应用（专属首页、专家、技能、连接器）；5.7.0 开发者可分享已公开发布的专家、应用、技能；5.8.0 优化「千级技能管理」。

推断：WorkBuddy 的扩展面主要靠技能和 MCP，而不是官方逐个对接的连接器。官方连接器几乎都是腾讯自家服务，第三方服务要靠用户或开发者通过 MCP、Skill 接入。

## 支付与本地生活

5.1.1（06-14）新增微信支付内置插件，「在对话中直接发起 AI 支付」完成下单；5.5.2 修复美团助手下单时未展示微信 AI 支付确认（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。资料没有说明美团助手是连接器、技能还是插件，也没有说明支付的限额与确认流程细节。

## 企业微信深度融合

10 月 14 日 WorkBuddy 宣布与企业微信深度融合。据数智奔流转述 10 月 15 日的官方直播：消息、文件、会议、邮件、日程、通讯录可以直接交给 AI 处理，其中消息能力「是新开放的」，与此前用连接器接入企业微信的方式不同；成员访问消息、邮件、文档的权限可以分级管控；企业控制台可以上传企业私有技能和 MCP 连接器，把内部系统接进来（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。

## 第三方的看法

阿言er 把 WorkBuddy 和千问办公列为把文件、通信、工作流接进既有入口的办公向产品，并提醒「装了技能，也不等于扩大了权限」（[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。黑咖啡全景解读认为国内产品的关键问题是生态围墙，缺少真实连接器和操作权限就难把事情办完（[黑咖啡全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})），该判断泛指国内产品，未特指 WorkBuddy。

## 资料缺口

- 国际版的连接器清单（Canva、GitHub、Morningstar、Notion 的出处与上线时间）。
- 微信支付插件的支付限额、确认流程；美团助手的形态。
- 连接器和技能的数量；第三方开发者上架的审核规则。
- 微信（非企业微信）本身能否作为数据源被读取。

## 主要资料

- 官方：[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})（连接器机制、授权与失效）、[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})（公共与个人授权）、[帮助：技能]({{< relref "/docs/workbuddy/sources/official/2026-10-16-help-skills" >}})（技能市场）、[腾讯官网文章]({{< relref "/docs/workbuddy/sources/official/2026-10-12-tencent-six-apps" >}})（国际版服务清单）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（连接器与生态的时间线）
- 社区：[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})（企业微信深度融合）、[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})、[黑咖啡全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})
