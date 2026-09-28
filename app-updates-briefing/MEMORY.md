# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻:2026-09-28 17:10 UTC
- 上次运行时刻:2026-09-18 10:39 UTC
- 实际覆盖窗口:2026-09-18 17:10 UTC 至 2026-09-28 17:10 UTC(距上次运行超过10天封顶,按封顶处理;窗口外 2026-09-18 10:39~17:10 约6.5小时缺口未见需单独补收的大事,当期 09-18 18:06 UTC 发布的 v2.1.277 已落在封顶窗口内,无实质遗漏)。
- 本期 VSCode / Claude App 两个方向检索均正常完成,无方向失败;窗口内未发现与两者直接相关、且不属于上述两板块内容的独立生态/社区事件,故省略该板块正文。VSCode:核实 VS Code 1.139 正式版于 09-23 发布、1.139.1 补丁于 09-25 发布,均落在窗口内,收录 Agent 会话进度保留、sandbox-policy 报告、MCP 远程 URL 变量、托管设置刷新失败清空修复等要点。Claude App:核实窗口内 Claude Code 版本 v2.1.277~v2.1.283(09-18~09-25,无 v2.1.279),选取信号最强的 5 个版本(v2.1.277/278/282/283,以及 v2.1.280 并入 Opus 5.5 条目)收录,v2.1.281 因偏企业/Bedrock 细节未单独收录;另收录 09-22 Anthropic 发布 Claude Opus 5.5(成本降40%、定价下调、性能对齐 Fable 5.1,经 METR/Frontier Design/NIST CAISI 评估 CB-1)的产品级公告,并跨源(Anthropic 官方页 + TechCrunch)交叉验证发布日期一致。Windows KB Cowork 沙盒故障续报:核实 Microsoft 于 09-14 发布带外紧急补丁 KB5129195/KB5129194 称已修复 Plan9 挂载回归,但窗口内 09-19 起出现多份新 GitHub issue(#94868/#94869/#95557 等)报告打补丁重启后全新会话首次挂载仍失败,故作为【续报】收录,问题未完全解决。周额度政策事件:窗口内未检索到 Anthropic 就 09-14 生效新政发布正式回应或政策调整的新证据,维持原状未续报。Claude Cowork/Docs/Slides/Design Beta 事件:窗口内未检索到扩展至 Team/Free 或转 GA 的新证据,维持原状未续报。
- 进行中事件表变更:Windows KB Cowork 沙盒故障事件更新最后进展日期与关注点(带外补丁未完全修复,继续等后续补丁或官方确认);其余两条(周额度政策回应、Cowork/Docs/Slides/Design Beta 推广)无新进展,保留原状。

## 2. 已报条目清单(最近 21 天)

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
- 2026-09-18 | Claude Code v2.1.277 发布,新增 AGENTS.md 支持与 /plugin install --marketplace | https://github.com/anthropics/claude-code/releases/tag/v2.1.277
- 2026-09-19 | Claude Code v2.1.278 发布,Auto Mode 默认改用服务端分类器 | https://github.com/anthropics/claude-code/releases/tag/v2.1.278
- 2026-09-19(报道日期) | Windows KB5129195 带外紧急补丁未完全修复 Cowork Plan9 挂载故障,用户报告新会话首次挂载仍失败 | https://github.com/anthropics/claude-code/issues/95557
- 2026-09-22 | Anthropic 发布 Claude Opus 5.5,成本降约40%、定价下调至 $4/$20 每百万 token,Claude Code v2.1.280 设为默认 Opus 模型 | https://www.anthropic.com/claude-opus-5-5
- 2026-09-23 | VS Code 1.139 正式版发布,新增 Agent 会话进度可视化保留、Copilot sandbox-policy 报告、MCP 远程 URL 变量等 | https://code.visualstudio.com/updates/v1_139
- 2026-09-24 | Claude Code v2.1.282 发布,修复含网页搜索结果会话全部请求 400 错误等问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.282
- 2026-09-25 | Claude Code v2.1.283 发布,新增 /doctor prompt-audit 与 availableModelsMatch/deniedModels 模型管控设置 | https://github.com/anthropics/claude-code/releases/tag/v2.1.283
- 2026-09-25 | VS Code 1.139.1 补丁发布,修复托管设置刷新失败被清空问题 | https://github.com/microsoft/vscode/releases/tag/1.139.1

## 3. 进行中事件表

- 事件:Claude Code 周额度新政 09-14 生效后引发用户取消订阅、转向 Codex 等批评;最后进展日期:2026-09-17;下一步关注点:等 Anthropic 是否就此发布正式回应或政策调整方案。
- 事件:Windows 09 月累积更新(KB5124008/KB5124012)导致 Claude Desktop Cowork 沙盒 Plan9 共享挂载失败,Microsoft 09-14 发布带外补丁 KB5129195/KB5129194 称已修复,但窗口内仍有用户报告全新会话首次挂载失败;最后进展日期:2026-09-19;下一步关注点:等 Microsoft 发布进一步修复补丁,或 Anthropic/Microsoft 确认问题已彻底解决。
- 事件:Claude Cowork 并入聊天界面,Claude Docs/Slides/Design 以 Beta 形式上线,首批面向 Pro/Max 灰度推送;最后进展日期:2026-09-16;下一步关注点:等功能扩展至 Team/Free 计划,或由 Beta 转为正式版(GA)。
