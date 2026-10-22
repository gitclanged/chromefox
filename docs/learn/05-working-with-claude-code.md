# Lesson 05 — Working with Claude Code

## What Claude Code reads automatically

- `CLAUDE.md` → which imports `AGENTS.md` (the rules) and `docs/STATUS.md` (where we are).
- `.claude/rules/*.md` — extra rules that load only when it touches certain folders.
- `.claude/output-styles/mentor.md` — tells it to explain its work to you as it goes.

Everything else it reads on demand. That's why the important state is in a few small files.

## Tools you'll use

| Tool | How you use it | What it's for |
| --- | --- | --- |
| **Skills** | Type `/start-session`, `/end-session`, `/new-feature compat-tab`, `/explain rebasing` | Repeatable procedures, done the same way every time |
| **Plan mode** | Ask "plan this first" or switch modes in the app | Claude researches and proposes before editing anything |
| **Subagents** | Claude uses them; you can ask "have the reviewer check this" | A fresh helper for a focused job, e.g. reviewing without bias |
| **Hooks** | Automatic | Rules that are enforced, not just requested |

## Hooks in this project (what they do for you)

| Hook | When | Effect |
| --- | --- | --- |
| Session start | Every new or resumed session | Shows the branch, uncommitted changes and recent commits |
| Git guard | Before shell commands | Blocks committing or pushing on `main` |
| Stop check | Whenever Claude tries to finish a turn | Refuses to finish while the patch registry or doc links are broken |

Instructions in Markdown are *requests*; hooks are *guarantees*. When a rule really matters,
it should become a hook or a CI check.

## Prompts that work well

- "Start a session." → `/start-session`
- "Before changing anything, explain the options and trade-offs, then recommend one."
- "Show me the evidence that this works." (Ask for the actual output, not a summary.)
- "What would break if Mozilla changed X in the next ESR?"
- "Write this decision down as an ADR."
- "That explanation used terms I don't know. Explain again with an analogy."

## Prompts that cause trouble

- "Just make it work." (Invites shortcuts and hidden breakage.)
- "Do all of Phase 2." (Too big; ask for the next task only.)
- "Don't worry about the docs this time." (That's how drift starts.)

## Context limits

Each session has limited working memory. Long sessions get summarized ("compacted"), and
details can be lost. Good habits: one task per session, `/end-session` when done, start fresh.
Nothing important should exist only in the chat.

## Check your understanding

1. Where does Claude learn the project rules at the start of a session?
2. What's the difference between a rule in `AGENTS.md` and a hook?
3. Why use a reviewer subagent instead of asking the same session to review its own work?
4. A session has been running for hours and seems confused. What do you do?
