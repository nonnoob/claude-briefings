# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻：2026-09-14 10:50 UTC。
- 上次运行时刻：2026-09-10 18:34 UTC，间隔约 3.7 天，未超 10 天封顶。
- 实际覆盖窗口：2026-09-10 18:34 UTC – 2026-09-14 10:50 UTC（常规）。
- 方向 A（watchlist）六项逐一核查：Kubernetes 本体、AWS EKS、Istio、Flux CD 及各 controller/Kustomize/Helm、Kyverno/SOPS、AWS Load Balancer Controller/NLB。kubernetes.io、docs.aws.amazon.com、aws.amazon.com、endoflife.date、istio.io、juliet.sh 直连 WebFetch 被出网代理拦截，改用 WebSearch 与 GitHub Releases/Security Advisories 页面交叉核实替代，未造成方向缺失，按"全量覆盖"落盘。方向 B/C 全量核查（含供应链、CNCF 项目状态、同栈事故复盘、替代技术威胁四类）。方向 D 栈位差表全量复核，与 2026-09-10 期相比各组件版本、支持窗口均无变化。
- 本期无新增"需要行动"或"留意"条目：窗口内除上期（2026-09-10）已报告的内容外，watchlist 各组件均无新发布、无新安全公告；方向 B/C 四条门槛均未命中新事件。按空期骨架落盘，保留栈位差表。
- 曾评估但排除：CVE-2026-31431（"Copy Fail"，Linux 内核页缓存漏洞，验证覆盖 EKS，容器逃逸至节点级代码执行）——该漏洞本体于 2026-04/05 披露、AWS 安全公告 2026-030-aws 随后发布，均早于本次覆盖窗口且早于本仓库最早归档（2026-07-26），本次检索中新出现的 PoC 仓库与技术博客未能确认其发布时间落在本次窗口内，故未收录；本条只作运行记录，不进 MEMORY 第 3 节追踪（不属于本次窗口产生的新事件，也非此前已建档的进行中事件）。
- 进行中事件表本期核查结果：5 条全部定向核查，均无实质新进展（Istio scream test 首次窗口 2026-09-15 尚未到期；Kyverno 无新 GHSA；SOPS allowlist 默认值未随新版本落地；SOPS CNCF 治理无新讨论；EKS 仍未支持 K8s 1.37），全部原样保留，无踢出。
- 已报条目清单：按 21 天窗口（截至 2026-09-14，含 2026-08-24 及以后）保留，移出 2026-08-03、2026-08-14（背景）、2026-08 EKS 控制面参数、2026-03-17 SOPS CNCF（背景，持续追踪见第 3 节）、2026-07-01 Argo CD、Kyverno 全年模式（背景，持续追踪见第 3 节）共 6 条过期条目。
- 推送：本会话被限定只能推送指定工作分支（云端 Routine 会话平台限制，无法直接推 main），按 SKILL.md 兜底流程推当前工作分支，依赖仓库内 auto-merge 工作流合并进 main。

## 2. 已报条目清单（最近 21 天）

2026-08-26 | Kubernetes v1.37「Garhwal」正式 GA，含静态 Pod 禁止引用 Secret/ConfigMap 等破坏性变更；EKS 尚未支持 | https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/
2026-08-27 | Istio 发布 ISTIO-SECURITY-2026-006 安全公告（CVSS 7.7），修复 EnvoyFilter 正则未限长导致的 istiod 拒绝服务及 13 个 Envoy CVE，发布 1.30.4/1.29.7 | https://istio.io/latest/news/security/istio-security-2026-006/
2026-08-31 | Istio 1.31.0 发布，宣布停止向 GCP 旧地址发布制品，断供测试定于 9/15 起分批执行 | https://istio.io/latest/news/releases/1.31.x/announcing-1.31/upgrade-notes/
2026-08-31 | Flux CD v2.9.5 发布，加固 kubeconfig Secret 校验（拒绝本地文件路径引用），Helm 迁回上游 v4.2.4 | https://github.com/fluxcd/flux2/releases/tag/v2.9.5
2026-09-09~10 | Helm v4.3.0 与 v3.22.0 发布，官方将 v3.22.0 定位为 v3 线路计划内最后一个 minor 版本 | https://github.com/helm/helm/releases/tag/v3.22.0
2026-09-10 | Kyverno v1.19.1 发布，同日修复 5 个安全公告，含 CVSS 9.9 严重级 apiCall urlPath 命名空间逃逸至集群管理员提权漏洞 GHSA-5qq8-67g6-4h2w | https://github.com/kyverno/kyverno/security/advisories/GHSA-5qq8-67g6-4h2w

## 3. 进行中事件表

- 事件：Istio GCP 制品托管退役（gcr.io/istio-release 等旧地址断供）| 最后进展日期：2026-08-31（1.31 发布，宣布断供计划）| 下一步关注点：等 2026-09-15 首次 scream test 结果，验证有无用户受影响、时间表是否调整；后续窗口 10/13、11/17、12/08。
- 事件：Kyverno apiCall/CEL 策略执行链命名空间隔离漏洞模式 | 最后进展日期：2026-09-10（v1.19.1 修复本轮 5 个 GHSA）| 下一步关注点：等是否有后续 CVE 编号分配，或官方推出结构性修复（如默认限制 apiCall/CEL 创建权限）。
- 事件：SOPS Vault/OpenBao allowlist 默认值收紧 | 最后进展日期：2026-08-14（GHSA-jgf3-f6rg-8x3h 预告）| 下一步关注点：等该默认值变更随具体版本发布，核实是否为破坏性变更。
- 事件：SOPS CNCF 治理状态（TOC 评估 MPL 许可证兼容性）| 最后进展日期：2026-03-17（issue 开启，无进一步公开讨论可核实）| 下一步关注点：等 TOC 就 cncf/toc#2098 做出结论（重新授权/迁出 CNCF/维持现状）。
- 事件：Amazon EKS 是否/何时支持 Kubernetes 1.37 | 最后进展日期：2026-09-10（确认仍未支持，最高至 1.36）| 下一步关注点：等 AWS What's New 官宣 EKS 支持 1.37，届时 1.37 的破坏性变更（静态 Pod Secret/ConfigMap 引用禁令、cgroup v1 kubelet 拒启等）转为对读者实际可命中。

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
