# 🛠️ 开发工具更新简报 · 2026-08-09

## Claude App 更新

- Claude Code 的"Auto Mode"（自动模式）将于 8 月 14 日起成为 Pro/Max/Team 计划新会话的默认权限模式：内置分类器逐条审核 Shell 命令与操作，官方 1053 人测试中拦截 89% 的危险命令（人工逐条审批仅拦截 13.6%），使用 Auto Mode 的团队产出 PR 数量提升约 25%；已自行设置过默认权限模式的用户不受影响（会收到一次性切换提示），分类器产生的额外 token 目前不计费。官方仍建议对生产环境高风险改动人工复核。来源：Anthropic 官方博客 [Auto mode is now the default in Claude Code](https://claude.com/blog/auto-mode-default-in-claude-code)；交叉验证：[the-decoder](https://the-decoder.com/anthropic-sets-claude-code-to-auto-mode-by-default-to-protect-developers-from-bad-approvals/)
