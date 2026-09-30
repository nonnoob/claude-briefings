# 🛠️ AI Agent 工程简报 · 2026-09-30

> 覆盖窗口：2026-09-29 10:01 UTC 至 2026-09-30 10:01 UTC（常规）

## Agent/Skill 设计模式

- Claude官方博客发布Asana案例研究：Asana基于Work Graph构建"可指导的人机协作团队"——agent角色受限、权限继承自触发者、跨任务共享记忆仅管理员可修改、任务级反馈与其他反馈区分、行为对团队全程可见可审计。这套"权限继承+记忆分级+全程可审计"的多agent系统设计，为构建企业级人机协作agent团队提供了可直接参考的落地范式。来源：Claude Blog https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude

## 开发者工具与工作流

- Claude Code发布v2.1.285：新增`CLAUDE_CODE_DISABLE_WEB_FETCH`等环境变量、`allowedProviders`受管设置（限制可用API供应商为Anthropic API/Bedrock/Vertex/Foundry等）、`claude plugin configure`命令，并修复约90余项问题，包括后台子agent权限提示被自动拒绝、模型切换后token限额报错、fork子agent丢失plan/dontAsk模式等。子agent权限与超时相关修复直接影响多agent编排的可靠性，企业环境可用`allowedProviders`锁定供应商防止误配置。来源：Claude Code changelog https://code.claude.com/docs/en/changelog
- GitHub Copilot CLI发布v1.0.90-3与v1.0.90-5：新增`--mcp-github-auth`参数将GitHub账号鉴权限制在受信任的MCP server来源、新增会话级只读目录授权；并修复MCP工具调用在server已返回结果后仍持续发送progress更新导致卡住无法完成的问题。收紧了对接第三方MCP server时的账号权限边界，降低凭据被恶意MCP server冒用的风险。来源：GitHub https://github.com/github/copilot-cli/releases/tag/v1.0.90-3
- OpenAI Codex CLI发布rust-v0.159.1：将GPT-6.1 Sol设为内置模型目录及Amazon Bedrock Mantle/Runtime目录的默认模型。未显式指定model参数的现有脚本/agent流水线行为与成本会随之变化，升级前建议核对默认模型依赖。来源：GitHub https://github.com/openai/codex/releases/tag/rust-v0.159.1
- Qwen Code发布v0.24.7：新增`/commit`斜杠命令（AI自动生成commit message）、为分支会话增加可选worktree支持，以及Managed Runtime/workspace-bound会话等基础设施改动；该版本未包含任何GitSpawn相关的git状态检测/hook安全修复（详见下文续报）。worktree支持降低了多分支并行agent会话间的上下文冲突成本。来源：GitHub https://github.com/QwenLM/qwen-code/releases/tag/v0.24.7

## 模型能力与 API 更新

- OpenAI DevDay 2026上Agents API与新Decisions API发布：Agents API新增OpenAI托管浏览器实现的computer use、可挂载MCP服务器、默认最多6个并行subagent、durable session状态保持；新Decisions API基于GPT-6 Luna定制版本，面向"有限预定义答案"的分类/路由/下一步决策场景，约150ms延迟，号称比常规Luna API调用快10倍。"用专用小模型做有限选项快速路由，替代完整LLM调用"是可直接复用的agent编排优化模式，托管subagent数量上限与durable session的具体参数也是设计长时运行agent时的架构参考。来源：Simon Willison's Weblog https://simonwillison.net/2026/Sep/29/openai-devday-2026-live-blog/

## 案例与最佳实践复盘

- 【续报】GitSpawn（git-config触发代码执行，波及Claude Code/Qwen Code/Grok Build等编码agent）：Claude Code v2.1.285本期出现多条git/worktree相关修复（SSH git配置读取修复、自托管runner侧git安全加固——跳过仓库自带Git LFS pre-push hook、忽略可写系统级`core.hooksPath`、未加`--configure-git`时不签名commit、沙箱git凭据存储报错修复、worktree证书校验修复），但逐条核对后均与GitSpawn核心攻击路径（交互式`git status`/`git diff`触发仓库自带`core.fsmonitor`等hook执行任意命令）无关，容易被误判为已修复，需明确区分；Grok Build仍无官方安全公告；Qwen Code v0.24.7未含相关修复，唯一相关PR（#12404）仅是让post-index-change hook测试用例在文件系统时钟漂移下更稳定，非安全补丁，Manifold编号F1（高危）的hook缺口仍未闭合。三方状态与9-29持平，继续追踪。来源：GitHub https://github.com/QwenLM/qwen-code/releases/tag/v0.24.7

## 社区热议与争议

- 【单源】Hacker News热议OpenAI DevDay 2026发布的"Dots"常驻后台agent：基于GPT-6 Astra，拥有独立云端算力、可持久保留上下文、接入约4000个应用，讨论聚焦"常驻/后台智能体"架构模式的技术可行性与安全信任边界，约476-515赞/357-392评论且持续增长。直接触及长时运行agent的编排、记忆持久化与后台执行安全边界等工程设计问题，是当前风向标级讨论。来源：Hacker News https://news.ycombinator.com/item?id=49896604
