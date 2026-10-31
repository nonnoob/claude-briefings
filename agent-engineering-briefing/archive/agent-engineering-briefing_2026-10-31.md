# 🛠️ AI Agent 工程简报 · 2026-10-31

> 覆盖窗口：2026-10-26 08:25 UTC 至 2026-10-31 11:32 UTC（常规）

今日要闻：Claude Code 增加工作目录外写入限制，并修复非交互启动失败却返回成功的问题，自动化任务应同步检查权限与退出码。

## Agent/Skill 设计模式

- VS Code 1.144 公布 Agent Host Protocol v1.0，支持通过 WebSocket 连接 Agent Host，并提供六种语言的库；自建客户端可评估协议接入，避免将会话控制绑定到某一编辑器界面。来源：Microsoft https://code.visualstudio.com/updates/v1_144

## Prompt 与 Context 工程

- 【续报】Claude Code v2.1.311 修复压缩后仍使用旧 MEMORY.md／CLAUDE.md、子 Agent 无法使用稍后接入的 MCP 工具，以及后代 Agent 未结束就清理隔离 worktree 的问题；长会话回归用例应覆盖「压缩后规则更新」和「后台后代仍在运行」两条路径。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.311
- 【续报】Claude Code v2.1.312 阻止仅部分读取大指令文件后直接整文件覆写，并修复 Bash 切换目录后的路径级 Skill 发现；维护大型规则文件时，应完整读取再覆写，或改用局部编辑。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.312

## 开发者工具与工作流

- 【续报】Claude Code v2.1.314 新增 `permissions.blockWritesOutsideWorkingDirectories`，启用后各权限模式下的 Write、Edit、NotebookEdit 都拒绝工作目录外写入，并让 `claude -p` 启动失败返回退出码 1；该限制针对这些工具，不能替代终端进程的系统级隔离。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.314
- 【续报】Codex rust-v0.166.0 新增 `codex queue --resume` 与 `codex doctor --network-only`，修复恢复／派生会话时已确认权限和推理 token 计数的保留；队列重启流程可改用恢复入口，并针对权限是否延续做回归检查。来源：OpenAI https://github.com/openai/codex/releases/tag/rust-v0.166.0
- 【续报】Copilot CLI v1.0.105 修复长上下文会话中选择 Copilot Fusion High／Max 不生效的问题；受影响的多模型评测应更新客户端后重跑，不宜把旧版本的选择失败当作模型能力差异。来源：GitHub https://github.com/github/copilot-cli/releases/tag/v1.0.105
- 【续报】VS Code 1.144 的 Copilot harness 恢复实验性 Keep／Undo 工作集，但终端命令造成的文件改动不进入该工作集；代码验收仍需查看完整 Git diff，不能只审核聊天面板列出的改动。来源：Microsoft https://code.visualstudio.com/updates/v1_144

## 模型能力与 API 更新

- Claude Code v2.1.316 公告：Opus 4.8 fast mode 已于 10 月 30 日弃用，将于 11 月 30 日移除，届时请求直接报错而不自动回退；仍固定该模式的任务应提前切换受支持模型，并验证错误处理。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.316
