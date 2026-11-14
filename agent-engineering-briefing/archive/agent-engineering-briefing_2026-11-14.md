# 🛠️ AI Agent 工程简报 · 2026-11-14

> 覆盖窗口：2026-11-13 10:10 UTC 至 2026-11-14 10:06 UTC（常规）

今日要闻：Claude Code v2.1.325 修复 zstd 响应解码安全问题，并修正子 Agent 在 opusplan/haiku 下被错误切换到计划模式模型的问题。

## 开发者工具与工作流

- Claude Code v2.1.325（11 月 13 日）修复 zstd 压缩响应解码的安全问题、带独立模型的子 Agent 在 `opusplan`/`haiku` 下被切到计划模式模型及按主会话模型估算文件读取大小的问题，并修复第三方网关/Foundry 每轮报上下文超长而不压缩的故障，另有多项 deny/ask 与 Bash 权限检查修复。若你用子 Agent 混搭模型或走第三方网关，建议升级并复测压缩与权限规则。来源：Claude Code Releases https://github.com/anthropics/claude-code/releases
- GitHub Copilot CLI v1.0.111 正式版（权限规则支持正则、`--host-allow-session-creation`、修复 MCP OAuth 重复重连）与 v1.0.112/-0：模型默认使用推荐上下文窗口，子 Agent 遵守 `--max-ai-credits` 会话额度，`/compact` 失败直接显示供应商报错。做多 Agent 成本管控时，可借此把额度上限下沉到子 Agent。来源：Copilot CLI Releases https://github.com/github/copilot-cli/releases
