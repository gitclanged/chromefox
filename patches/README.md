# patches/

Our changes to Firefox's source code. Each `.patch` file is a small, single-purpose diff
against the version pinned in `upstream/firefox.toml`. Patches are applied in numeric order.

## Series

| Folder | IDs | Purpose |
| --- | --- | --- |
| `0100-branding/` | CFX-0100 – 0199 | Name, icons, about dialog, removal of Mozilla trademarks |
| `0200-debloat/` | CFX-0200 – 0299 | Removing sponsored content, promotions, nags, background tasks |
| `0300-no-ai/` | CFX-0300 – 0399 | Anything AI-related that policies cannot fully handle |
| `0400-ublock/` | CFX-0400 – 0499 | uBlock Origin integration (expected to stay empty) |
| `0500-compat-tab/` | CFX-0500 – 0599 | UI hooks for the compat tab; logic lives in `compat-tab/` |
| `0600-performance/` | CFX-0600 – 0699 | Measured performance changes (ADR-0006) |

A new series needs an ADR.

## Rules

1. File name: `<NNNN>-<kebab-slug>.patch` inside the right series folder; `NNNN` is the ID.
2. Every patch has a row in [REGISTRY.md](REGISTRY.md). `scripts/check_registry.py` fails
   otherwise — locally (Claude Code stop hook) and in CI.
3. One purpose per patch; target < ~300 changed lines and < 5 upstream files.
4. Add a comment at each change site: `Chromefox: <why> (CFX-NNNN)`.
5. Gate behavior behind a `chromefox.*` pref where possible.
6. Prefer a policy, pref or extension. A patch's registry "Why" must say why those
   weren't enough.

## Making a patch

Use `/new-patch <series> <slug>`. In short: work in an unpacked, already-patched source tree
(`work/`), commit your change there in a throwaway git repo, export the diff as the patch
file, register it, then re-run `scripts/apply_patches.py` on a fresh tree to prove it
applies.
