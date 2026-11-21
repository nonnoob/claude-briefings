# 🛠️ AI Agent 工程简报 · 2026-11-21

> 覆盖窗口：2026-11-20 10:25 UTC 至 2026-11-21 10:10 UTC（常规）

今日要闻：Claude Code v2.1.330 上线 Enterprise Admin Console 登录并修复压缩长会话后卡死数分钟、worktree 被误删等问题。

## 开发者工具与工作流

- Claude Code 发布 v2.1.330：支持登录 Enterprise Admin Console 托管组织并套用其设置与云厂商/网关，新增内置 mod「easel」按需绘制图表，修复压缩超长对话后卡顿数分钟、ExitWorktree 误删其他会话正在使用的 worktree、多进程同时保存导致用户设置丢失、`--continue`/`--resume` 遇到无效时间戳失败。多会话并行用 worktree 的人建议尽快升级避免丢工作区；企业部署可借此统一组织配置。来源：claude-code-changelog 镜像 https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.330
- Copilot CLI 发布 v1.0.115-2 至 -5 预发布版：ACP 编辑器支持结构化澄清提问表单、修复插件初始化竞态、长时间本地会话占用磁盘更少且恢复更快、切换到 Copilot Fusion 时显示所请求的路由配置。长会话重度用户可关注恢复速度改进，自建 ACP 客户端可对接新的表单式澄清交互。来源：GitHub Releases https://github.com/github/copilot-cli/releases/tag/v1.0.115-5
