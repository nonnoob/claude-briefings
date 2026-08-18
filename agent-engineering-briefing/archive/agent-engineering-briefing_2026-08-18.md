# 🛠️ AI Agent 工程简报 · 2026-08-18

> 覆盖窗口：2026-08-17 至 2026-08-18（常规）

## 开发者工具与工作流

- 【续报】Claude Code 发布 2.1.234（08-17）：新增"用量限额重置后自动续跑"会话连续性开关（可在 /config 关闭），并修复 auto mode 默认化后暴露的两个可靠性问题——长会话经过 /compact 后反复误判沙箱命令的联网权限、后台 subagent 权限确认（含拒绝）被静默丢弃。为什么值得关注：这是 auto mode 对 Pro/Max/Team 默认开启（08-14起）后首次出现的针对性可靠性修复，用 auto mode 跑长任务时建议留意这两类问题是否曾影响过你的会话。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog

## 模型能力与 API 更新

- Anthropic 08-17 发生 Opus 5/Sonnet 5/Mythos 5/Fable 5 请求错误率升高故障，约13:56–15:29 UTC 修复并转入观察，是本周内第三次服务稳定性事件（继08-14鉴权+推理同时故障、08-16约36分钟多服务同时故障之后）。为什么值得关注：短期内连续出现的稳定性问题提示生产环境要为 Claude API 调用设计好重试与降级路径，不要假设单一供应商长期可用。来源：Anthropic Status https://status.anthropic.com/incidents/72f99lh1cj2c
