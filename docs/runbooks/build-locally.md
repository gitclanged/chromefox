# Runbook: build locally

**Status:** outline. Phase 1 tasks P1-01 … P1-08 turn this into exact, tested commands.

## Machine

| | Minimum (Mozilla's docs) | Recommended for this project |
| --- | --- | --- |
| RAM | 4 GB, 8 GB+ recommended | 16–32 GB (optimized builds with LTO are memory-hungry) |
| Disk | 30 GB (Linux/macOS), 40 GB (Windows) free | 100+ GB free on an SSD (source, build output, a second tree for rebasing, benchmarks) |
| CPU | 64-bit | 8+ cores; more cores = shorter builds |
| OS | Linux, macOS, Windows | Linux is the simplest build host; build the first platform's installer natively or as Mozilla supports |

On Windows, Mozilla recommends a Dev Drive for 5–10% faster builds, and requires short paths
without spaces for the source tree.

## Prerequisites

- Python 3 (also required by `mach` and by our scripts and hooks).
- Git.
- Firefox's own toolchain, installed by `./mach bootstrap` inside the unpacked source.
- On Windows: MozillaBuild (Mozilla's shell environment).

## Steps (to be finalized)

```bash
# 1. Fetch and verify the pinned Firefox source (P1-02)
python3 scripts/fetch_source.py            # → work/firefox-<version>/

# 2. Apply our patches in order (P1-03)
python3 scripts/apply_patches.py           # stops at the first failing patch

# 3. Install Firefox's toolchain (first time only)
cd work/firefox-<version> && ./mach bootstrap

# 4. Build (P1-04, P1-05)
MOZCONFIG=../../mozconfig ./mach build     # hours the first time

# 5. Try it
./mach run

# 6. Package (P1-08)
./mach package && cd ../.. && python3 scripts/package.py
```

## Build options (`mozconfig`, P1-04)

The release `mozconfig` must reproduce Mozilla's release optimizations, otherwise our build is
slower than stock Firefox (see `docs/features/performance.md`). Starting points for Claude to
**verify against the pinned version's build documentation** before use:

- release/optimized build settings;
- profile-guided optimization (PGO) and link-time optimization (LTO);
- `--with-branding=` pointing at our branding directory (Phase 1, P1-07);
- no debug symbols in release packages (keep them separately for crash analysis).

Every line in `mozconfig` gets a comment saying what it does and why.

## Frontend-only work: artifact builds

When a change touches only JavaScript/HTML/CSS, an artifact build downloads Mozilla's
compiled engine and builds in minutes. Confirm that Mozilla publishes matching artifacts for
our ESR revision before relying on this. Release builds are always full builds.

## Log

| Date | Who | Duration | Notes |
| --- | --- | --- | --- |
| | | | |
