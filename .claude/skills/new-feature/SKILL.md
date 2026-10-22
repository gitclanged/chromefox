---
name: new-feature
description: Start a new feature properly - create its spec from the template, decide whether an ADR is needed, add roadmap tasks, and get owner approval before any implementation. Use whenever the owner asks for a new capability or behavior change.
argument-hint: "[feature-name]"
---

# New feature: $ARGUMENTS

1. Check `docs/features/` and `docs/ROADMAP.md` — does this already exist or overlap?
2. Interview the owner briefly (at most five questions) to fill the gaps: the problem, what
   success looks like, what's out of scope, which platforms.
3. Copy `docs/features/TEMPLATE.md` to `docs/features/<kebab-name>.md` and fill in Problem,
   Goals, Non-goals, Design (layer choice and why), Security and privacy, Maintenance cost,
   Testing. Mark unknowns explicitly.
4. If the design makes a hard-to-reverse choice (new patch series, new dependency, a second
   engine, changes to updates/signing/security), draft an ADR from `docs/adr/0000-template.md`
   with status Proposed and add it to `docs/adr/README.md`.
5. Add task rows to `docs/ROADMAP.md` in the right phase, and the spec to
   `docs/features/README.md`.
6. Add a pref name `chromefox.<feature>.enabled` to the spec unless there's a reason not to.
7. Commit on a `docs/<feature>-spec` branch and open a pull request. Explain the spec to the
   owner in plain language and ask for approval. No implementation until it's merged.
