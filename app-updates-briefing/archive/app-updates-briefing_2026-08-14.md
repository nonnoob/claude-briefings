# 🛠️ 开发工具更新周报 · 2026-08-14

## Claude App 更新

- Claude Code v2.1.232 发布(2026-08-13 23:29 UTC),新增 subagent fork 模式默认开启(`subagent_type: "fork"` 子代理继承完整对话历史与 prompt 缓存)、输入 `@` 可跨会话直接提及并通过 SendMessage 通知另一个 Claude 会话、GitLab token 家族(glrt-/gloas-/glptt- 等)密钥脱敏与 GitLab 仓库插件市场支持;修复 PowerShell 参数覆盖 `$PSDefaultParameterValues` 权限绕过、Windows Git Bash 跟随 Cygwin 风格软链接绕过路径校验、嵌套 git 仓库继承父目录信任等安全问题,累计约 49 项改动 — 来源:[GitHub Releases](https://github.com/anthropics/claude-code/releases/tag/v2.1.232)
- 【续报】Claude Code Auto Mode 已于今日(8/14)起正式对 Pro/Max/Team 计划新会话默认开启,按 8/7 原公告时间表如期生效未推迟;已自行固定权限模式的用户不受影响,Enterprise/API/Bedrock/Vertex/Foundry 上仍为可选开启项 — 来源:[Anthropic Blog](https://claude.com/blog/auto-mode-default-in-claude-code)、[TechCrunch](https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/)
