# Chromefox (working codename)

A lean, fast, privacy-respecting browser built on **Firefox ESR**, with:

- **No AI features** — blocked and locked by default.
- **No bloat** — telemetry, studies, sponsored content and nagging turned off.
- **uBlock Origin built in** — installed on first run and kept up to date.
- **A compatibility escape hatch** for the few sites that only work in a Chromium-engine browser.
- **Measured performance** — every speed claim is backed by numbers in `perf/results/`.

> **Status:** Phase 0 (planning and scaffolding). Nothing here is a usable browser yet.
> See [docs/STATUS.md](docs/STATUS.md) for exactly where the project stands today and
> [docs/ROADMAP.md](docs/ROADMAP.md) for the plan.

> **Name:** "Chromefox" is an internal codename only. "Chrome" is a Google trademark and
> the public name must be chosen before any release. See
> [docs/adr/0005-naming-and-trademarks.md](docs/adr/0005-naming-and-trademarks.md).

## How this project is built

This repository does **not** contain a copy of Firefox. It contains:

| Folder | What lives there |
| --- | --- |
| `upstream/` | Which exact Firefox ESR release we build on (one pinned version). |
| `patches/` | Our small, numbered, documented changes to Firefox's source code. |
| `prefs/` | Configuration (enterprise policies and default preferences). |
| `branding/` | Name, icons and logos that replace Firefox branding. |
| `compat-tab/` | The Chromium-compatibility feature, built in stages. |
| `perf/` | Benchmark method, baselines and results. |
| `scripts/` | Tools that fetch Firefox, apply our patches, build, check and package. |
| `docs/` | Everything a human or an AI needs to understand and continue the work. |

The build takes the pinned Firefox source, applies `patches/` and `prefs/`, and compiles.
This "patch-set" approach is how LibreWolf and Zen stay maintainable; see
[docs/adr/0001-patch-set-not-hard-fork.md](docs/adr/0001-patch-set-not-hard-fork.md).

## Where to start

| You are… | Start with |
| --- | --- |
| The project owner | [docs/00-START-HERE.md](docs/00-START-HERE.md) |
| An AI coding agent | [AGENTS.md](AGENTS.md) |
| A human contributor | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Someone new to browsers | [docs/learn/README.md](docs/learn/README.md) |

## License

Firefox source code is under the Mozilla Public License 2.0 (MPL-2.0). Our patches to
MPL files are MPL-2.0 as well. uBlock Origin is GPL-3.0 and is distributed as a separate,
unmodified extension. See [docs/FEASIBILITY.md](docs/FEASIBILITY.md#legal-and-licensing).
This repository is licensed under MPL-2.0; the full text is in [LICENSE](LICENSE).
