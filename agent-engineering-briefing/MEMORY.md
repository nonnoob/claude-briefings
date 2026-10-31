# MEMORY

## 1. 本次运行

- 运行时刻及检索截止：2026-10-31 11:32 UTC（2026-10-31 04:32 PDT）。
- 实际覆盖窗口：2026-10-26 08:25 UTC 至 2026-10-31 11:32 UTC（常规）。
- 六方向与既有事件已检索；本期以官方 Releases 和 VS Code 更新说明为依据，收录权限边界、压缩后指令刷新、会话恢复、工作集及 Agent Host Protocol 1.0。未将未经核验的 Rust 重写性能报道当作实践案例，社区讨论与案例方向不补旧闻。
- Claude Code 目录写入限制只约束公告列出的工具，不等于系统级沙箱。Opus 4.8 fast mode 移除登记追踪；OpenCode 取证与 Kimi 权重兑现未获可靠新增，保留原进展日期。

## 2. 已报条目清单（保留最近 21 天）

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
- 2026-10-26 | Anthropic将Agent Skills标准捐赠给AAIF，OpenAI、Hugging Face、阿里同步捐出Open Responses、OpenEnv与OpenSandbox | https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation
- 2026-10-26 | LangChain提出构建企业多人共享生产级Agent的五要素Company Harness框架 | https://www.langchain.com/blog/components-building-company-harness
- 2026-10-26 | Hamel Husain发布《How To Use Decision Models for Evals》，倡导用轻量决策分类器校准阈值替代LLM自报置信度 | https://hamel.dev/blog/posts/decision-model-evals/
- 2026-10-26 | LangChain发表《Context Engineering Starts with Retrieval》，提出精确探路、大输出转存文件与子agent委读三层检索治理 | https://www.langchain.com/blog/context-engineering-starts-with-retrieval
- 2026-10-26 | OpenAI Responses API上线12小时超长Prompt Cache（ttl="12h"，写入费2.5x，同步应用于Codex与ChatGPT Work） | https://aiweekly.co/alerts/openai-adds-12-hour-prompt-cache-ttl-to-api-25x-write-cost
- 2026-10-26 | Claude Code发布v2.1.304至v2.1.310：/auto-mode-setup、safety_event遥测、MCP幂等重试限制、修复四处沙箱逃逸、云厂商Monitor工具 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-10-26 | OpenAI Codex CLI发布rust-v0.164.0：10槽位/presets、/model与/permissions内联参数配置、修复会话恢复覆盖线程设置 | https://sourceforge.net/projects/openai-codex.mirror/files/rust-v0.164.0/
- 2026-10-26 | GitHub Copilot CLI发布v1.0.100至v1.0.104（子agent原生结构化输出、assistedApprovalInstructions、ghapp插件安装）；Qwen Code发布v0.26.0（低水位线微压缩、daemon令牌持久化） | https://github.com/github/copilot-cli/releases
- 2026-10-26 | Anthropic发布API版本2026-10-21及Python SDK 2.0/TS SDK 1.0：彻底移除temperature/top_p/top_k（传参返400）、切换Bearer鉴权头 | https://docs.anthropic.com/en/release-notes/api
- 2026-10-26 | Moonshot AI发布2.8T MoE模型Kimi K3.1 Pro（1M上下文，承诺11/4开源权重）；LlamaIndex发布4B文档解析视觉模型OCRia-1 | https://simonwillison.net/2026/Oct/23/kimi-k31-pro/
- 2026-10-26 | Modal CEO Erik Bernhardsson在Latent Space复盘临时Agent沙箱（ephemeral sandboxes）爆发、快照克隆冷启动与隔离边界设计 | https://latent.space/p/modal-d/
- 2026-10-26 | 【续报】OpenCode Console密钥泄露后续：受害者遭盗刷最高逾1700美元，官方归因于大规模模型蒸馏攻击引发争议，提醒需赴模型厂商控制台手动吊销 | https://thehackernews.com/2026/10/opencode-console-breach-may-have.html
- 2026-10-26 | Kimi K3.1 Pro技术报告披露开源前主动清洗网络攻击与漏洞利用语料，引发社区关于安全对齐与自动化安全审计agent能力权衡热议 | https://simonwillison.net/2026/Oct/23/kimi-k31-pro/
- 2026-10-31 | VS Code 1.144 公布 Agent Host Protocol v1.0 与六种语言库 | https://code.visualstudio.com/updates/v1_144
- 2026-10-31 | Claude Code v2.1.311 修复压缩后规则文件过期、晚连接 MCP 工具不可见及后台后代 worktree 提前清理 | https://github.com/anthropics/claude-code/releases/tag/v2.1.311
- 2026-10-31 | Claude Code v2.1.312 阻止部分读取后覆写大指令文件，并修复切换目录后的 Skill 发现 | https://github.com/anthropics/claude-code/releases/tag/v2.1.312
- 2026-10-31 | Claude Code v2.1.314 新增工作目录外写入限制，非交互启动失败改返回退出码 1 | https://github.com/anthropics/claude-code/releases/tag/v2.1.314
- 2026-10-31 | Codex rust-v0.166.0 新增队列恢复与网络诊断，修复 resume/fork 权限和计数保留 | https://github.com/openai/codex/releases/tag/rust-v0.166.0
- 2026-10-31 | Copilot CLI v1.0.105 修复长上下文会话无法选择 Fusion High/Max | https://github.com/github/copilot-cli/releases/tag/v1.0.105
- 2026-10-31 | VS Code 1.144 实验性 Keep/Undo 工作集不涵盖终端命令改动 | https://code.visualstudio.com/updates/v1_144
- 2026-10-31 | Claude Code v2.1.316 公告 Opus 4.8 fast mode 将于 11 月 30 日移除且无自动回退 | https://github.com/anthropics/claude-code/releases/tag/v2.1.316

## 3. 进行中事件表

- 事件：OpenCode Console 第三方 AI 供应商密钥泄露事件后续；最后进展日期：2026-10-20（受害开发者出现数百至逾 1700 美元异常盗刷账单，OpenCode 将攻击归因于黑客利用被盗密钥抓取前沿模型输出进行"大规模蒸馏攻击"引发安全圈质疑，并提醒在 Console 界面删除密钥不会在模型厂商侧自动吊销）；下一步关注点：OpenCode 是否发布详细事后取证报告（post-mortem）及密钥加密存储架构改造方案。
- 事件：Kimi K3.1 Pro 完整模型权重开源兑现与编码 agent 实测；最后进展日期：2026-10-23（Moonshot AI 发布 2.8T 参数 MoE 模型 Kimi K3.1 Pro API 并承诺于 2026-11-04 开放完整模型权重）；下一步关注点：11 月 4 日是否如期发布完整开源权重、具体开源许可证条款及社区本地/私有云编码 agent 实测表现。
- 事件：Opus 4.8 fast mode 停用；最后进展日期：2026-10-31（v2.1.316 公告，弃用日 10 月 30 日）；下一步关注点：11 月 30 日移除前核对仍固定旧模式的客户端与任务，并确认不支持请求的报错处理及迁移公告。
