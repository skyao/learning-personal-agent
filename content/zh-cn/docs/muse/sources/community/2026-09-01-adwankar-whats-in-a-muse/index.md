---
title: "Muse 里面有什么？"
linkTitle: "Muse 沙箱剖析"
date: 2026-09-01
originalTitle: "What's in a Muse?"
sourceUrl: "https://rohanadwankar.github.io/posts/sandbox2.html"
author: "Rohan Adwankar"
publisher: "Rohan Adwankar（个人博客）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-21
tags: [运行环境, 安全]
products: [muse]
dateNote: "页面未标发布日期；仅知发表于 2026 年 9 月（文中观测日期为 9 月 11 日），按当月 01 日记；CSA 研究札记引作 September 2026。本轮经 CSA 引文发现后回填。"
---

{{< source-info >}}

**收录说明**：直接下载；经 CSA 研究札记引文发现回填；文中的两处一级标题式强调段按规则改为引用块；页面未标发布日期，见 dateNote。

**内容摘要**：个人博客对 Muse 沙箱的独立技术剖析：对照 Cloud Hypervisor 与 Firecracker 两种虚拟机监视器的差异，实测记录虚拟机的启动、滚动更新与生命周期管理，指出重启即替换整台虚拟机、虚拟机监视器不随 guest 重启存活；核查 metaaivm.com 与出站路径，记录 2026 年 8 月 15 日 cli.github.com 触发的全网人工审批风暴等 egress 细节；文中多处结论注明为实测而非推断，并区分了已验证与未验证的部分。

**保留理由**：对 Muse 运行时沙箱少有的独立实测剖析，含虚拟机监视器、启动与出站的一手观测，与已收官方安全文章、iFynx 解析及 NebuSec 技术详解互为对照；经本轮 CSA 引文发现后回填。

---

这是对一篇关于[智能体沙箱](https://rohanadwankar.github.io/posts/platforms.html)的文章的后续。

上次我们考察了几个智能体沙箱，有位评论者精辟地总结道「[一路往下都是 firecracker](https://news.ycombinator.com/item?id=49605644#:~:text=It%27s%20always%2C%20firecracker%20all%20the%20way%20down!)」，不过我们运气不错，仅仅一天之后 Meta 就发布了 Muse，给了我们一台新的虚拟机可以探索！

作为发布的一部分，其中一个大胆的说法是 Muse 是某些竞争对手的更快的替代品，这一点上次已经讨论过。那我们就掀开引擎盖看看他们到底做了什么。和上次一样，我们通过 [ws-term](https://github.com/RohanAdwankar/ws-term) 拨出一个 shell，用常用工具四处看看。开始之前最后说明一点：前一半讲沙箱本身，后一半讲我们从内部能看到的智能体框架（harness）部分，所以可以按兴趣跳到相应小节，因为这篇比上一篇稍长一些！

## 不是 Firecracker

一上来你就会注意到，`systemd-detect-virt` 和 DMI 表对这是一台什么机器的判断不一致，而两者都对：

```
$ systemd-detect-virt
systemd-nspawn
$ cat /sys/class/dmi/id/product_name
cloud-hypervisor
$ uname -r
7.0.0-26-generic                    # a stock Ubuntu kernel, not a custom build
$ hostname; id; nproc; free -h | grep Mem
htch-runtime
uid=0(root) gid=0(root) groups=0(root)
2
Mem:  7.7Gi  2.1Gi ...
```

所以这个 shell 是 **systemd-nspawn 容器**里的 root，而这个容器运行在一台虚拟机里，该虚拟机的 DMI 厂商、产品和 BIOS 字符串全都写着 [Cloud Hypervisor](https://github.com/cloud-hypervisor/cloud-hypervisor)。容器共享虚拟机的内核，所以它是普通的 Ubuntu `-generic` 内核，而不是 Claude Code 启动的那种 `-fc-` 定制构建。

这台机器上没有任何路径自称 Muse。守护进程叫 `hatch`，环境变量是 `JARVIS_*`，虚拟机叫「hatchling」，引导证书叫「yolk」，域名是 `metaaivm.com`，其 DNS 边缘是 `metaclaw`。产品名出现在运行时携带的东西里：家目录下的 `PROACTIVE_PREFERENCES.md` 写着「Muse reads this whole file before composing the day's edition」，技能树里有 `muse_db` 和 `muse-feedback`，镜像里带着 `models/ultra_muse_1000`。Meta 自己的[安全文章](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)证实了这一点：「Muse（代码库名：Hatch）。」我最后会回到那篇文章，因为它对这个盒子的描述相当精确。

```
$ cat /sys/class/dmi/id/sys_vendor /sys/class/dmi/id/product_name /sys/class/dmi/id/bios_version
Cloud Hypervisor
cloud-hypervisor
0
$ cat /proc/cmdline
console=ttyS0 root=/dev/vda rootfstype=btrfs ip=dhcp ds=nocloud;s=http://169.254.169.254/latest/
  lsm=landlock,lockdown,yama,integrity,apparmor,bpf ro
  systemd.set_credential=vmm.notify_socket:vsock-stream:2:512
```

Cloud Hypervisor 和 Firecracker 是兄弟：都是基于 KVM 的 Rust 虚拟机监视器（VMM），建立在同一套 `rust-vmm` crate 之上。Firecracker 出自 AWS Lambda，刻意做得极小；Cloud Hypervisor 出自 Intel，现在由 Linux 基金会托管，是「成年人版」的那一个。对这类产品而言要紧的差别是：

|  | Firecracker | Cloud Hypervisor |
| --- | --- | --- |
| 出身 | AWS（Lambda、Fargate） | Intel，现属 Linux 基金会 |
| 总线 | 仅 virtio over MMIO，`pci=off` | 完整 PCI，virtio-pci |
| SMBIOS/DMI | 无（`product_name` 为空） | 有，厂商字符串为「Cloud Hypervisor」 |
| 热插拔 | 无 | vCPU、内存、磁盘、网卡热插拔 |
| 设备 | 块、网络、vsock、气球 | 另加 vhost-user、virtio-fs、virtio-pmem、TPM、GPU 直通 |
| 气球（balloon） | 仅充气/放气 | 另加空闲页上报（guest 自动归还已释放内存） |
| 启动 | 仅直接内核 | 直接内核或固件（UEFI/OVMF） |
| 快照/恢复 | 有 | 有 |
| 沙箱 | 自带 `jailer` | seccomp，依赖外部沙箱 |

Muse 用的是右列：guest 有四块可以切换的 virtio-block 磁盘、一条回到 VMM 的 vsock 通知通道、一个带空闲页上报的气球，以及后来按任务租用的*浏览器虚拟机*。上次 E2B 和 Claude Code 都显示出 Firecracker 的签名（`pci=off`、空 DMI、`virtio_mmio.device=`）。这一台有 PCI 总线和 BIOS 字符串。

```
$ for d in /sys/bus/virtio/devices/*; do echo "$(basename $d) $(cat $d/device) $(basename $(readlink $d/driver))"; done
virtio0 0x0002 virtio_blk     virtio3 0x0001 virtio_net    virtio5 0x0013 vmw_vsock_virtio_transport
virtio1 0x0002 virtio_blk     virtio4 0x0004 virtio_rng    virtio6 0x0005 virtio_balloon
virtio2 0x0002 virtio_blk     virtio7 0x0002 virtio_blk
$ cat /sys/bus/virtio/devices/virtio6/features | cut -c1-6
011001                          # stats_vq, deflate_on_oom, and bit 5: free page REPORTING
```

最后这一位正是「一台长期在线的按用户虚拟机」能负担得起的原因：guest 释放页面时会把空闲页交还宿主机，于是一台闲置的 hatchling 只占用它约 2 GB 的工作集，而不是 8 GB 的分配量；在一个 126 核的 EPYC 上，两个 vCPU 处于 `load average: 0.00` 时几乎不花什么钱。

## 两个盒子

```
$ lsblk -o NAME,SIZE
vda    7.3G       # VM root, btrfs, read-only (ro on the cmdline)
vdb    7.5G       # overlay upper: the writable scratch layer for /
vdc    587M       # the "hatch image": daemon, tools, models, squashfs + verity
vdd    100G       # yours: the RV, btrfs, mounted at /home/hatch
$ df -h | grep -vE tmpfs
overlay         7.5G   17M  7.5G   1% /
/dev/mapper/rv  100G  111M   99G   1% /home/hatch
```

容器里没有 `/dev/mapper`，但 `/sys/block` 仍会列出 device-mapper 目标及其 UUID，而 UUID 前缀能告诉你每个是什么：

```
$ for d in /sys/block/dm-*; do echo "$(cat $d/dm/name) $(cat $d/dm/uuid)"; done
root_overlay  CRYPT-PLAIN-root_overlay              # vdb: dm-crypt plain mode, a throwaway key
opt_hatch     CRYPT-VERITY-0000...-opt_hatch        # vdc: dm-verity, integrity-checked, not secret
rv            CRYPT-LUKS2-5b3a29f5...-rv            # vdd: LUKS2. Your volume is encrypted at rest
```

所以工具镜像是被度量的（verity），暂存层用一个没人保存的密钥加密，而 RV——某个脚本把它展开为「Reliable Volume」（可靠卷）——是一个真正的 LUKS2 卷，装着 `/home/hatch`、`/var/lib/hatch` 和 Postgres 数据目录。这种划分和 Claude Code 的*你的盘 vs 他们的盘*是同一思路，只是外面画了一个容器：

```
flowchart TB
  subgraph vm["Cloud Hypervisor microVM (the hatchling)"]
    direction TB
    hostsvc["VM-side systemd: spawnd, sentinel, authd, hatch-safety, postgres, browser-broker, ingress-rev-proxy"]
    subgraph cell["systemd-nspawn runtime cell (htch-runtime)"]
      execd["hatch-execd, spawns your shells"]
      daemon["hatch daemon, the harness (entered from outside)"]
      home[("/home/hatch on vdd (rw, LUKS2), the RV, persists")]
      opt[("/opt/hatch squashfs on vdc (ro, verity), tools + skills + models")]
    end
    hostsvc -->|nsenter into the cell| daemon
    hostsvc -->|nsenter into the cell| execd
  end
  daemon -->|unix socket the cell can't see| inference["inference proxy"]
```

虚拟机侧的服务和 cell 共享 PID 命名空间，但不共享挂载命名空间。`hatch daemon` 和 `hatch-execd` 在 cell 内的 `ps` 里显示为 **PPID 0**：它们在虚拟机上启动，然后被 `nsenter` 进来。即使身为 cell 的 root，你也读不到 `/proc/<daemon>/ns/*` 或 `/proc/<daemon>/root`。这和 Claude Code 封起来的 `process_api` 是同一个把戏，只是这里的操作进程活在*你租户命名空间旁边*，而不是做它的 PID 1。

```
$ ps -eo pid,ppid,cmd | head -5
    1     0 /usr/lib/systemd/systemd
   17     1 /usr/lib/systemd/systemd-journald
 1347     0 /opt/hatch/bin/hatch-execd --runtime-cell-leader=1957    # PPID 0: entered from the VM
 1586     0 /opt/hatch/bin/hatch daemon --runtime-cell-leader=1957
$ readlink /proc/1586/ns/mnt
                                                                     # (empty: not yours to see)
$ ls /run/hatch/
auth  cell-anchors  egress-tls  egress-tz  noded  privsep  resume  runtime-cell  sandbox  sandbox-api  telemetry
                                                                     # no proxy/, no daemon/: inference socket is not in the cell's view
```

cell 里的 root 在虚拟机上对应 uid 131072，是一个用户命名空间，而你拿到的 shell 被刻意裁剪过：

```
$ grep -E 'Seccomp|NoNewPrivs' /proc/self/status
NoNewPrivs:      1
Seccomp:         2
Seccomp_filters: 4
$ python3 -c 'import ctypes,os; l=ctypes.CDLL(None,use_errno=True); l.syscall(425,0,0); print(os.strerror(ctypes.get_errno()))'
Operation not permitted                  # io_uring_setup is filtered
$ capsh --print | grep -o 'Bounding set.*' | grep -cE 'sys_ptrace|net_admin'
0                                        # no CAP_SYS_PTRACE, no CAP_NET_ADMIN, no CAP_NET_RAW, no CAP_SYS_MODULE
```

连你的工具 shell 之间也是相互隔离的：我的 bash 和 cell 的 PID 1 处在不同的挂载命名空间。智能体执行的每个 `exec` 都有自己的视图。

## 它是怎么启动的

幸运的是，`/opt/hatch/runtime-cell/` 和 `/opt/hatch-image/bin/` 里的脚本对此有详细记录，描述了一台启动时没有归属、随后被挂上归属的虚拟机。下面按我的理解总结其中与性能有关的关键点。

**虚拟机启动时没有身份。** `hatch-prewarm` 在「hatch-init 之后、任何 RV 挂载之前」运行，并把 cell 的启动文件称为*「无身份预启动」（identityless preboot）*。环境里带着 `JARVIS_IS_ASSIGNED=0`。把你挂到一台 hatchling 上是 `spawnd rv-graft`：

```
rv-graft   Graft RV identity onto the pre-booted runtime: verify the RV binds,
           superficially validate the resume handoff marker, ensure the os-intent
           ledger dir, and write the boot-id-stamped /hatch/data/resume/rv-identity-ready
```

**启动时不安装任何东西。** 虚拟机根文件系统是用 mkosi 构建的只读 btrfs；`/opt/hatch` 是位于 dm-verity 上的 squashfs（prewarm 脚本称之为「被度量的根文件系统」）；cell 的根文件系统按 KDL 清单（`runtime-cell.kdl`：约 110 个 apt 包，从 `build-essential` 到 `libreoffice-*-nogui`、`tigervnc`、`xvfb`、`cloudflared`、`nodejs 24`）核对，而发行版自带的 `apt-daily`/`unattended-upgrades` 定时器被*退役*了——用惰性的 unit 覆盖文件，这样就不会有无人归属的外联。智能体安装的包以意图记录在 RV 上一个只追加的账本里并在之后重放，而不持久化进根文件系统。

**页缓存被预热了。** 在 RV 挂载之前，`vmtouch -t` 会触碰 Postgres 服务器及其 `ldd` 闭包、hatch 守护进程二进制、`systemd-nspawn` 的闭包、以及 cell 的 init/loader/libc，预算为 256 MiB，自我截止时间为 10 秒，「处处失败即放行（fail-open everywhere）」。健康门要求 `is-system-running` 恰好是 `running`，一台虚拟机才有资格，所以这条路径上的任何东西都不能让某个 unit 失败。

**cell 的启动目标几乎是空的。**

```
$ systemctl list-units --type=service --state=running
  systemd-journald.service          # that's it
$ systemd-analyze
Startup finished in 2.212s (userspace)
default.target reached after 213ms in userspace
```

`default.target` 是一个自定义 unit，它唯一的 `Wants=` 是 `hatch-execd.socket`。其他一切（Postgres、Sentinel、authd、safety、telemetry、浏览器 broker）都活在虚拟机侧，以 Unix socket 的形式绑定挂载进来。

**框架与操作系统分开交付。** `hatch --version` 打印出一个构建于 `2026-09-11T02:29:54Z` 的提交，大约在我读到它之前两小时，`JARVIS_CD_CHANNEL=alpha`。守护进程是一个「实时更新包（live-update bundle）」，有自己的信任根（prewarm 脚本正是因此拒绝对它执行 `ldd`），所以新的框架并不意味着新的虚拟机镜像。

### 观察一次滚动发布

那个晚上有三次，我的 shell 掉了线，重拨循环重新连上，而盒子有了不同的启动时间和不同的框架构建：

```
$ grep btime /proc/stat; hatch --version
btime 1789094439   hatch 0.1.0 (17400c3e011)  built 02:29:54Z     # 19:40, the VM I started on
btime 1789100040   hatch 0.1.0 (17400c3e011)                       # 21:14
btime 1789102110   hatch 0.1.0 (5d489a6707a)  built 03:11:58Z     # 21:48
btime 1789105122   hatch 0.1.0 (052113f66d3)  built 03:38:10Z     # 22:38
$ journalctl | grep "Startup finished"
Sep 10 21:14:13 htch-runtime systemd[1]: Startup finished in 2.307s.
$ cat /run/hatch/resume/rv-identity-ready; cat /run/hatch/resume/execution-ready.marker
6c7da3cc-... 2026-09-11T04:14:21.732Z marker=present
2026-09-11T04:14:39.110151343+00:00
```

| 阶段 | 墙钟时间 | 距内核启动 |
| --- | --- | --- |
| 内核启动（`btime`） | 21:14:00 | 0 秒 |
| cell 的 `default.target` | 21:14:13 | 13 秒 |
| RV 已挂载，身份已知 | 21:14:21 | 21 秒 |
| 第二次 CA 刷新（发布身份专属锚点） | 21:14:35 | 35 秒 |
| `execution-ready` 标记 | 21:14:39 | 39 秒 |

这就是部署机制：频道上有新构建，就意味着一台带着新包的新 hatchling，挂上 RV，拆掉旧的，约 40 秒中断。每次我的家目录回来时所有文件都完好，时间戳也相同，因为没有任何东西活在虚拟机上。`/usr/sbin/reboot` 被一个脚本覆盖，它从另一个方向说了同样的事：

```
> A hatchling cannot reboot in place. The VMM does not survive a guest reset:
> the VM disappears, the hatchling goes UNHEALTHY, and the workflow recovers by
> REPLACING it with a brand new VM. That was measured, not assumed ...
> So `reboot` already means "replace this VM" ... Powering off reaches the same
> end state with services stopped in order.
```

守护进程的遥测字段也是这样记录的（`rollout_id`、`release_id`、`previous_build_id`、`target_build_id`、`outage_duration_ms`、`pre_deploy_all_healthy`），还有一整套 `hatch_mount_to_ws_ready_*` 指标（`postgresql_startup`、`db_preflight`、`runtime_cell`、`daemon_active_to_ws_ready`、`readiness_bottleneck`）覆盖上表中从挂载到就绪的窗口。

## 谁管理生命周期

这些二进制文件里包含着虚拟机向运行它的那一方呈现的接口，从内部看是这样的：

- **启动时的元数据。** 内核命令行把 cloud-init 的 `nocloud` 数据源指向 `169.254.169.254`，由 VMM 宿主机提供；每台虚拟机的身份、频道和区域（`JARVIS_VM_COMPUTE_REGION=scu`）就是从这里来的。
- **通过 vsock 报告就绪。** `vmm.notify_socket:vsock-stream:2:512` 让 systemd 的 `sd_notify` 直接送到 VMM，prewarm 的注释说控制平面的「健康门要求恰好是 `running`」。
- **从内部探健康。** `hatch-healthd` 在指标 socket 上轮询守护进程的 `/health`，「这样宿主机侧的 healthd 可以拨它，而不必穿过运行时 cell 的 IPv6 veth」。
- **救援。** `hatch-rescue` 有 `restart-component`、`emit-flare`，以及我最喜欢的 `emit-codex-session`：它在「救援 codex 家目录」里启动一个 `codex app-server` 来诊断 `kernel_incident`。`/opt/hatch-image/bin/` 里那个 258 MB 的 OpenAI Codex CLI 就是干这个的。这台虚拟机的值班人员是一个智能体。
- **替换。** reboot 脚本称之为「工作流（the workflow）」，守护进程向 `/v1/runtime-events` 和 `/v1/leased-vm-resources-events` 发送带 `host_region` 和 `git_sha` 的请求。

## metaaivm.com 是什么？

每台 hatchling 都有一个公开名字：

```
JARVIS_FQDN=70f9aa6e-1767-497b-96fd-6bbac24fe79b.metaaivm.com
$ dig +short 70f9aa6e-....metaaivm.com
edge-metaclaw.c10r.facebook.com.
57.144.221.192
$ host 57.144.221.192
... edge-metaclaw-shv-01-sjc6.facebook.com.     # a Meta PoP in San Jose, closest to me
$ whois metaaivm.com | grep -E 'Creation|Name Server' | head -2
Creation Date: 2026-02-26
Name Server: A.NS.FACEBOOK.COM
```

每台虚拟机的主机名是一条指向 Meta 边缘的 CNAME（`c10r` 是他们的边缘层；这个域名是今年二月注册的）。在它后面、*虚拟机内部*，是 `ingress-rev-proxy`，一个「带 Noise\_XX 加密的面向互联网的入口反向代理」：`:443` 用于基础设施（`health`、`version`、`journal`、`rescue`、`yolk`），`:4431` 用于公共数据平面（`ping`、`v1/noise`、`spaces`）。从我的笔记本上看，443 接受 TCP 连接然后重置 TLS ClientHello，而 4431 在边缘根本没有暴露。没有 Noise 握手，边缘就没有东西可转发。

这是与上次相比最大的架构差异。Claude Code 的虚拟机**完全没有入站**；Instinct 的 E2B 盒子只能由后端访问。Muse 的虚拟机是**一台带 DNS 名字的服务器**。手机应用通过 Meta 的边缘与你的虚拟机保持一条持久的 Noise 会话，而 `spaces`（公共监听器上的一条路由，守护进程字符串里有 `space.json` 构建格式，`/run/hatch/sandbox/` 里有四个 `space-*.sock` 沙箱）是智能体构建并*从你的虚拟机*提供服务的 Web 应用。

这种持久会话也是应用手感如此的原因。你一按发送，「正在回复」的气泡立刻出现，因为守护进程的准入步骤只是对本地 Postgres 的几次写入，打字指示器在那里就触发了，早于提示词组装，更早于任何一个模型 token。守护进程为整条路径埋了指标（`ingress_ms`、`admission_ms`、`pre_inference_prompt_assembly_*_ms`、`time_to_llm_ms`、`time_to_first_response_token_ms`、`tokens_per_second`），其中没有任何一环是在等虚拟机醒来。

```
flowchart LR
  phone(["Muse app"]) -->|TLS + Noise_XX| edge["edge-metaclaw.c10r.facebook.com"]
  edge -->|:4431 public / :443 infra| irp["ingress-rev-proxy (in the VM)"]
  irp --> daemon["hatch daemon"]
  irp --> spaces["spaces: agent-built web apps"]
  daemon -->|"/v1/messages, avocado, gpt"| inf["inference proxy"]
  subgraph cell["runtime cell"]
    shell["your exec / ws-term"]
  end
  shell -->|CONNECT, MITM| sentinel["Sentinel egress proxy :3128"]
  sentinel -->|allowlist + HITL approval| internet(["internet"])
```

## 出站

cell 只有一条 veth，一个 /30，网关同时是 DNS 服务器和代理：

```
$ ip -br a
host0@if3  UP  198.19.0.2/30  fd8b:4f84:7d32:99::2/64
$ grep -v '^#' /etc/hosts | tail -2
198.19.0.1 hatch-egress-proxy
fd8b:4f84:7d32:99::1 hatch-egress-proxy
$ env | grep -i proxy
HTTPS_PROXY=http://hatch-runtime:<rotated-per-boot>@hatch-egress-proxy:3128
NO_PROXY=localhost,127.0.0.1,::1,198.19.0.1,198.19.0.2,...
CURL_CA_BUNDLE=/run/hatch/egress-tls/ca-bundle.pem      # also GIT_SSL_CAINFO, NODE_EXTRA_CA_CERTS, AWS_CA_BUNDLE
```

试图绕过它时会发生什么：

```
$ dig +short @8.8.8.8 example.com
198.18.123.158                       # not example.com: a fake IP from the 198.18/15 bench range
$ curl https://1.1.1.1/              # direct 443, no proxy
curl: (35) ... SSL connect error     # TCP is answered, TLS is not: the gate ate it
$ curl -sv https://example.com/ 2>&1 | grep -E 'issuer|Connection Established'
< HTTP/1.1 200 Connection Established
*  issuer: CN=Hatch Sandbox Egress CA; O=Hatch          # MITM'd, like Claude Code's egress gateway
$ curl https://example.com:8443/     # non-standard port
< HTTP/1.1 200 Connection Established
curl: (28) Operation timed out       # CONNECT accepted, then held
```

DNS 由网关用合成地址应答，这样每条连接在代理处都能归因到某个*名字*，而 `pre-start.sh` 脚本挂上一个 eBPF `connect4`/`connect6` cgroup 钩子（`spawnd attach-cell-gate`），作为「Sentinel 之下的地板：用 `BPF_F_ALLOW_MULTI` 组合的 cgroup 钩子要求每个程序都放行，所以 Sentinel 死掉或被按住不再意味着无治理的 link-local/RFC1918/CGNAT 可达」。veth 的虚拟机侧还有第二个分类器，丢弃指向宿主机本地目的地的帧。

Sentinel 是策略引擎，运行时 cell 清单在一个解释为什么禁用发行版自带 apt 定时器的注释里，说明了它如何决策：

```
> ... their egress reaches Sentinel unattributed ... and fleet-wide HITL prompt
> storms whenever they dial a host the managed system-egress allowlist does not
> carry (the 2026-08-15 cli.github.com storm).
```

所以策略是按**主机**的：一个受管允许列表（`managed-internal-network-policies.yaml` 被点名为该文件），以及任何不在列表上的目标都要走人在环路中（HITL）的提示。无法归因的流量——即 Sentinel 无法关联到某个 cell cgroup 的进程——正是 eBPF 门要拦下的。代理密码和 CA 包都会在每次虚拟机替换时轮换，一个 `hatch-ca-trust.path` unit 监视轮换。盒子永远看不到的一样东西是推理端点：`api.anthropic.com` 经代理返回 404，可达但无密钥，而守护进程的推理 socket 没有挂载进 cell。

## 框架

框架是一个 327 MB 的 Rust 二进制（大小与 Claude Code 那个 324 MB 的 Bun 框架相近），烘焙在里面的 Cargo registry 路径就是依赖列表：

```
$ strings hatch | grep -oE 'index\.crates\.io-[a-f0-9]+/[a-zA-Z0-9_-]+-[0-9]' | sed 's/.*\///; s/-[0-9]$//' | sort | uniq -c | sort -rn
tokio hyper axum tokio-tungstenite reqwest rustls h2         # async runtime, HTTP, WebSocket
sqlx-postgres sqlx-sqlite sqlparser                          # Postgres client, and a SQL parser for muse.db
genai                                                        # multi-provider LLM client (rust-genai)
ort fastembed tokenizers hf-hub ndarray                      # ONNX runtime: the local classifiers + embeddings
boa_engine boa_parser                                        # a JavaScript engine, in Rust
seccompiler                                                  # builds the seccomp filters your shell runs under
tree-sitter scraper html5ever lopdf calamine image           # parsing code, HTML, PDF, xlsx, images
jsonschema schemars moka prometheus tracing-subscriber
$ strings hatch | grep -ciE 'langgraph|langchain|rmcp|modelcontextprotocol'
0
```

唯一一个开源且像智能体组件的依赖是 `genai`，一个供应商无关的 Rust 大模型客户端，一个二进制借此在单一接口后面对话多个模型家族：

```
$ strings /opt/hatch/bin/hatch | grep -oE '(claude|avocado|gpt)-[a-z0-9.-]+' | sort | uniq -c | sort -rn | head
  3 avocado-5.16-v4          # internal model family, also "avocado-memory-flush-v1"
  2 claude-opus-4-6
  2 claude-opus-4-8
  1 claude-sonnet-4-6
  1 gpt-5.6-sol
  1 gpt-5.5-codex
$ strings /opt/hatch/bin/hatch | grep -c anthropic     # "failed to parse anthropic response", "/v1/messages"
```

传输走的是 Meta 的内部网关，代码里叫 **ipnext**（`ipnext/stream.rs`、`ipnext/avocado-5.16-v4`、`ipnext/proxy_readiness.rs`），而 `JARVIS_ANTHROPIC_TIMEOUT_MS` / `JARVIS_AVOCADO_CONTEXT_WINDOW_TOKENS` 是各自独立的旋钮，所以这些供应商是一等公民，而不是藏在某个路由器后面。推理经 `JARVIS_INFERENCE_PROXY_SOCK` 离开守护进程，那是一个 cell 够不到的 Unix socket，因此由哪个模型回答是服务端的决定。Meta 的文章把主模型写成 **Muse Spark 1.3**；`avocado` 大概是它的代号。

这是一个智能体循环，符号名铺开了它的各个阶段：

```
admission → pre_inference (skill_loading, prompt_assembly, context_pressure, compaction)
          → model stream (ipnext / anthropic /v1/messages / openai responses)
          → tool_dispatch_batch (+ approval_intent)
          → post_tool_continuation → post_inference_terminalization
agent_loop(49)  message_execution(210)  objective_worker(258)  subagent_spawns(248)  compaction(152)
```

**压缩（compaction）** 很积极且后台运行（`started_eager_background_compaction`、`adopted_eager_background_compaction`），所以上下文摘要会在窗口填满之前就绪，而且它有自己的模型（`avocado-memory-flush-v1`）。**目标工作者（objective worker）** 是长期运行的目标，有自己的调度和「通知步骤」，驱动主动推送的每日版。**子智能体（sub-agent）** 是一等公民（`subagent_spawns`、`subagent_monitor`，家目录里的策略文件 `SUBAGENTS_MONITORING.md`），每个在 `agents/agent-<uuid>/sessions/` 下有自己的一份记录。每个阶段都有超时环境变量（`JARVIS_TOOL_DISPATCH_TIMEOUT_MS`、`JARVIS_MODEL_STREAM_FIRST_CHUNK_TIMEOUT_MS`、`JARVIS_POST_INFERENCE_TERMINALIZATION_TIMEOUT_MS`……）和 Postgres 里的重启检查点，这就是会话能在回合中途虚拟机被替换时存活下来的原因。

一个非常酷的功能是边车分类器（sidecar classifier），而且很多：

```
$ strings hatch | grep -oE '[a-z0-9_]*(classifier|prefilter|gatekeeper|judge|guard)[a-z0-9_]*' | sort | uniq -c | sort -rn | head
  198 judge             75 guard              70 classifier         45 gatekeeper
   27 safety_classifiers   13 policyguard     12 prefilter          11 visual_browser_screenshot_guard
    8 cbrne_returned_text_guard   8 browser_action_guard   7 phone_call_judge
```

有名字的模型：`9b_safety_classifier`、`2b_tool_call_classifier_v0_4`、`pi_3b_prefilter`（一个提示词注入预过滤器；还有一个「ORIGIN GATE」提示词，用来判定哪*一类来源*的文本可能携带注入，以及 `JARVIS_EXTERNAL_CONTENT_BOUNDARIES_ENABLED`）。有些通过 `ort` 在盒内运行，其余的走虚拟机侧的 `hatch-safety` socket。另有一条 `/alignment/system/steps/` 流水线（`judge`、`reflect`、`repair`、`distill`、`generalize`）和 Postgres 里的 `self_improvement` schema，在离线状态下给智能体自己的行为打分并改写，而 `JARVIS_DEFAULT_MAX_TRAINING_TIER` 读起来像是针对「哪些数据可被用作训练数据」的按用户同意级别。

有些模型也在盒子里：

```
$ ls /opt/hatch-image/models/
asr/       faster-whisper-tiny                          # local speech-to-text
memory/    models--Qdrant--all-MiniLM-L6-v2-onnx        # 91 MB embedding
           models--jinaai--jina-reranker-v1-turbo-en    # 153 MB reranker
$ ls /opt/hatch-image/bin/
bun  codex  rtc-sidecar  hatch-manifest  hatch-prewarm  ...
$ /opt/hatch-image/bin/codex --version
codex-cli 0.149.0                                        # OpenAI's Codex CLI, 258 MB, used by hatch-rescue
```

## 记忆

记忆不是 Instinct 那种 Markdown 的 git 仓库。它在虚拟机上的 **Postgres** 里，`muse_db` 技能把整个 schema 作为 4,116 行的参考文档随附，让智能体可以通过一个有界的只读 `SELECT` 界面查询它：

```
$ grep -c '^#### ' /opt/hatch/skills/muse_db/references/schema.md
194                                   # tables
$ grep '^### ' schema.md | tr '\n' ' '
activity agent device feed goals health ideas ingest media memory messages podcasts
runtime scheduler self_improvement shell spaces
$ grep '^#### `memory\.' schema.md
memory.claims  memory.entries  memory.entry_attributes  memory.embeddings
memory.embedding_models  memory.metadata
```

记忆本身是 `~/memory/` 下的 Markdown（按日期的日志、`bank/{world,experience,opinions}.md`、人物与群组页面），Postgres 是它上面的索引：每个片段进入 `memory.entries`，带 `path#L<行号>` 引用；作为 384 维 pgvector 行进入 `memory.embeddings`，由盒内的 MiniLM 模型生成；并作为一个 `tsvector` 用于关键词搜索；守护进程的 `memory_search` 工具和推理前的召回步骤对两者做混合检索，由 jina 重排器给命中结果排序。这就是嵌入模型放在本地的原因：这个语料是盒子里最私人的数据，每次记忆刷写追加内容时都会被重新嵌入，而一个 91 MB 的模型在两个核上做这件事，片段从不离开 LUKS 卷。
`device.*` schema 是你同步进来的手机数据（联系人、通话记录、日历事件、上传会话），`agent.*` 是对话记录、压缩和子智能体进度，schema 的说明还指出推理类字段通过脱敏投影提供。

它是每台虚拟机一个真正的服务器，而不是别处共用的一个：

```
$ grep -i pgsql /proc/net/unix | head -1        # net namespace is shared with the VM
... /run/hatch/postgres/.s.PGSQL.5432
$ ls -ld /var/lib/hatch/postgres
d---------  nobody nogroup  /var/lib/hatch/postgres   # data dir on the RV, mode 000 to the cell
$ find / -xdev -name .git 2>/dev/null
/home/hatch/workspace/wsterm/.git                # the only git repo on the box is mine
```

服务器二进制在虚拟机根的 `/opt/metasql`（prewarm 脚本称之为它拒绝换入的「全脂二进制（whole-fat-binary）」），数据目录乘着 LUKS2 的 RV，守护进程通过 Unix socket 用连接池（`postgres/pool.rs`、`postgres/write_retry.rs`）与它通信。凭证只发给「受信任的 Hatch 数据库调用方」：我在 shell 里运行 `hatch-doctor run` 被 `authd` 拒绝，返回 403，因为 `authd` 同时按 `SO_PEERCRED` 的 uid *和* cgroup 认证调用方。备份走 btrfs：`spawnd` 和守护进程都带着 `btrfs snapshot` / `subvolume snapshot` / `backup_path` 字符串，这与 Meta 所说的「你的虚拟机数据持续备份」相符。

智能体自己的文件对看过其他 2026 年助手的人来说非常熟悉，是一个 [OpenClaw](https://github.com/openclaw/openclaw) 风格的工作区：

```
root@htch-runtime:~# ls /home/hatch/
AGENTS.md                 USER.md   hooks
HEARTBEAT.md              agents    memory
IDENTITY.md               assets    prompts
MEMORY.md                 channels  runtime.lock
PROACTIVE_PREFERENCES.md  config    subscriptions
SOUL.md                   data      user
SUBAGENTS_MONITORING.md   docs      workspace
TOOLS.md                  dreams
root@htch-runtime:~#
```

这里也能看到拥抱子智能体、目标和 cron 任务的设计：

```
PROACTIVE_PREFERENCES.md      # "Muse reads this whole file before composing the day's edition"
agents/agent-<uuid>/sessions/<uuid>.jsonl     # 18 sub-agents so far, transcripts as JSONL
workspace/cron.d/{secondly,minutely,hourly,daily,weekly,monthly,yearly,runonce}
workspace/goals/<slug>/{GOAL.md,briefs,crons,agent_notes,files,references}
workspace/feed/  workspace/scheduler/
```

## 工具

```
$ ls /opt/hatch/bin | wc -l
70
$ ls /opt/hatch/bin | head -40 | tr '\n' ' '
authdc browser-broker browser-service calendly device-data duffel facebook-cli ... hatch-vault
hatch-ws-client hatch-zeitgeist healthkit-cli instagram-cli ... outlook-mail peloton philips-hue
places plaid printify ... spotify-api stripe-link tailscale tessie-api threads-cli ticketmaster tts ...
$ ls /run/hatch/privsep | wc -l
60
```

和 Instinct 一样，工具是 CLI 而不是 MCP 服务器。与 Instinct 不同的是，它们*在盒子上*运行，但每一个都作为自己的**特权分离工作者（privsep worker）**运行：`spawnd ensure-worker-accounts` 为每个工具创建一个 `hatch-w-<tool>` uid，给它一份其状态目录的 id 映射视图，cell 只能通过 `/run/hatch/privsep/<tool>.sock` 访问它。`/opt/hatch/bin` 里大多数二进制都是指向同一个 `hatch-multicall` 二进制的符号链接，而该二进制拒绝以自己的名字运行。有两个配置文件按 CD 频道控制一台虚拟机究竟*能看到*哪些工具和技能：

```
$ cat /opt/hatch/runtime-cell/skill-scopes.conf | grep -v '^#'
hatch-e2e ads_mcp health nutrition
internal-test ads_mcp audio_notes_read documents end-call health nutrition polymarket price-tracker
prod whatsapp
```

受门控的技能只暂存在宿主机上，在 cell 启动时「失败即关闭（fail-closed）」地覆盖进 `/opt/hatch/skills`；未知频道什么也看不到。

凭证从不进入 cell。`authdc --help` 把 `hatch-authd` 描述为「操作 auth-files」和「动态凭证」的东西，由对端凭证把关，而 Meta 的[文章](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)说明了这些动态凭证是什么：代理令牌（surrogate token），所以「智能体永远看不到真实令牌」。购买通过 Stripe Link 得到同样对待：有一个 `stripe-link-checkout-card` privsep socket 和虚拟机侧的 `checkout-spend.sock`，文章解释说签发的一次性卡号「绑定该特定商户、特定金额，且只在有限时间内有效」。

浏览器系统与我们看到的 Instinct 非常相似，带一个 broker/调度器概念来路由会话：

```
$ browser-broker --help
Long-running broker daemon that routes browser sessions to leased VMVM browsers

  --browser-vm-image <BROWSER_VM_IMAGE>
          Immutable leased browser VM image ref
  --socket <SOCKET>
          ... that subdir is DELIBERATELY not bind-mounted into the runtime cell:
          the cell has NO path to the broker. The sole client is the host daemon,
          admitted by exact cgroup identity plus --allowed-peer-uid; the in-cell→broker
          bind remains absent to close the HiTL-consent bypass
  --lease-helper-socket <LEASE_HELPER_SOCKET>
          UDS of the privileged lease helper the on-demand lease router relays lease
          ops through (forwards to the stefi-proxy; performs the viewer bind-mount)
  --retain-vmvm-for-debug
          Development only: retain an already-active failed VMVM route and its
          broker-private Docker API socket until the 15-minute lease TTL or broker
          shutdown ... restarts an exited retained browser container without
          recreating it. Has no effect on local-cell routes or VMVM admission
```

「VMVM」是 Meta 自己的词，从未展开，而那段帮助文本就是关于它的全部证据：浏览器会话被路由到一台*租用的虚拟机*，该虚拟机由「不可变的浏览器虚拟机镜像」构建，里面浏览器是一个 Docker 容器，通过 broker 私有的 Docker API socket 访问，租期 15 分钟，经 `stefi-proxy` 取得。只有守护进程能到达 broker，所以智能体在 cell 里运行的工具，不经过同意流程就无法驱动一个已登录的浏览器。驱动它的子智能体拿到的是可访问性树快照而不是 DOM，不能执行脚本，DevTools 被禁用（`visual_browser_screenshot_guard` 和 `browser_action_guard` 是监视它的分类器）。`/opt/meta-chromium` 也随 cell 提供，用于不需要你的 cookie 的无头工作。

租约本身由一个叫 **Stefi** 的东西中介。推理 socket 旁边有一个 `JARVIS_STEFI_PROXY_SOCK`，守护进程的字符串显示什么经过它：

```
$ strings /opt/hatch/bin/hatch | grep -i stefi
hatch-engine/crates/hatch-browser-lease/src/stefi.rs
stefi_create stefi_status stefi_renew stefi_release        # browser VM leases
(Stefi `consent_uri`, return_uri-stamped) resolved by the auth-status   # connector OAuth
STEFI WhatsApp cursor conflict:                             # WhatsApp channel pairing
parse Stefi onboarding avatars:                             # onboarding assets
Opaque monotonic Stefi version. Compare only; do not display as a count.
```

所以看起来 `stefi-proxy` 是这台虚拟机通往 Meta 控制平面的唯一一扇门：任何需要后端决定的事情（租一台虚拟机、关联一个账号、配对消息频道、发推送）都经那个 socket 出去，而 cell 同样没有路到它。

## 输入与输出

关于进出这个盒子的东西，最清晰的清单是编译进守护进程的 Unix socket 路径列表。每一个都是从虚拟机侧绑定挂载进来的，而 cell 只看到它需要的那几个：

```
$ strings hatch | grep -oE '/run/hatch/[a-z0-9_./-]+\.sock' | sort -u
/run/hatch/daemon/http-api.sock            realtime-protocol.sock   rtc-stats.sock      # the app, via ingress-rev-proxy
/run/hatch/proxy/inference.sock            # OUT: models, through ipnext
/run/hatch/proxy/stefi.sock                # OUT: Meta control plane (leases, consent, channels, push)
/run/hatch/sentinel/egress-approvals-admin.sock  daemon-egress-approvals.sock  http-api.sock   # egress policy + HITL
/run/hatch/safety/security.sock            # hatch-safety: the classifier ensemble
/run/hatch/auth/authd.sock                 vault-encrypt/encrypt.sock   whatsapp-keyd/keyd.sock  # secrets
/run/hatch/browser-broker/browser-broker.sock  research-browserd.sock  daemon/browser-control.sock  # leased browsers
/run/hatch/rtc/realtime.sock               voice-genui-decision.sock   present-widget.sock   # voice calls, live UI
/run/hatch/checkout-spend/checkout-spend.sock  credit-watcher.sock     # money: purchases and the credit meter
/run/hatch/cron-store/control.sock         noded/control.sock  tailscale/control.sock  ssh-access.sock
/run/hatch/telemetry/telemetry.sock        bugreport.sock  daemon/metrics.sock    # OUT: to Meta's logging (scuba)
/run/hatch/sandbox/space-{inference,media,web-search,privileged}.sock  sandbox-api/api.sock  space-share.sock
/run/hatch/exec/execd.sock                 daemon/enter-tool-environment.sock   # IN to the cell: your shell
/run/hatch/privsep/<tool>.sock  x60        # the tool workers
```

## 小结

|  | Claude Code | Instinct | Muse |
| --- | --- | --- | --- |
| 隔离原语 | Firecracker microVM | Firecracker microVM（E2B） | Cloud Hypervisor microVM **+ nspawn cell** |
| 虚拟机内的 guest | 定制 Rust PID 1 | 完整 Ubuntu + XFCE | Ubuntu 宿主服务 + Ubuntu 容器 |
| 启动（实测） | 约 6.4 秒到框架 | 约 1.26 秒到桌面 | 13 秒到 cell，约 40 秒到就绪 |
| 生命周期 | 空闲时回收，有消息时唤醒 | 超时、冷启动或快照恢复 | 预启动 hatchling，挂载 RV；每次发布替换；气球回收空闲内存 |
| 什么持久 | `vda` 块卷 | S3 里的 git 仓库 | `vdd`，一个 LUKS2 加密的 100 GB「Reliable Volume」 |
| 记忆模型 | 磁盘上的对话 | Markdown 库，git | 虚拟机上的 Postgres（194 张表）+ 本地嵌入/重排 |
| 入站 | 无 | 仅后端 | **公开 FQDN，经 Meta 边缘的 Noise\_XX** |
| 出站 | 仅 443 的 MITM 网关 | 开放 | MITM 代理 + eBPF 门 + 假 IP DNS + HITL 审批 |
| 框架 | 在盒子上，Bun | 不在盒子上 | 在盒子上，327 MB Rust，密封，从虚拟机侧进入 |
| 模型 | 经 SSE 的 Claude | 从不在盒子上 | 服务端路由：经 `genai` 的 `avocado-*`、`claude-*`、`gpt-*` |

看到相似的产品在实现策略上如何分化，是件很有意思的事。不管怎样，它们背后显然都有大量深思熟虑的工程，让一堆复杂的活动部件变成非常顺滑的用户体验。我期待看到这个领域如何演进，以及这些不同的架构决定最终如何收敛 :)。

## 附言

如果你对沙箱感兴趣，还有一条我若不提就失职的重大消息，是 OpenAI 智能体 SDK 采用 e2b 沙箱的发布。
你可能还记得 E2B 在上一篇文章中被提到，其 CEO 甚至现身回答问题。如果你好奇，我推荐看看他们的[公告](https://e2b.dev/resources/e2b-is-now-in-agents-sdk)。
