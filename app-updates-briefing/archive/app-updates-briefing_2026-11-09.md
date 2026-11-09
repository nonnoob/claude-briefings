# 🛠️ 开发工具更新周报 · 2026-11-09

> 覆盖窗口：2026-11-06 16:22 UTC 至 2026-11-09 21:50 UTC（常规）

今日要闻：Anthropic 发布新一代旗舰技术模型 Claude Fable 5.2 与受控准入的 Claude Mythos 5.2（生成速度提升 30%、API 定价下调 20%），Claude Code 连续更新 v2.1.319 至 v2.1.321 将 Fable 5.2 设为默认 Fable 模型并支持终端后台 MCP 任务与无人值守自动拒绝权限配置。

## VSCode 更新

- 【续报】VS Code 于 11 月 6 日发布 1.145.2 稳定版维护补丁（Commit `c4453f8`，Milestone `#469`），针对 1.145 正式版上线后的远程 Agent 会话、交互式 Canvases、Cron 本地自动化调度与窗口状态刷新等稳定性及回归问题提供热修复。来源：Microsoft https://code.visualstudio.com/updates/v1_145 https://github.com/microsoft/vscode/releases/tag/1.145.2
- 【续报】VS Code 1.146 Insiders 预览分支在符合条件的模型选择器中为 Compare Models（多模型对比）引入一次性实验性 Spotlight 引导提示（`#345917`），并将 Git Worktree 清理工作流的进度与结果直接内联至主列表展示而移除独立结果分区（`#345628`）。来源：Microsoft https://code.visualstudio.com/updates/v1_146
- GitHub 于 11 月 6 日更新 Copilot Code Review，支持通过 REST 与 GraphQL API 从企业策略到单仓库粒度管理代码审查配置，在 API 响应中新增显式归因字段、审查 effort 档位及所引用的 Agent Skills、MCP 服务器或自定义指令元数据，并精简审查概览评论格式。来源：GitHub https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates/

## Claude App 更新

- Anthropic 于 11 月 9 日发布旗舰技术与推理模型 Claude Fable 5.2（`claude-fable-5-2`）及面向网络安全与生命科学验证计划准入的同架构模型 Claude Mythos 5.2；Fable 5.2 全面登陆付费订阅计划、Claude Code 与 API，支持 1M 上下文窗口与最高 128K 输出，生成速度较 Fable 5.1 提升最高 30%，API 标准定价下调 20% 至输入 $8/百万 token、输出 $40/百万 token（缓存读取 $0.20/百万 token），并提供最高 2.5 倍提速的可选 Fast Mode（$16/$80 每百万 token）。来源：Anthropic https://www.anthropic.com/news/introducing-claude-fable-5-2-and-claude-mythos-5-2 https://platform.claude.com/docs/en/models/claude-fable-5-2
- 【续报】Claude Code v2.1.320 与 v2.1.321 于 11 月 7 日发布，将 `claude-fable-5-2` 设为默认 Fable 模型（Pro/Max 档位已保存的 `claude-fable-5-1` 配置自动迁移至 `fable` 别名），为 `claude remote-control` 新增 `--settings <file>` 统一会话配置参数，修复 MCP OAuth 重定向向外部主机泄露刷新令牌、只读 Bash 命令绕过沙箱免提示执行及 `cp`/`mv` 写入目录绕过拒绝规则等安全漏洞，并修复 UNC/WSL/`/net` 网络路径下 `Edit` 与 `NotebookEdit` 异常改写问题。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.321 https://github.com/anthropics/claude-code/releases/tag/v2.1.320
- Claude Code v2.1.319 于 11 月 6 日发布，支持在终端将 MCP 任务型工具调用（MCP Tasks）自动转入后台执行并在完成后回调（可通过 `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND=1` 关闭），新增无人值守场景自动拒绝需交互确认工具调用的 `permissions.denyInsteadOfPrompting` 配置与 `/claude-api latency-optimize` 延迟诊断命令，收紧关闭遥测或特性开关及自定义网关下的 Auto Mode 服务端校验（未校验调用改为询问或拒绝，`claude -p` 拒绝时退出码改为 `1`），并修复多项 Bash 环境前缀与 git worktree 沙箱逃逸漏洞。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.319
- 【续报】Anthropic 于 11 月 6 日面向 Claude Enterprise 推出项目成本标签 Project Tags（Beta），支持为项目配置最多 16 个内部成本代码或客户事项编号（如 `cost_code`、`client_matter`）以通过设置面板或 API 追踪项目聊天、Claude Desktop（需 v3.6556.1+）本地 Cowork 任务及 Claude Code（需 v2.1.305+）会话支出；Claude Desktop 3.6556.x 同步完成深色主题、对比度与聊天气泡布局重构。来源：Anthropic https://support.claude.com/en/articles/track-spend-by-cost-code-with-project-tags https://support.claude.com/en/articles/12138966-release-notes
- Anthropic 为 Claude Developer Platform 上线组织级 IP 白名单（IP Allowlisting，Beta），支持在 Claude Console 配置最多 1,000 条 IPv4/IPv6 地址或 CIDR 网段规则，对控制台及 Messages、Skills、Managed Agents、Admin 与 Compliance API 等核心端点拦截非白名单公网请求并返回 `403 permission_error`。来源：Anthropic https://platform.claude.com/docs/en/release-notes/overview

## 生态与社区动向

- 随 Claude Fable 5.2 发布，AWS（Amazon Bedrock 与 Claude Platform on AWS，结构化模型 ID `global.anthropic.claude-fable-5-2`）、Google Cloud Vertex AI 与 Microsoft Foundry 于 11 月 9 日同步上线 Fable 5.2 托管服务及可选 Fast Mode，支持企业结合云原生合规边界与 Claude Code `/claude-api migrate` 命令迁移工程与智能体工作流。来源：AWS https://aws.amazon.com/blogs/aws/introducing-claude-fable-5-2-on-aws/ https://platform.claude.com/docs/en/models/claude-fable-5-2
