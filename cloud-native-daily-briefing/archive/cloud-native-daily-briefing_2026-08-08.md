# ☁️ 云原生每日简报 · 2026-08-08

本期云厂商动态方向部分未覆盖：AWS 官方信源（aws.amazon.com）被出站网络代理拦截，未能直接核实；GCP、Azure 完成检索但未发现覆盖窗口内的实质新内容。

## 版本与变更

- 【续报】Kubernetes v1.37 已切出首个 Release Candidate（v1.37.0-rc.0，8 月 6 日发布），如期朝 8 月 26 日 GA 推进；DRA Partitionable Devices（KEP-4815）在本轮 RC 中仍处于此前的 alpha/beta 过渡阶段，尚未见官方明确其最终毕业级别，需等正式 release notes 核实。对使用者：计划升级到 v1.37 的用户可开始在 RC 上做兼容性验证，重点关注此前已披露的破坏性变更（containerd 2.0 最低版本要求、cgroup v1 节点在未设置 `failCgroupV1: false` 时 kubelet 将拒绝启动等）。来源：[kubernetes/kubernetes Releases](https://github.com/kubernetes/kubernetes/releases)

## 安全通告

- Linux 内核 SCTP 动态地址重配置（Dynamic Address Reconfiguration）代码中存在一个存续近 18 年的 use-after-free 漏洞 SCTPhantom（CVE-2026-64564，CVSS v4.0 评分 8.5，高危），本地攻击者可提权至 root，特定配置下可实现容器逃逸至宿主机；由腾讯朱雀实验室（Tencent Zhuque Lab）披露，8 月 6 日公开。已在上游修复（commit 9b2854f86f0b），并回溯至稳定内核 6.6.148、6.12.101、6.18.42、7.1.6（8 月 3 日发布）。对使用者：运行容器化工作负载的 Kubernetes 节点应尽快升级内核到上述修复版本；该漏洞已知可在 Debian 13、Ubuntu 24.04、Rocky Linux 9、RHEL 9、OpenCloudOS 上验证利用。来源：[Tencent Zhuque Lab](https://matrix.tencent.com/en/2026/08/06/sctphantom-CVE-2026-64564)、[The Hacker News](https://thehackernews.com/2026/08/18-year-old-linux-sctp-flaw-could-let.html)
