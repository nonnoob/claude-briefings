# 🛠️ 开发工具更新周报 · 2026-09-10

> 覆盖窗口:2026-08-31 至 2026-09-10(补漏:距上次运行超20天,按10天封顶处理,封顶外内容仅收录至今仍重要的大事)

## VSCode 更新

- VS Code 1.136 正式版发布(2026-09-02),新增 Agent Merge(预览)可令 agent 自动处理 PR 的评审意见、失败检查与合并冲突直至可合并,并实验性支持多根工作区(multi-root workspace)下的 Copilot/Claude agent 会话协作。来源:VS Code 官方更新页 https://code.visualstudio.com/updates/v1_136
- 同一版本将 Agent Host 迁移到开放的 Agent Host Protocol(AHP,基于 JSON-RPC、厂商中立),Claude Agent SDK 通过适配器接入该协议,与 Copilot SDK 共享同一套会话/工具/权限基础设施。来源:InfoWorld https://www.infoworld.com/article/4218856/visual-studio-code-1-136-introduces-agent-merges-for-pull-requests.html

## Claude App 更新

- Claude Code v2.1.251 发布(2026-08-28),修复文件工具(Read/Write/Edit)在权限检查后遭符号链接置换从而读写工作目录外文件、插件市场声明路径越界执行、Bash 算术赋值绕过权限确认等多处安全问题。来源:Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.251
- Anthropic 宣布(2026-08-30)Claude Code 周额度自 9 月 14 日起对 Pro/Max/Team/企业席位版"永久上调 25%",但因 5 月以来的临时 50% 上浮同期到期,较当前实际水平是下降 17%,引发社区质疑后追加说明。来源:MindStudio https://www.mindstudio.ai/blog/claude-code-weekly-rate-limit-changes
- Claude Code v2.1.257 发布(2026-09-01),将 Claude Fable 5.1(100 万 token 上下文)设为默认 Fable 模型,定价调整为输入 $10/输出 $50 每百万 token、缓存读取 $0.25,并为 Auto Mode 新增"隔离逃逸"规则,阻止云元数据凭据窃取、出口规避类操作被自动批准。来源:Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.257
- Claude Code v2.1.258 发布(2026-09-01),修复 macOS 12(Monterey)启动失败回归问题,以及远程/计划会话在权限批准后消息为空导致失败的问题。来源:Claude Code Docs Changelog https://code.claude.com/docs/en/changelog
- Claude Code v2.1.259–v2.1.261 发布(2026-09-02至04),新增组织托管 MCP 服务器(managedMcpServers)、面向无人值守环境的 --permission-prompts none、GitLab 合并请求识别、未提交改动 diff 面板与 /skill-doctor 未用技能诊断等企业与效率功能。来源:Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.261
- Claude Code v2.1.265/v2.1.267 发布(2026-09-08/09),修复插件目录符号链接容器边界检查、插件市场路径穿越绕过两处安全问题,新增跨供应商效力上限 maxEffortLevel 设置。来源:Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.267
