# 🛠️ AI Agent 工程简报 · 2026-10-02

> 覆盖窗口：2026-10-01 10:01 UTC 至 2026-10-02 10:00 UTC（常规）

## Agent/Skill 设计模式

- Claude Code v2.1.287上线"Mods"系统：允许TypeScript事件处理器在工具调用前后介入，拦截/改写prompt、批准或拒绝权限请求、从工具输出中redact密钥、新增UI面板，通过`/plugin`安装，在CLI/VSCode/`-p`模式/Agent SDK/云端session均生效；官方明确该机制不做沙箱隔离、与用户本人同权限，企业托管部署会强制最先加载内置`sec-default` mod防止插件绕过组织策略。为agent运行时装可插拔的拦截/审查层提供了官方范式，但引入插件即引入同等权限的攻击面，生产环境装载前务必审查来源。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- 同版本内置示例mod"You should know"：一个旁路的side agent在主agent工作期间同步观察session，标记用户或Claude本身可能忽略的问题，是官方对"观察者/评审agent"编排模式的一次产品化示范，可直接参考用于自建多agent评审流水线。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- Hamel Husain与Isaac Flath实测Anthropic新的Claude Code自动化eval工具（build_eval+hill-climb），用公寓租赁助手真实对话轨迹发现该工具会诱导用户"先写eval再看数据"，但正确顺序应该是先做错误分析（error analysis）看数据、再决定该写哪些eval，自动化只能辅助发现问题、不能替代人工判断哪些failure值得关注。给打算用自动化工具搭eval pipeline的团队一个具体的顺序纠偏。来源：Hamel Husain's Blog https://hamel.dev/blog/posts/claude-auto-evals/index.html
- LangChain披露在coding agent（Open SWE）的harness层（而非gateway层）做逐步骤模型分级路由的做法：973个线程A/B测试显示median成本从$2.61降到$0.94（降64%），质量无可测量下降，核心论点是"有效的路由器必须活在harness里，因为路由本质上是domain-specific的"。给正在做多模型成本优化的团队一个具体可复现的架构选址参考。来源：LangChain Blog https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness

## Prompt 与 Context 工程

- 【单源】Claude Code v2.1.287变更MCP服务器`alwaysLoad:false`语义：改为延迟该服务器全部工具直到tool search命中才加载，而非此前的局部/不同粒度行为，是管理大型MCP工具集上下文占用的直接可调参数。接入多个MCP服务器的项目可借此重新评估哪些服务器该标记为非常驻。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- 【单源】Claude Code v2.1.287将Bedrock/Vertex/Foundry及Claude apps gateway上Opus 4.7+与Fable的默认上下文窗口改为1M tokens，取消此前需显式`[1m]`后缀才能启用的要求（`CLAUDE_CODE_DISABLE_1M_CONTEXT=1`可退回200K）。长上下文架构不再需要手动申请即可拿到1M窗口，但也意味着托管网关上的默认成本/延迟基线发生变化，需重新评估预算。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog

## 开发者工具与工作流

- OpenAI Codex CLI发布rust-v0.160.0正式版（49个PR）：修复subagent启动时环境变量丢失问题、Guardian review新增读取更早用户指令与agent handoff上下文的能力，另修复SQLite连接/日志初始化卡死、Windows sandbox下PowerShell回退与长路径权限问题。子agent编排可靠性与审查类prompt可用的上下文窗口都直接受益。来源：OpenAI Codex CLI Releases https://github.com/openai/codex/releases/tag/rust-v0.160.0
- GitHub Copilot CLI发布v1.0.91正式版+v1.0.92-0预发布：新增`copilot sandbox ca`系列命令管理代理CA信任；完整且可静态分析的只读shell pipeline现可进入免人工批准的"execution-evidence review"快速通道，不完整/未绑定的pipeline仍需显式批准；修复MCP工具在OAuth重新认证后、工具定义未变时仍失效的问题。设计只读探测类工具时让pipeline保持无歧义、无未绑定重定向，就能吃到这个审批快速路径。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases/tag/v1.0.91
- 【单源】Qwen Code发布nightly构建v0.24.7-nightly.20261001（53个PR）：修复跨目录工具调用未正确遵循已批准权限的问题、完成租户级403访问控制契约，同时新增本地workspace-agent协作、持久化远程shell结果投递、托管MCP运行时等能力。若skill设计依赖"跨目录工具调用"的权限边界，升级后行为会变化，需要重新测试。来源：GitHub https://github.com/QwenLM/qwen-code/releases/tag/v0.24.7-nightly.20261001.a7deb01bcb

## 模型能力与 API 更新

- Cloudflare开源决策模型Clef（27B）与Clef-flash（9B）：不生成文本，而是对结构化问题直接返回带类型的概率分布，定位为agent工程中专门处理"选下一步动作"的决策层，对标OpenAI Decisions API与Amazon Strands Decider。HN讨论随即指出训练数据与pipeline未公开，严格说是open weights而非可复现的open source，也有评论认为小型分类器本地训练即可替代、无需额外网络请求。想在agent里拆出专门决策层之前，先看这场"够不够格叫open source"的争论。来源：Cloudflare Changelog https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/

## 案例与最佳实践复盘

- 【续报】GitSpawn漏洞（git-config触发code execution，波及Claude Code/Qwen Code/Grok Build/Hermes Agent等多款编码agent）：Hermes Agent合并PR #130661，为9月首轮修复（PR #101483）遗漏的kanban、worktree清理、subagent、`hermes -w`等调用点补上`noninteractive_repo_git_env()`防护，并对includeIf指令、超256个filter key等情况直接拒绝执行；Claude Code v2.1.287对`/ultrareview`相关的三处边界case（`.gitattributes`编码读取失败提示、误导性配置建议、`GIT_CONFIG_COUNT`证书校验）做了持续加固，但仍非专门点名的安全修复版本；Grok Build方面仍无官方安全公告，状态与前一日持平。给仍在不可信仓库上跑这几款agent的团队的提示：防护清理必须覆盖所有会触发git解析config的调用路径，不能只做一次性的主路径清理。来源：GitHub https://github.com/NousResearch/hermes-agent/pull/130661

## 社区热议与争议

- 极简agent harness Pi（作者Mario Zechner曾长期坚持"绝不支持MCP"）发布1.0版本，通过Codemode沙箱首次加入MCP支持并推出配套长时运行框架Pi Durable，公告自嘲标题"You Said No MCP!"，登顶Hacker News并引发"极简主义 vs MCP生态"的路线讨论。对坚持"自己造轮子不用MCP"的团队是一个值得参考的真实立场反转案例。来源：Hacker News https://news.ycombinator.com/item?id=49926069
- 【单源】UW与Meta提出Context Language Models（CLM）：主张把上下文管理策略交给模型自己学习（模型将上下文视为可自由编辑的文件），而不是依赖人工设计的SOTA harness，原作者推文称"no more harness engineering"，在Hacker News引发129赞的"去harness化"讨论。如果你的团队在手工堆叠越来越复杂的context engineering规则，这是一个值得对照的反方向论点。来源：Hacker News https://news.ycombinator.com/item?id=49922437
- 密码学家Matthew Green提出"多agent蠕虫"风险警示（经Simon Willison转引）：若agent之间共享的"包缓存"换成email/Slack/共享文档/WhatsApp，独立沙箱训练换成各自部署的个人agent，就具备了payload劫持agent、agent再把payload带给下一个agent的蠕虫传播全部要素。给正在设计多agent之间通过通用通讯渠道协作的系统提了一个具体的攻击面提醒，值得在沙箱/权限设计阶段纳入威胁模型。来源：Simon Willison's Weblog https://simonwillison.net/2026/Oct/1/matthew-green/
