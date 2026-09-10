# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻:2026-09-10 18:39 UTC
- 上次运行时刻:2026-08-21 12:45 UTC
- 实际覆盖窗口:距上次运行超20天,超过10天封顶上限,按封顶处理:2026-08-31 18:39 UTC 至 2026-09-10 18:39 UTC(正常窗口);封顶外(2026-08-21~2026-08-31)仅收录至今仍重要的大事,本期收录了 v2.1.251(08-28)安全修复与周额度调整公告(08-30)两项。
- 本期 VSCode / Claude App 两个方向检索均正常完成,无方向失败。VSCode:核实 VS Code 1.136 正式版(09-02)落在窗口内,已收录 Agent Merge 预览、多根工作区实验性支持、Agent Host 迁移至开放 AHP 协议(Claude Agent SDK 通过适配器接入)三项;未发现窗口内早于/晚于该版本的其他 VSCode 更新值得单独收录(1.135 于 08-26 发布,早于封顶窗口且已被 1.136 迭代覆盖,未收录;1.137 目前仅 Insiders 预览且改动较小,未收录)。Claude App:核实 Claude Code v2.1.239 至 v2.1.267(08-21至09-09)约30个版本,按主题合并收录 6 条(封顶外的 v2.1.251 安全修复因仍重要而破例收录;周额度政策调整公告 08-30 同理);Claude Fable 5.1 于 09-01 随 v2.1.257 成为默认 Fable 模型已收录;未发现 Claude Desktop/claude.ai 网页端在窗口内有超出 Claude Code 共享改动之外的独立重大更新。生态与社区动向:本期未发现与 VSCode/Claude App 直接相关的新第三方事件,故省略该板块正文。
- 进行中事件表中 Agent Plugins 条目自 2026-08-06 最后一次实质进展至今(09-10)已连续超过 21 天无新进展(本期为第 9 次窗口内定向检索,含官方博客/Newsroom、Claude Code Changelog(至 v2.1.267)、官方及第三方报道,仍未发现 Anthropic 官方回应或加入该标准治理机构的公告;检索到的"Claude Code 可安装 Agent Plugins"说法仅源于 SKILL.md/MCP 组件天然兼容,非 Anthropic 官方声明,不计入进展),按规则移出跟踪表。同时新增一条跟踪:Claude Code 周额度政策调整效果待验证。

## 2. 已报条目清单(最近 21 天)

- 2026-08-20 | Claude Code v2.1.237/v2.1.238 发布,新增内置 Concise 输出风格与 keybindingFlavor 设置,修复长会话内存增长问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.238
- 2026-08-20 | Claude Desktop v1.34493.0 发布,修复 macOS 启动卡死、周期任务日期错误、Touch ID 崩溃等问题 | https://claude.com/docs/cowork/changelog
- 2026-08-28 | Claude Code v2.1.251 发布,修复文件工具符号链接置换绕过权限检查、插件市场路径穿越执行、Bash 算术赋值权限检查绕过等安全问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.251
- 2026-08-30 | Anthropic 宣布 Claude Code 周额度自 09-14 起对 Pro/Max/Team/企业席位版永久上调 25%,但因 5 月以来临时 50% 上浮同期到期,较当前水平实际下降 17%,引发社区质疑后追加说明 | https://www.mindstudio.ai/blog/claude-code-weekly-rate-limit-changes
- 2026-09-01 | Claude Code v2.1.257 发布,将 Claude Fable 5.1(100万上下文)设为默认 Fable 模型,定价调整为 $10/$50 每百万 token,并为 Auto Mode 新增隔离逃逸规则阻止云凭据窃取类操作自动批准 | https://github.com/anthropics/claude-code/releases/tag/v2.1.257
- 2026-09-01 | Claude Code v2.1.258 发布,修复 macOS 12(Monterey)启动失败回归问题及远程/计划会话权限批准后消息为空导致失败的问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.258
- 2026-09-02 | VS Code 1.136 正式版发布,新增 Agent Merge(预览)自动处理 PR 评审意见/失败检查/合并冲突,实验性支持多根工作区 Copilot/Claude agent 会话 | https://code.visualstudio.com/updates/v1_136
- 2026-09-02 | VS Code 1.136 将 Agent Host 迁移至开放的 Agent Host Protocol(AHP,JSON-RPC、厂商中立),Claude Agent SDK 通过适配器接入该协议 | https://www.infoworld.com/article/4218856/visual-studio-code-1-136-introduces-agent-merges-for-pull-requests.html
- 2026-09-02~09-04 | Claude Code v2.1.259–v2.1.261 发布,新增组织托管 MCP 服务器 managedMcpServers、--permission-prompts none 无人值守模式、GitLab 合并请求识别、未提交改动 diff 面板与 /skill-doctor 未用技能诊断 | https://github.com/anthropics/claude-code/releases/tag/v2.1.261
- 2026-09-08 | Claude Code v2.1.265 发布,修复插件目录符号链接容器边界检查问题,新增用户邮箱/组遥测字段与 --plugin-dir 动态插件目录支持 | https://github.com/anthropics/claude-code/releases/tag/v2.1.265
- 2026-09-09 | Claude Code v2.1.267 发布,修复插件市场路径穿越绕过安全漏洞,新增跨供应商效力上限 maxEffortLevel 设置 | https://github.com/anthropics/claude-code/releases/tag/v2.1.267

## 3. 进行中事件表

- 事件:Claude Code 周额度政策调整——Anthropic 将 5 月以来的临时 50% 上浮于 09-13 到期,同时宣布 09-14 起"永久上调 25%",对比当前水平实为下降 17%,社区质疑后追加说明;最后进展日期:2026-08-30;下一步关注点:等 09-14 新额度正式生效后的实际用户反馈,以及 Anthropic 是否发布进一步说明或调整方案。

(已移出:Agent Plugins 跨客户端插件标准与 Claude Code 现有插件格式不兼容事件——2026-08-06 首次报告后,历经 2026-08-09、08-10、08-11、08-12、08-13、08-14、08-21、09-10 共 8 次窗口内定向检索,连续超过 21 天(至 09-10 已 35 天)未发现 Anthropic 官方回应或加入该标准治理机构的公告,按规则移出跟踪表;如后续 Anthropic 官宣加入或正式回应不兼容问题,将重新收录并作为新事件报告。)
