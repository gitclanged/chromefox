# perf/ — benchmark method and results

Rules: [ADR-0006](../docs/adr/0006-performance-claims-need-data.md). Goals and experiments:
[docs/features/performance.md](../docs/features/performance.md).

## Method (draft — finalized in P2-05)

1. **Same machine, same session.** Record CPU, RAM, OS version, power source, display.
2. **Baseline:** stock Firefox ESR of exactly our pinned version, fresh profile.
3. **Candidate:** our build, fresh profile, same extensions state (note uBlock on/off — it
   changes page-load results; measure both).
4. **Prepare:** reboot, close other apps, plug in power, wait for the system to go idle.
5. **Alternate runs** (baseline, candidate, baseline, …) to spread out thermal and background
   noise. At least 10 runs per benchmark.
6. **Report** median, minimum, maximum (or interquartile range), and run count.
7. **Conclude conservatively:** if the ranges overlap substantially, report "no measurable
   difference".

## Folder layout

| Path | Contents |
| --- | --- |
| `baselines/` | Baseline results per pinned Firefox version |
| `results/` | One Markdown summary per experiment: `YYYY-MM-DD-<experiment-id>.md` |
| `raw/` (git-ignored) | Raw benchmark output; summarized into `results/` |

## Result summary template

```markdown
# <experiment id> — <title>
Date · Machine · Firefox ESR version · Our commit
| Metric | Baseline median (range) | Candidate median (range) | Runs | Change |
Conclusion: keep / revert / inconclusive — one paragraph, including any regressions.
```
