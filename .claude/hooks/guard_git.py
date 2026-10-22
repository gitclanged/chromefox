#!/usr/bin/env python3
"""PreToolUse hook (Bash): block git commits and pushes that would land on main.

Blocks (exit code 2, reason on stderr, which Claude Code shows to Claude):
  * `git commit` while the current branch is main/master, unless the same command first
    creates a new branch, or the repository has no commits yet (the very first commit);
  * `git push` that targets main/master, or a bare `git push` while on main/master,
    except when main has exactly one commit (the initial push in P0-01);
  * force pushes without --force-with-lease (also denied in settings.json).

Anything else passes (exit 0). This is a safety net; GitHub branch protection is the
real enforcement.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

PROTECTED = {"main", "master"}


def git(cwd: Path, *args: str) -> str | None:
    try:
        # Git prints UTF-8; without an explicit encoding, Windows Python decodes with the
        # legacy code page and crashes on some branch names, which would let a push through.
        out = subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                             encoding="utf-8", errors="replace", timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def block(reason: str) -> int:
    print(f"Blocked by .claude/hooks/guard_git.py: {reason}", file=sys.stderr)
    return 2


def main() -> int:
    # Claude Code sends the payload as UTF-8 JSON. Decoded with the Windows legacy code page,
    # a non-English folder name in "cwd" is garbled, git can't run there, and the guard
    # would wrongly allow commits and pushes on main.
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    command = (payload.get("tool_input") or {}).get("command") or ""
    if "git" not in command:
        return 0
    cwd = Path(payload.get("cwd") or ".")

    creates_branch = re.search(r"git\s+(switch\s+(-c|--create)|checkout\s+-b)\s", command) is not None
    branch = git(cwd, "rev-parse", "--abbrev-ref", "HEAD")
    has_commits = git(cwd, "rev-parse", "--verify", "HEAD") is not None
    commit_count = int(git(cwd, "rev-list", "--count", "HEAD") or "0") if has_commits else 0
    on_protected = branch in PROTECTED

    if re.search(r"\bgit\s+(-c\s+\S+\s+)*commit\b", command):
        if on_protected and has_commits and not creates_branch:
            return block(f"you are on '{branch}'. Create a task branch first: "
                         "git switch -c <type>/<topic> (AGENTS.md rule 2.1).")

    for push in re.finditer(r"\bgit\s+push\b([^;&|]*)", command):
        args = push.group(1)
        if re.search(r"(^|\s)(--force|-f)(\s|$)", args) and "--force-with-lease" not in args:
            return block("force pushes are not allowed (AGENTS.md section 4).")
        targets_protected = re.search(r"(^|[\s:])(main|master)(\s|$)", args) is not None
        if on_protected and re.search(r"(^|[\s:])HEAD(\s|$)", args):
            targets_protected = True
        bare_push_on_protected = on_protected and not re.search(r"\s\S+\s+\S+", args)
        if (targets_protected or bare_push_on_protected) and commit_count > 1:
            return block("pushing to main is not allowed. Push your task branch and open a "
                         "pull request (docs/WORKFLOW.md).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
