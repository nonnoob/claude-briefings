# 🛠️ 开发工具更新简报 · 2026-07-29

本期覆盖窗口：2026-07-28 16:14 UTC 至 2026-07-29 12:11 UTC。VSCode、Claude App 两个方向本窗口内未发现符合收录标准的新内容（VSCode 最新稳定版 1.130、Insiders 1.131 均发布于窗口开始前；Claude Code 最新版本仍为窗口前发布的 v2.1.220，changelog 与 What's new 页面均无窗口内新条目）。

## 生态与社区动向

- 【续报】MCP（Model Context Protocol）2026-07-28 版本规范正式发布（非此前预期的 RC 预发布）：协议核心改为无状态，移除 `initialize`/`initialized` 握手与会话标识，改为每次请求自带协议版本与客户端信息；新增多轮往返请求（MRTR）替代原先需保持长连接的服务端发起请求、基于 HTTP 头的方法/工具路由（`Mcp-Method`/`Mcp-Name`）、带 `ttlMs`/`cacheScope` 的可缓存 List 响应；授权层面落实 RFC 9207 issuer 校验，并从动态客户端注册（DCR）转向客户端 ID 元数据文档（CIMD）。Roots、Sampling、Logging 三项能力及旧版 HTTP+SSE 传输标记弃用，承诺至少 12 个月向后兼容。Anthropic 官方博客确认 Claude Code、Claude Desktop 将跟进适配新规范。来源：[MCP 官方博客](https://blog.modelcontextprotocol.io/posts/2026-07-28/)；交叉验证：[Claude 官方博客](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)、[GitHub 里程碑 2026-07-28-FINAL](https://github.com/modelcontextprotocol/modelcontextprotocol/milestone/5)。
