# Stage 2 — companion window

Phase 4 (P4-03, P4-04). Design is in `docs/features/compat-tab.md` → "Stage 2".

## Planned pieces

| Piece | Purpose |
| --- | --- |
| Native-messaging host manifest | Registers the companion with the browser; allows only our extension ID |
| Companion program | Receives one URL, validates it (http/https only), launches the Chromium window |
| Launch adapters | One per supported engine: installed Edge/Chrome/Chromium/Brave in app mode with a dedicated profile; WebView2 shell on Windows |
| Installer integration | Installs and registers the companion with the browser |

## Decisions to make before coding (record as ADR)

- Implementation language for the companion (small, signed, cross-platform binary).
- Where the dedicated compat profile lives and how users can clear it.
- How the browser shows that a page was opened in the other engine.
