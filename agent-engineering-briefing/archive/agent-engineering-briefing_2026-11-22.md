# 🛠️ AI Agent 工程简报 · 2026-11-22

> 覆盖窗口：2026-11-21 10:10 UTC 至 2026-11-22 10:06 UTC（常规）

今日要闻：GitHub Copilot CLI 发布 v1.0.115-6，修复组织必装插件安装重试、/delegate 未登录提示与 Unix 下取消 shell 命令遗留子进程的问题。

## 开发者工具与工作流

- GitHub Copilot CLI 发布 v1.0.115-6：组织要求的插件在策略临时变更中断后可立即重试安装，未登录时 /delegate 明确提示需登录，Unix 下取消 shell 命令会清理进程组内遗留子进程，Sessions 侧栏将选模型中的 Copilot Fusion 会话显示为工作中。若在企业环境用 Copilot CLI 跑长任务，升级后可减少取消命令留下的孤儿进程与插件安装卡住的问题。来源：GitHub copilot-cli Releases https://github.com/github/copilot-cli/releases/tag/v1.0.115-6
