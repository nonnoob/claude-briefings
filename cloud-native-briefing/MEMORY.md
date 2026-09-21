# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻：2026-09-21 10:51 UTC。
- 上次运行时刻：2026-09-14 10:50 UTC，间隔约 7.0 天，未超 10 天封顶。
- 实际覆盖窗口：2026-09-14 10:50 UTC – 2026-09-21 10:51 UTC（常规）。
- 方向 A（watchlist）六项逐一核查：Kubernetes 本体、AWS EKS、Istio、Flux CD 及各 controller/Kustomize/Helm、Kyverno/SOPS、AWS Load Balancer Controller/NLB。istio.io 直连 WebFetch 被出网代理拦截，改用 WebSearch 与 GitHub Releases/Security Advisories 页面交叉核实替代，未造成方向缺失，按"全量覆盖"落盘。核查结果：Kubernetes 本体无新版本（v1.37 仍为最新，未见 1.37.1 补丁）、无新核心 CVE；AWS EKS 仍未支持上游 1.37（最高 1.36），本期无新公告；Istio 无新安全公告（最近仍为 08-27 的 ISTIO-2026-006），1.32 尚在准备中未发布；Flux CD/Kustomize/Helm 均无新版本（分别停留在 v2.9.5、v5.8.1、v4.3.0/v3.22.0）；Kyverno 无新 GHSA（v1.19.1 当日的 5 个公告已在上期报告，本期未见后续）；SOPS 无新版本（v3.13.3）；AWS Load Balancer Controller 无新版本（v3.5.0）。方向 B/C 全量核查（含供应链攻击、CNCF 项目状态、同栈事故复盘、替代技术威胁四类）：检出 CNCF 项目 Karmada 毕业（2026-09 announced）、npm/PyPI 供应链攻击（ChainDrop 等）、2026-05 Slack Istio 1.22 熔断配置事故复盘，均因不落在读者生产栈（编排/网格/交付/策略/入口六层）或不在窗口内而未收录。方向 D 栈位差表全量复核，与 2026-09-14 期相比各组件版本、支持窗口均无变化。
- 本期无新增"需要行动"或"留意"条目：窗口内 watchlist 各组件均无新发布、无新安全公告；方向 B/C 四条门槛均未命中新事件。按空期骨架落盘，保留栈位差表。
- 进行中事件表本期核查结果：5 条全部定向核查。①Istio GCP 制品托管退役——2026-09-15 首次 scream test 按计划应已执行，但 istio.io 直连被出网代理拦截、GitHub issue #61467 暂无后续评论，本期未能确认测试结果（用户是否受影响、时间表有无调整），保留待下次，下一步关注点更新为"确认 9/15 结果 + 等 10/13 第二次 scream test"。②Kyverno apiCall/CEL 命名空间隔离漏洞模式——无新 CVE，保留。③SOPS Vault/OpenBao allowlist 默认值收紧——自 2026-08-14 起连续超 21 天无新版本落地确认，按规则移出，若未来随版本发布将作为新条目收录。④SOPS CNCF 治理状态（toc#2098）——自 2026-03-17 起连续超 21 天无新公开讨论，按规则移出，若 TOC 做出结论将作为新条目收录。⑤EKS 是否支持 K8s 1.37——本期再次确认仍未支持（最高 1.36），未构成"新进展"，最后进展日期维持 2026-09-10，保留。
- 已报条目清单：按 21 天窗口（截至 2026-09-21，含 2026-08-31 及以后）保留，移出 2026-08-26（K8s v1.37 GA）、2026-08-27（Istio ISTIO-SECURITY-2026-006）共 2 条过期条目。
- 推送：本会话被限定只能推送指定工作分支（云端 Routine 会话平台限制，无法直接推 main），按 SKILL.md 兜底流程推当前工作分支，依赖仓库内 auto-merge 工作流合并进 main。

## 2. 已报条目清单（最近 21 天）

2026-08-31 | Istio 1.31.0 发布，宣布停止向 GCP 旧地址发布制品，断供测试定于 9/15 起分批执行 | https://istio.io/latest/news/releases/1.31.x/announcing-1.31/upgrade-notes/
2026-08-31 | Flux CD v2.9.5 发布，加固 kubeconfig Secret 校验（拒绝本地文件路径引用），Helm 迁回上游 v4.2.4 | https://github.com/fluxcd/flux2/releases/tag/v2.9.5
2026-09-09~10 | Helm v4.3.0 与 v3.22.0 发布，官方将 v3.22.0 定位为 v3 线路计划内最后一个 minor 版本 | https://github.com/helm/helm/releases/tag/v3.22.0
2026-09-10 | Kyverno v1.19.1 发布，同日修复 5 个安全公告，含 CVSS 9.9 严重级 apiCall urlPath 命名空间逃逸至集群管理员提权漏洞 GHSA-5qq8-67g6-4h2w | https://github.com/kyverno/kyverno/security/advisories/GHSA-5qq8-67g6-4h2w

## 3. 进行中事件表

- 事件：Istio GCP 制品托管退役（gcr.io/istio-release 等旧地址断供）| 最后进展日期：2026-08-31（1.31 发布，宣布断供计划）| 下一步关注点：确认 2026-09-15 首次 scream test 的实际结果（本期因 istio.io 访问受限未能确认），并等 2026-09-15 首次 scream test 结果核实后，继续关注 2026-10-13、2026-11-17、2026-12-08 后续窗口。
- 事件：Kyverno apiCall/CEL 策略执行链命名空间隔离漏洞模式 | 最后进展日期：2026-09-10（v1.19.1 修复本轮 5 个 GHSA）| 下一步关注点：等是否有后续 CVE 编号分配，或官方推出结构性修复（如默认限制 apiCall/CEL 创建权限）。
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
