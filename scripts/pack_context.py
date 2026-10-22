#!/usr/bin/env python3
"""Pack this repository into one Markdown file for a large-context reviewer (Gemini).

The output contains a header (date, git commit, file count, estimated tokens), a file tree,
and every text file in the repository with its path, in fenced code blocks.

Examples:
  python3 scripts/pack_context.py
  python3 scripts/pack_context.py --exclude docs/learn --exclude perf
  python3 scripts/pack_context.py --extra ../diffs/upstream-153.4-to-153.5.diff
  python3 scripts/pack_context.py --output .context/audit-2026-11-02.md

Token counts are estimates (characters / 4). Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

DEFAULT_SKIP_DIRS = {".git", "work", "engine", ".context", "node_modules", "__pycache__", ".venv", "raw"}
LANG_BY_SUFFIX = {
    ".md": "markdown", ".py": "python", ".json": "json", ".toml": "toml", ".yml": "yaml",
    ".yaml": "yaml", ".sh": "bash", ".patch": "diff", ".diff": "diff", ".js": "javascript",
    ".mjs": "javascript", ".css": "css", ".html": "html", ".xhtml": "html", ".ftl": "fluent",
    ".cfg": "javascript", ".txt": "text",
}


def git(root: Path, *args: str) -> str | None:
    try:
        out = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True)
        return out.stdout
    except (OSError, subprocess.CalledProcessError):
        return None


def candidate_files(root: Path) -> list[Path]:
    listed = git(root, "ls-files", "--cached", "--others", "--exclude-standard")
    if listed is not None:
        files = [root / line for line in listed.splitlines() if line.strip()]
    else:
        files = [p for p in root.rglob("*") if p.is_file()]
    result = []
    for path in files:
        rel_parts = path.relative_to(root).parts
        if any(part in DEFAULT_SKIP_DIRS for part in rel_parts[:-1]):
            continue
        if path.is_file():
            result.append(path)
    return sorted(set(result))


def read_text(path: Path, max_bytes: int) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if len(data) > max_bytes or b"\x00" in data[:8192]:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def fence_for(text: str) -> str:
    longest = max((len(m.group(0)) for m in re.finditer(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def tree(paths: list[str]) -> str:
    """Directory-grouped listing: each folder once, its files indented beneath it."""
    lines: list[str] = []
    shown_dirs: set[str] = set()
    for rel in paths:
        segments = rel.split("/")
        for depth in range(1, len(segments)):
            folder = "/".join(segments[:depth])
            if folder not in shown_dirs:
                shown_dirs.add(folder)
                lines.append("  " * (depth - 1) + segments[depth - 1] + "/")
        lines.append("  " * (len(segments) - 1) + segments[-1])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog="\n".join(__doc__.splitlines()[2:]))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path, default=None,
                        help="output file (default: .context/chromefox-context.md)")
    parser.add_argument("--exclude", action="append", default=[],
                        help="path prefix to leave out (repeatable), e.g. docs/learn")
    parser.add_argument("--extra", action="append", type=Path, default=[],
                        help="extra file from outside the repo to append (repeatable)")
    parser.add_argument("--max-file-bytes", type=int, default=300_000,
                        help="skip files larger than this (default 300000)")
    parser.add_argument("--warn-tokens", type=int, default=800_000,
                        help="warn when the estimate exceeds this (default 800000)")
    args = parser.parse_args()

    root = args.root.resolve()
    output = (args.output or (root / ".context" / "chromefox-context.md")).resolve()
    excludes = [e.strip("/").replace("\\", "/") for e in args.exclude]

    included: list[tuple[str, str]] = []
    skipped: list[str] = []
    for path in candidate_files(root):
        rel = path.relative_to(root).as_posix()
        if path == output or any(rel == e or rel.startswith(e + "/") for e in excludes):
            continue
        text = read_text(path, args.max_file_bytes)
        if text is None:
            skipped.append(rel)
            continue
        included.append((rel, text))

    for extra in args.extra:
        text = read_text(extra, args.max_file_bytes * 10)
        if text is None:
            print(f"pack_context: could not read extra file {extra}", file=sys.stderr)
            return 1
        included.append((f"EXTRA/{extra.name}", text))

    commit = (git(root, "rev-parse", "--short", "HEAD") or "uncommitted").strip()
    branch = (git(root, "rev-parse", "--abbrev-ref", "HEAD") or "n/a").strip()
    body_chars = sum(len(t) for _, t in included)
    est_tokens = body_chars // 4

    parts = [
        "# Chromefox repository context pack",
        "",
        f"- Generated: {dt.datetime.now().astimezone().isoformat(timespec='minutes')}",
        f"- Git: branch `{branch}`, commit `{commit}`",
        f"- Files included: {len(included)} (skipped binary/large: {len(skipped)})",
        f"- Estimated tokens: ~{est_tokens:,}",
        "",
        "Read GEMINI.md and AGENTS.md first; they define your role and the project rules.",
        "",
        "## File tree",
        "",
        "```text",
        tree([rel for rel, _ in included]),
        "```",
        "",
    ]
    for rel, text in included:
        fence = fence_for(text)
        lang = LANG_BY_SUFFIX.get(Path(rel).suffix.lower(), "")
        parts += [f"## {rel}", "", f"{fence}{lang}", text.rstrip("\n"), fence, ""]
    if skipped:
        parts += ["## Skipped files", ""] + [f"- {rel}" for rel in skipped] + [""]

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(parts), encoding="utf-8")

    print(f"pack_context: wrote {output} — {len(included)} files, ~{est_tokens:,} tokens")
    if est_tokens > args.warn_tokens:
        print(f"pack_context: WARNING estimate exceeds {args.warn_tokens:,} tokens; "
              "use --exclude to trim (Gemini 4 Argon's window is 1,048,576 tokens "
              "including its answer).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
