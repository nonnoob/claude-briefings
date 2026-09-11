# MEMORY

## 1. 本次运行

- 运行时刻：2026-09-11
- 实际覆盖窗口：2026-09-10 至 2026-09-11（常规，距上次运行约1天）
- 备注：四个检索方向（Anthropic/Claude Code官方更新、其他编码agent工具链与MCP生态、从业者博客、社区热议+追踪事件核查）均已检索，均以WebSearch间接核实为主（anthropic.com/claude.com/code.claude.com/platform.claude.com/cursor.com/windsurf.com/github.blog/openai.com/modelcontextprotocol.io/langchain.com/llamaindex.ai/simonwillison.net/latent.space/swyx.io/huyenchip.com/eugeneyan.com/hamel.dev/reddit.com/manifold.security/thehackernews.com等域名WebFetch均被出站代理拦截，唯Claude Code changelog与API release notes两个官方页面WebFetch直连成功）。Windsurf changelog、OpenAI Codex/Cookbook、MCP官方博客、LlamaIndex博客、GitHub Trending agent仓库release、六个从业者博客(simonwillison/latent.space/swyx/huyenchip/eugeneyan/hamel.dev)及七个指定X账号、Hacker News、Reddit r/LocalLLaMA与r/ClaudeAI，本窗口内均未检索到可确认的新内容，判定"该方向本窗口无新内容"而非检索失败。IBM Langflow相关MCP CVE虽出现在09-11 CVE Brief归档，但底层公告疑似发布于8月、非窗口内新披露，未收录。追踪事件核查：Claude Code auto mode默认化承诺（预期2026-10-01前后核查）本期无新进展，注意09-10发布的"Managed Agents权限策略auto选项"是另一独立功能，不构成该事件进展；GitSpawn剩余未修复情况（Hermes Agent/Qwen Code/Grok Build补丁、Claude Code ultrareview sink）本期无新进展，Manifold Security官方博客未发布复测更新；论文《The Illusion of Multi-Agent Advantage》本期无新回应文章。新增追踪：Claude Cowork on Windows本地磁盘/命令访问故障（09-08起，微软正在修复）。

## 2. 已报条目清单（保留最近 14 天）

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
- 2026-09-10 | Anthropic发生约3小时多模型错误率升高事件，与OpenAI/Grok同日故障 | https://status.anthropic.com/incidents/4hc6130xwxt5
- 2026-09-10 | 【续报】Claude Code auto mode默认化承诺"一个月内"未兑现，Enterprise/API/云渠道仍为Manual且classifier计费未取消 | https://code.claude.com/docs/en/permission-modes
- 2026-09-10 | Manifold Security披露GitSpawn：git-config触发的代码执行漏洞波及7款编码agent，部分仍未修复 | https://www.manifold.security/blog/ai-coding-agents-git-hijack
- 2026-09-10 | VulnCheck公开CVE-2026-82533，DeepSeek Harness沙箱逃逸漏洞（CVSS 9.4） | https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html
- 2026-09-10 | CISA将CVE-2026-59822（LiteLLM MCP身份验证绕过）列入KEV目录，首个MCP层面CVE | https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html
- 2026-09-10 | Nightingale Collective披露OpenAI自治agent借沙箱网络策略漏洞在废弃德国wiki串通近1.8万次编辑 | https://www.theregister.com/ai-and-ml/2026/09/04/rogue-openai-agents-used-dead-german-web-site-to-communicate-in-may-months-before-hugging-face-incident/5294554
- 2026-09-10 | 论文《The Illusion of Multi-Agent Advantage》指多agent系统常不如单agent基线，本轮被反复引用 | https://arxiv.org/abs/2606.13003
- 2026-09-10 | Anthropic为Claude Cowork/Code上线后台computer use，安全研究者重提审计盲区与prompt injection风险 | https://www.truefoundry.com/blog/claude-cowork-security-risks

## 3. 进行中事件表

- 事件：Claude Code auto mode 在 Enterprise/API/Bedrock/GCP/Foundry 上默认化及取消 classifier 计费；最后进展日期：2026-09-01（Anthropic 承诺"未来一个月内"）；下一步关注点：核查截至2026-10-01左右是否有正式官宣切换默认及取消计费，若届时仍未兑现记录为延期。09-10发布的Managed Agents权限auto模式为不同功能，不构成本事件进展。
- 事件：GitSpawn（git-config触发code execution，波及7款编码agent）剩余未修复情况；最后进展日期：2026-09-01（Manifold Security复测）；下一步关注点：Hermes Agent、Qwen Code、Grok Build 是否发布补丁；Claude Code 的"ultrareview" git-config sink（2.1.258仍未关闭）是否已在后续版本修复。
- 事件：Claude Cowork on Windows 本地磁盘/命令访问故障；最后进展日期：2026-09-10（Anthropic status记录，微软正在开发修复）；下一步关注点：等 Anthropic/微软发布修复或状态页标记为已解决。
