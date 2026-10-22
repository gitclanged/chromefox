## What and why

<!-- Plain language. The owner (not a programmer) must be able to follow this. -->

**Task:** P?-?? · **Spec / ADR:** <!-- links -->

## Changes

<!-- Bullet list by folder. Mention every patch ID added or changed. -->

## How verified

<!-- Verification level from docs/QUALITY.md, the exact commands/steps run, and what they showed.
     List anything NOT verified. "Should work" is not verification. -->

- Level:
- Ran:
- Result:
- Not verified:

## Checklist

- [ ] One purpose; matches the task and spec
- [ ] Least-intrusive layer (registry "Why" explains any patch)
- [ ] `patches/REGISTRY.md` updated; `scripts/check_registry.py` passes
- [ ] `scripts/check_links.py` passes
- [ ] Behavior switchable by a `chromefox.*` pref (or spec explains why not)
- [ ] Reviewer subagent ran; findings fixed or answered below
- [ ] Docs, `docs/STATUS.md`, devlog updated; `CHANGELOG.md` if user-visible
- [ ] Performance claims backed by `perf/results/` (or no claims made)

## Risk

<!-- Layer(s) touched. Any red-zone area (security, IPC, networking, updater, signing)?
     What could break on the next Firefox update? -->

## Reviewer findings

<!-- Paste the reviewer verdict and how each finding was handled. -->
