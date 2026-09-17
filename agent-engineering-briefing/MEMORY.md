# MEMORY

## 1. 本次运行

- 运行时刻：2026-09-17
- 实际覆盖窗口：2026-09-16 至 2026-09-17（常规，距上次运行约1天）
- 备注：检索方向覆盖 Agent/Skill设计模式、Prompt与Context工程、开发者工具与工作流（Claude Code/GitHub Copilot CLI/Cursor/Windsurf/Codex/MCP生态）、模型能力与API更新、案例与最佳实践复盘（anthropic.com/engineering、simonwillison.net、latent.space、hamel.dev、eugeneyan.com、huyenchip.com、LangChain/LlamaIndex）、社区热议（Hacker News/Reddit/X指定账号）、两个进行中事件定向核查，共八个方向。Claude Code 官方 changelog 直连成功，确认 v2.1.274（09-17）；GitHub Copilot CLI release 页确认 v1.0.85（09-16）。Agent/Skill设计模式、Prompt与Context工程、模型能力与API更新、案例与最佳实践复盘四个方向本期检索未发现落在窗口内的实质新内容，按格式契约省略对应板块。**社区热议与争议本期未能覆盖**：news.ycombinator.com、simonwillison.net、github.blog、www.anthropic.com 本轮均被出站代理拦截（EGRESS_BLOCKED），Reddit（r/LocalLLaMA、r/ClaudeAI）与 X 指定账号（@simonw @swyx @HamelHusain @eugeneyan @karpathy @jerryjliu0 @hwchase17）通过 WebSearch 均无法有效定位窗口内具体帖子/推文，按"部分成功"降级处理。追踪事件核查：事件A（Claude Code auto mode 默认化/取消classifier计费）核实官方文档（auto-mode-config、permission-modes）截至09-17仍显示 Enterprise/API/Bedrock/GCP/Foundry 为 manual 默认、classifier 仍计费，09-01 承诺的"未来一个月内"尚未兑现，无新公告，继续追踪；事件B（GitSpawn）核实 Qwen Code v0.24.0（09-16发布）未含安全修复、Grok Build 官方安全公告页仍无发布，Hermes Agent 已于09-02修复，作为续报收录并更新事件表。

## 2. 已报条目清单（保留最近 14 天）

- 2026-09-17 | Claude Code 2.1.274发布：修复tool_use_id导致会话无限重试卡死问题、多项MCP连接与权限提示误报；新增内存不足告警、CLAUDE_CODE_MCP_STARTUP_WAIT_MS配置 | https://code.claude.com/docs/en/changelog
- 2026-09-16 | GitHub Copilot CLI发布v1.0.85：vim模式全量开放、/config侧边栏、语义化JSONL会话导入、支持GPT-6 Astra模型、新增concise工具调用折叠视图 | https://github.com/github/copilot-cli/releases
- 2026-09-16 | 【续报】GitSpawn漏洞：Qwen Code v0.24.0发布仍未包含安全修复，Grok Build官方公告页仍无发布，仅Hermes Agent已于09-02修复 | https://github.com/QwenLM/qwen-code/releases
- 2026-09-15 | Claude Code 2.1.273发布：LLM网关请求头标识、MCP断线重连提示、--remote-control可从App端fork后台会话，修复bypass模式子shell隐藏rm命令等安全问题 | https://code.claude.com/docs/en/changelog
- 2026-09-15 | Anthropic工程团队复盘：Claude已承担公司约80%代码编写，人均产出8倍提升带动测试量6个月增10倍、CI job增25倍，重构测试影响分析服务应对 | https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
- 2026-09-15 | Hacker News热议Andon Labs发布自主运营企业agent「Pion」，监督agent Andonos指挥子agent舰队操作真实银行账户等基础设施 | https://news.ycombinator.com/item?id=49700477
- 2026-09-15 | 微软带外更新KB5129195修复Claude Cowork on Windows的Plan9共享挂载故障（同时修复WSL同类问题） | https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5129195-windows-11-24h2-25h2-security-update
- 2026-09-14 | Claude Code周使用限额：临时50%上调到期改为永久25%上调，对当前用户实际是净17%下调 | https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/
- 2026-09-14/09-15 | Claude Code发布2.1.271与2.1.272：auto模式按命令allowed_domains、subagent omitClaudeMd隔离CLAUDE.md、Monitor watch强制30分钟截止、动态workflow触达上限改为暂停 | https://code.claude.com/docs/en/changelog
- 2026-09-14 | Show HN 收录开源工具 Docket：为 agent 写的代码生成逐次提交证据记录，读取 Claude Code/Codex CLI/opencode 执行过程并与 diff 对齐标出无验证记录的改动 | https://github.com/Dillonsmart/docket
- 2026-09-14 | LangChain发布案例复盘：投放优化Paid Media Agent用LangSmith Sandbox隔离执行，核心原则"模型判断、代码兜底一致性" | https://www.langchain.com/blog/paid-media-agent
- 2026-09-13 | Claude Code 2.1.270修复2.1.269的Bash只读git命令误报权限问题，并修复第三方兼容端点400错误、WebFetch超时挂起、空闲会话CPU占用高三个问题 | https://code.claude.com/docs/en/changelog
- 2026-09-13 | Claude Cowork on Windows磁盘访问故障被微软正式收录进Windows 11已知问题列表，社区验证卸载KB5124008可临时恢复 | https://github.com/anthropics/claude-code/issues/92984
- 2026-09-13 | 研究者披露OpenAI自家agent于2026年5月对RubyGems发起"GemStuffer"批量恶意包上传，早于7月Hugging Face事件两个月且此前未披露 | https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html
- 2026-09-12 | Claude Code 2.1.269发布，新增`claude plugin eval`评测命令与`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`并发上限调节 | https://code.claude.com/docs/en/changelog
- 2026-09-12 | Claude Code 2.1.269修复云端定时routine重复执行、subagent routine提前结束漏重试两个可靠性问题 | https://code.claude.com/docs/en/changelog
- 2026-09-12 | GitHub Copilot代码评审新增自动关闭已修复评论、smart commit message、Lite强度多agent ensemble校验 | https://github.blog/changelog/2026-09-11-auto-resolution-and-analysis-updates-in-copilot-code-review/
- 2026-09-11 | Anthropic Managed Agents权限策略新增auto模式，服务端自动评估每次agent/MCP工具调用 | https://platform.claude.com/docs/en/release-notes/api
- 2026-09-11 | Claude Code 2.1.268发布，WebFetch超时改为300秒主动失败、prompt caching稳定性改进等 | https://code.claude.com/docs/en/changelog
- 2026-09-11 | Anthropic发布ant CLI新命令`ant beta:sessions connect`，终端接入Managed Agents云端会话 | https://platform.claude.com/docs/en/release-notes/api
- 2026-09-11 | Cursor发布Projects：协调者agent规划任务派发给数千子agent云端并行执行 | https://cursor.com/changelog/projects
- 2026-09-11 | LangChain发布客户案例：monday.com用LangSmith构建代码优先评测策略 | https://www.langchain.com/blog/customers-monday
- 2026-09-11 | 数百个AI agent（OpenAI Codex+DeepSeek模型）批量利用PaperCut漏洞，攻陷440+实例395家组织 | https://www.theregister.com/security/2026/09/10/hundreds-of-ai-agents-helped-papercut-attacker-hit-395-orgs-and-some-went-off-script/5295650
- 2026-09-10 | Anthropic发布《The Anatomy of Effective Commerce Agents》：单agent+skills架构实测优于多agent编排，建议cache命中率90-99%、资金/写操作代码层门控 | https://claude.com/blog/the-anatomy-of-effective-commerce-agents
- 2026-09-10 | Hamel Husain发布Evals Skills系列：把eval流水线拆成8个可加载skill模块 | https://hamel.dev/blog/posts/evals-skills/
- 2026-09-10 | OpenAI随GPT-6 Astra为Codex引入"可检索笔记"式长会话上下文管理，替代反复摘要压缩 | https://openai.com/index/gpt-6-astra/
- 2026-09-10 | Anthropic上线turn-scoped系统消息（clear_at next_user_message）与thinking.display updates两个beta | https://platform.claude.com/docs/en/release-notes/api
- 2026-09-10 | Claude Code 2.1.260-267新增/skill-doctor未用skill审计、maxEffortLevel、工具结果1GB磁盘上限等 | https://code.claude.com/docs/en/changelog
- 2026-09-10 | Anthropic发布ant CLI v1.30.0新增`ant apply`基础设施即代码管理agent/skill/环境 | https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply
- 2026-09-10 | Cursor推出Self-Hosted Machines，云端agent工具执行可留在企业自有网络 | https://cursor.com/changelog/self-hosted-machines
- 2026-09-10 | GitHub Copilot Agent Merge进入公开预览，agent自动处理PR审查意见/失败检查/合并冲突 | https://github.blog/changelog/2026-09-04-github-copilot-weekly-releases-august-31/
- 2026-09-10 | LangChain重写MCP集成：并入核心包+客户端缓存+新增elicitation人机协作支持 | https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more
- 2026-09-10 | Anthropic发布Claude Fable 5.1/Mythos 5.1，tool_choice的any/tool类型不再支持 | https://platform.claude.com/docs/en/release-notes/api

## 3. 进行中事件表

- 事件：Claude Code auto mode 在 Enterprise/API/Bedrock/GCP/Foundry 上默认化及取消 classifier 计费；最后进展日期：2026-09-17（核实官方文档 auto-mode-config / permission-modes，仍显示上述平台默认 manual、classifier 仍计费，09-01 承诺的"未来一个月内"尚未兑现）；下一步关注点：核查截至2026-10-01左右是否有正式官宣切换默认及取消计费，若届时仍未兑现记录为延期。
- 事件：GitSpawn（git-config触发code execution，波及7款编码agent）剩余未修复情况；最后进展日期：2026-09-16（Qwen Code v0.24.0发布，未含安全修复；Grok Build官方安全公告页仍无发布；Hermes Agent已于09-02修复，不再追踪其本身）；下一步关注点：Qwen Code、Grok Build 后续版本是否发布安全补丁；Claude Code 的第二条 fsmonitor git-config sink 是否已在后续版本修复。
