# MEMORY

## 1. 本次运行

- 运行时刻：2026-10-20 06:15 UTC
- 实际覆盖窗口：2026-10-13 06:15 UTC 至 2026-10-20 06:15 UTC（补漏：上次运行 2026-10-10 10:05 UTC，超出 7 天封顶；2026-10-10 至 2026-10-13 期间仅收录至今仍重要的大事）
- 备注：四个方向（开发者工具与工作流、模型能力与API更新、Agent架构与设计模式、社区热议与争议）均已检索核实。Claude Code 更新至 v2.1.303 并推出 Code Review GA；Anthropic 披露用自研服务端版本控制 Scion 替换核心单仓 Git；Codex CLI 发布 rust-v0.163.0；Copilot CLI 更新至 v1.0.99-3；Qwen Code 发布 v0.25.2/v0.25.3。

## 2. 已报条目清单（保留最近 14 天）

- 2026-10-19 | Claude Code发布v2.1.299至v2.1.303：54分钟终端空闲自动压缩、Mods虚拟文本与子agent轨迹视图、OTel tool_decision埋点、SDK/桌面/VS Code默认开启fork subagents | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-10-19 | Anthropic将Claude Code多agent代码审查（Code Review）转为正式版（GA），披露内部90%代码由Claude编写、持续流审查令回滚率降逾40% | https://www.unite.ai/anthropic-makes-code-review-for-claude-code-generally-available/
- 2026-10-19 | OpenAI Codex CLI发布rust-v0.163.0：默认即时转向、/config实时搜索、/keymap前缀键、/daemon管理与只读工具并行执行 | https://www.developersdigest.tech/blog/codex-cli-0-163-instant-steering-config-search-2026
- 2026-10-19 | GitHub Copilot CLI发布v1.0.97至v1.0.99-3（接入Gemini 4 Argon、--disable-client-telemetry）；Qwen Code发布v0.25.2/v0.25.3（跨agent同屏协作、快照隔离子agent、K8s持久化会话） | https://github.com/github/copilot-cli/releases
- 2026-10-19 | Claude Developer Platform上线OpenTelemetry导出（beta）并将Opus 5.5 Fast Mode转为正式版 | https://docs.anthropic.com/en/release-notes/api
- 2026-10-19 | OpenAI开放Decisions API公测（基于gpt-6-luna，提速10倍、仅按输入token计费$0.10/M） | https://developers.openai.com/api/docs/guides/decisions
- 2026-10-19 | Meta开源816B多模态模型Muse Spark Open（1M上下文），Reflection AI以Apache 2.0开放501B编码模型Beam 1.0权重 | https://huggingface.co/blog/meta-muse-spark-open
- 2026-10-19 | Anthropic工程博客披露因agent令日均合入暴增至3万次，用自研服务端版本控制系统Scion替代核心单仓Git | https://www.anthropic.com/engineering/redesigning-source-control
- 2026-10-19 | LangChain连发Deep Agents上下文工程与ScaleDown压缩长文，拆解虚拟文件系统记忆与子agent上下文隔离模式 | https://www.langchain.com/blog/context-engineering-deep-agents-remember
- 2026-10-19 | LangChain发表Agent Evals常见问答指南；LlamaIndex发布Extract v2.5与Just-in-Time Agentic OCR双遍按需精读模式 | https://www.langchain.com/blog/common-questions-about-agent-evals
- 2026-10-19 | HN热议Anthropic用Scion取代Git：agent时代重回集中式版本控制及对Piper/Sapling先驱归因争议 | https://news.ycombinator.com/item?id=50106738
- 2026-10-19 | Jeremy Scheff《My obituary for programming》（经Simon Willison推介）引发社区对传统手写代码解谜乐趣消逝的共鸣 | https://simonwillison.net/2026/Oct/19/my-obituary-for-programming/
- 2026-10-19 | OpenCode旧系统遭入侵波及约1.4% Console用户保存的第三方AI API密钥；印度CERT-In发布自治agent配置令牌越界警告 | https://seethroughai.substack.com/p/top-ai-news-of-the-week-33-october

- 2026-10-10 | Claude Code发布v2.1.296：subagent autoCompactWindow、CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL、Read allow_large | https://code.claude.com/docs/en/changelog
- 2026-10-10 | OpenAI Codex CLI发布rust-v0.162.1稳定版：修复TUI多行异步提问崩溃与启动特性不一致 | https://github.com/openai/codex/releases
- 2026-10-10 | GitHub Copilot CLI v1.0.95正式版与v1.0.96-0至-2预发布：权限时间线、/add-dir沙箱授权、密钥掩码主机 | https://github.com/github/copilot-cli/releases
- 2026-10-10 | Claude Managed Agents上线Dynamic Workflows beta：agent自写多agent工作流并服务端后台运行 | https://platform.claude.com/docs/en/release-notes/api
- 2026-10-10 | 【续报】【矛盾】GitSpawn：Grok Build修复状态仍无官方公告 | https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-coding-agent-git-config-rce-20260904-cs/

- 2026-10-09 | Claude Code发布v2.1.295：hook新增onFailure:"block"、claude.ai connector默认协商MCP 2026-07-28、MCP工具描述截断上限提至16384字符、subagent最多预加载32个skill | https://code.claude.com/docs/en/changelog
- 2026-10-09 | OpenAI Codex CLI发布rust-v0.162.0稳定版：受管Git worktree工具、Code Mode排序式tool search、自定义provider远程compaction | https://github.com/openai/codex/releases
- 2026-10-09 | GitHub Copilot CLI v1.0.95-0至-2预发布：沙箱injectHosts凭据注入、macOS Entra broker认证、--context对ACP会话生效 | https://github.com/github/copilot-cli/releases
- 2026-10-09 | Qwen Code发布v0.25.1-preview.1：后台Shell与Monitor运行时、实验性K8s CSI运行时、agent/goal声明默认延迟加载 | https://github.com/QwenLM/qwen-code/releases
- 2026-10-09 | 【续报】【矛盾】GitSpawn：Grok Build修复状态两说（Shattered.io称待定；Grith称1.0.13已修复），xAI无官方公告 | https://grith.ai/blog/git-config-key-2022-fix-coding-agents

- 2026-10-08 | Claude Code发布v2.1.293：Haiku 5.5成默认Haiku、修复compaction后重做已完成工作、HTTP MCP内存泄漏、mods新增isDeferred | https://code.claude.com/docs/en/changelog
- 2026-10-08 | Claude Code发布v2.1.294：修复指令式prompt/agent hook放行本应拦截动作、改进Stop/SubagentStop prompt hook判定 | https://code.claude.com/docs/en/changelog
- 2026-10-08 | OpenAI Codex CLI发布rust-v0.161.0稳定版：GPT-6.1 Sol成默认模型、/mcp login、提权保留读拒绝与网络限制 | https://github.com/openai/codex/releases
- 2026-10-08 | GitHub Copilot CLI v1.0.93转正式版（/sandbox全员开放、permissions.limitTo、MCP配置回合间生效）及v1.0.94预发布接入Haiku 5.5 | https://github.com/github/copilot-cli/releases
- 2026-10-08 | Anthropic发布Claude Haiku 5.5：1M上下文、$0.10/$0.50，Haiku 4.5迁移破坏性变更（budget_tokens返回400、默认自适应思考） | https://platform.claude.com/docs/en/release-notes/api
- 2026-10-08 | Sonnet 5.5 prompt cache读取价降至$0.10/百万token | https://platform.claude.com/docs/en/release-notes/api
- 2026-10-08 | Anthropic SDK上线browser use/computer use工具beta基类 | https://platform.claude.com/docs/en/release-notes/api
- 2026-10-08 | Claude Managed Agents收紧网络：allowed_hosts约束web工具、web_fetch仅限会话已出现URL | https://platform.claude.com/docs/en/release-notes/api

- 2026-10-07 | 【续报】GitSpawn：Claude Code v2.1.292修复沙箱命令读取/ultrareview上传暂存文件副本（未点名GitSpawn） | https://code.claude.com/docs/en/changelog
- 2026-10-07 | Claude Code发布v2.1.292：Agent工具effort参数、plugin install --marketplace、mods新事件、修复subagent permissionMode auto与PreToolUse hook UNC路径绕过 | https://code.claude.com/docs/en/changelog
- 2026-10-07 | GitHub Copilot CLI v1.0.93-0至-4预发布：/sandbox与--sandbox向全部用户开放、MCP配置变更下一轮生效、企业托管域名边界 | https://github.com/github/copilot-cli/releases

- 2026-10-06 | Claude Code发布v2.1.290：Mods hook新增serverToolUses与tool.check agentId/ceiling，修复WebFetch静默截断10万字符后文本、plan mode误批非只读connector工具等 | https://code.claude.com/docs/en/changelog
- 2026-10-06 | Claude Code发布v2.1.291：修复2.1.290云端session丢失权限提示答复、2.1.288退出时丢失最后消息两处回归 | https://code.claude.com/docs/en/changelog
- 2026-10-06 | OpenAI Codex CLI发布rust-v0.160.1：远程stdio MCP server保留SYSTEMROOT/TEMP/TMP环境变量 | https://github.com/openai/codex/releases
- 2026-10-06 | GitHub Copilot CLI v1.0.92转正式版：copilot config子命令、本地/云端环境选择器、shell输出实时流式、沙箱shell默认不带GitHub token | https://github.com/github/copilot-cli/releases

- 2026-10-05 | GitHub Copilot CLI发布v1.0.92-4预发布：copilot config子命令、MCP并发连接提速与挂起修复、沙箱权限修复 | https://github.com/github/copilot-cli/releases/tag/v1.0.92-4
- 2026-10-05 | 【单源】Show HN Pi pod：在自有服务器沙箱运行Pi编码agent，自托管隐私向 | https://news.ycombinator.com/item?id=49937304

## 3. 进行中事件表

- 事件：GitSpawn（git-config触发code execution，波及多款编码agent）剩余未修复情况；最后进展日期：2026-10-10（本期10/13-10/19窗口内无新增官方安全公告，Claude Code v2.1.299-303更新日志未点名GitSpawn，xAI对Grok Build仍无正式安全公告）；下一步关注点：Anthropic或xAI是否发布正式CVE或安全公告说明最终闭环。
- 事件：OpenCode Console 第三方 AI 供应商密钥泄露事件后续；最后进展日期：2026-10-16（OpenCode披露旧版系统入侵致约1.4% Console用户托管的OpenAI/Anthropic/Google API key潜在暴露并启动吊销）；下一步关注点：OpenCode是否发布详细事后取证报告（post-mortem）及密钥加密存储架构改造方案。
