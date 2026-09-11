# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻:2026-09-11 10:40 UTC
- 上次运行时刻:2026-09-10 18:39 UTC
- 实际覆盖窗口:2026-09-10 18:39 UTC 至 2026-09-11 10:40 UTC(正常窗口,间隔不足1天,无需封顶)。
- 本期 VSCode / Claude App 两个方向检索均正常完成,无方向失败。Claude App:核实 Claude Code v2.1.268(09-10 20:30 UTC 发布)落在窗口内,收录其中三项:修复 v2.1.265 引入的第三方 Anthropic 兼容端点 HTTP 400 回归、WebFetch 挂起新增 300 秒超时、模型访问缓存过期导致静默切换默认模型的修复,以及 Gateway 定价配置支持;未发现 v2.1.268 之后有更新版本,亦未发现 Claude Desktop/claude.ai 网页端在窗口内有独立更新。VSCode:核实 VS Code 最新 GitHub Release 为 1.137.0(09-09 15:32 UTC),发布时间早于本期窗口起点(09-10 18:39 UTC),属上期窗口内事件,上期已判定为"改动较小的 Insiders 预览"未收录,本期窗口内未发现更新的 VSCode 版本或该判定的新证据,故本期不重复处理,VSCode 板块本期无内容,省略板块正文。生态与社区动向:检索到的"周额度政策调整后 Anthropic 删除原帖并追加澄清(含'working on exciting changes'表态)"报道均指向 08-30 前后同一次澄清,与已报条目及进行中事件表所记录的"追加说明"为同一事件,未见晚于该次澄清的新实质进展,不作续报;窗口内未发现其他与 VSCode/Claude App 直接相关的第三方生态事件,故省略该板块正文。
- 进行中事件表:"Claude Code 周额度政策调整效果待验证"本期定向检索(官方公告页、社区/媒体报道)未发现晚于 08-30 澄清的新实质进展(09-14 新额度尚未生效),继续保留,关注点不变。

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

## 3. 进行中事件表

- 事件:Claude Code 周额度政策调整——Anthropic 将 5 月以来的临时 50% 上浮于 09-13 到期,同时宣布 09-14 起"永久上调 25%",对比当前水平实为下降 17%,社区质疑后追加说明(含删除原帖、补发承认下降的澄清声明);最后进展日期:2026-08-30;下一步关注点:等 09-14 新额度正式生效后的实际用户反馈,以及 Anthropic 是否发布进一步说明或调整方案。
