---
name: end-session
description: Close a working session - commit and push the branch, update STATUS.md, write the devlog entry for the owner, update CHANGELOG if user-visible, and open or update the pull request.
disable-model-invocation: true
---

# End a session

1. Run `python3 scripts/check_registry.py` and `python3 scripts/check_links.py`. Fix failures
   or record them as blockers.
2. Make sure everything is committed on the task branch with Conventional Commit messages.
   Never commit on `main`.
3. Update `docs/STATUS.md` (keep it under 60 lines): date, phase, what changed, new "Next up"
   (from `docs/ROADMAP.md`), blockers, risks.
4. Write `docs/devlog/YYYY-MM-DD-<topic>.md` from `docs/devlog/TEMPLATE.md`. Write it for the
   owner: what, why, how it connects, what was verified and what wasn't, new terms, next step.
   Add any new terms to `docs/GLOSSARY.md`.
5. If users would notice the change, add it to `CHANGELOG.md` under "Unreleased".
6. Commit these doc updates (`docs: update status and devlog for <task>`), push the branch.
7. If the task is complete: run the `reviewer` subagent, address findings, then open or
   update the pull request with `.github/PULL_REQUEST_TEMPLATE.md` filled in completely.
   If not complete: open a draft pull request so the work is visible.
8. Tell the owner in three to five lines: what's ready for them to review/merge, and what the
   next session will start with.
