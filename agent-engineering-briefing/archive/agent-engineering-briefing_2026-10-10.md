# 🛠️ AI Agent 工程简报 · 2026-10-10

> 覆盖窗口：2026-10-09 10:01 UTC 至 2026-10-10 10:01 UTC（常规）

今日要闻：Anthropic 在 Claude Managed Agents 上线 Dynamic Workflows beta，让 agent 自己编写并在服务端后台运行多 agent 分阶段工作流。

## 开发者工具与工作流

- Claude Code 发布 v2.1.296：subagent 新增 `autoCompactWindow` 可比主会话更早自动压缩，新增 `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` 让所有 workflow agent 统一用一个模型，Read 工具加 `allow_large` 选项，529 过载重试上限可通过环境变量拉长。长跑 subagent 可以给更小的压缩窗口防上下文膨胀，workflow 成本可靠统一模型来控。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- OpenAI Codex CLI 发布 rust-v0.162.1 稳定版：修复多行异步提问导致的 TUI 崩溃，以及后台 server 与 CLI 默认特性设置不一致引起的启动失败；0.163.0 alpha 持续滚动但无发布说明。属于稳定性补丁，用 0.162.0 遇到启动失败的应升级。来源：OpenAI Codex Releases https://github.com/openai/codex/releases
- GitHub Copilot CLI 发布 v1.0.95 正式版及 v1.0.96-0 至 -2 预发布：v1.0.96 起权限时间线显示每次权限决定由谁做出，`/add-dir` 可为当前会话授予沙箱访问，沙箱设置会提示可能的环境密钥并支持添加掩码主机。权限决策可追溯、密钥掩码的思路值得自建 agent 沙箱时参考。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases

## 模型能力与 API 更新

- Anthropic 为 Claude Managed Agents 上线 Dynamic Workflows（beta）：agent 可自行编写分阶段运行多 agent 的 workflow 程序，由服务端后台执行，通过 `workflow_run.*` 事件流跟踪，需 `managed-agents-2026-04-01` beta 头并设置 `multiagent` 字段为 `multiagent_20261001`。适合数百文档审阅这类大批量任务，编排逻辑从人写代码转为 agent 生成，需在 system prompt 里写清何时启动 run。来源：Claude API Release Notes https://platform.claude.com/docs/en/release-notes/api

## 社区热议与争议

- 【续报】【矛盾】GitSpawn：Grok Build 修复状态仍无官方公告，现有可检索资料仍显示 0.2.93/1.0.13 待修，与此前 Grith 称 1.0.13 已修复的说法并存。使用该类 agent 打开来源不明、带 `.git` 目录的压缩包或 U 盘仓库时仍需谨慎。来源：Cloud Security Alliance https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-coding-agent-git-config-rce-20260904-cs/
