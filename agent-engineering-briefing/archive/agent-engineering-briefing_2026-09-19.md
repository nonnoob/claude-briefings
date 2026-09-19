# 🛠️ AI Agent 工程简报 · 2026-09-19

> 覆盖窗口：2026-09-18 至 2026-09-19（常规）

## Agent/Skill 设计模式

- Claude Code "Projects" 改版为协调者-并行子agent架构：单个工程目标由协调者拆分给多个并行云端会话（各自开分支、共享项目文件与记忆），完成后自动审查并汇总结果，09-17起向部分Pro/Max用户开放beta，一周内扩大范围。为什么关注：把"多开会话手动协调"产品化为"协调者拆解+并行子agent+自动汇总"的标准范式，值得参考其共享上下文与审查环节的设计。来源：The Register https://www.theregister.com/ai-and-ml/2026/09/18/claude-code-revamps-projects-so-you-can-work-and-pay-in-parallel/5297532
- Hacker News热议论文《An Empirical Study of Harness Design for Coding Agents》：176组配置对比4个模型在SWE-Bench Verified与Terminal-Bench 2.1上的表现，发现预定义工具接口只对bash能力弱的模型有增益（强模型用纯bash更省钱效果更好）、规划模块主要帮弱模型提准确率、对强模型主要是省成本，上下文预算紧张时基于规则的裁剪比LLM摘要更关键。为什么关注：直接挑战"一套harness/框架默认配置打天下"的做法，提示按模型能力分别选择工具接口与上下文管理策略。来源：Hacker News https://news.ycombinator.com/item?id=49753878

## 开发者工具与工作流

- Claude Code发布v2.1.277：新增原生支持AGENTS.md（项目无CLAUDE.md时自动读取，可在/config开关），新增CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1正向代理出站模式与网关headers静态头配置，另有130+项bug修复；该版本在Hacker News引发热议（576赞206评论），肯定跨工具配置文件统一化的同时，也有人吐槽Bedrock/Vertex/Foundry尚未支持。为什么关注：AGENTS.md正成为跨Claude Code/Copilot/Codex/Gemini CLI的事实标准，新项目可考虑直接用它替代厂商专属配置文件。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- 【续报】Claude Code发布v2.1.278：此前追踪的auto mode默认化事件中，"classifier计费"分支已见进展——Claude API/Enterprise及Bedrock/Vertex/Foundry/网关场景auto mode改为默认走server端分类器，不再对分类器token计费（可用CLAUDE_CODE_AUTO_MODE_SERVER=0退出，/status新增一行显示分类器是否server端运行）；但"auto mode本身成为这些平台的默认权限模式"仍未变化，官方文档显示这些平台仍默认manual，只有Pro/Max/Team终端/VS Code场景默认auto。为什么关注：企业/网关部署的隐性开销先行降低，但默认权限模式切换的时间表仍未兑现，继续关注。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog
- GitHub Copilot CLI发布v1.0.87-0预发布：新增支持组织策略的自动路由分级、连续"steering"提示自动合并为待处理消息、可配置worktree路径模板、MCP慢连接阈值提示、执行型subagent实时耗时显示，并修复Windows沙箱代理与会话恢复问题。来源：GitHub Releases https://github.com/github/copilot-cli/releases
- OpenAI Codex CLI发布v0.155.1：修复本地TUI新会话默认关闭推理摘要的问题，避免部分不支持推理摘要的provider拒绝请求。来源：GitHub Releases https://github.com/openai/codex/releases
- Plugin4Shell漏洞披露：Claude Code、OpenAI Codex、GitHub Copilot、Google Gemini CLI的插件/市场机制存在零点击RCE——利用git分支名与commit哈希解析歧义，可让"看似SHA锁定"的插件检出实际解析到攻击者仓库的恶意代码；Anthropic与OpenAI已修复，GitHub Copilot尚未修复，Google选择弃用Gemini CLI而非修复。为什么关注：用了插件/skill市场机制的团队应立即核实所依赖的coding agent是否在四款受影响之列，未修复前避免自动更新第三方插件。来源：Help Net Security https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/
