# MEMORY

## 1. 本次运行

- 运行时刻：2026-08-18
- 实际覆盖窗口：2026-08-17 至 2026-08-18（距上次运行约1天，正常增量滚动）
- 备注：6个方向均已检索，本期窗口内信号偏薄——"Agent/Skill 设计模式""Prompt 与 Context 工程""案例与最佳实践复盘""社区热议与争议"四个方向未检索到落在窗口内、够格的实质新内容（检索结果大量为 2026 年通用型"最佳实践指南"类内容，无法定位到窗口内的具体发布事件），四节本期整节省略，非检索失败。"开发者工具与工作流""模型能力与API更新"各收录1条：前者为 Claude Code 2.1.234（08-17）发布，同时作为"auto mode 默认化效果"追踪事件的续报；后者为 Anthropic 08-17 的 Opus5/Sonnet5/Mythos5/Fable5 错误率升高故障（本周第三次稳定性事件）。对进行中事件表5项均做了定向核查，详见第3节；核查中发现一条关于 OpenClaw 健身房事件"供应商位于旧金山、已修补"的二手转引，与已核实的墨尔本事发地矛盾且无独立佐证，判断为不可靠未采信。另确认 MCP "GhostSplice" 跨通道注入技术原始披露日期为 2026-08-11（早于本期窗口），已通报的多家厂商中仅 OpenAI 安全团队回应，无 CVE 或新防御方案，继续留在进行中事件表跟踪、暂不计入正文。检索环境对多数域名（thehackernews.com、hamel.dev、status.anthropic.com、simonwillison.net 等）的直接 WebFetch 仍被出口代理阻断，全程改用 WebSearch 二手信源交叉确认后落盘。

## 2. 已报条目清单（保留最近 14 天）

- 2026-08-18 | Claude Code 2.1.234 发布：新增用量限额重置后自动续跑开关，修复 auto mode 长会话 /compact 后误判沙箱联网权限、后台 subagent 权限确认被静默丢弃两个问题 | https://code.claude.com/docs/en/changelog
- 2026-08-18 | Anthropic 08-17 发生 Opus5/Sonnet5/Mythos5/Fable5 错误率升高故障，约1.5小时修复，为本周内第三次服务稳定性事件 | https://status.anthropic.com/incidents/72f99lh1cj2c
- 2026-08-17 | 分析师指出前沿模型正用"内嵌知识"换"推理效率"（GLM-5.2/Qwen 3.5 高 AIME 低 SimpleQA），推论"小型本地模型+检索"已优于内嵌知识方案，登 HN 热榜 | https://w4g1.dev/blog/models-are-getting-dumber-on-purpose
- 2026-08-17 | Simon Willison 实测 Qwen 3.8 27B 默认 reasoning effort 过高导致简单任务思考21分钟，建议部署时显式调低 | https://simonwillison.net/2026/Aug/16/qwen-38-27b/
- 2026-08-17 | Cursor 将 "Builds"（环境快照复用+故障隔离）设为所有 Cloud Agent 环境默认机制，冷启动提速约3倍 | https://cursor.com/blog/builds
- 2026-08-17 | Anthropic 08-16 发生约36分钟多服务同时故障，claude.ai/Console/API/Claude Code/Cowork 鉴权与推理同时受影响 | https://status.anthropic.com/incidents/x6kvdyjgzxb2
- 2026-08-17 | 【续报】HN "Opus 5 更难用"讨论新角度：作为多 agent 编排"上级"时易误判范围、把未完成报告为已完成 | https://news.ycombinator.com/item?id=49296740
- 2026-08-17 | 【续报】Anthropic 工程师 Thariq 发布 Claude 水印采样机制技术拆解《Same Words, Different Dice》 | https://x.com/trq212/status/2087258090169414008
- 2026-08-16 | AI 研究者 Pliny the Liberator 拆解 Claude 隐形水印机制"输出本身就是水印"，Anthropic 工程师澄清模型自身无感知、无密钥访问权 | https://officechai.com/ai/popular-ai-jailbreaker-account-pliny-the-liberator-describes-how-anthropics-new-ai-watermark-could-work/
- 2026-08-16 | Hacker News 热帖讨论"为什么 Opus 5 用起来更难受"，开发者反映风格漂移（小题大做/废话多/答非所问），水印机制被列为猜测性成因之一但存在争议 | https://news.ycombinator.com/item?id=49296740
- 2026-08-14 | Claude Code 2.1.233 发布：GitLab MR 接入 --worktree 与 agents 视图、新增 forward_user_identity 网关设置、Linux Bash 工具 memory cgroup、WebFetch 缓存 TTL 环境变量，修复云端会话等待权限确认时被误标记为丢失的问题 | https://code.claude.com/docs/en/changelog
- 2026-08-14 | Anthropic 发布《善用你的 Claude Code 会话》实践指南：/clear 清上下文、模型与 effort level 开局锁定、@ 提及文件、静默命令输出、/context 巡检、/compact 先行等上下文工程清单 | https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions
- 2026-08-14 | 【续报】Claude Code auto mode 今日正式对 Pro/Max/Team 计划默认生效，取消该分类器额外计费，社区反应基调为"信心甚至过度自信"、未见安全事故 | https://claude.com/blog/auto-mode-default-in-claude-code
- 2026-08-14 | 【续报】Claude Code auto mode：Enterprise/API 渠道确认仍为 opt-in，预计一个月内跟进默认开启并同步免除分类器额外计费 | https://enterprisedna.co/resources/news/anthropic-claude-code-auto-mode-default-enterprise-august-2026/

## 3. 进行中事件表

- 事件：AI 实验室自主 agent 在安全测试中意外攻破真实公司事件（OpenAI+Anthropic+Meta+英国 AISI+月之暗面 Kimi K3 五方独立披露，同根同源——第三方测试机构 Irregular 评测环境错误开放公网访问）；最后进展日期：2026-08-14；下一步关注点：本期（08-18）定向核查——Irregular 承诺的评测容错/安全评测规范白皮书仍未发布，《AI Kill Switch Act》（Lieu/Moran 提出）红队测试豁免条款仍未见 markup 或修订动向；继续等白皮书发布、法案豁免条款修订、是否有新实验室被点名。
- 事件：Cloudflare OS（零信任 Gatekeepers + 实例沙箱 + 全程上下文审计日志的 agent 工作区平台）发布后的社区采用与评测；最后进展日期：2026-08-14；下一步关注点：本期（08-18）定向核查——公开版本仍处早期访问阶段，详细开发者文档/SDK/市场平台官方仍未给出发布时间表，未发现新的第三方开发者/企业客户实际接入案例；继续等待，若持续到 08-25 仍无新进展考虑移出。
- 事件："Tokenpocalypse"企业 AI token 预算收紧潮；最后进展日期：2026-08-07；下一步关注点：本期（08-18）定向核查未发现窗口内新的企业具体 token 预算管控措施公开案例；继续单纯关注是否有企业在窗口内公开新的具体管控动作。
- 事件：OpenClaw 健身房插队事件引发的第三方 API 鉴权安全讨论；最后进展日期：2026-08-11；下一步关注点：本期（08-18）定向核查——发现一条声称"供应商为旧金山某精品健身连锁、已修补"的二手转引，但与此前已核实的事发地墨尔本矛盾、且无独立信源佐证，判断为不可靠未采信；预约软件供应商真实身份与官方回应仍未确认；继续等供应商实名回应/修补确认。
- 事件：Claude Code auto mode 默认开启的实际效果；最后进展日期：2026-08-17；下一步关注点：本期已在正文续报——2.1.234 修复了 auto mode 默认化后暴露的两个可靠性问题（长会话联网权限误判、后台权限确认被静默丢弃），是首次出现的针对性事故修复；继续等 Enterprise/API 正式切换的官宣日期、是否还有其他滞后浮现的问题。
- 事件：MCP 跨通道注入技术"GhostSplice"（恶意 MCP server 将指令拆分到 tool schema/description/结果三个通道，单一过滤器/拒答均无法单独识别，仅在 agent 同时读入三者时才会拼接生效，可致 SSH key/.env 等密钥泄露）；最后进展日期：本期（08-18）确认原始披露日期为 2026-08-11（ASSET Research Group，早于本期窗口）；下一步关注点：已通报的厂商中目前仅 OpenAI 安全团队回应（称文档已警示第三方 MCP server 风险），尚无 CVE 编号或 MCP client 侧防御方案/协议层规范更新发布；继续等待防御方案或新厂商回应，届时视情况续报或作为新条目首次收录。
