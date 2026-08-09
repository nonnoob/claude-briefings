# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻：2026-08-09 12:14 UTC
- 上次运行时刻：2026-08-08 12:17 UTC
- 实际覆盖窗口：2026-08-08 12:17 UTC 至 2026-08-09 12:14 UTC（正常窗口，非补漏）
- 本期 VSCode / Claude App / 生态与社区动向三个方向检索均正常完成，无方向检索失败；VSCode（当前最新为 1.132 稳定版，1.133 仍在 Insiders 且仅有零散小改动）与生态/社区两个板块在窗口内未发现落在覆盖期内的实质新内容，故当期简报省略。

## 2. 已报条目清单（最近 14 天）

- 2026-07-28 | MCP 2026-07-28 版本规范正式发布，协议核心改为无状态，弃用 Roots/Sampling/Logging（保留 12 个月兼容），Anthropic 确认 Claude Code/Desktop 将跟进适配 | https://blog.modelcontextprotocol.io/posts/2026-07-28/
- 2026-07-29 | VS Code 1.131 正式版发布，新增子代理状态可视化、实验性内置听写与实验性混合 Markdown 编辑器 | https://code.visualstudio.com/updates/v1_131
- 2026-08-03 | Claude Code v2.1.221 发布，新增 VSCode 插件 Focus 视图与 Linux/WSL 沙箱凭据掩码，修复 Bash 权限绕过等安全问题 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-04 | Claude Code v2.1.222 发布，修复 worktree 隔离会话可对主检出执行破坏性 git 命令的安全漏洞 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-05 | VS Code 1.132 正式版发布，新增集成浏览器元素级评论、Agent Host 架构稳定推广（Claude 为受支持 agent host 之一）、混合 Markdown 编辑器 diff 查看、听写多语言支持 | https://code.visualstudio.com/updates/v1_132
- 2026-08-05 | Claude Code v2.1.223 发布，市场管理支持组织级通配符，修复权限提示 Unicode 隐藏命令等安全问题 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-05 | Claude Enterprise 推出 Inference Hooks 公测，企业可接入自有安全服务器对每次推理请求实时裁决 | https://platform.claude.com/docs/en/release-notes/overview
- 2026-08-05 | Claude Opus 4.1 模型正式退役，建议迁移至 Claude Opus 5 | https://platform.claude.com/docs/en/release-notes/overview
- 2026-08-06 | OpenAI/AWS/Cursor/GitHub/VS Code/Vercel 联合发布 Agent Plugins 跨客户端插件标准，Anthropic/Claude Code 未列入首发名单且格式不兼容 | https://explainx.ai/blog/agent-plugins-openai-standard-aws-cursor-github-vscode-2026
- 2026-08-07 | Claude Code v2.1.224 发布，新增自托管环境公测、archive 插件源、跨会话消息能力 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-08 | Claude Code v2.1.225 发布，新增网关支出上限用量预警与 claude agents 工作区信任提示，修复长期 OAuth token 被覆盖、macOS MCP OAuth keychain 超时批量 401 等问题 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-08 | Claude Code v2.1.226 发布，仅含稳定性与可靠性修复 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-08 | Anthropic 宣布 Claude Code Auto Mode 将于 8 月 14 日起成为 Pro/Max/Team 计划新会话默认权限模式，测试中拦截 89% 危险命令 | https://claude.com/blog/auto-mode-default-in-claude-code

## 3. 进行中事件表

- 事件：MCP 2026-07-28 版本规范在 Claude 产品线的具体适配进展（协议核心转为无状态，弃用 Roots/Sampling/Logging）；最后进展日期：2026-07-28（Anthropic 官方博客确认将跟进但未给版本号/时间表；2026-08-09 窗口内再次定向检索 Claude Code 最新 CHANGELOG（仍为 v2.1.226）及 Anthropic 官方博客/API release notes，仍未发现具体版本号或时间表）；下一步关注点：等 Anthropic 公布 Claude Code/Desktop 具体适配版本号或时间表。
- 事件：Agent Plugins 跨客户端插件标准与 Claude Code 现有插件格式不兼容，Anthropic 未列入首发维护方名单；最后进展日期：2026-08-06；下一步关注点：等 Anthropic 是否跟进采用该标准、或对不兼容问题公开回应；2026-08-09 窗口内定向检索仍未发现 Anthropic 官方回应。
