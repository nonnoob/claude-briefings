# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 运行时刻：2026-10-20 02:05 UTC（美西时间 2026-10-19 19:05，归档日期 2026-10-19）。
- 上次运行时刻：2026-10-05 10:51 UTC，间隔约 14.6 天（超 10 天封顶）。
- 实际覆盖窗口：2026-10-09 02:05 UTC – 2026-10-20 02:05 UTC（补漏：按 10 天封顶，并补收 2026-10-05 10:51 UTC – 2026-10-09 02:05 UTC 缺口期内重要动态）。
- 方向 A 六项均已通过 WebSearch 与 GitHub Releases / Security Advisories API 交叉核查。结果：Istio 于 2026-10-15 发布安全公告 ISTIO-SECURITY-2026-007 及补丁版本 1.31.2、1.30.6、1.29.9（1.29 已于 2026-10-12 EOL），修复 HTTP/2 下 AuthorizationPolicy 方法大小写绕过（GHSA-w44g-8m76-8gc5，CVSS 7.4，与历史 CVE-2021-39155 同源，同样影响读者在用的 Istio 1.25 且有配置层缓解方案，收录进"需要行动"）、Ambient 模式 waypoint 地址冲突致 istiod 崩溃循环（GHSA-7p2q-4xvg-vxc6，CVSS 7.7）及 Envoy OAuth2/api_key_auth 过滤器处理无 :path 的 CONNECT 请求崩溃（GHSA-8vc2-jrm4-835w CVSS 7.5、GHSA-47vj-9r25-wv5j CVSS 6.5）；Helm 于 2026-10-15 同步发布 v4.3.1 与 v3.22.1（修复 Go 依赖漏洞及 HookOnlyStrategy CRD 等待问题，收录进"留意"）；AWS Load Balancer Controller 于 2026-10-05 20:21 UTC（上次运行之后）发布 v3.6.0（新增 frontend-nlb-status-only 注解、修复安全组 CIDR 规范化与分权 DNS ACM 校验问题，收录进"留意"）；Kustomize 于 2026-10-08 发布 v5.8.3（纯依赖清理，无功能变更，仅更新栈位差）；Kubernetes 本体无新稳定版（最新仍为 v1.37.1，v1.37.2/v1.36.6/v1.35.10 尚未发布，窗口内仅发布 v1.38.0-alpha.2 不收）；AWS EKS 无新控制面版本或触及本栈的破坏性变更；Flux CD 最新仍为 v2.9.6（2026-10-01）；Kyverno 最新稳定版仍为 v1.19.1（v1.19.2-rc3 为预发布，无新安全公告）；SOPS 最新仍为 v3.13.3。方向 B/C 未检出满足门槛的窗口内新事件（CNCF Karmada 毕业实为 2026-09-07，早于窗口，不收）。
- 本期新增"需要行动"1 条（Istio ISTIO-SECURITY-2026-007）、"留意"2 条（Helm v4.3.1/v3.22.1、ALBC v3.6.0）。
- 版本清单已 66 天未复核（确认日 2026-08-14），未超 90 天，未写超期提示。
- 进行中事件表：Istio GCP 制品托管退役（2026-10-13 第二轮 3 小时 scream test 已过，继续追踪 11-17 与 12-08 窗口）；新增追踪 ISTIO-SECURITY-2026-007 四项 GHSA 的正式 CVE 编号分配。

## 2. 已报条目清单（最近 21 天）

2026-10-01 | AWS 宣布 EKS 与 EKS Distro 正式支持 Kubernetes 1.37 | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-distro-kubernetes-version-1-37/
2026-10-05 | AWS Load Balancer Controller v3.6.0 发布，新增 frontend-nlb-status-only 注解并修复安全组 CIDR 规范化及分权 DNS ACM 证书校验问题 | https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.0
2026-10-15 | Istio 发布安全公告 ISTIO-SECURITY-2026-007 与 1.31.2/1.30.6/1.29.9（1.29 同批 EOL），修复 HTTP/2 AuthorizationPolicy 方法大小写绕过（GHSA-w44g-8m76-8gc5，CVSS 7.4）、Ambient istiod 崩溃循环（GHSA-7p2q-4xvg-vxc6，CVSS 7.7）及两项 Envoy CONNECT 请求崩溃漏洞 | https://istio.io/latest/news/security/istio-security-2026-007/
2026-10-15 | Helm v4.3.1 与 v3.22.1 发布，修复上游 Go 依赖漏洞及 HookOnlyStrategy 下未等待 CRD 就绪问题 | https://github.com/helm/helm/releases/tag/v3.22.1

## 3. 进行中事件表

- 事件：Istio GCP 制品托管退役（gcr.io/istio-release 等旧地址断供）| 最后进展日期：2026-10-13（第二轮 3 小时 scream test 窗口执行）| 下一步关注点：关注 2026-11-17（6 小时）与 2026-12-08（24 小时）后续 scream test 及 12 月正式关停公告。
- 事件：Istio ISTIO-SECURITY-2026-007 四项 GHSA 正式 CVE 编号分配 | 最后进展日期：2026-10-15（GHSA-w44g-8m76-8gc5、GHSA-7p2q-4xvg-vxc6、GHSA-8vc2-jrm4-835w、GHSA-47vj-9r25-wv5j 披露时 CVE 栏均为空）| 下一步关注点：核查 GitHub Security Advisories 与 NVD 是否为上述四项分配正式 CVE-2026-* 编号（影响依赖 CVE 匹配的扫描器告警）。

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
