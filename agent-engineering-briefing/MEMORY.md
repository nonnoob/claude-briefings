# MEMORY

## 1. 本次运行

- 运行时刻及检索截止：2026-11-13 10:10 UTC。
- 实际覆盖窗口：2026-11-12 10:10 UTC 至 2026-11-13 10:10 UTC（常规）。
- 本期仅收录三家 CLI 发布。博客/社区方向经 WebSearch 未见窗口内新文（simonwillison.net 未能直接抓取，搜索未见 11 月 12 日新文）；Anthropic Engineering 无窗口内新文。

## 2. 已报条目清单（保留最近 14 天）

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
- 2026-11-09 | Anthropic发布《The Components of Agent Memory》，拆解四层跨会话记忆架构与离线“做梦”（Dreaming）记忆整理机制 | https://www.anthropic.com/research/components-of-agent-memory
- 2026-11-09 | LangChain发布《What Is Eval-Driven Development? How to Improve AI Agents》，提出面向Agent的评估驱动开发（EDD）三步法 | https://www.langchain.com/blog/what-is-eval-driven-development
- 2026-11-09 | Cursor通过裁剪系统提示词、动态工具加载与缓存复用将长程Agent运行Token成本降低约7%，并上线实时双向语音对话（Voice Chat） | https://cursor.com/changelog
- 2026-11-09 | Simon Willison提出用HTML `<details><summary>`标签折叠编码Agent生成的冗长PR描述以缓解代码审查疲劳 | https://simonwillison.net/2026/Nov/9/detals-summary/
- 2026-11-09 | Claude Code发布v2.1.319至v2.1.321：支持后台异步执行MCP任务、新增permissions.denyInsteadOfPrompting与/model fable（接入Claude Fable 5.2），修复MCP OAuth令牌泄露与沙箱绕过 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-11-09 | GitHub Copilot CLI发布v1.0.107与v1.0.108-1：沙箱模式下/cd自动重启本地MCP服务器、按原始工具名匹配MCP拒绝规则、支持Ctrl+C中断/compact | https://github.com/github/copilot-cli/releases
- 2026-11-09 | Anthropic发布Claude Fable 5.2与受限版Claude Mythos 5.2（100万上下文、提速30%、定价$8/$40每百万Token，FrontierSWE v2达69.9%） | https://www.anthropic.com/news/claude-fable-5-2-and-claude-mythos-5-2
- 2026-11-09 | Anthropic Science团队与Diode Computers发布《Testing Claude on real-world electronics design》，实测Claude Fable 5.2独立完成三款电子硬件从原理图、PCB布线到CAD外壳与固件的端到端原型设计 | https://www.anthropic.com/research/testing-claude-on-real-world-electronics-design
- 2026-11-09 | 斯坦福CS146S讲师Mihail Eric在Latent Space复盘AI原生软件工程教学与Monaco生产实践（200行手写Agent循环、开源PR实战与explain-diff差异走读） | https://latent.space/p/how-stanford-teaches-ai-native-engineering-mihail-eric-monaco
- 2026-11-09 | Simon Willison复盘借助Claude Opus 5.5编写并经800万次模糊测试验证C与Rust版SQLite数值解析扩展（基于Clinger快速路径将耗时压至16–19ns） | https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/
- 2026-11-09 | 安全机构Apiiro曝出Claude Code「不再询问」配置（.claude/settings.local.json）导致逾1100个公开GitHub仓库泄露明文密钥，官方回应正研发内置敏感信息擦除（secret scrubbing） | https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file-exposes.html
- 2026-11-10 | Claude Code 发布 v2.1.322：新增 Vertex global/us/eu 区域 fast mode，被拒时回退标准速度 | https://github.com/anthropics/claude-code/releases
- 2026-11-11 | GitHub Copilot CLI 发布 v1.0.109：加入 Claude Fable 5.2、沙箱规则支持 CIDR，预发布版实验遮罩密码提示应答 | https://github.com/github/copilot-cli/releases
- 2026-11-12 | GitHub Copilot CLI 发布 v1.0.110-1 至 -3 预发布版：MCP/settings 无效配置保留、/compact 遵守额度上限 | https://github.com/github/copilot-cli/releases
- 2026-11-13 | Claude Code v2.1.323 新增实验性 Code Mode 与插件 engines 版本声明 | https://github.com/anthropics/claude-code/releases
- 2026-11-13 | Codex rust-v0.168.0/v0.169.0 新增提供方选择、侧边对话标签，修复不受信目录 MCP 禁用 | https://github.com/openai/codex/releases
- 2026-11-13 | Copilot CLI v1.0.110 正式版与 v1.0.111-0：权限规则支持正则、--host-allow-session-creation | https://github.com/github/copilot-cli/releases

## 3. 进行中事件表

- 事件：Claude Code `.claude/settings.local.json` 内置敏感信息擦除（secret scrubbing）与安全默认保护落地；最后进展日期：2026-11-09（Apiiro 披露「Yes, and don't ask again」将含密钥的明文命令写入 `.claude/settings.local.json` 并在逾 1,100 个公开仓库泄露后，Claude Code 负责人 Boris Cherny 在 HN 回应称正原型验证内置 secret scrubbing 与自动防泄漏机制）；下一步关注点：Claude Code 后续版本（v2.1.323 仍未含此项，看 v2.1.324+）变更日志何时上线 `.claude/settings.local.json` 写入前的密钥自动脱敏/拦截及仓库级 `.gitignore` 保护改进。
- 事件：Claude Code 彻底移除模型上下文中的用户账号邮箱后续版本落地；最后进展日期：2026-11-09（v2.1.319–v2.1.322 均 进一步加固权限与 MCP OAuth 令牌安全，但尚未在变更日志中宣告将登录邮箱彻底移出模型系统上下文）；下一步关注点：Claude Code 后续版本变更日志是否兑现从系统上下文中彻底剥离用户邮箱，以及 `@author` 等场景的替代方案。
- 事件：OpenAI 收购 Pierre 后的 Code Storage 与 Codex 集成及 Pando 开源/上游回馈进展；最后进展日期：2026-11-04（OpenAI 披露内部 Git 后端 Pando 并宣布收购 Pierre，计划将 Pierre 的分布式机器导向 Git 存储层 Code Storage 深度整合进 Codex）；下一步关注点：Codex CLI（0.168.0/0.169.0 已发布但未见 Pierre 集成；看 0.170.0+）及云端环境何时开放基于 Pierre Code Storage 的多 Agent 并行分支与内联审查功能，以及 Pando 相关补丁是否回馈上游 Git。
- 事件：Opus 4.8 fast mode 停用；最后进展日期：2026-10-31（v2.1.316 公告，弃用日 10 月 30 日）；下一步关注点：11 月 30 日正式移除前后的客户端报错处理与迁移公告。
