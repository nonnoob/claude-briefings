# 🛠️ AI Agent 工程简报 · 2026-09-25

> 覆盖窗口：2026-09-24 至 2026-09-25 10:01 UTC（常规）

## Agent/Skill 设计模式

- LangSmith 新增 Trajectories 视图：把 agent 单次 session 拍平成按时间顺序排列的可读轨迹（消息、工具调用、子 agent 动作），可直接供在线 evaluator 打分，开箱支持 LangChain/LangGraph/Deep Agents、OpenAI/Claude SDK agent 及 Codex/Claude Code/Cursor 等编码 agent。排查 agent 失败路径时能省去手工穿透 trace 的功夫，适合接入自建 eval 流水线。来源：LangChain Blog https://www.langchain.com/blog/langsmith-trajectories-tracing
- LangChain 发布 Managed Deep Agents 0.8：新增用户级记忆（按访问策略隔离个人偏好，不与团队共享）、HTTP channel（把 agent 嵌入产品界面）、沙盒文件 API 与代理鉴权沙盒。多租户生产 agent 做记忆隔离设计时可直接参考这套权限模型。来源：LangChain Blog https://www.langchain.com/blog/langsmith-managed-deep-agents-whats-new

## 开发者工具与工作流

- Claude Code 发布 v2.1.282：direct Anthropic API 连接且遥测关闭时 auto mode 默认切换为服务端权限分类器；修复 resume 会话丢失此前 extended-thinking/reasoning 块的问题；修复 CLAUDE.md/规则文件 macOS symlink 逃逸安全漏洞；修复 Bash 权限规则 `:*` 中段匹配 bug。长会话 resume 时上下文完整性直接影响 agent 决策质量，值得关注该修复版本。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- GitHub Copilot CLI 发布 v1.0.89-2/v1.0.89-3：MCP 预注册 OAuth 客户端遵守配置的 oauthScopes、修复 MCP 配置加载在同级配置无效时误丢有效 workspace server 的 bug、修复 ask-user 表单 "Other" 自定义答案跨问题串号问题。排查多 MCP server 配置故障时可对照此修复。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases
- OpenAI Codex CLI 发布 rust-v0.157.0 稳定版：接入 GPT-6 Sol/Luna 并支持 Bedrock 兼容，新增全屏 transcript、Shift 点选文本、后台 server 自动启动、fork-conversation 快捷键。fork-conversation 降低了分支试验 prompt 策略的成本。来源：OpenAI Codex CLI Releases https://github.com/openai/codex/releases
- Windsurf 发布 v3.10.1035：修复 agent-command-center 内存泄漏，新增通过 ACP client `session/new`/`session/load` 传入的 MCP server 现可被 agent 直接调用并在 `/mcp` 中列出。此前 ACP 接入的 MCP server 对 agent 不可见，跨 IDE 共享 MCP 配置时该修复价值明显。来源：Windsurf Changelog https://windsurf.com/changelog/windsurf-next

## 模型能力与 API 更新

- Anthropic 发布博客《Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.》：披露过去 6 个月单次请求上下文量增长 2.6 倍，input:output token 比从 189:1 升至 324:1，cache-miss 率下降超 50%；Opus 5.5 单 prompt 运行时长约 3.3 倍、模型调用次数多 40%+，长会话中断率降 68%，输出速度快约 30%、典型工作负载成本比 Opus 5 低约 40%；开发者使用 tool server/skill 的比例翻倍，直接粘贴文本的比例降三分之一。这组数字直接反映长 agent 会话该怎么做缓存与成本控制，可用来对照自己项目的 prompt caching 命中率是否达标。来源：Claude Blog https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
- Anthropic API 上线 Refusal Billing Expansion：pre-output refusal 中 `stop_details.category` 为 `bio`、`frontier_llm`、`reasoning_extraction` 的请求即日起计费（此前不计费），其余拒绝类别与 fallback credit 策略不变。用高风险内容做安全护栏测试或红队评估时需要重新核算这部分请求的成本。来源：Anthropic Platform Docs https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#how-refusals-are-billed

## 案例与最佳实践复盘

- 【单源】AINews 每日摘要披露：某 "Fast Search API" 实测 p50 160ms/p95 230ms，单任务成本降 68%，已在 Hermes Agent 中免费开放，据称已成为 Shopify 主搜索 API。检索类工具的延迟/成本一旦卡在 agent 决策链路上会被逐步放大，这组数字可作为自建检索工具的性能基线参考，但摘要未点名服务提供方，建议核实后再引用。来源：Latent Space（AINews digest） https://www.latent.space/p/ainews-the-future-of-latent-space
