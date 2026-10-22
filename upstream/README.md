# upstream/

`firefox.toml` pins the one Firefox ESR release we build on. Everything in `patches/` is
written against exactly this version.

- Changing the pin is an **upstream update** — use `/upstream-update` and follow
  [docs/runbooks/upstream-update.md](../docs/runbooks/upstream-update.md).
- The source tarball is downloaded into `work/` (ignored by git) by `scripts/fetch_source.py`
  (Phase 1, P1-02), which must verify the checksum and Mozilla's signature on the checksum
  file before unpacking.
- Why ESR: [ADR-0002](../docs/adr/0002-esr-base.md).
