# 0003 — uBlock Origin via enterprise policy

- **Status:** Accepted
- **Date:** 2026-10-19
- **Related:** `docs/features/ublock-origin.md`, OPEN-QUESTIONS #2

## Context

The owner wants uBlock Origin (uBO) built in, rather than an engine-level blocker like
Waterfox's (which is built on Brave's MPL-licensed `adblock-rust`). uBO is GPL-3.0 and is
published, signed by Mozilla, on addons.mozilla.org (AMO). Firefox's `ExtensionSettings`
policy can install an extension automatically from a URL: `force_installed` prevents the
user from removing it; `normal_installed` allows the user to disable it.

## Options considered

1. **Policy install from AMO** (`ExtensionSettings`, extension ID `uBlock0@raymondhill.net`,
   URL `https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi`).
   Always the current, Mozilla-signed version; updates through AMO; zero code; licenses stay
   separate. Needs network on first run.
2. **Bundle the `.xpi` in the installer** (`distribution/extensions/`). Works offline on first
   run; we must ship every uBO update ourselves or let it auto-update afterwards.
3. **Merge uBO into the browser.** GPL-3.0 and MPL-2.0 entanglement; we'd maintain a large
   codebase we didn't write. Rejected.
4. **Engine blocker (adblock-rust)** like Waterfox. Not what the owner wants; large ongoing
   maintenance.

## Decision

Option 1 now. Consider adding option 2 later as an offline first-run fallback, keeping AMO
updates on. Install mode defaults to `normal_installed` until the owner decides
(OPEN-QUESTIONS #2).

## Consequences

- uBO updates are delivered by AMO, not by us.
- uBO does **not** run inside the compat tab's Chromium engine (stages 2–3). The spec must
  say so to users.
- Using any policy makes Firefox show "Your browser is being managed by your organization"
  in settings. Phase 2 task P2-04 decides how to present this.
- If AMO distribution of uBO ever changes, revisit with option 2.
