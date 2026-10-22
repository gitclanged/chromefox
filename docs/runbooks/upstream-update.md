# Runbook: upstream update (new Firefox ESR version)

Use the `/upstream-update <new-version>` skill; it follows this runbook. For a security-driven
update with a deadline, also follow [security-release.md](security-release.md).

## 0. Classify the update

| Kind | Example | Expected effort |
| --- | --- | --- |
| ESR dot release | 153.4.0esr → 153.5.0esr | Hours. Most patches apply cleanly |
| ESR major | 153.x esr → next ESR major | Weeks. Plan it as a project with its own roadmap tasks |

## 1. Gather information (upstream-scout subagent + Gemini)

1. Release notes and security advisories for the new version.
2. List of upstream files our patches touch (from `patches/REGISTRY.md`).
3. Upstream diff of those files between old and new version.
4. Gemini **Prompt 2** (upstream impact report, `docs/AI-TEAM.md`) → save to `docs/reviews/`.
5. Check the policy reference for new or renamed policies and new AI features.

## 2. Rebase on a branch

```bash
git switch -c chore/upstream-<new-version>
# edit upstream/firefox.toml: version, URL, checksum
python3 scripts/fetch_source.py
python3 scripts/apply_patches.py     # note each failure
```

For each failing patch: understand the upstream change first, then re-make our change on top
of it. Update the registry row (upstream files, risk, last rebased version). If a patch is no
longer needed, remove it and its row — that's the best outcome.

## 3. Verify

- Build; run smoke tests (`tests/`).
- Re-run the checks for `no-ai`, `debloat`, `ublock-origin` features.
- Performance spot-check against stock ESR of the **new** version.

## 4. Ship

Open the PR (title `chore(upstream): update to Firefox <new-version>`), reviewer subagent,
owner merges, then [release.md](release.md).

## Log

| Date | From → To | Patches failed | Time to ship | Notes |
| --- | --- | --- | --- | --- |
| | | | | |
