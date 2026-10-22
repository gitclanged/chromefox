# 0007 — AGENTS.md is the single source of agent instructions

- **Status:** Accepted
- **Date:** 2026-10-19
- **Related:** `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `docs/AI-TEAM.md`

## Context

Claude Code reads `CLAUDE.md` (and can read `AGENTS.md`); Gemini CLI reads `GEMINI.md`
(and can be configured to read other names). Both support importing other files with
`@path`. Duplicated instructions drift apart; contradictory instructions make agents pick one
at random. Claude Code's own guidance is to keep its instruction file under about 200 lines,
because longer files reduce adherence.

## Decision

- `AGENTS.md` holds every rule that applies to all agents.
- `CLAUDE.md` and `GEMINI.md` each start by importing `AGENTS.md` and `docs/STATUS.md`, then
  add only tool-specific notes.
- Long procedures live in skills (`.claude/skills/`) and runbooks, not in `AGENTS.md`.
- Area-specific rules live in `.claude/rules/` with `paths:` so they load only when relevant.

## Consequences

- One place to change a rule.
- `AGENTS.md` must stay concise; growth is a smell to address in the monthly review.
- Other tools that read `AGENTS.md` directly will work with the repository unchanged.
