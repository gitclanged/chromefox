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
plan stands until you decide. Status is `open`, `accepted → <task or ADR>`, or
`rejected (<why>)`.

| ID | Proposal | Instead of | Why it might be better | Risks / not yet verified | Raised | Status |
| --- | --- | --- | --- | --- | --- | --- |

## Decided

_Move rows here with the date and the decision._
