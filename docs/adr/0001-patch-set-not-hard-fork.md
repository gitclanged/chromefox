# 0001 — Patch-set repository, not a hard fork

- **Status:** Accepted
- **Date:** 2026-10-19
- **Related:** ADR-0002, `docs/ARCHITECTURE.md` §1

## Context

A Firefox-based browser can be organized two ways. A **hard fork** copies Firefox's entire
git history and commits changes directly into it. A **patch-set** repository stores only a
pinned Firefox version plus a list of patch files, and applies them at build time.
Firefox's canonical source has been on GitHub since 2025, so a hard fork is easy to *start*.
The cost is in *keeping up*: every upstream update becomes a large merge, and our changes
are mixed into millions of lines of history.

LibreWolf (source tarball + patches + settings + Makefile) and Zen (patches applied by its
Surfer tool) both use the patch-set model.

## Options considered

1. **Hard fork of `mozilla-firefox/firefox`.** Familiar git workflow; easy to start. Our
   changes are hard to list, review or re-apply; merges are huge; the repo is enormous.
2. **Patch-set with our own thin scripts.** Every change is a small, named, registered file;
   our repo stays small enough for any agent (and Gemini) to read whole. We write and
   maintain the scripts.
3. **Patch-set using Zen's Surfer.** Saves writing scripts; but Surfer describes itself as
   prerelease, is shaped around Zen's needs, and adds a dependency we don't control.

## Decision

Option 2: patch-set repository with our own small, documented Python scripts, modelled on
LibreWolf's structure. Revisit Surfer if our scripts grow beyond a few hundred lines.

## Consequences

- Our entire set of changes is visible in `patches/` and `patches/REGISTRY.md`.
- Upstream updates become "re-apply N small patches", and conflicts point at one file.
- We must keep patches minimal and well described; the registry check enforces existence.
- Developing a patch means working in an unpacked Firefox tree and exporting a diff;
  `/new-patch` documents that loop.
