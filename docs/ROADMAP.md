# Roadmap

Phases are ordered so each one delivers something usable and reduces risk for the next.
Each task has an ID (`P<phase>-<nn>`) that `STATUS.md`, branches, commits and pull requests
refer to. Durations assume a few sessions per week and are estimates, not promises.

Do not start a phase until the previous phase's **exit criteria** are met, except where
noted. When a task turns out bigger than expected, split it here first, then work on it.

---

## Phase 0 — Foundations (weeks 1–2)

Goal: a working process and proof that configuration alone delivers most of the value.

| ID | Task | Done when |
| --- | --- | --- |
| P0-01 | Git init, GitHub repo, branch protection, LICENSE via PR | `main` is protected; first PR merged by owner |
| P0-02 | Owner answers top items in `OPEN-QUESTIONS.md` | Answers recorded, ADRs updated if needed |
| P0-03 | Test `prefs/policies.json` on stock Firefox ESR 153 | Each policy verified in `about:policies`; results in feature specs |
| P0-04 | Daily-drive the Phase 0 setup for one week; log broken sites | `compat-tab/site-rules/README.md` has a real list of sites and symptoms |
| P0-05 | First Gemini audit of the scaffolding | Report in `docs/reviews/`; findings triaged |
| P0-06 | Owner completes learn lessons 01–04 | Owner can explain the build pipeline diagram in their own words |

**Exit criteria:** process works end to end (task → branch → PR → review → merge → status);
policies verified on ESR 153; real list of problem sites exists.

---

## Phase 1 — Reproducible build (weeks 3–8)

Goal: one command turns this repository into an installable, unbranded-then-branded browser
on the first platform.

| ID | Task | Done when |
| --- | --- | --- |
| P1-01 | Pin exact ESR dot release in `upstream/firefox.toml` | Version, URL and checksum recorded |
| P1-02 | `scripts/fetch_source.py` — download and verify the source tarball | Checksum verified; idempotent; documented |
| P1-03 | `scripts/apply_patches.py` — apply series in order, fail loudly | Works on an empty patch set and a test patch |
| P1-04 | `mozconfig` for release builds (optimization flags per `features/performance.md`) | Reviewed; flags explained in comments |
| P1-05 | First full build on the build machine | Build time, machine specs and warnings recorded in a devlog |
| P1-06 | Bake `prefs/policies.json` into the build's `distribution/` folder | Fresh install shows policies in `about:policies` |
| P1-07 | Branding patch series (`0100`) with placeholder name and icons | No Firefox trademarks visible in UI |
| P1-08 | `scripts/package.py` — installer/archive for the first platform | Installs and launches on a clean machine/VM |
| P1-09 | Smoke test checklist and script (`tests/`) | Launch, load sites, uBlock active, AI blocked |
| P1-10 | CI: verify patches apply to the pinned source | Workflow green on `main` |

**Exit criteria:** a clean machine can produce the installer by following
`runbooks/build-locally.md`; smoke tests pass; build time known.

---

## Phase 2 — Debloat and no-AI hardening (weeks 6–12, overlaps Phase 1)

| ID | Task | Done when |
| --- | --- | --- |
| P2-01 | Audit what still phones home or nags (network log of a fresh profile) | Findings listed in `features/debloat.md` |
| P2-02 | Fix each finding at the least intrusive layer | Each fix registered; re-audit is clean |
| P2-03 | Decide whether to compile out AI/ML code or rely on the locked policy | ADR written |
| P2-04 | Settings UI shows our defaults clearly (no "managed by your organization" confusion) | Owner approves screenshots |
| P2-05 | Performance baseline: stock ESR vs our build, same machine | Results in `perf/results/` |

---

## Phase 3 — The maintenance machine (weeks 8–14)

Goal: shipping a Firefox security update is boring, fast and mostly automated.

| ID | Task | Done when |
| --- | --- | --- |
| P3-01 | Run `runbooks/upstream-update.md` for a real ESR dot release | Shipped within the SECURITY.md target |
| P3-02 | CI job: test patches against the newest ESR as soon as it is tagged | Alerts on conflict |
| P3-03 | Gemini upstream impact report as a standard step | Report template in `docs/reviews/` |
| P3-04 | Track "time to ship" for every security release | Table in `docs/runbooks/security-release.md` |

**Exit criteria:** two consecutive ESR updates shipped on time with the runbook unchanged
or improved.

---

## Phase 4 — Compat tab stages 1–2 (months 3–5)

| ID | Task | Done when |
| --- | --- | --- |
| P4-01 | Stage 1: per-site Chrome user-agent rules, shipped as a built-in component | Owner's problem-site list re-tested; results recorded |
| P4-02 | Stage 1: UI to add a site to the rules list ("Pretend to be Chrome here") | Works without a restart |
| P4-03 | Stage 2: companion — open current page in a Chromium app window with a separate profile | Works on the first platform with an installed Chromium-family browser |
| P4-04 | Stage 2: Windows WebView2 shell (no Chrome install needed) | Only if the first platform is Windows |
| P4-05 | Privacy review: what data crosses between the two browsers | Documented in the spec |

---

## Phase 5 — Performance program (from month 3, ongoing)

See `docs/features/performance.md`. Tasks are added there as experiments; each ends with
"keep" or "revert" and the data.

---

## Phase 6 — Public distribution (month 4+)

| ID | Task | Done when |
| --- | --- | --- |
| P6-01 | Choose and check the public name (ADR-0005) | Owner decision recorded |
| P6-02 | Code signing on the first platform | Installer passes OS checks without warnings |
| P6-03 | Update mechanism (start: update notification + package managers) | ADR written; works |
| P6-04 | Website, download page, release notes process | Live |
| P6-05 | Second platform | Same exit criteria as Phase 1 |

---

## Phase 7 — Compat tab stage 3 research spike (month 6+, time-boxed)

| ID | Task | Done when |
| --- | --- | --- |
| P7-01 | Four-week prototype: WebView2 in a tab on Windows, behind a pref | Demo or a documented failure |
| P7-02 | Go / no-go ADR covering security, privacy, maintenance cost | Owner decision recorded |

---

## Not planned (and why)

- **Forking Chromium.** Cost far beyond one maintainer; see `FEASIBILITY.md`.
- **Tracking Firefox rapid release.** Two-week cadence; see ADR-0002.
- **Android/iOS.** Different codebases (GeckoView / WebKit-only on iOS).
