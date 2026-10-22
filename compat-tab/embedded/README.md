# Stage 3 — embedded tab (research)

Phase 7, time-boxed to four weeks, Windows first with WebView2, behind
`chromefox.compatTab.embedded.enabled` (default false). Ends with a go/no-go ADR.

## Research questions

1. How does a Firefox tab's content area get its native window region on Windows, and can a
   WebView2 child window be positioned and kept in sync with it?
2. Keyboard focus, shortcuts and accessibility across the two engines.
3. Pop-ups, downloads, printing, file pickers, permissions prompts, full screen.
4. Session restore and tab switching performance.
5. Security boundary: process model, sandboxing, what the WebView2 host can access.
6. Privacy: storage separation, clearing data, private browsing.
7. Update story for the embedded runtime.

## Notes

_Add findings here with sources (Searchfox links for Firefox, Microsoft docs for WebView2)._
