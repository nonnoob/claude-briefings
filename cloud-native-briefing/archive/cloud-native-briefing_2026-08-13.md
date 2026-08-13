☁️ 云原生每日简报 · 2026-08-13

**云厂商动态**

- Amazon EKS 新增 Kubernetes 控制平面组件参数配置能力，可直接调整 kube-scheduler、controller-manager、API server 的运行参数：例如将调度器节点资源适配策略设为 MostAllocated 以提升节点利用率（默认 LeastAllocated 侧重打散）、调节 HPA 响应灵敏度、设置事件保留时长等，覆盖所有 EKS 可用区域；回应了自 2021 年起长期存在的社区诉求，运维团队可据此减少自建 webhook/准入控制器的定制成本 | 来源：AWS What's New | https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-control-plane-configuration-parameters/

---

版本与变更、安全通告、CNCF 与社区、商业动向、工程实践五个板块本期（2026-08-12 12:15 UTC – 2026-08-13 12:16 UTC）经核实均无落在窗口内、且未曾报道过的实质新内容，故整节省略。CNCF 于 2026-08-11 宣布 Cloud Native Buildpacks 毕业，因发布时间早于本期窗口起点（且早于 2026-08-12 上期运行覆盖窗口截止），未纳入本期或上期报道，特此说明以免遗漏。

进行中事件复核：Kubernetes v1.37 发布周期仍停留在 v1.37.0-rc.0，未见新 RC 或 GA 消息，GA 仍定档 8/26；GitHub Actions 8/6 大规模故障的官方 postmortem/根因分析全文截至本次运行仍未发布。两项均继续跟踪。
