# 🛠️ 开发工具更新周报 · 2026-10-26

> 覆盖窗口：2026-10-20 02:05 UTC 至 2026-10-26 08:25 UTC（常规）

今日要闻：VS Code 1.143 正式版将 Copilot harness 设为新会话默认后端并推出多模型并行对比、本地运行 MAI Code 1.1 Flash 及闲置 worktree 清理工具；Anthropic 开放主动式自主智能体应用 Claude Duet 研究预览，并连续发布 Claude Code v2.1.305 至 v2.1.310 更新强化沙箱安全、OpenTelemetry 审计与云会话企业权限管控。

## VSCode 更新

- 【续报】VS Code 1.143 正式版（10-22）及 1.143.1 补丁发布，正式将基于 Copilot SDK 的 Copilot harness 设为新会话默认后端（支持编辑器与 Agents 窗口无缝后台切换），并在编辑器 `New Chat (+) > Canvas` 菜单开放直接启动已安装扩展提供的 Agent Canvases，同时在空侧边栏与实验性 Session Activity Bar 中集成 Canvas 快捷入口。来源：VS Code 官方发布说明 https://code.visualstudio.com/updates/v1_143
- VS Code 1.143 在 Agents 窗口新增 Compare Models 多模型并行对比功能（预览，通过 `sessions.chat.compareAgents.enabled` 开启），支持同时混用 Copilot、Claude 与 Codex harness 及不同推理档位独立执行同一任务，并可选定 Judge 模型按耗时、token 与验证证据打分及一键融合（Synthesize）最优方案。来源：VS Code 官方发布说明 https://code.visualstudio.com/updates/v1_143
- VS Code 1.143 新增多项实验性与预览能力：支持在配备 96GB 以上显存 NVIDIA GPU 的设备上本地运行 MAI Code 1.1 Flash 模型（`chat.copilot.localModel.enabled`）、在 Voice Mode 中通过 BYOK 接入自有 OpenAI 实时语音模型（`agents.voice.useBYOKVoiceModel`）、清理非活跃 Agent 会话 worktree 回收磁盘空间，以及在多文件 Diff 编辑器中提供改动文件总览与 Keep/Discard 分级回滚。来源：VS Code 官方发布说明 https://code.visualstudio.com/updates/v1_143
- VS Code 1.143 强化 Agent 沙箱与企业管控：为 Windows 与 macOS Agent 宿主新增沙箱凭证代理 CA 证书信任管理（`Sandbox: Manage Trusted CA`）、允许在企业策略许可下按单会话临时关闭终端沙箱、支持托管插件与受信仓库插件后台静默安装，并在 Windows/Linux/macOS 安装流程中集成 GitHub Copilot CLI 引导安装。来源：VS Code 官方发布说明 https://code.visualstudio.com/updates/v1_143

## Claude App 更新

- Anthropic 于 10-21 面向美国 Pro 与 Max 订阅用户开放新应用 Claude Duet 研究预览（候补名单制），支持 Claude 作为主动式智能体（proactive agent）主动梳理待办任务、在用户离开期间后台自主推进长周期工作，并仅在需要关键决策时向用户发起确认。来源：Claude 官方博客 https://claude.com/blog/claude-duet
- Claude Code v2.1.305（10-20）与 v2.1.306（10-21）新增 Linux/WSL2 下的 `sandbox.allowNestedUserNamespaces` 配置以允许沙箱内运行无头 Chromium 与 rootless Podman，新增 `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS`，修复 Vertex/Bedrock 及网关拒绝 `ToolSearch` 时请求全败的回归问题与 `claude -p` 在云会话中误报未登录问题，并为 Code Review 新增 `@claude review stop`（及 `off`/`pause`）指令以终止 PR 持续审查订阅。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.305
- Claude Code v2.1.307（10-21）新增 `/claude-api api-version` 命令协助将代码迁移至 `2026-10-21` API 规范，新增记录权限规则、自动模式、hook 或沙箱拦截/提示工具调用的 `claude_code.safety_event` OpenTelemetry 审计事件，改进并行的 fork 子 Agent 身份隔离，并修复 HTTP MCP 非幂等工具断连重发两次及大量 PDF/图片读取引发的自动压缩抖动问题。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.307
- Claude Code v2.1.309（10-22）集中修复多项沙箱与权限安全边界（含阻止沙箱命令与自动编辑篡改 `--mcp-config` 配置文件、修复 macOS 沙箱 `denyWrite` 经符号链接绕过及 shell 启动文件在沙箱外执行问题），将 `claude ultrareview` 改为强制要求工作区信任（脚本需传 `--trust-workspace`），并将 VS Code 插件聊天面板每次编辑后的诊断等待时间由 1–1.5 秒缩短至 0.75 秒。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.309
- Claude Code v2.1.310（10-23）在 Bedrock、Vertex、Foundry 及禁用遥测环境下全面开放 Monitor 工具与插件监控，将企业版云会话（Cloud sessions）与远程控制（Remote Control）权限纳入 Enterprise 自定义角色（Custom Roles）细粒度管控，修复网关拒绝 `effort-2025-11-24` beta 头或中途系统消息时的请求失败，并优化超长 base64/SVG 会话压缩策略。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.310

## 生态与社区动向

- Anthropic 在 10 月下旬行业大会期间宣布将源自 Claude Code 的开放工作流标准 Agent Skills（基于 `SKILL.md` 目录结构）正式捐赠给 Linux 基金会旗下的 Agentic AI Foundation（AAIF），与 MCP 协议协同推进跨 VS Code、Claude Code、Cursor 等平台的厂商中立智能体技能互通。来源：Linux Foundation https://www.linuxfoundation.org
- Claude Code CLI（需 v2.1.304+）与 MCP 生态落地对 MCP Tasks 与 Elicitations 的原生支持，将单次请求/响应式的 MCP 调用扩展为可通过任务句柄轮询与中断的持久异步工作流（MCP Tasks），并允许 MCP Server 在任务中途安全暂停以向终端用户交互式索取缺失参数或登录授权（Elicitations）。来源：Model Context Protocol https://modelcontextprotocol.io
- Microsoft 发布基于 ASP.NET Core 构建的官方 MCP C# SDK 2.0，对齐最新 MCP 规范将 Streamable HTTP 服务端默认设为无状态（stateless-by-default）架构以简化云原生水平扩缩容。来源：InfoQ https://www.infoq.com
