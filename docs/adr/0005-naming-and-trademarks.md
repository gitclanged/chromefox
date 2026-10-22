# 0005 — Naming and trademarks

- **Status:** Proposed (owner decision needed before Phase 6)
- **Date:** 2026-10-19
- **Related:** OPEN-QUESTIONS #4, `branding/README.md`

*Not legal advice. Get a trademark search and, ideally, a lawyer's opinion before release.*

## Context

- "Chrome" is a Google trademark for a web browser. A browser named "Chromefox" combines it
  with an obvious nod to Firefox, which increases the chance of a complaint from either side.
- Mozilla's trademark policy does not allow modified builds to use the Firefox name or logos.
  Source builds are unbranded by default; forks add their own branding.
- Inside Firefox's code, **"chrome" already means the browser UI** (`chrome://` URLs, "browser
  chrome"). Using "chrome" for our Chromium feature would confuse every reader and every
  search of the codebase.

## Options considered

1. Ship as "Chromefox". Highest legal risk; confusing in code.
2. Keep "Chromefox" as an internal codename; choose a distinct public name before Phase 6.
3. Rename now.

## Decision (proposed)

Option 2. The repository, docs and scripts may say "Chromefox" until a public name is chosen.
In code identifiers, prefs and file names for the compatibility feature, use **compat tab**
(`compat-tab`, `compatTab`, `chromefox.compatTab.*`), never "chrome".

## Consequences

- A rename pass is required before release (branding, prefs prefix, docs). Keeping the codename
  in few places (one `branding/` folder, the `chromefox.` pref prefix) keeps that pass small.
- Owner should start a name shortlist and basic trademark searches early.
