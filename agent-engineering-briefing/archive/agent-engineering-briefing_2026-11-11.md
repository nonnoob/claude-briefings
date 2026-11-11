# 🛠️ AI Agent 工程简报 · 2026-11-11

> 覆盖窗口：2026-11-10 10:05 UTC 至 2026-11-11 10:07 UTC（常规）

今日要闻：GitHub Copilot CLI v1.0.109 上线 Claude Fable 5.2 并为沙箱规则加入 CIDR 支持，同期预发布版提供 git/ssh/sudo 密码提示的遮罩应答。

## 开发者工具与工作流

- GitHub Copilot CLI 发布 v1.0.109（另有 v1.0.110-0/-1 预发布）：模型选择器加入 Claude Fable 5.2，沙箱主机允许/拒绝规则支持 IPv4/IPv6 CIDR 且路径设置支持环境变量，`/init` 会把其后输入的文字作为指导传给模型，预发布版实验性提供遮罩对话框应答 agent 命令的 git/ssh/sudo 密码提示。值得关注：给 agent 配沙箱网络白名单时可按网段而非逐主机维护，评估 Fable 5.2 时也可直接在 Copilot CLI 切换试用。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases
