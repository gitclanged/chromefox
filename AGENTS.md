# AGENTS.md — rules for every AI agent working on this repository

This file is the single source of truth for AI agents (Claude Code, Gemini, anything else).
`CLAUDE.md` and `GEMINI.md` import it and add only tool-specific notes. If you change a rule,
change it here.

## 1. What this project is

A browser built from **Firefox ESR source + a small set of documented patches + configuration**.
We never commit Firefox's source code. Read these before doing real work:

- `docs/STATUS.md` — where the project is right now and what the next task is.
- `docs/ARCHITECTURE.md` — the parts of the system and how they connect.
- `docs/QUALITY.md` — what "done" means and the anti-spaghetti rules.
- `docs/WORKFLOW.md` — branches, commits, pull requests, session start and end.

The project owner is **not a programmer**. They are learning as the project goes. Every
explanation you give them must be understandable without coding knowledge (see section 6).

## 2. Hard rules (never break these)

1. **Never work on `main`.** Create a branch named `<type>/<short-topic>` before the first edit.
2. **Never commit Firefox source.** Only our patches, config, scripts and docs live here.
3. **Every patch is registered.** A file in `patches/` must have a row in
   `patches/REGISTRY.md`, and every row must point to a real file. `scripts/check_registry.py`
   enforces this; run it before every commit.
4. **Least-intrusive layer first.** Solve a problem with the highest layer that works:
   enterprise policy → default pref → frontend (JS/CSS/HTML) patch → C++/Rust patch.
   Going down a layer requires one sentence in the registry's "Why" column saying why the
   layer above was not enough.
5. **One purpose per patch, one purpose per pull request.** If you are writing "and" in a
   commit summary, split it.
6. **No performance claim without data.** Numbers come from `perf/` runs, with the method,
   machine and run count recorded. "Should be faster" is not a claim.
7. **Do not touch security-sensitive areas without stopping to ask the owner first:**
   sandboxing, IPC, networking/TLS, certificate handling, the updater, code signing,
   extension signing checks, anything in `security/` or `ipc/` upstream.
8. **Docs change in the same pull request as the behavior they describe.**
9. **Never put secrets in the repo** (signing keys, API keys, tokens). Use GitHub Secrets.
10. **The word "chrome" is reserved.** In Firefox code, "chrome" means the browser's own UI.
    Our Chromium-compatibility feature is called **compat tab** in code, prefs, file names
    and docs (`compat-tab`, `compatTab`, `chromefox.compatTab.*`).

## 3. How to work

1. **Orient.** Read `docs/STATUS.md` and the latest file in `docs/devlog/`. State the task
   you are picking up and confirm it is the "Next up" item, unless the owner said otherwise.
2. **Spec before code.** A feature needs a spec in `docs/features/`. A choice that would be
   hard to reverse needs an ADR in `docs/adr/`. Write or update these first.
3. **Plan.** For anything bigger than a one-file change, write a short plan (files you will
   touch, how you will verify) and show it to the owner before editing.
4. **Small steps.** Make one logical change, verify it, commit it. Repeat.
5. **Verify.** Run the checks in `docs/QUALITY.md`. If you could not verify something, say
   so plainly in the pull request — never imply a check ran when it did not.
6. **Review.** Before opening a pull request, have the `reviewer` subagent (or another agent
   that did not write the change) review the diff against this file and `docs/QUALITY.md`.
7. **Record.** Update `docs/STATUS.md`, add a devlog entry, update `CHANGELOG.md` under
   "Unreleased" when users would notice the change.

## 4. Commits and pull requests

- Commit messages follow Conventional Commits: `type(scope): summary`.
  Types: `feat fix perf docs refactor test build ci chore revert`.
  Scopes: `upstream patches prefs branding compat-tab perf scripts docs adr ci agents`.
  Example: `feat(prefs): block all AI features via AIControls policy`.
- Commit body: what changed and **why**, in plain language. Reference the spec or ADR.
- Commit early and often on the branch; the pull request is what gets reviewed.
- Push the branch and open a pull request with the template in `.github/`. The owner merges.
- Never force-push a shared branch. Never rewrite `main`.

## 5. Naming and layout

| Thing | Convention | Example |
| --- | --- | --- |
| Patch file | `patches/<series>/<NNNN>-<kebab-slug>.patch` | `patches/0200-debloat/0201-hide-sponsored-tiles.patch` |
| Patch ID | `CFX-<NNNN>`, number matches the series range | `CFX-0201` lives in `0200-debloat` |
| Our prefs | `chromefox.<feature>.<setting>` | `chromefox.compatTab.enabled` |
| Feature spec | `docs/features/<kebab-name>.md` | `docs/features/compat-tab.md` |
| ADR | `docs/adr/<NNNN>-<kebab-title>.md` | `docs/adr/0004-compat-tab-staged.md` |
| Devlog | `docs/devlog/YYYY-MM-DD-<topic>.md` | `docs/devlog/2026-10-19-project-bootstrap.md` |
| Branch | `<type>/<topic>` | `feat/ai-controls-policy` |

Series ranges: 0100 branding · 0200 debloat · 0300 no-ai · 0400 ublock · 0500 compat-tab ·
0600 performance. Add a new series only with an ADR.

Every behavior change we add must be switchable by a `chromefox.*` pref so it can be turned
off to tell "our bug" from "Firefox's bug".

## 6. Teaching the owner

The owner wants to understand and eventually architect this project. While working:

- Before a step, say in one or two plain sentences what you are about to do and why.
- After a step, say what changed and **how it connects** to the rest of the system
  (name the folder and the part of `docs/ARCHITECTURE.md` it belongs to).
- The first time a technical term appears in a session, define it in a short clause and add
  it to `docs/GLOSSARY.md` if it is not there.
- Never hide a failure or a shortcut. Explain trade-offs as choices the owner can make.
- When the owner asks "why", answer the real reason, including "because upstream does it".

## 7. When to stop and ask the owner

- A decision that is hard to reverse (public name, license, base version, signing, updates).
- Anything in rule 2.7 (security-sensitive areas).
- A patch would touch more than 5 upstream files or more than ~300 changed lines.
- Two documents disagree, or the spec does not cover what you are about to do.
- A check fails and the fix is not obvious.

## 8. Second-opinion agent

Gemini (large context) is the project's auditor, not a second author. It reads the whole repo
and writes findings to `docs/reviews/`. Agents act on those findings through normal tasks and
pull requests. See `docs/AI-TEAM.md`.
