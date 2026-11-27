# 🛠️ AI Agent 工程简报 · 2026-11-27

> 覆盖窗口：2026-11-26 10:07 UTC 至 2026-11-27 10:07 UTC（常规）

今日要闻：GitHub Copilot CLI 连发 v1.0.117-2 至 -5 预发布，收紧 MCP 工具审批边界并为沙箱加入自定义 CA 配置。

## 开发者工具与工作流

- GitHub Copilot CLI 发布 v1.0.117-2 至 -5 预发布：批准某 MCP 服务器的工具不再连带批准 shell 等内置请求、MCP 服务器名大小写不敏感匹配、Autopilot 逐个询问扩展、沙箱新增 `sandbox.userPolicy.network.extraCaCertificates` 以兼容 TLS 拦截代理、linked worktree 中 git 提交/分支/stash 恢复可用。落地提示：设计 MCP 权限规则时应把"MCP 工具批准"与"内置命令批准"分开，企业代理环境可直接用新配置免去沙箱证书问题。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases

## 模型能力与 API 更新

- 【单源】据第三方对比站报道，OpenAI AgentKit 的部分工作流能力将自 2026-11-30 起停止在 OpenAI 平台运行，建议长时间运行的工作流改用 Agents SDK（PyPI 上 openai-agents 0.26.0 于 11-24 发布）。落地提示：若在用 AgentKit 托管工作流，需在 11-30 前评估迁移到自托管的 Agents SDK 编排；该说法尚未与 OpenAI 官方公告核对。来源：tech-insider.org https://tech-insider.org/ca/claude-agent-sdk-vs-openai-agentkit-vs-google-adk-2026/
