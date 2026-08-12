# 🛠️ 开发工具更新简报 · 2026-08-12

## VSCode 更新

- VS Code 1.133 正式版发布：Agent Host 支持会话中途在 Anthropic 与 Copilot 模型间自由切换（模型选择器分组显示两家供应商）；已配置 Claude API key 的用户现可免 GitHub 登录直接打开 Agents 窗口；新增聊天粘性滚动（长对话中固定当前 prompt，可点击跳转）；集成浏览器支持本地 HTML 文件磁盘改动自动刷新。来源：[VS Code 1.133 Release Notes](https://code.visualstudio.com/updates/v1_133)、[GitHub Releases](https://github.com/microsoft/vscode/releases/tag/1.133.0)

## Claude App 更新

- Claude Code v2.1.228 发布：修复交互会话偶发内部布局错误导致界面停止重绘、Windows 下从 git 安装目录父文件夹启动时找不到 git/Git Bash、`/tui` 在切换模型后错误回退到旧模型、跨会话消息安装或升级后首个会话收件箱缺失、Remote Control `/resume` 泄漏历史对话标题给已连接会话等问题，并对同步自 claude.ai 的 skills 做了安全加固（禁止其伪装本地命令/MCP 提示、描述做清洗标注、屏蔽其内嵌 `!` 命令与 `@` 文件展开）。来源：[Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- Claude Sonnet 5 定价：原定 2026 年 9 月 1 日起由 $2/$10 每百万 token 上调至 $3/$15 的计划被取消，$2/$10 引入价直接转为永久标准价。来源：[Claude Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview)（2026-08-10 条目）
- Compliance API 扩展支持读取 Cowork 与 Claude Code 在用户本机运行的会话记录（企业版公测）：新增 `GET /v1/compliance/apps/sessions/local` 系列接口，可列出组织内本地会话及其元数据、完整转录。来源：[Claude Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview)（2026-08-11 条目）
