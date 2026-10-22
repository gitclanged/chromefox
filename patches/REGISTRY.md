# Patch registry

Every patch in `patches/` has exactly one row here, and every row points to a real file.
`scripts/check_registry.py` enforces this, plus:

- **ID** is `CFX-NNNN` and matches the file's number and series range.
- **Feature** names a spec in `docs/features/<feature>.md`.
- **Layer** is one of `frontend`, `engine`, `build`, `branding`, `pref-default`.
- **Risk** is `low`, `medium` or `high` (chance of conflict or breakage on Firefox updates).
- **Why** is a real reason (at least 20 characters, not just "needed" or "fix"), and says why
  a policy, pref or extension was not enough. `engine` patches must cite an ADR (`ADR-NNNN`).

Keep rows in ID order. Update **Upstream files** and **Last rebased** on every upstream update.

| ID | File | Feature | Layer | Upstream files | Risk | Last rebased | Why |
| --- | --- | --- | --- | --- | --- | --- | --- |

<!--
Example row (kept in a comment so the checker ignores it):

| CFX-0201 | `patches/0200-debloat/0201-hide-sponsored-tiles.patch` | debloat | frontend | `browser/components/newtab/…` | low | 153.4.0esr | Sponsored tiles remain visible in the first-run layout even with the FirefoxHome policy set; only a frontend change removes them. |
-->
