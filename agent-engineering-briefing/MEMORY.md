# MEMORY

## 1. 本次运行

- 运行时刻及检索截止：2026-11-06 16:22 UTC（2026-11-06 08:22 PST）。
- 实际覆盖窗口：2026-10-31 11:32 UTC 至 2026-11-06 16:22 UTC（常规）。
- 六大方向与进行中事件表已完整检索：本期收录 LangChain 异步子 Agent 与浏览器优化、Anthropic Claude Enterprise 推理钩子 GA、MIT CSAIL 权重空间编程（Weight-Space Programming）、Claude Code v2.1.317–v2.1.318 及 HTTP User-Agent 邮箱泄露事件、OpenAI Codex rust-v0.167.0 与收购 Pierre / 内部 Git 后端 Pando、MCP 官方参考服务器 v2.3.0、GitHub Copilot CLI v1.0.106 系列、Kimi K3.1 Pro 开源权重兑现及 LlamaParse 私有化部署架构。
- OpenCode Console 密钥泄露事件自 2026-10-20 以来已逾 14 天无新取证报告发布，按规则移出进行中事件表。

## 2. 已报条目清单（保留最近 14 天）

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
- 2026-10-26 | OpenCode Console密钥泄露后续：受害者遭盗刷最高逾1700美元，官方归因于大规模模型蒸馏攻击引发争议，提醒需赴模型厂商控制台手动吊销 | https://thehackernews.com/2026/10/opencode-console-breach-may-have.html
- 2026-10-26 | Kimi K3.1 Pro技术报告披露开源前主动清洗网络攻击与漏洞利用语料，引发社区关于安全对齐与自动化安全审计agent能力权衡热议 | https://simonwillison.net/2026/Oct/23/kimi-k31-pro/
- 2026-10-31 | VS Code 1.144 公布 Agent Host Protocol v1.0 与六种语言库 | https://code.visualstudio.com/updates/v1_144
- 2026-10-31 | Claude Code v2.1.311 修复压缩后规则文件过期、晚连接 MCP 工具不可见及后台后代 worktree 提前清理 | https://github.com/anthropics/claude-code/releases/tag/v2.1.311
- 2026-10-31 | Claude Code v2.1.312 阻止部分读取后覆写大指令文件，并修复切换目录后的 Skill 发现 | https://github.com/anthropics/claude-code/releases/tag/v2.1.312
- 2026-10-31 | Claude Code v2.1.314 新增工作目录外写入限制，非交互启动失败改返回退出码 1 | https://github.com/anthropics/claude-code/releases/tag/v2.1.314
- 2026-10-31 | Codex rust-v0.166.0 新增队列恢复与网络诊断，修复 resume/fork 权限和计数保留 | https://github.com/openai/codex/releases/tag/rust-v0.166.0
- 2026-10-31 | Copilot CLI v1.0.105 修复长上下文会话无法选择 Fusion High/Max | https://github.com/github/copilot-cli/releases/tag/v1.0.105
- 2026-10-31 | VS Code 1.144 实验性 Keep/Undo 工作集不涵盖终端命令改动 | https://code.visualstudio.com/updates/v1_144
- 2026-10-31 | Claude Code v2.1.316 公告 Opus 4.8 fast mode 将于 11 月 30 日移除且无自动回退 | https://github.com/anthropics/claude-code/releases/tag/v2.1.316
- 2026-11-06 | LangChain发布《Agents Are Going Async》，在Managed Deep Agents中引入异步子Agent任务管理原语与async配置 | https://www.langchain.com/blog/agents-are-going-async
- 2026-11-06 | Anthropic将Claude Enterprise服务端推理钩子（Inference Hooks）转为正式版（GA），支持Prompt与工具调用前实时Webhook拦截 | https://claude.com/blog/claude-enterprise-inference-hooks
- 2026-11-06 | Harrison Chase发表《New context engineering challenges in late 2026》，探讨主动式常驻Agent跨会话状态与共享记忆挑战 | https://www.langchain.com/blog/context-engineering-challenges-late-2026
- 2026-11-06 | LangChain发布《How We Optimized Browser Use for Deep Agents》，采用Stagehand无障碍树快照与Code-Mode批量执行削减80%上下文消耗 | https://www.langchain.com/blog/how-we-optimized-browser-use-for-deep-agents
- 2026-11-06 | Claude Code v2.1.317移除Read工具未变更文件简短占位符（stub），并停止跨模型子Agent默认继承主会话effort级别 | https://github.com/anthropics/claude-code/releases/tag/v2.1.317
- 2026-11-06 | MIT CSAIL发布《Sparks of Weight-Space Programming》展示GPT-6 Astra免训练直接修改Qwen权重修复推理死循环，Simon Willison复现本地Qwen 3.8 27B权重解析 | https://simonwillison.net/2026/nov/3/weight-space-programming/
- 2026-11-06 | Claude Code发布v2.1.317至v2.1.318：新增外发请求包含登录邮箱拦截提示、隔离claude -p嵌套会话ID、SDK Hook失败阻断onFailure: "block"及凭证过期提前10天告警 | https://github.com/anthropics/claude-code/releases/tag/v2.1.318
- 2026-11-06 | OpenAI Codex CLI发布rust-v0.167.0（新增--no-daemon指挥中心控制与未读结果标记），并宣布收购Git基础设施初创公司Pierre以整合Code Storage | https://github.com/openai/codex/releases/tag/rust-v0.167.0
- 2026-11-06 | 官方MCP参考服务器发布modelcontextprotocol/servers v2.3.0：filesystem新增服务级--read-only标志，fetch新增--allowed-hosts域名白名单 | https://github.com/modelcontextprotocol/servers/releases/tag/v2.3.0
- 2026-11-06 | GitHub Copilot CLI发布v1.0.106系列（v1.0.106-2至v1.0.106-9）：修复/resume重复创建后台会话、ACP模式配置遵循与错误前缀格式 | https://github.com/github/copilot-cli/releases
- 2026-11-06 | Moonshot AI在Hugging Face发布2.8T MoE模型Kimi K3.1 Pro完整开源权重（MXFP4权重/MXFP8激活，自定义MIT风格许可证） | https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- 2026-11-06 | OpenAI公开内部Rust Git后端Pando（《Scaling Git at OpenAI》），支撑海量Agent并行写入并将monorepo中位push延迟降低近80% | https://openai.com/index/scaling-git-at-openai
- 2026-11-06 | LlamaIndex发布《Deploying LlamaParse in your own infrastructure》，详解结合OCRia在VPC/BYOC及本地环境私有化部署文档解析流水线 | https://www.llamaindex.ai/blog/deploying-llamaparse-in-your-own-infrastructure
- 2026-11-06 | Claude Code通过HTTP User-Agent泄露用户账号邮箱事件（GitHub Issue #107757）登顶Hacker News，官方致歉并通过v2.1.317及cc-plugin-privacy拦截外发 | https://github.com/anthropics/claude-code/issues/107757

## 3. 进行中事件表

- 事件：Claude Code 彻底移除模型上下文中的用户账号邮箱后续版本落地；最后进展日期：2026-11-05（Issue #107757 曝出 HTTP `User-Agent` 泄露用户登录邮箱后，Anthropic 先以 v2.1.317 弹窗拦截与 `cc-plugin-privacy` 缓解，并承诺在后续版本将账号邮箱从模型上下文中彻底移除）；下一步关注点：Claude Code 后续版本（v2.1.319+）变更日志是否兑现从系统上下文中彻底剥离用户邮箱，以及 `@author` 等场景的替代方案。
- 事件：OpenAI 收购 Pierre 后的 Code Storage 与 Codex 集成及 Pando 开源/上游回馈进展；最后进展日期：2026-11-04（OpenAI 披露内部 Git 后端 Pando 并宣布收购 Pierre，计划将 Pierre 的分布式机器导向 Git 存储层 Code Storage 深度整合进 Codex）；下一步关注点：Codex CLI 及云端环境何时开放基于 Pierre Code Storage 的多 Agent 并行分支与内联审查功能，以及 Pando 相关补丁是否回馈上游 Git。
- 事件：Opus 4.8 fast mode 停用；最后进展日期：2026-10-31（v2.1.316 公告，弃用日 10 月 30 日）；下一步关注点：11 月 30 日正式移除前后的客户端报错处理与迁移公告。
