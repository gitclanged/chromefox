# Runbook: security release

**Target:** ship within 72 hours of Mozilla's ESR release; within 24 hours when Mozilla marks
a fix critical or actively exploited. (`SECURITY.md`)

## Trigger

- Mozilla publishes an ESR release with security advisories (Mozilla Foundation Security
  Advisories, the release calendar, or the ESR release notes).
- Later (P3-02): a scheduled CI job notices a new ESR tag automatically and opens an issue.

## Steps

1. **Freeze features.** Pause other work; this takes priority.
2. **Read the advisory.** Note the highest severity and whether it's exploited in the wild.
3. **Run [upstream-update.md](upstream-update.md)** steps 1–4, skipping the Gemini report if
   time is critical (do it afterwards for the record).
4. **Release** per [release.md](release.md), with release notes linking Mozilla's advisory.
5. **Announce** that the update is available.
6. **Record** the time to ship below.

## If we can't make the target

Publish a short notice (README, release page): which Mozilla release is pending, why we're
late, expected date, and that users at risk should use Firefox ESR meanwhile. Honesty about
delays is part of the security policy.

## Time-to-ship log

| Mozilla version | Mozilla release date | Our release date | Hours | Notes |
| --- | --- | --- | --- | --- |
| | | | | |
