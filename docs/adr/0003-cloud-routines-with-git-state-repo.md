# 迁移到云端 Routines + git 状态仓库

定时任务从 Claude app 触发器（本机运行、依赖开机）迁移到 Claude Code Routines（云端运行），全部状态迁入本 git 仓库并设为公开，main 为唯一可信状态。运行时 clone 仓库读任务定义与记忆，产出后 commit 并显式直推 main（`git push origin HEAD:main`）；被拒时退推 `claude/*` 工作分支，由 `.github/workflows/auto-merge-briefings.yml` 兜底并入 main。

决策依据：app 触发器在云沙箱运行时读不到本地文件系统，记忆、归档、自愈三个核心机制全部失效；其 git 授权机制（`add_repo`）没有用户侧入口，push 永远打不通，实测确认。Routines 原生支持绑定 GitHub 仓库（`/web-setup` OAuth，push 权限不分分支）与本地时区调度（DST 自动处理，消灭了旧方案 3 月/11 月手动改 UTC cron 的问题）。仓库设为公开是为了云端免认证 clone；代价是内容公开，因此仓库内**禁止出现任何凭据与敏感信息**。

## Considered Options

- **Routines + 公开 git 状态仓库（选定）**：三机制完整保留，读免认证、写走 OAuth，git 天然提供逐字校验与历史。
- 留在 app 触发器、接受无状态运行：去重/续报/归档全部退化，简报质量不可接受。
- 私有仓库：安全性更好，但迁移当时读路径未打通，公开是最短路径；日后可转私有（Routines 的 OAuth 读写不受影响），届时删除本条的免认证假设即可。
- 连接器存状态（Google Drive / Gmail）：读写可靠性与逐字比对能力都不如 git，且绑定第三方生态。

## Consequences

- 落盘推送步骤必须显式 `HEAD:main`——云端会话默认工作在 `claude/*` 分支上，裸 `git push` 推的是工作分支（已实证）。
- auto-merge Action 只合并改动完全落在任务目录白名单内的 `claude/*` 分支；**新增任务时需同步白名单**。
- 自愈降级：云端会话没有任务更新工具时，以仓库文件为准执行本次运行、不回推 prompt（见 ADR-0002 的修订语义）。
- 本地检出只是工作副本：改 SKILL.md 后必须 push 才对下次运行生效；看云端产出先 pull。
- 公开仓库纪律：凭据、令牌、个人敏感信息一律不入库（无关工具目录整体 .gitignore）。
