# ☁️ 云原生周报 · 2026-09-28

> 覆盖窗口：2026-09-21 至 2026-09-28（常规）

## 需要行动

- 【续报】Kyverno CVE-2026-100703~100707：2026-09-26 官方为 2026-09-10 披露的 5 个 GHSA 正式分配 CVE 编号：CVE-2026-100706（apiCall urlPath 路径校验绕过提权至集群管理员，CVSS 9.9）、CVE-2026-100707（同类命名空间隔离绕过，CVSS 7.7）、CVE-2026-100703（globalcontext.Lib CEL 跨命名空间读取，CVSS 7.7）、CVE-2026-100704（ImageValidatingPolicy 跳过镜像签名校验，CVSS 7.7）、CVE-2026-100705（apiCall/GlobalContextEntry SSRF，CVSS 7.6）。均已随 v1.19.1（2026-09-10）修复，动作未变。影响：正式 CVE 编号落地后，依赖 CVE 匹配的漏洞扫描/合规工具才会真正告警；你的 Kyverno 版本未确认，凡低于 v1.19.1 均在受影响范围。动作：核实当前 Kyverno 版本，若低于 v1.19.1 则升级。来源：GitHub Security Advisories https://github.com/kyverno/kyverno/security/advisories/GHSA-5qq8-67g6-4h2w

## 留意

- Istio GHSA-qm8v-g4f9-qhjx（CVSS 6.8）：BackendTLSPolicy 引用的 CA 无法解析时曾静默降级为明文而非拒绝连接，已随 1.29.8/1.30.5/1.31.1（2026-09-21）修复为 fail-closed。影响：该特性需 Istio ≥1.28 才稳定支持（≥1.26 为实验特性），你在用的主集群 1.25 不具备该功能，暂不受影响。动作：暂无，等你升级至 1.28 及以上并启用 BackendTLSPolicy 时再评估。来源：GitHub Security Advisories https://github.com/istio/istio/security/advisories/GHSA-qm8v-g4f9-qhjx

## 栈位差

| 组件 | 我在用 | 当前最新 | 落后 | 支持窗口 | 我方版本确认日 |
| --- | --- | --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本（未给具体版本号） | 1.36（上游 1.37 已 GA；EKS Distro 已放出 1.37 预览包，管理控制面尚未正式支持） | — | — | 2026-08-14 |
| Kubernetes 本体 | 同 EKS 控制面版本（未给具体版本号） | v1.37.1（2026-09-23，纯缺陷修复，无 CVE） | — | — | 2026-08-14 |
| Istio（主） | 1.25 | 1.31.1（2026-09-21） | 6 档 | 已出窗口（自 2025-09-22 起） | 2026-08-14 |
| Istio（遗留） | 1.16 | 1.31.1 | 15 档 | 已出窗口（自 2023-07-25 起） | 2026-08-14 |
| Flux CD | 未确认 | v2.9.5（2026-08-31） | — | — | — |
| Kustomize | 未确认 | v5.8.1（2026-02-09） | — | — | — |
| Helm | 未确认 | v4.3.0 / v3.22.0（v3 线路计划内最后一个 minor 版本） | — | — | — |
| Kyverno | 未确认 | v1.19.1（2026-09-10） | — | — | — |
| SOPS | 未确认 | v3.13.3（2026-07-23） | — | — | — |
| AWS Load Balancer Controller | 未确认 | v3.5.0（2026-08-03） | — | — | — |
