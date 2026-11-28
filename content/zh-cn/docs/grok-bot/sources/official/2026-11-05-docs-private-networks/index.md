---
title: "文档：连接私有网络"
linkTitle: "文档：私有网络"
date: 2026-11-05
originalTitle: "Connect to private networks"
sourceUrl: "https://docs.x.ai/grok-bot/private-networks"
altUrls: ["https://cursor.com/docs/grok-bot/private-networks"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-11
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：Enterprise 管理员对本地出口路由的控制由「关闭 Allow Local Egress Routing」改为 Always on / Always off 两种锁定，Always off 时用户组设置仍可为该组成员放行"
tags: [运行环境, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Grok Bot 计算机运行在 Cursor 云端，通过共享的静态出口 IP 访问互联网，不提供每客户专用 IP。需要访问私有网络时有两种办法：把单个成员的流量经其桌面转出，使目标站点看到该设备的 IP（私有或 VPN 地址的站点仍默认被阻止），Enterprise 管理员可把这项锁为 Always on 或 Always off，Always off 时用户组设置仍可为该组成员放行；或者用 Team Setup Scripts 在每台团队计算机上安装组织自己的网络客户端。后者仅限 Enterprise，脚本以计算机用户身份运行，计算机启动时和大约每天一次刷新时执行，单个脚本超时 30 分钟，凭据应存为 Team Secret 而不是写进脚本。文中以 Tailscale 作为已验证的配置（经内部出口节点），Cloudflare Tunnel 作为对比；Cursor 不安装、运营或监控这个客户端，也没有脚本结果的整体视图。网络策略是单独一层，仍然适用。

**保留理由**：说明托管计算机怎样接入企业内网、哪些由 Cursor 负责哪些由客户自己负责，对评估私有部署场景的限制有用。

---

连接私有网络

Grok Bot 的电脑运行在 Cursor 云端，通过[共享的静态出口 IP 地址](https://docs.x.ai/grok-bot/security#static-egress-ips)访问互联网。如果 Bot 需要的系统位于私有网络，可以把流量经由成员的桌面转出，或通过 **团队设置脚本（Team Setup Scripts）** 在每个团队电脑上安装组织的网络客户端。

> **团队设置脚本仅限 Enterprise。** 它不会出现在其他套餐上。**网络控制（Network Controls）也仅限 Enterprise。** 那条[网络策略](https://docs.x.ai/grok-bot/security#network-policy)是单独的一层，仍然适用；能访问私有网络并不能取代你的目标允许列表。

## 你可以做什么

* 把一个成员的流量经其桌面转出，让目标站点看到该设备的 IP 地址。解析到私有或 VPN 地址的站点仍会被阻止，除非它们已为你的组织放行。
* 从一份管理员维护的清单，自动在每个团队电脑上安装你的网络客户端，无需逐台设置。
* 让 Bot 访问你私有网络上的服务，而不用把这些服务暴露到互联网，也不用把共享出口 IP 加入你的允许列表。
* 控制权留在你这边：你的网络、你的访问规则、你的身份提供方。你可以随时从自己的管理控制台撤销一台电脑。

## 选择连接方式

| 方式 | 适用情形 |
| --- | --- |
| 经桌面转出流量 | 某个成员需要公开站点看到其设备的 IP 地址，例如某站点只把办公 IP 加入允许列表 |
| 用团队设置安装网络客户端 | 你的 Enterprise 团队需要在每台托管电脑上有一致的连接 |

### 经成员的桌面转出

在 Grok Bot 桌面应用中，打开 **设置 → 电脑**，在 **你的电脑** 下开启 **经这台电脑转出流量（Route traffic through this computer）**。这条路径使用当前设备的网络和 IP 地址。关闭该设置，或 Enterprise 管理员把本地出口路由设为 **始终关闭（Always off）** 时，它就会停止。[组设置](https://docs.x.ai/grok-bot/teams-and-enterprises#group-settings)仍可为该组的成员放行这条路径。

这条路径不会把你的私有网络向 Bot 打开。解析到私有或 VPN 地址的站点会被阻止，除非它们已为你的组织放行；该设置会显示本次会话中阻止了多少个站点。要访问私有服务，[用团队设置安装网络客户端](#install-a-networking-client-with-team-setup)。

每位成员控制自己的桌面路径。Enterprise 管理员可以从 [Cursor 仪表盘中的 Grok Bot](https://cursor.com/dashboard/bot) 用 **始终开启（Always on）** 或 **始终关闭** 为整个团队锁定它。见[经你的桌面转出流量](https://docs.x.ai/grok-bot/settings-and-notifications#route-traffic-through-your-desktop)。

### 用团队设置安装网络客户端

这是由你运行的一种做法，不是 Cursor 托管的网络模式。Cursor 提供的是挂接点：团队设置脚本会在每台团队电脑上运行你的安装脚本。其余由你负责：安装客户端、配置它、让电脑通过认证、维护访问规则，并跟上厂商的变更。Cursor 默认不安装任何东西，不运营也不监控你的网络客户端，仪表盘也不显示客户端状态。安装和配置该软件以厂商文档为准；本页讲 Cursor 这一侧。

## 开始之前

* 你是 Enterprise 套餐的团队管理员。**团队设置脚本仅限 Enterprise**，不会出现在其他套餐上。
* 你的网络客户端运行在基于 Debian 的 Linux 上，并且能从 shell 脚本安装和启动。团队电脑运行 Linux，脚本以电脑用户身份运行，可使用 `sudo`。
* 你的网络为这个客户端留了入口：按厂商的架构，在你想要访问的 VPC 或内网中有一个网关、出口节点或隧道连接器。
* 你已经决定电脑如何向你的网络认证。凭据不要放进设置脚本；如果脚本需要凭据，把它存为[团队密钥（Team Secret）](https://docs.x.ai/grok-bot/teams-and-enterprises#team-secrets)。

## 团队设置如何运行你的脚本

**团队设置脚本**位于 [Cursor 仪表盘](https://cursor.com/dashboard/bot) **Grok Bot** 页面的 **Bot 电脑（Bot Computers）** 下：即会在每台团队电脑上运行的安装脚本清单。每份清单包含一个或多个脚本条目，每个条目有一个 **ID**、一个 **设置脚本（Setup Script）** 和一个可选的 **检查脚本（Check Script）**。如果只想在某个群组的电脑上运行某份清单，就改在群组的 Grok Bot 标签下添加它；见[组设置](https://docs.x.ai/grok-bot/teams-and-enterprises#group-settings)。群组清单遵循与下面相同的规则。

* 脚本以电脑用户身份在每台团队电脑上运行；需要特权安装时用 `sudo`。
* 它们会在电脑启动时运行，并在电脑运行期间按周期刷新，大约每天一次。
* 如果存在检查脚本且其退出码为 0，就跳过设置脚本；用它来避免每次刷新都重新安装。设置运行后，会再运行一次检查，确认它成功。
* 条目按顺序逐个运行。每个脚本超时 30 分钟。脚本失败不会阻塞电脑；它会在之后的刷新中重试。
* 脚本会把团队的[团队密钥](https://docs.x.ai/grok-bot/teams-and-enterprises#team-secrets)作为环境变量读取，所以脚本需要的凭据从不出现在清单里。密钥只在脚本运行时存在，脚本输出在记录前会被脱敏。设置来自多个团队的电脑不会收到任何密钥。

## 创建清单

1. 转到 [Cursor 仪表盘中的 Grok Bot](https://cursor.com/dashboard/bot)，在 **Bot 电脑** 下找到 **团队设置脚本**。
2. 在 **清单（Manifests）** 旁选择 **+** 创建一个 **新清单（New Manifest）**，然后输入 **清单 ID（Manifest ID）**，例如 `private-network`。
3. 在脚本条目中，设置 **ID**（例如 `install-network-client`），编写 **设置脚本**：按你提供方的 Linux 安装文档安装客户端，然后按你的配置启动它并连接到你的网络。
4. 可选地添加一个 **检查脚本**（例如 `command -v <your-client>`），让已安装客户端的电脑跳过安装。
5. 选择 **保存（Save）**。

如果你更愿意编辑 JSON，在编辑器顶部从 **表单（Form）** 切换到 **JSON**。清单的结构如下：

```json
{
  "manifestId": "private-network",
  "entries": [
    {
      "id": "install-network-client",
      "setup": "#!/usr/bin/env bash\nset -euo pipefail\n# 1) Install your networking client per your provider's Linux install docs\n# 2) Start the client and connect it to your network per your configuration",
      "check": "command -v <your-client>"
    }
  ]
}
```

> 不要把密钥值粘贴到脚本里。设置脚本以电脑用户身份在每台团队电脑上运行，而清单是应用到整个机群的纯文本。如果脚本需要认证密钥、令牌或其他凭据，把它存为[团队密钥](https://docs.x.ai/grok-bot/teams-and-enterprises#team-secrets)并从环境变量读取，例如 `"$MY_AUTH_KEY"`。在厂商支持的情况下，优先让成员在电脑的浏览器里交互式认证，那里适用你的身份提供方策略。

## 设置你的网络客户端

无论用哪种工具，最后一步都一样：每台电脑向你的网络认证，你在厂商的控制台确认连接，然后让一个 Bot 访问一个它之前无法访问的内部主机名来验证。交互式登录在电脑的浏览器里进行，与成员平时[在那里登录公司工具](https://docs.x.ai/grok-bot/identity-and-access)的方式相同。全面铺开前，先在一两台试点电脑上开始。

### Tailscale

在每台电脑上运行 Tailscale，并经你网络内的一个[出口节点](https://tailscale.com/docs/features/exit-nodes)转出。这是该做法已经实践过的配置。Tailscale 还提供[子网路由器](https://tailscale.com/docs/features/subnet-routers)来暴露特定的私有网段；在依赖它之前，先在一台试点电脑上验证这种安排。

**开始之前：** 你运营一个 tailnet，并在想要访问的 VPC 或内网中有一个出口节点。

**团队设置清单：**

* **设置脚本：** 按 [Tailscale 的安装文档](https://tailscale.com/docs/install/linux)安装 Linux 版 Tailscale，然后按你的配置把电脑接入你的 tailnet。
* **检查脚本：** `command -v tailscale`。

**连接并验证：**

1. 让每台电脑通过认证。Tailscale 会打印一个登录 URL，在电脑浏览器中打开，那里适用你的身份提供方策略。如果你更希望无需成员登录就加入电脑，可以把一个可重复使用、带标签的[认证密钥](https://tailscale.com/docs/concepts/auth-keys)存为[团队密钥](https://docs.x.ai/grok-bot/teams-and-enterprises#team-secrets)，并从环境变量传入，例如 `tailscale up --auth-key "$TS_AUTHKEY"`。这样每台团队电脑都以同一个密钥和标签加入，而不是以成员身份加入，所以要相应限定该密钥的 ACL 范围。绝不要把密钥粘贴到脚本本身。
2. 确认电脑出现在你的 Tailscale 管理控制台中，并被允许使用该出口节点。
3. 让一个 Bot 访问一个内部主机名。

**如果不起作用：**

* 客户端装好了，但没有人认证。用浏览器登录时，这一步是手动的；用认证密钥时，检查团队密钥是否存在、名称是否与脚本读取的一致、密钥是否过期。查看 Tailscale 管理控制台里的机器列表。
* 你团队的网络策略是仅允许列表（allowlist-only），阻止了 Tailscale 的协调服务器或中继。从 Tailscale 文档中放行这些端点。运行中的电脑大约一分钟内应用变更。休眠的电脑在下次唤醒时应用。
* 出口节点没有在你的 tailnet 中通告或获批。检查管理控制台里的路由设置。
* 电脑被重建了，例如镜像更新或重置之后，会话没有保留下来。重新认证。

### Cloudflare Tunnel

同样的团队设置机制也适用于 [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)：你网络内的 `cloudflared` 连接器通过 Cloudflare 边缘发布私有服务，由 Cloudflare Access 保护，电脑按主机名访问它们。这种安排在团队电脑上还没有像 Tailscale 那样实践过，所以全面铺开前先在一台试点电脑上验证。

**开始之前：** 你在私有网络内运行一个 Cloudflare Tunnel 连接器，所需服务都已经过它路由，并且你已经选好 Cloudflare Access 策略。基于身份的策略很适合这种做法，因为成员通过浏览器登录。Access 服务令牌是密钥；如果你使用它们，请存为[团队密钥](https://docs.x.ai/grok-bot/teams-and-enterprises#team-secrets)，而不是放在设置脚本里。

**团队设置清单：**

* **设置脚本：** 按 [Cloudflare 的下载文档](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/)安装 `cloudflared`。电脑上只装客户端；连接器留在你的网络里。
* **检查脚本：** `command -v cloudflared`。

**连接并验证：**

1. 私有 HTTP 服务：用你经隧道路由的主机名访问它们。Cloudflare Access 会执行你的策略；使用基于身份的策略时，成员通过电脑的浏览器登录。
2. 私有 TCP 服务，例如数据库或 SSH：在电脑上运行 `cloudflared access tcp` 打开一个本地监听，并让工具指向它。Cloudflare 的文档说明了这个流程。Bot 需要该服务时，可以在自己的 shell 里启动这个监听。
3. 让一个 Bot 访问该私有主机名或服务。

**如果不起作用：**

* 你网络内的连接器宕了。在 Cloudflare 仪表盘检查隧道健康状态；这是你这边的问题，不是电脑的。
* Cloudflare Access 拒绝了请求。检查 Access 日志，并确认成员已通过认证。
* 你团队的网络策略是仅允许列表，阻止了隧道主机名或 Cloudflare 的端点。放行它们。运行中的电脑大约一分钟内应用变更。休眠的电脑在下次唤醒时应用。
* 服务令牌被写进了设置脚本。不要这样做；清单是纯文本。改用基于身份的 Access，或把令牌存为团队密钥，让脚本从环境变量读取。
* Bot 需要时，`cloudflared access tcp` 的监听没有运行。监听不会跨会话保留；需要时再启动一个。

要在两者之间选择：Tailscale 给电脑网络层面的可达性，配合出口节点还能从你的网络出网。Cloudflare Tunnel 通过 Cloudflare 边缘在 Access 之后发布特定服务：是按服务而不是整个网络，而且其他服务看到的出口地址不会改变。

其他能在基于 Debian 的 Linux 上安装并运行的客户端，也遵循同样的团队设置步骤；全面铺开前先在一台试点电脑上验证你的客户端。

## 推送到现有电脑

* 新电脑在启动时应用清单。
* 运行中的电脑按周期刷新获取清单变更，大约每天一次。
* 要立即应用清单变更，就重建电脑，或让成员从桌面应用重置它。在 Enterprise 上，管理员可以从仪表盘重建或终止成员的电脑。持久磁盘会保留，下一台电脑启动时会应用当前清单。
* 镜像更新会自动重建电脑，你的脚本会重新应用。电脑重建后，登录会话（包括网络客户端的登录）可能需要重新建立。

## 与网络策略配合

Grok Bot 的[网络策略](https://docs.x.ai/grok-bot/security#network-policy)是单独的一层，控制团队电脑可以访问哪些目标。如果你的团队使用 **仅团队允许列表（Team allowlist only）**，请按厂商文档添加网络客户端需要的目标，例如协调服务器、中继和网关。运行中的电脑大约一分钟内应用策略变更。休眠的电脑在下次唤醒时应用。你不需要重建电脑。

## 限制

* 这是由你运营的做法，不是 Cursor 托管的网络模式。Cursor 不安装、不运营也不监控你的网络客户端，客户端本身的支持由厂商提供。
* 常规互联网流量仍经 Cursor 的共享静态 IP 段出网，除非你把它路由经你自己的网络。不提供按客户专用的出口 IP。
* 目前没有脚本结果的机群视图。全面铺开前先在一台试点电脑上验证。
* 这不是 Cloud Agents 的那套设置。Cloud Agents 文档有自己针对另一个产品面的 [Tailscale](https://cursor.com/docs/cloud-agent/setup#running-tailscale) 和 [Cloudflare Tunnel](https://cursor.com/docs/cloud-agent/setup#running-cloudflare-tunnel) 做法；Grok Bot 的电脑按本页所述通过团队设置配置。如果 Grok Bot 把工作交给 Cloud Agents，那些 agent 在 Cloud Agent 的网络设置下运行，而不是你电脑的网络客户端下。

## 常见问题

### 我可以在设置脚本里放认证密钥或凭据吗？

不要在脚本文本里放。清单是纯文本，仪表盘会警告不要往里粘贴密钥。把凭据存为 Grok Bot 页面上的[团队密钥](https://docs.x.ai/grok-bot/teams-and-enterprises#team-secrets)，让脚本以环境变量读取。团队密钥仅限 Enterprise。在厂商支持的情况下，交互式浏览器登录仍是最简单的选择，因为你的身份提供方策略适用于它。

### 我可以用哪些网络工具？

任何你的团队能从 shell 脚本安装并运行在基于 Debian 的 Linux 上的客户端。Tailscale 和 Cloudflare Tunnel 是本页的示例。先在一台试点电脑上验证你的客户端。

### 现有电脑会得到新清单吗？

会。运行中的电脑会周期性刷新清单，大约每天一次。要立即应用清单变更，就重建电脑，或让成员从桌面应用重置它。

### 这会改变我的服务看到的 IP 地址吗？

对于经你网络路由的流量，会。发往你私有网络的流量从你的网络内部，经你的出口节点、网关或隧道连接器到达。其余流量继续从 Cursor 的共享静态段出网。

### 我们使用严格的网络允许列表。我们的客户端能工作吗？

只有在你放行它的端点时才行。把客户端需要的目标加入团队的允许列表。运行中的电脑大约一分钟内应用变更。休眠的电脑在下次唤醒时应用。

### 这和 Cloud Agents 文档里的 Tailscale、Cloudflare Tunnel 章节一样吗？

不一样。那些做法专用于 Cloud Agent 的 VM；那里的 Tailscale 需要用户态网络和代理变量。Grok Bot 的电脑使用团队设置和你自己的网关或连接器，如本页所述。

### 哪些套餐包含团队设置脚本？

**团队设置脚本仅限 Enterprise。** 清单由团队管理员管理。如果你在仪表盘的 Grok Bot 页面上看不到它，说明你不在 Enterprise，或需要你的客户团队为组织启用 Grok Bot。

### 如果设置脚本在某些电脑上失败会怎样？

电脑仍会启动。失败的条目会在之后的刷新中重试。让脚本可重复运行，并使用检查脚本，让状态正常的电脑跳过安装。
