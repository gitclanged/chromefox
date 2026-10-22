---
name: new-patch
description: Create, export and register a patch to Firefox source correctly - right series and ID, minimal diff, change-site comments, pref gate, registry row, and proof it applies to a fresh tree. Use whenever a change to Firefox source code is needed.
argument-hint: "[series e.g. 0200-debloat] [kebab-slug]"
---

# New patch: $ARGUMENTS

Prerequisite: an approved spec in `docs/features/` that calls for a patch. If none, stop and
use `/new-feature`.

1. **Justify the layer.** Write one sentence on why a policy, pref or extension can't do this.
   If you can't, don't write a patch.
2. **Pick the ID.** Next free number in the series range (see `patches/REGISTRY.md`).
   File: `patches/<series>/<NNNN>-<slug>.patch`.
3. **Prepare a tree.** In `work/`, have the pinned source with all existing patches applied
   (`python3 scripts/apply_patches.py` once it exists). Make that tree a throwaway git repo
   if it isn't one (`git init && git add -A && git commit -qm base`) so you can diff cleanly.
4. **Find the code** in that tree (or Searchfox at the matching revision). Quote the file and
   lines you'll change to the owner before changing them.
5. **Make the minimal change.** Add `Chromefox: <why> (CFX-NNNN)` comments; gate behind the
   spec's `chromefox.*` pref where possible. Target < ~300 changed lines, < 5 files; if larger,
   stop and ask.
6. **Build and check** at the right verification level (artifact build if frontend-only).
7. **Export:** `git diff > <repo>/patches/<series>/<NNNN>-<slug>.patch` (paths relative to the
   source root, `a/` `b/` prefixes).
8. **Register:** add the row to `patches/REGISTRY.md` with upstream files, risk, pinned version
   in "Last rebased", and the Why. Run `python3 scripts/check_registry.py`.
9. **Prove it applies** to a fresh pristine tree with the whole series.
10. Update the spec's Results section. Explain the patch to the owner hunk by hunk in plain
    language, including the riskiest line.
