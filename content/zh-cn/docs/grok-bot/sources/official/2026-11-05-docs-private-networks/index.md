---
title: "文档：连接私有网络"
linkTitle: "文档：私有网络"
date: 2026-11-05
originalTitle: "Connect to private networks"
sourceUrl: "https://cursor.com/docs/grok-bot/private-networks"
altUrls: ["https://docs.x.ai/grok-bot/private-networks"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Grok Bot 计算机运行在 Cursor 云端，通过共享的静态出口 IP 访问互联网，不提供每客户专用 IP。需要访问私有网络时有两种办法：把单个成员的流量经其桌面转出，使目标站点看到该设备的 IP（私有或 VPN 地址的站点仍默认被阻止）；或者用 Team Setup Scripts 在每台团队计算机上安装组织自己的网络客户端。后者仅限 Enterprise，脚本以计算机用户身份运行，计算机启动时和大约每天一次刷新时执行，单个脚本超时 30 分钟，凭据应存为 Team Secret 而不是写进脚本。文中以 Tailscale 作为已验证的配置（经内部出口节点），Cloudflare Tunnel 作为对比；Cursor 不安装、运营或监控这个客户端，也没有脚本结果的整体视图。网络策略是单独一层，仍然适用。

**保留理由**：说明托管计算机怎样接入企业内网、哪些由 Cursor 负责哪些由客户自己负责，对评估私有部署场景的限制有用。

---

Grok Bot 计算机运行在 Cursor 云端，并通过[共享的静态出口 IP 地址](https://cursor.com/docs/grok-bot/security#static-egress-ips)访问互联网。如果你的 Bot 需要访问的系统位于私有网络中，可以通过某个成员的桌面转出流量，或通过 **Team Setup Scripts** 在每台团队计算机上安装组织的网络客户端。

**Team Setup Scripts** 仅限 Enterprise。它不会出现在其他套餐中。
**Network Controls 也仅限 Enterprise。** 该[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)是一个仍然适用的独立层；能够访问私有网络并不能替代你的目标允许列表（allowlist）。

## 你可以做什么

- **让一个成员的流量经其桌面转出**，使目标站点看到该设备的 IP 地址。解析到私有地址或 VPN 地址的站点仍会被阻止，除非已为你的组织允许。
- **自动在每台团队计算机上安装你的网络客户端**，只需一份由管理员管理的清单（manifest），无需逐台计算机设置。
- **让 Bot 访问你私有网络中的服务**，而无需把这些服务暴露到互联网，也无需把共享出口 IP 加入你的允许列表。
- **把控制权留在你这一侧。** 你的网络、你的访问规则、你的身份提供商。你可以随时从自己的管理控制台撤销一台计算机。

## 选择连接方式

| 方法 | 何时使用 |
| --- | --- |
| 通过桌面转出流量 | 某个成员需要公共站点看到其设备的 IP 地址，例如允许办公室 IP 的站点 |
| 通过 Team Setup 安装网络客户端 | 你的 Enterprise 团队需要在每台托管计算机上保持一致的连接 |

### 通过成员的桌面转出

在 Grok Bot 桌面应用中，打开 **Settings** > **Computer**，并在 **Your computer** 下开启 **Route traffic through this computer**。该路由使用当前设备的网络和 IP 地址。当该设置关闭，或 Enterprise 管理员禁用 **Allow Local Egress Routing** 时，它就会停止。

该路由不会向 Bot 开放你的私有网络。解析到私有地址或 VPN 地址的站点会被阻止，除非已为你的组织允许；该设置会显示本次会话中有多少站点被阻止。要访问私有服务，请[通过 Team Setup 安装网络客户端](#install-a-networking-client-with-team-setup)。

每个成员控制自己的桌面路由。Enterprise 管理员可以从 [Cursor 仪表盘中的 Grok Bot](https://cursor.com/dashboard/bot)为整个团队移除此选项。参见[通过你的桌面转出流量](https://cursor.com/docs/grok-bot/settings#route-traffic-through-your-desktop)。

### 通过 Team Setup 安装网络客户端

这是由你运行的一种模式，而不是 Cursor 管理的网络模式。Cursor 提供挂钩：Team Setup Scripts 在每台团队计算机上运行你的安装脚本。其余部分由你负责：安装客户端、配置它、对计算机进行身份验证、维护访问规则，以及跟进供应商的变更。Cursor 默认不安装任何东西，不运营也不监控你的网络客户端，仪表盘也不显示客户端状态。供应商的文档是安装和配置其软件的权威依据；本页只涵盖 Cursor 这一侧。

## 开始之前

- 你是 Enterprise 套餐的团队管理员。**Team Setup Scripts** 仅限 Enterprise，不会出现在其他套餐中。
- 你的网络客户端运行在基于 Debian 的 Linux 上，并且可以从 shell 脚本安装和启动。团队计算机运行 Linux，脚本以计算机用户身份运行，并可使用 `sudo`。
- 你的网络为该客户端提供了入口：按照供应商的架构，在你想要访问的 VPC 或内网中有一个网关、出口节点（exit node）或隧道连接器（tunnel connector）。
- 你已经决定计算机如何向你的网络进行身份验证。不要把凭据放进安装脚本；如果脚本需要凭据，请将其存为 [Team Secret](https://cursor.com/docs/grok-bot/teams#team-secrets)。

## Team Setup 如何运行你的脚本

**Team Setup Scripts** 位于 [Cursor 仪表盘](https://cursor.com/dashboard/bot)的 **Grok Bot** 页面下、**Bot Computers** 中：它是安装脚本的清单（manifest），这些脚本在每台团队计算机上运行。每份清单包含一个或多个脚本条目，每个条目有一个 **ID**、一个 **Setup Script** 和一个可选的 **Check Script**。若只想在一组（cohort）计算机上运行某份清单，请改为将其添加到该组的 Grok Bot 标签页下；参见[组设置](https://cursor.com/docs/grok-bot/teams#group-settings)。组清单遵循与下面相同的规则。

- 脚本在每台团队计算机上以**计算机用户**身份运行；特权安装请使用 `sudo`。
- 它们在计算机启动时运行，并在计算机运行期间按周期性刷新运行，大约每天一次。
- 如果存在 Check Script 且其退出码为 0，则跳过 Setup Script；用它来避免每次执行都重新安装。安装脚本运行后，检查脚本会再次运行以验证其成功。
- 条目按顺序一次运行一个。每个脚本有 30 分钟超时。失败的脚本不会阻塞计算机；它会在之后的刷新中重试。
- 脚本以环境变量形式读取你团队的 [Team Secrets](https://cursor.com/docs/grok-bot/teams#team-secrets)，因此脚本所需的凭据绝不会出现在清单中。机密仅在脚本运行期间存在，脚本输出在记录日志前会被脱敏。设置来自多个团队的计算机不会收到任何机密。

## 创建清单

1

### 打开 Team Setup Scripts

前往 [Cursor 仪表盘中的 Grok Bot](https://cursor.com/dashboard/bot)，在 **Bot Computers** 下找到 **Team Setup Scripts**。

2

### 创建清单

在 **Manifests** 旁边，选择 **+** 创建一份 **New Manifest**，然后输入 **Manifest ID**，例如 `private-network`。

3

### 编写安装脚本

在脚本条目中，设置 **ID**（例如 `install-network-client`）并编写 **Setup Script**：按照你的提供商 Linux 安装文档安装客户端，然后启动它，并按你的配置规定将其连接到你的网络。

4

### 添加检查脚本

可选地添加一个 **Check Script**（例如 `command -v <your-client>`），以便已经安装了客户端的计算机跳过安装。

5

### 保存

选择 **Save**。

更喜欢编辑 JSON？在编辑器顶部从 **Form** 切换到 **JSON**。清单结构：

```
{  "manifestId": "private-network",  "entries": [    {      "id": "install-network-client",      "setup": "#!/usr/bin/env bash\nset -euo pipefail\n# 1) Install your networking client per your provider's Linux install docs\n# 2) Start the client and connect it to your network per your configuration",      "check": "command -v <your-client>"    }  ]}
```

不要把机密值粘贴到脚本中。安装脚本以计算机用户身份在每台团队计算机上运行，而清单是应用于你整个机群的纯文本。如果脚本需要认证密钥、token 或其他凭据，请将其存为 [Team Secret](https://cursor.com/docs/grok-bot/teams#team-secrets)，并从环境变量读取，例如 `"$MY_AUTH_KEY"`。在供应商支持的情况下，优先让成员在计算机的浏览器中以交互方式完成身份验证，因为在那里你的身份提供商策略会生效。

## 设置你的网络客户端

无论你使用哪种工具，最后一公里都是一样的：每台计算机向你的网络进行身份验证，你在供应商的控制台中确认连接，然后让一个 Bot 访问它之前无法访问的内部主机名来验证。交互式登录在计算机的浏览器中进行，就像成员已经[在那里登录公司工具](https://cursor.com/docs/grok-bot/identity)一样。在向整个团队推广之前，先在一两台试点计算机上开始。

在每台计算机上运行 Tailscale，并通过你网络内部的[出口节点](https://tailscale.com/docs/features/exit-nodes)转出流量。这是该模式已经实践过的配置。Tailscale 还提供[子网路由器](https://tailscale.com/docs/features/subnet-routers)，用于暴露特定的私有地址范围；在依赖它之前，请先在试点计算机上验证这种安排。

**开始之前：** 你运营着一个 tailnet，并且在你想要访问的 VPC 或内网中有一个出口节点。

**Team Setup 清单：**

- **Setup Script：** 按照 [Tailscale 的安装文档](https://tailscale.com/docs/install/linux)安装 Linux 版 Tailscale，然后按你的配置把计算机接入你的 tailnet。
- **Check Script：** `command -v tailscale`。

**连接并验证：**

1. 对每台计算机进行身份验证。Tailscale 会打印一个登录 URL，在计算机的浏览器中打开，你的身份提供商策略会在那里生效。如果你不想让成员登录来加入计算机，可以把可复用、带标签的[认证密钥](https://tailscale.com/docs/concepts/auth-keys)存为 [Team Secret](https://cursor.com/docs/grok-bot/teams#team-secrets)，并从环境变量传入，例如 `tailscale up --auth-key "$TS_AUTHKEY"`。这样每台团队计算机就都以相同的密钥和标签加入，而不是以成员身份加入，因此请相应地限定该密钥的 ACL 范围。绝不要把密钥粘贴到脚本本身中。
2. 确认该计算机出现在你的 Tailscale 管理控制台中，并获准使用出口节点。
3. 让一个 Bot 访问某个内部主机名。

**如果不起作用：**

- 客户端已安装，但没有人完成身份验证。使用浏览器登录时，这一步是手动的；使用认证密钥时，请检查 Team Secret 是否存在、其名称是否与脚本读取的一致，以及密钥是否未过期。检查 Tailscale 管理控制台中的机器列表。
- 你团队的网络策略是仅允许列表（allowlist-only），并且阻止了 Tailscale 的协调服务器或中继。请从 Tailscale 的文档中允许相应端点。运行中的计算机大约在一分钟内应用更改。休眠中的计算机在下次唤醒时应用。
- 出口节点未在你的 tailnet 中通告或批准。请检查管理控制台中的路由设置。
- 计算机被重新创建，例如在镜像更新或重置之后，而会话没有保留下来。请重新进行身份验证。

在两者之间选择：Tailscale 为计算机提供网络层面的访问能力，并且借助出口节点，可以从你的网络转出。Cloudflare Tunnel 通过 Cloudflare 位于 Access 之后的边缘节点发布特定服务：是按服务而非整个网络，其他服务看到的出口地址不会改变。

其他能在基于 Debian 的 Linux 上安装并运行的客户端遵循相同的 Team Setup 步骤；在推广之前，请先在试点计算机上验证你的客户端。

## 推广到现有计算机

- **新计算机**在启动时应用清单。
- **运行中的计算机**在周期性刷新时获取清单更改，大约每天一次。
- **要立即应用清单更改，**请重新创建计算机，或让成员从桌面应用中重置它。在 Enterprise 上，管理员可以从仪表盘重新创建或终止成员的计算机。持久磁盘会被保留，下一台计算机在启动时会应用当前清单。
- **镜像更新**会自动重新创建计算机，你的脚本会重新应用。计算机被重新创建后，登录会话（包括网络客户端的登录）可能需要重新建立。

## 配合网络策略工作

Grok Bot 的[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)是一个独立的层，控制团队计算机可以访问哪些目标。如果你的团队使用 **Team allowlist only**，请根据供应商文档添加你的网络客户端所需的目标，例如协调服务器、中继和网关。运行中的计算机大约在一分钟内应用策略更改。休眠中的计算机在下次唤醒时应用。你不需要重新创建计算机。

## 限制

- 这是由你运营的一种模式，而不是 Cursor 管理的网络模式。Cursor 不安装、不运营也不监控你的网络客户端，客户端本身的支持来自你的供应商。
- 常规互联网流量仍通过 Cursor 的共享静态 IP 范围出口，除非你让它经自己的网络转出。不提供每客户专用的出口 IP。
- 目前没有脚本结果的机群视图。在向整个团队推广之前，请先验证一台试点计算机。
- 这不是 Cloud Agents 的设置。Cloud Agents 文档针对不同的产品界面有自己的 [Tailscale](https://cursor.com/docs/cloud-agent/setup#running-tailscale) 和 [Cloudflare Tunnel](https://cursor.com/docs/cloud-agent/setup#running-cloudflare-tunnel) 方案；Grok Bot 计算机如本文所述通过 Team Setup 配置。如果 Grok Bot 将工作委派给 Cloud Agents，那些智能体在 Cloud Agent 的网络设置下运行，而不是你计算机的网络客户端。

## 常见问题（FAQ）

### 我可以把认证密钥或凭据放进安装脚本吗？

不能放在脚本文本中。清单是纯文本，仪表盘会警告不要将机密粘贴到其中。请把凭据作为 [Team Secret](https://cursor.com/docs/grok-bot/teams#team-secrets) 存储在 Grok Bot 页面上，并让脚本以环境变量形式读取它。Team Secrets 仅限 Enterprise。在供应商支持的情况下，交互式浏览器登录仍然是最简单的选项，因为你的身份提供商策略会适用于它。

### 我可以使用哪些网络工具？

任何你的团队能在基于 Debian 的 Linux 上通过 shell 脚本安装并运行的客户端。Tailscale 和 Cloudflare Tunnel 是本页的示例。请先在试点计算机上验证你的客户端。

### 现有计算机会获得新清单吗？

会。运行中的计算机会定期刷新清单，大约每天一次。要立即应用清单更改，请重新创建计算机，或让成员从桌面应用中重置它。

### 这会改变我的服务看到的 IP 地址吗？

对于经你的网络转出的流量，会改变。发往你私有网络的流量从你的网络内部到达，经由你的出口节点、网关或隧道连接器。其他所有流量继续从 Cursor 的共享静态范围出口。

### 我们使用严格的网络允许列表。我们的客户端能工作吗？

只有在你允许其端点时才行。请把客户端需要访问的目标添加到团队允许列表。运行中的计算机大约在一分钟内应用更改。休眠中的计算机在下次唤醒时应用。

### 这与 Cloud Agents 文档中的 Tailscale 和 Cloudflare Tunnel 部分相同吗？

不同。那些方案特定于 Cloud Agent 虚拟机；那里的 Tailscale 需要用户空间网络（userspace networking）和代理变量。Grok Bot 计算机如本页所述，使用 Team Setup 以及你自己的网关或连接器。

### 哪些套餐包含 Team Setup Scripts？

**Team Setup Scripts** 仅限 Enterprise。团队管理员管理清单。如果你在仪表盘的 Grok Bot 页面上看不到它，说明你不在 Enterprise 套餐，或者你需要你的客户团队为组织启用 Grok Bot。

### 如果安装脚本在某些计算机上失败会怎样？

计算机仍会启动。失败的条目会在之后的刷新中重试。让脚本可重复运行，并使用 Check Script，以便健康的计算机跳过安装。
