# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻：2026-10-05 10:51 UTC。
- 上次运行时刻：2026-09-28 10:51 UTC，间隔约 7.0 天。
- 实际覆盖窗口：2026-09-28 10:51 UTC – 2026-10-05 10:51 UTC（常规）。
- 方向 A 六项均已核查；istio.io、aws.amazon.com 直连被出网代理拦截，改用 WebSearch 与 GitHub Releases 交叉核实。结果：EKS 于 2026-10-01 正式支持 K8s 1.37（收录为"留意"续报，事件闭合）；Istio ISTIO-SECURITY-2026-006（含 Envoy CVE）实为 2026-08-27 随 1.29.7/1.30.4 发布，早于窗口，不收；Istio 无新版本（最新 1.31.1）；Kubernetes 无新稳定版（v1.37.1，另有 v1.38.0-alpha.1 不收）；Flux 发布 v2.9.6（2026-10-01，仅缺陷修复，不触发判定，仅更新栈位差）；Kyverno v1.19.1、SOPS v3.13.3、ALBC v3.5.0 无新版本；Kustomize 页面显示 v5.8.2，发布日期无法确认；Helm 无新版本（v4.3.1/v3.22.1 计划 2026-10-14）。方向 B/C 未检出满足门槛的内容。
- 本期新增"留意"1 条（EKS 1.37），无"需要行动"。
- 版本清单已 52 天未复核，未超 90 天，未写超期提示。
- 进行中事件表：EKS 1.37 事件闭合移出；Istio GCP 退役事件本期仍无法确认 9/15 结果（istio.io 受限），保留。

## 2. 已报条目清单（最近 21 天）

2026-09-09~10 | Helm v4.3.0 与 v3.22.0 发布，官方将 v3.22.0 定位为 v3 线路计划内最后一个 minor 版本 | https://github.com/helm/helm/releases/tag/v3.22.0
2026-09-10 | Kyverno v1.19.1 发布，同日修复 5 个安全公告，含 CVSS 9.9 严重级 apiCall urlPath 命名空间逃逸至集群管理员提权漏洞 GHSA-5qq8-67g6-4h2w | https://github.com/kyverno/kyverno/security/advisories/GHSA-5qq8-67g6-4h2w
2026-09-21 | Istio 1.29.8/1.30.5/1.31.1 发布，修复 BackendTLSPolicy CA 未解析时明文降级问题 GHSA-qm8v-g4f9-qhjx | https://github.com/istio/istio/security/advisories/GHSA-qm8v-g4f9-qhjx
2026-09-26 | Kyverno 09-10 批次 5 个 GHSA 正式获分配 CVE 编号（CVE-2026-100703~100707，含 CVSS 9.9 的 100706） | https://github.com/kyverno/kyverno/security/advisories/GHSA-5qq8-67g6-4h2w
2026-10-01 | AWS 宣布 EKS 与 EKS Distro 正式支持 Kubernetes 1.37 | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-distro-kubernetes-version-1-37/

## 3. 进行中事件表

- 事件：Istio GCP 制品托管退役（gcr.io/istio-release 等旧地址断供）| 最后进展日期：2026-08-31（1.31 发布，宣布断供计划）| 下一步关注点：确认 2026-09-15 首次 scream test 的实际结果（istio.io 访问受限，连续三期未能确认），并继续关注 2026-10-13、2026-11-17、2026-12-08 后续窗口。

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
