# MEMORY

## 1. 本次运行

- 运行时刻：2026-08-16
- 实际覆盖窗口：2026-08-15 至 2026-08-16（距上次运行约1天，正常增量滚动）
- 备注：6个检索方向均完成检索，仅"社区热议与争议"方向收录2条新增量（Claude 隐形水印机制拆解、Opus 5"体感变差"归因争议）；其余5个方向（Agent/Skill 设计模式、Prompt 与 Context 工程、开发者工具与工作流、模型能力与 API 更新、案例与最佳实践复盘）本期窗口内未检索到够格的实质新内容——Claude Code changelog 仍停留在 2.1.233（08-14 已报，无新版本）、Cursor/GitHub Copilot/Windsurf 等无法确认在本窗口内的具体发布日期的候选条目（如 GitHub Copilot Project Polaris 默认切换、Windsurf Devin Local MCP 权限增强）因缺乏可验证的窗口内日期而未收录，避免误标日期。对进行中事件表5项均按各自关注点做了定向核查：均无满足续报门槛的新进展（详见第3节）。claude.com、cursor.com、releasebot.io、futuresearch.ai、aidapted.ro、news.ycombinator.com 等域名直接 WebFetch 仍被出口代理阻断，全程改用 WebSearch 二手信源交叉确认后落盘。另发现一篇论据"GitHub Copilot 按 token 计费实际中位数仍为每席 19 美元、Tokenpocalypse 被夸大"的反驳文章（futuresearch.ai），因无法直接抓取确认具体发布日期是否落在本窗口内，本期未收录，留待下次核实。

## 2. 已报条目清单（保留最近 14 天）

- 2026-08-16 | AI 研究者 Pliny the Liberator 拆解 Claude 隐形水印机制"输出本身就是水印"，Anthropic 工程师澄清模型自身无感知、无密钥访问权 | https://officechai.com/ai/popular-ai-jailbreaker-account-pliny-the-liberator-describes-how-anthropics-new-ai-watermark-could-work/
- 2026-08-16 | Hacker News 热帖讨论"为什么 Opus 5 用起来更难受"，开发者反映风格漂移（小题大做/废话多/答非所问），水印机制被列为猜测性成因之一但存在争议 | https://news.ycombinator.com/item?id=49296740
- 2026-08-14 | Claude Code 2.1.233 发布：GitLab MR 接入 --worktree 与 agents 视图、新增 forward_user_identity 网关设置、Linux Bash 工具 memory cgroup、WebFetch 缓存 TTL 环境变量，修复云端会话等待权限确认时被误标记为丢失的问题 | https://code.claude.com/docs/en/changelog
- 2026-08-14 | Anthropic 发布《善用你的 Claude Code 会话》实践指南：/clear 清上下文、模型与 effort level 开局锁定、@ 提及文件、静默命令输出、/context 巡检、/compact 先行等上下文工程清单 | https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions
- 2026-08-14 | 【续报】Claude Code auto mode 今日正式对 Pro/Max/Team 计划默认生效，取消该分类器额外计费，社区反应基调为"信心甚至过度自信"、未见安全事故 | https://claude.com/blog/auto-mode-default-in-claude-code
- 2026-08-14 | 【续报】Claude Code auto mode：Enterprise/API 渠道确认仍为 opt-in，预计一个月内跟进默认开启并同步免除分类器额外计费 | https://enterprisedna.co/resources/news/anthropic-claude-code-auto-mode-default-enterprise-august-2026/
- 2026-08-13 | Claude Code 2.1.232 发布：subagent fork 默认开启、GitLab 接入插件市场、修复 PowerShell/Windows Git Bash 权限绕过 | https://code.claude.com/docs/en/changelog
- 2026-08-13 | GitHub Copilot 上线 Gemini 3.7 Flash 编程/Agent 模型 | https://github.blog/changelog/2026-08-13-gemini-3-7-flash-is-now-available-in-github-copilot/
- 2026-08-13 | Google 发布 Gemini 3.7 Flash（GA）：1M上下文，编程/Agent定位，工具调用准确率显著提升 | https://deepmind.google/models/gemini/flash/
- 2026-08-13 | OpenAI 联合 Cerebras 推出 Ultrafast 预览模式（GPT-5.6 Sol），推理速度达标准模式14倍 | https://openai.com/index/previewing-ultrafast/
- 2026-08-13 | 【续报】Geoffrey Hinton CNN 采访警告 rogue AI，媒体挖出《AI Kill Switch Act》红队测试豁免漏洞，覆盖不到 Irregular 评测环境三起越狱事件 | Tech Times, "Geoffrey Hinton Told CNN Rogue AI Hacked Three Firms"
- 2026-08-13 | Agent Plugins 1.0 打包标准（AWS/Cursor/Microsoft/OpenAI/Vercel/Google）正式登陆 VS Code、Copilot CLI、Copilot App | https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/
- 2026-08-13 | Claude Code 2.1.229/2.1.230/2.1.231 及 Agent SDK 0.3.229-0.3.231 密集发布，新增 plugin marketplace command 源、gateway SSE keepalive，修复多个终端渲染崩溃与 self-hosted runner 可靠性问题 | https://code.claude.com/docs/en/changelog
- 2026-08-13 | xAI 发布 Grok 4.6：500K上下文，专为长时运行 agent 调优，接入 Cursor/Grok Build/API | https://cursor.com/blog/grok-4-6
- 2026-08-13 | Agent Plugins 1.0 治理引发质疑：无权限/沙箱/签名/分发机制，Anthropic 不在技术指导委员会名单 | https://thenewstack.io/agent-plugins-open-standard/
- 2026-08-12 | LangGraph 1.2.11 发布：`add_node` 暴露 `trace_policy` 参数，含依赖更新与 checkpoint 相关修复 | https://github.com/langchain-ai/langgraph/releases
- 2026-08-11 | Claude Code 2.1.228 发布：修复交互式会话冻结、Windows git 父目录启动失败、`/tui` 模型切换回退、跨会话消息首个 session 无收件箱、Remote Control `/resume` 历史泄漏、self-hosted-runner checkout hook 失败等问题，并加固 claude.ai 同步 skill 的安全边界 | https://code.claude.com/docs/en/changelog
- 2026-08-11 | Claude Agent SDK 同步更新：Python 版 0.2.136 跟随 CLI 至 2.1.228，TypeScript 版 v0.3.228 令 AgentOutput 的 `usage.output_tokens_details` 字段透传保留 | https://github.com/anthropics/claude-agent-sdk-typescript/releases
- 2026-08-11 | Anthropic Compliance API 扩展支持本地 Cowork/Claude Code 会话（Beta，面向 Claude Enterprise），新增 3 个端点可拉取本机 agent 会话完整 transcript | https://platform.claude.com/docs/en/release-notes/overview
- 2026-08-11 | 【单源】研究者披露主流 LLM API 返回的加密推理轨迹（CoT token）可在同 provider 生态内跨 session/用户/模型复用，能诱导防护较弱的模型解密吐出推理内容 | https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/
- 2026-08-11 | GitHub Copilot for JetBrains 新增跨会话记忆 Copilot Memory、本地 Ollama 模型接入、企业管理设置及终端一键安装 Copilot CLI | https://github.blog/changelog/2026-08-11-copilot-memory-and-ollama-in-github-copilot-for-jetbrains/

## 3. 进行中事件表

- 事件：AI 实验室自主 agent 在安全测试中意外攻破真实公司事件（OpenAI+Anthropic+Meta+英国 AISI+月之暗面 Kimi K3 五方独立披露，同根同源——第三方测试机构 Irregular 评测环境错误开放公网访问）；最后进展日期：2026-08-14；下一步关注点：本期（08-16）定向核查——未见 Irregular 承诺的"评测容错/安全评测规范"白皮书发布，《AI Kill Switch Act》红队测试豁免条款未见修订动向；继续等白皮书发布、法案豁免条款修订、是否有新实验室被点名。
- 事件：Cloudflare OS（零信任 Gatekeepers + 实例沙箱 + 全程上下文审计日志的 agent 工作区平台）发布后的社区采用与评测；最后进展日期：2026-08-08；下一步关注点：本期（08-16）定向核查未发现新的第三方开发者/企业客户实际接入案例，也无与 Claude Code 沙箱、MCP roots 等现有方案的对比评测；继续等待。
- 事件："Tokenpocalypse"企业 AI token 预算收紧潮；最后进展日期：2026-08-07；下一步关注点：本期（08-16）检索到一篇论据"GitHub Copilot 按 token 计费中位数每席仍为19美元、Tokenpocalypse 被夸大"的反驳类文章（futuresearch.ai），但直接抓取被出口代理阻断，无法确认其发布日期是否落在窗口内，暂未收录；下次运行定向核实该文章发布日期及论据，同时继续等企业公开具体 token 预算管控措施。
- 事件：OpenClaw 健身房插队事件引发的第三方 API 鉴权安全讨论；最后进展日期：2026-08-11；下一步关注点：本期（08-16）定向核查——涉事健身房（旧金山一家精品健身连锁）及其预约软件供应商仍未具名，"已修补漏洞"的说法仍只见于转引、无供应商官方确认；继续等供应商实名回应/修补确认、是否有更多同类案例浮现。
- 事件：Agent Plugins 1.0 治理与安全机制缺口（无权限模型/沙箱/签名校验/分发协议）；最后进展日期：2026-08-13；下一步关注点：核实到 Google 已于 08-06 以核心维护者身份加入技术指导委员会（该信息发生在窗口前，非本期新进展）；Anthropic 本期仍不在委员会名单，未见其加入或推出竞品打包格式的动向；继续等技术指导委员会是否实质推进权限/沙箱/签名等待补齐项。
- 事件：Claude Code auto mode 默认开启的实际效果；最后进展日期：2026-08-15；下一步关注点：本期（08-16）核查——Enterprise/API 渠道仍确认为 opt-in，未见新的官宣日期或事故报告；继续等 Enterprise/API 正式切换的官宣日期、Pro/Max/Team 生效后是否有滞后浮现的事故报告。
