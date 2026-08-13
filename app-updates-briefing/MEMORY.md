# MEMORY

## 1. 本次运行时刻与实际覆盖窗口

- 本次运行时刻:2026-08-13 12:14 UTC
- 上次运行时刻:2026-08-12 12:16 UTC
- 实际覆盖窗口:2026-08-12 12:16 UTC 至 2026-08-13 12:14 UTC(正常窗口)
- 本期 VSCode / Claude App / 生态与社区动向三个方向检索均正常完成。VSCode:GitHub Releases 双次核实,最新版本仍为 1.133.0(2026-08-12 09:41 UTC,发布于窗口开启前,已在上期报告),窗口内无 1.133.1 或更新版本,亦无新 Insiders 预览功能披露,故本期省略 VSCode 板块。Claude App:确认 Claude Code v2.1.229(2026-08-12 20:56 UTC)、v2.1.231(2026-08-13 08:38 UTC)、Claude Cowork 登陆 Chrome 侧边栏(2026-08-12,官方博客 + 9to5Mac/Engadget/TechRadar/The Decoder/官方 X 多源交叉验证)三条落在窗口内的实质新内容,均已收录;Auto Mode 定于 8/14 起默认开启一事本期未见推迟或新公告,原公告(2026-08-07)已在此前窗口报告,不重复收录,待明日实际生效后如有动态再报告。生态与社区动向:本期未发现新的直接相关第三方事件;进行中事件表中 Agent Plugins 条目本期第5次定向复查(检索 Anthropic 官方博客/Newsroom 8/10-8/13 全部条目、Claude Code Changelog 至 v2.1.231、官方 X 账号),仍未发现 Anthropic 官方回应,第三方博客(eesel.ai、digitalapplied.com 等)仍停留在社区实测/推测层面,不计入进展,故本期省略生态板块正文,仅保留跟踪表。

## 2. 已报条目清单(最近 14 天)

- 2026-08-03 | Claude Code v2.1.221 发布,新增 VSCode 插件 Focus 视图与 Linux/WSL 沙箱凭据掩码,修复 Bash 权限绕过等安全问题 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-04 | Claude Code v2.1.222 发布,修复 worktree 隔离会话可对主检出执行破坏性 git 命令的安全漏洞 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-05 | VS Code 1.132 正式版发布,新增集成浏览器元素级评论、Agent Host 架构稳定推广(Claude 为受支持 agent host 之一)、混合 Markdown 编辑器 diff 查看、听写多语言支持 | https://code.visualstudio.com/updates/v1_132
- 2026-08-05 | Claude Code v2.1.223 发布,市场管理支持组织级通配符,修复权限提示 Unicode 隐藏命令等安全问题 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-05 | Claude Enterprise 推出 Inference Hooks 公测,企业可接入自有安全服务器对每次推理请求实时裁决 | https://platform.claude.com/docs/en/release-notes/overview
- 2026-08-05 | Claude Opus 4.1 模型正式退役,建议迁移至 Claude Opus 5 | https://platform.claude.com/docs/en/release-notes/overview
- 2026-08-06 | OpenAI/AWS/Cursor/GitHub/VS Code/Vercel 联合发布 Agent Plugins 跨客户端插件标准,Anthropic/Claude Code 未列入首发名单且格式不兼容 | https://explainx.ai/blog/agent-plugins-openai-standard-aws-cursor-github-vscode-2026
- 2026-08-07 | Claude Code v2.1.224 发布,新增自托管环境公测、archive 插件源、跨会话消息能力 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-08 | Claude Code v2.1.225 发布,新增网关支出上限用量预警与 claude agents 工作区信任提示,修复长期 OAuth token 被覆盖、macOS MCP OAuth keychain 超时批量 401 等问题 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-08 | Claude Code v2.1.226 发布,仅含稳定性与可靠性修复 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 2026-08-08 | Anthropic 宣布 Claude Code Auto Mode 将于 8 月 14 日起成为 Pro/Max/Team 计划新会话默认权限模式,测试中拦截 89% 危险命令 | https://claude.com/blog/auto-mode-default-in-claude-code
- 2026-08-10 | Claude Code v2.1.227 发布,修复过期登录态下功能标志绕过订阅层级校验、claude-code-action 在受限用户模式下 Bash 命令全部失败、/tui 误恢复已回退对话等问题,优化 slash 命令菜单体验与性能 | https://github.com/anthropics/claude-code/releases/tag/v2.1.227
- 2026-08-10 | Claude Sonnet 5 定价:原定 9 月 1 日起上调至 $3/$15 每百万 token 的计划取消,$2/$10 引入价转为永久标准价 | https://platform.claude.com/docs/en/release-notes/overview
- 2026-08-11 | Anthropic 宣布 Claude 模型家族生成文本嵌入隐形水印、生成图片/文件附带 C2PA 签名溯源元数据,为履行 EU AI Act 第 50(2) 条透明度公约,标记能力面向全球部署 | https://the-decoder.com/anthropic-watermarks-all-claude-outputs-globally-with-marks-that-may-persist-through-some-editing/
- 2026-08-11 | Claude Code v2.1.228 发布,修复交互会话重绘死锁、Windows git/Git Bash 检测、/tui 模型回退、跨会话消息收件箱缺失、Remote Control /resume 历史泄漏等问题,并对同步自 claude.ai 的 skills 做安全加固 | https://code.claude.com/docs/en/changelog
- 2026-08-11 | Compliance API 扩展支持读取 Cowork 与 Claude Code 本地会话记录(企业版公测) | https://platform.claude.com/docs/en/release-notes/overview
- 2026-08-12 | VS Code 1.133 正式版发布,新增 Agent Host 会话中途切换 Anthropic/Copilot 模型、免 GitHub 登录打开 Agents 窗口、聊天粘性滚动、集成浏览器 HTML 自动刷新 | https://code.visualstudio.com/updates/v1_133
- 2026-08-12 | Claude Code v2.1.229 发布,新增 remote-control --continue、自托管 runner 服务端 hook 支持、插件市场 command 源 link 模式,修复约40项问题(流式输出重复/丢失、窄终端崩溃、Windows长路径崩溃、Auto Mode 特定账号失败等) | https://github.com/anthropics/claude-code/releases/tag/v2.1.229
- 2026-08-12 | Claude Cowork 登陆 Chrome 侧边栏,对话记录/技能/连接器与桌面端同步,任务可跨设备续接,Max/Team 今日起可用、Pro 陆续开放 | https://claude.com/blog/cowork-chrome-side-panel
- 2026-08-13 | Claude Code v2.1.231 发布,修复 MCP OAuth 对预注册 OAuth 客户端(如 Slack)redirect URI 不匹配问题 | https://github.com/anthropics/claude-code/releases/tag/v2.1.231

## 3. 进行中事件表

- 事件:Agent Plugins 跨客户端插件标准与 Claude Code 现有插件格式不兼容,Anthropic 未列入首发维护方名单;最后进展日期:2026-08-06;下一步关注点:等 Anthropic 是否跟进采用该标准、或对不兼容问题公开回应(2026-08-09、2026-08-10、2026-08-11、2026-08-12、2026-08-13 五次窗口内定向检索——含官方博客/Newsroom、Claude Code Changelog、官方 X 账号——仍未发现 Anthropic 官方回应;第三方社区解读称 Claude Code 插件系统与该标准事实上兼容/可转译安装,但这仅是社区推测非官方声明,不计入进展)。

(已移出:MCP 2026-07-28 版本规范在 Claude 产品线的具体适配进展——官方博客发布于 2026-07-28 当日,此后连续 14 天(至 2026-08-11)定向检索均未发现具体版本号或时间表,按规则移出跟踪表;如后续 Anthropic 官宣适配细节,将重新收录并作为新事件报告。)
