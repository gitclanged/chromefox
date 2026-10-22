---
name: upstream-update
description: Move Chromefox to a new Firefox ESR version following docs/runbooks/upstream-update.md - research, re-pin, rebase patches, verify, and open the pull request. Use when Mozilla releases a new ESR version, especially security releases.
argument-hint: "[new ESR version, e.g. 153.5.0esr]"
disable-model-invocation: true
---

# Upstream update to $ARGUMENTS

Follow `docs/runbooks/upstream-update.md` exactly; if reality differs from the runbook, update
the runbook in the same pull request.

1. Read `upstream/firefox.toml` for the current version. Classify: dot release or ESR major.
   If it's a security release, also follow `docs/runbooks/security-release.md` and tell the
   owner the deadline.
2. Run the `upstream-scout` subagent for old → new. Summarize urgency for the owner.
3. Suggest the owner run Gemini Prompt 2 (`/gemini-handoff upstream`) unless time is critical.
4. Branch `chore/upstream-$ARGUMENTS`. Update `upstream/firefox.toml` (version, sha256 from
   Mozilla's SHA256SUMS, pinned_on).
5. Fetch and verify the source; apply patches. For each failure: show the upstream change that
   caused it, re-make our change minimally, update the registry row. Remove patches that are
   no longer needed.
6. Re-check `prefs/policies.json` keys against the policy reference for the new version.
7. Build, run smoke tests and the no-ai / debloat / ublock-origin test steps.
8. Fill the runbook's log row. Update STATUS.md, devlog, CHANGELOG (link Mozilla's advisories).
9. Reviewer subagent → pull request titled `chore(upstream): update to Firefox $ARGUMENTS`.
