# 🛠️ AI Agent 工程简报 · 2026-11-17

> 覆盖窗口：2026-11-16 10:15 UTC 至 2026-11-17 10:15 UTC（常规）

今日要闻：Claude Code v2.1.326 允许在启用 agent teams 时开启 Code Mode，并修复多项权限规则、会话恢复与压缩缺陷。

## 开发者工具与工作流

- Anthropic 发布 Claude Code v2.1.326：Code Mode 可与 agent teams 同时启用，`/status` 新增显示被 provider 或 `DISABLE_TELEMETRY` 等环境变量关闭的功能，`--allowedTools` 等条目写法不完整时启动即告警，并修复 Bash `cp` 被 Edit deny 规则误拒、崩溃/低内存后恢复会话丢失近期轮次、Bedrock/Vertex/Foundry 压缩失败等问题。值得关注：多 agent 编排与 Code Mode 可叠加试用，权限规则写错会提前暴露，排查自定义 allow/deny 规则时可先看 `/status` 与启动警告。（发布时间未确认，仅知为 11 月 16 日）来源：GitHub Claude Code Releases https://github.com/anthropics/claude-code/releases
