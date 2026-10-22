# prefs/

Configuration that ships with the browser — layers 1 and 2 in `docs/ARCHITECTURE.md`.

## `policies.json` (enterprise policies)

Copied into the installed browser's `distribution/` folder by the build (P1-06). JSON can't
hold comments, so **every policy is documented here**. Policy reference:
https://firefox-admin-docs.mozilla.org/reference/policies/

| Policy | Setting | Why | Spec | Min. version | Tested on |
| --- | --- | --- | --- | --- | --- |
| `AIControls` | `Default` blocked, locked | Blocks all current and future Firefox AI features | no-ai | Firefox ESR 153 | — |
| `GenerativeAI` | disabled, locked | Older AI switch, kept as a second layer until P0-03 shows it's redundant | no-ai | Firefox 144 / ESR 140.4 | — |
| `DisableTelemetry` | true | No usage-data reporting | debloat | long-standing | — |
| `DisableFirefoxStudies` | true | No remote experiments | debloat | long-standing | — |
| `DisableFeedbackCommands` | true | Removes feedback/survey menu items | debloat | long-standing | — |
| `DontCheckDefaultBrowser` | true | No default-browser prompt | debloat | long-standing | — |
| `ExtensionSettings` → `uBlock0@raymondhill.net` | `normal_installed` from AMO, toolbar button | Installs uBlock Origin on first run; AMO keeps it updated | ublock-origin | long-standing (`default_area` since 113) | — |

### Try it on stock Firefox before any build exists (task P0-03)

1. Install **Firefox ESR 153** separately from your everyday Firefox (or use a VM).
2. Copy `policies.json` into its `distribution/` folder (create it if missing):
   - Windows: `C:\Program Files\Mozilla Firefox\distribution\` (inside the ESR install folder)
   - macOS: `Firefox.app/Contents/Resources/distribution/`
   - Linux: `<install dir>/distribution/`, or system-wide `/etc/firefox/policies/`
3. Start it, open `about:policies` and check every policy is listed as active with no errors.
4. Run the test steps in `docs/features/no-ai.md` and `docs/features/ublock-origin.md`;
   record results in their **Results** sections and in the "Tested on" column above.

Note: policies apply to every profile of that installation, and Firefox's settings page will
say the browser is "managed by your organization". That's expected (ADR-0003).

## Default prefs (layer 2)

For settings with no policy. Added as features need them, in a defaults file the build
copies into the tree (format decided in Phase 1). Each pref gets: name, value, why, the
upstream source location where the pref is defined (Searchfox link for our pinned version),
and the version it was verified on. Prefs that don't exist in our pinned version are bugs.

## Rules

- Don't add a pref because a "tweak list" recommends it. Every entry needs a spec and a reason.
- Never weaken security or privacy protections here (see `docs/features/performance.md`
  "Never do these for speed").
- Re-verify every entry on each ESR major update.
