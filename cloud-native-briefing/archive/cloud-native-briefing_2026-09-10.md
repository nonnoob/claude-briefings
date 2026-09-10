# ☁️ 云原生周报 · 2026-09-10

> 覆盖窗口：2026-08-31 至 2026-09-10（补漏：距上次运行 2026-08-17 已超 10 天封顶，窗口外仅收至今仍重要大事）

## 需要行动

- Kyverno GHSA-5qq8-67g6-4h2w（CVSS 9.9 严重）：2026-09-10 官方披露 apiCall urlPath 路径校验绕过，命名空间租户可提权至集群管理员；同日另有 4 个高危 GHSA（SSRF、镜像签名校验绕过、跨命名空间上下文读取），均已随 v1.19.1 修复。影响：多租户集群中任何具备 Policy 创建权限的命名空间用户可越权控制全集群准入配置；你方 Kyverno 版本未确认，凡低于 v1.19.1 均在受影响范围。动作：核实当前 Kyverno 版本并升级至 v1.19.1。来源：GitHub Security Advisories https://github.com/kyverno/kyverno/security/advisories/GHSA-5qq8-67g6-4h2w
- Istio ISTIO-SECURITY-2026-006（整体 CVSS 7.7）：2026-08-27 官方公告确认 EnvoyFilter proxyVersion 正则未限长可致 istiod 拒绝服务，官方注明连未在支持窗口内的旧版本（含你在用的 1.25）同样受影响；已随 1.30.4/1.29.7 修复，但 1.25 因已出支持窗口不会获得回补。影响：具备本命名空间 EnvoyFilter 创建权限的租户可构造超长正则使 istiod 配置下发全局中断。动作：收紧 EnvoyFilter 创建/更新权限至可信管理员（配置层缓解，无需等版本修复）。来源：Istio Security Bulletin https://istio.io/latest/news/security/istio-security-2026-006/
- Istio 制品托管迁移（GCP 退役）：1.31 起停止向 gcr.io/istio-release、registry.istio.io 及旧 GCS bucket 发布镜像与 Helm chart，断供测试分批定于 2026-09-15/10-13/11-17/12-08 执行。影响：无论你在用哪个 Istio 版本，只要 CI/CD 或集群仍从上述旧地址拉取镜像或 chart，2026-09-15 起的首次断供测试窗口就会导致拉取失败。动作：核实并将镜像源切至 Docker Hub、Helm chart 源切至 blob.istio.io/ghcr.io。来源：Istio 1.31 Upgrade Notes https://istio.io/latest/news/releases/1.31.x/announcing-1.31/upgrade-notes/

## 留意

- Kubernetes v1.37「Garhwal」：2026-08-26 正式 GA，含静态 Pod 禁止引用 Secret/ConfigMap、cgroup v1 节点 kubelet 拒绝启动、IPVS kube-proxy 模式进入弃用倒计时等破坏性变更；Amazon EKS 目前最高仅支持至 1.36，尚未纳入 1.37。影响：这些破坏性变更暂不会命中你的 EKS 集群。动作：暂无，等 EKS 官宣支持 1.37。来源：Kubernetes Blog https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/
- Amazon EKS 新增控制面参数配置能力：可调整 kube-scheduler/controller-manager/API server 参数（如调度器资源打分策略、HPA 响应速度、事件保留时长），已覆盖所有区域。影响：为可选新能力，不影响现有集群运行方式。动作：暂无，等你评估是否需要启用具体参数调优。来源：AWS What's New https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-control-plane-configuration-parameters/
- Flux CD v2.9.5：2026-08-31 发布，新增 kubeconfig Secret 校验，拒绝引用本地文件路径的证书/密钥（防御性加固，未编号漏洞），同步将 Helm 依赖迁回上游 v4.2.4。影响：若 HelmRelease/Kustomization 通过 kubeConfig Secret 引用本地文件路径证书，升级后会报错。动作：暂无，等你核实 fleet 内是否存在此类引用方式。来源：GitHub Releases https://github.com/fluxcd/flux2/releases/tag/v2.9.5
- 【单源】Helm v3 线路进入纯维护期：v3.22.0（2026-09-10）被官方定位为 v3 计划内最后一个 minor 版本，此后仅发安全补丁；v4 线路同步发布 v4.3.0（2026-09-09）。影响：长期使用 v3 将不再获得新特性，现有功能不受影响。动作：暂无，等你评估是否规划迁移至 v4。来源：GitHub Releases https://github.com/helm/helm/releases/tag/v3.22.0
- AWS Load Balancer Controller v3.5.0：2026-08-03 发布，Gateway API L4 路由（TCPRoute/UDPRoute）转正需 Gateway API CRD ≥1.6.0 且不再服务 v1alpha2，未同步升级 CRD 会导致 NLB Gateway 功能被控制器自动禁用。影响：若你用 Gateway API 管理 NLB 且尚未同步升级 CRD 与迁移 v1alpha2 清单，升级 controller 时会中断。动作：暂无，等你确认当前 controller 版本与 Gateway API CRD 版本是否已同步升级。来源：GitHub Releases https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.5.0
- SOPS Vault/OpenBao allowlist 默认值预告收紧：官方在 GHSA-jgf3-f6rg-8x3h 中预告 SOPS_HC_VAULT_ALLOWLIST 默认值将从 all 改为 none（可能不随大版本号发布），当前最新 v3.13.3（2026-07-23）仍是默认 all。影响：若你的解密链路依赖 Vault/OpenBao 且未显式设置该变量，届时可能突然拒绝解密。动作：暂无，等该默认值变更随具体版本落地。来源：GitHub Security Advisory https://github.com/getsops/sops/security/advisories/GHSA-jgf3-f6rg-8x3h

## 其他动态

- Argo CD 曝未认证 RCE，尚无补丁，可自查 Flux 内部服务暴露面。来源：The Hacker News https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html

## 趋势

- SOPS 面临 CNCF 治理风险：TOC 自 2026-03 起评估其 MPL 许可证与 CNCF 首选的 Apache-2.0 不兼容，尚无定论，可能导致其被要求重新授权、迁出 CNCF 或转入其他基金会。这威胁的是你密钥加密链路核心工具的长期维护与生态背书，与当下功能无关，但决定它未来是否仍受信任治理框架约束。来源：GitHub cncf/toc Issue #2098 https://github.com/cncf/toc/issues/2098
- Kyverno 的 apiCall/CEL 策略执行链全年反复出现命名空间隔离与提权漏洞（CVE-2026-22039→41068→54523→本次批次一脉相承），提示应默认限制 apiCall/GlobalContextEntry/CEL 策略类型的创建权限作为结构性缓解，而非仅逐次等补丁——这威胁的是策略引擎这层"信任边界"本身的可信度。来源：GitHub Security Advisories https://github.com/kyverno/kyverno/security/advisories

## 栈位差

| 组件 | 我在用 | 当前最新 | 落后 | 支持窗口 | 我方版本确认日 |
| --- | --- | --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本（未给具体版本号） | 1.36（上游 1.37 已 GA，EKS 尚未跟进） | — | — | 2026-08-14 |
| Kubernetes 本体 | 同 EKS 控制面版本（未给具体版本号） | v1.37「Garhwal」（2026-08-26 GA） | — | — | 2026-08-14 |
| Istio（主） | 1.25 | 1.31.0（2026-08-31） | 6 档 | 已出窗口（自 2025-09-22 起） | 2026-08-14 |
| Istio（遗留） | 1.16 | 1.31.0 | 15 档 | 已出窗口（自 2023-07-25 起） | 2026-08-14 |
| Flux CD | 未确认 | v2.9.5（2026-08-31） | — | — | — |
| Kustomize | 未确认 | v5.8.1（2026-02-09） | — | — | — |
| Helm | 未确认 | v4.3.0 / v3.22.0（v3 线路计划内最后一个 minor 版本） | — | — | — |
| Kyverno | 未确认 | v1.19.1（2026-09-10） | — | — | — |
| SOPS | 未确认 | v3.13.3（2026-07-23） | — | — | — |
| AWS Load Balancer Controller | 未确认 | v3.5.0（2026-08-03） | — | — | — |
