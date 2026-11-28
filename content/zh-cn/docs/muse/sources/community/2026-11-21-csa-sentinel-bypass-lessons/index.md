---
title: "打破智能体的出口关口：Muse Sentinel 绕过的教训"
linkTitle: "Sentinel 绕过的教训"
date: 2026-11-21
originalTitle: "Breaking the Agent’s Egress Gate: Lessons from the Muse Sentinel Bypass"
sourceUrl: "https://labs.cloudsecurityalliance.org/research/csa-research-note-meta-muse-sentinel-bypass-agent-egress-202/"
author: "Cloud Security Alliance AI Safety Initiative"
publisher: "Cloud Security Alliance"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-21
tags: [安全, 运行环境]
products: [muse]
dateNote: "页面 article:published_time 为 2026-11-21T13:49:26Z。"
---

{{< source-info >}}

**收录说明**：直接下载；删去重复的标题行；文末参考文献照录。文中对 NebuSec 数据的引用均注明出处，并提醒成功率与修复时间线等数字未经独立复现。

**内容摘要**：云安全联盟 AI Safety Initiative 于 11 月 21 日就 NebuSec 研究发布的研究札记：复述三段攻击链（Chromium 浏览器→Sentinel 静默外传→共享内核逃逸至虚拟机 root），指出 Sentinel 把无正文的 GET、HEAD、OPTIONS 请求视为可静默放行的「读」请求，固定解码与熵阈值可被攻击者学习利用，而 cgroup 挂钩只覆盖容器内进程、虚拟机层进程可直接出网。札记以对照表逐项映射官方所述的控制层与报告的弱点，并给出即时、短期与战略三档建议，包括收紧静默请求的放行范围、把出口管控锚定在虚拟机或宿主机网络层、对分类器做对抗测试。文中同时提醒，攻击链细节、成功率与修复时间线均出自 NebuSec 单方，未经独立复现，Meta 亦未就此发表声明。

**保留理由**：针对本次披露的独立第三方分析，把 NebuSec 的技术发现提炼为可迁移到其他智能体运行时的出口管控教训，并附控制层对照表与分层建议，是已收两篇 NebuSec 原文之外的分析补充。

---

**作者：**Cloud Security Alliance AI Safety Initiative
**发布：**2026-11-21

**分类：**智能体 AI 安全

[下载 PDF](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/11/CSA_research_note_meta_muse_sentinel_bypass_agent_egress_20261121-csa-styled.pdf)
[下载 Markdown](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/11/CSA_research_note_meta_muse_sentinel_bypass_agent_egress_20261121-csa-styled.md)

## 要点

2026 年 11 月 20 日，安全研究团队 NebuSec 发布两篇报告，描述其如何攻破 Meta 的 Muse 个人 AI 智能体。这条链路始于一个随附的 Chromium 浏览器，接着绕过 Muse 的「Sentinel」出口关口，静默外传用户的对话历史与已存记忆，最终从智能体容器逃逸，在每用户虚拟机上取得 root 权限 [1][2]。NebuSec 表示，Muse 团队知晓每一项发现，并已在发布前修补文中描述的所有漏洞利用 [1]。此事值得细究，因为 Sentinel 组合了少数公开记录的智能体平台会同时实现的若干控制措施：在智能体容器之外实施宿主侧策略、基于 eBPF 的污点追踪、替代凭据，以及带外用户审批 [3]。在 CSA 的评估中，其中两条失效的假设——容器范围内的执行与静默读取——是其他智能体运行时常见的设计选择。

第一条教训是：出口关口只有在每个请求都被正确分类时才有效。Sentinel 把无正文的 `GET`、`HEAD`、`OPTIONS` 请求当作可以静默放行的读取，并按固定的解码、熵与流量阈值筛查内容。NebuSec 详细记录了这些规则，并报告称，它通过在这些规则范围内操作，在没有触发审批提示的情况下把私有数据送了出去 [1]。第二条教训是：关口的覆盖范围止于命名空间的边界。Sentinel 的执行挂钩挂在容器的 cgroup 上，因此在共享内核逃逸之后，直接运行在虚拟机中的进程不再被强制经过 Sentinel，而有了自己通往互联网的路径 [1]。第三条教训关乎最薄弱的组件——它决定了智能体的实际权限。一个落后于上游补丁、且为导出 PDF 关闭了 IPC 沙箱的随附浏览器，让一个渲染器漏洞变成了以智能体权限执行的代码 [1]。

出口管控也覆盖不到智能体通过其他渠道摄取的数据。在另一则报道中，路透社发现，在与 Signal 员工及 AI Now Institute 共同进行的测试中，Muse 在 Android 和 macOS（但不包括 iPhone）上，通过安装时授予的操作系统权限获取了 Signal 消息内容。这条路径运行在 Meta 的连接器层之外，也在 Sentinel 管辖的一切之外 [6]。综合来看，这些发现意味着防御方应把智能体出口关口视为若干层中的一层。这种分层做法要求加固沙箱、在虚拟机层（而不仅是容器层）实施出口管控、采用默认拒绝的目的地策略，并专门针对分类器开展红队测试。

## 背景

Meta 于 2026 年 9 月 8 日发布 Muse，作为一款消费级个人智能体，可以代用户发邮件、订行程、填写表单和购物 [4]。每位用户获得一台专用云虚拟机，Meta 称之为 Muse Secure VM，智能体运行在该虚拟机上的一个容器中，可广泛访问 Linux 工具与文件 [3][5]。Meta 的发布公告把安全模型围绕单一控制点来表述：「Muse 所做的任何事，未经 Sentinel 批准都不会到达互联网」[4]。公司还在发布日把此前私有的漏洞赏金计划向所有人开放，对有效报告最高奖励 30 万美元，其中针对影响单个用户的成功提示注入最高 13 万美元 [3][7]。

Meta 发布日的工程文章把 Sentinel 描述为运行在智能体容器之外（按 NebuSec 的发现，位于每用户虚拟机内）的组件，并称其为「连接器操作与网络出口的唯一权限方」：智能体提出操作，只有 Sentinel 能批准 [3]。来自智能体容器的流量经过一个前向代理，由用户命名空间、veth 边界和 eBPF 过滤强制执行。Sentinel 在连接层和 HTTP 层检查每个请求，包括主机名、解析出的 IP、端口、方法、路径和解码后的请求内容 [3]。Meta 增加了一种名为「受污染出口」（tainted egress）的机制，使用 cgroup 上和 Linux 安全模块挂钩上的 eBPF 程序，把任何读取用户数据的工具进程标记为受污染；受污染的进程失去自动放行，回落到常规审批流程 [3]。凭据由单独的服务 `hatch-authd` 处理。智能体始终只持有替代令牌，Sentinel 在授权后于网络边界换入真实的、限定于具体连接器的凭据 [3]。当请求需要征得同意时，审批对话框出现在 Muse 客户端中、对话之外，因此模型无法伪造或拦截它 [3]。

Meta 的设计明确围绕 Simon Willison 的「致命三要素」构建：智能体既能访问私有数据、又暴露于不可信内容、还能对外通信 [3][9]。Meta 自己的文章承认「提示注入仍是业界未解的问题」[3]。Sentinel 的目的是确定性地切断三要素中的第三条腿，使被操纵的智能体无法在不经过策略检查的情况下把数据送出去。发布后不久的一项独立分析从运行时内部记录了这套架构的许多内容。研究者 Rohan Adwankar 描述了 Cloud Hypervisor 微虚拟机、`systemd-nspawn` 运行时单元、假 IP DNS、由「Hatch Sandbox Egress CA」进行的 TLS 拦截，以及作为 Sentinel 之下底层的 eBPF 连接关口 [5]。

## 安全分析

NebuSec 的研究分三个阶段展开，每个阶段检验 Muse 设计中的一个不同假设。下面的分析依次跟随这条链路，然后考察出口模型在哪里失守，以及哪些数据路径完全位于关口之外。

### 攻击链

与许多公开报道的智能体入侵不同，NebuSec 的链路不依赖提示注入。Muse 有四种浏览器后端，NebuSec 针对的是 Muse 直接使用或经 Playwright 用于截图、缩略图和 PDF 导出的随附 Chromium 二进制 [1]。10 月初，容器仍附带 Chromium 152 版，这是 9 月 3 日发布的一个补丁版本。NebuSec 估计「有五个以上公开的 V8 漏洞可用于」该版本，并利用一个公开的解析器漏洞逃出了 V8 沙箱 [1]。决定性的配置错误是，用于导出 PDF 的 Chromium 进程关闭了 IPC 沙箱。当用户要求 Muse 把一个由攻击者控制的页面保存为 PDF 时，一个渲染器漏洞——NebuSec 估计其在漏洞市场上的价值约 500 美元——就给了攻击者在运行时容器中以智能体权限执行 shell 命令的能力。NebuSec 称之为「0.5 次点击」的远程代码执行（RCE），意为在受攻击者影响的内容上进行一次普通用户操作就足够了 [1]。

从这个立足点出发，NebuSec 最初的几次外传尝试触发了 Sentinel 的审批提示，即使命令以容器 root 身份运行 [1]。这一点值得直说：面对朴素的外传手法，这套架构做到了它被设计要做的事。随后 NebuSec 研究了 Sentinel 的策略行为，并报告称「我们利用浏览器链路把用户的对话历史和已存记忆发送到我们的服务器，而没有触发审批提示」[1]。研究者还能注入对话历史并修改已存记忆，因此智能体的完整性也受到影响，而不只是用户机密性 [2]。NebuSec 尚未公布外传流量的具体形态，因此具体的编码或请求模式无法从公开来源确认。

最后一个阶段完全抛开了出口关口。Muse 的容器与每用户虚拟机共享一个定制的、源自 Ubuntu 的 Linux 7.0 内核。NebuSec 报告称，若干内核加固选项被关闭，且内核版本落在多个 CVE 已公布的影响范围内 [1]。其自动化漏洞利用生成框架产出的内核漏洞利用，NebuSec 称在超过 99.9% 的测试运行中成功，使研究者取得了虚拟机的 root 权限 [1][2]。作为虚拟机 root，他们可以触及用户的持久卷、安全凭据存储以及 Sentinel 本身 [2]。NebuSec 明确表示，它没有演示逃逸到虚拟机监控器宿主机或其他租户环境中 [2]。

读者在权衡这些发现时应留意其来源。对这条链路的叙述，包括修补时间线、成功率数字和漏洞利用成本估计，都来自 NebuSec 自己的发布物 [1][2]。本札记引用的来源中没有任何一份包含 Meta 就 NebuSec 发现发表的声明，成功率与漏洞利用成本数字也未经独立复现。

### 出口模型在哪里失守

这次绕过很有启发，因为它并未正面击败 Sentinel 的架构。相反，它利用了那些让常驻智能体可用的策略决定，NebuSec 的分析对此有详细描述。在默认的「部分操作需询问」设置下，只有无正文的 `GET`、`HEAD`、`OPTIONS` 请求算作读取，「写入需要审批，除非有允许规则覆盖；而读取可以静默放行」[1]。内容筛查会对 URL 的每个组成部分尝试十六进制和 Base64 解码，并查找电子邮件地址、电话号码和一次性验证码。无法解码的片段按各字符类的香农熵阈值评分，并按域名在滚动 60 分钟窗口内应用流量预算 [1]。NebuSec 特别指出了一处不对称：经过 Base64 编码的短电子邮件地址会触发审查，而同一地址以明文出现则被放行 [1]。

这些选择各自都合理。合在一起，它们定义出了一条信道。一个被归类为读取的请求可以把数据放进它的 URL，而任何建立在固定模式和阈值上的检测器都会告诉有耐心的攻击者能发送多少、以什么形式发送。Meta 的设计直接承认这种张力：其既定目标是「把摩擦放在真正需要同意的地方，同时让日常操作顺畅流动」[3]。一个整天必须浏览、搜索、抓取页面的智能体无法对每个 `GET` 都提示用户。教训并不是 Sentinel 的分类器设计草率。任何允许向任意目的地静默读取的分类器都是一条带宽受限的外传路径，其限制应被视为攻击者可以发现的东西。

共享内核阶段暴露了第二个结构性假设。NebuSec 观察到「那个曾强制我们容器连接经过 Sentinel 的 cgroup 挂钩并不覆盖直接运行在用户虚拟机中的进程」，而且虚拟机有自己的公网 IPv6 地址，使虚拟机层进程可以不经 Sentinel 直接发送流量 [1]。因此 Sentinel 的执行绑定在容器的命名空间和 cgroup 上，而不是虚拟机的网络接口上。一旦代码运行在 cgroup 之外，关口就不再适用于它。这是容器安全中熟悉的模式，但对智能体而言更重要。出口关口的全部价值在于：在智能体的推理已被攻陷之后它仍然成立；而被攻陷的智能体恰恰有动机去寻找内核逃逸。

下表把 Muse 有记录的控制层对应到 NebuSec 研究报告的内容，以及可迁移到其他智能体平台的教训。若某项弱点是 CSA 的推断而非研究中的直接陈述，表中会注明。

| 控制层 | 设计意图（据 Meta） | 报告的弱点 | 可迁移的教训 |
| --- | --- | --- | --- |
| 随附 Chromium（PDF 导出） | 智能体沙箱内的渲染工具 | 落后于上游补丁；IPC 沙箱被关闭；单个渲染器漏洞即可导致 RCE [1] | 辅助工具继承智能体的权限，必须达到同样的补丁与沙箱标准 |
| Sentinel 的读/写分类 | 为保持可用性，读取静默、写入受控 [3] | 无正文的 `GET`/`HEAD`/`OPTIONS` 被视为可静默放行的读取 [1] | 被归类为读取、发往任意主机的出口是一条外传信道 |
| 内容筛查与熵检查 | 检测 URL 中经过编码的个人数据 [3] | 固定的解码器与阈值可被学习；明文能通过而 Base64 不能 [1] | 基于模式与阈值的数据防泄漏（DLP）提高攻击成本，但不能作为安全边界依赖 |
| 受污染出口（eBPF） | 剥夺读取用户数据进程的自动放行 [3] | 未见其阻止所报告的静默外传；外传进程是否被标记为受污染未披露（CSA 推断）[1] | 污点追踪必须覆盖每条进程路径与数据流才具决定性 |
| cgroup 范围的出口挂钩 | 强制所有容器流量经过 Sentinel [3] | 内核逃逸后不适用于虚拟机层进程；虚拟机有自己的公网 IPv6 地址 [1] | 在虚拟机或宿主网络层实施出口管控，而不仅按容器 |
| 共享内核 | 每用户虚拟机内的容器隔离 | 加固选项被关闭；内核处于受影响 CVE 范围内 [1] | 共享内核才是真正的边界；应把它作为一个整体来加固和打补丁 |

### 关口之外的入口路径

另一条报道线索显示了智能体真实的攻击面有多少位于任何出口关口之外。2026 年 11 月 18 日，路透社报道，在与 Signal 员工及 AI Now Institute 共同进行的测试中，Muse 在 Android 和 macOS 上获取了 Signal 消息内容，但在 iPhone 上没有。每一次它都绕过了 Meta 自己的连接器层，转而依赖用户在安装时授予的操作系统权限 [6]。一位 Meta 发言人称这些是「孤立事件」[6]。更早之前，据 NeuralTrust 报道 [8]，安全研究者 Patrick Wardle 披露了 Muse macOS 客户端的一个缺陷：一个未公开的偏好键让无特权的本地进程可以重定向听写流并截获认证令牌。据同一报道，Meta 发布了热修复，Wardle 于 9 月 22 日确认 [8]。

严格来说，这些问题都不是 Sentinel 绕过，但与 NebuSec 的发现合在一起，它们指向同一个结论。Meta 的发布宣传把 Sentinel 描述为智能体互联网访问的单一控制点。NebuSec 的逃逸表明，这一说法对容器之外的进程并不成立；路透社的发现则表明，大量进入智能体的数据流根本不经过 Sentinel。运行在容器 cgroup 之外的代码，以及通过客户端操作系统权限进入智能体的数据，从来就不在 Sentinel 的范围内。因此，评估任何智能体平台的安全团队都应当问：出口控制实际看到了什么，以及它运作得有多好。

## 建议

以下建议按时间跨度组织。它们既面向员工使用厂商托管的消费级智能体的组织，也面向构建或运营自有智能体平台的团队，因为两者可用的控制手段差别很大。

### 即时行动

允许员工使用 Muse 或类似消费级个人智能体的组织，应首先审查这些智能体能接触到什么。NebuSec 报告 Meta 已修补所述漏洞利用 [1]，但架构层面的教训适用于每一个设计类似的智能体平台。安全团队应查明哪些企业账户、电子邮件、日历和消息应用已连接到个人智能体，以及它们的桌面和移动客户端持有哪些操作系统级权限。鉴于路透社的发现，无障碍、通知访问和屏幕录制授权尤其值得关注 [6]。

合适的网络控制取决于智能体运行在哪里。对于像 Muse 这样由厂商托管的智能体，企业无法把智能体自身的出站流量纳入企业控制，因为该流量源自厂商的基础设施。此时的实际控制手段是：限制可连接的企业账户与数据，对这些连接器实施条件访问与令牌范围限制，并监控连接器侧的审计日志。对于自托管或企业部署的智能体，智能体产生的出站流量还应经过企业控制的安全 Web 网关或 DNS 过滤器，使厂商自己的关口不是唯一的控制。

运营自有智能体平台的团队，应按与智能体本身相同的标准审计打包进智能体运行时的每一个辅助二进制文件。浏览器、PDF 渲染器、文档转换器和媒体工具都算在内。处理受攻击者影响内容的渲染组件应在沙箱完全启用的情况下运行，并在数日内跟进上游安全版本。

### 短期缓解

在未来一到三个月内，智能体平台所有者应重新审视其出口策略如何对待读取。对静默请求采用默认拒绝的目的地允许列表，对任意主机要求审批或经中间代理抓取，会显著收窄依赖「读取」分类进行外传的信道。不过，会记录或回显查询参数的允许列表目的地仍可携带数据，应加以审查。若开放网页浏览是产品需求，抓取应经过一个无法访问智能体私有数据的独立浏览服务。Muse 也确实把部分页面抓取路由到单独的远程服务 [1]，这种做法若与私有数据隔离，就符合这一模式。以这种方式分离能力，是在结构上而非依赖检测来打破致命三要素 [9]。

出口管控还应锚定在智能体无法触及的最低层。容器级 cgroup 挂钩有用，但还需要虚拟机级或宿主机级的出口控制，使虚拟机内任何进程（包括逃逸后的进程）的流量都被强制经过策略点。一台拥有自己直连互联网路径的虚拟机会削弱容器级关口。在智能体容器与虚拟机之间共享内核的平台，应启用标准内核加固、尽量减少暴露的攻击面，并按「已公布的内核 CVE 可能被迅速武器化」的假设安排补丁节奏。NebuSec 报告其自动化框架为受影响的 Muse 内核产出了可靠的漏洞利用 [1]。

### 战略考量

NebuSec 的研究表明，智能体出口关口本身也需要对抗性测试。智能体平台的红队项目应包含针对分类器的测试。实践中，这意味着探测哪些请求类型被视为静默读取、哪些编码与熵水平能逃过筛查，以及按域名预算允许多少数据。测试期间的审批提示应被看作关口在起作用的证据，测试还应继续检查：一个研究过关口的攻击者能否避开它们。

更长期看，组织应优先选择这样的智能体架构：最敏感的数据与开放网页出口能力从不在同一执行上下文中并存。机密虚拟机（Confidential VM）设计与更强的隔离边界——例如使用独立虚拟机而非共享内核容器——会提高逃逸阶段的成本。Meta 已表示计划推出 Confidential VM 模式 [4]。智能体平台的采购与风险评估应要求厂商准确说明：其出口控制执行的是哪条边界、它看不到哪些流量，以及它在沙箱逃逸后如何表现。

## CSA 资源对照

本事件延续了 CSA 在近期若干研究札记中追踪的一个模式。《当沙箱泄漏：ChatGPT 锁定模式绕过》（2026 年 11 月）分析了 HTML 预览沙箱如何为内容提供了一条绕过 OpenAI 确定性出口限制的路径 [10]。其结论是：能力移除类控制只有在覆盖每条出口路径、且其执行点无法从应用内部绕过时才成立。Muse 的发现把这一结论从客户端渲染层一直带到了内核层。Sentinel 的执行点在其 cgroup 内有效，却不覆盖其外的进程，而辅助渲染组件再次成为攻击者的入口。

《自托管 Qwen3.8 智能体的非请求出口》（2026 年 10 月）建议采用默认拒绝、按智能体划分并与工作负载身份绑定的出口策略，在智能体之外执行，同时用执行代理在命令运行前校验目的地 [11]。这些建议与 NebuSec 研究在静默读取分类和容器范围执行上暴露的缺口直接对应。CSA 早先对致命三要素的分析提出了 Meta 与本札记都依赖的能力分离原则 [12]。《GuardFall》札记描述的编码智能体护栏中的检查-执行差距，与 Sentinel 的分类器按一套攻击者可学习并绕过的风险模型来判断请求的方式相似 [13]。对于这条链路的沙箱与逃逸阶段，《沙箱化智能体 AI：面向 MCP 与编码智能体的最小权限模式》（2026 年 5 月）讨论了智能体与宿主机之间的最小权限隔离，而共享内核的发现正使这一点受到质疑 [16]。

在控制映射方面，CSA AI Controls Matrix（AICM）v1.1 提供了治理框架 [14]。其「基础设施与虚拟化安全」和「威胁与漏洞管理」域对应共享内核加固与随附组件打补丁的问题。其「数据安全与隐私生命周期管理」和「身份与访问管理」域对应出口数据丢失控制与替代凭据模型。CSA 的 MAESTRO 智能体威胁建模框架也相关 [15]。MAESTRO 的分层模型直接对应这条链路：工具层的浏览器失陷、智能体运行时的策略绕过，以及基础设施层的逃逸。团队可以用它来识别自己的出口控制在哪些地方依赖于单一层的成立。

## 参考文献

[1] NebuSec. “[Inside Meta Muse: Browser, Sentinel and the Shared-Kernel Boundary](https://nebusec.ai/research/inside-meta-muse/).” NebuSec Research, November 20, 2026.

[2] NebuSec. “[Hacking Muse: Stealing Private Chats Through Browser Use](https://nebusec.ai/research/meta-muse-credential-exposure/).” NebuSec Research, November 20, 2026.

[3] Sheasha, Tarek (Meta). “[How We Built Safety Into Muse](https://muse.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse).” Muse Blog, September 8, 2026.

[4] Meta. “[Introducing Muse: The World’s First Personal AI Agent Built for Everyone](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/).” Meta Newsroom, September 8, 2026 (updated November 10, 2026).

[5] Adwankar, Rohan. “[What’s in a Muse?](https://rohanadwankar.github.io/posts/sandbox2.html).” Personal blog, September 2026.

[6] Reuters. “[As Meta bets big on Muse AI agent, early safety mishaps surface](https://www.thestar.com.my/news/world/2026/11/18/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface).” Reuters (via The Star), November 18, 2026.

[7] Meta. “[Meta Bug Bounty](https://bugbounty.meta.com/).” Meta, accessed November 21, 2026.

[8] Howroyd, Roger. “[Meta Muse Security: What CISOs Must Know](https://neuraltrust.ai/blog/meta-muse-ai-agent-security).” NeuralTrust, October 14, 2026.

[9] Willison, Simon. “[The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/).” simonwillison.net, June 16, 2025.

[10] Cloud Security Alliance. “[When the Sandbox Leaks: ChatGPT Lockdown Mode Bypass](https://labs.cloudsecurityalliance.org/research/csa-research-note-chatgpt-lockdown-mode-bypass-20261106-csa/).” CSA AI Safety Initiative, November 6, 2026.

[11] Cloud Security Alliance. “[Unrequested Egress from Self-Hosted Qwen3.8 Agents: What Defenders Should Do Now](https://labs.cloudsecurityalliance.org/research/csa-research-note-qwen38-agent-unexpected-egress-20261029-cs/).” CSA AI Safety Initiative, October 29, 2026.

[12] Cloud Security Alliance. “[The AI Agent Lethal Trifecta](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-agent-lethal-trifecta-capability-securi/).” CSA AI Safety Initiative, June 2026.

[13] Cloud Security Alliance. “[GuardFall: Shell Injection Bypass Defeats AI Coding Agent Guardrails](https://labs.cloudsecurityalliance.org/research/csa-research-note-guardfall-ai-coding-agent-shell-injection/).” CSA AI Safety Initiative, June 30, 2026.

[14] Cloud Security Alliance. “[AI Controls Matrix (AICM) v1.1](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1).” Cloud Security Alliance, 2026.

[15] Cloud Security Alliance. “[Agentic AI Threat Modeling Framework: MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro).” Cloud Security Alliance, February 6, 2025.

[16] Cloud Security Alliance. “[Sandboxing Agentic AI: Least-Privilege Patterns for MCP and Coding Agents](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_research_note_agentic_ai_sandbox_least_privilege_mcp_20260530-csa-styled.pdf).” CSA AI Safety Initiative, May 30, 2026.

[← 返回研究索引](/research/)
