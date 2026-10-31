# 🛠️ 开发工具更新周报 · 2026-10-31

> 覆盖窗口：2026-10-26 08:25 UTC 至 2026-10-31 11:32 UTC（常规）

今日要闻：VS Code 1.144 扩展云端会话与多模型工作流，Keep／Undo 已恢复但仍属实验功能，且不涵盖终端改动。

## VSCode 更新

- 【续报】VS Code 1.144 于 10 月 28 日发布，可从编辑器或 Agents 窗口启动云端会话，并提供 Cloud Automations 预览；云端会话需要付费 Copilot 权限且受组织策略约束，本地未提交改动不会自动复制过去。来源：Microsoft https://code.visualstudio.com/updates/v1_144
- Copilot Fusion 在 VS Code 正式可用，提供 Standard、High、Max 档位，其中 High／Max 限符合条件的付费方案；参与模型分别按标准费率计费，公告中的 30% 优惠截至 11 月 30 日，不能按单模型请求估算总成本。来源：Microsoft https://code.visualstudio.com/updates/v1_144
- 【续报】Compare Models 对符合条件的新会话默认启用并支持无文件夹／空仓库场景，但不支持 Dev Containers；Agent Canvases 仍为预览版，本轮主要改善发现与管理入口。来源：Microsoft https://code.visualstudio.com/updates/v1_144
- 【续报】Copilot harness 的实验性工作集默认显示 Keep／Undo，可逐项或按文件处理 Agent 工具产生的编辑，但终端命令改动不会出现；Agents 窗口仍通过 Changes 视图丢弃文件改动。来源：Microsoft https://code.visualstudio.com/updates/v1_144
- Assisted permissions 正式可用，通过模型评估操作风险，但要求 Folder isolation 且遵守组织限制；它不等于对任意目录或命令无条件放行。来源：Microsoft https://code.visualstudio.com/updates/v1_144

## Claude App 更新

- 【续报】Claude Code v2.1.311／v2.1.312 修复压缩后指令文件过期、动态接入 MCP 工具对子 Agent 不可见等问题，并在 VS Code 扩展登录后及时获取组织托管策略。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.311 https://github.com/anthropics/claude-code/releases/tag/v2.1.312
- 【续报】Claude Code v2.1.314 为 VS Code 与桌面端 Code 标签页加入缓存过期后的长会话空闲压缩，同时提供工作目录外写入限制；这次更新针对编码会话，不代表 Claude Duet 扩大开放范围。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.314
- Claude Code v2.1.316 支持独立配置子 Agent 默认 effort，并公告 Opus 4.8 fast mode 将于 11 月 30 日移除且不自动回退；仍使用旧模式的桌面编码工作流需要提前调整。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.316

## 生态与社区动向

- VS Code 发布 Agent Host Protocol v1.0，并提供六种语言的库与 WebSocket 连接方式，为外部客户端接入 Agent Host 提供版本化协议。来源：Microsoft https://code.visualstudio.com/updates/v1_144
