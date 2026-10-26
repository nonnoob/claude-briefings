# 🛠️ AI Agent 工程简报 · 2026-10-26

> 覆盖窗口：2026-10-20 06:15 UTC 至 2026-10-26 08:25 UTC（常规）

今日要闻：Anthropic 将已获超 70 家平台采用的 Agent Skills 标准正式捐赠给 Linux 基金会旗下的 Agentic AI Foundation（AAIF），同日 OpenAI、Hugging Face 与阿里巴巴分别捐出 Open Responses、OpenEnv 与 OpenSandbox，同时 Anthropic 发布三年来首个新 API 版本 `2026-10-21` 并彻底移除 `temperature`/`top_p`/`top_k` 参数。

## Agent/Skill 设计模式

- Anthropic 于 10 月 22 日在圣何塞 AGNTCon + MCPCon 大会上宣布将 Agent Skills 开放标准（基于 `SKILL.md` 的渐进式按需加载规范，发布 10 个月已积累超 100 万个技能、近 2.8 亿次安装并获 ChatGPT、Cursor、Copilot 等 70 余家平台集成，含域名 `agentskills.io` 与 GitHub 组织）捐赠给 Linux 基金会旗下的 Agentic AI Foundation（AAIF）；同场 OpenAI 捐出跨厂商统一请求与工具调用规范 Open Responses，Hugging Face 捐出可组合强化学习与 agent 评测环境框架 OpenEnv，阿里巴巴捐出基于 Docker/K8s 的通用安全代码执行沙箱协议 OpenSandbox。继 MCP 之后，技能封装、模型接口、评测环境与执行沙箱四大核心层全面走向跨厂商中立标准，自建 agent 架构应优先对齐这些开放原语以降低锁定风险。来源：Anthropic https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation 、AAIF https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects 、Simon Willison https://simonwillison.net/2026/Oct/22/donating-agent-skills/
- LangChain 团队 Harrison Chase 与 C. Broekhuizen 于 10 月 24 日发表《The five components of building a 'company harness'》，总结从单人对话走向全公司多人共享生产级 agent 的五项核心底座：嵌入 Slack 等团队既有协作流、区分"代表特定用户（OBO）"与服务自身身份的权限模型、兼顾公司全局与个人粒度的分层作用域记忆（Scoped Memory）、带鉴权令牌的安全沙箱代码执行，以及以定时或事件触发为主的后台常驻运行（Scheduled Runs）。设计团队级共享 agent 时，身份代理（OBO）与记忆作用域隔离是比提示词调优更前置的架构边界。来源：LangChain Blog https://www.langchain.com/blog/components-building-company-harness
- Hamel Husain 于 10 月 20 日发表《How To Use Decision Models for Evals》，演示如何用低成本专用决策分类器（如 OpenAI Decisions API、Perplexity Decider 等）替代高耗时且未校准的"LLM 自报置信度"，通过量化校准决策阈值来判定 agent 何时应中止执行并向人类求助或切换路由。将 agent 线上护栏与评估从模糊的生成式打分转为可测试的阈值校准工程，可大幅压降生产环境拦截延迟与成本。来源：Hamel Husain https://hamel.dev/blog/posts/decision-model-evals/

## Prompt 与 Context 工程

- LangChain 工程师 Jess Weng 于 10 月 23 日发表《Context Engineering Starts with Retrieval》，指出长程 agent 的"上下文腐烂"（context rot）往往始于粗糙检索将噪声塞入窗口，提出三层检索侧治理模式：先用 `glob`/`grep` 等精确文件系统工具探路而非全量拉取、将大体积工具输出转存为文件而在主上下文仅保留路径与摘要预览，以及把重度文本阅读委派给子 agent 在外部消化后再返回结论。设计工具接口时默认返回"文件句柄+摘要"而非原始大负载，是维持长会话推理精度的关键习惯。来源：LangChain Blog https://www.langchain.com/blog/context-engineering-starts-with-retrieval
- OpenAI 于 10 月 20 日在 Responses API（GPT-5.6 及后续模型）中上线 12 小时超长 Prompt Cache（设 `prompt_cache_options.ttl = "12h"` 即可突破默认 30 分钟限制，并同步应用于 Codex 与 ChatGPT Work 会话），写入附加费为标准输入价的 2.5 倍（30 分钟档为 1.25 倍），缓存读取仍享 0.05x–0.1x 折扣且支持单请求内按断点混用不同 TTL。适合跨午休或隔夜恢复的全天候编码 agent 与长周期后台循环，可将高稳定性的系统指令与工具集钉在 12 小时缓存层以摊薄重算开销。来源：AI Weekly https://aiweekly.co/alerts/openai-adds-12-hour-prompt-cache-ttl-to-api-25x-write-cost 、OpenAI Community https://community.openai.com/t/12-hour-prompt-caching-day-16-of-28-days-of-quality-of-life-improvements-and-or-a-full-reset/1403525?page=5

## 开发者工具与工作流

- Claude Code 连续发布 v2.1.304 至 v2.1.310：v2.1.304 新增扫描工作区历史以安全配置自动模式的 `/auto-mode-setup` 及组织级 Code Review 深度档位策略；v2.1.307 新增 `/claude-api api-version` 迁移命令、记录权限/沙箱/hook 拦截详情的 `claude_code.safety_event` OTel 事件，并限制 HTTP MCP 断线仅对声明 `readOnlyHint`/`idempotentHint` 的工具自动重试；v2.1.309 紧急修复 macOS/Linux 沙箱在沙箱外执行 shell 启动文件、篡改 `--mcp-config`、后台进程存活越过主会话后写拒绝失效及符号链接绕过 `denyWrite` 四处逃逸漏洞（此外，前期追踪的 GitSpawn 漏洞已连续逾 14 天无新增官方安全公告，本期起移出追踪）；v2.1.310 将 Monitor 工具扩展至 Bedrock/Vertex/Foundry 并改进 base64/SVG 触发超长报错后的压缩恢复。为自定义 MCP 工具显式标注 `readOnlyHint` 与 `idempotentHint`，现已直接决定网络抖动时是否会触发重复副作用调用。来源：Claude Code Changelog https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- OpenAI Codex CLI 于 10 月 23 日发布 `rust-v0.164.0`，新增 10 个编号 `/presets` 槽位以保存可复用的提示词与斜杠命令组合，支持在 `/model` 与 `/permissions` 中直接通过内联参数动态设定模型、推理强度、速度与权限配置，并修复会话恢复时全局默认设置覆盖线程已保存配置的问题。将高频复用的检查清单固化进 `/presets` 并配合内联参数切档，可显著减少多步骤排错中的交互按键次数。来源：SourceForge Mirror https://sourceforge.net/projects/openai-codex.mirror/files/rust-v0.164.0/ 、ExplainX https://explainx.ai/blog/openai-12-hour-prompt-caching-codex-work-cache-forever-claimed-vs-verified-2026
- GitHub Copilot CLI 连发 v1.0.100 至 v1.0.104，新增动态工作流子 agent 原生结构化输出、引导辅助审批判定的 `assistedApprovalInstructions`、通过 `ghapp://` 链接直接安装已验证 Skills/插件、macOS 沙箱直连本地 TCP 服务，以及子 agent 继承 MCP 工具审批结果避免重复弹窗；Qwen Code 发布 v0.26.0，新增按低水位线清理旧工具结果以保护 prompt cache 前缀的尺寸触发微压缩（microcompaction）、`qwen daemon start --save-token` 守护进程令牌持久化，以及提醒模型记录命令所写文件的 shell 钩子。Qwen Code 的"低水位线微压缩"提供了一个避免每轮改写前缀导致缓存失效的实用工程范式。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases 、Qwen Code Releases https://github.com/QwenLM/qwen-code/releases

## 模型能力与 API 更新

- Anthropic 于 10 月 21 日发布自 `2023-06-01` 以来首个新 API 版本 `2026-10-21`，并同步推出默认指向该版本的 Python SDK 2.0.0 与 TypeScript SDK 1.0.0（开源协议由 MIT 改为 Apache 2.0）：新版本彻底移除 `temperature`、`top_p` 与 `top_k` 采样参数，请求中若携带上述任一字段（即便传入原默认值）将直接返回 HTTP 400 错误，同时将 SDK 默认鉴权头从 `X-Api-Key` 切换为 `Authorization: Bearer`，并禁止在 assistant 消息内直接放置文档块。升级新主版本 SDK 前务必全局排查并清理遗留的 `temperature=0` 等采样参数及自定义网关鉴权头解析逻辑（旧代码可通过显式固定 `2023-06-01` 版本头过渡）。来源：Claude API Release Notes https://docs.anthropic.com/en/release-notes/api 、Enjoy.dev https://enjoy.dev/blog/claude-api-2026-10-21/
- Moonshot AI 于 10 月 23 日发布 2.8 万亿参数（104B 激活、100 万上下文）MoE 模型 Kimi K3.1 Pro，支持 `low`/`medium`/`max` 三档推理强度且兼容 OpenAI 接口，在 Terminal-Bench 4.0 等长程编码与工具调用评测中逼近 Claude Opus 5.5 与 GPT-6 Astra，API 定价仅为西方同类旗舰约一半（输入 2 美元/百万、输出 10 美元/百万 token）并承诺于 11 月 4 日开放完整权重；同期 LlamaIndex 发布驱动 LlamaParse 的 4B 参数文档解析视觉模型 OCRia-1，在 ParseBench 取得 87.4 分（35B 以下模型 SOTA），专攻跨页嵌套表格、多轴图表与公式结构化提取。高性价比百万上下文底座与轻量级专用表格解析 VLM 的组合，进一步拉低了私有化长程编码与文档 agent 的构建成本。来源：Simon Willison https://simonwillison.net/2026/Oct/23/kimi-k31-pro/ 、LlamaIndex Blog https://www.llamaindex.ai/blog/parse-ocria-1

## 案例与最佳实践复盘

- Modal 首席执行官 Erik Bernhardsson 在 Latent Space 播客访谈中复盘"临时 Agent 沙箱"（ephemeral agent sandboxes）基础设施的演进，披露随着自主编码与工具调用 agent 普及，按需拉起、用完即毁的隔离沙箱已跃升为 Modal 核心增长引擎，并剖析了海量并发容器极速冷启动、文件系统快照挂载与防止失控 agent 耗尽计算资源的隔离边界设计。自建生产级代码执行 agent 时，用毫秒级文件系统快照克隆替代常规容器冷启动是打通交互延迟瓶颈的关键。来源：Latent Space https://latent.space/p/modal-d/

## 社区热议与争议

- 【续报】OpenCode Console 密钥泄露事件持续发酵：多名开发者反映被盗的 OpenAI、Anthropic 与 Google API 密钥在数小时内遭高频盗刷，产生数百至逾 1700 美元异常账单并触发云厂商封禁；OpenCode 联合创始人 Dax Raad 强调本地 CLI/桌面端（密钥存于本地 SQLite 或 `auth.json`）未受影响，并将攻击归因于黑客利用被盗凭据抓取前沿模型输出进行"大规模模型蒸馏攻击"，但安全观察人士质疑该定性意在淡化凭据托管防护失职，同时官方提醒在 Console 界面删除密钥并不会在模型厂商侧自动失效；截至 10 月 26 日详细取证报告仍未公布。任何交由第三方 agent 平台托管的 API key 均须配置硬性消费上限（hard spend cap），且遇险时必须直接赴模型厂商控制台手动吊销。来源：The Hacker News https://thehackernews.com/2026/10/opencode-console-breach-may-have.html
- Moonshot AI 在 Kimi K3.1 Pro 技术披露中说明团队在训练阶段主动过滤并剔除了网络攻击与漏洞利用相关语料以遏制模型的高阶黑客能力，在 Hacker News 与开发者社区引发关于"即将开源的前沿模型主动清洗攻防知识是否会削弱合法自动化安全审计与漏洞修补 agent 能力"的讨论。构建安全审计或 DevSecOps 类 agent 时，需针对性评测底座模型是否因安全语料过滤而出现特定漏洞模式识别盲区。来源：Simon Willison https://simonwillison.net/2026/Oct/23/kimi-k31-pro/
