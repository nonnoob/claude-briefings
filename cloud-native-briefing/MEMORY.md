# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻及检索截止：2026-11-06 16:22 UTC（2026-11-06 08:22 PST）。
- 实际覆盖窗口：2026-10-31 11:32 UTC 至 2026-11-06 16:22 UTC（常规）。
- 方向 A 六项通过官方 Releases、安全公告与 GitHub Security Advisories 核查：AWS 于 2026-11-04 发布安全公告 `2026-170-AWS`（CVE-2026-122266 / GHSA-mm5f-ggvx-hmvw，CVSS 8.7），修复 Amazon EKS Network Policy Agent（`< 1.3.7` / Amazon VPC CNI 附加组件 `< 1.22.3`）共享 eBPF conntrack 状态隔离不当致同节点 Pod 绕过 NetworkPolicy 入站策略问题；AWS 于 2026-10-31 发布安全公告 `2026-160-AWS`（Linux 内核 IPv4 TCP 握手路径 RCU 释放后重用高危漏洞 CVE-2026-98432）并同步推出 EKS 优化版 AL2023 AMI `v20261031`；NVD 与 GitHub Security Advisories 于 2026-11-03 至 11-05 期间为 Kyverno v1.19.2 批次安全公告正式分配 `CVE-2026-122300` 至 `CVE-2026-122323` 编号（含 CVE-2026-122310、CVE-2026-122311、CVE-2026-122303、CVE-2026-122304、CVE-2026-122313、CVE-2026-122321 等严重级漏洞），以【续报】收录并闭合对应追踪项。
- 其余 watchlist 组件：Kubernetes 最新稳定版仍为 1.37.2（11 月补丁版目标日为 11-10）；Istio 最新稳定版仍为 1.31.3（1.32.0 尚处 RC 阶段）；Flux CD 最新仍为 v2.10.0；Kustomize 仍为 v5.8.3；Helm 仍为 v4.3.1 / v3.22.1（下一补丁计划 11-11）；Kyverno 仍为 v1.19.2；SOPS 仍为 v3.13.3；AWS Load Balancer Controller 仍为 v3.6.2。AWS EKS 于 11-03 宣布 EKS Capabilities 支持 Argo CD Notifications，因读者使用 Flux CD 且仅属托管 Argo CD 增量通知特性，未达方向 B 替代威胁门槛，不收。方向 B/C 本期无达标新事件。
- 版本清单确认日（2026-08-14）距本期 84 天，未超 90 天；第 4 节原样保留。
- 已报条目清单：按最近 21 天窗口（2026-10-16 至 2026-11-06）保留，移出已满 22 天的 2026-10-15 条目 2 条。进行中事件表：Kyverno v1.19.2 批次 CVE 编号分配已随本期续报闭合移出；ISTIO-SECURITY-2026-007 四项 GHSA 自 2026-10-15 起已满 22 天仍未分配正式 CVE 编号，按连续 21 天无新进展规则移出；保留 Istio GCP 制品托管退役（待 2026-11-17 第三轮 6 小时 scream test）。

## 2. 已报条目清单（最近 21 天）

2026-10-20 | Kyverno 发布 v1.19.2 并批量披露 26 项 GHSA 安全公告（含 GHSA-3xfv-vq8x-qhg4、GHSA-39w8-hv5g-f73w 等 11 项 CVSS 9.1–9.9 严重级多租户提权与镜像验签绕过漏洞），同时对 CEL PolicyException 强制校验 exceptionNamespace | https://github.com/kyverno/kyverno/releases/tag/v1.19.2
2026-10-21 | Istio 发布安全公告 ISTIO-SECURITY-2026-008（CVE-2026-111943）与 1.31.3/1.30.7/1.29.10，吊销私钥泄露的 8 个 eMudhra 中间 CA 证书信任并修复自签名根证书过期启动失败问题 | https://istio.io/latest/news/security/istio-security-2026-008/
2026-10-24 | Flux CD 各核心控制器先行发布 v1.10.0 / v1.7.0（Notification API 升 v1、Object Identity 转正并收紧默认 serviceaccounts/token RBAC、引入控制器间 SPIFFE mTLS、支持 HelmRelease OCIRepository 模板及 SOPS 注释正则解密） | https://github.com/fluxcd/notification-controller/releases/tag/v1.10.0
2026-10-25 | AWS Load Balancer Controller 发布 v3.6.1 与 v3.6.2，新增对账状态指标、修复安全组释放 InvalidGroup.NotFound 对账死循环、移除失信 eMudhra 根证书并优化 Gateway 首次缓存同步性能 | https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.2
2026-10-31 | Flux v2.10.0 聚合版本正式发布，落实 Notification v1 与默认 token RBAC 变更，最低 Kubernetes 补丁为 1.35.2/1.36.1/1.37.0 | https://github.com/fluxcd/flux2/releases/tag/v2.10.0
2026-10-31 | AWS 发布安全公告 2026-160-AWS（Linux 内核 IPv4 TCP 握手路径 RCU 释放后重用漏洞 CVE-2026-98432）与 EKS 优化版 AL2023 AMI v20261031 | https://aws.amazon.com/security/security-bulletins/2026-160-aws/
2026-11-04 | AWS 发布 EKS 安全公告 2026-170-AWS（CVE-2026-122266 / GHSA-mm5f-ggvx-hmvw，CVSS 8.7），修复 VPC CNI Network Policy Agent（< 1.3.7 / VPC CNI < 1.22.3）共享 eBPF conntrack 状态隔离绕过漏洞 | https://aws.amazon.com/security/security-bulletins/2026-170-aws/
2026-11-05 | NVD 与 GitHub Security Advisories 为 Kyverno v1.19.2 批次安全公告正式分配 CVE-2026-122300 至 CVE-2026-122323 编号 | https://github.com/kyverno/kyverno/security/advisories/GHSA-3xfv-vq8x-qhg4

## 3. 进行中事件表

- 事件：Istio GCP 制品托管退役（gcr.io/istio-release 等旧地址断供）| 最后进展日期：2026-10-13（第二轮 3 小时 scream test 窗口执行）| 下一步关注点：关注 2026-11-17（6 小时）与 2026-12-08（24 小时）后续 scream test 及 12 月正式关停公告。

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
