# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻：2026-10-26 08:25 UTC（归档日期 2026-10-26）。
- 上次运行时刻：2026-10-20 02:05 UTC，间隔约 6.26 天（常规窗口）。
- 实际覆盖窗口：2026-10-20 02:05 UTC – 2026-10-26 08:25 UTC（常规）。
- 方向 A 六项均已通过 WebSearch 与 GitHub Releases / Security Advisories API 交叉核查。结果：Kyverno 于 2026-10-20 发布 v1.19.2（Helm chart 3.9.2）并于 10-21 至 10-23 批量披露 26 项 GHSA 安全公告（11 项严重最高 CVSS 9.9、14 项高危、1 项中危，涵盖 v1.19.1 apiCall 命名空间隔离补丁的畸形百分号编码绕过 GHSA-3xfv-vq8x-qhg4 / GHSA-39w8-hv5g-f73w、CEL 路径穿越 GHSA-4pqm-wqq6-h9q2、NamespacedMutatingPolicy 跨命名空间覆写 GHSA-jcw5-3wcg-fqx5 / GHSA-f96w-622v-rqpq、CleanupPolicy 越权 GHSA-p58h-r4j3-h5vx / GHSA-rcxg-3f92-3mgr、generate 变量目标跳过鉴权 GHSA-vjfx-fp68-rh4v、verifyImages 缓存碰撞与伪造注解绕过 GHSA-2r43-6962-xcw5 / GHSA-h3pm-q9ww-f439 等，且在 Webhook 中对 CEL PolicyException 强制校验 exceptionNamespace，收录进"需要行动"）；Istio 于 2026-10-21 发布安全公告 ISTIO-SECURITY-2026-008（CVE-2026-111943）及补丁版本 1.31.3、1.30.7 与破例补丁 1.29.10（移除 8 个私钥于 10-20 泄露的 eMudhra 中间 CA 证书信任，同样影响读者在用的 Istio 1.25 出向 HTTPS 校验并有配置层缓解方案，收录进"需要行动"）；Flux CD 各核心子控制器（source-controller v1.10.0、kustomize-controller v1.10.0、notification-controller v1.10.0、helm-controller v1.7.0、image-reflector/automation-controller v1.3.0、source-watcher v2.3.0）于 2026-10-24 先行发布（含 Notification API 升 v1 与废弃字段移除、Object Identity 转正及默认 RBAC 移除 serviceaccounts/token create 权限的破坏性变更、控制器间 SPIFFE mTLS、HelmRelease OCIRepository 模板与 SOPS 注释正则解密修复，因顶层 flux2 v2.10.0 尚未正式打标发布，收录进"留意"并转入进行中事件表追踪）；AWS Load Balancer Controller 于 2026-10-21 与 10-25 相继发布 v3.6.1 与 v3.6.2（新增对账状态指标、修复安全组删除 InvalidGroup.NotFound 对账死循环、移除失信 eMudhra 根证书、优化 Gateway 首次缓存同步性能，收录进"留意"）；Kubernetes 本体无新稳定版（最新仍为 v1.37.1）；AWS EKS 窗口内仅发布 EMR on EKS 降价 30%（不触及本栈，不收）；Kustomize 最新仍为 v5.8.3；Helm 最新仍为 v4.3.1 / v3.22.1；SOPS 最新仍为 v3.13.3。方向 B/C 未检出独立于上述条目的窗口内达标新事件。
- 本期新增"需要行动"2 条（Kyverno v1.19.2 及 26 项 GHSA、Istio ISTIO-SECURITY-2026-008）、"留意"2 条（Flux 核心控制器 v1.10.0/v1.7.0 先行发布、ALBC v3.6.1/v3.6.2）。
- 版本清单已 73 天未复核（确认日 2026-08-14），未超 90 天，未写超期提示。
- 进行中事件表：核查 ISTIO-SECURITY-2026-007 四项 GHSA 仍未分配正式 CVE 编号，继续追踪；新增追踪 Kyverno v1.19.2 批次 26 项 GHSA 的正式 CVE 编号分配，以及 Flux v2.10.0 聚合版本正式发布。

## 2. 已报条目清单（最近 21 天）

2026-10-05 | AWS Load Balancer Controller v3.6.0 发布，新增 frontend-nlb-status-only 注解并修复安全组 CIDR 规范化及分权 DNS ACM 证书校验问题 | https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.0
2026-10-15 | Istio 发布安全公告 ISTIO-SECURITY-2026-007 与 1.31.2/1.30.6/1.29.9（1.29 同批 EOL），修复 HTTP/2 AuthorizationPolicy 方法大小写绕过（GHSA-w44g-8m76-8gc5，CVSS 7.4）、Ambient istiod 崩溃循环（GHSA-7p2q-4xvg-vxc6，CVSS 7.7）及两项 Envoy CONNECT 请求崩溃漏洞 | https://istio.io/latest/news/security/istio-security-2026-007/
2026-10-15 | Helm v4.3.1 与 v3.22.1 发布，修复上游 Go 依赖漏洞及 HookOnlyStrategy 下未等待 CRD 就绪问题 | https://github.com/helm/helm/releases/tag/v3.22.1
2026-10-20 | Kyverno 发布 v1.19.2 并批量披露 26 项 GHSA 安全公告（含 GHSA-3xfv-vq8x-qhg4、GHSA-39w8-hv5g-f73w 等 11 项 CVSS 9.1–9.9 严重级多租户提权与镜像验签绕过漏洞），同时对 CEL PolicyException 强制校验 exceptionNamespace | https://github.com/kyverno/kyverno/releases/tag/v1.19.2
2026-10-21 | Istio 发布安全公告 ISTIO-SECURITY-2026-008（CVE-2026-111943）与 1.31.3/1.30.7/1.29.10，吊销私钥泄露的 8 个 eMudhra 中间 CA 证书信任并修复自签名根证书过期启动失败问题 | https://istio.io/latest/news/security/istio-security-2026-008/
2026-10-24 | Flux CD 各核心控制器先行发布 v1.10.0 / v1.7.0（Notification API 升 v1、Object Identity 转正并收紧默认 serviceaccounts/token RBAC、引入控制器间 SPIFFE mTLS、支持 HelmRelease OCIRepository 模板及 SOPS 注释正则解密） | https://github.com/fluxcd/notification-controller/releases/tag/v1.10.0
2026-10-25 | AWS Load Balancer Controller 发布 v3.6.1 与 v3.6.2，新增对账状态指标、修复安全组释放 InvalidGroup.NotFound 对账死循环、移除失信 eMudhra 根证书并优化 Gateway 首次缓存同步性能 | https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.2

## 3. 进行中事件表

- 事件：Istio GCP 制品托管退役（gcr.io/istio-release 等旧地址断供）| 最后进展日期：2026-10-13（第二轮 3 小时 scream test 窗口执行）| 下一步关注点：关注 2026-11-17（6 小时）与 2026-12-08（24 小时）后续 scream test 及 12 月正式关停公告。
- 事件：Istio ISTIO-SECURITY-2026-007 四项 GHSA 正式 CVE 编号分配 | 最后进展日期：2026-10-15（截至 2026-10-26 核查 GHSA-w44g-8m76-8gc5、GHSA-7p2q-4xvg-vxc6、GHSA-8vc2-jrm4-835w、GHSA-47vj-9r25-wv5j 的 CVE 栏仍为空）| 下一步关注点：核查 GitHub Security Advisories 与 NVD 是否为上述四项分配正式 CVE-2026-* 编号（影响依赖 CVE 匹配的扫描器告警）。
- 事件：Kyverno v1.19.2 批次 26 项 GHSA 正式 CVE 编号分配 | 最后进展日期：2026-10-23（26 项 GHSA 全部披露完毕，CVE 栏均为空）| 下一步关注点：核查 GitHub Security Advisories 与 NVD 是否为 GHSA-3xfv-vq8x-qhg4、GHSA-39w8-hv5g-f73w 等严重/高危公告分配正式 CVE-2026-* 编号。
- 事件：Flux v2.10.0 聚合版本正式发布 | 最后进展日期：2026-10-24（source/kustomize/notification-controller v1.10.0 与 helm-controller v1.7.0 等子控制器已先行发版，flux2 主仓库于 10-25 合入最低 Kubernetes 1.35 等迁移提交）| 下一步关注点：关注 fluxcd/flux2 v2.10.0 正式 Release 发布及官方升级指南（含 Notification v1 废弃字段移除与 serviceaccounts/token 默认 RBAC 变更）。

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
