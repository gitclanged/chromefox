# Runbook: release

**Status:** outline; completed in Phase 6 (signing, update channel, website).

## Version numbers

`<firefox-esr-version>-cfx.<n>` — e.g. `153.4.0-cfx.1`. `n` restarts at 1 for each new
Firefox version and increases for our own fixes on the same Firefox version. Git tag:
`v153.4.0-cfx.1`.

## Checklist

1. `main` is green; every PR for this release is merged.
2. `CHANGELOG.md`: move "Unreleased" items under the new version with today's date. Security
   releases list Mozilla's advisory links.
3. Compat tab: `chromeMajor` in the site-rules data matches current Chrome stable.
4. Build from a clean checkout of the tag (not from a working tree).
5. Smoke tests pass on a clean machine or VM.
6. Sign installers (once P6-02 exists).
7. Create the GitHub release from the tag; attach installers and checksums.
8. Update the website/download page and package-manager manifests (once they exist).
9. Update `docs/STATUS.md`.

## Log

| Version | Date | Who | Notes |
| --- | --- | --- | --- |
| | | | |
