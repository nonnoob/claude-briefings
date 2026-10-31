# ☁️ 云原生周报 · 2026-10-31

> 覆盖窗口：2026-10-26 08:25 UTC 至 2026-10-31 11:32 UTC（常规）

今日要闻：Flux v2.10.0 聚合版本正式发布，升级前须核对 Kubernetes 最低版本及 Notification v1、身份授权配置。

## 留意

- 【续报】Flux v2.10.0 于 10 月 26 日正式发布，支持的 Kubernetes 最低补丁分别为 1.35.2／1.36.1／1.37.0，并落实 Notification v1 废弃字段移除和默认 RBAC 不再授予创建 `serviceaccounts/token` 的权限。影响：读者在用 Flux 版本与相关字段尚未确认，不能断言生产环境已经受影响；计划升级时需核对 `Alert.spec.summary` 等字段迁移，以及确有需要的身份令牌授权。动作：暂无，等实际 Flux／Kubernetes 版本和现用通知、身份配置确认后确定升级方案。来源：Flux https://github.com/fluxcd/flux2/releases/tag/v2.10.0

## 栈位差

| 组件 | 我在用 | 当前最新 | 落后 | 支持窗口 | 我方版本确认日 |
| --- | --- | --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本 | 1.37 | —，实际版本未确认 | 我方剩余支持期未确认；1.37 标准支持至 2027-12-01，延长支持至 2028-12-01；https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html | 2026-08-14 |
| Kubernetes | 同 EKS 控制面版本 | 1.37.2 | —，实际版本未确认 | 上游支持最近三个 minor；1.34 已于 2026-10-27 EOL，不能据此推断 EKS 1.34 已停服；https://kubernetes.io/releases/ | 2026-08-14 |
| Istio（主） | 1.25 | 1.31.3 | 6 个 minor | 已出窗口（1.25 于 2025-09-30 EOL）；https://istio.io/latest/docs/releases/supported-releases/ | 2026-08-14 |
| Istio（遗留） | 1.16 | 1.31.3 | 15 个 minor | 已出窗口（1.16 于 2023-07-25 EOL）；https://istio.io/latest/docs/releases/supported-releases/ | 2026-08-14 |
| Flux CD | 未确认 | 2.10.0 | — | 我方支持状态未确认；当前版支持 Kubernetes 最近三个 minor，最低补丁见上文 | — |
| Kustomize | 未确认 | 5.8.3 | — | 未确认；版本来源 https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize/v5.8.3 | — |
| Helm | 未确认 | 4.3.1／3.22.1 | — | 我方支持状态未确认；版本来源 https://github.com/helm/helm/releases | — |
| Kyverno | 未确认 | 1.19.2 | — | 我方支持状态未确认；版本来源 https://github.com/kyverno/kyverno/releases/tag/v1.19.2 | — |
| SOPS | 未确认 | 3.13.3 | — | 未确认；版本来源 https://github.com/getsops/sops/releases/tag/v3.13.3 | — |
| AWS Load Balancer Controller | 未确认 | 3.6.2 | — | 未确认；版本来源 https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.2 | — |
