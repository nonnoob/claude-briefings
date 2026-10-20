# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻：2026-10-20 02:05 UTC（归档日期 2026-10-19，America/Los_Angeles）
- 上次运行时刻：2026-10-09 10:36 UTC
- 实际覆盖窗口：2026-10-10 02:05 UTC 至 2026-10-20 02:05 UTC（补漏：距上次运行约 10 天 15.5 小时，超过 10 天封顶，窗口外的约 15.5 小时缺口仅收仍重要的大事）。
- 本期 VSCode、Claude App、生态与社区动向三方向检索均正常。封顶窗口外 10-09 的 Claude Docs/Slides/Design 转正暨 Dashboards/Motion Beta 发布（亦属进行中事件续报）及 Claude Code v2.1.296 纳入本期收录；Claude Code v2.1.297/v2.1.298 未发布 npm，v2.1.301/v2.1.303 常规修复已合并简述或从略。
- 进行中事件表变更：
  1. 「Claude Cowork 并入聊天界面，Claude Docs/Slides/Design Beta」迎实质进展——Docs/Slides/Design 已结束 Beta 全量开放至含 Free 在内的所有计划，同时新增 Dashboards（付费计划 Beta）与 Motion（Team/Enterprise Beta），独立站 `claude.ai/design` 定于 2026-12-14 下线；更新该追踪项为追踪 Dashboards/Motion 转正与 `claude.ai/design` 停服迁移。
  2. 「Claude Code 周额度新政争议」（最后进展 2026-09-17）与「Windows 09 月累积更新致 Cowork Plan9 挂载故障」（最后进展 2026-09-19）均已连续超过 21 天无新进展，按规则移出进行中事件表。
  3. 新增追踪「VS Code 1.142 Agent Canvases（预览）」。

## 2. 已报条目清单（最近 21 天）

- 2026-09-28 | Anthropic 发布 Claude Sonnet 5.5，维持原定价，输出速度提升超30%、单任务成本降约30%，支持100万token上下文，Claude Code v2.1.284 设为默认 Sonnet 模型 | https://www.anthropic.com/claude-sonnet-5-5
- 2026-09-29 | Claude Code v2.1.285 发布，新增 claude --desktop 与 claude plugin configure 命令，新增 allowedProviders 托管设置 | https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- 2026-09-30 | Claude Code v2.1.286 发布，堆叠权限请求新增排队计数提示，VS Code 插件新增书签面板 | https://github.com/anthropics/claude-code/releases/tag/v2.1.286
- 2026-09-30 | VS Code 1.140 正式版发布，新增跨文件夹 Agent 会话、远程任务委托、HydraFusion 多模型协同研究预览等 | https://code.visualstudio.com/updates/v1_140
- 2026-10-01 | Claude Code v2.1.287 发布，新增 Mods 插件深层行为改写机制与内置风险提醒 agent | https://github.com/anthropics/claude-code/releases/tag/v2.1.287
- 2026-10-03 | Claude Code v2.1.289 修复 deny/ask 规则漏判嵌套复合命令与 Read deny 经符号链接绕过，新增 agent.spawn | https://github.com/anthropics/claude-code/releases
- 2026-10-05 | Claude Code v2.1.290 新增 claude attach/logs 命令，WebFetch 支持 offset | https://github.com/anthropics/claude-code/releases
- 2026-10-06 | Claude Code v2.1.292 修复 UNC 路径与 rm -rf 短名等权限绕过安全问题，新增 Agent effort 参数 | https://github.com/anthropics/claude-code/releases
- 2026-10-07 | VS Code 1.141 正式版发布，新增 Copilot agent 跨平台沙箱、多会话分屏网格、Agent worktree 清理、外部会话续接 | https://code.visualstudio.com/updates/v1_141
- 2026-10-07 | Anthropic 发布 Claude Haiku 5.5，$0.10/$0.50 每百万 token、较 Haiku 4.5 平均便宜约75%，首个带 effort 档位的 Haiku，Claude Code v2.1.293 设为默认 Haiku | https://aiweekly.co/alerts/introducing-claude-haiku-55
- 2026-10-07 | Sonnet 5.5 缓存读取价格减半，Max/Team 订阅新增每月 API 额度 | https://aiweekly.co/alerts/introducing-claude-haiku-55
- 2026-10-08 | Claude Code v2.1.295 为 hook 新增 onFailure: "block"，修复网关拒绝 context-1m beta 时 [1m] 模型请求全失败 | https://github.com/anthropics/claude-code/releases
- 2026-10-09 | Anthropic 将 Claude Docs、Slides、Design 转正并开放至含 Free 在内的所有计划，同时上线 Claude Dashboards（付费计划 Beta）与 Claude Motion（Team/Enterprise Beta），独立站 claude.ai/design 定于 2026-12-14 下线 | https://claude.com/blog/build-live-dashboards-and-animate-explainers
- 2026-10-09 | Claude Code v2.1.296 发布，Read 工具新增 allow_large 参数，子 Agent 新增 autoCompactWindow 配置 | https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- 2026-10-13 | Microsoft 发布 VS Code 1.141.1 修复 CVE-2026-102238 与 CVE-2026-70098 等安全漏洞，次日发布 1.141.2 修复其引发的 WSL 下 Claude Code/Codex/Markdown 预览回归故障 | https://github.com/microsoft/vscode/releases/tag/1.141.2
- 2026-10-13 | Workday 与 Anthropic 宣布基于 MCP 协议打通 Claude 与 Workday Sana AI Agent 的企业级集成合作 | https://www.prnewswire.com/news-releases/workday-and-anthropic-announce-new-partnership-to-connect-reasoning-to-the-rules-that-run-the-business-wherever-people-choose-to-work-302274488.html
- 2026-10-13 | Notion 发布 3.8 更新，深化 MCP 协议集成以支持 Claude 及第三方 Agent 读写工作区与同步逾 150 款工具技能 | https://www.notion.com/releases/
- 2026-10-14 | VS Code 1.142 正式版发布，推出 Agent Canvases（预览）、跨目录/worktree 迁移会话、Markdown 粘贴图片与大纲增强、重设计模型选择器及企业级 Agent 沙箱策略控制 | https://code.visualstudio.com/updates/v1_142
- 2026-10-14 | Claude Code v2.1.299 与 v2.1.300 发布，新增超 20 万 token 会话空闲自动压缩（Idle Compaction）、提示词缓存 TTL 控制与 PDF 分页限制 | https://github.com/anthropics/claude-code/releases/tag/v2.1.299
- 2026-10-15 | Anthropic 宣布 Claude Code Review 面向 Team 与 Enterprise 正式转正（GA），支持三档审查深度且提速约 3 倍，并公开内部替代 Git 的自研版本控制系统 Scion | https://www.anthropic.com/news/redesigning-source-control-at-anthropic
- 2026-10-16 | Claude Code v2.1.302 发布，在 claude -p、Agent SDK、VS Code 插件与桌面端默认启用 fork 子 Agent，新增 CLAUDE_CODE_AUTO_MODE_MODEL，并修复额度计费下自动提示词建议误扣额度问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.302
- 2026-10-18 | Claude Code v2.1.304 发布，支持 Code Review 审查级别配置与组织级批量仓库策略、mod tool.check 新增 decider: "person"，修复 claude --worktree 退出时未经确认误删分支问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.304
- 2026-10-19 | VS Code 1.143 Insiders 新增新建聊天菜单 Canvas 子菜单、.mcp.json 环境变量展开，并修复便携模式 CLI 状态路径问题 | https://code.visualstudio.com/updates

## 3. 进行中事件表

- 事件：Anthropic 上线 Claude Dashboards（付费计划 Beta）与 Claude Motion（Team/Enterprise Beta），同时宣布独立站点 `claude.ai/design` 将于 2026-12-14 停服下线；最后进展日期：2026-10-16；下一步关注点：核实 Claude Dashboards 与 Claude Motion 何时扩展覆盖范围或由 Beta 转 GA，以及 `claude.ai/design` 下线前是否推出自动迁移工具。
- 事件：VS Code 1.142 推出交互式可视化协作工作区 Agent Canvases（预览，需开启 `chat.canvases.enabled`）并逐步将 Copilot harness 设为默认会话后端；最后进展日期：2026-10-14；下一步关注点：关注 VS Code 1.143 正式版中 Agent Canvases 是否默认开启或开放第三方 Agent（如 Claude Code）接入 Canvas API。
