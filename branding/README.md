# branding/

Name, icons and logos that replace Firefox branding. Built into the browser through Firefox's
branding mechanism (a branding directory selected in `mozconfig`), plus patches in
`patches/0100-branding/` for anything that mechanism doesn't cover.

## Status

Placeholder. The public name is undecided ([ADR-0005](../docs/adr/0005-naming-and-trademarks.md)).
Phase 1 (P1-07) uses a neutral placeholder name and icon so no Mozilla trademarks appear.

## Planned contents

| Item | Notes |
| --- | --- |
| App name strings | Short name, full name, vendor |
| Icons | All sizes each platform needs; source SVG kept here |
| About dialog / wordmark | |
| Installer artwork | Per platform |

## Rules

- No Firefox name or logos anywhere in the shipped UI.
- Keep the codename in as few places as possible so the rename before release is small.
- Licensing of icons and fonts recorded here.
