# 🛠️ 开发工具更新周报 · 2026-10-02

> 覆盖窗口：2026-09-28 17:10 UTC 至 2026-10-02 10:36 UTC（常规）

## VSCode 更新

- VS Code 1.140 正式版发布，新增跨文件夹 Agent 会话（Multi-folder sessions，实验性）、远程主机任务委托（Remote delegation，实验性），并上线多模型协同起草/互评/修订的 HydraFusion 研究预览。来源：VS Code Updates https://code.visualstudio.com/updates/v1_140
- 同版本新增共享 worktree 文件夹（复用依赖安装、避免重复产物，实验性），并支持在工作区根目录 `.mcp.json` 中配置可随仓库共享的 MCP 服务器。来源：VS Code Updates https://code.visualstudio.com/updates/v1_140

## Claude App 更新

- Anthropic 发布 Claude Sonnet 5.5：维持 Sonnet 5 原定价（$2/$10 每百万 token），据官方测试输出速度提升超 30%、单任务成本平均降低约 30%，支持 100 万 token 上下文；是首个采用对标高能力模型的网络安全防护措施的 Sonnet 模型；Claude Code v2.1.284 同步将其设为默认 Sonnet 模型。来源：Anthropic https://www.anthropic.com/claude-sonnet-5-5
- Claude Code v2.1.285 发布，新增 `claude --desktop`（命令行定位当前目录打开 Claude 桌面应用）与 `claude plugin configure` 插件配置命令，新增 `allowedProviders` 托管设置以限制可用 API 供应商。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- Claude Code v2.1.286 发布，堆叠权限请求新增"2 of 5"进度计数提示，VS Code 插件新增用于保存 Claude 回复的书签面板及带选项预览的提问卡片。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.286
- Claude Code v2.1.287 发布，新增 Mods 机制：插件可用 TypeScript 函数改写提示词、替换内置功能或新增 UI，默认启用且不设沙盒隔离；同时内置 "You should know" 旁路 agent 风险提醒功能。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.287
