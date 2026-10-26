# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻：2026-10-26 08:25 UTC（归档日期 2026-10-26，America/Los_Angeles）
- 上次运行时刻：2026-10-20 02:05 UTC
- 实际覆盖窗口：2026-10-20 02:05 UTC 至 2026-10-26 08:25 UTC（常规）。
- 本期 VSCode、Claude App、生态与社区动向三方向检索均正常。收录 VS Code 1.143/1.143.1 正式版（Copilot harness 默认化、Compare Models 预览、本地模型与沙箱 CA 管理）、Claude Duet 研究预览、Claude Code v2.1.305 至 v2.1.310 系列更新（v2.1.308 为常规修复已合并从略）、Agent Skills 捐赠 Linux 基金会 AAIF、MCP Tasks/Elicitations 落地及 Microsoft MCP C# SDK 2.0。

## 2. 已报条目清单（最近 21 天）

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
- 2026-10-22 | VS Code 1.143 及 1.143.1 正式版发布，将 Copilot harness 设为新会话默认后端，新增 Compare Models 多模型对比（预览）、本地运行 MAI Code 1.1 Flash、worktree 空间回收及沙箱 CA 证书管理 | https://code.visualstudio.com/updates/v1_143
- 2026-10-21 | Anthropic 面向美国 Pro 与 Max 用户开放主动式智能体应用 Claude Duet 研究预览（候补名单制） | https://claude.com/blog/claude-duet
- 2026-10-21 | Claude Code v2.1.305 与 v2.1.306 发布，新增 Linux 沙箱嵌套用户命名空间支持、修复 Vertex/Bedrock 网关拒绝 ToolSearch 请求失败，并新增 @claude review stop 指令 | https://github.com/anthropics/claude-code/releases/tag/v2.1.305
- 2026-10-21 | Claude Code v2.1.307 发布，新增 /claude-api api-version（迁移至 2026-10-21）与 claude_code.safety_event OpenTelemetry 安全审计事件 | https://github.com/anthropics/claude-code/releases/tag/v2.1.307
- 2026-10-22 | Claude Code v2.1.309 发布，修复多项沙箱与符号链接权限绕过漏洞，claude ultrareview 强制要求工作区信任，VS Code 编辑诊断等待缩至 0.75 秒 | https://github.com/anthropics/claude-code/releases/tag/v2.1.309
- 2026-10-23 | Claude Code v2.1.310 发布，在 Bedrock/Vertex/Foundry 开放 Monitor 工具，并为 Enterprise 自定义角色新增云会话与远程控制权限管控 | https://github.com/anthropics/claude-code/releases/tag/v2.1.310
- 2026-10-23 | Anthropic 将 Agent Skills 开放标准捐赠给 Linux 基金会 AAIF；Claude Code 原生支持 MCP Tasks 与 Elicitations；微软发布默认无状态的 MCP C# SDK 2.0 | https://www.linuxfoundation.org

## 3. 进行中事件表

- 事件：Anthropic 上线 Claude Dashboards（付费计划 Beta）与 Claude Motion（Team/Enterprise Beta），同时宣布独立站点 `claude.ai/design` 将于 2026-12-14 停服下线；最后进展日期：2026-10-16；下一步关注点：核实 Claude Dashboards 与 Claude Motion 何时扩展覆盖范围或由 Beta 转 GA，以及 `claude.ai/design` 下线前是否推出自动迁移工具。
- 事件：VS Code 推出 Agent Canvases（预览）与 Compare Models 多模型并行对比（预览），并在 1.143 正式版将 Copilot harness 设为默认后端；最后进展日期：2026-10-22；下一步关注点：关注 VS Code 1.144 Insiders/正式版中 Agent Canvases 与 Compare Models 是否转正默认开启，以及 Keep/Undo 文件级与行级回滚恢复进展。
- 事件：Anthropic 开放主动式自主智能体应用 Claude Duet 研究预览（美国 Pro/Max 候补名单）；最后进展日期：2026-10-21；下一步关注点：关注 Claude Duet 何时结束候补名单全量开放或扩展至 Team/Enterprise 与非美地区。
