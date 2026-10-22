# 2026-10-22 — Session 0: repository bootstrap and audit

**Task(s):** P0-01 (mostly done), owner request "ingenuity rule" · **Branch / PR:** #1–#6 ·
**Agent:** Claude Code (+ four `reviewer` subagent runs)

## What we did

We turned the starter kit into a real Git repository. It is on GitHub (public) with a
baseline commit and a first green CI run. We then tested every guardrail on your Windows
machine; the fixes went into separate pull requests:

- The ignore list missed several kinds of Firefox build output, including Firefox's source
  unpacked in the wrong folder (#1).
- The hooks and scripts crashed on non-English text. In the worst case the git guard
  silently let pushes to `main` through (#2).

You asked for a preference for ingenuity to be written down. It is now section 9 of
`AGENTS.md` (#3), and the first five compat-tab ideas are recorded for you to decide (#4).
We also added the MPL-2.0 license (#5) and built the first context pack for Gemini.

## Why

- **The baseline commit is the starter kit exactly as delivered.** Every change after it is
  a reviewable pull request, which is the habit the whole project depends on.
- **Your commits use GitHub's private "noreply" address,** so your email never appears in a
  public history. This is set only in this folder's Git settings. On another computer, set
  it again with `git config user.email 105825431+gitclanged@users.noreply.github.com`.
- **The repository is public** because GitHub Free can't protect `main` on a private
  repository. You chose that over paying for GitHub Pro or going without protection.

## How it connects

Almost everything this session is the development system (`docs/ARCHITECTURE.md` §3):

- Git and GitHub: where the work lives;
- the hooks and checks: the guardrails;
- the Gemini pack: the auditor's input.

The ignore list and line-ending rules protect the build pipeline (§1). They keep Firefox's
source out of the repository, and keep future patch files exactly as written.

**Hook changes (required note, `.claude/hooks/README.md`):** in #2, `guard_git.py`,
`session_start.py` and `stop_check.py` now read and write UTF-8. Merging #2 is your
approval of those changes.

## Verified

- **The checks catch real problems.** `check_registry.py` and `check_links.py` pass in Git
  Bash and PowerShell, and caught all eight errors planted in a deliberately broken copy.
- **The guard works live.** It blocked a real `git commit` on `main` inside Claude Code.
  The 8-case simulated test passes.
- **Every Windows text failure was reproduced, then fixed.** Each was shown to fail before
  the fix and pass after it.
- **CI passed on GitHub** for `main`.
- **Independent review.** Each pull request was reviewed by a `reviewer` subagent, and its
  findings were fixed or answered in the pull request.
- **Not verified:**
  - whether Claude Code sends hook input as raw UTF-8 (the fix handles both forms);
  - anything inside a real browser (no build exists; `policies.json` is untested);
  - every Firefox, Edge and WebView2 fact behind the compat-tab ideas.

## New terms

Repository terms: Git ignore list, Tarball, Line endings (LF / CRLF), Character encoding,
Exit code, PATH, Stacked pull request. Compat-tab terms: App mode, declarativeNetRequest
(DNR). All are in `docs/GLOSSARY.md`; some arrive with #1–#4.

## Next

1. You turn on branch protection for `main`. Ask Claude for the walkthrough.
2. You review and merge #1–#6; merge #2 and #6 together.
3. Claude then updates #4 to sit on `main` instead of #3.
4. Then P0-02 (your answers to `OPEN-QUESTIONS.md` rows 1–3 and 10) and P0-03 (testing the
   policies on stock Firefox ESR 153).

## Questions for the owner

- OPEN-QUESTIONS rows 1–3 and 10, and the proposals IDEA-01 – IDEA-05.
- Gemini's role: the docs call it the "auditor"; you call it your co-project manager.
  Should `docs/AI-TEAM.md` change?
