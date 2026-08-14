# claude-briefings

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Built with Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-d97757)](https://claude.ai/code)
[![Runs on a schedule](https://img.shields.io/badge/Runs-scheduled%20%C2%B7%20cloud-2ea44f)](https://claude.ai/code/routines)

[中文](README.md) | English

A reusable spec for generating recurring topic briefings with Claude Code Routines. The git repository carries all state — task definitions, cross-run memory, and archived issues live here, and `main` is the single source of truth. Runs on a schedule in the cloud; your machine doesn't need to be on.

**How this differs from the usual "RSS scraper + LLM summary" setup:**

- **Zero infrastructure, zero secrets** — no scraper code, no server, no API keys to configure; after forking, the only thing to set up is the Routine itself.
- **Cross-run, event-level semantic dedup** — dedup memory persists in git, so the same story is recognized even under a different outlet, headline, or URL; most comparable projects hash links, or dedup only within a single run.
- **Gaps refill the coverage window, not just the run** — pause for three days and the next run backfills those three days instead of starting over from "today".
- **Pure prompt-as-spec** — the task definition *is* the prompt, and it lives in exactly one place: this repo. Changing behavior means editing markdown and pushing, with no runtime code to maintain and no second copy to keep in sync.

**Sample output (real archives):** [Tech news briefing · 2026-07-26](tech-news-briefing/archive/tech-news-briefing_2026-07-26.md) · [AI industry briefing · 2026-07-26](ai-industry-briefing/archive/ai-industry-briefing_2026-07-26.md) · [more](tech-news-briefing/archive/) *(output language is per-task; current tasks publish in Chinese)*

## The problem it solves

The hard part of a scheduled briefing isn't retrieval — it's **continuity**:

- Never re-report an already-covered event (event-level semantic dedup that survives outlet/headline changes);
- Follow developing stories ([UPDATE] mechanism, with targeted searches driven by each story's "what to watch next");
- Include credible but unannounced news ([RUMOR] mechanism: name the source, track until confirmed or debunked);
- Label evidence strength ([SINGLE-SOURCE] / [CONFLICTING]) instead of passing unverified items off as settled;
- After downtime, backfill the missed window automatically — no gaps, no duplicates.

All of these mechanisms live in one task template; each new task is just an instantiation.

## Repository layout

```
├── _template/SKILL.md      # The task spec (single authority): assembly checklist + runtime body skeleton
├── <topic-slug>/           # One directory per task
│   ├── SKILL.md            # Task definition — the only copy of the behaviour spec
│   ├── MEMORY.md           # Cross-run memory (machine-managed; absent before first run)
│   └── archive/            # One snapshot per issue, append-only
├── skills/new-briefing/    # Claude Code skill: one-line topic → fully assembled new task
├── .github/workflows/      # auto-merge (branch → main) + briefing-watchdog (missing/format alerts)
├── .github/scripts/        # lint_archive.py — mechanical format-contract checker
├── CONTEXT.md              # Glossary
├── docs/adr/               # Architecture decision records (why it's built this way)
```

## Watchdog

Three kinds of failure never surface on their own: the scheduler silently stops firing, a run starts but dies before writing anything, or a run writes something whose format has drifted.
`briefing-watchdog` runs daily at 19:00 UTC and checks that each task's archive for that day **exists** and **satisfies the mechanically checkable half of the output contract** (H1 title, coverage-window line, `##` sections, every item carrying a source and a resolvable bare URL, no markdown link syntax — see [`.github/scripts/lint_archive.py`](.github/scripts/lint_archive.py)). Anything failing opens an Issue; repeated failures only add comments to the same Issue, which closes itself once everything is healthy again.

Checks are restricted to regex-decidable structure and **never judge content quality** — a rule that cries wolf gets ignored, and an ignored alert is no alert at all. When adding a task or changing its cadence, update the `DAILY` / `WEEKLY` lists in that workflow.

## Lifecycle of one run

```mermaid
flowchart LR
    A["Scheduled trigger<br/>(Routine holds only a pointer)"] --> B["clone/pull<br/>state repo"]
    B --> C["Read SKILL.md body<br/>the only copy of the spec"]
    C --> D["Read MEMORY.md<br/>compute window"]
    D --> E["Search by direction<br/>semantic dedup · updates · rumors"]
    E --> F["Write to the output contract"]
    F --> G["Write archive/<br/>rewrite MEMORY.md"]
    G --> H["push claude/&lt;slug&gt;-&lt;date&gt;<br/>Action merges into main"]
    H --> I["Reply = verbatim copy of the archive"]
    I -.next run.-> B
```

On each tick (daily or weekly, per task), the cloud Routine executes one full lifecycle:

1. clone/pull this repository;
2. Read the task's `SKILL.md` body — **the spec exists in exactly one place**; the Routine stores only a ten-line pointer to it (see [ADR-0004](docs/adr/0004-routine-as-thin-pointer.md)). To change a task, edit the file and push; never touch the Routine;
3. Read `MEMORY.md` and compute the coverage window (since the last run, capped at N days; rebuilt from archives if missing);
4. Search by direction, dedup at event level, and check every entry in the open-stories table;
5. Produce the briefing against the **output contract** (a literal skeleton in the template) → write `archive/` and `MEMORY.md` → commit and push `claude/<slug>-<date>`, which an Action merges into main (see [ADR-0005](docs/adr/0005-always-push-branch.md));
6. The final message of the session is a **verbatim copy** of the archive just written — not a link to it.

## Build your own

```bash
# 1. Fork this repo, clone it, run the one-shot setup (installs the new-briefing skill; paths and repo URL are auto-detected)
git clone https://github.com/<you>/<your-fork>.git && cd <your-fork> && ./setup.sh

# 2. Connect GitHub inside Claude Code (once)
/web-setup

# 3. Create a briefing task: sections designed, files assembled and pushed, Routine instructions provided
/new-briefing <topic>
```

Then follow the printed instructions to create the Routine at [claude.ai/code/routines](https://claude.ai/code/routines) (a web step that can't be automated): bind your repository and set the schedule; after creating, remove unneeded connectors in the *edit* dialog (removals in the create form don't stick).

Changing briefing content = edit `SKILL.md` and push. Changing the run time = edit the Routine schedule. The two never mix.

## Design docs

- Glossary: [CONTEXT.md](CONTEXT.md)
- Decision records: [docs/adr/](docs/adr/) (memory/archive separation, file-as-authority, cloud Routines + git state repo, Routine reduced to a pointer, always-push-a-branch)
- Task spec: [_template/SKILL.md](_template/SKILL.md)

## Note

This repository is public (unauthenticated clone from the cloud, see ADR-0003): **never commit credentials, tokens, or any sensitive information.**

## License

MIT
