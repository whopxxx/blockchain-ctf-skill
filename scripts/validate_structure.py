#!/usr/bin/env python3
"""Validate stable structure and links for the blockchain CTF skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md",
    "AGENT.md",
    "README.md",
    "TEST_PLAN.md",
    "agents/openai.yaml",
    "references/methodology.md",
    "references/evm.md",
    "references/move.md",
    "references/solana.md",
    "references/cross-chain.md",
    "references/other-platforms-and-zk.md",
    "references/tooling.md",
    "references/vm-and-forensics.md",
    "references/verification-and-reporting.md",
    "benchmarks/README.md",
    "benchmarks/manifest.yaml",
    "tests/README.md",
    "tests/cases/manifest.yaml",
)
REFERENCE_LINKS = {path for path in REQUIRED if path.startswith("references/")}
MARKERS = re.compile(r"\b(?:TODO|TBD)\b|\[TODO:", re.IGNORECASE)
LOCAL_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md has no valid YAML frontmatter block")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def local_links(text: str) -> set[str]:
    links: set[str] = set()
    for raw in LOCAL_LINK.findall(text):
        target = raw.split("#", 1)[0].strip()
        if target and "://" not in target and not target.startswith(("#", "mailto:")):
            links.add(target.replace("\\", "/"))
    return links


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return errors

    skill = skill_path.read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(skill)
    except ValueError as exc:
        errors.append(str(exc))
        frontmatter = {}

    if frontmatter.get("name") != "blockchain-ctf":
        errors.append("SKILL.md name must be blockchain-ctf")
    if not frontmatter.get("description"):
        errors.append("SKILL.md description must be nonempty")

    links = local_links(skill)
    for target in links:
        resolved = (root / target).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            errors.append(f"local link escapes repository: {target}")
            continue
        if not resolved.is_file():
            errors.append(f"broken local link in SKILL.md: {target}")

    missing_routes = REFERENCE_LINKS - links
    for target in sorted(missing_routes):
        errors.append(f"reference is not routed from SKILL.md: {target}")

    shipped = [skill_path, *(root / path for path in REFERENCE_LINKS)]
    for path in shipped:
        if path.is_file() and MARKERS.search(path.read_text(encoding="utf-8")):
            errors.append(f"unfinished scaffold marker in {path.relative_to(root)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Skill structure is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
