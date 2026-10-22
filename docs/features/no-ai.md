# Feature: No AI

- **Status:** Draft (policy written, not yet tested)
- **Owner decision needed:** yes — OPEN-QUESTIONS #3 (translations)
- **Roadmap tasks:** P0-03, P2-01, P2-03
- **Pref switch:** controlled by policy; no separate `chromefox.*` pref needed in Phase 0
- **Patch series:** `patches/0300-no-ai/` (only if policies prove insufficient)

## Problem

Mozilla has been adding generative-AI features to Firefox (a sidebar chatbot, link-preview
summaries, smart tab grouping and more). After user backlash, Firefox 148 (February 2026) added an "AI controls" section with a "Block AI
enhancements" switch that disables current and future generative-AI features, and enterprise
policies to set and lock it. Users of this browser should never see or run these features.

## Definition of "AI" for this project

**In scope (blocked):** every feature Mozilla lists under AI Controls — the sidebar chatbot,
link-preview key points, smart tab grouping, PDF image alt-text generation, smart window
features, on-device speech recognition and AI translations — plus any future feature Mozilla
adds there.

**Out of scope (not blocked):** Mozilla states that AI Controls do not cover "traditional
machine learning" used to classify, rank or personalize. Examples could include tracker or
phishing classification. Those are security features and stay on unless a spec says
otherwise.

**Decision pending:** translations run locally and are useful; Mozilla classes them as AI.
Default: blocked, with a documented way to re-enable (OPEN-QUESTIONS #3).

## Design

Layer 1 (enterprise policies), in `prefs/policies.json`:

- `AIControls` — `Default: { Value: "blocked", Locked: true }`. Available in Firefox ESR 153+.
  Per Mozilla's docs, blocking removes downloaded on-device models and hides the feature.
- `GenerativeAI` — `Enabled: false, Locked: true`. Older policy (Firefox 144 / ESR 140.4),
  kept as a second layer in case a feature is controlled by only one of the two.

Mozilla's reference lists the prefs `AIControls` affects (e.g. `browser.ml.chat.enabled`,
`browser.ai.control.*`, `browser.translations.enable`, `pdfjs.enableAltText`,
`browser.ml.linkPreview.enabled`, `browser.tabs.groups.smart.userEnabled`). Those are what the
tests check.

Phase 2 question (P2-03): is a locked policy enough, or should the ML code be removed from
the build? Removal reduces download size and attack surface but adds patches that must be
rebased every year. Decide with data (size, idle behavior) in an ADR.

## Security and privacy

Blocking reduces network traffic (model downloads, chatbot provider pages) and attack surface.
No new risk.

## Maintenance cost

Low. Policies are a supported interface. Each ESR major update: check the AIControls policy
reference for new keys and the release notes for new AI features (the upstream-scout agent
and Gemini's upstream report both look for this).

## Testing

Manual (P0-03), on a fresh profile of stock Firefox ESR 153 with `prefs/policies.json`
installed in its `distribution/` folder:

1. `about:policies` → Active tab lists `AIControls` and `GenerativeAI` with no errors.
2. Settings → AI Controls: "Block AI enhancements" is on and cannot be changed.
3. Sidebar: no chatbot option. Right-click a link: no AI link preview. PDF: no alt-text
   generation offer. Tab groups: no AI suggestions.
4. `about:config`: the affected prefs listed above show the blocked values and are locked.
5. Visit a page in another language: translation offer behaves per the translations decision.

## Results

_Not yet tested._

## Open questions

- Translations (OPEN-QUESTIONS #3).
- Does `GenerativeAI` add anything once `AIControls` is set? Record the answer and remove
  redundancy if not.
