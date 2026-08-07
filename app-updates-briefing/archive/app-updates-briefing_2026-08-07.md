# 🛠️ 开发工具更新简报 · 2026-08-07

> 上次运行为 2026-07-30 12:13 UTC，间隔超过 7 天封顶，本期实际覆盖 2026-07-31 16:39 UTC 至 2026-08-07 16:39 UTC。

## VSCode 更新

- **VS Code 1.132 正式版发布**（2026-08-05）：继 1.131 之后的最新稳定版，合入集成浏览器"侧聊"等多项新功能。来源：[VSCode 官方 Release Notes](https://code.visualstudio.com/updates/v1_132)、[Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/08/05/vs-code-1-132-sharpens-agent-workflows-with-side-chats-browser-comments.aspx)
- **Agent Host 架构进一步走向稳定推广，Claude 被列为受支持的 agent host 之一**：让 Copilot/Claude/Codex 等 agent harness 运行在独立进程中、支持多窗口共享同一会话，需通过 `chat.agentHost.enabled` 手动开启。来源：[VSCode 官方文档](https://code.visualstudio.com/docs/agents/concepts/agent-host)、Visual Studio Magazine、[InfoWorld](https://www.infoworld.com/article/4205750/visual-studio-code-1-132-advances-built-in-dictation.html)
- **集成浏览器新增"元素级评论"功能**：可在集成浏览器中选中网页元素直接添加评论，供 Agent 精确定位处理反馈。来源：VSCode 官方 Release Notes、Visual Studio Magazine
- **【续报】混合 Markdown 编辑器新增 diff 查看能力**：上期报道的实验性混合 Markdown 编辑器（1.131）在 1.132 中新增可在渲染视图中直接查看改动 diff、并继续编辑该文档。来源：VSCode 官方 Release Notes、InfoWorld
- **【续报】内置听写升级为多语言支持**：上期报道的实验性内置听写（1.131）在 1.132 中新增多语言听写与自动语言检测，并新增可定制转写用语的命令。来源：VSCode 官方 Release Notes、[Neowin](https://www.neowin.net/news/microsoft-drops-visual-studio-code-1132-this-is-whats-new/)

## Claude App 更新

- **Claude Code v2.1.224 发布**（2026-08-07，今日）：新增自托管环境（self-hosted environments，公测）——通过 `claude self-hosted-runner` 可在自有机器/容器运行 Claude Code web/mobile/desktop 会话（Team/Enterprise）；新增 `archive` 插件源，支持从 zip 包直接安装插件；新增跨会话消息能力。来源：[Claude Code 官方 CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)、releasebot.io
- **Claude Enterprise 推出"Inference Hooks"公测**（2026-08-05）：企业可接入自有安全服务器，在每次推理请求执行前进行放行/拒绝裁决，支持签名请求与合规审计日志。来源：[Anthropic 官方 Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview)、Proofpoint 官方博客
- **【单源】Claude Opus 4.1 模型正式退役**（2026-08-05）：`claude-opus-4-1-20250805` 停止服务，所有调用返回错误，官方建议迁移至 Claude Opus 5，影响 Claude App 内可选模型列表。来源：Anthropic 官方 Platform Release Notes
- **Claude Code v2.1.223 发布**（2026-08-05）：市场管理设置新增组织级通配符条目，Workflow 代理在子代理模型受限时发出警告，并修复 Bash 权限绕过、权限提示中用 Unicode 隐藏命令等安全问题。来源：Claude Code 官方 CHANGELOG、Havoptic
- **Claude Code v2.1.221–222 发布**（2026-08-03～04）：修复 worktree 隔离会话可对主检出执行破坏性 git 命令的安全漏洞、pre-tool-use auto-allow hooks 绕过后台代理工具限制等多个安全问题，VSCode 插件新增 Focus 视图。来源：Claude Code 官方 CHANGELOG、dev.classmethod.jp

## 生态与社区动向

- **"Agent Plugins"跨客户端插件开放标准发布，Anthropic/Claude Code 未列入首发名单**（2026-08-06）：OpenAI、AWS、Cursor、GitHub、VS Code、Vercel 联合发布打包 Agent Skills + MCP 配置的跨客户端清单格式，首发支持客户端含 ChatGPT/Codex/Cursor/GitHub Copilot/Kiro/VS Code，但不含 Claude Code；且新标准的可见路径格式与 Claude Code 现有插件目录结构（隐藏路径的 `.claude-plugin/plugin.json`）不兼容。来源：[explainx.ai](https://explainx.ai/blog/agent-plugins-openai-standard-aws-cursor-github-vscode-2026)、eesel AI、kingy.ai（三家均为二手报道交叉确认，未能直连官方一手公告页面）
