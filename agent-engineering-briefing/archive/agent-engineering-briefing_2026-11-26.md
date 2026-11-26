# 🛠️ AI Agent 工程简报 · 2026-11-26

> 覆盖窗口：2026-11-25 10:07 UTC 至 2026-11-26 10:07 UTC（常规）

今日要闻：GitHub Copilot CLI 1.0.116 转正并连发 1.0.117 预发布，自定义 agent 可显式声明可用工具。

## 开发者工具与工作流

- GitHub Copilot CLI 发布 v1.0.116 正式版（新增对所有子进程生效的 `env` 设置、插件与独立 MCP 服务器连同一端点时告警），随后 v1.0.117-0/-1/-2 预发布加入自定义 agent 显式工具暴露、后台 agent 重启后续聊、子 agent 遵循自定义 agent 文件中的工具清单。写自定义 agent 时可据此把工具白名单收紧到最小，并检查插件与 MCP 是否重复接入同一服务。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases
