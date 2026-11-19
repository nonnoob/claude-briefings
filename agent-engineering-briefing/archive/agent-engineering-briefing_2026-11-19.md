# 🛠️ AI Agent 工程简报 · 2026-11-19

> 覆盖窗口：2026-11-18 10:07 UTC 至 2026-11-19 10:07 UTC（常规）

今日要闻：Google 发布 Gemini 4 Neon（100 万上下文、四档思考强度、$3/$15 定价），主打更低的每任务成本，agent 选型多了一个高性价比选项。

## 开发者工具与工作流

- Claude Code v2.1.328 发布：auto mode 扩展到 Bedrock、Google Cloud、Microsoft Foundry 与 Claude apps gateway 上的 Opus/Sonnet 4.6，未设权限模式的交互会话默认进入 auto mode；MCP 工具 hook 新增 `onFailure: "block"`，hook 调用失败即阻断被保护的动作；/status 与 claude doctor 会提示 OpenTelemetry exporter 未配置端点。若你在云厂商上跑 Claude Code，可评估 auto mode 减少审批打断；给 MCP hook 加 `onFailure: "block"` 能让安全类 hook 失败时默认拒绝而非放行。来源：Claude Code Changelog（X）https://x.com/ClaudeCodeLog/status/2123226990551445634
- GitHub Copilot CLI v1.0.114 正式版（11 月 18 日 05:59 UTC，上期漏报，发布时间略早于上期窗口）：`copilot mcp enable` 在 mcp-config.json 无效时仍可对多数服务器生效，另修复 /settings 窄终端显示与会话侧栏退出问题。属小幅稳定性更新，MCP 配置一旦写坏也不至于整体失效，可直接升级。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases

## 模型能力与 API 更新

- 【单源】Google 发布 Gemini 4 Neon：按报道 API 定价 $3/$15 每百万 token（缓存输入 $0.15，Batch/Flex 半价），统一 1,048,576 token 上下文与四档思考强度（默认 high），Google 称 Artificial Analysis 评测中每任务成本比 Gemini 4 Carbon 低 32%；Simon Willison 的笔记将 Neon 定位为深度推理、Hydrogen 定位为日常编码与 agent 工作流。该数据为厂商口径且工具调用能力细节未见报道，做 agent 选型时需自行跑 eval，并注意思考 token 计入输出计费。来源：InfoWorld https://www.infoworld.com/article/4250618/google-launches-gemini-4-neon-touting-lower-costs-for-complex-ai-coding-tasks.html
