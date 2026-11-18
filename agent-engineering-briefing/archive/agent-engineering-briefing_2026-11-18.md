# 🛠️ AI Agent 工程简报 · 2026-11-18

> 覆盖窗口：2026-11-17 10:15 UTC 至 2026-11-18 10:07 UTC（常规）

今日要闻：Claude Code v2.1.327 大版本发布，`mcp add-json` 支持 stdin 传入令牌、修复 `.mcp.json` 被覆盖与子 Agent 模型/权限继承等多处数据丢失与配置类缺陷。

## 开发者工具与工作流

- Anthropic 发布 Claude Code v2.1.327：新增 `claude mcp add-json <name> -` 从 stdin 读取服务器 JSON（令牌不再出现在命令行），修复项目级 `mcp add/remove` 误删 `.mcp.json` 其他顶层键，`/status` 能列出损坏的 agent/skill/command 文件与永不匹配的 hook matcher，子 Agent 恢复时不再沿用兄弟的模型与 effort 并遵循会话权限设置。建议用 `/status` 体检自己的 skill 与 hook 配置，并把含令牌的 MCP 配置改走 stdin。来源：GitHub anthropics/claude-code https://github.com/anthropics/claude-code/releases/tag/v2.1.327
- 【续报】Claude Code v2.1.327 在 Code Mode 方面不再因已安装的 mod 挂钩工具调用而拒绝启动，auto mode 下后续脚本不再被反复弹权限；另有一项提示称 auto mode 回退到计费分类器请求的做法将在后续版本移除，`claude -p` 无人值守脚本届时遇到原本由分类器判定的操作会改为询问或拒绝（出自单个用户的 issue 报告）。依赖 `claude -p` 的自动化应提前为这类操作配置显式 allow/deny 规则。来源：GitHub Adam-S-Daniel/wsl-automation Issue #123 https://github.com/Adam-S-Daniel/wsl-automation/issues/123
- OpenAI 发布 Codex CLI rust-v0.170.0：TUI 支持 WebRTC 实时语音通话协商，OpenTelemetry HTTP 导出器支持自动刷新的认证头，实验性支持跨环境保留同名 MCP 服务器，并修复 MCP OAuth 凭证竞态。多环境同名 MCP 服务不再冲突，对统一配置多套工作区的团队有直接帮助。来源：GitHub openai/codex https://github.com/openai/codex/releases/tag/rust-v0.170.0
- GitHub Copilot CLI 发布 v1.0.113：管理员可通过托管设置 `features.browserUse` 关闭内置 Browser Use（对已运行会话也生效）；社区摘要称同版本把 SDK 包从 @github/copilot-sdk 改名为 @microsoft/copilot-sdk 且无迁移说明（官方说明未证实）。企业环境可借此收紧浏览器类工具，SDK 用户升级前先核对依赖名。来源：GitHub github/copilot-cli https://github.com/github/copilot-cli/releases/tag/v1.0.113

## 模型能力与 API 更新

- 【单源】MCP 官方博客宣布改为固定的每六个月一次的规范发布节奏（通常为 3 月与 9 月最后一个周二），当前规范仍为 2026-07-28 版（协议无状态化），下一目标约 2027-03-30，文件上传/下载作为实验性扩展探索中。做 MCP server 的团队可按此节奏规划兼容性升级，不必追逐临时变更（下一目标日期未经官方路线图直接确认）。来源：Model Context Protocol Blog https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/
