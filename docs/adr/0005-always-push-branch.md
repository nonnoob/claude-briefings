# 落盘一律推分支，由 Action 并入 main

> 修订 ADR-0003 的落盘推送步骤：该 ADR 规定"显式直推 main，被拒时退推 `claude/*` 分支"，自本决策起改为一律推分支、不再尝试直推 main。

运行结束时不再尝试 `git push origin HEAD:main`，而是一律推 `claude/<topic-slug>-<YYYY-MM-DD>`，由 `auto-merge-briefings` Action 并入 main 并删除该分支。分支名带日期是为了避免与尚未被合并掉的同名旧分支撞成非快进；同名已存在时追加 `-<HHmm>` 重推一次。推送走哪个分支名不属于异常，不写运行备注；仅当两次都被拒才告警。

决策依据：云端会话能否直推 main 由平台侧的 git 权限决定，同一任务会连续多天推不动 main（实测：`cloud-native` 08-11/12/13 连续三天、`automotive` 08-09/10 连续两天，且这几天里分支名前缀稳定，说明是会话权限而非推送竞争），prompt 侧无法修复。保留"先 main 后分支"的阶梯意味着每次运行的行为取决于一个我们无法控制也无法预测的外部条件，产出的运行备注随之在"推了 main"和"推了 claude/peaceful-lamport-4mvxcx"之间摇摆——而消灭这类不可预测的分叉正是本轮改造的主线。压成单一路径后，rebase 重试逻辑可整段删除，分支名也从平台生成的 `claude/<形容词>-<科学家>-<哈希>` 变成确定可读的 `claude/<topic-slug>`。

## Consequences

- 每一期简报都硬依赖 auto-merge Action。Action 失效时内容停在分支上、进不了 main，下次运行 `git pull` 拿不到新的 MEMORY，覆盖窗口会算错。缓解：看门狗查的正是"main 上当天有没有归档"，最坏情况是隔天发现而非静默烂掉。
- 保留 `claude/` 前缀是刻意的——平台的推送放行很可能按该前缀判定，且现有 Action 触发器为 `branches: ['claude/**']`，无需改动。
- 分支不再复用固定名字，因此不需要 force push，也就不存在覆盖掉某次未被合并成功的产出的风险。
- 运行备注中不再出现任何推送相关内容；推送走哪条路径不属于异常。
