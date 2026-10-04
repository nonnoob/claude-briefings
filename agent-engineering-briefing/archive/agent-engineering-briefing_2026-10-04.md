# 🛠️ AI Agent 工程简报 · 2026-10-04

> 覆盖窗口：2026-10-03 10:01 UTC 至 2026-10-04 10:00 UTC（常规）

## 开发者工具与工作流

- Claude Code 发布 v2.1.289：修复 Read deny 规则对 @ 提及文件与符号链接文件不生效、Bash deny/ask 规则漏判环境变量前缀命令、嵌套复合 shell 命令的 deny/ask 在用户安装的 mod 批准下失效等权限问题，并为 teammate 新增 `agent.spawn`、在插件 hook 事件间统一 agent ID。若你用 deny 规则做 agent 护栏，应尽快升级并复核规则覆盖面；写 mod/插件时可借 agent ID 串联多 agent 事件日志。来源：Claude Code Changelog https://code.claude.com/docs/en/changelog

## 案例与最佳实践复盘

- 【单源】Simon Willison 撰文主张"几乎一切都需要默认硬预算上限"：编码 agent 与个人 agent 让人极易拉起会调用付费 API、按量计费托管服务的代码，应让 agent 倾向推荐带硬性额度上限的服务商，并提醒新手勿把无上限服务直接上线。给 agent 写部署类 skill/prompt 时，值得把"优先选带 hard cap 的服务、部署前显式提示计费风险"写成默认规则。来源：Simon Willison's Weblog https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/
