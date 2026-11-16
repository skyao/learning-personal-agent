---
title: "实地核查：Shopify 店铺的 poppy.json 实际是 0.4 版"
linkTitle: "Poppy 文件实地核查"
date: 2026-11-14
originalTitle: "Yesterday Shopify published a file on your store that tells AI agents what they may do. We read it on nine storefronts. It is version 0.4, it grants one permission, and it answers the question we told you to decide in October."
sourceUrl: "https://jtstechservices.ca/blog/your-store-already-has-a-poppy-file"
author: "Jeremy Souffir"
publisher: "JTS Tech Services"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-15
tags: [连接器, 安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载全文。删去了文末的自我推广一节与装饰题图，两张说明图已本地化；原文的 Sources 清单保留在 original.md 末尾。文中「同一天，柜台另一边」一节涉及 OpenAI 的 ChatGPT Wallet（dots 产品），照录原文。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：2026 年 11 月 13 日 Sierra 发布 Personal Agent Protocol 1.0，Shopify 称已为平台全部商家自动启用 Poppy 文件，Meta 的 Muse 访问网站时会优先读取该文件；作者同日检查了 11 家 Shopify 店铺，其中 9 家返回了该文件。9 份文件除品牌名外内容完全相同：protocol_version 为 0.4 而非 1.0；仅授予一个权限 dev.ucp.shopping.checkout:manage，即以登录顾客身份准备结账、由买家完成付款，并标记为 changes: irreversible、personal_data: true；文件指向 /.well-known/ucp 的 UCP 清单（版本 2026-08-25），web 段为空，且不含订单读取、地址、退货、账户等权限。11 家中有 2 家在一台主机名上返回 404、另一台主机名上返回文件，裸域名与 www 主机名各有一例。作者指出，文件未提供查订单、改地址、发起退货等顾客最常需要的操作路径，且空白的 web 段并未禁止智能体用顾客密码登录普通网站这一兜底做法。

**保留理由**：此前已收资料只有 Sierra 的 1.0 发布公告与 Muse 官方稿，本篇是独立实地核查：11 家店铺中 9 家实际返回文件、文件均为 0.4 版、仅一个权限、web 段为空、2 家店铺主机名不一致，并指出密码登录兜底未被文件堵住——这些实测细节是公告稿中没有的。
