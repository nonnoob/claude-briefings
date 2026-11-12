# 🛠️ AI Agent 工程简报 · 2026-11-12

> 覆盖窗口：2026-11-11 10:07 UTC 至 2026-11-12 10:07 UTC（常规）

今日要闻：GitHub Copilot CLI 连发 v1.0.110-1 至 -3 预发布版，集中加固 MCP 配置与会话的容错与保护。

## 开发者工具与工作流

- GitHub Copilot CLI 发布 v1.0.110-1 至 v1.0.110-3 预发布版：`/mcp add`/`edit` 与 `copilot mcp add` 遇到无效配置时保留原有条目并提示保存错误，无效 `settings.json` 不再抹掉插件设置，`/compact` 遵守会话 AI 额度上限，被中断的部分响应标注为未完成。若你在写依赖 MCP 配置或长会话的 agent 工作流，可据此检查自己的配置容错与额度兜底逻辑（均为预发布版，正式版以 v1.0.109 为准）。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases
