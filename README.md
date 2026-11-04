# md2csv — built by speccoder

A small CLI that turns Markdown tables into CSV, built end to end by [speccoder](https://github.com/hupe1980/speccoder) from one line of intent:

> a CLI that turns Markdown tables into CSV

**See it run: [the pull request](https://github.com/hupe1980/speccoder-example-md2csv/pull/1)** — one commit per task, the tests that judged it, and its signed evidence. The `speccoder / evidence` check verifies every tick.

How it was made (model: `gpt-5.4-mini`):

1. `speccoder new md2csv --idea "a CLI that turns Markdown tables into CSV" --stack python`
2. `speccoder spec specify "…" --through tasks` — spec, plan and tasks with Spec Kit's own skills; the spec reviewed and approved requirement by requirement.
3. `speccoder run` — 17 tasks. Each story's acceptance tests were written from the spec before its code, red first; a task is verified when it turns them green and no check regresses. Three tests speccoder wrote were wrong and ruled so by a person — the rulings are recorded on the ticks.

```sh
git switch speccoder/001-markdown-to-csv
printf '| a | b |\n|---|---|\n| 1 | 2 |\n' | uv run md2csv
```
