# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻:2026-09-18 10:39 UTC
- 上次运行时刻:2026-09-11 10:40 UTC
- 实际覆盖窗口:2026-09-11 10:40 UTC 至 2026-09-18 10:39 UTC(正常周更窗口)。
- 本期 VSCode / Claude App 两个方向检索均正常完成,无方向失败;本期窗口内未发现与两者直接相关、且不属于上述两板块内容的独立生态/社区事件,故省略该板块正文。VSCode:核实 VS Code 1.138 正式版于 09-16 发布,落在窗口内,收录 Dev Container Agent 会话、Codex 跨应用/跨订阅支持、会话自动清理预览、CJK 等宽字体对齐等要点。Claude App:核实窗口内 Claude Code 版本 v2.1.269~v2.1.276(09-11~09-18)共 8 个版本发布,选取信号最强的若干版本(v2.1.269/271/273/274/275/276)合并为 5 条收录,其余(v2.1.270、v2.1.272)为无实质新增的小修复版本未单独收录;另收录 09-16 Anthropic 宣布 Claude Cowork 并入聊天界面并上线 Docs/Slides/Design Beta 的产品级公告,以及 09-08 起 Windows 累积更新(KB5124008/KB5124012)导致 Claude Desktop Cowork 沙盒故障、经多个独立 GitHub issue 确认且窗口内仍未修复的问题(首次收录,事件起点早于窗口但持续影响窗口内的可用性,予以收录并登记进行中事件表跟踪)。周额度政策续报:核实 09-14 新额度已正式生效,较临时上浮期实际下降约 17%,窗口内出现用户取消订阅、转向 Codex 等实质反馈,作为【续报】收录,Anthropic 尚未就此发布新的正式回应或调整方案。
- 进行中事件表变更:原"Claude Code 周额度政策调整效果待验证"事件的预期里程碑(09-14 生效及用户反馈)已在本期观测到并作为续报收录,更新关注点为后续是否有官方回应/政策调整,继续保留;新增两条:Windows 累积更新导致 Cowork 沙盒故障(等修复)、Claude Cowork/Chat 合并与 Docs/Slides/Design Beta 灰度扩大(等推广至 Team/Free 或转正式版)。

## 2. 已报条目清单(最近 21 天)

- 2026-08-28 | Claude Code v2.1.251 发布,修复文件工具符号链接置换绕过权限检查、插件市场路径穿越执行、Bash 算术赋值权限检查绕过等安全问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.251
- 2026-08-30 | Anthropic 宣布 Claude Code 周额度自 09-14 起对 Pro/Max/Team/企业席位版永久上调 25%,但因 5 月以来临时 50% 上浮同期到期,较当前水平实际下降 17%,引发社区质疑后追加说明 | https://www.mindstudio.ai/blog/claude-code-weekly-rate-limit-changes
- 2026-09-01 | Claude Code v2.1.257 发布,将 Claude Fable 5.1(100万上下文)设为默认 Fable 模型,定价调整为 $10/$50 每百万 token,并为 Auto Mode 新增隔离逃逸规则阻止云凭据窃取类操作自动批准 | https://github.com/anthropics/claude-code/releases/tag/v2.1.257
- 2026-09-01 | Claude Code v2.1.258 发布,修复 macOS 12(Monterey)启动失败回归问题及远程/计划会话权限批准后消息为空导致失败的问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.258
- 2026-09-02 | VS Code 1.136 正式版发布,新增 Agent Merge(预览)自动处理 PR 评审意见/失败检查/合并冲突,实验性支持多根工作区 Copilot/Claude agent 会话 | https://code.visualstudio.com/updates/v1_136
- 2026-09-02 | VS Code 1.136 将 Agent Host 迁移至开放的 Agent Host Protocol(AHP,JSON-RPC、厂商中立),Claude Agent SDK 通过适配器接入该协议 | https://www.infoworld.com/article/4218856/visual-studio-code-1-136-introduces-agent-merges-for-pull-requests.html
- 2026-09-02~09-04 | Claude Code v2.1.259–v2.1.261 发布,新增组织托管 MCP 服务器 managedMcpServers、--permission-prompts none 无人值守模式、GitLab 合并请求识别、未提交改动 diff 面板与 /skill-doctor 未用技能诊断 | https://github.com/anthropics/claude-code/releases/tag/v2.1.261
- 2026-09-08 | Claude Code v2.1.265 发布,修复插件目录符号链接容器边界检查问题,新增用户邮箱/组遥测字段与 --plugin-dir 动态插件目录支持 | https://github.com/anthropics/claude-code/releases/tag/v2.1.265
- 2026-09-09 | Claude Code v2.1.267 发布,修复插件市场路径穿越绕过安全漏洞,新增跨供应商效力上限 maxEffortLevel 设置 | https://github.com/anthropics/claude-code/releases/tag/v2.1.267
- 2026-09-10 | Claude Code v2.1.268 发布,修复第三方兼容端点 HTTP 400 回归与 WebFetch 挂起问题(新增 300 秒超时),修复模型访问缓存过期导致静默切换默认模型的问题,新增 Gateway 定价配置支持 | https://github.com/anthropics/claude-code/releases/tag/v2.1.268
- 2026-09-11 | Claude Code v2.1.269 发布,新增插件评分工具 claude plugin eval、/output-style 输出风格切换与 Bash 工具改动 diff | https://github.com/anthropics/claude-code/releases/tag/v2.1.269
- 2026-09-12(报道日期) | Windows 09 月累积更新(KB5124008/KB5124012)导致 Claude Desktop Cowork 沙盒 Plan9 共享挂载失败,device_bash 无响应,窗口内仍未修复 | https://github.com/anthropics/claude-code/issues/92958
- 2026-09-14 | Claude Code 周额度新政正式生效,较临时上浮期实际削减约 17%,引发部分高阶订阅用户取消订阅转向 Codex | https://www.mindstudio.ai/blog/claude-code-weekly-rate-limit-changes
- 2026-09-14 | Claude Code v2.1.271 发布,为 Remote 会话新增 Fast Mode 并支持按命令设置 Auto Mode 域名白名单 | https://github.com/anthropics/claude-code/releases/tag/v2.1.271
- 2026-09-16 | VS Code 1.138 正式版发布,新增 Dev Container 内运行 Agent 会话、扩展 Codex 跨应用/跨订阅支持 | https://code.visualstudio.com/updates/v1_138
- 2026-09-16 | Anthropic 宣布将 Claude Cowork 并入 Claude 聊天界面,并以 Beta 上线 Claude Docs、Claude Slides、Claude Design | https://www.technology.org/2026/09/17/anthropic-claude-chat-cowork-merge-docs-slides/
- 2026-09-17 | Claude Code v2.1.274 新增内存临界告警,修复会话记录损坏导致的 unexpected tool_use_id 报错(自愈) | https://github.com/anthropics/claude-code/releases/tag/v2.1.274
- 2026-09-17 | Claude Code v2.1.275 新增发送并打断快捷键与 claude.ai 账号技能/插件同步终端功能 | https://github.com/anthropics/claude-code/releases/tag/v2.1.275
- 2026-09-18 | Claude Code v2.1.276 修复 v2.1.275 引入的第三方网关/代理下全部请求 400 错误回归 | https://github.com/anthropics/claude-code/releases/tag/v2.1.276

## 3. 进行中事件表

- 事件:Claude Code 周额度新政 09-14 生效后引发用户取消订阅、转向 Codex 等批评;最后进展日期:2026-09-17;下一步关注点:等 Anthropic 是否就此发布正式回应或政策调整方案。
- 事件:Windows 09 月累积更新(x64 KB5124008 / ARM64 KB5124012)导致 Claude Desktop Cowork 沙盒虚拟机 Plan9 共享挂载失败,device_bash 无响应,应用内暂无规避方案;最后进展日期:2026-09-12;下一步关注点:等 Microsoft 撤回/修复该 KB,或 Anthropic 发布沙盒绕行方案。
- 事件:Claude Cowork 并入聊天界面,Claude Docs/Slides/Design 以 Beta 形式上线,首批面向 Pro/Max 灰度推送;最后进展日期:2026-09-16;下一步关注点:等功能扩展至 Team/Free 计划,或由 Beta 转为正式版(GA)。
