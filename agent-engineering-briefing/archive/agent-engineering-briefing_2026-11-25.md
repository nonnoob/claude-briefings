# 🛠️ AI Agent 工程简报 · 2026-11-25

> 覆盖窗口：2026-11-24 10:07 UTC 至 2026-11-25 10:07 UTC（常规）

今日要闻：Claude Code v2.1.332 让 MCP 服务器可以直接分发 skill（beta），skill 与 MCP 两条路线开始合流。

## 开发者工具与工作流

- Claude Code 发布 v2.1.332：MCP 服务器可提供 skill（beta）、新增 PreSkillShellCommand hook 事件，Foundry 默认 Sonnet/opus 别名升至 Sonnet 5.5/Opus 5.5，桌面 Code 标签页 OTel 服务名改为 claude-code-desktop。想把 skill 随 MCP 服务统一下发的团队可以试用；依赖旧 OTel 服务名做过滤的看板需同步修改。来源：Claude Code CHANGELOG https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 【单源】GitHub Copilot CLI 发布 v1.0.116-0 至 -5 预发布版：插件与独立 MCP 连同一端点时给出告警、修复长会话流式回复缓存致内存无限增长、ACP 客户端可按会话选上下文大小、ACP 的 shell 授权提示显示真实命令。长会话内存泄漏与授权提示展示真实命令都是做 agent 宿主时值得参照的细节。来源：Copilot CLI Releases https://github.com/github/copilot-cli/releases/tag/v1.0.116-5

## 案例与最佳实践复盘

- Simon Willison 发文《Three LLM inflection points in twelve months》，据其 AI Engineer Code Summit 主题演讲整理：去年 11 月 Opus 4.5 与 GPT-5.1-Codex 让编码 agent 默认可靠，随后"Fable 级"模型在给定目标与工具后可暴力解题；结论是目标定义清晰加合适工具是解锁模型的关键，描述需求的能力比手写代码更重要。设计 agent 任务时值得把精力放在目标与验收标准的表述上。来源：Simon Willison's Weblog https://simonwillison.net/2026/Nov/24/llm-inflection-points/
