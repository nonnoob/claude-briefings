# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻：2026-09-28 10:51 UTC。
- 上次运行时刻：2026-09-21 10:51 UTC，间隔约 7.0 天，未超 10 天封顶。
- 实际覆盖窗口：2026-09-21 10:51 UTC – 2026-09-28 10:51 UTC（常规）。
- 方向 A（watchlist）六项逐一核查：Kubernetes 本体、AWS EKS、Istio、Flux CD 及各 controller/Kustomize/Helm、Kyverno/SOPS、AWS Load Balancer Controller/NLB。istio.io、kubernetes.io 直连 WebFetch 仍被出网代理拦截，改用 WebSearch 与 GitHub Releases/Security Advisories/PR 页面交叉核实替代，未造成方向缺失，按"全量覆盖"落盘。核查结果：Kubernetes 本体发布 v1.37.1（2026-09-23），纯缺陷修复（DeviceTaintRule 匹配、Windows kube-proxy 崩溃、DRA 调度器 panic、kubeadm 配置），无 CVE，不影响读者（EKS 仍在 1.36）；AWS EKS 管理控制面仍未支持上游 1.37（最高 1.36），但 EKS Distro 已于 2026-09-22 放出 1.37 预览包（v1-37-eks-3），GA 尚未官宣；Istio 发布 1.29.8/1.30.5/1.31.1（2026-09-21），修复 GHSA-qm8v-g4f9-qhjx（BackendTLSPolicy CA 未解析时明文降级，CVSS 6.8）——该特性需 Istio ≥1.28 稳定支持，读者主集群 1.25 不具备，不受影响，收录为"留意"；1.32 尚在准备中（issue #61724）未发布；Flux CD/Kustomize/Helm 均无新版本（分别停留在 v2.9.5、v5.8.1、v4.3.0/v3.22.0）；Kyverno 无新版本，但 2026-09-26 官方为 09-10 披露的 5 个 GHSA 正式分配 CVE 编号（CVE-2026-100703~100707，含 CVSS 9.9 的 100706），均已随 v1.19.1 修复，收录为"需要行动"续报；SOPS 无新版本（v3.13.3）；AWS Load Balancer Controller 无新版本（v3.5.0）。另检出 AWS Security Bulletin 2026-113（CVE-2026-86831，EKS Network Policy Agent 跨命名空间授权绕过，CVSS 8.7，修复版本 aws-network-policy-agent v1.4.0/VPC CNI v1.22.4 早已于 2026-07-22 发布），但该公告披露日期为 2026-09-16，落在上期（2026-09-14~09-21）覆盖窗口内而非本期，且上期未收录；按"只收录发布时间落在覆盖窗口内的内容"规则，本期不追溯补报，不在简报正文体现，仅在此记录供排查用。方向 B/C 全量核查（供应链攻击、CNCF 项目状态、同栈事故复盘、替代技术威胁四类）：检出 CNCF Karmada 正式毕业公告、K8s CVE 记录历史漏报修正报道（bex.co, 09-26）等，均因不落在读者生产栈或不构成新增可执行信息而未收录。方向 D 栈位差表全量复核并更新（K8s 本体、Istio 主/遗留最新版本号刷新）。
- 本期新增"需要行动"1 条（Kyverno CVE 编号分配，续报）、"留意"1 条（Istio BackendTLSPolicy fail-open）。
- 进行中事件表本期核查结果：3 条全部定向核查。①Istio GCP 制品托管退役——istio.io 直连仍被拦截，GitHub issue #61467 无新评论，本期仍未能确认 2026-09-15 首次 scream test 的实际结果，保留待下次，下一步关注点维持"确认 9/15 结果 + 等 10/13 第二次 scream test"。②Kyverno apiCall/CEL 命名空间隔离漏洞模式——本期等到的"后续 CVE 编号分配"已发生（见上），事件闭合，移出本表；若后续再现同类新 CVE 将作为新条目收录。③EKS 是否支持 K8s 1.37——仍未支持（最高 1.36），但 EKS Distro 已放出 1.37 预览包，出现新进展，最后进展日期更新为 2026-09-22，下一步关注点维持"等 AWS 官宣 EKS 托管控制面支持 1.37"。
- 已报条目清单：按 21 天窗口（截至 2026-09-28，含 2026-09-07 及以后）保留，移出 2026-08-31（Istio 1.31.0 发布）、2026-08-31（Flux CD v2.9.5）共 2 条过期条目。
- 推送：本会话被限定只能推送指定工作分支（云端 Routine 会话平台限制，无法直接推 main），按 SKILL.md 兜底流程推当前工作分支，依赖仓库内 auto-merge 工作流合并进 main。

## 2. 已报条目清单（最近 21 天）

2026-09-09~10 | Helm v4.3.0 与 v3.22.0 发布，官方将 v3.22.0 定位为 v3 线路计划内最后一个 minor 版本 | https://github.com/helm/helm/releases/tag/v3.22.0
2026-09-10 | Kyverno v1.19.1 发布，同日修复 5 个安全公告，含 CVSS 9.9 严重级 apiCall urlPath 命名空间逃逸至集群管理员提权漏洞 GHSA-5qq8-67g6-4h2w | https://github.com/kyverno/kyverno/security/advisories/GHSA-5qq8-67g6-4h2w
2026-09-21 | Istio 1.29.8/1.30.5/1.31.1 发布，修复 BackendTLSPolicy CA 未解析时明文降级问题 GHSA-qm8v-g4f9-qhjx | https://github.com/istio/istio/security/advisories/GHSA-qm8v-g4f9-qhjx
2026-09-26 | Kyverno 09-10 批次 5 个 GHSA 正式获分配 CVE 编号（CVE-2026-100703~100707，含 CVSS 9.9 的 100706） | https://github.com/kyverno/kyverno/security/advisories/GHSA-5qq8-67g6-4h2w

## 3. 进行中事件表

- 事件：Istio GCP 制品托管退役（gcr.io/istio-release 等旧地址断供）| 最后进展日期：2026-08-31（1.31 发布，宣布断供计划）| 下一步关注点：确认 2026-09-15 首次 scream test 的实际结果（istio.io 访问受限，GitHub issue #61467 无新评论，连续两期未能确认），并继续关注 2026-10-13、2026-11-17、2026-12-08 后续窗口。
- 事件：Amazon EKS 是否/何时支持 Kubernetes 1.37 | 最后进展日期：2026-09-22（EKS Distro 放出 1.37 预览包 v1-37-eks-3，托管控制面仍未支持）| 下一步关注点：等 AWS What's New 官宣 EKS 托管控制面支持 1.37，届时 1.37 的破坏性变更（静态 Pod Secret/ConfigMap 引用禁令、cgroup v1 kubelet 拒启等）转为对读者实际可命中。

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
