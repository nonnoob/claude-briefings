# 🛠️ 开发工具更新周报 · 2026-09-11

> 覆盖窗口:2026-09-10 18:39 UTC 至 2026-09-11 10:40 UTC(常规)

## Claude App 更新

- Claude Code v2.1.268 发布,修复自 v2.1.265 起第三方 Anthropic 兼容端点(ANTHROPIC_BASE_URL)因工件工具输入模式正则错误导致每轮请求报 HTTP 400 的回归问题,并为 WebFetch 长时间不返回的挂起问题新增 300 秒超时保护。来源:GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.268
- v2.1.268 同时修复运行中会话在模型访问权限缓存过期时被静默切换至组织默认模型的问题,并为 Claude 应用网关(Gateway)新增按托管设置同步计费费率的定价配置支持。来源:GitHub Releases https://github.com/anthropics/claude-code/releases/tag/v2.1.268
