# Open questions (owner decisions)

Each question has a **default** the agents will use until you decide otherwise. When you
decide, write the answer here (with the date), and if it changes architecture, ask Claude to
update or add an ADR.

| # | Question | Default until decided | Why it matters | Needed by |
| --- | --- | --- | --- | --- |
| 1 | **Which platform ships first?** Windows, macOS or Linux | The OS you use daily. Builds happen on Linux if possible | Packaging, signing and the compat tab differ per OS. WebView2 makes compat stages 2–3 much easier on Windows | P1-01 |
| 2 | **uBlock Origin install mode:** `force_installed` (cannot be removed) or `normal_installed` (installed, user can disable) | `normal_installed` | "Built in" vs "user stays in control" | P0-03 |
| 3 | **Are Firefox Translations "AI"?** They run on-device and are useful, but Mozilla classes them as AI | Blocked, with a documented one-click way to re-enable | Your "no AI" promise needs a precise definition | P0-03 |
| 4 | **Public name** | "Chromefox" stays a codename | Trademark risk; branding work. The codename is public since 2026-10-22, so start trademark research earlier | P6-01 |
| 5 | **CPU baseline:** support all x86-64 CPUs, or require x86-64-v3 (roughly 2015+ CPUs with AVX2) for speed | All CPUs; v3 only if measurements justify it, possibly as a second download | Performance vs who can run it | Phase 5 |
| 6 | **Auto-update approach** | Notify-only + package managers until signing exists | Security vs infrastructure cost | P6-03 |
| 7 | **Sync and accounts:** keep Firefox Sync (Mozilla account) or remove | Keep, off by default | Users expect sync; it's Mozilla infrastructure | Phase 2 |
| 8 | **Default search engine** | Keep Firefox's default list, no deals | Revenue vs neutrality | Phase 2 |
| 10 | **Budget ceiling per month** (AI usage, machines, certificates) | None set | Prevents surprise costs | P0-02 |
| 11 | **Gemini's role:** auditor only (as `docs/AI-TEAM.md` says) or co-project manager (as the owner describes it) | Auditor: reads and reports; Claude stays the only writer | Decides what Gemini is asked for, and whether `AI-TEAM.md` and `GEMINI.md` change | P0-05 |

## Decided

Move rows here with the date and the decision.

| ID | Question / proposal | Decision | Date | Why |
| --- | --- | --- | --- | --- |
| 9 | **Public or private repository** (default was "private until Phase 6") | **Public now** | 2026-10-22 | GitHub Free offers branch protection only on public repositories; the owner chose public over paying for GitHub Pro or going without protection. Accepted consequence: the codename and all docs are visible early, so trademark research (ADR-0005) is more urgent. |
