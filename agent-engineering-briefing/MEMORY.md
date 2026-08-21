# MEMORY

## 1. 本次运行

- 运行时刻：2026-08-21
- 实际覆盖窗口：2026-08-20 至 2026-08-21（距上次运行约1天，正常增量滚动）
- 备注：6个方向均已检索。"Agent/Skill 设计模式""Prompt 与 Context 工程""案例与最佳实践复盘""社区热议与争议"四个方向本期未定位到落在窗口内、够格的实质新内容（Google ADK Skills 指南发布于08-13，落在窗口外；Simon Willison 08-20 文章聚焦 GEO/搜索流量追踪，非 agent 构建方法论；多 agent 编排/eval 相关检索结果均为常青内容或早于窗口），四节整节省略，非检索失败。"开发者工具与工作流"收2条（Claude Code 2.1.238、Google Antigravity CLI 1.1.17，均08-20发布）；"模型能力与 API 更新"收1条（Anthropic 08-20 新一轮稳定性事件，已交叉多个独立信源核实时间线）。官方源 code.claude.com/changelog、GitHub antigravity-cli releases 直接 WebFetch 核实通过；status.anthropic.com/status.claude.com/statusgator.com/unite.ai 被出口代理拦截，故障事件改用 WebSearch 多方聚合信源交叉确认时间线一致。对进行中事件表5项均做定向核查，详见第3节；"Tokenpocalypse"企业 token 预算收紧潮因连续14天（08-07至08-21）无窗口内新进展，按规则移出跟踪表。

## 2. 已报条目清单（保留最近 14 天）

- 2026-08-21 | Claude Code 2.1.238（08-20）新增 keybindingFlavor=readline 快捷键风格、插件市场 headersHelper、自托管 runner --defer-shutdown-max-min 与代理鉴权刷新参数，修复长会话内存无界增长、输出风格漂移 | https://code.claude.com/docs/en/changelog
- 2026-08-21 | Google Antigravity CLI 1.1.17（08-20）将 agent 执行 harness 合并为单一执行路径提升行为一致性，修复斜杠命令消失、Vim 模式 Enter 冲突、Ogg 附件 MIME 识别错误 | https://github.com/google-antigravity/antigravity-cli/releases
- 2026-08-21 | Anthropic 08-20 发生新一轮错误率升高事件（19:16 UTC通告，实际影响20:14-20:38 UTC约24分钟，claude.ai/API/Claude Code/Cowork同时受影响），另有独立的 Google 连接器故障（18:32-19:01 UTC） | https://statusgator.com/services/anthropic/outage-history
- 2026-08-20 | Claude Code 2.1.236（08-19）新增 ANTHROPIC_DEFAULT_MODEL、跨会话 notify_when_idle 空闲通知、收紧 macOS 通配符只读拒绝沙箱规则，并含 auto mode 专项改动（Monitor 规则搁置、云端分类器对齐、git 状态检查加固） | https://code.claude.com/docs/en/changelog
- 2026-08-20 | Claude Code 2.1.237（08-20）修复 LLM 网关/自定义 base URL 会话的 prompt caching 失效，新增内置 Concise 输出风格 | https://code.claude.com/docs/en/changelog
- 2026-08-20 | Cursor 08-19 云端 Agent 常驻化：Subscriptions（PR/Slack/定时唤醒）、/goal 跨会话长期目标、子 Agent 隔离 VM+干净项目副本、引导消息排队 | https://cursor.com/changelog/08-19-26
- 2026-08-20 | Simon Willison 08-19 实测 smolvm 1.8.3 作不可信 Python/JS 代码沙箱：硬件隔离 VM、冷启 0.6-1.5s/热执行约50ms、无网络+资源限额+只读输入挂载均按预期生效 | https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/
- 2026-08-20 | Anthropic 08-19 Agent Skills 与 Skills API（/v1/skills）正式 GA，移除 skills-2025-10-02 beta header 要求 | https://platform.claude.com/docs/en/release-notes/api
- 2026-08-20 | Anthropic 08-19 Files API 正式 GA，移除 files-api-2025-04-14 header，GA 响应格式变化（expires_in_seconds、page/next_page+ids[] 分页、1TB/组织、500 req/min） | https://platform.claude.com/docs/en/release-notes/api
- 2026-08-20 | Anthropic 08-19 Managed Agents web_search/web_fetch 新增 allowed_domains/blocked_domains 域名管控、max_content_tokens、user_location，自托管沙箱会话可挂载 memory store | https://platform.claude.com/docs/en/release-notes/api
- 2026-08-20 | Anthropic 08-19 Opus5/Haiku4.5 错误率升高事件（约09:42-11:02 UTC），为本周第五起稳定性事件 | https://statusgator.com/services/anthropic/outage-history
- 2026-08-20 | Simon Willison 08-19 撰文：编码 agent 侵蚀软件概念完整性（conceptual integrity），瓶颈从打字速度转向团队认知负荷 | https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/
- 2026-08-19 | Claude Code 2.1.235 发布：修复语言服务器重连导致的全量 prompt cache 失效、SendMessage 提前拒绝过大跨会话消息、优化云端后台会话内存与CPU占用、上下文用满提示 auto-compact 状态 | https://code.claude.com/docs/en/changelog
- 2026-08-19 | Anthropic 08-18 发生 Opus5/Sonnet5/Mythos5/Fable5/Haiku4.5 错误率升高故障，16:11-18:23 UTC 修复，为当周第四次稳定性事件 | https://startupfortune.com/claude-ai-suffers-widespread-outage-across-all-its-models-on-august-18/
- 2026-08-19 | Irregular 首次公开解释实验室 agent 意外攻破真实公司事件根因为"人为疏忽"（评测用虚构公司名撞真实域名），白皮书未发布 | https://cyberscoop.com/irregular-ai-sandbox-escape-human-oversight/
- 2026-08-18 | Claude Code 2.1.234 发布：新增用量限额重置后自动续跑开关，修复 auto mode 长会话 /compact 后误判沙箱联网权限、后台 subagent 权限确认被静默丢弃 | https://code.claude.com/docs/en/changelog
- 2026-08-18 | Anthropic 08-17 发生 Opus5/Sonnet5/Mythos5/Fable5 错误率升高故障，约1.5小时修复，为当周第三次稳定性事件 | https://status.anthropic.com/incidents/72f99lh1cj2c
- 2026-08-17 | 分析师指出前沿模型正用"内嵌知识"换"推理效率"（GLM-5.2/Qwen 3.5 高 AIME 低 SimpleQA），推论"小型本地模型+检索"已优于内嵌知识方案，登 HN 热榜 | https://w4g1.dev/blog/models-are-getting-dumber-on-purpose
- 2026-08-17 | Simon Willison 实测 Qwen 3.8 27B 默认 reasoning effort 过高导致简单任务思考21分钟，建议部署时显式调低 | https://simonwillison.net/2026/Aug/16/qwen-38-27b/
- 2026-08-17 | Cursor 将 "Builds"（环境快照复用+故障隔离）设为所有 Cloud Agent 环境默认机制，冷启动提速约3倍 | https://cursor.com/blog/builds
- 2026-08-17 | Anthropic 08-16 发生约36分钟多服务同时故障，claude.ai/Console/API/Claude Code/Cowork 鉴权与推理同时受影响 | https://status.anthropic.com/incidents/x6kvdyjgzxb2
- 2026-08-16 | Hacker News 热帖讨论"为什么 Opus 5 用起来更难受"，开发者反映风格漂移，作为多 agent 编排上级时易误判范围/把未完成报告为已完成 | https://news.ycombinator.com/item?id=49296740

## 3. 进行中事件表

- 事件：Claude Code auto mode 默认开启的实际效果；最后进展日期：2026-08-20；下一步关注点：本期（08-21）定向核查——Pro/Max/Team 自08-14起已默认开启；Enterprise/API/AWS/GCP/Foundry 仍为 opt-in，官方口径仍是"计划一个月内切换默认"（即约09-14前后），未见具体官宣日期；继续等正式切换官宣日期与是否有滞后问题浮现。
- 事件：AI 实验室自主 agent 在安全测试中意外攻破真实公司事件（五方独立披露，同根同源——第三方测试机构 Irregular 评测环境错误开放公网访问）；最后进展日期：2026-08-19；下一步关注点：本期（08-21）定向核查——Irregular 承诺的评测容错/安全评测规范白皮书仍未发布；未发现新进展；继续等白皮书发布、法案豁免条款修订、新实验室点名。
- 事件：MCP 跨通道注入技术"GhostSplice"（恶意 MCP server 将指令拆分到 tool schema/description/结果三通道，仅在 agent 同时读入三者时拼接生效，可致 SSH key/.env 泄露）；最后进展日期：2026-08-11（ASSET Research Group 原始披露）；下一步关注点：本期（08-21）核查确认仍无更新——仍无 CVE 编号（待协调披露）、无新厂商回应、无 MCP client 侧防御方案或协议层规范更新；继续等 CVE/防御方案/新厂商回应。
- 事件：Cloudflare OS（零信任 Gatekeepers + 实例沙箱 + 全程上下文审计日志的 agent 工作区平台）发布后的社区采用与评测；最后进展日期：2026-08-14；下一步关注点：本期（08-21）定向核查——仍为 early access，无 GA 时间表，未发现新的第三方开发者/企业接入案例；若到 08-25 仍无新进展将移出。
- 事件：OpenClaw 健身房插队事件引发的第三方 API 鉴权安全讨论；最后进展日期：2026-08-11；下一步关注点：预约软件供应商真实身份与官方回应仍未确认；连续追踪已近上限，若 08-25 前仍无供应商实名回应/修补确认将移出。
