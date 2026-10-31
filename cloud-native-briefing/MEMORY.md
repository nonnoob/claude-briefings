# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻及检索截止：2026-10-31 11:32 UTC（2026-10-31 04:32 PDT）。
- 实际覆盖窗口：2026-10-26 08:25 UTC 至 2026-10-31 11:32 UTC（常规）。
- Watchlist 经官方 Releases、支持文档与 GitHub Advisory API 核查；Flux v2.10.0 于 10 月 26 日正式发布，Kubernetes 最新为 1.37.2；其余表内最新版本无已确认增量。Flux 在用版本及配置未确认，升级影响只作条件判断，归入“留意”，不声称生产已受影响。
- Istio 两项及 Envoy 两项被追踪 GHSA 的 cve_id 仍为空；查询到的 Kyverno 10 月下旬公告也未新增正式 CVE，不采用搜索生成的编号。已报安全事项不重复充当本期新闻。
- 方向 B/C 未取得新的达标条目；部分组件官方支持期限未确认，表内明确保留未知。上游 Kubernetes 1.34 EOL 与 EKS 1.34 支持期限不同，不能混用；“跟随最新 GA”不转换成读者实际版本号。
- 版本清单确认日距本期 78 天，未超 90 天；第 4 节原样保留。Flux 聚合 Release 待办已闭合，其他事件保留原实际进展日期。

## 2. 已报条目清单（最近 21 天）

2026-10-15 | Istio 发布安全公告 ISTIO-SECURITY-2026-007 与 1.31.2/1.30.6/1.29.9（1.29 同批 EOL），修复 HTTP/2 AuthorizationPolicy 方法大小写绕过（GHSA-w44g-8m76-8gc5，CVSS 7.4）、Ambient istiod 崩溃循环（GHSA-7p2q-4xvg-vxc6，CVSS 7.7）及两项 Envoy CONNECT 请求崩溃漏洞 | https://istio.io/latest/news/security/istio-security-2026-007/
2026-10-15 | Helm v4.3.1 与 v3.22.1 发布，修复上游 Go 依赖漏洞及 HookOnlyStrategy 下未等待 CRD 就绪问题 | https://github.com/helm/helm/releases/tag/v3.22.1
2026-10-20 | Kyverno 发布 v1.19.2 并批量披露 26 项 GHSA 安全公告（含 GHSA-3xfv-vq8x-qhg4、GHSA-39w8-hv5g-f73w 等 11 项 CVSS 9.1–9.9 严重级多租户提权与镜像验签绕过漏洞），同时对 CEL PolicyException 强制校验 exceptionNamespace | https://github.com/kyverno/kyverno/releases/tag/v1.19.2
2026-10-21 | Istio 发布安全公告 ISTIO-SECURITY-2026-008（CVE-2026-111943）与 1.31.3/1.30.7/1.29.10，吊销私钥泄露的 8 个 eMudhra 中间 CA 证书信任并修复自签名根证书过期启动失败问题 | https://istio.io/latest/news/security/istio-security-2026-008/
2026-10-24 | Flux CD 各核心控制器先行发布 v1.10.0 / v1.7.0（Notification API 升 v1、Object Identity 转正并收紧默认 serviceaccounts/token RBAC、引入控制器间 SPIFFE mTLS、支持 HelmRelease OCIRepository 模板及 SOPS 注释正则解密） | https://github.com/fluxcd/notification-controller/releases/tag/v1.10.0
2026-10-25 | AWS Load Balancer Controller 发布 v3.6.1 与 v3.6.2，新增对账状态指标、修复安全组释放 InvalidGroup.NotFound 对账死循环、移除失信 eMudhra 根证书并优化 Gateway 首次缓存同步性能 | https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.2
2026-10-31 | Flux v2.10.0 聚合版本正式发布，落实 Notification v1 与默认 token RBAC 变更，最低 Kubernetes 补丁为 1.35.2/1.36.1/1.37.0 | https://github.com/fluxcd/flux2/releases/tag/v2.10.0

## 3. 进行中事件表

- 事件：Istio GCP 制品托管退役（gcr.io/istio-release 等旧地址断供）| 最后进展日期：2026-10-13（第二轮 3 小时 scream test 窗口执行）| 下一步关注点：关注 2026-11-17（6 小时）与 2026-12-08（24 小时）后续 scream test 及 12 月正式关停公告。
- 事件：Istio ISTIO-SECURITY-2026-007 四项 GHSA 正式 CVE 编号分配 | 最后进展日期：2026-10-15（截至 2026-10-26 核查 GHSA-w44g-8m76-8gc5、GHSA-7p2q-4xvg-vxc6、GHSA-8vc2-jrm4-835w、GHSA-47vj-9r25-wv5j 的 CVE 栏仍为空）| 下一步关注点：核查 GitHub Security Advisories 与 NVD 是否为上述四项分配正式 CVE-2026-* 编号（影响依赖 CVE 匹配的扫描器告警）。
- 事件：Kyverno v1.19.2 批次 26 项 GHSA 正式 CVE 编号分配 | 最后进展日期：2026-10-23（26 项 GHSA 全部披露完毕，CVE 栏均为空）| 下一步关注点：核查 GitHub Security Advisories 与 NVD 是否为 GHSA-3xfv-vq8x-qhg4、GHSA-39w8-hv5g-f73w 等严重/高危公告分配正式 CVE-2026-* 编号。

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
