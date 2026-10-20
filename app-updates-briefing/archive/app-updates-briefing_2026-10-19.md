# 🛠️ 开发工具更新周报 · 2026-10-19

> 覆盖窗口：2026-10-10 02:05 UTC 至 2026-10-20 02:05 UTC（补漏：距上次运行超过 10 天封顶，窗口外的约 15.5 小时缺口仅收仍重要的大事）

今日要闻：VS Code 1.142 正式版于 10-14 发布，推出可视化协作工作区 Agent Canvases（预览）、跨目录/Git worktree 无损迁移会话及企业级 Agent 沙箱策略管控；Anthropic 同周宣布 Claude Code Review 正式转正（GA），并将 Claude Docs、Slides、Design 全量开放至含免费版在内的所有计划。

## VSCode 更新

- VS Code 1.142 正式版于 10-14 发布，新增 Agent Canvases（预览，通过 `chat.canvases.enabled` 开启）提供看板等交互式可视化 Agent 协作区，支持将活跃聊天无损迁移至其他文件夹或新 Git worktree，并将基于 Copilot SDK 的 Copilot harness 逐步设为新会话默认后端。来源：VS Code 官方发布说明 https://code.visualstudio.com/updates/v1_142
- VS Code 1.142 升级 Markdown 编辑器（支持剪贴板图片直接粘贴落盘、大纲与面包屑标题导航、重命名文件自动更新链接）、重设计模型选择器（简化 Copilot 与 BYOK 模型切换及上下文/effort 调节）、支持安装扩展免重载，并为企业管理员新增强制沙箱与权限模式策略控制。来源：VS Code 官方发布说明 https://code.visualstudio.com/updates/v1_142
- Microsoft 于 10-13 紧急发布 VS Code 1.141.1 修复 CVE-2026-102238、CVE-2026-70098 等远程代码执行与路径穿越高危漏洞，但因跳过常规预览验证导致 WSL 下 Claude Code、Codex 及 Markdown 预览中断；官方于 10-14 推出 1.141.2 补丁修复该回归问题。来源：VS Code GitHub Releases https://github.com/microsoft/vscode/releases/tag/1.141.2
- VS Code 1.143 Insiders 预览分支在编辑器新建聊天菜单中集成 Canvas 子菜单、支持工作区根目录 `.mcp.json` 使用 `${VAR}` 与 `${VAR:-default}` 环境变量展开，并修复便携模式（Portable Mode）下 CLI 状态与缓存写入家目录的问题。来源：VS Code Updates https://code.visualstudio.com/updates

## Claude App 更新

- 【续报】Anthropic 宣布 Claude Docs、Slides、Design 正式结束 Beta 并向含 Free 免费版在内的所有计划全面开放，同时上线两项新 Beta：连接 Redshift/BigQuery/Snowflake/Salesforce 等数据源生成实时可核验图表的 Claude Dashboards（付费计划），以及用可编辑代码生成 MP4 动画解说的 `/motion` Claude Motion（Team 与 Enterprise）；独立站点 `claude.ai/design` 定于 2026-12-14 下线。来源：Claude 官方博客 https://claude.com/blog/build-live-dashboards-and-animate-explainers
- Anthropic 于 10-15 宣布多 Agent PR 审查工具 Claude Code Review 面向 Team 与 Enterprise 正式转正（GA），平均审查耗时由约 20 分钟降至 6–10 分钟，支持按仓库配置 Quick、Standard、Deep 三档深度，并同步公开内部为应对日均超 3 万次 AI 代码合并而替代 Git 的自研版本控制系统 Scion。来源：Anthropic 官方新闻 https://www.anthropic.com/news/redesigning-source-control-at-anthropic
- Claude Code v2.1.296（10-09）为 `Read` 工具新增 `allow_large` 参数以在需要完整文件上下文时绕过体积限制，并引入子 Agent `autoCompactWindow` 自动压缩窗口配置项。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- Claude Code v2.1.299 与 v2.1.300（10-14）新增空闲自动压缩（Idle Compaction，超 20 万 token 的长会话在约 54 分钟无操作、1 小时提示词缓存过期前自动压缩）、`CLAUDE_CODE_DISABLE_FILE_MENTIONS` 环境变量、提示词缓存 TTL 控制与 PDF 分页读取限制，并将 `UserPromptSubmit` hook 调整至技能展开前执行。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.299
- Claude Code v2.1.302（10-16）在 `claude -p`、Agent SDK、VS Code 插件及桌面端默认启用 fork 子 Agent（可通过 `CLAUDE_CODE_FORK_SUBAGENT=0` 关闭），新增 `/config` 空闲压缩开关与指定客户端分类器模型的 `CLAUDE_CODE_AUTO_MODE_MODEL`，限制单事件并发 hook 上限为 12，并修复按额度计费计划下自动后续提示词建议误扣用户额度的问题。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.302
- Claude Code v2.1.304（10-18）支持配置 Code Review 审查级别与组织级批量仓库策略、扩展 `/auto-mode-setup` 引导配置、为 mod `tool.check` 新增 `decider: "person"` 强制人工确认选项，并修复 `claude --worktree` 在游离 HEAD 或切换分支退出时未经确认误删 worktree 及分支导致提交丢失的缺陷（注：此前追踪的周额度新政争议与 Windows Cowork Plan9 挂载故障均已逾 21 天无新进展，本期起移出追踪表）。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.304

## 生态与社区动向

- Workday 与 Anthropic 于 10-13 在 Workday Rising 2026 大会上宣布达成合作伙伴关系，基于开放标准 MCP 打通 Claude 与 Workday Sana AI Agent，支持在不迁出企业数据的前提下跨平台流转 HR 与财务上下文及任务。来源：PR Newswire https://www.prnewswire.com/news-releases/workday-and-anthropic-announce-new-partnership-to-connect-reasoning-to-the-rules-that-run-the-business-wherever-people-choose-to-work-302274488.html
- Notion 于 10-13 发布 Notion 3.8 更新，深化 MCP 协议集成，支持 Claude 及第三方自定义 Agent 通过 MCP 直接读取工作区上下文、更新任务追踪器并与逾 150 款工具同步技能。来源：Notion Releases https://www.notion.com/releases/
