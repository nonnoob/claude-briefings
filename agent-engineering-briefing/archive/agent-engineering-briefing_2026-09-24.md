# 🛠️ AI Agent 工程简报 · 2026-09-24

> 覆盖窗口：2026-09-23 至 2026-09-24（常规）

## 开发者工具与工作流

- Claude Code发布v2.1.281，约130项改动：`claude plugin validate`新增MCP server校验、auto mode服务端分类器审核范围扩大到只读shell命令、危险rm操作现需等待2分钟才会自动拒绝确认（可关闭）、系统提示词改为通过私有文件传递而非命令行文本（`--system-prompt-file`替代`--system-prompt`，为breaking change）。用自建runner/CI跑Claude Code或依赖auto mode做无人值守自动化的团队需要检查脚本兼容性，并重新评估会被新规则拦截的命令范围。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- Anthropic上线Claude Marketplace，统一入口聚合2000+ connector/plugin及Atlassian、Google、Microsoft、Notion、Salesforce、Cursor、Snowflake等合作伙伴产品，明确上架标准为公开的MCP协议与Agent Skills规范。计划发布自研MCP server或skill的工程师现在有了官方分发入口，值得关注提交与审核路径。来源：Claude Blog https://claude.com/blog/claude-marketplace
- GitHub Copilot CLI发布v1.0.89-1预发布，新增GPT-6 Sol/GPT-6 Luna模型支持并修复view工具行范围处理问题。用Copilot CLI编排agent任务的工程师可评估新模型的推理/成本特性是否需要调整默认模型选择。来源：GitHub Releases https://github.com/github/copilot-cli/releases
- OpenAI Codex CLI发布v0.156.1稳定版，模型选择器新增GPT-6 Sol/GPT-6 Luna，触发限流时的兜底切换模型也改为GPT-6 Luna。依赖Codex CLI限流自动降级策略的工程师需要同步更新对兜底模型能力的预期。来源：GitHub Releases https://github.com/openai/codex/releases
- OpenHands Enterprise发布0.70.0：新增组织级共享Secrets、用户预算/用量仪表盘，以及MCP服务器的OAuth认证支持（含GitLab、Atlassian Rovo）。此前接入企业级MCP服务器往往要手工传token，这个特性大幅简化了多租户场景下的MCP授权管理。来源：OpenHands Docs https://docs.openhands.dev/enterprise/release-notes/0.70.0

## 案例与最佳实践复盘

- Anthropic前线部署工程师团队发布代码现代化项目方法论：六步流程（定义目标、建立"certificate"验收标准、设定晋级策略、准备前提条件、构建agentic workflow、小范围验证后规模化），核心论点是agent加速了改代码本身，但瓶颈转移到了组织如何围绕变更动员。为设计大规模多agent并行代码迁移workflow的工程师提供了可直接复用的"目标/验收标准/晋级策略"框架。来源：Claude Blog https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects

## 社区热议与争议

- 【续报】【单源】极简agent架构实现"Jev in 25 Lines of Python"引发Hacker News热议（约636赞/200评论），社区就"决策器与LLM分离的极简架构能否撑起生产级可靠性"展开路线之争，另有热帖讨论OpenAI能否凭借平台优势快速跟进复制该模式。想验证轻量级agent架构是否适合生产环境的工程师可参考讨论中的正反论据。来源：Hacker News https://news.ycombinator.com/item?id=49812769
- 【单源】Hacker News热议"一旦能衡量Claude做的事，就能让它更快"：讨论给agent设定可量化基准后使其持续自我优化代码性能的工程方法论。为设计agent自优化/自迭代workflow的工程师提供了"先建立可测量基准再放手让agent迭代"的思路。来源：Hacker News https://news.ycombinator.com/item?id=49821196
- 【续报】【单源】Claude Code被发现存在仅在遥测开关打开时才读取AGENTS.md配置文件的bug（现已修复），Hacker News热议约460赞/261评论，延续此前AGENTS.md标准化的讨论热度。依赖AGENTS.md做团队级agent配置标准化的工程师应确认自己的Claude Code版本已包含该修复，避免配置静默失效。来源：Hacker News https://news.ycombinator.com/item?id=49814947
