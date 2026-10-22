# Architecture Decision Records

An ADR records a decision that would be expensive to reverse: what we chose, what else we
considered, and why. Future you (and future agents) will ask "why is it like this?" — the
ADR is the answer.

## Rules

- Copy [0000-template.md](0000-template.md); number sequentially; never reuse a number.
- Status is one of: `Proposed`, `Accepted`, `Superseded by NNNN`, `Rejected`.
- Once **Accepted**, don't rewrite the decision. If it changes, write a new ADR that
  supersedes it and update the old one's status line only.
- An ADR is short: one page is ideal.
- The owner accepts ADRs. Agents may propose them.

## Index

| # | Title | Status |
| --- | --- | --- |
| 0001 | [Patch-set repository, not a hard fork](0001-patch-set-not-hard-fork.md) | Accepted |
| 0002 | [Build on Firefox ESR](0002-esr-base.md) | Accepted |
| 0003 | [uBlock Origin via enterprise policy](0003-ublock-via-policy.md) | Accepted |
| 0004 | [Compat tab in stages](0004-compat-tab-staged.md) | Accepted |
| 0005 | [Naming and trademarks](0005-naming-and-trademarks.md) | Proposed |
| 0006 | [Performance claims need data](0006-performance-claims-need-data.md) | Accepted |
| 0007 | [AGENTS.md is the single source of agent instructions](0007-agents-md-single-source.md) | Accepted |
