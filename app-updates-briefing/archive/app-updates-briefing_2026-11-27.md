# 🛠️ 开发工具更新周报 · 2026-11-27

> 覆盖窗口：2026-11-20 至 2026-11-27（常规）

今日要闻：Anthropic 11-23 推出 Claude Ship（PR Steward 与 Claude Approvals 两个 Beta 智能体，面向 Team/Enterprise 的 GitHub 仓库），VS Code 1.148 稳定版同在本周发布。

## VS Code 更新

- VS Code 1.148 稳定版于 11-25 发布：聊天响应启动平均快约 30%，新增预览设置 `sessions.keepAwakeWhileWorking` 在 Agent 工作期间阻止主机休眠，远程 Agent 获得重设计的环境表、故障排查页与远程 worktree 清理。来源：VS Code 官方更新页 https://code.visualstudio.com/updates/v1_148
- 1.148 实验性特性：无需 devcontainer.json 即可创建隔离的 Ubuntu Dev Container 并移交任务，远程主机可各自配置沙箱 profile；另有 MCP Apps 全屏、集成浏览器支持 HTTP Basic 认证、Copilot harness 终端可在聊天中输入 sudo/ssh/git 密码（不发送给模型）、Rust WebAssembly diff 算法（中位数快逾 2 倍）、CLI 体积缩小约 40%、Agent Host Protocol 1.1.0。来源：VS Code 官方更新页 https://code.visualstudio.com/updates/v1_148
- 【续报】Local harness 仍确认将于 2027 年 2 月移除，1.148 未调整日期。来源：VS Code 官方更新页 https://code.visualstudio.com/updates/v1_148

## Claude App 更新

- Anthropic 于 11-23 推出 Claude Ship：含已 GA 的 Code Review，以及两个 Beta 智能体 PR Steward 与 Claude Approvals，用于审查、修复并批准代码变更，面向 Team/Enterprise 方案的 GitHub 仓库。来源：TechCrunch https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/
- Claude 与 Claude Code 于 11-24 公测 Skills over MCP，MCP 服务器可随工具一并下发标准化工作流指令，Claude Code 需 v2.1.331 及以上。来源：Crypto Briefing https://cryptobriefing.com/anthropic-skills-over-mcp-claude-beta
- Claude Desktop 于 11-24 至 11-25 在 Beta 中支持将 Artifacts 经 Share 菜单「Install as app」安装为 Mac/Windows 独立应用，全部方案可用，Enterprise 需先手动开启。来源：MacRumors https://www.macrumors.com/2026/11/25/claude-install-artifacts-desktop-apps/
- Claude Code v2.1.330 至 v2.1.332（11-20 至 11-25）：`claude auth login` 支持登录 Enterprise Admin Console 托管组织与内置 easel 图表 mod（2.1.330）；Code Mode 扩展到 Bedrock/Google Cloud/Foundry 终端会话、`claude doctor` 新增 API 连通性检测、VS Code 新增「Fix with Claude Code」与「Resolve Merge Conflicts」（2.1.331）；MCP 技能进入 `/` 菜单并新增 `PreSkillShellCommand` hook，另修复多项卡死问题（2.1.332）。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases
- 【续报】Claude Code v2.1.331 公告：自 11-30 起，托管 `extraKnownMarketplaces` 中的插件市场默认自动更新（可设 `"autoUpdate": false` 退出）；Windows 上 HKLM 注册表托管策略将优先于 managed-settings.json；Opus 4.8 fast mode 仍定于 11-30 移除。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases
- 【单源】Claude Desktop 月度回顾（monthly recaps）结束 Beta，/ship 于 11-24 起在 Claude Code 与桌面端逐步上线；11-20 起新版 Claude Desktop 提供 computer use。来源：Releasebot 转录的 Anthropic 发布说明 https://releasebot.io/updates/anthropic/claude
