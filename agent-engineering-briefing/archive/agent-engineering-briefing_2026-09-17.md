# 🛠️ AI Agent 工程简报 · 2026-09-17

> 覆盖窗口：2026-09-16 至 2026-09-17（常规）

## 开发者工具与工作流

- Claude Code 发布 v2.1.274：修复"unexpected tool_use_id"导致会话陷入无限重试卡死的问题（损坏 transcript 现可自我修复），修复多个 MCP 连接与权限提示误报（Streamable HTTP 超时、list-changed 通知不刷新、403 错误误导为登录过期），新增内存严重不足可见警告与 `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` 启动等待配置。长会话或挂多个 MCP server 的团队可直接受益于这批稳定性修复。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- GitHub Copilot CLI 发布 v1.0.85：vim 编辑模式面向全体用户开放、新增 `/config` 侧边栏与语义化 JSONL 格式的会话/记忆导入、支持 GPT-6 Astra 模型，并新增把工具调用折叠为可展开摘要的"concise" transcript 视图。后一项对高频调用工具、希望终端输出保持可扫读的开发者是直接可用的体验改进。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases
- 【续报】GitSpawn 漏洞（git-config 触发编码 agent 代码执行，此前波及 7 款工具）：Qwen Code 09-16 发布 v0.24.0，更新内容仅为 workflow token 预算与多模态管线，未包含任何安全修复；经核查 Grok Build 官方安全公告页也仍无已发布公告。目前仅 Hermes Agent 已于 09-02 修复，Qwen Code、Grok Build 及 Claude Code 的第二条 fsmonitor 触发路径仍未修复。在这些工具上对不受信仓库运行 agent 的团队需继续手动规避 git config 触发路径。来源：Qwen Code Releases https://github.com/QwenLM/qwen-code/releases
