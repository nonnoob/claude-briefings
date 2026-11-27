# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻及检索截止：2026-11-27 10:45 UTC。
- 上次运行时刻：2026-11-20（据归档）。
- 实际覆盖窗口：2026-11-20 至 2026-11-27（常规）。
- 方向覆盖：VS Code 更新页、Claude Code Releases、新闻检索已覆盖；生态与社区动向本期未单独检索。

## 2. 已报条目清单（最近 21 天）

- 2026-10-31 | VS Code 1.144 发布云端会话与 Cloud Automations 预览，云端不复制未提交本地改动 | https://code.visualstudio.com/updates/v1_144
- 2026-10-31 | Copilot Fusion GA，High/Max 受方案限制，参与模型分别计费 | https://code.visualstudio.com/updates/v1_144
- 2026-10-31 | Compare Models 对符合条件新会话默认启用但不支持 Dev Containers，Canvases 仍为预览 | https://code.visualstudio.com/updates/v1_144
- 2026-10-31 | Copilot harness 恢复实验性 Keep/Undo 工作集，终端命令改动不纳入 | https://code.visualstudio.com/updates/v1_144
- 2026-10-31 | Assisted permissions GA，要求 Folder isolation 并遵守组织策略 | https://code.visualstudio.com/updates/v1_144
- 2026-10-31 | Claude Code v2.1.311/312 修复规则缓存、动态 MCP 工具及 VS Code 登录后组织策略获取 | https://github.com/anthropics/claude-code/releases/tag/v2.1.312
- 2026-10-31 | Claude Code v2.1.314 为 VS Code/Desktop Code 标签页扩展空闲压缩并提供目录写入限制 | https://github.com/anthropics/claude-code/releases/tag/v2.1.314
- 2026-10-31 | Claude Code v2.1.316 支持子 Agent 独立 effort，公告 Opus 4.8 fast mode 11 月 30 日移除 | https://github.com/anthropics/claude-code/releases/tag/v2.1.316
- 2026-10-31 | VS Code 公布 Agent Host Protocol v1.0 与 WebSocket 接入库 | https://code.visualstudio.com/updates/v1_144
- 2026-11-03 | Claude Code v2.1.317 调整跨模型子 Agent effort 回退逻辑，新增账号邮箱外发隐私确认（cc-plugin-privacy）、Agent SDK hook onFailure: "block"、嵌套 claude -p 会话 ID 隔离并移除 Read 未变更文件占位简写 | https://github.com/anthropics/claude-code/releases/tag/v2.1.317
- 2026-11-03 | Claude Code v2.1.318 新增 claude.ai 登录过期时间字段与提前 10 天告警、支持云端无仓库会话与网关 Mantle 跨账号 assume_role，并修复 --continue 丢历史及共享网络主目录配置清空问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.318
- 2026-11-04 | VS Code 1.145 及 1.145.1 正式版发布，支持远程 Agent 应用预览与远程 Canvases（预览）、跨 harness 嵌套聊天会话、三档聊天详略度模式、本地自动化五字段 cron 调度及 files.exclude 细粒度保留 | https://code.visualstudio.com/updates/v1_145
- 2026-11-05 | Anthropic 宣布 Claude Enterprise 服务端推理钩子（Inference Hooks）正式转正（GA），上线 Security Center（Beta）与 admin.claude.com 父级组织集中管理控制台（Beta），以及 Check Point、Proofpoint、TrueFoundry 原生 Webhook 集成 | https://claude.com/resources/articles/claude-enterprise-security-updates
- 2026-11-05 | Anthropic 面向美国 Pro/Max/Ultra 用户推出基于 Plaid 只读连接的 Personal Finance（Beta），并为 Claude Desktop（v3.1623.0+）新增 /storage 磁盘空间管理面板与 Code 标签页远程受管策略状态提示 | https://support.claude.com/en/articles/12138966-release-notes
- 2026-11-05 | Microsoft 宣布将于 2026 年底前把 Microsoft Copilot 中集成的 Claude 模型纳入欧盟数据边界（EU Data Boundary） | https://www.microsoft.com/en-us/copilot/blog/2026/11/05/bringing-claude-models-in-microsoft-copilot-into-the-eu-data-boundary/
- 2026-11-05 | Anthropic 为 Claude Developer Platform 上线组织级 IP 白名单（IP Allowlisting，Beta），支持在 Claude Console 配置最多 1,000 条 IPv4/IPv6 或 CIDR 规则拦截非授权公网 API 请求 | https://platform.claude.com/docs/en/release-notes/overview
- 2026-11-06 | MCP 技能扩展规范 SEP-2640（io.modelcontextprotocol/skills）正式定稿并在 VS Code 1.146 Insiders 落地，1.146 Insiders 同时升级 Compare Models 分组、Agent 自动发起多模型对比、Spotlight 引导及 Worktree 清理列表内联 | https://code.visualstudio.com/updates/v1_146
- 2026-11-06 | VS Code 1.145.2 稳定版维护补丁发布，修复 1.145 远程 Agent 会话、Canvases 与本地自动化等回归问题 | https://github.com/microsoft/vscode/releases/tag/1.145.2
- 2026-11-06 | GitHub Copilot Code Review 新增 REST 与 GraphQL API 策略配置支持、显式审查归因与引用技能/MCP 元数据字段，并精简审查概览评论格式 | https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates/
- 2026-11-06 | Claude Code v2.1.319 发布，支持终端后台执行 MCP Tasks、新增 permissions.denyInsteadOfPrompting 与 /claude-api latency-optimize、收紧网关与无遥测下 Auto Mode 服务端校验并修复多项沙箱逃逸漏洞 | https://github.com/anthropics/claude-code/releases/tag/v2.1.319
- 2026-11-06 | Anthropic 面向 Claude Enterprise 上线项目成本标签 Project Tags（Beta），支持跨项目聊天、Claude Desktop（v3.6556.1+）本地 Cowork 与 Claude Code 按内部成本代码追踪支出，Claude Desktop 3.6556.x 同步重构界面主题布局 | https://support.claude.com/en/articles/track-spend-by-cost-code-with-project-tags
- 2026-11-07 | Claude Code v2.1.320 与 v2.1.321 发布，将 claude-fable-5-2 设为默认 Fable 模型，新增 claude remote-control --settings 参数，并修复 MCP OAuth 重定向令牌泄露、只读 Bash 绕过沙箱及网络路径文件编辑问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.321
- 2026-11-09 | Anthropic 发布旗舰模型 Claude Fable 5.2 与受控准入的 Claude Mythos 5.2（生成速度提升 30%、API 定价下调 20% 至 $8/$40 每百万 token，支持可选 Fast Mode），AWS Bedrock、Google Cloud Vertex AI 与 Microsoft Foundry 同步上线 Fable 5.2 | https://www.anthropic.com/news/introducing-claude-fable-5-2-and-claude-mythos-5-2
- 2026-11-10 | VS Code 1.145.3 维护补丁与 1.146.0 稳定版（11-11）在 GitHub 发布，特性清单未核实 | https://github.com/microsoft/vscode/releases/tag/1.146.0
- 2026-11-10 | Claude Code v2.1.322 为 Vertex 增加 fast mode | https://github.com/anthropics/claude-code/releases
- 2026-11-12 | Claude Code v2.1.323 发布实验性 Code Mode、插件版本范围限制并收紧 Bash 权限检查 | https://github.com/anthropics/claude-code/releases/tag/v2.1.323
- 2026-11-12 | Claude Meetings（Google Meet）Beta 面向 Team/Enterprise，另有 Whiteboards 与 Sheets Beta | https://support.claude.com/en/articles/12138966-release-notes
- 2026-11-12 | Claude Developer Platform 推出自托管 Claude Managed Agents | https://platform.claude.com/docs/en/release-notes/overview
- 2026-11-09 | Claude Fable 5.2 在 GitHub Copilot 正式可用（含 VS Code 模型选择器，需管理员启用策略） | https://letsdatascience.com/news/anthropics-claude-fable-52-reaches-general-availability-in-g-90d9b700
- 2026-11-18 | VS Code 1.147 稳定版发布 Send Later、Draft requests、Browser Use 预览、模型路由器与 Dev Container 聊天持久化，Skills over MCP 默认启用，管理员可放行 Claude/Codex harness | https://code.visualstudio.com/updates/v1_147
- 2026-11-18 | VS Code 1.147 弃用 macOS Ventura/Sonoma 与 32 位 ARM Linux 桌面版并移除状态栏 AI 用量统计 | https://code.visualstudio.com/updates/v1_147
- 2026-11-11 | VS Code 1.146 特性清单核实：Inbox 模式、聊天独立窗口、Copilot CLI /code 移交、Local harness 将于 2027 年 2 月移除 | https://code.visualstudio.com/updates/v1_146
- 2026-11-19 | Claude Code v2.1.325–v2.1.329 发布（zstd 安全修复、mcp add-json 标准输入、Opus/Sonnet 4.6 云平台 auto mode、/tasks 汇总、钥匙串登出修复） | https://github.com/anthropics/claude-code/releases
- 2026-11-17 | Claude Developer Platform 推出关联计费（Linked billing，Beta） | https://releasebot.io/updates/anthropic/claude
- 2026-11-17 | Claude Desktop 新增 Stable/Latest 更新通道 | https://releasebot.io/updates/anthropic/claude
- 2026-11-19 | Claude Meetings Beta 因需求高峰无法加入大量会议 | https://releasebot.io/updates/anthropic/claude
- 2026-11-25 | VS Code 1.148 稳定版发布（Agent 启动提速、keep-awake、远程 Dev Container 实验、Agent Host Protocol 1.1.0） | https://code.visualstudio.com/updates/v1_148
- 2026-11-23 | Anthropic 推出 Claude Ship（PR Steward、Claude Approvals Beta） | https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/
- 2026-11-24 | Claude/Claude Code 公测 Skills over MCP | https://cryptobriefing.com/anthropic-skills-over-mcp-claude-beta
- 2026-11-25 | Claude Desktop Beta 支持 Artifacts 安装为桌面应用 | https://www.macrumors.com/2026/11/25/claude-install-artifacts-desktop-apps/
- 2026-11-25 | Claude Code v2.1.330–2.1.332 发布（easel mod、Code Mode 扩展、MCP 技能入菜单、11-30 插件市场默认自动更新） | https://github.com/anthropics/claude-code/releases
- 2026-11-24 | Claude Desktop 月度回顾转正、/ship 上线 | https://releasebot.io/updates/anthropic/claude

## 3. 进行中事件表

- 事件：Claude Fable 5.2 与 Claude Mythos 5.2 发布及生态集成；最后进展日期：2026-11-09；下一步关注点：Claude Fable 5.2 已在 Claude 全平台、Claude Code（v2.1.320+ 默认 Fable 模型）及 AWS Bedrock、Vertex AI、Microsoft Foundry 上线，Copilot 已于 11-09 接入 Fable 5.2（待核实 GitHub 原文），后续关注 Mythos 5.2 验证计划与 Claude Security 企业功能扩展情况。
- 事件：VS Code Agent 会话、Canvases、Compare Models 与改动审核；最后进展日期：2026-11-18；下一步关注点：1.145.2 已完成首轮稳定性修复，1.146 Insiders 已支持 Compare Models 分组集合、Agent 自动发起对比与 Spotlight 引导，1.146 清单已核实、1.147（11-18）已发布，Canvases 仍为预览，后续关注 Canvases 何时转 GA、Compare Models 何时支持 Dev Containers、Keep/Undo 实验性工作集何时覆盖终端命令改动。
- 事件：Claude Enterprise 安全与治理套件（Security Center、父级组织管理控制台、Project Tags、Developer Platform IP Allowlisting）与 Personal Finance Beta；最后进展日期：2026-11-06；下一步关注点：关注 Security Center、`admin.claude.com` 集中管理控制台、Project Tags 成本标签与 IP Allowlisting 何时由 Beta 转 GA，以及 Personal Finance Beta 何时扩展至非美地区或更多订阅计划。
- 事件：Microsoft Copilot 集成的 Claude 模型纳入欧盟数据边界（EU Data Boundary）；最后进展日期：2026-11-05；下一步关注点：微软计划于 2026 年底前完成落地，关注年底前正式上线公告及区域租户默认启用策略变化。
- 事件：Opus 4.8 fast mode 移除与 Copilot Fusion 优惠截止；最后进展日期：2026-10-31；下一步关注点：11 月 30 日旧 fast mode 正式移除及 Copilot Fusion 30% 优惠结束前核对模型配置、收费变化与客户端迁移提示。
- 事件：Anthropic 开放主动式自主智能体应用 Claude Duet 研究预览（美国 Pro/Max 候补名单）；最后进展日期：2026-10-21；下一步关注点：关注 Claude Duet 何时结束候补名单全量开放或扩展至 Team/Enterprise 与非美地区。
- 事件：VS Code Local harness 弃用（2027 年 2 月移除）与 Claude/Codex harness 企业放行；最后进展日期：2026-11-18；下一步关注点：关注 1.148 是否新增迁移工具或调整移除日期，以及 `vscode.allowedHarnesses` 的企业落地反馈。
- 事件：Claude Ship（PR Steward、Claude Approvals Beta）与 Skills over MCP 公测；最后进展日期：2026-11-24；下一步关注点：关注二者何时转 GA 或扩展到 GitHub 以外平台。
