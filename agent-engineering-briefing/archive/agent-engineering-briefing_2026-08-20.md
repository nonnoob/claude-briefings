# 🛠️ AI Agent 工程简报 · 2026-08-20

> 覆盖窗口：2026-08-19 至 2026-08-20（常规）

## 开发者工具与工作流

- Claude Code 2.1.236（08-19）新增 `ANTHROPIC_DEFAULT_MODEL` 指定新会话起始模型（`/model` 手选仍覆盖并跨重启保留）、跨会话 `SendMessage` 新增 opt-in 免轮询的 `notify_when_idle` 空闲通知（macOS/Linux），并收紧 macOS 沙箱：`**/.env` 这类通配符只读拒绝规则现在在允许读取区内优先生效、覆盖整个匹配目录且无法靠重命名绕过。团队统一模型策略与多会话协同可直接用这两个开关落地，沙箱收紧则意味着几条旧的读取绕过路径已失效，值得复核自己的权限假设。来源：Claude Code 官方更新日志 https://code.claude.com/docs/en/changelog
- 【续报】同版 2.1.236 首次带来 auto mode 专项改动：Monitor 的 allow 规则在 auto mode 期间被搁置、Monitor 命令改为与 Bash 同级审查，Bedrock/Vertex AI/Foundry 对齐 Claude API 的分类器默认值（含严重度打分），auto mode 的 git 状态检查不再被仓库 `status.showUntrackedFiles=no` 蒙混过关。此前 auto mode 在云端部署上的分类口径与 Claude API 不一致，跨云团队现在可以按同一套预期评估自动执行的风险面。来源：Claude Code 官方更新日志 https://code.claude.com/docs/en/changelog
- Claude Code 2.1.237（08-20）修复了经 LLM 网关或自定义 base URL 的会话中 prompt caching 失效的问题，并新增内置 "Concise" 输出风格（直接给结果、省略前言与叙述），可在 `/config` → Output style 选择。走网关代理的团队此前可能在毫不知情的情况下按全价重算每轮上下文，升级后应重新测一遍缓存命中率与成本曲线。来源：Claude Code 官方更新日志 https://code.claude.com/docs/en/changelog
- Cursor 08-19 把云端 Agent 改造为常驻系统：新增 Subscriptions 让 agent 由 PR、Slack 线程或定时任务唤醒，`/goal` 命令交付跨会话保持的长期目标（官方示例为"修完所有 flaky test 并让 CI 转绿"），子 Agent 改为各自运行在隔离 VM 中、每个拿到干净的项目副本，运行中的引导消息改为排队而非打断。这是编码 agent 从"单轮补全"转向"长期在线看护代码库"的范式样本，`/goal` + 隔离子 VM 的组合对自建自治 agent 系统的编排层设计有直接参考价值。来源：Cursor Changelog https://cursor.com/changelog/08-19-26
- Simon Willison 08-19 实测 smolvm 1.8.3 作为不可信 Python/JavaScript 代码沙箱：硬件隔离 VM 而非共享内核容器，冷启动约 0.6–1.5 秒、热执行约 50 毫秒，完整 create-run-teardown 冷态 577–643 毫秒、热态约 48 毫秒，无网络、CPU/RAM 限额、guest 端超时、只读输入挂载与可写输出挂载、`--unprivileged` 均按预期生效。给 agent 执行模型生成代码的场景一直卡在"够安全"与"够快"之间，这组实测数字可作为选型基线直接引用。来源：Simon Willison's Weblog https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/

## 模型能力与 API 更新

- Anthropic 08-19 将 Agent Skills 与 Skills API（`/v1/skills`）正式 GA：包括通过 `container` 参数加载 Skill 的 Messages API 请求在内，均不再需要 `skills-2025-10-02` beta header，仍发送该 header 的请求保持兼容。Skill 从 beta 转正意味着可以正式进入生产架构与合规评审，此前因"还在 beta"而搁置 Skill 化改造的团队可以重启该议程。来源：Claude Platform 发布说明 https://platform.claude.com/docs/en/release-notes/api
- Anthropic 08-19 同时将 Files API 正式 GA，去掉 `files-api-2025-04-14` beta header 要求，但 GA 响应格式有行为变化：上传时需显式设置 `expires_in_seconds`、文件对象返回 `expires_at`，列表分页改为 `page`/`next_page` 加 `ids[]` 过滤，存储上限每组织 1TB、限速 500 请求/分钟。这是一次会静默改变行为的"转正"——不带 header 的请求直接走新格式，依赖旧分页或默认不过期假设的代码需要在升级前逐一核对。来源：Claude Platform 发布说明 https://platform.claude.com/docs/en/release-notes/api
- Anthropic 08-19 给 Claude Managed Agents 的 `web_search`/`web_fetch` 加上域名管控：在 `agent_toolset_20260401` 的 `configs` 数组中设 `allowed_domains` 或 `blocked_domains`，`web_fetch` 另支持 `max_content_tokens`、`web_search` 支持 `user_location`；同日自托管沙箱会话可挂载 memory store，Python/TS/Go SDK worker 会在 `mount_path` 下载并把 agent 的改动同步回写。域名白名单把"agent 上网"从不可控行为收敛成可审计的策略配置，是把浏览类 agent 推上生产的一块关键拼图。来源：Claude Platform 发布说明 https://platform.claude.com/docs/en/release-notes/api
- Anthropic 08-19 再发生一起 Claude Opus 5 与 Haiku 4.5 错误率升高事件，约 09:42 UTC 开始、10:33 UTC 定位原因、11:02 UTC 恢复，为继 08-16、08-17、08-18 之后本周第五起服务稳定性事件；官方状态页在本次检索环境中不可直达，时间线来自多家状态聚合站交叉印证。连续一周的高频抖动已经不能当偶发处理，把重试退避、跨模型降级路径和用户侧超时预算显式写进 agent 编排层是当下的合理防御。来源：StatusGator https://statusgator.com/services/anthropic/outage-history

## 案例与最佳实践复盘

- Simon Willison 08-19 撰文指出编码 agent 正在侵蚀软件的"概念完整性"（conceptual integrity，Brooks《人月神话》术语）：过去"这个功能要写一周"本身就是一道纪律门槛，如今加代码近乎免费，约束消失后系统迅速长成温彻斯特神秘屋，真正的瓶颈从打字速度转移到团队认知负荷跟不上代码增量。对用 agent 提效的团队是一句直接的告诫——把定期删减、重构与"这个功能该不该存在"的评审显式排进流程，否则 agent 的杠杆只是把技术债生产速度也一起放大了。来源：Simon Willison's Weblog https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/
