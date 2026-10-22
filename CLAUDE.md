@AGENTS.md

@docs/STATUS.md

## Claude Code specifics

- **Output style:** this project sets the `Mentor` output style (`.claude/output-styles/mentor.md`)
  so every session explains its work to the owner. Do not switch it off unless the owner asks.
- **Session start:** the `SessionStart` hook prints the current branch, uncommitted changes
  and recent commits. If you were resumed after a context compaction, re-read
  `docs/STATUS.md` before continuing.
- **Skills (type `/name`):** `start-session`, `end-session`, `new-feature`, `new-patch`,
  `upstream-update`, `explain`, `gemini-handoff`. Prefer them over improvising the same steps.
- **Subagents:** use `reviewer` before every pull request; `upstream-scout` when a new
  Firefox ESR release lands; `perf-analyst` for anything in `perf/`; `docs-keeper` when
  docs may have drifted from reality.
- **Plan mode:** use it for any change that touches more than one area of the repo.
- **Hooks you will see:** a guard blocks commits and pushes on `main`; a stop check refuses to
  end a turn while `patches/REGISTRY.md` or internal doc links are broken. If a hook blocks
  you, fix the cause — do not look for a way around the hook.
- **Path-scoped rules** in `.claude/rules/` load automatically when you open files under
  `patches/`, `prefs/` or `compat-tab/`.
