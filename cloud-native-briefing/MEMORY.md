# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻及检索截止：2026-11-16 10:50 UTC。
- 实际覆盖窗口：2026-11-09 21:50 UTC 至 2026-11-16 10:50 UTC（常规）。
- 方向 A 通过 GitHub Releases 核查：Kyverno v1.20.0（11-12）收录至「留意」；Istio 1.32.0（11-09 发布，时刻未确认，未收条目，仅入栈位差）；AWS LBC v3.6.3（11-13，Go/x/net 安全重建）、Helm v4.3.2（11-13）为常规补丁，仅入栈位差；Kubernetes 仍为 1.37.2，Flux v2.10.0、Kustomize v5.8.3、SOPS v3.13.3 无新版。
- 本期未覆盖：istio.io、kubernetes.io、aws.amazon.com 在本会话网络下不可达，Istio 1.32 发布说明、Kubernetes 官方公告、AWS/EKS 安全公告与 What's New 未能核查；方向 B/C 仅靠 WebSearch 浅查，无达标事件。Istio ISTIO-SECURITY-2026-009 的 8 项 GHSA 的 CVE 编号分配本期未能确认。
- 版本清单确认日（2026-08-14）距本期 94 天，已超 90 天，简报已附提示；第 4 节原样保留。

## 2. 已报条目清单（最近 21 天）

## 2. 已报条目清单（最近 21 天）
2026-10-31 | Flux v2.10.0 聚合版本正式发布，落实 Notification v1 与默认 token RBAC 变更，最低 Kubernetes 补丁为 1.35.2/1.36.1/1.37.0 | https://github.com/fluxcd/flux2/releases/tag/v2.10.0
2026-10-31 | AWS 发布安全公告 2026-160-AWS（Linux 内核 IPv4 TCP 握手路径 RCU 释放后重用漏洞 CVE-2026-98432）与 EKS 优化版 AL2023 AMI v20261031 | https://aws.amazon.com/security/security-bulletins/2026-160-aws/
2026-11-04 | AWS 发布 EKS 安全公告 2026-170-AWS（CVE-2026-122266 / GHSA-mm5f-ggvx-hmvw，CVSS 8.7），修复 VPC CNI Network Policy Agent（< 1.3.7 / VPC CNI < 1.22.3）共享 eBPF conntrack 状态隔离绕过漏洞 | https://aws.amazon.com/security/security-bulletins/2026-170-aws/
2026-11-05 | NVD 与 GitHub Security Advisories 为 Kyverno v1.19.2 批次安全公告正式分配 CVE-2026-122300 至 CVE-2026-122323 编号 | https://github.com/kyverno/kyverno/security/advisories/GHSA-3xfv-vq8x-qhg4
2026-11-06 | Istio 发布安全公告 ISTIO-SECURITY-2026-009（8 项 GHSA，最高 CVSS 8.2）与 1.31.4/1.30.8 补丁，修复 istiod 调试 xDS 请求崩溃循环、Sidecar conntrack 流量劫持绕过、AuthorizationPolicy 主机头大小写敏感绕过及 Ambient mTLS 绕过等漏洞 | https://istio.io/latest/news/security/istio-security-2026-009/
2026-11-09 | NVD 与 CVE.org 为 Kyverno v1.19.2 批次剩余两项多租户越权公告 GHSA-39w8-hv5g-f73w 与 GHSA-vjfx-fp68-rh4v 正式分配 CVE-2026-124440（CVSS 9.9）与 CVE-2026-124441（CVSS 8.8） | https://github.com/kyverno/kyverno/security/advisories/GHSA-39w8-hv5g-f73w
2026-11-09 | AWS 宣布 Amazon EKS 支持 AWS Nitro Sandboxes，通过 Kubernetes RuntimeClass 提供基于 Nitro Hypervisor 的 Pod 级微虚拟机硬件隔离与密码学证明 | https://aws.amazon.com/blogs/containers/aws-nitro-sandboxes-hardware-enforced-workload-isolation-on-amazon-eks/
2026-11-12 | Kyverno 发布 v1.20.0，删除旧版 kyverno.io 策略引擎、拒绝旧版策略创建与更新，并含多项 CVE 依赖修复 | https://github.com/kyverno/kyverno/releases/tag/v1.20.0

## 3. 进行中事件表

- 事件：Istio GCP 制品托管退役（gcr.io/istio-release 等旧地址断供）| 最后进展日期：2026-10-13（第二轮 3 小时 scream test 窗口执行）| 下一步关注点：关注 2026-11-17（6 小时）与 2026-12-08（24 小时）后续 scream test 及 12 月正式关停公告。
- 事件：Istio ISTIO-SECURITY-2026-009（8 项 GHSA）正式 CVE 编号分配 | 最后进展日期：2026-11-06（安全公告与 GHSA 发布）| 下一步关注点：关注 GHSA-rr2c-p22p-6r9r、GHSA-635j-qv98-9275、GHSA-cxwg-46mx-q8hf、GHSA-7m6f-j3gp-2r53 等 8 项安全公告在 NVD 与 GitHub Security Advisories 的正式 CVE 编号分配（本期未能核查）。
- 事件：Kyverno v1.20.0 移除旧版策略引擎 | 最后进展日期：2026-11-12 | 下一步关注点：关注 v1.20.x 首个补丁版本及升级路径问题反馈。

## 4. 读者在用的版本清单

栈位差表"我在用"一列的唯一数据源。**本节只由读者手动更新，定时任务不得改写其中的版本值与确认日期。**

| 组件 | 我在用 | 确认日期 | 备注 |
| --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本 | 2026-08-14 | 读者口径为"最新版"，未给具体控制面版本号；下次复核时填入实际版本，否则"距 EOL ≤ 3 个月"这条判定无法精确计算 |
| Kubernetes | 同 EKS 控制面版本 | 2026-08-14 | 不独立维护版本号 |
| Istio（主） | 1.25 | 2026-08-14 | |
| Istio（遗留） | 1.16 | 2026-08-14 | 已出官方支持窗口。只在栈位差表中列示，不为它单独检索、不做迁移追踪 |
| Flux CD | 未确认 | — | |
| Kustomize | 未确认 | — | |
| Helm | 未确认 | — | |
| Kyverno | 未确认 | — | |
| SOPS | 未确认 | — | |
| AWS Load Balancer Controller | 未确认 | — | |
