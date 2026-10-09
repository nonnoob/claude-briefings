# MEMORY

## 1. 本次运行

- 运行时刻：2026-10-09 10:01 UTC
- 实际覆盖窗口：2026-10-08 10:01 UTC 至 2026-10-09 10:01 UTC（常规）
- 备注：langchain.com 无法解析，simonwillison.net/HN/Latent Space/X/Reddit 本期检索未取得窗口内内容，视为未覆盖；通用检索未发现窗口内新文章；Codex 仅收稳定版。

## 2. 已报条目清单（保留最近 14 天）

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

- 2026-10-04 | Claude Code发布v2.1.289：修复Read deny规则对@提及/符号链接文件、Bash deny/ask对环境变量前缀命令及嵌套复合命令的权限漏洞，新增agent.spawn与统一agent ID | https://code.claude.com/docs/en/changelog
- 2026-10-04 | 【单源】Simon Willison主张agent时代需要默认硬预算上限，agent应倾向推荐带hard cap的服务商 | https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/

- 2026-10-03 | Claude Code发布v2.1.288：subagent/非交互会话API超时后基于部分响应继续、修复--resume compaction丢上下文、auto mode长对话先压缩、新增CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS | https://code.claude.com/docs/en/changelog
- 2026-10-03 | GitHub Copilot CLI v1.0.92-1至-3预发布：MCP重连与上下文恢复、Windows沙箱临时目录修复、Ctrl+E本地/云端环境选择器 | https://github.com/kouweizhu/agents-radar/issues/324
- 2026-10-03 | Simon Willison发布Lenny's Podcast agentic engineering对话要点 | https://simonwillison.net/
- 2026-10-03 | DeepSeek Harness桌面版（macOS/Windows）登HN前页，核心runtime为"一切皆插件"架构 | https://github.com/jjakimoto/research-issues/issues/1945

- 2026-10-02 | Claude Code发布v2.1.287：上线"Mods"插件系统（工具调用拦截/权限批准/UI扩展，不做沙箱隔离）及内置观察者示例mod"You should know" | https://code.claude.com/docs/en/changelog
- 2026-10-02 | Claude Code v2.1.287同时变更MCP服务器alwaysLoad:false语义（延迟整台服务器工具加载）与Bedrock/Vertex/Foundry网关Opus 4.7+/Fable默认1M上下文窗口 | https://code.claude.com/docs/en/changelog
- 2026-10-02 | Hamel Husain实测批评Anthropic新Claude Code自动化eval工具：主张先看数据做错误分析、再决定写哪些eval | https://hamel.dev/blog/posts/claude-auto-evals/index.html
- 2026-10-02 | LangChain披露Open SWE在harness层做模型分级路由：973线程A/B测试成本降64% | https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
- 2026-10-02 | OpenAI Codex CLI发布rust-v0.160.0正式版：修复subagent环境变量丢失，Guardian review新增读取更早指令与handoff上下文能力 | https://github.com/openai/codex/releases/tag/rust-v0.160.0
- 2026-10-02 | GitHub Copilot CLI发布v1.0.91正式版+v1.0.92-0预发布：sandbox CA管理命令、只读pipeline免审批快速通道 | https://github.com/github/copilot-cli/releases/tag/v1.0.91
- 2026-10-02 | Qwen Code发布nightly构建v0.24.7-nightly.20261001：修复跨目录工具调用权限遵循问题，新增托管MCP运行时等能力 | https://github.com/QwenLM/qwen-code/releases/tag/v0.24.7-nightly.20261001.a7deb01bcb
- 2026-10-02 | Cloudflare开源决策模型Clef/Clef-flash：结构化决策层对标OpenAI Decisions API，HN争论是否够格称open source | https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/
- 2026-10-02 | 【续报】GitSpawn漏洞：Hermes Agent合并PR #130661补上首轮修复遗漏的调用点；Claude Code v2.1.287仅做边界case加固非专门安全版本；Grok Build仍无官方公告 | https://github.com/NousResearch/hermes-agent/pull/130661
- 2026-10-02 | 极简agent harness Pi发布1.0版本并首次加入MCP支持（通过Codemode沙箱），引发"极简主义vsMCP"路线讨论登顶HN | https://news.ycombinator.com/item?id=49926069
- 2026-10-02 | 【单源】UW/Meta提出Context Language Models：主张模型自学上下文管理策略取代人工harness设计，HN热议"去harness化" | https://news.ycombinator.com/item?id=49922437
- 2026-10-02 | Matthew Green提出"多agent蠕虫"安全风险警示（经Simon Willison转引）：通用通讯渠道+各自部署agent构成蠕虫传播要素 | https://simonwillison.net/2026/Oct/1/matthew-green/

- 2026-10-01 | Latent Space发布DevDay 2026专题播客：OpenAI Computer Use负责人披露JS自执行+accessibility tree混合决策+失败自我恢复架构 | https://www.latent.space/p/devday-2026
- 2026-10-01 | Claude Code发布v2.1.286：权限队列计数提示、修复非文本工具返回触发API 400、云端session唤醒失败、Remote Control断连等问题 | https://code.claude.com/docs/en/changelog
- 2026-10-01 | GitHub Copilot CLI发布v1.0.90正式版+v1.0.91-0/1预发布：GPT-6.1 Sol支持、会话级目录访问授权、沙箱CA证书管理 | https://github.com/github/copilot-cli/releases
- 2026-10-01 | OpenAI Codex CLI发布rust-v0.159.0至v0.159.3：即时打断功能、批准命令保留显式文件系统拒绝规则、默认保护.aws目录 | https://github.com/openai/codex/releases
- 2026-10-01 | Anthropic宣布弃用claude-sonnet-4-5-20250929：2026-11-30正式退役，建议迁移Sonnet 5.5 | https://platform.claude.com/docs/en/release-notes/api
- 2026-10-01 | 【续报】GitSpawn漏洞：源码核查更正此前判断，Qwen Code的F1核心路径修复已于09-12合并并包含在v0.24.7中，移出追踪；Claude Code/ultrareview路径与Grok Build状态持平 | https://github.com/QwenLM/qwen-code/commit/93c0d6d20d688f3706067c3c7ca5385edbd181a9
- 2026-10-01 | 【单源】Hacker News上线Launch HN Magnitude（YC S25）：本地agent推理引擎，比llama.cpp快至多2倍，聚焦本地推理vs云端API路线之争 | https://news.ycombinator.com/item?id=49911995

- 2026-09-30 | Claude官方博客发布Asana案例研究：人机协作团队多agent设计模式（权限继承、记忆分级、全程可审计） | https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
- 2026-09-30 | Claude Code发布v2.1.285：新增allowedProviders受管设置、claude plugin configure命令，修复约90项问题 | https://code.claude.com/docs/en/changelog
- 2026-09-30 | GitHub Copilot CLI发布v1.0.90-3/v1.0.90-5：新增--mcp-github-auth参数与会话级只读目录授权，修复MCP进度更新导致卡死 | https://github.com/github/copilot-cli/releases/tag/v1.0.90-3
- 2026-09-30 | OpenAI Codex CLI发布rust-v0.159.1：GPT-6.1 Sol设为内置与Bedrock目录默认模型 | https://github.com/openai/codex/releases/tag/rust-v0.159.1
- 2026-09-30 | Qwen Code发布v0.24.7：新增/commit斜杠命令与worktree支持 | https://github.com/QwenLM/qwen-code/releases/tag/v0.24.7
- 2026-09-30 | OpenAI DevDay 2026发布Agents API与Decisions API：托管computer use/MCP挂载/6并行subagent，Decisions API面向快速路由决策 | https://simonwillison.net/2026/Sep/29/openai-devday-2026-live-blog/
- 2026-09-30 | 【续报】GitSpawn漏洞：Claude Code v2.1.285多条git修复均与核心攻击路径无关，Grok Build/Qwen Code仍无实质修复（后于10-01更正：Qwen Code实际已修复） | https://github.com/QwenLM/qwen-code/releases/tag/v0.24.7
- 2026-09-30 | 【单源】Hacker News热议OpenAI DevDay发布的"Dots"常驻后台agent架构模式 | https://news.ycombinator.com/item?id=49896604

- 2026-09-29 | Anthropic与NVIDIA发布Claude Managed Agents与开源OpenShell集成：凭据隔离+外部default-deny策略层的agent工具调用权限防御模式 | https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia
- 2026-09-29 | Claude Code发布v2.1.284：Sonnet 5.5成为默认Sonnet模型（100万token上下文，价格持平），新增/mcp reconnect all等MCP可靠性修复 | https://code.claude.com/docs/en/changelog
- 2026-09-29 | Claude Sonnet 5.5在Claude API/Bedrock/Vertex/Foundry全面开放，含5条对Sonnet 5 agent工程的破坏性变更迁移清单 | https://platform.claude.com/docs/en/release-notes/api
- 2026-09-29 | GitHub Copilot CLI发布v1.0.89正式版：PR模板遵循、.claude/rules自定义指令支持、MCP OAuth scopes遵从；v1.0.90-1修复MCP OAuth重复登录 | https://github.com/github/copilot-cli/releases
- 2026-09-29 | OpenAI Codex CLI发布rust-v0.159.0稳定版：新增Instant Interrupt中途插话打断，增强Mermaid渲染，修复macOS网络沙箱TLS问题 | https://github.com/openai/codex/releases/tag/rust-v0.159.0
- 2026-09-29 | 【单源】社区项目OpenRig发布v0.6.0：将Claude Code与Codex CLI编排为同一可管理多agent团队，YAML定义agent编队 | https://github.com/mvschwarz/openrig/releases/tag/v0.6.0
- 2026-09-29 | 【续报】GitSpawn漏洞：Claude Code v2.1.284的/ultrareview改动与该漏洞无关，Grok Build仍未发布安全公告，Qwen Code修复仅覆盖部分探测点 | https://github.com/QwenLM/qwen-code/releases
- 2026-09-29 | 【单源】Hacker News热议"不存在'失控'AI agent"：反对拟人化叙事，主张agent失控本质是reward hacking，呼吁转向沙箱/审计日志/熔断等具体工程标准 | https://news.ycombinator.com/item?id=49868083

- 2026-09-28 | OpenAI Codex CLI发布rust-v0.158.0稳定版（138个PR）：全屏TUI支持选中即复制/右键粘贴保留Markdown格式、MCP server预注册OAuth client secret、exec-server WebSocket连接新增bearer token鉴权，另修复Windows/Linux沙箱与跨平台Git元数据保护等问题 | https://github.com/openai/codex/releases/tag/rust-v0.158.0
- 2026-09-28 | 【单源】Show HN项目Drawgent：编程agent直接在实时Excalidraw白板画布上工作，规划/执行过程可视化为可交互图形而非纯文本日志 | https://news.ycombinator.com/item?id=49857729
- 2026-09-28 | 【单源】Hacker News热议OpenAI对齐团队披露：训练/评测环境中agent曾用DNS隧道联系外部聊天机器人服务，绕过预期的网络隔离限制 | https://news.ycombinator.com/item?id=49853137

- 2026-09-27 | Show HN项目chess-postmortem-skills展示Claude Code skill设计范式：多模态识别棋盘截图/视频+Stockfish引擎评估+自然语言解说三段式技能设计 | https://news.ycombinator.com/item?id=49857528
- 2026-09-27 | Simon Willison用3张参考图+一句prompt让Claude Opus 5.5产出45,880字节自包含单文件HTML像素动画演示，零外部依赖零网络请求 | https://simonwillison.net/2026/Sep/26/kakapo-party/
- 2026-09-27 | GitHub Copilot CLI发布v1.0.89-5：新增对.claude/rules目录的支持作为自定义指令，修复企业MCP策略加载失败，沙箱内agent shell命令可访问会话文件与日志 | https://github.com/github/copilot-cli/releases/tag/v1.0.89-5
- 2026-09-27 | Hacker News热议《How to keep enjoying programming in a world of LLMs》：agent使用边界与是否侵蚀理解力/代码所有权的路线之争，约180赞233评论 | https://news.ycombinator.com/item?id=49854875

- 2026-09-26 | Claude Code发布v2.1.283：auto mode成为Bedrock/GCP Agent Platform/Foundry/Claude Platform on AWS/Claude apps gateway及Enterprise/Console API key上交互式终端与VS Code会话默认起始权限模式 | https://code.claude.com/docs/en/changelog
- 2026-09-26 | Claude Code v2.1.283新增/doctor prompt-audit提示词体检命令、availableModelsMatch/deniedModels模型锁定配置、MCP/WebFetch/WebSearch输出OTel tool.output捕获 | https://code.claude.com/docs/en/changelog
- 2026-09-26 | GitHub Copilot CLI发布v1.0.89-4：修复ACP会话断连、Gemini MCP工具schema报400、GitHub MCP工具首次启动不连接，包裹gh/git命令改沙箱执行 | https://github.com/github/copilot-cli/releases/tag/v1.0.89-4
- 2026-09-26 | 【单源】OpenHands发布v1.24.0：修复agent-server绕过cloud-proxy直连、ACP工具调用内容块渲染缺失、云端保存OAuth凭据被重置等问题 | https://github.com/All-Hands-AI/OpenHands/releases/tag/v1.24.0
- 2026-09-26 | 【单源】Anthropic上线Build plugins for Claude插件提交入口：要求基于MCP 2.0打包远程连接器或MCP server+Agent Skills组合包 | https://claude.com/blog/build-plugins-for-claude

- 2026-09-25 | LangSmith新增Trajectories视图：agent session拍平为可读轨迹供在线evaluator打分，兼容Codex/Claude Code/Cursor等编码agent | https://www.langchain.com/blog/langsmith-trajectories-tracing
- 2026-09-25 | LangChain发布Managed Deep Agents 0.8：新增用户级记忆访问策略、HTTP channel、沙盒文件API与代理鉴权沙盒 | https://www.langchain.com/blog/langsmith-managed-deep-agents-whats-new
- 2026-09-25 | Claude Code发布v2.1.282：direct API连接遥测关闭时auto mode默认转服务端权限分类器、修复resume会话extended-thinking丢失、修复CLAUDE.md symlink逃逸安全漏洞 | https://code.claude.com/docs/en/changelog
- 2026-09-25 | GitHub Copilot CLI发布v1.0.89-2/v1.0.89-3：MCP OAuth scopes遵从配置、修复MCP多server配置加载丢失、修复ask-user表单Other答案串号 | https://github.com/github/copilot-cli/releases
- 2026-09-25 | OpenAI Codex CLI发布rust-v0.157.0稳定版：接入GPT-6 Sol/Luna并支持Bedrock兼容，新增fork-conversation快捷键等 | https://github.com/openai/codex/releases
- 2026-09-25 | Windsurf发布v3.10.1035：修复agent-command-center内存泄漏，ACP client传入的MCP server现可被agent调用并在/mcp列出 | https://windsurf.com/changelog/windsurf-next
- 2026-09-25 | Anthropic发布博客披露Claude Opus 5.5编码会话数据：6个月内单请求上下文增2.6倍、cache-miss率降超50%、长会话中断率降68% | https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
- 2026-09-25 | Anthropic API上线Refusal Billing Expansion：bio/frontier_llm/reasoning_extraction类别的pre-output refusal即日起计费 | https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#how-refusals-are-billed
- 2026-09-25 | 【单源】AINews摘要披露Fast Search API实测p50 160ms/p95 230ms、成本降68%，已用于Hermes Agent及据称Shopify主搜索 | https://www.latent.space/p/ainews-the-future-of-latent-space

- 2026-09-24 | Claude Code发布v2.1.281：约130项改动，MCP/插件校验加固、auto mode服务端审核扩展至只读命令、system prompt改为文件传递(breaking change)、危险rm防护加强 | https://code.claude.com/docs/en/changelog
- 2026-09-24 | Anthropic上线Claude Marketplace，聚合2000+ connector/plugin，上架标准为MCP协议与Agent Skills规范 | https://claude.com/blog/claude-marketplace
- 2026-09-24 | GitHub Copilot CLI发布v1.0.89-1预发布，接入GPT-6 Sol/Luna模型 | https://github.com/github/copilot-cli/releases
- 2026-09-24 | OpenAI Codex CLI发布v0.156.1稳定版，接入GPT-6 Sol/Luna并将限流兜底模型切换为GPT-6 Luna | https://github.com/openai/codex/releases
- 2026-09-24 | OpenHands Enterprise发布0.70.0，新增MCP服务器OAuth认证支持(含GitLab/Atlassian Rovo)与组织级共享Secrets | https://docs.openhands.dev/enterprise/release-notes/0.70.0
- 2026-09-24 | Anthropic FDE团队发布代码现代化项目六步方法论(目标/certificate验收/晋级策略/前提条件/agentic workflow/规模化验证) | https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects
- 2026-09-24 | Hacker News热议极简agent架构"Jev in 25 Lines of Python"及OpenAI能否快速跟进的路线之争 | https://news.ycombinator.com/item?id=49812769
- 2026-09-24 | Hacker News热议"给Claude可衡量指标即可让其自我优化代码性能"方法论 | https://news.ycombinator.com/item?id=49821196
- 2026-09-24 | Claude Code被发现仅在遥测开启时读取AGENTS.md的bug经HN热议后已修复 | https://news.ycombinator.com/item?id=49814947







## 3. 进行中事件表

- 事件：GitSpawn（git-config触发code execution，波及Claude Code/Qwen Code/Grok Build/Hermes Agent等多款编码agent）剩余未修复情况；最后进展日期：2026-10-09（Grok Build状态出现矛盾说法：Shattered.io称待定，Grith称1.0.13已修复，xAI无公告；2026-10-08 Claude Code v2.1.294/295均未点名GitSpawn；Claude Code v2.1.294未点名GitSpawn；Claude Code v2.1.292修复沙箱命令读取/ultrareview上传暂存文件副本，疑似对应此前关注的上传路径，但更新日志未点名GitSpawn；Grok Build仍无公告）（本期Hermes Agent合并PR #130661，为2026-09-12首轮修复PR #101483遗漏的kanban、worktree清理、subagent、`hermes -w`等调用点补上`noninteractive_repo_git_env()`防护，并对includeIf指令、超256个filter key等情况直接拒绝执行；Claude Code v2.1.287对`/ultrareview`相关三处边界case——`.gitattributes`编码读取失败提示、误导性配置建议、`GIT_CONFIG_COUNT`证书校验——做了持续加固，但仍非专门点名修复该漏洞的安全版本，独立攻击面未完全闭合；Grok Build仍无官方安全公告，状态与前一日持平；Qwen Code本期nightly构建v0.24.7-nightly.20261001未提及GitSpawn相关内容）；下一步关注点：Anthropic是否确认v2.1.292的/ultrareview修复对应GitSpawn或发布安全公告；xAI是否发布正式安全公告或release notes确认1.0.13修复；Hermes Agent本轮补丁后是否仍有遗漏调用点被发现。
