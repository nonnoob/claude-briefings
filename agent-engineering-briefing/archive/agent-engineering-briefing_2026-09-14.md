# 🛠️ AI Agent 工程简报 · 2026-09-14

> 覆盖窗口：2026-09-13 至 2026-09-14（常规）

## 开发者工具与工作流

- Show HN 收录开源工具 Docket：为"agent 写的代码"生成逐次提交证据记录，读取 Claude Code / Codex CLI / opencode 的执行过程并与 diff 对齐，逐块标出改动是否有验证记录、哪些改动完全没人复核过；证据格式由独立的 Commit Evidence Record 规范（Apache 2.0）定义，Docket 只是其参考实现，方便其他工具复用同一格式。对大量合并 agent 生成代码的团队，这提供了一种比逐行通读更聚焦的复核入口——直接定位"没有证据支撑"的高风险改动。来源：GitHub (Dillonsmart/docket) https://github.com/Dillonsmart/docket

## 案例与最佳实践复盘

- LangChain 发布内部案例复盘《How We Built LangChain's Paid Media Agent》：投放优化 agent 的每次运行都在专属 LangSmith Sandbox（隔离 microVM、32GB 磁盘、可执行 shell，预装 pandas/DuckDB 做分析、openpyxl 处理表格、WeasyPrint+Jinja2 出报告）中跑；核心设计原则是"模型只负责判断、代码负责一致性"——把计算逻辑、事实来源规则和安全护栏都下沉到确定性代码，模型只负责解读结果和给下一步建议，agent 因此更快、更省、更可靠，团队已将其开源作为参考实现。这是少见的附带代码级细节的"sandbox+确定性代码兜底"架构范式，可直接套用到数据/运营类 agent 设计。来源：LangChain Blog https://www.langchain.com/blog/paid-media-agent
