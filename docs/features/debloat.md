# Feature: Debloat

- **Status:** Draft (four policies written; audit not started)
- **Roadmap tasks:** P0-03, P2-01, P2-02, P2-04
- **Pref switch:** per item; listed in the table as items are added
- **Patch series:** `patches/0200-debloat/`

## Problem

Stock Firefox sends usage data, runs remote experiments ("studies"), shows sponsored content
and promotional messages, and nags about being the default browser. Each costs a little
network, CPU, attention or trust.

## Goals

- A fresh profile left idle for 30 minutes makes **no** network requests except those needed
  for security (certificate revocation, blocklists, safe browsing, extension and browser
  updates) and the ones the user asked for.
- No sponsored content or Mozilla product promotions anywhere in the UI.
- No "make default browser" or survey prompts.

## Non-goals — things we keep on purpose

These look like "phoning home" but protect users. **Do not disable them** without an ADR:

- Remote Settings security collections (certificate revocation data, add-on and plugin
  blocklists). Mozilla's own policy for turning Remote Settings off is named
  `DisableRemoteSettingsAndAcceptSecurityConsequences` for a reason.
- Safe Browsing (phishing and malware protection), until a spec weighs the privacy trade-off.
- Update checks (browser and extensions).
- Site isolation, sandboxing and HTTPS protections — these are not bloat.

## Design

Layer 1 first. Current draft in `prefs/policies.json`:

| Policy | Value | What it does | Verified on ESR 153? |
| --- | --- | --- | --- |
| `DisableTelemetry` | `true` | Stops usage-data reporting | No |
| `DisableFirefoxStudies` | `true` | Stops remote experiments | No |
| `DisableFeedbackCommands` | `true` | Removes "Submit feedback" menu items | No |
| `DontCheckDefaultBrowser` | `true` | No default-browser prompt | No |

Candidates to evaluate in P2-01 (verify each against the policy reference for ESR 153 before
adding — key names change between versions): `FirefoxHome` (sponsored shortcuts and stories),
`FirefoxSuggest` (sponsored address-bar suggestions), `UserMessaging` (recommendations,
onboarding), `DisableDefaultBrowserAgent` (Windows background task),
`DisableRemoteImprovements`, `NewTabPage`, `SkipTermsOfUse`.

Anything a policy can't reach → default pref in `prefs/` → frontend patch in `0200-debloat`.

## How the audit works (P2-01)

1. Fresh profile, our policies installed.
2. Record all network requests from launch through 30 minutes idle (Firefox's network
   monitor for the browser itself, or a local intercepting proxy).
3. For each destination: what is it, which feature, is it in "keep on purpose"?
4. Walk every screen (new tab, settings, menus, address bar suggestions) and screenshot
   anything sponsored or promotional.
5. Record findings in the table below; each becomes a task.

## Findings

| # | What | Where seen | Fix layer | Status |
| --- | --- | --- | --- | --- |
| — | _Audit not run yet_ | | | |

## Testing

Re-run the audit after each fix; a clean audit is the exit criterion.
