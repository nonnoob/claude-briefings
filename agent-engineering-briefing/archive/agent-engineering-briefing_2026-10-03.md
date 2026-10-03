# 🛠️ AI Agent 工程简报 · 2026-10-03

> 覆盖窗口：2026-10-02 10:00 UTC 至 2026-10-03 10:01 UTC（常规）

## 开发者工具与工作流

- Claude Code 发布 v2.1.288（10-02）：非交互会话与 subagent 遇 API 超时改为基于已收到的部分响应继续而非直接失败，修复 `--resume` 在 compaction 时丢文件/上下文，auto mode 对长对话改为先压缩再继续而非逐个工具调用询问，新增 `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS` 以兼容拒绝 structured outputs 的网关，并支持 2025-11-25 协议 MCP 服务器的 URL 交互式登录提示。长任务/无人值守 agent 的超时与 resume 可靠性明显提升，用网关或跑 subagent 的团队建议升级并检查结构化输出开关。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- 【单源】GitHub Copilot CLI 连续推送 v1.0.92-1 至 v1.0.92-3 预发布：修复 MCP 服务器重连与上下文恢复，Windows 沙箱命令改写入授权的临时目录（解决"临时文件 rename"类工具失败），新增会话前 Ctrl+E 本地/云端运行环境选择器。依赖 MCP 长会话或 Windows 沙箱的用户可关注下个正式版。来源：agents-radar AI CLI Tools Digest 2026-10-03（转引 Copilot CLI release） https://github.com/kouweizhu/agents-radar/issues/324

## 案例与最佳实践复盘

- 【单源】Simon Willison 发布《Highlights from my conversation about agentic engineering on Lenny's Podcast》（10-02），梳理他在播客中关于 agentic engineering 实践的要点；可作为了解其编码 agent 工作方法的浓缩入口，正文未能直接读取，具体观点待下期核实。来源：Simon Willison's Weblog（无公开链接：站点被代理拦截，仅由搜索摘要得知标题与日期）

## 社区热议与争议

- 【单源】HN 10-02 前页出现 DeepSeek 桌面版 Harness（macOS/Windows）发布的讨论；其 Harness 核心 runtime 此前已开源（"一切皆插件"：模型适配、工具注册、session log 乃至 agent loop 均可替换，四种运行模式，MIT 许可，开发者预览），本条仅指桌面端新动向，具体功能细节未取得。想评估插件化 harness 架构的人可对照 Pi 1.0 的极简路线比较。来源：Hacker News 前页日报（research-issues #1945） https://github.com/jjakimoto/research-issues/issues/1945
