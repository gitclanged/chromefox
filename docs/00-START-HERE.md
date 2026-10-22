# Start here (for the project owner)

You are the owner and architect of this project. Claude Code writes and runs the code;
Gemini audits it; you decide what gets built and approve what gets merged. This page tells
you how to do that without being a programmer.

## 1. What you have right now

A **starter repository**: the folder layout, the rules the AI agents follow, the plan, the
decision records, a learning curriculum, and a few small scripts that keep the repository
honest. There is no browser yet. The first phases of [ROADMAP.md](ROADMAP.md) build it.

Read in this order (about two hours total, spread over a few days is fine):

1. [FEASIBILITY.md](FEASIBILITY.md) — what is realistic, what is hard, what it costs.
2. [ARCHITECTURE.md](ARCHITECTURE.md) — the parts and how they connect.
3. [ROADMAP.md](ROADMAP.md) — the phases and their exit criteria.
4. [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) — decisions only you can make.
5. [learn/README.md](learn/README.md) — your curriculum, one lesson at a time.

## 2. One-time setup

You need: a computer you can leave building for hours (see
[runbooks/build-locally.md](runbooks/build-locally.md) for specs), a GitHub account,
Git, the GitHub CLI (`gh`), Python 3, and Claude Code. Install each from its official site
(Claude Code: https://code.claude.com/docs/en/quickstart · GitHub CLI: https://cli.github.com).
For Gemini, use whichever surface gives you Gemini 4 Argon (Gemini CLI, Google AI Studio or the
Gemini app) — see [AI-TEAM.md](AI-TEAM.md).

Then open a terminal in this folder, start Claude Code, and paste:

```text
This is a new project. Please:
1. Run `git init -b main`, add everything, and make the first commit
   ("chore: initial project scaffolding").
2. Create a public GitHub repository named chromefox with `gh repo create`
   and push main to it. (Public, because GitHub Free can't protect main on a
   private repository; see OPEN-QUESTIONS "Decided" #9.)
3. Walk me through turning on branch protection for main in the GitHub website
   (require a pull request and the "Repository consistency" and "Conventional PR title" checks to pass). Explain each setting.
4. Add an MPL-2.0 LICENSE file on a branch and open a pull request for it, so I can
   practice reviewing and merging.
Explain each step as you go.
```

Merging that first pull request yourself is the point: it is the loop you will repeat for
the whole project.

## 3. How a working session goes

Every session follows the same shape, so nothing depends on anyone's memory:

1. **Start:** type `/start-session`. Claude reads `STATUS.md`, the latest devlog and open
   pull requests, then tells you the next task and its plan in plain language.
2. **Agree:** say yes, change the plan, or pick a different task.
3. **Work:** Claude makes small commits on a branch and explains each step (the `Mentor`
   output style makes this automatic). Ask "why?" whenever you like.
4. **Review:** Claude runs the `reviewer` subagent, fixes what it finds, then opens a pull
   request.
5. **End:** type `/end-session`. Claude updates `STATUS.md`, writes a devlog entry for you,
   and pushes.
6. **You merge** — after reading the pull request summary and the "How verified" section.

If a session crashes or you switch computers, nothing is lost: the state lives in
`STATUS.md`, the devlog, the branch and the pull request, not in the chat.

## 4. How to review work when you cannot read code

You are not reviewing syntax. You are reviewing **decisions and evidence**. For each pull
request, check:

- **Does the summary match the task** in `STATUS.md`? Unasked-for extras are a red flag.
- **Is it small?** One purpose. If the summary has "and" in it, ask for a split.
- **Is there evidence?** "How verified" should list checks that ran and what they showed.
  "Should work" is not evidence.
- **Did the docs change with it?** New behavior with no doc change means drift is starting.
- **Did the reviewer subagent run,** and were its findings fixed or explained?
- **Is anything in a red zone?** Security, signing, updates, licensing — those need your
  explicit sign-off and often an ADR.

When unsure, ask Claude: "Explain this pull request as if I were going to defend it to a
skeptical engineer." Then ask Gemini the same question about the same diff and compare.

## 5. Your weekly rhythm (about 2 hours of your attention)

| When | What | Time |
| --- | --- | --- |
| Each session | `/start-session`, approve plan, review and merge PRs, `/end-session` | as available |
| Weekly | Gemini whole-repo audit (`/gemini-handoff audit`), read the report, turn findings into tasks | 30–45 min |
| Weekly | One lesson from `learn/` | 30 min |
| Each Firefox ESR update | Run the upstream update (`/upstream-update`), review, release | see runbook |
| Monthly | Re-read `ROADMAP.md`; are the phases still right? Update `OPEN-QUESTIONS.md` | 30 min |

## 6. Rules for yourself

- **Do not skip the process when you are excited.** The process is what keeps an AI-built
  project from turning into spaghetti.
- **Write decisions down.** If you decide something in chat, ask Claude to record it as an
  ADR or in `OPEN-QUESTIONS.md`. A decision that is only in a chat window will be lost.
- **Security updates beat features.** When Mozilla ships an ESR security release, everything
  else waits.
- **Kill features that don't earn their maintenance.** Every patch must be re-applied to
  every future Firefox release, forever.
