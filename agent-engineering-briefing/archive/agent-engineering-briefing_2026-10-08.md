# 🛠️ AI Agent 工程简报 · 2026-10-08

> 覆盖窗口：2026-10-07 10:01 UTC 至 2026-10-08 10:01 UTC（常规）

## 开发者工具与工作流

- Claude Code 发布 v2.1.293：新增 Haiku 5.5 为默认 Haiku 模型，修复 compaction 后 Claude 把压缩前动作当作已完成而重做/撤回工作的问题、HTTP MCP 连接累积每个请求的内存泄漏，mods 的 `$.tool.register` 新增 `isDeferred`（可让工具 schema 一开始就列入 prompt 而非藏在 tool search 之后）。为什么值得关注：长会话 agent 若遇到"做过的事又重做"，升级即可排查；关键工具不想被延迟加载可用 isDeferred 控制。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- Claude Code 发布 v2.1.294：修复以"指令式"写法编写的 `prompt`/`agent` hook（如"阻止……命令"）会放行本应拦截动作的问题，并改进 Stop/SubagentStop 上 prompt hook 的判定。为什么值得关注：如果你用自然语言 hook 做护栏，需要升级并复测拦截是否生效。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- OpenAI Codex CLI 发布 rust-v0.161.0 稳定版：GPT-6.1 Sol 成为内置与 Bedrock 目录默认模型，新增会话内 `/mcp login <name>`，已批准的文件系统提权在放宽写权限时仍保留读拒绝与网络限制，Bedrock 支持 multi-agent V2。为什么值得关注：权限升级时"拒绝规则不被覆盖"是沙箱型 agent 的通用设计要点，可对照自己的审批流。来源：OpenAI Codex Releases https://github.com/openai/codex/releases
- GitHub Copilot CLI v1.0.93 转正式版：`/sandbox` 与 `--sandbox` 向全部用户开放、企业 `permissions.limitTo` 强制托管域名边界、MCP 配置变更在回合间生效无需重启；1.0.94 预发布已接入 Claude Haiku 5.5 并允许托管策略将会话锁定为手动审批。为什么值得关注：给团队推广编码 agent 时，网络域名白名单加沙箱是可直接照搬的企业治理组合。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases

## 模型能力与 API 更新

- Anthropic 发布 Claude Haiku 5.5（`claude-haiku-5-5`）：100 万 token 上下文、12.8 万最大输出、自适应思考与 effort 参数，定价 $0.10/$0.50 每百万 token（超 10 万 token 提示为 $0.50/$2.50）；从 Haiku 4.5 迁移需注意手动 `budget_tokens` 扩展思考会返回 400、默认开启自适应思考、同样文本消耗更多 token。为什么值得关注：subagent/路由层的廉价模型档位有了长上下文选项，但迁移前要改掉 budget_tokens 并重估 token 成本。来源：Anthropic API Release Notes https://platform.claude.com/docs/en/release-notes/api
- Anthropic 将 Sonnet 5.5 的 prompt cache 读取价从 $0.20 降至 $0.10 每百万 token（基础输入价的 0.05 倍），写入与其他价格不变。为什么值得关注：长前缀、多轮调用的 agent 缓存收益更高，可重新评估"稳定前缀+缓存"与摘要压缩的成本平衡。来源：Anthropic API Release Notes https://platform.claude.com/docs/en/release-notes/api
- Anthropic Python/TypeScript SDK 上线浏览器使用与 computer use 工具的 beta 基类：继承后每个工具只需实现一个方法，SDK 负责工具循环、URL/文件策略与审批回调。为什么值得关注：自建 computer-use agent 可省掉手写工具循环与策略层，审批回调是现成的人在回路接入点。来源：Anthropic API Release Notes https://platform.claude.com/docs/en/release-notes/api
- Claude Managed Agents 收紧网络策略：`limited` 网络下 `allowed_hosts` 现同样约束 web 工具，`allowed_domains` 超出 `allowed_hosts` 即 400，且 `web_fetch` 只能抓取会话上下文中已出现的 URL（否则返回 `url_not_in_prior_context`）。为什么值得关注：这是针对提示注入外泄的"只抓已知 URL"防御模式，可借鉴到自建 agent 的 fetch 工具；已有 Managed Agents 会话需检查配置是否被拒。来源：Anthropic API Release Notes https://platform.claude.com/docs/en/release-notes/api
