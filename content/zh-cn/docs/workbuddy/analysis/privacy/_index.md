---
title: "WorkBuddy：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 的隐私说明散在各功能页：记忆仅本人可见、不与第三方共享；自定义模型与本地模型可让数据不经 WorkBuddy 或不出本机。是否用于训练、保存多久、能否导出，资料都没有回答。
---

## 概要

- 记忆默认开启，官方称仅本人可见、不涉及第三方共享、只用于个性化服务；关闭或删除后停止用于后续对话，但已生成的输出不追溯撤回。
- 数据流向因功能而异：内置模型经 WorkBuddy；自定义模型的内容直达第三方，WorkBuddy 称除必要情形外不读取、不存储；本地 Ollama 模型则不出本机。
- 每个功能页都列了收集项（邮箱、定时任务、连接器），并写明调用外部模型、MCP、连接器、通知通道时「发生数据共享」。
- 涉及他人信息时，官方把责任交给用户：提交前须确认已获授权。
- 资料中没有训练用途、保存期限、导出与账号删除的说明；数据管理页只有分享链接和归档任务的管理。

## 记忆数据

记忆页写明（[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})）：记忆默认开启，仅用户本人可见，遵循隐私政策，「记忆功能不涉及第三方共享」，数据只用于产品内部的个性化服务；提取由 WorkBuddy 自费完成。关闭记忆后停止提取新记忆；关闭或删除条目后，相应数据停止用于后续对话，但「已生成的输出不会因此追溯撤回」（[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})）。页面没有说明已提取的数据是否从服务器删除。机制见[记忆与上下文]({{< relref "/docs/workbuddy/analysis/memory" >}})。

## 数据经过谁：内置、自定义、本地模型

- **自定义模型**：API Key 只存本地；输入直达第三方模型，按用户与第三方的协议处理；WorkBuddy 除完成请求、必要传输、安全审计、故障排查、依法留存外「不读取、不存储相关内容」。接入存在违法违规风险时，WorkBuddy 可依用户协议中止或限制该模型（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。
- **本地模型**：Ollama 让「代码与对话内容不出本机」，官方称适合金融、政企、敏感项目（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。
- **产物**：4.7.5 起有产物回传开关，可以控制是否把产物回传到云端（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

内置模型的数据如何处理、是否用于训练，资料没有说明。

## 各功能的收集项

| 功能 | 收集什么 | 资料 |
| --- | --- | --- |
| 我的邮箱 | 必要：邮箱地址、手机号；非必要：邮件正文与附件、收件人地址、邮箱别名；邮件数据由 WorkBuddy 维护，用于代为处理 | [帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}}) |
| 定时任务 | 账户身份、任务提示词与规则、使用行为日志（创建、启停、触发、结果与耗时）；调用外部模型、MCP、连接器、OAuth 平台或通知通道时发生数据共享 | [帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}}) |
| 连接器 | 第三方账号标识、授权凭据、按需读取的第三方业务数据 | [帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}}) |

邮箱数据绑定账号实例，个人版与企业版相互隔离（[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})）。项目中转交任务时，原任务的完整对话、调用记录和中间产物会复制给接收方（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})）。

## 他人的信息

记忆页要求，会话中涉及他人个人信息时，用户「请在提交前确认已获得相关授权」（[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})）。资料没有说明 WorkBuddy 在企业微信群、转发的聊天记录中如何处理群成员和联系人的信息。阿言er 的通用建议是，接入飞书或微信前，先要解释谁能看到资料（[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。

## 删除与管理

数据管理页（[帮助：数据管理]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-data" >}})）只有两项：「我分享的文件」可复制链接、下载、取消分享，取消后他人无法再通过链接访问；「已归档任务」可删除（删除后不可查看和继续对话）或取消归档。各功能页的声明区写明这些说明是服务协议和隐私保护指引的组成部分，与协议原文不一致时以原文为准（[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})）。

## 资料缺口

- WorkBuddy 隐私政策与服务协议原文。
- 对话、文件、记忆是否用于模型训练，默认设置与退出方式。
- 各类数据的保存期限；导出与注销账号。
- 企业微信、群聊场景中第三方成员信息的处理；企业版的数据归属。
- 海外版的数据存储地区与适用法规。

## 主要资料

- 官方：[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})（记忆数据）、[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})（自定义与本地模型的数据流向）、[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})、[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})、[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})（收集项）、[帮助：数据管理]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-data" >}})（数据管理）、[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})（转交）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（产物回传开关）
- 社区：[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})
