# 🛠️ 开发工具更新周报 · 2026-08-21

> 覆盖窗口:2026-08-14 12:50 UTC 至 2026-08-21 12:45 UTC(常规)

## VSCode 更新

- VS Code 1.134 正式版发布(2026-08-19),Agent Host 支持跨窗口分组与共享会话(可将相关聊天与子代理会话并排比较)、新增 prompt 时间线快速定位历史提示与文件改动、新增"在聊天中查找"全文搜索、集成浏览器可设为本地 HTML 文件默认预览方式。来源:VS Code 官方更新页 https://code.visualstudio.com/updates/v1_134

## Claude App 更新

- Claude Code v2.1.233 发布(2026-08-14),修复 Windows NT 设备路径前缀绕过 UNC 路径校验导致的 NTLM 凭据泄露漏洞,新增 GitLab MR 支持,并将 Todo/任务追踪工具从 Opus 4.8+、Sonnet 5、Fable 5、Mythos 5 等新模型的默认工具集中移除(可用环境变量恢复)。来源:Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.233
- Claude Code v2.1.234–v2.1.236 相继发布(2026-08-17至19),新增用量限额重置后自动续接会话、`ANTHROPIC_DEFAULT_MODEL` 默认模型环境变量、可选拼写检查(aspell/hunspell/ispell)、跨会话消息空闲通知等配置类特性。来源:Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.236
- Claude Code v2.1.237–v2.1.238 发布(2026-08-20),新增内置 Concise 输出风格与可自定义快捷键风格(keybindingFlavor)、插件市场 HTTP Header 生成器,并修复网关/自定义 base URL 场景下 prompt 缓存失效、长交互会话内存无界增长等问题。来源:Claude Code GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.238
- Claude Desktop v1.34493.0 发布(2026-08-20),修复 macOS 上启用 iCloud"优化 Mac 存储"时的启动卡死、"每 N 天/月"周期性任务命中错误日期、Touch ID 登录导致应用崩溃(密钥登录暂时下线)、磁盘写满或停止听写时应用退出等问题。来源:Anthropic Claude Desktop Changelog https://claude.com/docs/cowork/changelog
