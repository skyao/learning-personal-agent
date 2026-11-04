---
title: "not-a-mused：Muse macOS 本地漏洞概念验证"
linkTitle: "Wardle：not-a-mused"
date: 2026-09-21
originalTitle: "not-a-mused"
sourceUrl: "https://github.com/pwardle/not-a-mused"
author: "Patrick Wardle"
publisher: "GitHub（pwardle）"
language: en
fidelity: 全文翻译
collectedAt: 2026-11-04
dateNote: "日期取仓库创建时间（GitHub API created_at，2026-09-21T14:04:11Z）；本页为仓库 README.md 的全文翻译，代码未收入"
tags: [安全, 设备]
products: [muse]
---

{{< source-info >}}

一个针对 Muse（https://muse.ai）本地 0day 漏洞的概念验证（proof-of-concept），该漏洞可以让一个非特权的本地进程重定向 Muse 的听写流量，并滥用该应用被授予的信任和访问权限。

## 它展示了什么

Muse 暴露了一个未公开文档的设置：

`endo_voyager_dictation_endpoint`

本地攻击者或恶意软件可以在没有特殊权限的情况下修改这个端点。

一旦被重定向，听写的提示就可能被发送到攻击者控制的端点，从而可能导致：

* 截获听写的音频或提示
* 向 Muse 注入提示
* 窃取 Muse 的认证材料
* 滥用用户授予 Muse 的任何访问权限

简而言之：Muse 的访问权限有可能变成攻击者的访问权限。

## 用法

运行：

```bash
./not-a-mused -h
```

查看可用选项。

这个概念验证实现了 Muse 暴露的 50 多个命令中的一部分。

运行后，点击 Muse 中的麦克风按钮并口述一条提示，即可触发这个概念验证。

## 说明

这是一个**本地攻击**。攻击者必须已经能够以本地用户的身份执行代码。

令人担忧的是，Muse 拥有的访问权限可能比普通的本地恶意软件广泛得多，这使它成为获取权限或扩大访问的一个特别有用的目标。

## 免责声明

仅用于安全研究和教育目的。
