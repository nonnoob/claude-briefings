# 🛠️ AI Agent 工程简报 · 2026-11-24

> 覆盖窗口：2026-11-23 10:07 UTC 至 2026-11-24 10:07 UTC（常规）

今日要闻：Anthropic 推出 Claude Ship 套件（Code Review 正式可用，PR Steward 与 Claude Approvals 公测），把“审查—修复—按仓库内自然语言策略放行”整条 PR 流水线交给 agent。

## 开发者工具与工作流

- Anthropic 推出 Claude Ship：Code Review（GA，可选 Quick/Standard/Deep 深度）、PR Steward（beta，自动处理 CI 失败、合并冲突与审查意见，每次推送后评论改动与回滚方式）、Claude Approvals（beta，按仓库内自然语言策略文件放行改动）；面向 Team/Enterprise，仅支持 GitHub。落地提示：官方建议先在单仓库以 Claude Approvals 的仅观察模式试跑并设月度支出上限，审批策略写成仓库文件也是可借鉴的“策略即代码”做法。来源：TechCrunch https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/
- Claude Code v2.1.331 发布：Code Mode 支持 Bedrock/Google Cloud/Foundry/AWS 上的终端会话，修复格式异常回复导致 MCP 工具调用最长挂起 30 分钟，新增 `claude doctor` API 连通性检查、trace span 的 `gen_ai.*` 字段与插件清单 `optionalDependencies`，并预告 11 月 30 日起托管 `extraKnownMarketplaces` 默认自动更新（可设 `"autoUpdate": false` 退出）。落地提示：用云厂商网关的团队可试 Code Mode，长期挂起的 MCP 调用可升级排除；Windows 注册表托管设置升级前先检查。来源：GitHub anthropics/claude-code https://github.com/anthropics/claude-code/releases/tag/v2.1.331
- Codex rust-v0.172.0 转稳定版：可选 stdio MCP 服务器按首次调用惰性启动，可为单个连接应用工具配置审批 reviewer，`codex exec resume` 恢复已存沙箱权限与工作目录，内置 openai-docs skill 加入 GPT-6.2 Astra/Sol 迁移指引。落地提示：MCP 惰性启动可缩短启动耗时，脚本化续跑不再丢沙箱设置。来源：GitHub openai/codex https://github.com/openai/codex/releases/tag/rust-v0.172.0
- Copilot CLI v1.0.115-8（预发布）：Assisted Permissions 首个审查模型卡住或失败时可换备用模型，并可复用同会话相同请求的一次性批准；`--usage-output-file` 按子 agent 名称汇总用量与启动次数。落地提示：便于按子 agent 核算成本、减少权限弹窗打断。来源：GitHub github/copilot-cli https://github.com/github/copilot-cli/releases
