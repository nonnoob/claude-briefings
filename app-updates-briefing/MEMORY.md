# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻：2026-10-09 10:36 UTC
- 上次运行时刻：2026-10-02 10:36 UTC
- 实际覆盖窗口：2026-10-02 10:36 UTC 至 2026-10-09 10:36 UTC（常规，7天）。
- 本期 VSCode / Claude App 两方向检索正常；无独立生态/社区事件，省略该板块。code.visualstudio.com 与 havoptic 直连失败（DNS），改用 GitHub Releases 页与 WebSearch 摘要（含官方页摘要）。Claude Code v2.1.288~v2.1.295 逐一核对，选取信号最强的 5 个版本收录；v2.1.288/291/293/294 细节未单列。进行中事件表定向检索：周额度回应——未见新正式回应（搜索结果均为 5–6 月旧闻）；Windows KB Cowork 故障——未见窗口内新进展（仅有 09-14 已报的 KB5129195 相关旧文）；Cowork/Docs/Slides Beta——官方支持页称 Docs Beta 已覆盖 Pro/Max/Team/Enterprise（Team 默认开启），但页面无日期、无法确认发生在本窗口，未作续报，下次定向核实 Slides/Design 的 Team 状态与日期。
- 进行中事件表变更：无。

## 2. 已报条目清单（最近 21 天）

- 2026-09-16 | VS Code 1.138 正式版发布，新增 Dev Container 内运行 Agent 会话、扩展 Codex 跨应用/跨订阅支持 | https://code.visualstudio.com/updates/v1_138
- 2026-09-16 | Anthropic 宣布将 Claude Cowork 并入 Claude 聊天界面，并以 Beta 上线 Claude Docs、Claude Slides、Claude Design | https://www.technology.org/2026/09/17/anthropic-claude-chat-cowork-merge-docs-slides/
- 2026-09-17 | Claude Code v2.1.274 新增内存临界告警，修复会话记录损坏导致的 unexpected tool_use_id 报错(自愈) | https://github.com/anthropics/claude-code/releases/tag/v2.1.274
- 2026-09-17 | Claude Code v2.1.275 新增发送并打断快捷键与 claude.ai 账号技能/插件同步终端功能 | https://github.com/anthropics/claude-code/releases/tag/v2.1.275
- 2026-09-18 | Claude Code v2.1.276 修复 v2.1.275 引入的第三方网关/代理下全部请求 400 错误回归 | https://github.com/anthropics/claude-code/releases/tag/v2.1.276
- 2026-09-18 | Claude Code v2.1.277 发布，新增 AGENTS.md 支持与 /plugin install --marketplace | https://github.com/anthropics/claude-code/releases/tag/v2.1.277
- 2026-09-19 | Claude Code v2.1.278 发布，Auto Mode 默认改用服务端分类器 | https://github.com/anthropics/claude-code/releases/tag/v2.1.278
- 2026-09-19(报道日期) | Windows KB5129195 带外紧急补丁未完全修复 Cowork Plan9 挂载故障，用户报告新会话首次挂载仍失败 | https://github.com/anthropics/claude-code/issues/95557
- 2026-09-22 | Anthropic 发布 Claude Opus 5.5，成本降约40%、定价下调至 $4/$20 每百万 token，Claude Code v2.1.280 设为默认 Opus 模型 | https://www.anthropic.com/claude-opus-5-5
- 2026-09-23 | VS Code 1.139 正式版发布，新增 Agent 会话进度可视化保留、Copilot sandbox-policy 报告、MCP 远程 URL 变量等 | https://code.visualstudio.com/updates/v1_139
- 2026-09-24 | Claude Code v2.1.282 发布，修复含网页搜索结果会话全部请求 400 错误等问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.282
- 2026-09-25 | Claude Code v2.1.283 发布，新增 /doctor prompt-audit 与 availableModelsMatch/deniedModels 模型管控设置 | https://github.com/anthropics/claude-code/releases/tag/v2.1.283
- 2026-09-25 | VS Code 1.139.1 补丁发布，修复托管设置刷新失败被清空问题 | https://github.com/microsoft/vscode/releases/tag/1.139.1
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
- 2026-10-07 | Sonnet 5.5 缓存读取价格减半，Max/Team 订阅新增每月 API 额度（二手报道） | https://aiweekly.co/alerts/introducing-claude-haiku-55
- 2026-10-08 | Claude Code v2.1.295 为 hook 新增 onFailure: "block"，修复网关拒绝 context-1m beta 时 [1m] 模型请求全失败 | https://github.com/anthropics/claude-code/releases

## 3. 进行中事件表

- 事件：Claude Code 周额度新政 09-14 生效后引发用户取消订阅、转向 Codex 等批评；最后进展日期：2026-09-17；下一步关注点：等 Anthropic 是否就此发布正式回应或政策调整方案（`/rate-limit-options` 不计）。
- 事件：Windows 09 月累积更新(KB5124008/KB5124012)导致 Claude Desktop Cowork 沙盒 Plan9 共享挂载失败，Microsoft 09-14 发布带外补丁 KB5129195/KB5129194 称已修复，但仍有用户报告全新会话首次挂载失败；最后进展日期：2026-09-19；下一步关注点：等 Microsoft 发布进一步修复补丁，或 Anthropic/Microsoft 确认问题已彻底解决。
- 事件：Claude Cowork 并入聊天界面，Claude Docs/Slides/Design 以 Beta 上线；官方支持页显示 Docs Beta 已覆盖 Pro/Max/Team/Enterprise（日期未确认）；最后进展日期：2026-09-16；下一步关注点：核实 Slides/Design 是否扩展至 Team/Free 及时间，或由 Beta 转 GA。
