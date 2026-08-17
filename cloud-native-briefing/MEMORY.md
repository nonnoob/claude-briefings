# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻：2026-08-17 12:49 UTC。
- 上次运行时刻：2026-08-14 18:22 UTC，间隔约 2 天 18 小时。
- 实际覆盖窗口：2026-08-14 18:22 UTC – 2026-08-17 12:49 UTC（常规）。
- 方向 A（watchlist）六项逐一核查：Kubernetes 本体、AWS EKS、Istio、Flux CD 及各 controller/Kustomize/Helm、Kyverno/SOPS、AWS Load Balancer Controller/NLB，均取得有效检索结果（部分官方站点 istio.io/aws.amazon.com/docs.aws.amazon.com 被沙箱出网代理拦截，改用 WebSearch 与 GitHub Releases/Security Advisories 交叉验证补齐，未造成方向缺失）。方向 B/C 全量核查，窗口内无满足门槛内容。方向 D 栈位差表全量刷新。
- 本期发现两项需要行动：① Istio 1.25（读者主网格版本）经核实官方支持已于 2025-09-22 结束，此前从未在本任务下报告过，属新发现的持续性风险状态；② SOPS 于 2026-08-14 一次性回顾披露 4 个历史安全漏洞（3.13.0/3.13.2 起已修复，无正式 CVE 编号）。
- 推送：本会话被限定只能推送指定工作分支（云端 Routine 会话平台限制，无法直接推 main），按 SKILL.md 兜底流程推当前工作分支，依赖仓库内 auto-merge 工作流合并进 main。

## 2. 已报条目清单（最近 21 天）

2026-07-27 | CNCF 博客发布 Linkerd 多集群零停机架构实践文章（联邦+镜像两种模式组合，3 个 GKE 集群验证）| https://www.cncf.io/blog/2026/07/27/federating-clusters-for-zero-downtime-kubernetes/
2026-07-28 | ArgoCon Japan 2026 举行，披露 Argo CD 3.5 RC 特性（ApplicationSets 转正、Impersonation 升至 beta、repo-server mTLS 等）| https://www.cncf.io/blog/2026/07/20/argocon-japan-2026-meeting-the-maintainers-enterprise-insights-and-the-road-to-argo-cd-3-5/
2026-07-28~29 | KubeCon + CloudNativeCon Japan 2026 在横滨开幕，聚焦 K8s GPU 动态资源分配、OpenTelemetry 毕业、Keycloak-MCP 鉴权，CNCF 称 66% 受访组织已将 K8s 视为 AI"操作系统" | https://www.techtimes.com/articles/321774/20260728/kubecon-japan-2026-kubernetes-gpu-scheduling-otel-graduation-converge-ai-era.htm
2026-07-30 | KubeCon + CloudNativeCon Japan 2026 收官，OpenTelemetry 毕业成果专场及大规模边缘场景实践分享收尾 | https://opentelemetry.io/blog/2026/kubecon-japan/
2026-07-31 | Kubernetes v1.37 发布 Sneak Peek 博客，DRA Extended Resource 确认毕业至 GA，GA 定档 8/26 不变 | https://kubernetes.io/blog/2026/07/31/kubernetes-v1-37-sneak-peek/
2026-07-31 | GKE Dataplane V2 扩容支持单集群 1.5 万节点（GA）并保持 Network Policy 全量生效 | https://cloud.google.com/blog/topics/ai-infrastructure/whats-new-in-ai-infrastructure-this-month
2026-07-31 | GKE 上 llm-d 引入协作式时间分片，强化学习作业加速器利用率从 40% 提至 70% | https://cloud.google.com/blog/topics/ai-infrastructure/whats-new-in-ai-infrastructure-this-month
2026-08-03 | CNCF 项目 Cortex 完成 OSTIF 独立安全审计，7 个漏洞均已修复 | https://www.cncf.io/blog/2026/08/03/cortex-completes-ostif-security-audit/
2026-08-03 | Kubeflow SDK 统一 Python 接口下载量突破 100 万次 | https://www.cncf.io/blog/2026/08/03/kubeflow-sdk-evolution-one-million-downloads-and-counting/
2026-08-04 | Argo CD v3.5.0 正式 GA，按原定日程发布，含 OCI 明文仓库需显式 flag、--repo-server-strict-tls 废弃等破坏性变更 | https://github.com/argoproj/argo-cd/releases/tag/v3.5.0
2026-08-04 | HashiCorp 修复 Terraform MCP Server 跨租户凭证复用漏洞 CVE-2026-16498（CVSS 10.0），发布 1.2.0 | https://thehackernews.com/2026/08/veeam-terraform-mcp-django-patch.html
2026-08-04 | IBM/Red Hat 向高校、NGO、智库免费开放 Lightwell 开源供应链安全服务 | https://newsroom.ibm.com/2026-08-04-ibm-and-red-hat-offer-lightwell-at-no-cost-to-universities,-ngos-and-think-tanks
2026-08-04 | OpenTelemetry Collector v0.158.0 发布 | https://github.com/open-telemetry/opentelemetry-collector-releases/releases
2026-08-05 | Red Hat OpenShift 连续第三年入选 2026 Gartner 云原生应用平台魔力象限"领导者" | https://www.businesswire.com/news/home/20260805596970/en/Red-Hat-Positioned-as-a-Leader-in-the-2026-Gartner-Magic-Quadrant-for-Cloud-Native-Application-Platforms
2026-08-05 | K8gb 成为 CNCF Incubating 项目 | https://www.cncf.io/announcements/2026/08/05/k8gb-becomes-a-cncf-incubating-project/
2026-08-06 | cosign 曝出旧版 JSON bundle 签名校验绕过漏洞 GHSA-fx35-mq7g-6g98（CVSS 7.4），已发布 2.6.5/3.1.3 补丁 | https://github.com/sigstore/cosign/security/advisories/GHSA-fx35-mq7g-6g98
2026-08-06 | GitHub Actions 发生约 9-10 小时大规模故障，初步根因为向 runner 分配无效 job，源于对内部 Actions 事件处理服务的一次常规部署暴露了已有的容量/并发缺陷 | https://www.githubstatus.com/
2026-08-06 | LitmusChaos 发布 2026 上半年进展报告，称为项目最活跃阶段之一 | https://www.cncf.io/blog/2026/08/06/litmuschaos-q1-q2-2026-update-community-contributions-and-project-progress/
2026-08-02~08-06 | Cloudflare 举办"Agents Week 2026"系列发布，含 WebMCP 开发者预览与 Agent Access Model | https://blog.cloudflare.com/
2026-08-06 | Linux 内核 SCTP 实现曝出存续18年的 use-after-free 漏洞 SCTPhantom（CVE-2026-64564，CVSS v4.0 8.5），本地攻击者可提权至 root 并在特定配置下逃逸容器，已修复并回溯至多条稳定内核分支 | https://matrix.tencent.com/en/2026/08/06/sctphantom-CVE-2026-64564
2026-08-06 | Kubernetes v1.37 切出首个 Release Candidate（v1.37.0-rc.0），如期朝 8/26 GA 推进 | https://github.com/kubernetes/kubernetes/releases
2026-08-07 | Flux CD 发布 v2.9.4 补丁版本，含 source-watcher 安全加固 | https://github.com/fluxcd/flux2/releases
2026-08-10 | CNCF 公布 KubeCon + CloudNativeCon North America 2026（11 月 9–12 日，盐湖城）完整日程，新增 AI Inference + Agentic 专场 | https://www.cncf.io/announcements/2026/08/10/cncf-reveals-kubecon-cloudnativecon-north-america-2026-schedule-adds-new-ai-inference-agentic-track/
2026-08-10 | Docker docker cp/sbx cp 命令曝出容器逃逸漏洞 CVE-2026-17106（"CopyEscape"），可覆写宿主机文件、特定条件下获得 root 代码执行，Imperva 披露，Docker 已发布修复版本 | https://www.imperva.com/blog/copyescape-taking-over-docker-hosts-with-docker-cp/
2026-08-11 | Windows Container Isolation FS Filter Driver（unionfs.sys）曝出篡改漏洞 CVE-2026-72971（CVSS 5.5），随微软 8 月补丁星期二修复 | https://www.csoonline.com/article/4208185/patch-tuesday-august-2026-a-zero-day-winsock-driver-hole-under-exploit-and-a-maximum-severity-sap-vulnerability.html
2026-08-13 | Amazon EKS 新增 Kubernetes 控制平面组件（调度器/controller-manager/API server）参数配置能力，覆盖所有可用区域 | https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-control-plane-configuration-parameters/
2026-08-13~14 | TeamPCP 3 月 Trivy/LiteLLM 供应链攻击（CVE-2026-33634，CVSS 9.4）曝出新影响评估：153GB 被窃数据涉 2,488 企业域名，部分被窃凭据 5 个月后仍可用 | https://www.helpnetsecurity.com/2026/08/13/litellm-breach-stolen-credentials-leak/
2025-09-22（2026-08-17 首次核实收录）| Istio 1.25（读者主网格版本）官方支持结束，不再回滲安全与关键缺陷修复 | https://istio.io/latest/news/support/announcing-1.25-eol-final/
2026-08-14 | SOPS 项目一次性回顾披露 4 个历史安全漏洞（最严重 GHSA-jgf3-f6rg-8x3h，CVSS 7.4，Vault/OpenBao 令牌 SSRF 泄露），均已于 3.13.0/3.13.2 起修复 | https://github.com/getsops/sops/security/advisories/GHSA-jgf3-f6rg-8x3h

## 3. 进行中事件表

- 事件：Kubernetes v1.37 发布周期 | 最后进展日期：2026-08-06（v1.37.0-rc.0 切出，release candidate 阶段）| 下一步关注点：等 8/26 GA 官宣及正式 release notes，核实 DRA Partitionable Devices（KEP-4815，目前仍处 alpha 阶段）毕业情况及 v1.37 破坏性变更完整清单。（2026-08-09～08-17 已连续核查：均无新 RC/GA 消息，08-17 核查确认 rc.0 仍为最新，DRA Partitionable Devices 仍处 alpha，GA 仍定档 8/26。）

## 4. 读者在用的版本清单

栈位差表"我在用"一列的唯一数据源。**本节只由读者手动更新，定时任务不得改写其中的版本值与确认日期。**

| 组件 | 我在用 | 确认日期 | 备注 |
| --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本 | 2026-08-14 | 读者口径为"最新版"，未给具体控制面版本号；下次复核时填入实际版本，否则"距 EOL ≤ 3 个月"这条判定无法精确计算 |
| Kubernetes | 同 EKS 控制面版本 | 2026-08-14 | 不独立维护版本号 |
| Istio（主） | 1.25 | 2026-08-14 | |
| Istio（遗留） | 1.16 | 2026-08-14 | 已出官方支持窗口。只在栈位差表中列示，不为其单独检索、不做迁移追踪 |
| Flux CD | 未确认 | — | |
| Kustomize | 未确认 | — | |
| Helm | 未确认 | — | |
| Kyverno | 未确认 | — | |
| SOPS | 未确认 | — | |
| AWS Load Balancer Controller | 未确认 | — | |
