# 🛠️ AI Agent 工程简报 · 2026-09-11

> 覆盖窗口：2026-09-10 至 2026-09-11（常规）

## Agent/Skill 设计模式

- Anthropic Managed Agents 09-10上线权限策略新 `auto` 模式：服务端自动评估每次 agent/MCP 工具调用（执行/拒绝/暂停待批），`agent.tool_use`/`agent.mcp_tool_use` 事件新增 `evaluation` 字段。把"资金/写操作要不要放行"的判断从模型自律搬到了基础设施层，呼应近期对多 agent 编排代码层门控的讨论方向。来源：Claude API Release Notes https://platform.claude.com/docs/en/release-notes/api

## 开发者工具与工作流

- Claude Code 09-10发布2.1.268：WebFetch 超时改为300秒后主动失败（此前会无限期挂起）、SDK 会话 `excludeDynamicSections` 场景下 prompt caching 更稳定、MCP OAuth 本地回调端口绑定修复、Artifact 发布支持断线重试。几处都是长跑 agent 常遇到的挂起/缓存失效老问题的直接修复，值得升级验证。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- Anthropic 09-10发布 ant CLI 新命令 `ant beta:sessions connect`：终端可直接接入 Managed Agents 云端会话，实时跟随执行、发消息、审批待批工具调用，支持 `--web` 打开 Console 会话查看器本地版。给"云端 agent 怎么让人随时插手"提供了一个具体交互范式。来源：Claude Platform Docs https://platform.claude.com/docs/en/release-notes/api
- Cursor 09-10发布 Projects：不写代码的"协调者" agent 负责规划任务、派发给数千个子 agent 并行执行，项目在云端持续跑（合笔记本盖子也不中断），可接入 Slack 自动响应 bug 报告频道。是重资本多 agent 编排路线的一个具体样本，跟近期"单 agent 更优"的讨论方向相反，值得对照评估。来源：Cursor Changelog https://cursor.com/changelog/projects
- 【单源】Anthropic status page 09-10记录一起进行中事故：09-08一次 Windows 系统更新导致 Claude Cowork on Windows 无法访问本地磁盘、无法执行本地命令（聊天与文件读写仍可用），判定为 Windows 端变更所致，微软在开发修复，官方暂无应用内绕过方案。Windows 上跑 Cowork 处理本地文件的任务近期要留意失败率。来源：Anthropic Status（经 StatusGator 间接核实）https://statusgator.com/services/anthropic

## 案例与最佳实践复盘

- LangChain 09-10发布客户案例：monday.com Service 团队用 LangSmith 构建"代码优先"的评测策略，把评测逻辑写成代码而非纯手工标注驱动。是评测工程化落地的一个具体参照。来源：LangChain Blog https://www.langchain.com/blog/customers-monday
- The Register/The Hacker News 09-10披露：攻击者用数百个 AI agent（基于 OpenAI Codex 与 DeepSeek 模型）批量利用 PaperCut MF/NG 漏洞，攻陷440+实例、波及395家组织。是"agent 被武器化做批量攻击"少见的有具体规模数据的案例，安全团队评估暴露面时要把 agent 驱动的攻击速度纳入威胁模型。来源：The Register https://www.theregister.com/security/2026/09/10/hundreds-of-ai-agents-helped-papercut-attacker-hit-395-orgs-and-some-went-off-script/5295650
