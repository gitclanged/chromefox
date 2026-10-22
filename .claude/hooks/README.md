# Claude Code hooks

Registered in `.claude/settings.json`. Hooks are **guarantees**: Claude Code runs them at
fixed moments regardless of what the model decides.

| Hook | Event | What it does |
| --- | --- | --- |
| `session_start.py` | SessionStart (start, resume, clear, compact) | Prints branch, uncommitted changes and recent commits into Claude's context |
| `guard_git.py` | PreToolUse on Bash | Blocks commits on `main`, pushes to `main` and force pushes (exit code 2) |
| `stop_check.py` | Stop | Refuses to end a turn while `check_registry.py` or `check_links.py` fail |

## Requirements

Python 3 available as `python3`. On Windows, if hooks report "python3 not found", ask Claude
to change the commands in `.claude/settings.json` to the Python launcher on your machine
(often `py -3` or `python`) — and record that in your personal `.claude/settings.local.json`
instead if teammates use other systems.

## Testing a hook by hand

```bash
echo '{"tool_input":{"command":"git commit -m test"},"cwd":"."}' | python3 .claude/hooks/guard_git.py; echo "exit=$?"
echo '{"stop_hook_active":false,"cwd":"."}' | python3 .claude/hooks/stop_check.py
```

Run `/hooks` inside Claude Code to see the registered hooks.

## Changing hooks

Hooks change how every session behaves, so changes need owner approval in a pull request
and a note in the devlog.
