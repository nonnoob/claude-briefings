# 🛠️ AI Agent 工程简报 · 2026-10-07

> 覆盖窗口：2026-10-06 10:01 UTC 至 2026-10-07 10:01 UTC（常规）

## 开发者工具与工作流

- 【续报】GitSpawn 漏洞：Claude Code v2.1.292 修复了"沙箱内命令可读取 `/ultrareview` 上传的暂存文件副本"，正是此前追踪的 `/ultrareview` 上传路径；但更新日志未点名 GitSpawn，是否完整闭合仍待确认。落地提示：用 `/ultrareview` 的团队应升级到 v2.1.292，Grok Build 仍无官方公告。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- Claude Code v2.1.292：Agent 工具新增 `effort` 参数、`claude plugin install --marketplace <source>`，mods 新增 `prompt.autocomplete` 事件与 `$.model.complete` 提示缓存，`agent.spawn` hook 覆盖 workflow agent；修复 `permissionMode: auto` 的 subagent 在 auto 不可用时仍进入 auto、PreToolUse hook 批准绕过 UNC 路径权限提示、`claude -p`/Agent SDK 不等待后台命令。落地提示：可按子任务难度给 subagent 指定 effort，并检查依赖 hook 自动放行的权限策略。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- GitHub Copilot CLI v1.0.93-0 至 -4 预发布：命令沙箱经 `/sandbox` 与 `--sandbox` 向全部用户开放（含 localhost 网络支持），MCP 配置变更无需重启会话、下一轮即生效，企业权限可强制托管域名边界。落地提示：MCP server 调试可免重启迭代，沙箱成为可直接试用的默认安全层。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases
