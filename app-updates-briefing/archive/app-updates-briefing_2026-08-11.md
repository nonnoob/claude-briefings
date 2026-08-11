# 🛠️ 开发工具更新简报 · 2026-08-11

## Claude App 更新

- **Claude Code v2.1.227 发布**：修复过期登录态下功能标志（feature flag）绕过订阅层级校验、可能误提示 Max 计划用户开通 Fable 用量额度的问题；修复 `claude-code-action` 在 `allowed_non_write_users` 限制下、GitHub-hosted runner 上所有 Bash 命令执行失败的问题；修复 `/tui` 会错误恢复已被回退（rewind）对话的问题；并优化 slash 命令菜单体验与事件循环性能。来源：[Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)、[GitHub Releases](https://github.com/anthropics/claude-code/releases/tag/v2.1.227)
- **Claude 模型家族生成内容将加入隐形水印与溯源元数据**：Anthropic 宣布为履行 EU AI Act 第 50(2) 条透明度公约，Claude 生成文本将嵌入不影响可读性、复制粘贴后仍可检测的隐形水印；生成的图片/文件（PNG/JPG/SVG 等）将附带符合 C2PA 标准的签名溯源元数据。标记能力面向全球用户部署、不限于欧盟，旧版模型暂不回溯支持，官方同时提示水印可能因大幅编辑或翻译而失效，不构成绝对溯源证明。来源：[The Decoder](https://the-decoder.com/anthropic-watermarks-all-claude-outputs-globally-with-marks-that-may-persist-through-some-editing/)、[Business Standard](https://www.business-standard.com/technology/tech-news/claude-invisible-watermark-ai-generated-text-how-it-works-126081100381_1.html)（Anthropic 官方博客 claude.com 本次网络不可直接访问，以上述独立信源交叉验证）

*进行中事件表更新：MCP 2026-07-28 规范对 Claude 产品线的具体适配版本号/时间表，自官方博客 7/28 发布以来连续 14 天定向检索无新进展，本期起从跟踪表移出（如后续官宣将重新收录）；Agent Plugins 跨客户端标准与 Anthropic 的关系继续跟踪，本期仍无官方回应。*
