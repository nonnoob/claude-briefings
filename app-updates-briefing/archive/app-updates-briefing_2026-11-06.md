# 🛠️ 开发工具更新周报 · 2026-11-06

> 覆盖窗口：2026-10-31 11:32 UTC 至 2026-11-06 16:22 UTC（常规）

今日要闻：VS Code 1.145 正式版发布远程 Agent 应用预览与远程 Canvases、跨 harness 嵌套聊天会话及本地 Cron 自动化调度；Anthropic 连续发布 Claude Code v2.1.317/v2.1.318 并正式推出覆盖 Claude Code 与网页端的服务端推理钩子（Inference Hooks）。

## VSCode 更新

- 【续报】VS Code 1.145 正式版及 1.145.1 补丁于 11 月 4 日发布，支持在远程 Agent 宿主会话中通过内置浏览器远程代理（`workbench.browser.enableRemoteProxy`）直接预览开发服务器与 Web 应用，并将 Agent Canvases（`chat.canvases.enabled`，仍为预览版）扩展至远程会话。来源：Microsoft https://code.visualstudio.com/updates/v1_145
- VS Code 1.145 新增跨 harness 嵌套聊天会话（支持在主会话内调用 Claude、Codex 或 Copilot 等不同后端的独立子会话协同审查且保留各自模型与权限配置），并提供 Conversation、Verbose、Compact 三档聊天详略度视图模式。来源：Microsoft https://code.visualstudio.com/updates/v1_145
- VS Code 1.145 为本地自动化任务（Local Automations）引入自定义五字段 cron 表达式调度与工作区级自定义 Agent 支持，改进 `files.exclude` 以允许保留被排除目录内的指定文件可见可搜，并提升企业托管 MCP 服务器白名单优先级。来源：Microsoft https://code.visualstudio.com/updates/v1_145
- 【续报】VS Code 1.146 Insiders 预览分支升级 Compare Models 多模型对比（支持自定义分组集合、由 Agent 自动发起 2 至 10 组配置对比及读取评判轨迹），在 Copilot 会话中支持由 MCP 服务器动态下发 Agent Skills，并为内置 Issue Reporter 新增 Markdown 预览。来源：Microsoft https://code.visualstudio.com/updates/v1_146

## Claude App 更新

- 【续报】Claude Code v2.1.317 于 11 月 3 日发布，将切换非主会话模型的子 Agent 与协作者改为回退至目标模型自身默认 effort 而非继承主会话档位，新增网络与 Shell 工具外发账号邮箱前的隐私确认提示（`cc-plugin-privacy`）与 Agent SDK hook `onFailure: "block"` 阻断配置，默认隔离云端/自托管运行器内的嵌套 `claude -p` 会话 ID，并移除 `Read` 工具重读未变更文件时的占位简写。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.317
- Claude Code v2.1.318 于 11 月 3 日发布，在 `claude auth status` 与 `claude -p` 输出中新增 `claude.ai` 登录过期时间字段及提前 10 天的 `stderr` 告警，支持 Anthropic 托管云端无仓库（No repository）会话启动，为网关 Mantle 上游新增跨账号 AWS `assume_role` 与成本归因，并修复 v2.1.314 引入的 `--continue` 丢失早期历史及共享网络主目录下配置文件与 MCP 设置偶发清空问题。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.318
- Anthropic 于 11 月 5 日宣布 Claude Enterprise 服务端推理钩子（Inference Hooks）正式转正（GA），支持在提示词与工具调用到达模型前统一对网页聊天、Claude Code 与 Cowork 执行无代理实时 DLP 放行或拦截，并同步上线安全中心仪表盘（Security Center，Beta）与父级组织集中管理控制台（`admin.claude.com`，Beta）。来源：Anthropic https://claude.com/resources/articles/claude-enterprise-security-updates https://support.claude.com/en/articles/12138966-release-notes
- Claude Desktop（v3.1623.0 及以上）新增 `/storage` 命令与 `Settings > Storage` 存储管理面板，支持按核心运行时、Cowork 任务、Code 会话及 worktree、缓存查看磁盘占用并清理闲置满 30 天的本地会话与任务，同时在 Code 标签页新增组织远程受管策略加载状态提示。来源：Anthropic https://support.claude.com/en/articles/12138966-release-notes
- Anthropic 于 11 月 5 日面向美国区 Pro、Max 与 Ultra 个人订阅用户推出 Personal Finance（Beta），支持通过 Plaid 只读连接银行、信用卡、贷款与投资账户以进行自然语言财务分析与看板生成，且相关财务对话不用于模型训练。来源：Anthropic https://support.claude.com/en/articles/18185620-use-personal-finance-in-claude https://support.claude.com/en/articles/12138966-release-notes

## 生态与社区动向

- Microsoft 于 11 月 5 日宣布将于 2026 年底前把 Microsoft Copilot（含 Copilot Cowork 与 M365 应用）中集成的 Claude 模型纳入欧盟数据边界（EU Data Boundary），使欧盟与欧洲自由贸易联盟组织在管理员显式启用后可在区域数据驻留合规范围内使用 Claude。来源：Microsoft https://www.microsoft.com/en-us/copilot/blog/2026/11/05/bringing-claude-models-in-microsoft-copilot-into-the-eu-data-boundary/
- 【续报】由 Anthropic、Bloomberg、Nordstrom 等共同制定的 MCP 技能扩展规范 SEP-2640（`io.modelcontextprotocol/skills`）正式定稿，通过复用 MCP 资源原语定义 `skills/list` 与 `skills/get` 等接口支持服务端零安装按需下发 `SKILL.md` 智能体技能目录，并已在 VS Code 1.146 Insiders 中率先落地。来源：Model Context Protocol https://modelcontextprotocol.info/seps/2640-skills-extension/ https://www.bloomberg.com/company/stories/skills-over-mcp-how-bloomberg-helped-standardize-agent-skills-at-scale/
- 随 Claude Enterprise Inference Hooks 转正，Check Point、Proofpoint 与 TrueFoundry 等安全与网关厂商宣布上线原生 Webhook 集成，支持对 Claude 网页端、桌面端、Cowork 及 Claude Code 实施零代理实时敏感数据防泄漏（DLP）拦截与合规审计。来源：Check Point https://blog.checkpoint.com/ai-security/native-ai-security-comes-to-claude-why-anthropics-inference-hooks-matter/ https://www.proofpoint.com/us/blog/data-security/real-time-data-loss-prevention-claude-inference-hooks
