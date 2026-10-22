---
paths:
  - "compat-tab/**"
  - "patches/0500-compat-tab/**"
  - "docs/features/compat-tab.md"
---

# Rules for the compat tab

- The word "chrome" is reserved (Mozilla uses it for the browser UI). Use `compat-tab`,
  `compatTab`, `chromefox.compatTab.*`.
- Follow the stages in ADR-0004. Don't start stage 2 work before stage 1 ships, or stage 3
  before the owner approves the spike.
- Prefer a built-in WebExtension plus the native companion over frontend patches.
- The companion accepts only `http:`/`https:` URLs and launches only allow-listed executables.
  No cookies, passwords or history cross between engines.
- Zero measurable cost when unused: no Chromium process, memory or startup time until the
  user invokes the feature.
- Every behavior is behind its `chromefox.compatTab.*` pref.
