#!/usr/bin/env python3
"""Stop hook: don't let a turn end while repository invariants are broken.

Runs scripts/check_registry.py and scripts/check_links.py. If either fails, returns
{"decision": "block", "reason": ...} so Claude keeps working and fixes the problem.
If the previous stop was already blocked by this hook (stop_hook_active), it lets the turn
end to avoid loops — Claude must then report the remaining problem to the owner.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

CHECKS = ["scripts/check_registry.py", "scripts/check_links.py"]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        payload = {}
    if payload.get("stop_hook_active"):
        return 0

    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".")
    failures = []
    for rel in CHECKS:
        script = root / rel
        if not script.is_file():
            continue
        try:
            # The checks print UTF-8 (see their main()); decode it as such on every OS.
            result = subprocess.run([sys.executable, str(script), "--root", str(root)],
                                    capture_output=True, encoding="utf-8", errors="replace",
                                    timeout=60)
        except (OSError, subprocess.TimeoutExpired) as exc:
            failures.append(f"{rel} could not run: {exc}")
            continue
        if result.returncode != 0:
            failures.append(result.stdout.strip() or result.stderr.strip())

    if failures:
        reason = ("Repository checks failed. Fix these before finishing, or explain to the "
                  "owner why they can't be fixed now:\n\n" + "\n\n".join(failures))
        print(json.dumps({"decision": "block", "reason": reason}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
