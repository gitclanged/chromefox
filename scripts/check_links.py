#!/usr/bin/env python3
"""Check that relative links in Markdown files point to files that exist.

Checks:
  * [text](relative/path) and ![alt](relative/path) links in every .md file;
  * @path imports at the start of lines in AGENTS.md, CLAUDE.md and GEMINI.md.
Skips external links (http, https, mailto), pure #anchors, placeholders containing < or >,
and anything inside fenced code blocks or inline code. Anchors are not validated.

Exit code 0 when every link resolves, 1 otherwise. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

SKIP_DIRS = {".git", "work", "engine", ".context", "node_modules", "__pycache__", ".venv"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*([^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
IMPORT_FILES = {"AGENTS.md", "CLAUDE.md", "GEMINI.md"}
IMPORT_RE = re.compile(r"^@(\S+)\s*$")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
INLINE_CODE_RE = re.compile(r"(`+)(?:(?!\1).)+?\1")


def markdown_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def visible_lines(text: str):
    """Yield (line_number, line) for lines outside fenced code blocks, inline code removed."""
    fence: str | None = None
    for lineno, line in enumerate(text.splitlines(), start=1):
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(1)
            if fence is None:
                fence = marker[0] * len(marker)
                continue
            if marker.startswith(fence):
                fence = None
                continue
        if fence is not None:
            continue
        yield lineno, INLINE_CODE_RE.sub("", line)


def is_skipped(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith(("http://", "https://", "mailto:", "tel:", "#"))
        or "<" in target
        or ">" in target
        or "{" in target
    )


def resolve(base_dir: Path, target: str, root: Path) -> Path:
    target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if target.startswith("/"):
        return root / target.lstrip("/")
    return base_dir / target


def check(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    checked = 0
    for md in markdown_files(root):
        text = md.read_text(encoding="utf-8", errors="replace")
        rel = md.relative_to(root).as_posix()
        for lineno, line in visible_lines(text):
            for target in LINK_RE.findall(line):
                if is_skipped(target):
                    continue
                checked += 1
                if not resolve(md.parent, target, root).exists():
                    errors.append(f"{rel}:{lineno}: broken link -> {target}")
            if md.name in IMPORT_FILES and md.parent == root:
                m = IMPORT_RE.match(line.strip())
                if m:
                    checked += 1
                    if not resolve(md.parent, m.group(1), root).exists():
                        errors.append(f"{rel}:{lineno}: broken @import -> {m.group(1)}")
    return errors, checked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="repository root (default: parent of scripts/)")
    args = parser.parse_args()
    errors, checked = check(args.root.resolve())
    if errors:
        print(f"check_links: {len(errors)} broken link(s):")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(f"check_links: OK ({checked} relative link(s) checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
