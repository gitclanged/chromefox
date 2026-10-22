# 2026-10-19 — Project bootstrap

**Task(s):** pre-P0 · **Branch / PR:** none yet (repository not initialized) · **Agent:** Claude (planning session)

## What we did

Assessed the feasibility of the project and created the starter repository: agent rules
(`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`), architecture, roadmap, seven decision records,
feature specs, a learning curriculum, runbooks, Claude Code configuration (hooks, skills,
subagents, a teaching output style, path rules), GitHub templates and checks, and three
small scripts that keep the repository consistent and pack it for Gemini.

## Why

The project will be built mostly by AI agents across many sessions, with an owner who is not
a programmer. That only works if the project's state, rules and decisions live in files that
any session can read, and if the most important rules are enforced automatically. So the
scaffolding comes before any browser code.

Key decisions (each has an ADR): build on Firefox ESR 153 with a patch-set repository;
install uBlock Origin by enterprise policy; block AI features by policy first; build the
compat tab in stages starting with user-agent rules; require data for performance claims;
treat "Chromefox" as a codename.

## How it connects

Everything here is the "development system" in `docs/ARCHITECTURE.md` §3. The first piece
of the actual browser — `prefs/policies.json` — is layer 1 in §2.

## Verified

- `scripts/check_registry.py` and `scripts/check_links.py` pass on the scaffolding.
- `scripts/pack_context.py` produces a context file.
- JSON files parse.
- **Not verified:** `prefs/policies.json` has not been tested in a real browser (task P0-03).
  Hooks have not been run inside Claude Code yet (they will run in the first session).

## New terms

See `docs/GLOSSARY.md` — the whole glossary is new.

## Next

P0-01: initialize git, create the GitHub repository, push, protect `main`, add LICENSE by PR.

## Questions for the owner

The top three rows of `docs/OPEN-QUESTIONS.md`: first platform, uBlock install mode,
whether translations count as AI.
