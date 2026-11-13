---
title: "Today AI：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Today 的安全设计以「对外动作一律先确认」为核心：发送、改日历、付款等由用户最终确认，Shell 脚本每次运行需批准，Chrome 插件可指定做到哪一步。资料中没有提示注入防护、独立审查模型、凭证存放方式或安全事件的信息。
---

## 概要

- 官方反复强调「主动不等于自主」：没有用户明确确认，不发邮件、不挪日历、不给任何人发消息；人始终是批准关卡。品玩实测中邮件在作者回复「确认」后才发出。
- 设备端权限逐项授予、可撤销：Computer Control 在用户批准动作时才点击输入，Shell 脚本每次运行都需批准。
- Chrome 插件可指定任务做到哪一步为止（如先不提交）；插件保存连接浏览器所需的登录和连接信息；断开不会自动删除已发送的数据。
- 能力页承认外部操作「不一定都能撤销」，任务状态区分草稿、待确认、已完成。
- 截至 2026-11-10 的资料，没有 Today 的提示注入防护、独立审查模型、凭证管理、漏洞或安全事件的信息。

## 对外动作先确认

官方博客称没有用户的明确确认，Today 不会发邮件、不会挪动日历事件、不会给任何人发消息；Today 不适合想要「完全自主、没有确认步骤」的用户（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）。官方定义文称个人智能体的循环是察觉、检索、提议、等确认、执行，不可逆的事在确认前一概不发生（[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})）。团队自述称授权访问不等于授权替用户做所有决定，日程调整需要确认，支付和重要决定的最终确认权在用户（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。

能力页的说法：外部操作和敏感变更可能需要确认，也不一定都能撤销；任务状态区分草稿、待确认、已完成；不同连接器、地区和账户的确认方式可能不同（[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})）。

品玩实测与官方描述一致：Today 起草邀约邮件，作者回复「确认」后邮件才发出（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。

## 设备与浏览器的权限

集成页称设备权限由用户授予并可撤销；Computer Control 只在用户批准动作时点击和输入；Shell & Scripts「每次运行都需要批准」（[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})）。

中国版 Chrome 插件允许用户指定任务做到哪一步为止；插件保存连接浏览器所需的登录和连接信息；用户可在插件里退出登录，或在 Chrome 中停用、移除插件来断开，断开不会自动删除已发送的数据（[Chrome 插件（中国版）]({{< relref "/docs/today/sources/official/2026-10-15-chrome-extension-china" >}})）。插件让 Today 在用户已登录的网站里操作，但资料没有说明对恶意网页或提示注入的防护。

## 执行中的误判

极客公园记录了一次误判：mod 汉化完成后，Today 在安装步骤上给出多条「说得很笃定」但无效的指令，作者反复重启游戏测试了一小时，直到让它查官方文档才解决；作者认为它分不清轻重缓急，权限越接近真实操作越关键（[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})）。这不是安全事件，但说明在本机执行时错误指令的成本由用户承担。

## 评测框架中的信任维度

官方评测框架设有权限与隐私（授权粒度、撤回是否干净）、透明度（事后能否追溯是哪条记忆、规则、权限产生了某封邮件）等维度，用「一位拿了钥匙的住家客人」作比喻（[官方评测框架]({{< relref "/docs/today/sources/official/2026-09-20-today-assistant-benchmark" >}})）。框架发布时未打分。

## 资料缺口

- 提示注入、恶意网页的防护；是否有独立审查模型。
- 凭证管理：邮箱、浏览器登录状态在云端如何保存，智能体能否看到。
- 确认机制的实现细节：哪些动作可以预先授权自动运行（能力页提到「部分预先授权」）。
- 漏洞赏金、外部审计、安全事件及厂商回应。

## 主要资料

- 官方：[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})（确认原则）；[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})（不可撤销、任务状态）；[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})（设备权限）；[Chrome 插件（中国版）]({{< relref "/docs/today/sources/official/2026-10-15-chrome-extension-china" >}})；[官方评测框架]({{< relref "/docs/today/sources/official/2026-09-20-today-assistant-benchmark" >}})。
- 媒体：[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})；[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})（确认后发送）；[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})（执行误判）。
