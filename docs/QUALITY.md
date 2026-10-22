# Quality: definition of done and the anti-spaghetti rules

"Vibe code spaghetti" happens when changes pile up faster than anyone understands them:
no specs, big mixed diffs, copy-pasted code, docs that describe a different program, and
nobody able to say why a line exists. These rules exist to make that impossible to do by
accident. They apply to agents and humans equally.

## Definition of done (every pull request)

A change is done only when **all** of these are true:

- [ ] It does one thing, and that thing is a roadmap task or an issue.
- [ ] A spec (`docs/features/`) describes the behavior; an ADR exists if a hard-to-reverse
      choice was made.
- [ ] It uses the least-intrusive layer that works, and the registry says why if not.
- [ ] Every patch is in `patches/REGISTRY.md`; `scripts/check_registry.py` passes.
- [ ] `scripts/check_links.py` passes (no broken internal doc links).
- [ ] New behavior has a `chromefox.*` pref switch, or the spec says why it can't.
- [ ] It was verified at the right level (see below), and the PR says exactly how.
- [ ] A reviewer that did not write the change reviewed it; findings were fixed or answered.
- [ ] Docs, `STATUS.md`, devlog and (if user-visible) `CHANGELOG.md` are updated.
- [ ] Any performance claim has data in `perf/results/`.

## Verification levels

Use the highest level available for the change; say which level in the PR.

| Level | What it means | Example |
| --- | --- | --- |
| 0 — Not verified | Nothing ran. Must be stated plainly | A doc-only change |
| 1 — Static checks | Repository checks, lint, the patch applies cleanly | Registry change |
| 2 — Builds | The browser builds with the change | Any patch |
| 3 — Runs | Launched and the behavior observed by hand, with steps written down | A UI change |
| 4 — Automated test | A test in `tests/` (or a Firefox mochitest/xpcshell test) covers it | A feature with logic |
| 5 — Measured | Benchmarked per `perf/README.md` | A performance change |

## The anti-spaghetti rules

1. **Spec first.** No feature code without a spec. The spec says what, why, how it's tested,
   and what's out of scope.
2. **Small patches.** Target under ~300 changed lines and under 5 upstream files per patch.
   Bigger needs owner approval and a reason in the registry.
3. **Never copy a whole upstream file** into our repo to change it. Patch the lines you need.
   Copied files silently miss every future Mozilla fix to that file.
4. **No dead code.** Delete instead of commenting out; git remembers.
5. **One concept, one place.** If two patches implement similar logic, factor it into one
   module our patches share, and note the dependency in the registry.
6. **Names say what things are.** No `utils2`, `temp`, `fix`, `new` in names.
   Follow AGENTS.md section 5.
7. **Pref switches** for every behavior change (`chromefox.*`), so any bug can be bisected
   between "ours" and "Firefox's" by flipping a pref.
8. **Explain the why in the code** where it isn't obvious; explain the what in the spec.
9. **Docs are code.** A doc that no longer matches reality is a bug; file it and fix it.
10. **Cleanup cadence.** After every fifth feature PR, run a cleanup pass: Gemini audit,
    remove obsolete patches and prefs, re-check sizes, refresh docs.

## Review checklist (for the `reviewer` subagent, Gemini and humans)

- Does the diff match the task and the spec? Anything extra?
- Is this the least-intrusive layer?
- Is the patch minimal? Any unrelated formatting or refactoring mixed in?
- Are names, file locations and IDs per AGENTS.md section 5?
- Are failure cases handled (missing pref, missing file, offline, different OS)?
- Any red-zone area touched (AGENTS.md rule 2.7)?
- Could this break the next Firefox update? Which upstream files are most likely to conflict?
- Are the claims in the PR description supported by evidence?
- Do the docs now describe what the code does?

## Smells that trigger a stop

If any of these appear, stop and raise it with the owner instead of pushing on:

- A fix requires changing more than one patch series.
- The same bug comes back after being "fixed".
- An agent says "this should work" without having run it.
- The registry's "Why" column for a patch is vague ("needed", "improvement").
- A patch keeps growing across PRs.
- Two agents disagree about how something works and neither cites the source.
