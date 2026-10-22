# compat-tab/

Components of the Chromium-compatibility feature. Read the spec first:
[docs/features/compat-tab.md](../docs/features/compat-tab.md). Decision:
[ADR-0004](../docs/adr/0004-compat-tab-staged.md).

| Folder | Stage | What will live here | Phase |
| --- | --- | --- | --- |
| [site-rules/](site-rules/README.md) | 1 | Problem-site log, rules data, built-in extension that applies Chrome user-agent rules | 0 (log), 4 (code) |
| [companion/](companion/README.md) | 2 | Native-messaging companion app that opens a page in a Chromium-engine window | 4 |
| [embedded/](embedded/README.md) | 3 | Research notes and, if approved, the prototype | 7 |

Naming reminder: never call anything here "chrome" — in Firefox that word means the browser
UI. Use `compat-tab` / `compatTab`.

Performance requirement: zero measurable cost when the feature isn't being used.
