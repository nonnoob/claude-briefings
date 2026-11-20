# 🛠️ AI Agent 工程简报 · 2026-11-20

> 覆盖窗口：2026-11-19 10:20 UTC 至 2026-11-20 10:07 UTC（常规）

今日要闻：Claude Code v2.1.329 发布，新增 hooks 来源信任提示，并明确 Code Mode 下报错的 PreToolUse hook 不再拦截工具调用，必须拦截需显式设 `"onFailure": "block"`。

## 开发者工具与工作流

- Claude Code 发布 v2.1.329（11 月 19 日）：新增文件夹 hooks 声明位置的信任对话框警告；Code Mode 下报错的 PreToolUse hook 不再拒绝脚本的工具调用，须在 hook 上设 `"onFailure": "block"`；`/code-review <pr>` 改用 `gh pr diff`；`/tasks` 汇总定时任务、`/loop` 唤醒与 fork，旧版已保存的定时任务通常需重新调度。值得关注：依赖 hook 做安全拦截的团队要给关键 hook 显式加 onFailure 并复查 Code Mode 下的行为；本版仍未见 settings.local.json 密钥擦除。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.329
- OpenAI Codex CLI 发布 rust-v0.171.0：模型目录加入 GPT-6.2 Sol 与 Astra 且 Sol 成默认，TUI workspace 默认开启（含子 Agent 转录），新增 `codex exec --remote <ADDR>` 在已有 app server 上跑非交互会话，修复企业 MCP 登录对不返回 refresh token 的 IdP 的兼容。值得关注：`--remote` 便于把 CI/脚本里的 agent 任务挂到常驻服务端；本版未见 Pierre/Code Storage 集成。来源：OpenAI Codex GitHub Releases https://github.com/openai/codex/releases/tag/rust-v0.171.0
- GitHub Copilot CLI 发布 v1.0.115-0/-1：MCP 登录在服务端授予所需 scope 但不返回自动请求的 refresh-token scope 时可继续，直接执行工作流会等待项目扩展工作流注册完成。值得关注：自建 MCP 服务的 OAuth 实现若省略 refresh scope，现在客户端侧可容忍。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases/tag/v1.0.115-1

## Prompt 与 Context 工程

- 【单源】有二手文章转述一项覆盖 138 个仓库的研究：由 LLM 生成的 AGENTS.md 会降低任务成功率，并使推理成本上升逾 20%（发布时间未确认）。值得关注：给仓库写 agent 指令宜手写精简、避免让模型批量生成；原研究未核对，建议先查原文再据此改流程。来源：tutorials.technology 转述 https://tutorials.technology/tutorials/context-engineering-ai-agents-2026.html

## 案例与最佳实践复盘

- Simon Willison 转载 Claire Vo 的视频复盘：ChatPRD 免费试用遭滥用，攻击者转卖 token，她因此正在取消免费试用。值得关注：对外暴露 agent/LLM 功能的产品需在设计阶段加入额度、账号与滥用检测，而不是事后补。来源：Simon Willison's Weblog https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/

## 社区热议与争议

- 【单源】Hacker News 上一帖讨论“哈佛研究者发现 AI 编码 agent 把瓶颈转移到代码审查”，评论认为审查能力远落后于生成，且“人+agent”审查优于单独 agent（帖子约两日前，研究原文未核对）。值得关注：团队引入编码 agent 时需同步规划审查流程与容量，如分层审查和 PR 折叠摘要。来源：Hacker News https://news.ycombinator.com/item?id=50538303
