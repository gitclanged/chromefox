# Lesson 04 — Git and GitHub for this project

## The four ideas you need

1. **Commit** — a saved snapshot of changes with a message. Our history is a list of
   commits. Good commits are small and say *why*.
2. **Branch** — a separate line of commits. `main` is the official version. Each task gets
   its own branch (`feat/ai-controls-policy`), so unfinished work never touches `main`.
3. **Pull request (PR)** — a request to merge a branch into `main`. It shows every change,
   runs automatic checks, and is where review happens.
4. **Merge** — accepting a PR. We use **squash and merge**: the PR's commits become one
   commit on `main`, with the PR title as its message.

## The loop you'll repeat

```text
STATUS.md says next task → Claude creates a branch → small commits → pushes
→ opens PR → checks run → reviewer findings fixed → you read and merge → branch deleted
```

## Reading a pull request (what to look at, in order)

1. **Title** — `type(scope): summary`. Does it match the task?
2. **Description** — what, why, how verified, risk. Written for you.
3. **Checks** — green tick or red cross at the bottom. Red means don't merge.
4. **Files changed** — the list of files is more useful to you than the code: are they in
   the folders you'd expect for this task? Is `docs/` among them?
5. **Conversation** — reviewer findings and responses.

## Protecting `main`

Branch protection (set once, see `docs/00-START-HERE.md`) means nobody — not Claude, not
you by accident — can push directly to `main` or merge a PR with failing checks. Claude Code
also has a hook that blocks commits on `main` locally. Two layers, because mistakes happen.

## Tags and releases

A **tag** marks one commit permanently, e.g. `v153.4.0-cfx.1`. A GitHub **release** attaches
installers and notes to a tag. Released versions are always tags on `main`.

## When things go wrong

- **"Merge conflict"** — two branches changed the same lines. Ask Claude to resolve it and
  explain what it chose.
- **A merged change broke something** — ask Claude to `git revert` the merge commit on a new
  branch and open a PR. Reverting is safe and keeps history; never rewrite `main`.
- **Lost track of what's happening** — `/start-session`. The state is in the files.

## Check your understanding

1. Why does each task get its own branch?
2. A PR has a red cross. What do you do?
3. Why squash-merge rather than merging every small commit?
4. Something on `main` is broken. Why revert instead of deleting the commit?
