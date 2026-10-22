# Feature: Performance program

- **Status:** Spec draft
- **Roadmap tasks:** P1-04, P2-05, Phase 5 experiments
- **Rules:** [ADR-0006](../adr/0006-performance-claims-need-data.md) — no claim without data
- **Method:** [perf/README.md](../../perf/README.md)
- **Patch series:** `patches/0600-performance/`

## Goal, stated honestly

Be **measurably leaner and at least as fast** as stock Firefox ESR of the same version on
every tracked metric, and faster where our choices (less background work, tuned builds)
allow. Publish every result, including the ones where we don't win.

## The biggest risk: being *slower* than stock

Mozilla's release builds use profile-guided optimization (PGO) and link-time optimization
(LTO). A plain source build does not get those automatically. **A fork built with default
options can be noticeably slower than the Firefox it came from.** Task P1-04 must produce a
`mozconfig` that matches Mozilla's release optimization settings for our platform, and P2-05
must prove it against stock ESR before any other performance work matters.

## Metrics

| Metric | Why it matters | Tool (to confirm in P2-05) |
| --- | --- | --- |
| Speedometer 3 score | Responsiveness of real web-app patterns | browserbench.org |
| JetStream score | JavaScript and WebAssembly throughput | browserbench.org |
| MotionMark score | Graphics/animation | browserbench.org |
| Cold and warm startup time | What users feel first | Scripted launch timing |
| Memory with a fixed set of N tabs | Laptops and long sessions | `about:memory` reports |
| Idle CPU wakeups and network requests | Battery, privacy, "bloat" | OS tools + network log |
| Page-load time on a fixed page set | Everyday browsing | Mozilla's `mach perftest` tooling or equivalent |
| Download / install size | Bloat | File sizes |

## Experiment backlog

Each experiment: hypothesis → pref or build flag → measure against baseline → keep or revert.

| ID | Hypothesis | Layer | Risk |
| --- | --- | --- | --- |
| E1 | Our build matches stock ESR when PGO + LTO are configured like Mozilla's | Build | None — this is the baseline requirement |
| E2 | Building for x86-64-v3 (AVX2) speeds up JS/graphics benchmarks by a measurable amount | Build | Won't run on older CPUs (OPEN-QUESTIONS #5) |
| E3 | Removing telemetry, studies, sponsored fetches and AI models reduces idle CPU, network and memory | Policies | Low |
| E4 | Fewer bundled system add-ons/features shortens startup | Prefs / patches | Medium — check what each add-on does first |
| E5 | Compat tab adds zero cost when unused | Design | Must hold or the feature is redesigned |

## Never do these for speed

- Disable site isolation, sandboxing, or process separation.
- Disable security-related Remote Settings data, Safe Browsing or certificate checks.
- Lower TLS or HTTPS requirements.
- Copy settings from online "tweak" lists without a hypothesis and a measurement.

## Results

_No measurements yet. Baseline is task P2-05._
