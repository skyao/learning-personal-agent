---
title: "Today AI：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  官方称连接数据不用于训练模型，记忆可查看、修改、删除；团队称删除后底层数据库「完全不会保留」。中国服务由国内主体单独运营，账号、插件与国际服务分开。有第三方称 Today 索要大量权限、扫描本地磁盘，但没有出处。隐私政策原文与数据保存期限不在资料库中。
---

## 概要

- 官方集成页称连接数据只用于回答用户和构建其记忆，不用于训练模型；断开某来源即移除访问权限。
- 记忆可查看、修改、删除；团队自述称删除后底层数据库「完全不会保留」，并采用渐进式授权。能力页的措辞更保守，限定在「产品支持的范围内」。
- 中国服务由汇翮（上海）智能科技有限公司运营，适用中国区协议与隐私政策；国内外服务、插件、账号会话分开，开发者主体为 TODAY AI PTE. LTD.。
- Chrome 插件会把网页内容、截图、网址及浏览历史、书签查询结果发给 Today 中国服务处理；登录诊断经脱敏发送给 Sentry。
- Datawhale 与鸿煊两篇综述称 Today 索要大量权限、扫描本地磁盘并受到海外用户批评，均无出处。录音中对方的同意、声纹数据处理等问题资料未涉及。

## 训练与数据用途

集成页常见问题称 Today 不会用连接数据训练模型，连接数据只用于回答用户和构建其记忆（[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})）。官方博客称健康数据只做生活方式支持、不做医疗诊断，推理服务提供商的数据处理见 Privacy 页（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）。资料库没有收录 Privacy 页本身，对话内容是否用于训练、默认设置如何，资料中没有直接说明。

## 记忆的查看与删除

团队自述：记忆库对用户完全可见，可随时删除，「删除之后底层数据库完全不会保留」；采用渐进式授权，需要某信息时才请求权限；内测中授权比例「相当高」，但用户偏早期尝鲜者，不代表大众（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。官方定义文称黑箱式用户画像过不了信任这一关（[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})）。能力页则写「在产品支持的范围内查看、修正或删除相关记忆」（[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})）。

## 国内外服务分开

中国版 Chrome 插件页说明：中国服务由汇翮（上海）智能科技有限公司运营，适用中国区服务协议和隐私政策；国内外服务、插件、账号会话分开，插件不能切换为国际服务；登录需中国大陆手机号（[Chrome 插件（中国版）]({{< relref "/docs/today/sources/official/2026-10-15-chrome-extension-china" >}})）。

同页披露的数据处理：浏览器任务可能把网页内容、截图、网址及浏览历史或书签的查询结果发送给 Today 中国服务处理；向 Sentry 发送脱敏的登录诊断（版本、流程阶段、耗时、错误分类，不含账号、网页内容、网址或令牌）；商店页声明处理个人身份、身份验证、网络记录、用户活动和网站内容，不出售给第三方，不用于与核心功能无关的目的，不用于信用判断（[Chrome 插件（中国版）]({{< relref "/docs/today/sources/official/2026-10-15-chrome-extension-china" >}})）。

团队称国内连接器生态不如美国成熟，还需额外考虑隐私合规（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。

## 权限范围的争议

Datawhale 刊发的阿里云专家综述称 Today 登录后会扫描本地磁盘以实现「非常了解你」，因索要大量权限而「遭到了海外部分用户的批评」（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）；鸿煊综述有相同说法（[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。两篇都没有注明出处，资料库中没有对应的用户反馈或官方回应。集成页显示 macOS 客户端确实可申请屏幕录制、辅助功能、桌面与下载文件夹等权限，但都标明由用户授予（[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})）。

## 第三方与录音

Today Recording 每次录音须用户亲手点击，会前提醒不会自动录音；声纹识别在内部测试（[官方：Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})）。资料没有说明会议中其他参与者的知情同意、声纹数据的处理，以及邮件、通讯录中他人信息的处理方式。

## 资料缺口

- 国际版与中国区隐私政策原文；数据保存期限、导出与账号删除流程。
- 对话内容是否用于训练、默认设置与退出方式。
- 「扫描本地磁盘」说法的一手出处与官方回应。
- 录音中第三方的同意、声纹数据处理。

## 主要资料

- 官方：[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})（不用于训练、设备权限）；[Chrome 插件（中国版）]({{< relref "/docs/today/sources/official/2026-10-15-chrome-extension-china" >}})（运营主体、数据处理）；[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})；[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})；[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})；[Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})。
- 媒体：[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})（删除、渐进授权、合规）。
- 社区：[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})（权限争议，无出处）。
