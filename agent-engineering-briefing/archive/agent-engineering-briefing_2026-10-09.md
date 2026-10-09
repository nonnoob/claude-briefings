# 🛠️ AI Agent 工程简报 · 2026-10-09

> 覆盖窗口：2026-10-08 10:01 UTC 至 2026-10-09 10:01 UTC（常规）

今日要闻：Claude Code v2.1.295 为 command/HTTP hook 新增 `onFailure: "block"`，hook 启动失败、超时或异常退出时改为拦截动作而非放行，堵住"hook 挂了等于没防护"的洞。

## 开发者工具与工作流

- Anthropic 发布 Claude Code v2.1.295：command/HTTP hook 新增 `onFailure: "block"`（hook 无法启动、超时或异常退出时拦截而非放行）；claude.ai connector 默认协商 MCP 协议版本 2026-07-28（可设 `MCP_PROTOCOL_NEGOTIATION=legacy` 退回）；经 tool search 加载的 MCP 工具描述截断上限由 2,048 提到 16,384 字符；subagent 的 `skills` 字段最多预加载 32 个 skill；另有 97 项修复，含 headless/SDK 会话远程 MCP 断线后带退避重连。为什么值得关注：把安全类 hook 的失败策略显式设为 block 即可避免 fail-open，写长 MCP 工具描述的作者也不必再被 2KB 截断卡住。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- OpenAI Codex CLI 发布 rust-v0.162.0 稳定版：新增受管 Git worktree 工具、Code Mode 可选的排序式 tool search、自定义模型提供方的实时联网与远程 compaction 设置，并遵循服务端 `Retry-After`、修复 `apply_patch` 的 CRLF 保留及多项 Linux 沙箱问题。为什么值得关注：worktree 工具让并行 agent 任务的隔离不必再靠手写脚本，tool search 则是应对工具过多撑爆上下文的现成方案。来源：OpenAI Codex Releases https://github.com/openai/codex/releases
- GitHub Copilot CLI 发布 v1.0.95-0 至 -2 预发布：沙箱支持 `injectHosts` 配置做凭据注入、macOS 原生 Microsoft Entra broker 认证、托管插件 setup 改为每小时或策略变更时重试、`--context` 对新建与恢复的 ACP 会话均生效。为什么值得关注：`injectHosts` 体现"凭据留在沙箱外、按目标主机注入"的模式，可对照自家 agent 沙箱的密钥处理方式。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases
- Qwen Code 发布 v0.25.1-preview.1：新增后台 Shell 与 Monitor 运行时（面向受管 agent）、实验性 Kubernetes CSI 运行时，agent 与 goal 声明默认延迟加载，并修复记忆发现越过 Git 根目录等问题。为什么值得关注：延迟加载声明与后台监控是控制启动上下文和长任务可观测性的参考做法。来源：Qwen Code Releases https://github.com/QwenLM/qwen-code/releases

## 案例与最佳实践复盘

- 【续报】【矛盾】GitSpawn：Grok Build 的修复状态说法不一——Shattered.io 称其修复仍待定、列为未关闭变体；Grith 的对照表称已于 2026-07-14 作为既有报告的重复项关闭、1.0.13 已修复；xAI 官方公告仍未见，两说无法调和，建议先查 xAI release notes 再下结论（发布时间未确认）。为什么值得关注：若你的 agent 会在不可信仓库里自动执行 git status/diff，仍应按漏洞类别自查（如核对 `core.fsmonitor`），不依赖单一厂商声明。来源：Shattered.io https://shattered.io/gitspawn-ai-coding-agent-vulnerability-2026/ ；Grith https://grith.ai/blog/git-config-key-2022-fix-coding-agents
