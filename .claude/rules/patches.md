---
paths:
  - "patches/**"
---

# Rules for work under patches/

- Before writing a patch, confirm a higher layer (policy, pref, extension) can't do it, and
  say so in the registry's Why column.
- Find the upstream code in **our pinned version** (the unpacked tree in `work/` or Searchfox
  at the matching revision). Never patch from memory of Firefox code.
- Use `/new-patch`. File name `<NNNN>-<slug>.patch` in the right series; ID `CFX-NNNN`.
- Mark every change site with a comment: `Chromefox: <why> (CFX-NNNN)`.
- Gate behavior behind a `chromefox.*` pref when possible.
- Keep the patch under ~300 changed lines and 5 upstream files; otherwise stop and ask.
- Touching `security/`, `ipc/`, `netwerk/`, sandboxing, the updater or signing: stop and ask
  the owner first (AGENTS.md rule 2.7).
- After writing: add the registry row, run `python3 scripts/check_registry.py`, and prove the
  patch applies to a fresh tree.
