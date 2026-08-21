# 🛠️ AI Agent 工程简报 · 2026-08-21

> 覆盖窗口：2026-08-20 至 2026-08-21（常规）

## 开发者工具与工作流

- Claude Code 2.1.238（08-20）发布：新增 keybindingFlavor=readline 的 Bash 风格快捷键、插件市场 headersHelper（为目录/归档请求签发短时 token 等 HTTP 头）、自托管 runner 新增 --defer-shutdown-max-min 与出口代理 --proxy-authorization-command/file 参数，并修复长交互会话内存无界增长、输出风格漂移回默认等问题。长会话内存泄漏与出口代理鉴权刷新是生产部署里的高频痛点，值得升级验证。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- Google Antigravity CLI 1.1.17（08-20）发布：将 agent 执行 harness 合并为单一执行路径以提升工具/hook/prompt 行为一致性，同时修复部分斜杠命令消失、Vim 插入模式下 Enter 无法唤起后台任务/子 agent、Ogg 音视频附件因 MIME 类型识别错误被模型拒收等问题。执行路径碎片化导致的行为不一致是自建多 agent 编排里常见的隐性 bug 源，这次"单一执行路径"的合并思路可供参考。来源：Antigravity CLI Releases https://github.com/google-antigravity/antigravity-cli/releases

## 模型能力与 API 更新

- Anthropic 08-20 发生新一轮错误率升高事件：19:16 UTC 发出故障通告，claude.ai、API（api.anthropic.com）、Claude Code、Cowork 同时受影响，实际影响窗口 20:14–20:38 UTC（约24分钟）后恢复；同日另有 18:32–19:01 UTC 的 Google 连接器（Sheets/Docs/Slides/Chat）独立故障。延续本月以来近乎逐日出现的稳定性事件序列，生产 agent 的模型调用路径建议预留重试与多模型降级策略。来源：StatusGator Anthropic Outage History https://statusgator.com/services/anthropic/outage-history
