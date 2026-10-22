# 0004 — Compat tab in stages

- **Status:** Accepted
- **Date:** 2026-10-19
- **Related:** `docs/features/compat-tab.md`, `docs/FEASIBILITY.md` "The compat tab", ROADMAP phases 4 and 7

## Context

Some sites refuse to work outside Chrome. Causes range from cheap to fix (the site only
checks the user-agent string) to impossible without Blink (the site depends on APIs only
Chromium implements, such as WebUSB/WebHID/WebSerial, or on Chromium rendering quirks).
Embedding a Chromium engine inside a Gecko tab has no known precedent in a Firefox-based
browser and would add a second browser's security, privacy and update burden.

## Options considered

1. **Embedded Chromium tab first.** Best user experience if it works; months of risky native
   work on each OS; a second engine to secure and update; uBO doesn't cover it.
2. **Staged:** (1) per-site user-agent rules; (2) companion Chromium **window** in a separate
   process and profile; (3) time-boxed research spike on embedding, Windows first via WebView2.
3. **Do nothing; tell users to keep Chrome installed.** Zero cost; poor experience.

## Decision

Option 2. Each stage ships independently and must be justified by real failing sites
collected in `compat-tab/site-rules/README.md`. Stage 3 is a four-week, pref-gated prototype
with a written go/no-go ADR; it may never ship.

Implementation preference for stages 1–2: a **built-in WebExtension** plus a small native
companion app over native messaging, rather than deep frontend patches — this keeps the patch
surface (and rebase cost) small. A frontend patch is allowed for UI that an extension cannot
provide, per AGENTS.md rule 2.4.

## Consequences

- Most "requires Chrome" sites are fixed quickly and cheaply by stage 1.
- Stage 2 relies on an installed Chromium-family browser or, on Windows, the WebView2 runtime
  (updated by Microsoft). We do not ship or build Chromium.
- Users must be told clearly: pages opened in the Chromium window have separate cookies and
  logins, and are not filtered by uBlock Origin.
- The internal name is "compat tab" everywhere (ADR-0005, AGENTS.md rule 2.10).
