# ☁️ 云原生周报 · 2026-10-26

> 覆盖窗口：2026-10-20 至 2026-10-26（常规）

今日要闻：Kyverno 发布 v1.19.2 集中修复 26 项安全公告（含 11 项 CVSS 9.1–9.9 严重级多租户提权与镜像校验绕过漏洞，覆盖 v1.19.1 apiCall 命名空间隔离补丁绕过），Istio 同步发布 ISTIO-SECURITY-2026-008（CVE-2026-111943）与 1.31.3/1.30.7 吊销私钥泄露的 eMudhra 中间 CA 信任。

## 需要行动

- Kyverno v1.19.2 及 26 项 GHSA 安全公告（含 GHSA-3xfv-vq8x-qhg4、GHSA-39w8-hv5g-f73w 等 11 项 CVSS 9.1–9.9 严重级漏洞）：2026-10-20 发布 v1.19.2（Helm chart 3.9.2）并于 10-21 至 10-23 批量披露 26 项安全公告（11 项严重、14 项高危、1 项中危，正式 CVE 编号尚未分配），包括 v1.19.1 apiCall 路径与命名空间隔离补丁的畸形百分号编码绕过（GHSA-3xfv-vq8x-qhg4、GHSA-39w8-hv5g-f73w，均 CVSS 9.9）、CEL 策略 resource.get()/post() 路径穿越致集群接管（GHSA-4pqm-wqq6-h9q2，CVSS 9.9）、NamespacedMutatingPolicy mutate-existing 跨命名空间覆写（GHSA-jcw5-3wcg-fqx5、GHSA-f96w-622v-rqpq，均 CVSS 9.9）、CleanupPolicy 上下文与 API 调用越权（GHSA-p58h-r4j3-h5vx、GHSA-rcxg-3f92-3mgr，均 CVSS 9.9）、generate 规则目标使用变量时跳过鉴权（GHSA-vjfx-fp68-rh4v，严重）、verifyImages 缓存键碰撞及伪造注解绕过镜像签名校验（GHSA-2r43-6962-xcw5 CVSS 9.1、GHSA-h3pm-q9ww-f439 CVSS 7.7）及变量替换与通配符匹配准入 DoS（GHSA-338x-hgrv-626h、GHSA-8mrj-27wr-599g，均 CVSS 7.7）；同版还在准入 Webhook 中对 CEL PolicyException 强制校验 exceptionNamespace（#17651）。影响：你的 Kyverno 版本未确认，凡 <= v1.19.1（含上月建议升级的 v1.19.1）均在受影响范围内，多租户集群中具备命名空间策略创建权限的用户可提权至集群管理员或绕过镜像验签，且升级后不在 exceptionNamespace 内的 CEL PolicyException 将被拒绝。动作：核实当前 Kyverno 版本并升级至 v1.19.2（Helm chart 3.9.2），升级前检查 CEL PolicyException 所在命名空间是否符合 exceptionNamespace 配置，并收紧命名空间级 Policy/NamespacedMutatingPolicy/CleanupPolicy 创建权限。来源：GitHub Releases https://github.com/kyverno/kyverno/releases/tag/v1.19.2
- Istio ISTIO-SECURITY-2026-008（CVE-2026-111943，CVSS 未评分）与 1.31.3 / 1.30.7 / 1.29.10：2026-10-21 官方发布安全公告及补丁版本（1.29 已于 10-12 EOL，1.29.10 为破例补丁），紧急移除对 8 个私钥于 10-20 泄露的 eMudhra 中间 CA 证书（含 Sectigo 交叉签名）的信任——由于 Envoy、Go 与 ztunnel 均不强制校验证书透明度（CT），持有泄露私钥者可为任意域名签发受容器系统根证书包信任的伪造证书；补丁从 ubuntu 与 distroless 基础镜像移除 emSign ECC Root CA - G3，并将 1.30/1.31 的 istiod/istioctl/pilot-agent 升级至 Go 1.26.10（在 crypto/x509 中硬编码拒绝泄露中间 CA 公钥）、ztunnel 升级至 rustls-webpki 0.103.16，同时修复 istiod 缩容至零期间自签名根证书过期无法启动及默认 PILOT_AUTO_SEND_UNHEALTHY_ENDPOINTS 下遗漏不健康 ServiceEntry/WorkloadEntry 端点的问题。影响：网格内部 mTLS 不受影响，但你在用的主集群 Istio 1.25 包含未更新的系统根证书包与旧版 Go 运行时，凡出向 HTTPS 流量使用未显式指定 caCertificates/credentialName 的 DestinationRule（tls.mode: SIMPLE）、RequestAuthentication 远程拉取 jwksUri 或配置 XDS_ROOT_CA=SYSTEM 的场景均面临中间人伪造证书风险。动作：对访问外部 HTTPS 服务的 DestinationRule 显式指定受信任的 caCertificates/credentialName 或通过 caCrl 吊销泄露中间 CA 作为配置层立即缓解，并推进主集群从已出窗口的 1.25 升级至 1.30.7 或 1.31.3。来源：Istio Security Bulletin https://istio.io/latest/news/security/istio-security-2026-008/

## 留意

- Flux CD 核心控制器先行发布（source/kustomize/notification-controller v1.10.0、helm-controller v1.7.0 等）：2026-10-24 各子控制器赶在 Flux v2.10.0 聚合发布前集中发版——notification-controller v1.10.0 将 Event、Alert、Provider API 升至 notification.toolkit.fluxcd.io/v1（v1beta3 标记废弃，转换至 v1 时移除已废弃的 Alert.spec.summary、Provider.spec.interval、Azure Event Hub 静态 JWT 及 Provider.spec.secretRef 内的 TLS/代理字段，改用 eventMetadata.summary、proxySecretRef 与 certSecretRef）；各控制器将对象级工作负载身份转正并更名为 Object Identity（移除 ObjectLevelWorkloadIdentity 特性门控并默认常开，新增 spiffe 凭据提供方），同时带来破坏性 RBAC 变更（默认 Flux RBAC 不再授予对 serviceaccounts/token 的 create 权限，依赖默认 RBAC 签发对象级令牌需提前绑定额外 ClusterRole，见 fluxcd/flux2#6139）；此外引入控制器间 SPIFFE mTLS，helm-controller v1.7.0 支持在 HelmRelease .spec.chart.kind 直接内联声明 OCIRepository 并内置 Helm 4.3.1 SDK，kustomize-controller v1.10.0 修复使用 encrypted_comment_regex/unencrypted_comment_regex 加密的 SOPS 资源因 kustomize 剥离注释导致解密失败的问题并新增 --override-manager-before-dry-run 标志。影响：你的 Flux 版本未确认，且顶层 fluxcd/flux2 v2.10.0 尚未正式打标发布（当前最新仍为 v2.9.6），当下不会立即触发升级，但后续升至 v2.10 时将受 Notification v1 字段裁剪、serviceaccounts/token 默认 RBAC 收紧及最低 Kubernetes 版本升至 1.35 影响。动作：暂无，等 Flux v2.10.0 正式聚合发布后再按迁移清单核查 Alert/Provider 废弃字段与 serviceaccounts/token RBAC 授权。来源：GitHub Releases https://github.com/fluxcd/notification-controller/releases/tag/v1.10.0
- AWS Load Balancer Controller v3.6.1 / v3.6.2：分别于 2026-10-21 与 10-25 发布（均无 CRD 变更），v3.6.1 新增 awslbc_controller_reconcile_condition 指标以监控 Ingress/Service/Gateway/TargetGroupBinding 对账失败状态、将释放自动生成后端安全组时的 InvalidGroup.NotFound 视为成功以避免带外删除引发对账死循环，并将 Go 升至 1.26.10；v3.6.2 基于更新后的 eks-distro-minimal-base-nonroot 基础镜像重建以移除 3 个失信 eMudhra 根证书（emSign ECC Root CA - G3/C3 与 emSign Root CA - C1）、在 informer 首次缓存同步期间跳过 Gateway 子资源冗余扇出以缩短大规模集群启动耗时，并升级测试依赖 klauspost/compress 至 v1.18.7（修复 CVE-2026-63209，未编译进生产二进制）。影响：你的 ALBC 版本未确认，两版均为无 CRD 与注解默认语义变更的补丁升级，根证书清理仅影响控制器自身发起的出向 TLS 校验。动作：暂无，等你确认在用 ALBC 版本或规划例行补丁升级时再一并纳入。来源：GitHub Releases https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.2

## 栈位差

| 组件 | 我在用 | 当前最新 | 落后 | 支持窗口 | 我方版本确认日 |
| --- | --- | --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本（未给具体版本号） | 1.37（2026-10-01 起 EKS 支持） | — | — | 2026-08-14 |
| Kubernetes 本体 | 同 EKS 控制面版本（未给具体版本号） | v1.37.1（2026-09-23，纯缺陷修复，无 CVE） | — | — | 2026-08-14 |
| Istio（主） | 1.25 | 1.31.3（2026-10-21） | 6 档 | 已出窗口（自 2025-09-22 起；1.29 亦于 2026-10-12 EOL） | 2026-08-14 |
| Istio（遗留） | 1.16 | 1.31.3 | 15 档 | 已出窗口（自 2023-07-25 起） | 2026-08-14 |
| Flux CD | 未确认 | v2.9.6（2026-10-01；各核心 controller 已于 2026-10-24 先行发布 v1.10.0/v1.7.0） | — | — | — |
| Kustomize | 未确认 | v5.8.3（2026-10-08，纯依赖清理，无功能变更） | — | — | — |
| Helm | 未确认 | v4.3.1 / v3.22.1（2026-10-15） | — | — | — |
| Kyverno | 未确认 | v1.19.2（2026-10-20） | — | — | — |
| SOPS | 未确认 | v3.13.3（2026-07-23） | — | — | — |
| AWS Load Balancer Controller | 未确认 | v3.6.2（2026-10-25） | — | — | — |
