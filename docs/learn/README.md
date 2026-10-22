# Learning path for the owner

Goal: by the end, you can explain how every part of this project connects, judge proposals
from AI agents, and make architecture decisions with confidence. You do not need to learn to
program — you need to learn to **reason about systems**.

Each lesson takes about 30 minutes. Do one per week alongside the work; the work will make
more sense as you go, and vice versa.

| # | Lesson | You'll be able to… |
| --- | --- | --- |
| 01 | [How a browser works](01-how-a-browser-works.md) | Explain what happens between typing a URL and seeing a page |
| 02 | [Inside Firefox](02-inside-firefox.md) | Name Firefox's main parts and which ones we change |
| 03 | [How a fork works](03-how-a-fork-works.md) | Explain pinning, patching, rebasing, and why we chose ESR |
| 04 | [Git and GitHub for this project](04-git-and-github.md) | Read a pull request, understand branches, merge safely |
| 05 | [Working with Claude Code](05-working-with-claude-code.md) | Use skills, subagents and plan mode; know what hooks enforce |
| 06 | [Reading a patch](06-reading-a-patch.md) | Read a diff well enough to ask good questions |
| 07 | [Performance 101](07-performance-101.md) | Tell an honest benchmark from a misleading one |

## How to use these lessons with Claude

- After reading a lesson, ask Claude: `/explain <topic from the lesson> using our repo as the example`.
- Ask Claude to quiz you: "Give me five questions on lesson 03 and grade my answers."
- When a lesson and the real code disagree, that's a docs bug — ask Claude to fix one or the other.

## After the curriculum

Read the ADRs in order (`docs/adr/`). Each is a worked example of an architecture decision.
Then try writing one yourself for the next open question.
