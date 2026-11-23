# ☁️ 云原生周报 · 2026-11-23

> 覆盖窗口：2026-11-16 10:50 UTC 至 2026-11-23 10:50 UTC（常规）

今日要闻：Istio 官方确认 GCP 旧镜像仓库将于 2026-12-16 停服，仍从 gcr.io/istio-release 拉取的需在此前迁走。

## 需要行动

- 【续报】Istio 旧制品托管退役：官方博客确认 gcr.io/istio-release、registry.istio.io/release、istio-release.storage.googleapis.com 将于 2026-12-16 15:00 UTC 正式停服；11-17 已执行 6 小时 scream test，下一轮 12-08/09。影响：任何从这些地址拉取 istiod/proxy 镜像或 Helm 制品的链路（含 Flux HelmRepository/OCI 源、镜像镜像同步配置）会在停服后拉取失败；读者具体拉取地址未知，此处为假设。动作：核查各集群与 Flux 源是否仍引用上述地址，12-16 前迁至 docker.io/istio 或自有拉取缓存，Helm 制品迁至 ghcr.io/istio/release 或 blob.istio.io。来源：Istio 官方博客 https://istio.io/latest/blog/2026/retirement-of-gcp/

## 留意

- 【续报】Kyverno v1.20.0：下游已出现升级破坏报告（如 Gardener 依赖的旧版 ClusterPolicy 不再被执行），印证旧版策略类型升级后不再生效，Helm 默认闸门会拦截含旧版策略的升级。影响：读者 Kyverno 版本与策略类型仍未确认，现在不必动。动作：暂无，等读者确认 Kyverno 在用版本及是否仍有旧版 ClusterPolicy，再规划迁移 CEL 策略类型。来源：GitHub kyverno/kyverno 跟踪议题 https://github.com/kyverno/kyverno/issues/17701

## 栈位差

| 组件 | 我在用 | 当前最新 | 落后 | 支持窗口 | 我方版本确认日 |
| --- | --- | --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本 | 1.37（10 月起支持） | — | — | 2026-08-14 |
| Kubernetes | 同 EKS 控制面版本 | 1.37.2 | — | — | 2026-08-14 |
| Istio（主） | 1.25 | 1.32.0 | 7 档 | 已出窗口 | 2026-08-14 |
| Istio（遗留） | 1.16 | 1.32.0 | — | 已出窗口 | 2026-08-14 |
| Flux CD | 未确认 | v2.10.1 | — | — | — |
| Kustomize | 未确认 | v5.8.3 | — | — | — |
| Helm | 未确认 | v4.3.2 / v3.22.1 | — | — | — |
| Kyverno | 未确认 | v1.20.0 | — | — | — |
| SOPS | 未确认 | v3.13.3 | — | — | — |
| AWS Load Balancer Controller | 未确认 | v3.6.3 | — | — | — |

版本清单已 101 天未复核：AWS EKS、Kubernetes、Istio（主）、Istio（遗留），请确认后更新 MEMORY.md 第 4 节。
