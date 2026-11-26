# MEMORY

## 1. 本次运行

- 运行时刻及检索截止：2026-11-26 10:07 UTC。
- 实际覆盖窗口：2026-11-25 10:07 UTC 至 2026-11-26 10:07 UTC（常规）。
- 收录 1 条（Copilot CLI v1.0.116 正式版与 v1.0.117 预发布）。Claude Code 无新版（最新仍 v2.1.332）；Codex 仅 0.173/0.174 alpha；Anthropic 工程博客、Simon Willison（仅 datasette-charts 小版本）、社区方向未检出窗口内实质新内容。

## 2. 已报条目清单（保留最近 14 天）

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
- 2026-11-14 | Claude Code v2.1.325 修复 zstd 解码安全问题、子 Agent 模型切换错误及第三方网关压缩失败 | https://github.com/anthropics/claude-code/releases
- 2026-11-14 | Copilot CLI v1.0.111 正式版与 v1.0.112：子 Agent 遵守 --max-ai-credits、默认推荐上下文窗口 | https://github.com/github/copilot-cli/releases
- 2026-11-16 | Claude Code v2.1.326：Code Mode 可与 agent teams 并用、/status 显示被关闭功能、修复权限规则与会话恢复等 | https://github.com/anthropics/claude-code/releases
- 2026-11-17 | Claude Code v2.1.327：mcp add-json 支持 stdin、修复 .mcp.json 被覆盖、/status 体检 skill/hook、子 Agent 模型与权限继承修复 | https://github.com/anthropics/claude-code/releases/tag/v2.1.327
- 2026-11-17 | 提示 Claude Code auto mode 将移除回退计费分类器请求，claude -p 无人值守将改为询问或拒绝 | https://github.com/Adam-S-Daniel/wsl-automation/issues/123
- 2026-11-17 | Codex rust-v0.170.0：WebRTC 语音、OTel 刷新认证头、实验性跨环境同名 MCP | https://github.com/openai/codex/releases/tag/rust-v0.170.0
- 2026-11-17 | Copilot CLI v1.0.113：features.browserUse 托管开关；传 SDK 改名为 @microsoft/copilot-sdk | https://github.com/github/copilot-cli/releases/tag/v1.0.113
- 2026-11-11 | MCP 官方宣布每六个月固定发布节奏，当前规范 2026-07-28 | https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/
- 2026-11-18 | Claude Code v2.1.328：auto mode 扩展至云厂商/网关上的 Opus/Sonnet 4.6、MCP hook onFailure: "block"、OTel 无端点提示 | https://x.com/ClaudeCodeLog/status/2123226990551445634
- 2026-11-18 | Copilot CLI v1.0.114：mcp enable 容忍无效 mcp-config.json、/settings 窄终端修复 | https://github.com/github/copilot-cli/releases
- 2026-11-19 | Google 发布 Gemini 4 Neon（$3/$15、100 万上下文、四档思考强度） | https://www.infoworld.com/article/4250618/google-launches-gemini-4-neon-touting-lower-costs-for-complex-ai-coding-tasks.html

- 2026-11-20 | Claude Code v2.1.329：hooks 来源信任提示、Code Mode 下报错的 PreToolUse hook 不再拦截（需 onFailure: "block"） | https://github.com/anthropics/claude-code/releases/tag/v2.1.329
- 2026-11-20 | Codex rust-v0.171.0：GPT-6.2 Sol/Astra 入目录、TUI workspace 默认开、codex exec --remote | https://github.com/openai/codex/releases/tag/rust-v0.171.0
- 2026-11-20 | Copilot CLI v1.0.115-0/-1：MCP 登录容忍缺失 refresh-token scope | https://github.com/github/copilot-cli/releases/tag/v1.0.115-1
- 2026-11-20 | 二手文章转述研究：LLM 生成的 AGENTS.md 降低任务成功率、成本升逾 20% | https://tutorials.technology/tutorials/context-engineering-ai-agents-2026.html
- 2026-11-20 | Claire Vo 复盘 ChatPRD 免费试用遭 token 转卖滥用（Simon Willison 转载） | https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/
- 2026-11-20 | HN 讨论哈佛研究称 AI 编码 agent 使瓶颈转向代码审查 | https://news.ycombinator.com/item?id=50538303
- 2026-11-21 | Claude Code v2.1.330：Enterprise Admin Console 登录、easel 图表 mod、压缩后卡死/worktree 误删/设置丢失修复 | https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.330
- 2026-11-21 | Copilot CLI v1.0.115-2~-5：ACP 结构化澄清表单、长会话磁盘与恢复优化 | https://github.com/github/copilot-cli/releases/tag/v1.0.115-5
- 2026-11-22 | Copilot CLI v1.0.115-6：组织必装插件可立即重试、/delegate 未登录提示、取消 shell 命令清理孤儿子进程 | https://github.com/github/copilot-cli/releases/tag/v1.0.115-6
- 2026-11-22 | Copilot CLI v1.0.115-7：--ui-server 客户端可即时接入恢复会话、修复 npm 版启动期停止后残留进程 | https://github.com/github/copilot-cli/releases/tag/v1.0.115-7
- 2026-11-23 | Anthropic 推出 Claude Ship（Code Review GA，PR Steward 与 Claude Approvals beta） | https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/
- 2026-11-23 | Claude Code v2.1.331：Code Mode 上云厂商终端、MCP 挂起修复、claude doctor 连通性检查、11-30 起托管 marketplace 默认自动更新 | https://github.com/anthropics/claude-code/releases/tag/v2.1.331
- 2026-11-24 | Codex rust-v0.172.0 稳定版：MCP 惰性启动、exec resume 恢复沙箱权限、GPT-6.2 迁移指引 | https://github.com/openai/codex/releases/tag/rust-v0.172.0
- 2026-11-23 | Copilot CLI v1.0.115-8：Assisted Permissions 备用审查模型、按子 agent 汇总用量 | https://github.com/github/copilot-cli/releases
- 2026-11-25 | Claude Code v2.1.332：MCP 服务器可提供 skill（beta）、PreSkillShellCommand hook、Foundry 别名升至 Sonnet 5.5/Opus 5.5 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-11-25 | Copilot CLI v1.0.116-0~-5 预发布：插件/MCP 同端点告警、长会话内存泄漏修复、ACP 上下文大小可选 | https://github.com/github/copilot-cli/releases/tag/v1.0.116-5
- 2026-11-24 | Simon Willison《Three LLM inflection points in twelve months》 | https://simonwillison.net/2026/Nov/24/llm-inflection-points/
- 2026-11-25 | Copilot CLI v1.0.116 正式版与 v1.0.117 预发布：env 设置、自定义 agent 显式工具暴露、后台 agent 重启续聊 | https://github.com/github/copilot-cli/releases


## 3. 进行中事件表

- 事件：Claude Code `.claude/settings.local.json` 内置敏感信息擦除（secret scrubbing）与安全默认保护落地；最后进展日期：2026-11-09（Apiiro 披露「Yes, and don't ask again」将含密钥的明文命令写入 `.claude/settings.local.json` 并在逾 1,100 个公开仓库泄露后，Claude Code 负责人 Boris Cherny 在 HN 回应称正原型验证内置 secret scrubbing 与自动防泄漏机制）；下一步关注点：Claude Code 后续版本（v2.1.323、v2.1.325 摘要均未见此项，v2.1.326 亦未见，v2.1.327–v2.1.332 亦未见（v2.1.332 于 11-24 发布仍无此项；11-26 检索 npm 最新仍为 v2.1.332），看 v2.1.333+）变更日志何时上线 `.claude/settings.local.json` 写入前的密钥自动脱敏/拦截及仓库级 `.gitignore` 保护改进。
- 事件：Claude Code 彻底移除模型上下文中的用户账号邮箱后续版本落地；最后进展日期：2026-11-09（v2.1.319–v2.1.329 均 进一步加固权限与 MCP OAuth 令牌安全，但尚未在变更日志中宣告将登录邮箱彻底移出模型系统上下文）；下一步关注点：Claude Code 后续版本变更日志是否兑现从系统上下文中彻底剥离用户邮箱，以及 `@author` 等场景的替代方案。
- 事件：OpenAI 收购 Pierre 后的 Code Storage 与 Codex 集成及 Pando 开源/上游回馈进展；最后进展日期：2026-11-04（OpenAI 披露内部 Git 后端 Pando 并宣布收购 Pierre，计划将 Pierre 的分布式机器导向 Git 存储层 Code Storage 深度整合进 Codex）；下一步关注点：Codex CLI（0.170.0–0.172.0 稳定版均未见，0.173 仅有 alpha Pierre 集成，看 0.173+）及云端环境何时开放基于 Pierre Code Storage 的多 Agent 并行分支与内联审查功能，以及 Pando 相关补丁是否回馈上游 Git。
- 事件：Opus 4.8 fast mode 停用；最后进展日期：2026-10-31（v2.1.316 公告，弃用日 10 月 30 日）；下一步关注点：11 月 30 日正式移除前后的客户端报错处理与迁移公告。
