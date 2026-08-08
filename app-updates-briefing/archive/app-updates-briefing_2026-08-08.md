# 🛠️ 开发工具更新简报 · 2026-08-08

## Claude App 更新

- Claude Code v2.1.225 发布：新增网关（gateway）支出上限用量预警（提示会写明上限额度、重置时间及运营方留言）、`claude agents` 对不受信任目录新增工作区信任确认提示；修复长期有效的 `CLAUDE_CODE_OAUTH_TOKEN` 被已登录账号的短期 token 顶替导致无人值守会话中断的问题，以及 macOS 上 MCP OAuth 服务器因钥匙串读取超时而成批误报 401 未认证的问题 — 来源：Claude Code CHANGELOG（<https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md>）
- Claude Code v2.1.225 新增 SendMessage 可按名称主动向其他设备上的 Remote Control 会话发起对话（此前只能被动应答对方消息）；VSCode 插件修复 Focus 视图中待办列表、待确认问题及其上下文被意外折叠消失的问题 — 来源：同上
- Claude Code v2.1.226 发布，仅含稳定性与可靠性修复，未附具体条目 — 来源：同上

运行备注：SKILL.md 正文与本次收到的执行指令存在差异（第2步去重/单源标注规则、第4步进行中事件表格式要求更详细），已按仓库最新正文执行；本会话无定时任务更新工具，未同步远端 prompt。
