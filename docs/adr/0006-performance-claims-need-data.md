# 0006 — Performance claims need data

- **Status:** Accepted
- **Date:** 2026-10-19
- **Related:** `docs/features/performance.md`, `perf/README.md`, AGENTS.md rule 2.6

## Context

The owner's goal is the most performant Firefox-based browser. Browser forks frequently
advertise speedups based on single benchmark runs, different machines, or settings copied
from "tweak" lists that trade away security or stability. Mozilla's official builds already
use PGO and LTO, so real gains are usually small and must be measured carefully to be seen
at all.

## Decision

1. No change is described as a performance improvement anywhere (PR, changelog, website)
   without results in `perf/results/` produced by the documented method in `perf/README.md`.
2. Every comparison is against **stock Firefox ESR of the same version, on the same machine,
   in the same session**, with run counts, medians and spread reported.
3. A change that improves one benchmark and regresses another is reported with both numbers.
4. Settings that weaken security or privacy are not performance tweaks, whatever they
   measure.
5. Performance experiments are pref-gated and end with "keep" or "revert" plus the data.

## Consequences

- Fewer, smaller, honest claims — which is what builds trust in a niche browser.
- The project needs a benchmark harness early (Phase 2, task P2-05).
- Benchmarks consume build-machine time; schedule them, don't run them ad hoc.
