# 🛠️ AI Agent 工程简报 · 2026-11-28

> 覆盖窗口：2026-11-27 10:07 UTC 至 2026-11-28 10:07 UTC（常规）

今日要闻：OpenAI Agent Builder/Evals 平台与 v1 prompts API 将于 11-30 下线，多个来源确认官方迁移路径为 Agents SDK，需尽快规划迁移。

## 开发者工具与工作流

- GitHub Copilot CLI 发布 v1.0.117 正式版及 v1.0.118-0 至 -2 预发布：自定义 agent 可显式声明暴露的工具，MCP 批准不再连带内置权限类型，计划模式的 Assisted Permissions 在建分支、装包等动作前询问，沙箱支持自定义 CA 证书；MCP 工具输出 schema 含 null anyOf 不再中断交互轮次。若你在给团队写自定义 agent 或沙箱策略，这批权限收紧值得对照检查。来源：GitHub Copilot CLI Releases https://github.com/github/copilot-cli/releases

## 模型能力与 API 更新

- 【续报】OpenAI AgentKit 下线范围已被多个来源确认（不再单源）：官方 6 月 3 日已宣布，Agent Builder 画布、Evals 平台与 v1 prompts API 于 11-30 下线，Agents SDK、Responses API、ChatKit 保留；构建器内可导出为 Agents SDK 代码（TypeScript/Python），强确定性分支流程不宜迁到 Workspace Agents；已发布工作流是否仍能经 ChatKit 执行尚无定论（均为二手转述，未核 OpenAI 官方页）。落地提示：确定性强的流程直接导出代码迁 SDK，并先自建评估集替代 Evals。来源：Forkast https://forkast.news/openai-agent-builders-nov-30-shutdown-puts-migration-on-a-code-and-validation-path/
