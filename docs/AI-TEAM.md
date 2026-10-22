# The AI team: who does what

| Role | Who | Writes code? | Main job |
| --- | --- | --- | --- |
| Owner / architect | You | No | Decide what to build, answer open questions, approve and merge |
| Engineer | Claude Code | Yes — the only one | Plan, implement, verify, commit, open PRs, explain |
| In-session reviewer | Claude Code `reviewer` subagent | No | Fresh-context review of every diff before a PR |
| Auditor / historian | Gemini 4 Argon | No | Whole-repo audits, upstream impact reports, design second opinions |

**Why one writer:** two agents editing the same files produce conflicting styles and changes
nobody fully owns. Gemini's value here is *independence*: a different model, reading the
whole project at once, that did not write the code it is checking.

**Agreement is not proof.** If Claude and Gemini agree, that is encouraging, not evidence.
Evidence is a check that ran, a build that passed, a test, a measurement.

---

## Claude Code setup in this repo

| Piece | File(s) | What it does |
| --- | --- | --- |
| Project instructions | `CLAUDE.md` → imports `AGENTS.md` and `docs/STATUS.md` | Loaded every session; re-loaded after compaction |
| Teaching style | `.claude/output-styles/mentor.md` | Plain-language explanations of each step and how it connects |
| Path rules | `.claude/rules/*.md` | Extra rules that load only when touching `patches/`, `prefs/`, `compat-tab/` |
| Skills | `.claude/skills/*/SKILL.md` | Repeatable procedures: `/start-session`, `/end-session`, `/new-feature`, `/new-patch`, `/upstream-update`, `/explain`, `/gemini-handoff` |
| Subagents | `.claude/agents/*.md` | `reviewer`, `upstream-scout`, `perf-analyst`, `docs-keeper` |
| Hooks | `.claude/settings.json`, `.claude/hooks/*.py` | Show git state at session start; block commits/pushes on `main`; refuse to finish a turn with a broken registry or doc links |
| Permissions | `.claude/settings.json` | Deny force-pushes and reading secret files |

Hooks enforce; instructions guide. Anything that must *always* happen is a hook or a CI
check, not a sentence in a Markdown file.

---

## Gemini 4 Argon setup

**What it is:** Google's frontier model released September 30, 2026, with a 1,048,576-token
context window. It is available through the Gemini API (model ID `gemini-4-argon`), Google AI
Studio, Google Antigravity and the Gemini app on paid plans. Introductory API pricing is
$2 per million input tokens and $10 per million output tokens through November 30, 2026.

**What 1M tokens is good for here:** the *whole of this repository* — docs, patches, prefs,
scripts, reviews — fits easily for a long time. **Firefox itself does not** (it is many times
larger). Give Gemini our repo plus targeted slices of Firefox (the upstream files our patches
touch), never "all of Firefox".

**How to give it the project:**

```bash
python3 scripts/pack_context.py            # writes .context/chromefox-context.md
python3 scripts/pack_context.py --help     # options: exclude folders, add extra files
```

The packed file has a file tree, then every text file with its path. The script prints an
estimated token count and warns above 800k. Then either:

- **Gemini CLI**, if it offers the Argon model to you: run it in the repo root; it reads
  `GEMINI.md` (which imports `AGENTS.md` and `STATUS.md`) automatically. Point it at the
  packed file or let it read the folder.
- **AI Studio / Gemini app:** upload `.context/chromefox-context.md` and paste one of the
  prompts below.

Save the answer as `docs/reviews/YYYY-MM-DD-<topic>.md` (Claude can do this for you with
`/gemini-handoff save`). Then ask Claude to triage it: each finding becomes a task in
`STATUS.md`, an issue, or a written "won't fix, because…".

### Prompt 1 — weekly audit

```text
You are the independent auditor for the Chromefox project. The attached file contains the
whole repository. Follow GEMINI.md and AGENTS.md.

Produce a report with:
1. A five-sentence summary for a non-programmer owner: overall health, the biggest risk,
   and the one thing to fix first.
2. Findings, each with: severity (blocker / should-fix / consider), file path (and patch ID
   or line), what is wrong, evidence from the files, and the smallest fix.
   Check especially:
   - docs that disagree with patches, prefs or scripts (drift)
   - violations of AGENTS.md hard rules and QUALITY.md anti-spaghetti rules
   - patches whose registry "Why" is vague or whose size/risk looks understated
   - duplicated logic across patches or scripts
   - STATUS.md "Next up" that no longer matches ROADMAP.md
   - performance claims without data in perf/results/
3. A list of things you could NOT verify from the files provided.
Do not propose rewrites; propose minimal changes.
```

### Prompt 2 — upstream impact report (before each ESR update)

```text
Chromefox is moving from Firefox <OLD> to <NEW>. Attached: our repository (with
patches/REGISTRY.md), Mozilla's release notes / security advisories for <NEW>, and the
upstream diff between <OLD> and <NEW> for every file our patches touch.

For each of our patches: predict APPLIES CLEANLY / NEEDS REBASE / LIKELY OBSOLETE /
NEEDS REDESIGN, with the reason and the upstream change responsible. Then list any new
upstream feature that conflicts with our goals (new AI feature, new telemetry, new sponsored
content, new prefs replacing ones in prefs/). Finish with a recommended order of work.
Mark clearly what is prediction versus what you verified in the diff.
```

### Prompt 3 — design second opinion

```text
Attached: the Chromefox repository and a proposed <ADR / feature spec> at <path>.
Act as a skeptical senior browser engineer. List: (1) risks the proposal misses, especially
security, privacy and maintenance-across-Firefox-updates; (2) cases not covered; (3) a simpler
alternative if one exists; (4) questions the owner should answer before approving.
Keep it under 800 words, and write the first paragraph for a non-programmer.
```

### Cadence and cost

| Activity | When | Typical input size |
| --- | --- | --- |
| Weekly audit | Weekly, and before every release | Whole repo (small early on) |
| Upstream impact report | Each ESR update, before rebasing | Repo + diffs of touched files |
| Design second opinion | Each new ADR or large spec | Repo + the proposal |

Check the token estimate before sending. Prefer re-using a cached conversation when the
surface supports it; the repo changes slowly between audits.

---

## Failure modes to watch for

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Agent invents a Firefox pref, API or file path | Model memory instead of source | Require a Searchfox/source link for every upstream reference |
| Agent claims a check passed that didn't run | Over-confident summary | PR template forces "How verified"; owner asks "show me the output" |
| Docs drift from code | Docs not updated in same PR | Definition of done + weekly Gemini audit |
| Patches keep growing | Scope creep inside a task | Split; size limits in QUALITY.md |
| Same instructions repeated in chat every session | Missing rule or skill | Add it to AGENTS.md or a skill, not to memory |
| Long session gets confused | Context full | `/end-session`, start fresh; state is in files |
