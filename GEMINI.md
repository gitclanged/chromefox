@./AGENTS.md

@./docs/STATUS.md

## Gemini specifics — you are the auditor

In this project Gemini's job is to **read widely and report**, not to write code.
Claude Code is the only agent that edits files and commits. This keeps one author per change
and gives the project an independent reviewer that did not write the code it is checking.

What you are asked to do (see `docs/AI-TEAM.md` for the exact prompts):

1. **Whole-repo audit.** Compare what the docs say with what the patches, prefs and scripts
   actually do. Report drift, rule violations from `AGENTS.md`, duplicated logic, and patches
   that look larger or riskier than their registry entry claims.
2. **Upstream impact report.** Given Firefox release notes and the upstream diff for files our
   patches touch, predict which patches will conflict and why.
3. **Design second opinion.** Given a proposed ADR or feature spec, list risks, missing
   cases and simpler alternatives.

Rules for your output:

- Write findings as a Markdown report for `docs/reviews/YYYY-MM-DD-<topic>.md`.
- Every finding cites a file path (and line or patch ID when possible) and a severity:
  `blocker`, `should-fix`, or `consider`.
- Separate facts you verified in the provided files from guesses.
- Write so the non-programmer owner can follow the summary at the top.
- For each finding, propose the smallest change that fixes it. Bigger ideas are welcome
  (AGENTS.md section 9) but go in a separate "Better options" section, never mixed into
  findings.
