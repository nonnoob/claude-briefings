# 🛠️ AI Agent 工程简报 · 2026-11-13

> 覆盖窗口：2026-11-12 10:10 UTC 至 2026-11-13 10:10 UTC（常规）

今日要闻：Claude Code v2.1.323 新增实验性 Code Mode，让模型写 JavaScript 批量调用工具。

## 开发者工具与工作流

- Claude Code 发布 v2.1.323：新增实验性、需手动开启的 Code Mode（Claude 编写 JavaScript 来调用自身工具），插件可在 `plugin.json` 用 `engines["claude-code"]` 声明兼容的 Claude Code 版本范围，并修复 `.git`、`.claude` 等敏感路径的 Bash 权限提示及 `--permission-mode auto` 不可用时回退 Manual。Code Mode 可把多次工具往返合并为一段代码以省 token，插件版本范围声明则便于分发 skill/插件时避免版本不兼容。来源：GitHub Releases https://github.com/anthropics/claude-code/releases
- OpenAI Codex CLI 发布 rust-v0.168.0 与 v0.169.0：新增模型提供方浏览与默认选择、`features.tui_workspace` 侧边对话、多个持久化的 side-chat 标签与历史任务搜索，`codex exec` 在不受信目录保持项目配置与 MCP 服务器禁用，并改进运行中 turn 的 steering 送达。想在 CI 或陌生仓库里跑非交互 agent 的人，可借此确认不受信目录下的 MCP 隔离行为。来源：GitHub Releases https://github.com/openai/codex/releases
- GitHub Copilot CLI 发布 v1.0.110 正式版与 v1.0.111-0 预发布：企业托管的 Shell/Bash/PowerShell 权限规则支持正则，新增 `--host-allow-session-creation` 允许远程客户端在 CLI 主机创建会话。需要统一管控 agent 命令权限的团队可用正则规则收紧或放行命令模式。来源：GitHub Releases https://github.com/github/copilot-cli/releases
