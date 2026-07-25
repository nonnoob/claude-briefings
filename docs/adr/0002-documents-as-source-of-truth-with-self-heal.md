# Documents 侧 SKILL.md 为唯一权威源，运行时自愈同步

任务定义的唯一权威是 `/Users/jace.chen/Documents/Claude/schedule/<topic-slug>/SKILL.md`；调度器里注册的 prompt 只是其运行时正文的推送副本。每次运行的第 0 步做自愈校验：发现副本与权威源不一致时，按权威源执行本次运行，并调用 `update_scheduled_task` 把权威源正文推回调度器。

决策依据：原方案要求两处"逐字一致、人肉双写"，第一个任务上线两周即漂移（两侧开头文字不同、互相指认对方为权威），人肉双写被实践证伪。同时发现"整文件逐字推送"与工具机制冲突——`create/update_scheduled_task` 会用 taskId+description 自动生成 frontmatter 包住 prompt，导致调度器侧出现嵌套双 frontmatter。故推送物固定为：正文 → prompt 参数，description → description 参数，frontmatter 永不进 prompt。

## Considered Options

- 运行时自愈（选定）：正常运行不依赖读文件（prompt 自包含），仅在漂移时以 Documents 为准修复；用户改任务只改一个文件，下次运行自动生效。
- 人肉双写 + 装配时回读校验：只防装配出错，防不了事后单边手改，已发生过。
- 放弃 Documents 副本、调度器为唯一定义：彻底消灭双写，但失去"在自己文件夹里直接看/改/备份任务定义"的能力——这是建立本规范的痛点 #1。

## Consequences

- 自愈步骤成为每个任务运行正文的固定第 0 步；日后若更换同步模型，需要触达所有任务的 prompt（难逆转，故记录本 ADR）。
- 防御边界：权威源文件缺失或为空时不同步，照当前 prompt 执行并在回复末尾的运行备注中告警——防止误删文件导致任务被清空。
- 定时任务默认写权限因此包含两项：写本任务目录内文件、自愈所需的 update_scheduled_task。
