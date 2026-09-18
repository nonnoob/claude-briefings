# 🛠️ 开发工具更新周报 · 2026-09-18

> 覆盖窗口：2026-09-11 10:40 UTC 至 2026-09-18 10:39 UTC（常规）

## VSCode 更新

- VS Code 1.138 正式版发布（09-16）：新增 Agent 会话可在项目本地 Dev Container 中运行（自带项目工具链与依赖），并扩展 Codex 支持——会话可在 ChatGPT App 与 VS Code 间切换、Copilot 与 ChatGPT 订阅可中途互换。来源：VS Code Updates https://code.visualstudio.com/updates/v1_138
- 1.138 同时加入已合并会话自动清理（预览）、Insiders 版新增可跨应用分享/重新打开的会话链接，以及 `editor.forceFullwidthCharacterWidth` 设置改善等宽字体下 CJK 文本的表格对齐。来源：Windows Report https://windowsreport.com/vs-code-1-138-releases-with-dev-container-agent-sessions-expanded-codex-support-more/

## Claude App 更新

- Anthropic 宣布将 Claude Cowork 并入 Claude 聊天主界面（09-16），同一对话中可即问即答，也可委派长任务并在设备关闭后继续运行；同时以 Beta 形式上线 Claude Docs、Claude Slides（可导出 PDF/PPT）及集成进对话的 Claude Design，先向 Pro/Max 的网页、桌面、移动端灰度推送，Team/Free 计划后续跟进，企业管理员将提前 30 天收到通知。来源：Technology.org https://www.technology.org/2026/09/17/anthropic-claude-chat-cowork-merge-docs-slides/
- 【续报】Claude Code 周额度新政 09-14 正式生效，对比此前临时上浮期水平实际削减约 17%；多名 Max 20x 等高阶订阅用户反映使用 Fable 5.1 单任务即耗尽 80%~90% 额度，已有用户在生效当天取消订阅并转向 OpenAI Codex，Anthropic 回应称此举是把此前临时额度永久化、后续会改进用量可见性与控制手段，尚未就用户流失批评发布进一步调整方案。来源：MindStudio https://www.mindstudio.ai/blog/claude-code-weekly-rate-limit-changes
- Windows 09 月累积更新（x64 KB5124008 / ARM64 KB5124012）导致 Claude Desktop 的 Cowork 本地沙盒虚拟机 Plan9 共享挂载静默失败、`device_bash` 无响应，应用内暂无规避方案，目前只有回滚该补丁可恢复；多名用户在 GitHub 上各自独立提交问题予以确认。来源：GitHub Issues https://github.com/anthropics/claude-code/issues/92958
- Claude Code v2.1.269（09-11）新增 `claude plugin eval` 插件评分与 HTML 报告、`/output-style` 快速切换输出风格、Bash 工具文件改动 diff 展示，以及 OpenTelemetry 仓库级指标。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.269
- Claude Code v2.1.271（09-14）为 Remote 云端/自托管会话新增 Fast Mode，并支持在 Auto Mode 下为 Bash/PowerShell/Monitor 按命令设置 `allowed_domains` 域名白名单。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.271
- Claude Code v2.1.273/v2.1.274（09-15~09-17）新增网关提示头、MCP 服务器断线通知、可从 Remote Control 会话派生（fork）新会话，以及内存临界告警提示；并修复了会话记录损坏导致的 "unexpected tool_use_id" 报错（现可自愈修复）。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.274
- Claude Code v2.1.275（09-17）新增发送并打断当前回合的快捷键（Ctrl+Enter / Ctrl+X Ctrl+S）、将 claude.ai 账号里的技能与插件同步到终端会话、`/plugin install --marketplace` 参数；次日 v2.1.276 紧急修复了该版本引入的、经第三方兼容网关/代理转发时全部请求返回 400 错误的回归问题。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.275
