# 🛠️ 开发工具更新周报 · 2026-09-28

> 覆盖窗口：2026-09-18 17:10 UTC 至 2026-09-28 17:10 UTC（补漏：距上次运行超过10天封顶，窗口外的约6.5小时缺口仅收仍重要的大事）

## VSCode 更新

- VS Code 1.139 正式版发布，新增 Chat 会话进度可视化保留（实验性）、Copilot Agent 会话 `/sandbox-policy` 沙盒策略报告、Agent Host 专属横幅邀请并行工作会话、MCP 远程 URL 变量安装模板、F2 重命名会话标题等。来源：VS Code Updates https://code.visualstudio.com/updates/v1_139
- VS Code 1.139.1 补丁发布，修复托管设置（managed settings）在刷新失败时被清空的问题。来源：GitHub Releases https://github.com/microsoft/vscode/releases/tag/1.139.1

## Claude App 更新

- Anthropic 发布 Claude Opus 5.5：相比 Opus 5，典型工作负载成本降低约 40%、输出速度提升超 30%，定价降至 $4/$20 每百万 token（缓存读取降 60% 至 $0.20/MTok），性能对齐 Claude Fable 5.1；经 METR、Frontier Design 及 NIST CAISI 评估为 CB-1 能力级别（未达 CB-2）；同日 Claude Code v2.1.280 将其设为默认 Opus 模型。来源：Anthropic https://www.anthropic.com/claude-opus-5-5
- Claude Code v2.1.277 发布，新增 AGENTS.md（CLAUDE.md 替代方案）支持与 `/plugin install <plugin> --marketplace <source>`，修复 `claude -p`/SDK 会话报错后挂起、模型切换后扩展思维丢失、重复流事件导致工具调用执行两次等问题。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.277
- Claude Code v2.1.278 发布，Auto Mode 默认改用服务端分类器，避免额外计费的分类调用，并在 `/status` 新增 "Auto mode server" 状态行。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.278
- Claude Code v2.1.282 发布，修复含"不可解密"网页搜索结果的会话中全部请求报 400 错误的问题，以及续接/恢复会话重发旧消息、摘要被拒时压缩失败等问题。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.282
- Claude Code v2.1.283 发布，新增 `/doctor prompt-audit` 提示词模式审计、`availableModelsMatch`/`deniedModels` 托管设置，修复 SDK 会话丢失延迟工具调用、MCP 进度通知被丢弃等问题，并改善启动与首次回复延迟。来源：GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.283
- 【续报】Windows 09 月累积更新导致的 Cowork 沙盒 Plan9 挂载故障，Microsoft 于 09-14 发布紧急带外补丁 KB5129195/KB5129194 称已修复，但用户 09-19 报告打补丁重启后、全新会话首次挂载连接文件夹仍然失败，问题未完全解决。来源：GitHub Issues https://github.com/anthropics/claude-code/issues/95557

