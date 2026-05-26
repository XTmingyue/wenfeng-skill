#!/usr/bin/env python3
"""Minimal validator for Codex skill folders."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ALLOWED_KEYS = {"name", "description"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> tuple[bool, dict[str, str] | str]:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return False, "Missing or invalid YAML frontmatter"

    raw = match.group(1).splitlines()
    data: dict[str, str] = {}
    i = 0
    while i < len(raw):
        line = raw[i]
        if not line.strip():
            i += 1
            continue
        if ":" not in line:
            return False, f"Invalid frontmatter line: {line}"
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key not in ALLOWED_KEYS:
            return False, f"Unexpected frontmatter key: {key}"
        if value == "|":
            block: list[str] = []
            i += 1
            while i < len(raw) and (raw[i].startswith("  ") or not raw[i].strip()):
                block.append(raw[i][2:] if raw[i].startswith("  ") else "")
                i += 1
            data[key] = "\n".join(block).strip()
            continue
        data[key] = value.strip("\"'")
        i += 1
    return True, data


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"SKILL.md not found: {skill_md}"]

    ok, parsed = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if not ok:
        return [str(parsed)]
    frontmatter = parsed

    name = frontmatter.get("name", "").strip()
    description = frontmatter.get("description", "").strip()
    if not name:
        errors.append("Missing frontmatter name")
    elif not NAME_RE.match(name):
        errors.append("Skill name must use lowercase letters, digits, and hyphens")

    if not description:
        errors.append("Missing frontmatter description")
    elif len(description) > 1024:
        errors.append("Description must be 1024 characters or fewer")

    missing = ALLOWED_KEYS - set(frontmatter)
    for key in sorted(missing):
        errors.append(f"Missing frontmatter key: {key}")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_skill.py <skill-dir>")
        return 2

    errors = validate(Path(sys.argv[1]).resolve())
    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1

    print("Skill is valid!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
