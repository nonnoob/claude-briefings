# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻：2026-10-02 10:36 UTC
- 上次运行时刻：2026-09-28 17:10 UTC
- 实际覆盖窗口：2026-09-28 17:10 UTC 至 2026-10-02 10:36 UTC（常规，约3.7天，未超10天封顶）。
- 本期 VSCode / Claude App 两个方向检索均正常完成，无方向失败；窗口内未发现与两者直接相关、且不属于上述两板块内容的独立生态/社区事件，故省略该板块正文。VSCode：核实 VS Code 1.140 正式版于 09-30 发布，落在窗口内，收录跨文件夹 Agent 会话、远程任务委托、HydraFusion 多模型协同研究预览、共享 worktree 文件夹、工作区级 `.mcp.json` 等要点。Claude App：核实窗口内 Claude Code 版本 v2.1.284~v2.1.287（09-28~10-01），逐一核对后选取信号最强的内容收录：v2.1.284 的 Claude Sonnet 5.5 默认模型切换并入 Sonnet 5.5 产品级公告一并收录（官方页 + SiliconANGLE/VentureBeat 独立报道交叉验证日期一致），v2.1.285/286 各取一条代表性变更，v2.1.287 的 Mods 插件深层改写机制作为本期最大功能更新单独收录；其余细碎修复未逐条收录。进行中事件表逐一按关注点定向检索：周额度政策回应——未检索到 Anthropic 就此发布正式回应或政策调整的新证据（v2.1.284 新增的 `/rate-limit-options` 仅为既有命令发现性优化，非政策调整，未作续报），维持原状；Windows KB Cowork 沙盒故障——未检索到窗口内（09-28~10-01）的新证据，9-21 的 #95910（同一问题在 Release Preview build 复发）在窗口开始前已存在且无新评论，维持原状；Claude Cowork/Docs/Slides/Design Beta——未检索到扩展至 Team/Free 或转 GA 的新证据，维持原状。三项均无实质新进展，故本期简报正文不含续报条目。
- 进行中事件表变更：无（三条均无新进展，保留原状）。

## 2. 已报条目清单（最近 21 天）

- 2026-09-11 | Claude Code v2.1.269 发布，新增插件评分工具 claude plugin eval、/output-style 输出风格切换与 Bash 工具改动 diff | https://github.com/anthropics/claude-code/releases/tag/v2.1.269
- 2026-09-12(报道日期) | Windows 09 月累积更新(KB5124008/KB5124012)导致 Claude Desktop Cowork 沙盒 Plan9 共享挂载失败，device_bash 无响应，窗口内仍未修复 | https://github.com/anthropics/claude-code/issues/92958
- 2026-09-14 | Claude Code 周额度新政正式生效，较临时上浮期实际削减约 17%，引发部分高阶订阅用户取消订阅转向 Codex | https://www.mindstudio.ai/blog/claude-code-weekly-rate-limit-changes
- 2026-09-14 | Claude Code v2.1.271 发布，为 Remote 会话新增 Fast Mode 并支持按命令设置 Auto Mode 域名白名单 | https://github.com/anthropics/claude-code/releases/tag/v2.1.271
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

## 3. 进行中事件表

- 事件：Claude Code 周额度新政 09-14 生效后引发用户取消订阅、转向 Codex 等批评；最后进展日期：2026-09-17；下一步关注点：等 Anthropic 是否就此发布正式回应或政策调整方案（v2.1.284 新增的 `/rate-limit-options` 仅为既有命令发现性优化，不计入实质回应）。
- 事件：Windows 09 月累积更新(KB5124008/KB5124012)导致 Claude Desktop Cowork 沙盒 Plan9 共享挂载失败，Microsoft 09-14 发布带外补丁 KB5129195/KB5129194 称已修复，但窗口内仍有用户报告全新会话首次挂载失败；最后进展日期：2026-09-19；下一步关注点：等 Microsoft 发布进一步修复补丁，或 Anthropic/Microsoft 确认问题已彻底解决。
- 事件：Claude Cowork 并入聊天界面，Claude Docs/Slides/Design 以 Beta 形式上线，首批面向 Pro/Max 灰度推送；最后进展日期：2026-09-16；下一步关注点：等功能扩展至 Team/Free 计划，或由 Beta 转为正式版(GA)。
