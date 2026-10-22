# Open questions (owner decisions)

Each question has a **default** the agents will use until you decide otherwise. When you
decide, write the answer here (with the date), and if it changes architecture, ask Claude to
update or add an ADR.

| # | Question | Default until decided | Why it matters | Needed by |
| --- | --- | --- | --- | --- |
| 1 | **Which platform ships first?** Windows, macOS or Linux | The OS you use daily. Builds happen on Linux if possible | Packaging, signing and the compat tab differ per OS. WebView2 makes compat stages 2–3 much easier on Windows | P1-01 |
| 2 | **uBlock Origin install mode:** `force_installed` (cannot be removed) or `normal_installed` (installed, user can disable) | `normal_installed` | "Built in" vs "user stays in control" | P0-03 |
| 3 | **Are Firefox Translations "AI"?** They run on-device and are useful, but Mozilla classes them as AI | Blocked, with a documented one-click way to re-enable | Your "no AI" promise needs a precise definition | P0-03 |
| 4 | **Public name** | "Chromefox" stays a codename | Trademark risk; branding work | P6-01 |
| 5 | **CPU baseline:** support all x86-64 CPUs, or require x86-64-v3 (roughly 2015+ CPUs with AVX2) for speed | All CPUs; v3 only if measurements justify it, possibly as a second download | Performance vs who can run it | Phase 5 |
| 6 | **Auto-update approach** | Notify-only + package managers until signing exists | Security vs infrastructure cost | P6-03 |
| 7 | **Sync and accounts:** keep Firefox Sync (Mozilla account) or remove | Keep, off by default | Users expect sync; it's Mozilla infrastructure | Phase 2 |
| 8 | **Default search engine** | Keep Firefox's default list, no deals | Revenue vs neutrality | Phase 2 |
| 9 | **Public or private repository** | Private until Phase 6 | MPL requires publishing source when you distribute binaries | Before first public binary |
| 10 | **Budget ceiling per month** (AI usage, machines, certificates) | None set | Prevents surprise costs | P0-02 |

## Proposals (better options)

Ideas from Claude, Gemini or you that would change the plan (AGENTS.md section 9). The current
plan stands until you decide. When you decide, move the row to "Decided" below with the date
and the outcome: accepted (with the task or ADR it became) or rejected (with the reason).

| ID | Proposal | Instead of | Why it might be better | Risks / not yet verified | Raised | Status |
| --- | --- | --- | --- | --- | --- | --- |
| IDEA-01 | Build compat-tab stage 1 on `declarativeNetRequest` header rules plus content scripts registered only for listed sites | The spec's open "modifies requests to listed hosts" mechanism, e.g. a request listener in extension code | Hypothesis: Firefox applies the rules itself, so unlisted sites run no extension code, making "no measurable cost when unused" easier to meet. Must be measured (ADR-0006); Firefox may still evaluate the rules on every request | Not verified: that Firefox ESR 153 lets these rules change the `User-Agent` header, and that a registered script can set `navigator.userAgent` before page scripts read it. Check on Searchfox/MDN before P4-01 | Claude, 2026-10-22 | open |
| IDEA-02 | "Upstream first" for class A sites: report each to Mozilla's web-compatibility tracker, link the report from our rule, and delete our rule once Mozilla ships an intervention | Keeping our own rule list forever | Mozilla's interventions (`about:compat`) come with Firefox, so our list shrinks instead of growing, and every Firefox user benefits | A few minutes per site (estimate); Mozilla may decline some sites; how fast their fixes reach our build depends on our update setup (not verified) | Claude, 2026-10-22 | open |
| IDEA-03 | On Windows, stage 2 targets Microsoft Edge in app mode with a dedicated profile first, and builds the WebView2 shell (P4-04) only if users without Edge turn out to matter | Building the Chromium-browser launcher (P4-03) and the WebView2 shell (P4-04) together | Defers P4-04, the bigger piece, possibly for good: Edge is believed to come with Windows 10 and 11, so one launcher may cover nearly every Windows user | Only relevant if Windows ships first (question 1). Not verified, needs Microsoft sources: that Edge is present on current Windows installs, where it can be removed (reportedly the EEA), and how Edge behaves with `--app` plus a separate profile folder | Claude, 2026-10-22 | open |
| IDEA-04 | Start the stage 3 spike with a "docked" companion window — a borderless Chromium window that follows the tab's position and size — before trying true embedding | Going straight to a WebView2 child window inside Firefox's own window | Much of the "feels like a tab" experience, possibly with few changes inside Firefox; if good enough, stage 3 may never need engine-level work | **Security:** while the window covers the tab, Firefox's address bar and padlock show the tab's address, not the page the user is really on (spoofing risk; needs a clear boundary). Not verified that an extension can even learn the content area's position and size, so a frontend patch may be needed. Fragile: focus, stacking order, high-DPI, multiple monitors. Untested | Claude, 2026-10-22 | open |
| IDEA-05 | Write the stage 2 companion program in Rust | Leaving the language open (`compat-tab/companion/README.md` lists it as an ADR to write) | Rust is already required to build Firefox, so no new language or toolchain to install, learn or keep updated | Like any companion it still needs code signing (P6-02). Decide by ADR when P4-03 starts | Claude, 2026-10-22 | open |

## Decided

_Move rows here with the date and the decision._
