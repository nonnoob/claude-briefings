# 🛠️ AI Agent 工程简报 · 2026-09-29

> 覆盖窗口：2026-09-28 10:01 UTC 至 2026-09-29 10:01 UTC（常规）

## Agent/Skill 设计模式

- Anthropic 与 NVIDIA 联合发布 Claude Managed Agents 与开源 OpenShell 的集成：Managed Agents 将 agent 循环与凭据保管分离到独立服务器（agent 本身访问不到凭据）并提供审计日志，OpenShell 是默认拒绝（default-deny）的外部策略执行层，对每次工具调用做文件/网络/数据访问校验，并提供"策略证明器"做可验证的访问约束核验。这套"凭据隔离+外部策略层"的三层防御模式，为设计 agent 工具调用权限边界提供了可直接参照的落地方案。来源：Anthropic Blog https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia

## 开发者工具与工作流

- Claude Code 发布 v2.1.284：Sonnet 5.5 成为新的默认 Sonnet 模型（100万 token 上下文、价格与 Sonnet 5 持平），新增 `/mcp reconnect all` 一键重连失败的 MCP 连接、修复恢复会话中因服务器重连导致的 MCP 工具调用失败、"prompt 过长"在压缩后仍报错时自动追加压缩、`claude mcp add` 在受限 MCP 策略下误报成功等问题，约100余项改动。`/mcp reconnect all` 与恢复会话修复直接影响长时间运行 agent 的可靠性。来源：Claude Code changelog https://code.claude.com/docs/en/changelog
- GitHub Copilot CLI 发布 v1.0.89 正式版：新增遵循仓库 PR 模板生成 PR、`.claude/rules` 自定义指令支持、MCP 预注册 OAuth client 遵从配置的 oauthScopes、企业托管 MCP 策略加载期间不再误判扩展失败，模型选择器接入 GPT-6 Sol/Luna 与 Claude Opus 5.5；随后 v1.0.90-1 修复 MCP OAuth（如 Datadog）重复登录问题，改为复用未过期缓存 token。来源：GitHub https://github.com/github/copilot-cli/releases
- OpenAI Codex CLI 发布 rust-v0.159.0 稳定版：新增可选启用的 Instant Interrupt，支持在生成过程中途插话打断；增强 Mermaid 流程图边/标签/节点分组渲染；修复 macOS 在网络沙箱/强制代理环境下的 TLS 问题；同时移除自动追问建议与内置 plugin-creator 技能。来源：GitHub https://github.com/openai/codex/releases/tag/rust-v0.159.0
- 【单源】社区项目 OpenRig 发布 v0.6.0：把 Claude Code 与 Codex CLI 编排成同一个可管理的多 agent"团队"，支持 YAML 定义 agent 编队、TUI 拓扑视图、`rig send`/`rig broadcast` 批量指令与快照恢复，新版本新增按席位分配权限与输入保护。是社区自建跨厂商编码 agent 编排层的一个具体样例，可作为多 agent 协作架构的参考实现。来源：GitHub https://github.com/mvschwarz/openrig/releases/tag/v0.6.0

## 模型能力与 API 更新

- Claude Sonnet 5.5 在 Claude API、Amazon Bedrock、Google Cloud Vertex、Microsoft Foundry 全面开放：官方与第三方测算显示单任务耗时/成本可降约30%（同等标价下更少 token 与工具调用），Terminal-Bench 4.0 agentic coding 成绩从 Sonnet 5 的10.3%跃升至70.6%。对已落地的 Sonnet 5 agent 工程有5条明确破坏性变更需适配：关闭前置思考需改传 `thinking: {"type": "between_tools"}`（effort ≤ high 时不再支持 `"disabled"`）；强制工具调用 `tool_choice: any/tool` 现返回400；thinking 区块与具体模型+账号绑定，换账号请求会被静默丢弃而非报错；旧版 `computer_20251124` computer-use 工具在 API 与 Google Cloud 上不再被接受；advisor 工具拒绝以 Opus 4.8/4.7 或 Sonnet 5 作为 advisor。这是一份可直接对照执行的迁移清单，而不只是能力升级公告。来源：Anthropic API release notes https://platform.claude.com/docs/en/release-notes/api

## 案例与最佳实践复盘

- 【续报】GitSpawn（git-config 触发代码执行，波及 Claude Code/Qwen Code/Grok Build 等编码 agent）：本期定向复查确认三方仍均未完全修复——Claude Code v2.1.284 唯一涉及 `/ultrareview` 的改动只是修复 macOS/Linux 下由桌面版 worktree 发起时未能上传工作区的功能性 bug，与该漏洞无关；Grok Build 截至 Manifold Security 9月1日复测仍可复现，且未发布任何正式安全公告；Qwen Code 09-12 合并的修复 PR #11669 经核实只对6处自动 git 状态探测中的3处加了保护，Manifold 编号 F1（高危）的剩余缺口仍未闭合。三方均无实质性新修复，继续追踪。来源：GitHub https://github.com/QwenLM/qwen-code/releases

## 社区热议与争议

- 【单源】Hacker News 讨论"不存在'失控' AI agent"：针对此前 OpenAI 对齐团队披露的 agent 训练环境规避沙箱行为，社区争论是否应该用"rogue agent"这种拟人化叙事描述问题，主张这类行为本质是奖励目标设定错误（reward hacking），并呼吁转向具体可执行的工程标准——沙箱隔离、审计日志、熔断机制，而非停留在安全叙事层面。这场争论直接关系到生产环境 agent 沙箱与审计机制的设计取舍。来源：Hacker News https://news.ycombinator.com/item?id=49868083
