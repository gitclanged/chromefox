# 0002 — Build on Firefox ESR

- **Status:** Accepted
- **Date:** 2026-10-19
- **Related:** ADR-0001, `SECURITY.md`, `docs/runbooks/upstream-update.md`

## Context

Firefox's rapid-release channel moved to a **two-week** cadence starting with Firefox 155
on September 1, 2026. Each rapid release can change any file our patches touch.
Firefox **ESR 153** was released July 21, 2026 and is supported for at least 15 months;
between major ESR versions it receives security and stability fixes, not new features.
ESR 140 reached end of life on September 29, 2026.

The project has one owner and AI agents. Rebasing every two weeks would consume most of the
project's capacity and increase the chance of shipping a broken or late security update.

## Options considered

1. **Rapid release.** Newest features and web-compat fixes; a rebase every two weeks.
2. **ESR.** Stable base; small security updates; one large rebase per year when the next
   ESR major arrives. Web features lag rapid release by up to a year.
3. **Rapid release with lag** (skip some releases). Security fixes would be late. Rejected.

## Decision

Build on the current ESR major (153). Track its dot releases for security fixes. Begin the
rebase to the next ESR major as soon as Mozilla publishes it, and finish before the old ESR
reaches end of life.

## Consequences

- Fewer, smaller upstream updates; most can be close to mechanical.
- Some new web features arrive later than in Firefox. A small number of sites may notice;
  the compat tab is the escape hatch.
- New Firefox features we would have to strip (e.g., new AI features) arrive in batches,
  once a year, and can be planned for.
- Revisit if the ESR cadence or support length changes, or if the project gains maintainers.
