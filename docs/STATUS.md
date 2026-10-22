# Project status

<!-- Keep this file under 60 lines. It is loaded into every Claude and Gemini session.
     Update it at the end of every session (the /end-session skill does this). -->

**Last updated:** 2026-10-19 · **Phase:** 0 — Foundations · **Upstream pin:** Firefox ESR 153 (dot release not yet pinned)

## Where we are

- Repository scaffolding exists: agent rules, architecture, roadmap, ADRs 0001–0007,
  learning curriculum, runbooks, repository checks, Claude Code and Gemini configuration.
- Nothing is built yet. No patches exist. `prefs/policies.json` is a draft that has not been
  tested in a real browser.
- The repository has not been pushed to GitHub yet.

## Next up

1. **P0-01** — Initialize git, create the GitHub repo, push, enable branch protection,
   add the MPL-2.0 LICENSE via a pull request. (Owner + Claude, see `docs/00-START-HERE.md`.)
2. **P0-02** — Owner answers the top three items in `docs/OPEN-QUESTIONS.md`
   (first platform, uBlock install mode, translations policy).
3. **P0-03** — Test `prefs/policies.json` on a stock Firefox ESR 153 install; record results
   in `docs/features/no-ai.md` and `docs/features/ublock-origin.md`.

## Blocked / waiting on owner

- Public name (ADR-0005) — not needed until Phase 6, but trademark research takes time.

## Known risks right now

- None of the policy keys in `prefs/policies.json` have been tested together on ESR 153 yet.

## Last session

See the newest file in `docs/devlog/`.
