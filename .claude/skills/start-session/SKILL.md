---
name: start-session
description: Begin a working session - reconstruct project state from STATUS.md, the latest devlog, the current branch and open pull requests, then propose the next task and a plan. Use at the start of every session or after losing context.
---

# Start a session

1. Read `docs/STATUS.md` and the newest file in `docs/devlog/` (by name).
2. Run `git status --short`, `git branch --show-current`, `git log --oneline -5`.
3. Run `gh pr list --state open` if `gh` is available and authenticated; otherwise say so.
4. If an unfinished task branch exists, summarize where it stopped (last commits, open PR,
   what the devlog says is next).
5. Check `docs/reviews/` for a report without a completed triage table; mention it.
6. Tell the owner, in plain language and under 150 words:
   - where the project is (phase, last thing done);
   - the proposed task (default: first "Next up" item in STATUS.md, with its roadmap ID);
   - the plan: steps, files likely touched, how it will be verified;
   - anything waiting on the owner (OPEN-QUESTIONS, PRs to merge).
7. Wait for approval before editing anything. When approved, create the task branch
   (`<type>/<topic>`) if one doesn't exist.
