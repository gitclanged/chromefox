# Project status

**Last updated:** 2026-10-22 · **Phase:** 0 — Foundations · **Upstream pin:** Firefox ESR 153 (dot release not yet pinned)

## Where we are

- The repository is on GitHub: https://github.com/gitclanged/chromefox. It is **public**
  since 2026-10-22 (owner decision, `docs/OPEN-QUESTIONS.md` "Decided") so that branch
  protection works on GitHub Free. `main` holds the baseline "initial project scaffolding".
- CI ("Repository consistency") passed on `main`.
- Session 0 pull requests waiting for the owner: #1 git hygiene · #2 Windows text-encoding
  fixes for hooks and scripts (merge together with #6) · #3 AGENTS.md section 9 "Better
  ideas are welcome" · #4 compat-tab proposals (stacked on #3) · #5 MPL-2.0 LICENSE ·
  #6 this status update and the session devlog.
- Nothing is built yet. No patches exist. `prefs/policies.json` has not been tested.

## Next up

1. **P0-01 (finish)** — Owner turns on branch protection for `main` (ask Claude for the
   walkthrough), then reviews and merges #1–#6. Claude updates #4 after #3 merges.
2. **P0-02** — Owner answers `docs/OPEN-QUESTIONS.md` rows 1–3 and 10 (first platform,
   uBlock install mode, translations, budget).
3. **P0-03** — Test `prefs/policies.json` on a stock Firefox ESR 153 install.
4. **P0-05** — First Gemini audit with the context pack (`/gemini-handoff audit`).

## Follow-up tasks found in session 0

- `.claude/hooks/guard_git.py` matches command *text*: `git -C <dir> commit` gets past it;
  mentioning `git switch -c` or `--force-with-lease` anywhere disables a check; commit
  messages or test data that quote git commands get blocked. Branch protection is the
  real backstop.
- `scripts/pack_context.py` packs every file, ignoring `.gitignore`, when git is unavailable
  (tested: a `.env` file was included). It should refuse instead.
- Patch line endings: `/new-patch` should turn off `core.autocrlf` in its throwaway repo, and
  a check should flag unexpected CR characters in patches (review of #1).

## Blocked / waiting on owner

- Branch protection on `main`: only the owner can turn it on in GitHub's settings.
- Decisions: OPEN-QUESTIONS rows 1–3 and 10; proposals IDEA-01 – IDEA-05 (once #3 and #4
  are merged); whether Gemini's documented role ("auditor") should change.
- Public name (ADR-0005): the codename is now publicly visible, so trademark research is
  more urgent than planned.

## Known risks right now

- `main` is unprotected until branch protection is on.
- None of the policy keys in `prefs/policies.json` have been tested on ESR 153 yet.

## Last session

See the newest file in `docs/devlog/`.
