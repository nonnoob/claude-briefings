# ☁️ 云原生每日简报 · 2026-08-07

> 上次运行为 2026-07-30 12:10 UTC，因间隔超过 7 天封顶，本期实际覆盖 2026-07-31 16:47 UTC 至 2026-08-07 16:47 UTC（约 7 天，按封顶规则处理）；窗口外（2026-07-30 12:10–07-31 16:47）未发现至今仍重要、需额外补收的大事。

## 版本与变更

- 【续报】Argo CD v3.5.0 正式 GA，按原定日程如期发布（未跳票）：Source Hydrator、Impersonation 转正至 beta，新增 repo-server mTLS、提交签名验证、Gateway API 支持等。**需要行动**：使用非 HTTPS OCI 仓库（含 Helm Chart 中 `oci://` 依赖）的用户升级后必须显式加 `--insecure-oci-force-http` 标志，否则会失败；`--repo-server-strict-tls` 标志已废弃，需迁移配置方式。该事件至此闭合，移出跟踪表。来源：GitHub Releases — https://github.com/argoproj/argo-cd/releases/tag/v3.5.0
- 【续报】Kubernetes v1.37 发布 Sneak Peek 博客：DRA Extended Resource 确认将毕业至 GA；nftables 有望成为 kube-proxy 默认后端候选（先加告警过渡）；GA 日程不变，仍为 2026-08-26。DRA Partitionable Devices（KEP-4815）本期毕业阶段在多个二手信源间存在冲突，暂未坐实，继续跟踪。来源：Kubernetes 官方博客 — https://kubernetes.io/blog/2026/07/31/kubernetes-v1-37-sneak-peek/
- Flux CD 发布 v2.9.4 补丁版本，重点是安全加固：限制 source-watcher 的 tarball 解压范围与 glob 展开范围。**建议行动**：属常规安全补丁，按例行流程升级即可，无破坏性变更。来源：GitHub Releases — https://github.com/fluxcd/flux2/releases
- OpenTelemetry Collector 发布 v0.158.0，core/contrib 及 opampsupervisor、builder 组件同步升级，属常规迭代版本。来源：GitHub Releases — https://github.com/open-telemetry/opentelemetry-collector-releases/releases

## 安全通告

- HashiCorp 修复 Terraform MCP Server 跨租户凭证复用漏洞 **CVE-2026-16498（CVSS 10.0，严重）**：该组件用于连接 AI 助手与 Terraform，漏洞可致跨租户凭证被复用。已发布 1.2.0 修复版，**使用该组件的用户应立即升级**。来源：The Hacker News — https://thehackernews.com/2026/08/veeam-terraform-mcp-django-patch.html
- cosign 曝出旧版 JSON bundle 签名校验绕过漏洞 **GHSA-fx35-mq7g-6g98（CVSS 7.4，高危）**：证书解析失败时会静默回退为裸公钥校验，跳过 X.509 与 OIDC 签发者校验，可导致身份不匹配仍验证"通过"。受影响版本 cosign/v2 ≤2.6.4、cosign/v3 ≤3.1.2，已发布 v2.6.5 / v3.1.3 修复；临时缓解可改用 `--new-bundle-format`。**建议行动**：依赖 cosign 校验旧版 JSON bundle 的供应链安全流程应尽快升级或切换 bundle 格式。来源：GitHub Security Advisories — https://github.com/sigstore/cosign/security/advisories/GHSA-fx35-mq7g-6g98

## 云厂商动态

- Google Cloud / GKE：Dataplane V2 正式 GA 支持单集群扩展至 1.5 万节点，同时保持 Network Policy 全量强制生效，面向超大规模企业与 AI/ML 工作负载。来源：Google Cloud Blog — https://cloud.google.com/blog/topics/ai-infrastructure/whats-new-in-ai-infrastructure-this-month
- Google Cloud / GKE：llm-d 引入协作式时间分片（Co-operative Time-Slicing），允许强化学习（RL）作业交错共享同一加速器，平均利用率从约 40% 提升到 70% 且不影响收敛精度。来源：同上
- 【单源】本期未发现 AWS EKS、Azure AKS 有落在窗口内的新功能发布或版本矩阵变化；AWS 官方信源（aws.amazon.com 等）因出站网络限制未能直接核实，存在遗漏可能，Azure 侧已通过 GitHub AKS release tracker 直接确认窗口内无新版本。

## CNCF 与社区

- CNCF 宣布 K8gb（Kubernetes 全局负载均衡/GSLB 方案）晋升为 **Incubating** 项目。来源：CNCF Announcements — https://www.cncf.io/announcements/2026/08/05/k8gb-becomes-a-cncf-incubating-project/
- LitmusChaos 发布 2026 上半年进展报告：上半年发布 6 个版本，社区各渠道持续增长，称为项目历史上最活跃阶段之一。来源：CNCF Blog — https://www.cncf.io/blog/2026/08/06/litmuschaos-q1-q2-2026-update-community-contributions-and-project-progress/
- Kubeflow SDK（统一 Python 接口）在 PyPI 上下载量突破 100 万次，路线图计划通过 MCP 将其暴露为 AI 可调用工具。来源：CNCF Blog — https://www.cncf.io/blog/2026/08/03/kubeflow-sdk-evolution-one-million-downloads-and-counting/
- CNCF Incubating 项目 Cortex 完成 OSTIF 独立安全审计（Quarkslab 执行），聚焦多租户边界与集群运维安全，发现的 7 个问题（6 中危 1 低危）均已修复。来源：CNCF Blog — https://www.cncf.io/blog/2026/08/03/cortex-completes-ostif-security-audit/

## 商业动向

- Red Hat OpenShift 连续第三年入选 2026 Gartner 云原生应用平台魔力象限"领导者"象限。来源：BusinessWire — https://www.businesswire.com/news/home/20260805596970/en/Red-Hat-Positioned-as-a-Leader-in-the-2026-Gartner-Magic-Quadrant-for-Cloud-Native-Application-Platforms
- IBM 与 Red Hat 宣布向 185+ 所高校、100+ NGO/智库免费开放 Lightwell（开源漏洞修复/供应链安全服务），生态合作方包括 AWS、GitLab、Microsoft、NVIDIA 等。来源：IBM Newsroom — https://newsroom.ibm.com/2026-08-04-ibm-and-red-hat-offer-lightwell-at-no-cost-to-universities,-ngos-and-think-tanks
- 【单源，覆盖不完整】SUSE/Rancher、Isovalent、Solo.io 等厂商本期未发现窗口内融资/并购/产品线调整消息；因检索配额耗尽，未能对这几家厂商及部分周边厂商（Kong、Tetrate、Buoyant 等）做深入补充检索，不排除遗漏。

## 工程实践

- GitHub Actions 于 2026-08-06 发生约 9 小时大规模故障，波及 Actions 本身、GitHub Pages、Copilot 代码评审/编码 agent、hosted runners、Enterprise Importer 迁移及 webhook 投递。初步根因为"向 runner 分配了无效的 job"，官方尚未发布正式事后分析（postmortem）。报道称这是 8 月前 6 天内 GitHub 记录的第 6 起可用性事件，凸显其基础设施在快速增长下的可靠性压力。来源：GitHub Status — https://www.githubstatus.com/ ；WebProNews 报道
- Cloudflare 举办"Agents Week 2026"系列发布（08-02～08-06）：新增 Agent Access Model（任务域身份代理 + 持续鉴权 + 有状态信任）、`wrangler dev` 为 agent 调试生成结构化 trace、Workers 经 Durable Objects/Containers 转发入站 TCP、WebMCP 开发者预览（使网站无需新增 API 即可被浏览器 AI agent 调用）。属平台工程 / edge 计算原语方向的系统性发布。来源：Cloudflare Blog — https://blog.cloudflare.com/
