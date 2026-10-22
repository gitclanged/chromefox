# scripts/

Small tools, one job each, Python 3 standard library unless a README entry says otherwise.
Every script supports `--help`. The same checks run in Claude Code hooks and in CI.

## Available now

| Script | What it does | Used by |
| --- | --- | --- |
| `check_registry.py` | Verifies `patches/` and `patches/REGISTRY.md` agree (IDs, file names, series ranges, specs, layers, reasons) | Stop hook, CI, before every commit |
| `check_links.py` | Verifies relative links and `@imports` in all Markdown files resolve | Stop hook, CI |
| `pack_context.py` | Packs the repo into `.context/chromefox-context.md` for Gemini, with a token estimate | `/gemini-handoff` |

```bash
python3 scripts/check_registry.py
python3 scripts/check_links.py
python3 scripts/pack_context.py --help
```

## Planned (each is a roadmap task; contracts below are the spec)

| Script | Task | Contract |
| --- | --- | --- |
| `fetch_source.py` | P1-02 | Read `upstream/firefox.toml`; download tarball and `SHA256SUMS` (+ signature) into `work/`; verify; unpack to `work/firefox-<version>/`; idempotent; exit non-zero on any mismatch |
| `apply_patches.py` | P1-03 | Apply every `patches/*/*.patch` in numeric order to a pristine tree; stop at the first failure and print patch ID, file and rejected hunk; `--check` mode applies nothing |
| `package.py` | P1-08 | Turn `mach package` output into the platform installer/archive with checksums in `dist/` |
| `bench.py` | P2-05 | Run the benchmark method in `perf/README.md`; write raw data to `perf/raw/`, summary to `perf/results/` |
| `upstream_diff.py` | P3-03 | For two Firefox versions, produce the diff of every upstream file listed in the registry (input for Gemini Prompt 2) |

## Rules for scripts

- One job per script; compose them in runbooks, not inside each other.
- Fail loudly with a message a non-programmer can act on.
- No network access except `fetch_source.py`.
- Never modify files outside `work/`, `dist/`, `perf/`, `.context/` unless that's the script's
  documented job.
