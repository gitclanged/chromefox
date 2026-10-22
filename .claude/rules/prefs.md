---
paths:
  - "prefs/**"
---

# Rules for work under prefs/

- Every policy or pref must be documented in `prefs/README.md`: setting, why, spec, minimum
  Firefox version, and the version it was tested on.
- Verify each policy key against Mozilla's policy reference for our pinned ESR version
  (https://firefox-admin-docs.mozilla.org/reference/policies/) before adding it. Policy and
  pref names change between versions.
- `policies.json` must stay valid JSON with no comments or unknown keys.
- Never weaken security or privacy (site isolation, sandboxing, Safe Browsing, Remote
  Settings security data, certificate checks, HTTPS) — see `docs/features/performance.md`.
- A "tweak list" on the internet is not a reason. Each entry needs a spec and a reason.
