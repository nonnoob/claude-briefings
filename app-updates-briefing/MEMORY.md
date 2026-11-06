# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻及检索截止：2026-11-06 16:22 UTC（2026-11-06 08:22 PST）。
- 上次运行时刻：2026-10-31 11:32 UTC。
- 实际覆盖窗口：2026-10-31 11:32 UTC 至 2026-11-06 16:22 UTC（常规）。
- 三方向均已完整检索：核实收录 VS Code 1.145（及 1.145.1）正式版、VS Code 1.146 Insiders、Claude Code v2.1.317/v2.1.318、Claude Enterprise Inference Hooks GA 与 Security Center Beta、Claude Desktop v3.1623.0+ `/storage` 存储管理、claude.ai Personal Finance Beta、Microsoft Copilot Claude 模型纳入欧盟数据边界，以及 MCP 技能扩展规范 SEP-2640 定稿与安全厂商接入 Inference Hooks。

## 2. 已报条目清单（最近 21 天）

- 2026-10-16 | Claude Code v2.1.302 发布，在 claude -p、Agent SDK、VS Code 插件与桌面端默认启用 fork 子 Agent，新增 CLAUDE_CODE_AUTO_MODE_MODEL，并修复额度计费下自动提示词建议误扣额度问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.302
- 2026-10-18 | Claude Code v2.1.304 发布，支持 Code Review 审查级别配置与组织级批量仓库策略、mod tool.check 新增 decider: "person"，修复 claude --worktree 退出时未经确认误删分支问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.304
- 2026-10-19 | VS Code 1.143 Insiders 新增新建聊天菜单 Canvas 子菜单、.mcp.json 环境变量展开，并修复便携模式 CLI 状态路径问题 | https://code.visualstudio.com/updates
- 2026-10-21 | Anthropic 面向美国 Pro 与 Max 用户开放主动式智能体应用 Claude Duet 研究预览（候补名单制） | https://claude.com/blog/claude-duet
- 2026-10-21 | Claude Code v2.1.305 与 v2.1.306 发布，新增 Linux 沙箱嵌套用户命名空间支持、修复 Vertex/Bedrock 网关拒绝 ToolSearch 请求失败，并新增 @claude review stop 指令 | https://github.com/anthropics/claude-code/releases/tag/v2.1.305
- 2026-10-21 | Claude Code v2.1.307 发布，新增 /claude-api api-version（迁移至 2026-10-21）与 claude_code.safety_event OpenTelemetry 安全审计事件 | https://github.com/anthropics/claude-code/releases/tag/v2.1.307
- 2026-10-22 | VS Code 1.143 及 1.143.1 正式版发布，将 Copilot harness 设为新会话默认后端，新增 Compare Models 多模型对比（预览）、本地运行 MAI Code 1.1 Flash、worktree 空间回收及沙箱 CA 证书管理 | https://code.visualstudio.com/updates/v1_143
- 2026-10-22 | Claude Code v2.1.309 发布，修复多项沙箱与符号链接权限绕过漏洞，claude ultrareview 强制要求工作区信任，VS Code 编辑诊断等待缩至 0.75 秒 | https://github.com/anthropics/claude-code/releases/tag/v2.1.309
- 2026-10-23 | Claude Code v2.1.310 发布，在 Bedrock/Vertex/Foundry 开放 Monitor 工具，并为 Enterprise 自定义角色新增云会话与远程控制权限管控 | https://github.com/anthropics/claude-code/releases/tag/v2.1.310
- 2026-10-23 | Anthropic 将 Agent Skills 开放标准捐赠给 Linux 基金会 AAIF；Claude Code 原生支持 MCP Tasks 与 Elicitations；微软发布默认无状态的 MCP C# SDK 2.0 | https://www.linuxfoundation.org
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
- 2026-11-06 | MCP 技能扩展规范 SEP-2640（io.modelcontextprotocol/skills）正式定稿并在 VS Code 1.146 Insiders 落地，1.146 Insiders 同时升级 Compare Models 分组与 Agent 自动发起多模型对比 | https://code.visualstudio.com/updates/v1_146

## 3. 进行中事件表

- 事件：VS Code Agent 会话、Canvases、Compare Models 与改动审核；最后进展日期：2026-11-06；下一步关注点：1.145 已支持远程 Agent 应用预览与远程 Canvases（仍为预览版），1.146 Insiders 已支持 Compare Models 分组集合与 Agent 自动发起对比，后续核实 Canvases 何时转 GA、Compare Models 何时支持 Dev Containers，以及 Keep/Undo 实验性工作集何时覆盖终端命令改动。
- 事件：Anthropic 上线 Claude Dashboards（付费计划 Beta）与 Claude Motion（Team/Enterprise Beta），同时宣布独立站点 `claude.ai/design` 将于 2026-12-14 停服下线；最后进展日期：2026-10-16；下一步关注点：核实 Claude Dashboards 与 Claude Motion 何时扩展覆盖范围或由 Beta 转 GA，以及 `claude.ai/design` 在 12 月 14 日停服关停前的迁移提醒与下线执行情况。
- 事件：Anthropic 开放主动式自主智能体应用 Claude Duet 研究预览（美国 Pro/Max 候补名单）；最后进展日期：2026-10-21；下一步关注点：关注 Claude Duet 何时结束候补名单全量开放或扩展至 Team/Enterprise 与非美地区。
- 事件：Opus 4.8 fast mode 移除与 Copilot Fusion 优惠截止；最后进展日期：2026-10-31；下一步关注点：11 月 30 日旧 fast mode 正式移除及 Copilot Fusion 30% 优惠结束前核对模型配置、收费变化与客户端迁移提示。
- 事件：Claude Enterprise 安全中心（Security Center）、父级组织管理控制台与 Personal Finance Beta；最后进展日期：2026-11-05；下一步关注点：关注 Security Center 与 `admin.claude.com` 集中管理控制台何时由 Beta 转 GA，以及 Personal Finance Beta 何时扩展至非美地区或更多计划。
- 事件：Microsoft Copilot 集成的 Claude 模型纳入欧盟数据边界（EU Data Boundary）；最后进展日期：2026-11-05；下一步关注点：微软计划于 2026 年底前完成落地，关注年底前正式上线公告及区域租户默认启用策略变化。
