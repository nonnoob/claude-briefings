# 🛠️ 开发工具更新周报 · 2026-11-13

> 覆盖窗口：2026-11-09 21:50 UTC 至 2026-11-13 10:40 UTC（常规）

今日要闻：Claude Code v2.1.323 发布实验性 Code Mode，Claude Meetings 以 Beta 形式让 Claude 加入 Google Meet 会议。

## VSCode 更新

- 【续报】【单源】VS Code 1.146.0 稳定版于 11 月 11 日在 GitHub 发布（此前仅有 Insiders），1.145.3 维护补丁于 11 月 10 日发布；本次未能取得 1.146 正式版特性清单，详情待官方更新页核实。来源：VS Code GitHub Releases https://github.com/microsoft/vscode/releases/tag/1.146.0

## Claude App 更新

- Claude Code v2.1.323 发布，新增实验性可选启用的 Code Mode（Claude 编写 JavaScript 调用工具）、插件 `engines["claude-code"]` 版本范围限制，并收紧 Bash 通配符与 sudo/env 包装命令的权限检查，Auto 模式不可用时改为回退至 Manual 模式，未识别模型 ID 的上下文窗口默认改为 1M。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.323
- Claude Code v2.1.322 发布，为 Vertex 的 global、us、eu 区域新增 fast mode（被拒时回退标准速度）。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases
- Anthropic 以 Beta 形式面向 Team 与 Enterprise 推出 Claude Meetings，Claude 可作为可见参会者加入 Google Meet 会议记笔记并生成文档、白板与幻灯片，并同步推出 Claude Whiteboards 与 Claude Sheets Beta；外部访客会议默认需管理员放行。来源：Claude 支持中心发布说明 https://support.claude.com/en/articles/12138966-release-notes
- Claude Developer Platform 推出自托管 Claude Managed Agents，可在自有基础设施上运行完整 Managed Agents 服务并存储智能体与会话历史，需联系 Anthropic 客户团队开通。来源：Claude Platform 发布说明 https://platform.claude.com/docs/en/release-notes/overview

## 生态与社区动向

- 【续报】【单源】Claude Fable 5.2 于 11 月 9 日在 GitHub Copilot 正式可用（Pro+、Max、Business、Enterprise，逐步放量，可在 VS Code 模型选择器选用），Business/Enterprise 需管理员启用策略且该模型要求数据留存、不适用零数据留存。来源：Let's Data Science（转述 GitHub 公告，未取得 GitHub 原文） https://letsdatascience.com/news/anthropics-claude-fable-52-reaches-general-availability-in-g-90d9b700
