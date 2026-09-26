# 🛠️ AI Agent 工程简报 · 2026-09-26

> 覆盖窗口：2026-09-25 10:01 UTC 至 2026-09-26 10:01 UTC（常规）

## 开发者工具与工作流

- 【续报】Claude Code 发布 v2.1.283：auto mode（服务端权限分类器）成为 Bedrock、GCP Agent Platform、Microsoft Foundry、Claude Platform on AWS、Claude apps gateway 及 Enterprise/Console API key 上交互式终端与 VS Code 会话的默认起始权限模式，不再局限于 Pro/Max/Team（`claude -p`/Agent SDK 仍默认 manual，组织可用 `permissions.disableAutoMode` 关闭）。这是"少监督、多分类器"权限模型推向企业与云平台部署的收官一步，无人值守/CI 场景下的默认安全姿态因此改变，值得据此重新核查组织级权限策略。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- Claude Code v2.1.283 同时新增 `/doctor prompt-audit`（同 `/checkup prompt-audit`）：扫描 CLAUDE.md、skills、agents 与自定义命令，标记为旧模型写就、已过时的 prompting 模式；另新增 `availableModelsMatch`/`deniedModels` 组织级模型锁定配置，以及 MCP/WebFetch/WebSearch 输出的 OpenTelemetry `tool.output` span 捕获（`OTEL_LOG_TOOL_CONTENT=1`）。给 agent/skill 维护者提供了内置的"提示词过时"体检工具，模型迭代后可以直接跑一遍再决定要不要重写。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- GitHub Copilot CLI 发布 v1.0.89-4：修复 ACP 会话在客户端暂停读取大响应时被断开、Gemini 模型因 MCP 工具 schema 混用 type/properties 与 anyOf 而报 400、GitHub MCP 工具登录后首次启动不自动连接等问题，并让包裹 `gh`/`git` 的命令（如 `timeout 60 gh ...`）改在沙箱会话中执行。这类问题此前会在不易察觉的情况下静默打断 agent 的工具调用链路，排查类似故障时可直接对照。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases/tag/v1.0.89-4
- 【单源】OpenHands 发布 v1.24.0：修复 agent-server 运行时绕过 `/api/cloud-proxy` 直连、ACP 工具调用内容块渲染缺失、云端保存时 OAuth 凭据被意外重置需重新授权等问题。多后端部署 OpenHands agent 时，这批修复直接影响会话稳定性与鉴权可靠性。来源：GitHub Releases https://github.com/All-Hands-AI/OpenHands/releases/tag/v1.24.0
- 【单源】Anthropic 上线"Build plugins for Claude"插件提交入口：面向付费计划开放自助提交，要求基于 MCP 2.0（无状态核心）打包单个远程 MCP 连接器，或打包含 MCP server + Agent Skills 的 GitHub 仓库组合包，并提供自动化安全扫描与按渠道/版本的安装分析看板。今后分发 MCP + Skills 组合包时，这是需要遵守的打包与提交规范。来源：Claude Blog https://claude.com/blog/build-plugins-for-claude
