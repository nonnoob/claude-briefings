# ☁️ 云原生周报 · 2026-10-19

> 覆盖窗口：2026-10-09 至 2026-10-19（补漏：距上次运行 2026-10-05 约 14.6 天，按 10 天封顶并补收 10-05 至 10-09 间重要动态）

今日要闻：Istio 发布安全公告 ISTIO-SECURITY-2026-007 与 1.31.2/1.30.6/1.29.9 补丁，修复 HTTP/2 下 AuthorizationPolicy 方法大小写绕过漏洞（GHSA-w44g-8m76-8gc5，CVSS 7.4），该匹配逻辑同样影响在用的 Istio 1.25。

## 需要行动

- Istio ISTIO-SECURITY-2026-007（GHSA-w44g-8m76-8gc5，CVSS 7.4 高危）：2026-10-15 官方随 1.31.2、1.30.6 及 1.29.9（1.29 已于 10-12 正式 EOL，此为最终补丁）披露并修复 HTTP/2 下 AuthorizationPolicy 方法大小写绕过漏洞——含 methods 的 DENY 规则或含 notMethods 的 ALLOW 规则此前被编译为大小写敏感的 :method 匹配器，攻击者发送小写或混写方法（如 post 代替 POST）即可绕过策略直达工作负载（HTTP/1.1 因编解码器直接拒绝非大写方法不受影响）；同批公告还修复了 Ambient 模式 waypoint 地址冲突致 istiod 崩溃循环（GHSA-7p2q-4xvg-vxc6，CVSS 7.7）及 Envoy OAuth2/api_key_auth 过滤器处理无 :path 的 CONNECT 请求崩溃问题（GHSA-8vc2-jrm4-835w CVSS 7.5、GHSA-47vj-9r25-wv5j CVSS 6.5）。影响：官方公告虽仅列支持窗口内的 1.29–1.31，但该 RBAC 方法大小写敏感匹配系与 CVE-2021-39155 同源的历史实现，你在用的主集群 Istio 1.25 同样受影响，凡在 HTTP/2（含 gRPC）链路上使用 DENY+methods 或 ALLOW+notMethods 的授权策略均可被绕过。动作：排查集群内所有 AuthorizationPolicy，将基于方法黑名单的 DENY+methods 或 ALLOW+notMethods 规则改写为显式大写方法白名单（ALLOW+methods）以立即缓解，并规划将主集群从已出窗口的 1.25 升级至受支持且已修复的 1.30.6 或 1.31.2。来源：Istio Security Bulletin https://istio.io/latest/news/security/istio-security-2026-007/

## 留意

- Helm v4.3.1 / v3.22.1：2026-10-15 双线同步发布补丁版本，其中 v3.22.1 为 v3 进入安全维护期后的首个补丁，将 k8s.io 依赖升至 v0.37.1、OpenTelemetry OTLP 导出器升至 v1.45.0 以修复上游 Go 依赖安全漏洞；v4.3.1 修复 HookOnlyStrategy 下未等待 CRD 建立完成即继续执行的问题。影响：你的 Helm 版本未确认，且集群内 Helm 发布主要由 Flux helm-controller 驱动（当前最新 Flux v2.9.6 尚未合入该版 SDK），当下无直接破坏性影响。动作：暂无，等你确认本地 Helm CLI 版本或等 Flux 新版本合入该补丁后再评估升级。来源：GitHub Releases https://github.com/helm/helm/releases/tag/v3.22.1
- AWS Load Balancer Controller v3.6.0：2026-10-05 发布（位于上次运行后的补漏区间），新增 frontend-nlb-status-only 注解以解决前置 NLB 场景下 ExternalDNS 记录创建异常，修复安全组入站规则 CIDR 规范化避免重复对账失败、修复分权 DNS 下公有 ACM 证书误选私有 Route 53 托管区卡在 PENDING_VALIDATION 的问题，并支持跨账号 TargetGroupBinding IP 靶标按 Pod 可用区注册（需显式开启）；Gateway API CRD 维持 v1.6.0 不变。影响：你的 ALBC 版本未确认，本次变更为增量修复与可选注解扩展，未改变现有 NLB/ALB 注解默认语义，不必立即升级。动作：暂无，等你确认在用版本或遇到前置 NLB ExternalDNS 联动、分权 DNS ACM 校验问题时再升级。来源：GitHub Releases https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.0

## 栈位差

| 组件 | 我在用 | 当前最新 | 落后 | 支持窗口 | 我方版本确认日 |
| --- | --- | --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本（未给具体版本号） | 1.37（2026-10-01 起 EKS 支持） | — | — | 2026-08-14 |
| Kubernetes 本体 | 同 EKS 控制面版本（未给具体版本号） | v1.37.1（2026-09-23，纯缺陷修复，无 CVE） | — | — | 2026-08-14 |
| Istio（主） | 1.25 | 1.31.2（2026-10-15） | 6 档 | 已出窗口（自 2025-09-22 起；1.29 亦于 2026-10-12 EOL） | 2026-08-14 |
| Istio（遗留） | 1.16 | 1.31.2 | 15 档 | 已出窗口（自 2023-07-25 起） | 2026-08-14 |
| Flux CD | 未确认 | v2.9.6（2026-10-01） | — | — | — |
| Kustomize | 未确认 | v5.8.3（2026-10-08，纯依赖清理，无功能变更） | — | — | — |
| Helm | 未确认 | v4.3.1 / v3.22.1（2026-10-15） | — | — | — |
| Kyverno | 未确认 | v1.19.1（2026-09-10） | — | — | — |
| SOPS | 未确认 | v3.13.3（2026-07-23） | — | — | — |
| AWS Load Balancer Controller | 未确认 | v3.6.0（2026-10-05） | — | — | — |
