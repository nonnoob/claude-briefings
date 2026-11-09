# ☁️ 云原生周报 · 2026-11-09

> 覆盖窗口：2026-11-06 16:22 UTC 至 2026-11-09 21:50 UTC（常规）

今日要闻：Istio 发布安全公告 ISTIO-SECURITY-2026-009 与 1.31.4/1.30.8 补丁，修复 istiod 调试 xDS 请求崩溃循环、Sidecar conntrack 流量劫持绕过及 AuthorizationPolicy 主机头大小写敏感绕过等 8 项漏洞。

## 需要行动

- Istio ISTIO-SECURITY-2026-009（8 项 GHSA，最高 CVSS 8.2 高危）与 1.31.4 / 1.30.8：2026-11-06 官方发布安全公告及 1.31.4、1.30.8 补丁版本（1.29 已 EOL 不再提供补丁，正式 CVE 编号待分配），集中修复 8 项安全漏洞——其中触及标准控制面与 Sidecar 数据面的包括：`GHSA-635j-qv98-9275`（CVSS 7.7 高危，持有合法网格身份的任意工作负载发送资源名无法通过 URL 解析的畸形 `istio.io/debug` xDS 请求即可触发 `istiod` 持续崩溃循环）、`GHSA-cxwg-46mx-q8hf`（CVSS 7.4 高危，`iptables`/`nftables` 流量劫持模式下复用刚断开连接四元组的新入站连接可命中残留 `conntrack ESTABLISHED` 表项从而绕过 Sidecar 代理，补丁通过前置 `SYN` 规则修复）、`GHSA-7m6f-j3gp-2r53`（CVSS 6.5 中危，`AuthorizationPolicy` 的 `when` 条件匹配 `request.headers[:authority]` 或 `request.headers[host]` 时此前按大小写敏感求值，攻击者变换主机头大小写即可绕过策略）及 `GHSA-gf6w-6mxv-5fj4`（CVSS 6.3 中危，多集群场景下代理引导时可冒用其他集群 `CLUSTER_ID` 通过 SDS 获取目标集群 `kubernetes://` Secret）；同批还修复了 Ambient 模式 `PeerAuthentication` 算符优先级错误跳过端口级 `STRICT` 致明文放行（`GHSA-rr2c-p22p-6r9r`，CVSS 8.2 高危）、`ztunnel` 解析畸形 55 字节 `traceparent` 头 panic（`GHSA-77vw-rg85-wx5x`，CVSS 6.5）、Ambient `AuthorizationPolicy` 空 `to`/`from` 条目漏检致 `istiod` 崩溃循环（`GHSA-8jw7-82jp-wr2c`，CVSS 6.3）及 HBONE 链路 `ipBlocks`/`source.ip` 误匹配内部监听器地址致 DENY 失效（`GHSA-9gqj-583v-mpqp`，CVSS 5.6），此外 1.31.4/1.30.8 还修复了 JWKS 后台刷新缓存漏洞与仅注解元数据更新触发冗余 xDS 推送的问题。影响：官方公告虽仅列支持窗口内的 1.30.0–1.30.7 与 1.31.0–1.31.3，但 `istiod` 调试 xDS 崩溃循环、Sidecar `conntrack` 劫持绕过、`AuthorizationPolicy` 主机头 `when` 条件大小写敏感绕过及多集群 SDS `CLUSTER_ID` 冒用均落在通用控制面与 Sidecar 链路上，你在用的主集群 Istio 1.25 同样暴露于上述风险。动作：排查集群内 `AuthorizationPolicy`，将针对 `request.headers[:authority]` 或 `request.headers[host]` 的 `when` 条件改写为大小写不敏感的 `to[].operation.hosts`/`notHosts` 字段（或在网关层规范化主机头大小写）以立即缓解，收紧不可信负载对控制面调试通道的访问及多集群令牌边界，并推进主集群从已出窗口的 1.25 升级至 1.30.8 或 1.31.4。来源：Istio Security Bulletin https://istio.io/latest/news/security/istio-security-2026-009/
- 【续报】Kyverno CVE-2026-124440 与 CVE-2026-124441（v1.19.2 批次剩余两项高危/严重级 GHSA 正式分配 CVE 编号）：继 11-03 至 11-05 分配 `CVE-2026-122300` 至 `CVE-2026-122323` 后，NVD 与 CVE.org 于 2026-11-08 至 11-09 为 Kyverno v1.19.2（2026-10-20 发布）26 项安全公告中的最后两项多租户越权漏洞补齐正式 CVE 编号——`CVE-2026-124440` 对应 `GHSA-39w8-hv5g-f73w`（CVSS 9.9 严重，v1.19.1 引入的 `apiCall` 命名空间钳制被 `urlPath` 畸形百分号转义绕过，命名空间租户可借 `admission-controller` 权限发起跨命名空间与集群级请求并提权至集群管理员），`CVE-2026-124441` 对应 `GHSA-vjfx-fp68-rh4v`（CVSS 8.8 高危，`< v1.19.2` 中命名空间租户在 `generate` 规则目标 `kind` 与 `namespace` 字段使用变量模板时可绕过鉴权，诱导 `background-controller` 向任意受害命名空间或 `kube-system` 写入 `RoleBinding`/`NetworkPolicy` 等敏感资源）；至此 v1.19.2 批次全部 26 项 GHSA 均已入库 NVD，修复版本仍为 v1.19.2。影响：两项新 CVE 编号入库后，安全扫描器将针对 `CVE-2026-124440` 与 `CVE-2026-124441` 触发新增告警；你的 Kyverno 版本未确认，凡低于 v1.19.2 均受影响。动作：核实当前 Kyverno 版本并升级至 v1.19.2（Helm chart 3.9.2），暂未升级前严格限制命名空间级 `Policy` 创建权限。来源：GitHub Security Advisories https://github.com/kyverno/kyverno/security/advisories/GHSA-39w8-hv5g-f73w

## 留意

- AWS EKS AWS Nitro Sandboxes（基于 Nitro 硬件虚拟化的 Pod 级微虚拟机强隔离）：2026-11-09 AWS 宣布在 Amazon EKS（以及 ECS 与 EC2）上推出 AWS Nitro Sandboxes，允许通过 Kubernetes `RuntimeClass` 将单个 EKS Pod 封装在由 AWS Nitro Hypervisor 驱动的独立轻量级硬件隔离虚拟机中运行（在支持的 Nitro EC2 实例上无额外沙箱软件费用），阻断共享宿主机 Linux 内核带来的容器逃逸与跨租户内核攻击面；该模式原生兼容 Amazon VPC CNI、EKS Pod Identity、EBS/EFS/S3 存储驱动、CoreDNS 与 CloudWatch，并支持密码学证明（cryptographic attestation）以仅向通过完整性校验的沙箱释放 KMS 密钥。影响：该能力为按需通过 `RuntimeClass` 启用的可选隔离运行时，不改变现有 EKS 节点与 Pod 默认运行行为，当下不必改动生产配置。动作：暂无，等集群需要运行不受信代码、多租户强隔离负载或高权限 CI/CD 任务并评估 Pod 级硬件内核隔离时再测试启用。来源：AWS Containers Blog https://aws.amazon.com/blogs/containers/aws-nitro-sandboxes-hardware-enforced-workload-isolation-on-amazon-eks/

## 栈位差

| 组件 | 我在用 | 当前最新 | 落后 | 支持窗口 | 我方版本确认日 |
| --- | --- | --- | --- | --- | --- |
| AWS EKS | 跟随最新 GA 版本 | 1.37 | —，实际版本未确认 | 我方剩余支持期未确认；1.37 标准支持至 2027-12-01，延长支持至 2028-12-01；https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html | 2026-08-14 |
| Kubernetes | 同 EKS 控制面版本 | 1.37.2 | —，实际版本未确认 | 上游支持最近三个 minor；1.34 已于 2026-10-27 EOL，不能据此推断 EKS 1.34 已停服；https://kubernetes.io/releases/ | 2026-08-14 |
| Istio（主） | 1.25 | 1.31.4 | 6 个 minor | 已出窗口（1.25 于 2025-09-30 EOL）；https://istio.io/latest/docs/releases/supported-releases/ | 2026-08-14 |
| Istio（遗留） | 1.16 | 1.31.4 | 15 个 minor | 已出窗口（1.16 于 2023-07-25 EOL）；https://istio.io/latest/docs/releases/supported-releases/ | 2026-08-14 |
| Flux CD | 未确认 | 2.10.0 | — | 我方支持状态未确认；当前版支持 Kubernetes 最近三个 minor（最低补丁 1.35.2／1.36.1／1.37.0）；https://github.com/fluxcd/flux2/releases/tag/v2.10.0 | — |
| Kustomize | 未确认 | 5.8.3 | — | 未确认；版本来源 https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize/v5.8.3 | — |
| Helm | 未确认 | 4.3.1／3.22.1 | — | 我方支持状态未确认；版本来源 https://github.com/helm/helm/releases | — |
| Kyverno | 未确认 | 1.19.2 | — | 我方支持状态未确认；版本来源 https://github.com/kyverno/kyverno/releases/tag/v1.19.2 | — |
| SOPS | 未确认 | 3.13.3 | — | 未确认；版本来源 https://github.com/getsops/sops/releases/tag/v3.13.3 | — |
| AWS Load Balancer Controller | 未确认 | 3.6.2 | — | 未确认；版本来源 https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/tag/v3.6.2 | — |
