# claude-briefings

用 Claude Code Routines 每天自动生成主题简报的一套可复用规范。git 仓库承载全部状态——任务定义、跨运行记忆、历史归档都在这里，`main` 即唯一事实；云端定时运行，本机无需开机。

## 解决什么问题

简报类定时任务的难点不在检索，在**连续性**：

- 不重复报已报过的事件（按事件级语义去重，换媒体换标题也认得出）；
- 追踪进行中事件的后续（【续报】机制）；
- 收录未官宣但有可信度的消息（【传闻】机制，写明信源、跟踪至证实或辟谣）;
- 断档几天后自动补窗，而不是漏报或重报。

这些机制全部写进一份任务模板，每个新任务只需实例化。

## 仓库结构

```
├── _template/SKILL.md      # 任务规范（唯一权威）：装配 checklist + 运行时正文骨架
├── <topic-slug>/           # 每个任务一个目录
│   ├── SKILL.md            # 任务定义（正文 = Routine 的 prompt，逐字）
│   ├── MEMORY.md           # 跨运行记忆（机器读写，首次运行前不存在）
│   └── archive/            # 每期简报快照，只增不改
├── CONTEXT.md              # 术语表
├── docs/adr/               # 架构决策记录（为什么这么设计）
└── .github/workflows/      # claude/* 分支兜底合并 Action
```

## 工作原理

每天定时，云端 Routine 执行一次完整生命周期：

1. clone/pull 本仓库；
2. **自愈校验**：任务 `SKILL.md` 正文与注册 prompt 不一致时，以文件为准执行（改任务只需改文件并 push，无需碰 Routine）；
3. 读 `MEMORY.md` 计算覆盖窗口（自上次运行至今，封顶 N 天；缺失时从归档重建）;
4. 分方向检索，按事件级语义去重，逐一核查进行中事件表；
5. 产出简报 → 写 `archive/` 与 `MEMORY.md` → commit 并 `git push origin HEAD:main`（被拒则退推 `claude/*` 分支，由 Action 自动并入 main）。

## 自己搭一套

1. Fork 本仓库（或参照 `_template/SKILL.md` 从零装配任务目录）；
2. 本机 Claude Code 里跑 `/web-setup`，OAuth 连接 GitHub；
3. 在 [claude.ai/code/routines](https://claude.ai/code/routines) 新建 Routine：Instructions = 任务 `SKILL.md` 的运行时正文（逐字，边界定义见模板）、绑定你的仓库、设定时；
4. 按最小权限原则移除 Routine 上不需要的连接器（创建表单里移除不生效，创建后在编辑弹窗里摘）；
5. 新增任务时同步 `.github/workflows/auto-merge-briefings.yml` 的目录白名单。

改简报内容 = 改 `SKILL.md` 并 push；改运行时间 = 只改 Routine 调度。两者永不混放。

## 设计文档

- 术语表：[CONTEXT.md](CONTEXT.md)
- 决策记录：[docs/adr/](docs/adr/)（记忆与归档分离、文件为唯一权威源 + 自愈、云端 Routines + git 状态仓库）
- 任务规范：[_template/SKILL.md](_template/SKILL.md)

## 注意

本仓库公开（云端免认证 clone，见 ADR-0003）：**任何凭据、令牌、敏感信息一律不得入库。**

## License

MIT
