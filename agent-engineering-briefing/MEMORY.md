# MEMORY

## 1. 本次运行

- 运行时刻：2026-09-14
- 实际覆盖窗口：2026-09-13 至 2026-09-14（常规，距上次运行约1天）
- 备注：检索方向覆盖 Anthropic/Claude Code 官方更新、Cursor/GitHub Copilot/OpenAI Codex 等编码 agent 与 MCP 生态、从业者博客（simonwillison.net/Latent Space/swyx/Chip Huyen/Eugene Yan/Hamel Husain）、LangChain/LlamaIndex、社区热议（Hacker News AI Digest/Reddit/X 指定账号）、进行中事件定向核查六个方向。code.claude.com WebFetch 直连成功，changelog 最新仍为 2.1.270（09-12），窗口内无新版本。anthropic.com/engineering、claude.com/blog、platform.claude.com、status.claude.com、cursor.com、github.blog、langchain.com、simonwillison.net、news.ycombinator.com 等本轮 WebFetch 均被出站代理拦截，改用 WebSearch 间接核实：均未发现窗口内（09-13/09-14）新条目，或经核实条目发布日期落在窗口外（如 LangChain/GitHub Copilot/OpenAI Codex 相关更新集中在 09-09~09-11）。Hacker News 经 GitHub 镜像digest（sikm-lqs/agents-radar#176）核实到 09-14 前页，其中"Nine coding harnesses vs. your laptop"因 WebSearch 结果与多篇同类第三方文章内容混淆、无法可靠核实具体数据，予以舍弃不收录，避免误报；同 digest 中的 Anthropic 威胁情报报告（胡塞武装用 Claude Code 开发导弹制导软件）判定为安全/政策类新闻而非"工程实践"范畴，不收录。simonwillison.net 09-13/09-14 两条个人小工具发布（shot-scraper 1.12、commit-rewriter 0.1）信号强度不足，未收录。追踪事件核查：Claude Code auto mode 默认化承诺（Enterprise/API/Bedrock/GCP/Foundry）本期无新进展；GitSpawn 剩余未修复情况（Hermes Agent、Qwen Code、Grok Build、Claude Code 第二处 config 路径）经核实仍停留在 09-01/09-02 复测结果，本期无新进展；Claude Cowork on Windows 磁盘访问故障经核实仍无官方修复补丁，本期无新进展。
- 本期新增条目分布在"开发者工具与工作流""案例与最佳实践复盘"两个板块，其余板块本窗口无可靠新内容，按格式契约省略。

## 2. 已报条目清单（保留最近 14 天）

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
- 2026-09-11 | 【单源】Anthropic status记录Claude Cowork on Windows本地磁盘/命令访问故障，微软正在修复 | https://statusgator.com/services/anthropic
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

- 事件：Claude Code auto mode 在 Enterprise/API/Bedrock/GCP/Foundry 上默认化及取消 classifier 计费；最后进展日期：2026-09-01（Anthropic 承诺"未来一个月内"）；下一步关注点：核查截至2026-10-01左右是否有正式官宣切换默认及取消计费，若届时仍未兑现记录为延期。
- 事件：GitSpawn（git-config触发code execution，波及7款编码agent）剩余未修复情况；最后进展日期：2026-09-01（Manifold Security复测）；下一步关注点：Hermes Agent、Qwen Code、Grok Build 是否发布补丁；Claude Code 的"ultrareview" git-config sink 是否已在后续版本修复。
- 事件：Claude Cowork on Windows 本地磁盘/命令访问故障；最后进展日期：2026-09-13（微软将其正式收录进Windows 11 25H2已知问题列表，确认为KB5124008/KB5124012引发的Plan9共享挂载失败；社区验证卸载该KB可临时恢复，仍无官方修复补丁）；下一步关注点：等微软通过Windows Update发布正式修复，或Anthropic/Claude端提供绕过Plan9依赖的官方方案。
