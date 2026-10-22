#!/usr/bin/env python3
"""Check that patches/ and patches/REGISTRY.md agree.

Rules enforced (see patches/REGISTRY.md and AGENTS.md):
  * every .patch file under patches/ has exactly one registry row, and vice versa;
  * IDs look like CFX-NNNN, are unique, match the file name and fall in the series range;
  * the Feature column names an existing docs/features/<feature>.md spec;
  * Layer and Risk use the allowed values;
  * Why is a real reason, and engine patches cite an ADR.

Exit code 0 when everything is consistent, 1 otherwise. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ALLOWED_LAYERS = {"frontend", "engine", "build", "branding", "pref-default"}
ALLOWED_RISKS = {"low", "medium", "high"}
VAGUE_WHY = {"needed", "need", "fix", "fixes", "improvement", "tweak", "cleanup", "todo", "tbd"}
ID_RE = re.compile(r"^CFX-(\d{4})$")
SERIES_RE = re.compile(r"^(\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*$")
FILE_RE = re.compile(r"^(\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*\.patch$")
EXPECTED_COLUMNS = ["id", "file", "feature", "layer", "upstream files", "risk", "last rebased", "why"]


def strip_html_comments(text: str) -> str:
    # Replace each comment with the same number of newlines so line numbers stay correct.
    return re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.DOTALL)


def clean_cell(cell: str) -> str:
    cell = cell.strip()
    if len(cell) >= 2 and cell.startswith("`") and cell.endswith("`"):
        cell = cell[1:-1].strip()
    return cell


def split_row(line: str) -> list[str]:
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [clean_cell(c) for c in inner.split("|")]


def parse_registry(path: Path, errors: list[str]) -> list[dict]:
    if not path.is_file():
        errors.append(f"{path}: registry file is missing")
        return []
    text = strip_html_comments(path.read_text(encoding="utf-8"))
    rows: list[dict] = []
    header_ok = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        if not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        lowered = [c.lower() for c in cells]
        if lowered and lowered[0] == "id":
            if lowered != EXPECTED_COLUMNS:
                errors.append(
                    f"{path}:{lineno}: table header should be: | "
                    + " | ".join(c.title() if c != "id" else "ID" for c in EXPECTED_COLUMNS)
                    + " |"
                )
            else:
                header_ok = True
            continue
        if set("".join(cells)) <= set("-: "):
            continue  # separator row
        if len(cells) != len(EXPECTED_COLUMNS):
            errors.append(f"{path}:{lineno}: expected {len(EXPECTED_COLUMNS)} columns, found {len(cells)}")
            continue
        rows.append(dict(zip(EXPECTED_COLUMNS, cells), lineno=lineno))
    if not header_ok:
        errors.append(f"{path}: could not find the registry table header")
    return rows


def check(root: Path) -> list[str]:
    errors: list[str] = []
    patches_dir = root / "patches"
    registry_path = patches_dir / "REGISTRY.md"
    features_dir = root / "docs" / "features"

    rows = parse_registry(registry_path, errors)

    # Series folders
    if patches_dir.is_dir():
        for child in sorted(patches_dir.iterdir()):
            if child.is_dir() and not SERIES_RE.match(child.name):
                errors.append(f"{child.relative_to(root)}: series folder must look like NNNN-kebab-name")

    patch_files = sorted(p for p in patches_dir.rglob("*.patch")) if patches_dir.is_dir() else []
    on_disk = {p.relative_to(root).as_posix() for p in patch_files}

    seen_ids: dict[str, int] = {}
    seen_files: dict[str, int] = {}
    for row in rows:
        where = f"{registry_path.relative_to(root)}:{row['lineno']}"
        rid, rfile = row["id"], row["file"]

        m = ID_RE.match(rid)
        if not m:
            errors.append(f"{where}: ID '{rid}' must look like CFX-NNNN")
            continue
        number = int(m.group(1))
        if rid in seen_ids:
            errors.append(f"{where}: duplicate ID {rid} (also on line {seen_ids[rid]})")
        seen_ids[rid] = row["lineno"]

        if rfile in seen_files:
            errors.append(f"{where}: file {rfile} is listed twice (also on line {seen_files[rfile]})")
        seen_files[rfile] = row["lineno"]

        parts = Path(rfile).parts
        if len(parts) != 3 or parts[0] != "patches":
            errors.append(f"{where}: file must be patches/<series>/<NNNN>-<slug>.patch, got '{rfile}'")
        else:
            series, filename = parts[1], parts[2]
            sm, fm = SERIES_RE.match(series), FILE_RE.match(filename)
            if not sm:
                errors.append(f"{where}: series folder '{series}' must look like NNNN-kebab-name")
            if not fm:
                errors.append(f"{where}: file name '{filename}' must look like NNNN-kebab-slug.patch")
            if fm and int(fm.group(1)) != number:
                errors.append(f"{where}: file number {fm.group(1)} does not match {rid}")
            if sm:
                base = int(sm.group(1))
                if not (base <= number <= base + 99):
                    errors.append(f"{where}: {rid} is outside series {series} (allowed {base:04d}-{base + 99:04d})")
        if rfile not in on_disk:
            errors.append(f"{where}: {rfile} does not exist")

        feature = row["feature"]
        if not feature or not (features_dir / f"{feature}.md").is_file():
            errors.append(f"{where}: feature '{feature}' has no spec at docs/features/{feature}.md")

        if row["layer"] not in ALLOWED_LAYERS:
            errors.append(f"{where}: layer '{row['layer']}' must be one of {sorted(ALLOWED_LAYERS)}")
        if row["risk"] not in ALLOWED_RISKS:
            errors.append(f"{where}: risk '{row['risk']}' must be one of {sorted(ALLOWED_RISKS)}")
        if not row["upstream files"]:
            errors.append(f"{where}: list the upstream files this patch touches")

        why = row["why"].strip()
        if len(why) < 20 or why.lower().rstrip(".") in VAGUE_WHY:
            errors.append(f"{where}: 'Why' is too vague; explain the reason and why a policy/pref/extension was not enough")
        if row["layer"] == "engine" and not re.search(r"ADR-\d{4}", why):
            errors.append(f"{where}: engine patches must cite an ADR (ADR-NNNN) in 'Why'")

    for path in sorted(on_disk - set(seen_files)):
        errors.append(f"{path}: patch file has no row in patches/REGISTRY.md")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="repository root (default: parent of scripts/)")
    args = parser.parse_args()
    root = args.root.resolve()

    errors = check(root)
    patch_count = len(list((root / "patches").rglob("*.patch"))) if (root / "patches").is_dir() else 0
    if errors:
        print(f"check_registry: {len(errors)} problem(s) found:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(f"check_registry: OK ({patch_count} patch file(s), registry consistent)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
