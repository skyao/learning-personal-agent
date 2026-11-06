---
title: "文档：配置 TLS 检查代理"
linkTitle: "文档：TLS 检查代理"
date: 2026-11-05
originalTitle: "Configure TLS-inspecting proxies"
sourceUrl: "https://cursor.com/docs/grok-bot/proxies"
altUrls: ["https://docs.x.ai/grok-bot/proxies"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：桌面应用从成员设备连到两处：Cursor API（*.cursor.sh）和成员托管计算机的嵌套主机名（*.*.cursorvm.com）。带 TLS 检查的安全网关（如 Zscaler）常放行前者而破坏后者，表现为计算机设置挂起，聊天有时仍可用。文中列出必须放行的域名模式，其中 *.*.cursorvm.com 必需，只配 *.cursorvm.com 仍会失败；这些域名还要豁免 TLS 检查并关闭响应缓冲，且要应用到包括离网在内的所有配置。验证办法包括用 curl 查看证书签发方应为 Amazon RSA、用 nslookup 查计算机主机名、测试流式输出。文末区分了四种相近的控制：设备到 Cursor 的路径、计算机可访问的目的地（网络策略）、经桌面转出、在计算机上安装网络客户端。

**保留理由**：明确了客户端到托管计算机的连接路径和常见故障原因，也从侧面说明计算机是通过独立主机名与应用相连的。

---

Grok Bot 桌面应用会从每位成员的设备连接到两个地方：聊天、登录和审批所用的 `*.cursor.sh` 上的 Cursor API，以及计算机设置、屏幕和 shell 所用的成员托管计算机（hosted computer），其地址是一个嵌套的 `*.*.cursorvm.com` 主机名。执行 TLS 检查（TLS inspection）的安全 Web 网关通常放行前者，却让后者无法工作。随后桌面应用会在计算机设置期间挂起或报错；在某些配置中，聊天继续可用，而计算机始终无法连接。Zscaler 是最常见的例子，本页以它来说明具体细节；同样的步骤适用于任何会重新签署 TLS 或缓冲响应的网关。本页面向运行你的网关的 IT 团队。共享的域名列表和流式测试位于[企业网络配置](https://cursor.com/docs/enterprise/network-configuration)；本页介绍 Grok Bot 额外增加的内容。

本页讨论的是从成员设备到 Cursor 的路径。它不改变托管计算机本身可以连接到哪里；那属于[网络策略](https://cursor.com/docs/grok-bot/security#network-policy)。从计算机访问你私有网络上的服务，见[连接到私有网络](https://cursor.com/docs/grok-bot/private-networks)。

## 症状

- **计算机设置挂起或失败。** 应用始终无法完成与计算机的连接。聊天可能继续工作，因为它能访问 `api2.cursor.sh`，也可能随之停滞；无论哪种情况，计算机链路都需要 `cursorvm.com`。
- **在热点或个人设备上可用**，但在公司网络上或网关客户端运行时失败。
- **在办公室可用，在家里失败。** 例外只应用到了办公室位置。见[应用到每个配置文件](#apply-to-every-profile-including-off-network)。
- **登录或聊天也停滞。** TLS 检查或响应缓冲仍在 `cursor.sh` 上生效。

## 允许这些域名模式

在网关和任何 DNS 过滤中允许以下全部内容。优先使用通配符（wildcard），而不是逐一枚举主机名；计算机主机名是按每台计算机生成的。

| 模式 | 用途 |
| --- | --- |
| `*.cursor.sh` | 聊天、登录、审批以及 Cursor API 的其余部分 |
| `*.cursor-cdn.com` | 静态资源 |
| `*.cursorapi.com` | 扩展市场及相关 API |
| `*.cursorvm.com` | 托管计算机及其控制平面 |
| `*.*.cursorvm.com` | 同上，但深一层。必需。 |
| `cursor.com`、`downloads.cursor.com` | 安装和更新桌面应用 |

两个 `cursorvm.com` 模式都要添加。计算机主机名在 `cursorvm.com` 下有两级标签，形式为 `<computer>.<cluster>.cursorvm.com`，而单层通配符只匹配一级。只配置 `*.cursorvm.com` 的网关看起来正确，却仍会让计算机无法访问。这是在已经允许 `cursor.sh` 的网络上，计算机设置失败的常见原因。

## 让相同域名豁免 TLS 检查和缓冲

仅允许流量还不够。对上述每个域名：

- **绕过 TLS（SSL）检查。** 当网关用自己的证书重新签署连接时，即使主机名已被允许，计算机设置握手也会失败。Cursor 的连接本来就是端到端加密的。
- **关闭响应缓冲（response buffering）。** 聊天和计算机链路都使用流式传输。把响应一直保留到完成的网关，会让应用等待永远不会到达的输出。

如果你的策略要求检查所有流量，网关必须满足 [SSL 检查与 DLP](https://cursor.com/docs/enterprise/network-configuration#ssl-inspection-and-dlp) 下的要求：HTTP/2 或 Cursor 的 HTTP/1.1 回退、不经缓冲的服务器发送事件（Server-Sent Events）直通，以及不会被强制超时的长连接。

## 应用到每个配置文件，包括离网

Zscaler Client Connector 在设备离开办公室后仍继续运行，并会应用它自己的离网配置文件。添加到办公室位置或单一策略的例外不会跟着设备回家。把允许规则、TLS 检查豁免以及任何 DNS 例外，应用到 Grok Bot 成员所属的每个位置、配置文件和策略组，包括漫游和离网场景。其他把在网和离网策略分开的网关也需要同样处理。

判断线索：Grok Bot 在办公室能用，同一台笔记本在家里却失败，而网关客户端仍在运行。

## 从成员设备验证

在 IT 应用更改后，在一台成员设备上、网关客户端运行时执行以下检查。

1

### 检查证书由谁签发

```
curl -v https://api2.cursor.sh |& grep -C1 issuer:
```

签发方应为 **Amazon RSA**。如果显示 Zscaler 或你的网关供应商，说明该设备的配置文件上，`cursor.sh` 的 TLS 检查仍然生效。

2

### 检查计算机主机名能否解析

```
nslookup test.us9.cursorvm.com
```

你应该能拿回地址。如果查询失败，试试 `nslookup test.us9.cursorvm.com 1.1.1.1`。如果公共解析器能回答而默认解析器不能，问题就出在设备的 DNS 或网关配置文件，那里缺少嵌套的 `*.*.cursorvm.com` 例外。

3

### 测试流式传输

运行[测试代理连通性](https://cursor.com/docs/enterprise/network-configuration#testing-proxy-connectivity)下的 HTTP/1.1 和 HTTP/2 流式测试。输出应逐行到达，而不是一次性全部到达。

4

### 在应用中重试

在同一台设备上打开 Grok Bot 桌面应用并连接到计算机。如果仍然失败，从该设备重复上述检查；热点通过而公司网络失败，即可确认网络是原因。

## 范围

有三种控制容易混淆：

| 你想 | 使用 |
| --- | --- |
| 让成员设备通过你的网关访问 Cursor 及其托管计算机 | 本页 |
| 限制托管计算机可以访问哪些目的地 | [网络策略](https://cursor.com/docs/grok-bot/security#network-policy)，仅限 Enterprise |
| 让托管计算机的流量经成员设备路由 | [通过你的桌面转出流量](https://cursor.com/docs/grok-bot/settings#route-traffic-through-your-desktop) |
| 在每台托管计算机上安装网络客户端 | [Team Setup Scripts](https://cursor.com/docs/grok-bot/private-networks#install-a-networking-client-with-team-setup)，仅限 Enterprise |

默认情况下，托管计算机自身的流量从 Cursor 的[共享静态出口 IP](https://cursor.com/docs/grok-bot/security#static-egress-ips) 离开，不经过成员设备上的网关。当成员开启 **Route traffic through this computer** 时，被路由的流量使用该设备的网络，并受其网关策略约束。

## 常见问题

### 我们已将 \*.cursorvm.com 加入允许列表。为什么计算机设置仍然失败？

通常有两个原因。缺少嵌套的 `*.*.cursorvm.com` 模式，因此计算机的主机名不匹配。或者域名已允许但仍被 TLS 检查，于是网关的证书破坏了设置握手。添加嵌套模式，让两个模式都豁免检查，然后运行[检查](#verify-from-a-members-device)。

### 我们已允许 cursor.sh。为什么这没有覆盖计算机？

它们使用不同的主机名。聊天、登录和审批发往 `api2.cursor.sh`，大多数网关已经允许。计算机链路发往嵌套的 `cursorvm.com` 主机名，需要它自己的允许规则和检查豁免。这也是为什么在某些网络上聊天可以继续工作，而计算机始终无法连接。

### 在办公室能用，在家不能用。有什么不同？

网关客户端在家里仍在运行，其离网配置文件没有获得这些例外。请也把它们应用到漫游和离网配置文件。

### 我们的策略要求检查所有流量的 TLS。

那么网关必须原样放行流式传输。要求见 [SSL 检查与 DLP](https://cursor.com/docs/enterprise/network-configuration#ssl-inspection-and-dlp)。豁免 Cursor 的域名是可靠的路径；Cursor 的连接本来就是端到端加密的。

### 这个列表也覆盖 Cursor 编辑器吗？

覆盖。它与[企业网络配置](https://cursor.com/docs/enterprise/network-configuration#ip-allowlisting)是同一个列表。编辑器的聊天和 Tab 功能不需要 `cursorvm.com` 模式也能工作，这就是为什么对编辑器没问题的网关仍可能破坏 Grok Bot。
