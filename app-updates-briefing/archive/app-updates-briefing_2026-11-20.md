# 🛠️ 开发工具更新周报 · 2026-11-20

> 覆盖窗口：2026-11-13 至 2026-11-20（常规）

今日要闻：VS Code 1.147 于 11-18 发布，新增定时发送（Send Later）、草稿请求、Browser Use 预览与模型路由器，且默认启用 Skills over MCP。

## VS Code 更新

- VS Code 1.147 稳定版于 11-18 发布，新增实验性 Send Later（定时发送聊天请求）与 Draft requests（多份未发送草稿）、Browser Use 预览（Agent 经 Copilot 浏览器扩展操作 Chrome/Edge）、YAML 模型路由器（实验）、Dev Container 聊天跨重建持久化（实验）及 Agent 窗口内联 HTML/可视化响应（默认关闭）。来源：VS Code 官方更新页 https://code.visualstudio.com/updates/v1_147
- 1.147 企业与权限更新：管理员可通过 `vscode.allowedHarnesses` 放行 Claude 与 Codex harness，托管 shell 权限规则支持正则，Assisted permissions 支持自定义审查指令，Skills over MCP 默认启用。来源：VS Code 官方更新页 https://code.visualstudio.com/updates/v1_147
- 1.147 宣布弃用 macOS Ventura/Sonoma 与 32 位 ARM Linux 上的 VS Code 桌面版，并移除实验性状态栏 AI 用量统计（`editor.aiStats.enabled`）。来源：VS Code 官方更新页 https://code.visualstudio.com/updates/v1_147
- 【续报】1.146（11-11 发布）特性清单已核实：Inbox 模式（跨项目汇总待处理会话）、聊天独立窗口（预览）、Copilot CLI 用 `/code` 移交会话至 VS Code、Mermaid 12 渲染、沙箱环境变量掩码；Local harness 被弃用并将于 2027 年 2 月移除，Canvases 仍为预览。来源：VS Code 官方更新页 https://code.visualstudio.com/updates/v1_146

## Claude App 更新

- Claude Code v2.1.325 至 v2.1.329 于 11-13 至 11-19 连续发布：修复 zstd 响应解码安全问题并收紧 Bash 权限规则（2.1.325）、`claude mcp add-json <name> -` 支持从标准输入读取以避免令牌上命令行（2.1.327）、Opus 4.6/Sonnet 4.6 在 Bedrock、Google Cloud、Foundry 及 Claude 应用网关上支持 auto mode 与 MCP 工具 hook 的 `onFailure: "block"`（2.1.328）、`/tasks` 汇总定时任务/loop/目标/fork 并修复 macOS 钥匙串反复登出（2.1.329）。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases
- Claude Developer Platform 于 11-17 推出关联计费（Linked billing，Beta），第三方工具经客户授权并设每月额度后即可代付 API 用量，无需交出 API 密钥。来源：Releasebot 转录的 Anthropic 发布说明 https://releasebot.io/updates/anthropic/claude
- Claude Desktop 于 11-17 新增 Stable/Latest 更新通道，Stable 为默认，Latest 约每日更新。来源：Releasebot 转录的 Anthropic 发布说明 https://releasebot.io/updates/anthropic/claude
- 【续报】【单源】Claude Meetings（Beta）11-19 因需求高峰无法加入大量会议。来源：Releasebot 转录的 Anthropic 状态与发布说明 https://releasebot.io/updates/anthropic/claude
