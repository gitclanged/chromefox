#!/usr/bin/env python3
"""SessionStart hook: print git state so every session (and every resume after compaction)
starts knowing where the work stands. Claude Code adds this hook's stdout to the context.

Never fails the session: any problem is reported as text and the hook exits 0.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def git(cwd: Path, *args: str) -> str | None:
    try:
        # Git prints UTF-8; without an explicit encoding, Windows Python decodes with the
        # legacy code page and crashes on some characters (e.g. in commit messages).
        out = subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                             encoding="utf-8", errors="replace", timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def main() -> int:
    # Captured output on Windows defaults to the legacy code page, which can't print every
    # character a commit message may contain; Claude Code reads hook output as UTF-8.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        payload = {}
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".")

    lines = ["## Repository state (from the session-start hook)"]
    if git(root, "rev-parse", "--is-inside-work-tree") != "true":
        lines.append("- Not a git repository yet. First task: docs/00-START-HERE.md section 2 (P0-01).")
        print("\n".join(lines))
        return 0

    branch = git(root, "rev-parse", "--abbrev-ref", "HEAD") or "(no commits yet)"
    lines.append(f"- Current branch: `{branch}`")
    if branch in ("main", "master"):
        lines.append("- You are on main. Create a task branch before editing (AGENTS.md rule 2.1).")

    status = git(root, "status", "--short") or ""
    changed = [l for l in status.splitlines() if l.strip()]
    if changed:
        lines.append(f"- Uncommitted changes ({len(changed)}):")
        lines += [f"    {l}" for l in changed[:20]]
        if len(changed) > 20:
            lines.append(f"    … and {len(changed) - 20} more")
    else:
        lines.append("- Working tree clean.")

    log = git(root, "log", "--oneline", "-5")
    if log:
        lines.append("- Recent commits:")
        lines += [f"    {l}" for l in log.splitlines()]

    lines.append("- Next: read docs/STATUS.md 'Next up' (already loaded via CLAUDE.md) "
                 "or run /start-session.")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
