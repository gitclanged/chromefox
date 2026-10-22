---
name: gemini-handoff
description: Prepare work for Gemini 4 Argon (the project's auditor) or bring its report back - pack the repository, produce the right prompt, save the returned report to docs/reviews/, and triage its findings.
argument-hint: "[audit | upstream <old> <new> | design <path> | save]"
disable-model-invocation: true
---

# Gemini handoff: $ARGUMENTS

Roles and prompts are defined in `docs/AI-TEAM.md`. Gemini reviews; Claude implements.

## audit / upstream / design

1. Run `python3 scripts/pack_context.py` (for `upstream`, add the upstream diff with
   `--extra <diff file>`; generate it first if needed). Report the token estimate.
2. Print the matching prompt from `docs/AI-TEAM.md` (Prompt 1, 2 or 3) with placeholders
   filled in, ready to paste.
3. Tell the owner exactly what to do: which file to upload (`.context/chromefox-context.md`),
   where (Gemini CLI if it offers Argon, otherwise AI Studio or the Gemini app), and to paste
   the answer back here followed by `/gemini-handoff save`.

## save

1. Save the pasted report to `docs/reviews/YYYY-MM-DD-<topic>.md` on a `docs/review-<date>`
   branch.
2. Verify each finding against the repository yourself: mark it **confirmed**, **not
   reproducible**, or **disagree (with reason)**. Gemini can be wrong; so can you — cite files.
3. Add the triage table (see `docs/reviews/README.md`): fix / defer / won't fix, with roadmap
   task or reason. Add accepted items to `docs/STATUS.md` or `docs/ROADMAP.md`.
4. Explain the top findings to the owner in plain language and ask them to approve the triage.
   Commit and open a pull request.
