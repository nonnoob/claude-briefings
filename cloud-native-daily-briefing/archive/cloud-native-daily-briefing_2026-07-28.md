# ☁️ 云原生每日简报 · 2026-07-28

## CNCF 与社区

- 【续报】KubeCon + CloudNativeCon Japan 2026 预会日今日在横滨 PACIFICO 拉开帷幕（Japan Community Day 等 colocated 活动），正式主会场 keynote 与议题定于 7/29–30。来源：[LF Events](https://events.linuxfoundation.org/kubecon-cloudnativecon-japan/)
- ArgoCon Japan 2026 半日会议今日举行，Argo CD 负责人 Michael Crenshaw（Intuit）分享下一版本路线图提案；同期 Argo CD 3.5（RC 已发布）聚焦 ApplicationSets 转正为稳定一等公民、Impersonation 由 alpha 升级至 beta、repo-server 支持 mTLS、Helm 4 兼容与 Git 提交签名验证等供应链安全能力。对使用者影响：计划升级 Argo CD 的团队可关注 3.5 GA 节奏，ApplicationSet 相关工作流预计改动较大。来源：[CNCF Blog](https://www.cncf.io/blog/2026/07/20/argocon-japan-2026-meeting-the-maintainers-enterprise-insights-and-the-road-to-argo-cd-3-5/)

## 工程实践

- CNCF 博客发布 Linkerd 社区技术文章，演示如何组合"联邦"（同一服务多集群单一入口、自动故障转移）与"镜像"（按名访问指定远程集群服务）两种多集群模式，在 3 个 GKE 集群间构建零停机架构，并提供混沌测试（整集群下线）验证脚本。来源：[CNCF Blog](https://www.cncf.io/blog/2026/07/27/federating-clusters-for-zero-downtime-kubernetes/)

进行中事件持续跟踪：Kubernetes v1.37 仍处于代码/测试冻结后的收尾阶段（无实质新进展，GA 仍定档 8/26）；本轮已就安全通告、云厂商动态、商业动向三个方向检索，未发现落在本期覆盖窗口（2026-07-27 16:18 – 2026-07-28 16:12 UTC）内且满足时效与信号强度要求的新内容。

运行备注：已按仓库最新正文执行，未同步远端 prompt（对应定时任务 trig_01BRa893aujPi2kPRYkmHyBU 由 http_api 创建，本会话工具无权限更新其 prompt）；本会话被限定只能推送至分支 `claude/vigilant-brown-7rhyi9`，已推送，仓库已配置自动合并工作流（改动限于任务目录内时会自动合并进 main）。
