# ☁️ 云原生周报 · 2026-11-06

> 覆盖窗口：2026-10-31 11:32 UTC 至 2026-11-06 16:22 UTC（常规）

今日要闻：AWS 发布 EKS 安全公告 2026-170-AWS 修复 VPC CNI Network Policy Agent eBPF 连接跟踪隔离绕过漏洞（CVE-2026-122266，CVSS 8.7），并发布优化版 AL2023 AMI v20261031 修复 Linux 内核 IPv4 TCP 远程代码执行漏洞（CVE-2026-98432）。

## 需要行动

- AWS EKS 安全公告 2026-170-AWS（CVE-2026-122266 / GHSA-mm5f-ggvx-hmvw，CVSS 8.7 高危）：2026-11-04 AWS 披露 Amazon EKS Network Policy Agent（`aws-network-policy-agent` < 1.3.7，随 Amazon VPC CNI 托管附加组件 < 1.22.3 分发）存在共享 eBPF 连接跟踪（conntrack）状态隔离不当漏洞，同节点（co-located）Pod 内的已认证相邻攻击者可构造特制 `AF_PACKET` 帧污染 eBPF conntrack 映射表，绕过同节点 Pod 的 Kubernetes `NetworkPolicy` 入站隔离策略；官方已发布 `aws-network-policy-agent` v1.3.7 与 Amazon VPC CNI 托管附加组件 v1.22.3（SageMaker HyperPod 增强子网发现场景建议直升 v1.22.4），无配置层临时缓解手段，且 v1.3.7 升级了内部 Pod 标识符格式（升级自动迁移，但若回滚至旧版则回滚前创建的 Pod 将失去策略保护直至节点替换）。影响：你在用 AWS EKS，若集群启用了 VPC CNI NetworkPolicy 且附加组件版本低于 v1.22.3（或独立部署的 `aws-network-policy-agent` 低于 v1.3.7），同节点跨命名空间 Pod 入站网络隔离可被绕过。动作：核查集群 Amazon VPC CNI 附加组件版本及是否启用 NetworkPolicy，若受影响则升级至 v1.22.3 及以上（内含 `aws-network-policy-agent` v1.3.7）。来源：AWS Security Bulletins https://aws.amazon.com/security/security-bulletins/2026-170-aws/
- AWS 安全公告 2026-160-AWS（Linux 内核 CVE-2026-98432）与 EKS 优化版 AL2023 AMI v20261031：2026-10-31 AWS 发布公告响应 Linux 内核（4.4 及以上版本）IPv4 TCP 握手路径 `inet_opt`/`ireq_opt` RCU 释放竞态与释放后重用（use-after-free）高危漏洞（CVE-2026-98432），远程未认证攻击者可向受影响监听端口发送含 IP 选项的特制 TCP 报文触发内核崩溃、内存损坏，或在启用多路径 TCP（MPTCP）监听的主机上实现远程代码执行（RCE）；EKS 托管控制面及 11-01 后启动的 Fargate Pod 已由 AWS 自动修补，EKS 同日发布含修复内核的优化版 Amazon Linux 2023 AMI `v20261031`（基于 `2023.12.20261102.0` 最小基础镜像，覆盖 K8s 1.31–1.37）。影响：你的 EKS 工作节点共享宿主机 Linux 内核，尚未轮换至 `v20261031` 及以后 AMI 的托管节点组、自管节点或 Karpenter 节点面临远程内核崩溃或潜在 RCE 风险。动作：将 EKS 工作节点滚动更新至优化版 AMI `v20261031` 及以上版本并重启生效；暂无法轮换节点时可通过 sysctl 设置 `net.mptcp.enabled=0` 禁用 MPTCP 以阻断已知 RCE 利用路径。来源：AWS Security Bulletins https://aws.amazon.com/security/security-bulletins/2026-160-aws/
- 【续报】Kyverno CVE-2026-122300~122323（v1.19.2 批次安全公告正式分配 CVE 编号）：2026-11-03 至 11-05 期间，NVD 与 GitHub Security Advisories 为 10 月下旬随 Kyverno v1.19.2 披露的批量安全公告正式分配 `CVE-2026-122300` 至 `CVE-2026-122323` 编号，其中核心严重级（CVSS 9.1–9.9）对应关系为：`CVE-2026-122310`（GHSA-3xfv-vq8x-qhg4，Policy `apiCall` `urlPath` 查询串/锚点隐藏 `../` 路径穿越提权至集群管理员，CVSS 9.4/9.9）、`CVE-2026-122311`（GHSA-4pqm-wqq6-h9q2，命名空间 CEL 策略 `resource.get()`/`resource.post()` 路径穿越致集群接管，CVSS 9.9）、`CVE-2026-122303` 与 `CVE-2026-122313`（GHSA-jcw5-3wcg-fqx5 / GHSA-f96w-622v-rqpq，`NamespacedMutatingPolicy` `mutate-existing` 目标表达式跨命名空间覆写与提权，均 CVSS 9.9）、`CVE-2026-122304`（GHSA-p58h-r4j3-h5vx / GHSA-rcxg-3f92-3mgr，`CleanupPolicy` 上下文加载器 nil policy 跨命名空间越权，CVSS 9.9）、`CVE-2026-122321`（GHSA-2r43-6962-xcw5，`verifyImages` 按可变 tag 缓存验签结果致镜像验签绕过，CVSS 9.1），以及 `CVE-2026-122305`/`122306`/`122309`/`122322`/`122323` 等变量循环替换、指数级通配符匹配、CEL 推导式与验签层解压 OOM 准入 DoS 漏洞；上述问题均已随 v1.19.2（2026-10-20）修复，修复动作未变。影响：正式 CVE 编号入库后，依赖 CVE 编号匹配的漏洞扫描与合规工具将集中告警；你的 Kyverno 版本未确认，凡低于 v1.19.2（含 v1.19.1）均在受影响范围内。动作：核实当前 Kyverno 版本并升级至 v1.19.2（Helm chart 3.9.2），升级前检查 CEL PolicyException 是否符合 `exceptionNamespace` 校验要求，并收紧命名空间级策略创建权限。来源：GitHub Security Advisories https://github.com/kyverno/kyverno/security/advisories/GHSA-3xfv-vq8x-qhg4

## 栈位差

| 组件 | 我在用 | 当前最新 | 落后 | 支持窗口 | 我方版本确认日 |
| --- | --- | --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本 | 1.37 | —，实际版本未确认 | 我方剩余支持期未确认；1.37 标准支持至 2027-12-01，延长支持至 2028-12-01；https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html | 2026-08-14 |
| Kubernetes | 同 EKS 控制面版本 | 1.37.2 | —，实际版本未确认 | 上游支持最近三个 minor；1.34 已于 2026-10-27 EOL，不能据此推断 EKS 1.34 已停服；https://kubernetes.io/releases/ | 2026-08-14 |
| Istio（主） | 1.25 | 1.31.3 | 6 个 minor | 已出窗口（1.25 于 2025-09-30 EOL）；https://istio.io/latest/docs/releases/supported-releases/ | 2026-08-14 |
| Istio（遗留） | 1.16 | 1.31.3 | 15 个 minor | 已出窗口（1.16 于 2023-07-25 EOL）；https://istio.io/latest/docs/releases/supported-releases/ | 2026-08-14 |
| Flux CD | 未确认 | 2.10.0 | — | 我方支持状态未确认；当前版支持 Kubernetes 最近三个 minor（最低补丁 1.35.2／1.36.1／1.37.0）；https://github.com/fluxcd/flux2/releases/tag/v2.10.0 | — |
| Kustomize | 未确认 | 5.8.3 | — | 未确认；版本来源 https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize/v5.8.3 | — |
| Helm | 未确认 | 4.3.1／3.22.1 | — | 我方支持状态未确认；版本来源 https://github.com/helm/helm/releases | — |
| Kyverno | 未确认 | 1.19.2 | — | 我方支持状态未确认；版本来源 https://github.com/kyverno/kyverno/releases/tag/v1.19.2 | — |
| SOPS | 未确认 | 3.13.3 | — | 未确认；版本来源 https://github.com/getsops/sops/releases/tag/v3.13.3 | — |
| AWS Load Balancer Controller | 未确认 | 3.6.2 | — | 未确认；版本来源 https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.2 | — |
