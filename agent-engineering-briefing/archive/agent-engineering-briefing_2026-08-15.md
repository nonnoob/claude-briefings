# 🛠️ AI Agent 工程简报 · 2026-08-15

> 覆盖窗口：2026-08-14 至 2026-08-15（常规）

## Prompt 与 Context 工程

- Anthropic 官方发布《善用你的 Claude Code 会话》实践指南：任务间用 /clear 清空无关上下文、开局前锁定模型与 effort level（中途切换会打破 prompt cache、推高成本）、用 @ 提及文件而非让 Claude 自行搜索读取、给吵闹命令加静默参数或丢进 subagent 执行、新会话跑一次 /context 巡检已加载内容以便裁剪、离开键盘前先 /compact（prompt cache 一小时过期，趁未过期时压缩更省钱）。相当于把"减少无谓上下文"的工程直觉整理成一份可直接对照执行的清单，写 CLAUDE.md 或调 agent 工作流时能直接拿来用。来源：Anthropic Blog https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions

## 开发者工具与工作流

- Claude Code 2.1.233 发布：--worktree 与 agents 视图新增 GitLab MR 支持（显示为 !N）、新增 opt-in 的 forward_user_identity 网关设置（让代理网关按登录用户归因花费）、Linux 上 Bash 工具新增 opt-in memory cgroup（防止失控构建拖垮会话）、新增 CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS 环境变量可调 WebFetch 缓存时长，并修复云端会话在等待权限确认期间环境关闭、被误标记为"丢失"的问题。用 GitLab 协作或跑自托管 runner 的团队可以直接用上这批修复。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- 【续报】Claude Code auto mode 默认开启事件：Enterprise 与 API 渠道目前确认仍维持 opt-in，Anthropic 计划在未来一个月内跟进默认开启，届时同步取消该渠道下分类器额外消耗的计费，为企业管理员留出配置组织级默认值的窗口期。跑 Enterprise/API 的团队可提前评估权限策略，不必现在抢着切换。来源：Enterprise DNA https://enterprisedna.co/resources/news/anthropic-claude-code-auto-mode-default-enterprise-august-2026/
