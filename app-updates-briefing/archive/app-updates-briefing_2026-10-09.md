# 🛠️ 开发工具更新周报 · 2026-10-09

> 覆盖窗口：2026-10-02 10:36 UTC 至 2026-10-09 10:36 UTC（常规）

今日要闻：Anthropic 于 10-07 发布 Claude Haiku 5.5，输入/输出低至 $0.10/$0.50 每百万 token，较 Haiku 4.5 平均便宜约 75%，并首次为 Haiku 加入 effort 档位。

## VSCode 更新

- VS Code 1.141 正式版于 10-07 发布，主打 Agent 管理：Copilot agent host 跨平台沙箱（Windows 端为实验性、默认网络放行、需手动开启）、Agents 窗口多会话分屏网格、按体积/闲置时长清理 Agent worktree，以及可在 VS Code 中续接 Copilot CLI / GitHub Copilot app 会话。来源：VS Code 官方发布说明 https://code.visualstudio.com/updates/v1_141
- VS Code 1.141 另含矩形粘贴（列编辑）、同时登录多个 GHE.com / GitHub Enterprise Server 实例（单值 `github-enterprise.uri` 设置被列表式设置取代），并新增实验性"并排运行并对比多个 Agent 实现"操作。来源：Neowin https://www.neowin.net/news/visual-studio-code-1141-tracks-how-much-disk-space-dead-agent-sessions-waste/

## Claude App 更新

- Anthropic 发布 Claude Haiku 5.5（`claude-haiku-5-5`）：提示 ≤10 万 token 时 $0.10/$0.50 每百万 token（超出为 $0.50/$2.50），较 Haiku 4.5 平均约便宜 75%，首个带 effort 档位的 Haiku，同步登陆 AWS/Google Cloud/Azure；Claude Code v2.1.293 将其设为默认 Haiku 模型。来源：AI Weekly https://aiweekly.co/alerts/introducing-claude-haiku-55
- Anthropic 同步将 Sonnet 5.5 缓存读取价格减半（称多数 Agent 工作负载约便宜 20%），并为 Max 和 Team 订阅新增每月 API 额度（据二手报道，未见官方原文）。来源：AI Weekly https://aiweekly.co/alerts/introducing-claude-haiku-55
- Claude Code v2.1.289（10-03）修复 deny/ask 规则漏判嵌套复合命令、`Read` deny 规则可经符号链接绕过的问题，并新增 `agent.spawn` 供队友 Agent 使用。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases
- Claude Code v2.1.290（10-05）新增 `claude attach <name>` 与 `claude logs <name>`（支持会话名前缀匹配），修复 WebFetch 静默截断 10 万字符以后文本（现支持 `offset`）及压缩后定时任务丢失。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases
- Claude Code v2.1.292（10-06）修复 UNC 路径文件读取下 PreToolUse 批准与 auto mode 绕过权限提示、`rm -rf` 命中家目录 8.3 短名等安全问题，新增 Agent 工具 `effort` 参数与 `claude plugin install --marketplace`。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases
- Claude Code v2.1.295（10-08）为命令/HTTP hook 新增 `onFailure: "block"`（hook 启动失败、超时或异常退出时拦截动作），并修复网关拒绝 context-1m beta 时所有 `[1m]` 模型请求失败的问题；v2.1.291 为 v2.1.290 回归（云端会话丢权限提示答复）的热修复。来源：Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases
