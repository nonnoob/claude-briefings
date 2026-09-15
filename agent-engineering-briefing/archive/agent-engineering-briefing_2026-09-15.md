# 🛠️ AI Agent 工程简报 · 2026-09-15

> 覆盖窗口：2026-09-14 至 2026-09-15（常规）

## 开发者工具与工作流

- Claude Code发布2.1.271（09-14）与2.1.272（09-15）：auto模式新增按命令的`allowed_domains`网络白名单（覆盖Bash/PowerShell/Monitor）、subagent frontmatter新增`omitClaudeMd`可让自定义/插件子agent不继承用户/项目/本地CLAUDE.md上下文、Monitor watch强制不超过30分钟截止时间、动态workflow触达用量上限时改为暂停等待重置而非删除受影响agent；2.1.272为纯可靠性修复版本。为什么值得关注：`omitClaudeMd`能隔离子agent上下文减少无关指令污染，配合新的按命令allowed_domains可在auto模式下更细粒度地控制不同工具调用的网络出站范围。来源：Claude Code Docs Changelog https://code.claude.com/docs/en/changelog
- Claude Code周使用限额09-14起变更：此前自5月起的临时50%上调到期，同日改为在5月前基线上永久上调25%——对已适应150%额度的当前用户而言实际是约17%的净下调，Anthropic随后的说明承认了这一净减少（仅影响周额度，5小时额度等其他额度不变）。为什么值得关注：团队做容量/成本规划时应按新的125%基线（而非近几个月的150%）重新核算并发agent数量与workflow规模上限。来源：BleepingComputer https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/
- 【续报】此前收录的Claude Cowork on Windows磁盘/命令访问故障（Windows 11 KB5124008导致的Plan9共享挂载失败）已由微软09-14发布的带外更新KB5129195修复，该更新同时修复了WSL的同类Plan9共享问题；截至本次核实，Anthropic官方GitHub issue #92984仍未关闭。为什么值得关注：受影响的Windows用户升级到该带外更新（或后续常规更新）即可恢复Cowork本地命令执行能力，无需再手动卸载KB5124008。来源：Microsoft Support https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5129195-windows-11-24h2-25h2-security-update
