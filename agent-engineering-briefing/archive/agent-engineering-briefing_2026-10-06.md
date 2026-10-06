# 🛠️ AI Agent 工程简报 · 2026-10-06

> 覆盖窗口：2026-10-05 10:01 UTC 至 2026-10-06 10:01 UTC（常规）

## 开发者工具与工作流

- Claude Code 发布 v2.1.290：Mods 插件 hook 新增 `serverToolUses` 工具调用明细、`tool.check` 事件带 `agentId` 以区分 subagent 权限检查、审批要求新增 `ceiling`；修复含数百张图片的长会话卡在 "Request rejected as unprocessable"、WebFetch 静默丢弃 10 万字符之后的页面文本（现提示未读量并支持 `offset`）、compaction 后定时任务在 resume 时丢失、plan mode 误批非只读 connector 工具。写 Mods 做权限/审计的人可按 agentId 精细化策略，依赖 WebFetch 长页面的 skill 应留意截断提示与 offset 用法。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- Claude Code v2.1.291 紧急修复两处回归：2.1.290 引入的云端 session 丢失权限提示答复，以及 2.1.288 引入的退出时丢失会话最后几条消息。云端/无人值守场景若已升到 v2.1.290，建议直接升到 v2.1.291。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- OpenAI Codex CLI 发布 rust-v0.160.1：启动带显式远程环境变量的远程 stdio MCP server 时保留 SYSTEMROOT/TEMP/TMP，使 Unix 主机上的 Windows executor 能保持启动环境。跨平台远程跑 MCP server 的团队可借此排查 Windows 执行端启动失败问题。来源：GitHub openai/codex releases https://github.com/openai/codex/releases
- GitHub Copilot CLI v1.0.92 转为正式版：新增 `copilot config` 子命令与本地/云端环境选择器，shell 工具调用实时流式输出 stdout/stderr，沙箱 shell 默认不再带 GitHub token。需要在沙箱里跑 agent 的团队可核对默认不传 token 是否影响现有脚本。来源：GitHub github/copilot-cli releases https://github.com/github/copilot-cli/releases
