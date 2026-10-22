# tests/

Phase 1 (P1-09) adds the first smoke test. Until then, each feature spec's **Testing**
section is the test.

## Planned

| Test | Type | Checks |
| --- | --- | --- |
| Smoke | Scripted launch | Browser starts, loads a page, quits cleanly |
| Policies | Scripted check of `about:policies` state | All policies active, no errors |
| uBlock | Scripted | uBO installed and enabled on first run |
| No AI | Scripted | AI-related prefs locked to blocked values |
| Compat stage 1 | Scripted | Listed host gets Chrome UA; unlisted host doesn't |

Firefox's own test frameworks (mochitest for browser UI, xpcshell for JS modules) are used
for patches that change frontend logic; those tests live alongside the patch in the same
series and are run with `./mach test`.
